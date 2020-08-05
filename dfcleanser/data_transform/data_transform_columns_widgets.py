"""
# data_transform_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg 
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_transform.data_transform_model as dtm

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR)

from dfcleanser.common.common_utils import (opStatus, get_parms_for_input, display_exception,
                                            is_numeric_col, display_generic_grid, get_select_defaults, 
                                            get_dtype_str_for_datatype, does_col_contain_nan, is_column_in_df,
                                            get_help_note_html, is_string_col, is_float_col, is_int_col)

from dfcleanser.common.display_utils import display_column_names

from dfcleanser.sw_utilities.sw_utility_genfunc_model import  (get_generic_function_desc, get_genfunc_list, 
                                                               get_apply_function_parms, get_apply_function_return_datatype,
                                                               get_apply_function_parms_datatypes,get_reserved_function_form_type, 
                                                               get_reserved_function_parms, get_reserved_function_return_datatype,
                                                               get_reserved_function_parms_datatypes,
                                                               DF_COL, DF_COL_NUM, DF_COL_NUM_NUM, DF_NUM_NUM)

"""
#--------------------------------------------------------------------------
#   column transform task bar
#--------------------------------------------------------------------------
"""
columns_transform_tb_doc_title              =   "DataFrame Columns Options"
columns_transform_tb_title                  =   "DataFrame Columns Options"
columns_transform_tb_id                     =   "columnstransformoptionstb"

columns_transform_tb_keyTitleList           =   ["Rename</br> Column",
                                                 "Add</br>Column",
                                                 "Drop</br>Column",
                                                 "Reorder</br>Columns",
                                                 "Save</br> Column",
                                                 "Copy</br>Column",
                                                 "More",
                                                 "Return","Help"]

columns_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_SAVE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.MORE_TASKBAR)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ID) + "')"]

columns_transform_tb_centered               =   True


columns_transform_tb1_doc_title             =   "DataFrame Columns Options"
columns_transform_tb1_title                 =   "DataFrame Columns Options"
columns_transform_tb1_id                    =   "columnstransformoptionstb1"

columns_transform_tb1_keyTitleList          =   ["Apply</br>fn To</br>Column",
                                                 "Map</br>Column",
                                                 "Dummies</br>For</br>Column",
                                                 "Make</br> Column</br>Categorical",
                                                 "Change</br> Column</br>Datatype",
                                                 "Return","Help"]

columns_transform_tb1_jsList                =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_APPLY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_MAP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DUMMIES_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_CAT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DATATYPE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ID) + "')"]

columns_transform_tb1_centered              =   True


columns_transform_tbA_doc_title             =   "DataFrame Columns Options"
columns_transform_tbA_title                 =   "DataFrame Columns Options"
columns_transform_tbA_id                    =   "columnstransformoptionstbA"

columns_transform_tbA_keyTitleList          =   ["Rename</br> Column",
                                                 "Add</br>Column",
                                                 "Drop</br>Column",
                                                 "Reorder</br>Columns",
                                                 "Save</br> Column"]

columns_transform_tbA_jsList                =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_SAVE_COLUMN)+")"]

columns_transform_tbA_centered              =   True

columns_transform_tbB_doc_title             =   "DataFrame Columns Options"
columns_transform_tbB_title                 =   "DataFrame Columns Options"
columns_transform_tbB_id                    =   "columnstransformoptionstbB"

columns_transform_tbB_keyTitleList          =   ["Copy</br>Column",
                                                 "Apply</br>fn To</br>Column",
                                                  "Map</br> Column",
                                                  "Dummies</br>For</br>Column"]

columns_transform_tbB_jsList                =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_APPLY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_MAP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DUMMIES_COLUMN)+")"]

columns_transform_tbB_centered              =   True

columns_transform_tbC_doc_title             =   "DataFrame Columns Options"
columns_transform_tbC_title                 =   "DataFrame Columns Options"
columns_transform_tbC_id                    =   "columnstransformoptionstbC"

columns_transform_tbC_keyTitleList          =   ["Make</br> Column</br>Categorical",
                                                 "Change</br> Column</br>Datatype",
                                                 "Return","Help"]

columns_transform_tbC_jsList                =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_CAT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DATATYPE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_COLS_MDC_ID) + "')"]

columns_transform_tbC_centered              =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    add new column data
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

ADD_COLUMN_RETURN           =   4


"""
#--------------------------------------------------------------------------
#    add new column
#--------------------------------------------------------------------------
"""
add_column_input_title                  =   "Add Column"
add_column_input_id                     =   "addcolInput"
add_column_input_idList                 =   ["addColumnName",
                                             "addColumnNamedf",
                                             "addColumnDataType",
                                             None,None,None,None]

add_column_input_labelList              =   ["new_column_name",
                                             "new_column_name_df",
                                             "new_column_data_type",
                                             "Get</br>Column</br>Values</br>From File",
                                             "Get</br>Column</br>Values</br>From Code",
                                             "Get</br>Column</br>Values</br>From df",
                                             "Return"]

add_column_input_typeList               =   ["text","select","select","button","button","button","button"]

add_column_input_placeholderList        =   ["enter the new column name",
                                             "enter the new column name df",
                                             "enter the new column data type",
                                             None,None,None,None]

add_column_input_jsList                 =    [None,None,None,
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_FILE_OPTION) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_DFC_FUNCS) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_DF_OPTION) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")"]

add_column_input_reqList                =   [0,1,2]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    add new column - from files
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    add new column - file input
#--------------------------------------------------------------------------
"""
add_column_file_input_title              =   "Add Column"
add_column_file_input_id                 =   "addcolfileInput"
add_column_file_input_idList             =   ["addfcolumnname",
                                              "addcolumnNamedf",
                                              "addfcolumndtype",
                                              "addcolumnfilename",
                                              "nafillvalue",
                                              None,None,None]

add_column_file_input_labelList          =   ["new_column_name",
                                              "new_column_name_df",
                                              "new_column_data_type",
                                              "column_values_file_name",
                                              "na_fill_value",
                                              "Add New</br>Column</br>From File",
                                              "Return","Help"]

add_column_file_input_typeList           =   ["text","select","select","file","text",
                                              "button","button","button"]

add_column_file_input_placeholderList    =   ["enter the new column name",
                                              "enter the new column name df",
                                              "enter the new column data type",
                                              "enter the file name of list to use as values",
                                              "na fill value (default : no value retain nas)",
                                              None,None,None]

add_column_file_input_jsList             =    [None,None,None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_FILE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_FILE_ID) + "')"]

add_column_file_input_reqList            =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    add new column - index file input
#--------------------------------------------------------------------------
"""

add_colind_file_input_title              =   "Add Column"
add_colind_file_input_id                 =   "addidxcolfileInput"
add_colind_file_input_idList             =   ["addfcolumnname",
                                              "addColumnNamedf",
                                              "addfcolumndtype",
                                              "addcolumnfilename",
                                              "nafillvalue",
                                              "indexmap",
                                              None,None,None]

add_colind_file_input_labelList          =   ["new_column_name",
                                              "new_column_name_df",
                                              "new_column_data_type",
                                              "column_values_file_name",
                                              "index_mapping",
                                              "na_fill_value",
                                              "Add New</br>Column</br>From File",
                                              "Return","Help"]

add_colind_file_input_typeList           =   ["text","select","select","file","text",maketextarea(4),
                                              "button","button","button"]

add_colind_file_input_placeholderList    =   ["enter the new column name",
                                              "enter the new column name df",
                                              "enter the new column data type",
                                              "enter the file name of list to use as values",
                                              "na fill value (default : no value retain nas)",
                                              "map file index to df index",
                                              None,None,None]

add_colind_file_input_jsList             =    [None,None,None,None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_FILE_WITH_INDEX_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_FILE_ID) + "')"]

add_colind_file_input_reqList            =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    add new column - from dfx funcs
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs default no dfc selected
#--------------------------------------------------------------------------
"""
add_column_code_dfc_funcs_input_title           =   "Add Column"
add_column_code_dfc_funcs_input_id              =   "addcoldfcfuncInput"
add_column_code_dfc_funcs_input_idList          =   ["addcolname",
                                                     "addcolnamedf",
                                                     "addcoldtype",
                                                     "addcolfuncs",
                                                     "addcolcodefcode",
                                                     "addcoldesc",
                                                     None,None,None,None]

add_column_code_dfc_funcs_input_labelList       =   ["new_column_name",
                                                     "new_column_name_df",
                                                     "new_column_data_type",
                                                     "dfc_function",
                                                     "dfc_function_code",
                                                     "dfc_function_description"]
                                                     
add_column_code_dfc_funcs_input_labelListA      =   ["Add New</br>Column</br>from</br>dfc fns",
                                                     "Add New</br>Column</br>from</br>User Code",
                                                     "Return","Help"]

add_column_code_dfc_funcs_input_typeList        =   ["text","select","select","select",
                                                     maketextarea(5),maketextarea(5)]
                                                     
add_column_code_dfc_funcs_input_typeListA       =   ["button","button","button","button"]

add_column_code_dfc_funcs_input_placeholderList =   ["enter the new column name",
                                                     "enter the new column name df",
                                                     "enter the column data type",
                                                     "generic function",
                                                     "function code",
                                                     "function description"]
                                                     
add_column_code_dfc_funcs_input_placeholderListA =   [None,None,None,None]

add_column_code_dfc_funcs_input_jsList          =    [None,None,None,None,None,None]
                                                      
add_column_code_dfc_funcs_input_jsListA         =    ["data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_DFC_FUNCS) + ")",
                                                      "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_CODE_OPTION) + ")",
                                                      "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                                      "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_DFC_ID) + "')"]

add_column_code_dfc_funcs_input_reqList         =   [0,1,2,3]





"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs DF_COL type
#--------------------------------------------------------------------------
""" 
add_column_code_dfc_funcs_DF_COL_parms_input_id              =   "addcoldfcdfcolInput"
add_column_code_dfc_funcs_DF_COL_parms_input_idList          =   ["addcolname",
                                                                  "addcolnamedf",
                                                                  "addcoldtype",
                                                                  "addcolfuncsdfcol",
                                                                  "addcolcodefcode",
                                                                  "addcoldesc",
                                                                  "addcoldftitledfcol",
                                                                  "addcoldfcoldfcol",
                                                                  None,None,None,None]

"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs DF_COL_NUM type
#--------------------------------------------------------------------------
""" 
add_column_code_dfc_funcs_DF_COL_NUM_parms_input_id              =   "addcoldfcdfcolnumInput"
add_column_code_dfc_funcs_DF_COL_NUM_parms_input_idList          =   ["addcolname",
                                                                      "addcolnamedf",
                                                                      "addcoldtype",
                                                                      "addcolfuncsdfcolnum",
                                                                      "addcolcodefcode",
                                                                      "addcoldesc",
                                                                      "addcoldftitledfcolnum",
                                                                      "addcoldfcoldfcolnum",
                                                                      "addcoldfnparm",
                                                                      None,None,None,None]

"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs DF_COL_NUM_NUM type
#--------------------------------------------------------------------------
""" 
add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_id              =   "addcoldfcdfcolnumnumInput"
add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_idList          =   ["addcolname",
                                                                          "addcolnamedf",
                                                                          "addcoldtype",
                                                                          "addcolfuncsdfcolnumnum",
                                                                          "addcolcodefcode",
                                                                          "addcoldesc",
                                                                          "addcoldftitledfcolnumnum",
                                                                          "addcoldfcoldfcolnumnum",
                                                                          "addcoldfcolnum",
                                                                          "addcoldfcolnum1",
                                                                          None,None,None,None]

"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs DF_NUM_NUM type
#--------------------------------------------------------------------------
""" 
add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_id              =   "addcoldfcdfnumnumInput"
add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_idList          =   ["addcolname",
                                                                      "addcolnamedf",
                                                                      "addcoldtype",
                                                                      "addcolfuncsdfnumnum",
                                                                      "addcolcodefcode",
                                                                      "addcoldesc",
                                                                      "addcoldfnumnum",
                                                                      "addcoldfcolnum",
                                                                      "addcoldfcolnum1",
                                                                      None,None,None,None]

"""
#--------------------------------------------------------------------------
#    add new column - user code funcs
#--------------------------------------------------------------------------
"""

add_column_code_user_fns_input_title           =   "Add Column"
add_column_code_user_fns_input_id              =   "addcolcodefnInput"
add_column_code_user_fns_input_idList          =   ["addcolumncame",
                                                    "addcolumncamedf",
                                                    "addcolumndtype",
                                                    "addColumnftitle",
                                                    "addcolmodule",
                                                    "addcolname",
                                                    "addcolcodefcode",
                                                    None,None,None,None,None,None]

add_column_code_user_fns_input_labelList       =   ["new_column_name",
                                                    "new_column_name_df",
                                                    "new_column_data_type",
                                                    "user_function",
                                                    "user_function_module",
                                                    "user_function_name",
                                                    "user_function_code",
                                                    "Add New</br>Column</br>from</br>User Code",
                                                    "Add New</br>Column</br>from</br>dfc fns",
                                                    "Save As</br>User</br>Defined</br>Function",
                                                    "Maintain</br>User</br>Defined</br>Functions",
                                                    "Return","Help"]

add_column_code_user_fns_input_typeList        =   ["text","select","select","select","text","text",maketextarea(10),
                                                    "button","button","button","button","button","button"]

add_column_code_user_fns_input_placeholderList =   ["enter the new column name",
                                                    "enter the new column name df",
                                                    "enter the column data type",
                                                    "user function",
                                                    "function module",
                                                    "function name",
                                                    "function code",
                                                    None,None,None,None,None,None]

add_column_code_user_fns_input_jsList          =    [None,None,None,None,None,None,None,
                                                     "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_CODE_OPTION) + ")",
                                                     "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_DFC_FUNCS) + ")",
                                                     "data_transform_add_cols_callback(" + str(dtm.PROCESS_SAVE_USER_FUNC) + ")",
                                                     "data_transform_add_cols_callback(" + str(dtm.DISPLAY_MAINTAIN_USER_FUNC) + ")",
                                                     "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                                     "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + "')"]

add_column_code_user_fns_input_reqList         =   [0,1,2,3,4,5,6]


"""
#--------------------------------------------------------------------------
#    maintain user code funcs
#--------------------------------------------------------------------------
"""

maintain_user_fns_input_title                   =   "Maintain User Fns"
maintain_user_fns_input_id                      =   "maintainuserfnsInput"
maintain_user_fns_input_idList                  =   ["userfnsftitle",
                                                    "userfntitle",
                                                    "userfnsmodule",
                                                    "userfnscode",
                                                    None,None,None,None]

maintain_user_fns_input_labelList               =   ["user_function",
                                                     "user_function_title",
                                                    "user_function_module",
                                                    "user_function_code",
                                                    "Save</br>Updated</br>User fn",
                                                    "Delete</br>Current</br>User fn",
                                                    "Return","Help"]

