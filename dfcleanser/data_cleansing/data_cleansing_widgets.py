
"""
# data_cleansing_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
import dfcleanser.common.cfg  as cfg

this = sys.modules[__name__]

import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_cleansing.data_cleansing_model as dcm
import dfcleanser.data_transform.data_transform_model as dtm

from dfcleanser.common.html_widgets import (ButtonGroupForm, InputForm, DEFAULT_PAGE_WIDTH)

from dfcleanser.common.table_widgets import (dcTable,SCROLL_DOWN) 

from dfcleanser.common.common_utils import (is_int_col, get_select_defaults,
                                            display_exception, opStatus, get_parms_for_input, 
                                            is_numeric_col, RunningClock,display_generic_grid,
                                            get_help_note_html, whitecolor, yellowcolor, redcolor, greencolor)

from dfcleanser.common.display_utils import (display_df_unique_column, display_single_row, display_dfcleanser_taskbar)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing widget functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def     get_options_flag(key) :
    
    if(key == dcm.UNIQUES_FLAG) :
        if(cfg.get_config_value(cfg.UNIQUES_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.UNIQUES_FLAG_KEY))
            
    elif(key == dcm.DATA_TYPES_FLAG) :
        if(cfg.get_config_value(cfg.DATA_TYPES_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.DATA_TYPES_FLAG_KEY))
        
    else :
        return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data cleansing form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    data cleansing main task bar
#--------------------------------------------------------------------------
"""
data_cleansing_tb_doc_title             =   "Cleansing Options"
data_cleansing_tb_title                 =   "Cleansing Options"
data_cleansing_tb_id                    =   "cleanseingoptionstb"

data_cleansing_tb_keyTitleList          =   ["Cleanse</br>Numeric Column",
                                             "Cleanse</br>Non Numeric</br> Column",
                                             "Cleanse Row",
                                             "Clear","Reset","Help"]

data_cleansing_tb_jsList                =   ["cleansing_tb_callback(0)",
                                             "cleansing_tb_callback(1)",
                                             "cleansing_tb_callback(2)",
                                             "cleansing_tb_callback(3)",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_MAIN_TASKBAR_ID) + ")"]

data_cleansing_tb_centered              =   True

data_cleansing_pu_tb_keyTitleList       =   ["Cleanse</br>Numeric</br>Column",
                                             "Cleanse</br>Non</br>Numeric</br>Column",
                                             "Cleanse</br>Row",
                                             "Clear","Reset","Help"]

"""
#--------------------------------------------------------------------------
#    columns uniques change values input
#--------------------------------------------------------------------------
"""
change_values_input_title               =   "Change Data Value Parameters"
change_values_input_id                  =   "dcchangevalsinput"
change_values_input_idList              =   ["changecval","changenval",None,None,None,None]

