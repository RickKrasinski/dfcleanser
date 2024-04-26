"""
# DataExportModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

"""
DEBUG_IMPORT_HISTORY            =   False
DEBUG_IMPORT_HISTORY_DETAILS    =   False
DEBUG_IMPORT_FILE               =   False
DEBUG_IMPORT_PARMS              =   False

DEBUG_IMPORT                    =   True
DEBUG_SQL_IMPORT                =   False
DEBUG_SQL_IMPORT_HTML           =   False
DEBUG_IMPORT_VALUES             =   False
"""

"""
#--------------------------------------------------------------------------
#   pandas export ids
#--------------------------------------------------------------------------
"""
CSV_EXPORT                      =   0
EXCEL_EXPORT                    =   1
JSON_EXPORT                     =   2
HTML_EXPORT                     =   3
SQLTABLE_EXPORT                 =   4
CUSTOM_EXPORT                   =   5
XML_EXPORT                      =   6

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   pandas export forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

from dfcleanser.sw_utilities.dfc_qt_model import (maketextarea)

"""
#--------------------------------------------------------------------------
#   pandas export csv form parms
#--------------------------------------------------------------------------
"""
pandas_export_csv_title         =   "Pandas CSV Export"
pandas_export_csv_id            =   "exportPandasCSV"
pandas_export_csv_idList        =   ["ecsvdataframe",
                                     "ecsvpath",
                                     "ecsvpathhistory",
                                     "ecsvcolheader",
                                     "ecsvindex",
                                     "ecsvaddlParms",
                                     None,None,None,None]

pandas_export_csv_labelList     =   ["dataframe_to_export",
                                     "path_or_buf",
                                     "csv_exports_path_history",
                                     "header",
                                     "index",
                                     "Additional Parm(s)",
                                     "Export</br>CSV File","Clear","Return","Help"]

pandas_export_csv_typeList      =   ["select","file","select",
                                     "select","select",
                                     maketextarea(4),
                                     "button","button","button","button"]

pandas_export_csv_placeholderList = ["select dataframe to export",
                                     "enter CSV File name or browse to file below",
                                     "select CSV File name",
                                     "write out column names row to file (default True)",
                                     "write row ids (default True)",
                                     "enter additional parms as dict { Key :  Value} ... (default None)",
                                     None,None,None,None]

pandas_export_csv_reqList       =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#   pandas export excel input form components
#--------------------------------------------------------------------------
"""

pandas_export_excel_title       =   "Pandas Excel Export"
pandas_export_excel_id          =   "exportPandasExcel"

pandas_export_excel_idList      =   ["exceldataframe",
                                     "excelwriter",
                                     "excelwriterhistory",
                                     "excelSheetName",
                                     "excelheader",
                                     "excelindex",
                                     "eexceladdlParms",
                                     None,None,None,None]

pandas_export_excel_labelList   =   ["dataframe_to_export",
                                     "excel_writer",
                                     "excel_exports_writer_history",
                                     "sheet_name",
                                     "header",
                                     "index",
                                     "Additional Parm(s)",
                                     "Export</br>Excel File","Clear","Return","Help"]

pandas_export_excel_typeList    =   ["select","file","select","text",
                                     "select","select",
                                     maketextarea(4),
                                     "button","button","button","button"]

pandas_export_excel_placeholderList = ["select dataframe to export",
                                       "enter Excel IO path",
                                       "select Excel IO path",
                                       "enter sheet name",
                                       "write out column names row to file (default True)",
                                       "write row ids (default True)",
                                       "enter additional parms as dict { Key :  Value} ... (default None)",
                                       None,None,None,None]

pandas_export_excel_reqList     =   [0,1,2,3,4,5]

"""
#--------------------------------------------------------------------------
#   pandas import json input form components
#--------------------------------------------------------------------------
"""

pandas_export_json_title        =   "Pandas JSON Export"
pandas_export_json_id           =   "exportPandasJSON"

pandas_export_json_idList       =   ["jsondataframe",
                                     "jsonPath",
                                     "jsonPathhistory",
                                     "jsonOrient",
                                     "ejsonaddlParmsl",
                                     None,None,None,None]

pandas_export_json_labelList    =   ["dataframe_to_export",
                                     "path_or_buf",
                                     "json_exports_path_history",
                                     "orient",
                                     "Additional Parm(s)",
                                     "Export</br>JSON File","Clear","Return","Help"]

pandas_export_json_typeList     =   ["select","file","select","select",
                                     maketextarea(4),
                                     "button","button","button","button"]

