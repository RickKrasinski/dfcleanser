"""
# data_import_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]
import time

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_import.data_import_model as dim

from dfcleanser.common.html_widgets import (maketextarea, opStatus, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_DOWN, SIMPLE, ROW_MAJOR)


from dfcleanser.common.common_utils import (display_exception, display_status, 
                                            display_notes, display_inline_help, get_formatted_time,
                                            get_parms_for_input, RunningClock,
                                            get_select_defaults, display_generic_grid) 

from dfcleanser.common.db_utils import (get_stored_con_Parms, get_db_connector_list) 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   import forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main import form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   main import form task bar
#--------------------------------------------------------------------------
"""
import_task_bar_doc_title       =   "Import Options"
import_task_bar_title           =   "Import Options"
import_task_bar_id              =   "importoptions"

import_task_bar_keyTitleList    =   ["Pandas</br>Dataframe","Custom","Clear","Reset","Help"]

import_task_bar_jsList          =   ["import_taskbar_callback(0)",
                                     "import_taskbar_callback(1)",
                                     "import_taskbar_callback(2)",
                                     "process_pop_up_cmd(6)",
                                     "displayhelp(" + str(dfchelp.IMPORT_MAIN_TASKBAR_ID) + ")"]

import_task_bar_centered        =   True

import_task_bar_pu_keyTitleList =   ["Pandas</br>Dataframe","Custom","Clear","Reset","Help"]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   pandas import main input form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
pandas_import_task_bar_doc_title     =  "Pandas Dataframe Import Options"
pandas_import_task_bar_title         =  "Pandas Dataframe Import Options"
pandas_import_task_bar_id            =  "pandasimportdataframe"

pandas_import_task_bar_keyTitleList  =   ["CSV","Fixed Width </br>File",
                                          "Excel File","JSON","HTML","SQL Table",
                                          "SQL Query","Return"]

pandas_import_task_bar_jsList        =   ["pandas_import_tb_select_callback("+str(dim.CSV_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.FWF_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.EXCEL_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.JSON_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.HTML_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.SQLTABLE_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.SQLQUERY_IMPORT)+")",
                                          "pandas_import_tb_return_callback()"]

pandas_import_task_bar_centered      =   True


pandas_import_task_barA_doc_title    =  "Pandas Dataframe Import Options"
pandas_import_task_barA_title        =  "Pandas Dataframe Import Options"
pandas_import_task_barA_id           =  "pandasimportdataframeA"

pandas_import_task_barA_keyTitleList =   ["CSV","Fixed Width </br>File",
                                          "Excel File","JSON"]

pandas_import_task_barA_jsList       =   ["pandas_import_tb_select_callback("+str(dim.CSV_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.FWF_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.EXCEL_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.JSON_IMPORT)+")"]

pandas_import_task_barA_centered     =   True

pandas_import_task_barB_doc_title    =  "Pandas Dataframe Import Options"
pandas_import_task_barB_title        =  "Pandas Dataframe Import Options"
pandas_import_task_barB_id           =  "pandasimportdataframeB"

pandas_import_task_barB_keyTitleList =   ["HTML","SQL Table",
                                          "SQL Query","Return"]

pandas_import_task_barB_jsList       =   ["pandas_import_tb_select_callback("+str(dim.HTML_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.SQLTABLE_IMPORT)+")",
                                          "pandas_import_tb_select_callback("+str(dim.SQLQUERY_IMPORT)+")",
                                          "pandas_import_tb_return_callback()"]

pandas_import_task_barB_centered     =   True



"""
#--------------------------------------------------------------------------
#   pandas import csv form parms
#--------------------------------------------------------------------------
"""
pandas_import_csv_title         =   "Pandas CSV Import Parameters"
pandas_import_csv_id            =   "importPandasCSV"
pandas_import_csv_idList        =   ["csvdftitle",
                                     "csvFileName",
                                     "csvcolNamesRow",
                                     "csvcolNamesList",
                                     "csvcolRowIds",
                                     "csvaddlParms",
                                     None,None,None,None]

pandas_import_csv_labelList     =   ["dataframe_title",
                                     "filepath_or_buffer",
                                     "header",
                                     "names",
                                     "index_col",
                                     "Additional Parm(s)",
                                     "Import</br>CSV File","Clear",
                                     "Return","Help"]

pandas_import_csv_typeList      =   ["text","file","text","file",
                                     "text",maketextarea(6),
                                     "button","button","button","button"]

pandas_import_csv_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "enter CSV File name or browse to file below",
                                     "enter row number containing column names (default infer)",
                                     "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                     "enter column number to use for row ids (default None)",
                                     "enter additional parms { Key :  Value} ... (default None)",
                                     None,None,None,None]

pandas_import_csv_jsList       =    [None,None,None,None,None,None,
                                     "pandas_details_import_callback("+str(dim.CSV_IMPORT)+")",
                                     "pandas_details_clear_callback("+str(dim.CSV_IMPORT)+")",
                                     "pandas_details_return_callback(0)",
                                     "display_help_url('"+str(dfchelp.CSV_IMPORT_URL)+"')"]

pandas_import_csv_reqList       =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import fwf input form components
#--------------------------------------------------------------------------
"""

pandas_import_fwf_title         =   "Pandas Fixed Width File Import Parameters"
pandas_import_fwf_id            =   "importPandasFWF"
pandas_import_fwf_idList        =   ["fwfdftitle",
                                     "fwfFileName",
                                     "fwfFileDelimiter",
                                     "fwfcolNamesRow",
                                     "fwfcolNamesList",
                                     "fwfcolRowIds",
                                     "fwfdtypes",
                                     "fwfaddlParms",
                                     None,None,None,None]

pandas_import_fwf_labelList     =   ["dataframe_title",
                                     "filepath_or_buffer ",
                                     "delimiter",
                                     "header",
                                     "names","index_col",
                                     "dtype",
                                     "Additional Parm(s)",
                                     "Import</br>FWF File",
                                     "Clear","Return","Help"]

pandas_import_fwf_typeList      =   ["text","file","text","text","file",
                                     "text","file",maketextarea(6),
                                     "button","button","button","button"]

pandas_import_fwf_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "enter Fixed Width File name or browse to file below",
                                     "enter file delimeter (default , (comma)) ",
                                     "enter row number containing column names (default infer)",
                                     "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                     "enter column number to use for row ids (default None)",
                                     "enter Data Types file name or browse to a json file or as a List (List format - [value, value ...] (default infer)",
                                     "enter additional parms { Key :  Value} ... (default None)",
                                     None,None,None,None]

pandas_import_fwf_jsList        =   [None,None,None,None,None,None,None,None,
                                     "pandas_details_import_callback("+str(dim.FWF_IMPORT)+")",
                                     "pandas_details_clear_callback("+str(dim.FWF_IMPORT)+")",
                                     "pandas_details_return_callback(0)",
                                     "display_help_url('"+str(dfchelp.FWF_IMPORT_URL)+"')"]

pandas_import_fwf_reqList       =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import excel input form components
#--------------------------------------------------------------------------
"""
pandas_import_excel_title       =   "Pandas Excel Import Parameters"
pandas_import_excel_id          =   "importPandasExcel"

