"""
# data_import_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.data_import.data_import_widgets as diw
import dfcleanser.data_import.data_import_model as dim

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (get_function_parms, INT_PARM, 
                                            STRING_PARM, displayParms, display_exception,
                                            opStatus, RunningClock, get_string_value,
                                            display_notes)

from dfcleanser.common.db_utils import (get_stored_con_Parms, set_dbcon_dict)

from IPython.display import clear_output

from dfcleanser.scripting.data_scripting_control import add_to_script


import pandas as pd
import json
import time

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Data Import functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   pass through to display widgets
#--------------------------------------------------------------------------
"""
def display_import_forms(id, detid=0, notes=False) :
    from dfcleanser.data_import.data_import_widgets import display_dc_import_forms
    display_dc_import_forms(id, detid, notes)


def display_sql_details_form(sqlimportid,dblibid) :
    from dfcleanser.data_import.data_import_widgets import display_dc_sql_details_forms
    display_dc_sql_details_forms(sqlimportid,dblibid)

def get_tables(importparms) :
    
    from dfcleanser.common.db_utils import get_db_connector_idList
    dbid        =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    cplist      =   get_db_connector_idList(dbid)
    cparms      =   get_stored_con_Parms(dbid)
    conparms    =   [cplist,cparms]
    
    diw.display_pandas_import_sql_inputs(dim.SQLTABLE_IMPORT,dim.TABLE_NAMES,dbid,conparms,importparms)

def get_columns(importparms) :

    from dfcleanser.common.db_utils import get_db_connector_idList
    dbid        =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    cplist      =   get_db_connector_idList(dbid)
    cparms      =   get_stored_con_Parms(dbid)
    conparms    =   [cplist,cparms]
    
    diw,display_pandas_import_sql_inputs(dim.SQLTABLE_IMPORT,dim.COLUMN_NAMES,dbid,conparms,importparms)

def get_datetimeformats(importparms) :
    cfg.set_config_value(diw.pandas_import_sqltable_common_id+"Parms",importparms)
    diw.display_pandas_import_sql_inputs(dim.SQLTABLE_IMPORT,dim.DATETIME_FORMATS,None,None,importparms)

def display_pandas_import_sql_inputs(importtype,formtype,DBid,dbconparms,importparms=None) :
    diw.display_dc_pandas_import_sql_inputs(importtype,formtype,DBid,dbconparms,importparms=None)


    
"""
#--------------------------------------------------------------------------
#   process pandas import functions
#--------------------------------------------------------------------------
"""
def process_import_form(formid, parms, display=True) :
    
    if( (formid == dim.CSV_IMPORT)  or (formid == dim.EXCEL_IMPORT) or 
        (formid == dim.JSON_IMPORT) or (formid == dim.HTML_IMPORT) or 
        (formid == dim.FWF_IMPORT)  or (formid == dim.CUSTOM_IMPORT) )  :
    
        s       =   time.time()
        opstat  =   opStatus()
        cfg.drop_dc_dataframe()  
    
        if(display) :
            clear_output()
            diw.display_import_main_taskbar()
            clock = RunningClock()
            clock.start()
    
        if (formid == dim.CSV_IMPORT) :
            fparms      =   diw.get_csv_import_inputs(parms)
            opstat      =   import_pandas_csv(fparms,
                                              diw.get_csv_import_form_id(),
                                              diw.get_csv_import_form_labels())
            
            parmstitle  =   "Pandas CSV Import Parms"
            parmslist   =   diw.get_csv_import_form_labels()[:5]
        
        if (formid == dim.FWF_IMPORT) :
            fparms      =   diw.get_fwf_import_inputs(parms)
            opstat      =   import_pandas_fwf(fparms,
                                              diw.get_fwf_import_form_id(),
                                              diw.get_fwf_import_form_labels())
            
            parmstitle  =   "Pandas FWF Import Parms"
            parmslist   =   diw.get_fwf_import_form_labels()[:5]
        
        elif (formid == dim.EXCEL_IMPORT) :
            fparms      =   diw.get_excel_import_inputs(parms)
            opstat      =   import_pandas_excel(fparms,
                                                diw.get_excel_import_form_id(),
                                                diw.get_excel_import_form_labels())
            
            parmstitle  =   "Pandas Excel Import Parms"
            parmslist   =   diw.get_excel_import_form_labels()[:6]
        
        elif (formid == dim.JSON_IMPORT) : 
            fparms      =   diw.get_json_import_inputs(parms)
            opstat      =   import_pandas_json(fparms,
                                               diw.get_json_import_form_id(),
                                               diw.get_json_import_form_labels())
            
            parmstitle  =   "Pandas JSON Import Parms"
            parmslist   =   diw.get_json_import_form_labels()[:2]
        
        elif (formid == dim.HTML_IMPORT) : 
            fparms      =   diw.get_html_import_inputs(parms)
            opstat      =   import_pandas_html(fparms,
                                               diw.get_html_import_form_id(),
                                               diw.get_html_import_form_labels())
            
            parmstitle  =   "Pandas HTML Import Parms"
            parmslist   =   diw.get_html_import_form_labels()[:4]

        elif (formid == dim.CUSTOM_IMPORT) : 
            (dispstats, opstat)     =   import_custom(parms)
            
            if(dispstats) :
                parmstitle  =   "Custom Import Parms"
                parmslist   =   diw.get_custom_import_form_labels()[0]

           
        if(opstat.get_status()) : 
            if(display) :
                if (formid == dim.CUSTOM_IMPORT) :
                    if(dispstats) : 
                        ciparms = parms[0].replace("\n","</br>")
                        displayParms(parmstitle,parmslist,[ciparms],cfg.DataImport_ID)
                        diw.display_data_import_notes(s,parms[0])
                else :
                    displayParms(parmstitle,parmslist,fparms,cfg.DataImport_ID)
                    diw.display_data_import_notes(s,fparms[0])
                    
        else :
            display_exception(opstat)

        if(display) :
            clock.stop()
        
    elif (formid == dim.SQLTABLE_IMPORT) : 
        import_sql_table(parms)
        
    elif (formid == dim.SQLQUERY_IMPORT) :
        import_sql_query(parms)
        
    else :
        print("Invalid formid "+ str(formid))
        return



