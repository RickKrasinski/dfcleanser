"""
# data_export_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_export.data_export_model as dem

from dfcleanser.common.html_widgets import (display_composite_form, get_header_form, maketextarea,
                                            get_button_tb_form, get_input_form, displayHeading,
                                            get_html_spaces, ButtonGroupForm, InputForm)

from dfcleanser.common.common_utils import (opStatus, display_exception, 
                                            display_notes, display_status, display_inline_help, get_parms_for_input,
                                            get_formatted_time, display_grid) 

from dfcleanser.common.display_utils import display_df_sizing_info

from dfcleanser.common.db_utils import (parse_connector_parms, get_stored_con_Parms, get_db_connector_list)

from dfcleanser.data_inspection.data_inspection_widgets import (display_inspection_data)

from IPython.display import clear_output

import time

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data export form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   export main taskbar
#--------------------------------------------------------------------------
"""
export_task_bar_doc_title       =   "Export Options"
export_task_bar_title           =   "Export Options"
export_task_bar_id              =   "exportoptions"

export_task_bar_keyTitleList    =   ["Pandas Dataframe","Custom",
                                     "Clear","Help"]

export_task_bar_jsList          =   ["export_taskbar_callback(0)",
                                     "export_taskbar_callback(1)",
                                     "export_taskbar_callback(2)",
                                     "displayhelp(" + str(dfchelp.EXPORT_MAIN_TASKBAR_ID) + ")"]

export_task_bar_centered        =   False

"""
#--------------------------------------------------------------------------
#   pandas export main taskbar
#--------------------------------------------------------------------------
"""
pandas_export_task_bar_doc_title     =  "Pandas Dataframe Export Options"
pandas_export_task_bar_title         =  "Pandas Dataframe Export Options"
pandas_export_task_bar_id            =  "pandasexportdataframe"

pandas_export_task_bar_keyTitleList  =   ["CSV","Excel File","JSON","HTML",
                                          "SQL Table","Return"]

pandas_export_task_bar_jsList        =   ["pandas_export_tb_select_callback("+str(dem.CSV_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.EXCEL_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.JSON_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.HTML_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.SQLTABLE_EXPORT)+")",
                                          "pandas_export_tb_return_callback()"]

pandas_export_task_bar_centered      =   False

"""
#--------------------------------------------------------------------------
#   pandas export csv form parms
#--------------------------------------------------------------------------
"""
pandas_export_csv_title         =   "Pandas CSV Export Parameters"
pandas_export_csv_id            =   "exportPandasCSV"
pandas_export_csv_idList        =   ["ecsvpath",
                                     "ecsvnarep",
                                     "ecsvcolheader","ecsvindex",
                                     "ecsvaddlParms",
                                     None,None,None,None]

pandas_export_csv_labelList     =   ["path_or_buf",
                                     "na_rep",
                                     "header","index",
                                     "Additional Parm(s)",
                                     "Export CSV File","Clear","Return","Help"]

pandas_export_csv_typeList      =   ["file","text","text",
                                     "text",maketextarea(6),
                                     "button","button","button","button"]

pandas_export_csv_placeholderList = ["enter CSV File name or browse to file below",
                                     "enter value to use to fill nans",
                                     "write out column names row to file (default True)",
                                     "write row ids (default True - Infer)",
                                     "enter additional parms { Key :  Value} ... (default None)",
                                     None,None,None,None]

pandas_export_csv_jsList        =   [None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.CSV_EXPORT)+")",
                                     "pandas_details_export_clear_export_callback("+str(dem.CSV_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.CSV_EXPORT_URL)+"')"]

pandas_export_csv_reqList       =   [0]

"""
#--------------------------------------------------------------------------
#   pandas export excel input form components
#--------------------------------------------------------------------------
"""

pandas_export_excel_title       =   "Pandas Excel Export Parameters"
pandas_export_excel_id          =   "exportPandasExcel"

pandas_export_excel_idList      =   ["excelwriter","excelSheetName",
                                     "excelna_rep","excelheader",
                                     "excelindex",
                                     "eexceladdlParms",
                                     None,None,None,None]