pandas_import_excel_idList      =   ["exceldftitle",
                                     "excelIO",
                                     "excelSheetName",
                                     "excelcolNamesRow",
                                     "excelcolNamesList",
                                     "excelcolRowIds",
                                     "exceladdlParms",
                                     None,None,None,None]

pandas_import_excel_labelList   =   ["dataframe_title",
                                     "io",
                                     "sheetname",
                                     "header",
                                     "names",
                                     "index_col",
                                     "Additional Parm(s)",
                                     "Import</br>Excel File",
                                     "Clear","Return","Help"]

pandas_import_excel_typeList    =   ["text","file","text","text","file","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_import_excel_placeholderList = ["dataframe title (default 'filename'_df)",
                                       "enter Excel IO path",
                                       "enter sheet name",
                                       "enter row number containing column names (default infer)",
                                       "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                       "enter column number to use for row ids (default None)",
                                       "enter additional parms { Key :  Value} ... (default None)",
                                       None,None,None,None]

pandas_import_excel_jsList      =   [None,None,None,None,None,None,None,
                                     "pandas_details_import_callback("+str(dim.EXCEL_IMPORT)+")",
                                     "pandas_details_clear_callback("+str(dim.EXCEL_IMPORT)+")",
                                     "pandas_details_return_callback(0)",
                                     "display_help_url('"+str(dfchelp.EXCEL_IMPORT_URL)+"')"]

pandas_import_excel_reqList     =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import json input form components
#--------------------------------------------------------------------------
"""
pandas_import_json_title        =   "Pandas JSON Import Parameters"
pandas_import_json_id           =   "importPandasJSON"

pandas_import_json_idList       =   ["jsondftitle",
                                     "jsonPath",
                                     "jsonOrient",
                                     "jsonimportType","jsondataTypes",
                                     "jsonaddlParms",
                                     None,None,None,None]

pandas_import_json_labelList    =   ["dataframe_title",
                                     "path_or_buf",
                                     "orient",
                                     "type",
                                     "dtype",
                                     "Additional Parm(s)",
                                     "Import</br>JSON File",
                                     "Clear","Return","Help"]

pandas_import_json_typeList     =   ["text","file","text","text","file",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_import_json_placeholderList = ["dataframe title (default 'filename'_df)",
                                      "enter JSON path or browse to file (can be url)",
                                      "enter JSON orientation",
                                      "series or dataframe (default dataframe)",
                                      "enter data types file name or browse to a json file or as a List (List format - [value, value ...] (default infer)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_import_json_jsList       =   [None,None,None,None,None,None,
                                     "pandas_details_import_callback("+str(dim.JSON_IMPORT)+")",
                                     "pandas_details_clear_callback("+str(dim.JSON_IMPORT)+")",
                                     "pandas_details_return_callback(0)",
                                     "display_help_url('"+str(dfchelp.JSON_IMPORT_URL)+"')"]

pandas_import_json_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import html input form components
#--------------------------------------------------------------------------
"""
pandas_import_html_title        =   "Pandas HTML Import Parameters"
pandas_import_html_id           =   "importPandasHTML"

pandas_import_html_idList       =   ["htmldftitle",
                                     "htmlPath",
                                     "htmlMatch",
                                     "htmlFlavor",
                                     "htmlColNamesRow",
                                     "htmnColNamesFile",
                                     "htmlRowIndexColumn",
                                     "htmladdlParms",
                                     None,None,None,None]

pandas_import_html_labelList    =   ["dataframe_title",
                                     "io",
                                     "match",
                                     "flavor",
                                     "header",
                                     "names",
                                     "index_col",
                                     "Additional Parm(s)",
                                     "Import</br>HTML File",
                                     "Clear","Return","Help"]

pandas_import_html_typeList     =   ["text","file","text","text",
                                     "text","file","text",
                                     maketextarea(6),
                                     "button","button","button","button"]

