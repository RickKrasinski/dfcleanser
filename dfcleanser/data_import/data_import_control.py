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
import dfcleanser.common.db_utils as dbu

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (get_function_parms, INT_PARM, 
                                            STRING_PARM, displayParms, display_exception,
                                            opStatus, RunningClock, get_string_value, display_status,
                                            display_notes, display_generic_grid, get_formatted_time)

from dfcleanser.common.db_utils import (get_stored_con_Parms, set_dbcon_dict, parse_connector_parms, 
                                        validate_connection_parms, display_db_connector_inputs)

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
def display_import_forms(importid, detid=0, notes=False) :
    
    if(importid == 0) :
        clear_data_import_data()    
    
    from dfcleanser.data_import.data_import_widgets import display_dc_import_forms
    display_dc_import_forms(importid, detid, notes)
    
    if(importid == 0) :
        clear_data_import_data()    
   

def display_sql_details_form(sqlimportid,dblibid) :
    from dfcleanser.data_import.data_import_widgets import display_dc_sql_connector_forms
    display_dc_sql_connector_forms(sqlimportid,dblibid)

def get_columns(importparms) :

    from dfcleanser.common.db_utils import get_db_connector_idList
    dbid        =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    cplist      =   get_db_connector_idList(dbid)
    cparms      =   get_stored_con_Parms(dbid)
    conparms    =   [cplist,cparms]
    
    diw.display_dc_pandas_import_sql_inputs(dim.SQLTABLE_IMPORT,dim.COLUMN_NAMES,dbid,conparms,importparms)

def get_datetimeformats(importparms) :
    
    sqltype     =   importparms[0]
    formparms   =   importparms[1]
    
    if(sqltype == 0) :
        cfg.set_config_value(diw.pandas_import_sqltable_common_id+"Parms",importparms)
        diw.display_dc_pandas_import_sql_inputs(dim.SQLTABLE_IMPORT,dim.DATETIME_FORMATS,None,None,formparms)
    else :
        cfg.set_config_value(diw.pandas_import_sqlquery_id+"Parms",importparms)
        diw.display_dc_pandas_import_sql_inputs(dim.SQLQUERY_IMPORT,dim.DATETIME_FORMATS,None,None,formparms)
        

def display_pandas_import_sql_inputs(importtype,formtype,DBid,dbconparms,importparms=None) :
    
    #$check_list  =   diw.get_dbcondict(DBid,dbconparms,formtype)#validate_connection_parms(dbcondict)
    #$print("check_list",check_list)
    
    #$error_msg   =   check_list[2]
    
    #print("error_msg",error_msg)
    
    #if(error_msg is None) :
    opstat  =   diw.display_dc_pandas_import_sql_inputs(importtype,formtype,DBid,dbconparms,importparms=None)
    
    if( not (opstat.get_status())) :
        
        display_import_forms(2,5)
        print("\n")
        display_exception(opstat)


    
