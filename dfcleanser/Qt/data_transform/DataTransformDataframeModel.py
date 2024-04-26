"""
# DataTransformDataframeModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.sw_utilities.dfc_qt_model import (maketextarea)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                 dataframe transform sort df forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    sort df by column
#--------------------------------------------------------------------------
"""
sort_df_column_input_title               =   "Sort Column"
sort_df_column_input_id                  =   "sortcolInput"
sort_df_column_input_idList              =   ["sortcol",
                                             "sortOrder",
                                             "sortkind",
                                             "sortna",
                                             "resetRowIds",
                                             None,None,None]

sort_df_column_input_labelList           =   ["sort_column_name",
                                             "ascending_order_flag",
                                             "kind",
                                             "na_position",
                                             "reset_row_index_flag",
                                             "Sort By</br>Column",
                                             "Return","Help"]

sort_df_column_input_typeList            =   ["text","select","select","select","select",
                                             "button","button","button"]

sort_df_column_input_placeholderList     =   ["column to sort",
                                             "ascending sort order (default = False)",
                                             "sort method (default = quicksort)",
                                             "na position (default = last)",
                                             "reorder the row id column after the sort (default True)",
                                             None,None,None]

sort_df_column_input_reqList             =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               dataframe transform column name rows forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dataframe remove column id row inputs
#--------------------------------------------------------------------------
"""
df_save_row_transform_input_title           =   "Save Column Names Row"
df_save_row_transform_input_id              =   "savecolnamestransform"
df_save_row_transform_input_idList          =   ["filesavename",
                                                 None,None,None]

df_save_row_transform_input_labelList       =   ["column_names_file_name",
                                                 "Save Column</br> Names",
                                                 "Return","Help"]

df_save_row_transform_input_typeList        =   ["file",
                                                 "button","button","button"]

df_save_row_transform_input_placeholderList     = ["enter File name to save column names to or browse to file below (default use df name)",
                                                   None,None,None]

df_save_row_transform_input_reqList         =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe add column id row inputs
#--------------------------------------------------------------------------
"""
df_add_row_transform_input_title            =   "Add Column Names Row"
df_add_row_transform_input_id               =   "addcolnamestransform"
df_add_row_transform_input_idList           =   ["filereadname",
                                                 "newcolname",
                                                 None,None,None]

df_add_row_transform_input_labelList        =   ["column_names_file_name",
                                                 "column_names",
                                                 "Add Column</br> Names Row",
                                                 "Return","Help"]

df_add_row_transform_input_typeList         =   ["file",maketextarea(6),
                                                 "button","button","button"]

df_add_row_transform_input_placeholderList  =   ["enter File name to read or browse to file (default see below)",
                                                 "enter new column names)",
                                                 None,None,None]

df_add_row_transform_input_reqList          =   [0,1]


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Dataframe Index flags                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DF_INDEX_MAIN                               =   0
DF_SHOW_INDEX                               =   1
DF_SET_INDEX                                =   2
DF_RESET_INDEX                              =   3
DF_REINDEX_INDEX                            =   4
DF_APPEND_INDEX                             =   5
DF_SORT_INDEX                               =   6

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                    dataframe transform index forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_index_transform_input_title            =   "Set New Index Column"
df_set_index_transform_input_id               =   "setnewindextransform"
df_set_index_transform_input_idList           =   ["setnewindexindexcols",
                                                   "setnewindexdrop",
                                                   "setnewindexverify",
                                                   None,None,None]

df_set_index_transform_input_labelList        =   ["columns_for_index",
                                                   "drop_original_column(s)",
                                                   "verify_integrity",
                                                   "Set</br>Index",
                                                   "Return","Help"]

df_set_index_transform_input_typeList         =   [maketextarea(2),"select","select",
                                                   "button","button","button"]

df_set_index_transform_input_placeholderList  =  ["columns for the index",
                                                  "drop df column (default : True)",
                                                   "verify integrity",
                                                   None,None,None]

