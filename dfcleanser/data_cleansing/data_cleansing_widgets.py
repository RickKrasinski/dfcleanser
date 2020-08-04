
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
import pandas as pd

this = sys.modules[__name__]

import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_cleansing.data_cleansing_model as dcm
import dfcleanser.data_transform.data_transform_model as dtm

from dfcleanser.common.html_widgets import (ButtonGroupForm, InputForm, DEFAULT_PAGE_WIDTH)

from dfcleanser.common.table_widgets import (dcTable) 

from dfcleanser.common.common_utils import (is_int_col, get_select_defaults,is_categorical_col,
                                            display_exception, opStatus, get_parms_for_input, 
                                            is_numeric_col, RunningClock,display_generic_grid,
                                            get_help_note_html, whitecolor, yellowcolor, redcolor, greencolor)

from dfcleanser.common.display_utils import (display_df_unique_column, get_single_row, display_dfcleanser_taskbar,
                                             display_df_describe, display_df_nn_describe) 

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

data_cleansing_tb_jsList                =   ["cleansing_tb_callback(" + str(dcm.DISPLAY_CLEANSE_NUMERIC_COLUMNS) + ")",
                                             "cleansing_tb_callback(" + str(dcm.DISPLAY_CLEANSE_NON_NUMERIC_COLUMNS) + ")",
                                             "cleansing_tb_callback(" + str(dcm.DISPLAY_SELECT_ROW_ID) + ")",
                                             "cleansing_tb_callback(" + str(dcm.DISPLAY_CLEANSE_CLEAR) + ")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_MAIN_TASKBAR_ID) + "')"]

data_cleansing_tb_centered              =   True

data_cleansing_pu_tb_keyTitleList       =   ["Cleanse</br>Numeric</br>Column",
                                             "Cleanse</br>Non</br>Numeric</br>Column",
                                             "Cleanse</br>Row",
                                             "Clear","Reset","Help"]





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    columns change values forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    numeric columns change values input
#--------------------------------------------------------------------------
"""
change_values_input_title               =   "Change Data Value"
change_values_input_id                  =   "dcchangevalsinput"
change_values_input_idList              =   ["changecval","changenval",None,None,None,None]

change_values_input_labelList           =   ["current_value",
                                             "new_value",
                                             "Show</br>Uniques",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

change_values_input_typeList            =   ["text","text","button","button","button","button"]

change_values_input_placeholderList     =   ["","",None,None,None,None]

change_values_input_jsList              =   [None,None,
                                             "show_uniques_callback()",
                                             "change_uvals_callback(0)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_CHANGE_ID) + "')"]

change_values_input_reqList             =   [0,1]
change_values_input_short               =   True

"""
#--------------------------------------------------------------------------
#    non numeric columns change values input
#--------------------------------------------------------------------------
"""
nn_change_values_input_title            =   "Change Data Value"
nn_change_values_input_id               =   "dcnnchangevalsinput"
nn_change_values_input_idList           =   ["changecval","changenval",None,None,None,None]

nn_change_values_input_labelList        =   ["current_value",
                                             "new_value",
                                             "Show</br>Uniques",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

nn_change_values_input_typeList         =   ["text","text","button","button","button","button"]

nn_change_values_input_placeholderList  =   ["","",None,None,None,None]

nn_change_values_input_jsList           =   [None,None,
                                             "show_uniques_callback()",
                                             "change_uvals_callback(1)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_NO_NANS_CHANGE_ID) + "')"]

nn_change_values_input_reqList          =   [0,1]
nn_change_values_input_short            =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    columns find unique values forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    numeric find unique values input
#--------------------------------------------------------------------------
"""
find_values_input_title                 =   "Find Data Value"
find_values_input_id                    =   "dcfindvalsinput"
find_values_input_idList                =   ["findmin",
                                             "findmax",
                                             None,None]

find_values_input_labelList             =   ["min_value",
                                             "max_value",
                                             "Find</br>Values",
                                             "Help"]

find_values_input_typeList              =   ["text","text","button","button","button"]

find_values_input_placeholderList       =   ["(default : min column value)",
                                             "(default : max column value)",None,None]

find_values_input_jsList                =   [None,None,
                                             "find_uvals_callback()",
                                             "displayhelp('" + str(dfchelp.CLEANSE_UNIQUE_VALS_ID) + "')"]

find_values_input_reqList               =   [0,1]
find_values_input_short                 =   True


"""
#--------------------------------------------------------------------------
#    non numeric find unique values input
#--------------------------------------------------------------------------
"""
nn_find_values_input_title              =   "Find Data Value"
nn_find_values_input_id                 =   "dcnnfindvalsinput"
nn_find_values_input_idList             =   ["findcval",
                                             None,None]

nn_find_values_input_labelList          =   ["value_in_column",
                                             "Find</br>Values",
                                             "Help"]

nn_find_values_input_typeList           =   ["text","button","button"]

nn_find_values_input_placeholderList    =   ["string to find in column",None,None]

nn_find_values_input_jsList             =   [None,
                                             "find_nn_uvals_callback()",
                                             "displayhelp('" + str(dfchelp.CLEANSE_UNIQUE_VALS_ID) + "')"]

nn_find_values_input_reqList            =   [0]
nn_find_values_input_short              =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    df row cleanser input
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
change_row_values_input_title            =   "Change Data Value"
change_row_values_input_id               =   "changerowinput"
change_row_values_input_idList           =   ["changercval",
                                              "changernval"
                                              ,None,None,None,None,None]

change_row_values_input_labelList        =   ["current_value",
                                             "new_value",
                                             "Change</br>Row</br>Values",
                                             "Get</br>New</br>Row",
                                             "Drop</br>Current</br>Row",
                                             "Return",
                                             "Help"]

change_row_values_input_typeList         =   ["text","text","button","button","button","button","button"]

change_row_values_input_placeholderList  =   ["","",None,None,None,None,None]

change_row_values_input_jsList           =   [None,None,
                                             "change_rowvals_callback(" + str(dcm.CHANGE_ROW_VALUES) + ")",
                                             "cleansing_tb_callback(" + str(dcm.DISPLAY_SELECT_ROW_ID) + ")",
                                             "change_rowvals_callback(" + str(dcm.DROP_ROW) + ")",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_ROW_ID) + "')"]

