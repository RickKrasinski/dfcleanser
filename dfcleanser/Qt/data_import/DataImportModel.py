"""
# DataImportModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.common.common_utils import (opStatus)
from dfcleanser.common.cfg import (add_error_to_log, SEVERE_ERROR, set_config_value, get_config_value, CURRENT_IMPORTED_DATA_SOURCE_KEY)

DEBUG_IMPORT_HISTORY            =   False
DEBUG_IMPORT_HISTORY_DETAILS    =   False
DEBUG_IMPORT_FILE               =   False
DEBUG_IMPORT_PARMS              =   False

DEBUG_IMPORT                    =   True
DEBUG_SQL_IMPORT                =   False
DEBUG_SQL_IMPORT_HTML           =   False
DEBUG_IMPORT_VALUES             =   False

DEBUG_EXPORT                    =   False

"""
#--------------------------------------------------------------------------
#   pandas import ids
#--------------------------------------------------------------------------
"""
CSV_IMPORT                      =   0
FWF_IMPORT                      =   1
EXCEL_IMPORT                    =   2
JSON_IMPORT                     =   3
HTML_IMPORT                     =   4
SQLTABLE_IMPORT                 =   5
SQLQUERY_IMPORT                 =   6
CUSTOM_IMPORT                   =   7
XML_IMPORT                      =   8
PDF_IMPORT                      =   9


def get_text_for_import_type(import_id) :

    if(import_id == CSV_IMPORT) : return("CSV File")
    elif(import_id == FWF_IMPORT) : return("FWF File")
    elif(import_id == EXCEL_IMPORT) : return("EXCEL File")
    elif(import_id == JSON_IMPORT) : return("JSON File")
    elif(import_id == HTML_IMPORT) : return("HTML File")
    elif(import_id == SQLTABLE_IMPORT) : return("SQL Table")
    elif(import_id == SQLQUERY_IMPORT) : return("SQL QueryT")
    elif(import_id == CUSTOM_IMPORT) : return("CUSTOM File")
    elif(import_id == XML_IMPORT) : return("XML File")
    elif(import_id == PDF_IMPORT) : return("PDF File")
    return("Unknowm Import")

"""
#-----------------------------------------------------
#   sql input table identifiers 
#----------------------------------------------------
"""

SQL_CUSTOM      =   0
SQL_COMMON      =   1

"""
* ----------------------------------------------------
# html import df list
* ----------------------------------------------------
""" 
     
def set_dfs_list(dfs_list) :
    dfsList.set_dfs_list(dfs_list)

def get_dfs_list() :   
    return(dfsList.get_dfs_list())

def clear_dfs_list() :   
    dfsList.drop_dfs_list()

def get_current_df_id() :   
    return(dfsList.get_df_id())

def set_current_df_id(dfid) :   
    dfsList.set_df_id(dfid)

def get_current_df_url() :   
    return(dfsList.get_df_url())

def set_current_df_url(url) :   
    dfsList.set_df_url(url)

class dfs_list :
    
    # instance variables
    dfs_list        =   None
    df_id           =   None
    df_url          =   None
    
    # full constructor
    def __init__(self) :
        self.dfs_list        =   None
        self.df_id           =   None
        self.df_url          =   None
        
    def set_dfs_list(self,dfslist) :
        self.dfs_list  =   dfslist

    def get_dfs_list(self) :
        return(self.dfs_list)
        
    def set_df_id(self,dfid) :
        self.df_id  =   dfid

    def get_df_id(self) :
        return(self.df_id)
        
    def set_df_url(self,dfurl) :
        self.df_url  =   dfurl

    def get_df_url(self) :
        return(self.df_url)
        
    def drop_dfs_list(self) :
        self.dfs_list   =   None
        self.df_id      =   None
        self.df_url     =   None

dfsList     =   dfs_list() 


def get_formid_for_import(detid) :
    """
    * ------------------------------------------
    * function : get addl parms for import
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * -----------------------------------------
    """
    
    if(detid == CSV_IMPORT) :
        formid  =   pandas_import_csv_id
    elif(detid == FWF_IMPORT) :
        formid  =   pandas_import_fwf_id
    elif(detid == EXCEL_IMPORT) :
        formid  =   pandas_import_excel_id
    elif(detid == JSON_IMPORT) :
        formid  =   pandas_import_json_id
    elif(detid == HTML_IMPORT) :
        formid  =   pandas_import_html_id
    elif(detid == SQLTABLE_IMPORT) :
        formid  =   pandas_import_sqltable_common_id
    elif(detid == SQLQUERY_IMPORT) :
        formid  =   pandas_import_sqlquery_id
    elif(detid == CUSTOM_IMPORT) :
        formid  =   custom_import_id
    else :
        return(None)
    
    return(formid)


"""
#----------------------------------------------------
#----------------------------------------------------
#   Dataframe Cleanser import form objects objects
#----------------------------------------------------
#----------------------------------------------------
"""

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
from dfcleanser.common.common_utils import (opStatus)

from dfcleanser.sw_utilities.dfc_qt_model import (maketextarea, makefilearea)



"""
#-------------------------------------------
#   pandas import csv form parms
#-------------------------------------------
"""
pandas_import_csv_title         =   "Pandas CSV Import"
pandas_import_csv_id            =   "importPandasCSV"
pandas_import_csv_idList        =   ["csvdftitle",
                                     "prevcsvdftitle",
                                     "csvFileName",
                                     "csvcolNamesRow",
                                     "csvcolNamesList",
                                     "csvcolRowIds",
                                     "csvcoldtypes",
                                     "csvaddlParms",
                                     None,None,None,None]

pandas_import_csv_labelList     =   ["dataframe_title",
                                     "csv_imports_history",
                                     "filepath_or_buffer",
                                     "header",
                                     "names",
                                     "index_col",
                                     "dtypes",
                                     "Additional Parm(s)",
                                     "Import</br>CSV File","Clear",
                                     "Return","Help"]

pandas_import_csv_typeList      =   ["text","select","file","text",maketextarea(1),
                                     "text",maketextarea(1),maketextarea(4),
                                     "button","button","button","button"]

pandas_import_csv_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "select dataframe title",
                                     "enter CSV File name or browse to file below",
                                     "enter row number containing column names (default infer)",
                                     "enter Column Names file name or as a json list - (default None)",
                                     "enter column number to use for row ids (default None)",
                                     "enter column datatypes as json dict - (default None)",
                                     "enter additional parms as json dict - (default None)",
                                     None,None,None,None]

pandas_import_csv_reqList       =   [0,1,2]


"""
#-----------------------------------------------
#   pandas import fwf input form components
#-----------------------------------------------
"""

pandas_import_fwf_title         =   "Pandas Fixed Width File Import"
pandas_import_fwf_id            =   "importPandasFWF"
pandas_import_fwf_idList        =   ["fwfdftitle",
                                     "prevfwfdftitle",
                                     "fwfFileName",
                                     "fwfcplspecs",
                                     "fwfwidths",
                                     "fwfinfernrows",
                                     "fwfkwds",
                                     None,None,None,None]

pandas_import_fwf_labelList     =   ["dataframe_title",
                                     "fwf_imports_history",
                                     "filepath_or_buffer ",
                                     "col_specs",
                                     "widths",
                                     "infer_nrows",
                                     "kwds",
                                     "Import</br>FWF File",
                                     "Clear","Return","Help"]

pandas_import_fwf_typeList      =   ["text","select","file","text","text","text","text",
                                     "button","button","button","button"]

pandas_import_fwf_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "select dataframe title",
                                     "enter Fixed Width File name or browse to file below",
                                     "enter colspecs",
                                     "enter widths",
                                     "enter nrows",
                                     "enter keywords (default None)",
                                     None,None,None,None]

pandas_import_fwf_reqList       =   [0,1,2]

"""
#--------------------------------------------------
#   pandas import excel input form components
#--------------------------------------------------
"""
pandas_import_excel_title       =   "Pandas Excel Import"
pandas_import_excel_id          =   "importPandasExcel"

pandas_import_excel_idList      =   ["exceldftitle",
                                     "prevexceldftitle",
                                     "excelIO",
                                     "excelSheetName",
                                     "excelcolNamesRow",
                                     "excelcolNamesList",
                                     "excelcolRowIds",
                                     "excelcoldtype",
                                     "exceladdlParms",
                                     None,None,None,None]

pandas_import_excel_labelList   =   ["dataframe_title",
                                     "excel_imports_history",
                                     "io",
                                     "sheet_name",
                                     "header",
                                     "names",
                                     "index_col",
                                     "dtypes",
                                     "Additional Parm(s)",
                                     "Import</br>Excel File",
                                     "Clear","Return","Help"]

pandas_import_excel_typeList    =   ["text","select","file","text","text",
                                     maketextarea(1),"text",maketextarea(1),maketextarea(4),
                                     "button","button","button","button"]

pandas_import_excel_placeholderList = ["dataframe title (default 'filename'_df)",
                                       "select dataframe title",
                                       "enter Excel IO path",
                                       "enter sheet name",
                                       "enter row number containing column names (default infer)",
                                       "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                       "enter column number to use for row ids (default None)",
                                       "enter Data Types file name or browse to a json file or json dict - {'col' : 'str', ...} (default None)",
                                       "enter additional parms { Key :  Value} ... (default None)",
                                       None,None,None,None]

pandas_import_excel_reqList     =   [0,1,2]


"""
#-------------------------------------------------
#   pandas import json input form components
#-------------------------------------------------
"""
pandas_import_json_title        =   "Pandas JSON Import"
pandas_import_json_id           =   "importPandasJSON"

pandas_import_json_idList       =   ["jsondftitle",
                                     "prevjsondftitle",
                                     "jsonPath",
                                     "jsonOrient",
                                     "jsonimportType","jsondataTypes",
                                     "jsonaddlParms",
                                     None,None,None,None]

pandas_import_json_labelList    =   ["dataframe_title",
                                     "json_imports_history",
                                     "path_or_buf",
                                     "orient",
                                     "typ",
                                     "dtype",
                                     "Additional Parm(s)",
                                     "Import</br>JSON File",
                                     "Clear","Return","Help"]

pandas_import_json_typeList     =   ["text","select","file","select","select", makefilearea(1),
                                     maketextarea(3),
                                     "button","button","button","button"]

pandas_import_json_placeholderList = ["dataframe title (default 'filename'_df)",
                                      "select dataframe title",
                                      "enter JSON path or browse to file (can be url)",
                                      "enter JSON orientation",
                                      "series or dataframe (default dataframe)",
                                      "enter data types file name or browse to a json file or json dict - {'col' : 'str', ...} (default None)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_import_json_reqList      =   [0,1,2]


"""
#-------------------------------------------
#   pandas import xml form parms
#-------------------------------------------
"""
pandas_import_xml_title         =   "Pandas XML Import"
pandas_import_xml_id            =   "importPandasXML"
pandas_import_xml_idList        =   ["xmldftitle",
                                     "prevxmldftitle",
                                     "xmlFileName",
                                     "xmlcolNamesRow",
                                     "xmlcolNamesList",
                                     "xmlcolRowIds",
                                     "xmlcoldtypes",
                                     "xmladdlParms",
                                     None,None,None,None]

pandas_import_xml_labelList     =   ["dataframe_title",
                                     "xml_imports_history",
                                     "filepath_or_buffer",
                                     "xpath",
                                     "namespaces",
                                     "elems_only",
                                     "attrs_only",
                                     "Additional Parm(s)",
                                     "Import</br>XML File","Clear",
                                     "Return","Help"]

pandas_import_xml_typeList      =   ["text","select","file","text",maketextarea(2),
                                     "select","select",maketextarea(4),
                                     "button","button","button","button"]

pandas_import_xml_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "select dataframe title",
                                     "enter XML File name or browse to file below",
                                     "enter xpath string",
                                     "enter namespaces dict",
                                     "elements only flag",
                                     "attributes only flag",
                                     "enter additional parms as json dict - (default None)",
                                     None,None,None,None]


pandas_import_xml_reqList       =   [0,1,2]


"""
#-------------------------------------------
#   pandas import pdf form parms
#-------------------------------------------
"""
pandas_import_pdf_title         =   "Pandas PDF Import"
pandas_import_pdf_id            =   "importPandasXML"
pandas_import_pdf_idList        =   ["pdfdftitle",
                                     "prevpdfdftitle",
                                     "pdfFileName",
                                     None,None,None,None]

pandas_import_pdf_labelList     =   ["dataframe_title",
                                     "pdf_imports_history",
                                     "filepath_or_buffer",
                                     "Import</br>PDF File","Clear",
                                     "Return","Help"]

pandas_import_pdf_typeList      =   ["text","select","file",
                                     "button","button","button","button"]

pandas_import_pdf_placeholderList = ["dataframe title (default 'filename'_df)",
                                     "select dataframe title",
                                     "enter XML File name or browse to file below",
                                     None,None,None,None]


pandas_import_pdf_reqList       =   [0,1,2]


"""
#------------------------------------------------
#   pandas import html input form components
#------------------------------------------------
"""
pandas_import_html_title        =   "Pandas HTML Import"
pandas_import_html_id           =   "importPandasHTML"

pandas_import_html_idList       =   ["htmldftitle",
                                     "prevhtmlurls",
                                     "htmlMatch",
                                     "htmlFlavor",
                                     "htmlHeader",
                                     "htmladdlParms",
                                     None,None,None,None]

pandas_import_html_labelList    =   ["html_url",
                                     "html_url_history",
                                     "match",
                                     "flavor",
                                     "header",
                                     "Additional Parm(s)",
                                     "Import</br>HTML File",
                                     "Clear","Return","Help"]

pandas_import_html_typeList     =   ["text","select","text","text","text",
                                     maketextarea(4),
                                     "button","button","button","button"]

pandas_import_html_placeholderList = ["html url to retrieve",
                                      "select url",
                                      "enter match string (default None)",
                                      "parsing flavor (default None bs4-html5)",
                                      "enter row id containing column names or as List [value, value ...] (default None)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]


pandas_import_html_reqList      =   [0,1,2]


"""
#----------------------------------------------
#   pandas import html input form components
#----------------------------------------------
"""
pandas_import_html_json_title        =   "Pandas HTML Import JSON Save"
pandas_import_html_json_id           =   "importPandasHTMLJSON"

pandas_import_html_json_idList       =   ["htmljsondftitle",
                                          "jsonfilePath",
                                          None,None,None,None]

pandas_import_html_json_labelList    =   ["html_df_title",
                                          "json_file_path",
                                          "Add df</br>to dfcleanser",
                                          "Save as</br>JSON File",
                                          "Return","Help"]

pandas_import_html_json_typeList     =   ["text","file",
                                          "button","button","button","button"]

pandas_import_html_json_placeholderList = ["dataframe title",
                                           "enter file path, or choose file to store inported df to)",
                                           None,None,None,None]

pandas_import_html_json_reqList      =   [0,1]



"""
#---------------------------------------------
#   pandas import html df form components
#---------------------------------------------
"""


pandas_import_html_df_title             =   "Pandas HTML df Import"
pandas_import_html_df_id                =   "importPandasHTMLdf"

pandas_import_html_df_idList            =   ["dfdftitle",
                                             "dfnames",
                                             "dfindexcol",
                                             "dfdtype",
                                             None,None,None]

pandas_import_html_df_labelList         =   ["dataframe_title",
                                             "names",
                                             "index_col",
                                             "dtype",
                                             "Import</br>JSON Table",
                                             "Return","Help"]

pandas_import_html_df_typeList          =   ["text",makefilearea(3),maketextarea(3),makefilearea(3),
                                             "button","button","button"]

pandas_import_html_df_placeholderList   =   ["dataframe title (default 'filename'_df)",
                                             "enter Column Names file name or browse to a json file or as a List (List format - [value, value ...] (default None)",
                                             "enter column number to use for row ids (default None)",
                                             "enter Data Types file name or browse to a json file or json dict - {'col' : 'str', ...} (default None)",
                                             None,None,None]

pandas_import_html_df_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#   pandas import sqltable common mysql-mssqlserver-postgresql parms
#--------------------------------------------------------------------------
"""
pandas_import_sqltable_common_title        =   "Pandas SQL Table Import"
pandas_import_sqltable_common_id           =   "importPandasSQLCommonTable"

