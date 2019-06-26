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

DISPLAY_DATAFRAME_TRANSFORM                 =   1
DISPLAY_COLUMNS_TRANSFORM                   =   2
DISPLAY_DATETIME_TRANSFORM                  =   3
DISPLAY_DF_SCHEMA_TRANSFORM                 =   4

DFC_TRANSFORM_RETURN                        =   5





TRANSFORM_OPTION                            =   6




DATAFRAME_DISPLAY_OPTION                    =   9
DATAFRAME_PROCESS_OPTION                    =   10

DISPLAY_TRANSFORM_COLS_OPTION               =   11

DISPLAY_DATETIME_OPTION                     =   13

PROCESS_DATETIME_OPTION                     =   14
PROCESS_DATETIME_TIMEDELTA_OPTION           =   15
PROCESS_DATETIME_MERGESPLIT_OPTION          =   16

PROCESS_DF_SCHEMA_OPTION                    =   17

PROCESS_DATETIME_COMPONNETS_OPTION          =   21


CHANGE_NA_OPTION                            =   38

DISPLAY_DROP_NA_OPTION                      =   39
DISPLAY_FILL_NA_OPTION                      =   40
DISPLAY_DATATYPE_OPTION                     =   41

PROCESS_DROP_NA_OPTION                      =   42
PROCESS_FILL_NA_OPTION                      =   43
PROCESS_DATATYPE_OPTION                     =   44

PROCESS_CHECK_NUMERIC                       =   45

"""
#--------------------------------------------------------------------------
#    Datatime Transform Taskbar Display IDs
#--------------------------------------------------------------------------
"""
DISPLAY_DATETIME_DATATYPE                   =   0
DISPLAY_DATE_DATATYPE                       =   1
DISPLAY_TIME_DATATYPE                       =   2
DISPLAY_TIMEDELTA                           =   3
DISPLAY_DATETIME_SPLIT                      =   4
DISPLAY_DATETIME_MERGE                      =   5
DISPLAY_DATETIME_COMPONENTS                 =   6

SPLIT                                       =   0
MERGE                                       =   1

DISPLAY_NO_FUNCTIONS                        =   0
DISPLAY_FUNCTIONS                           =   1


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Dataframe transform taskbar processing ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
SAVE_COLUMN_NAMES_ROW           =   0
ADD_COLUMN_NAMES_ROW            =   1
CHANGE_COLUMN_NAMES             =   2
SET_NEW_ROW_IDS_COL             =   3
RESET_ROW_IDS                   =   4
DROP_ROW_IDS_COL                =   5
SORT_ROWS                       =   6
DROP_DUPLICATE_ROWS             =   7
DF_TRANSFORM_RETURN             =   8
DF_TRANSFORM_HELP               =   9


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Columns transform taskbar processing options
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
MORE_TASKBAR                    =   0

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
SORT_COLUMN                     =   13
APPLY_COLUMN                    =   14
APPLY_COLUMN_GF                 =   15


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display transform column display ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    display transform column display intermediate ids
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
SORTING                 =   13
APPLYING                =   14
APPLYING_SEL_FUN        =   15



"""
#--------------------------------------------------------------------------
#    display transform column display details ids
#--------------------------------------------------------------------------
"""
RENAMING_DETAILS            =   21
ADDING_DETAILS              =   22
DROPPING_DETAILS            =   23
MOVING_DETAILS              =   24
MAPPING_DETAILS             =   25
DUMMIES_DETAILS             =   26
CATEGORIES_DETAILS          =   27
DATATYPE_DETAILS            =   28
SAVING_DETAILS              =   31
COPYING_DETAILS             =   32

SORTING_DETAILS             =   34
APPLYING_DETAILS            =   35
APPLYING_DETAILS_GF         =   36
APPLYING_DETAILS_GF_DESC    =   37


