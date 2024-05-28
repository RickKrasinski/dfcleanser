"""
# Debug Utilities 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

#from dfcleanser.common.common_utils import (opStatus, does_dir_exist, does_file_exist)
#from dfcleanser.common.cfg import (add_error_to_log, SEVERE_ERROR, set_config_value, get_config_value, CURRENT_IMPORTED_DATA_SOURCE_KEY)
#from dfcleanser.common.cfg import print_to_string, add_debug_to_log

DC_CONSOLE_ID               =   0
DC_SYSTEM_ID                =   1
DC_DATA_IMPORT_ID           =   2
DC_DATA_IMPORT_MORE_ID      =   14
DC_DATA_INSPECTION_ID       =   3  
DC_DATA_CLEANSING_ID        =   4
DC_DATA_TRANSFORM_ID        =   5
DC_DATA_EXPORT_ID           =   6

DC_GEOCODE_UTILITY_ID       =   7
DC_DF_BROWSER_ID            =   8
DC_CENSUS_ID                =   9
DC_ZIPCODE_UTILITY_ID       =   10
DC_GEOCODE_BULK_ID          =   11
DC_WORKING_TITLE_ID         =   12
DC_WORKING_CELL_ID          =   13

DataCleansing_ID        =   "DataCleansing"
DataExport_ID           =   "DataExport"
DataImport_ID           =   "DataImport"
DataInspection_ID       =   "DataInspection"
DataScripting_ID        =   "DataScripting"
DataTransform_ID        =   "DataTransform"
SWUtilities_ID          =   "SWUtilities"
SWGeocodeUtility_ID     =   "SWGeocodeUtility"
SWBulkGeocodeUtility_ID     =   "SWBulkGeocodeUtility"
SWZipcodeUtility_ID     =   "SWZipcodeUtility"
SWCensusUtility_ID      =   "SWCensusUtility"
System_ID               =   "System"
dfBrowserUtility_ID     =   "SWdfBrowserUtility"

DBUtils_ID              =   "DBUtils"
DumpUtils_ID            =   "DumpUtils"
Help_ID                 =   "Help"
GenFunction_ID          =   "GenFunction"



#from dfcleanser.common.cfg import (DC_SYSTEM_ID, DC_DATA_IMPORT_ID, DC_DATA_INSPECTION_ID, DC_DATA_CLEANSING_ID, DC_DATA_TRANSFORM_ID, DC_DATA_EXPORT_ID, 
#                                   DBUtils_ID, SWUtilities_ID, DC_CENSUS_ID, DC_ZIPCODE_UTILITY_ID, DC_GEOCODE_UTILITY_ID)

#from dfcleanser.common.cfg import (System_ID,DataImport_ID,DataInspection_ID,DataCleansing_ID,DataTransform_ID,DataExport_ID,
#                                   SWGeocodeUtility_ID,SWZipcodeUtility_ID,SWCensusUtility_ID,DBUtils_ID,SWUtilities_ID) 

#import json

from PyQt5.QtCore import QSize, Qt


# -----------------------------------------------------------------#
# -                     System Chapter parms                      -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
System_cb1 = QCheckBox("syscb1")
System_cb2 = QCheckBox("syscb2")  
System_cb3 = QCheckBox("syscb3")
System_cb4 = QCheckBox("syscb4")
System_cb5 = QCheckBox("syscb4")

Systemcbs   =   [System_cb1,System_cb2,System_cb3,System_cb4,System_cb5]

def syscb() :
    set_chapter_debug_flag(System_ID,0)
def syscb1() :
    set_chapter_debug_flag(System_ID,1)
def syscb2() :
    set_chapter_debug_flag(System_ID,2)
def syscb3() :
    set_chapter_debug_flag(System_ID,3) 
def syscb4() : 
    set_chapter_debug_flag(System_ID,4)


Systemtext          =   ["DEBUG_SYSTEM","DEBUG_SYSTEM_DFS","DEBUG_SYSTEM_INFO","DEBUG_SYSTEM_INFO_DETAILS","DEBUG_SYSTEM_FILES"]
Systemflags         =   [False,False,False,False,False] 
Systemcallbacks     =   [syscb,syscb1,syscb2,syscb3,syscb4]

# -----------------------------------------------------------------#
# -                  Data Import Chapter parms                    -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Import_cb1 = QCheckBox("impcb1")
Import_cb2 = QCheckBox("impcb2")  
Import_cb3 = QCheckBox("impcb3")
Import_cb4 = QCheckBox("impcb4")
Import_cb5 = QCheckBox("impcb5")
Import_cb6 = QCheckBox("impcb6")
Import_cb7 = QCheckBox("impcb7")  
Import_cb8 = QCheckBox("impcb8")
Import_cb9 = QCheckBox("impcb9")
Import_cb10 = QCheckBox("impcb10")
Import_cb11 = QCheckBox("impcb11")
Import_cb12 = QCheckBox("impcb12")  
Import_cb13 = QCheckBox("impcb13")
Import_cb14 = QCheckBox("impcb14")
Import_cb15 = QCheckBox("impcb15")
Import_cb16 = QCheckBox("impcb16")
Import_cb17 = QCheckBox("impcb17")  

def impcb1() :
    set_chapter_debug_flag(DataImport_ID,0)
def impcb2() :
    set_chapter_debug_flag(DataImport_ID,1)
def impcb3() :
    set_chapter_debug_flag(DataImport_ID,2) 
def impcb4() : 
    set_chapter_debug_flag(DataImport_ID,3)
def impcb5() :
    set_chapter_debug_flag(DataImport_ID,4)
def impcb6() :
    set_chapter_debug_flag(DataImport_ID,5)
def impcb7() :
    set_chapter_debug_flag(DataImport_ID,6)
def impcb8() :
    set_chapter_debug_flag(DataImport_ID,7) 
def impcb9() : 
    set_chapter_debug_flag(DataImport_ID,8)
def impcb10() :
    set_chapter_debug_flag(DataImport_ID,9)
def impcb11() :
    set_chapter_debug_flag(DataImport_ID,10)
def impcb12() :
    set_chapter_debug_flag(DataImport_ID,11)
def impcb13() :
    set_chapter_debug_flag(DataImport_ID,12) 
def impcb14() : 
    set_chapter_debug_flag(DataImport_ID,13)
def impcb15() :
    set_chapter_debug_flag(DataImport_ID,14)
def impcb16() :
    set_chapter_debug_flag(DataImport_ID,15)
def impcb17() :
    set_chapter_debug_flag(DataImport_ID,16)



DataImportcbs           =   [Import_cb1,Import_cb2,Import_cb3,Import_cb4,Import_cb5,Import_cb6,Import_cb7,Import_cb8,Import_cb9,Import_cb10,
                             Import_cb11,Import_cb12,Import_cb13,Import_cb14,Import_cb15,Import_cb16,Import_cb17]

DataImporttext          =   ["DEBUG_DATA_IMPORT","DEBUG_DATA_IMPORT_DETAILS","DEBUG_DATA_IMPORT_FORMS","DEBUG_DATA_IMPORT_CONNECTORS","DEBUG_DATA_IMPORT_CSV",
                             "DEBUG_DATA_IMPORT_FWF","DEBUG_DATA_IMPORT_EXCEL","DEBUG_DATA_IMPORT_JSON","DEBUG_DATA_IMPORT_XML","DEBUG_DATA_IMPORT_HTML",
                             "DEBUG_DATA_IMPORT_SQLTABLE","DEBUG_DATA_IMPORT_SQLQUERY","DEBUG_DATA_IMPORT_FILE_TYPES","DEBUG_DATA_IMPORT_HISTORY","DEBUG_DATA_EXPORT_HISTORY",
                             "DEBUG_DATA_IMPORT_PARMS","DEBUG_DATA_IMPORT_DFS_HISTORY"]

DataImportflags         =   [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False] 

DataImportcallbacks     =   [impcb1,impcb2,impcb3,impcb4,impcb5,impcb6,impcb7,impcb8,impcb9,impcb10,impcb11,impcb12,impcb13,impcb14,impcb15,impcb16,impcb17]


# -----------------------------------------------------------------#
# -                  Data Inspect Chapter parms                   -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Inspect_cb1 = QCheckBox("inscb1")
Inspect_cb2 = QCheckBox("inscb2")  
Inspect_cb3 = QCheckBox("inscb3")
Inspect_cb4 = QCheckBox("inscb4")
Inspect_cb5 = QCheckBox("inscb5")
Inspect_cb6 = QCheckBox("inscb6")
Inspect_cb7 = QCheckBox("inscb7")  
Inspect_cb8 = QCheckBox("inscb8")
Inspect_cb9 = QCheckBox("inscb9")
Inspect_cb10 = QCheckBox("inscb10")
Inspect_cb11 = QCheckBox("inscb11")

def inscb1() :
    set_chapter_debug_flag(DataInspection_ID,0)
def inscb2() :
    set_chapter_debug_flag(DataInspection_ID,1)
def inscb3() :
    set_chapter_debug_flag(DataInspection_ID,2) 
def inscb4() : 
    set_chapter_debug_flag(DataInspection_ID,3)
def inscb5() :
    set_chapter_debug_flag(DataInspection_ID,4)
def inscb6() :
    set_chapter_debug_flag(DataInspection_ID,5)
def inscb7() :
    set_chapter_debug_flag(DataInspection_ID,6)
def inscb8() :
    set_chapter_debug_flag(DataInspection_ID,7) 
def inscb9() : 
    set_chapter_debug_flag(DataInspection_ID,8)
def inscb10() :
    set_chapter_debug_flag(DataInspection_ID,9)


DataInspectcbs          =   [Inspect_cb1,Inspect_cb2,Inspect_cb3,Inspect_cb4,Inspect_cb5,Inspect_cb6,Inspect_cb7,Inspect_cb8,Inspect_cb9,Inspect_cb10]

DataInspecttext         =   ["DEBUG_DATA_INSPECT","DEBUG_DATA_INSPECT_DTYPES","DEBUG_DATA_INSPECT_ROWS","DEBUG_DATA_INSPECT_COLUMNS","DEBUG_DATA_INSPECT_CATEGORIES",
                             "DEBUG_DATA_INSPECT_COLUMNS_DETAILS","DEBUG_INSPECT_ROWS_DETAILS","DEBUG_INSPECT_CATS","DEBUG_INSPECT_OUTLIERS","DEBUG_DISPLAY_TRACE"]

DataInspectflags         =   [False,False,False,False,False,False,False,False,False,False] 

DataInspectcallbacks     =   [inscb1,inscb2,inscb3,inscb4,inscb5,inscb6,inscb7,inscb8,inscb9,inscb10]


# -----------------------------------------------------------------#
# -                 Data Cleansnig Chapter parms                  -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Cleanse_cb1 = QCheckBox("clncb1")
Cleanse_cb2 = QCheckBox("clncb2")  
Cleanse_cb3 = QCheckBox("clncb3")
Cleanse_cb4 = QCheckBox("clncb4")
Cleanse_cb5 = QCheckBox("clncb5")
Cleanse_cb6 = QCheckBox("clncb6")
Cleanse_cb7 = QCheckBox("clncb7")  
Cleanse_cb8 = QCheckBox("clncb8")
Cleanse_cb9 = QCheckBox("clncb9")
Cleanse_cb10 = QCheckBox("clncb10")
Cleanse_cb11 = QCheckBox("clncb11")
Cleanse_cb12 = QCheckBox("clncb12")  
Cleanse_cb13 = QCheckBox("clncb13")  

def clncb0() :
    set_chapter_debug_flag(DataCleansing_ID,0)
def clncb1() :
    set_chapter_debug_flag(DataCleansing_ID,1)
def clncb2() :
    set_chapter_debug_flag(DataCleansing_ID,2)
def clncb3() :
    set_chapter_debug_flag(DataCleansing_ID,3) 
def clncb4() : 
    set_chapter_debug_flag(DataCleansing_ID,4)
def clncb5() :
    set_chapter_debug_flag(DataCleansing_ID,5)
def clncb6() :
    set_chapter_debug_flag(DataCleansing_ID,6)
def clncb7() :
    set_chapter_debug_flag(DataCleansing_ID,7)
def clncb8() :
    set_chapter_debug_flag(DataCleansing_ID,8) 
def clncb9() : 
    set_chapter_debug_flag(DataCleansing_ID,9)
def clncb10() :
    set_chapter_debug_flag(DataCleansing_ID,10)
def clncb11() :
    set_chapter_debug_flag(DataCleansing_ID,11)
def clncb12() :
    set_chapter_debug_flag(DataCleansing_ID,12)
def clncb13() :
    set_chapter_debug_flag(DataCleansing_ID,13)

DataCleansecbs          =   [Cleanse_cb1,Cleanse_cb2,Cleanse_cb3,Cleanse_cb4,Cleanse_cb5,Cleanse_cb6,Cleanse_cb7,Cleanse_cb8,Cleanse_cb9,Cleanse_cb10,
                             Cleanse_cb11,Cleanse_cb12]

DataCleansetext         =   ["DEBUG_CUNIQUES","DEBUG_CLEANSING","DEBUG_CLEANSING_DETAILS","DEBUG_CLEANSE_COLUMN","DEBUG_CLEANSE_COLUMN_DETAILS",
                             "DEBUG_CLEANSE_COLUMN_SINGLE","DEBUG_CLEANSE_ROWS","DEBUG_CLEANSE_ROWS_FILTER","DEBUG_CLEANSE_ROWS_FILTER_DETAILS",
                             "DEBUG_FILTERS_COLUMN_TABLE","DEBUG_FILTERS_STATS_TABLE","DEBUG_DATA_CLEANSING","DEBUG_USER_FNS"]

DataCleanseflags         =   [False,False,False,False,False,False,False,False,False,False,False,False,False] 

DataCleansecallbacks     =   [clncb1,clncb2,clncb3,clncb4,clncb5,clncb6,clncb7,clncb8,clncb9,clncb10,clncb11,clncb12,clncb13]


# -----------------------------------------------------------------#
# -                 Data Transform Chapter parms                  -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Transform_cb1 = QCheckBox("trncb1")
Transform_cb2 = QCheckBox("trncb2")  
Transform_cb3 = QCheckBox("trncb3")
Transform_cb4 = QCheckBox("trncb4")
Transform_cb5 = QCheckBox("trncb5")

def trncb0() :
    set_chapter_debug_flag(DataTransform_ID,0)
def trncb1() :
    set_chapter_debug_flag(DataTransform_ID,1)
def trncb2() :
    set_chapter_debug_flag(DataTransform_ID,2)
def trncb3() :
    set_chapter_debug_flag(DataTransform_ID,3) 
def trncb4() : 
    set_chapter_debug_flag(DataTransform_ID,4)
def trncb5() :
    set_chapter_debug_flag(DataTransform_ID,5)

DataTransformcbs          =   [Transform_cb1,Transform_cb2,Transform_cb3,Transform_cb4,Transform_cb5]

DataTransformtext         =   ["DEBUG_TRANSFORM","DEBUG_TRANSFORM_DATAFRAMES","DEBUG_TRANSFORM_DATETIME","DEBUG_TRANSFORM_COLUMN","DEBUG_TRANSFORM_COLUMN_DETAILS"]

DataTransformflags         =   [False,False,False,False,False]

DataTransformcallbacks     =   [trncb0,trncb1,trncb2,trncb3,trncb4,trncb5]


# -----------------------------------------------------------------#
# -                   Data Export Chapter parms                   -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Export_cb1 = QCheckBox("expcb1")
Export_cb2 = QCheckBox("expcb2")  
Export_cb3 = QCheckBox("expcb3")
Export_cb4 = QCheckBox("expcb4")
Export_cb5 = QCheckBox("expcb5")
Export_cb6 = QCheckBox("expcb6")
Export_cb7 = QCheckBox("expcb7")
Export_cb8 = QCheckBox("expcb8")
Export_cb9 = QCheckBox("expcb9")
Export_cb10 = QCheckBox("expcb10")

def expcb0() :
    set_chapter_debug_flag(DataExport_ID,0)
def expcb1() :
    set_chapter_debug_flag(DataExport_ID,1)
def expcb2() :
    set_chapter_debug_flag(DataExport_ID,2)
def expcb3() :
    set_chapter_debug_flag(DataExport_ID,3) 
def expcb4() : 
    set_chapter_debug_flag(DataExport_ID,4)
def expcb5() :
    set_chapter_debug_flag(DataExport_ID,5) 
def expcb6() : 
    set_chapter_debug_flag(DataExport_ID,6)
def expcb7() :
    set_chapter_debug_flag(DataExport_ID,7)
def expcb8() :
    set_chapter_debug_flag(DataExport_ID,8)
def expcb9() :
    set_chapter_debug_flag(DataExport_ID,9)



DataExportcbs           =   [Export_cb1,Export_cb2,Export_cb3,Export_cb4,Export_cb5,Export_cb6,Export_cb7,Export_cb8,Export_cb9,Export_cb10]

DataExporttext          =   ["DEBUG_DATA_EXPORT","DEBUG_DATA_EXPORT_DETAILS","DEBUG_DATA_EXPORT_HISTORIES","DEBUG_DATA_EXPORT_FILE_TYPE","DEBUG_DATA_EXPORT_FORMS",
                             "DEBUG_DATA_EXPORT_CONNECTORS","DEBUG_DATA_EXPORT_FILE_TYPES","DEBUG_DATA_EXPORT_HISTORY","DEBUG_DATA_EXPORT_HISTORY",
                             "DEBUG_DATA_EXPORT_PARMS"]

DataExportflags         =   [False,False,False,False,False,False,False,False,False,False]

DataExportcallbacks     =   [expcb0,expcb1,expcb2,expcb3,expcb4,expcb5,expcb6,expcb7,expcb8,expcb9]


# -----------------------------------------------------------------#
# -                         DButils parms                         -#
# -----------------------------------------------------------------#


from PyQt5.QtWidgets import QCheckBox
dbutils_cb1 = QCheckBox("dbucb1")
dbutils_cb2 = QCheckBox("dbucb2")  
dbutils_cb3 = QCheckBox("dbucb3")
dbutils_cb4 = QCheckBox("dbucb4")
dbutils_cb5 = QCheckBox("dbucb5")
dbutils_cb6 = QCheckBox("dbucb6")
dbutils_cb7 = QCheckBox("dbucb7")  
dbutils_cb8 = QCheckBox("dbucb8")
dbutils_cb9 = QCheckBox("dbucb9")
dbutils_cb10 = QCheckBox("dbucb10")


def dbucb1() :
    set_chapter_debug_flag(DBUtils_ID,0)
def dbucb2() :
    set_chapter_debug_flag(DBUtils_ID,1)
def dbucb3() :
    set_chapter_debug_flag(DBUtils_ID,2) 
def dbucb4() : 
    set_chapter_debug_flag(DBUtils_ID,3)
def dbucb5() :
    set_chapter_debug_flag(DBUtils_ID,4)
def dbucb6() :
    set_chapter_debug_flag(DBUtils_ID,5)
def dbucb7() :
    set_chapter_debug_flag(DBUtils_ID,6)
def dbucb8() :
    set_chapter_debug_flag(DBUtils_ID,7) 
def dbucb9() : 
    set_chapter_debug_flag(DBUtils_ID,8)
def dbucb10() : 
    set_chapter_debug_flag(DBUtils_ID,9)


DBUtilscbs              =   [dbutils_cb1,dbutils_cb2,dbutils_cb3,dbutils_cb4,dbutils_cb5,dbutils_cb6,dbutils_cb7,dbutils_cb8,dbutils_cb9,dbutils_cb10]

DBUtilstext             =   ["DEBUG_DBUTILS","DEBUG_DBUTILS_DBCONNECTORS","DEBUG_DBUTILS_TEST_CONNECTOR","DEBUG_DBUTILS_DBCON_FORM_DETAILS","DEBUG_SQL_DBUTILS",
                             "DEBUG_DBUTILS_SQL_FORM","DEBUG_DBUTILS_SQL_FORM_DETAILS","DEBUG_DBUTILS_SQL_FORM_COL_NAMES","DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES",
                             "DEBUG_DBUTILS_DBCONNECTOR_FORM"]

DBUtilsflags            =   [False,False,False,False,False,False,False,False,False,False] 

DBUtilscallbacks        =   [dbucb1,dbucb2,dbucb3,dbucb4,dbucb5,dbucb6,dbucb7,dbucb8,dbucb9,dbucb10]


# -----------------------------------------------------------------#
# -                    Common Utils parms                         -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
swutils_cb1 = QCheckBox("swucb1")
swutils_cb2 = QCheckBox("swucb2")  
swutils_cb3 = QCheckBox("swucb3")
swutils_cb4 = QCheckBox("swucb4")

def swucb1() :
    set_chapter_debug_flag(SWUtilities_ID,0)
def swucb2() :
    set_chapter_debug_flag(SWUtilities_ID,1)
def swucb3() :
    set_chapter_debug_flag(SWUtilities_ID,2) 
def swucb4() : 
    set_chapter_debug_flag(SWUtilities_ID,3)

SWUtilscbs              =   [swutils_cb1,swutils_cb2,swutils_cb3,swutils_cb4]

SWUtilstext             =   ["DEBUG_COMMON","DEBUG_INPUT_FORMS","DEBUG_INPUT_FORMS_DETAILS","DEBUG_COMMON_EXCEPT"]

SWUtilsflags            =   [False,False,False,False] 

SWUtilscallbacks        =   [swucb1,swucb2,swucb3,swucb4]


# -----------------------------------------------------------------#
# -                    Census Utils parms                         -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
census_cb1 = QCheckBox("cencb1")
census_cb2 = QCheckBox("cencb2")  

def cencb1() :
    set_chapter_debug_flag(SWCensusUtility_ID,0)
def cencb2() :
    set_chapter_debug_flag(SWCensusUtility_ID,1)

censuscbs              =   [census_cb1,census_cb2]

censustext             =   ["DEBUG_CENSUS","DEBUG_CENSUS_DETAILS"]

censusflags            =   [False,False] 

censuscallbacks        =   [cencb1,cencb2]


# -----------------------------------------------------------------#
# -                    Zipcode Utils parms                        -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
zipcode_cb1 = QCheckBox("zipcb1")
zipcode_cb2 = QCheckBox("zipcb2")  
zipcode_cb3 = QCheckBox("zipcb3")  

def zipcb1() :
    set_chapter_debug_flag(SWZipcodeUtility_ID,0)
def zipcb2() :
    set_chapter_debug_flag(SWZipcodeUtility_ID,1)
def zipcb3() :
    set_chapter_debug_flag(SWZipcodeUtility_ID,2)

zipcodecbs              =   [zipcode_cb1,zipcode_cb2,zipcode_cb3]

zipcodetext             =   ["DEBUG_ZIPCODE","DEBUG_ZIPS","DEBUG_ZIPCODE_DETAILS"]

zipcodeflags            =   [False,False,False] 

zipcodecallbacks        =   [zipcb1,zipcb2,zipcb3]


# -----------------------------------------------------------------#
# -                    Geocode Utils parms                        -#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import QCheckBox
Geocode_cb1 = QCheckBox("geocb1")
Geocode_cb2 = QCheckBox("geocb2")  
Geocode_cb3 = QCheckBox("geocb3")
Geocode_cb4 = QCheckBox("geocb4")
Geocode_cb5 = QCheckBox("geocb5")
Geocode_cb6 = QCheckBox("geocb6")
Geocode_cb7 = QCheckBox("geocb7")  
Geocode_cb8 = QCheckBox("geocb8")
Geocode_cb9 = QCheckBox("geocb9")
Geocode_cb10 = QCheckBox("geocb10")
Geocode_cb11 = QCheckBox("geocb11")
Geocode_cb12 = QCheckBox("geocb12")  
Geocode_cb13 = QCheckBox("geocb13")
Geocode_cb14 = QCheckBox("geocb14")
Geocode_cb15 = QCheckBox("geocb15")
Geocode_cb16 = QCheckBox("geocb16")
Geocode_cb17 = QCheckBox("geocb17")  

def geocb0() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,0)
def geocb1() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,1)
def geocb2() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,2)
def geocb3() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,3) 
def geocb4() : 
    set_chapter_debug_flag(SWGeocodeUtility_ID,4)
def geocb5() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,5)
def geocb6() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,6)
def geocb7() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,7)
def geocb8() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,8) 
def geocb9() : 
    set_chapter_debug_flag(SWGeocodeUtility_ID,9)
def geocb10() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,10)
def geocb11() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,11)
def geocb12() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,12)
def geocb13() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,13) 
def geocb14() : 
    set_chapter_debug_flag(SWGeocodeUtility_ID,14)
def geocb15() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,15)
def geocb16() :
    set_chapter_debug_flag(SWGeocodeUtility_ID,16)



Geocodecbs              =   [Geocode_cb1,Geocode_cb2,Geocode_cb3,Geocode_cb4,Geocode_cb5,Geocode_cb6,Geocode_cb7,Geocode_cb8,Geocode_cb9,Geocode_cb10,
                             Geocode_cb11,Geocode_cb12,Geocode_cb13,Geocode_cb14,Geocode_cb15,Geocode_cb16]


Geocodetext             =   ["DEBUG_GEOCODE","DEBUG_GEOCODE_DETAILS","DEBUG_GEOCODE_GET_GEOCODE","DEBUG_GEOCODE_GET_GEOCODE_DETAILS","DEBUG_GEOCODE_UTILITY",
                             "DEBUG_GEOCODE_BULK","DEBUG_BULK_CONSOLE","DEBUG_GEOCODE_BULK_UTILS","GEOCODE_THREAD_DEBUG","DEBUG_GEOCODE_GET_RUN_TASK",
                             "DEBUG_GEOCODE_ADD_RESULT","DEBUG_GEOCODE_DISPLAY_FORM","DEBUG_MERGE","DEBUG_GEOCODE_PROCESS_RESULTS","DEBUG_GEOCODE_FLUSH_RESULTS",
                             "DEBUG_GEOCODE_PROCESS_ERRORS"]

Geocodeflags            =   [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False] 

Geocodecallbacks        =   [geocb0,geocb1,geocb2,geocb3,geocb4,geocb5,geocb6,geocb7,geocb8,geocb9,geocb10,geocb11,geocb12,geocb13,geocb14,geocb15,geocb16]


#------------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       Debug Utilities                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_chapter_parms(chapterid) :

    if(chapterid    ==  DC_SYSTEM_ID): 
        debug_chapter   =   get_debug_chapter(System_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [Systemcbs,Systemtext,Systemflags,Systemcallbacks]
        else :
            chapter_parms   =   [Systemcbs,Systemtext,get_debug_chapter(System_ID).get_chapter_values(),Systemcallbacks]    
    elif(chapterid    ==  DC_DATA_IMPORT_ID):  
        debug_chapter   =   get_debug_chapter(DataImport_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DataImportcbs,DataImporttext,DataImportflags,DataImportcallbacks]
        else :
            chapter_parms   =   [DataImportcbs,DataImporttext,get_debug_chapter(DataImport_ID).get_chapter_values(),DataImportcallbacks]    
    elif(chapterid    ==  DC_DATA_INSPECTION_ID): 
        debug_chapter   =   get_debug_chapter(DataInspection_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DataInspectcbs,DataInspecttext,DataInspectflags,DataInspectcallbacks]  
        else :  
            chapter_parms   =   [DataInspectcbs,DataInspecttext,get_debug_chapter(DataInspection_ID).get_chapter_values(),DataInspectcallbacks]    
    elif(chapterid    ==  DC_DATA_CLEANSING_ID):  
        debug_chapter   =   get_debug_chapter(DataCleansing_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DataCleansecbs,DataCleansetext,DataCleanseflags,DataCleansecallbacks] 
        else : 
            chapter_parms   =   [DataCleansecbs,DataCleansetext,get_debug_chapter(DataCleansing_ID).get_chapter_values(),DataCleansecallbacks]    
    elif(chapterid    ==  DC_DATA_TRANSFORM_ID): 
        debug_chapter   =   get_debug_chapter(DataTransform_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DataTransformcbs,DataTransformtext,DataTransformflags,DataTransformcallbacks]    
        else :
            chapter_parms   =   [DataTransformcbs,DataTransformtext,get_debug_chapter(DataTransform_ID).get_chapter_values(),DataTransformcallbacks]    
    elif(chapterid    ==  DC_DATA_EXPORT_ID):
        debug_chapter   =   get_debug_chapter(DataExport_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DataExportcbs,DataExporttext,DataExportflags,DataExportcallbacks]
        else :
            chapter_parms   =   [DataExportcbs,DataExporttext,get_debug_chapter(DataExport_ID).get_chapter_values(),DataExportcallbacks]    
    elif(chapterid    ==  DBUtils_ID):
        debug_chapter   =   get_debug_chapter(DBUtils_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [DBUtilscbs,DBUtilstext,DBUtilsflags,DBUtilscallbacks]
        else :
            chapter_parms   =   [DBUtilscbs,DBUtilstext,get_debug_chapter(DBUtils_ID).get_chapter_values(),DBUtilscallbacks]    
    elif(chapterid    ==  SWUtilities_ID): 
        debug_chapter   =   get_debug_chapter(SWUtilities_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [SWUtilscbs,SWUtilstext,SWUtilsflags,SWUtilscallbacks] 
        else :   
            chapter_parms   =   [SWUtilscbs,SWUtilstext,get_debug_chapter(SWUtilities_ID).get_chapter_values(),SWUtilscallbacks]    
    elif(chapterid    ==  DC_CENSUS_ID): 
        debug_chapter   =   get_debug_chapter(SWCensusUtility_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [censuscbs,censustext,censusflags,censuscallbacks]    
        else :
            chapter_parms   =   [censuscbs,censustext,get_debug_chapter(SWCensusUtility_ID).get_chapter_values(),censuscallbacks]    
    elif(chapterid    ==  DC_ZIPCODE_UTILITY_ID): 
        debug_chapter   =   get_debug_chapter(SWZipcodeUtility_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [zipcodecbs,zipcodetext,zipcodeflags,zipcodecallbacks]    
        else :
            chapter_parms   =   [zipcodecbs,zipcodetext,get_debug_chapter(SWZipcodeUtility_ID).get_chapter_values(),zipcodecallbacks]    
    elif(chapterid    ==  DC_GEOCODE_UTILITY_ID): 
        debug_chapter   =   get_debug_chapter(SWGeocodeUtility_ID) 
        if(debug_chapter is None) :
            chapter_parms   =   [Geocodecbs,Geocodetext,Geocodeflags,Geocodecallbacks]    
        else :
            chapter_parms   =   [Geocodecbs,Geocodetext,get_debug_chapter(SWGeocodeUtility_ID).get_chapter_values(),Geocodecallbacks]    

    return(chapter_parms)


def build_chapter_debug_flags(chapterid,chparms) : 

    #print("build_chapter_debug_flags",chapterid)
    
    cbs             =   chparms[0]
    boxtext         =   chparms[1]
    checkedflags    =   chparms[2]
    connectcalls    =   chparms[3]

    from PyQt5.QtWidgets import QVBoxLayout, QWidget
    debugLayout     =   QVBoxLayout()

    if(chapterid        ==  DC_SYSTEM_ID):              QLabelText  =   "\nSystem Chapter"
    elif(chapterid      ==  DC_DATA_IMPORT_ID):         QLabelText  =   "\nData Import Chapter"
    elif(chapterid      ==  DC_DATA_INSPECTION_ID):     QLabelText  =   "\nData Inspection Chapter"
    elif(chapterid      ==  DC_DATA_CLEANSING_ID):      QLabelText  =   "\nData Cleansing Chapter"
    elif(chapterid      ==  DC_DATA_TRANSFORM_ID):      QLabelText  =   "\nData Transform Chapter"
    elif(chapterid      ==  DC_DATA_EXPORT_ID):         QLabelText  =   "\nData Export Chapter"
    elif(chapterid      ==  DBUtils_ID):                QLabelText  =   "\nDatabase Utilities"
    elif(chapterid      ==  SWUtilities_ID):            QLabelText  =   "\nSoftware Utilities"
    elif(chapterid      ==  DC_CENSUS_ID):              QLabelText  =   "\nCensus Chapter"
    elif(chapterid      ==  DC_ZIPCODE_UTILITY_ID):     QLabelText  =   "\nZipcode Chapter"
    elif(chapterid      ==  DC_GEOCODE_UTILITY_ID):     QLabelText  =   "\nGeocode Chapter"

    from PyQt5.QtWidgets import QLabel
    debug_title_label   =   QLabel()
    debug_title_label.setText(QLabelText)
    debug_title_label.setAlignment(Qt.AlignLeft)
    debug_title_label.resize(480,50)
    debug_title_label.setStyleSheet("font-size: 13px; font-weight: bold; font-family: Arial; ")
    debugLayout.addWidget(debug_title_label)

    from PyQt5.QtWidgets import QCheckBox

    for i in range(len(cbs)) :

        cbs[i].setText(boxtext[i])
        cbs[i].setStyleSheet("font-size: 9px; font-weight: normal; font-family: Arial; ")
        cbs[i].setChecked(checkedflags[i])
        cbs[i].stateChanged.connect(connectcalls[i])
        debugLayout.addWidget(cbs[i]) 
    
    debugLayout.addStretch()

    return(debugLayout)

def set_chapter_debug_flag(chapterid,flagoffset) : 

    current_value   =   get_debug_flag_value(chapterid,flagoffset) 

    if(current_value == True) :
        new_value   =   False
    else :
        new_value   =   True

    set_debug_flag_value(chapterid,flagoffset,new_value) 

def is_debug_set(chapterid,flagvalue) :

    chapter         =   dfc_debug_values.get_debug_chapter(chapterid)
    if(chapter is None) :
        return(False)
    else :
        debug_value     =   chapter.get_debug_value(flagvalue) 
        return(debug_value)   

def save_debug_file() :

    dfc_debug_values.save_debug_values_file()    

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Debug Current Values Class                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                Debug Chapter Values Class                     -#
# -----------------------------------------------------------------#

class DataframeCleanserChapterDebugValues :
    
    # instance variables
    
    # error log
    chapter_debug_values        =    []

    chapter_id                  =    None
    chapter_texts               =    None
    chapter_values              =    None
    
    # full constructor
    def __init__(self, chapterid,chaptertexts,chaptervalues) :

        #print("construct debug flags",chapterid,chaptertexts,chaptervalues)
        
        self.chapter_id             =   chapterid
        self.chapter_texts          =   chaptertexts
        self.chapter_values         =   chaptervalues

        self.chapter_debug_values   =   [self.chapter_id,self.chapter_texts,self.chapter_values]

    def get_chapter_id(self) :
        return(self.chapter_id)

    def get_chapter_texts(self) :
        return(self.chapter_texts)

    def get_chapter_values(self) :
        return(self.chapter_values)

    def get_debug_value(self, chaptertext) :

        if(chaptertext in self.chapter_texts) :
            for i in range(len(self.chapter_texts)) :
                if(self.chapter_texts[i] == chaptertext) :
                    return(self.chapter_values[i])
                
        return(False)
    
    def set_debug_value(self, flagid, debugvalue) :

        print("[DataframeCleanserChapterDebugValues] : set_debug_value ",flagid, debugvalue)

        chaptertext     =   self.chapter_texts[flagid]
        print("[DataframeCleanserChapterDebugValues] : chaptertext ",chaptertext)

        if(chaptertext in self.chapter_texts) :

            for i in range(len(self.chapter_texts)) :
                if(self.chapter_texts[i] == chaptertext) :
                    print("[DataframeCleanserChapterDebugValues] : set_debug_value ",self.chapter_texts[i])
                    print("[DataframeCleanserChapterDebugValues] : set_debug_value ",self.chapter_values)
                    self.chapter_values[i] = debugvalue
                    break

    def get_serial_chapter_values(self) :

        return(self.chapter_debug_values)
                

# -----------------------------------------------------------------#
# -                Helper Methods Values Class                    -#
# -----------------------------------------------------------------#


def get_debug_flag_value(chapter,debugid) :

    value   =   dfc_debug_values.get_debug_value(chapter,debugid)
    return(value)

def set_debug_flag_value(chapter,debugid,debugvalue) :

    dfc_debug_values.set_debug_value(chapter,debugid,debugvalue)

def get_debug_chapter(chapter) :

    return(dfc_debug_values.get_debug_chapter(chapter))

class DataframeCleanserDebugValues :
    
    # instance variables
    
    # error log
    debug_values               =   []
    debug_values_loaded        =   False
    
    # full constructor
    def __init__(self) :

        #print("construct debug flags : init")
        
        self.debug_values              =   []
        self.debug_values_loaded       =   False
 
        self.load_debug_values_from_file() 
        
    def get_debug_values_dir_name(self) :

        import os
        
        from dfcleanser.common.cfg import get_notebookPath, get_notebookName
        nbdir   =   get_notebookPath()
        nbname  =   get_notebookName()

        if((nbdir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(nbdir,nbname + "_files"))
   
    def get_debug_values_file_name(self) :
        
        import os

        from dfcleanser.common.cfg import get_notebookName
        eldir   =   self.get_debug_values_dir_name()
        nbname  =   get_notebookName()

        if((eldir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(eldir,nbname + "_debugvalues.json"))    
    

    def init_debug_values(self) :

        debug_chapters      =   [System_ID,DataImport_ID,DataInspection_ID,DataCleansing_ID,DataTransform_ID,DataExport_ID,
                                 SWGeocodeUtility_ID,SWZipcodeUtility_ID,SWCensusUtility_ID,DBUtils_ID,SWUtilities_ID]

        debug_values_ids    =   [Systemtext,DataImporttext,DataInspecttext,DataCleansetext,DataTransformtext,DataExporttext,
                                 Geocodetext,zipcodetext,censustext,DBUtilstext,SWUtilstext]

        self.debug_values              =   []

        for i in range(len(debug_chapters)) :

            init_chapter_values     =   []
            for j in range(len(debug_values_ids[i])) :
                init_chapter_values.append(False)

            new_chapter     =  DataframeCleanserChapterDebugValues(debug_chapters[i],debug_values_ids[i],init_chapter_values)

            self.debug_values.append(new_chapter)

        self.save_debug_values_file()

    def load_debug_values_from_file(self) :

        debug_values_dirname   =   self.get_debug_values_dir_name()

        if(not (debug_values_dirname is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist
            if(not (does_dir_exist(debug_values_dirname))) :
                make_dir(debug_values_dirname)
        
            debug_values_filename   =   self.get_debug_values_file_name()

            from dfcleanser.common.common_utils import does_file_exist
            if(not (does_file_exist(debug_values_filename))) :

                self.init_debug_values()
                self.save_debug_values_file()
                self.debug_values_loaded = True

            else :
                
                try :

                    import json

                    with open(debug_values_filename, 'r') as debug_values_file :
                        serialized_debug_values =   json.load(debug_values_file)
                        self.debug_values       =   self.deserialize_debug_values(serialized_debug_values)
                        debug_values_file.close()
                        
                    self.debug_values_loaded = True
                    
                except json.JSONDecodeError :
                    print("[Debug Values File Corrupted] "  + str(sys.exc_info()[0].__name__))
                except :
                    print("[Load Error Debug Values Error] "  + str(sys.exc_info()[0].__name__))
        
    def save_debug_values_file(self) :

        try :

            import json

            with open(self.get_debug_values_file_name(), 'w') as debug_values_file :
                json.dump(self.serialize_debug_values(),debug_values_file)
                debug_values_file.close()

        except Exception as e:
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[save_debug_values_file] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

   
    def is_debug_flags_loaded(self) :
        return(self.debug_values_loaded)

    def set_debug_value(self,chapterid,flagid,flagvalue) :

        if(not (self.is_debug_flags_loaded())) :
            self.load_debug_values_from_file()

        print("[DataframeCleanserDebugValues] : is_debug_flags_loaded",self.is_debug_flags_loaded())

        for i in range(len(self.debug_values)) :

            if(self.debug_values[i].get_chapter_id() == chapterid) :
                chapter     =   self.debug_values[i]
                print("[DataframeCleanserDebugValues] : chapter : ",chapter.get_chapter_values())
                chapter.set_debug_value(flagid,flagvalue) 
                print("[DataframeCleanserDebugValues] : chapter : after ",chapter.get_chapter_values())
                break       
        
        self.save_debug_values_file()

    def get_debug_value(self,chapterid,chaptertext) :

        if(not (self.is_debug_flags_loaded())) :
            self.load_debug_values_from_file()

        for i in range(len(self.debug_values)) :
            if(self.debug_values[i].get_chapter_id() == chapterid) :
                return(self.debug_values[i].get_debug_value(chaptertext)) 
        
        return(False)

    def get_debug_chapter(self,chapterid) :

        if(not (self.is_debug_flags_loaded())) :
            self.load_debug_values_from_file()

        for i in range(len(self.debug_values)) :
            if(self.debug_values[i].get_chapter_id() == chapterid) :
                return(self.debug_values[i]) 

    def clear_log(self) :
        self.debug_values               =   []
        
    def get_debug_values(self) :
        return(self.debug_values)

    def serialize_debug_values(self) :

        serial_debug_values     =   []
        
        for i in range(len(self.debug_values)) :
            serial_debug_values.append(self.debug_values[i].get_serial_chapter_values())
        
        return(serial_debug_values)

    def deserialize_debug_values(self,serial_values) :

        deserialized_debug_values     =   []
        
        for i in range(len(serial_values)) :

            new_deserialized_chapter    =   DataframeCleanserChapterDebugValues(serial_values[i][0],serial_values[i][1],serial_values[i][2])
            deserialized_debug_values.append(new_deserialized_chapter)
        
        return(deserialized_debug_values)
    

    def dump_debug_values(self) :

        for i in range(len(self.debug_values)) :
            print(self.debug_values[i].get_chapter_id())
            print(self.debug_values[i].get_chapter_texts())
            print(self.debug_values[i].get_chapter_values())
    
dfc_debug_values   =   DataframeCleanserDebugValues()  