change_values_input_labelList           =   ["Current_Value",
                                             "New_Value",
                                             "Show</br>Uniques",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

change_values_input_typeList            =   ["text","text","button","button","button","button"]

change_values_input_placeholderList     =   ["","",None,None,None,None]

change_values_input_jsList              =   [None,None,
                                             "show_uniques_callback()",
                                             "change_uvals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

change_values_input_reqList             =   [0,1]
change_values_input_short               =   True

"""
#--------------------------------------------------------------------------
#    non numeric columns uniques change values input
#--------------------------------------------------------------------------
"""
nn_change_values_input_title            =   "Change Data Value Parameters"
nn_change_values_input_id               =   "dcchangevalsinput"
nn_change_values_input_idList           =   ["changecval","changenval",None,None,None,None]

nn_change_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Show</br>Uniques",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

nn_change_values_input_typeList         =   ["text","text","button","button","button","button"]

nn_change_values_input_placeholderList  =   ["","",None,None,None,None]

nn_change_values_input_jsList           =   [None,None,
                                             "show_uniques_callback()",
                                             "change_uvals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

nn_change_values_input_reqList          =   [0,1]
nn_change_values_input_short            =   True

"""
#--------------------------------------------------------------------------
#    numeric find values input
#--------------------------------------------------------------------------
"""
find_values_input_title                 =   "Find Data Value Parameters"
find_values_input_id                    =   "dcchangevalsinput"
find_values_input_idList                =   ["findmin",
                                             "findmax",
                                             None,None]

find_values_input_labelList             =   ["min_value",
                                             "max_value",
                                             "Find</br>Values",
                                             "Help"]

find_values_input_typeList              =   ["text","text","button","button","button"]

find_values_input_placeholderList       =   ["min value","max value",None,None]

find_values_input_jsList                =   [None,None,
                                             "find_uvals_callback()",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

find_values_input_reqList               =   [0,1]
find_values_input_short                 =   True



"""
#--------------------------------------------------------------------------
#    non numeric find values input
#--------------------------------------------------------------------------
"""
nn_find_values_input_title              =   "Find Data Value Parameters"
nn_find_values_input_id                 =   "dcchangevalsinput"
nn_find_values_input_idList             =   ["findcval",
                                             None,None]

nn_find_values_input_labelList          =   ["value_in_column",
                                             "Find</br>Values",
                                             "Help"]

nn_find_values_input_typeList           =   ["text","button","button"]

nn_find_values_input_placeholderList    =   ["string to find in column",None,None]

nn_find_values_input_jsList             =   [None,
                                             "find_uvals_callback()",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

nn_find_values_input_reqList            =   [0]
nn_find_values_input_short              =   True

"""
#--------------------------------------------------------------------------
#    change row values input
#--------------------------------------------------------------------------
"""
change_row_values_input_title            =   "Change Data Value Parameters"
change_row_values_input_id               =   "changerowinput"
change_row_values_input_idList           =   ["changercval","changernval",None,None,None,None,None]

change_row_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Show</br>Uniques",
                                             "Change</br>Value",
                                             "Drop</br>Row",
                                             "Return",
                                             "Help"]

change_row_values_input_typeList         =   ["text","text","button","button","button","button","button"]

change_row_values_input_placeholderList  =   ["","",None,None,None,None,None]

change_row_values_input_jsList           =   [None,None,
                                             "show_uniques_callback()", 
                                             "change_rowvals_callback(0)",
                                             "change_rowvals_callback(1)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

change_row_values_input_reqList          =   [0,1]
change_row_values_input_short            =   True

"""
#--------------------------------------------------------------------------
#    round column input text
#--------------------------------------------------------------------------
"""
col_round_input_title                   =   ""
col_round_input_id                      =   "columnroundinput"
col_round_input_idList                  =   ["columnround",None,None,None]

col_round_input_labelList               =   ["Number_Of_Decimals",
                                             "Round</br>Column",
                                             "Return",
                                             "Help"]

col_round_input_typeList                =   ["text","button","button","button"]

col_round_input_placeholderList         =   ["",None,None,None]

col_round_input_jsList                  =   [None,
                                             "round_col_vals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

col_round_input_reqList                 =   [0]
col_round_input_short                   =   True

"""
#--------------------------------------------------------------------------
#    data transform remove whitespace input 
#--------------------------------------------------------------------------
"""
transform_remwhite_input_title          =   "Remove Whitespace Parameters"
transform_remwhite_input_id             =   "remwhitetransformInput"
transform_remwhite_input_idList         =   ["wschars",
                                             "leadtrailflag",
                                             None,None,None]

transform_remwhite_input_labelList      =   ["whitespace_chars",
                                             "remove_type_flag",
                                             "Remove</br>Whitspace",
                                             "Return","Help"]

transform_remwhite_input_typeList       =   ["selectmultiple","select","button","button","button"]

transform_remwhite_input_placeholderList =  ["whitespace chars",
                                             "remove leading and trailing",
                                             None,None,None]

transform_remwhite_input_jsList         =   [None,None,
                                             "whitespace_vals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

transform_remwhite_input_reqList        =   [0,1]


"""
#--------------------------------------------------------------------------
#    cleanse numeric cols round task bar
#--------------------------------------------------------------------------
"""
col_cleanse_round_tb_title              =   ""
col_cleanse_round_tb_title              =   ""
col_cleanse_round_tb_id                 =   "colcleansenormaloptionstb"

col_cleanse_round_tb_keyTitleList       =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value</br>Rows",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Round </br>Column</br>Values",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]

col_cleanse_round_tb_jsList             =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_DROPNA_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DISPLAY_ROUND_COLUMN_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_FILLNA_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_cleanse_round_tb_centered           =   True

col_cleanse_round_pu_tb_keyTitleList    =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value</br>Rows",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Round </br>Column</br>Values",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse numeric nonans cols round task bar
#--------------------------------------------------------------------------
"""
col_nonans_cleanse_round_tb_title              =   ""
col_nonans_cleanse_round_tb_title              =   ""
col_nonans_cleanse_round_tb_id                 =   "colnonanscleansenormaloptionstb"

col_nonans_cleanse_round_tb_keyTitleList       =   ["Drop</br>Column",
                                                    "Drop</br>Current</br>Value Rows",
                                                    "Round </br>Column</br>Values",
                                                    "Change</br>Data Type"]

col_nonans_cleanse_round_tb_jsList             =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DISPLAY_ROUND_COLUMN_OPTION) + ")",
                                                    "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_nonans_cleanse_round_tb_centered           =   True

col_nonans_cleanse_round_pu_tb_keyTitleList    =   ["Drop</br>Column",
                                                    "Drop</br>Current</br>Value</br>Rows",
                                                    "Round </br>Column</br>Values",
                                                    "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse int cols task bar
#--------------------------------------------------------------------------
"""
col_cleanse_int_tb_title                =   ""
col_cleanse_int_tb_title                =   ""
col_cleanse_int_tb_id                   =   "colcleanseroundoptionstb"

col_cleanse_int_tb_keyTitleList         =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data Type"]

col_cleanse_int_tb_jsList               =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_DROPNA_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_FILLNA_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_cleanse_int_tb_centered             =   True

col_cleanse_int_pu_tb_keyTitleList      =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value</br>Rows",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse int cols task bar
#--------------------------------------------------------------------------
"""
col_nonans_cleanse_int_tb_title                =   ""
col_nonans_cleanse_int_tb_title                =   ""
col_nonans_cleanse_int_tb_id                   =   "colnonanscleanseroundoptionstb"

col_nonans_cleanse_int_tb_keyTitleList         =   ["Drop</br>Column",
                                                    "Drop</br>Current</br>Value Rows",
                                                    "Change</br>Data Type"]

col_nonans_cleanse_int_tb_jsList               =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                                    "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_nonans_cleanse_int_tb_centered             =   True

col_nonans_cleanse_int_pu_tb_keyTitleList      =   ["Drop</br>Column",
                                                    "Drop</br>Current</br>Value</br>Rows",
                                                    "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse numeric cols change task bar
#--------------------------------------------------------------------------
"""
col_cleanse_change_tb_doc_title         =   ""
col_cleanse_change_tb_title             =   ""
col_cleanse_change_tb_id                =   "colcleansechangeoptionstb"

col_cleanse_change_tb_keyTitleList      =   ["Drop</br>Column",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Change Column</br>Values",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data Type"]

col_cleanse_change_tb_jsList            =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_DROPNA_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DISPLAY_COL_CHANGE_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_FILLNA_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_cleanse_change_tb_centered          =   True

col_cleanse_change_pu_tb_keyTitleList   =   ["Drop</br>Column",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Change</br>Column</br>Values",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]



"""
#--------------------------------------------------------------------------
#    cleanse numeric nonans cols change task bar
#--------------------------------------------------------------------------
"""
col_nonans_cleanse_change_tb_doc_title         =   ""
col_nonans_cleanse_change_tb_title             =   ""
col_nonans_cleanse_change_tb_id                =   "colcleansechangeoptionstb"

col_nonans_cleanse_change_tb_keyTitleList      =   ["Drop</br>Column",
                                                    "Change Column</br>Values",
                                                    "Change</br>Data Type"]

col_nonans_cleanse_change_tb_jsList            =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DISPLAY_COL_CHANGE_OPTION) + ")",
                                                    "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

col_nonans_cleanse_change_tb_centered          =   True

col_nonans_cleanse_change_pu_tb_keyTitleList   =   ["Drop</br>Column",
                                                    "Change</br>Column</br>Values",
                                                    "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse non_numeric cols change task bar
#--------------------------------------------------------------------------
"""
nn_col_cleanse_change_tb_doc_title      =   ""
nn_col_cleanse_change_tb_title          =   ""
nn_col_cleanse_change_tb_id             =   "colcleansechoptionstb"

nn_col_cleanse_change_tb_keyTitleList   =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value</br>Rows",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Remove</br>White</br>Space",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]

nn_col_cleanse_change_tb_jsList         =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_DROPNA_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DISPLAY_REM_WHTSPC_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dcm.DISPLAY_FILLNA_OPTION) + ")",
                                             "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

nn_col_cleanse_change_tb_centered       =   True

nn_col_cleanse_change_pu_tb_keyTitleList =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value</br>Rows",
                                             "Drop</br>Column</br>Nan</br>Rows",
                                             "Remove</br>White</br>Space",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    cleanse non_numeric nonans cols change task bar
#--------------------------------------------------------------------------
"""
nn_nonans_col_cleanse_change_tb_doc_title      =   ""
nn_nonans_col_cleanse_change_tb_title          =   ""
nn_nonans_col_cleanse_change_tb_id             =   "colnoncleansechoptionstb"

nn_nonans_col_cleanse_change_tb_keyTitleList   =   ["Drop</br> Column",
                                                    "Drop</br>Current</br>Value Rows",
                                                    "Remove</br>White</br>Space",
                                                    "Change</br>Data Type"]

nn_nonans_col_cleanse_change_tb_jsList         =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                                    "process_cols_callback(" + str(dcm.DISPLAY_REM_WHTSPC_OPTION) + ")",
                                                    "process_cols_na_callback(" + str(dtm.DISPLAY_DATATYPE_OPTION) + ")"]

nn_nonans_col_cleanse_change_tb_centered       =   True

nn_nonans_col_cleanse_change_pu_tb_keyTitleList =   ["Drop</br>Column",
                                                     "Drop</br>Current</br>Value</br>Rows",
                                                     "Remove</br>White</br>Space",
                                                     "Change</br>Data</br>Type"]


"""
#--------------------------------------------------------------------------
#    convert datatype task bar
#--------------------------------------------------------------------------
"""
conv_datatype_doc_title                 =   ""
conv_datatype_title                     =   ""
conv_datatype_id                        =   "convdatatype"

conv_datatype_keyTitleList              =   ["Convert DataType"]
conv_datatype_jsList                    =   ["process_cols_na_callback(41)"]

conv_datatype_centered                  =   True

"""
#--------------------------------------------------------------------------
#    list unique values task bar
#--------------------------------------------------------------------------
"""
list_unique_doc_title                   =   ""
list_unique_title                       =   ""
list_unique_id                          =   "listuniques"

list_unique_keyTitleList                =   ["Cleanse Column"]
list_unique_jsList                      =   ["show_details_callback()"]

list_unique_centered                    =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data type components 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   data type input (dropna) 
#--------------------------------------------------------------------------
"""
dt_data_type_dn_input_title             =   "Change Data Type Parameters"
dt_data_type_dn_input_id                =   "dtdndatatypeinput"
dt_data_type_dn_input_idList            =   ["dtnaoption",
                                             "dtanyall",
                                             "dtthreshold",
                                             "inplace",
                                             None,None,None]

dt_data_type_dn_input_labelList         =   ["na_option",
                                             "any_or_all",
                                             "threshold",
                                             "inplace",
                                             "Change</br>DataType",
                                             "Return","Help"]

dt_data_type_dn_input_typeList          =   ["select","select","text","select",
                                             "button","button","button"]

dt_data_type_dn_input_placeholderList   =   ["na option",
                                             "drop any or all",
                                             "dropna threshold - (default : None)",
                                             "dropna inplace",
                                             None,None,None]

dt_data_type_dn_input_jsList            =   [None,None,None,None,
                                             "process_cleanse_datatype_callback(" + str(dcm.DROP_NA_OPTION) + ",0,1)",
                                             "process_cleanse_datatype_callback(" + str(dcm.DROP_NA_OPTION) + ",1,1)",
                                             "display_help_url('" + str(dfchelp.PANDAS_DROPNA) + "')"]

dt_data_type_dn_input_reqList           =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   non data type input (dropna) 
#--------------------------------------------------------------------------
"""
ndt_data_type_dn_input_title            =   "Change Data Type Parameters"
ndt_data_type_dn_input_id               =   "dtdndatatypeinput"
ndt_data_type_dn_input_idList           =   ["dtanyall",
                                             "dtthreshold",
                                             None,None,None]

ndt_data_type_dn_input_labelList        =   ["any_or_all",
                                             "threshold",
                                             "Drop</br>Nans",
                                             "Return","Help"]

ndt_data_type_dn_input_typeList         =   ["select","text",
                                             "button","button","button"]

ndt_data_type_dn_input_placeholderList  =   ["drop any or all",
                                             "dropna threshold (default : None)",
                                             None,None,None]

ndt_data_type_dn_input_jsList           =   [None,None,
                                             "process_cols_dropna_fillna_transform_callback(5)",
                                             "process_cols_dropna_fillna_transform_callback(0)",
                                             "display_help_url('" + str(dfchelp.PANDAS_DROPNA) + "')"]

ndt_data_type_dn_input_reqList          =   [0,1]


"""
#--------------------------------------------------------------------------
#   numeric data type input (fillnana) 
#--------------------------------------------------------------------------
"""
dt_data_type_fn_input_title             =   "Change Data Type Parameters"
dt_data_type_fn_input_id                =   "dtfndatatypeinput"
dt_data_type_fn_input_idList            =   ["dtnaoption",
                                             "dtfillvalue",
                                             "dtfillmethod",
                                             "dtfilllimit",
                                             None,None,None]

dt_data_type_fn_input_labelList         =   ["na_option",
                                             "fillna_value",
                                             "fillna_method",
                                             "limit",
                                             "Change</br> DataType",
                                             "Return","Help"]

dt_data_type_fn_input_typeList          =   ["select","text","select","text",
                                             "button","button","button"]

dt_data_type_fn_input_placeholderList   =   ["na option",
                                             "fillna value",
                                             "fillna method",
                                             "limit (default = None)",
                                             None,None,None]

dt_data_type_fn_input_jsList            =   [None,None,None,None,
                                             "process_cleanse_datatype_callback(" + str(dcm.FILL_NA_OPTION) + ",0,1)",
                                             "process_cleanse_datatype_callback(" + str(dcm.FILL_NA_OPTION) + ",1,1)",
                                             "display_help_url('" + str(dfchelp.PANDAS_FILLNA) + "')"]

dt_data_type_fn_input_reqList           =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   numeric non data type input (fillnana) 
#--------------------------------------------------------------------------
"""
ndt_data_type_fn_input_title            =   "Change Data Type Parameters"
ndt_data_type_fn_input_id               =   "dtfndatatypeinput"
ndt_data_type_fn_input_idList           =   ["dtfillvalue",
                                             "dtfillmethod",
                                             "dtfilllimit",
                                             None,None,None]

ndt_data_type_fn_input_labelList        =   ["fillna_value",
                                             "fillna_method",
                                             "limit",
                                             "Fill</br>Nans",
                                             "Return","Help"]

ndt_data_type_fn_input_typeList         =   ["text","select","text",
                                             "button","button","button"]

ndt_data_type_fn_input_placeholderList  =   ["fillna value",
                                             "fillna method",
                                             "limit (default = None)",
                                             None,None,None]

ndt_data_type_fn_input_jsList           =   [None,None,None,
                                             "process_cols_dropna_fillna_transform_callback(9)",
                                             "process_cols_dropna_fillna_transform_callback(0)",
                                             "display_help_url('" + str(dfchelp.PANDAS_FILLNA) + "')"]

ndt_data_type_fn_input_reqList          =   [0,1]


"""
#--------------------------------------------------------------------------
#   non numeric data type fill na input 
#--------------------------------------------------------------------------
"""
dt_nn_fn_data_type_input_title           =   "Change Data Type Parameters"
dt_nn_fn_data_type_input_id              =   "dtdatatypeinput"
dt_nn_fn_data_type_input_idList          =   ["dtnnnaoption",
                                              "dtnnfillvalue",
                                              "dtnnfilllimit",
                                              None,None,None]

dt_nn_fn_data_type_input_labelList       =   ["na_option",
                                              "fillna_value",
                                              "limit",
                                              "Change</br> DataType",
                                              "Return","Help"]

dt_nn_fn_data_type_input_typeList        =   ["select","text","text",
                                             "button","button","button"]

dt_nn_fn_data_type_input_placeholderList =   ["na option",
                                              "fillna value",
                                              "limit (default = None)",
                                              None,None,None]

dt_nn_fn_data_type_input_jsList          =   [None,None,None,
                                              "process_cleanse_datatype_callback(" + str(dcm.FILL_NA_OPTION) + ",0,0)",
                                              "process_cleanse_datatype_callback(" + str(dcm.FILL_NA_OPTION) + ",1,0)",
                                              "display_help_url('" + str(dfchelp.PANDAS_FILLNA) + "')"]

dt_nn_fn_data_type_input_reqList         =   [0,1]


"""
#--------------------------------------------------------------------------
#   non numeric non data type fill na input 
#--------------------------------------------------------------------------
"""
ndt_nn_fn_data_type_input_title          =   "Change Data Type Parameters"
ndt_nn_fn_data_type_input_id             =   "dtdatatypeinput"
ndt_nn_fn_data_type_input_idList         =   ["dtnnfillvalue",
                                              "dtnnfilllimit",
                                              None,None,None]

ndt_nn_fn_data_type_input_labelList      =   ["fillna_value",
                                              "limit",
                                              "Fill</br>Nans",
                                              "Return","Help"]

ndt_nn_fn_data_type_input_typeList       =   ["text","text",
                                             "button","button","button"]

ndt_nn_fn_data_type_input_placeholderList =   ["fillna value",
                                              "limit (default = None)",
                                              None,None,None]

ndt_nn_fn_data_type_input_jsList         =   [None,None,None,
                                              "process_cols_dropna_fillna_transform_callback(9)",
                                              "process_cols_dropna_fillna_transform_callback(0)",
                                              "display_help_url('" + str(dfchelp.PANDAS_FILLNA) + "')"]

ndt_nn_fn_data_type_input_reqList        =   [0]


datacleansing_inputs        =   [change_values_input_id,nn_change_values_input_id,find_values_input_id,
                                 nn_find_values_input_id,change_row_values_input_id,col_round_input_id,
                                 transform_remwhite_input_id]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_no_data_heading() :
    display_data_cleansing_main_taskbar()
    from dfcleanser.data_inspection.data_inspection_widgets import display_df_size_data
    display_df_size_data()

def display_data_cleansing_main_taskbar() :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_dfcleanser_taskbar(ButtonGroupForm(data_cleansing_tb_id,
                                                   data_cleansing_tb_keyTitleList,
                                                   data_cleansing_tb_jsList,
                                                   data_cleansing_tb_centered))
    else :
        display_dfcleanser_taskbar(ButtonGroupForm(data_cleansing_tb_id,
                                                   data_cleansing_pu_tb_keyTitleList,
                                                   data_cleansing_tb_jsList,
                                                   data_cleansing_tb_centered))
    
    
def get_change_row_values_inputs(parms) :
    return(get_parms_for_input(parms[1],change_row_values_input_idList))

    
def get_header_widths(labels,values) :

    maxlabellength = 0
    maxvaluelength = 0
    
    for i in range(len(labels)) :
        if(len(labels[i]) > maxlabellength)  :
            maxlabellength = len(labels[i])
            
    for i in range(len(values)) :
        if(len(values[i]) > maxvaluelength)  :
            maxvaluelength = len(values[i])
            
    import math
    charwidth = int(math.ceil((DEFAULT_PAGE_WIDTH / 9 )))
    width = int(math.ceil( ((maxlabellength + maxvaluelength + 1) / charwidth) * 100) )     
    pctlabels =  int(math.ceil((maxlabellength / (maxlabellength + maxvaluelength)) * 100)) - 4       
    pctvalues =  100 - pctlabels 

    return([width,pctlabels,pctvalues])    
    

def display_col_stats(df,colname,display=True,full_size=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display column statistics
    * 
    * parms :
    *   df          -   dataframe
    *   colname     -   column name 
    *   numeric     -   numeric column flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    numeric     =   is_numeric_col(df,colname)
    
    df_col = df[colname]

    num_stats = []

    labels  =   []
    values  =   []
    
    try :
        num_stats.append(df_col.count())
        if(numeric) :
            num_stats.append(float("{0:.3f}".format(df_col.mean())))
            num_stats.append(float("{0:.3f}".format(df_col.std())))
            
            if(is_int_col(df,colname)) :
                num_stats.append(df_col.min())
                num_stats.append(df_col.max())
            else :
                num_stats.append(float("{0:.3f}".format(df_col.min())))
                num_stats.append(float("{0:.3f}".format(df_col.max())))
            
            num_stats.append(float("{0:.3f}".format(df_col.skew())))
            num_stats.append(float("{0:.3f}".format(df_col.kurtosis())))
                
    except : 
        num_stats = [0, 0, 0, 0, 0, 0, 0]

    statsHeader    =   ["",""]
    statsRows      =   []
    statsWidths    =   []
    statsAligns    =   ["left","left"]
    
    colorList = []    

    statsRows.append(["Column Name",colname])
    labels.append("Column Name")
    values.append(colname)

    colorList.append([whitecolor,whitecolor])

    found = -1
    df_cols     = df.columns.tolist()
    df_dtypes   = df.dtypes.tolist()
    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            found = i
    
    if(found != -1) :
        ftype = df_dtypes[found]
    
    statsRows.append(["Column Data Type",str(ftype)])
    labels.append("Column Data Type")
    values.append(str(ftype))
    colorList.append([whitecolor,whitecolor])

    statsRows.append(["Non Nan Count",num_stats[0]])
    labels.append("Non Nan Count")
    values.append(str(num_stats[0]))
    colorList.append([whitecolor,whitecolor])
    
    df_col    =     df[colname]
    nans      =     df[colname].isnull().sum()
    
    statsRows.append(["Total Nans",nans])
    labels.append("Total Nans")
    values.append(str(nans))
    colorList.append([whitecolor,whitecolor])
    
    if(nans > 0) :
        pct = float("{0:.3f}".format(100*(nans/len(df))))
        statsRows.append(["&nbsp;&nbsp;% of Total Col Values",str(pct)+"%"])
        labels.append("&nbsp;&nbsp;% of Total Col Values")
        values.append(str(pct)+"%")
        colorList.append([whitecolor,whitecolor])

    try :
        uniques     =   df[colname].unique()
    except :
        try :
            uniques     =   list(map(list, set(map(lambda i: tuple(i), df[colname])))) 
        except :
            uniques     =   []
    
    statsRows.append(["Column Uniques Count",len(uniques)])
    labels.append("Column Uniques Count")
    values.append(str(len(uniques)))
    colorList.append([whitecolor,whitecolor])
    
    if(numeric) :
        statsRows.append(["Mean",num_stats[1]])
        labels.append("Mean")
        values.append(str(num_stats[1]))
        
        statsRows.append(["Std",num_stats[2]])
        labels.append("Std")
        values.append(str(num_stats[2]))
        
        statsRows.append(["Min",num_stats[3]])
        labels.append("Min")
        values.append(str(num_stats[3]))
        
        statsRows.append(["Max",num_stats[4]])
        labels.append("Max")
        values.append(str(num_stats[4]))
        
        statsRows.append(["Skew",num_stats[5]])
        labels.append("Skew")
        values.append(str(num_stats[5]))

        statsRows.append(["Kurtosis",num_stats[6]])
        labels.append("Kurtosis")
        values.append(str(num_stats[6]))

    if(numeric) :
        for i in range(4) :
            colorList.append([whitecolor,whitecolor])
        
        if( (num_stats[5] < -1.0) or (num_stats[5] > 1.0) ) :
            colorList.append([whitecolor,redcolor])
        elif( (num_stats[5] < -0.5) or (num_stats[5] > 0.5) ) :
            colorList.append([whitecolor,yellowcolor])
        else : 
            colorList.append([whitecolor,greencolor])
        
        if( (num_stats[6] < -2.0) or (num_stats[6] > 2.0) ) :
            colorList.append([whitecolor,redcolor])
        elif( (num_stats[6] < -1.0) or (num_stats[6] > 1.0) ) :
            colorList.append([whitecolor,yellowcolor])
        else :
            colorList.append([whitecolor,greencolor])
    

    headerdata = get_header_widths(labels,values)
    statsWidths = [str(headerdata[1]),str(headerdata[2])]
    
    stats_table = dcTable("Column Stats","colstatsTable",cfg.DataCleansing_ID,
                          statsHeader,statsRows,statsWidths,statsAligns)

    stats_table.set_rowspertable(len(statsRows))
    stats_table.set_color(True)
    stats_table.set_colorList(colorList)
    stats_table.set_small(True)
    
    if(not (full_size)) :
        stats_table.set_smallwidth(50)
        stats_table.set_smallmargin(154)
    else :
        stats_table.set_smallwidth(99)
        stats_table.set_smallmargin(1)

    stats_table.set_border(False)
    stats_table.set_checkLength(False)
    
    if(display) :
        stats_table.display_table()
    else :
        return(stats_table.get_html())

   
def display_col_data(showUniques=False,uniquesRange=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display numeric column data
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
    #colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    display_unique_col_data(df,showUniques)


def get_cleansing_tb_js_list(jslist,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the final datacleansing task bar
    * 
    * parms :
    *   jslist      -   javascript list
    *   dfc_id      -   dfc id
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    new_js_list     =   []
    
    return(jslist)
    
    for i in range(len(jslist)) :
        if(dfc_id == cfg.DataCleansing_ID) :
            if(not(jslist[i]) is None) :
                if(jslist[i].find("39") > -1) :
                    newjs   =   jslist[i].replace("39","4")
                elif(jslist[i].find("40") > -1) :
                    newjs   =   jslist[i].replace("40","8")
                elif(jslist[i].find("41") > -1) :
                    newjs   =   jslist[i].replace("41","10")
                else :
                    newjs   =   jslist[i]
            else :
                newjs   =   jslist[i]    
                
        elif(dfc_id == cfg.DataTransform_ID) :
            newjs   =   jslist[i] 
            
        new_js_list.append(newjs)
        
    return(new_js_list)


def get_cleansing_tb_html(df,colname,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the final datacleansing task bar
    * 
    * parms :
    *   df          -   dataframe
    *   colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #print("get_cleansing_tb_html",colname,dfc_id,is_numeric_col(df,colname),is_int_col(df,colname))

    nans            =   df[colname].isnull().sum()
    
    if (is_numeric_col(df,colname) ) :
        if(is_int_col(df,colname)) :
                
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    
                if(nans > 0) :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_cleanse_int_tb_id,
                                                        col_cleanse_int_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_cleanse_int_tb_jsList,dfc_id),
                                                        col_cleanse_int_tb_centered)
                        
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":90, "left-margin":35})
                        
                else :
                    
                    print("",)
                        
                    col_uniques_tb  =   ButtonGroupForm(col_nonans_cleanse_int_tb_id,
                                                        col_nonans_cleanse_int_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_nonans_cleanse_int_tb_jsList,dfc_id),
                                                        col_nonans_cleanse_int_tb_centered)
                    
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":70})
                                        
            else :
                col_uniques_tb  =   ButtonGroupForm(col_cleanse_int_tb_id,
                                                    col_cleanse_int_pu_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(col_cleanse_int_tb_jsList,dfc_id),
                                                    col_cleanse_int_tb_centered)
                
        else :
                
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    
                if(nans > 0) :

                    col_uniques_tb  =   ButtonGroupForm(col_cleanse_round_tb_id,
                                                        col_cleanse_round_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_cleanse_round_tb_jsList,dfc_id),
                                                        col_cleanse_round_tb_centered)
                        
                    col_uniques_tb.set_customstyle({"font-size":13, "height":90, "width":78, "left-margin":1})
                        
                else :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_nonans_cleanse_round_tb_id,
                                                        col_nonans_cleanse_round_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_nonans_cleanse_round_tb_jsList,dfc_id),
                                                        col_nonans_cleanse_round_tb_centered)
                    
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":0})
                                        
            else :
                    
                if(nans > 0) :
                    
                    col_uniques_tb  =   ButtonGroupForm(col_cleanse_round_tb_id,
                                                        col_cleanse_round_pu_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_cleanse_round_tb_jsList,dfc_id),
                                                        col_cleanse_round_tb_centered)
                        
                else :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_nonans_cleanse_round_tb_id,
                                                        col_nonans_cleanse_round_pu_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_nonans_cleanse_round_tb_jsList,dfc_id),
                                                        col_nonans_cleanse_round_tb_centered)

    else :
            
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                
            if(nans > 0) :
                    
                col_uniques_tb  =   ButtonGroupForm(nn_col_cleanse_change_tb_id,
                                                    nn_col_cleanse_change_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(nn_col_cleanse_change_tb_jsList,dfc_id),
                                                    nn_col_cleanse_change_tb_centered)
                    
                col_uniques_tb.set_customstyle({"font-size":13, "height":90, "width":78, "left-margin":0})

            else :
                    
                col_uniques_tb  =   ButtonGroupForm(nn_nonans_col_cleanse_change_tb_id,
                                                    nn_nonans_col_cleanse_change_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(nn_nonans_col_cleanse_change_tb_jsList,dfc_id),
                                                    nn_nonans_col_cleanse_change_tb_centered)
                
                col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":15})
                
        else :
                
            if(nans > 0) :
                    
                col_uniques_tb  =   ButtonGroupForm(nn_col_cleanse_change_tb_id,
                                                    nn_col_cleanse_change_pu_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(nn_col_cleanse_change_tb_jsList,dfc_id),
                                                    nn_col_cleanse_change_tb_centered)
                    
            else :
                    
                col_uniques_tb  =   ButtonGroupForm(nn_nonans_col_cleanse_change_tb_id,
                                                    nn_nonans_col_cleanse_change_pu_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(nn_nonans_col_cleanse_change_tb_jsList,dfc_id),
                                                    nn_nonans_col_cleanse_change_tb_centered)
 
               
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        col_uniques_tb.set_gridwidth(480)

    else :
        col_uniques_tb.set_gridwidth(480)
        col_uniques_tb.set_custombwidth(75)

    cleansing_text_tb_html          =   col_uniques_tb.get_html()
    cleansing_text_tb_html          =   "<br>" + cleansing_text_tb_html
               
    return(cleansing_text_tb_html)           
                

def get_unique_col_html(df,colname,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : display unique vals for a column
    * 
    * parms :
    *   df          -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    sethrefs    =   True

    if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

        findparms = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if(is_numeric_col(df,colname)) :

            if( (len(findparms[0]) < 1) and (len(findparms[1]) < 1)) :
            
                opstat.set_status(False)
                opstat.set_errorMsg("Find values input values are invalid")
                
        else :
            
            if(len(findparms[0]) < 1) :
            
                opstat.set_status(False)
                opstat.set_errorMsg("Find values input values are invalid")
            
    try :
        counts      =   df[colname].value_counts().to_dict()
        uniques     =   list(counts.keys())
    
    except :
        
        try :
            uniques     =   list(map(list, set(map(lambda i: tuple(i), df[colname]))))
            counts      =   {}
        
            uniques_length  =  len(df[colname])
            if(uniques_length > 250) :
                uniques_length = 250
                
            import json
            for i in range(uniques_length) :
                ukey    =   json.dumps(df[colname][i])
                uniques_count   =   counts.get(ukey,0)
                counts.update({ukey : uniques_count + 1})
        except :
            counts      =   0
            
    try :
        
        col_uniques_table = dcTable("Unique Values and Counts",
                                    "uvalsTbl",
                                    cfg.DataCleansing_ID)
        
        if(not (is_numeric_col(df,colname)) ) :

            unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,counts,False)
            find_values_inputs  =   InputForm(nn_find_values_input_id,
                                              nn_find_values_input_idList,
                                              nn_find_values_input_labelList,
                                              nn_find_values_input_typeList,
                                              nn_find_values_input_placeholderList,
                                              nn_find_values_input_jsList,
                                              nn_find_values_input_reqList)
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":40})
            find_values_inputs.set_gridwidth(280)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
            help_note       =   "Enter a value_in_column to locate a values containing the value_in_column."
            
        else :

            
            unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,counts,False)
            find_values_inputs  =   InputForm(find_values_input_id,
                                              find_values_input_idList,
                                              find_values_input_labelList,
                                              find_values_input_typeList,
                                              find_values_input_placeholderList,
                                              find_values_input_jsList,
                                              find_values_input_reqList)
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":40})
            find_values_inputs.set_gridwidth(280)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
            help_note       =   "Enter a min_value and max_value to get a subset of unique values."
            
    except Exception as e:
        
        opstat.store_exception("Unable to display column uniques",e)
        display_exception(opstat)
        
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :    
        uniques_find_heading_html       =   "<div>Find Uniques</div>"
        uniques_find_html               =   find_values_html
    else :
        uniques_find_html               =   find_values_html
        
    if(opstat.get_status()) :
        find_notes_html =   get_help_note_html(help_note)
    else :
        help_note       =   "Invalid min_value or max_value entered."
        find_notes_html =   get_help_note_html(help_note)

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-right","dfc-footer"]
        gridhtmls       =   [unique_cols_html,uniques_find_heading_html,uniques_find_html,find_notes_html]
        
        display_generic_grid("display-df-cleanser-unique-columns-wrapper",gridclasses,gridhtmls)
    else :
        
        gridclasses     =   ["dfc-top","dfc-main","dfc-footer"]
        gridhtmls       =   [unique_cols_html,uniques_find_html,find_notes_html]
        
        display_generic_grid("display-df-cleanser-unique-columns-pop-up-wrapper",gridclasses,gridhtmls)
        
    cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)


    print("\n")
 
    
def display_unique_col_data(df,showUniques=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display unique vals for a column
    * 
    * parms :
    *   df          -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    colname = cfg.get_config_value(cfg.CLEANSING_COL_KEY)

    opstat                  =   opStatus()
    
    clock = RunningClock()
    clock.start()

    
    """
    * -------------------------------------------------------------------------- 
    * ------------------------ get the uniques table --------------------------- 
    * -------------------------------------------------------------------------- 
    """
    if(showUniques) :
        get_unique_col_html(df,colname,opstat)


    """
    * -------------------------------------------------------------------------- 
    * ---------------------- get the input form html --------------------------- 
    * -------------------------------------------------------------------------- 
    """
    
    if(is_numeric_col(df,colname)) :
            
        cleansing_text_inputs   =   InputForm(change_values_input_id,
                                              change_values_input_idList,
                                              change_values_input_labelList,
                                              change_values_input_typeList,
                                              change_values_input_placeholderList,
                                              change_values_input_jsList,
                                              change_values_input_reqList) 

    else :
            
        cleansing_text_inputs   =   InputForm(nn_change_values_input_id,
                                              nn_change_values_input_idList,
                                              nn_change_values_input_labelList,
                                              nn_change_values_input_typeList,
                                              nn_change_values_input_placeholderList,
                                              nn_change_values_input_jsList,
                                              nn_change_values_input_reqList)
            
    """
    * -------------------------------------------------------------------------- 
    * -------------------- displpay the cleansing grid ------------------------- 
    * -------------------------------------------------------------------------- 
    """
    unique_column_heading_html      =   "<div>" + colname + " Cleansing Parms</div><br>"
    
    cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":50})
    cleansing_text_inputs.set_gridwidth(480)
    cleansing_text_inputs.set_shortForm(True)
    cleansing_text_input_html       =   cleansing_text_inputs.get_html()    
        
    cleansing_text_tb_html          =   get_cleansing_tb_html(df,colname,cfg.DataCleansing_ID)

    col_stats_html  =   display_col_stats(df,colname,display=False,full_size=True)
    

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :

        gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
        gridhtmls       =   [col_stats_html,unique_column_heading_html,cleansing_text_input_html,cleansing_text_tb_html]
        display_generic_grid("display-df-cleanser-input-wrapper",gridclasses,gridhtmls)
    else :

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
        gridhtmls       =   [unique_column_heading_html,cleansing_text_input_html,cleansing_text_tb_html]
        display_generic_grid("display-df-cleanser-input-pop-up-wrapper",gridclasses,gridhtmls)
    
    clock.stop()

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_row_data(df,rowid,colid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display row data
    * 
    * parms :
    *   df          -   dataframe
    *   rowid       -   row id 
    *   colid       -   column id 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    rows_table = dcTable("Sample Row","dcdisrow",cfg.DataCleansing_ID)
    
    refList = []
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        for i in range(3) :
            refList.append([None,None,None,None,None,None,None,None,None,None])
            refList.append(["frval","frval","frval","frval","frval",
                            "frval","frval","frval","frval","frval"])
            
    else :
        
        for i in range(6) :
            refList.append([None,None,None,None,None])
            refList.append(["frval","frval","frval","frval","frval"])
        
    rows_table.set_refList(refList)
    
    opstat = opStatus()
    
    df_row_cleanser_table_html    =   display_single_row(df,rows_table,rowid,colid,opstat,False)
    
    if(not opstat.get_status()) :
        display_exception(opstat)

    else :
        
        print("\n")
        
        df_row_cleanser_heading_html    =   "<div>dataframe Row Cleanser : Row " + str(rowid) + "</div>"
        
        df_row_input_form               =   InputForm(change_row_values_input_id,
                                                      change_row_values_input_idList,
                                                      change_row_values_input_labelList,
                                                      change_row_values_input_typeList,
                                                      change_row_values_input_placeholderList,
                                                      change_row_values_input_jsList,
                                                      change_row_values_input_reqList)
        
        df_row_input_form.set_shortForm(True)
        df_row_input_form.set_gridwidth(400)
        df_row_input_form.set_custombwidth(75)
        
        df_row_cleanser_input_html      =   df_row_input_form.get_html()
        
        gridclasses     =   ["dfcleanser-common-grid-header", 
                             "dfc-top",
                             "dfc-footer"]

        gridhtmls       =   [df_row_cleanser_heading_html,
                             df_row_cleanser_table_html,
                             df_row_cleanser_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-df-row-cleanser-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("display-df-row-cleanser-pop-up-wrapper",gridclasses,gridhtmls)


"""            
#------------------------------------------------------------------
#               Whitespace chars table objects
#------------------------------------------------------------------
"""


white_space_cb_html = """
                <div class="form-check dc-whitespace-cb-div" style="font-size:12px; font-family:Arial; background-color:#F8F5E1;" >
                    <input type='checkbox' id="XXXXcbId" value="XXXXcbvalue" checked >XXXXcbtext</input>
                </div>
"""


def get_whitespace_chars_cb(cbid,val,text) : 
    
    ws_html     =   white_space_cb_html[0:]
    ws_html     =   ws_html.replace("XXXXcbId",cbid+"cbId")
    ws_html     =   ws_html.replace("XXXXcbvalue",str(val))
    ws_html     =   ws_html.replace("XXXXcbtext",str(text))
    
    return(ws_html)


def display_option(df,colname,input_html,heading_html) :
    
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    print("\n")

    gridclasses     =   ["dfc-middle","dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [col_stats_html,heading_html,input_html]
        
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("col-change-datatype-fn-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("col-change-datatype-fn-pop-up-wrapper",gridclasses,gridhtmls)
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

    
def display_dropna_option(df,colname) :
    
    common_column_heading_html      =   "<div>Drop Na Parameters</div><br>"
        
    #from dfcleanser.data_transform.data_transform_columns_widgets import get_dropna_display
    cleansing_text_input_html   =   get_dropna_display(False,cfg.DataCleansing_ID)+"<br>"

    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def display_fillna_option(df,colname) :
    
    common_column_heading_html      =   "<div>Fill Na Parameters</div><br>"
        
    #from dfcleanser.data_transform.data_transform_columns_widgets import get_fillna_display
    cleansing_text_input_html   =   get_fillna_display(df,colname,False,cfg.DataCleansing_ID)+"<br>"

    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def display_round_option(df,colname) :
    
    cleansing_text_inputs   =   InputForm(col_round_input_id,
                                          col_round_input_idList,
                                          col_round_input_labelList,
                                          col_round_input_typeList,
                                          col_round_input_placeholderList,
                                          col_round_input_jsList,
                                          col_round_input_reqList)
    
    cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":30})
    cleansing_text_inputs.set_gridwidth(360)
    cleansing_text_inputs.set_shortForm(True)
    cleansing_text_input_html       =   cleansing_text_inputs.get_html()+"<br>"    
    
    common_column_heading_html      =   "<div>Round Column Parameters</div><br>"
        
    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def display_whitespace_option(df,colname) :
    
    remws_uniques_table = dcTable("Unique Values for "+colname,
                                  "remwsuniquesTable",
                                  cfg.DataCleansing_ID)

    from dfcleanser.common.display_utils import  display_df_unique_column     
    uniques_html    =   display_df_unique_column(df,remws_uniques_table,colname,False,None,False)
    
    cleansing_text_inputs   =   InputForm(transform_remwhite_input_id,
                                          transform_remwhite_input_idList,
                                          transform_remwhite_input_labelList,
                                          transform_remwhite_input_typeList,
                                          transform_remwhite_input_placeholderList,
                                          transform_remwhite_input_jsList,
                                          transform_remwhite_input_reqList)
        
    selectDicts         =   []
    
    wschars             =   {"default":"All","list":["All","Horizontal Tab","Linefeed","Formfeed","Cariage Return","Backspace","Vertical Tab"]}
    selectDicts.append(wschars)

    typesflag           =   {"default":"All","list":["Leading and Trailing","Leading Only","Trailing Only","All"]}
    selectDicts.append(typesflag)

    get_select_defaults(cleansing_text_inputs,
                        transform_remwhite_input_id,
                        transform_remwhite_input_idList,
                        transform_remwhite_input_typeList,
                        selectDicts)
        
    cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":80, "left-margin":5})
    cleansing_text_inputs.set_gridwidth(280)
    cleansing_text_inputs.set_shortForm(True)
    
    cleansing_text_input_html   =   cleansing_text_inputs.get_html()+"<br>"
    
    common_column_heading_html      =   "<br><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove Whitespace Parameters</div>"
        
    print("\n")

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :

        gridclasses     =   ["dfc-left","dfc-right","dfc-footer"]
        gridhtmls       =   [uniques_html,common_column_heading_html,cleansing_text_input_html]
        display_generic_grid("display-df-cleanser-unique-columns-wrapper",gridclasses,gridhtmls)

    else :
        
        gridclasses     =   ["dfc-top","dfc-main","dfc-footer"]
        gridhtmls       =   [uniques_html,common_column_heading_html,cleansing_text_input_html]
        display_generic_grid("display-df-cleanser-unique-columns-pop-up-wrapper",gridclasses,gridhtmls)    
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display datatype, fillna and dropna methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 

def get_dt_js_list(jslist,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the final datacleansing task bar
    * 
    * parms :
    *   jslist      -   javascript list
    *   dfc_id      -   dfc id
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    new_js_list     =   []
    
    for i in range(len(jslist)) :
        if(dfc_id == cfg.DataCleansing_ID) :
            if(not (jslist[i] is None)) :
                if(jslist[i].find("DataTransform") > -1) :
                    newjs   =   jslist[i].replace("DataTransform","DataCleansing")
                else :
                    newjs   =   jslist[i]
            else :
                newjs   =   jslist[i]    
                
        elif(dfc_id == cfg.DataTransform_ID) :
            newjs   =   jslist[i] 
            
        new_js_list.append(newjs)
        
    return(new_js_list)


def get_dropna_display(withdt,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the dropna html
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(withdt) :
        
        grid_input_form     =   InputForm(dt_data_type_dn_input_id,
                                          dt_data_type_dn_input_idList,
                                          dt_data_type_dn_input_labelList,
                                          dt_data_type_dn_input_typeList,
                                          dt_data_type_dn_input_placeholderList,
                                          dt_data_type_dn_input_jsList,
                                          dt_data_type_dn_input_reqList)
        
    else :
        
        grid_input_form     =   InputForm(ndt_data_type_dn_input_id,
                                          ndt_data_type_dn_input_idList,
                                          ndt_data_type_dn_input_labelList,
                                          ndt_data_type_dn_input_typeList,
                                          ndt_data_type_dn_input_placeholderList,
                                          ndt_data_type_dn_input_jsList,
                                          ndt_data_type_dn_input_reqList)

    selectDicts     =   []
    
    if(withdt) : 
        if(dfc_id == cfg.DataTransform_ID) :
            naoption         =   {"default" : "dropna", "list" : ["dropna","fillna"],"callback":"dtselect_dropna_change"}
        else :
            naoption         =   {"default" : "dropna", "list" : ["dropna","fillna"],"callback":"dtcselect_dropna_change"}
        
        selectDicts.append(naoption)
    
    anyall  =   {"default" : "any", "list" : ["any","all"]}
    selectDicts.append(anyall)            
    
    if(withdt) :        
 
        get_select_defaults(grid_input_form,
                            dt_data_type_dn_input_id,
                            dt_data_type_dn_input_idList,
                            dt_data_type_dn_input_typeList,
                            selectDicts)
    
    else :
        
        get_select_defaults(grid_input_form,
                            ndt_data_type_dn_input_id,
                            ndt_data_type_dn_input_idList,
                            ndt_data_type_dn_input_typeList,
                            selectDicts)
    
    #grid_input_form.set_custombwidth(80)
    grid_input_form.set_gridwidth(400)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":5})
    grid_input_form.set_shortForm(True)
    
    return(grid_input_form.get_html())

    
def get_fillna_display(df,colname,withdt,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the fillna html
    * 
    * parms :
    *   df      -   dataframe
    *   colname -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(is_numeric_col(df,colname)) :
        
        if(withdt) :

            grid_input_form     =   InputForm(dt_data_type_fn_input_id,
                                              dt_data_type_fn_input_idList,
                                              dt_data_type_fn_input_labelList,
                                              dt_data_type_fn_input_typeList,
                                              dt_data_type_fn_input_placeholderList,
                                              get_dt_js_list(dt_data_type_fn_input_jsList,dfc_id),
                                              dt_data_type_fn_input_reqList)
            
        else :
            
            grid_input_form     =   InputForm(ndt_data_type_fn_input_id,
                                              ndt_data_type_fn_input_idList,
                                              ndt_data_type_fn_input_labelList,
                                              ndt_data_type_fn_input_typeList,
                                              ndt_data_type_fn_input_placeholderList,
                                              ndt_data_type_fn_input_jsList,
                                              ndt_data_type_fn_input_reqList)
                
    else :
        
        if(withdt) :
            
            grid_input_form     =   InputForm(dt_nn_fn_data_type_input_id,
                                              dt_nn_fn_data_type_input_idList,
                                              dt_nn_fn_data_type_input_labelList,
                                              dt_nn_fn_data_type_input_typeList,
                                              dt_nn_fn_data_type_input_placeholderList,
                                              get_dt_js_list(dt_nn_fn_data_type_input_jsList,dfc_id),
                                              dt_nn_fn_data_type_input_reqList)
            
        else :
            
            grid_input_form     =   InputForm(ndt_nn_fn_data_type_input_id,
                                              ndt_nn_fn_data_type_input_idList,
                                              ndt_nn_fn_data_type_input_labelList,
                                              ndt_nn_fn_data_type_input_typeList,
                                              ndt_nn_fn_data_type_input_placeholderList,
                                              ndt_nn_fn_data_type_input_jsList,
                                              ndt_nn_fn_data_type_input_reqList)
    
    selectDicts     =   []
    
    if(withdt) : 
        if(dfc_id == cfg.DataTransform_ID) :
            naoption         =   {"default" : "fillna", "list" : ["dropna","fillna"],"callback":"dtselect_dropna_change"}
        else :
            naoption         =   {"default" : "fillna", "list" : ["dropna","fillna"],"callback":"dtcselect_dropna_change"}
        
        selectDicts.append(naoption)
    
    if(is_numeric_col(df,colname)) :
        fillnas         =   {"default" : "None - use fillna_value", "list" : ["None - use fillna_value","mean","bfill","ffill"]}
        selectDicts.append(fillnas)
    
    if(is_numeric_col(df,colname)) :
        
        if(withdt) :
        
            get_select_defaults(grid_input_form,
                                dt_data_type_fn_input_id,
                                dt_data_type_fn_input_idList,
                                dt_data_type_fn_input_typeList,
                                selectDicts)
            
        else :
            
            get_select_defaults(grid_input_form,
                                ndt_data_type_fn_input_id,
                                ndt_data_type_fn_input_idList,
                                ndt_data_type_fn_input_typeList,
                                selectDicts)
            
    
    else :
    
        if(withdt) :
            
            get_select_defaults(grid_input_form,
                                dt_nn_fn_data_type_input_id,
                                dt_nn_fn_data_type_input_idList,
                                dt_nn_fn_data_type_input_typeList,
                                selectDicts)
            
        else :
            
            get_select_defaults(grid_input_form,
                                ndt_nn_fn_data_type_input_id,
                                ndt_nn_fn_data_type_input_idList,
                                ndt_nn_fn_data_type_input_typeList,
                                selectDicts)
    
    grid_input_form.set_gridwidth(400)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":5})
    
    return(grid_input_form.get_html())


def display_dropna(df,colname,withdt,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : display dropna form
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    print("display_dropna",colname,withdt,dfc_id)
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_column_uniques
    uniques_html    =   display_column_uniques(df,colname,False)        

    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    dropna_html     =   get_dropna_display(withdt)
    
    heading_html    =   "<div>Drop na Parameters</div><br>"

    gridclasses     =   ["dfc-top","dfc-middle","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [uniques_html,col_stats_html,heading_html,dropna_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("col-change-datatype-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("col-change-datatype-pop-up-wrapper",gridclasses,gridhtmls)
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_fillna(df,colname,withdt,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : display dropna form
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    print("display_fillna",colname,withdt,dfc_id)
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_column_uniques
    uniques_html    =   display_column_uniques(df,colname,False)        

    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    fillna_html     =   get_fillna_display(df,colname,withdt)
    
    heading_html    =   "<div>Fill na Parameters</div><br>"

    gridclasses     =   ["dfc-top","dfc-middle","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [uniques_html,col_stats_html,heading_html,fillna_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("col-change-datatype-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("col-change-datatype-pop-up-wrapper",gridclasses,gridhtmls)
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
