pandas_import_sqltable_common_idList       =    ["sqldftitle",
                                                 "sqldfhistory",
                                                 "sqltablecommontableName",
                                                 "sqltablecommonschema",
                                                 "sqltableindexcol",
                                                 "sqltablecoercefloat",
                                                 "sqltableparsedates",
                                                 "sqltablecolumns",
                                                 "sqltablechunksize",
                                                 None,None,None,None,None,None]

pandas_import_sqltable_common_labelList    =   ["dataframe_title",
                                                "sql_table_imports_history",
                                                "table_name",
                                                "schema",
                                                "index_col",
                                                "coerce_float",
                                                "parse_dates",
                                                "columns",
                                                "chunksize",
                                                "Import</br>Table",
                                                "Set</br>'columns'",
                                                "Set</br>'index_col'",
                                                "Set</br>'parse_dates'",
                                                "Return","Help"]

pandas_import_sqltable_common_typeList     =   ["text","select","select","text",maketextarea(2),"select",
                                                maketextarea(2),maketextarea(2),"text",
                                                "button","button","button","button","button","button"]

pandas_import_sqltable_common_placeholderList = ["dataframe title",
                                                 "dataframe title",
                                                 "enter the table name",
                                                 "enter the database schema  (default None)",
                                                 "enter col name or list of column names - use 'Set index_col' ... (default None)",
                                                 "convert values of non-string, non-numeric objects (default True)",
                                                 "enter col name or dict of col names : format - use 'Set parse_dates' (default : None)",
                                                 "enter col name or list of col names - use 'Set columns' (default : all columns)",
                                                 "enter chunk size in num rows (default None)",
                                                 None,None,None,None,None,None]

pandas_import_sqltable_common_reqList      =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   pandas import sqltable common mysql-mssqlserver-postgresql parms
#--------------------------------------------------------------------------
"""
pandas_2_0_import_sqltable_common_title        =   "Pandas SQL Table Import"
pandas_2_0_import_sqltable_common_id           =   "importPandasSQLCommonTable"

pandas_2_0_import_sqltable_common_idList       =    ["sqldftitle",
                                                    "sqldfhistory",
                                                    "sqltablecommontableName",
                                                    "sqltablecommonschema",
                                                    "sqltableindexcol",
                                                    "sqltablecoercefloat",
                                                    "sqltablecommondateformatlist",
                                                    "sqltablecommoncolumns",
                                                    "sqltablechunksize",
                                                    "sqltabledtypebackend", 
                                                    None,None,None,None,None,None]

pandas_2_0_import_sqltable_common_labelList    =   ["dataframe_title",
                                                "sql_table_imports_history",
                                                "table_name",
                                                "schema",
                                                "index_col",
                                                "coerce_float",
                                                "parse_dates",
                                                "columns",
                                                "chunksize",
                                                "dtypes_backend",
                                                "Import</br>Table",
                                                "Set</br>'columns'",
                                                "Set</br>'index_col'",
                                                "Set</br>'parse_dates'",
                                                "Return","Help"]

pandas_2_0_import_sqltable_common_typeList     =   ["text","select","select","text",maketextarea(2),"select",maketextarea(2),
                                                maketextarea(2),"text","select",
                                                "button","button","button","button","button","button"]

pandas_2_0_import_sqltable_common_placeholderList = ["dataframe title",
                                                 "dataframe title",
                                                 "enter the table name",
                                                 "enter the database schema  (default None)",
                                                 "enter col name or list of column names - use 'Set index_col' ... (default None)",
                                                 "convert values of non-string, non-numeric objects (default True)",
                                                 "enter col name or dict of col names : format - use 'Set parse_dates' (default : None)",
                                                 "enter col name or list of col names - use 'Set columns' (default : all columns)",
                                                 "enter chunk size in num rows (default None)",
                                                 "enter dtype backend",
                                                 None,None,None,None,None,None]

pandas_2_0_import_sqltable_common_reqList      =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   pandas import sqlquery input form components
#--------------------------------------------------------------------------
"""
pandas_import_sqlquery_title        =   "Pandas SQL Query Import"
pandas_import_sqlquery_id           =   "importPandasSQLQuery"

pandas_import_sqlquery_idList       =   ["sqlquerydftitle",
                                         "sqlquerysql",
                                         "sqlquerytableName",
                                         "sqlqueryindexcol",
                                         "sqlquerycoerce",
                                         "sqlquerysqlparms",
                                         "sqlqueryparsedates",
                                         "sqlquerydateformat",
                                         "sqlquerydateformatlist",
                                         "sqlquerychunksize",
                                         None,None,None,None,None]

pandas_import_sqlquery_labelList    =   ["dataframe_title",
                                         "sql",
                                         "table_name",
                                         "index_col",
                                         "coerce_float",
                                         "params",
                                         "parse_dates",
                                         "dates_format",
                                         "dates_format_list",
                                         "chunksize",
                                         "Run</br>SQL Query",
                                         "Set</br>'index_col'",
                                         "Set</br>'parse_dates'",
                                         "Return","Help"]

pandas_import_sqlquery_typeList     =   ["text",maketextarea(3),"select",maketextarea(1),
                                         "select",maketextarea(1),maketextarea(1),
                                         "text","select","text",
                                         "button","button","button","button","button"]

pandas_import_sqlquery_placeholderList = ["dataframe title ",
                                          "enter the sql query",
                                          "table names",
                                          "enter col name or dict of col names : format - use 'Set index_col' (default : None)",
                                          "convert values of non-string, non-numeric objects (default True)", 
                                          "enter sql parameters as list or dict of values - use single quotes (default None)",
                                          "enter col name or dict of col names : format - use 'Set parse_dates' (default : None)",
                                          "current parse date to use with parse date column",
                                          "parse and date format (default None)",
                                          "number of rows (default None)",
                                          None,None,None,None,None]

pandas_import_sqlquery_reqList      =   [0,1,2]

"""
#--------------------------------------------------------------------------
#   Custom Import input form parm lists
#--------------------------------------------------------------------------
"""
custom_import_title             =   "Custom Import Code"
custom_import_id                =   "importPandasCustomdf"
custom_import_idList            =   ["customImportdftitle",
                                     "customImporthistory",
                                     "customImportCode",
                                     None,None,None,None]

custom_import_labelList         =   ["dataframe_title",
                                     "custom_imports_history",
                                     "custom_import_code",
                                     "Run Custom </br>Import Code",
                                     "Clear",
                                     "Return","Help"]

custom_import_typeList          =   ["text","select",maketextarea(4),
                                     "button","button","button","button"]