pandas_export_excel_labelList   =   ["excel_writer","sheet_name","na_rep",
                                     "header ","index",
                                     "Additional Parm(s)",
                                     "Export Excel File","Clear","Return","Help"]

pandas_export_excel_typeList    =   ["file","text","text",
                                     "text","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_excel_placeholderList = ["enter Excel IO path",
                                       "enter sheet name",
                                       "enter nan value (default '')",
                                       "write out column names row to file (default True)",
                                       "write row ids (default True - Infer)",
                                       "enter additional parms { Key :  Value} ... (default None)",
                                       None,None,None,None]

pandas_export_excel_jsList      =   [None,None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.EXCEL_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.EXCEL_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.EXCEL_EXPORT_URL)+"')"]

pandas_export_excel_reqList     =   [0]

"""
#--------------------------------------------------------------------------
#   pandas import json input form components
#--------------------------------------------------------------------------
"""

pandas_export_json_title        =   "Pandas JSON Export Parameters"
pandas_export_json_id           =   "exportPandasJSON"

pandas_export_json_idList       =   ["jsonPath","jsonOrient",
                                     "jsondateformat",
                                     "ejsonaddlParmsl",
                                     None,None,None,None]

pandas_export_json_labelList    =   ["path_or_buf","orient",
                                     "date_format",
                                     "Additional Parm(s)",
                                     "Export JSON File","Clear","Return","Help"]