maintain_user_fns_input_typeList                =   ["select","text","text",maketextarea(15),
                                                    "button","button","button","button"]

maintain_user_fns_input_placeholderList         =   ["user function",
                                                    "function title",
                                                    "function module",
                                                    "function code",
                                                    None,None,None,None]

maintain_user_fns_input_jsList                  =    [None,None,None,None,
                                                     "data_transform_add_cols_callback(" + str(dtm.PROCESS_SAVE_USER_FUNC) + ")",
                                                     "data_transform_add_cols_callback(" + str(dtm.PROCESS_DELETE_USER_FUNC) + ")",
                                                     "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                                     "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + "')"]

maintain_user_fns_input_reqList                 =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    add new column - df
#--------------------------------------------------------------------------
"""

add_column_source_df_input_title               =   "Add Column"
add_column_source_df_input_id                  =   "addcoldfSourceInput"
add_column_source_df_input_idList              =   ["addcolsourcedftitle",
                                                    "addcolsourcecolname",
                                                    "addcolsourceindex",
                                                    None]

add_column_source_df_input_labelList           =   ["source_dataframe_title",
                                                    "source_column_name_to_retrieve",
                                                    "source_index_column_name(s)",
                                                    "Clear"]

add_column_source_df_input_typeList            =   ["select","select","select","button"]

add_column_source_df_input_placeholderList     =   ["enter the source dataframe title",
                                                    "enter the source column name",
                                                    "enter the source index column name",
                                                    None]

add_column_source_df_input_jsList              =   [None,None,None,
                                                    "data_transform_add_cols_callback(" + str(dtm.CLEAR_SOURCE_PARMS) + ")"]

add_column_source_df_input_reqList             =   [0,1,2]


add_column_output_df_input_title               =   "Add Column"
add_column_output_df_input_id                  =   "addcoldfOutputInput"
add_column_output_df_input_idList              =   ["addcoloutputdftitle",
                                                    "addcoloutputcolname",
                                                    "addcoloutputdftype",
                                                    "addcoloutputindex",
                                                    None]

add_column_output_df_input_labelList           =   ["output_dataframe_title",
                                                    "output_new_column_name",
                                                    "output_new_column_datatype",
                                                    "soutput_index_column_name(s)",
                                                   "Clear"]

add_column_output_df_input_typeList            =   ["select","text","select","select","button"]

add_column_output_df_input_placeholderList     =   ["enter the output dataframe title",
                                                    "enter the new column name",
                                                    "enter the new column datatype",
                                                    "enter the output index column name",
                                                    None]

add_column_output_df_input_jsList              =   [None,None,None,None,
                                                    "data_transform_add_cols_callback(" + str(dtm.CLEAR_OUTPUT_PARMS) + ")"]

add_column_output_df_input_reqList             =   [0,1,2,3]






add_column_df_input_title               =   "Add Column"
add_column_df_input_id                  =   "addcoldfInput"
add_column_df_input_idList              =   ["addcoldfsourceindexlist",
                                             "addcoldfoutputindexlist",
                                             "addcolddfbafill",
                                             None,None,None,None]

add_column_df_input_labelList           =   ["source_dataframe_index_list",
                                             "output_dataframe_index_list",
                                             "na_fill_value",
                                             "Add New</br>Column</br>From df",
                                             "Clear","Return","Help"]

add_column_df_input_typeList            =   ["text","text","text",
                                             "button","button","button","button"]

add_column_df_input_placeholderList     =   ["[]",
                                             "[]",
                                             "enter the na fill value",
                                             None,None,None,None]

add_column_df_input_jsList              =    [None,None,None,
                                              "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_DF_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                              "displayhelp('" + str(dfchelp.TRANSFORM_COLS_ADD_DF_ID) + "')"]

add_column_df_input_reqList             =   [0,1,2]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    transform columns display objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#    rename column input for single column
#--------------------------------------------------------------------------
"""
rename_column_input_title               =   "Column Renaming"
rename_column_input_id                  =   "renamecolInput"
rename_column_input_idList              =   ["renamecolumnname",
                                             "renameoldColumnName",
                                             None,None,None]

rename_column_input_labelList           =   ["new_column_name",
                                             "column_to_rename",
                                             "Rename</br> Column",
                                             "Return","Help"]

rename_column_input_typeList            =   ["text","select",
                                             "button","button","button"]

rename_column_input_placeholderList     =   ["enter the new column name",
                                             "column name",
                                             None,None,None]

rename_column_input_jsList              =   [None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_RENAME_COLUMN)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "display_help_url('" + dfchelp.TRANSFORM_COLS_RENAME_COL_ID + "')"]

rename_column_input_reqList             =   [0,1]




"""
#--------------------------------------------------------------------------
#    drop column
#--------------------------------------------------------------------------
"""
drop_column_input_title                 =   "Drop Column"
drop_column_input_id                    =   "dropcolInput"
drop_column_input_idList                =   ["dropcolInputname",
                                             "dropsavedroppedflag",
                                             "dropColumnfname",
                                             "dropColumnfdir",
                                             "dropColumnftype",
                                             None,None,None]

drop_column_input_labelList             =   ["column(s)_to_drop",
                                             "save_col(s)_to_drop",
                                             "col(s)_to_drop_save_file(s)_name",
                                             "col(s)_to_drop_save_dir",
                                             "col(s)_to_drop_save_file(s)_type",
                                             "Drop</br> Column(s)",
                                             "Return","Help"]

drop_column_input_typeList              =   ["selectmultiple","select","text","text","select",
                                             "button","button","button"]

drop_column_input_placeholderList       =   ["drop column name",
                                             "save column(s) to drop",
                                             "file names for drop columns list",
                                             "enter File dir to save dropped column (default Notebook path)",
                                             "enter File save type (default : json)",
                                             None,None,None]

drop_column_input_jsList                =    [None,None,None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_DROP_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "display_help_url('" + dfchelp.TRANSFORM_COLS_DROP_COL_ID + "')"]

drop_column_input_reqList               =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#    save column
#--------------------------------------------------------------------------
"""
save_column_input_title                 =   "Save Column"
save_column_input_id                    =   "savecolInput"
save_column_input_idList                =   ["savecolnames",
                                             "savecolnameslist",
                                             "savefilename",
                                             "savefiletype",
                                             None,None,None]

save_column_input_labelList             =   ["column(s)_to_save",
                                             "column_names_list",
                                             "save_column(s)_file_name",
                                             "save_column(s)_file_type",
                                             "Save</br> Column(s)",
                                             "Return","Help"]

save_column_input_typeList              =   ["text","select","text","select",
                                             "button","button","button"]

save_column_input_placeholderList       =   ["column(s) to save",
                                             "column names)",
                                             "File name to save columns to",
                                             "enter File save type (default : json)",
                                             None,None,None]

save_column_input_jsList                =    [None,None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_SAVE_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "displayhelp('" + str(dfchelp.TRANSFORM_COLS_SAVE_ID) + "')"]

save_column_input_reqList               =   [0,1,2,3]





save_colind_input_title                 =   "Save Column"
save_colind_input_id                    =   "savecolindxInput"
save_colind_input_idList                =   ["savecolindxnames",
                                             "savecolindxnameslist",
                                             "saveindxfilename",
                                             "saveindxfiletype",
                                             "saveColindxflag",
                                             None,None,None]

save_colind_input_labelList             =   ["column(s)_to_save",
                                             "column_names_list",
                                             "save_column(s)_file_name",
                                             "save_column(s)_file_type",
                                             "save_index_flag",
                                             "Save</br> Column(s)",
                                             "Return","Help"]

save_colind_input_typeList              =   ["text","select","text","select","select",
                                             "button","button","button"]

save_colind_input_placeholderList       =   ["column(s) to save",
                                             "column names)",
                                             "File name to save columns to",
                                             "enter File save type (default : json)",
                                             "save with index",
                                             None,None,None]

save_colind_input_jsList                =    [None,None,None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_SAVE_COLUMN_WITH_INDEX)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "displayhelp('" + str(dfchelp.TRANSFORM_COLS_SAVE_ID) + "')"]

save_colind_input_reqList               =   [0,1,2,3,4]



"""
#--------------------------------------------------------------------------
#    reorder columns
#--------------------------------------------------------------------------
"""
reorder_columns_input_title              =   "Reorder Column"
reorder_columns_input_id                 =   "reordercolInput"
reorder_columns_input_idList             =   ["moveColumnname",
                                              "moveColumnnameslist",
                                              "moveafterColumnname",
                                              "movetoColumnnameslist",
                                              None,None,None]

reorder_columns_input_labelList          =   ["column_to_move",
                                              "column_to_move_column_names_list",
                                              "column_to_move_after",
                                              "column_to_move_after_column_names_list",
                                              "Move</br> Column",
                                              "Return","Help"]

reorder_columns_input_typeList           =   ["text","select","text","select",
                                              "button","button","button"]

reorder_columns_input_placeholderList    =   ["column to move",
                                              "column name list",
                                              "column to move after", 
                                              "column name list",
                                              None,None,None]

reorder_columns_input_jsList             =    [None,None,None,None,
                                               "data_transform_process_cols_callback("+str(dtm.PROCESS_REORDER_COLUMNS)+")",
                                               "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                               "displayhelp('" + str(dfchelp.TRANSFORM_COLS_REORDER_ID) + "')"]

reorder_columns_input_reqList            =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    copy columns
#--------------------------------------------------------------------------
"""
copy_columns_input_title                =   "Copy Column"
copy_columns_input_id                   =   "copycolInput"
copy_columns_input_idList               =   ["copyfromColumnname",
                                             "copyColumnname",
                                             "newcolumnname",
                                             None,None,None]

copy_columns_input_labelList            =   ["column_to_copy_from",
                                             "column_to_copy_to",
                                             "new_column_name_to_copy_to",
                                             "Copy</br>Column",
                                             "Return","Help"]

copy_columns_input_typeList             =   ["select","select","text",
                                             "button","button","button"]

copy_columns_input_placeholderList      =   ["column to copy",
                                             "column to copy to",
                                             "new column to copy to",
                                             None,None,None]

copy_columns_input_jsList               =    [None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_COPY_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "displayhelp('" + str(dfchelp.TRANSFORM_COLS_COPY_ID) + "')"]

copy_columns_input_reqList              =   [0,1,2]



"""
#--------------------------------------------------------------------------
#    apply lambda fn column
#--------------------------------------------------------------------------
"""
apply_column_lambda_input_title              =   "Apply dfc fn To Column"
apply_column_lambda_input_id                 =   "applyldfccolInput"
apply_column_lambda_input_idList             =   ["currentdf",
                                                  "applycolname",
                                                  "fnlfnsel",
                                                  "fntoapply",
                                                  None,None,None,None,None,None]

apply_column_lambda_input_labelList          =   ["dataframe_to_apply_fn_to",
                                                  "column_to_apply_fn_to",
                                                  "dfc_fns",
                                                  "dfc_fn_code",
                                                  "Show</br>Uniques",
                                                  "Define</br>User</br>Function",
                                                  "Apply</br>dfc fn</br>To</br>Column",
                                                  "Clear","Return","Help"]

apply_column_lambda_input_typeList           =   ["select","select","select",maketextarea(2),
                                                  "button","button","button","button","button","button"]

apply_column_lambda_input_placeholderList    =   ["dataframe to apply fn to",
                                                  "column to apply fn to",
                                                  "dfc function",
                                                  "function code",
                                                  None,None,None,None,None,None]

apply_column_lambda_input_jsList             =    [None,None,None,None,
                                                   "data_transform_process_cols_callback("+str(dtm.DISPLAY_APPLY_COLUMN_UNIQUES)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.DISPLAY_APPLY_USER_FN_COLUMN)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.PROCESS_APPLY_COLUMN)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.DISPLAY_CLEAR_COLUMN)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                                   "displayhelp('" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + "')"]

apply_column_lambda_input_reqList            =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    apply fn with gf to column
#--------------------------------------------------------------------------
"""

apply_column_gf_input_title              =   "Apply fn To Column"
apply_column_gf_input_id                 =   "applyfncolInput"
apply_column_gf_input_idList             =   ["currentdf",
                                              "applyfncolname",
                                              "fntoapply",
                                              None,None,None,None,None,None]

apply_column_gf_input_labelList          =   ["dataframe_to_apply_fn_to",
                                              "column_to_apply_fn_to",
                                              "user_function",
                                              "Show</br>Uniques",
                                              "Select</br>dfc fn</br>To</br>Apply",
                                              "Apply</br>User fn</br>To</br>Column",
                                              "Clear","Return","Help"]

apply_column_gf_input_typeList           =   ["select","select",maketextarea(10),
                                              "button","button","button","button","button","button"]

apply_column_gf_input_placeholderList    =   ["dataframe to apply fn to",
                                              "column to apply fn to",
                                              "function to apply",
                                              None,None,None,None,None,None]

apply_column_gf_input_jsList             =    [None,None,None,
                                               "data_transform_process_cols_callback(" + str(dtm.DISPLAY_APPLY_USER_FN_COLUMN_UNIQUES) + ")",
                                               "data_transform_process_cols_callback(" + str(dtm.DISPLAY_APPLY_COLUMN) + ")",
                                               "data_transform_process_cols_callback(" + str(dtm.PROCESS_APPLY_USER_FN_COLUMN) + ")",
                                               "data_transform_process_cols_callback(" + str(dtm.DISPLAY_CLEAR_COLUMN)+")",
                                               "data_transform_process_cols_callback(" + str(dtm.RETURN_CLEAR_COLUMN)+")",
                                               "displayhelp('" + str(dfchelp.TRANSFORM_COLS_APPLY_USER_FN_ID) + "')"]

apply_column_gf_input_reqList            =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    data transform map input for single column
#--------------------------------------------------------------------------
"""
transform_map_input_title               =   "Column Mapping"
transform_map_input_id                  =   "maptransformInput"
transform_map_input_idList              =   ["mapcolumnname",
                                             "mapkeys",
                                             "mapvals",
                                             "mapfn",
                                             "mapfilename",
                                             "mapvalsdt",
                                             "handlena",
                                             None,None,None,None,None]

transform_map_input_labelList           =   ["mapping_column_name",
                                             "mapping_keys",
                                             "mapping_values",
                                             "mapping_values_function",
                                             "mapping_values_list_file_name",
                                             "mapping_values_datatype",
                                             "handle_nan",
                                             "Map</br>Column</br>from</br>File",
                                             "Map</br>Column</br>from</br>Values",
                                             "Map</br>Column</br>from</br>Function",
                                             "Return","Help"]

transform_map_input_typeList            =   ["select",maketextarea(8),maketextarea(8),
                                             maketextarea(8),"file","select","select",
                                             "button","button","button","button","button"]

transform_map_input_placeholderList     = ["column to map",
                                           "mapping keys",
                                           "enter mapping values (comma separated)",
                                           "mapping function to generate mapping values.\nUse list object mapkeys as sorted column uniques.\nReturn values in mapvals list object.",
                                           "enter File name containing mapping or browse to file below",
                                           "mapping values datatype",
                                           "ignore Nans (default = True)",
                                           None,None,None,None,None]