"""
#--------------------------------------------------------------------------
#   process pandas import functions
#--------------------------------------------------------------------------
"""
def process_import_form(formid, parms, display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process import form
    * 
    * parms :
    *  formid   -   form id
    *  parms    -   import parms                      
    *  display  -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if( (formid == dim.CSV_IMPORT)  or (formid == dim.EXCEL_IMPORT) or 
        (formid == dim.JSON_IMPORT) or (formid == dim.HTML_IMPORT) or 
        (formid == dim.FWF_IMPORT)  or (formid == dim.CUSTOM_IMPORT) )  :
        
        #s       =   time.time()
        opstat  =   opStatus()
    
        if(display) :
            clear_output()
            diw.display_import_main_taskbar()
            clock = RunningClock()
            clock.start()

        if (formid == dim.CSV_IMPORT) :
            fparms      =   diw.get_csv_import_inputs(parms)
            opstat      =   import_pandas_csv(fparms)
            
            parmstitle  =   "Pandas CSV Import Parms"
            parmslist   =   diw.pandas_import_csv_labelList[:6]
        
        if (formid == dim.FWF_IMPORT) :
            fparms      =   diw.get_fwf_import_inputs(parms)
            opstat      =   import_pandas_fwf(fparms)
            
            parmstitle  =   "Pandas FWF Import Parms"
            parmslist   =   diw.pandas_import_fwf_labelList[:7]
        
        elif (formid == dim.EXCEL_IMPORT) :
            fparms      =   diw.get_excel_import_inputs(parms)
            opstat      =   import_pandas_excel(fparms)
            
            parmstitle  =   "Pandas Excel Import Parms"
            parmslist   =   diw.pandas_import_excel_labelList[:7]
        
        elif (formid == dim.JSON_IMPORT) : 
            fparms      =   diw.get_json_import_inputs(parms)
            opstat      =   import_pandas_json(fparms)
            
            parmstitle  =   "Pandas JSON Import Parms"
            parmslist   =   diw.pandas_import_json_labelList[:8]
        
        elif (formid == dim.HTML_IMPORT) : 
            fparms      =   diw.get_html_import_inputs(parms)
            opstat      =   import_pandas_html(fparms)
            
            parmstitle  =   "Pandas HTML Import Parms"
            parmslist   =   diw.pandas_import_html_labelList[:8]

        elif (formid == dim.CUSTOM_IMPORT) : 
            (dispstats, opstat)     =   import_custom(parms)
            
            if(dispstats) :
                parmstitle  =   "Custom Import Parms"
                parmslist   =   diw.custom_import_labelList[:2]

        if(opstat.get_status()) : 
            if(display) :
                if (formid == dim.CUSTOM_IMPORT) :
                    if(dispstats) : 
                        ciparms = parms[0].replace("\n","</br>")
                        display_data_import_parms(parmstitle,parmslist,[ciparms],cfg.DataImport_ID,parms[0])

                else :
                    display_data_import_parms(parmstitle,parmslist,fparms,cfg.DataImport_ID,fparms[1])
                    
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

def save_data_import_start() :
    cfg.set_config_value(cfg.CURRENT_IMPORT_START_TIME,time.time())    
def drop_data_import_start() :
    cfg.drop_config_value(cfg.CURRENT_IMPORT_START_TIME)    
def get_data_import_start() :
    return(cfg.get_config_value(cfg.CURRENT_IMPORT_START_TIME))   


def display_data_import_parms(title,plist,fparms,importID,fname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display import parms
    * 
    * parms :
    *  title    -   table title
    *  plist    -   labels list                      
    *  fparms   -   parms list                      
    *  importID -   table id                      
    *  fname    -   file name                     
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    ptitles     =   []
    
    for i in range(len(plist)) :
        ptitles.append(plist[i])
        
    ptitles.append("NUMBER OF ROWS")
    ptitles.append("NUMBER OF COLS")
    
    df  =   cfg.get_current_chapter_df(cfg.CURRENT_IMPORT_DF)
    
    pvalues     =   []
    
    for i in range(len(fparms)) :
        pvalues.append(fparms[i])
        
    pvalues.append(str(len(df)))
    pvalues.append(str(len(df.columns)))
    
    parms_html  =   displayParms(title,ptitles,pvalues,importID,90,20,False,11)
    
    status_html     =   display_status("File " + fname + " Imported successfully as a pandas dataframe ",False)
    importnotes     =   ["[Total Import Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-cfg.get_config_value(cfg.CURRENT_IMPORT_START_TIME)))+ " seconds"]
    notes_html      =   display_notes(importnotes,False)
    drop_data_import_start()

    gridclasses     =   ["dfc-top","dfc-left","dfc-right"]
    gridhtmls       =   [parms_html,status_html,notes_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("data-import-stats-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("data-import-stats-pop-up-wrapper",gridclasses,gridhtmls)
        

    #diw.display_data_import_notes(time.time(),fname)
    

def import_sql_table(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : import a sql table into pandas dataframe 
    * 
    * parms :
    *  parms   -   sql input form parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    diw.display_import_main_taskbar() 
    
    if(display) :
        save_data_import_start()
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
        
        diw.display_data_import_notes(get_data_import_start(),sqltableparms[0],True)
        
    else :
        display_exception(opstat)

    if(display) :
        drop_data_import_start()
        clock.stop()

    
def import_sql_query(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : import from sql query into pandas dataframe 
    * 
    * parms :
    *  parms   -   sql input form parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    diw.display_import_main_taskbar() 
    
    if(display) :
        save_data_import_start()
        clock = RunningClock()
        clock.start()
    
    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    dbcondict = set_dbcon_dict(dbid,get_stored_con_Parms(dbid))

    sqlqueryparms = diw.get_sqlquery_import_inputs(parms)
    
    (import_notes, opstat) = import_pandas_sqlquery(sqlqueryparms, dbcondict, diw.pandas_import_sqlquery_id)
    
    if(opstat.get_status()) : 
        
        for i in range(len(sqlqueryparms)) :
            sqlqueryparms[i]  =  get_string_value(sqlqueryparms[i]) 
            
        displayParms("Pandas SQL Query Import Parms",
                     diw.pandas_import_sqlquery_labelList[0:6],
                     sqlqueryparms[0:6],cfg.DataImport_ID)
        
        display_notes(["DB Connector String : ",
                       "&nbsp;&nbsp;" + import_notes])
        
        diw.display_data_import_notes(get_data_import_start(),sqlqueryparms[0],True)
        
    else :
        display_exception(opstat)
        
    if(display) :
        drop_data_import_start()
        clock.stop()


def import_custom(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : import from custom into pandas dataframe 
    * 
    * parms :
    *  parms   -   associated import parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    functionid = parms[0]
    
    opstat      =   opStatus()
    dispstats   =   False
    
    if(functionid == dim.PROCESS_CUSTOM_IMPORT) :
        opstat      =   process_custom_import(parms[1],diw.custom_import_id,display=True) 
        dispstats   =   True
        
    elif(functionid == dim.CLEAR_CUSTOM_IMPORT) :
        cfg.drop_config_value(diw.custom_import_id + "Parms")
        display_import_forms(dim.IMPORT_CUSTOM_ONLY)

    return(dispstats, opstat)
    
"""
#--------------------------------------------------------------------------
#   process pandas import functions
#--------------------------------------------------------------------------
"""

def get_file_name(filefullname) :
    
    filename    =   filefullname[0:]
    endnewname  =   filename.rfind(".")
    if(endnewname > -1) :
        filename    =   filename[0:endnewname]
        
    startnewname    =   filename.rfind("/")
    if(startnewname > -1) :
        filename    =   filename[startnewname+1:]
        
    return(filename)


"""
#------------------------------------------------------------------
#   import csv file into pandas dataframe
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""
def import_pandas_csv(fparms,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import csv file into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    importId    =   diw.pandas_import_csv_id
    labellist   =   diw.pandas_import_csv_labelList
    
    
    if(display) :
        save_data_import_start() 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[1]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No file_path defined")
        else :
        
            try :

                csvkeys         =   [labellist[2],labellist[3],labellist[4]] 
                csvvals         =   [fparms[2],fparms[3],fparms[4]]
                csvtypes        =   [INT_PARM,STRING_PARM,INT_PARM]
    
                csvparms        =   {}
                csvaddlparms    =   {}
            
            except Exception as e:
                opstat.store_exception("Error parsing import parms",e)
                
            if(opstat.get_status()) :

                if(len(fparms[3]) > 0) :
                    try :
                        with open(fparms[3], 'r') as col_names_file :
                            colNames = json.load(col_names_file)
                            csvvals[1] = colNames
                    except Exception as e: 
                        opstat.store_exception("Unable to open csv column names file " + fparms[3],e)
    
    if(opstat.get_status()) :
        
        try :
            
            csvparms        =   get_function_parms(csvkeys,csvvals,csvtypes)
            if(not (fparms[5] == "")) :
                csvaddlparms    =   json.loads(fparms[5])
            
            if (len(csvaddlparms) > 0) :
                addlparmskeys = csvaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    csvparms.update({addlparmskeys[i]:csvaddlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms ",e)

    if(opstat.get_status()) :
    
        try :
            df = pd.read_csv(fparms[1], **csvparms)
        except Exception as e:
            opstat.store_exception("Unable to import csv file" + fparms[1],e)

    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            csv_title   =   get_file_name(fparms[1])
            fparms[0]   =   csv_title
        else :
            csv_title   =   fparms[0]
        
        csv_df  =   cfg.dfc_dataframe(csv_title,df,fparms[1])
        cfg.add_dfc_dataframe(csv_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,csv_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import CSV File ",
                             "from dfcleanser.data_import.data_import_control import import_pandas_csv",
                             "import_pandas_csv(" + json.dumps(fparms) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            fparms[0]   =   csv_title
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[1])
    
    return(opstat)

    
def import_pandas_fwf(fparms,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import fixed width file into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
                                              
    importId    =   diw.pandas_import_fwf_id
    labellist   =   diw.pandas_import_fwf_labelList
    
    if(display) :
        save_data_import_start() 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[1]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No file_path defined")
            
        else :

            try :

                fwfkeys         =   [labellist[2],labellist[3],labellist[4],labellist[5],labellist[6]] 
                fwfvals         =   [fparms[2],fparms[3],fparms[4],fparms[5],fparms[6]]
                fwftypes        =   [STRING_PARM,INT_PARM,STRING_PARM,INT_PARM,STRING_PARM]
    
                fwfparms        =   {}
                fwfaddlparms    =   {}
            
            except Exception as e:
                opstat.store_exception("Error parsing import parms",e)

            if(opstat.get_status()) :
    
                if(len(fparms[4]) > 0) :
        
                    try :
                        with open(fparms[4], 'r') as col_names_file :
                            colNames = json.load(col_names_file)
                            fwfvals[3] = colNames
                    except Exception as e: 
                        opstat.store_exception("Unable to open fwf column names file" + fparms[4],e)

    if(opstat.get_status()) :
        
        try :
            
            fwfparms        =   get_function_parms(fwfkeys,fwfvals,fwftypes)
            
            if(not (fparms[7] == "")) :
                fwfaddlparms    =   json.loads(fparms[7])
            
            if (len(fwfaddlparms) > 0) :
                addlparmskeys = fwfaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    fwfparms.update({addlparmskeys[i]:fwfaddlparms.get(addlparmskeys[i])})
            
        except Exception as e:
            opstat.store_exception("Unable to get additional parms",e)
    
        
    if(opstat.get_status()) :
    
        try :
            df = pd.read_fwf(fparms[1], **fwfparms)
        except Exception as e:
            opstat.store_exception("Unable to import fwf file" + fparms[1],e)
    
    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            fwf_title   =   get_file_name(fparms[1])
            fparms[0]   =   fwf_title
        else :
            fwf_title   =   fparms[0]
        
        fwf_df  =   cfg.dfc_dataframe(fwf_title,df,fparms[1])
        cfg.add_dfc_dataframe(fwf_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,fwf_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import FWF File ",
                             "from dfcleanser.data_import.data_import_control import import_pandas_fwf",
                             "import_pandas_fwf(" + json.dumps(fparms) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            fparms[0]   =   fwf_title
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[1])
    
    return(opstat)
    

def import_pandas_excel(fparms,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import excel file into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    importId    =   diw.pandas_import_excel_id
    labellist   =   diw.pandas_import_excel_labelList  
    
    if(display) :
        save_data_import_start() 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[1]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No file_path defined")
            
        else :


            try :
                excelkeys         =   [labellist[2],labellist[3],labellist[4],labellist[5]] 
                excelvals         =   [fparms[2],fparms[3],fparms[4],fparms[5]]
                exceltypes        =   [STRING_PARM,STRING_PARM,STRING_PARM,INT_PARM]

                excelparms        =   {}
                exceladdlparms    =   {}
            
            except Exception as e:
                opstat.store_exception("Error parsing import parms",e)
    
            if(opstat.get_status()) :
        
                try :
            
                    excelparms        =   get_function_parms(excelkeys,excelvals,exceltypes)
            
                    if(not (fparms[6] == "")) :
                        exceladdlparms    =   json.loads(fparms[6])
            
                    if (len(exceladdlparms) > 0) :
                        addlparmskeys = exceladdlparms.keys()
                        for i in range(len(addlparmskeys)) : 
                            excelparms.update({addlparmskeys[i]:exceladdlparms.get(addlparmskeys[i])})
            
                except Exception as e:
                    opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :
    
        try :
            if(len(excelparms) == 0) :
                df = pd.read_excel(fparms[1])
            else :
                df = pd.read_excel(fparms[1], **excelparms)
        except Exception as e: 
            opstat.store_exception("Unable to import excel file" + fparms[1],e)
    
    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            excel_title     =   get_file_name(fparms[1])
            fparms[0]       =   excel_title
        else :
            excel_title     =   fparms[0]
        
        excel_df  =   cfg.dfc_dataframe(excel_title,df,fparms[1])
        cfg.add_dfc_dataframe(excel_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,excel_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import Excel File ",
                             "from dfcleanser.data_import.data_import_control import import_pandas_excel",
                             "import_pandas_excel(" + json.dumps(fparms) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            fparms[0]   =   excel_title
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[1])
    
    return(opstat)

  
def import_pandas_json(fparms,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import json file into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    importId    =   diw.pandas_import_json_id
    labellist   =   diw.pandas_import_json_labelList 
    
    if(display) :
        save_data_import_start() 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[1]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No file_path defined")
            
        else :

            try :

                jsonkeys         =   [labellist[2],labellist[3],labellist[4]] 
                jsonvals         =   [fparms[2],fparms[3],fparms[4]]
                jsontypes        =   [STRING_PARM,STRING_PARM,STRING_PARM]
    
                jsonparms        =   {}
                jsonaddlparms    =   {}

            except Exception as e:
                opstat.store_exception("Error parsing import parms",e)
    
            if(opstat.get_status()) :
        
                try :
            
                    jsonparms        =   get_function_parms(jsonkeys,jsonvals,jsontypes)
            
                    if(not (fparms[5] == "")) :
                        jsonaddlparms    =   json.loads(fparms[5])
            
                    if (len(jsonaddlparms) > 0) :
                        addlparmskeys = jsonaddlparms.keys()
                        for i in range(len(addlparmskeys)) : 
                            jsonparms.update({addlparmskeys[i]:jsonaddlparms.get(addlparmskeys[i])})
            
                except Exception as e:
                    opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :
    
        try :
            if(len(jsonparms) == 0) :
                df = pd.read_json(fparms[1])
            else :
                df = pd.read_json(fparms[1], **jsonparms)
            
        except Exception as e:
            opstat.store_exception("Unable to import json file" + fparms[1],e)

    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            json_title     =   get_file_name(fparms[1])
            fparms[0]      =   json_title
        else :
            json_title     =   fparms[0]
        
        json_df  =   cfg.dfc_dataframe(json_title,df,fparms[1])
        cfg.add_dfc_dataframe(json_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,json_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import JSON File ",
                             "from dfcleanser.data_import.data_import_control import import_pandas_json",
                             "import_pandas_json(" + json.dumps(fparms) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            fparms[0]   =   json_title
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[1])
    
    return(opstat)

   
def import_pandas_html(fparms,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import html file into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    importId    =   diw.pandas_import_html_id
    labellist   =   diw.pandas_import_html_labelList
    
    if(display) :
        save_data_import_start() 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[1]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No file_path defined")
            
        else :

            try :

                htmlkeys         =   [labellist[2],labellist[3],labellist[4],labellist[5]] 
                htmlvals         =   [fparms[2],fparms[3],fparms[4],fparms[5]]
                htmltypes        =   [STRING_PARM,STRING_PARM,STRING_PARM,STRING_PARM]
    
                htmlparms        =   {}
                htmladdlparms    =   {}

            except Exception as e:
                opstat.store_exception("Error parsing import parms",e)
    
            if(opstat.get_status()) :
        
                try :
            
                    htmlparms        =   get_function_parms(htmlkeys,htmlvals,htmltypes)
            
                    if(not (fparms[6] == "")) :
                        htmladdlparms    =   json.loads(fparms[6])
            
                    if (len(htmladdlparms) > 0) :
                        addlparmskeys = htmladdlparms.keys()
                        for i in range(len(addlparmskeys)) : 
                            htmlparms.update({addlparmskeys[i]:htmladdlparms.get(addlparmskeys[i])})
            
                except Exception as e:
                    opstat.store_exception("Unable to get additional parms",e)

    if(opstat.get_status()) :  
    
        try :
            if(len(htmlparms) == 0) :
                df = pd.read_html(fparms[1])
            else :
                df = pd.read_html(fparms[1], **htmlparms)
        except Exception as e:
            opstat.store_exception("Unable to import html file" + fparms[1],e)

    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            html_title     =   get_file_name(fparms[1])
            fparms[0]      =   html_title
        else :
            html_title     =   fparms[0]
        
        html_df  =   cfg.dfc_dataframe(html_title,df,fparms[1])
        cfg.add_dfc_dataframe(html_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,html_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import HTML File ",
                             "from dfcleanser.data_import.data_import_control import import_pandas_html",
                             "import_pandas_html(" + json.dumps(fparms) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            fparms[0]   =  html_title 
            cfg.set_config_value(importId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,fparms[1])
        
    return(opstat)

   
def import_pandas_sqltable(sqltableparms,dbcondict,importid,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : import a sql table into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  dbcondict -   db connector dict                      
    *  importId  -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
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
        
        if(sqltableparms[1] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("Invalid Table Name")
        
        if(sqltableparms[2] == "") :
            sqltableparms[2] = None
        
        if(sqltableparms[3] == "") :
            sqltableparms[3] = None
        else :
            sqltableparms[3] = sqltableparms[3].split(",")
        
        if(sqltableparms[4] == "") :
            sqltableparms[4] = True
        else :
            sqltableparms[4] = False
        
        if(sqltableparms[5] == "") :
            sqltableparms[5] = None
         
        if(sqltableparms[6] == "") :
            sqltableparms[6] = None
        else :
            sqltableparms[6] = sqltableparms[6].split(",")
        
        if(sqltableparms[7] == "") :
            sqltableparms[7] = None
        else :
            sqltableparms[7] = int(sqltableparms[7])
    
        if(opstat.get_status()) :  
    
            try :
                if(dbcondict.get("dbid") == dbu.Oracle) :
                    df = pd.read_sql("select * from " + sqltableparms[1],dbconnector)
                else :
                    df = pd.read_sql_table(sqltableparms[1],dbconnector,sqltableparms[2],sqltableparms[3],
                                           sqltableparms[4],sqltableparms[5],sqltableparms[6],sqltableparms[7])
            except Exception as e:
                opstat.store_exception("Unable to import sql table " + sqltableparms[1],e)
                
    import_notes    =   ""

    if(opstat.get_status()) : 
        
        if(len(sqltableparms[0]) == 0) :
            sql_title           =   sqltableparms[1] + "_df"
            sqltableparms[0]    =   sql_title
        else :
            sql_title           =   sqltableparms[0]
        
        sql_df  =   cfg.dfc_dataframe(sql_title,df,sqltableparms[1])
        cfg.add_dfc_dataframe(sql_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,sql_title)
        
        if(display) :
            
            #make scriptable
            import json 
            add_to_script(["# Import SQL Table ",
                           "from dfcleanser.data_import.data_import_control import import_pandas_sqltable",
                           "import_pandas_sqltable(" + json.dumps(sqltableparms) + 
                           "," + json.dumps(dbcondict) + "," + 
                           str(importid) + ",False)"],opstat)
       
        import_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms) 
        
        if(len(sqltableparms) > 0) :
            sqltableparms[0]   =   sql_title
            cfg.set_config_value(importid + "Parms",sqltableparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,sqltableparms[1])

    return(import_notes, opstat)    

   
def import_pandas_sqlquery(sqlqueryparms,dbcondict,importid,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : import sql query results into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  dbcondict -   db connector dict                      
    *  importId  -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
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
        
        if(sqlqueryparms[1] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No SQL String Defined")
        
        if(sqlqueryparms[2] == "") :
            sqlqueryparms[2] = None
        else :
            sqlqueryparms[2] = sqlqueryparms[2].split(",")
        
        if(sqlqueryparms[3] == "") :
            sqlqueryparms[3] = True
        else :
            sqlqueryparms[3] = False
        
        if(sqlqueryparms[4] == "") :
            sqlqueryparms[4] = None
        else :
            sqlqueryparms[4] = sqlqueryparms[4].split(",")
         
        if(sqlqueryparms[5] == "") :
            sqlqueryparms[5] = None
        else :
            sqlqueryparms[5] = sqlqueryparms[5].split(",")
        
        if(sqlqueryparms[6] == "") :
            sqlqueryparms[6] = None
        else :
            sqlqueryparms[6] = int(sqlqueryparms[6])
    
        if(opstat.get_status()) :  
    
            try :
                df = pd.read_sql_query(sqlqueryparms[1],dbconnector,sqlqueryparms[2],sqlqueryparms[3],
                                       sqlqueryparms[4],sqlqueryparms[5],sqlqueryparms[6])
            except Exception as e:
                opstat.store_exception("Unable to run sql query " + sqlqueryparms[1],e)

    import_notes    =   ""

    if(opstat.get_status()) : 
        
        if(len(sqlqueryparms[0]) == 0) :
            sql_title           =   "sql_query_df"
        else :
            sql_title           =   sqlqueryparms[0]
        
        sql_df  =   cfg.dfc_dataframe(sql_title,df,sqlqueryparms[1])
        cfg.add_dfc_dataframe(sql_df)
        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,sql_title)
        
        if(display) :
        
            #make scriptable
            import json 
            add_to_script(["# Import SQL Query ",
                           "from dfcleanser.data_import.data_import_control import import_pandas_sqlquery",
                           "import_pandas_sqlquery(" + json.dumps(sqlqueryparms) +"," + json.dumps(dbcondict) + 
                           "," + str(importid) + ",False)"],opstat)
       
        import_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms) 
        
        
        if(len(sqlqueryparms) > 0) :
            sqlqueryparms[0]    =   sql_title
            cfg.set_config_value(importid + "Parms",sqlqueryparms)
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,sqlqueryparms[1])

    return(import_notes, opstat)    


def process_custom_import(fparms,import_id,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : process custom import into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  importId  -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus() 
       
    try :
        df = exec(fparms[1])
    except Exception as e:
            opstat.store_exception("Unable to import custom" + fparms[1],e)

    if(opstat.get_status()) : 
        
        if(len(fparms[0]) == 0) :
            custom_title    =   "CurrentImportedData"
            fparms[0]       =   custom_title
        else :
            custom_title    =   fparms[0]
        
        custom_df  =   cfg.dfc_dataframe(custom_title,df,fparms[1])
        cfg.add_dfc_dataframe(custom_df)
        cfg.save_config_value(cfg.CURRENT_IMPORT_DF,custom_title)
        
        if(display) :
            #make scriptable
            script      =   ["# Import Custom ",
                             "from dfcleanser.data_import.data_import_control import process_custom_export",
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
    """
    * -------------------------------------------------------------------------- 
    * function : test a swl connector 
    * 
    * parms :
    *  importtype      -   import type                      
    *  driverid        -   db driver id                      
    *  sqlinputparms   -   sql parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
      
    opstat  =   opStatus()
    
    try :
        
        connectParms  =   {}
        parmslist = parse_connector_parms(sqlinputparms,cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),connectParms)
    
        errormsg = validate_connection_parms(connectParms)
    
        if(errormsg is None) :
        
            from dfcleanser.common.db_utils import test_db_connector, SQL_IMPORT, SQL_QUERY, NATIVE, SQLALCHEMY
            if(importtype == dim.SQLTABLE_IMPORT) :
                test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),NATIVE,sqlinputparms,SQL_IMPORT,opstat)
                test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),SQLALCHEMY,sqlinputparms,SQL_IMPORT,opstat)
            else :
                test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),NATIVE,sqlinputparms,SQL_QUERY,opstat)
                test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),SQLALCHEMY,sqlinputparms,SQL_QUERY,opstat)
                    
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg(errormsg)
            
            
    except Exception as e: 
        opstat.store_exception("DB Connection failed ",e)
        #display_exception(opstat)        
    
    #if(importtype == dim.SQLTABLE_IMPORT) :
    #    display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),parmslist,dbu.SQL_IMPORT) 
    #else :
    #    display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),parmslist,dbu.SQL_QUERY) 
    
    #if(not (opstat.get_status())) :
    #    display_exception(opstat)        


"""
#--------------------------------------------------------------------------
#   Import bookeeping
#--------------------------------------------------------------------------
"""

def clear_data_import_data() :
    
    drop_owner_tables(cfg.DataImport_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    define_inputs(cfg.DataImport_ID,diw.dataimport_inputs)
    delete_all_inputs(cfg.DataImport_ID)
    clear_data_import_cfg_values()
    
def clear_data_import_cfg_values() :
    
    cfg.drop_config_value(cfg.CURRENT_DB_ID_KEY)
    cfg.drop_config_value(cfg.CURRENT_SQL_IMPORT_ID_KEY)
    cfg.drop_config_value(cfg.CURRENT_IMPORT_START_TIME)    

    return(True)



