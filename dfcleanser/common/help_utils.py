"""
# Help Utilities 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Help methods and data  
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

NO_HELP_ID                  =   -1

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   chapter level form ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
SYS_ENVIRONMENT_HELP_ID         =   "SystemHelp"
IMPORT_HELP_ID                  =   "ImportHelp"
INSPECT_HELP_ID                 =   "InspectionHelp"
CLEANSE_HELP_ID                 =   "CleansingHelp"
TRANSFORM_HELP_ID               =   "TransformHelp"
EXPORT_HELP_ID                  =   "ExportHelp"
SCRIPTING_HELP_ID               =   "ScriptingHelp"
LIST_UTILITY_HELP_ID            =   "DCListUtilityHelp"
GEN_FUNCTION_UTILITY_HELP_ID    =   "DCGenFunctionUtilityHelp"
GEOCODING_HELP_ID               =   "DCGeocodeUtilityHelp"
DFSUBSET_HELP_ID                =   "DCDFSubsetUtilityHelp"
DFCONCAT_HELP_ID                =   "DCDFConcatUtilityHelp"



SYS_ENVIRONMENT_HELP_BASE           =   100
SYS_ENVIRONMENT_HELP_END            =   107
IMPORT_HELP_BASE                    =   200
IMPORT_HELP_END                     =   212
INSPECT_HELP_BASE                   =   300
INSPECT_HELP_END                    =   306
CLEANSE_HELP_BASE                   =   400
CLEANSE_HELP_END                    =   410
TRANSFORM_HELP_BASE                 =   500
TRANSFORM_HELP_END                  =   550
EXPORT_HELP_BASE                    =   600
EXPORT_HELP_END                     =   608
SCRIPTING_HELP_BASE                 =   700
SCRIPTING_HELP_END                  =   707
LIST_UTILITY_HELP_BASE              =   800
LIST_UTILITY_HELP_END               =   805
GEN_FUNCTION_UTILITY_HELP_BASE      =   900
GEN_FUNCTION_UTILITY_HELP_END       =   907
GEOCODING_HELP_BASE                 =   1000
GEOCODING_HELP_END                  =   1011
DFSUBSET_HELP_BASE                  =   1100
DFSUBSET_HELP_END                   =   1119
DFCONCAT_HELP_BASE                  =   1200
DFCONCAT_HELP_END                   =   1203


    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common system environment help data
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

SYS_ENVIRONMENT_MAIN_TASKBAR_ID             =   SYS_ENVIRONMENT_HELP_BASE + 1
SYS_ENVIRONMENT_SEL_CHAPTER_ID              =   SYS_ENVIRONMENT_HELP_BASE + 2
SYS_ENVIRONMENT_RESET_ID                    =   SYS_ENVIRONMENT_HELP_BASE + 3
SYS_ENVIRONMENT_CLEAR_ID                    =   SYS_ENVIRONMENT_HELP_BASE + 4
SYS_ENVIRONMENT_SYSTEM_ID                   =   SYS_ENVIRONMENT_HELP_BASE + 5
SYS_ENVIRONMENT_COPY_ID                     =   SYS_ENVIRONMENT_HELP_BASE + 6
SYS_ENVIRONMENT_ABOUT_ID                    =   SYS_ENVIRONMENT_HELP_BASE + 7
SYS_ENVIRONMENT_EULA_ID                     =   SYS_ENVIRONMENT_HELP_BASE + 8



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common import help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

PYMYSQL_CONNECTOR_NATIVE        =    'http://pymysql.readthedocs.io/en/latest/user/index.html'
MYSQL_CONNECTOR_NATIVE          =    'https://dev.mysql.com/doc/connector-python/en/'
PYODBC_CONNECTOR_NATIVE         =    'https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc'
PYMSSQL_CONNECTOR_NATIVE        =    'https://docs.microsoft.com/en-us/sql/connect/python/pymssql/python-sql-driver-pymssql'
SQLITE_CONNECTOR_NATIVE         =    'https://docs.python.org/2/library/sqlite3.html'
POSTGRESQL_CONNECTOR_NATIVE     =    'http://initd.org/psycopg/docs/'
ORACLE_CONNECTOR_NATIVE         =    'https://oracle.github.io/python-cx_Oracle/'

PYMYSQL_CONNECTOR_SQLALC        =    "http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql"
MYSQL_CONNECTOR_SQLALC          =    "http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc"
PYODBC_CONNECTOR_SQLALC         =    "http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector"
PYMSSQL_CONNECTOR_SQLALC        =    "http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pymssql"
SQLITE_CONNECTOR_SQLALC         =    "http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html"
POSTGRESQL_CONNECTOR_SQLALC     =    "http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2"
ORACLE_CONNECTOR_SQLALC         =    "http://docs.sqlalchemy.org/en/latest/dialects/oracle.html#module-sqlalchemy.dialects.oracle.cx_oracle"

CSV_IMPORT_URL                  =   'https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_csv.html'
FWF_IMPORT_URL                  =   'https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_fwf.html'
EXCEL_IMPORT_URL                =   'https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_excel.html'
JSON_IMPORT_URL                 =   'https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_json.html'
HTML_IMPORT_URL                 =   'https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html'
SQLTABLE_IMPORT_URL             =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql_table.html'
SQLQUERY_IMPORT_URL             =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql_query.html'


IMPORT_MAIN_TASKBAR_ID              =   IMPORT_HELP_BASE + 1

IMPORT_PANDAS_ID                        =   IMPORT_HELP_BASE + 2

IMPORT_PANDAS_SQL_TABLE_ID              =   IMPORT_HELP_BASE + 3
IMPORT_PANDAS_SQL_TABLE_IMPORT_ID       =   IMPORT_HELP_BASE + 4
IMPORT_PANDAS_SQLT_TABLES_IMPORT_ID         =   IMPORT_HELP_BASE + 5
IMPORT_PANDAS_SQLT_COLS_IMPORT_ID           =   IMPORT_HELP_BASE + 6
IMPORT_PANDAS_SQLT_DATES_IMPORT_ID          =   IMPORT_HELP_BASE + 7

IMPORT_PANDAS_SQL_QUERY_ID          =   IMPORT_HELP_BASE + 8
IMPORT_PANDAS_SQL_QUERY_RUN_ID          =   IMPORT_HELP_BASE + 9

IMPORT_CUSTOM_ID                    =   IMPORT_HELP_BASE + 10
IMPORT_CUSTOM_CCELL_ID              =   IMPORT_HELP_BASE + 11

IMPORT_FILE_ID                      =   IMPORT_HELP_BASE + 12


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common inspect help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

INSPECT_MAIN_TASKBAR_ID             =   INSPECT_HELP_BASE + 1
INSPECT_DATA_TYPES_ID               =   INSPECT_HELP_BASE + 2
INSPECT_NANS_ID                     =   INSPECT_HELP_BASE + 3
INSPECT_ROWS_ID                     =   INSPECT_HELP_BASE + 4
INSPECT_COLS_ID                     =   INSPECT_HELP_BASE + 5
INSPECT_CATS_ID                     =   INSPECT_HELP_BASE + 6


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common transform help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

SET_INDEX                           =    "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html"
RESET_INDEX                         =    "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index"
SORT_INDEX                          =    "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html"
DROP_DUPS                           =    "http://pandas.pydata.org/pandas-docs/version/0.17/generated/pandas.DataFrame.drop_duplicates.html"

PANDAS_DROPNA                       =    'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html'
PANDAS_FILLNA                       =    'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html'

TRANSFORM_MAIN_TASKBAR_ID           =   TRANSFORM_HELP_BASE + 1
TRANSFORM_DF_ID                     =   TRANSFORM_HELP_BASE + 2
TRANSFORM_DF_SAVE_COL_NAME_ID           =   TRANSFORM_HELP_BASE + 3
TRANSFORM_DF_SET_COL_NAME_ID            =   TRANSFORM_HELP_BASE + 4
TRANSFORM_DF_RESET_ROW_ID_ID            =   TRANSFORM_HELP_BASE + 5
TRANSFORM_DF_SET_ROW_ID_ID              =   TRANSFORM_HELP_BASE + 6
TRANSFORM_DF_DROP_ROW_ID_ID             =   TRANSFORM_HELP_BASE + 7
TRANSFORM_DF_DROP_DUP_ID                =   TRANSFORM_HELP_BASE + 8

TRANSFORM_COLS_ID                   =   TRANSFORM_HELP_BASE + 9
TRANSFORM_COLS_RENAME_ID                =   TRANSFORM_HELP_BASE + 10
TRANSFORM_COLS_ADD_ID                   =   TRANSFORM_HELP_BASE + 11
TRANSFORM_COLS_ADD_FILE_ID                  =   TRANSFORM_HELP_BASE + 12
TRANSFORM_COLS_ADD_USER_ID                  =   TRANSFORM_HELP_BASE + 13
TRANSFORM_COLS_ADD_USER_CELL_ID                 =   TRANSFORM_HELP_BASE + 14

TRANSFORM_COLS_DROP_ID                  =   TRANSFORM_HELP_BASE + 15
TRANSFORM_COLS_REORDER_ID               =   TRANSFORM_HELP_BASE + 16
TRANSFORM_COLS_SAVE_ID                  =   TRANSFORM_HELP_BASE + 17
TRANSFORM_COLS_COPY_ID                  =   TRANSFORM_HELP_BASE + 18
TRANSFORM_COLS_MDC_ID                   =   TRANSFORM_HELP_BASE + 19
TRANSFORM_COLS_MAP_ID                       =   TRANSFORM_HELP_BASE + 20
TRANSFORM_COLS_DUMMY_ID                     =   TRANSFORM_HELP_BASE + 21
TRANSFORM_COLS_CAT_ID                       =   TRANSFORM_HELP_BASE + 22
TRANSFORM_COLS_DTYPE_ID                 =   TRANSFORM_HELP_BASE + 23

TRANSFORM_DATETIME_ID                   =   TRANSFORM_HELP_BASE + 24
TRANSFORM_DATETIME_CONVERT_ID           =   TRANSFORM_HELP_BASE + 25
TRANSFORM_DATETIME_CONVERT1_ID              =   TRANSFORM_HELP_BASE + 26
TRANSFORM_DATETIME_CONVERT2_ID              =   TRANSFORM_HELP_BASE + 27
TRANSFORM_DATETIME_CONVERT3_ID              =   TRANSFORM_HELP_BASE + 28
TRANSFORM_DATETIME_CONVERT4_ID              =   TRANSFORM_HELP_BASE + 29


TRANSFORM_DATETIME_DELTA_ID             =   TRANSFORM_HELP_BASE + 30
TRANSFORM_DATETIME_DELTA1_ID                =   TRANSFORM_HELP_BASE + 31

TRANSFORM_DATETIME_SPLIT_ID             =   TRANSFORM_HELP_BASE + 32
TRANSFORM_DATETIME_SPLIT1_ID                =   TRANSFORM_HELP_BASE + 33

TRANSFORM_DATETIME_MERGE_ID             =   TRANSFORM_HELP_BASE + 34
TRANSFORM_DATETIME_MERGE1_ID                =   TRANSFORM_HELP_BASE + 35
TRANSFORM_DATETIME_MERGE2_ID                =   TRANSFORM_HELP_BASE + 36

TRANSFORM_DF_CHANGE_COL_NAMES_ID        =   TRANSFORM_HELP_BASE + 40
TRANSFORM_COLS_SORT_BY_COL_ID           =   TRANSFORM_HELP_BASE + 41
TRANSFORM_DF_SORT_INDEX_ID              =   TRANSFORM_HELP_BASE + 42
TRANSFORM_COLS_APPLY_FN_ID              =   TRANSFORM_HELP_BASE + 43

TRANSFORM_DF_SCHEMA_ID                  =   TRANSFORM_HELP_BASE + 50


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common cleanse help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
CLEANSE_MAIN_TASKBAR_ID                 =   CLEANSE_HELP_BASE + 1

CLEANSE_NUMERIC_ID                      =   CLEANSE_HELP_BASE + 2
CLEANSE_NUM_UNIQUE_ID                       =   CLEANSE_HELP_BASE + 3
CLEANSE_NUM_UNIQUE_ROUND_ID                     =   CLEANSE_HELP_BASE + 4
CLEANSE_NUM_UNIQUE_DATATYPE_ID                  =   CLEANSE_HELP_BASE + 5
CLEANSE_GRAPH_ID                            =   CLEANSE_HELP_BASE + 6
CLEANSE_NUM_OUTLIER_ID                      =   CLEANSE_HELP_BASE + 7

CLEANSE_NON_NUMERIC_ID                  =   CLEANSE_HELP_BASE + 8
CLEANSE_NONNUM_WHITESPACE_ID                =   CLEANSE_HELP_BASE + 9

CLEANSE_ROW_ID                          =   CLEANSE_HELP_BASE + 10


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common export help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

CSV_EXPORT_URL              =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html'
EXCEL_EXPORT_URL            =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html'
JSON_EXPORT_URL             =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html'
HTML_EXPORT_URL             =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html'
SQLTABLE_EXPORT_URL         =   'https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html'

EXPORT_MAIN_TASKBAR_ID              =   EXPORT_HELP_BASE + 1
EXPORT_PANDAS_ID                    =   EXPORT_HELP_BASE + 2
EXPORT_PANDAS_SQL_TABLE_ID              =   EXPORT_HELP_BASE + 3
EXPORT_PANDAS_SQL_TABLE_EXPORT_ID       =   EXPORT_HELP_BASE + 4
EXPORT_PANDAS_SQLT_TABLES_EXPORT_ID         =   EXPORT_HELP_BASE + 5
EXPORT_PANDAS_SQLT_COLS_EXPORT_ID           =   EXPORT_HELP_BASE + 6

EXPORT_CUSTOM_ID                    =   EXPORT_HELP_BASE + 7
EXPORT_CUSTOM_CCELL_ID              =   EXPORT_HELP_BASE + 8


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common scripting help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

SCRIPTING_MAIN_TASKBAR_ID           =   SCRIPTING_HELP_BASE + 1
SCRIPTING_SHOW_CURRENT_ID           =   SCRIPTING_HELP_BASE + 2
SCRIPTING_CLEAR_CURRENT_ID          =   SCRIPTING_HELP_BASE + 3
SCRIPTING_RUN_CURRENT_ID            =   SCRIPTING_HELP_BASE + 4
SCRIPTING_LOAD_BACKUP_ID            =   SCRIPTING_HELP_BASE + 5
SCRIPTING_BACKUP_CURRENT_ID         =   SCRIPTING_HELP_BASE + 6
SCRIPTING_ADD_TO_CURRENT_ID         =   SCRIPTING_HELP_BASE + 7


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common list utility help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
LIST_UTILITY_MAIN_TASKBAR_ID            =   LIST_UTILITY_HELP_BASE + 1
LIST_UTILITY_BUILD_LIST_ID              =   LIST_UTILITY_HELP_BASE + 2
LIST_UTILITY_BUILD_LIST1_ID             =   LIST_UTILITY_HELP_BASE + 3
LIST_UTILITY_BUILD_DICT_ID              =   LIST_UTILITY_HELP_BASE + 4
LIST_UTILITY_BUILD_DICT1_ID             =   LIST_UTILITY_HELP_BASE + 5


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common generic functions help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
GENFUNC_GEN_ID                      =   GEN_FUNCTION_UTILITY_HELP_BASE + 1
GENFUNC_GEN_NEW_ID                  =   GEN_FUNCTION_UTILITY_HELP_BASE + 2
GENFUNC_OPEN_CC_ID                  =   GEN_FUNCTION_UTILITY_HELP_BASE + 3
GENFUNC_LOAD_CC_ID                  =   GEN_FUNCTION_UTILITY_HELP_BASE + 4
GENFUNC_SAVE_CODE_ID                =   GEN_FUNCTION_UTILITY_HELP_BASE + 5
GENFUNC_DEL_FUNC_ID                 =   GEN_FUNCTION_UTILITY_HELP_BASE + 6
GENFUNC_RUN_CODE_ID                 =   GEN_FUNCTION_UTILITY_HELP_BASE + 7


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoding help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   geocoding service urls
#--------------------------------------------------------------------------
"""
GeoPy_url                        =   "https://geopy.readthedocs.io/en/stable/"
GeoPyDistance_url                =   "https://geopy.readthedocs.io/en/stable/#module-geopy.distance"