"""
#------------------------------------------------------------------
#   import a sql table into pandas dataframe - javascript helper
#
#    parms       -   html input form parms 
#
#------------------------------------------------------------------
"""   
def import_sql_table(parms) :
    
    opstat  =   opStatus()
    
    diw.display_import_main_taskbar() 
    
    s = time.time()
    clock = RunningClock()
    clock.start()
    
    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    dbcondict = set_dbcon_dict(dbid,get_stored_con_Parms(dbid))

    from dfcleanser.common.db_utils import Custom
    if(dbid == Custom) :
        sqltableparms   =   diw.get_sqltable_import_inputs(parms,dim.SQL_CUSTOM)
        importid        =   diw.get_sqltable_import_form_id(dim.SQL_CUSTOM)
    else :
        sqltableparms   =   diw.get_sqltable_import_inputs(parms,dim.SQL_COMMON)
        importid        =   diw.get_sqltable_import_form_id(dim.SQL_COMMON)
        
    (import_notes, opstat) = import_pandas_sqltable(sqltableparms, dbcondict, importid)

    if(opstat.get_status()) : 
        
        for i in range(len(sqltableparms)) :
            sqltableparms[i]  =  get_string_value(sqltableparms[i]) 
        
        if(dbid == Custom) :
            displayParms("Pandas SQL Table Import Parms",
                         diw.get_sqltable_import_form_labels(dim.SQL_CUSTOM)[0:7],
                         sqltableparms[0:7],cfg.DataImport_ID)
        else :
            displayParms("Pandas SQL Table Import Parms",
                         diw.get_sqltable_import_form_labels(dim.SQL_COMMON)[0:7],
                         sqltableparms[0:7],cfg.DataImport_ID)
        
        display_notes(["DB Connector String : ",
                       "&nbsp;&nbsp;" + import_notes])
        
        diw.display_data_import_notes(s,sqltableparms[0],True)
        
    else :
        display_exception(opstat)

    