"""
#--------------------------------------------------------------------------
#    apply fn to column transform processing ids
#--------------------------------------------------------------------------
"""
APPLY_FN_COLUMN_SAVE    =   6
APPLY_FN_COLUMN_APPLY   =   7
APPLY_FN_COLUMN_SHOW    =   8
APPLY_FN_COLUMN_CLEAR   =   9
APPLY_FN_COLUMN_RETURN  =   10


"""
#--------------------------------------------------------------------------
#    add column transform display ids
#--------------------------------------------------------------------------
"""
DISPLAY_BASE_ADD_OPTION             =   -1
DISPLAY_ADD_FROM_FILE_OPTION        =   0
DISPLAY_ADD_FROM_CODE_OPTION        =   1
DISPLAY_ADD_FROM_DF_OPTION          =   2

"""
#--------------------------------------------------------------------------
#    add column transform processing ids
#--------------------------------------------------------------------------
"""  
ADD_COLUMN_CLEAR        =   4        
ADD_COLUMN_RETURN       =   5
 
PROCESS_FILE_OPTION                 =   13
PROCESS_MAKE_NEW_CODE_OPTION        =   14
PROCESS_ADD_NEW_CODE_OPTION         =   15
PROCESS_SELECT_FUNC_OPTION          =   16
DISPLAY_GENERIC_FUNCTIONS_OPTION    =   17
PROCESS_ADD_NEW_FROM_DF_OPTION      =   18


"""
#--------------------------------------------------------------------------
#    na options
#--------------------------------------------------------------------------
"""
DROP_NA_OPTION          =   0
FILL_NA_OPTION          =   1
NO_NA_OPTION            =   2


"""
#--------------------------------------------------------------------------
#    check numeric status
#--------------------------------------------------------------------------
"""  
UNKNOWN_STATUS      =   0
INT_STATUS          =   1
FLOAT_STATUS        =   2
NOT_INT_STATUS      =   3
NOT_FLOAT_STATUS    =   4


UNKNOWN_TEXT        =   "&nbsp;Unknown"
INT_TEXT            =   "&nbsp;Can Be Int"
FLOAT_TEXT          =   "&nbsp;Can Be Float"
NOT_INT_TEXT        =   "&nbsp;Can Not Be Int"
NOT_FLOAT_TEXT      =   "&nbsp;Can Not Be Float"


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   working data
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

"""
#------------------------------------------------------------------
#   check numeric candidate status
#------------------------------------------------------------------
""" 

class chknum_status :
   
    # full constructor
    def __init__(self,    
                 status_dict    =   {}) :
        
        # minimum init attributes
        self.statusdict     =   status_dict

    def set_col_status(self,colname,status) :
        self.statusdict.update({colname:status})
        
    def get_col_status(self,colname) :
        return(self.statusdict.get(colname,UNKNOWN_STATUS))
        
    def clear_chknum_status(self) :
        self.statusdict     =   {}

checknum_status     =   chknum_status()


"""
#------------------------------------------------------------------
#   dfschema col stats
#------------------------------------------------------------------
""" 

class dfschema_stats :
   
    # full constructor
    def __init__(self,    
                 stats_dict    =   {}) :
        
        # minimum init attributes
        self.statsdict     =   stats_dict

    def set_col_status(self,colname,status) :
        self.statusdict.update({colname:status})
    
    def get_df_title(self) :
        return(self.statsdict.get("df_title"))
        
    def get_col_list(self) :
        return(self.statsdict.get("df_cols"))
    
    def get_col_dtypes(self) :
        return(self.statsdict.get("df_dtypes"))
    
    def get_col_nans(self) :
        return(self.statsdict.get("df_nans"))
    
    def get_col_uniques(self) :
        return(self.statsdict.get("df_uniques"))
        
    def clear_dfschema_stats(self) :
        self.statsdict     =   {}
    
    def reload_dfschema_stats(self,statsd) :
        self.statsdict     =   statsd

schema_dict     =   dfschema_stats()