ArcGISHelp                       =   "https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm"
BingHelp                         =   "https://msdn.microsoft.com/en-us/library/ff701715.aspx"
DataBCHelp                       =   "http://www.data.gov.bc.ca/dbc/geographic/locate/geocoding.page"
GoogleHelp                       =   "https://developers.google.com/maps/documentation/geocoding/"
OpenMapQuestHelp                 =   "https://developer.mapquest.com/documentation/open/"
NominatimHelp                    =   "https://wiki.openstreetmap.org/wiki/Nominatim"

ArcGISQueryHelp                  =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.ArcGIS.geocode"
BingQueryHelp                    =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Bing.geocode"
DataBCQueryHelp                  =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.DataBC.geocode"
GoogleQueryHelp                  =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.GoogleV3.geocode"
OpenMapQuestQueryHelp            =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.OpenMapQuest.geocode"
NominatimQueryHelp               =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Nominatim.geocode"

ArcGISReverseHelp                =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.ArcGIS.reverse"
BingReverseHelp                  =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Bing.reverse"
GoogleReverseHelp                =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.GoogleV3.reverse"
OpenMapQuestReverseHelp          =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.OpenMapQuest.reverse"
NominatimReverseHelp             =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Nominatim.reverse"

ArcGISInitHelp                   =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.ArcGIS"
BingInitHelp                     =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Bing"
DataBCInitHelp                   =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.DataBC"
GoogleInitHelp                   =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.GoogleV3"
OpenMapQuestInitHelp             =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.OpenMapQuest"
NominatimInitHelp                =   "https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Nominatim"