"""
#------------------------------------------------------------------
#   import a sql table into pandas dataframe - javascript helper
#
##   parms       -   html input form parms 
#
#------------------------------------------------------------------
"""   
def import_sql_query(parms) :
    
    opstat  =   opStatus()
    
    diw.display_import_main_taskbar() 
    
    s = time.time()
    clock = RunningClock()
    clock.start()
    
    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    dbcondict = set_dbcon_dict(dbid,get_stored_con_Parms(dbid))

    sqlqueryparms = diw.get_sqlquery_import_inputs(parms)
    
    (import_notes, opstat) = import_pandas_sqlquery(sqlqueryparms, dbcondict, diw.get_sqlquery_import_form_id())
    
    if(opstat.get_status()) : 
        
        for i in range(len(sqlqueryparms)) :
            sqlqueryparms[i]  =  get_string_value(sqlqueryparms[i]) 
            
        displayParms("Pandas SQL Query Import Parms",
                     diw.get_sqlquery_import_form_labels()[0:6],
                     sqlqueryparms[0:6],cfg.DataImport_ID)
        
        display_notes(["DB Connector String : ",
                       "&nbsp;&nbsp;" + import_notes])
        
        diw.display_data_import_notes(s,sqlqueryparms[0],True)
        
    else :
        display_exception(opstat)