transform_map_input_jsList              = [None,None,None,None,None,None,None,
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN)+")",
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN_VALUES)+")",
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN_FUNCTION)+")",
                                           "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                           "displayhelp('" + str(dfchelp.TRANSFORM_COLS_MAP_ID) + "')"]

transform_map_input_reqList             =   [0,1,2,3,4,5,6]

"""
#--------------------------------------------------------------------------
#    data transform dummy input 
#--------------------------------------------------------------------------
"""
transform_dummy_input_title             =   "Column Dummies"
transform_dummy_input_id                =   "dummytransformInput"
transform_dummy_input_idList            =   ["dummycol",
                                             "removecol",
                                             None,None,None]

transform_dummy_input_labelList         =   ["column_set_dummies_for",
                                             "remove_original_column",
                                             "Make </br>Dummies</br> for Column",
                                             "Return","Help"]

transform_dummy_input_typeList          =   ["select","select","button","button","button"]

transform_dummy_input_placeholderList   =   ["column to set dummies for",
                                             "remove original column (default = True)",
                                             None,None,None]
 
transform_dummy_input_jsList            =   [None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_DUMMIES_COLUMN)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DUMMY_ID) + "')"]

transform_dummy_input_reqList           =   [0,1]

"""
#--------------------------------------------------------------------------
#    data transform category input 
#--------------------------------------------------------------------------
"""
transform_category_input_title          =   "Column Category"
transform_category_input_id             =   "categorytransformInput"
transform_category_input_idList         =   ["catcolumnname",
                                             "catcolumnnameordered",
                                             "catcolumncompleteuniques",
                                             None,None,None]

transform_category_input_labelList      =   ["categorical_column_name",
                                             "categorical_column_ordered",
                                             "categorical_column_categories_all_uniques",
                                             "Make</br>Column</br>Categorical",
                                             "Return","Help"]

transform_category_input_typeList       =   ["select","select","select","button","button","button"]

transform_category_input_placeholderList =  ["column to make categorical",
                                             "oredered categorical (default = False)",
                                             "all uniques as categories (default = True)",
                                             None,None,None]

transform_category_input_jsList         =   [None,None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_CAT_COLUMN)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_COLS_CAT_ID) + "')"]

transform_category_input_reqList        =   [0,1,2]


transform_cat_exclude_input_title       =   "Column Category"
transform_cat_exclude_input_id          =   "categorytransformexcludeInput"
transform_cat_exclude_input_idList      =   ["catexcludecolumnname",
                                             "catexcludecolumnnameordered",
                                             "excludeuniques",
                                             None,None,None]

transform_cat_exclude_input_labelList   =   ["categorical_column_name",
                                             "categorical_column_ordered",
                                             "uniques_excluded_from_categories",
                                             "Make</br>Column</br>Categorical",
                                             "Return","Help"]

transform_cat_exclude_input_typeList    =   ["select","select",maketextarea(5),"button","button","button"]

transform_cat_exclude_input_placeholderList =  ["column to make categorical",
                                                "oredered categorical (default = False)",
                                                "uniques to exclude as categories (default = None)",
                                                None,None,None]

transform_cat_exclude_input_jsList      =   [None,None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_CAT_COLUMN_EXCLUDE)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_COLS_CAT_ID) + "')"]

transform_cat_exclude_input_reqList     =   [0,1,2]

"""
#--------------------------------------------------------------------------
#   datatype no nons 
#--------------------------------------------------------------------------
"""
dt_data_type_input_title                =   "Change Data Type"
dt_data_type_input_id                   =   "dtdatatypeinput"
dt_data_type_input_idList               =   ["dtcolname",
                                             "dtdatatype",
                                             None,None,None,None,None]

dt_data_type_input_labelList            =   ["column_to_change_datatype",
                                             "datatype",
                                             "Show</br>Uniques",
                                             "Check</br>DataType</br>Compat",
                                             "Change</br>DataType",
                                             "Return","Help"]

dt_data_type_input_typeList             =   ["select","select","button","button","button","button","button"]

dt_data_type_input_placeholderList      =   ["column name",
                                             "datatype selected",
                                             None,None,None,None,None]

dt_data_type_input_jsList               =   [None,None,
                                             "process_transform_datatype_callback(" + str(dtm.NO_NA_OPTION) + ",0)",
                                             "process_transform_datatype_callback(" + str(dtm.NO_NA_OPTION) + ",1)",
                                             "process_transform_datatype_callback(" + str(dtm.NO_NA_OPTION) + ",2)",
                                             "process_transform_datatype_callback(" + str(dtm.NO_NA_OPTION) + ",3)",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + "')"]

dt_data_type_input_reqList              =   [0,1]


"""
#--------------------------------------------------------------------------
#   datatype nons with fillna 
#--------------------------------------------------------------------------
"""
dt_nans_data_type_input_title           =   "Change Data Type"
dt_nans_data_type_input_id              =   "dtfndatatypeinput"
dt_nans_data_type_input_idList          =   ["dtcolname",
                                             "dtdatatype",
                                             "naoption",
                                             "dtfillnavalue",
                                             "dtfillnamethod",
                                             "dtfillnalimit",
                                             None,None,None,None,None]

dt_nans_data_type_input_labelList       =   ["column_to_change_datatype",
                                             "datatype",
                                             "na_option",
                                             "fillna_value",
                                             "fillna_method",
                                             "fillna_threshold",
                                             "Show</br>Uniques",
                                             "Check</br>DataType</br>Compat",
                                             "Change</br>DataType",
                                             "Return","Help"]

dt_nans_data_type_input_typeList        =   ["select","select","select","text","select","text","button","button","button","button","button"]

dt_nans_data_type_input_placeholderList =   ["column name",
                                             "datatype selected",
                                             "na option",
                                             "fillna value",
                                             "fillna method",
                                             "limit (default = None)",
                                             None,None,None,None,None]

dt_nans_data_type_input_jsList          =   [None,None,None,None,None,None,
                                             "process_transform_datatype_callback(" + str(dtm.FILL_NA_OPTION) + ",0)",
                                             "process_transform_datatype_callback(" + str(dtm.FILL_NA_OPTION) + ",1)",
                                             "process_transform_datatype_callback(" + str(dtm.FILL_NA_OPTION) + ",2)",
                                             "process_transform_datatype_callback(" + str(dtm.FILL_NA_OPTION) + ",3)",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + "')"]

dt_nans_data_type_input_reqList         =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#   datatype nons with dropna 
#--------------------------------------------------------------------------
"""
dt_drop_nans_data_type_input_title           =   "Change Data Type"
dt_drop_nans_data_type_input_id              =   "dtdndatatypeinput"
dt_drop_nans_data_type_input_idList          =   ["dtcolname",
                                                  "dtdatatype",
                                                  "naoption",
                                                  "dtanyall",
                                                  "dtthreshold",
                                                  None,None,None,None,None]

dt_drop_nans_data_type_input_labelList       =   ["column_to_change_datatype",
                                                  "datatype",
                                                  "na_option",
                                                  "dropna_any_or_all",
                                                  "dropna_threshold",
                                                  "Show</br>Uniques",
                                                  "Check</br>DataType</br>Compat",
                                                  "Change</br>DataType",
                                                  "Return","Help"]

dt_drop_nans_data_type_input_typeList        =   ["select","select","select","select","text","button","button","button","button","button"]

dt_drop_nans_data_type_input_placeholderList =   ["column name",
                                                  "datatype selected",
                                                  "na option",
                                                  "drop any or all",
                                                  "dropna threshold (default : None)",
                                                  None,None,None,None,None]

dt_drop_nans_data_type_input_jsList          =   [None,None,None,None,None,
                                                  "process_transform_datatype_callback(" + str(dtm.DROP_NA_OPTION) + ",0)",
                                                  "process_transform_datatype_callback(" + str(dtm.DROP_NA_OPTION) + ",1)",
                                                  "process_transform_datatype_callback(" + str(dtm.DROP_NA_OPTION) + ",2)",
                                                  "process_transform_datatype_callback(" + str(dtm.DROP_NA_OPTION) + ",3)",
                                                  "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + "')"]

dt_drop_nans_data_type_input_reqList         =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   check column datatype compatability 
#--------------------------------------------------------------------------
"""
dt_check_data_type_input_title           =   "Check Column Compatability"
dt_check_data_type_input_id              =   "checkdtinput"
dt_check_data_type_input_idList          =   ["checkdtcolname",
                                              "checkdtdatatypes",
                                              "checkdtdatatypesok",
                                              None,None,None,None]

dt_check_data_type_input_labelList       =   ["column_to_check_datatype_compatability",
                                              "datatypes_to_check_for_compatability",
                                              "compatable_datatypes",
                                              "Show</br>Uniques",
                                              "Check</br>Data Type</br>Compatability",
                                              "Return","Help"]

dt_check_data_type_input_typeList        =   ["select","selectmultiple",maketextarea(4),"button","button","button","button"]

dt_check_data_type_input_placeholderList =   ["column name",
                                              "datatype selected",
                                              "compatable datatypes",
                                              None,None,None,None]

dt_check_data_type_input_jsList          =   [None,None,None,
                                              "process_transform_check_compatability(0)",
                                              "process_transform_check_compatability(1)",
                                              "process_transform_check_compatability(3)",
                                              "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + "')"]

dt_check_data_type_input_reqList         =   [0,1]


"""
#--------------------------------------------------------------------------
#   check column str datatype compatability 
#--------------------------------------------------------------------------
"""
dt_str_check_data_type_input_title           =   "Check Column Compatability"
dt_str_check_data_type_input_id              =   "checkstrdtinput"
dt_str_check_data_type_input_idList          =   ["checkdtcolname",
                                                  "checkdtdatatypes",
                                                  "checkdtdatatypesok",
                                                  "checkdtsmaplesize",
                                                  None,None,None,None]

dt_str_check_data_type_input_labelList       =   ["column_to_check_for_datatype_compatability",
                                                  "datatypes_to_check_for_compatability",
                                                  "compatable_datatypes",
                                                  "sample_size_percent",
                                                  "Show</br>Uniques",
                                                  "Check</br>Data Type</br>Compatability",
                                                  "Return","Help"]

dt_str_check_data_type_input_typeList        =   ["select","selectmultiple",maketextarea(4),"text","button","button","button","button"]

dt_str_check_data_type_input_placeholderList =   ["column name",
                                                  "datatype selected",
                                                  "compatable datatypes",
                                                  "column values sample size (default : 5%)",
                                                  None,None,None,None]

dt_str_check_data_type_input_jsList          =   [None,None,None,None,
                                                  "process_transform_check_compatability(0)",
                                                  "process_transform_check_compatability(2)",
                                                  "process_transform_check_compatability(3)",
                                                  "displayhelp('" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + "')"]

dt_str_check_data_type_input_reqList         =   [0,1]


datatransform_columns_inputs                 =   [add_column_input_id, add_column_file_input_id, add_colind_file_input_id,add_column_code_dfc_funcs_input_id, 
                                                  add_column_code_dfc_funcs_DF_COL_parms_input_id,add_column_code_dfc_funcs_DF_COL_NUM_parms_input_id,
                                                  add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_id,add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_id,
                                                  add_column_code_user_fns_input_id, add_column_source_df_input_id,
                                                  add_column_df_input_id, rename_column_input_id, drop_column_input_id, save_column_input_id,
                                                  save_colind_input_id, reorder_columns_input_id, copy_columns_input_id, apply_column_lambda_input_id,
                                                  apply_column_gf_input_id, transform_map_input_id, transform_dummy_input_id, transform_category_input_id,
                                                  transform_cat_exclude_input_id, dt_data_type_input_id, dt_nans_data_type_input_id, dt_drop_nans_data_type_input_id,
                                                  dt_check_data_type_input_id, dt_str_check_data_type_input_id]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Column transform display components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_base_data_transform_columns_taskbar() :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
    
        from dfcleanser.common.display_utils import display_dfcleanser_taskbar
        display_dfcleanser_taskbar(ButtonGroupForm(columns_transform_tb_id,
                                                   columns_transform_tb_keyTitleList,
                                                   columns_transform_tb_jsList,
                                                   columns_transform_tb_centered))
        
    else :

        transform_tb_A     =   ButtonGroupForm(columns_transform_tbA_id,
                                               columns_transform_tbA_keyTitleList,
                                               columns_transform_tbA_jsList,
                                               columns_transform_tbA_centered)
        
        transform_tb_A.set_gridwidth(480)
        transform_tb_A_html    =   transform_tb_A.get_html()
        
        transform_tb_B     =   ButtonGroupForm(columns_transform_tbB_id,
                                               columns_transform_tbB_keyTitleList,
                                               columns_transform_tbB_jsList,
                                               columns_transform_tbB_centered)
        
        transform_tb_B.set_gridwidth(480)
        transform_tb_B_html    =   transform_tb_B.get_html()
        
        transform_tb_C     =   ButtonGroupForm(columns_transform_tbC_id,
                                               columns_transform_tbC_keyTitleList,
                                               columns_transform_tbC_jsList,
                                               columns_transform_tbC_centered)
        
        transform_tb_C.set_gridwidth(480)
        transform_tb_C_html    =   transform_tb_C.get_html()
        
        gridclasses     =   ["dfc-top-","dfc-main","dfc-footer"]
        gridhtmls       =   [transform_tb_A_html,transform_tb_B_html,transform_tb_C_html]
    
        display_generic_grid("dfcleanser-transform-tb-pop-up-wrapper",gridclasses,gridhtmls)
        

def display_more_transform_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(columns_transform_tb1_id,
                                               columns_transform_tb1_keyTitleList,
                                               columns_transform_tb1_jsList,
                                               True))
    


def get_df_colslist() :
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    colslist    =   df.columns.tolist()
        
    colname     =   cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
    if(colname is None) :
        colname     =   colslist[0]
    else :
        if(not (is_column_in_df(df,colname))) :
            colname     =   colslist[0]
            
    return(df,colslist,colname)

    