change_row_values_input_reqList          =   [0,1]
change_row_values_input_short            =   True



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    column operations input forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    round column input text
#--------------------------------------------------------------------------
"""
col_round_input_title                   =   "Column Round"
col_round_input_id                      =   "columnroundinput"
col_round_input_idList                  =   ["columnround",None,None,None]

col_round_input_labelList               =   ["number_of_decimals",
                                             "Round</br>Column",
                                             "Return",
                                             "Help"]

col_round_input_typeList                =   ["text","button","button","button"]

col_round_input_placeholderList         =   ["",None,None,None]

col_round_input_jsList                  =   [None,
                                             "round_col_vals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_ROUND_COLUMN_ID) + "')"]

col_round_input_reqList                 =   [0]
col_round_input_short                   =   True


"""
#--------------------------------------------------------------------------
#    data transform remove whitespace input 
#--------------------------------------------------------------------------
"""
transform_remwhite_input_title          =   "Remove Whitespace"
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
                                             "displayhelp('" + str(dfchelp.CLEANSE_REMOVE_WHITESPACE_ID) + "')"]

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
                                             "process_cols_na_callback(" + str(dcm.PROCESS_DROPNA_ROWS_OPTION) + ")",
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
                                             "process_cols_na_callback(" + str(dcm.PROCESS_DROPNA_ROWS_OPTION) + ")",
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
                                             "process_cols_na_callback(" + str(dcm.PROCESS_DROPNA_ROWS_OPTION) + ")",
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
#    cleanse category cols change task bar
#--------------------------------------------------------------------------
"""
cat_cleanse_change_tb_doc_title         =   ""
cat_cleanse_change_tb_title             =   ""
cat_cleanse_change_tb_id                =   "catcleansechangeoptionstb"

cat_cleanse_change_tb_keyTitleList      =   ["Drop</br>Column",
                                             "Add</br>New</br>Category(s)",
                                             "Remove</br>Category(s)",
                                             "Remove</br>Unused</br>Category(s)"]

cat_cleanse_change_tb_jsList            =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback("+ str(dcm.DISPLAY_ADD_CATEGORY) + ")",
                                             "process_cols_callback(" + str(dcm.DISPLAY_REMOVE_CATEGORY) + ")",
                                             "process_cols_callback(" + str(dcm.PROCESS_REMOVE_UNUSED_CATEGORY) + ")"]

cat_cleanse_change_tb_centered          =   True

cata_cleanse_change_tb_doc_title        =   ""
cata_cleanse_change_tb_title            =   ""
cata_cleanse_change_tb_id               =   "catacleansechangeoptionstb"

cata_cleanse_change_tb_keyTitleList     =   ["Remove</br>White</br>Space in</br>Category(s)",
                                             "Reorder</br>Categories",
                                             "Toggle</br>Category</br>Order"]

cata_cleanse_change_tb_jsList           =   ["process_cols_callback(" + str(dcm.DISPLAY_REMOVE_CATEGORY_WHITESPACE) + ")",
                                             "process_cols_callback(" + str(dcm.DISPLAY_REORDER_CATEGORY) + ")",
                                             "process_cols_callback(" + str(dcm.PROCESS_TOGGLE_CATEGORY_ORDER) + ")"]

cata_cleanse_change_tb_centered         =   True


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
                                             "process_cols_na_callback(" + str(dcm.PROCESS_DROPNA_ROWS_OPTION) + ")",
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
#--------------------------------------------------------------------------
#   na components 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   numeric fillna form
#--------------------------------------------------------------------------
"""
col_fillna_input_title                  =   "Change Data Type"
col_fillna_input_id                     =   "fillnainput"
col_fillna_input_idList                 =   ["naoption",
                                             "fillvalue",
                                             "fillmethod",
                                             "filllimit",
                                             None,None,None]

col_fillna_input_labelList              =   ["na_option",
                                             "fillna_value",
                                             "fillna_method",
                                             "limit",
                                             "Fill</br>Nans",
                                             "Return","Help"]

col_fillna_input_typeList               =   ["select","text","select","text",
                                             "button","button","button"]

col_fillna_input_placeholderList        =   ["na option",
                                             "fillna value",
                                             "fillna method",
                                             "limit (default = None)",
                                             None,None,None]

col_fillna_input_jsList                 =   [None,None,None,None,
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.PROCESS_FILLNA_OPTION) + ")",
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.MAIN_OPTION) + ")",
                                             "displayhelp('" + str(dfchelp.CLEANSE_FILLNA_COLUMN_ID) + "')"]

col_fillna_input_reqList                =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   non numeric fillna form
#--------------------------------------------------------------------------
"""
nn_col_fillna_input_title               =   "Fill Na"
nn_col_fillna_input_id                  =   "nnfillna"
nn_col_fillna_input_idList              =   ["naoption",
                                             "dropanyall",
                                              "dropthresh",
                                              None,None,None]

nn_col_fillna_input_labelList           =   ["na_option",
                                             "dropna_any_or_all",
                                             "dropna_threshold",
                                              "Drop</br>Nans",
                                              "Return","Help"]

nn_col_fillna_input_typeList            =   ["select","text","text",
                                             "button","button","button"]

nn_col_fillna_input_placeholderList     =   ["na option",
                                             "dropna type",
                                              "threshold (default = None)",
                                              None,None,None]

nn_col_fillna_input_jsList              =   [None,None,None,
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.PROCESS_DROPNA_OPTION) + ")",
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.MAIN_OPTION) + ")",
                                              "displayhelp('" + str(dfchelp.CLEANSE_FILLNA_COLUMN_ID) + "')"]

nn_col_fillna_input_reqList             =   [0]


