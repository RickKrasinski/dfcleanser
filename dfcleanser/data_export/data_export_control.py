"""
# data_export_control
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.data_export.data_export_widgets as dew
import dfcleanser.data_export.data_export_model as dem

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (get_function_parms, opStatus, RunningClock, display_exception, 
                                            INT_PARM, STRING_PARM, displayParms, get_string_value, display_notes)

from dfcleanser.common.db_utils import (get_stored_con_Parms, set_dbcon_dict)


from dfcleanser.common.html_widgets import (displayHeading)


from dfcleanser.scripting.data_scripting_control import add_to_script

from IPython.display import clear_output
     
import json
import time

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process export functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process export functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   pass through to display widgets
#--------------------------------------------------------------------------
"""
def display_export_forms(id, detid=0, notes=False) :
    dew.display_dc_export_forms(id, detid, notes)

def display_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms=None) :
    dew.display_dc_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms)

"""
#--------------------------------------------------------------------------
#   export routing function
#--------------------------------------------------------------------------
"""
def process_export_form(formid, parms, display=True) :

    if( not (cfg.is_a_dfc_dataframe_loaded()) ) :
        print("No Dataframe Currently Loadad")
        return()
    
    if( (formid == dem.CSV_EXPORT)  or (formid == dem.EXCEL_EXPORT) or 
        (formid == dem.JSON_EXPORT) or (formid == dem.HTML_EXPORT) or 
        (formid == dem.CUSTOM_EXPORT) )  :
    
        s       =   time.time()
        opstat  =   opStatus()
    
        if(display) :
            clear_output()
            dew.display_export_main_taskbar()
            clock = RunningClock()
            clock.start()
    
            displayHeading("Exporting",4)
    
        if (formid == dem.CSV_EXPORT) :
            fparms      =   dew.get_csv_export_inputs(parms)
            opstat      =   export_pandas_csv(fparms,
                                              dew.get_csv_export_form_id(),
                                              dew.get_csv_export_form_labels())
            
            parmstitle  =   "Pandas CSV Export Parms"
            parmslist   =   dew.get_csv_export_form_labels()[:5]
        
        elif (formid == dem.EXCEL_EXPORT) :
            fparms      =   dew.get_excel_export_inputs(parms)
            opstat      =   export_pandas_excel(fparms,
                                                dew.get_excel_export_form_id(),
                                                dew.get_excel_export_form_labels())
            
            parmstitle  =   "Pandas Excel Export Parms"
            parmslist   =   dew.get_excel_export_form_labels()[:6]
        
        elif (formid == dem.JSON_EXPORT) : 
            fparms      =   dew.get_json_export_inputs(parms)
            opstat      =   export_pandas_json(fparms,
                                               dew.get_json_export_form_id(),
                                               dew.get_json_export_form_labels())
            
            parmstitle  =   "Pandas JSON Export Parms"
            parmslist   =   dew.get_json_export_form_labels()[:2]
        
        elif (formid == dem.HTML_EXPORT) : 
            fparms      =   dew.get_html_export_inputs(parms)
            opstat      =   export_pandas_html(fparms,
                                               dew.get_html_export_form_id(),
                                               dew.get_html_export_form_labels())
            
            parmstitle  =   "Pandas HTML Export Parms"
            parmslist   =   dew.get_html_export_form_labels()[:4]

        elif (formid == dem.CUSTOM_EXPORT) : 
            (dispstats, opstat)     =   export_custom(parms)
            
            if(dispstats) :
                parmstitle  =   "Custom Export Parms"
                parmslist   =   dew.get_custom_export_form_labels()[0]
           
        if(opstat.get_status()) : 
            if(display) :
                if (formid == dem.CUSTOM_EXPORT) :
                    if(dispstats) : 
                        ciparms = parms[0].replace("\n","</br>")
                        displayParms(parmstitle,parmslist,[ciparms],cfg.DataExport_ID)
                        dew.display_data_export_notes(s,fparms[0])
                else : 
                    displayParms(parmstitle,parmslist,fparms,cfg.DataExport_ID)
                    dew.display_data_export_notes(s,fparms[0])
        else :
            display_exception(opstat)

        if(display) :
            clock.stop()
        
    elif (formid == dem.SQLTABLE_EXPORT) : 
        export_sql_table(parms)
    else :
        print("Invalid formid "+ str(formid))
        return

"""
#------------------------------------------------------------------
#   export a sql table into pandas dataframe - javascript helper
#
#    parms       -   html input form parms 
#
#------------------------------------------------------------------
"""   
def export_sql_table(parms,display=True) :
    
    opstat  =   opStatus()
    
    dew.display_export_main_taskbar()
    s = time.time()
    
    clock = RunningClock()
    clock.start()
    
    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    dbcondict = set_dbcon_dict(dbid,get_stored_con_Parms(dbid))

    sqltableparms = dew.get_sqltable_export_inputs(parms)
    
    (export_notes, opstat) = export_pandas_sqltable(sqltableparms, dbcondict, dew.get_sqltable_export_form_id)    

    clock.stop() 
    
    if(opstat.get_status()) : 
        
        for i in range(len(sqltableparms)) :
            sqltableparms[i]  =  get_string_value(sqltableparms[i]) 
            
        displayParms("Pandas SQL Table Export Parms",
                     dew.get_sqltable_export_form_labels()[0:7],
                     sqltableparms[0:7],cfg.DataExport_ID)
        
        display_notes(["DB Connector String : ",
                       "&nbsp;&nbsp;" + export_notes])
        
        dew.display_data_export_notes(s,sqltableparms[0],True)
        
    else :
        display_exception(opstat)
      