def display_dct_form(gridclasses,gridhtmls) :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-transform-480px-3-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-transform-480px-3-vert-wrapper",gridclasses,gridhtmls,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_column_transform_forms(option,parms=None) :
    """
    * -------------------------------------------------------- 
    * function : display grid cols forms
    * 
    * parms :
    *
    *   option - col transform option
    *    
    * returns : display form html
    * --------------------------------------------------------
    """
    
    if(option == dtm.MORE_TASKBAR) :
        display_more_transform_taskbar()
        return()        
    
    display_base_data_transform_columns_taskbar()
    print("\n")

    if(option == dtm.DISPLAY_RENAME_COLUMN) :
        
        common_column_heading_html      =   "<div>Rename Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(rename_column_input_id,
                                                      rename_column_input_idList,
                                                      rename_column_input_labelList,
                                                      rename_column_input_typeList,
                                                      rename_column_input_placeholderList,
                                                      rename_column_input_jsList,
                                                      rename_column_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname, "list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
        
        get_select_defaults(grid_input_form,
                            rename_column_input_id,
                            rename_column_input_idList,
                            rename_column_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html   =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0}) 
        grid_input_form.set_gridwidth(480)
        grid_input_html =   grid_input_form.get_html()

        gridclasses     =   ["dfc-main","dfcleanser-common-grid-header","dfc-bottom"]
        gridhtmls       =   [colstats_html,common_column_heading_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)

    if(option == dtm.DISPLAY_DROP_COLUMN) :
        
        common_column_heading_html      =   "<div>Drop Column(s)</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(drop_column_input_id,
                                                      drop_column_input_idList,
                                                      drop_column_input_labelList,
                                                      drop_column_input_typeList,
                                                      drop_column_input_placeholderList,
                                                      drop_column_input_jsList,
                                                      drop_column_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname, "list" : colslist, "size" : 10, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
        
        sflag           =   {"default" : "False", "list" : ["True","False"]}
        selectDicts.append(sflag)
        
        ftypesel        =   {"default" : "json","list" : ["json","csv"]}
        selectDicts.append(ftypesel)
        
        try :
            get_select_defaults(grid_input_form,
                                drop_column_input_id,
                                drop_column_input_idList,
                                drop_column_input_typeList,
                                selectDicts)
        except :
            print("unable to display drop option screen")
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        
        cfg.set_config_value(drop_column_input_id+"Parms",[colname,"False","",cfg.get_notebookPath(),"json"])
        
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_REORDER_COLUMNS) : 
        
        df,colslist,colname             =   get_df_colslist()
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note("None")
        col_names_html  =   display_column_names(df,col_names_table,None,False)
        
        common_column_heading_html      =   "<div>Reorder Columns</div><br>"
        
        grid_input_form     =   InputForm(reorder_columns_input_id,
                                          reorder_columns_input_idList,
                                          reorder_columns_input_labelList,
                                          reorder_columns_input_typeList,
                                          reorder_columns_input_placeholderList,
                                          reorder_columns_input_jsList,
                                          reorder_columns_input_reqList)
        
        selectDicts     =   []
        
        current_df      =   cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID)
        colnames        =   current_df.columns.tolist()
        cols_name_list  =   [" "]
        
        for i in range(len(colnames)) :
            cols_name_list.append(colnames[i])
            
        cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_reorder_cols"}
        selectDicts.append(cnames)
        
        to_col_names_list   =   ["","Head Of List"]
        for i in range(len(colnames)) :
            to_col_names_list.append(colnames[i])
        
        tocnames        =   {"default":to_col_names_list[0],"list": to_col_names_list, "callback" : "change_reorder_to_cols"}
        selectDicts.append(tocnames)
        
        get_select_defaults(grid_input_form,
                            reorder_columns_input_id,
                            reorder_columns_input_idList,
                            reorder_columns_input_typeList,
                            selectDicts)
        
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":40})
        grid_input_form.set_gridwidth(480)
        grid_input_html   =   grid_input_form.get_html()
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            gridclasses     =   ["main"]
            gridhtmls       =   [col_names_html]
            display_generic_grid("df-reorder-colnames-wrapper",gridclasses,gridhtmls)
            
            print("\n")
            
            gridclasses     =   ["dfcleanser-common-grid-header","main"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
            
        else :
            
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
            gridhtmls       =   [common_column_heading_html,col_names_html,grid_input_html]

            display_dct_form(gridclasses,gridhtmls)
        

    elif(option == dtm.DISPLAY_SAVE_COLUMN) :
        
        common_column_heading_html      =   "<div>Save Column(s)</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        indices = df.index.name
        if(indices is None) :
            index_present   =   False
        else :
            index_present   =   True
            
        if(not (index_present)) :
        
            grid_input_form                 =   InputForm(save_column_input_id,
                                                          save_column_input_idList,
                                                          save_column_input_labelList,
                                                          save_column_input_typeList,
                                                          save_column_input_placeholderList,
                                                          save_column_input_jsList,
                                                          save_column_input_reqList)
            
        else :
            
            grid_input_form                 =   InputForm(save_colind_input_id,
                                                          save_colind_input_idList,
                                                          save_colind_input_labelList,
                                                          save_colind_input_typeList,
                                                          save_colind_input_placeholderList,
                                                          save_colind_input_jsList,
                                                          save_colind_input_reqList)

        selectDicts     =   []
        
        current_df      =   cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID)
        colnames        =   current_df.columns.tolist()
        cols_name_list  =   [" "]
        for i in range(len(colnames)) :
            cols_name_list.append(colnames[i])
        
        if(not (index_present)) :    
            cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_save_cols"}
        else :
            cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_saveindx_cols"}            
        
        selectDicts.append(cnames)

        ftypes          =   {"default" : "json", "list" : ["json","csv","excel"]}
        selectDicts.append(ftypes)
        
        if(index_present) :
            iflags          =   {"default" : "True", "list" : ["True","False"]}
            selectDicts.append(iflags)
        
        if(not(index_present)) :

            cfg.drop_config_value(save_column_input_id+"Parms")
            
            get_select_defaults(grid_input_form,
                                save_column_input_id,
                                save_column_input_idList,
                                save_column_input_typeList,
                                selectDicts)
            
            #fname = colname.replace(" ", "_");
            #fname = fname.replace(".", "_");
            #fname = "'" + fname + "'"

            cfg.set_config_value(save_column_input_id+"Parms",["","","","json"])
            
        else :
            
            cfg.drop_config_value(save_colind_input_id+"Parms")
            
            get_select_defaults(grid_input_form,
                                save_colind_input_id,
                                save_colind_input_idList,
                                save_colind_input_typeList,
                                selectDicts)
            
            cfg.set_config_value(save_colind_input_id+"Parms",[colname,"[]",cfg.get_notebookPath(),"json","True"])
            
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0}) 
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_COPY_COLUMN) :
        
        common_column_heading_html      =   "<div>Copy Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(copy_columns_input_id,
                                                      copy_columns_input_idList,
                                                      copy_columns_input_labelList,
                                                      copy_columns_input_typeList,
                                                      copy_columns_input_placeholderList,
                                                      copy_columns_input_jsList,
                                                      copy_columns_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname,"list" : colslist, "size" : 5}
        selectDicts.append(cnames)
        selectDicts.append(cnames)
        
        get_select_defaults(grid_input_form,
                            copy_columns_input_id,
                            copy_columns_input_idList,
                            copy_columns_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        blank_html       =   ""
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,blank_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)

    elif( (option == dtm.DISPLAY_APPLY_COLUMN) or 
          (option == dtm.DISPLAY_APPLY_USER_FN_COLUMN) or 
          (option == dtm.DISPLAY_APPLY_COLUMN_UNIQUES) or
          (option == dtm.DISPLAY_APPLY_USER_FN_COLUMN_UNIQUES) or 
          (option == dtm.DISPLAY_APPLY_CHANGE_FN) ) :
        
        display_apply_fn_inputs(option,parms)
        
    elif(option == dtm.DISPLAY_MAP_COLUMN) :
        
        common_column_heading_html      =   "<div>Map Column </div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        counts  =   df[colname].value_counts().to_dict()
        uniques =   list(counts.keys())

        if(is_numeric_col(df,colname)) :
            uniques.sort()

        keyslist = ""
            
        for i in range(len(uniques)) :
            keyslist = (keyslist + str(uniques[i])) 
            if(not((i+1) == len(uniques))) :
                keyslist = (keyslist + str(", "))
        
        if(len(keyslist) > 300) :
            parmslist = ["","mapping keys too large to define by hand","","","","",""]
            parmsProtect = [False,True,False,False,False,False,False]
        else :
            parmslist = ["",keyslist,"","","","",""]
            parmsProtect = [False,True,False,False,False,False,False]
        
        cfg.set_config_value(transform_map_input_id+"Parms",parmslist)
        cfg.set_config_value(transform_map_input_id+"ParmsProtect",parmsProtect)

        grid_input_form     =   InputForm(transform_map_input_id,
                                          transform_map_input_idList,
                                          transform_map_input_labelList,
                                          transform_map_input_typeList,
                                          transform_map_input_placeholderList,
                                          transform_map_input_jsList,
                                          transform_map_input_reqList)
    
        selectDicts     =   []
        
        cnames          =   {"default" : colname,"list" : colslist, "size" : 10, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
    
        data_type_str   =   get_dtype_str_for_datatype(df[colname].dtype)

        from dfcleanser.common.common_utils import get_datatypes_list      
        dtypes          =   {"default":data_type_str,"list":get_datatypes_list()}
        selectDicts.append(dtypes)

        mapsel     =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(mapsel)
           
        get_select_defaults(grid_input_form,
                            transform_map_input_id,
                            transform_map_input_idList,
                            transform_map_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html   =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":90, "width":90, "left-margin":1})
        grid_input_form.set_gridwidth(480)
        
        grid_input_html =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_DUMMIES_COLUMN) :
        
        common_column_heading_html      =   "<div>Dummies for Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(transform_dummy_input_id,
                                                      transform_dummy_input_idList,
                                                      transform_dummy_input_labelList,
                                                      transform_dummy_input_typeList,
                                                      transform_dummy_input_placeholderList,
                                                      transform_dummy_input_jsList,
                                                      transform_dummy_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
        
        inplacesel      =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
        get_select_defaults(grid_input_form,
                            transform_dummy_input_id,
                            transform_dummy_input_idList,
                            transform_dummy_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_CAT_COLUMN_EXCLUDE) :
        
        df,colslist,colname             =   get_df_colslist()
        
        if(not (parms is None)) :
            
            if("catexcludecolumnname" in parms[0]) :
                fparms      =   get_parms_for_input(parms,transform_cat_exclude_input_idList)
                colname     =   fparms[0]
                ordered     =   fparms[1]
                exclude     =   "[]"
                
            else :
                fparms      =   get_parms_for_input(parms,transform_category_input_idList)
                colname     =   fparms[0]
                ordered     =   fparms[1]
                exclude     =   "[]"
            
        else :
            ordered     =   "False"
            exclude     =   "[]"
            
        display_uniques_and_find(df,colname,callback="select_exclude_unique",dispfind=False)
        
        print("\n")
        
        from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
        col_stats_html  =   display_col_stats(df,colname,False,True)
         
        common_column_heading_html      =   "<div>Convert Column to category</div><br>"
        
        grid_input_form     =   InputForm(transform_cat_exclude_input_id,
                                          transform_cat_exclude_input_idList,
                                          transform_cat_exclude_input_labelList,
                                          transform_cat_exclude_input_typeList,
                                          transform_cat_exclude_input_placeholderList,
                                          transform_cat_exclude_input_jsList,
                                          transform_cat_exclude_input_reqList)
        
        selectDicts     =   []

        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_category_callback"}
        selectDicts.append(cnames)

        catsel          =   {"default" : ordered,"list" : ["True","False"]}
        selectDicts.append(catsel)
        
        get_select_defaults(grid_input_form,
                            transform_cat_exclude_input_id,
                            transform_cat_exclude_input_idList,
                            transform_cat_exclude_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":100, "left-margin":0}) 
        grid_input_form.set_gridwidth(480)
        
        cfg.set_config_value(transform_cat_exclude_input_id+"Parms",[colname,ordered,exclude])
        grid_input_html     =   grid_input_form.get_html()
        
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
            gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [col_stats_html,common_column_heading_html,grid_input_html]
        
            display_generic_grid("col-change-datatype-dt-wrapper",gridclasses,gridhtmls) 
            
        else :
            gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [col_stats_html,common_column_heading_html,grid_input_html]
        
            display_generic_grid("col-change-datatype-dt-pop-up-wrapper",gridclasses,gridhtmls)
        

    elif(option == dtm.DISPLAY_CAT_COLUMN) :
        
        df,colslist,colname             =   get_df_colslist()
        
        if(not (parms is None)) :
            fparms      =   get_parms_for_input(parms,transform_category_input_idList)
            
            colname     =   fparms[0]
            ordered     =   fparms[1]
            exclude     =   fparms[2]
            
        else :
            ordered     =   "False"
            exclude     =   "True"
        
        display_uniques_and_find(df,colname,callback=None,dispfind=False)
        
        print("\n")
        
        from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
        col_stats_html  =   display_col_stats(df,colname,False,True)
         
        common_column_heading_html      =   "<div>Convert Column to category</div><br>"
        
        grid_input_form     =   InputForm(transform_category_input_id,
                                          transform_category_input_idList,
                                          transform_category_input_labelList,
                                          transform_category_input_typeList,
                                          transform_category_input_placeholderList,
                                          transform_category_input_jsList,
                                          transform_category_input_reqList)
        
        selectDicts     =   []

        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_category_callback"}
        selectDicts.append(cnames)

        catsel          =   {"default" : ordered,"list" : ["True","False"]}
        selectDicts.append(catsel)
        
        catsel          =   {"default" : exclude,"list" : ["True","False"], "callback" : "exclude_uniques_callback"}
        selectDicts.append(catsel)
           
        get_select_defaults(grid_input_form,
                            transform_category_input_id,
                            transform_category_input_idList,
                            transform_category_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":100, "left-margin":0}) 
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
            gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [col_stats_html,common_column_heading_html,grid_input_html]
        
            display_generic_grid("col-change-datatype-dt-wrapper",gridclasses,gridhtmls) 
            
        else :
            gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [col_stats_html,common_column_heading_html,grid_input_html]
        
            display_generic_grid("col-change-datatype-dt-pop-up-wrapper",gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_DATATYPE_COLUMN) :
        
        df,colslist,colname             =   get_df_colslist()
        if(not (parms is None)) :
            colname     =   parms[0]
        
        display_convert_datatype(df,colname,False,False,cfg.DataTransform_ID)
        
    elif(option == dtm.DISPLAY_DATATYPE_CHANGE_NA) :
        
        df,colslist,colname             =   get_df_colslist()

        if(parms[1] == "fillna") :
            display_convert_datatype(df,parms[0],True,False,cfg.DataTransform_ID) 
        else :
            display_convert_datatype(df,parms[0],False,True,cfg.DataTransform_ID) 
        
    elif(option == dtm.DISPLAY_CHECK_COMPATABILITY) :
        
        display_check_compatability(parms,False) 
        
    elif(option == dtm.DISPLAY_CHECK_COMPATABILITY_UNIQUES) :
        
        display_check_compatability(None,True)        
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display apply fn onjects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 
apply_column_lambda_parms_input_id   =   "applylfntocolInput"

apply_fn_idList                      =   []

def get_current_apply_fn_idList() :
    return(apply_fn_idList)
def set_current_apply_fn_idList(idlist) :
    global apply_fn_idList
    apply_fn_idList = idlist


def display_apply_fn_inputs(optionid,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the apply function to column parms
    * 
    * parms :
    *  showuniques  -   show uniques
    *  userfn       -   user function
    *  parms        -   input form parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
 
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import applyfns
    
    opstat  =   opStatus()
    
    if(optionid == dtm.DISPLAY_APPLY_COLUMN) :
        
        if(parms is None) :
        
            fparms          =   None
            dftitle         =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
            colname         =   None
            dfc_fn          =   None
            dfc_code        =   ""
            
        else :
            
            if("applyfncolname" in parms[0]) :
                
                fparms          =   get_parms_for_input(parms,apply_column_gf_input_idList)
                
                dftitle         =   fparms[0]
                colname         =   fparms[1]
                dfc_fn          =   None
                dfc_code        =   ""
                
            else :
            
                fparms          =   get_parms_for_input(parms,apply_column_lambda_input_idList)
            
                dftitle         =   fparms[0]
                colname         =   fparms[1]
                dfc_fn          =   None
                dfc_code        =   ""
        
        showuniques     =   False
        userfn          =   False
        
    elif(optionid == dtm.DISPLAY_APPLY_USER_FN_COLUMN) :
        
        if("applycolname" in parms[0]) :
            
            fparms          =   get_parms_for_input(parms,apply_column_lambda_input_idList)
            
            dftitle         =   fparms[0]
            colname         =   fparms[1]
            dfc_fn          =   None
            dfc_code        =   ""
            
        else :
        
            fparms          =   get_parms_for_input(parms,apply_column_gf_input_idList)
        
            dftitle         =   fparms[0]
            colname         =   fparms[1]
            dfc_fn          =   None
            dfc_code        =   fparms[2]
        
        showuniques     =   False
        userfn          =   True
        
    elif(optionid == dtm.DISPLAY_APPLY_COLUMN_UNIQUES) :
        
        fparms          =   get_parms_for_input(parms,apply_column_lambda_input_idList)
            
        dftitle         =   fparms[0]
        colname         =   fparms[1]
        dfc_fn          =   fparms[2]
        dfc_code        =   fparms[3]
        
        showuniques     =   True
        userfn          =   False
        
    elif(optionid == dtm.DISPLAY_APPLY_USER_FN_COLUMN_UNIQUES) :
        
        fparms          =   get_parms_for_input(parms,apply_column_gf_input_idList)
        
        dftitle         =   fparms[0]
        colname         =   fparms[1]
        dfc_fn          =   None        
        dfc_code        =   fparms[2]
        
        showuniques     =   True
        userfn          =   True
        
    elif(optionid == dtm.DISPLAY_APPLY_CHANGE_FN) :
    
        fparms          =   get_parms_for_input(parms,apply_column_lambda_input_idList)
        
        dftitle         =   fparms[0]
        colname         =   fparms[1]
        dfc_fn          =   fparms[2]        
        dfc_code        =   get_generic_function_desc(dfc_fn)
        
        showuniques     =   False
        userfn          =   False
        
    if(dftitle is None) :
        df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    else :
        df  =   cfg.get_dfc_dataframe_df(dftitle)
    
    colslist    =   df.columns.tolist()
    
    if(colname is None) :
        colname     =   colslist[0]
        
    if(showuniques) :
        from dfcleanser.data_cleansing.data_cleansing_widgets import get_unique_col_html
        get_unique_col_html(df,colname,opstat)
    
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    if(not(userfn)) :
        
        applyfn_input_form = InputForm(apply_column_lambda_input_id,
                                       apply_column_lambda_input_idList,
                                       apply_column_lambda_input_labelList,
                                       apply_column_lambda_input_typeList,
                                       apply_column_lambda_input_placeholderList,
                                       apply_column_lambda_input_jsList,
                                       apply_column_lambda_input_reqList)
        
    else :
        
        applyfn_input_form = InputForm(apply_column_gf_input_id,
                                       apply_column_gf_input_idList,
                                       apply_column_gf_input_labelList,
                                       apply_column_gf_input_typeList,
                                       apply_column_gf_input_placeholderList,
                                       apply_column_gf_input_jsList,
                                       apply_column_gf_input_reqList)
    
    
    selectDicts     =   []
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    dataframes          =   {"default":dftitle,"list":dataframes_loaded, "callback":"change_apply_df_callback"}
    selectDicts.append(dataframes)
        
    cnames          =   {"default":colname,"list": colslist, "callback":"change_apply_col_stats_callback"}
    selectDicts.append(cnames)
        
    if(not(userfn)) :
        
        fns             =   []
        for i in range(len(applyfns)) :
            
            fnretType   =   get_apply_function_return_datatype(applyfns[i])
            

            if(fnretType == "numeric") :
                if(is_numeric_col(df,colname)) :
                    fns.append(applyfns[i]) 
            elif(fnretType == "float") :
                if(is_float_col(df,colname)) :
                    fns.append(applyfns[i]) 
            elif(fnretType == "int") :
                if(is_int_col(df,colname)) :
                    fns.append(applyfns[i]) 
            elif(fnretType == "str") :
                if(is_string_col(df,colname)) :
                    fns.append(applyfns[i]) 
            
        if(dfc_fn is None) :
            dfc_fn  =   fns[0]
        
        lambdas         =   {"default":dfc_fn,"list":fns,"callback":"get_apply_fn"}
        selectDicts.append(lambdas)

        get_select_defaults(applyfn_input_form,
                            apply_column_lambda_input_id,
                            apply_column_lambda_input_idList,
                            apply_column_lambda_input_typeList,
                            selectDicts)
        
        funcparms   =   get_apply_function_parms(dfc_fn)
        
        if(funcparms is None) :
            dfc_code    =   str(dfc_fn) + "()"
            fnProtect   =   True
        else :
            dfc_code    =   str(dfc_fn)
            dfc_code    =   dfc_code[0:dfc_code.find("(")] + "("
            
            funcptypes  =   get_apply_function_parms_datatypes(dfc_fn)
            
            for i in range(len(funcparms)) :
                if(funcptypes[i] == str) :
                    dfc_code    =   dfc_code + "'" + funcparms[i] + "'"
                else :
                    dfc_code    =   dfc_code + funcparms[i] 
                    
                if(not((i+1) == len(funcparms))) :
                    dfc_code    =   dfc_code + ","
                    
            dfc_code    =   dfc_code + ")"
             
            fnProtect   =   False
        
        cfg.set_config_value(apply_column_lambda_input_id+"Parms",[dftitle,colname,dfc_fn,dfc_code])
        cfg.set_config_value(apply_column_lambda_input_id+"ParmsProtect",[False,False,False,fnProtect])

        applyfn_heading_html    =   "<div>" + apply_column_lambda_input_title + "</div><br>"
        
        if(funcparms is None) :
            help_note           =   "Select a new dfc_fn to run or hit 'Apply dfc fn To Column' to run the current dfc fn."
        else :
            help_note           =   "Select a new dfc_fn to run or enter the parms in 'dfc_fn_code' and hit 'Apply dfc fn To Column' to run the current dfc fn."
        
    else :
        
        dfc_code    =   "from dfcleanser.common.cfg import get_dataframe\n"
        dfc_code    =   (dfc_code + "df = get_dataframe('" + str(dftitle) + "')\n")
        dfc_code    =   (dfc_code + "colname = '" + str(colname) + "'\n")
       
        get_select_defaults(applyfn_input_form,
                            apply_column_gf_input_id,
                            apply_column_gf_input_idList,
                            apply_column_gf_input_typeList,
                            selectDicts)
        

        cfg.set_config_value(apply_column_gf_input_id+"Parms",[dftitle,colname,dfc_code])
        cfg.set_config_value(apply_column_gf_input_id+"ParmsProtect",[False,False,False])

        applyfn_heading_html    =   "<div>Apply User fn to Column</div><br>"
        help_note               =   "Use df in 'user_function' for the 'dataframe_to_apply_fn_to' value.</br>"
        help_note               =   (help_note + "Use colname in 'user_function' for the 'column_to_apply_fn_to' value.</br>")
        help_note               =   (help_note + "Include all imports to insure visibility in an exec() call.")

    help_note_html =   get_help_note_html(help_note)


    applyfn_input_form.set_buttonstyle({"font-size":13, "height":90, "width":75, "left-margin":5})
    applyfn_input_form.set_custom_font_size("fntoapply",14)
    applyfn_input_form.set_gridwidth(480)
    applyfn_input_form.set_shortForm(True)
    applyfn_input_form.set_fullparms(True)
        
    applyfn_input_html = ""
    applyfn_input_html = applyfn_input_form.get_html()
    
    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
    gridhtmls       =   [col_stats_html,applyfn_heading_html,applyfn_input_html,help_note_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("display-df-apply-fn-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("display-df-apply-fn-wrapper",gridclasses,gridhtmls,True)
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display add column specific methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    


"""
#--------------------------------------------------------------------------
#    display add column from dfc funcs working idlist
#--------------------------------------------------------------------------
""" 

add_column_code_dfc_funcs_idList                      =   []

def get_current_dfc_funcs_idlist() :
    return(add_column_code_dfc_funcs_idList)
def set_current_dfc_funcs_idlist(idlist) :
    global add_column_code_dfc_funcs_idList
    add_column_code_dfc_funcs_idList = idlist


def display_add_cols_df_funcs_with_parms(option,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the add cols with parms input
    * 
    * parms :
    *   parms   -   add column parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    if("addcolfuncs" in parms[0]) :
        
        fparms  =   get_parms_for_input(parms,add_column_code_dfc_funcs_input_idList)
        
        newcolname      =   fparms[0]
        newcolnamedf    =   fparms[1]
        newdatatype     =   fparms[2]
        ftitle          =   fparms[3]
        dfparm          =   None
        
    elif( ("addcolfuncsdfcol" in parms[0]) or ("addcoldftitledfcol" in parms[0]) ) :
        
        fparms  =   get_parms_for_input(parms,add_column_code_dfc_funcs_DF_COL_parms_input_idList)
        
        newcolname      =   fparms[0]
        newcolnamedf    =   fparms[1]
        newdatatype     =   fparms[2]
        ftitle          =   fparms[3]
        dfparm          =   fparms[6]
        
    elif( ("addcolfuncsdfcolnum" in parms[0]) or ("addcoldftitledfcolnum" in parms[0]) ) :
        
        fparms  =   get_parms_for_input(parms,add_column_code_dfc_funcs_DF_COL_NUM_parms_input_idList)
        
        newcolname      =   fparms[0]
        newcolnamedf    =   fparms[1]
        newdatatype     =   fparms[2]
        ftitle          =   fparms[3]
        dfparm          =   fparms[6]
        
    elif( ("addcolfuncsdfcolnumnum" in parms[0]) or ("addcoldftitledfcolnumnum" in parms[0]) ) :
        
        fparms  =   get_parms_for_input(parms,add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_idList)
        
        newcolname      =   fparms[0]
        newcolnamedf    =   fparms[1]
        newdatatype     =   fparms[2]
        ftitle          =   fparms[3]
        dfparm          =   fparms[6]
    
    elif( ("addcolfuncsdfnumnum" in parms[0]) or ("addcoldftitledfnumnum" in parms[0]) ) :
        
        fparms  =   get_parms_for_input(parms,add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_idList)
        
        newcolname      =   fparms[0]
        newcolnamedf    =   fparms[1]
        newdatatype     =   fparms[2]
        ftitle          =   fparms[3]
        dfparm          =   fparms[6]

    else :
        
        newcolname      =   None
        newcolnamedf    =   None
        newdatatype     =   None
        ftitle          =   None
        dfparm          =   None
        


    if(ftitle is None)  :
        
        common_id           =   add_column_code_dfc_funcs_input_id
        common_idList       =   add_column_code_dfc_funcs_input_idList
        common_typelist     =   merge_lists([add_column_code_dfc_funcs_input_typeList,add_column_code_dfc_funcs_input_typeListA])
        
        gt_input_form   = InputForm(common_id,
                                    common_idList,
                                    merge_lists([add_column_code_dfc_funcs_input_labelList,add_column_code_dfc_funcs_input_labelListA]),
                                    common_typelist,
                                    merge_lists([add_column_code_dfc_funcs_input_placeholderList,add_column_code_dfc_funcs_input_placeholderListA]),
                                    merge_lists([add_column_code_dfc_funcs_input_jsList,add_column_code_dfc_funcs_input_jsListA]),
                                    add_column_code_dfc_funcs_input_reqList)
        
    else :
        
        formtype    =   get_reserved_function_form_type(ftitle)
        
        if(formtype == DF_COL) :
            
            parms   =   get_reserved_function_parms(ftitle)
            
            common_id           =   add_column_code_dfc_funcs_DF_COL_parms_input_id
            common_idList       =   add_column_code_dfc_funcs_DF_COL_parms_input_idList
            common_typelist     =   merge_lists([add_column_code_dfc_funcs_input_typeList,["select","select"],add_column_code_dfc_funcs_input_typeListA])
            
            gt_input_form   = InputForm(common_id,
                                        common_idList,
                                        merge_lists([add_column_code_dfc_funcs_input_labelList,[parms[0],parms[1]],add_column_code_dfc_funcs_input_labelListA]),
                                        common_typelist,
                                        merge_lists([add_column_code_dfc_funcs_input_placeholderList,[parms[0],parms[1]],add_column_code_dfc_funcs_input_placeholderListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_jsList,[None,None],add_column_code_dfc_funcs_input_jsListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_reqList,[6,7]]))
            
        elif(formtype == DF_COL_NUM) :
            
            parms   =   get_reserved_function_parms(ftitle)
            
            common_id           =   add_column_code_dfc_funcs_DF_COL_NUM_parms_input_id
            common_idList       =   add_column_code_dfc_funcs_DF_COL_NUM_parms_input_idList
            common_typelist     =   merge_lists([add_column_code_dfc_funcs_input_typeList,["select","select","text"],add_column_code_dfc_funcs_input_typeListA])
            
            gt_input_form   = InputForm(common_id,
                                        common_idList,
                                        merge_lists([add_column_code_dfc_funcs_input_labelList,[parms[0],parms[1],parms[2]],add_column_code_dfc_funcs_input_labelListA]),
                                        common_typelist,
                                        merge_lists([add_column_code_dfc_funcs_input_placeholderList,[parms[0],parms[1],parms[2]],add_column_code_dfc_funcs_input_placeholderListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_jsList,[None,None,None],add_column_code_dfc_funcs_input_jsListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_reqList,[6,7,8]]))

        elif(formtype == DF_COL_NUM_NUM) :
            
            parms   =   get_reserved_function_parms(ftitle)
            
            common_id           =   add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_id
            common_idList       =   add_column_code_dfc_funcs_DF_COL_NUM_NUM_parms_input_idList
            common_typelist     =   merge_lists([add_column_code_dfc_funcs_input_typeList,["select","select","text","text"],add_column_code_dfc_funcs_input_typeListA])
            
            gt_input_form   = InputForm(common_id ,
                                        common_idList,
                                        merge_lists([add_column_code_dfc_funcs_input_labelList,[parms[0],parms[1],parms[2],parms[3]],add_column_code_dfc_funcs_input_labelListA]),
                                        common_typelist,
                                        merge_lists([add_column_code_dfc_funcs_input_placeholderList,[parms[0],parms[1],parms[2],parms[3]],add_column_code_dfc_funcs_input_placeholderListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_jsList,[None,None,None,None],add_column_code_dfc_funcs_input_jsListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_reqList,[6,7,8,9]]))
            
        elif(formtype == DF_NUM_NUM) :
            
            parms       =   get_reserved_function_parms(ftitle)
            
            common_id           =   add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_id
            common_idList       =   add_column_code_dfc_funcs_DF_NUM_NUM_parms_input_idList
            common_typelist     =   merge_lists([add_column_code_dfc_funcs_input_typeList,["select","text","text"],add_column_code_dfc_funcs_input_typeListA])
            
            gt_input_form   = InputForm(common_id,
                                        common_idList,
                                        merge_lists([add_column_code_dfc_funcs_input_labelList,[parms[0],parms[1],parms[2]],add_column_code_dfc_funcs_input_labelListA]),
                                        common_typelist,
                                        merge_lists([add_column_code_dfc_funcs_input_placeholderList,[parms[0],parms[1],parms[2]],add_column_code_dfc_funcs_input_placeholderListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_jsList,[None,None,None],add_column_code_dfc_funcs_input_jsListA]),
                                        merge_lists([add_column_code_dfc_funcs_input_reqList,[6,7,8]]))
            
        else :
            
            opstat.set_status(False) 
            opstat.set_errorMsg("Invalid form type")
   
    if(opstat.get_status()) :
    
        selectDicts     =   []
    
        dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
        dataframes          =   {"default":newcolnamedf,"list":dataframes_loaded}
        selectDicts.append(dataframes)
    
        cdatatype       =   get_reserved_function_return_datatype(ftitle)
    
        dtypes          =   {"default":cdatatype,"list":["str","int","float","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                         "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                         "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object"]}
        selectDicts.append(dtypes)

        funcs_list  =   get_genfunc_list()
        
        funcs           =   []
        funcs.append(" ")
        
        if(not (funcs_list == None)) :
            for i in range(len(funcs_list)) :
                funcs.append(funcs_list[i])
        
        funclist    =   {"default":ftitle,"list":funcs,"callback":"get_dfc_func_value"}
        selectDicts.append(funclist)
        
        if(not (formtype is None)) :
            
            dfs_loaded   =   cfg.get_dfc_dataframes_titles_list()
            if(dfparm is None) :
                dfparm  =  dfs_loaded[0] 
            dfs          =   {"default":dfparm,"list":dfs_loaded, "callback":"get_dfc_func_value"}
            selectDicts.append(dfs)
            
            if(not (formtype == DF_NUM_NUM)) :
                
                colslist    =   cfg.get_dataframe(dfparm).columns.tolist()
                cols        =   {"default":colslist[0],"list":colslist}
                selectDicts.append(cols)

           
        cfg.drop_config_value(common_id+"Parms")
     
        get_select_defaults(gt_input_form,
                            common_id,
                            common_idList,
                            common_typelist,
                            selectDicts)

        gt_input_form.set_shortForm(True)
        gt_input_form.set_gridwidth(480)
        gt_input_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":2})
        gt_input_form.set_fullparms(True)
        gt_input_form.set_custom_font_size("addcolcodefcode",13)
        
        if(ftitle is None) :
    
            inputparms      =   [newcolname,newcolnamedf,"str","","",""]
            inputpparms     =   [False,False,False,False,True,True]
            
        else :
            
            gfdesc      =   get_generic_function_desc(ftitle)
            gfdesc      =   gfdesc.replace("'",'"')
            
            gfparms     =   get_reserved_function_parms(ftitle)
            gfpdtypes   =   get_reserved_function_parms_datatypes(ftitle)
            
            gfcode      =   "new_column_list = " + ftitle + "("
            
            for i in range(len(gfparms)) :
                
                if(gfpdtypes[i] == str) :
                    gfcode  =   gfcode + "'" + gfparms[i] + "'"
                else :
                    gfcode  =   gfcode + gfparms[i] 
                    
                if(not ((i+1)==len(gfparms))) :
                    gfcode  =   gfcode + ","
                    
            gfcode  =   gfcode + ")"
                
            if(formtype == DF_COL) :
                
                inputparms      =   [newcolname,newcolnamedf,get_reserved_function_return_datatype(ftitle),ftitle,gfcode,gfdesc,dfparm,colslist[0]]
                inputpparms     =   [False,False,False,False,True,True,False,False]
             
            elif(formtype == DF_COL_NUM) :
            
                inputparms      =   [newcolname,newcolnamedf,get_reserved_function_return_datatype(ftitle),ftitle,gfcode,gfdesc,dfparm,colslist[0],""]
                inputpparms     =   [False,False,False,False,True,True,False,False,False]

            elif(formtype == DF_COL_NUM_NUM) :
            
                inputparms      =   [newcolname,newcolnamedf,get_reserved_function_return_datatype(ftitle),ftitle,gfcode,gfdesc,dfparm,colslist[0],"",""]
                inputpparms     =   [False,False,False,False,True,True,False,False,False,False]
            
            elif(formtype == DF_NUM_NUM) :
            
                inputparms      =   [newcolname,newcolnamedf,get_reserved_function_return_datatype(ftitle),ftitle,gfcode,gfdesc,dfparm,"",""]
                inputpparms     =   [False,False,False,False,True,True,False,False,False]
        
        cfg.set_config_value(common_id+"Parms",inputparms)
        cfg.set_config_value(common_id+"ParmsProtect",inputpparms)
        
        gt_input_html   =   ""
        gt_input_html   =   gt_input_form.get_html()
        
        gt_heading_html     =   "<div>Add New Column From dfc Functions</div><br>"
        help_note           =   "After setting and reviewing parms in the above form click on 'Add New Column From dfc fns' to add a new column."
        from dfcleanser.common.common_utils import get_help_note_html
        addcol_notes_html   =   get_help_note_html(help_note)
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [gt_heading_html,gt_input_html,addcol_notes_html]

        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls,True)

        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()


def display_add_cols_option(option,parms,displayBase=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the add cols input
    * 
    * parms :
    *   parms   -   add column parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    if(displayBase) :
        display_base_data_transform_columns_taskbar()

    newcolname      =   ""
    newdatatype     =   ""
    
    opstat  =   opStatus()
    
    if(option == dtm.DISPLAY_ADD_COLUMN) :
        newcolname      =   None
        newcolnamedf    =   None
        newdatatype     =   None
        
    if(opstat.get_status()) :

        if(option == dtm.DISPLAY_ADD_COLUMN) :
        
            cfg.drop_config_value(add_column_input_id + "Parms")
        
            common_column_heading_html      =   "<br><div>Add New Column </div><br>"
            
            grid_input_form                 =   InputForm(add_column_input_id,
                                                          add_column_input_idList,
                                                          add_column_input_labelList,
                                                          add_column_input_typeList,
                                                          add_column_input_placeholderList,
                                                          add_column_input_jsList,
                                                          add_column_input_reqList)
        
            selectDicts     =   []
            
            dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
            dataframes          =   {"default":dataframes_loaded[0],"list":dataframes_loaded, "callback":"change_apply_df_callback"}
            selectDicts.append(dataframes)
            
            dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                         "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                         "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
            selectDicts.append(dtypes)

            get_select_defaults(grid_input_form,
                                add_column_input_id,
                                add_column_input_idList,
                                add_column_input_typeList,
                                selectDicts)
            
            
        
            grid_input_form.set_buttonstyle({"font-size":12, "height":90, "width":110, "left-margin":2})
            grid_input_form.set_gridwidth(480)
            grid_input_form.set_fullparms(True) 

            grid_input_html   =   grid_input_form.get_html()

            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
            
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()

                 
        elif(option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
        
            fparms = get_parms_for_input(parms,add_column_input_idList)
            
            if(len(fparms[0]) == 0) :   newcolname      =   ""
            else :                      newcolname      =   fparms[0]
            
            if(len(fparms[1]) == 0) :   newcolnamedf    =   ""
            else :                      newcolnamedf    =   fparms[1]
            
            if(len(fparms[2]) == 0) :   newdatatype     =   ""
            else :                      newdatatype     =   fparms[2]
            
            cfg.set_config_value(add_column_file_input_id+"Parms",[newcolname,newcolnamedf,newdatatype,"",""])
        
            common_column_heading_html      =   "<br><div>Add New Column From File</div><br>"
            
            grid_input_form                 =   InputForm(add_column_file_input_id,
                                                          add_column_file_input_idList,
                                                          add_column_file_input_labelList,
                                                          add_column_file_input_typeList,
                                                          add_column_file_input_placeholderList,
                                                          add_column_file_input_jsList,
                                                          add_column_file_input_reqList)
        
            selectDicts     =   []
            
            dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
            dataframes          =   {"default":dataframes_loaded[0],"list":dataframes_loaded, "callback":"change_apply_df_callback"}
            selectDicts.append(dataframes)
            
            dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                         "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                         "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
            selectDicts.append(dtypes)
        
            get_select_defaults(grid_input_form,
                                add_column_file_input_id,
                                add_column_file_input_idList,
                                add_column_file_input_typeList,
                                selectDicts)
            
            grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":120, "left-margin":40})
            grid_input_form.set_gridwidth(480)
            grid_input_form.set_fullparms(True)
            grid_input_form.set_shortForm(True)
    
            grid_input_html   =   grid_input_form.get_html()

            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
    
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()


        elif( (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) or 
              (option == dtm.DISPLAY_ADD_FROM_CODE_OPTION) or 
              (option == dtm.DISPLAY_ADD_FROM_CODE_FN_OPTION) ) :
        
            if(option == dtm.DISPLAY_ADD_FROM_CODE_FN_OPTION) :
                fparms = get_parms_for_input(parms,add_column_code_user_fns_input_idList)
                
                newcolname      =   fparms[0]
                newcolnamedf    =   fparms[1]
                newdatatype     =   fparms[2]
                ftitle          =   fparms[3]
                fmodule         =   fparms[4]
                fname           =   fparms[5]
                fcode           =   fparms[6]

            else :
                fparms = get_parms_for_input(parms,add_column_input_idList)
            
                newcolname      =   fparms[0]
                newcolnamedf    =   fparms[1]
                newdatatype     =   fparms[2]
                ftitle          =   ""
                fmodule         =   ""
                fname           =   ""
                fcode           =   ""
                
            
            if(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
                cfg.set_config_value(add_column_code_dfc_funcs_input_id+"Parms",[newcolname,newcolnamedf,newdatatype,"","",""])
                cfg.set_config_value(add_column_code_dfc_funcs_input_id+"ParmsProtect",[False,False,False,False,True,True])
            else :
                cfg.set_config_value(add_column_code_user_fns_input_id+"Parms",[newcolname,newcolnamedf,newdatatype,ftitle,fmodule,fname,fcode])
                
            display_add_cols_code(option)
            
        elif( (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS_PARMS) ):
            
            display_add_cols_df_funcs_with_parms(option,parms) 
            
        elif( (option == dtm.DISPLAY_MAINTAIN_USER_FUNC) ):
            
            common_column_heading_html      =   "<div>Maintain User Defined Functions</div><br>"
            
            maintain_input_form               =   InputForm(maintain_user_fns_input_id,
                                                            maintain_user_fns_input_idList,
                                                            maintain_user_fns_input_labelList,
                                                            maintain_user_fns_input_typeList,
                                                            maintain_user_fns_input_placeholderList,
                                                            maintain_user_fns_input_jsList,
                                                            maintain_user_fns_input_reqList)
            
            selectDicts     =   [] 
            
            from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_generic_user_functions_names_list
            userfuncs       =   get_generic_user_functions_names_list()
            
            if(len(userfuncs) > 0) :
            
                if(not (parms is None)) :
                    if("userfnsftitle" in parms[0]) :
                        fparms  =   get_parms_for_input(parms,maintain_user_fns_input_idList)
                        current_func    =   fparms[0]
                    else :
                        current_func    =   userfuncs[0]
                else :
                    current_func    =   userfuncs[0]
                    
                funclist    =   {"default":current_func,"list":userfuncs,"callback":"change_user_func_value"}
                selectDicts.append(funclist)
                
                from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_generic_user_function
                user_func       =   get_generic_user_function(current_func)
                fmodule         =   user_func[0] 
                fcode           =   user_func[1]
                fname           =   current_func
            
            else :
                
                current_func    =   ""
                
                funclist    =   {"default":current_func,"list":[""],"callback":"change_user_func_value"}
                selectDicts.append(funclist)
                
                fmodule         =   "" 
                fcode           =   ""
                fname           =   ""
            
            get_select_defaults(maintain_input_form,
                                maintain_user_fns_input_id,
                                maintain_user_fns_input_idList,
                                maintain_user_fns_input_typeList,
                                selectDicts)
            
            cfg.set_config_value(maintain_user_fns_input_id+"Parms",[current_func,fname,fmodule,fcode])
        
            maintain_input_form.set_shortForm(True)
            maintain_input_form.set_gridwidth(480)
    
            maintain_input_form.set_buttonstyle({"font-size":12, "height":90, "width":110, "left-margin":2})
        
            maintain_input_form.set_fullparms(True)
    
            maintain_input_html   =   ""
            maintain_input_html   =   maintain_input_form.get_html()
            
            if(len(userfuncs) > 0) :
                help_note           =   "Select a user_fn in order to edit or felete it."
            else :
                help_note           =   "There are no user fns currently defined."
        
            from dfcleanser.common.common_utils import get_help_note_html
            addcol_notes_html   =   get_help_note_html(help_note)
    
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
            gridhtmls       =   [common_column_heading_html,maintain_input_html,addcol_notes_html]

            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls,True)

            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()


        elif(option == dtm.DISPLAY_ADD_FROM_DF_OPTION) :
        
            common_column_heading_html      =   "<div>Add New Column From df</div><br>"
            
            source_input_form               =   InputForm(add_column_source_df_input_id,
                                                          add_column_source_df_input_idList,
                                                          add_column_source_df_input_labelList,
                                                          add_column_source_df_input_typeList,
                                                          add_column_source_df_input_placeholderList,
                                                          add_column_source_df_input_jsList,
                                                          add_column_source_df_input_reqList)
            
            output_input_form               =   InputForm(add_column_output_df_input_id,
                                                          add_column_output_df_input_idList,
                                                          add_column_output_df_input_labelList,
                                                          add_column_output_df_input_typeList,
                                                          add_column_output_df_input_placeholderList,
                                                          add_column_output_df_input_jsList,
                                                          add_column_output_df_input_reqList)
            
            grid_input_form                 =   InputForm(add_column_df_input_id,
                                                          add_column_df_input_idList,
                                                          add_column_df_input_labelList,
                                                          add_column_df_input_typeList,
                                                          add_column_df_input_placeholderList,
                                                          add_column_df_input_jsList,
                                                          add_column_df_input_reqList)
            
            dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
            current_df_name     =   cfg.get_config_value(cfg.DataTransform_ID)
            
            current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
            colnames        =   current_df.columns.tolist()
            cnames          =   {"default":colnames[0],"list": colnames,"callback":"add_df_change_col_source"}
            cnames1         =   {"default":colnames[0],"list": colnames, "callback":"add_df_col_change_col", "size":5}
        
            dataframes      =   {"default":current_df_name,"list":dataframes_loaded, "callback":"add_df_col_df_change", "size":2}
            
            sourceselectDicts     =   []            
            sourceselectDicts.append(dataframes)
            sourceselectDicts.append(cnames)
            sourceselectDicts.append(cnames1)
            
            outputselectDicts     =   []
            outputselectDicts.append(dataframes)
            
            source_col_dtype    =   current_df[colnames[0]].dtype
            from dfcleanser.common.common_utils import get_dtype_str_for_datatype
            dtype_str           =   get_dtype_str_for_datatype(source_col_dtype)
            
            from dfcleanser.common.common_utils import get_datatypes_list
            dtypes          =   {"default":dtype_str,"list":get_datatypes_list()}
            outputselectDicts.append(dtypes)
            outputselectDicts.append(cnames1)

            get_select_defaults(source_input_form,
                                add_column_source_df_input_id,
                                add_column_source_df_input_idList,
                                add_column_source_df_input_typeList,
                                sourceselectDicts)
            
            get_select_defaults(output_input_form,
                                add_column_output_df_input_id,
                                add_column_output_df_input_idList,
                                add_column_output_df_input_typeList,
                                outputselectDicts)
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                
                source_input_form.set_buttonstyle({"font-size":13, "height":30, "width":100, "left-margin":100})
                source_input_form.set_gridwidth(360)
                source_input_form.set_fullparms(True)
            
            else :
                
                source_input_form.set_buttonstyle({"font-size":13, "height":30, "width":100, "left-margin":50})
                source_input_form.set_gridwidth(240)
                source_input_form.set_fullparms(True)
                
            source_input_html   =   source_input_form.get_html()
            
            get_select_defaults(output_input_form,
                                add_column_output_df_input_id,
                                add_column_output_df_input_idList,
                                add_column_output_df_input_typeList,
                                outputselectDicts)
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                
                output_input_form.set_buttonstyle({"font-size":13, "height":30, "width":100, "left-margin":100})
                output_input_form.set_gridwidth(360)
                output_input_form.set_fullparms(True)
                
            else :
            
                output_input_form.set_buttonstyle({"font-size":13, "height":30, "width":100, "left-margin":50})
                output_input_form.set_gridwidth(240)
                output_input_form.set_fullparms(True)
        
            output_input_html   =   output_input_form.get_html()
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                            
                grid_input_form.set_buttonstyle({"font-size":13, "height":90, "width":90, "left-margin":150})
                grid_input_form.set_gridwidth(720)
                grid_input_form.set_fullparms(True)
                grid_input_form.set_shortForm(True)

            else :
            
                grid_input_form.set_buttonstyle({"font-size":13, "height":90, "width":90, "left-margin":50})
                grid_input_form.set_gridwidth(480)
                grid_input_form.set_fullparms(True)
                grid_input_form.set_shortForm(True)
        
            grid_input_html   =   grid_input_form.get_html()
            
            print("\n")
        
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-footer"]
            gridhtmls       =   [common_column_heading_html,source_input_html,output_input_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-add-col-from-df-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-add-col-from-df-pop-up-wrapper",gridclasses,gridhtmls)
    
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()
    
            
    else :
        display_exception(opstat)
        
        
def merge_lists(lists) :
    
    merged_list     =   []
    
    for i in range(len(lists)) :
        for j in range(len(lists[i])) :
            merged_list.append(lists[i][j])
    
    
    return(merged_list)


def display_add_cols_code(option,colname=None,dtype=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display add column fom code inputs
    * 
    * parms :
    *   option  -   display option
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
 
    if(dtype is None) :
        defdtype   =    "str" 
    else :
        defdtype    =   dtype
    
    if(option==dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
        
        gt_input_form   = InputForm(add_column_code_dfc_funcs_input_id,
                                    add_column_code_dfc_funcs_input_idList,
                                    merge_lists([add_column_code_dfc_funcs_input_labelList,add_column_code_dfc_funcs_input_labelListA]),
                                    merge_lists([add_column_code_dfc_funcs_input_typeList,add_column_code_dfc_funcs_input_typeListA]),
                                    merge_lists([add_column_code_dfc_funcs_input_placeholderList,add_column_code_dfc_funcs_input_placeholderListA]),
                                    merge_lists([add_column_code_dfc_funcs_input_jsList,add_column_code_dfc_funcs_input_jsListA]),
                                    add_column_code_dfc_funcs_input_reqList)
        
    else :
        
        gt_input_form   = InputForm(add_column_code_user_fns_input_id,
                                    add_column_code_user_fns_input_idList,
                                    add_column_code_user_fns_input_labelList,
                                    add_column_code_user_fns_input_typeList,
                                    add_column_code_user_fns_input_placeholderList,
                                    add_column_code_user_fns_input_jsList,
                                    add_column_code_user_fns_input_reqList)

    selectDicts     =   []
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    dataframes          =   {"default":dataframes_loaded[0],"list":dataframes_loaded, "callback":"change_apply_df_callback"}
    selectDicts.append(dataframes)
            
    dtypes          =   {"default" : defdtype, "list": ["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                        "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                        "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
    selectDicts.append(dtypes)

    if(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) : 
        
        funcs_list  =   get_genfunc_list()
        
        funcs           =   []
        funcs.append(" ")
        
        if(not (funcs_list == None)) :
            for i in range(len(funcs_list)) :
                funcs.append(funcs_list[i])
        
        funclist    =   {"default":" ","list":funcs,"callback":"get_dfc_func_value"}
        selectDicts.append(funclist)
        
        get_select_defaults(gt_input_form,
                            add_column_code_dfc_funcs_input_id,
                            add_column_code_dfc_funcs_input_idList,
                            merge_lists([add_column_code_dfc_funcs_input_typeList,add_column_code_dfc_funcs_input_typeListA]),
                            selectDicts)
        
    else :
        
        if(option == dtm.DISPLAY_ADD_FROM_CODE_FN_OPTION) :
            fparms      =   cfg.get_config_value(add_column_code_user_fns_input_id+"Parms")
                
            newcolname      =   fparms[0]
            newdftitle      =   fparms[1]
            newdatatype     =   fparms[2]
            ftitle          =   fparms[3]
            fmodule         =   fparms[4]
            fname           =   fparms[5]
            fcode           =   fparms[6]
                
        else :
                
            newcolname      =   ""
            newdftitle      =   ""
            newdatatype     =   ""
            ftitle          =   ""
            fmodule         =   ""
            fname           =   ""
            fcode           =   ""

        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_generic_user_functions_names_list
        userfuncs       =   get_generic_user_functions_names_list()
        funcs           =   [" "]
        for i in range(len(userfuncs)) :
            funcs.append(userfuncs[i])
            
        if(option == dtm.DISPLAY_ADD_FROM_CODE_FN_OPTION) :
            deffunc     =   ftitle
        else :
            deffunc     =   funcs[0]
            
        funclist    =   {"default":deffunc,"list":funcs,"callback":"get_user_func_value"}
        selectDicts.append(funclist)
            
        get_select_defaults(gt_input_form,
                            add_column_code_user_fns_input_id,
                            add_column_code_user_fns_input_idList,
                            add_column_code_user_fns_input_typeList,
                            selectDicts)
            
        if(not (ftitle == ""))  :
                
            from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_generic_user_function
            user_func       =   get_generic_user_function(deffunc)
            fmodule         =   user_func[0] 
            fname           =   ftitle
            fcode           =   user_func[1]
            
        else :
                
            fmodule         =   ""
            fname           =   ""
            fcode           =   ""
                
        cfg.set_config_value(add_column_code_user_fns_input_id+"Parms",[newcolname,newdftitle,newdatatype,ftitle,fmodule,fname,fcode])
        
    gt_input_form.set_shortForm(True)
    gt_input_form.set_gridwidth(480)
    
    if(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
        gt_input_form.set_buttonstyle({"font-size":12, "height":90, "width":110, "left-margin":2})
    else :
        gt_input_form.set_buttonstyle({"font-size":12, "height":90, "width":75, "left-margin":5})
        
    gt_input_form.set_fullparms(True)
    
    gt_input_html   =   ""
    gt_input_html   =   gt_input_form.get_html()
    
    if(option==dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
        help_note           =   "Select a dfc_function in order to add a new column."
    else :
        if(fcode ==   "") :
            help_note           =   ("Select a user_function or enter new user code and hit 'Add New Column from User Code' in order to add a new column.<br>"+
            "The column value list to add to the df must be stored in the 'newcol_values_list' in the user_function_code.<br>"+
            "Include all dependencies to run the user code since the code will be run with an exec()")
        else :
            help_note           =   ("Fill in the function parm values in the 'user_function_code' and hit 'Add New Column from User Code' in order to add a new column.<br>"+
            "The column value list to add to the df must be stored in the 'newcol_values_list' in the user_function_code.<br>"+
            "Include all dependencies to run the user code since the code will be run with an exec()")
        
    from dfcleanser.common.common_utils import get_help_note_html
    addcol_notes_html   =   get_help_note_html(help_note)

    
    if(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) : 
        gt_heading_html =   "<br><div>Add New Column From dfc Functions</div><br>"
    else :
        gt_heading_html =   "<br><div>Add New Column From User Code</div><br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom",]
    gridhtmls       =   [gt_heading_html,gt_input_html,addcol_notes_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

        
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    end display add column specific methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    
        
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display datatype, fillna and dropna methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 



def display_column_uniques(df,colname,samplesize,uniquesperrow,display=True,callback=None) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display col uniques
    * 
    * parms :
    *  df          -   data frame
    *  colname     -   column name
    *  display     -   boolean display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
 
    uniques             =   df[colname].unique().tolist()
    
    if(is_numeric_col(df,colname)) :
        uniques.sort()
    else :
        if(does_col_contain_nan(df,colname)) :
            import pandas as pd
            uniques = pd.Series(uniques).fillna("nan").tolist()
            uniques.sort()
        else :
            uniques.sort()

    uniqueHeader    =   []
    uniqueWidths    =   []
    uniqueAligns    =   []
    
    if(len(uniques) < uniquesperrow) :
        uniquesperrow       =   len(uniques)
        samplesize          =   len(uniques)
        
    colwidth    =   100/uniquesperrow
    
    for i in range(uniquesperrow) :
        uniqueHeader.append("Value")
        uniqueWidths.append(colwidth)
        uniqueAligns.append("center")
        
    uniqueRows      =   []
    uniqueHrefs     =   []
    
    uniquerow       =   []
    
    if(samplesize > len(uniques)) :
        samplesize = len(uniques)
    
    for i in range(samplesize) :
        
        if(i < len(uniques)) :
            uniquerow.append(uniques[i])

            if((i+1) % uniquesperrow == 0) :
                uniqueRows.append(uniquerow)
                
                uniqueHrefs     =   []
                
                for k in range(uniquesperrow) :
                    if(callback is None) :
                        uniqueHrefs.append(None)
                    else :
                        uniqueHrefs.append(callback)
                uniquerow   =   []
    
    if((samplesize % uniquesperrow) != 0) :

        for k in range(uniquesperrow - (samplesize % uniquesperrow)) :
            uniquerow.append("")

        uniqueRows.append(uniquerow) 
        
        uniqueHrefs     =   []
        
        for k in range(uniquesperrow) :
            
            if(callback is None) :
                uniqueHrefs.append(None)
            else :
                uniqueHrefs.append(callback)
            
    uniques_table = dcTable("Unique Values for "+colname,"dtuniquesTable",
                            cfg.DataTransform_ID,
                            uniqueHeader,uniqueRows,
                            uniqueWidths,uniqueAligns)
    
    uniques_table.set_tabletype(ROW_MAJOR)
    uniques_table.set_small(True)
    uniques_table.set_smallwidth(100)
    uniques_table.set_rowspertable(6)
    uniques_table.set_refList(uniqueHrefs)

    if(display) :
        uniques_table.display_table()
    else :
        return(uniques_table.get_html())


def display_uniques_and_find(df,colname,callback=None,dispfind=True) :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
         uniques_html    =   display_column_uniques(df,colname,48,6,False,callback)
    else :
         uniques_html    =   display_column_uniques(df,colname,24,4,False,callback)
    
    if(dispfind) : 
        
        if(not (is_numeric_col(df,colname)) ) :
        
            import dfcleanser.data_cleansing.data_cleansing_widgets as dcw

            find_values_inputs  =   InputForm(dcw.nn_find_values_input_id,
                                              dcw.nn_find_values_input_idList,
                                              dcw.nn_find_values_input_labelList,
                                              dcw.nn_find_values_input_typeList,
                                              dcw.nn_find_values_input_placeholderList,
                                              dcw.nn_find_values_input_jsList,
                                              dcw.nn_find_values_input_reqList)
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":40})
            find_values_inputs.set_gridwidth(280)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
        else :
        
            import dfcleanser.data_cleansing.data_cleansing_widgets as dcw

            find_values_inputs  =   InputForm(dcw.find_values_input_id,
                                              dcw.find_values_input_idList,
                                              dcw.find_values_input_labelList,
                                              dcw.find_values_input_typeList,
                                              dcw.find_values_input_placeholderList,
                                              dcw.find_values_input_jsList,
                                              dcw.find_values_input_reqList)
            
            find_values_inputs.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":40})
            find_values_inputs.set_gridwidth(280)
            find_values_inputs.set_shortForm(True)

            find_values_html    =   find_values_inputs.get_html()
            
        uniques_heading_html  =   "<div>Find Uniques</div><br>"    
            
    else :
        
        find_values_html        =   " "
        uniques_heading_html    =   " "
    
    if(dispfind) :
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
            gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [uniques_html,uniques_heading_html,find_values_html]
        
            display_generic_grid("col-change-datatype-uniques-wrapper",gridclasses,gridhtmls) 
            
        else :
            gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [uniques_html,uniques_heading_html,find_values_html]
        
            display_generic_grid("col-change-datatype-uniques-pop-up-wrapper",gridclasses,gridhtmls)
            
    else :
        
        gridclasses     =   ["dfc-main"]
        gridhtmls       =   [uniques_html]
        
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
            display_generic_grid("col-cat-uniques-wrapper",gridclasses,gridhtmls) 
        else :
            display_generic_grid("col-cat-uniques-pop-up-wrapper",gridclasses,gridhtmls)


def get_uniques_display(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the uniques and change datatype
    * 
    * parms :
    *   colname   -   column name
    *   noButtons -   input no buttons flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    display_base_data_transform_columns_taskbar()
    
    print("\n")
    
    display_uniques_and_find(df,colname) 
    
    print("\n")
    
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)

    nans            =   df[colname].isnull().sum()
    
    if(nans > 0) :
        change_dt_html  =   get_datatype_display(df,colname,True,False,cfg.DataTransform_ID) + "<br><br><br><br><br>"
        common_column_heading_html  =   "<div>Data Type Change</div><br>"
    else :
        change_dt_html  =   get_datatype_display(df,colname,False,False,cfg.DataTransform_ID) + "<br><br><br><br><br>"
        common_column_heading_html  =   "<br><br><div>Data Type Change</div><br>"
     
        
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [col_stats_html,common_column_heading_html,change_dt_html]
        
        display_generic_grid("col-change-datatype-dt-wrapper",gridclasses,gridhtmls) 
            
    else :
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [col_stats_html,common_column_heading_html,change_dt_html]
        
        display_generic_grid("col-change-datatype-dt-pop-up-wrapper",gridclasses,gridhtmls)

    
def get_datatype_display(df,colname,nansflag,nadropflag,dfc_id) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the fillna html
    * 
    * parms :
    *   colname   -   column name
    *   noButtons -   input no buttons flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(nansflag) :
        
        if(nadropflag) :
            
            grid_input_form     =   InputForm(dt_drop_nans_data_type_input_id,
                                              dt_drop_nans_data_type_input_idList,
                                              dt_drop_nans_data_type_input_labelList,
                                              dt_drop_nans_data_type_input_typeList,
                                              dt_drop_nans_data_type_input_placeholderList,
                                              dt_drop_nans_data_type_input_jsList,
                                              dt_drop_nans_data_type_input_reqList)
            
        else :
        
            grid_input_form     =   InputForm(dt_nans_data_type_input_id,
                                              dt_nans_data_type_input_idList,
                                              dt_nans_data_type_input_labelList,
                                              dt_nans_data_type_input_typeList,
                                              dt_nans_data_type_input_placeholderList,
                                              dt_nans_data_type_input_jsList,
                                              dt_nans_data_type_input_reqList)
        
    else :
    
        grid_input_form     =   InputForm(dt_data_type_input_id,
                                          dt_data_type_input_idList,
                                          dt_data_type_input_labelList,
                                          dt_data_type_input_typeList,
                                          dt_data_type_input_placeholderList,
                                          dt_data_type_input_jsList,
                                          dt_data_type_input_reqList)
    
    selectDicts     =   []
    
    current_df      =   df
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colname,"list": colnames, "callback":"change_dt_col_callback"}
    selectDicts.append(cnames)
    
    data_type_str   =   get_dtype_str_for_datatype(df[colname].dtype)

    from dfcleanser.common.common_utils import get_datatypes_list      
    dtypes          =   {"default":data_type_str,"list":get_datatypes_list()}
    selectDicts.append(dtypes)
    
    if(nansflag) :
        
        if(nadropflag) :
            
            nanopts     =   {"default":"dropna","list": ["fillna","dropna"], "callback":"change_na_option_callback"}
            selectDicts.append(nanopts)
            
            dropopts     =   {"default":"any","list": ["any","all"]}
            selectDicts.append(dropopts)
            
            get_select_defaults(grid_input_form,
                                dt_drop_nans_data_type_input_id,
                                dt_drop_nans_data_type_input_idList,
                                dt_drop_nans_data_type_input_typeList,
                                selectDicts)
            
        else :
            
            nanopts     =   {"default":"fillna","list": ["fillna","dropna"], "callback":"change_na_option_callback"}
            selectDicts.append(nanopts)
            
            methodopts     =   {"default":"None","list": ["None","backfill","bfill","pad","ffill"]}
            selectDicts.append(methodopts)
    
            get_select_defaults(grid_input_form,
                                dt_nans_data_type_input_id,
                                dt_nans_data_type_input_idList,
                                dt_nans_data_type_input_typeList,
                                selectDicts)
        
    else :
        
        get_select_defaults(grid_input_form,
                            dt_data_type_input_id,
                            dt_data_type_input_idList,
                            dt_data_type_input_typeList,
                            selectDicts)
        
    #grid_input_form.set_custombwidth(80)
    grid_input_form.set_gridwidth(480)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":1})
    
    return(grid_input_form.get_html())


def display_convert_datatype(df,colname,fillflag,dropflag,dfc_id) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display column change data type
    * 
    * parms :
    *  colid      -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    cfg.set_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY,colname) 
    
    if(dfc_id == cfg.DataCleansing_ID) :
        cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,cfg.get_config_value(cfg.CURRENT_CLEANSE_DF))

    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    nans            =   df[colname].isnull().sum()
        
    if(nans > 0) :
        
        if(fillflag) :  
             dt_html     =   get_datatype_display(df,colname,True,False,dfc_id)
            
        else :
            
            if(dropflag) :  
                dt_html     =   get_datatype_display(df,colname,True,True,dfc_id)
                
            else :
                dt_html     =   get_datatype_display(df,colname,True,False,dfc_id)

    else :
 
        dt_html     =   get_datatype_display(df,colname,False,False,dfc_id)
        
    common_column_heading_html      =   "<div>Data Type Change</div><br>"

    gridclasses     =   ["dfc-main","dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [col_stats_html,common_column_heading_html,dt_html]
     
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("col-change-datatype-transform-wrapper",gridclasses,gridhtmls) 
            
    else :
        display_generic_grid("col-change-datatype-transform-wrapper",gridclasses,gridhtmls,True) 
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
    

def get_compatable_dtypes(df,colname) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get compatable data types
    * 
    * parms :
    *  df        -   dataframe
    *  colname   -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    import numpy as np
    
    from dfcleanser.common.common_utils import is_datetime64_col, is_timedelta64_col, is_datetime_col, is_date_col, is_time_col, is_timedelta_col
    
    col_dtype           =   df[colname].dtype
    check_dtypes_list   =   []
    
    if(col_dtype == np.int8)        :   check_dtypes_list     =   ["np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]    
    elif(col_dtype == np.int16)     :   check_dtypes_list     =   ["np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]     
    elif(col_dtype == np.int32)     :   check_dtypes_list     =   ["np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]    
    elif(col_dtype == np.int64)     :   check_dtypes_list     =   ["np.float32","np.float64","str","object"]    
        
    elif(col_dtype == np.uint8)     :   check_dtypes_list     =   ["np.int8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]    
    elif(col_dtype == np.uint16)    :   check_dtypes_list     =   ["np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]    
    elif(col_dtype == np.uint32)    :   check_dtypes_list     =   ["np.int64","np.uint64","np.float16","np.float32","np.float64","str","object"]
    elif(col_dtype == np.uint64)    :   check_dtypes_list     =   ["np.float32","np.float64","str","object"]
        
    elif(col_dtype == np.float16)   :   check_dtypes_list     =   ["np.int64","np.uint64","np.float32","np.float64","str","object"]    
    elif(col_dtype == np.float32)   :   check_dtypes_list     =   ["np.float64","str","object"] 
    elif(col_dtype == np.float64)   :   check_dtypes_list     =   ["str","object"]
    
    elif(is_datetime64_col(df,colname))     :   check_dtypes_list     =   ["np.float64","str","object"]
    elif(is_timedelta64_col(df,colname))    :   check_dtypes_list     =   ["np.float64","str","object"]
    elif(is_datetime_col(df,colname))       :   check_dtypes_list     =   ["np.datetime64","str","object"]
    elif(is_date_col(df,colname))           :   check_dtypes_list     =   ["str","object"]
    elif(is_time_col(df,colname))           :   check_dtypes_list     =   ["str","object"]
    elif(is_timedelta_col(df,colname))      :   check_dtypes_list     =   ["np.timedelta64","np.float64","str","object"]

    elif(col_dtype == int)          :   check_dtypes_list     =   ["np.float64","str","object"]       
    elif(col_dtype == float)        :   check_dtypes_list     =   ["np.float64","str","object"]

    elif(col_dtype == object)       :   check_dtypes_list     =   ["object"]
    
    else :  check_dtypes_list     =   ["Unknown"]
        

    return(check_dtypes_list)    


    
def get_check_dtypes(df,colname) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display check data type compatability
    * 
    * parms :
    *  df        -   dataframe
    *  colname   -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    import numpy as np
    
    from dfcleanser.common.common_utils import is_datetime64_col, is_timedelta64_col, is_datetime_col, is_date_col, is_time_col, is_timedelta_col, is_Timestamp_col, is_Timedelta_col
    
    col_dtype           =   df[colname].dtype
    check_dtypes_list   =   []
    
    if(col_dtype == np.int8)        :   check_dtypes_list     =   ["np.uint8"]    
    elif(col_dtype == np.int16)     :   check_dtypes_list     =   ["np.int8","np.uint8","np.uint16"]    
    elif(col_dtype == np.int32)     :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.uint32","np.float16","timedelta"]    
    elif(col_dtype == np.int64)     :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.uint64","np.float16","np.float32","timedelta"]    
        
    elif(col_dtype == np.uint8)     :   check_dtypes_list     =   ["compatable with all dtypes"]    
    elif(col_dtype == np.uint16)    :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","timedelta"]    
    elif(col_dtype == np.uint32)    :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","int","np.float16","timedelta"]    
    elif(col_dtype == np.uint64)    :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.int64","np.uint32","int","np.int64","np.float16","np.float32","timedelta"]    
        
    elif(col_dtype == np.float16)   :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int",".timedelta"]    
    elif(col_dtype == np.float32)   :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int","np.float16","timedelta"]    
    elif(col_dtype == np.float64)   :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int","np.float16","np.float32","timedelta"]    
    
    elif(is_datetime64_col(df,colname))     :   check_dtypes_list     =   ["np.float16","np.float32","np.float64","datetime.datetime","datetime.date","datetime.time"]    
    elif(is_timedelta64_col(df,colname))    :   check_dtypes_list     =   ["np.float16","np.float32","datetime.timedelta"]    

    elif(col_dtype == int)      :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.uint32","np.float16","timedelta"]    
    elif(col_dtype == float)    :   check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","timedelta"]    


    elif(col_dtype == object) :
        
        if(is_datetime_col(df,colname))     :   check_dtypes_list     =   ["np.datetime64"]    
        elif(is_date_col(df,colname))       :   check_dtypes_list     =   ["np.datetime64"] 
        elif(is_time_col(df,colname))       :   check_dtypes_list     =   ["np.datetime64"]
        elif(is_timedelta_col(df,colname))  :   check_dtypes_list     =   ["np.timedelta64"]
        elif(is_Timestamp_col(df,colname))  :   check_dtypes_list     =   ["np.datetime64"]
        elif(is_Timedelta_col(df,colname))  :   check_dtypes_list     =   ["np.timedelta64"]
        else :
            check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","datetime.datetime","datetime.timedelta","np.datetime64","np.timedelta64"]    
   
    else :
        check_dtypes_list     = ["Unknown"]           
    
    return(check_dtypes_list)    
    

def display_check_compatability(parms,uniques=False) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display check data type compatability
    * 
    * parms :
    *  colid      -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    if(parms is None) :
        colname     =   cfg.get_config_value(cfg.COMPAT_COL_KEY)
    else :
        
        if(len(parms) == 1) :
            colname     =   parms[0]
            
        else :
            
            if(len(parms[0]) == 2) :
                
                    fparms  =   get_parms_for_input(parms,dt_data_type_input_idList)
                
            elif(len(parms[0]) == 3) :
                fparms  =   get_parms_for_input(parms,dt_check_data_type_input_idList)
                
            else :
                
                if("dtanyall" in parms[0]) :
                    fparms  =   get_parms_for_input(parms,dt_drop_nans_data_type_input_idList)
                    print("dtanyall",fparms)
                    
                elif("dtfillnamethod" in parms[0]) : 
                    fparms  =   get_parms_for_input(parms,dt_nans_data_type_input_idList)
                    print("dtfillnamethod",fparms)
                    
                else :
                
                    fparms  =   get_parms_for_input(parms,dt_str_check_data_type_input_idList)
                
            colname     =   fparms[0]
            
        cfg.set_config_value(cfg.COMPAT_COL_KEY,colname)
        
    if(uniques) :
        from dfcleanser.data_cleansing.data_cleansing_widgets import get_unique_col_html
        opstat  =   opStatus()
        get_unique_col_html(df,colname,opstat)
    
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)
    
    if(is_numeric_col(df,colname)) :
        
        grid_input_form     =   InputForm(dt_check_data_type_input_id,
                                          dt_check_data_type_input_idList,
                                          dt_check_data_type_input_labelList,
                                          dt_check_data_type_input_typeList,
                                          dt_check_data_type_input_placeholderList,
                                          dt_check_data_type_input_jsList,
                                          dt_check_data_type_input_reqList)
        
    else :
        
        grid_input_form     =   InputForm(dt_str_check_data_type_input_id,
                                          dt_str_check_data_type_input_idList,
                                          dt_str_check_data_type_input_labelList,
                                          dt_str_check_data_type_input_typeList,
                                          dt_str_check_data_type_input_placeholderList,
                                          dt_str_check_data_type_input_jsList,
                                          dt_str_check_data_type_input_reqList)
    
    selectDicts     =   []
    
    colnames        =   df.columns.tolist()
    cnames          =   {"default":colname,"list": colnames, "callback":"change_col_for_check_callback"}
    selectDicts.append(cnames)

    check_dtypes    =   get_check_dtypes(df,colname)     
    dtypes          =   {"default":check_dtypes[0],"list":check_dtypes, "size":10}
    selectDicts.append(dtypes)
    
    get_select_defaults(grid_input_form,
                        dt_check_data_type_input_id,
                        dt_check_data_type_input_idList,
                        dt_check_data_type_input_typeList,
                        selectDicts)
    
    grid_input_form.set_gridwidth(420)
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":100, "left-margin":1})

    compatable_dtypes   =   get_compatable_dtypes(df,colname)
    compatable_str      =   str(compatable_dtypes)
    
    if(not (is_numeric_col(df,colname))) :
        compatable_parms    =   [colname,check_dtypes[0],compatable_str,"5"]
        protect_parms       =   [False,False,True,False]

        cfg.set_config_value(dt_str_check_data_type_input_id + "Parms",compatable_parms)
        cfg.set_config_value(dt_str_check_data_type_input_id + "ParmsProtect",protect_parms)
        
    else :
        compatable_parms    =   [colname,check_dtypes[0],compatable_str]
        protect_parms       =   [False,False,True]
    
        cfg.set_config_value(dt_check_data_type_input_id + "Parms",compatable_parms)
        cfg.set_config_value(dt_check_data_type_input_id + "ParmsProtect",[False,False,True])

    check_html  =   grid_input_form.get_html()   
        
    common_column_heading_html      =   "<div>Check Datatype Compatability</div><br>"
     
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [common_column_heading_html,col_stats_html,check_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("check-compatability-wrapper",gridclasses,gridhtmls) 
            
    else :
        display_generic_grid("check-compatability-pop-up-wrapper",gridclasses,gridhtmls) 
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


#