"""
#--------------------------------------------------------------------------
#   numeric fillna form
#--------------------------------------------------------------------------
"""
col_dropna_input_title                  =   "Drop Na"
col_dropna_input_id                     =   "dropnainput"
col_dropna_input_idList                 =   ["naoption",
                                             "dropnaanyall",
                                             "dropnathreshold",
                                             None,None,None]

col_dropna_input_labelList              =   ["na_option",
                                             "dropna_any_or_all",
                                             "dropna_threshold",
                                             "Drop</br>Nans",
                                             "Return","Help"]

col_dropna_input_typeList               =   ["select","select","text",
                                             "button","button","button"]

col_dropna_input_placeholderList        =   ["na option",
                                             "dropna type",
                                             "dropna threshold (default = None)",
                                             None,None,None]

col_dropna_input_jsList                 =   [None,None,None,
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.PROCESS_DROPNA_OPTION) + ")",
                                              "process_cols_dropna_fillna_transform_callback(" + str(dcm.MAIN_OPTION) + ")",
                                             "displayhelp('" + str(dfchelp.CLEANSE_DROPNA_COLUMN_ID) + "')"]

col_dropna_input_reqList                =   [0,1,2]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    compatability check forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#    columns check alphanuimeric compatability
#--------------------------------------------------------------------------
"""
nn_alpha_compat_input_title             =   "Check for Non Numeric Compat"
nn_alpha_compat_input_id                =   "nnchkcompat"
nn_alpha_compat_input_idList            =   ["chksamplesize",None,None,None]

nn_alpha_compat_input_labelList         =   ["sample_size",
                                             "Check</br>Alphanumeric</br>Compatability",
                                             "Return",
                                             "Help"]

nn_alpha_compat_input_typeList          =   ["text","button","button","button"]

nn_alpha_compat_input_placeholderList   =   ["check sample size (default : 100%",None,None,None]

nn_alpha_compat_input_jsList            =   [None,
                                             "process_nn_check_compatability(0)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_CHECK_ALPHA_ID) + "')"]

nn_alpha_compat_input_reqList           =   [0]
nn_alpha_compat_input_short             =   True


"""
#--------------------------------------------------------------------------
#    columns check nuimeric compatability
#--------------------------------------------------------------------------
"""
nn_numeric_compat_input_title            =   "Check for Non Numeric Compat"
nn_numeric_compat_input_id               =   "nnchkcompat"
nn_numeric_compat_input_idList           =   ["chksamplesize",None,None,None]

nn_numeric_compat_input_labelList        =   ["sample_size",
                                             "Check</br>Numeric</br>Compatability",
                                             "Return",
                                             "Help"]

nn_numeric_compat_input_typeList         =   ["text","button","button","button"]

nn_numeric_compat_input_placeholderList  =   ["check sample size (default : 100%",None,None,None]

nn_numeric_compat_input_jsList           =   [None,
                                             "process_nn_check_compatability(1)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_CHECK_NUMERIC_ID) + "')"]

nn_numeric_compat_input_reqList          =   [0]
nn_numeric_compat_input_short            =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    category options inputs   
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    category add forms
#--------------------------------------------------------------------------
"""

cat_change_values_input_title           =   "Change Data Value"
cat_change_values_input_id              =   "dccatchangevalsinput"
cat_change_values_input_idList          =   ["changecatval","changencatval",None,None,None]

cat_change_values_input_labelList       =   ["current_category",
                                             "new_category",
                                             "Rename</br>Category",
                                             "Return",
                                             "Help"]

cat_change_values_input_typeList        =   ["text","text","button","button","button"]

cat_change_values_input_placeholderList =   ["","",None,None,None]