custom_import_placeholderList   =   ["dataframe title",
                                     "dataframe title history",
                                     "# custom import ",
                                     None,None,None,None]

custom_import_reqList           =   [0,1,2]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser import form objects objects end
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   CSV Import Parms
#--------------------------------------------------------------------------
"""
csv_import_parms                 =   ["filepath_or_buffer","header","names","index_col","dtype"]
csv_import_parms_dtypes          =   [str,int,list,int,list]
csv_import_parms_defaults        =   [None,'infer',None,None,None]

csv_import_addl_parms            =   ["sep","delimiter","usecols",
                                      "engine","converters","true_values","false_values",
                                      "skipinitialspace","skiprows","skipfooter","nrows","na_values",
                                      "keep_default_na","na_filter","verbose","skip_blank_lines","parse_dates",
                                      "keep_date_col","date_format","dayfirst ","cache_dates",
                                      "iterator","chunksize","compression","thousands","decimal",
                                      "lineterminator","quotechar","quoting","doublequote","escapechar",
                                      "comment","encoding","encoding_errors","dialect","on_bad_lines",
                                      "delim_whitespace","low_memory","memory_map","float_precision","storage_options",
                                      "dtype_backend"
                                     ]

csv_import_addl_parms_dtypes     =   [str,str,bool,
                                      str,dict,list,list,
                                      bool,[int,list],int,int,[str,list,dict],
                                      bool,bool,bool,bool,[bool,list,dict],
                                      bool,str,bool,bool,
                                      bool,int,str,str,str,
                                      str,str,int,bool,str,
                                      str,str,str,str,str,
                                      bool,bool,bool,str,dict,
                                      str
                                     ]

csv_import_addl_parms_defaults   =   [',',None,None,
                                      None,None,None,None,
                                      False,None,0,None,None,
                                      True,True,False,True,None,
                                      False,None,False,True,
                                      False,None,'infer',None,'.',
                                      None,None,0,True,None,
                                      None,None,"strict",None,"error",
                                      False,True,False,None,None,
                                      None
                                     ]

"""
#--------------------------------------------------------------------------
#   Fixed Width File Import Parms
#--------------------------------------------------------------------------
"""
fwf_import_parms                 =   ["filepath_or_buffer","delimiter","header","names","index_col","dtype"]
fwf_import_parms_dtypes          =   [str,str,int,list,int,list]
fwf_import_parms_defaults        =   [None,' ',None,None,None,None]

fwf_import_addl_parms            =   ["colspecs","widths","infer_nrows","dtype_backend"]

fwf_import_addl_parms_dtypes     =   [list,[list],int,None]

fwf_import_addl_parms_defaults   =   ['infer',None,100,None]

"""
#--------------------------------------------------------------------------
#   Excel Import Parms
#--------------------------------------------------------------------------
"""
excel_import_parms                  =   ["io","sheet_name","header","names","index_col","dtype"]
excel_import_parms_dtypes           =   [str,[str,int,list],[int,list],list,[int,list],dict]
excel_import_parms_defaults         =   [None,0,0,None,None,None]

excel_import_addl_parms             =   ["usecols","engine","converters","true_values",
                                         "false_values","skiprows","nrows","na_values","keep_default_na",
                                         "na_filter","verbose","parse_dates","date_format","thousands",
                                         "comment","skipfooter","mangle_dupe_cols","storage_options","dtype_backend"
                                        ]

excel_import_addl_parms_dtypes      =   [[int,list],str,dict,list,
                                         list,[int,list],int,[str,list,dict],bool,
                                         bool,bool,[bool,list,dict],str,str,
                                         str,int,bool,dict,str
                                        ]
                                         
excel_import_addl_parms_defaults    =   [None,None,None,None,
                                         None,None,None,None,True,
                                         True,False,False,None,None,
                                         None,0,True,None,None
                                        ]
                                         
"""
#--------------------------------------------------------------------------
#   JSON Import Parms
#--------------------------------------------------------------------------
"""
json_import_parms                   =   ["path_or_buf","orient","typ","dtype"]
json_import_parms_dtypes            =   [str,str,str,[bool,dict]]
json_import_parms_defaults          =   [None,None,'frame',None]


json_import_addl_parms              =   ["convert_axes","convert_dates","keep_default_dates","precise_float","date_unit",
                                         "encoding","encoding_errors",
                                         "lines","chunksize","compression","nrows",
                                         "storage_options","dtype_backend","engine"
                                        ]

json_import_addl_parms_dtypes       =   [bool,[bool,list],bool,bool,str,
                                         str,str,
                                         bool,int,str,int,
                                         [dict],str,str
                                        ]
                                         
json_import_addl_parms_defaults     =   [None,True,True,False,None,
                                         'utf-8',"strict",
                                         False,None,'infer',None,
                                         None,None,None
                                        ]

"""
#--------------------------------------------------------------------------
#   HTML Import Parms
#--------------------------------------------------------------------------
"""                                         
html_import_parms                   =   ["match","flavor","header"]
html_import_parms_dtypes            =   [str,str,[int,list]]
html_import_parms_defaults          =   [".+",None,None]

html_import_addl_parms              =   ["index_col","skiprows","attrs","parse_dates",
                                         "thousands","encoding","decimal","converters",
                                         "na_values","keep_default_na","displayed_only",
                                         "extract_links","dtype_backend"
                                        ]
                                         
html_import_addl_parms_dtypes       =   [[int,list],[int,list],dict,bool,
                                         str,str,str,dict,
                                         str,bool,bool,
                                         str,str
                                        ]
                                         
html_import_addl_parms_defaults     =   [None,None,None,False,
                                         ',',None,'.',None,
                                         None,True,True,
                                         None,None
                                        ]


def get_addl_parm_dtype(detid,parmname) :
    
    if(detid == CSV_IMPORT) :   
        parm_names   =   csv_import_addl_parms
        parm_dtypes  =   csv_import_addl_parms_dtypes
    elif(detid == FWF_IMPORT) :   
        parm_names   =   fwf_import_addl_parms
        parm_dtypes  =   fwf_import_addl_parms_dtypes
    elif(detid == EXCEL_IMPORT) :   
        parm_names   =   excel_import_addl_parms
        parm_dtypes  =   excel_import_addl_parms_dtypes
    elif(detid == JSON_IMPORT) :   
        parm_names   =   json_import_addl_parms
        parm_dtypes  =   json_import_addl_parms_dtypes
    elif(detid == HTML_IMPORT) :   
        parm_names   =   html_import_addl_parms
        parm_dtypes  =   html_import_addl_parms_dtypes

    for i in range(len(parm_names)) :
        if(parm_names[i] == parmname) :
            return(parm_dtypes[i])
        
    return(None)

"""
#--------------------------------------------------------------------------
#   SQL Table Import Parms
#--------------------------------------------------------------------------
"""                                         
sqlt_import_parms                   =   ["table_name","schema","index_col","coerce_float","parse_dates","columns","chunksize"]
sqlt_import_parms_dtypes            =   [str,str,[str,list],bool,[dict,list],str,str,list,int]
sqlt_import_parms_defaults          =   [None,None,None,True,None,None,None]


"""
#--------------------------------------------------------------------------
#   SQL Query Import Parms
#--------------------------------------------------------------------------
"""                                         
sqlq_import_parms                   =   ["sql","index_col","coerce_float","params","parse_dates","chunksize"]
sqlq_import_parms_dtypes            =   [str,[str,list],bool,[dict,list],[dict,list],int]
sqlq_import_parms_defaults          =   [None,None,True,None,None,None]



def get_addl_parms_names(importflag, importid) :

    if(importflag == 0) :
    
        if(importid       ==  CSV_IMPORT)   :   return(csv_import_addl_parms)
        elif(importid     ==  FWF_IMPORT)   :   return(fwf_import_addl_parms)
        elif(importid     ==  EXCEL_IMPORT) :   return(excel_import_addl_parms)
        elif(importid     ==  JSON_IMPORT)  :   return(json_import_addl_parms)
        else                                :   return(html_import_addl_parms)

    else :

        from dfcleanser.Qt.data_export.DataExportModel import (CSV_EXPORT, EXCEL_EXPORT, JSON_EXPORT)
        from dfcleanser.Qt.data_export.DataExportModel import (csv_export_addl_parms, excel_export_addl_parms, json_export_addl_parms, html_export_addl_parms)

        if(importid       ==  CSV_EXPORT)   :   return(csv_export_addl_parms)
        elif(importid     ==  EXCEL_EXPORT) :   return(excel_export_addl_parms)
        elif(importid     ==  JSON_EXPORT)  :   return(json_export_addl_parms)
        else                                :   return(html_export_addl_parms)



def get_addl_parms_types(importflag, importid) :

    if(importflag == 0) :
    
        if(importid     ==  CSV_IMPORT)     :   return(csv_import_addl_parms_dtypes)
        elif(importid     ==  FWF_IMPORT)   :   return(fwf_import_addl_parms_dtypes)
        elif(importid     ==  EXCEL_IMPORT) :   return(excel_import_addl_parms_dtypes)
        elif(importid     ==  JSON_IMPORT)  :   return(json_import_addl_parms_dtypes)
        else                                :   return(html_import_addl_parms_dtypes)

    else :

        from dfcleanser.Qt.data_export.DataExportModel import (CSV_EXPORT, EXCEL_EXPORT, JSON_EXPORT)
        from dfcleanser.Qt.data_export.DataExportModel import (csv_export_addl_parms_dtypes, excel_export_addl_parms_dtypes, json_export_addl_parms_dtypes, html_export_addl_parms_dtypes)
        
        if(importid       ==  CSV_EXPORT)   :   return(csv_export_addl_parms_dtypes)
        elif(importid     ==  EXCEL_EXPORT)  :  return(excel_export_addl_parms_dtypes)
        elif(importid     ==  JSON_EXPORT)  :   return(json_export_addl_parms_dtypes)
        else                                :   return(html_export_addl_parms_dtypes)


def get_addl_parms_defaults(importflag, importid) :

    if(importflag == 0) :
    
        if(importid     ==  CSV_IMPORT)     :   return(csv_import_addl_parms_defaults)
        elif(importid     ==  FWF_IMPORT)   :   return(fwf_import_addl_parms_defaults)
        elif(importid     ==  EXCEL_IMPORT) :   return(excel_import_addl_parms_defaults)
        elif(importid     ==  JSON_IMPORT)  :   return(json_import_addl_parms_defaults)
        else                                :   return(html_import_addl_parms_defaults)

    else :

        from dfcleanser.Qt.data_export.DataExportModel import (CSV_EXPORT, EXCEL_EXPORT, JSON_EXPORT)
        from dfcleanser.Qt.data_export.DataExportModel import (csv_export_addl_parms_defaults, excel_export_addl_parms_defaults, json_export_addl_parms_defaults, html_export_addl_parms_defaults)

        if(importid     ==  CSV_EXPORT)     :   return(csv_export_addl_parms_defaults)
        elif(importid     ==  EXCEL_EXPORT) :   return(excel_export_addl_parms_defaults)
        elif(importid     ==  JSON_EXPORT)  :   return(json_export_addl_parms_defaults)
        else                                :   return(html_export_addl_parms_defaults)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser import history class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

class DataframeCleanserHistoryParms() :

     
    
    # full constructor
    def __init__(self,importtype,filetype,dftitle,fullparms,addlparms) :
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("DataframeCleanserHistoryParms : init",importtype,filetype,dftitle,"\n  ",fullparms,"\n  ",addlparms)
        
        self.import_type        =   importtype
        self.file_type          =   filetype
        self.df_title           =   dftitle
        self.full_parms         =   fullparms
        self.addl_parms         =   addlparms
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :   
            print("DataframeCleanserHistoryParms - self",self.import_type ,self.file_type,self.df_title,self.full_parms,self.addl_parms)     
        
    def get_import_type(self) :
        return(self.import_type)
    
    def get_file_type(self) :
        return(self.file_type)

    def get_df_title(self) :
        return(self.df_title)

    def get_full_parms(self) :
        return(self.full_parms)

    def get_addl_parms(self) :
        return(self.addl_parms)
    
    def dump(self) :
        print("\n    import_type : ",type(self.import_type),self.import_type)
        print("    file_type   : ",type(self.file_type),self.file_type)
        print("    df_title    : ",type(self.df_title),self.df_title)
        print("    full_parms  : ",type(self.full_parms),self.full_parms)
        print("    addl_parms  : ",type(self.addl_parms),self.addl_parms)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser import/Export history class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

IMPORT_HISTORY  =   0
EXPORT_HISTORY  =   1

class DataframeCleanserHistory :
    
    # instance variables
    
    # notebook specific import history data
    notebook_history            =   {}
    default_history             =   {}
    history_file_loaded         =   False
    history_type                =   None
    
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self,history_type) :
        
        self.history_type               =   history_type
        self.notebook_history           =   {}
        
        self.history_file_loaded        =   False
        self.load_history_file()



    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser import history files methods
    #--------------------------------------------------------------------------
    """
    
    def get_history_dir_name(self,history_type) :
        
        import os
        
        from dfcleanser.common.cfg import DataframeCleansercfg
        
        #nbdir   =   DataframeCleansercfg.get_notebookpath()
        #nbname  =   DataframeCleansercfg.get_notebookname()
        return(str(cfg.get_dfcleanser_location()+"files"))
        #if((nbdir is None)or(nbname is None)) :
        #    return(None)
        #else :
        #    return(os.path.join(nbdir,nbname + "_files"))
    
    def get_history_file_name(self,history_type) :
        
        #import os
        
        from dfcleanser.common.cfg import DataframeCleansercfg
        
        cfgdir  =   DataframeCleansercfg.get_cfg_dir_name()
        nbname  =   DataframeCleansercfg.get_notebookname()
        file_loc    =   str(cfg.get_dfcleanser_location()+"files")
        if(0):#(cfgdir is None)or(nbname is None)) :
            return(None)
        else :
            if(history_type == IMPORT_HISTORY) :
                return("dfcleanserCommon_import_history.json") 
            else :
                return("dfcleanserCommon_export_history.json") 

    def get_history_full_file_name(self,history_type) :
        
        import os
        
        from dfcleanser.common.cfg import DataframeCleansercfg
        
        cfgdir  =   self.get_history_dir_name(history_type)#DataframeCleansercfg.get_cfg_dir_name()
        #nbname  =   DataframeCleansercfg.get_notebookname()
        
        if(0):#(cfgdir is None)or(nbname is None)) :
            return(None)
        else :
            if(history_type == IMPORT_HISTORY) :
                return(os.path.join(cfgdir,"dfcleanserCommon_import_history.json")) 
            else :
                return(os.path.join(cfgdir,"dfcleanserCommon_export_history.json")) 

    def load_history_file(self) :
        
        import json

        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n[load_history_file] : self.history_file_loaded  ",self.history_file_loaded )

        history_data             =   []
        
        history_dir_name         =   self.get_history_dir_name(self.history_type)
        history_file_name        =   self.get_history_file_name(self.history_type)
        history_full_file_name   =   self.get_history_full_file_name(self.history_type)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("load_history_file",history_dir_name,"\n",history_file_name,"\n",history_full_file_name)
        
        if(not (history_dir_name is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist, make_dir
            if(not (does_dir_exist(history_dir_name))) :
                make_dir(history_dir_name)
            
            from dfcleanser.common.common_utils import does_file_exist
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("[load_history_file] : does_file_exist ",does_file_exist(history_full_file_name))
            
            if(not (does_file_exist(history_full_file_name))) :
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("load_history_file - file not found\n",history_full_file_name)
                    print("load_history_file - file not found : history type",self.history_type)
 
                self.history_file_loaded    =   False    
                self.notebook_history       =   {}
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("load_history_file - file not found : history length ",len(self.notebook_history))
                    self.dump_history()
            
            # import history file does exist
            else :
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("[load_history_file]  - file found\n  ",history_full_file_name)
                
                try :

                    with open(history_full_file_name,'r') as  history_file :
                            
                        history_data = json.load(history_file)
                        history_file.close()

                    if(DEBUG_IMPORT_HISTORY_DETAILS) :
                        print("[load_history_file]  - history_data  ",type(history_data),len(history_data))
                    
                    self._parse_history_file_to_dict(history_data)
                    self.history_file_loaded = True
                    
                    if(DEBUG_IMPORT_HISTORY_DETAILS) :
                        print("[load_history_file]  - self.history_file_loaded  ",self.history_file_loaded)
                        
                except :
                        
                    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
                    add_error_to_log("[Load history file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("[load_history_file] - complete : ",self.history_file_loaded)

    def save_history_file(self) :
        
        import json
        
        history_data     =   []
        
        history_dir_name     =   self.get_history_dir_name(self.history_type)
        history_file_name    =   self.get_history_full_file_name(self.history_type)
            
        from dfcleanser.common.common_utils import does_dir_exist, make_dir
        if(not (does_dir_exist(history_dir_name))) :
            make_dir(history_dir_name)
            
        history_data     =   self._parse_history_dict_to_list()  
            
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\nhistory_data")
            for i in range(len(history_data)) :
                print("history",history_data[i])
            
        try :
                    
            with open(history_file_name, 'w') as  history_file :
                json.dump(history_data,history_file)
                history_file.close()
                    
            if(DEBUG_IMPORT_HISTORY) :
                print("import history file saved ok")
                            
        except :
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[Save dfc cfg file Error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

    def _parse_history_file_to_dict(self,history_file) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history file into a dict
        * 
        * parms :
        *  history_file     -   history_file to convert                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        total_entries    =   len(history_file)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n[parse_history_file_to_dict]  ",self.history_type,type(history_file),total_entries,"\n")
            for i in range(total_entries) :
                print("    [",i,"] ",history_file[i])
        
        try :
       
            for i in range(total_entries) :
            
                file_type           =   history_file[i][0]
                df_title            =   history_file[i][1]
                parms               =   history_file[i][2]
                addl_keys           =   history_file[i][3]
                addl_vals           =   history_file[i][4]
            
                addl_parms_dict     =   {}
                for j in range(len(addl_keys)) :
                    addl_parms_dict.update({addl_keys[j] : addl_vals[j]})
                
                history_entry    =   DataframeCleanserHistoryParms(self.history_type,file_type,df_title,parms,addl_parms_dict)
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\n[_parse_history_file_to_dict] - history_entry[",i,"]")
                    history_entry.dump()
            
                self._add_entry_to_history_dict(history_entry)

        except Exception as e:
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[_parse_history_file_to_dict Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
            
            title       =   "dfcleanser exception"
            status_msg  =   "[parse import/export file] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


    
    def _add_entry_to_history_dict(self,history_entry) :
        """
        * -------------------------------------------------------- 
        * function : add an import history entry to the dict
        * 
        * parms :
        *  history_file     -   history_file to convert                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        opstat  =   opStatus()
        
        try :
            
            type_dict    =   self.notebook_history.get(history_entry.get_file_type())
        
            if(type_dict is None) :
        
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_entry_to_history_dict - no import_type_dict")
                    print("add_entry_to_import_history_dict - history_entry.get_df_title()",history_entry.get_df_title())
                
                df_titles_dict  =   {}
                df_titles_dict.update({ history_entry.get_df_title() : history_entry})
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_entry_to_history_dict - df_titles_dict",len(df_titles_dict))
                    print(list(df_titles_dict.keys()))
            
                self.notebook_history.update({history_entry.get_file_type() : df_titles_dict })
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_entry_to_import_history_dict - notebook_history",len(self.notebook_history))
            
            else :
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_entry_to_history_dict - type_dict",len(type_dict))
                    history_entry.dump()

            
                df_titles_dict  =   self.notebook_history.get(history_entry.get_file_type())
                df_titles_dict.update({ history_entry.get_df_title() : history_entry})
            
                self.notebook_history.update({ history_entry.get_file_type() : df_titles_dict })
            
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[add_entry_to_history_dict] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            add_error_to_log("[add_entry_to_history_dict] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


 

    def _parse_history_dict_to_list(self) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history dict to a list 
        * 
        * parms :
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n\nparse_history_dict_to_list")
            self.dump_history()
        
        try :
        
            history_data_list    =   []
        
            history_types    =   list(self.notebook_history.keys())
            history_types.sort()
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("\nparse_history_dict_to_list - history types",history_types)
        
            for i in range(len(history_types)) :
                df_titles_dict  =   self.notebook_history.get(history_types[i])
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nparse_history_dict_to_list - history_type : ",history_types[i])
                    print("    df_titles_dict",len(df_titles_dict))
            
            
                df_titles    =   list(df_titles_dict.keys())
                df_titles.sort()
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nparse_history_dict_to_list - df_titles",len(df_titles)," : ",df_titles)

                for j in range(len(df_titles)) :
                
                    history_entry        =   df_titles_dict.get(df_titles[j])
                
                    if(DEBUG_IMPORT_HISTORY_DETAILS) :
                        print("\nparse_history_dict_to_list - import_entry[",j,"]",type(history_entry),history_entry)
                
                    history_entry_list   =   []
                
                    history_entry_list.append(history_entry.get_file_type())
                    history_entry_list.append(history_entry.get_df_title())
                    history_entry_list.append(history_entry.get_full_parms())
                
                    history_entry_addl_parms_dict    =  history_entry.get_addl_parms() 
                
                    if(not (history_entry_addl_parms_dict is None)) :
                    
                        addl_parms_keys    =   list(history_entry_addl_parms_dict.keys())
                        addl_parms_keys.sort()
                
                        addl_parms_keys_list    =   []
                        addl_parms_vals_list    =   []
                
                        for k in range(len(addl_parms_keys)) :
                    
                            addl_parms_keys_list.append(addl_parms_keys[k])
                            addl_parms_vals_list.append(history_entry_addl_parms_dict.get(addl_parms_keys[k]))
                
                    else :
                    
                        addl_parms_keys_list    =   []
                        addl_parms_vals_list    =   []
                    
                    history_entry_list.append(addl_parms_keys_list)
                    history_entry_list.append(addl_parms_vals_list)
                    
                    history_data_list.append(history_entry_list)
                
            return(history_data_list)
    
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[parse_history_dict_to_list] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
            
            add_error_to_log("[parse_history_dict_to_list] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser import history entry methods
    #--------------------------------------------------------------------------
    """

    def get_df_titles_for_file_type(self,fileType) :
        """
        * -------------------------------------------------------- 
        * function : get all import df titles for a file type 
        * 
        * parms :
        *  fileType     -   type of import                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n[get_df_titles_for_file_type] : fileType : self.history_file_loaded",fileType,self.history_file_loaded)
            print("[get_df_titles_for_file_type ]: file name ",self.get_history_full_file_name(self.history_type))
            
        if(not (self.history_file_loaded)) :
            self.load_history_file()    
        
        df_titles_dict  =   self.notebook_history.get(fileType)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\ndf_titles_dict : ",fileType,"\n",df_titles_dict)
        
        if(not (df_titles_dict is None)) :
            
            df_titles_list  =   list(df_titles_dict.keys())
            
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("\ndf_titles_list",df_titles_list)
                self.dump_history()
            
            if(not (df_titles_list is None)) :
                df_titles_list.sort()
                return(df_titles_list)
            else :
                return(None)
            
        else :
            
            return(None)
        
    def add_to_history(self,filetype,dfTitle,fullParms,addlParms) :
        """
        * -------------------------------------------------------- 
        * function : add a new import to history table
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *  fullParms    -   import full parms                    
        *  addlParms    -   additional prms                   
        *
        * returns : N/A
        * --------------------------------------------------------
        """
       
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n  [add_to_history] : filetype : dftitle : ",filetype,dfTitle)
            self.dump_history()    
        
        try :
            
            new_entry    =   DataframeCleanserHistoryParms(self.history_type,filetype,dfTitle,fullParms,addlParms)
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("  [add_to_history] : df : ",dfTitle," history type : ",self.history_type," filetype : ",filetype,"\n fullparms : ",fullParms,"\n addlparms : ",addlParms)
                print("  [add_to_history] - new_entry - dump")
                new_entry.dump()
            
            df_titles_dict  =   self.notebook_history.get(filetype)
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("  [add_to_history] : df_titles_dict\n",df_titles_dict)

            if(df_titles_dict is None) :
            
                new_type_dict    =   {}
                new_type_dict.update({dfTitle : new_entry})
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_to_history : new_type_dict",new_type_dict,filetype)
            
                self.notebook_history.update({filetype : new_type_dict})
            
            else :
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("  [add_to_history] - df_titles_dict : ",type(df_titles_dict),len(df_titles_dict))
            
                df_titles_dict.update({dfTitle : new_entry})    
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("  [add_to_history] - df_titles_dict : ",type(df_titles_dict),len(df_titles_dict),"\n dict : ",df_titles_dict)

                self.notebook_history.update({filetype : df_titles_dict})
        
            self.save_history_file() 
        
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[add_to_history] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            add_error_to_log("[add_to_history] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("  [add_import_to_history] - new_history : ")
            self.dump_history()

    def delete_from_history(self,filetype,dfTitle) :
        """
        * -------------------------------------------------------- 
        * function : adelete import from history table
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *
        * returns : N/A
        * --------------------------------------------------------
        """
       
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY) :
            print("\ndelete_from_history\n",filetype,"\n",dfTitle)
            
        df_titles_dict  =   self.notebook_history.get(filetype)
        
        if(not (df_titles_dict is None) ) :
            
            try :
                
                df_titles_dict.pop(dfTitle)
                self.save_history_file() 
                
            except Exception as e:

                opstat.set_status(False)

                title       =   "dfcleanser exception"
                status_msg  =   "[delete_from_history] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
            
                add_error_to_log("[delete_from_history] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

        
    def get_df_title_entry(self,fileType,dfTitle) :
        """
        * -------------------------------------------------------------------- 
        * function : get the import history entry for a file type and dftitle
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *
        * returns : N/A
        * -------------------------------------------------------------------
        """
        
        if(DEBUG_IMPORT_HISTORY_DETAILS):
            print("    [get_df_title_entry] : filetype : ",fileType," dftitle : ",dfTitle)
        
        if(not (self.history_file_loaded)) :
            self.load_history_file()    
        
        df_titles_dict  =   self.notebook_history.get(fileType)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS):
            dict_keys = list(df_titles_dict.keys())
            print("    [get_df_title_entry] : dftitles dict keys : \n   ",dict_keys)

        if(df_titles_dict is None) :
            return(None)
        else :
            
            if( (DEBUG_IMPORT_HISTORY_DETAILS) ):
                print("    [get_df_title_entry] : dfTitle len : ",len(dfTitle),dfTitle)

            df_title_dict   =   df_titles_dict.get(dfTitle)
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("    [get_df_title_entry] : df_title_dict : ",type(df_title_dict))
                if(not (df_title_dict is None)) :
                    df_title_dict.dump()
            
            return(df_title_dict)
             
    def dump_history(self) :
        """
        * -------------------------------------------------------------------- 
        * function : dump the history table
        * 
        * parms :
        *
        * returns : N/A
        * -------------------------------------------------------------------
        """
        
        hkeys   =   list(self.notebook_history.keys())
        
        print("\nhkeys",hkeys)
        
        for i in range(len(hkeys)) :
            print("\nfile type : ",hkeys[i])
            ftdict  =   self.notebook_history.get(hkeys[i])
            ftkeys  =   list(ftdict.keys())
            
            for j in range(len(ftkeys)) :
                print("\ndftitle : ",ftkeys[j])
                ftdict.get(ftkeys[j]).dump()


"""
* ----------------------------------------------------
# static instantiation of the history objects
* ----------------------------------------------------
"""    
ImportHistory   =   DataframeCleanserHistory(IMPORT_HISTORY)
ExportHistory   =   DataframeCleanserHistory(EXPORT_HISTORY)




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Import parms helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""

#--------------------------------------------------------------------------
#   dftitles methods
#--------------------------------------------------------------------------
"""

def get_dftitles_list(historytype,detid) :
    """
    * ------------------------------------------------------------ 
    * function : get_dftitles_list
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * ------------------------------------------------------------
    """
    
    #opstat  =   opStatus()

    if(DEBUG_IMPORT_FILE) :
        print("    [get_dftitles_list] : historytype :  detid : ",historytype,detid)

    
    if(historytype  ==  IMPORT_HISTORY) :
        history_df_titles        =   ImportHistory.get_df_titles_for_file_type(detid)
    else :
        history_df_titles        =   ExportHistory.get_df_titles_for_file_type(detid)
        
    return(history_df_titles)


def get_last_dftitle(detid,df_titles) :
    """
    * ------------------------------------------------------------ 
    * function : get_last_dftitle
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * ------------------------------------------------------------
    """
    
    if(DEBUG_IMPORT_FILE) :
        print("    [get_last_dftitle] :  detid : ",detid,"\n       dftitles : ",df_titles)

    formid                  =   get_formid_for_import(detid) + "Parms"
    last_history_cfg_data   =   get_config_value(formid)
    
    if(DEBUG_IMPORT) :
        print("    [get_last_dftitle] :  last_history_cfg_data : \n    ",last_history_cfg_data)

    if(not (last_history_cfg_data is None)) :

        if( not (is_valid_import_cfg_parms(detid,last_history_cfg_data)))  :
            last_history_cfg_data   =    None
            add_error_to_log("[Invalid cfg values for : " + formid + "]",SEVERE_ERROR)

    if(not (last_history_cfg_data is None) and (not (last_history_cfg_data[SQL_CFG_DF_NAME_ID] == ""))) :
        last_df_title   =   SQLTableImportData.get_sql_parm_from_cfg_value(last_history_cfg_data,SQL_CFG_DF_NAME_ID)
    else :
        if( (not (df_titles is None)) and (len(df_titles) > 0) ) :
            last_df_title   =   df_titles[0]
        else :
            last_df_title           =   None 
    
    return(last_df_title) 

"""
#--------------------------------------------------------------------------
#   parms and data
#--------------------------------------------------------------------------
"""

def get_Parms_cfg_value_for_import(importType,import_full_parms,import_input_parms) :

    if(DEBUG_IMPORT_FILE):
        print("get_Parms_cfg_value_for_import : importType : ",importType,"\n full_parms : ",import_full_parms,"\n input_parms : ",import_input_parms)
    
    import json
    
    if(importType == CSV_IMPORT) :

        if(len(import_full_parms) == 5) :
        
            if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
                if(import_full_parms[0] == csv_import_parms_defaults[0]) :
                    path    =   import_full_parms[0]
                else :
                    path    =   str(import_full_parms[0])
            else :
                path    =   ""
                    
            if(not ((import_full_parms[1] is None) or (len(import_full_parms[1]) == 0)) ) :
                if(import_full_parms[1] == csv_import_parms_defaults[1]) :
                    header  =   import_full_parms[1]
                else :
                    header  =   int(import_full_parms[1])
            else :
                header  =   ""
                
            if( (not (import_full_parms[2] is None)) and (len(import_full_parms[2]) > 0) ) :
                try :
                    cnames   =   import_full_parms[2]
                    try :
                        names   =   json.dumps(cnames)    
                    except :
                        names   =   ""
                        add_error_to_log("[dump cnames] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

                except :
                    names   =   ""
                    add_error_to_log("[dump cnames] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                names   =   "" 
                add_error_to_log("[dump cnames] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    
            if(not ( (import_full_parms[3] is None) or (len(import_full_parms[3]) == 0) )) :
                index   =   int(import_full_parms[3])
            else :
                index   =   ""
                        
            if(not ( (import_full_parms[4] is None) or (len(import_full_parms[4]) == 0) )) :
                try :
                    dtypes  =   json.loads(import_full_parms[4])
                except :
                    dtypes  =   ""
                    add_error_to_log("[json.loads] " + import_full_parms[4] + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                dtypes   =   ""
        
            import_input_parms.append(path)            
            import_input_parms.append(header)
            import_input_parms.append(names)    
            import_input_parms.append(index)
            import_input_parms.append(dtypes) 

        else :
            
            import_parms_err_txt = ""

            for i in range(5) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import CSV entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)
           
               
    elif(importType == FWF_IMPORT) : 

        if(len(import_full_parms) == 6) :
                
            if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
                if(import_full_parms[0] == fwf_import_parms_defaults[0]) :
                    path    =   import_full_parms[0]
                else :
                    path    =   str(import_full_parms[0])
            else :
                path    =   ""
                
            if(not ((import_full_parms[1] is None) or (len(import_full_parms[1]) == 0)) ) :
                delimiter  =   import_full_parms[1]
            else :
                delimiter  =   ""
                
            if(not ((import_full_parms[2] is None) or (len(import_full_parms[2]) == 0)) ) :
                if(import_full_parms[2] == fwf_import_parms_defaults[2]) :
                    header  =   import_full_parms[2]
                else :
                    header  =   int(import_full_parms[2])
            else :
                header  =   ""
                
            if(not ( (import_full_parms[3] is None) or (len(import_full_parms[3]) == 0) )) :
                try :
                    cnames   =   import_full_parms[3]
                    try :
                        names   =   json.dumps(cnames)    
                    except :
                        names   =   ""
                        add_error_to_log("[json.dumps] " + cnames + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

                except :
                    names   =   ""
                    add_error_to_log("[json.dumps] " + cnames + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                names   =   ""
                    
            if(not ( (import_full_parms[4] is None) or (len(import_full_parms[4]) == 0) )) :
                index   =   int(import_full_parms[4])
            else :
                index   =   ""
                        
            if(not ( (import_full_parms[5] is None) or (len(import_full_parms[5]) == 0) )) :
                try :
                    dtypes  =   json.loads(import_full_parms[5])
                except :
                    dtypes  =   ""
                    add_error_to_log("[json.loads] " + import_full_parms[5] + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                dtypes   =   ""
        
            import_input_parms.append(path)        
            import_input_parms.append(delimiter)    
            import_input_parms.append(header)
            import_input_parms.append(names)    
            import_input_parms.append(index)
            import_input_parms.append(dtypes) 

        else :
            
            import_parms_err_txt = ""

            for i in range(6) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import FWF entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)
           
        
    elif(importType == EXCEL_IMPORT) : 
        
        if(len(import_full_parms) == 6) :
               
            if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
                if(import_full_parms[0] == excel_import_parms_defaults[0]) :
                    path    =   import_full_parms[0]
                else :
                    path    =   str(import_full_parms[0])
            else :
                path    =   ""
        
            if(not (import_full_parms[1] is None) ) :
                sheet_name  =   int(import_full_parms[1])
            else :
                sheet_name  =   ""
                
            if(not (import_full_parms[2] is None) ) :
                if(import_full_parms[2] == excel_import_parms_defaults[2]) :
                    header  =   import_full_parms[2]
                else :
                    header  =   int(import_full_parms[2])
            else :
                header  =   ""
                
            if( (not (import_full_parms[3] is None)) and (len(import_full_parms[3]) > 0) ) :
                try :
                    cnames   =   import_full_parms[3]
                    try :
                        names   =   json.dumps(cnames)    
                    except :
                        names   =   ""
                        add_error_to_log("[json.dumps] " + cnames + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

                except :
                    names   =   ""
                    add_error_to_log("[json.dumps] " + cnames + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                names   =   ""  
                    
            if(not ( (import_full_parms[4] is None) or (len(import_full_parms[4]) == 0) )) :
                index   =   int(import_full_parms[4])
            else :
                index   =   ""
                        
            if(not ( (import_full_parms[5] is None) or (len(import_full_parms[5]) == 0) )) :
                try :
                    dtypes  =   json.loads(import_full_parms[5])
                except :
                    dtypes  =   ""
                    add_error_to_log("[json.loads] " + import_full_parms[5] + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                dtypes   =   ""
        
            import_input_parms.append(path)        
            import_input_parms.append(str(sheet_name))    
            import_input_parms.append(header)
            import_input_parms.append(names)    
            import_input_parms.append(index)
            import_input_parms.append(dtypes) 
        
        else :
            
            import_parms_err_txt = ""

            for i in range(6) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import EXCEL entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)


    elif(importType == JSON_IMPORT) : 

        if(len(import_full_parms) == 4) :
                
            if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
                if(import_full_parms[0] == json_import_parms_defaults[0]) :
                    path    =   import_full_parms[0]
                else :
                    path    =   str(import_full_parms[0])
            else :
                path    =   ""
                
            if(not ((import_full_parms[1] is None) or (len(import_full_parms[1]) == 0)) ) :
                orient  =   import_full_parms[1]
            else :
                orient  =   ""
                
            if(not ((import_full_parms[2] is None) or (len(import_full_parms[2]) == 0)) ) :
                jtype  =   import_full_parms[2]
            else :
                jtype  =   ""
                        
            if(not ( (import_full_parms[3] is None) or (len(import_full_parms[3]) == 0) )) :
                try :
                    dtypes  =   json.load(import_full_parms[3])
                except :
                    dtypes  =   ""
                    add_error_to_log("[json.load] " + import_full_parms[3] + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                dtypes   =   ""
        
            import_input_parms.append(path)        
            import_input_parms.append(orient)    
            import_input_parms.append(jtype)
            import_input_parms.append(dtypes) 

        else :
            
            import_parms_err_txt = ""

            for i in range(4) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import JSON entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)
          

    elif(importType == HTML_IMPORT) : 

        if(len(import_full_parms) == 3) :

            if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
                match  =   import_full_parms[0]
            else :
                match  =   ""
                
            if(not ((import_full_parms[1] is None) or (len(import_full_parms[1]) == 0)) ) :
                flavor  =   import_full_parms[1]
            else :
                flavor  =   ""
                        
            if(not ( (import_full_parms[2] is None) or (len(import_full_parms[2]) == 0) )) :
                try :
                    header  =   int(import_full_parms[2])
                except :
                    header  =   ""
                    add_error_to_log("[json.load] " + import_full_parms[2] + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

            else :
                header   =   ""
        
            import_input_parms.append(match)    
            import_input_parms.append(flavor)
            import_input_parms.append(header) 

        else :
            
            import_parms_err_txt = ""

            for i in range(3) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import HTML entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)

    
    elif(importType == SQLTABLE_IMPORT) :

        if(DEBUG_IMPORT_FILE) :
            print("get_Parms_cfg_value_for_import : len : ",len(import_full_parms),"\n import_full_parms : ",import_full_parms)


        if(len(import_full_parms) == 11) :
        
            if(not ((import_full_parms[2] is None) or (len(import_full_parms[2]) == 0)) ) :
                tablename  =   import_full_parms[2]
            else :
                tablename  =   sqlt_import_parms_defaults[0]
                    
            if(not ((import_full_parms[3] is None) or (len(import_full_parms[3]) == 0)) ) :
                schema  =   import_full_parms[3]
            else :
                schema  =   sqlt_import_parms_defaults[1]
                
            if( (not (import_full_parms[4] is None)) and (len(import_full_parms[4]) > 0) ) :
                try :
                    index_col   =   json.dumps(import_full_parms[2])    
                except :
                    index_col   =   ""
                    add_error_to_log("[json.dumps ] : ["  + import_full_parms[2] + "]",SEVERE_ERROR)

            else :
                index_col   =   ""    
        
            if(not (import_full_parms[5] is None) ) :
                coerce_float   =   import_full_parms[5]
            else :
                coerce_float   =   ""
            
            if( (not (import_full_parms[6] is None)) and (len(import_full_parms[6]) > 0) ) :
                try :
                    parse_dates   =   json.dumps(import_full_parms[6])    
                except :
                    parse_dates   =   ""
                    add_error_to_log("[json.dumps ] : ["  + import_full_parms[6] + "]",SEVERE_ERROR)

            else :
                parse_dates   =   ""    
            
            if( (not (import_full_parms[7] is None)) and (len(import_full_parms[7]) > 0) ) :
                try :
                    dates_format   =   json.dumps(import_full_parms[7])    
                except :
                    dates_format   =   ""
                    add_error_to_log("[json.dumps ] : ["  + import_full_parms[7] + "]",SEVERE_ERROR)

            else :
                dates_format   =   ""    
        
            if( (not (import_full_parms[8] is None)) and (len(import_full_parms[8]) > 0) ) :
                dates_format_list   =   import_full_parms[8]  
            else :
                dates_format_list   =   ""  
            
            if( (not (import_full_parms[9] is None)) and (len(import_full_parms[9]) > 0) ) :
                try :
                    columns   =   json.dumps(import_full_parms[9])    
                except :
                    columns   =   ""
                    add_error_to_log("[json.dumps ] : ["  + import_full_parms[9] + "]",SEVERE_ERROR)
 
            else :
                columns   =   ""    
            
            if( (not (import_full_parms[10] is None)) and (len(import_full_parms[10]) > 0) ) :
                try :
                    chunksize   =   int(import_full_parms[10])    
                except :
                    chunksize   =   ""
                    add_error_to_log("[json.dumps ] : ["  + import_full_parms[10] + "]",SEVERE_ERROR)
            else :
                chunksize   =   ""    

            import_input_parms.append(tablename)              
            import_input_parms.append(schema)
            import_input_parms.append(index_col)    
            import_input_parms.append(coerce_float)
            import_input_parms.append(parse_dates) 
            import_input_parms.append(dates_format)  
            import_input_parms.append(dates_format_list)
            import_input_parms.append(columns)
            import_input_parms.append(chunksize)        

        else :
            
            import_parms_err_txt = ""

            for i in range(9) :
                import_input_parms.append("")

            for i in range(len(import_full_parms)) :
                try :
                    import_parms_err_txt    =   import_parms_err_txt + str(import_full_parms[i]) + ","
                except :
                    import_parms_err_txt    =   import_parms_err_txt + "NONE" + ","

            add_error_to_log("[Invalid Import SQLTable entry ] : ["  + import_parms_err_txt + "]",SEVERE_ERROR)

                
    elif(importType == SQLQUERY_IMPORT) :
        
        if(not ((import_full_parms[0] is None) or (len(import_full_parms[0]) == 0)) ) :
            sql  =   import_full_parms[0]
        else :
            sql  =   ""
                    
        if( (not (import_full_parms[1] is None)) and (len(import_full_parms[1]) > 0) ) :
            try :
                index_col   =   json.dumps(import_full_parms[1])    
            except :
                index_col   =   ""
        else :
            index_col   =   ""    
        
        if(not (import_full_parms[2] is None) ) :
            coerce_float   =   import_full_parms[2]
        else :
            coerce_float   =   ""
        
        if( (not (import_full_parms[3] is None)) and (len(import_full_parms[3]) > 0) ) :
            try :
                sql_params   =   json.dumps(import_full_parms[3])    
            except :
                sql_params   =   ""
        else :
            sql_params   =   ""    
            
        if( (not (import_full_parms[4] is None)) and (len(import_full_parms[4]) > 0) ) :
            try :
                parse_dates   =   json.dumps(import_full_parms[4])    
            except :
                parse_dates   =   ""
        else :
            parse_dates   =   ""  
            
        if( (not (import_full_parms[5] is None)) and (len(import_full_parms[5]) > 0) ) :
            dates_format   =   import_full_parms[5]  
        else :
            dates_format   =   ""  
            
        if( (not (import_full_parms[6] is None)) and (len(import_full_parms[6]) > 0) ) :
            dates_format_list   =   import_full_parms[6]  
        else :
            dates_format_list   =   ""  
        
        if( (not (import_full_parms[5] is None)) and (len(import_full_parms[5]) > 0) ) :
            try :
                chunksize   =   int(import_full_parms[5])    
            except :
                chunksize   =   ""
        else :
            chunksize   =   ""    
            
        import_input_parms.append(sql)
        import_input_parms.append(index_col)    
        import_input_parms.append(coerce_float)
        import_input_parms.append(sql_params)
        import_input_parms.append(parse_dates)
        import_input_parms.append(dates_format)  
        import_input_parms.append(dates_format_list)
        import_input_parms.append(chunksize) 
                
    if(DEBUG_IMPORT_FILE):
        print("get_Parms_cfg_value_for_import : import_input_parms \n",import_input_parms)

    return(import_input_parms)



def get_addl_parms_for_cfg(addl_parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get string version of addl parmsa dict
    * 
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    new_dict    =   {}
    
    if(not (addl_parms is None)) :
    
        addl_parms_keys     =   list(addl_parms.keys())

        for i in range(len(addl_parms_keys)) :
            
            addl_parm_val   =   addl_parms.get(addl_parms_keys[i])
            if(addl_parm_val is None) :
                new_dict.update({addl_parms_keys[i]:"None"})
            elif(type(addl_parm_val) is bool) :
                if(addl_parm_val) :
                    new_dict.update({addl_parms_keys[i]:"True"})
                else :
                    new_dict.update({addl_parms_keys[i]:"False"})
            else :
                new_dict.update({addl_parms_keys[i]:str(addl_parm_val)})
                
        new_dict_str    =   "{"
        
        for i in range(len(addl_parms_keys)) :
            new_dict_str = (new_dict_str + '"' + addl_parms_keys[i] + '"')
            new_dict_str = (new_dict_str + " : ")
            new_dict_str = (new_dict_str + '"' + new_dict.get(addl_parms_keys[i]) + '"')
            if(i < (len(addl_parms_keys)-1)) :
                new_dict_str = (new_dict_str + ",\n") 
                
        new_dict_str = (new_dict_str + "}")
        
        return(new_dict_str)

    else :
        
        return(None)


def get_import_form_cfg_values_from_defaults(importid,df_title,df_titles) :
    """
    * -------------------------------------------------------------------------- 
    * function : set cfg value for form parms
    * 
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * --------------------------------------------------------
    """
                
    if(DEBUG_SQL_IMPORT) :
        print("\n[get_import_form_cfg_values_from_defaults] : importid : ",importid," dftitle : ",df_title,"\n df_titles : \n",df_titles)

    cfgparms    =   []
    cfgparms.append(df_title)

    if(df_titles is None) :
        cfgparms.append(None)
    else :
        cfgparms.append(df_titles)

    for i in range(len(sqlt_import_parms_defaults)) :
        cfgparms.append(sqlt_import_parms_defaults[i])
    
    if(DEBUG_SQL_IMPORT) :
        print("\n[get_import_form_cfg_values_from_defaults] : cfgparms : \n",cfgparms)

    return(cfgparms)


def set_import_form_cfg_values_from_histroy_entry(detid,conparms=None,history_entry=None) :
    """
    * --------------------------------------------------------
    * 
    * parms :
    *   detid   -   type details
    *
    * returns : N/A
    * --------------------------------------------------------
    """
                
    if(DEBUG_IMPORT) :
        print("\n[set_import_form_cfg_values_from_histroy_entry] : detid : ",detid,"\n conparms : ",conparms,"\n history_entry : ",history_entry)
    
    formid                  =   get_formid_for_import(detid)
    
    if(not (history_entry is None)) :
            
        import_input_parms      =   [history_entry.get_df_title(),
                                     history_entry.get_df_title()]
        import_full_parms       =   history_entry.get_full_parms()
        import_form_parms       =   get_Parms_cfg_value_for_import(detid,import_full_parms,import_input_parms)
        
        # -----------------------------
        # got addl import form parms
        # -----------------------------  
         
        if( not ((detid == SQLTABLE_IMPORT) or (detid == SQLQUERY_IMPORT)) ) :
            
            import_addl_parms  =   history_entry.get_addl_parms()
            
            if( (not (import_addl_parms is None)) and (len(import_addl_parms) > 0) ) :
                addl_parms  =   get_addl_parms_for_cfg(import_addl_parms)#get_import_addl_parms(detid,import_addl_parms)
            else :
               addl_parms  =   [""]
                
            import_form_parms.append(addl_parms)
        
    else :
            
        import_input_parms  =   None
    
    if(DEBUG_IMPORT) :
        print("\n[set_import_form_cfg_values_from_histroy_entry] : import_input_parms \n",import_input_parms,"\n")
    
    # ----------------------------------
    # store input parms before display
    # ----------------------------------  
    if(not (import_input_parms is None)) :
        
        for i in range(len(import_input_parms)) :
            if(not (type(import_input_parms[i]) == str)) :
                if(import_input_parms[i] is None) :
                    import_input_parms[i]   =   ""
                elif(type(import_input_parms[i]) == bool) :
                    if(not (import_input_parms[i])) :
                        import_input_parms[i]   =   "False"
                    else :
                        import_input_parms[i]   =   "True"
                else :
                    import_input_parms[i]   =   ""    
            
    if(not (import_input_parms is None)) : 
        
        if(DEBUG_IMPORT) :
            print("\n[set_import_form_cfg_values_from_histroy_entry] : mport_input_parms \n",import_input_parms)

        import dfcleanser.common.cfg as cfg
        cfg.set_config_value(formid + "Parms",import_input_parms)
    
    return()


def is_valid_import_cfg_parms(importid,cfgparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the input cfg parms value
    * 
    * parms :
    *  importid     -   type of import
    *  cfgparms     -   config parms                      
    *
    * returns : True or False
    * --------------------------------------------------------
    """

    good_cfg_parms  =   True

    if(importid == CSV_IMPORT) :
        if(not (len(cfgparms) == 8)) : good_cfg_parms = False 
    elif(importid == FWF_IMPORT) :
        if(not (len(cfgparms) == 9)) : good_cfg_parms = False 
    elif(importid == EXCEL_IMPORT) :
        if(not (len(cfgparms) == 9)) : good_cfg_parms = False 
    elif(importid == JSON_IMPORT) :
        if(not (len(cfgparms) == 7)) : good_cfg_parms = False 
    elif(importid == HTML_IMPORT) :
        if(not (len(cfgparms) == 7)) : good_cfg_parms = False 
    elif(importid == SQLTABLE_IMPORT) :
        if(not (len(cfgparms) == 12)) : good_cfg_parms = False 
    elif(importid == SQLQUERY_IMPORT) :
        if(not (len(cfgparms) == 10)) : good_cfg_parms = False 
    elif(importid == CUSTOM_IMPORT) :
        if(not (len(cfgparms) == 3)) : good_cfg_parms = False 
    
    return(good_cfg_parms)


"""
#--------------------------------------------------------------------------
#   Data Import addl parms functions
#--------------------------------------------------------------------------
"""

def get_addl_parms(addlparms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get additional parms to diaply on import parms tanle
    * 
    * parms :
    *  addlparms  -   additional parms                      
    *
    * returns : [additional_parms_names,additional_parms_values]
    * --------------------------------------------------------
    """
    
    if(len(addlparms) > 0) :
        
        try :
        
            import json
            addl_parms_dict     =   json.loads(addlparms)
    
            addlparms_keys      =   list(addl_parms_dict.keys())
    
            addlparms_names     =   []
            addlparms_vals      =   []
    
            for i in range(len(addlparms_keys)) :
                addlparms_names.append(addlparms_keys[i]) 
                addlparms_vals.append(addl_parms_dict.get(addlparms_keys[i]))
    
        except Exception as e:
            opstat.store_exception("Unable to parse adittional parms string. " + addlparms,e)

        if(opstat.get_status()) :
            return(addl_parms_dict)
        else :
            return(None)
        
    else :
        return(None)








# sql import table import history fullparms ids
SQL_CFG_SERVER_ID                   =   0
SQL_CFG_DATABASE_ID                 =   1
SQL_CFG_DF_NAME_ID                  =   2

SQL_CFG_TABLE_NAME_ID               =   3
SQL_CFG_SCHEMA_ID                   =   4
SQL_CFG_INDEX_COL_ID                =   5
SQL_CFG_COERCE_FLOAT_ID             =   6
SQL_CFG_PARSE_DATES_ID              =   7
SQL_CFG_DATES_FORMAT_ID             =   8
SQL_CFG_DATES_FORMATS_LIST_ID       =   9
SQL_CFG_COLUMNS_ID                  =   10
SQL_CFG_CHUNKSIZE_ID                =   11

# sql import table cfg parm name 
SQL_CFG_VALUES_NAME                 =   "importPandasSQLCommonTable"+"Parms"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser SQL Table Import History Object
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

class SQLTableImportHistoryData :
    
    # instance variables
    
    dftitle                 =   None
    fullparms               =   None
    addlparmstitles         =   None
    addlparmsvals           =   None
    
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self,dfname,fparms,addlptitles,addlpvals) :
        
        self.dftitle                =   None
        self.fullparms              =   None
        self.addlparmstitles        =   None
        self.ddlparmsvals           =   None




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser SQL Table Import Object
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

class SQLTableImportData :
    
    # instance variables
    
    # sql table import sub objects
    dbconparms                 =   None
    
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self,db_conparms) :
        
        self.dbconparms               =   db_conparms
        
    """
    #--------------------------------------------------------------------------
    #   static methods for simple sql import data
    #--------------------------------------------------------------------------
    """
    
    @staticmethod
    def get_sql_parm_from_cfg_value(cfgparms,cfg_val_id) :

        return(cfgparms[cfg_val_id])

    @staticmethod
    def set_sql_parm_from_cfg_value(fparms,cfg_val_id,new_val,write=True) :

        fparms[cfg_val_id]  =   new_val

        if(write) :
            set_config_value(SQL_CFG_VALUES_NAME,fparms)



    """
    #--------------------------------------------------------------------------
    #   static methods for simple sql import history
    #--------------------------------------------------------------------------
    """

    @staticmethod
    def get_sqltable_import_history_details(dftitle,titleslist,parmslist,addl_parms) :

        if(DEBUG_IMPORT_HISTORY_DETAILS):
            print("  [get_sqltable_import_history_details] : \n   titles\n    ",titleslist,"\n   values\n    ",parmslist)

        pvals           =   []
        ptitles         =   []
                
        ptitles.append("dataframe_title")
        pvals.append(dftitle)
        ptitles.append("server")
        pvals.append(parmslist[0])
        ptitles.append("database")
        pvals.append(parmslist[1])
        ptitles.append("table_name")
        pvals.append(parmslist[2])

        intitles        =   titleslist[3:]
        invals          =   parmslist[3:]

        if(DEBUG_IMPORT_HISTORY_DETAILS):
            print("  [get_sqltable_import_history_details] : \n   intitles  \n   ",intitles,"\n   invals :\n   ",invals)
    
        for i in range(len(intitles)) :

            if(len(str(invals[i])) > 0) :
                ptitles.append(intitles[i])
                pvals.append(invals[i])
             
        if( (not (addl_parms is None)) and (len(addl_parms) > 0) ) :
            addl_parms_keys     =   list(addl_parms.keys())
            
            for i in range(len(addl_parms_keys)) :
                ptitles.append(addl_parms_keys[i])
                pvals.append(addl_parms.get(addl_parms_keys[i]))

        return([ptitles,pvals])


    def get_import_sqltable_call_parms(self,fparms,opstat) :
        """
        * -------------------------------------------------------------------------- 
        * function : get the list of parms necessary to import sql table 
        * 
        * parms :
        *  fparms   -   sql input form parms                      
        *
        * returns : sql cpandas all parms
        * --------------------------------------------------------
        """
                
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            
            if(len(fparms[2]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No table defined")
            else :
                
                table   =   fparms[2]
                    
                import json
                
                if(len(fparms[3]) == 0):
                    tschema   =   sqlt_import_parms_defaults[1]
                else :
                    tschema   =   fparms[3]
                        
                if(len(fparms[4]) == 0):
                    tindex_col   =   sqlt_import_parms_defaults[2]
                else :
                    try :
                            
                        tindex_col    =   fparms[4].replace('"',"")
                        tindex_col    =   tindex_col.replace("[","")
                        tindex_col    =   tindex_col.replace("]","")
                        tindex_col    =   tindex_col.replace(", ",",")
                        tindex_col    =   tindex_col.replace("'","")
                        tindex_col    =   tindex_col.split(",")

                    except Exception as e:
                        opstat.store_exception("Unable to get index_col  : " + str(fparms[4]),e)
                        tindex_col   =   sqlt_import_parms_defaults[2]
                            
                if(len(fparms[5]) == 0):
                    tcoerce_float   =   sqlt_import_parms_[3]
                else :
                    if(fparms[5] == "False") :
                        tcoerce_float   =   False
                    else :
                        tcoerce_float   =   True 

                if(len(fparms[6]) == 0):
                    tparse_dates   =   sqlt_import_parms_defaults[4]
                else :
                    try :
                            
                        tparse_dates   =   fparms[6]
                        print("tparse_dates",type(tparse_dates),tparse_dates)
                        tparse_dates   =   tparse_dates.replace("'",'"')
                            
                        tparse_dates   =   json.loads(tparse_dates)    
                    except Exception as e:

                        opstat.set_status(False)

                        title       =   "dfcleanser exception"
                        status_msg  =   "[Unable to get parse_dates] error "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)

                if(len(fparms[7]) == 0):
                    tdates_formats   =   sqlt_import_parms_defaults[4]
                else :
                    tdates_formats   =   fparms[7]
                    
                if(len(fparms[9]) == 0):
                    tcolumns   =   sqlt_import_parms_defaults[5]
                else :
                    try :
                            
                        pcolumns    =   fparms[9].replace('"',"")
                        tcolumns    =   pcolumns.replace("[","")
                        tcolumns    =   tcolumns.replace("]","")
                        tcolumns    =   tcolumns.replace(", ",",")
                        tcolumns    =   tcolumns.replace("'","")
                        tcolumns    =   tcolumns.split(",")
                            
                    except Exception as e:
                        opstat.store_exception("Unable to get columns  : " + str(fparms[9]),e) 
                        tcolumns   =   sqlt_import_parms_defaults[5]
                            
                if(len(fparms[10]) == 0):
                    tchunksize   =   sqlt_import_parms_defaults[6]
                else :
                    try :
                        tchunksize   =   int(fparms[10])   
                    except :

                        opstat.set_status(False)

                        title       =   "dfcleanser exception"
                        status_msg  =   "[Unable to get chunksize] error "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)

                    
                server      =   self.dbconparms.get("server")
                database    =   self.dbconparms.get("database")

                import_sql_table_call_parms = [server,database,df_title,table,tschema,tindex_col,tcoerce_float,tparse_dates,tcolumns,tchunksize]

                return(import_sql_table_call_parms)

    
    def add_import_sqltable_to_import_history(self,dftitle,importparms) :
        """
        * -------------------------------------------------------------------------- 
        * function : add the sql table import to the import history table
        * 
        * parms :
        *  dftitle       -   pandas df title                     
        *  importparms   -   sql input form parms                      
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        #add_to_history(self,filetype,dfTitle,fullParms,addlParms) 
        ImportHistory.add_to_history(SQLTABLE_IMPORT,dftitle,importparms,None)



    def set_import_sqltable_cfg_values(self,dftitle,importparms,parmid,opstat) :
        """
        * -------------------------------------------------------------------------- 
        * function : add the sql table import to the config file
        * 
        * parms :
        *  dftitle       -   pandas df title                     
        *  importparms   -   sql input form parms                      
        *
        * returns : N/A
        * --------------------------------------------------------
        """

        import json

        new_cfg_parms   =   []
        new_cfg_parms.append(dftitle)
        new_cfg_parms.append(dftitle)
            
        for i in range(len(importparms)) :
            if(importparms[i] is None) :
                new_cfg_parms.append("") 
            else :
                    
                if( (type(importparms[i]) is list) or (type(importparms[i]) is dict) ) :
                    try :
                        new_cfg_parms.append(json.dumps(importparms[i]))
                    except Exception as e:
                        opstat.store_exception("Unable to store cfg parm for parm : " + str(i),e)
                        new_cfg_parms.append("")
                            
                else :
                    new_cfg_parms.append(str(importparms[i]))    
            
        set_config_value(parmid,new_cfg_parms)
        set_config_value(CURRENT_IMPORTED_DATA_SOURCE_KEY,importparms[0],True)
            


def get_import_details_values(importParms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get import parms for dftitle and filetype
    * 
    * parms :
    *  filetpye      -   import file type                     
    *  dftitle       -   pandas df title                     
     *
    * returns : values and titles
    * --------------------------------------------------------
    """

    if(DEBUG_IMPORT) :
        print("  [get_import_details_values] importParms : ",importParms)    

    fileType        =   int(importParms[0])
    dfTitle         =   importParms[1]

    if(DEBUG_IMPORT) :
        print("  [get_import_details_values] filetype : dftitle : ",fileType,dfTitle)    
    
    Import_Details  =   ImportHistory.get_df_title_entry(fileType,dfTitle)
    
    if(DEBUG_IMPORT) :
        print("  [get_import_details_values] Import_Details : \n    ",Import_Details)    
    
    file_Type       =   Import_Details.get_file_type()
    df_title        =   Import_Details.get_df_title()
    full_parms      =   Import_Details.get_full_parms()
    addl_parms      =   Import_Details.get_addl_parms()

    if(DEBUG_IMPORT) :
        print("  [get_import_details_values] filetype : dftitle : ",fileType,dfTitle)
        print("    full_parms :  ",full_parms)
        print("    addl_parms :  ",addl_parms)

    import dfcleanser.Qt.data_import.DataImportModel as DIM
    if( (fileType == file_Type) and (dfTitle == df_title) ) :

        if(fileType == SQLTABLE_IMPORT) :

            [final_ptitles,pvals]  =   SQLTableImportData.get_sqltable_import_history_details(dfTitle,
                                                                                              pandas_import_sqltable_common_labelList[0:9],
                                                                                              full_parms,addl_parms)
        else :
        
            if(fileType == CSV_IMPORT) :
                ptitles     =   pandas_import_csv_labelList[0:7]
                ptitles.pop(1)
            elif(fileType == FWF_IMPORT) :
                ptitles     =   pandas_import_fwf_labelList[0:8]
                ptitles.pop(1)
            elif(fileType == EXCEL_IMPORT) :
                ptitles     =   pandas_import_excel_labelList[0:8]
                ptitles.pop(1)
            elif(fileType == JSON_IMPORT) :
                ptitles     =   pandas_import_json_labelList[0:6]
                ptitles.pop(1)
            elif(fileType == HTML_IMPORT) :
                ptitles     =   pandas_import_html_labelList[0:5]
                ptitles.pop(1)
            elif(fileType == SQLQUERY_IMPORT) :
                ptitles     =   pandas_import_sqlquery_labelList[0:10]
                #ptitles.pop(1)
            elif(fileType == CUSTOM_IMPORT) :
                ptitles     =   custom_import_labelList[0:2]
            elif(fileType == XML_IMPORT) :
                ptitles     =   pandas_import_xml_labelList[0:7]
                ptitles.pop(1)
            else :
                ptitles     =   pandas_import_pdf_labelList[0:6]
                ptitles.pop(1)

    
            if(DEBUG_IMPORT) :
                print("  [get_import_details_values] ")
                print("    ptitles: \n      ",ptitles)
    
            pvals               =   []
            final_ptitles       =   []

            try :

                if(fileType == SQLQUERY_IMPORT) :

                    pvals           =   full_parms
                    final_ptitles   =   ptitles

                else :

                    # set the dftitle parm
                    pvals.append(dfTitle)
                    final_ptitles.append(ptitles[0])
   
                    for i in range(len(full_parms)) :
                        pvals.append(full_parms[i])
                        final_ptitles.append(ptitles[(i+1)])
        
                    if( (not (addl_parms is None)) and (len(addl_parms) > 0) ) :

                        pvals.append("")
                        final_ptitles.append("Additional Parm(s)")

                        addl_parms_keys     =   list(addl_parms.keys())
            
                        for i in range(len(addl_parms_keys)) :
                            final_ptitles.append(addl_parms_keys[i])
                            pvals.append(addl_parms.get(addl_parms_keys[i]))

                    if(DEBUG_IMPORT) :
                        print("  [get_import_details_values] ")
                        print("    final_ptitles : \n      ",final_ptitles)
                        print("    pvals         : \n      ",pvals)

            except Exception as e:
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[get_import_details_values] error - for  : " + str(fileType) + str(dfTitle)
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                final_ptitles   =   []
                pvals           =   []

             
    return([final_ptitles,pvals])


def get_export_details_values(exportParms) :
    """
    * --------------------------------------------------------
    * function : get export parms for dftitle and filetype
    * 
    * parms :
    *  filetpye      -   export file type                     
    *  dftitle       -   pandas df title                     
     *
    * returns : values and titles
    * --------------------------------------------------------
    """


    fileType        =   int(exportParms[0])
    dfTitle         =   exportParms[1]

    if(DEBUG_EXPORT) :
        print("   [get_export_details_values]",fileType,dfTitle)

    from dfcleanser.Qt.data_export.DataExportModel import pandas_export_sqltable_labelList, pandas_export_csv_labelList
    from dfcleanser.Qt.data_export.DataExportModel import pandas_export_excel_labelList, pandas_export_json_labelList, pandas_export_html_labelList, custom_export_labelList

    from dfcleanser.Qt.data_export.DataExportModel import CSV_EXPORT, EXCEL_EXPORT, JSON_EXPORT, HTML_EXPORT, SQLTABLE_EXPORT, CUSTOM_EXPORT

    Export_Details  =   ExportHistory.get_df_title_entry(fileType,dfTitle)
    
    if(DEBUG_EXPORT) :
        print("   [get_export_details_values] Export_Details : ",Export_Details)

    ptitles     =   []
    pvals       =   []

    if(not (Export_Details is None)) :
        
        file_Type       =   Export_Details.get_file_type()
        df_title        =   Export_Details.get_df_title()
        full_parms      =   Export_Details.get_full_parms()
        addl_parms      =   Export_Details.get_addl_parms()

        if(DEBUG_EXPORT) :
            print("   [get_export_details_values] full_parms : ",full_parms)
            print("   [get_export_details_values] addl_parms : ",addl_parms)
    
        if( (fileType == file_Type) and (dfTitle == df_title) ) :
        
            if(fileType == CSV_EXPORT) :
                ptitles     =   pandas_export_csv_labelList[0:6]
                ptitles.pop(2)
            elif(fileType == EXCEL_EXPORT) :
                ptitles     =   pandas_export_excel_labelList[0:7]
                ptitles.pop(2)
            elif(fileType == JSON_EXPORT) :
                ptitles     =   pandas_export_json_labelList[0:5]
                ptitles.pop(2)
            elif(fileType == HTML_EXPORT) :
                ptitles     =   pandas_export_html_labelList[0:6]
                ptitles.pop(2)
            elif(fileType == SQLTABLE_EXPORT) :
                ptitles     =   pandas_export_sqltable_labelList[0:9]
                #ptitles.pop(2)
            elif(fileType == CUSTOM_EXPORT) :
                ptitles     =   custom_export_labelList[0:2]

            else :
                ptitles     =   []

            if(DEBUG_EXPORT) :
                print("   [get_export_details_values] ptitles : ",ptitles)

   
            pvals   =   []
        
            if(fileType == SQLTABLE_EXPORT) :
                pvals   =   full_parms

            else :

                for i in range(len(ptitles)) :
                
                    if(i==0) :
                        pvals.append(full_parms[0])
                    elif(i==1) :
                        if(fileType == CUSTOM_EXPORT) :
                            pvals.append(full_parms[1])   
                        else :
                            pvals.append(full_parms[1])#pvals.append(dfTitle)
                    else :
                        if(i>2) :
                            pvals.append(full_parms[i])#pvals.append(str(full_parms[i-1]))
            
                if( (not (addl_parms is None)) and (len(addl_parms) > 0) ) :
                    addl_parms_keys     =   list(addl_parms.keys())
            
                    for i in range(len(addl_parms_keys)) :
                        ptitles.append(addl_parms_keys[i])
                        pvals.append(addl_parms.get(addl_parms_keys[i]))
                else :

                    pvals.append("")    


    return([ptitles,pvals])