"""
#--------------------------------------------------------------------------
#   pandas custom export
#--------------------------------------------------------------------------
"""     
"""
#--------------------------------------------------------------------------
#   pandas custom export
#--------------------------------------------------------------------------
"""     
def export_custom(parms) :
    
    functionid = parms[0]
    
    opstat      =   opStatus()
    dispstats   =   False
    
    if(functionid == 1) :
        opstat      =   process_custom_export(parms[1],dew.get_custom_export_form_id(),display=True) 
        dispstats   =   True
        
    elif(functionid == 2) :
        custom_code = "# custom export\n"
        custom_code = custom_code + parms[1]
        cfg.set_config_value(dew.get_custom_export_form_id() + "Parms",custom_code)
        display_export_forms(dem.EXPORT_CUSTOM_ONLY)
        
    elif(functionid == 3) :
        cfg.drop_config_value(dew.get_custom_export_form_id() + "Parms")
        display_export_forms(dem.EXPORT_CUSTOM_ONLY)
        
    elif(functionid == 5) :
        display_export_forms(dem.EXPORT_CUSTOM_ONLY,-1,True)

    return(dispstats, opstat)


"""
#------------------------------------------------------------------
#   test the sql db connector
#
#    importtype         -   pandas import identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
""" 
def test_export_sql_db_connector(driverid,sqlinputparms) :
    
    opstat  =   opStatus()
    
    try :
        export_test_sql_db_connector(driverid,sqlinputparms)
    except Exception as e: 
        opstat.store_exception("DB Connection failed ",e)
        display_exception(opstat)        








"""
#--------------------------------------------------------------------------
#   pandas csv export
#--------------------------------------------------------------------------
"""
def export_pandas_csv(fparms,exportId,labellist,display=True) : 
    
    opstat          =   opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            csvkeys         =   [labellist[1],labellist[2],labellist[3]] 
            csvvals         =   [fparms[1],fparms[2],fparms[3]]
            csvtypes        =   [INT_PARM,STRING_PARM,INT_PARM]

            csvparms        =   {}
            csvaddlparms    =   {}

        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
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
            opstat.store_exception("Unable to get additional parms for csv export",e)

    if(opstat.get_status()) :
        
        df = cfg.get_dfc_dataframe()
        
        try :
            if(len(csvparms) > 0) :
                df.to_csv(fparms[0], **csvparms)
            else :
                df.to_csv(fparms[0])
            
        except Exception as e: 
            opstat.store_exception("Unable to export to csv file " + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export CSV File ",
                             "from dfcleanser.data_export.data_export_widgets import export_pandas_csv",
                             "export_pandas_csv(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)
        
"""
#--------------------------------------------------------------------------
#   pandas excel export
#--------------------------------------------------------------------------
"""
def export_pandas_excel(fparms,exportId,labellist,display=True) : 
    
    opstat          =   opStatus()    
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            excelkeys       =   [labellist[1],labellist[2],labellist[3],labellist[4]] 
            excelvals       =   [fparms[1],fparms[2],fparms[3],fparms[4]]
            exceltypes      =   [STRING_PARM,STRING_PARM,STRING_PARM,INT_PARM]
    
            excelparms      =   {}
            exceladdlparms  =   {}

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
            opstat.store_exception("Unable to get additional parms for excel export",e)
    
    if(opstat.get_status()) : 
        
        df = cfg.get_dfc_dataframe()
    
        try :
            if(len(excelparms) > 0) :
                df.to_excel(fparms[0], **excelparms)
            else :
                df.to_excel(fparms[0])
            
        except Exception as e: 
            opstat.store_exception("Unable to export excel file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export Excel File ",
                             "from dfcleanser.data_export.data_export_widgets import export_pandas_excel",
                             "export_pandas_excel(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])
    
    return(opstat)

"""
#--------------------------------------------------------------------------
#   pandas json export
#--------------------------------------------------------------------------
"""
def export_pandas_json(fparms,exportId,labellist,display=True) : 
    
    opstat          =   opStatus()    

    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            jsonkeys         =   [labellist[1],labellist[2]] 
            jsonvals         =   [fparms[1],fparms[2]]
            jsontypes        =   [STRING_PARM,STRING_PARM]

            jsonparms        =   {}
            jsonaddlparms    =   {}

        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
    if(opstat.get_status()) :

        try :
            
            jsonparms        =   get_function_parms(jsonkeys,jsonvals,jsontypes)
            if(not (fparms[3] == "")) :
                jsonaddlparms    =   json.loads(fparms[3])
            
            if (len(jsonaddlparms) > 0) :
                addlparmskeys = jsonaddlparms.keys()
                for i in range(len(addlparmskeys)) : 
                    jsonparms.update({addlparmskeys[i]:jsonaddlparms.get(addlparmskeys[i])})

        except Exception as e:
            opstat.store_exception("Unable to get additional parms for json export",e)

    if(opstat.get_status()) :
        
        df = cfg.get_dfc_dataframe()
    
        try :
            if(len(jsonparms) > 0) :
                df.to_json(fparms[0], **jsonparms)
            else :
                df.to_json(fparms[0])
            
        except Exception as e: 
            opstat.store_exception("Unable to export json file" + fparms[0],e)
            #display_exception(opstat)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export JSON File ",
                             "from dfcleanser.data_export.data_export_widgets import export_pandas_json",
                             "export_pandas_json(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)

"""
#--------------------------------------------------------------------------
#   pandas html export
#--------------------------------------------------------------------------
"""    
def export_pandas_html(fparms,exportId,labellist,display=True) : 
    
    opstat          =   opStatus()    

    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            htmlkeys        =   [labellist[1],labellist[2],labellist[3],labellist[4]] 
            htmlvals        =   [fparms[1],fparms[2],fparms[3],fparms[4]]
            htmltypes       =   [INT_PARM,STRING_PARM,STRING_PARM,STRING_PARM]

            htmlparms       =   {}
            htmladdlparms   =   {}

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
        
        df = cfg.get_dfc_dataframe()
    
        try :
            if(len(htmlparms) > 0) :
                df.to_html(fparms[0], **htmlparms)
            else :
                df.to_html(fparms[0])
        
        except Exception as e: 
            opstat.store_exception("Unable to export html file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export HTML File ",
                             "from dfcleanser.data_export.data_export_widgets import export_pandas_html",
                             "export_pandas_html(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]
                             
            add_to_script(script,opstat)
            
        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)

"""
#--------------------------------------------------------------------------
#   custom export
#--------------------------------------------------------------------------
"""
def process_custom_export(fparms,exportId,display=True) : 

    opstat          =   opStatus()
    
    fparms[0] = fparms[0].replace("\n","<br/>")
        
    try :
        exec(fparms[0])
    except Exception as e:
            opstat.store_exception("Unable to export custom",e)
            
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export Custom ",
                             "from dfcleanser.data_export.data_export_widgets import process_custom_export",
                             "process_custom_export(" + json.dumps(fparms) + "," +
                             str(exportId) + ",False)"]
                             
            add_to_script(script,opstat)
            
        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms","custom")
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,"custom")

    return(opstat)

       
