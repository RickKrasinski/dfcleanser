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

from dfcleanser.common.html_widgets import (get_html_spaces, ButtonGroupForm, 
                                            InputForm, DEFAULT_PAGE_WIDTH)

from dfcleanser.common.table_widgets import (dcTable, MULTIPLE, SCROLL_DOWN, get_mult_table) 

from dfcleanser.common.common_utils import (is_int_col, get_select_defaults, run_javaScript,
                                            display_exception, opStatus, get_parms_for_input, 
                                            is_numeric_col, RunningClock, get_col_uniques, displayParms,
                                            display_generic_grid, is_datetime_datatype, whitecolor, yellowcolor, redcolor, greencolor)

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
            
    elif(key == dcm.OUTLIERS_FLAG) :
        if(cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY))
            
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
change_values_input_idList              =   ["changecval","changenval",None,None,None]

change_values_input_labelList           =   ["Current_Value",
                                             "New_Value",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

change_values_input_typeList            =   ["text","text","button","button","button"]

change_values_input_placeholderList     =   ["","",None,None,None]

change_values_input_jsList              =   [None,None,
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
nn_change_values_input_idList           =   ["changecval","changenval",None,None,None]

nn_change_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Change</br>Values",
                                             "Return",
                                             "Help"]

nn_change_values_input_typeList         =   ["text","text","button","button","button"]

nn_change_values_input_placeholderList  =   ["","",None,None,None]

nn_change_values_input_jsList           =   [None,None,
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
find_values_input_id                    =   "dcnumchangevalsinput"
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
                                             "find_nn_uvals_callback()",
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
nn_find_values_input_idList             =   ["findcval",None,None]

nn_find_values_input_labelList          =   ["value_in_column",
                                             "Find</br>Values",
                                             "Help"]

nn_find_values_input_typeList           =   ["text","button","button"]

nn_find_values_input_placeholderList    =   ["string to find in column",None,None]

nn_find_values_input_jsList             =   [None,
                                             "find_nn_uvals_callback()",
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
change_row_values_input_idList           =   ["changercval","changernval",None,None,None,None]

change_row_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Change</br>Value",
                                             "Drop</br>Row",
                                             "Return",
                                             "Help"]

change_row_values_input_typeList         =   ["text","text","button","button","button","button"]

change_row_values_input_placeholderList  =   ["","",None,None,None,None]

change_row_values_input_jsList           =   [None,None,
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
transform_remwhite_input_idList         =   ["leadtrailflag",
                                             None,None,None]

transform_remwhite_input_labelList      =   ["remove_type_flag",
                                             "Remove</br>Whitspace",
                                             "Return","Help"]

transform_remwhite_input_typeList       =   ["select","button","button","button"]

transform_remwhite_input_placeholderList =  ["remove leading and trailing",
                                             None,None,None]

transform_remwhite_input_jsList         =   [None,
                                             "whitespace_vals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

transform_remwhite_input_reqList        =   [0]

"""
#--------------------------------------------------------------------------
#    round column input text
#--------------------------------------------------------------------------
"""
"""
col_fillna_input_title                  =   ""
col_fillna_input_id                     =   "colfillnainput"
col_fillna_input_idList                 =   ["fncolname",
                                             "fnoption",
                                             "fnvalue",
                                             None,None,None]

col_fillna_input_labelList              =   ["column_name",
                                             "fillna_algorithm",
                                             "fillna_value",
                                             "fillna",
                                             "Return",
                                             "Help"]

col_fillna_input_typeList               =   ["text","select","text","button","button","button"]

col_fillna_input_placeholderList        =   ["column name",
                                             "fillna algorithm",
                                             "fillna value",
                                             None,None,None]

col_fillna_input_jsList                 =   [None,None,None,
                                             "fillna_col_vals_callback()",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

col_fillna_input_reqList                =   [0,1,2]
col_fillna_input_short                  =   True
"""

"""
#--------------------------------------------------------------------------
#    cleanse numeric cols round task bar
#--------------------------------------------------------------------------
"""
col_cleanse_round_tb_title              =   ""
col_cleanse_round_tb_title              =   ""
col_cleanse_round_tb_id                 =   "colcleansenormaloptionstb"

col_cleanse_round_tb_keyTitleList       =   ["Drop</br>Column",
                                             "Drop</br>Current</br>Value Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Round </br>Column</br>Values",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data Type"]

col_cleanse_round_tb_jsList             =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                             "process_cols_na_callback(39)",
                                             "process_cols_callback(" + str(dcm.DISPLAY_ROUND_COLUMN_OPTION) + ")",
                                             "process_cols_na_callback(40)",
                                             "process_cols_na_callback(41)"]

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
                                                    "process_cols_na_callback(41)"]

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
                                             "process_cols_na_callback(39)",
                                             "process_cols_na_callback(40)",
                                             "process_cols_na_callback(41)"]

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
                                                    "process_cols_na_callback(41)"]

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
                                             "process_cols_na_callback(39)",
                                             "process_cols_callback(" + str(dcm.DISPLAY_COL_CHANGE_OPTION) + ")",
                                             "process_cols_na_callback(40)",
                                             "process_cols_na_callback(41)"]

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
                                                    "process_cols_na_callback(41)"]

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

