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


"""
#--------------------------------------------------------------------------
#    Data Transform Main Taskbar Option IDs
#--------------------------------------------------------------------------
"""

MAIN_OPTION                                 =   0

DISPLAY_DATAFRAME_TRANSFORM                 =   1
DISPLAY_COLUMNS_TRANSFORM                   =   2
DISPLAY_DATETIME_TRANSFORM                  =   3

DFC_TRANSFORM_RETURN                        =   5

TRANSFORM_COLS_OPTION                       =   6

DATAFRAME_DISPLAY_OPTION                    =   9
DATAFRAME_PROCESS_OPTION                    =   10

DISPLAY_DATETIME_OPTION                     =   13
PROCESS_DATETIME_OPTION                     =   14

DISPLAY_DATETIME_FORMAT_OPTION              =   15

DISPLAY_DATETIME_TIMEDELTA_OPTION           =   16
PROCESS_DATETIME_TIMEDELTA_OPTION           =   17

DISPLAY_DATETIME_MERGE_OPTION               =   18
PROCESS_DATETIME_MERGE_OPTION               =   19

DISPLAY_DATETIME_SPLIT_OPTION               =   20
PROCESS_DATETIME_SPLIT_OPTION               =   21

DISPLAY_TIMEDELTA_CALCULATE_OPTION          =   22
PROCESS_TIMEDELTA_CALCULATE_OPTION          =   23

DISPLAY_DATETIME_COMPONNETS_OPTION          =   24
PROCESS_DATETIME_COMPONNETS_OPTION          =   25

PROCESS_DATETIME_RETURN                     =   26

DISPLAY_DATETIME_COMP_TD_OPTION             =   28

DISPLAY_DATATYPE_OPTION                     =   41
PROCESS_DATATYPE_OPTION                     =   44

PROCESS_CHECK_COMPATABILITY                 =   45


SPLIT                                       =   0
MERGE                                       =   1


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Dataframe transform taskbar processing ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_SAVE_COLUMN_NAMES_ROW           =   100
DISPLAY_ADD_COLUMN_NAMES_ROW            =   101
DISPLAY_CHANGE_COLUMN_NAMES             =   102

DISPLAY_SET_DF_INDEX                    =   103
DISPLAY_RESET_DF_INDEX                  =   104
DISPLAY_APPEND_TO_INDEX                 =   105
DISPLAY_SORT_DF_INDEX                   =   106
DISPLAY_DROP_DUPLICATE_ROWS             =   107
DF_TRANSFORM_RETURN                     =   108
DF_TRANSFORM_HELP                       =   109

PROCESS_SAVE_COLUMN_NAMES_ROW           =   110
PROCESS_ADD_COLUMN_NAMES_ROW            =   111
PROCESS_CHANGE_COLUMN_NAMES             =   112
PROCESS_SET_DF_INDEX                    =   113
PROCESS_RESET_DF_INDEX                  =   114
PROCESS_APPEND_TO_INDEX                 =   115
PROCESS_SORT_DF_INDEX                   =   116
PROCESS_DROP_DUPLICATE_ROWS             =   117

DISPLAY_SHOW_DF_INDEX                   =   118

PROCESS_SHOW_COLUMN_NAMES_ROW           =   120
PROCESS_DROP_COLUMN_NAMES_ROW           =   121

DISPLAY_COLUMN_NAMES_OPTIONS            =   122
DISPLAY_INDICES_OPTIONS                 =   123

DISPLAY_SORT_COLUMN                     =   124
PROCESS_SORT_COLUMN                     =   125

DISPLAY_WHITESPACE_COLUMN_NAMES         =   126
PROCESS_WHITESPACE_COLUMN_NAMES         =   127



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Columns transform taskbar processing options
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
MORE_TASKBAR                            =   200

