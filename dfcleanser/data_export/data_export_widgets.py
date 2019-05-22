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

from dfcleanser.common.html_widgets import (display_composite_form, maketextarea,
                                            get_input_form, 
                                            ButtonGroupForm, InputForm)

from dfcleanser.common.common_utils import (opStatus, display_exception, 
                                            display_notes, display_status, display_inline_help, get_parms_for_input,
                                            get_formatted_time, display_generic_grid, get_select_defaults) 

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

export_task_bar_keyTitleList    =   ["Pandas</br>Dataframe","Custom",
                                     "Clear","Reset","Help"]

export_task_bar_jsList          =   ["export_taskbar_callback(0)",
                                     "export_taskbar_callback(1)",
                                     "export_taskbar_callback(2)",
                                     "process_pop_up_cmd(6)",
                                     "displayhelp(" + str(dfchelp.EXPORT_MAIN_TASKBAR_ID) + ")"]

export_task_bar_centered        =   False

export_task_bar_pu_keyTitleList =   ["Pandas</br>Dataframe","Custom",
                                     "Clear","Reset","Help"]

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

pandas_export_task_bar_centered      =   True

pandas_export_task_bar_pu_doc_title     =  "Pandas Dataframe Export Options"
pandas_export_task_bar_pu_title         =  "Pandas Dataframe Export Options"
pandas_export_task_bar_pu_id            =  "pandasexportdataframe"

pandas_export_task_bar_pu_keyTitleList  =   ["CSV","Excel</br>File","JSON","HTML",
                                          "SQL</br>Table","Return"]

pandas_export_task_bar_pu_jsList        =   ["pandas_export_tb_select_callback("+str(dem.CSV_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.EXCEL_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.JSON_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.HTML_EXPORT)+")",
                                          "pandas_export_tb_select_callback("+str(dem.SQLTABLE_EXPORT)+")",
                                          "pandas_export_tb_return_callback()"]

pandas_export_task_bar_pu_centered      =   True


"""
#--------------------------------------------------------------------------
#   pandas export csv form parms
#--------------------------------------------------------------------------
"""
pandas_export_csv_title         =   "Pandas CSV Export Parameters"
pandas_export_csv_id            =   "exportPandasCSV"
pandas_export_csv_idList        =   ["ecsvdataframe",
                                     "ecsvpath",
                                     "ecsvnarep",
                                     "ecsvcolheader",
                                     "ecsvindex",
                                     "ecsvaddlParms",
                                     None,None,None,None]

pandas_export_csv_labelList     =   ["dataframe_to_export",
                                     "path_or_buf",
                                     "na_rep",
                                     "header","index",
                                     "Additional Parm(s)",
                                     "Export</br>CSV File","Clear","Return","Help"]

pandas_export_csv_typeList      =   ["select","file","text","select",
                                     "select",maketextarea(6),
                                     "button","button","button","button"]

pandas_export_csv_placeholderList = ["select dataframe to export",
                                     "enter CSV File name or browse to file below",
                                     "string representation of NAN to use (default NaN)",
                                     "write out column names row to file (default True)",
                                     "write row ids (default True)",
                                     "enter additional parms as dict { Key :  Value} ... (default None)",
                                     None,None,None,None]

pandas_export_csv_jsList        =   [None,None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.CSV_EXPORT)+")",
                                     "pandas_details_export_clear_export_callback("+str(dem.CSV_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.CSV_EXPORT_URL)+"')"]

