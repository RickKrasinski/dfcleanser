"""
# data_transform_process 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]


MAIN_OPTION                                 =   0
EXTERNAL_MAP_OPTION                         =   1

DISPLAY_MAP_OPTION                          =   2
DISPLAY_DUMMY_OPTION                        =   3
DISPLAY_CATEGORY_OPTION                     =   4

TRANSFORM_OPTION                            =   5
DATA_TYPE_OPTION                            =   6

DATAFRAME_DISPLAY_OPTION                    =   9
DATAFRAME_PROCESS_OPTION                    =   10

DISPLAY_TRANSFORM_COLS_OPTION               =   11
PROCESS_TRANSFORM_COLS_OPTION               =   13

DISPLAY_DATETIME_TRANSFORM_OPTION           =   13

PROCESS_DATETIME_TRANSFORM_OPTION           =   14
PROCESS_DATETIME_TIMEDELTA_OPTION           =   15
PROCESS_DATETIME_MERGESPLIT_OPTION          =   16

PROCESS_DF_SCHEMA_TRANSFORM_OPTION          =   17

DISPLAY_TRANSFORM_COLS_FROM_CLEANSE_OPTION  =   18



DISPLAY_DATAFRAME_TRANSFORM                 =   0
DISPLAY_COLUMNS_TRANSFORM                   =   1
DISPLAY_DATETIME_TRANSFORM                  =   2
DISPLAY_DF_SCHEMA_TRANSFORM                 =   3
DFC_TRANSFORM_RETURN                        =   5

DISPLAY_DATETIME_DATATYPE                   =   0
DISPLAY_DATE_DATATYPE                       =   1
DISPLAY_TIME_DATATYPE                       =   2
DISPLAY_TIMEDELTA                           =   3
DISPLAY_DATETIME_SPLIT                      =   4
DISPLAY_DATETIME_MERGE                      =   5

SPLIT                                       =   0
MERGE                                       =   1

DISPLAY_NO_FUNCTIONS                        =   0
DISPLAY_FUNCTIONS                           =   1


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Dataframe transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
SAVE_COLUMN_NAMES_ROW           =   0
ADD_COLUMN_NAMES_ROW            =   1
RESET_ROW_IDS                   =   2
SET_NEW_ROW_IDS_COL             =   3
DROP_ROW_IDS_COL                =   4
SORT_ROWS                       =   5
DROP_DUPLICATE_ROWS             =   6
DF_TRANSFORM_RETURN             =   7
DF_TRANSFORM_HELP               =   8

SET_NEW_ROW_IDS_COL_SEL         =   9

CHANGE_COLUMN_NAMES             =   10


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Column transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

CATS_TASKBAR                    =   0

RENAME_COLUMN                   =   1
ADD_COLUMN                      =   2
DROP_COLUMN                     =   3
REORDER_COLUMNS                 =   4
MAP_COLUMN                      =   5
DUMMIES_COLUMN                  =   6
CAT_COLUMN                      =   7
DATATYPE_COLUMN                 =   8
CLEAR_COLUMN                    =   9
HELP_COLUMN                     =   10

SAVE_COLUMN                     =   11
COPY_COLUMN                     =   12

DATETIME_DATATYPE_COLUMN        =   13

SORT_COLUMN                     =   14
APPLY_COLUMN                    =   15
APPLY_COLUMN_GF                 =   16
        
"""
#--------------------------------------------------------------------------
#    display transform column options ids
#--------------------------------------------------------------------------
"""
RENAMING                =   1
ADDING                  =   2
DROPPING                =   3
MOVING                  =   4
MAPPING                 =   5
DUMMIES                 =   6
CATEGORIES              =   7
DATATYPE                =   8
SAVING                  =   11
COPYING                 =   12

SORTING                 =   14
APPLYING                =   15
APPLYING_SEL_FUN        =   16


RENAMING_DETAILS        =   21
ADDING_DETAILS          =   22
DROPPING_DETAILS        =   23
MOVING_DETAILS          =   24
MAPPING_DETAILS         =   25
DUMMIES_DETAILS         =   26
CATEGORIES_DETAILS      =   27
DATATYPE_DETAILS        =   28
SAVING_DETAILS          =   31
COPYING_DETAILS         =   32

SORTING_DETAILS         =   34
APPLYING_DETAILS        =   35
APPLYING_DETAILS_GF     =   36

ADD_COLUMN_CLEAR        =   4        
ADD_COLUMN_RETURN       =   5

"""
#--------------------------------------------------------------------------
#    display add column transform options ids
#--------------------------------------------------------------------------
"""
DISPLAY_BASE_ADD_OPTION             =   -1
DISPLAY_ADD_FROM_FILE_OPTION        =   0
DISPLAY_ADD_FROM_CODE_OPTION        =   1
   
PROCESS_FILE_OPTION                 =   13
PROCESS_MAKE_NEW_CODE_OPTION        =   14
PROCESS_ADD_NEW_CODE_OPTION         =   15
PROCESS_SELECT_FUNC_OPTION          =   16
DISPLAY_GENERIC_FUNCTIONS_OPTION    =   17