df_set_index_transform_input_reqList          =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe reset row ids col inputs
#--------------------------------------------------------------------------
"""
df_reset_index_transform_input_title        =   "Reset Index Column"
df_reset_index_transform_input_id           =   "resetindextransform"
df_reset_index_transform_input_idList       =   ["resetindexdroplevels",
                                                 "resetindexlevels",
                                                 "resetindexinsertlevel",
                                                 None,None,None]

df_reset_index_transform_input_labelList    =   ["index_columns_to_drop",
                                                 "index_levels",
                                                 "insert_dropped_index_columns_back_into_df",
                                                 "Reset</br>Index",
                                                 "Return","Help"]

df_reset_index_transform_input_typeList     =   [maketextarea(2),"select","select",
                                                 "button","button","button"]

df_reset_index_transform_input_placeholderList =  ["index levels to drop",
                                                   "index levels list",
                                                   "insert df levels to df flag (default : True)",
                                                   None,None,None]

df_reset_index_transform_input_reqList      =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe reindex index inputs
#--------------------------------------------------------------------------
"""
df_reindex_index_transform_input_title      =   "ReIndex Index Column"
df_reindex_index_transform_input_id         =   "reindexindextransform"
df_reindex_index_transform_input_idList     =   ["reindexkeywords",
                                                 "reindexfillmethod",
                                                 "reindexfillvalue",
                                                 "reindexlevel",
                                                 "reindexlimit",
                                                 "reindextolerance",
                                                 None,None,None]

df_reindex_index_transform_input_labelList  =   ["keywords",
                                                 "fill_method",
                                                 "fill_value",
                                                 "level",
                                                 "limit",
                                                 "tolerance",
                                                 "ReIndex</br>Index",
                                                 "Return","Help"]

df_reindex_index_transform_input_typeList   =   ["text","select","text","text","text","text",
                                                 "button","button","button"]

df_reindex_index_transform_input_placeholderList =  ["index keywords",
                                                     "fill methods",
                                                     "fill value",
                                                     "level",
                                                     "limit",
                                                     "tolerance",
                                                   None,None,None]

df_reindex_index_transform_input_reqList    =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_append_index_transform_input_title         =   "Append Index Column"
df_append_index_transform_input_id            =   "appendindextransform"
df_append_index_transform_input_idList        =   ["appendindexcols",
                                                   "appendindexdrop",
                                                   "appendindexverify",
                                                   None,None,None]

df_append_index_transform_input_labelList     =   ["columns_to_append",
                                                   "drop_index_column_name(s)_cols_from_df",
                                                   "verify_integrity",
                                                   "Append</br>Index",
                                                   "Return","Help"]

df_append_index_transform_input_typeList      =   [maketextarea(2),"select","select",
                                                   "button","button","button"]

df_append_index_transform_input_placeholderList   =  ["append columns",
                                                      "drop df column (default : False)",
                                                      "verify integrity",
                                                      None,None,None]

df_append_index_transform_input_reqList       =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe sort row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_index_transform_input_title            =   "Sort Row Index Column"
df_sort_index_transform_input_id               =   "sortindextransform"
df_sort_index_transform_input_idList           =   ["sortindexorder",
                                                    "sortindexsortkind",
                                                    "sortindexnaposition",
                                                    None,None,None]

df_sort_index_transform_input_labelList        =   ["ascending",
                                                    "kind",
                                                    "na_position",
                                                    "Sort</br>Index",
                                                    "Return","Help"]

df_sort_index_transform_input_typeList         =   ["select","select","select",
                                                    "button","button","button"]

df_sort_index_transform_input_placeholderList  =   ["Order of sort : True - ascending - False - descending (default True )",
                                                    "sort method quicksort, mergesort, heapsort (default - quicksort )",
                                                    "where to put nas - first : last (default - last )",
                                                    None,None,None]

df_sort_index_transform_input_reqList          =   [0,1,2]




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Dataframe Transform flags                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DATETIME_MAIN                               =   0
DATETIME_CONVERT                            =   1
DATETIME_CONVERT_TIMEDELTA                  =   2
DATETIME_CALCULATE_TIMEDELTA                =   3
DATETIME_SPLIT                              =   4
DATETIME_MERGE                              =   5
DATETIME_COMPONENTS                         =   6
DATETIME_TIME_CONVERT                       =   7

