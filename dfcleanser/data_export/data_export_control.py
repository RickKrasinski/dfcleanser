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
                                            INT_PARM, STRING_PARM, BOOLEAN_PARM, DICT_PARM, 
                                            displayParms, get_string_value, display_generic_grid, 
                                            display_status, display_notes, get_formatted_time)

from dfcleanser.common.db_utils import (get_stored_con_Parms, set_dbcon_dict)


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
def display_export_forms(exportid, detid=0, notes=False) :
    
    if(exportid == dem.EXPORT_TB_ONLY) :
        clear_data_export_data()    

    dew.display_dc_export_forms(exportid, detid, notes)
    
def display_export_sql_details_form(cmd,dblibid) :
    from dfcleanser.data_import.data_import_widgets import display_dc_sql_connector_forms
    from dfcleanser.common.db_utils import SQL_EXPORT
    display_dc_sql_connector_forms(dblibid)

def display_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms=None) :
    dew.display_dc_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms)


def process_export_form(formid, parms, display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process export function
    * 
    * parms :
    *   formid   -   form id
    *   fname    -   export parms
    *   display  -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.DataExport_ID)) ) :
        define_inputs(cfg.DataExport_ID,dew.dataexport_inputs)

    if( not (cfg.is_a_dfc_dataframe_loaded()) ) :
        print("No Dataframe Currently Loadad")
        return()
    
    if( (formid == dem.CSV_EXPORT)  or (formid == dem.EXCEL_EXPORT) or 
        (formid == dem.JSON_EXPORT) or (formid == dem.HTML_EXPORT) or 
        (formid == dem.CUSTOM_EXPORT) )  :
    
        opstat  =   opStatus()
    
        if(display) :
            clear_output()
            dew.display_export_main_taskbar()
            
            save_data_export_start()
            clock = RunningClock()
            clock.start()
    
        if (formid == dem.CSV_EXPORT) :
            fparms      =   dew.get_csv_export_inputs(parms)
            opstat      =   export_pandas_csv(fparms,
                                              dew.pandas_export_csv_id,
                                              dew.pandas_export_csv_labelList)
            
            parmstitle  =   "Pandas CSV Export Parms"
            parmslist   =   dew.pandas_export_csv_labelList[:6]
        
        elif (formid == dem.EXCEL_EXPORT) :
            fparms      =   dew.get_excel_export_inputs(parms)
            opstat      =   export_pandas_excel(fparms,
                                                dew.pandas_export_excel_id,
                                                dew.pandas_export_excel_labelList)
            
            parmstitle  =   "Pandas Excel Export Parms"
            parmslist   =   dew.pandas_export_excel_labelList[:7]
        
        elif (formid == dem.JSON_EXPORT) : 
            fparms      =   dew.get_json_export_inputs(parms)
            opstat      =   export_pandas_json(fparms,
                                               dew.pandas_export_json_id,
                                               dew.pandas_export_json_labelList)
            
            parmstitle  =   "Pandas JSON Export Parms"
            parmslist   =   dew.pandas_export_json_labelList[:6]
        
        elif (formid == dem.HTML_EXPORT) : 
            fparms      =   dew.get_html_export_inputs(parms)
            opstat      =   export_pandas_html(fparms,
                                               dew.pandas_export_html_id,
                                               dew.pandas_export_html_labelList)
            
            parmstitle  =   "Pandas HTML Export Parms"
            parmslist   =   dew.pandas_export_html_labelList[:8]

        elif (formid == dem.CUSTOM_EXPORT) : 
            (dispstats, opstat)     =   export_custom(parms)
            
            if(dispstats) :
                parmstitle  =   "Custom Export Parms"
                parmslist   =   dew.custom_export_labelList[:4]
           
        if(opstat.get_status()) : 
            if(display) :
                if (formid == dem.CUSTOM_EXPORT) :
                    if(dispstats) : 
                        ciparms = parms[0].replace("\n","</br>")
                        display_data_export_parms(parmstitle,parmslist,[ciparms],cfg.DataExport_ID,fparms[1],True)

                else : 
                    display_data_export_parms(parmstitle,parmslist,fparms,cfg.DataExport_ID,fparms[1])

        else :
            display_exception(opstat)

        if(display) :
            clock.stop()
        
    elif (formid == dem.SQLTABLE_EXPORT) : 
        export_sql_table(parms)
    else :
        print("Invalid formid "+ str(formid))
        return

def save_data_export_start() :
    cfg.set_config_value(cfg.CURRENT_EXPORT_START_TIME,time.time())    