pandas_export_csv_reqList       =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas export excel input form components
#--------------------------------------------------------------------------
"""

pandas_export_excel_title       =   "Pandas Excel Export Parameters"
pandas_export_excel_id          =   "exportPandasExcel"

pandas_export_excel_idList      =   ["exceldataframe",
                                     "excelwriter",
                                     "excelSheetName",
                                     "excelna_rep",
                                     "excelheader",
                                     "excelindex",
                                     "eexceladdlParms",
                                     None,None,None,None]

pandas_export_excel_labelList   =   ["dataframe_to_export",
                                     "excel_writer",
                                     "sheet_name",
                                     "na_rep",
                                     "header ",
                                     "index",
                                     "Additional Parm(s)",
                                     "Export</br>Excel File","Clear","Return","Help"]

pandas_export_excel_typeList    =   ["select","file","text","text",
                                     "select","select",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_excel_placeholderList = ["select dataframe to export",
                                       "enter Excel IO path",
                                       "enter sheet name",
                                       "string representation of NAN to use (default NaN)",
                                       "write out column names row to file (default True)",
                                       "write row ids (default True)",
                                       "enter additional parms as dict { Key :  Value} ... (default None)",
                                       None,None,None,None]

pandas_export_excel_jsList      =   [None,None,None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.EXCEL_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.EXCEL_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.EXCEL_EXPORT_URL)+"')"]

pandas_export_excel_reqList     =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import json input form components
#--------------------------------------------------------------------------
"""

pandas_export_json_title        =   "Pandas JSON Export Parameters"
pandas_export_json_id           =   "exportPandasJSON"

pandas_export_json_idList       =   ["jsondataframe",
                                     "jsonPath",
                                     "jsonOrient",
                                     "jsondateformat",
                                     "ejsonaddlParmsl",
                                     None,None,None,None]

pandas_export_json_labelList    =   ["dataframe_to_export",
                                     "path_or_buf",
                                     "orient",
                                     "date_format",
                                     "Additional Parm(s)",
                                     "Export</br>JSON File","Clear","Return","Help"]