nn_col_cleanse_change_tb_keyTitleList   =   ["Drop</br> Column",
                                             "Drop</br>Current</br>Value Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Remove</br>White</br>Space",
                                             "Fill</br>NaN</br>Values",
                                             "Change</br>Data Type"]

nn_col_cleanse_change_tb_jsList         =   ["process_cols_callback(" + str(dcm.DROP_COL_OPTION) + ")",
                                             "process_cols_callback(" + str(dcm.DROP_ROWS_OPTION) + ")",
                                             "process_cols_na_callback(39)",
                                             "process_cols_callback(" + str(dcm.DISPLAY_REM_WHTSPC_OPTION) + ")",
                                             "process_cols_na_callback(40)",
                                             "process_cols_na_callback(41)"]

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
                                                    "process_cols_na_callback(41)"]

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
list_unique_jsList                      =   ["show_uniques_callback()"]

list_unique_centered                    =   True

"""
#--------------------------------------------------------------------------
#    graphs values task bar
#--------------------------------------------------------------------------
"""
show_graphs_doc_title                   =   ""
show_graphs_title                       =   ""
show_graphs_id                          =   "showgraphs"

show_graphs_keyTitleList                =   ["Show Column Graphs"]
show_graphs_jsList                      =   ["show_graphs_callback()"]

show_graphs_centered                    =   True

add_graph_doc_title                     =   ""
add_graph_title                         =   ""
add_graph_id                            =   "addgraph"

add_graph_keyTitleList                  =   ["Add User Graphs"]
add_graph_jsList                        =   ["add_graph_callback()"]

add_graph_centered                      =   True

"""
#--------------------------------------------------------------------------
#    outliers task bar
#--------------------------------------------------------------------------
"""
outliers_tb_doc_title                   =   ""
outliers_tb_title                       =   ""
outliers_tb_id                          =   "outlierstb"

outliers_tb_keyTitleList                =   ["Show Outliers"]
outliers_tb_jsList                      =   ["show_outliers_callback()"]

outliers_tb_centered                    =   True

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_no_data_heading() :
    display_data_cleansing_main_taskbar()
    from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
    display_inspection_data()

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
    
    
def display_data_select_df() :
    
        from dfcleanser.data_inspection.data_inspection_widgets import get_select_df_form
        select_df_form              =   get_select_df_form("Cleanse")
    
        gridclasses     =   ["dfc-footer"]
        gridhtmls       =   [select_df_form.get_html()]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)
    
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
        stats_table.set_smallwidth(99)
        stats_table.set_smallmargin(1)
    else :
        stats_table.set_smallwidth(99)
        stats_table.set_smallmargin(1)

    stats_table.set_border(False)
    stats_table.set_checkLength(False)
    
    if(display) :
        stats_table.display_table()
    else :
        return(stats_table.get_html())