def drop_data_export_start() :
    cfg.drop_config_value(cfg.CURRENT_EXPORT_START_TIME)    
def get_data_export_start() :
    return(cfg.get_config_value(cfg.CURRENT_EXPORT_START_TIME))   

def display_data_export_parms(title,plist,fparms,exportID,fname,custom=False,dbnote=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display export parms
    * 
    * parms :
    *   title       -   poarms title
    *   plist       -   label list
    *   fparms      -   values list
    *   exportID    -   export table id
    *   fname       -   file name
    *   dbnote      -   dbnote flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    #print("display_data_export_parms",title,plist,fparms)
    
    parms_html  =   displayParms(title,plist,fparms,exportID,100,2,False)
    
    if(custom) :
        status_html     =   display_status("Custom export code Exported successfully",False,False)
        
        exportnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-get_data_export_start()))+ " seconds",
                       "( check if df exists via dfcleanser.common.cfg.is_a_dfc_dataframe_loaded() )"]
        
    else :
        
        if(dbnote) :
            status_html     =   display_status(" Dataframe Exported successfully to table " + fname,False,False)
        else :    
            status_html     =   display_status(" Dataframe Exported successfully to File " + fname,False,False)

        exportnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-get_data_export_start()))+ " seconds"]

    notes_html  =   display_notes(exportnotes,False)
    
    gridclasses     =   ["dfc-top","dfc-left","dfc-right"]
    gridhtmls       =   [parms_html,status_html,notes_html]
    display_generic_grid("data-import-stats-wrapper",gridclasses,gridhtmls)
    