"""
#------------------------------------------------------------------
#   import from custom into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def import_custom(parms) :

    functionid = parms[0]
    
    opstat      =   opStatus()
    dispstats   =   False
    
    if(functionid == dim.PROCESS_CUSTOM_IMPORT) :
        opstat      =   process_custom_import(parms[1],diw.get_custom_import_form_id(),display=True) 
        dispstats   =   True
        
    elif(functionid == dim.STORE_CUSTOM_IMPORT) :
        codetext = diw.get_custom_import_inputs(parms)
        custom_code = "# custom import\n"
        custom_code = custom_code + codetext[0]
        #custom_code = custom_code.replace("\n","</br>")
        cfg.set_config_value(diw.get_custom_import_form_id() + "Parms",custom_code)
        display_import_forms(dim.IMPORT_CUSTOM_ONLY)
        
    elif(functionid == dim.DROP_CUSTOM_IMPORT) :
        cfg.drop_config_value(diw.get_custom_import_form_id() + "Parms")
        display_import_forms(dim.IMPORT_CUSTOM_ONLY)

    return(dispstats, opstat)
    
"""
#--------------------------------------------------------------------------
#   process pandas import functions
#--------------------------------------------------------------------------
"""

"""
#------------------------------------------------------------------
#   import csv file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def import_pandas_csv(fparms,importId,labellist,display=True) : 
    
    opstat          =   opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        try :

            csvkeys         =   [labellist[1],labellist[2],labellist[3]] 
            csvvals         =   [fparms[1],fparms[2],fparms[3]]
            csvtypes        =   [INT_PARM,STRING_PARM,INT_PARM]
    
            csvparms        =   {}
            csvaddlparms    =   {}
            
        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)

    
    if(len(fparms[2]) > 0) :
        try :
            with open(fparms[2], 'r') as col_names_file :
                colNames = json.load(col_names_file)
                csvvals[1] = colNames
        except Exception as e: 
            opstat.store_exception("Unable to open csv column names file" + fparms[2],e)
    
    if(opstat.get_status()) :
        
        try :
            
            csvparms        =   get_function_parms(csvkeys,csvvals,csvtypes)
            if(not (fparms[4] == "")) :
                csvaddlparms    =   json.loads(fparms[4])
            
            if (len(csvaddlparms) > 0) :
                addlparmskeys = csvaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    csvparms.update({addlparmskeys[i]:csvaddlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :
    
        try :
            df = pd.read_csv(fparms[0], **csvparms)
        except Exception as e:
            opstat.store_exception("Unable to import csv file" + fparms[0],e)

    if(opstat.get_status()) : 
        
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            script      =   ["# Import CSV File ",
                             "from dfcleanser.data_import.data_import_controller import import_pandas_csv",
                             "import_pandas_csv(" + json.dumps(fparms) + "," +
                             str(importId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[0])
        
    return(opstat)
    
"""
#------------------------------------------------------------------
#   import fixed width file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def import_pandas_fwf(fparms,importId,labellist,display=True) : 
    
    opstat = opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        try :

            fwfkeys         =   [labellist[1],labellist[2],labellist[3],labellist[4],labellist[5]] 
            fwfvals         =   [fparms[1],fparms[2],fparms[3],fparms[4],fparms[5]]
            fwftypes        =   [STRING_PARM,INT_PARM,STRING_PARM,INT_PARM,STRING_PARM]
    
            fwfparms        =   {}
            fwfaddlparms    =   {}
            
        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)

    if(opstat.get_status()) :
    
        if(len(fparms[3]) > 0) :
        
            try :
                with open(fparms[3], 'r') as col_names_file :
                    colNames = json.load(col_names_file)
                    fwfvals[2] = colNames
            except Exception as e: 
                opstat.store_exception("Unable to open fwf column names file" + fparms[3],e)

    if(opstat.get_status()) :
        
        try :
            
            fwfparms        =   get_function_parms(fwfkeys,fwfvals,fwftypes)
            
            if(not (fparms[6] == "")) :
                fwfaddlparms    =   json.loads(fparms[6])
            
            if (len(fwfaddlparms) > 0) :
                addlparmskeys = fwfaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    fwfparms.update({addlparmskeys[i]:fwfaddlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)
    
        
    if(opstat.get_status()) :
    
        try :
            df = pd.read_fwf(fparms[0], **fwfparms)
        except Exception as e:
            opstat.store_exception("Unable to import fwf file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            script      =   ["# Import FWF File ",
                             "from dfcleanser.data_import.data_import_controller import import_pandas_fwf",
                             "import_pandas_fwf(" + json.dumps(fparms) + "," +
                             str(importId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[0])
        
    return(opstat)
    
"""
#------------------------------------------------------------------
#   import excel file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def import_pandas_excel(fparms,importId,labellist,display=True) : 
    
    opstat = opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        try :
            excelkeys         =   [labellist[1],labellist[2],labellist[3],labellist[4]] 
            excelvals         =   [fparms[1],fparms[2],fparms[3],fparms[4]]
            exceltypes        =   [STRING_PARM,STRING_PARM,STRING_PARM,INT_PARM]

            excelparms        =   {}
            exceladdlparms    =   {}
            
        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
    if(opstat.get_status()) :
        
        try :
            
            excelparms        =   get_function_parms(excelkeys,excelvals,exceltypes)
            
            if(not (fparms[5] == "")) :
                exceladdlparms    =   json.loads(fparms[5])
            
            if (len(exceladdlparms) > 0) :
                addlparmskeys = exceladdlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    excelparms.update({addlparmskeys[i]:exceladdlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :
    
        try :
            if(len(excelparms) == 0) :
                df = pd.read_excel(fparms[0])
            else :
                df = pd.read_excel(fparms[0], **excelparms)
        except Exception as e: 
            opstat.store_exception("Unable to import excel file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            script      =   ["# Import Excel File ",
                             "from dfcleanser.data_import.data_import_controller import import_pandas_excel",
                             "import_pandas_excel(" + json.dumps(fparms) + "," +
                             str(importId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[0])
        
    return(opstat)

"""
#------------------------------------------------------------------
#   import json file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""    
def import_pandas_json(fparms,importId,labellist,display=True) : 
    
    opstat = opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        try :

            jsonkeys         =   [labellist[1],labellist[2],labellist[3]] 
            jsonvals         =   [fparms[1],fparms[2],fparms[3]]
            jsontypes        =   [STRING_PARM,STRING_PARM,STRING_PARM]
    
            jsonparms        =   {}
            jsonaddlparms    =   {}

        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
    if(opstat.get_status()) :
        
        try :
            
            jsonparms        =   get_function_parms(jsonkeys,jsonvals,jsontypes)
            
            if(not (fparms[4] == "")) :
                jsonaddlparms    =   json.loads(fparms[4])
            
            if (len(jsonaddlparms) > 0) :
                addlparmskeys = jsonaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    jsonparms.update({addlparmskeys[i]:jsonaddlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :
    
        try :
            if(len(jsonparms) == 0) :
                df = pd.read_json(fparms[0])
            else :
                df = pd.read_json(fparms[0], **jsonparms)
            
        except Exception as e:
            opstat.store_exception("Unable to import json file" + fparms[0],e)

    if(opstat.get_status()) : 
        
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            script      =   ["# Import JSON File ",
                             "from dfcleanser.data_import.data_import_controller import import_pandas_json",
                             "import_pandas_json(" + json.dumps(fparms) + "," +
                             str(importId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[0])
        
    return(opstat)

"""
#------------------------------------------------------------------
#   import html file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""    
def import_pandas_html(fparms,importId,labellist,display=True) : 
    
    opstat = opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        try :

            htmlkeys         =   [labellist[1],labellist[2],labellist[3],labellist[4]] 
            htmlvals         =   [fparms[1],fparms[2],fparms[3],fparms[4]]
            htmltypes        =   [STRING_PARM,STRING_PARM,STRING_PARM,STRING_PARM]
    
            htmlparms        =   {}
            htmladdlparms    =   {}

        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
    
    if(opstat.get_status()) :
        
        try :
            
            htmlparms        =   get_function_parms(htmlkeys,htmlvals,htmltypes)
            
            if(not (fparms[5] == "")) :
                htmladdlparms    =   json.loads(fparms[5])
            
            if (len(htmladdlparms) > 0) :
                addlparmskeys = htmladdlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    htmlparms.update({addlparmskeys[i]:htmladdlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :  
    
        try :
            if(len(htmlparms) == 0) :
                df = pd.read_html(fparms[0])
            else :
                df = pd.read_html(fparms[0], **htmlparms)
        except Exception as e:
            opstat.store_exception("Unable to import html file" + fparms[0],e)

    if(opstat.get_status()) : 
        
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            script      =   ["# Import HTML File ",
                             "from dfcleanser.data_import.data_import_controller import import_pandas_html",
                             "import_pandas_html(" + json.dumps(fparms) + "," +
                             str(importId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[0])
        
    return(opstat)

"""
#------------------------------------------------------------------
#   import a sql table into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""    
def import_pandas_sqltable(sqltableparms,dbcondict,importid,display=True) :
    
    opstat = opStatus()

    import dfcleanser.common.db_utils as dbu
    dbcon = dbu.dbConnector()
    
    from dfcleanser.common.db_utils import grab_connection_parms
    if(dbcondict == None) :
        parmslist = get_stored_con_Parms(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY))
        dbcondict = set_dbcon_dict(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),parmslist)
        dbconparms = grab_connection_parms(dbcondict)
    else :
        dbconparms = grab_connection_parms(dbcondict)
    
    dbcon.set_ConnectionParms(dbconparms)
    dbconnector = dbcon.connect_to_db(dbu.SQLALCHEMY,opstat)
    
    if(opstat.get_status()) :
        
        if(sqltableparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("Invalid Table Name")
        
        if(sqltableparms[1] == "") :
            sqltableparms[1] = None
        
        if(sqltableparms[2] == "") :
            sqltableparms[2] = None
        else :
            sqltableparms[2] = sqltableparms[2].split(",")
        
        if(sqltableparms[3] == "") :
            sqltableparms[3] = True
        else :
            sqltableparms[3] = False
        
        if(sqltableparms[4] == "") :
            sqltableparms[4] = None
         
        if(sqltableparms[5] == "") :
            sqltableparms[5] = None
        else :
            sqltableparms[5] = sqltableparms[5].split(",")
        
        if(sqltableparms[6] == "") :
            sqltableparms[6] = None
        else :
            sqltableparms[6] = int(sqltableparms[6])
    
        if(opstat.get_status()) :  
    
            try :
                if(dbcondict.get("dbid") == dbu.Oracle) :
                    df = pd.read_sql("select * from " + sqltableparms[0],dbconnector)
                else :
                    df = pd.read_sql_table(sqltableparms[0],dbconnector,sqltableparms[1],sqltableparms[2],
                                           sqltableparms[3],sqltableparms[4],sqltableparms[5],sqltableparms[6])
            except Exception as e:
                opstat.store_exception("Unable to import sql table",e)
                
    import_notes    =   ""

    if(opstat.get_status()) : 
        
        if(display) :
            
            #make scriptable
            import json 
            add_to_script(["# Import SQL Table ",
                           "from dfcleanser.data_import.data_import_controller import import_pandas_sqltable",
                           "import_pandas_sqltable(" + json.dumps(sqltableparms) + 
                           "," + json.dumps(dbcondict) + "," + 
                           str(importid) + ",False)",
                           "from dfcleanser.common.cfg import set_dc_dataframe",
                           "set_dc_dataframe(df)"],opstat)
       
        import_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms) 
        
        if(len(sqltableparms) > 0) :
            cfg.set_config_value(importid + "Parms",sqltableparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,sqltableparms[0])

        cfg.set_dc_dataframe(df)

    return(import_notes, opstat)    


"""
#------------------------------------------------------------------
#   import sql query results into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""    
def import_pandas_sqlquery(sqlqueryparms,dbcondict,importid,display=True) : 
    
    opstat = opStatus()
    
    import dfcleanser.common.db_utils as dbu
    dbcon = dbu.dbConnector()
    
    from dfcleanser.common.db_utils import grab_connection_parms
    if(dbcondict == None) :
        parmslist = get_stored_con_Parms(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY))
        dbcondict = set_dbcon_dict(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),parmslist)
        dbconparms = grab_connection_parms(dbcondict)
    else :
        dbconparms = grab_connection_parms(dbcondict)
    
    dbcon.set_ConnectionParms(dbconparms)
    
    dbconnector = dbcon.connect_to_db(dbu.SQLALCHEMY,opstat)
    
    if(opstat.get_status()) :
        
        if(sqlqueryparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No SQL String Defined")
        
        if(sqlqueryparms[1] == "") :
            sqlqueryparms[1] = None
        else :
            sqlqueryparms[1] = sqlqueryparms[1].split(",")
        
        if(sqlqueryparms[2] == "") :
            sqlqueryparms[2] = True
        else :
            sqlqueryparms[2] = False
        
        if(sqlqueryparms[3] == "") :
            sqlqueryparms[3] = None
        else :
            sqlqueryparms[3] = sqlqueryparms[3].split(",")
         
        if(sqlqueryparms[4] == "") :
            sqlqueryparms[4] = None
        else :
            sqlqueryparms[4] = sqlqueryparms[5].split(",")
        
        if(sqlqueryparms[5] == "") :
            sqlqueryparms[5] = None
        else :
            sqlqueryparms[5] = int(sqlqueryparms[6])
    
        if(opstat.get_status()) :  
    
            try :
                df = pd.read_sql_query(sqlqueryparms[0],dbconnector,sqlqueryparms[1],sqlqueryparms[2],
                                       sqlqueryparms[3],sqlqueryparms[4],sqlqueryparms[5])
            except Exception as e:
                opstat.store_exception("Unable to run sql query",e)

    import_notes    =   ""

    if(opstat.get_status()) : 
        
        if(display) :
        
            #make scriptable
            import json 
            add_to_script(["# Import SQL Query ",
                           "from dfcleanser.data_import.data_import_controller import import_pandas_sqlquery",
                           "import_pandas_sqlquery(" + json.dumps(sqlqueryparms) +"," + json.dumps(dbcondict) + 
                           "," + str(importid) + ",False)",
                           "from dfcleanser.common.cfg import set_dc_dataframe",
                           "set_dc_dataframe(df)"],opstat)
       
        import_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms) 
        
        
        if(len(sqlqueryparms) > 0) :
            cfg.set_config_value(importid + "Parms",sqlqueryparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,sqlqueryparms[0])

        cfg.set_dc_dataframe(df)

    return(import_notes, opstat)    


"""
#------------------------------------------------------------------
#   process custom import into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def process_custom_import(fparms,import_id,display=True) : 
    
    opstat = opStatus() 
       
    try :
        exec(fparms[0])
    except Exception as e:
            opstat.store_exception("Unable to import custom" + fparms[0],e)

    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Import Custom ",
                             "from dfcleanser.data_import.data_import_widgets import process_custom_export",
                             "process_custom_import(" + json.dumps(fparms) + "," +
                             str(import_id) + ",False)"]
                             
            add_to_script(script,opstat)
            
        if(len(fparms) > 0) :
            cfg.set_config_value(import_id + "Parms","custom")
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,"custom")

    return(opstat)
    
        
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   DB Connector testing
#    
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  

def test_import_sql_db_connector(importtype,driverid,sqlinputparms) :
    
    opstat  =   opStatus()
    
    try :
        from dfcleanser.common.db_utils import test_db_connector, SQL_IMPORT, SQL_QUERY
        if(importtype == dim.SQLTABLE_IMPORT) :
            test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),driverid,sqlinputparms,SQL_IMPORT)
        else :
            test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),driverid,sqlinputparms,SQL_QUERY)
            
    except Exception as e: 
        opstat.store_exception("DB Connection failed ",e)
        display_exception(opstat)        




"""
#--------------------------------------------------------------------------
#   Import bookeeping
#--------------------------------------------------------------------------
"""

def clear_data_import_data() :
    
    drop_owner_tables(cfg.DataImport_ID)
    clear_data_import_cfg_values()
    
def clear_data_import_cfg_values() :
    
    cfg.drop_config_value(cfg.CURRENT_DB_ID_KEY)
    cfg.drop_config_value(cfg.CURRENT_SQL_IMPORT_ID_KEY)

    return(True)