pandas_import_html_placeholderList = ["dataframe title (default default 'filename'_df)",
                                      "enter HTML path or browse to file (can be url)",
                                      "enter match string (default None)",
                                      "parsing flavor (default None bs4-html5)",
                                      "enter row id containing column names or as List [value, value ...] (default None)",
                                      "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                      "enter column id containing row ids or as List [value, value ...] (default None)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_import_html_jsList       =   [None,None,None,None,None,None,None,None,
                                     "pandas_details_import_callback("+str(dim.HTML_IMPORT)+")",
                                     "pandas_details_clear_callback("+str(dim.HTML_IMPORT)+")",
                                     "pandas_details_return_callback(0)",
                                     "display_help_url('"+str(dfchelp.HTML_IMPORT_URL)+"')"]


pandas_import_html_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import sqltable common mysql-mssqlserver-postgresql parms
#--------------------------------------------------------------------------
"""
pandas_import_sqltable_common_title        =   "Pandas SQL Table Import Parameters"
pandas_import_sqltable_common_id           =   "importPandasSQLCommonTable"

pandas_import_sqltable_common_idList       =    ["sqldftitle",
                                                 "sqltablecommontableName",
                                                 "sqltablecommonschema",
                                                 "sqltableindexcol",
                                                 "sqltablecoercefloat",
                                                 "sqltablechunksize",
                                                 "sqltablecommoncolumns",
                                                 "sqltablecommonparsedateformats",
                                                 "sqltablecommonparsedates",
                                                 None,None,None,None,None]

pandas_import_sqltable_common_labelList    =   ["dataframe_title",
                                                "table_name",
                                                "schema",
                                                "index_col",
                                                "coerce_float",
                                                "chunksize",
                                                "table_columns_to_import",
                                                "table_columns_parse_date_format",
                                                "table_columns_to_parse_as_dates",
                                                "Import</br>Table",
                                                "Get</br>Columns",
                                                "Get</br>Date</br>Columns",
                                                "Return","Help"]

pandas_import_sqltable_common_typeList     =   ["text","select","text",maketextarea(2),"select","text","text","select",maketextarea(4),
                                                "button","button","button","button","button"]

pandas_import_sqltable_common_placeholderList = ["dataframe title (default default 'filename'_df)",
                                                 "enter the table name",
                                                 "enter the database schema  (default None)",
                                                 "enter col indices or select from columns list (default None)",
                                                 "convert values of non-string, non-numeric objects (default True)",
                                                 "enter chunk size in num rows (default None)",
                                                 "enter list or click column name (blank : all columns)",
                                                 "parse and date format (default None)",
                                                 "parse and convert date columns (default None)",
                                                 None,None,None,None,None]

pandas_import_sqltable_common_jsList       =   [None,None,None,None,None,None,None,None,None,
                                                "pandas_import_sql_callback(0)",
                                                "pandas_details_get_columns_callback()",
                                                "pandas_details_get_strftime_callback(0)",
                                                "pandas_details_clear_callback("+str(dim.SQLTABLE_IMPORT)+")",
                                                "display_help_url('"+str(dfchelp.SQLTABLE_IMPORT_URL)+"')"]


pandas_import_sqltable_common_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import sqltable common mysql-mssqlserver-postgresql parms
#--------------------------------------------------------------------------
"""
pandas_import_sqltable_custom_title        =   "Pandas SQL Table Import Parameters"
pandas_import_sqltable_custom_id           =   "importPandasSQLCustomTable"

pandas_import_sqltable_custom_idList       =    ["sqltablecustomdftitle",
                                                 "sqltablecustomtableName",
                                                 "sqltablecustomschema",
                                                 "sqltablecustomindexcol",
                                                 "sqltablecustomcoercefloat",
                                                 "sqltablecustomchunksize",
                                                 "sqltablecustomcommonparsedates",
                                                 "sqltablecustomcommoncolumns",
                                                 None,None,None,None]

pandas_import_sqltable_custom_labelList    =   ["dataframe_title",
                                                "table_name",
                                                "schema",
                                                "index_col",
                                                "coerce_float",
                                                "chunksize",
                                                "table_columns_to_parse_as_dates",
                                                "table_columns_to_import",
                                                "Import</br>Table",
                                                "Date Time</br>Formats",
                                                "Return","Help"]

pandas_import_sqltable_custom_typeList     =   ["text","select","text",maketextarea(2),"select","text",maketextarea(4),"text",
                                                "button","button","button","button"]

pandas_import_sqltable_custom_placeholderList = ["dataframe title (default 'filename'_df)",
                                                 "enter the table name",
                                                 "enter the database schema  (default None)",
                                                 "enter col indices or select from columns list (default None)",
                                                 "convert values of non-string, non-numeric objects (default True)",
                                                 "enter chunk size in num rows (default None)",
                                                 "convert dates (default None)",
                                                 "enter list or click on column name(s) to select from SQL table (default all columns)",
                                                 None,None,None,None,None,None]

pandas_import_sqltable_custom_jsList       =   [None,None,None,None,None,None,None,None,
                                                "pandas_import_sql_callback(5)",
                                                "pandas_details_get_strftime_callback(0)",
                                                "pandas_details_clear_callback("+str(dim.SQLTABLE_IMPORT)+")",
                                                "display_help_url('"+str(dfchelp.SQLTABLE_IMPORT_URL)+"')"]

pandas_import_sqltable_custom_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   pandas import sqlquery input form components
#--------------------------------------------------------------------------
"""
pandas_import_sqlquery_title        =   "Pandas SQL Query Import Parameters"
pandas_import_sqlquery_id           =   "importPandasSQLQuery"

pandas_import_sqlquery_idList       =   ["sqlquerydftitle",
                                         "sqlquerysql",
                                         "sqlqueryindices",
                                         "sqlquerycoerce",
                                         "sqlquerychunksize",
                                         "sqlquerysqlparms",
                                         "sqlquerycommonparsedateformats",
                                         "sqlqueryparsedates",
                                         None,None,None,None]

pandas_import_sqlquery_labelList    =   ["dataframe_title",
                                         "sql",
                                         "index_col",
                                         "coerce_float",
                                         "chunksize",
                                         "params",
                                         "table_columns_parse_date_format",
                                         "table_columns_to_parse_as_dates",
                                         "Run</br>SQL Query",
                                         "Clear","Return","Help"]

pandas_import_sqlquery_typeList     =   ["text",maketextarea(10),maketextarea(2),
                                         "select",maketextarea(3),
                                         maketextarea(3),"select","text",
                                         "button","button","button","button","button"]

pandas_import_sqlquery_placeholderList = ["dataframe title (default 'filename'_df)",
                                          "enter the sql query",
                                          "enter col indices or as List value, value ... (default None)",
                                          "convert values of non-string, non-numeric objects (default True)", 
                                          "number of rows (default None)",
                                          "enter sql parameters (default None)",
                                          "parse and date format (default None)",
                                          "list or dict of columns to parse (default None)",
                                          None,None,None,None]

pandas_import_sqlquery_jsList       =   [None,None,None,None,None,None,None,None,
                                         "pandas_import_sql_callback(1)",
                                         "pandas_details_clear_callback("+str(dim.SQLQUERY_IMPORT)+")",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(dfchelp.SQLQUERY_IMPORT_URL)+"')"]

pandas_import_sqlquery_reqList      =   [0,1]

"""
#--------------------------------------------------------------------------
#   Custom Import input form parm lists
#--------------------------------------------------------------------------
"""
custom_import_title             =   "Custom Import Code"
custom_import_id                =   "customImport"
custom_import_idList            =   ["customImportdftitle",
                                     "customImportCode",
                                     "customscriptflag",
                                     None,None,None,None]

custom_import_labelList         =   ["dataframe_title",
                                     "custom_import_code",
                                     "add_to_script_flag",
                                     "Run Custom </br>Import Code",
                                     "Clear",
                                     "Return","Help"]

custom_import_typeList          =   ["text",maketextarea(15),"select","button",
                                     "button","button","button"]

custom_import_placeholderList   =   ["dataframe title (default 'filename'_df)",
                                     "# custom import ",
                                     "add to notebook script",
                                     None,None,None,None]

custom_import_jsList            =   [None,None,None,
                                     "custom_import_callback("+str(dim.PROCESS_CUSTOM_IMPORT)+")",
                                     "custom_import_callback("+str(dim.CLEAR_CUSTOM_IMPORT)+")",
                                     "custom_import_callback("+str(dim.RETURN_CUSTOM_IMPORT)+")",
                                     "displayhelp(" + str(dfchelp.IMPORT_CUSTOM_ID) + ")"]

custom_import_reqList           =   [0,1]

dataimport_inputs           =   [pandas_import_csv_id,pandas_import_fwf_id,pandas_import_excel_id,
                                 pandas_import_json_id,pandas_import_html_id,pandas_import_sqltable_common_id,
                                 pandas_import_sqltable_custom_id,pandas_import_sqlquery_id,custom_import_id]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display import helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

SQL_CUSTOM      =   0

def display_import_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_dfcleanser_taskbar(ButtonGroupForm(import_task_bar_id,
                                                   import_task_bar_keyTitleList,
                                                   import_task_bar_jsList,
                                                   import_task_bar_centered))
    else :
        display_dfcleanser_taskbar(ButtonGroupForm(import_task_bar_id,
                                                   import_task_bar_pu_keyTitleList,
                                                   import_task_bar_jsList,
                                                   import_task_bar_centered))


def display_import_pandas_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_dfcleanser_taskbar(ButtonGroupForm(pandas_import_task_bar_id,
                                                   pandas_import_task_bar_keyTitleList,
                                                   pandas_import_task_bar_jsList,
                                                   pandas_import_task_bar_centered))
    else :
        display_dfcleanser_taskbar(ButtonGroupForm(pandas_import_task_barA_id,
                                                   pandas_import_task_barA_keyTitleList,
                                                   pandas_import_task_barA_jsList,
                                                   pandas_import_task_barA_centered))
        
        display_dfcleanser_taskbar(ButtonGroupForm(pandas_import_task_barB_id,
                                                   pandas_import_task_barB_keyTitleList,
                                                   pandas_import_task_barB_jsList,
                                                   pandas_import_task_barB_centered))
        
        
def get_csv_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_csv_idList))

def get_fwf_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_fwf_idList))

def get_excel_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_excel_idList))

def get_json_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_json_idList))

def get_html_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_html_idList))

def get_custom_import_inputs(parms) :
    return(get_parms_for_input(parms,custom_import_idList))

def get_sqltable_import_inputs(parms,stype) :
    if(stype == SQL_CUSTOM) :
        return(get_parms_for_input(parms,pandas_import_sqltable_custom_idList))
    else :
        return(get_parms_for_input(parms,pandas_import_sqltable_common_idList))
def get_sqltable_import_form_id(stype) :
    if(stype == SQL_CUSTOM) :
        return(pandas_import_sqltable_custom_id)
    else :
        return(pandas_import_sqltable_common_id)
def get_sqltable_import_form_labels(stype) :
    if(stype == SQL_CUSTOM) :
        return(pandas_import_sqltable_custom_labelList)
    else :
        return(pandas_import_sqltable_common_labelList)

def get_sqlquery_import_inputs(parms) :
    return(get_parms_for_input(parms,pandas_import_sqlquery_idList))



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#    Import Display functions
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""


def display_dc_import_forms(id, detid=0, notes=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display data import forms
    * 
    * parms :
    *   id      -    IMPORT_TB_ONLY                          
    *                IMPORT_PANDAS_TB_ONLY                   
    *                IMPORT_PANDAS_TB_PLUS_DETAILS           
    *                IMPORT_CUSTOM_ONLY                      
    *
    *   detid   -   type details
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    
    from IPython.display import clear_output
    clear_output()

    from dfcleanser.common.cfg import check_if_dc_init
    if(not check_if_dc_init()) :
        display_import_main_taskbar()    
        return
    
    from dfcleanser.system.system_control import isEULA_read       
    if( not isEULA_read()) :
        display_import_main_taskbar()        
        display_status("Please review the EULA in the System Chapter")
        return
    
    # add the main import task bar
    if (id == dim.IMPORT_TB_ONLY) :
        
        display_import_main_taskbar()        
        if(cfg.is_a_dfc_dataframe_loaded()) :
            if(not(cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY) is None)) :
                display_notes([cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY) + " imported as dataframe source"])
        else :
            cfg.drop_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY)
            

    # add the pandas import task bar or pandas details form 
    elif ( (id == dim.IMPORT_PANDAS_TB_ONLY) or 
           (id == dim.IMPORT_PANDAS_TB_PLUS_DETAILS) ) :

        # add the pandas import details form 
        if (id == dim.IMPORT_PANDAS_TB_PLUS_DETAILS) :
    
            if( (detid==dim.SQLTABLE_IMPORT)  or (detid==dim.SQLQUERY_IMPORT) ):
                cfg.drop_config_value(pandas_import_sqltable_common_id + "Parms")
                cfg.drop_config_value(pandas_import_sqlquery_id  + "Parms")
                
                import dfcleanser.common.db_utils as dbutils
                
                dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
                cfg.set_config_value(cfg.CURRENT_SQL_IMPORT_ID_KEY,detid)
                
                if(dbid == None)                        :   
                    cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,dbutils.MySql)
                    conparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = ["","","","",dbutils.pymysql_library]

                elif(dbid == dbutils.MySql)             :   
                    conparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = ["","","","",dbutils.pymysql_library]
                        
                elif(dbid == dbutils.MS_SQL_Server)     :   
                    conparms = cfg.get_config_value(dbutils.MSSQL_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = ["","","","",dbutils.pyodbc_library]
                    
                elif(dbid == dbutils.SQLite)            :   
                    conparms = cfg.get_config_value(dbutils.SQLITE_DBCON_PARMS)
                    if(conparms == None) :
                        conparms =  ["",dbutils.sqlite3_library]
                    
                elif(dbid == dbutils.Postgresql)        :   
                    conparms = cfg.get_config_value(dbutils.POSTGRESQL_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = ["","","","",dbutils.psycopg2_library]
                    
                elif(dbid == dbutils.Oracle)            :   
                    conparms = cfg.get_config_value(dbutils.ORACLE_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = ["","","",dbutils.cx_oracle_library]
                    
                elif(dbid == dbutils.Custom)            :   
                    conparms = cfg.get_config_value(dbutils.CUSTOM_DBCON_PARMS)
                    if(conparms == None) :
                        conparms = [""]
                        
                if( detid==dim.SQLTABLE_IMPORT):
                    dbutils.display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),conparms,dbutils.SQL_IMPORT)
                else :
                    dbutils.display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),conparms,dbutils.SQL_QUERY)
                
            else :
                display_import_main_taskbar()
                
                pandas_input_form  =   get_pandas_import_input_form(detid)

                if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    pandas_input_form.set_shortForm(True)
                    pandas_input_form.set_gridwidth(640)
                    pandas_input_form.set_custombwidth(110)
                else :
                    pandas_input_form.set_gridwidth(480)
                    pandas_input_form.set_custombwidth(100)
                    
    
                pandas_input_html = ""
                pandas_input_html = pandas_input_form.get_html() 
    
                pandas_input_heading_html =   "<div>" + get_pandas_import_input_title(detid) + "</div><br>"

                gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
                gridhtmls       =   [pandas_input_heading_html,pandas_input_html]


                if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    display_generic_grid("data-import-wrapper",gridclasses,gridhtmls)
                else :
                    display_generic_grid("data-import-pop-up-wrapper",gridclasses,gridhtmls)
               
        else :
 
            # display the composite form 
            display_import_pandas_taskbar() 
            
              
    else :
        
        display_import_main_taskbar()
        
        if(notes) :
            customNotes =  ["To create custom import code in the code cell below hit 'New Custom Import'",
                            "&nbsp;&nbsp;&nbsp;&nbsp;(enter and test import in the code cell below)",
                            "&nbsp;&nbsp;&nbsp;&nbsp;(leave the '# custom import' comment line in the code cell",
                            "To run the import code in the Custom Import Code box hit 'Run Custom Import' button",
                            "&nbsp;&nbsp;&nbsp;&nbsp;(only the code in the Custom Import Code box is run and stored for scripting)",
                            "Once import successful hit 'Save Custom Import' button to store import code for future retrieval",
                            "To drop the custom import and clear the Custom Import Code box hit 'Drop Custom Import' button"]
        
            print("\n")
            display_inline_help(customNotes,92)
            
                
        pandas_input_form  =   InputForm(custom_import_id,
                                         custom_import_idList,
                                         custom_import_labelList,
                                         custom_import_typeList,
                                         custom_import_placeholderList,
                                         custom_import_jsList,
                                         custom_import_reqList)

        selectDicts     =   []
            
        flags  =   {"default":"False","list":["True","False"]}
        selectDicts.append(flags)
            
        get_select_defaults(pandas_input_form,
                            custom_import_id,
                            custom_import_idList,
                            custom_import_typeList,
                            selectDicts)

        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            pandas_input_form.set_shortForm(True)
            pandas_input_form.set_gridwidth(640)
            pandas_input_form.set_custombwidth(110)
        else :
            pandas_input_form.set_gridwidth(480)
            pandas_input_form.set_custombwidth(100)

        pandas_input_form.set_fullparms(True)
        
        from dfcleanser.common.html_widgets import new_line
        custom_code     =   "# add USER CODE to import into df" + new_line
        custom_code     =   (custom_code + "df = USER CODE" + new_line + new_line)
        custom_code     =   (custom_code + "from dfcleanser.common.cfg import dfc_dataframe, add_dfc_dataframe" + new_line)
        custom_code     =   (custom_code + "newdcdf = dfc_dataframe(dataframe_title, df, " + "'USER NOTES'" + ")" + new_line)
        custom_code     =   (custom_code + "add_dfc_dataframe(newdcdf)" + new_line)
        
        cfg.set_config_value(custom_import_id+"Parms",["",custom_code,""])                    
    
        pandas_input_html = ""
        pandas_input_html = pandas_input_form.get_html() 
    
        pandas_input_heading_html =   "<div>Custom Import</div><br>"

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [pandas_input_heading_html,pandas_input_html]

        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("data-import-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("data-import-pop-up-wrapper",gridclasses,gridhtmls)
            


def display_dc_sql_connector_forms(sqlimportid,dblibid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get sql connector form
    * 
    * parms :
    *  sqlimportid -   type of sql op
    *  dblibid     -   db lib identifier                      
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
        inparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    if(dbid == dbutils.MySql) :
        inparms = cfg.get_config_value(dbutils.MYSQL_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.MS_SQL_Server) :
        inparms = cfg.get_config_value(dbutils.MSSQL_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.Postgresql) :
        inparms = cfg.get_config_value(dbutils.POSTGRESQL_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["","","","",dblibid]
        else :
            inparms[4] = dblibid
            
    elif(dbid == dbutils.SQLite) :
        inparms = cfg.get_config_value(dbutils.SQLITE_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["",dblibid]
        else :
            inparms[1] = dblibid
            
    elif(dbid == dbutils.Oracle) :
        inparms = cfg.get_config_value(dbutils.ORACLE_DBCON_PARMS)
        if(inparms == None) :
            inparms = ["","","",dblibid]
        else :
            inparms[1] = dblibid
                
    elif(dbid == dbutils.Custom) :
        inparms = cfg.get_config_value(dbutils.CUSTOM_DBCON_PARMS)
        
    from dfcleanser.common.db_utils import display_db_connector_inputs, SQL_IMPORT, SQL_QUERY, SQL_EXPORT
    if(sqlimportid == dim.SQLTABLE_IMPORT) :
        display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms,SQL_IMPORT)
        
    elif(sqlimportid == dim.SQLTABLE_IMPORT) :
        display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms,SQL_QUERY)
        
    else :
        display_db_connector_inputs(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms,SQL_EXPORT)
        

def get_pandas_import_input_form(impid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get pandas import form
    * 
    * parms :
    *  id       -   pandas import identifier
    *  dbid     -   pandas db identifier                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(impid < dim.SQLTABLE_IMPORT) :
        
        if(impid == dim.CSV_IMPORT) :  
            import_form     =   InputForm(pandas_import_csv_id,
                                          pandas_import_csv_idList,
                                          pandas_import_csv_labelList,
                                          pandas_import_csv_typeList,
                                          pandas_import_csv_placeholderList,
                                          pandas_import_csv_jsList,
                                          pandas_import_csv_reqList)
        
        if(impid == dim.FWF_IMPORT) :  
            import_form     =   InputForm(pandas_import_fwf_id,
                                          pandas_import_fwf_idList,
                                          pandas_import_fwf_labelList,
                                          pandas_import_fwf_typeList,
                                          pandas_import_fwf_placeholderList,
                                          pandas_import_fwf_jsList,
                                          pandas_import_fwf_reqList)
        
        
        if(impid == dim.EXCEL_IMPORT) :  
            import_form     =   InputForm(pandas_import_excel_id,
                                          pandas_import_excel_idList,
                                          pandas_import_excel_labelList,
                                          pandas_import_excel_typeList,
                                          pandas_import_excel_placeholderList,
                                          pandas_import_excel_jsList,
                                          pandas_import_excel_reqList)
            
        if(impid == dim.JSON_IMPORT) :  
            import_form     =   InputForm(pandas_import_json_id,
                                          pandas_import_json_idList,
                                          pandas_import_json_labelList,
                                          pandas_import_json_typeList,
                                          pandas_import_json_placeholderList,
                                          pandas_import_json_jsList,
                                          pandas_import_json_reqList)
            
        if(impid == dim.HTML_IMPORT) :  
            import_form     =   InputForm(pandas_import_html_id,
                                          pandas_import_html_idList,
                                          pandas_import_html_labelList,
                                          pandas_import_html_typeList,
                                          pandas_import_html_placeholderList,
                                          pandas_import_html_jsList,
                                          pandas_import_html_reqList)
        
        return(import_form)
        
    else :

        if(id == dim.SQLQUERY_IMPORT) : 
            
            import_form     =   InputForm(pandas_import_sqlquery_id,
                                          pandas_import_sqlquery_idList,
                                          pandas_import_sqlquery_labelList,
                                          pandas_import_sqlquery_typeList,
                                          pandas_import_sqlquery_placeholderList,
                                          pandas_import_sqlquery_jsList,
                                          pandas_import_sqlquery_reqList)
            
            
            return(import_form)


def get_pandas_import_input_title(id,dbid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get pandas import form title
    * 
    * parms :
    *  id       -   pandas import identifier
    *  dbid     -   pandas db identifier                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import dfcleanser.common.db_utils as dbutils    
    
    if(dbid == None) :
        pandas_title = {dim.CSV_IMPORT      : pandas_import_csv_title,
                        dim.FWF_IMPORT      : pandas_import_fwf_title,
                        dim.EXCEL_IMPORT    : pandas_import_excel_title,
                        dim.JSON_IMPORT     : pandas_import_json_title,
                        dim.HTML_IMPORT     : pandas_import_html_title,
                        dim.SQLTABLE_IMPORT : pandas_import_sqltable_common_title,
                        dim.SQLQUERY_IMPORT : pandas_import_sqlquery_title} 
       
        return("<br>"+ pandas_title[id] + "<br>")
        
    else :
        
        if(id == dim.SQLTABLE_IMPORT) :  
            
            if(dbid == dbutils.MySql) :
                return(pandas_import_sqltable_common_title + " - " + "MySQL")
            if(dbid == dbutils.MS_SQL_Server) :
                return(pandas_import_sqltable_common_title + " - " + "MS SQL Server")
            if(dbid == dbutils.SQLite) :
                return(pandas_import_sqltable_common_title + " - " + "SQLite")
            if(dbid == dbutils.Postgresql) :
                return(pandas_import_sqltable_common_title + " - " + "Postgresql")
            if(dbid == dbutils.Oracle) :
                return(pandas_import_sqltable_common_title + " - " + "Oracle")
            else :
                return(pandas_import_sqltable_common_title)
                
        elif(id == dim.SQLQUERY_IMPORT) :
            
            return(pandas_import_sqlquery_title)
            
            
def display_sql_table_custom_forms(sqlimportid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display sql custom input form
    * 
    * parms :
    *  sqlimportid   -   sql type table or query                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(sqlimportid == dim.SQLTABLE_IMPORT) :
        
        from IPython.display import clear_output
        clear_output()
        
        display_import_main_taskbar() 
        
        custom_import_form  =   InputForm(pandas_import_sqltable_custom_id,
                                          pandas_import_sqltable_custom_idList,
                                          pandas_import_sqltable_custom_labelList,
                                          pandas_import_sqltable_custom_typeList,
                                          pandas_import_sqltable_custom_placeholderList,
                                          pandas_import_sqltable_custom_jsList,
                                          pandas_import_sqltable_custom_reqList)
   
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            custom_import_form.set_shortForm(True)
            custom_import_form.set_buttonstyle({"font-size":12, "height":75, "width":140, "left-margin":8})
            custom_import_form.set_gridwidth(640)
            custom_import_form.set_fullparms(True)
        
        else :
            
            custom_import_form.set_shortForm(True)
            custom_import_form.set_buttonstyle({"font-size":12, "height":75, "width":140, "left-margin":8})
            custom_import_form.set_gridwidth(480)
            custom_import_form.set_fullparms(True)
    
        custom_import_form_html     =   custom_import_form.get_html()
        custom_import_title_html    =   "<div>Custom SQL Table Import</div><br>"
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [custom_import_title_html,custom_import_form_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("data-import-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("data-import-pop-up-wrapper",gridclasses,gridhtmls)

        
        
        


def display_data_import_notes(s,fname,dbnote=False,custom=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : Build the dc table rowlist and table for columns, datetime
    * 
    * parms :
    *  s       -   start of import 
    *  fname   -   name of file imported                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
     
    if(custom) :
        display_status("Custom import code Imported successfully as a pandas dataframe ")
        
        importnotes = ["[Total Import Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds"]
        
    else :
        
        if(dbnote) :
            display_status("Table " + fname + " Imported successfully as a pandas dataframe ") 
        else :
            display_status("File " + fname + " Imported successfully as a pandas dataframe ")

        importnotes = ["[Total Import Time]&nbsp;&nbsp;:&nbsp;&nbsp;" + str(get_formatted_time(time.time()-s))+ " seconds"]
    
    display_notes(importnotes)


def get_rows_html(rowslist,formtype,forExport=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : Build the dc table rowlist and table for columns, datetime
    * 
    * parms :
    *  rowslist      -    rows list 
    *  formtype      -    tabled id                      
    *  forExport     -    flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("get_rows_html",rowslist,formtype,forExport)

    if( not (rowslist == None) ) :       
        tableslistHeader    =   [""]
        tableslistRows      =   []
        tableslistWidths    =   [100]
        tableslistAligns    =   ["left"]
        tableslistHrefs     =   []
    
        for i in range(len(rowslist)) :
            tableslistrow = [rowslist[i]]
            tableslistRows.append(tableslistrow)
            if(formtype == dim.TABLE_NAMES) :
                if(not(forExport)) :
                    tableslistHrefs.append(["select_table"])
                else :
                    tableslistHrefs.append(["select_export_table"])
                    
            elif(formtype == dim.COLUMN_NAMES) :
                if(not(forExport)) :
                    tableslistHrefs.append(["select_column"])
                else :
                    tableslistHrefs.append(["select_export_column"])
                    
                table_names_table = dcTable("Columns","columnnamesTable",
                                            cfg.DataImport_ID,
                                            tableslistHeader,tableslistRows,
                                            tableslistWidths,tableslistAligns)
                
            else :
                if(not(forExport)) :
                    tableslistHrefs.append(["select_date_column"])
                else :
                    tableslistHrefs.append(["select_export_date_column"])
            
                table_names_table = dcTable("date Columns","datetimeformatsTable",
                                            cfg.DataImport_ID,
                                            tableslistHeader,tableslistRows,
                                            tableslistWidths,tableslistAligns)
        
        #table_names_table = None
                
        #if(formtype == dim.COLUMN_NAMES) :
        #    table_names_table = dcTable("Columns","columnnamesTable",
        #                                cfg.DataImport_ID,
        #                                tableslistHeader,tableslistRows,
        #                                tableslistWidths,tableslistAligns)
        #else :
        #    table_names_table = dcTable("datetime Formats","datetimeformatsTable",
        #                                cfg.DataImport_ID,
        #                                tableslistHeader,tableslistRows,
        #                                tableslistWidths,tableslistAligns)
            
        #if(not (formtype == dim.DATETIME_FORMATS) ) :
        table_names_table.set_refList(tableslistHrefs)
        #else :
        #    table_names_table.set_refList(None)
    
        table_names_table.set_small(True)
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            table_names_table.set_smallwidth(98)
            table_names_table.set_smallmargin(10)
        else :
            table_names_table.set_smallwidth(98)
            table_names_table.set_smallmargin(4)
            
        table_names_table.set_border(True)
        
        if(not (formtype == dim.DATETIME_FORMATS) ) :
            table_names_table.set_checkLength(True)
            table_names_table.set_textLength(20)
        else :
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                table_names_table.set_checkLength(False)
            else :
                table_names_table.set_checkLength(True)
                table_names_table.set_textLength(18)
        
        table_names_table.set_html_only(True) 
    
        table_names_table.set_tabletype(SIMPLE)#ROW_MAJOR)
        #table_names_table.set_rowspertable(14)
        #table_names_table.set_lastrowdisplayed(-1)

        listHtml = table_names_table.get_html()#get_row_major_table(table_names_table,SCROLL_DOWN,False)
        
        return(listHtml)
        
    else :
        return(None)


def check_dbcondict(dbid,conparms) :
    
    from dfcleanser.common.db_utils import get_dbcondict
    dbcondict = get_dbcondict(dbid,conparms)
    
    dbdict_keys     =   list(dbcondict.keys())
    
    for i in range(len(dbdict_keys)) :
        dbcon_val   =  dbcondict.get(dbdict_keys[i]) 
        if(len(dbcon_val) == 0) :
            return(False)
    
    return(True)


def display_dc_pandas_import_sql_inputs(importtype,formtype,DBid,dbconparms,importparms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the input form
    * 
    * parms :
    *  importtype      -    sqltable or sqlquery 
    *  formtype        -    type of form DBLIBS, TABLE_NAMES, ...                      
    *  dbid            -    Database Id
    *  dbconparms      -    db connector parms                      
    *  importparms     -    import parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    opstat      =   opStatus()
    
    listHtml    =   ""
    
    if(DBid == None) :
        dbid = cfg.get_config_value(cfg.CURRENT_DB_ID_KEY)
        if(dbid == None) :
            from dfcleanser.common.db_utils import MySql
            dbid = MySql
    else :
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,DBid)
        dbid = DBid

    dbcondict = {}
    if(dbconparms != None) :
        from dfcleanser.common.db_utils import get_db_connector_idList
        if(formtype == dim.SQLTABLE_IMPORT) :
            conparms = get_parms_for_input(dbconparms,get_db_connector_idList(dbid))
        else :
            conparms = get_parms_for_input(dbconparms,get_db_connector_idList(dbid))
    else :
        conparms = get_stored_con_Parms(dbid)        
    
    from dfcleanser.common.db_utils import get_dbcondict
    dbcondict = get_dbcondict(dbid,conparms)

    if(check_dbcondict(dbid,conparms)) :
    
        opstat = opStatus()
    
        if(importtype == dim.SQLTABLE_IMPORT) :
        
            if(importparms != None) :
                inparms = get_parms_for_input(importparms,pandas_import_sqltable_common_idList)
                cfg.set_config_value(pandas_import_sqltable_common_id+"Parms",inparms)
        
            # if the list is table names or column names
            if(formtype == dim.COLUMN_NAMES) :
        
                if(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY) == None) :        
                    columnslist = get_column_names(0,inparms[1],opstat)
                else :
                    columnslist = get_column_names(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms[1],opstat) 
            
                listHtml = get_rows_html(columnslist,formtype)
    
            elif(formtype == dim.DATETIME_FORMATS) :
            
                if(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY) == None) :        
                    columnslist = get_column_names(0,inparms[1],opstat)
                else :
                    columnslist = get_column_names(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),inparms[1],opstat) 
            
                listHtml = get_rows_html(columnslist,formtype)
            
            # build the db connector parms list             
            else :
                listHtml = get_db_connector_list(dbid,dbcondict)
            
        else : 
        
            listHtml = get_db_connector_list(dbid,dbcondict)
        
        if(importtype == dim.SQLTABLE_IMPORT) :
        
            from dfcleanser.common.db_utils import Custom
            if(dbid != Custom) :
                from dfcleanser.common.html_widgets import InputForm
                pandas_import_sqltable_form = InputForm(pandas_import_sqltable_common_id,
                                                        pandas_import_sqltable_common_idList,
                                                        pandas_import_sqltable_common_labelList,
                                                        pandas_import_sqltable_common_typeList,
                                                        pandas_import_sqltable_common_placeholderList,
                                                        pandas_import_sqltable_common_jsList,
                                                        pandas_import_sqltable_common_reqList)
            
                selectDicts     =   []
            
                if(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY) is None) :        
                    tableslist = get_table_names(0,opstat)
                else :
                    tableslist = get_table_names(cfg.get_config_value(cfg.CURRENT_DB_ID_KEY),opstat)  
                
                if(not (tableslist is None)) :
                    tables  =   {"default":str(tableslist[0]),"list":tableslist,"callback":"select_table"}
                else :
                    tables  =   {"default":"No Tables Found","list":["No Tables Found"]}
                
                selectDicts.append(tables)
            
                flags  =   {"default":"True","list":["True","False"]}
                selectDicts.append(flags)
            
                datetimeformats     =   get_datetime_formats()
                formats  =   {"default":str(datetimeformats[1]),"list":datetimeformats,"callback":"select_dtformat"}
                selectDicts.append(formats)
            
                get_select_defaults(pandas_import_sqltable_form,
                                    pandas_import_sqltable_common_id,
                                    pandas_import_sqltable_common_idList,
                                    pandas_import_sqltable_common_typeList,
                                    selectDicts)

            else :
                pandas_import_sqltable_form = InputForm(pandas_import_sqltable_custom_id,
                                                        pandas_import_sqltable_custom_idList,
                                                        pandas_import_sqltable_custom_labelList,
                                                        pandas_import_sqltable_custom_typeList,
                                                        pandas_import_sqltable_custom_placeholderList,
                                                        pandas_import_sqltable_custom_jsList,
                                                        pandas_import_sqltable_custom_reqList)
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                pandas_import_sqltable_form.set_shortForm(False)
                pandas_import_sqltable_form.set_gridwidth(680)
                pandas_import_sqltable_form.set_custombwidth(125)
            else :
                pandas_import_sqltable_form.set_shortForm(True)
                pandas_import_sqltable_form.set_gridwidth(360)
                pandas_import_sqltable_form.set_custombwidth(70)
            
            pandas_import_sqltable_form.set_fullparms(True)
        
            import_sql_input_html = ""
            import_sql_input_html = pandas_import_sqltable_form.get_html()
        
            import_sql_heading_html     =   "<div>" + get_pandas_import_input_title(dim.SQLTABLE_IMPORT,dbid) + "</div><br>"

        else :
        
            from dfcleanser.common.html_widgets import InputForm       
            import_sql_input_form = InputForm(pandas_import_sqlquery_id,
                                              pandas_import_sqlquery_idList,
                                              pandas_import_sqlquery_labelList,
                                              pandas_import_sqlquery_typeList,
                                              pandas_import_sqlquery_placeholderList,
                                              pandas_import_sqlquery_jsList,
                                              pandas_import_sqlquery_reqList)
            
            selectDicts     =   []
            
            flags  =   {"default":"True","list":["True","False"]}
            selectDicts.append(flags)
            
            datetimeformats     =   get_datetime_formats()
            formats  =   {"default":str(datetimeformats[1]),"list":datetimeformats,"callback":"select_dtformat"}
            selectDicts.append(formats)
        
            get_select_defaults(import_sql_input_form,
                                pandas_import_sqlquery_id,
                                pandas_import_sqlquery_idList,
                                pandas_import_sqlquery_typeList,
                                selectDicts)
        
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                import_sql_input_form.set_shortForm(False)
                import_sql_input_form.set_gridwidth(680)
                import_sql_input_form.set_custombwidth(125)
            else :
                import_sql_input_form.set_shortForm(True)
                import_sql_input_form.set_gridwidth(360)
                import_sql_input_form.set_custombwidth(70)
            
            import_sql_input_form.set_fullparms(True)
        
            import_sql_input_html = ""
            import_sql_input_html = import_sql_input_form.get_html()
        
            import_sql_heading_html     =   "<div>" + get_pandas_import_input_title(dim.SQLQUERY_IMPORT,dbid) + "</div><br>"
    
        if( not (importparms == None) ) :
            inparms = get_parms_for_input(importparms,pandas_import_sqltable_common_idList)
            cfg.set_config_value(pandas_import_sqltable_common_id+"Parms",inparms)

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [import_sql_heading_html,listHtml,import_sql_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("data-import-sql-table-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("data-import-sql-table-pop-up-wrapper",gridclasses,gridhtmls)
    
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Cannnot connect to db : Invalid connect parms")
    
    return(opstat)

"""
#------------------------------------------------------------------
#   fetch rows into a list 
#
#   dbid            -   database id
#   dbcon           -   database connector
#   queryString     -   sql query to run
#   opstat          -   op status container
#   colid           -   column id
#
#------------------------------------------------------------------
"""
def fetch_rows(dbid,dbcon,queryString,opstat,colid=0) :
    """
    * -------------------------------------------------------------------------- 
    * function : fetch rows into a list
    * 
    * parms :
    *  dbid            -   database id
    *  dbcon           -   database connector
    *  queryString     -   sql query to run
    *  opstat          -   op status container
    *  colid           -   column id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import dfcleanser.common.db_utils as dbutils
    
    try :

        cursor = dbcon.get_dbConnection().cursor()
            
        crows = []
        number_of_tables = 0
            
        if(dbid == dbutils.MySql) :

            if(dbcon.get_ConnectionParms().get("dblibrary") == dbutils.pymysql_library) :
                number_of_tables = cursor.execute(queryString)
                crows = cursor.fetchall()
            else :
                cursor.execute(queryString)
                crows = cursor.fetchall()
                number_of_tables = len(crows)

        elif(dbid == dbutils.MS_SQL_Server) :
            
            cursor.execute(queryString)
            row = cursor.fetchone()
            while row:
                crows.append(row)
                number_of_tables = number_of_tables + 1
                row = cursor.fetchone()
            
        elif(dbid == dbutils.SQLite) :
                
            cursor.execute(queryString)    
            crows = cursor.fetchall()
            number_of_tables = len(crows)
                    
        elif(dbid == dbutils.Postgresql) :

            cursor.execute(queryString)    
            crows = cursor.fetchall()
            number_of_tables = len(crows)
            
        elif(dbid == dbutils.Oracle) :

            cursor.execute(queryString)
            for row in cursor.fetchall():
                number_of_tables = number_of_tables + 1    
                crows.append(row)
                
            cursor.close()
                
        else :

            number_of_tables = cursor.execute(queryString)
            crows = cursor.fetchall()
            
        tableList = []
        for i in range(number_of_tables) :
            tableList.append(crows[i][colid])

    except Exception as e:
        opstat.store_exception("Unable to get rows ",e)

    if(opstat.get_status() ) :
        return(tableList) 
    else :
        return(None)

def get_table_names(dbid,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table names from a db
    * 
    * parms :
    *  dbid    -   database id
    *  opstat  -   op status container
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import dfcleanser.common.db_utils as dbutils

    from dfcleanser.common.db_utils import get_dbcondict
    dbconDict  =   get_dbcondict(dbid,None)
    
    print("dbconDict",dbconDict)
    
    clock = RunningClock()
    clock.start()
    
    tableList = None
    
    from dfcleanser.common.db_utils import dbConnector, NATIVE
    dbcon = dbConnector()

    dbcon.connect_to_db(NATIVE,opstat,dbconDict)
    
    if( (opstat.get_status()) and (len(dbconDict.get("database"))>0) ) :
        
        dbid = dbcon.get_ConnectionParms().get("dbid")

        if(dbid == dbutils.MySql) :
        
            gettablesquery = ("SELECT table_name FROM information_schema.tables WHERE table_schema = '" + 
                              dbconDict.get("database") + "'")
            
        elif(dbid == dbutils.MS_SQL_Server) :
            
            gettablesquery =  "SELECT Distinct TABLE_NAME FROM information_schema.TABLES"
            
        elif(dbid == dbutils.SQLite) : 
            
            gettablesquery = ("SELECT name FROM sqlite_master WHERE type='table'")
            
        elif(dbid == dbutils.Postgresql) : 
            
            gettablesquery = ("SELECT tablename FROM pg_tables WHERE schemaname = 'public'")
            
        elif(dbid == dbutils.Oracle) : 
            
            gettablesquery = ("SELECT table_name FROM user_tables")#("SELECT table_name FROM " + 

        else :
           return(None)

        tableList = []
        tableList = fetch_rows(dbid,dbcon,gettablesquery,opstat) 
        
        if(opstat.get_status()) :
            if(dbid == dbutils.SQLite) :
                sqlitelist = []
                for i in range(len(tableList)) :
                    if(tableList[i].find("sqlite") == -1) :
                        sqlitelist.append(tableList[i])

                tableList = sqlitelist
        else :
            tableList = None
            
        dbcon.close_dbConnection(opstat)
        
        clock.stop() 
    
    else : 
        
        clock.stop() 
        
        if(dbid != dbutils.Custom) :
            if(len(dbconDict.get("database")) < 1) :
                opstat.set_errorMsg("Unable to Connect : Invalid Connect Parms")
        else :
            opstat.set_errorMsg("Unable to Connect : Invalid Connect Parms")
       
    return(tableList)  

    
"""
#------------------------------------------------------------------
#   get column names 
#
#   dbid        -   database id
#   tablename   -   table name
#   opstat      -   op status container
#
#------------------------------------------------------------------
"""
def get_column_names(dbid,tablename,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get column names from a table
    * 
    * parms :
    *  dbid        -   database id
    *  tablename   -   table name
    *  opstat  -   op status container
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import dfcleanser.common.db_utils as dbutils
    
    dbconDict  =   {}
    from dfcleanser.common.db_utils import get_dbcondict
    dbconDict  =   get_dbcondict(dbid,None)
    
    columnList = [] 
    
    if( len(tablename) == 0 ) :
        return(columnList)
    
    clock = RunningClock()
    clock.start()

    from dfcleanser.common.db_utils import dbConnector, NATIVE
    dbcon = dbConnector()
    dbcon.connect_to_db(NATIVE,opstat,dbconDict)
    

    if( (opstat.get_status()) and (len(tablename) > 0) ) :

        if(dbid == dbutils.MySql) :
        
            getcolumnsquery = ("SELECT column_name FROM information_schema.columns "  + 
                               "where table_schema='" + dbconDict.get("database") + "'" + 
                               " AND table_name = '" + tablename + "'")
            
        elif(dbid == dbutils.MS_SQL_Server) :
            
            getcolumnsquery = ("SELECT column_name FROM information_schema.columns " +  
                               "WHERE table_name='" + tablename + "'")

        elif(dbid == dbutils.SQLite) : 
            
            getcolumnsquery = ("PRAGMA table_info(" + tablename + ")")

        elif(dbid == dbutils.Postgresql) : 
            
            getcolumnsquery = ("SELECT column_name FROM information_schema.columns " + 
                               "WHERE table_schema = 'public' " + 
                               "AND table_name = '" + tablename + "'")
            
        elif(dbid == dbutils.Oracle) : 
            
            getcolumnsquery = ("SELECT COLUMN_NAME from ALL_TAB_COLUMNS where TABLE_NAME='" + tablename + "'")
            
        else :
            
            print("Invalid DB ID for get columns")
            return(None)

        if(dbid == dbutils.SQLite) :
            columnList = fetch_rows(dbid,dbcon,getcolumnsquery,opstat,1)
        else :
            columnList = fetch_rows(dbid,dbcon,getcolumnsquery,opstat) 
        
        if(not (opstat.get_status())) :
            columnList = None
        
        dbopstat = opStatus()
        dbcon.close_dbConnection(dbopstat)
        
    else : 
        if(len(tablename) < 1) :
                opstat.set_errorMsg("Invalid Table Name")
        
    clock.stop()
    
    return(columnList)  

    
"""
#------------------------------------------------------------------
#   get date time formats 
#------------------------------------------------------------------
"""
def get_datetime_formats() :

    formatsList = ["None"]
    
    from dfcleanser.sw_utilities.sw_utility_control import get_Dict
    formats = get_Dict("strftime")

    keys = list(formats.keys())
    keys.sort()
    
    for i in range(len(keys)) :
        #formatsList.append(keys[i])
        formatsList.append(formats.get(keys[i]))

    timestamp_formats   =   ["D","s","ns","ms","us"]
    for i in range(len(timestamp_formats)) :
        formatsList.append(timestamp_formats[i])    
    
    return(formatsList)  