def export_sql_table(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : export a sql table into pandas dataframe
    * 
    * parms :
    *   parms       -   sql parms
    *   display     -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    dew.display_export_main_taskbar()
    
    save_data_export_start()
    clock = RunningClock()
    clock.start()
    
    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    dbcondict = set_dbcon_dict(dbid,get_stored_con_Parms(dbid))

    sqltableparms = dew.get_sqltable_export_inputs(parms)
    
    (export_notes, opstat) = export_pandas_sqltable(sqltableparms, dbcondict, dew.pandas_export_sqltable_id)    

    clock.stop() 
    
    if(opstat.get_status()) : 
        
        for i in range(len(sqltableparms)) :
            sqltableparms[i]  =  get_string_value(sqltableparms[i]) 
        
        sqltableparms   =   sqltableparms[0:8]
        sqltableparms.append(export_notes)
        sqltablelabels  =   dew.pandas_export_sqltable_labelList[0:8]
        sqltablelabels.append("DB Connector String")
        
        display_data_export_parms("Pandas SQL Table Export Parms",
                                  sqltablelabels,sqltableparms,
                                  cfg.DataExport_ID,sqltableparms[1],True)        
        
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
    """
    * -------------------------------------------------------------------------- 
    * function : export a custom 
    * 
    * parms :
    *   parms       -   sql parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    functionid = parms[0]
    
    opstat      =   opStatus()
    dispstats   =   False
    
    if(functionid == 1) :
        opstat      =   process_custom_export(parms[1],dew.custom_export_id,display=True) 
        dispstats   =   True
        
    elif(functionid == 2) :
        custom_code = "# custom export\n"
        custom_code = custom_code + parms[1]
        cfg.set_config_value(dew.custom_export_id + "Parms",custom_code)
        display_export_forms(dem.EXPORT_CUSTOM_ONLY)
        
    elif(functionid == 3) :
        cfg.drop_config_value(dew.custom_export_id + "Parms")
        display_export_forms(dem.EXPORT_CUSTOM_ONLY)
        
    elif(functionid == 5) :
        display_export_forms(dem.EXPORT_CUSTOM_ONLY,-1,True)

    return(dispstats, opstat)


def test_export_sql_db_connector(driverid,sqlinputparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : test the sql db connector 
    * 
    * parms :
    *   importtype         -   pandas export identifier
    *   sqlinputparms      -   connection string
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    try :
        export_test_sql_db_connector(driverid,sqlinputparms)
    except Exception as e: 
        opstat.store_exception("DB Connection failed ",e)
        display_exception(opstat)        


def export_pandas_csv(fparms,exportId,labellist,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : pandas csv export 
    * 
    * parms :
    *   fparms        -   export parms
    *   exportId      -   export id
    *   labellist     -   parm label list
    *   display       -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat          =   opStatus()
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            csvkeys         =   [labellist[2],labellist[3],labellist[4]] 
            csvvals         =   [fparms[2],fparms[3],fparms[4]]
            csvtypes        =   [STRING_PARM,BOOLEAN_PARM,BOOLEAN_PARM]

            csvparms        =   {}
            csvaddlparms    =   {}

        except Exception as e:
            opstat.store_exception("Error parsing import parms",e)
    
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
            opstat.store_exception("Unable to get additional parms for csv export",e)

    if(opstat.get_status()) :
        
        if(fparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe slected")
        else :
            df = cfg.get_dfc_dataframe_df(fparms[0])            
        
            try :
                if(len(csvparms) > 0) :
                    df.to_csv(fparms[1], **csvparms)
                else :
                    df.to_csv(fparms[1])
            
            except Exception as e: 
                opstat.store_exception("Unable to export to csv file " + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export CSV File ",
                             "from dfcleanser.data_export.data_export_control import export_pandas_csv",
                             "export_pandas_csv(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)
        

def export_pandas_excel(fparms,exportId,labellist,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : pandas excel export 
    * 
    * parms :
    *   fparms        -   export parms
    *   exportId      -   export id
    *   labellist     -   parm label list
    *   display       -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat          =   opStatus()    
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            excelkeys       =   [labellist[2],labellist[3],labellist[4],labellist[5]] 
            excelvals       =   [fparms[2],fparms[3],fparms[4],fparms[5]]
            exceltypes      =   [STRING_PARM,STRING_PARM,BOOLEAN_PARM,BOOLEAN_PARM]
    
            excelparms      =   {}
            exceladdlparms  =   {}

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
            opstat.store_exception("Unable to get additional parms for excel export",e)
    
    if(opstat.get_status()) : 
        
        if(fparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe slected")
        else :
            df = cfg.get_dfc_dataframe_df(fparms[0])            
    
            try :
                if(len(excelparms) > 0) :
                    df.to_excel(fparms[1], **excelparms)
                else :
                    df.to_excel(fparms[1])
            
            except Exception as e: 
                opstat.store_exception("Unable to export excel file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export Excel File ",
                             "from dfcleanser.data_export.data_export_control import export_pandas_excel",
                             "export_pandas_excel(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])
    
    return(opstat)


def export_pandas_json(fparms,exportId,labellist,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : pandas json export 
    * 
    * parms :
    *   fparms        -   export parms
    *   exportId      -   export id
    *   labellist     -   parm label list
    *   display       -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat          =   opStatus()    

    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            jsonkeys         =   [labellist[2],labellist[3]] 
            jsonvals         =   [fparms[2],fparms[3]]
            jsontypes        =   [STRING_PARM,STRING_PARM]

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
            opstat.store_exception("Unable to get additional parms for json export",e)

    if(opstat.get_status()) :
        
        if(fparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe slected")
        else :
            df = cfg.get_dfc_dataframe_df(fparms[0])            
    
            try :
                if(len(jsonparms) > 0) :
                    df.to_json(fparms[1], **jsonparms)
                else :
                    df.to_json(fparms[1])
            
            except Exception as e: 
                opstat.store_exception("Unable to export json file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export JSON File ",
                             "from dfcleanser.data_export.data_export_control import export_pandas_json",
                             "export_pandas_json(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]

            add_to_script(script,opstat)

        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)

   
def export_pandas_html(fparms,exportId,labellist,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : pandas html export 
    * 
    * parms :
    *   fparms        -   export parms
    *   exportId      -   export id
    *   labellist     -   parm label list
    *   display       -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat          =   opStatus()    

    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        try :

            htmlkeys        =   [labellist[2],labellist[3],labellist[4],labellist[5]] 
            htmlvals        =   [fparms[2],fparms[3],fparms[4],fparms[5]]
            htmltypes       =   [INT_PARM,BOOLEAN_PARM,BOOLEAN_PARM,STRING_PARM]

            htmlparms       =   {}
            htmladdlparms   =   {}

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
        
        if(fparms[0] == "") :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe slected")
        else :
            df = cfg.get_dfc_dataframe_df(fparms[0])            
    
            try :
                if(len(htmlparms) > 0) :
                    df.to_html(fparms[1], **htmlparms)
                else :
                    df.to_html(fparms[1])
        
            except Exception as e: 
                opstat.store_exception("Unable to export html file" + fparms[0],e)
    
    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            script      =   ["# Export HTML File ",
                             "dfcleanser.data_export.data_export_control import export_pandas_html",
                             "export_pandas_html(" + json.dumps(fparms) + "," +
                             str(exportId) + "," + json.dumps(labellist) + ",False)"]
                             
            add_to_script(script,opstat)
            
        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms",fparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[0])

    return(opstat)


def process_custom_export(fparms,exportId,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : custom export 
    * 
    * parms :
    *   fparms        -   export parms
    *   exportId      -   export id
    *   display       -   display flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """

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
                             "from dfcleanser.data_export.data_export_control import process_custom_export",
                             "process_custom_export(" + json.dumps(fparms) + "," +
                             str(exportId) + ",False)"]
                             
            add_to_script(script,opstat)
            
        if(len(fparms) > 0) :
            cfg.set_config_value(exportId + "Parms","custom")
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,"custom")

    return(opstat)

       