GEOCODING_MAIN_TASKBAR_ID               =   GEOCODING_HELP_BASE + 1

GEOCODING_GET_COORDS_ID                 =   GEOCODING_HELP_BASE + 2
GEOCODING_GET_COORDS_DETAILS_ID             =   GEOCODING_HELP_BASE + 3
GEOCODING_GET_DF_COORDS_DETAILS_ID          =   GEOCODING_HELP_BASE + 4

GEOCODING_GET_ADDRESS_ID                =   GEOCODING_HELP_BASE + 5
GEOCODING_GET_ADDRESS_DETAILS_ID            =   GEOCODING_HELP_BASE + 6
GEOCODING_GET_DF_ADDRESS_DETAILS_ID         =   GEOCODING_HELP_BASE + 7

GEOCODING_CALC_DISTANCE_ID              =   GEOCODING_HELP_BASE + 8
GEOCODING_CALC_SINGLE_DISTANCE_ID           =   GEOCODING_HELP_BASE + 9
GEOCODING_CALC_DF_DISTANCE_ID               =   GEOCODING_HELP_BASE + 10

GEOCODING_SELECT_GEOCODER_ID            =   GEOCODING_HELP_BASE + 11


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common dfsebset utility help parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DFSUBSET_MAIN_TASKBAR_ID            =   DFSUBSET_HELP_BASE + 1
DFSUBSET_MAIN_ID                    =   DFSUBSET_HELP_BASE + 2
DFSUBSET_MAIN_1_ID                  =   DFSUBSET_HELP_BASE + 3
DFSUBSET_MAIN_2_ID                  =   DFSUBSET_HELP_BASE + 4