DISPLAY_RENAME_COLUMN                   =   201
DISPLAY_ADD_COLUMN                      =   202
DISPLAY_DROP_COLUMN                     =   203
DISPLAY_REORDER_COLUMNS                 =   204
DISPLAY_MAP_COLUMN                      =   205
DISPLAY_DUMMIES_COLUMN                  =   206
DISPLAY_CAT_COLUMN                      =   207
DISPLAY_DATATYPE_COLUMN                 =   208
DISPLAY_CLEAR_COLUMN                    =   209
DISPLAY_HELP_COLUMN                     =   210
DISPLAY_SAVE_COLUMN                     =   211
DISPLAY_COPY_COLUMN                     =   212
DISPLAY_APPLY_COLUMN                    =   214
DISPLAY_APPLY_USER_FN_COLUMN            =   215

RETURN_CLEAR_COLUMN                     =   216

DISPLAY_APPLY_COLUMN_UNIQUES            =   217
DISPLAY_APPLY_USER_FN_COLUMN_UNIQUES    =   218
DISPLAY_APPLY_CHANGE_FN                 =   219

DISPLAY_DATATYPE_CHANGE_NA              =   220
DISPLAY_DATATYPE_UNIQUES                =   221
DISPLAY_CHECK_COMPATABILITY             =   222
DISPLAY_CHECK_COMPATABILITY_UNIQUES     =   223

DISPLAY_CAT_COLUMN_EXCLUDE              =   224

PROCESS_RENAME_COLUMN                   =   250
PROCESS_DROP_COLUMN                     =   251
PROCESS_SAVE_COLUMN                     =   252
PROCESS_REORDER_COLUMNS                 =   253
PROCESS_COPY_COLUMN                     =   254
PROCESS_APPLY_COLUMN                    =   256
PROCESS_MAP_COLUMN                      =   257
PROCESS_MAP_COLUMN_VALUES               =   258
PROCESS_MAP_COLUMN_FUNCTION             =   259
PROCESS_DUMMIES_COLUMN                  =   260
PROCESS_CAT_COLUMN                      =   261
PROCESS_CAT_COLUMN_EXCLUDE              =   262

DISPLAY_CAT_COLUMN_EXTERNAL             =   265


PROCESS_CHANGE_DATATYPE_COLUMNS         =   270
PROCESS_APPLY_USER_FN_COLUMN            =   271

PROCESS_SAVE_COLUMN_WITH_INDEX          =   273


MAP_FROM_FILE                           =   0
MAP_FROM_VALUES                         =   1
MAP_FROM_FUNCTION                       =   2


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
ADDING                  =   2
DATATYPE                =   8


"""
#--------------------------------------------------------------------------
#    display transform column display details ids
#--------------------------------------------------------------------------
"""
APPLYING_DETAILS            =   35
APPLYING_DETAILS_PARMS      =   36


"""
#--------------------------------------------------------------------------
#    add column transform option ids
#--------------------------------------------------------------------------
"""
DISPLAY_BASE_ADD_OPTION                     =   -1

DISPLAY_ADD_FROM_FILE_OPTION                =   400
PROCESS_ADD_FROM_FILE_OPTION                =   401

DISPLAY_ADD_FROM_CODE_OPTION                =   402
PROCESS_ADD_FROM_CODE_OPTION                =   403

DISPLAY_ADD_FROM_DFC_FUNCS                  =   404
DISPLAY_ADD_FROM_DFC_FUNCS_PARMS            =   405
PROCESS_ADD_FROM_DFC_FUNCS                  =   406

DISPLAY_ADD_FROM_DF_OPTION                  =   407
PROCESS_ADD_FROM_DF_OPTION                  =   408

ADD_COLUMN_CLEAR                            =   411        
ADD_COLUMN_RETURN                           =   412

DISPLAY_ADD_FROM_FILE_WITH_INDEX_OPTION     =   415
PROCESS_ADD_FROM_FILE_WITH_INDEX_OPTION     =   416

PROCESS_DELETE_USER_FUNC                    =   420

DISPLAY_MAINTAIN_USER_FUNC                  =   421
PROCESS_SAVE_USER_FUNC                      =   422

DISPLAY_ADD_FROM_CODE_FN_OPTION             =   423

CLEAR_SOURCE_PARMS                          =   430
CLEAR_OUTPUT_PARMS                          =   431