def export_pandas_sqltable(sqltableparms,dbcondict,exportid,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : export pandas dataframe into sql table 
    * 
    * parms :
    *   sqltableparms    -   export parms
    *   dbcondict        -   db connector dict
    *   exportId         -   export id
    *   display          -   display flag
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
        
        if(len(sqltableparms) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No Export parameters defined")
        
        else :
            
            if(sqltableparms[0] == "") :
                opstat.set_status(False)
                opstat.set_errorMsg("No dataframe selcted to export")
                
            else :
                
                if(sqltableparms[1] == "") :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No tabl;e selcted to export to")
                
                else :
                
                    df = cfg.get_dfc_dataframe_df(sqltableparms[0])            
            
                    labellist   =   dew.pandas_export_sqltable_labelList
            
                    try :

                        sqlkeys         =   [labellist[2],labellist[3],labellist[4],
                                             labellist[5],labellist[6],labellist[7]] 
                        sqlvals         =   [sqltableparms[2],sqltableparms[3],sqltableparms[4],
                                             sqltableparms[5],sqltableparms[6],sqltableparms[7]]
                        sqltypes        =   [STRING_PARM,STRING_PARM,BOOLEAN_PARM,
                                             STRING_PARM,INT_PARM,DICT_PARM]
    
                        sqlparms        =   {}
                        sqladdlparms    =   {}
            
                    except Exception as e:
                        opstat.set_status(False)
                        opstat.store_exception("Error parsing Export parms",e)

                    if(opstat.get_status()) :
        
                        try :
            
                            sqlparms        =   get_function_parms(sqlkeys,sqlvals,sqltypes)
                            if(not (sqltableparms[8] == "")) :
                                sqladdlparms    =   json.loads(sqltableparms[8])
            
                            if (len(sqladdlparms) > 0) :
                                addlparmskeys = sqladdlparms.keys()
                                for i in range(len(addlparmskeys)) : 
                                    sqlparms.update({addlparmskeys[i]:sqladdlparms.get(addlparmskeys[i])})
            
                        except Exception as e:
                            opstat.set_status(False)
                            opstat.store_exception("Error parsing Export additional parms",e)

                        if(opstat.get_status()) :  

                            try :
                            
                                df.to_sql(sqltableparms[1], dbconnector, **sqlparms)
                            #df.to_sql(sqltableparms[1],dbconnector,sqltableparms[2],sqltableparms[3],
                                      #sqltableparms[4],sqltableparms[5],sqltableparms[6],sqltableparms[7])
                
                            except Exception as e:
                                opstat.store_exception("Unable to export to sql table",e)
        
    export_notes    =   ""

    if(opstat.get_status()) : 
        
        if(display) :
            #make scriptable
            add_to_script(["# Export SQL Table ",
                           "from dfcleanser.data_export.data_export_control export export_pandas_sqltable",
                           "export_pandas_sqltable(" + json.dumps(sqltableparms) + "," + 
                           json.dumps(dbcondict) + "," + str(exportid) + ",False)"],opstat)
       
        export_notes    =   dbu.get_SQLAlchemy_connector_string(dbconparms)
        
        if(len(sqltableparms) > 0) :
            cfg.set_config_value(exportid + "Parms",sqltableparms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,sqltableparms[0])

    return(export_notes, opstat)    


def export_test_sql_db_connector(driverid,sqlinputparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : export pandas dataframe into sql table 
    * 
    * parms :
    *   driverid        -   driver id
    *   sqlinputparms   -   connection string
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    try :

        from dfcleanser.common.db_utils import test_db_connector, SQL_EXPORT, NATIVE, SQLALCHEMY
        opstat  =   test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),NATIVE,sqlinputparms,SQL_EXPORT)
        opstat  =   test_db_connector(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),SQLALCHEMY,sqlinputparms,SQL_EXPORT)
            
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
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.DataExport_ID)
    clear_data_export_cfg_values()
    
def clear_data_export_cfg_values() :

    cfg.drop_config_value(cfg.CURRENT_EXPORT_START_TIME)
    
    return(True)