pandas_export_json_typeList     =   ["file","text","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_json_placeholderList = ["enter JSON path or browse to file ",
                                      "enter JSON orientation",
                                      "enter date-format (default iso)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_json_jsList       =   [None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.JSON_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.JSON_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.JSON_EXPORT_URL)+"')"]

pandas_export_json_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#   pandas import html input form components
#--------------------------------------------------------------------------
"""

pandas_export_html_title        =   "Pandas HTML Export Parameters"
pandas_export_html_id           =   "exportPandasHTML"

pandas_export_html_idList       =   ["exhtmlPath","excolspace",
                                     "exhtmlheader",
                                     "exhtmlColNamesRow",
                                     "exhtmlRowIndexColumn",
                                     "exhtmladdlParms",
                                     None,None,None,None]

pandas_export_html_labelList    =   ["io","col_space",
                                     "header",
                                     "index","na_rep",
                                     "Additional Parm(s)",
                                     "Export HTML File","Clear","Return","Help"]

pandas_export_html_typeList     =   ["file","text","text",
                                     "text","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_html_placeholderList = ["enter HTML path or browse to file ",
                                      "minimum col width (default 1)",
                                      "whether to print column names (default True)",
                                      "whether to print row ids (default True)",
                                      "string representation of NAN to use (default NaN)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_html_jsList       =   [None,None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.HTML_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.HTML_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.HTML_EXPORT_URL)+"')"]

pandas_export_html_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#   pandas export sqltable input form components
#--------------------------------------------------------------------------
"""

pandas_export_sqltable_title        =   "Pandas SQL Table Export Parameters"
pandas_export_sqltable_id           =   "exportPandasSQLTable"

pandas_export_sqltable_idList       =    ["exportsqltableName",
                                          "exportsqltableflavor",
                                          "exportsqltableschema",
                                          "exportsqltableexists",
                                          "exportsqltableindex",
                                          "exportsqltableindexlabel",
                                          "exportsqltablechunksize",
                                          "exportsqltabledtype",
                                          None,None,None,None,None,None]

pandas_export_sqltable_labelList    =   ["table_name",
                                         "flavor",
                                         "schema",
                                         "if_exists",
                                         "index",
                                         "index_label",
                                         "chunksize",
                                         "dtype",
                                         "Get</br>Tables",
                                         "Get</br>Columns",
                                         "Export</br>Table",
                                         "Clear","Return","Help"]

pandas_export_sqltable_typeList     =   ["text","text","text","text",
                                         "text","text","text","text",
                                         "button","button","button","button","button","button"]

pandas_export_sqltable_placeholderList = ["enter the table name",
                                          "‘sqlite’, default None",
                                          "specify the schema (if database flavor supports this). If None, use default schema.",
                                          "{‘fail’, ‘replace’, ‘append’}, (default ‘fail’)",
                                          "write DataFrame index as a column (default None)",
                                          "column label for index column(s) (default None)",
                                          "number of rows (default None)",
                                          "dict of column name to SQL type, (default None)",
                                          None,None,None,None,None,None]

pandas_export_sqltable_jsList       =   [None,None,None,None,None,None,None,None,
                                         "pandas_export_sql_callback(0)",
                                         "pandas_export_sql_callback(1)",
                                         "pandas_export_sql_callback(2)",
                                         "pandas_details_export_clear_callback("+str(dem.SQLTABLE_EXPORT)+")",
                                         "pandas_details_export_return_callback()",
                                         "display_help_url('"+str(dfchelp.SQLTABLE_EXPORT_URL)+"')"]

pandas_export_sqltable_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#   Custom Export input form parm lists
#--------------------------------------------------------------------------
"""
custom_export_title             =   "Custom Export Code"
custom_export_id                =   "customExport"

custom_export_idList            =   ["customExportCode",None,None,None,None,None,None]

custom_export_labelList         =   ["Custom Export Code",
                                     "New </br>Custom </br>Export",
                                     "Run </br>Custom </br>Export",
                                     "Save </br>Custom </br>Export",
                                     "Drop </br>Custom </br>Export",
                                     "Return","Help"]

custom_export_typeList          =   [maketextarea(8),"button","button","button","button","button","button"]

custom_export_placeholderList   =   ["# custom export",None,None,None,None,None,None]
                                     
custom_export_jsList            =   [None,
                                     "custom_export_callback(0)",
                                     "custom_export_callback(1)",
                                     "custom_export_callback(2)",
                                     "custom_export_callback(3)",
                                     "custom_export_callback(4)",
                                     "displayhelp"+str(dfchelp.EXPORT_CUSTOM_ID)+")"]

custom_export_reqList           =   [0]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display export helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_export_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(export_task_bar_id,
                                                               export_task_bar_keyTitleList,
                                                               export_task_bar_jsList,
                                                               export_task_bar_centered))])

def get_csv_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_csv_idList))
def get_csv_export_form_id() :
    return(pandas_export_csv_id)
def get_csv_export_form_labels() :
    return(pandas_export_csv_labelList)

def get_excel_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_excel_idList))
def get_excel_export_form_id() :
    return(pandas_export_excel_id)
def get_excel_export_form_labels() :
    return(pandas_export_excel_labelList)

def get_json_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_json_idList))
def get_json_export_form_id() :
    return(pandas_export_json_id)
def get_json_export_form_labels() :
    return(pandas_export_json_labelList)

def get_html_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_html_idList))
def get_html_export_form_id() :
    return(pandas_export_html_id)
def get_html_export_form_labels() :
    return(pandas_export_html_labelList)

def get_custom_export_form_id() :
    return(custom_export_id)
def get_custom_export_form_labels() :
    return(custom_export_labelList)

def get_sqltable_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_sqltable_idList))
def get_sqltable_export_form_id() :
    return(pandas_export_sqltable_id)
def get_sqltable_export_form_labels() :
    return(pandas_export_sqltable_labelList)
   



"""
#------------------------------------------------------------------
#   display data export notes 
#
#   s       -   start of import
#   fname   -   name of file imported
#
#------------------------------------------------------------------
"""
def display_data_export_notes(s,fname,dbnote=False,custom=False) :

    displayHeading("Data Exported",4)
        
    display_df_sizing_info(cfg.get_dc_dataframe())
    print("\n")
    
    if(custom) :
        display_status("Custom export code Exported successfully")
        
        importnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds",
                       "( set dataframe via dfcleanser.common.cfg.set_dc_dataframe(df) )",
                       "( check if df exists via dfcleanser.common.cfg.is_dc_dataframe_loaded() )"]
        
    else :
        
        if(dbnote) :
            display_status(" Dataframe Exported successfully to table " + fname)
        else :    
            display_status(" Dataframe Exported successfully to File " + fname)

        importnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds",
                       "( get dataframe via dfcleanser.common.cfg.get_dc_dataframe() )",
                       "( set dataframe via dfcleanser.common.cfg.set_dc_dataframe(df) )",
                       "( check if df exists via dfcleanser.common.cfg.is_dc_dataframe_loaded() )"]
    
    display_notes(importnotes)


"""
#------------------------------------------------------------------
#   get pandas export input form  
#
#   id      -   export type
#
#------------------------------------------------------------------
"""
def get_pandas_export_input_form(exid) :
 
    if(exid == dem.CSV_EXPORT)      : 
        export_form = InputForm(pandas_export_csv_id,
                                pandas_export_csv_idList,
                                pandas_export_csv_labelList,
                                pandas_export_csv_typeList,
                                pandas_export_csv_placeholderList,
                                pandas_export_csv_jsList,
                                pandas_export_csv_reqList)
        
    elif(exid == dem.EXCEL_EXPORT)    : 
         export_form = InputForm(pandas_export_excel_id,
                                 pandas_export_excel_idList,
                                 pandas_export_excel_labelList,
                                 pandas_export_excel_typeList,
                                 pandas_export_excel_placeholderList,
                                 pandas_export_excel_jsList,
                                 pandas_export_excel_reqList)    

    elif(exid == dem.JSON_EXPORT)    : 
         export_form = InputForm(pandas_export_json_id,
                                 pandas_export_json_idList,
                                 pandas_export_json_labelList,
                                 pandas_export_json_typeList,
                                 pandas_export_json_placeholderList,
                                 pandas_export_json_jsList,
                                 pandas_export_json_reqList)    
    
    elif(exid == dem.HTML_EXPORT)    : 
         export_form = InputForm(pandas_export_html_id,
                                 pandas_export_html_idList,
                                 pandas_export_html_labelList,
                                 pandas_export_html_typeList,
                                 pandas_export_html_placeholderList,
                                 pandas_export_html_jsList,
                                 pandas_export_html_reqList)    
    
    elif(exid == dem.SQLTABLE_EXPORT)    : 
         export_form = InputForm(pandas_export_sqltable_id,
                                 pandas_export_sqltable_idList,
                                 pandas_export_sqltable_labelList,
                                 pandas_export_sqltable_typeList,
                                 pandas_export_sqltable_placeholderList,
                                 pandas_export_sqltable_jsList,
                                 pandas_export_sqltable_reqList)    
       
    return(export_form)

"""
#------------------------------------------------------------------
#   get pandas export input form title 
#
#   id      -   export type
#
#------------------------------------------------------------------
"""
def get_pandas_export_input_title(id,dbid=None) :
    
    if(dbid == None) :
        pandas_title = {dem.CSV_EXPORT      : pandas_export_csv_title,
                        dem.EXCEL_EXPORT    : pandas_export_excel_title,
                        dem.JSON_EXPORT     : pandas_export_json_title,
                        dem.HTML_EXPORT     : pandas_export_html_title,
                        dem.SQLTABLE_EXPORT : pandas_export_sqltable_title} 
        
        return(pandas_title[id])
    else :
        
        import dfcleanser.common.db_utils as dbutils
        if(dbid == dbutils.MySql) :
            return(pandas_export_sqltable_title + " - " + "MySQL")
        if(dbid == dbutils.MS_SQL_Server) :
            return(pandas_export_sqltable_title + " - " + "MS SQL Server")
        if(dbid == dbutils.SQLite) :
            return(pandas_export_sqltable_title + " - " + "SQLite")
        if(dbid == dbutils.Postgresql) :
            return(pandas_export_sqltable_title + " - " + "Postgresql")
        if(dbid == dbutils.Oracle) :
            return(pandas_export_sqltable_title + " - " + "Oracle")
        else :
            return(pandas_export_sqltable_title)
                

"""
#------------------------------------------------------------------
#   display pandas export input form title 
#
#   id      -   export type
#
#------------------------------------------------------------------
"""
def display_dc_export_forms(id, detid=0, notes=False) :
    
    clear_output()

    # add the main import task bar
    if (id == dem.EXPORT_TB_ONLY) :

        display_composite_form([get_button_tb_form(ButtonGroupForm(export_task_bar_id,
                                                                   export_task_bar_keyTitleList,
                                                                   export_task_bar_jsList,
                                                                   export_task_bar_centered)),
                                get_header_form("&nbsp;&nbsp;&nbsp;Data")])
    
        display_inspection_data() 
        
        dfchelp.clear_help_text(dfchelp.EXPORT_HELP_BASE)

    # add the pandas import task bar or pandas details form 
    elif ( (id == dem.EXPORT_PANDAS_TB_ONLY) or 
           (id == dem.EXPORT_PANDAS_TB_PLUS_DETAILS) ) :
        
        if(not (cfg.is_dc_dataframe_loaded())) :
            
            display_composite_form([get_button_tb_form(ButtonGroupForm(export_task_bar_id,
                                                                       export_task_bar_keyTitleList,
                                                                       export_task_bar_jsList,
                                                                       export_task_bar_centered)),
                                    get_header_form("&nbsp;&nbsp;&nbsp;Data")])
    
            display_inspection_data() 

        else :
            
            # add the pandas import details form 
            if (id == dem.EXPORT_PANDAS_TB_PLUS_DETAILS) :
                
                if(detid==dem.SQLTABLE_EXPORT):
                    
                    import dfcleanser.common.db_utils as dbutils
                 
                    cfg.drop_config_value(pandas_export_sqltable_id + "Parms")
                
                    dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
                
                    if(dbid == None)                        :   
                        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.MySql)
                        conparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
                        if(conparms == None) : conparms = ["","","","",dbutils.pymysql_library]

                    elif(dbid == dbutils.MySql)             :   
                        conparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
                        if(conparms == None) : conparms = ["","","","",dbutils.pymysql_library]
                        
                    elif(dbid == dbutils.MS_SQL_Server)     :   
                        conparms = cfg.get_config_value(dbutils.MSSQL_DBCON_PARMS)
                        if(conparms == None) : conparms = ["","","","",dbutils.pyodbc_library]
                    
                    elif(dbid == dbutils.SQLite)            :   
                        conparms = cfg.get_config_value(dbutils.SQLITE_DBCON_PARMS)
                        if(conparms == None) :conparms =  ["",dbutils.sqlite3_library]
                    
                    elif(dbid == dbutils.Postgresql)        :   
                        conparms = cfg.get_config_value(dbutils.POSTGRESQL_DBCON_PARMS)
                        if(conparms == None) : conparms = ["","","","",dbutils.psycopg2_library]
                    
                    elif(dbid == dbutils.Oracle)            :   
                        conparms = cfg.get_config_value(dbutils.ORACLE_DBCON_PARMS)
                        if(conparms == None) : conparms = ["","","",dbutils.cx_oracle_library]
                    
                    elif(dbid == dbutils.Custom)            :   
                        conparms = cfg.get_config_value(dbutils.CUSTOM_DBCON_PARMS)
                        if(conparms == None) : conparms = [""]

                    dbutils.display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),conparms,dbutils.SQL_EXPORT) 
                
                else :
            
                    # display the composite form
                    display_composite_form([get_input_form(get_pandas_export_input_form(detid),
                                                           get_pandas_export_input_title(detid))])
            else :
                
                # display the composite form
                display_composite_form([get_button_tb_form(ButtonGroupForm(pandas_export_task_bar_id,
                                                                           pandas_export_task_bar_keyTitleList,
                                                                           pandas_export_task_bar_jsList,
                                                                           pandas_export_task_bar_centered))])
                
    else :
        
        if(not (cfg.is_dc_dataframe_loaded())) :
            
            display_composite_form([get_button_tb_form(ButtonGroupForm(export_task_bar_id,
                                                                       export_task_bar_keyTitleList,
                                                                       export_task_bar_jsList,
                                                                       export_task_bar_centered)),
                                    get_header_form("&nbsp;&nbsp;&nbsp;Data")])
    
            display_inspection_data() 
            
        else : 
            
            # add the custom import form 
            exportCustomDetailsForm     =   get_input_form(InputForm(custom_export_id,
                                                                     custom_export_idList,
                                                                     custom_export_labelList,
                                                                     custom_export_typeList,
                                                                     custom_export_placeholderList,
                                                                     custom_export_jsList,
                                                                     custom_export_reqList))

            if(notes) :
                customNotes =  ["To create custom export code in the code cell below hit 'New Custom Export'",
                                "&nbsp;&nbsp;&nbsp;&nbsp;(enter and test export in the code cell below)",
                                "&nbsp;&nbsp;&nbsp;&nbsp;(leave the '# custom export' comment line in the code cell",
                                "&nbsp;&nbsp;&nbsp;&nbsp;(call dfcleanser.common.cfg.get_dc_dataframe() to get the current dataframe)",
                                "To run the export code in the Custom Export Code box hit 'Run Custom Export' button",
                                "&nbsp;&nbsp;&nbsp;&nbsp;(only the code in the Custom Export Code box is run and stored for scripting)",                        "Once import successful hit 'Save Custom Import' button to store import code for future retrieval",
                                "To drop the custom export code and clear the Custom Export Code box hit 'Drop Custom Export' button"]
            
                print("\n")
                display_inline_help(customNotes,92)
        
            # display the composite form
            display_composite_form([exportCustomDetailsForm])

"""
#------------------------------------------------------------------
#   display pandas sql export form 
#
#------------------------------------------------------------------
"""
def display_dc_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms=None) :
    
    opstat          =   opStatus()
    opstatStatus    =   True
    listHtml        =   ""
    dbid            =   int(dbId)
    fid             =   int(fId)
    fparms          =   None
    
    if(fid == 0) :
           
        dbid        =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
        from dfcleanser.data_import.data_import_widgets import (get_table_names, TABLE_NAMES, get_rows_html) 
        tablelist   =   get_table_names(dbid,opstat)
        listHtml    =   get_rows_html(tablelist,TABLE_NAMES,True)
        
    elif(fid == 1)  : 
        
        fparms  =   get_parms_for_input(exportparms,pandas_export_sqltable_idList)
        dbid    =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
        cfg.set_config_value(pandas_export_sqltable_id+"Parms",fparms)

        if(len(fparms[0]) > 0) :
            from dfcleanser.data_import.data_import_widgets import (get_column_names, COLUMN_NAMES, get_rows_html)
            columnlist  =   get_column_names(dbid,fparms[0],opstat)
            listHtml    =   get_rows_html(columnlist,COLUMN_NAMES,True)
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("No Table Selected")

    elif(fid == 2)  : 
    
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbid)
    
        dbcondict = {}
        if(not (dbconparms == None) ) :
            parse_connector_parms(dbconparms,dbid,dbcondict)
        else :
            conparms = get_stored_con_Parms(dbid)        
            parse_connector_parms(conparms,dbid,dbcondict)
            
        listHtml = get_db_connector_list(dbid,dbcondict)
        
    if(not (opstat.get_status() )) :
        dbcondict = {}
        conparms = get_stored_con_Parms(dbid)        
        parse_connector_parms(conparms,dbid,dbcondict)
            
        listHtml = get_db_connector_list(dbid,dbcondict)
        
        opstatStatus    =   opstat.get_status()
        opstatErrormsg  =   opstat.get_errorMsg()
        opstat.set_status(True)
        
    if(opstat.get_status()) :
    
        export_sql_input_form = InputForm(pandas_export_sqltable_id,
                                          pandas_export_sqltable_idList,
                                          pandas_export_sqltable_labelList,
                                          pandas_export_sqltable_typeList,
                                          pandas_export_sqltable_placeholderList,
                                          pandas_export_sqltable_jsList,
                                          pandas_export_sqltable_reqList,
                                          shortForm=False)
        
        export_sql_input_form.set_gridwidth(700)

        export_sql_input_html = ""
        export_sql_input_html = export_sql_input_form.get_html()
        
        export_sql_heading_html = "<h4>" + get_html_spaces(12) + get_pandas_export_input_title(dem.SQLTABLE_EXPORT,dbid) + "</h4>"

        if( not (exportparms == None) ) :
            cfg.set_config_value(pandas_export_sqltable_id+"Parms",fparms)
    

        display_grid("export_sql_table_wrapper",
                     export_sql_heading_html,
                     listHtml,
                     export_sql_input_html,
                     None)
    
    if( not (opstatStatus)) :
        opstat.set_status(opstatStatus)
        opstat.set_errorMsg(opstatErrormsg)
        display_exception(opstat)


