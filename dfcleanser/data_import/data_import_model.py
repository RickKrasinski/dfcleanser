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

"""
#--------------------------------------------------------------------------
#   pandas import ids
#--------------------------------------------------------------------------
"""
CSV_IMPORT          =   0
FWF_IMPORT          =   1
EXCEL_IMPORT        =   2
JSON_IMPORT         =   3
HTML_IMPORT         =   4
SQLTABLE_IMPORT     =   5
SQLQUERY_IMPORT     =   6
CUSTOM_IMPORT       =   7

"""
#--------------------------------------------------------------------------
#   import option ids
#--------------------------------------------------------------------------
"""
IMPORT_TB_ONLY                          =   0
IMPORT_PANDAS_TB_ONLY                   =   1
IMPORT_PANDAS_TB_PLUS_DETAILS           =   2
IMPORT_CUSTOM_ONLY                      =   3

"""
#------------------------------------------------------------------
#   sql input table identifiers 
#------------------------------------------------------------------
"""
DBLIBS              =   0
TABLE_NAMES         =   1
COLUMN_NAMES        =   2
DATETIME_FORMATS    =   3

SQL_CUSTOM      =   0
SQL_COMMON      =   1

PROCESS_CUSTOM_IMPORT   =       1
STORE_CUSTOM_IMPORT     =       2
DROP_CUSTOM_IMPORT      =       3