DFSUBSET_FILTER_ID                  =   DFSUBSET_HELP_BASE + 5
DFSUBSET_FILTER_1_ID                =   DFSUBSET_HELP_BASE + 6
DFSUBSET_FILTER_2_ID                =   DFSUBSET_HELP_BASE + 7
DFSUBSET_FILTER_3_ID                =   DFSUBSET_HELP_BASE + 8
DFSUBSET_FILTER_4_ID                =   DFSUBSET_HELP_BASE + 9
DFSUBSET_FILTER_5_ID                =   DFSUBSET_HELP_BASE + 10
DFSUBSET_FILTER_6_ID                =   DFSUBSET_HELP_BASE + 11
DFSUBSET_FILTER_7_ID                =   DFSUBSET_HELP_BASE + 12
DFSUBSET_FILTER_8_ID                =   DFSUBSET_HELP_BASE + 13
DFSUBSET_FILTER_9_ID                =   DFSUBSET_HELP_BASE + 14
DFSUBSET_FILTER_10_ID               =   DFSUBSET_HELP_BASE + 15
DFSUBSET_FILTER_11_ID               =   DFSUBSET_HELP_BASE + 16
DFSUBSET_FILTER_12_ID               =   DFSUBSET_HELP_BASE + 17

DFSUBSET_GET_SUBSET_ID              =   DFSUBSET_HELP_BASE + 18
DFSUBSET_GET_SUBSET_NO_FILTERS_ID   =   DFSUBSET_HELP_BASE + 19



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common help utility helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