DISPLAY_NO_FUNCTIONS                        =   0
DISPLAY_FUNCTIONS                           =   1



"""
#--------------------------------------------------------------------------
#    add column transform processing ids
#--------------------------------------------------------------------------
"""  

 
#PROCESS_FILE_OPTION                 =   13
#PROCESS_MAKE_NEW_CODE_OPTION        =   14
#PROCESS_SELECT_FUNC_OPTION          =   16
#DISPLAY_GENERIC_FUNCTIONS_OPTION    =   17





"""
#--------------------------------------------------------------------------
#    dataframe schema 
#--------------------------------------------------------------------------
"""  


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
UNKNOWN_STATUS          =   0
INT_STATUS              =   1
FLOAT_STATUS            =   2
DATETIME_STATUS         =   3


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   check compatability data type values 
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
VALUES_OK                               =   -1
VALUE_OUT_OF_RANGE                      =   0
PRECISION_LOSS                          =   1
VALUE_NOT_NUMERIC                       =   2
VALUE_NOT_DATATYPE_COMPATABLE           =   3


MIN_DATETIME_TIMEDELTA_SECONDS          =   -86399999913600.0
MIN_DATETIME_TIMEDELTA_MILLISECONDS     =   1000 * MIN_DATETIME_TIMEDELTA_SECONDS
MIN_DATETIME_TIMEDELTA_MICROSECONDS     =   1000 * MIN_DATETIME_TIMEDELTA_MILLISECONDS
MIN_DATETIME_TIMEDELTA_NANOSECONDS      =   1000 * MIN_DATETIME_TIMEDELTA_MICROSECONDS

MAX_DATETIME_TIMEDELTA_SECONDS          =   86400000000000
MAX_DATETIME_TIMEDELTA_MILLISECONDS     =   1000 * MAX_DATETIME_TIMEDELTA_SECONDS
MAX_DATETIME_TIMEDELTA_MICROSECONDS     =   1000 * MAX_DATETIME_TIMEDELTA_MILLISECONDS
MAX_DATETIME_TIMEDELTA_NANOSECONDS      =   1000 * MAX_DATETIME_TIMEDELTA_MICROSECONDS

MIN_NP_TIMEDELTA_SECONDS                =   -1943161946.9376225
MIN_NP_TIMEDELTA_MILLISECONDS           =   1000 * MIN_NP_TIMEDELTA_SECONDS
MIN_NP_TIMEDELTA_MICROSECONDS           =   1000 * MIN_NP_TIMEDELTA_MILLISECONDS
MIN_NP_TIMEDELTA_NANOSECONDS            =   1000 * MIN_NP_TIMEDELTA_MICROSECONDS

MAX_NP_TIMEDELTA_SECONDS                =   1943161946.9376225
MAX_NP_TIMEDELTA_MILLISECONDS           =   1000 * MAX_NP_TIMEDELTA_SECONDS
MAX_NP_TIMEDELTA_MICROSECONDS           =   1000 * MAX_NP_TIMEDELTA_MILLISECONDS
MAX_NP_TIMEDELTA_NANOSECONDS            =   1000 * MAX_NP_TIMEDELTA_MICROSECONDS






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

    def set_col_status(self,colname,dtype,status) :
        
        statuslist  =  self.statusdict.get(colname,None) 
        if(statuslist is None) :
            statuslist  =   [None,None,None]
            
        if(dtype == INT_STATUS)         :   statuslist[0]   =   status
        elif(dtype == FLOAT_STATUS)     :   statuslist[1]   =   status
        else                            :   statuslist[2]   =   status
        
        self.statusdict.update({colname:statuslist})
        
    def get_col_status(self,colname,dtype) :
        
        statuslist  =  self.statusdict.get(colname,None) 
        
        if(statuslist is None) :
            
            return(None)
            
        else :
            
            if(dtype == INT_STATUS)         :   return(statuslist[0])
            elif(dtype == FLOAT_STATUS)     :   return(statuslist[1])
            else                            :   return(statuslist[2])

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
    def __init__(self,stats_dict    =   {}) :
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