pandas_export_json_typeList     =   ["select","file","text","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_json_placeholderList = ["select dataframe to export",
                                      "enter JSON path or browse to file ",
                                      "enter JSON orientation",
                                      "enter date-format (default iso)",
                                      "enter additional parms as dict { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_json_jsList       =   [None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.JSON_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.JSON_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.JSON_EXPORT_URL)+"')"]

pandas_export_json_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import html input form components
#--------------------------------------------------------------------------
"""

pandas_export_html_title        =   "Pandas HTML Export Parameters"
pandas_export_html_id           =   "exportPandasHTML"

pandas_export_html_idList       =   ["exhtmldataframe",
                                     "exhtmlPath",
                                     "excolspace",
                                     "exhtmlheader",
                                     "exhtmlColNamesRow",
                                     "exhtmlRowIndexColumn",
                                     "exhtmladdlParms",
                                     None,None,None,None]

pandas_export_html_labelList    =   ["dataframe_to_export",
                                     "io",
                                     "col_space",
                                     "header",
                                     "index",
                                     "na_rep",
                                     "Additional Parm(s)",
                                     "Export</br>HTML File","Clear","Return","Help"]

pandas_export_html_typeList     =   ["select","file","text","select",
                                     "select","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_export_html_placeholderList = ["select dataframe to export",
                                      "enter HTML path or browse to file ",
                                      "minimum col width (default 1)",
                                      "whether to print column names (default True)",
                                      "whether to print row ids (default True)",
                                      "string representation of NAN to use (default NaN)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_html_jsList       =   [None,None,None,None,None,None,None,
                                     "pandas_details_export_callback("+str(dem.HTML_EXPORT)+")",
                                     "pandas_details_export_clear_callback("+str(dem.HTML_EXPORT)+")",
                                     "pandas_details_export_return_callback()",
                                     "display_help_url('"+str(dfchelp.HTML_EXPORT_URL)+"')"]

pandas_export_html_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas export sqltable input form components
#--------------------------------------------------------------------------
"""

pandas_export_sqltable_title        =   "Pandas SQL Table Export Parameters"
pandas_export_sqltable_id           =   "exportPandasSQLTable"

pandas_export_sqltable_idList       =    ["exportsqldataframe",
                                          "exportsqltableName",
                                          "exportsqltableschema",
                                          "exportsqltableexists",
                                          "exportsqltableindex",
                                          "exportsqltableindexlabel",
                                          "exportsqltablechunksize",
                                          "exportsqltabledtype",
                                          "exportsqltableaddlParms",
                                          None,None,None,None,None]

pandas_export_sqltable_labelList    =   ["dataframe_to_export",
                                         "table_name",
                                         "schema",
                                         "if_exists",
                                         "index",
                                         "index_label",
                                         "chunksize",
                                         "dtype",
                                         "Additional Parm(s)",
                                         "Export</br>Table",
                                         "Get</br>Columns",
                                         "Clear","Return","Help"]

pandas_export_sqltable_typeList     =   ["select","text","text","select",
                                         "select","text","text","text",maketextarea(4),
                                         "button","button","button","button","button"]

pandas_export_sqltable_placeholderList = ["select dataframe to export",
                                          "enter the table name",
                                          "specify the schema (if database flavor supports this). If None, use default schema.",
                                          "{‘fail’, ‘replace’, ‘append’}, (default ‘fail’)",
                                          "write DataFrame index as a column (default None)",
                                          "column label for index column(s) (default None)",
                                          "number of rows (default None)",
                                          "dict of column name to SQL type, (default None)",
                                          "enter additional parms { Key :  Value} ... (default None)",
                                          None,None,None,None,None]

pandas_export_sqltable_jsList       =   [None,None,None,None,None,None,None,None,None,
                                         "pandas_export_sql_callback(2)",
                                         "pandas_export_sql_callback(1)",
                                         "pandas_details_export_clear_callback("+str(dem.SQLTABLE_EXPORT)+")",
                                         "pandas_details_export_return_callback()",
                                         "display_help_url('"+str(dfchelp.SQLTABLE_EXPORT_URL)+"')"]

pandas_export_sqltable_reqList      =   [0,1]

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
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_dfcleanser_taskbar(ButtonGroupForm(export_task_bar_id,
                                                   export_task_bar_keyTitleList,
                                                   export_task_bar_jsList,
                                                   export_task_bar_centered))
    else :
        display_dfcleanser_taskbar(ButtonGroupForm(export_task_bar_id,
                                                   export_task_bar_pu_keyTitleList,
                                                   export_task_bar_jsList,
                                                   export_task_bar_centered))


def display_pandas_export_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_dfcleanser_taskbar(ButtonGroupForm(pandas_export_task_bar_id,
                                                   pandas_export_task_bar_keyTitleList,
                                                   pandas_export_task_bar_jsList,
                                                   pandas_export_task_bar_centered))
    else :
        display_dfcleanser_taskbar(ButtonGroupForm(pandas_export_task_bar_pu_id,
                                                   pandas_export_task_bar_pu_keyTitleList,
                                                   pandas_export_task_bar_pu_jsList,
                                                   pandas_export_task_bar_pu_centered))


def display_data_select_df() :
    
        from dfcleanser.data_inspection.data_inspection_widgets import get_select_df_form
        select_df_form              =   get_select_df_form("Export")
    
        gridclasses     =   ["dfc-footer"]
        gridhtmls       =   [select_df_form.get_html()]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)
    

def get_csv_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_csv_idList))

def get_excel_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_excel_idList))

def get_json_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_json_idList))

def get_html_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_html_idList))

def get_sqltable_export_inputs(parms) :
    return(get_parms_for_input(parms,pandas_export_sqltable_idList))
   