"""
#------------------------------------------------------------------
#   export pandas dataframe into sql table
#
##   parms       -   associated import parms 
#
#------------------------------------------------------------------
"""      
def export_pandas_sqltable(sqltableparms,dbcondict,exportid,display=True) :
    
    opstat = opStatus()
    
    df = cfg.get_dfc_dataframe()

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
        
        if(sqltableparms[3] == "") :
            sqltableparms[3] = 'fail'
        
        if(sqltableparms[4] == "") :
            sqltableparms[4] = True
         
        if(sqltableparms[5] == "") :
            sqltableparms[5] = None
        
        if(sqltableparms[6] == "") :
            sqltableparms[6] = None
        else :
            sqltableparms[6] = int(sqltableparms[6])
        
        if(sqltableparms[7] == "") :
            sqltableparms[7] = None
        
    
        if(opstat.get_status()) :  
    
            try :
                df.to_sql(sqltableparms[0],dbconnector,sqltableparms[1],sqltableparms[2],
                          sqltableparms[3],sqltableparms[4],sqltableparms[5],sqltableparms[6],
                          sqltableparms[7])
                
            except Exception as e:
                opstat.store_exception("Unable to export sql table",e)

    export_notes    =   ""

    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            add_to_script(["# Export SQL Table ",
                           "from dfcleanser.data_export.data_export_widgets export export_pandas_sqltable",
                           "export_pandas_sqltable(" + json.dumps(sqltableparms) + "," + 
                           + json.dumps(dbcondict) + "," + str(exportid) + ",False)",
                           "from dfcleanser.common.cfg import set_current_dfc_dataframe",
                           "set_current_dfc_dataframe(df)"],opstat)
       
        export_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms)
        
        if(len(sqltableparms) > 0) :
            cfg.set_config_value(exportid + "Parms",sqltableparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,sqltableparms[0])

    return(export_notes, opstat)    


"""
#------------------------------------------------------------------
#   test the sql db connector
#
#    importtype         -   pandas import identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
"""    
def export_test_sql_db_connector(driverid,sqlinputparms) :
    
    try :

        from dfcleanser.common.db_utils import test_db_connector, SQL_EXPORT
        opstat  =   test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),driverid,sqlinputparms,SQL_EXPORT)
            
    except Exception as e: 
        opstat.store_exception("DB Connection failed ",e)
        display_exception(opstat)        


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   misc data export functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def clear_data_export_data() :
    
    drop_owner_tables(cfg.DataExport_ID)
    clear_data_export_cfg_values()
    
def clear_data_export_cfg_values() :
    
    return(True)