pandas_export_json_placeholderList = ["select dataframe to export",
                                      "enter JSON path or browse to file ",
                                      "select JSON path",
                                      "enter JSON orientation",
                                      "enter additional parms as dict { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_json_reqList      =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   pandas import xml input form components
#--------------------------------------------------------------------------
"""

pandas_export_xml_title        =   "Pandas XML Export"
pandas_export_xml_id           =   "exportPandasXML"

pandas_export_xml_idList       =   ["xmldataframe",
                                     "xmlPath",
                                     "xmlPathhistory",
                                     "xmlindex",
                                     "xmlroot",
                                     "xmlrow",
                                     "xmlnarep",
                                     "xmladdlParmsl",
                                     None,None,None,None]

pandas_export_xml_labelList    =   ["dataframe_to_export",
                                     "path_or_buf",
                                     "xml_exports_path_history",
                                     "index",
                                     "root_name",
                                     "row_name",
                                     "na_rep",
                                     "Additional Parm(s)",
                                     "Export</br>XML File","Clear","Return","Help"]

pandas_export_xml_typeList     =   ["select","file","select","select",
                                     "text","text","text",maketextarea(4),
                                     "button","button","button","button"]

pandas_export_xml_placeholderList = ["select dataframe to export",
                                      "enter XML path or browse to file ",
                                      "select XML path",
                                      "enter XML Index",
                                      "enter XML root_name",
                                      "enter XML row_name",
                                      "enter XML na_rep",
                                      "enter additional parms as dict { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_xml_reqList      =   [0,1,2,3]




"""
#--------------------------------------------------------------------------
#   pandas import html input form components
#--------------------------------------------------------------------------
"""

pandas_export_html_title        =   "Pandas HTML Export"
pandas_export_html_id           =   "exportPandasHTML"

pandas_export_html_idList       =   ["exhtmldataframe",
                                     "exhtmlPath",
                                     "exhtmlPathhistory",
                                     "exhtmlheader",
                                     "exhtmlRowIndexColumn",
                                     "exhtmladdlParms",
                                     None,None,None,None]

pandas_export_html_labelList    =   ["dataframe_to_export",
                                     "buf",
                                     "html_exports_io_history",
                                     "header",
                                     "index",
                                     "Additional Parm(s)",
                                     "Export</br>HTML File","Clear","Return","Help"]

pandas_export_html_typeList     =   ["select","file","select","select",
                                     "select",maketextarea(4),
                                     "button","button","button","button"]

pandas_export_html_placeholderList = ["select dataframe to export",
                                      "enter HTML path or browse to file ",
                                      "select HTML path",
                                      "whether to print column names (default True)",
                                      "whether to print row ids (default True)",
                                      "enter additional parms { Key :  Value} ... (default None)",
                                      None,None,None,None]

pandas_export_html_reqList      =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   pandas export sqltable input form components
#--------------------------------------------------------------------------
"""

pandas_export_sqltable_title        =   "Pandas SQL Table Export"
pandas_export_sqltable_id           =   "exportPandasSQLTable"

pandas_export_sqltable_idList       =    ["exportsqldataframe",
                                          "exportsqltableName",
                                          "exportsqltableschema",
                                          "exportsqltableexists",
                                          "exportsqltableindex",
                                          "exportsqltableindexlabel",
                                          "exportsqltablechunksize",
                                          "exportsqltabledtype",
                                          "exportsqltablemethod",
                                         None,None,None,None]

pandas_export_sqltable_labelList    =   ["dataframe_to_export",
                                         "table_name",
                                         "schema",
                                         "if_exists",
                                         "index",
                                         "index_label",
                                         "chunksize",
                                         "dtype",
                                         "method",
                                         "Export</br>Table",
                                         "Clear","Return","Help"]

pandas_export_sqltable_typeList     =   ["select","text","text","select",
                                         "select","text","text","text","select",
                                         "button","button","button","button"]

pandas_export_sqltable_placeholderList = ["select dataframe to export",
                                          "enter the table name",
                                          "specify the schema (if database flavor supports this). If None, use default schema.",
                                          "{‘fail’, ‘replace’, ‘append’}, (default ‘fail’)",
                                          "write DataFrame index as a column (default None)",
                                          "column label for index column(s) (default None)",
                                          "number of rows (default None)",
                                          "dict of column name to SQL type, (default None)",
                                          "sql method (default None)",
                                          None,None,None,None]

pandas_export_sqltable_reqList      =   [0,1,2]

"""
#--------------------------------------------------------------------------
#   Custom Export input form parm lists
#--------------------------------------------------------------------------
"""
custom_export_title             =   "Custom Export Code"
custom_export_id                =   "customExport"

custom_export_idList            =   ["customexporttitle",
                                     "customexportcode",
                                     None,None,None,None]

custom_export_labelList         =   ["dataframe_title",
                                     "custom_export_code",
                                     "Run Custom </br>Export Code",
                                     "Clear",
                                     "Return","Help"]

custom_export_typeList          =   ["select",
                                     maketextarea(8),
                                     "button","button","button","button"]

custom_export_placeholderList   =   ["select dataframe to export",
                                     "# custom export",
                                     None,None,None,None]
                                     
custom_export_reqList           =   [0,1]





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Export Addl Parms and Utilities
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   CSV Export Addl Parms
#--------------------------------------------------------------------------
"""
csv_import_parms                 =   ["path_or_buf","header","index_col"]
csv_import_parms_dtypes          =   [str,bool,bool]
csv_import_parms_defaults        =   [None,None,None]

csv_export_addl_parms            =   ["sep","na_rep","float_format",
                                      "columns","index_label","mode",
                                      "encoding","compression","quoting",
                                      "quotechar","lineterminator","chunksize",
                                      "date_format","doublequote","escapechar",
                                      "decimal","errors","storage_options"]

csv_export_addl_parms_dtypes     =   [str,str,str,
                                      list,[bool,str,list],str,
                                      str,[str,dict],int,
                                      str,str,int,
                                      str,bool,str,
                                      str,str,dict]

csv_export_addl_parms_defaults   =   [',',None,None,
                                      None,None,"w",
                                      None,"infer",0,
                                      '"',None,None,
                                      None,True,None,
                                      '.',"strict",None]

"""
#--------------------------------------------------------------------------
#   Excel Export Addl Parms
#--------------------------------------------------------------------------
"""
excel_import_parms                 =   ["excel_writer","sheet_name","header","index_col"]
excel_import_parms_dtypes          =   [str,str,bool,bool]
excel_import_parms_defaults        =   [None,None,None,None]

excel_export_addl_parms            = ["na_rep","float_format","columns","index_label",
                                      "startrow","startcol","engine","merge_cells", 
                                      "inf_rep","freeze_panes","storage_options"]

excel_export_addl_parms_dtypes     = [str,str,list,[bool,str,list],
                                      int,int,str,bool,
                                      str,tuple,dict]

excel_export_addl_parms_defaults   = [None,None,None,None,
                                      0,0,None,True,
                                      None,None,None]


"""
#--------------------------------------------------------------------------
#   JSON Export Addl Parms
#--------------------------------------------------------------------------
"""
json_import_parms                 =   ["path_or_buf","orient"]
json_import_parms_dtypes          =   [str,str]
json_import_parms_defaults        =   [None,None]

json_export_addl_parms            = ["date_format","double_precision","force_ascii","date_unit",
                                      "default_handler","lines","compression","index", 
                                      "indent","storage_options","mode"]

json_export_addl_parms_dtypes     = [str,int,bool,str,
                                      str,str,[str,dict],bool,
                                      int,dict,str]

json_export_addl_parms_defaults   = [None,10,True,None,
                                     "'ms'" ,None,"infer",None,
                                      None,None,"'w'"]


"""
#--------------------------------------------------------------------------
#   JSON Export Addl Parms
#--------------------------------------------------------------------------
"""
html_import_parms                 =   ["buf","header","index"]
html_import_parms_dtypes          =   [str,str,str]
html_import_parms_defaults        =   [None,None,None]

html_export_addl_parms            = ["columns","col_space","na_rep","formatters",
                                      "float_format","sparsify","ndex_names","justify", 
                                      "max_rows","max_cols","show_dimensions","decimal",
                                      "bold_rows","classes","escape","notebook",
                                      "border","table_id","render_links","encoding"]

html_export_addl_parms_dtypes     = [list,[str,int,list],str,[list,tuple,dict],
                                      str,bool,bool,str,
                                      int,int,bool,str,
                                      bool,str,bool,bool,
                                      int,str,bool,str]

html_export_addl_parms_defaults   = [None,None,None,None,
                                     None,True,True,None,
                                      None,None,True,None,
                                      True,None,True,True,
                                      None,None,False,"utf-8"]



def get_export_addl_parm_dtype(detid,parmname) :
    
    if(detid == CSV_EXPORT) :   
        parm_names   =   csv_export_addl_parms
        parm_dtypes  =   csv_export_addl_parms_dtypes
    elif(detid == EXCEL_EXPORT) :   
        parm_names   =   excel_export_addl_parms
        parm_dtypes  =   excel_export_addl_parms_dtypes
    elif(detid == JSON_EXPORT) :   
        parm_names   =   json_export_addl_parms
        parm_dtypes  =   json_export_addl_parms_dtypes
    elif(detid == HTML_EXPORT) :   
        parm_names   =   html_export_addl_parms
        parm_dtypes  =   html_export_addl_parms_dtypes

    for i in range(len(parm_names)) :
        if(parm_names[i] == parmname) :
            return(parm_dtypes[i])
        
    return(None)