def display_export_dc_sql_details_forms(dblibid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display export sql form
    * 
    * parms :
    *   dblibid   -   db loib id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import dfcleanser.common.db_utils as dbutils
    
    if(dblibid == None) :
        cfg.drop_config_value(cfg.CURRENT_DB_ID_KEY) 
        
    if((dblibid == dbutils.pymysql_library) or (dblibid == dbutils.mysql_connector_library)) :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.MySql)
    elif((dblibid == dbutils.pyodbc_library) or (dblibid == dbutils.pymssql_library)) :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.MS_SQL_Server)
    elif((dblibid == dbutils.sqlite_library) or (dblibid == dbutils.sqlite3_library)) :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.SQLite)
    elif(dblibid == dbutils.psycopg2_library) :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.Postgresql)
    elif(dblibid == dbutils.cx_oracle_library) :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.Oracle)
    elif(dblibid == "custom") :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.Custom)
        
    dbid =  cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
    
    if(dbid == None) :
        inparms = cfg.get_config_value(cfg.MYSQL_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    if(dbid == dbutils.MySql) :
        inparms = cfg.get_config_value(cfg.MYSQL_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.MS_SQL_Server) :
        inparms = cfg.get_config_value(cfg.MSSQL_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.Postgresql) :
        inparms = cfg.get_config_value(cfg.POSTGRESQL_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.SQLite) :
        inparms = cfg.get_config_value(cfg.SQLITE_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["",dblibid]
        else :
            inparms[1] = dblibid
            
    elif(dbid == dbutils.Oracle) :
        inparms = cfg.get_config_value(cfg.ORACLE_IMPORT_PARMS_KEY)
        if(inparms == None) :
            inparms = ["","","",dblibid]
        else :
            inparms[1] = dblibid
                
    elif(dbid == dbutils.Custom) :
        inparms = cfg.get_config_value(cfg.CUSTOM_IMPORT_PARMS_KEY)
        
    from dfcleanser.common.db_utils import display_db_connector_inputs, SQL_EXPORT
    display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms,SQL_EXPORT) 
        

def display_data_export_notes(s,fname,dbnote=False,custom=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display data export notes
    * 
    * parms :
    *   s       -   start of import
    *   fname   -   name of table exported to
    *   dbnote  -   db note
    *   custom  -   custom export flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(custom) :
        display_status("Custom export code Exported successfully")
        
        importnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds",
                       "( set dataframe via dfcleanser.common.cfg.set_current_dfc_dataframe(df) )",
                       "( check if df exists via dfcleanser.common.cfg.is_a_dfc_dataframe_loaded() )"]
        
    else :
        
        if(dbnote) :
            display_status(" Dataframe Exported successfully to table " + fname)
        else :    
            display_status(" Dataframe Exported successfully to File " + fname)

        importnotes = ["[Total Export Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds"]
    
    display_notes(importnotes)


def get_pandas_export_input_form(exid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get pandas export input form
    * 
    * parms :
    *   exid    -   export type
    *
    * returns : N/A
    * --------------------------------------------------------
    """
 
    selectDicts     =   []
    
    if(exid == dem.CSV_EXPORT)      : 
        export_form = InputForm(pandas_export_csv_id,
                                pandas_export_csv_idList,
                                pandas_export_csv_labelList,
                                pandas_export_csv_typeList,
                                pandas_export_csv_placeholderList,
                                pandas_export_csv_jsList,
                                pandas_export_csv_reqList)
        
        dataframes      =   cfg.get_dfc_dataframes_select_list()
        selectDicts.append(dataframes)

        boolFlag        =   {"default":"True","list":["True","False"]}
        selectDicts.append(boolFlag)
        selectDicts.append(boolFlag)
        
        get_select_defaults(export_form,
                            pandas_export_csv_id,
                            pandas_export_csv_idList,
                            pandas_export_csv_typeList,
                            selectDicts)
        
    elif(exid == dem.EXCEL_EXPORT)    : 
        export_form = InputForm(pandas_export_excel_id,
                                 pandas_export_excel_idList,
                                 pandas_export_excel_labelList,
                                 pandas_export_excel_typeList,
                                 pandas_export_excel_placeholderList,
                                 pandas_export_excel_jsList,
                                 pandas_export_excel_reqList)
        
        dataframes      =   cfg.get_dfc_dataframes_select_list()
        selectDicts.append(dataframes)

        boolFlag        =   {"default":"True","list":["True","False"]}
        selectDicts.append(boolFlag)
        selectDicts.append(boolFlag)
        
        get_select_defaults(export_form,
                            pandas_export_excel_id,
                            pandas_export_excel_idList,
                            pandas_export_excel_typeList,
                            selectDicts)

    elif(exid == dem.JSON_EXPORT)    : 
         export_form = InputForm(pandas_export_json_id,
                                 pandas_export_json_idList,
                                 pandas_export_json_labelList,
                                 pandas_export_json_typeList,
                                 pandas_export_json_placeholderList,
                                 pandas_export_json_jsList,
                                 pandas_export_json_reqList)
         
         dataframes      =   cfg.get_dfc_dataframes_select_list()
         selectDicts.append(dataframes)
        
         get_select_defaults(export_form,
                            pandas_export_json_id,
                            pandas_export_json_idList,
                            pandas_export_json_typeList,
                            selectDicts)
    
    elif(exid == dem.HTML_EXPORT)    : 
        export_form = InputForm(pandas_export_html_id,
                                 pandas_export_html_idList,
                                 pandas_export_html_labelList,
                                 pandas_export_html_typeList,
                                 pandas_export_html_placeholderList,
                                 pandas_export_html_jsList,
                                 pandas_export_html_reqList)    
        
        dataframes      =   cfg.get_dfc_dataframes_select_list()
        selectDicts.append(dataframes)

        boolFlag        =   {"default":"True","list":["True","False"]}
        selectDicts.append(boolFlag)
        selectDicts.append(boolFlag)
        
        get_select_defaults(export_form,
                            pandas_export_html_id,
                            pandas_export_html_idList,
                            pandas_export_html_typeList,
                            selectDicts)

    elif(exid == dem.SQLTABLE_EXPORT)    : 
         export_form = InputForm(pandas_export_sqltable_id,
                                 pandas_export_sqltable_idList,
                                 pandas_export_sqltable_labelList,
                                 pandas_export_sqltable_typeList,
                                 pandas_export_sqltable_placeholderList,
                                 pandas_export_sqltable_jsList,
                                 pandas_export_sqltable_reqList)
         
         dataframes      =   cfg.get_dfc_dataframes_select_list()
         selectDicts.append(dataframes)
         
         ifexists        =   {"default":"fail","list":["fail","replace","append"]}
         selectDicts.append(ifexists)
         
         index           =   {"default":"True","list":["True","False"]}
         selectDicts.append(index)
         
        
         get_select_defaults(export_form,
                            pandas_export_sqltable_id,
                            pandas_export_sqltable_idList,
                            pandas_export_sqltable_typeList,
                            selectDicts)

       
    return(export_form)


def get_pandas_export_input_title(exid,dbid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get pandas export input form title
    * 
    * parms :
    *   exid    -   export type
    *   dbid    -   db lib id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(dbid == None) :
        pandas_title = {dem.CSV_EXPORT      : pandas_export_csv_title,
                        dem.EXCEL_EXPORT    : pandas_export_excel_title,
                        dem.JSON_EXPORT     : pandas_export_json_title,
                        dem.HTML_EXPORT     : pandas_export_html_title,
                        dem.SQLTABLE_EXPORT : pandas_export_sqltable_title} 
        
        return(pandas_title[exid])
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
                

def display_dc_export_forms(exid, detid=0, notes=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display pandas export input forms
    * 
    * parms :
    *   exid    -   export type
    *   detid   -   detail id
    *   notes   -   notes flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    clear_output()

    # add the main import task bar
    if (exid == dem.EXPORT_TB_ONLY) :

        display_export_main_taskbar()  
        display_data_select_df()

    # add the pandas import task bar or pandas details form 
    elif ( (exid == dem.EXPORT_PANDAS_TB_ONLY) or 
           (exid == dem.EXPORT_PANDAS_TB_PLUS_DETAILS) ) :
        
        if(not (cfg.is_a_dfc_dataframe_loaded())) :
            
            display_export_main_taskbar()            
            display_inspection_data() 

        else :
            
            # add the pandas import details form 
            if (exid == dem.EXPORT_PANDAS_TB_PLUS_DETAILS) :
                
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
                    
                    display_export_main_taskbar()
                
                    pandas_export_form     =   get_pandas_export_input_form(detid)

                    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                        pandas_export_form.set_shortForm(True)
                        pandas_export_form.set_gridwidth(640)
                        pandas_export_form.set_custombwidth(110)
                    else :
                        pandas_export_form.set_gridwidth(480)
                        pandas_export_form.set_custombwidth(100)
                    
    
                    pandas_input_html = ""
                    pandas_input_html = pandas_export_form.get_html() 
    
                    pandas_input_heading_html =   "<div>" + get_pandas_export_input_title(detid) + "</div>"

                    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
                    gridhtmls       =   [pandas_input_heading_html,pandas_input_html]

                    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                        display_generic_grid("data-import-wrapper",gridclasses,gridhtmls)
                    else :
                        display_generic_grid("data-import-pop-up-wrapper",gridclasses,gridhtmls)

            else :
                
                # display the composite form
                display_pandas_export_taskbar()              
    else :
        
        if(not (cfg.is_a_dfc_dataframe_loaded())) :
            
            display_export_main_taskbar()
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
                                "&nbsp;&nbsp;&nbsp;&nbsp;(call dfcleanser.common.cfg.get_dfc_dataframe() to get the current dataframe)",
                                "To run the export code in the Custom Export Code box hit 'Run Custom Export' button",
                                "&nbsp;&nbsp;&nbsp;&nbsp;(only the code in the Custom Export Code box is run and stored for scripting)",                        
                                "Once import successful hit 'Save Custom Import' button to store import code for future retrieval",
                                "To drop the custom export code and clear the Custom Export Code box hit 'Drop Custom Export' button"]
            
                print("\n")
                display_inline_help(customNotes,92)
        
            # display the composite form
            display_composite_form([exportCustomDetailsForm])


def display_dc_pandas_export_sql_inputs(fId,dbId,dbconparms,exportparms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display pandas sql export form
    * 
    * parms :
    *   fid             -   export type
    *   dbid            -   database id
    *   dbconparms      -   db connector parms
    *   exportparms     -   export parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
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
            from dfcleanser.data_import.data_import_widgets import (get_column_names, get_rows_html)
            from dfcleanser.data_import.data_import_model import COLUMN_NAMES
            columnlist  =   get_column_names(dbid,fparms[1],opstat)
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
        
        selectDicts     =   []
        df_list         =   cfg.get_dfc_dataframes_select_list()
        selectDicts.append(df_list)
        
        #dbid        =   cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
        #from dfcleanser.data_import.data_import_widgets import get_table_names
        #tableslist  =   get_table_names(dbid,opstat)
        #tables  =   {"default":str(tableslist[0]),"list":tableslist}
        #selectDicts.append(tables)
        exists  =   {"default":"fail","list":["fail","replace","append"]}
        selectDicts.append(exists)
        index  =   {"default":"True","list":["True","False"]}
        selectDicts.append(index)
        
        get_select_defaults(export_sql_input_form,
                            pandas_export_sqltable_id,
                            pandas_export_sqltable_idList,
                            pandas_export_sqltable_typeList,
                            selectDicts)

        export_sql_input_form.set_shortForm(False)
        export_sql_input_form.set_gridwidth(680)
        export_sql_input_form.set_custombwidth(125)
        export_sql_input_form.set_fullparms(True)

        export_sql_input_html = ""
        export_sql_input_html = export_sql_input_form.get_html()
        
        export_sql_heading_html     =   "<div>" + get_pandas_export_input_title(dem.SQLTABLE_EXPORT,dbid) + "</div>"

        if( not (exportparms == None) ) :
            cfg.set_config_value(pandas_export_sqltable_id+"Parms",fparms)
    
        gridclasses     =   ["geocode-final-header",
                             "dfc-left",
                             "dfc-right"]
    
        gridhtmls       =   [export_sql_heading_html,
                             listHtml,
                             export_sql_input_html]
    
        display_generic_grid("data-import-sql-table-wrapper",gridclasses,gridhtmls)

    if( not (opstatStatus)) :
        opstat.set_status(opstatStatus)
        opstat.set_errorMsg(opstatErrormsg)
        display_exception(opstat)