def display_cleanse_console(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display column cleanse console
    * 
    * parms :
    *   df          -   dataframe
    *   colname     -   column name 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    numeric     =   is_numeric_col(df,colname)
    
    console_stats_html  =   display_col_stats(df,colname,False,True)

    
    console_unitb_form  =   ButtonGroupForm(list_unique_id,
                                            list_unique_keyTitleList,
                                            list_unique_jsList,
                                            list_unique_centered)
    console_unitb_form.set_custombwidth(260)
    console_unitb_form.set_gridwidth(480)
    console_unitb_html  =   console_unitb_form.get_html() 

    
    console_graph_form  =   ButtonGroupForm(show_graphs_id,
                                            show_graphs_keyTitleList,
                                            show_graphs_jsList,
                                            show_graphs_centered)
    console_graph_form.set_custombwidth(260)
    console_graph_form.set_gridwidth(480)
    console_graph_html  =   console_graph_form.get_html() 
    
    console_outls_form  =   ButtonGroupForm(outliers_tb_id,
                                            outliers_tb_keyTitleList,
                                            outliers_tb_jsList,
                                            outliers_tb_centered)
    console_outls_form.set_custombwidth(260)
    console_outls_form.set_gridwidth(480)
    console_outls_html  =   console_outls_form.get_html() 
    
    if(numeric) :
        console_tb_html     =   ("<div style='margin-left: 2px;'>" + console_unitb_html + console_graph_html + console_outls_html + "</div>")
    else :
        console_tb_html     =   ("<div style='margin-left: 2px;'>" + console_unitb_html + "</div>")

    console_heading_html      =   "<div>Column '" + colname + "' Data Cleansing</div><br>"

    gridclasses     =   ["dfcleanser-common-grid-header", 
                         "dfc-top",
                         "dfc-footer"]
        
    gridhtmls       =   [console_heading_html,
                         console_stats_html,
                         console_tb_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("display-dfcleansing-console-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("display-dfcleansing-console-pop-up-wrapper",gridclasses,gridhtmls)
    
    print("\n")


def display_pop_up_graphs(colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display numeric column data
    * 
    * parms :
    *   dftitle     -   dataframe title
    *   colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    code    =   "from dfcleanser.data_cleansing.data_cleansing_widgets import display_common_graphs" + "\\n"
    code    =   code + "display_common_graphs('"+str(colname)+"')"

    print("\n\ncode",code)
    cmd     =   'run_code_in_popupcodecell("'+code+'");'
    
    print("\n\ncmd",cmd)
    run_javaScript(cmd)


def display_common_graphs(colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display numeric column data
    * 
    * parms :
    *   colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    clock = RunningClock()
    clock.start()

    try :
        
        try :
            import os
            os.remove("hist.png")
            os.remove("zscore.png")
        except :
            df = None   
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
            
        import numpy as np
        counts      =   df[colname].value_counts().to_dict()
        dfuniques   =   list(counts.keys())
        uniques     =   np.asarray(dfuniques)
        ucounts     =   list(counts.values())
        ucounts     =   np.asarray(ucounts)

        import matplotlib.pyplot as plt
        fig     =   plt.figure()
        plt.style.use('ggplot')
        plt.hist(uniques,weights=ucounts)
        plt.title("'" + colname + "'" + " Histogram")
        fig.savefig("hist.png")
        plt.close()
            
        cmean       =   df[colname].mean() 
        cstd        =   df[colname].std()

        zscores      =   []
        for i in range(len(dfuniques)) :
            zscores.append((dfuniques[i]-cmean)/cstd)
        
        # dictionary of lists  
        zdict = {'ZScore': zscores, 'Frequency': ucounts}  
    
        import pandas as pd
        zdf     =   pd.DataFrame(zdict)     
        ax = zdf.plot(x='ZScore', y='Frequency', kind='kde', figsize=(10, 6))
        fig1    =   ax.get_figure()
        arr = ax.get_children()[0]._x
        plt.xticks(np.linspace(arr[0], arr[-1]), rotation=90)
        plt.title("'" + colname + "'" + " ZScores")
        fig1.savefig("zscore.png")
        plt.close()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        
        title_html      =   "<div>Column Graphs</div>"
        hist_html       =   "<br><br><img src='hist.png' alt='Histogram' height='400' width='400'>"
        zscore_html     =   "<img src='zscore.png' alt='ZScores' height='480' width='640'>"
        
        gridhtmls       =   [title_html,hist_html,zscore_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-dfcleansing-graphs-wrapper",gridclasses,gridhtmls)
        else :
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
            display_generic_grid("display-dfcleansing-graphs-pop-up-wrapper",gridclasses,gridhtmls)
        
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to plot column",e)
        display_exception(opstat)

    clock.stop()

   
def display_col_data() :
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
    df = cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
    
    colname         =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    outliers        =   cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY)
    if(outliers == None) : 
        outliers = False
        
    showuniques     =   cfg.get_config_value(cfg.UNIQUES_FLAG_KEY)
    if(showuniques == None) : 
        showuniques = False

    if (showuniques) :
       #print("\n")
       display_unique_col_data(df)
       print("\n")
       
    else :
        display_cleanse_console(df,colname)

    if(not (cfg.get_config_value(cfg.GRAPHS_FLAG_KEY) == None)) :

        display_common_graphs(colname)
        print("\n")
        
    if(outliers) :
        get_simple_outliers(df,cfg.get_config_value(cfg.CLEANSING_COL_KEY))


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

    nans            =   df[colname].isnull().sum()
    
    if (is_numeric_col(df,colname) ) :
        if(is_int_col(df,colname)) :
                
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    
                if(nans > 0) :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_cleanse_int_tb_id,
                                                        col_cleanse_int_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_cleanse_int_tb_jsList,dfc_id),
                                                        col_cleanse_int_tb_centered)
                        
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":135})
                        
                else :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_nonans_cleanse_int_tb_id,
                                                        col_nonans_cleanse_int_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_nonans_cleanse_int_tb_jsList,dfc_id),
                                                        col_nonans_cleanse_int_tb_centered)
                    
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":260})
                                        
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
                        
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":80})
                        
                else :
                        
                    col_uniques_tb  =   ButtonGroupForm(col_nonans_cleanse_round_tb_id,
                                                        col_nonans_cleanse_round_tb_keyTitleList,
                                                        get_cleansing_tb_js_list(col_nonans_cleanse_round_tb_jsList,dfc_id),
                                                        col_nonans_cleanse_round_tb_centered)
                    
                    col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":190})
                                        
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
                    
                col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":80})

            else :
                    
                col_uniques_tb  =   ButtonGroupForm(nn_nonans_col_cleanse_change_tb_id,
                                                    nn_nonans_col_cleanse_change_tb_keyTitleList,
                                                    get_cleansing_tb_js_list(nn_nonans_col_cleanse_change_tb_jsList,dfc_id),
                                                    nn_nonans_col_cleanse_change_tb_centered)
                
                col_uniques_tb.set_customstyle({"font-size":13, "height":75, "width":120, "left-margin":195})
                
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
        col_uniques_tb.set_gridwidth(860)

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

        minmax = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if( (len(minmax[1]) < 1) or (len(minmax[2]) < 1)) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Find values input values are invalid")
            display_exception(opstat)
            
            parmslabels = ["Min_Value","Max_Value"]
            parmsvals   = [minmax[1],minmax[2]]
            displayParms("Find Values Inputs",parmslabels,parmsvals,cfg.DataCleansing_ID)
            cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
            
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
            uniques     =   {}
            
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
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":80})
            find_values_inputs.set_gridwidth(360)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
        else :

            
            unique_cols_html    =   display_df_unique_column(df,col_uniques_table,colname,sethrefs,counts,False)
            find_values_inputs  =   InputForm(find_values_input_id,
                                              find_values_input_idList,
                                              find_values_input_labelList,
                                              find_values_input_typeList,
                                              find_values_input_placeholderList,
                                              find_values_input_jsList,
                                              find_values_input_reqList)
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":80})
            find_values_inputs.set_gridwidth(360)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
    except Exception as e:
        
        opstat.store_exception("Unable to display column uniques",e)
        display_exception(opstat)

    gridclasses     =   ["dfc-top","dfc-main"]
    gridhtmls       =   [unique_cols_html,find_values_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("display-df-cleanser-unique-columns-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("display-df-cleanser-unique-columns-pop-up-wrapper",gridclasses,gridhtmls)

    print("\n")
 
    
def display_unique_col_data(df) :
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
    
    cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":30})
    cleansing_text_inputs.set_gridwidth(360)
    cleansing_text_inputs.set_shortForm(True)
    cleansing_text_input_html       =   cleansing_text_inputs.get_html()    
        
    cleansing_text_tb_html          =   get_cleansing_tb_html(df,colname,cfg.DataCleansing_ID)

    
    gridclasses     =   ["dfcleanser-common-grid-header", 
                         "dfc-bottom",
                         "dfc-footer"]
        
    gridhtmls       =   [unique_column_heading_html,
                         cleansing_text_input_html,
                         cleansing_text_tb_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("display-df-cleanser-input-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("display-df-cleanser-input-pop-up-wrapper",gridclasses,gridhtmls)
    
    clock.stop()

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def get_simple_outliers(df,colname) :  
    """
    * -------------------------------------------------------------------------- 
    * function : get simple outliers
    * 
    * parms :
    *   df          -   dataframe
    *   colname    -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    clock = RunningClock()
    clock.start()
        
    totrows     =   len(df)
    
    std         =   df[colname].std()
    mean        =   df[colname].mean()
    minv        =   df[colname].min()
    maxv        =   df[colname].max()

    Red     = "#FAA78F"
    Green   = "#8FFAC0"
    Yellow  = "#FAFB95"

    try :
        
        outliersCount = get_simple_col_outliers(df,colname)
            
        outHeader    =   ["Num</br>std devs</br>from Mean","Count","% Total</br>Values","Values Range"]
        outRows      =   []
        outWidths    =   [10,10,15,65]
        outAligns    =   ["center","center","center","left"]
        colorList    =   []    
        
        for i in range(len(outliersCount)) :

            outrow      =   []
            colorRow    =   []
            
            if(outliersCount[i] > 0) :
                outrow.append(i)
                outrow.append(str(outliersCount[i]))
                outrow.append(float("{0:.5f}".format(100 * (outliersCount[i] / totrows))))
                if(i == 0) :
                    outrow.append("{0:.2f}".format(mean - ((i+1)*std)) + " - " + "{0:.2f}".format(mean + ((i+1)*std)))
                    colorRow = [Green,Green,Green,Green]

                else :

                    lowermin = mean - ((i+1)*std)
                    lowermax = mean - ((i)*std)
                    if(lowermin < minv) : lowermin = minv
                    if(lowermax < minv) : lowermax = minv
                    
                    uppermin = mean + ((i)*std)
                    uppermax = mean + ((i+1)*std)
                    if(uppermin > maxv) : uppermin = maxv
                    if(uppermax > maxv) : uppermax = maxv
                    
                    rangestr    =   ""
                    rangestr1   =   ""
                    
                    if(lowermax > minv) :
                        rangestr = "{0:.2f}".format(lowermin) + " - " + "{0:.2f}".format(lowermax)
                    if(uppermin < maxv) :
                        rangestr1 = rangestr1 + "{0:.2f}".format(uppermin) + " - " + "{0:.2f}".format(uppermax)
                    
                    if( (len(rangestr) > 0) and (len(rangestr1) > 0) ) :
                            rangestr = rangestr + "  and  " + rangestr1
                    else :
                        rangestr = rangestr + rangestr1
                    
                    outrow.append(rangestr)
                    if(i > 2) :
                        colorRow = [Red,Red,Red,Red]
                    else :
                        colorRow = [Yellow,Yellow,Yellow,Yellow]
                    
                outRows.append(outrow)
                colorList.append(colorRow)
          

        outliers_table = dcTable("Simple Outliers","simpleoutliers",cfg.DataCleansing_ID,
                                 outHeader,outRows,outWidths,outAligns)
        
        outliers_table.set_colsperrow(4)
        outliers_table.set_rowspertable(30)
        outliers_table.set_maxtables(1)
        outliers_table.set_checkLength(False)
        outliers_table.set_color(True)
        outliers_table.set_colorList(colorList)
        
        outliers_table.display_table()
            
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to get simple outliers",e)
        display_exception(opstat)

    clock.stop() 
           
    return(opstat)    
        

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
        df_row_input_form.set_custombwidth(90)
        
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
#------------------------------------------------------------------
#   Datacleansing dispaly utilities 
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def display_non_numeric_df_describe(df,table,datatype=None,colList=None,display=True,) :#,checkboxes=False) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display non numeric column descriptive data
    * 
    * parms :
    *   df          -   dataframe
    *   table       -   table
    *   datatype    -   datatype
    *   colList     -   list of columns
    *   display     -   Boolean flag
    *
    * returns : 
    *  N/A for display - True table html display - False
    * --------------------------------------------------------
    """

    import pandas
    import datetime

    df_cols     =   df.columns.tolist()
    nanrow      =   []
    uniquerow   =   []
    maxlrow     =   []
    
    nn_cols         =   []
    col_stats       =   []
    df_stats        =   []

    # build the column stats for the columns list
    if(colList == None) :

        if(datatype == None) :
            
            for i in range(len(df_cols)) :
                if(not(is_numeric_col(df,df_cols[i]))) :
                    nn_cols.append(df_cols[i])    
        else :
            
            from dfcleanser.data_inspection.data_inspection_model import get_df_datatypes_data
            df_data_info = get_df_datatypes_data(df) 

            for i in range(len(df_data_info[0])) :
                if(datatype == object) :
                    if(df_data_info[0][i] == object) :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
                elif(datatype == str) :
                    if(df_data_info[0][i] == "str") :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
                elif(datatype == datetime.datetime) :
                    if(is_datetime_datatype(df_data_info[0][i])) :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
        
                elif(datatype == pandas.core.dtypes.dtypes.CategoricalDtype) :
                    if(df_data_info[0][i] == pandas.core.dtypes.dtypes.CategoricalDtype) :
                        nn_cols = df_data_info[2].get("category")
                    
    else :
        nn_cols = colList
    
    for i in range(len(nn_cols)) :
        
        try :
                
            col_stats.append(df[nn_cols[i]].isnull().sum())
            uniques = get_col_uniques(df,nn_cols[i])
            col_stats.append(len(uniques))
                
            maxlength = 0 
            alphanum  = False
            for j in range(len(uniques)) :
                if(len(str(uniques[j])) > maxlength) :
                    maxlength =  len(str(uniques[j])) 
                if(str(uniques[j]).isalnum()) :
                    alphanum = True
            col_stats.append(maxlength)
            col_stats.append(alphanum)
        except : 
            col_stats = [0, 0, 0, 0, False]
                
                
        df_stats.append(col_stats)
        col_stats   =   []
        
    # build the table lists from the column stats
    dfHeader        =   ["    "]
    dfRows          =   []
    dfWidths        =   [9]
    dfAligns        =   ["center"]
    dfchrefs        =   [None]
    
    nanrow          =   []
    uniquerow       =   []
    maxlrow         =   []
    alphanumrow     =   []
    
    dfHeaderList    =   []
    dfRowsList      =   []
    dfWidthsList    =   []
    dfAlignsList    =   []
    dfchrefsList    =   []
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        table.set_colsperrow(7)
    else :
        table.set_colsperrow(3)
        
    table.set_rowspertable(5)
    table.set_maxtables(1)
    
    import datetime
    if(datatype == object) :
        dtstr = "Column Stats for datatype "+"&#60;object&#62;"
    elif(datatype == str) :
        dtstr = "Column Stats for datatype "+"&#60;str&#62;"
    elif(datatype == datetime.datetime) :
        dtstr = "Column Stats for datatype "+"&#60;datetime&#62;"
    elif(datatype == datetime.timedelta) :
        dtstr = "Column Stats for datatype "+"&#60;timedelta&#62;"
    elif(datatype == pandas.core.dtypes.dtypes.CategoricalDtype) :
        dtstr = "Column Stats for datatype "+"&#60;category&#62;"
    elif(datatype == None) :
        dtstr = "Non Numeric Columns"
    else :
        dtstr = "Column Stats for datatype "+"&#60;other&#62;"
    
    for i in range(len(nn_cols)) :
        
        dfHeader.append(nn_cols[i])
        nanrow.append(df_stats[i][0])
        uniquerow.append(df_stats[i][1])
        maxlrow.append(df_stats[i][2])
        alphanumrow.append(df_stats[i][3])
        
        dfWidths.append(13)
        dfAligns.append("center")
        dfchrefs.append("ncol")
        
        if( ( ((i+1) % table.get_colsperrow()) == 0) and (i>0) ) :
                
            dfHeaderList.append(dfHeader)
            dfRowsList.append(get_nn_rows(table.get_tableid(),nanrow,
                                          uniquerow,maxlrow,alphanumrow))#,checkboxes))
            
            dfWidthsList.append(dfWidths)
            dfAlignsList.append(dfAligns)
            dfchrefsList.append(dfchrefs)
                
            dfHeader    =   ["    "]
            dfRows      =   []
            dfWidths    =   [9]
            dfAligns    =   ["center"]
            dfchrefs    =   [None]

            nanrow          =   []
            uniquerow       =   []
            maxlrow         =   []
            alphanumrow     =   []
            
    # handle any incomplete rows 
    if( ((i+1) % table.get_colsperrow())  != 0) :
        
        for k in range((table.get_colsperrow() - ((i+1) % table.get_colsperrow()))):#+2) :
            dfHeader.append("")
            dfRows.append("")
            dfWidths.append(13)
            dfAligns.append("center")
            dfchrefs.append(None)
            
            nanrow.append("")
            uniquerow.append("")
            maxlrow.append("")
            alphanumrow.append("")
            
    if(len(dfRows) > 0) :
        
        dfHeaderList.append(dfHeader)    
        dfRowsList.append(get_nn_rows(table.get_tableid(),nanrow,
                                      uniquerow,maxlrow,alphanumrow))#,checkboxes))
                
        dfWidthsList.append(dfWidths)
        dfAlignsList.append(dfAligns)
        dfchrefsList.append(dfchrefs)

    title = dtstr
    table.set_title(title)    
    
    table.set_headerList(dfHeaderList)
    table.set_widthList(dfWidthsList)
    table.set_alignList(dfAlignsList)
    table.set_hhrefList(dfchrefsList)
    table.set_rowList(dfRowsList)
    
    table.set_tabletype(MULTIPLE)
    table.set_numtables(len(dfHeaderList))
    table.set_note(get_html_spaces(10)+"<b>*</b> To select column to cleanse click on Column Name above")

    #table.dump()

    if(display) :
        get_mult_table(table,SCROLL_DOWN)
    else :
        return(get_mult_table(table,SCROLL_DOWN,False))


"""            
#------------------------------------------------------------------
#   get non numeric data and form table rows
#
#   counts  -   list of counts for rows
#   means   -   list of means for rows
#   stds    -   list of counts for rows
#   mins    -   list of mins for rows
#   maxs    -   list of maxs for rows
#
#------------------------------------------------------------------
"""
def get_nn_rows(formId,nans,uniques,maxlens,alphanums) :#,checkboxes) :    
    """
    * -------------------------------------------------------------------------- 
    * function : get non numeric data and form table rows
    * 
    * parms :
    *   formId     -   form id
    *   nans       -   nans list
    *   uniques    -   uniques list
    *   maxlens    -   max lens list
    *   alphanums  -   alphanumerics list
    *
    * returns : 
    *  table rows
    * --------------------------------------------------------
    """

    currentRow  =   []
    allrows     =   []
    
    txtCol      =   ["<b>NaNs</b>","<b>Uniques</b>","<b>Max Len</b>","<b>AlphaNum</b>"] 
    
    for i in range(len(txtCol)) :
        currentRow.append(txtCol[i])
        
        if(i == 0) :
            for j in range(len(nans)) : 
                currentRow.append(nans[j])
        elif(i == 1) :
            for j in range(len(uniques)) : 
                currentRow.append(uniques[j])
        elif(i == 2) :
            for j in range(len(maxlens)) : 
                currentRow.append(maxlens[j])
        elif(i == 3) :
            for j in range(len(alphanums)) : 
                currentRow.append(alphanums[j])
            
        allrows.append(currentRow)
        currentRow = []
        
    return(allrows)
    

def get_simple_col_outliers(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a simplelist of outliers based on stddev from means
    * 
    * parms :
    *   df       -   dataframe
    *   colname  -   column name
    *
    * returns : 
    *  outliers
    * --------------------------------------------------------
    """

    outliers        =   []
    outlierscount   =   []
    
    numstddevs      =   15
    
    for i in range(numstddevs) :
        outliers.append([])
        outlierscount.append(0)
    
    mean    =   df[colname].mean()
    std     =   df[colname].std()
    
    counts  =   df[colname].value_counts().to_dict()
    uniques =   list(counts.keys())
    
    if(is_numeric_col(df,colname)) :
        uniques.sort()

    for i in range(len(uniques)) :
        import pandas as pd
        if( not pd.isnull(uniques[i])) :
            difference = abs(mean - uniques[i])
        
            import math
            outindex = math.floor(difference / std)
            outlierscount[outindex] = outlierscount[outindex] + counts.get(uniques[i])
    
    return(outlierscount)        


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


def get_whitespace_chars_table() :    
    """
    * -------------------------------------------------------------------------- 
    * function : get the whitespace chars table
    * 
    * parms :
    *
    * returns : 
    *  NA
    * --------------------------------------------------------
    """

    # build the table lists from the column stats
    dfHeader        =   []
    dfRows          =   []
    dfWidths        =   [100]
    dfAligns        =   ["left"]
    
    for i in range(len(dcm.whitespace_chars)) :
        
        row_html    =   get_whitespace_chars_cb(dcm.whitespace_chars_ids[i],
                                                dcm.whitespace_chars[i],
                                                dcm.whitespace_chars_text[i])
        
        dfRows.append([row_html])
        
    wchars_table = dcTable("Whitespace chars","wscharsTable",cfg.DataCleansing_ID,
                           dfHeader,dfRows,dfWidths,dfAligns)
    
    wchars_table.set_refList(None)
    wchars_table.set_hhrefList(None)
    wchars_table.set_small(True)
    wchars_table.set_smallwidth(98)
    wchars_table.set_smallmargin(5)
    wchars_table.set_checkLength(False)

    wchars_table.set_border(True)
    
    from dfcleanser.common.table_widgets import ROW_MAJOR,SCROLL_DOWN, get_row_major_table
    wchars_table.set_tabletype(ROW_MAJOR)
    wchars_table.set_rowspertable(len(dcm.whitespace_chars_ids))

    tablehtml = get_row_major_table(wchars_table,SCROLL_DOWN,False)

        
    return(tablehtml)
    

def display_option(df,colname,input_html,heading_html) :
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_column_uniques
    uniques_html    =   display_column_uniques(df,colname,False)        

    col_stats_html  =   display_col_stats(df,colname,False,False)
    
    print("\n")

    gridclasses     =   ["dfc-top","dfc-middle","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [uniques_html,col_stats_html,heading_html,input_html]
    
    display_generic_grid("col-change-datatype-wrapper",gridclasses,gridhtmls)
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

    
def display_dropna_option(df,colname) :
    
    common_column_heading_html      =   "<div>Drop Na Parameters</div><br>"
        
    from dfcleanser.data_transform.data_transform_columns_widgets import get_dropna_display
    cleansing_text_input_html   =   get_dropna_display(False,cfg.DataCleansing_ID)+"<br>"

    display_option(df,colname,cleansing_text_input_html,common_column_heading_html)


def display_fillna_option(df,colname) :
    
    common_column_heading_html      =   "<div>Fill Na Parameters</div><br>"
        
    from dfcleanser.data_transform.data_transform_columns_widgets import get_fillna_display
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
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_column_uniques
    uniques_html    =   display_column_uniques(df,colname,False)        
    
    col_stats_html  =   display_col_stats(df,colname,False,False)
    
    whitespace_html =   get_whitespace_chars_table()
    
    cleansing_text_inputs   =   InputForm(transform_remwhite_input_id,
                                          transform_remwhite_input_idList,
                                          transform_remwhite_input_labelList,
                                          transform_remwhite_input_typeList,
                                          transform_remwhite_input_placeholderList,
                                          transform_remwhite_input_jsList,
                                          transform_remwhite_input_reqList)
        
    selectDicts     =   []
    typesflag         =   {"default":"All","list":["Leading and Trailing Only","All"]}
    selectDicts.append(typesflag)

    get_select_defaults(cleansing_text_inputs,
                        transform_remwhite_input_id,
                        transform_remwhite_input_idList,
                        transform_remwhite_input_typeList,
                        selectDicts)
        
    cleansing_text_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":20})
    cleansing_text_inputs.set_gridwidth(360)
    cleansing_text_inputs.set_shortForm(True)
    
    cleansing_text_input_html   =   cleansing_text_inputs.get_html()+"<br>"
    
    common_column_heading_html      =   "<div>Remove Whitespace Parameters</div><br>"
        
    print("\n")

    gridclasses     =   ["dfc-top","dfc-middle","dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [uniques_html,col_stats_html,common_column_heading_html,whitespace_html,cleansing_text_input_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("display-df-whitespace-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("display-df-whitespace-pop-up-wrapper",gridclasses,gridhtmls)    
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

