MERGE     = 0
SPLIT     = 1

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                          datetime convert forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

error_handlers          =   ["raise","coerce","ignore"]
error_handlers_text     =   ["raise exception and terminate","coerce and set result to NaT","ignore and set result to input"]

"""
#--------------------------------------------------------------------------
#   datetime format input 
#--------------------------------------------------------------------------
"""
datetime_format_input_title            =   "Datetime Format"
datetime_format_input_id               =   "datetimeformatinput"
datetime_format_input_idList           =   ["dtcolname",
                                            "dtnanthreshold",
                                            "dterrors",
                                            "dtformatstring",
                                            "dtformatstrings",
                                            None,None,None,None]

datetime_format_input_labelList        =   ["column_to_convert",
                                            "NaT_threshold",
                                             "errors",
                                             "format_string",
                                             "format_strings",
                                             "Convert</br>to</br>datetime",
                                             "Convert</br>to</br>datetime.time",
                                             "Return","Help"]

datetime_format_input_typeList         =   ["text","text","select","text","select","button","button","button","button"]

datetime_format_input_placeholderList  =   ["column to convert",
                                            "percent of NaTs to cancel convert : default (do not check)",
                                             "parse error handling (default = NaT)",
                                             "format string to use (default = infer)",
                                             "format strings samples",
                                             None,None,None,None]

datetime_format_input_reqList          =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   datetime.time format input 
#--------------------------------------------------------------------------
"""
datetime_time_format_input_title            =   "Datetime Format"
datetime_time_format_input_id               =   "datetimeformatinput"
datetime_time_format_input_idList           =   ["dtcolname",
                                                "dtnanthreshold",
                                                "dterrors",
                                                "dtincrubits",
                                                "dtunitstype",
                                                None,None,None]

datetime_time_format_input_labelList        =   ["column_to_convert",
                                                "NaT_threshold",
                                                "errors",
                                                "units_per_increment",
                                                "type_of_units",
                                                "Convert</br>to</br>datetime.time",
                                                "Return","Help"]

datetime_time_format_input_typeList         =   ["text","text","select","text","select",
                                                 "button","button","button"]

datetime_time_format_input_placeholderList  =   ["column to convert",
                                                "percent of NaTs to cancel convert : default (do not check)",
                                                "parse error handling (default = NaT)",
                                                "number of units per increment",
                                                "units type",
                                                None,None,None]

datetime_time_format_input_reqList          =   [0,1,2,3]



"""
#--------------------------------------------------------------------------
#   timedelta format input 
#--------------------------------------------------------------------------
"""
timedelta_format_input_title            =   "timedelta Format"
timedelta_format_input_id               =   "timedeltaformatinput"
timedelta_format_input_idList           =   ["dtcolname",
                                             "dtnanthreshold",
                                             "tdunits",
                                             "tderrors",
                                             None,None,None]

timedelta_format_input_labelList        =   ["column_to_convert",
                                             "NaT_threshold",
                                             "units",
                                             "errors",
                                             "Convert</br>to</br>timedelta",
                                             "Return","Help"]

timedelta_format_input_typeList         =   ["text","text","select","select","button","button","button"]

timedelta_format_input_placeholderList  =   ["column to convert",
                                             "percent of NaTs to cancel convert : default (do not check)",
                                             "units of time (default = infer)",
                                             "parse error handling (default = NaT)",
                                             None,None,None]

timedelta_format_input_reqList          =   [0,1,2,3]


timedelta_units         =   ["Y","M","W","D","hours","minutes","seconds","milliseconds","microseconds","nanoseconds"]


error_handlers          =   ["raise","coerce","ignore"]
error_handlers_text     =   ["raise exception and terminate","coerce and set result to NaT","ignore and set result to input"]


"""
#--------------------------------------------------------------------------
#   datetime calculate timedelta input 
#--------------------------------------------------------------------------
"""
datetime_tdelta_input_title             =   "Datetime timedelta"
datetime_tdelta_input_id                =   "datetimetdeltainput"
datetime_tdelta_input_idList            =   ["dtcolname1",
                                             "dtcolname2",
                                             "dtcolnamesel",
                                             "dttdrescolname",
                                             "dttdelta",
                                             "dttdunits",
                                             None,None,None]

datetime_tdelta_input_labelList         =   ["datetime_column_name1",
                                             "datetime_column_name2",
                                             "column_name_select",
                                             "new_timedelta_column_name",
                                             "new_timedelta_column_name_data_type",
                                             "time_units",
                                             "Calculate</br>timedelta",
                                             "Return","Help"]

datetime_tdelta_input_typeList          =   ["text","text","select","text","select","select",
                                             "button","button","button"]

datetime_tdelta_input_placeholderList   =   ["colname 1",
                                             "colname 2",
                                             "colname select",
                                             "result time delta column name",
                                             "result time delta column name data type",
                                             "time delta units",
                                              None,None,None]

datetime_tdelta_input_reqList           =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#   datetime split input 
#--------------------------------------------------------------------------
"""
datetime_split_input_title              =   "Datetime Split"
datetime_split_input_id                 =   "datetimetsplitinput"
datetime_split_input_idList             =   ["dtscolname",
                                             "dtsdatecolname",
                                             "dtstimecolname",
                                             None,None,None]