cat_change_values_input_jsList          =   [None,None,
                                             "process_cols_callback("+ str(dcm.PROCESS_RENAME_CATEGORY) + ")",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp('" + str(dfchelp.CLEANSE_CAT_COL_RENAME_ID) + "')"]

cat_change_values_input_reqList         =   [0,1]
cat_change_values_input_short           =   True


"""
#--------------------------------------------------------------------------
#    add category form   
#--------------------------------------------------------------------------
"""
add_category_input_title                  =   ""
add_category_input_id                     =   "addcatinput"
add_category_input_idList                 =   ["addcatname",
                                               None,None,None]

add_category_input_labelList              =   ["new_category_name",
                                               "Add</br>New</br>Category",
                                               "Return",
                                               "Help"]

add_category_input_typeList               =   ["text","button","button","button"]

add_category_input_placeholderList        =   ["new category name",None,None,None]

add_category_input_jsList                 =   [None,
                                               "process_cat_function_callback(" + str(dcm.PROCESS_ADD_CATEGORY) + ")",
                                               "cleansing_tb_callback(3)",
                                               "displayhelp('" + str(dfchelp.CLEANSE_CAT_COL_ADD_ID) + "')"]

add_category_input_reqList                =   [0]

"""
#--------------------------------------------------------------------------
#    remove category form   
#--------------------------------------------------------------------------
"""
remove_category_input_title                =   ""
remove_category_input_id                   =   "removecatinput"
remove_category_input_idList               =   ["removecatname",
                                               None,None,None]

remove_category_input_labelList            =   ["category_to_remove",
                                               "Remove</br>Category",
                                               "Return",
                                               "Help"]

remove_category_input_typeList             =   ["text","button","button","button"]

remove_category_input_placeholderList      =   ["new category name",None,None,None]

remove_category_input_jsList               =   [None,
                                               "process_cat_function_callback(" + str(dcm.PROCESS_REMOVE_CATEGORY) + ")",
                                               "cleansing_tb_callback(3)",
                                               "displayhelp('" + str(dfchelp.CLEANSE_CAT_COL_REMOVE_ID) + "')"]

remove_category_input_reqList              =   [0]

"""
#--------------------------------------------------------------------------
#    remove category whitespace form   
#--------------------------------------------------------------------------
"""
remove_cat_whtspc_input_title              =   ""
remove_cat_whtspc_input_id                 =   "removewscatinput"
remove_cat_whtspc_input_idList             =   ["remwhtspccatname",
                                               None,None,None]

remove_cat_whtspc_input_labelList          =   ["category_name(s)_to_remove_whitespace_from",
                                               "Remove</br>Whitespace",
                                               "Return",
                                               "Help"]

remove_cat_whtspc_input_typeList           =   ["text","button","button","button"]

remove_cat_whtspc_input_placeholderList    =   ["category name",None,None,None]

remove_cat_whtspc_input_jsList             =   [None,
                                               "process_cat_function_callback(" + str(dcm.PROCESS_REMOVE_CATEGORY_WHITESPACE) + ")",
                                               "cleansing_tb_callback(3)",
                                               "displayhelp('" + str(dfchelp.CLEANSE_CAT_COL_WHITESPACE_ID) + "')"]

remove_cat_whtspc_input_reqList            =   [0]

"""
#--------------------------------------------------------------------------
#    reorder category form   
#--------------------------------------------------------------------------
"""
reorder_category_input_title              =   ""
reorder_category_input_id                 =   "reordercatinput"
reorder_category_input_idList             =   ["reorderorderlist",
                                               "reorderorderflag",
                                               None,None,None]

reorder_category_input_labelList          =   ["reorder_category_list",
                                               "ordered",
                                               "Reorder</br>Categories",
                                               "Return",
                                               "Help"]

reorder_category_input_typeList           =   ["text","select","button","button","button"]

reorder_category_input_placeholderList    =   ["new categories ordered list","order",None,None,None]

reorder_category_input_jsList             =   [None,None,
                                               "process_cat_function_callback(" + str(dcm.PROCESS_REORDER_CATEGORY) + ")",
                                               "cleansing_tb_callback(3)",
                                               "displayhelp('" + str(dfchelp.CLEANSE_CAT_COL_REORDER_ID) + "')"]

reorder_category_input_reqList            =   [0]

"""
#--------------------------------------------------------------------------
#    data cleansing category task bar
#--------------------------------------------------------------------------
"""
cat_cleansing_tb_doc_title              =   "Category Cleansing Options"
cat_cleansing_tb_title                  =   "Category Cleansing Options"
cat_cleansing_tb_id                     =   "category cleanseingoptionstb"

cat_cleansing_tb_keyTitleList           =   ["ReCleanse Category Column"]

cat_cleansing_tb_jsList                 =   ["process_cols_callback(" + str(dcm.GENERIC_COLUMN_OPTION) + ")"]

cat_cleansing_tb_centered               =   True


"""
#--------------------------------------------------------------------------
#    change df row input form
#--------------------------------------------------------------------------
"""
change_df_row_input_title            =   ""
change_df_row_input_id               =   "scrolldfrowsinput"
change_df_row_input_idList           =   ["scrolldfrowsrowid",
                                           "scrolldfrowsindexcols",
                                           "scrolldfrowsindexvals",
                                           None,None,None,None]

change_df_row_input_labelList       =   ["df_row_id",
                                          "df_index_cols",
                                          "df_index_values",
                                          "Display</br>Row ID",
                                          "Display</br>Index Row",
                                          "Return","Help"]

change_df_row_input_typeList        =   ["text","text","text","button","button","button","button"]

change_df_row_input_placeholderList =   ["","","",None,None,None,None]

change_df_row_input_jsList          =   [None,None,None,
                                         "inspection_task_bar_callback(" + str(dcm.PROCESS_GET_ROW_BY_ID) + ")",
                                         "inspection_task_bar_callback(" + str(dcm.PROCESS_GET_ROW_BY_INDEX) + ")",
                                         "inspection_task_bar_callback(" + str(dcm.DISPLAY_CLEANSE_ROW) + ")",
                                         "displayhelp('" + str(dfchelp.INSPECT_ROW_NANS_ID) + "')"]

change_df_row_input_reqList         =   [0]

change_df_row_input_short           =   True


"""
#--------------------------------------------------------------------------
#    select df row input form
#--------------------------------------------------------------------------
"""
select_df_rows_input_title            =   ""
select_df_rows_input_id               =   "selectdfrowsinput"
select_df_rows_input_idList           =   ["selectdfrowsrowid",
                                           "selectdfrowsindexcols",
                                           "selectdfrowsindexvals",
                                           None,None,None]

select_df_rows_input_labelList       =   ["df_row_id",
                                          "df_index_cols",
                                          "df_index_values",
                                          "Get</br>Selected</br>Row",
                                          "Return","Help"]

select_df_rows_input_typeList        =   ["text","text","text","button","button","button"]

select_df_rows_input_placeholderList =   ["","","",None,None,None,None]

select_df_rows_input_jsList          =   [None,None,None,
                                          "cleansing_tb_callback(" + str(dcm.PROCESS_SELECT_ROW_ID) + ")",
                                          "cleansing_tb_callback(" + str(dcm.DISPLAY_CLEANSE_CLEAR) + ")",
                                          "displayhelp('" + str(dfchelp.INSPECT_ROW_NANS_ID) + "')"]

select_df_rows_input_reqList         =   [0,1,2]

select_df_rows_input_short           =   True


import dfcleanser.data_inspection.data_inspection_widgets as diw

datacleansing_inputs        =   [change_values_input_id, nn_change_values_input_id, cat_change_values_input_id,
                                 find_values_input_id, nn_find_values_input_id, change_row_values_input_id,
                                 col_round_input_id, transform_remwhite_input_id, col_fillna_input_id, nn_col_fillna_input_title,
                                 nn_alpha_compat_input_id, nn_numeric_compat_input_id, add_category_input_id,
                                 remove_category_input_id, remove_cat_whtspc_input_id, reorder_category_input_id,
                                 diw.data_cleansing_df_input_id]


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

def display_cat_cleansing_taskbar() :
    
    catBGroup   =   ButtonGroupForm(cat_cleansing_tb_id,
                                    cat_cleansing_tb_keyTitleList,
                                    cat_cleansing_tb_jsList,
                                    cat_cleansing_tb_centered)
    
    catBGroup.set_custombwidth(480)
    catBGroup.set_centered(True)
        
    gridclasses     =   ["main"]
    gridhtmls       =   [catBGroup.get_html()]
    
    display_generic_grid("dfc-common-480px-single-wrapper",gridclasses,gridhtmls)
    print("\n")
    
    
def display_dfc_cleansing_main() :
    """
    * -------------------------------------------------------------------------- 
    * function : display the dfc cleansing taskbar and select forms
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    display_data_cleansing_main_taskbar()
    cfg.display_data_select_df(cfg.DataCleansing_ID)
    
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
    

def display_numeric_cols() :
    """
    * -------------------------------------------------------------------------- 
    * function : display numeric cols
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
                    
    cols_heading_html  =   "<div>Numeric Columns</div>"

    try :
        print("display_numeric_cols")            
        col_table_html  =   display_df_describe(False)
                    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [cols_heading_html,col_table_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
                        
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to display numeric column names",e)
        display_exception(opstat)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
    
    
def display_non_numeric_cols() :
    """
    * -------------------------------------------------------------------------- 
    * function : display non numeric cols
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    cols_heading_html  =   "<div>Non Numeric Columns</div>"
                
    try :
        
        nn_cols_html    =   display_df_nn_describe(False) 
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [cols_heading_html,nn_cols_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
                    
    except Exception as e:
        opstat = opStatus()
        opstat.store_exception("Unable to display non numeric column names",e)
        display_exception(opstat)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_simple_col_stats(df,colname) :
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
    
    col_stats_html  =  display_col_stats(df,colname,False,True)  
    
    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [col_stats_html]

    display_generic_grid("dfc-short-note-wrapper",gridclasses,gridhtmls)


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
    
    from dfcleanser.common.common_utils import is_datetime_col, is_date_col, is_time_col, is_timedelta_col, is_Timestamp_col, is_Timedelta_col
    
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
        
    if(ftype == object) :
        
        if(is_datetime_col(df,colname))     :   ftype     =   "datetime.datetime"    
        elif(is_date_col(df,colname))       :   ftype     =   "datetime.date" 
        elif(is_time_col(df,colname))       :   ftype     =   "datetime.time" 
        elif(is_timedelta_col(df,colname))  :   ftype     =   "datetime.timedelta" 
        elif(is_Timestamp_col(df,colname))  :   ftype     =   "Timestamp" 
        elif(is_Timedelta_col(df,colname))  :   ftype     =   "Timedelta" 

    
    statsRows.append(["Column Data Type",str(ftype)])
    labels.append("Column Data Type")
    values.append(str(ftype))
    colorList.append([whitecolor,whitecolor])
    
    if(is_categorical_col(df,colname)) :
        
        CI  =   pd.CategoricalIndex(df[colname])
        statsRows.append(["Category Ordered",str(CI.ordered)])
        labels.append("Category Ordered")
        values.append(str(CI.ordered))
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
    
    if(is_categorical_col(df,colname)) :
        
        CI      =   pd.CategoricalIndex(df[colname])
        cats    =   CI.categories.tolist()
        statsRows.append(["Categories Count",str(len(cats))])
        labels.append("Categories Count")
        values.append(str(len(cats)))
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

   
def display_col_data(showUniques=False) :
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

    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
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
        
        if(not(is_categorical_col(df,colname))) :
            
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
                    
        else :
            
            col_uniques_tb  =   ButtonGroupForm(cat_cleanse_change_tb_id,
                                                cat_cleanse_change_tb_keyTitleList,
                                                cat_cleanse_change_tb_jsList,
                                                cat_cleanse_change_tb_centered)
                    
            col_uniques_tb.set_customstyle({"font-size":13, "height":90, "width":110, "left-margin":15})
                
            col_uniques_tba  =   ButtonGroupForm(cata_cleanse_change_tb_id,
                                                 cata_cleanse_change_tb_keyTitleList,
                                                 cata_cleanse_change_tb_jsList,
                                                 cata_cleanse_change_tb_centered)
                    
            col_uniques_tba.set_customstyle({"font-size":13, "height":90, "width":110, "left-margin":70})
 
               
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        col_uniques_tb.set_gridwidth(480)

    else :
        col_uniques_tb.set_gridwidth(480)
        col_uniques_tb.set_custombwidth(75)

    if(not(is_categorical_col(df,colname))) :
        
        cleansing_text_tb_html          =   col_uniques_tb.get_html()
        
    else :
        
        cleansing_text_tb_html          =   col_uniques_tb.get_html() + col_uniques_tba.get_html()
        #print(cleansing_text_tb_html)
        
    cleansing_text_tb_html          =   "<br>" + cleansing_text_tb_html
               
    return(cleansing_text_tb_html)           
                

def get_unique_col_html(df,colname,opstat,sethrefs=True) :
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
    
    try :
    
        if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

            findparms = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
            if(len(findparms) > 0) :
            
                if(is_numeric_col(df,colname)) :

                    if(len(findparms[0]) < 1) :
                        minvalue    =   str(df[colname].min())
                    else :
                        minvalue    =   findparms[0]
                    
                    if(len(findparms[1]) < 1) :
                        maxvalue    =   str(df[colname].max())
                    else :
                        maxvalue    =   findparms[1]
                    
                    cfg.set_config_value(cfg.UNIQUES_RANGE_KEY,[minvalue,maxvalue])
                    
                else :
            
                    if(len(findparms[0]) < 1) :
                        cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY) 
                        
            else :
            
                cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)    
            
                
        col_uniques_table = dcTable("Unique Values and Counts",
                                    "uvalsTbl",
                                    cfg.DataCleansing_ID)
        
        if(not (is_numeric_col(df,colname)) ) :
            
            
            if(not (is_categorical_col(df,colname)) ) :
                
                unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,False)
                
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
                
                unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,False)
                
        else :

            
            unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,False)
            
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
        #display_exception(opstat)
    
    if(opstat.get_status()) :
    
        if(not (is_categorical_col(df,colname)) ) :
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :    
                uniques_find_heading_html       =   "<div>Find Unique Values</div>"
                uniques_find_html               =   find_values_html
            else :
                uniques_find_html               =   find_values_html
        
            if(opstat.get_status()) :
                find_notes_html =   get_help_note_html(help_note)
            else :
                help_note       =   "Invalid min_value or max_value entered."
                find_notes_html =   get_help_note_html(help_note)

        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
            if(not (is_categorical_col(df,colname)) ) :
        
                gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-right","dfc-footer"]
                gridhtmls       =   [unique_cols_html,uniques_find_heading_html,uniques_find_html,find_notes_html]
        
                display_generic_grid("display-df-cleanser-unique-columns-wrapper",gridclasses,gridhtmls)
            
            else :
            
                gridclasses     =   ["dfc-left"]
                gridhtmls       =   [unique_cols_html]
        
                display_generic_grid("display-df-cleanser-unique-columns-no-find-wrapper",gridclasses,gridhtmls)
            
        else :
        
            if(not (is_categorical_col(df,colname)) ) :
        
                gridclasses     =   ["dfc-top","dfc-main","dfc-footer"]
                gridhtmls       =   [unique_cols_html,uniques_find_html,find_notes_html]
        
                display_generic_grid("display-df-cleanser-unique-columns-pop-up-wrapper",gridclasses,gridhtmls)
            
            else :
            
                gridclasses     =   ["dfc-top"]
                gridhtmls       =   [unique_cols_html]
        
                display_generic_grid("display-df-cleanser-unique-columns-no-find-pop-up-wrapper",gridclasses,gridhtmls)
        
    
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
    
    colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    opstat  =   opStatus()
    
    clock = RunningClock()
    clock.start()

    try :
        
        """
        * -------------------------------------------------------------------------- 
        * ------------------------ get the uniques table --------------------------- 
        * -------------------------------------------------------------------------- 
        """
        if( (showUniques) or (is_categorical_col(df,colname)) ) :
            get_unique_col_html(df,colname,opstat)
            
            if(not opstat.get_status()) :
                display_exception(opstat)


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
            
            if(not(is_categorical_col(df,colname))) :
            
                cleansing_text_inputs   =   InputForm(nn_change_values_input_id,
                                                      nn_change_values_input_idList,
                                                      nn_change_values_input_labelList,
                                                      nn_change_values_input_typeList,
                                                      nn_change_values_input_placeholderList,
                                                      nn_change_values_input_jsList,
                                                      nn_change_values_input_reqList)
                
            else :
                
                cleansing_text_inputs   =   InputForm(cat_change_values_input_id,
                                                      cat_change_values_input_idList,
                                                      cat_change_values_input_labelList,
                                                      cat_change_values_input_typeList,
                                                      cat_change_values_input_placeholderList,
                                                      cat_change_values_input_jsList,
                                                      cat_change_values_input_reqList)
                
            
        """
        * -------------------------------------------------------------------------- 
        * -------------------- displpay the cleansing grid ------------------------- 
        * -------------------------------------------------------------------------- 
        """
        if(not(is_categorical_col(df,colname))) :
            unique_column_heading_html      =   "<div>'" + colname + "' Cleansing</div><br>"
        else :
            unique_column_heading_html      =   "<div>Rename Category</div><br>"            
    
        if( (not (is_numeric_col(df,colname))) and (is_categorical_col(df,colname)) ) :
            cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":90})
        else :
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
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
    
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to display column data",e)
        display_exception(opstat)
    
    clock.stop()



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
    
    df_title    =   cfg.get_config_value(cfg.CURRENT_CLEANSE_DF)
    
    rows_table = dcTable("df '" + df_title + "' : Row " + str(rowid),"dcdisrow",cfg.DataCleansing_ID)
    
    opstat = opStatus()
    
    df_row_cleanser_table_html    =   get_single_row(df,rows_table,rowid,colid,opstat,False)
    
    if(not (opstat.get_status()) ) :
        display_exception(opstat)

    else :
        
        print("\n")
        
        df_row_cleanser_heading_html    =   "<div>dataframe Row Cleanser</div></br>"
        
        df_row_input_form               =   InputForm(change_row_values_input_id,
                                                      change_row_values_input_idList,
                                                      change_row_values_input_labelList,
                                                      change_row_values_input_typeList,
                                                      change_row_values_input_placeholderList,
                                                      change_row_values_input_jsList,
                                                      change_row_values_input_reqList)
        
        df_row_input_form.set_shortForm(True)
        df_row_input_form.set_gridwidth(480)
        df_row_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":5})
        
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



def display_option(df,colname,input_html,heading_html) :
    """
    * -------------------------------------------------------------------------- 
    * function : display common column options
    * 
    * parms :
    *   df              -   dataframe
    *   colname         -   column name
    *   input_html      -   input form
    *   heading_html    -   form heading
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    print("\n")
        
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [col_stats_html,heading_html,input_html]

        display_generic_grid("col-change-datatype-fn-wrapper",gridclasses,gridhtmls)
    else :
        
        gridclasses     =   ["dfc-middle","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [col_stats_html,heading_html,input_html]

        display_generic_grid("col-change-datatype-fn-pop-up-wrapper",gridclasses,gridhtmls)
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_round_option() :
    """
    * -------------------------------------------------------------------------- 
    * function : display round column option
    * 
    * parms :
    *   df          -   dataframe
    *   colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
                
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
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
    cleansing_text_input_html       =   cleansing_text_inputs.get_html()+"<br><br><br><br><br><br><br><br><br><br><br>"    
    
    common_column_heading_html      =   "<div>Round Columns</div><br>"
        
    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def display_whitespace_option() :
    """
    * -------------------------------------------------------------------------- 
    * function : display whitespace remove option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    remws_uniques_table = dcTable("Unique Values for "+colname,
                                  "remwsuniquesTable",
                                  cfg.DataCleansing_ID)

    uniques_html            =   display_df_unique_column(df,remws_uniques_table,colname,False,False)
    
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
    
    common_column_heading_html      =   "<br><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove Whitespace</div>"
        
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


def display_fillna_option() :
    """
    * -------------------------------------------------------------------------- 
    * function : display fillna option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
                
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    common_column_heading_html  =   "<div>Fill Na</div><br>"
    cleansing_text_input_html   =   get_fillna_display(df,colname,cfg.DataCleansing_ID)+"<br><br><br><br><br><br>"

    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def get_fillna_display(df,colname,dfc_id) :
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
        
        grid_input_form     =   InputForm(col_fillna_input_id,
                                          col_fillna_input_idList,
                                          col_fillna_input_labelList,
                                          col_fillna_input_typeList,
                                          col_fillna_input_placeholderList,
                                          col_fillna_input_jsList,
                                          col_fillna_input_reqList)
            
    else :
        
        grid_input_form     =   InputForm(nn_col_fillna_input_id,
                                          nn_col_fillna_input_idList,
                                          nn_col_fillna_input_labelList,
                                          nn_col_fillna_input_typeList,
                                          nn_col_fillna_input_placeholderList,
                                          nn_col_fillna_input_jsList,
                                          nn_col_fillna_input_reqList)
    
    selectDicts     =   []
    
    naopts          =   {"default" : "fillna", "list" : ["fillna","dropna"],"callback" : "change_cleanse_na_opt"}
    selectDicts.append(naopts)
    
    
    if(is_numeric_col(df,colname)) :
        fillnas         =   {"default" : "None - use fillna_value", "list" : ["None - use fillna_value","mean","bfill","ffill"]}
        selectDicts.append(fillnas)
    
        get_select_defaults(grid_input_form,
                                col_fillna_input_id,
                                col_fillna_input_idList,
                                col_fillna_input_typeList,
                                selectDicts)
    
    grid_input_form.set_gridwidth(400)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":5})
    
    return(grid_input_form.get_html())


def display_dropna_option() :
    """
    * -------------------------------------------------------------------------- 
    * function : display dropna option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
                
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    common_column_heading_html  =   "<div>Drop Na</div><br>"
    cleansing_text_input_html   =   get_dropna_display(df,colname,cfg.DataCleansing_ID)+"<br><br><br><br><br><br>"

    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def get_dropna_display(df,colname,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the dropna html
    * 
    * parms :
    *   df      -   dataframe
    *   colname -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    grid_input_form     =   InputForm(col_dropna_input_id,
                                      col_dropna_input_idList,
                                      col_dropna_input_labelList,
                                      col_dropna_input_typeList,
                                      col_dropna_input_placeholderList,
                                      col_dropna_input_jsList,
                                      col_dropna_input_reqList)
            
    
    selectDicts     =   []
    
    naopts          =   {"default" : "dropna", "list" : ["fillna","dropna"],"callback" : "change_cleanse_na_opt"}
    selectDicts.append(naopts)
    
    droptype        =   {"default" : "any", "list" : ["any","all"]}
    selectDicts.append(droptype)
    
    get_select_defaults(grid_input_form,
                        col_dropna_input_id,
                        col_dropna_input_idList,
                        col_dropna_input_typeList,
                        selectDicts)
    
    grid_input_form.set_gridwidth(400)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":5})
    
    return(grid_input_form.get_html())


def display_check_alpha_num(option,colname) :
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
    
    
    cfg.set_config_value(cfg.CHKNUM_COL_KEY,colname)
    
    cols_heading_html  =   "<div>Non Numeric Columns</div>"
                
    clock = RunningClock()
    clock.start()

    try :
        from dfcleanser.common.table_widgets import get_table_value
        nn_df_describe_table = get_table_value("dcnngendfdesc")        

        nn_cols_html    =   nn_df_describe_table.get_html() 
                    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [cols_heading_html,nn_cols_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
                    
    except Exception as e:
        opstat = opStatus()
        opstat.store_exception("Unable to display non numeric column names",e)
        display_exception(opstat)

    clock.stop()
    
    print("\n")
    
    if(option == dcm.DISPLAY_ALPHANUMERIC_CHECK) :
        
        heading_html    =   "<div>Check '" + colname + "' Alphanumeric</br> Compatability</div><br>"
        
        grid_input_form     =   InputForm(nn_alpha_compat_input_id,
                                          nn_alpha_compat_input_idList,
                                          nn_alpha_compat_input_labelList,
                                          nn_alpha_compat_input_typeList,
                                          nn_alpha_compat_input_placeholderList,
                                          nn_alpha_compat_input_jsList,
                                          nn_alpha_compat_input_reqList)
            
    else :
        
        heading_html    =   "<div>Check '" + colname + "' Numeric</br> Compatability</div><br>"
            
        grid_input_form     =   InputForm(nn_numeric_compat_input_id,
                                          nn_numeric_compat_input_idList,
                                          nn_numeric_compat_input_labelList,
                                          nn_numeric_compat_input_typeList,
                                          nn_numeric_compat_input_placeholderList,
                                          nn_numeric_compat_input_jsList,
                                          nn_numeric_compat_input_reqList)
        
    grid_input_form.set_gridwidth(480)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":50})
    input_form_html =   grid_input_form.get_html() 
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [heading_html,input_form_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_cat_option(option,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display category option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    if(option == dcm.DISPLAY_ADD_CATEGORY) :
        
        get_unique_col_html(df,colname,opstat)
        
        cat_input_form      =   InputForm(add_category_input_id,
                                          add_category_input_idList,
                                          add_category_input_labelList,
                                          add_category_input_typeList,
                                          add_category_input_placeholderList,
                                          add_category_input_jsList,
                                          add_category_input_reqList)
        
        cat_input_form.set_gridwidth(480)
        cat_input_form.set_shortForm(True)
        cat_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":50})
        
        
        cfg.drop_config_value(cat_change_values_input_id+"Parms")
        cfg.drop_config_value(remove_category_input_id+"Parms")
        cfg.drop_config_value(remove_cat_whtspc_input_id+"Parms")
        cfg.drop_config_value(reorder_category_input_id+"Parms")
        
        cfg.set_config_value(add_category_input_id+"Parms",[""])
        
        cat_input_html      =   cat_input_form.get_html() 
        cat_heading_html    =   "<div>Add Category</div><br>"

    elif(option == dcm.DISPLAY_REMOVE_CATEGORY) :
        
        get_unique_col_html(df,colname,opstat)
        
        cat_input_form      =   InputForm(remove_category_input_id,
                                          remove_category_input_idList,
                                          remove_category_input_labelList,
                                          remove_category_input_typeList,
                                          remove_category_input_placeholderList,
                                          remove_category_input_jsList,
                                          remove_category_input_reqList)
        
        cat_input_form.set_gridwidth(480)
        cat_input_form.set_shortForm(True)
        cat_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":50})
        
        cfg.drop_config_value(cat_change_values_input_id+"Parms")
        cfg.drop_config_value(add_category_input_id+"Parms")
        cfg.drop_config_value(remove_cat_whtspc_input_id+"Parms")
        cfg.drop_config_value(reorder_category_input_id+"Parms")
        
        cfg.set_config_value(remove_category_input_id+"Parms",["[]"])
        
        cat_input_html      =   cat_input_form.get_html() 
        cat_heading_html    =   "<div>Remove Category</div><br>"
    
    elif(option == dcm.DISPLAY_REMOVE_CATEGORY_WHITESPACE) :
        
        get_unique_col_html(df,colname,opstat)
        
        cat_input_form      =   InputForm(remove_cat_whtspc_input_id,
                                          remove_cat_whtspc_input_idList,
                                          remove_cat_whtspc_input_labelList,
                                          remove_cat_whtspc_input_typeList,
                                          remove_cat_whtspc_input_placeholderList,
                                          remove_cat_whtspc_input_jsList,
                                          remove_cat_whtspc_input_reqList)
        
        cat_input_form.set_gridwidth(480)
        cat_input_form.set_shortForm(True)
        cat_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":50})
        
        cfg.drop_config_value(cat_change_values_input_id+"Parms")
        cfg.drop_config_value(add_category_input_id+"Parms")
        cfg.drop_config_value(reorder_category_input_id+"Parms")
        cfg.drop_config_value(remove_category_input_id+"Parms")
        
        cfg.set_config_value(remove_cat_whtspc_input_id+"Parms",["[]"])
        
        cat_input_html      =   cat_input_form.get_html() 
        cat_heading_html    =   "<div>Remove Category Whitespace</div><br>"
        
    elif(option == dcm.DISPLAY_REORDER_CATEGORY) :
        
        get_unique_col_html(df,colname,opstat)
        
        cat_input_form      =   InputForm(reorder_category_input_id,
                                          reorder_category_input_idList,
                                          reorder_category_input_labelList,
                                          reorder_category_input_typeList,
                                          reorder_category_input_placeholderList,
                                          reorder_category_input_jsList,
                                          reorder_category_input_reqList)
        
        selectDicts         =   []
 
        truefalseflag       =   {"default":"False","list":["True","False"]}
        selectDicts.append(truefalseflag)

        get_select_defaults(cat_input_form,
                            reorder_category_input_id,
                            reorder_category_input_idList,
                            reorder_category_input_typeList,
                            selectDicts)

        
        cat_input_form.set_gridwidth(480)
        cat_input_form.set_shortForm(True)
        cat_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":50})
        
        cfg.drop_config_value(cat_change_values_input_id+"Parms")
        cfg.drop_config_value(add_category_input_id+"Parms")
        cfg.drop_config_value(remove_category_input_id+"Parms")
        cfg.drop_config_value(remove_cat_whtspc_input_id+"Parms")
        
        cfg.set_config_value(reorder_category_input_id+"Parms",["[]","False"])
        
        cat_input_html      =   cat_input_form.get_html() 
        cat_heading_html    =   "<div>Reorder Categories</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [cat_heading_html,cat_input_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
        
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_select_df_row(parms) :
    """
    * -------------------------------------------------------- 
    * function : display scroll to input form
    * 
    * parms :
    *   N/A          -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    scroll_form   = InputForm(select_df_rows_input_id,
                              select_df_rows_input_idList,
                              select_df_rows_input_labelList,
                              select_df_rows_input_typeList,
                              select_df_rows_input_placeholderList,
                              select_df_rows_input_jsList,
                              select_df_rows_input_reqList)
    
    scroll_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":55})
    scroll_form.set_gridwidth(480)
    
    df = cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    
    index_names     =   []
                    
    index_columns   =   df.index.names
    
    if(len(index_columns) > 0) :
        for i in range(len(index_columns)) :
            if( not (index_columns[i] is None) ) :
                index_names.append(index_columns[i])
        
    if(len(index_names) == 0) :
        cfg.set_config_value(select_df_rows_input_id+"Parms",["","",""])
        cfg.set_config_value(select_df_rows_input_id+"ParmsProtect",[False,True,True]) 
    else :
        
        index_cols  =   "["
        for i in range(len(index_names)) :
            index_cols  =   index_cols + index_names[i]
            if(not (i == (len(index_names) - 1))) :
                index_cols  =   index_cols + ","
                
        index_cols      =   index_cols + "]"
        
        cfg.set_config_value(select_df_rows_input_id+"Parms",["",index_cols,""]) 
        cfg.set_config_value(select_df_rows_input_id+"ParmsProtect",[False,True,False]) 
    
    scroll_form_html    =   scroll_form.get_html()
    
    scroll_header_html    =   "<div>Select df Row To Cleanse</div><br>"
            
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [scroll_header_html,scroll_form_html]
            
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :       
        display_generic_grid("df-inspection-row-scroll-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-inspection-row-scroll-pop-up-wrapper",gridclasses,gridhtmls,True)