datetime_split_input_labelList          =   ["datetime_column_name",
                                             "new_datetime.date_column_name",
                                             "new_datetime.time_column_name",
                                             "Split</br>Column",
                                              "Return","Help"]

datetime_split_input_typeList           =   ["text","text","text","button","button","button"]

datetime_split_input_placeholderList    =   ["datetime column name",
                                             "date column name",
                                             "time column name",
                                              None,None,None]

datetime_split_input_reqList            =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   datetime merge input 
#--------------------------------------------------------------------------
"""
datetime_merge_input_title              =   "Datetime Merge"
datetime_merge_input_id                 =   "datetimetmergeinput"
datetime_merge_input_idList             =   ["dtmdateolname",
                                             "dttimecolname"
                                             "dtmselcolname",
                                             "dtmdatetimecolname",
                                             "dtmdatatype",
                                             "dtmthresh",
                                             "dtmerror",
                                             None,None,None]

datetime_merge_input_labelList          =   ["date_column_name",
                                             "time_column_name",
                                             "select_column_name_type",
                                             "new_datetime_column_name",
                                             "new_datetime_column_data_type",
                                             "NaT_threshold",
                                             "errors",
                                             "Merge</br>Columns",
                                             "Return","Help"]

datetime_merge_input_typeList           =   ["text","text","select","text","select","text","select",
                                             "button","button","button"]

datetime_merge_input_placeholderList    =   ["existing date column name",
                                             "existing time column name",
                                             "select colname type",
                                             "new datetime merged column name",
                                             "new datetime merged column data type",
                                             "merge nat threshold",
                                             "merge nat error",
                                              None,None,None]

datetime_merge_input_reqList            =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#   datetime components input 
#--------------------------------------------------------------------------
"""
datetime_comp_input_title               =   "Datetime Split"
datetime_comp_input_id                  =   "datetimecompinput"
datetime_comp_input_idList              =   ["dtccolname",
                                             "dtcresultcolname",
                                             "dtccomptype",
                                             None,None,None]

datetime_comp_input_labelList           =   ["datetime_column_name",
                                             "new_datetime_component_column_name",
                                             "datetime_component",
                                             "Get</br>Component",
                                             "Return","Help"]

datetime_comp_input_typeList            =   ["text","text","select","button","button","button"]

datetime_comp_input_placeholderList     =   ["datetime column name",
                                             "result column name",
                                             "result component",
                                              None,None,None]

datetime_comp_input_reqList             =   [0,1,2]
    
dtcomps           =   ["year","quarter","month","week","week of year","day","day of year","day of week","time","hour","minute","second","microsecond","nanosecond"]
tdcomps           =   ["days","seconds","microseconds","nanoseconds"]
