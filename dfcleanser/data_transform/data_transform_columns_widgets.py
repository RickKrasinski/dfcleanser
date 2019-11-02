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

from dfcleanser.common.common_utils import (get_datatype_id, opStatus, get_parms_for_input, display_exception,
                                            is_numeric_col, display_generic_grid, get_select_defaults, 
                                            get_datatype_str, does_col_contain_nan, is_column_in_df)

from dfcleanser.common.display_utils import display_column_names

from IPython.display import (clear_output)


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
                                                 "Sort</br>By</br>Column",
                                                 "More",
                                                 "Return","Help"]

columns_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_SAVE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_SORT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.MORE_TASKBAR)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ID) + ")"]

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
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ID) + ")"]

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
                                                 "Sort</br>By</br>Column",
                                                 "Apply</br>fn To</br>Column",
                                                  "Map</br> Column",
                                                  "Dummies</br>For</br>Column"]

columns_transform_tbB_jsList                =   ["cols_transform_tb_callback("+str(dtm.DISPLAY_COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DISPLAY_SORT_COLUMN)+")",
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
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MDC_ID) + ")"]

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
add_column_input_title                  =   "Add Column Parameters"
add_column_input_id                     =   "addcolInput"
add_column_input_idList                 =   ["addColumnName",
                                             "addColumnDataType",
                                             None,None,None,None,None]

add_column_input_labelList              =   ["new_column_name",
                                             "new_column_data_type",
                                             "Get</br>Column</br>Values</br>From</br>File",
                                             "Get</br>Column</br>Values</br>From</br>dfc</br>Functions",
                                             "Get</br>Column</br>Values</br>From</br>User</br>Code",
                                             "Get</br>Column</br>Values</br>From</br>df",
                                             "Return"]

add_column_input_typeList               =   ["text","select","button","button","button","button","button"]

add_column_input_placeholderList        =   ["enter the new column name",
                                             "enter the new column data type",
                                             None,None,None,None,None]

add_column_input_jsList                 =    [None,None,
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_FILE_OPTION) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_DFC_FUNCS) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_CODE_OPTION) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_DF_OPTION) + ")",
                                              "data_transform_display_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")"]

add_column_input_reqList                =   [0,1]

"""
#--------------------------------------------------------------------------
#    add new column - file input
#--------------------------------------------------------------------------
"""
add_column_file_input_title              =   "Add Column Parameters"
add_column_file_input_id                 =   "addcolfileInput"
add_column_file_input_idList             =   ["addfcolumnname",
                                              "addfcolumndtype",
                                              "addcolumnfname",
                                              None,None,None]

add_column_file_input_labelList          =   ["new_column_name",
                                              "new_column_data_type",
                                              "Column Values File",
                                              "Add New</br>Column</br>From File",
                                              "Return","Help"]

add_column_file_input_typeList           =   ["text","select","file",
                                              "button","button","button"]

add_column_file_input_placeholderList    =   ["enter the new column name",
                                              "enter the new column data type",
                                              "enter the file name of list to use as values",
                                              None,None,None]

add_column_file_input_jsList             =    [None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_FILE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_FILE_ID) + ")"]

add_column_file_input_reqList            =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    add new column - dfc funcs
#--------------------------------------------------------------------------
"""

add_column_code_dfc_funcs_input_title           =   "Add Column Parameters"
add_column_code_dfc_funcs_input_id              =   "addcoldfcfuncInput"
add_column_code_dfc_funcs_input_idList          =   ["addcolName",
                                                     "addcoldtype",
                                                     "addcolfuncs",
                                                     "addcolcodefcode",
                                                     "addcoldesc",
                                                     None,None,None,None]

add_column_code_dfc_funcs_input_labelList       =   ["new_column_name",
                                                     "new_column_data_type",
                                                     "generic_function",
                                                     "function_code",
                                                     "function_description",
                                                     "Add New</br>Column</br>From Code",
                                                     "Clear","Return","Help"]

add_column_code_dfc_funcs_input_typeList        =   ["text","select","select",
                                                     maketextarea(5),maketextarea(10),
                                                     "button","button","button","button"]

add_column_code_dfc_funcs_input_placeholderList =   ["enter the new column name",
                                                     "enter the column data type",
                                                     "generic function",
                                                     "function code",
                                                     "function description",
                                                     None,None,None,None]

add_column_code_dfc_funcs_input_jsList          =    [None,None,None,None,None,
                                                      "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_DFC_FUNCS) + ")",
                                                      "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                                      "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                                      "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_code_dfc_funcs_input_reqList         =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    display add column from dfc funcs objects
#--------------------------------------------------------------------------
""" 

add_column_code_dfc_funcs_parms_input_title           =   "Add Column Parameters"
add_column_code_dfc_funcs_parms_input_id              =   "addcoldfcfuncInput"
add_column_code_dfc_funcs_parms_input_idList          =   ["addcolName",
                                                           "addcoldtype",
                                                           "addcolfuncs",
                                                           "addcolcodefcode",
                                                           "addcoldesc"]

add_column_code_dfc_funcs_parms_input_labelList       =   ["new_column_name",
                                                           "new_column_data_type",
                                                           "dfc_function",
                                                           "function_call",
                                                           "function_description"]

add_column_code_dfc_funcs_parms_input_labelList1      =   ["Add New</br>Column</br>From Code",
                                                           "Clear","Return","Help"]

add_column_code_dfc_funcs_parms_input_typeList        =   ["text","select","select",
                                                           maketextarea(5),maketextarea(10)]

add_column_code_dfc_funcs_parms_input_placeholderList =   ["enter the new column name",
                                                           "enter the column data type",
                                                           "generic function",
                                                           "function code",
                                                           "function description"]

add_column_code_dfc_funcs_parms_input_jsList          =    [None,None,None,None,None]

add_column_code_dfc_funcs_parms_input_jsList1         =    ["data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_DFC_FUNCS) + ")",
                                                            "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                                            "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                                            "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_code_dfc_funcs_parms_input_reqList         =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    add new column - user code
#--------------------------------------------------------------------------
"""

add_column_code_gf_input_title           =   "Add Column Parameters"
add_column_code_gf_input_id              =   "addcolcodeInput"
add_column_code_gf_input_idList          =   ["addColumnName",
                                              "addColumndtype",
                                              "addcolmodule",
                                              "addcolname",
                                              "addcolcodefcode",
                                              None,None,None,None]

add_column_code_gf_input_labelList       =   ["new_column_name",
                                              "new_column_data_type",
                                              "function_module",
                                              "function_name",
                                              "function_code",
                                              "Add New</br>Column</br>From Code",
                                              "Clear","Return","Help"]

add_column_code_gf_input_typeList        =   ["text","select","text","text",maketextarea(5),
                                              "button","button","button","button"]

add_column_code_gf_input_placeholderList =   ["enter the new column name",
                                              "enter the column data type",
                                              "function module",
                                              "function name",
                                              "function code",
                                              None,None,None,None]

add_column_code_gf_input_jsList          =    [None,None,None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_code_gf_input_reqList         =   [0,1,2,3,4]



"""
#--------------------------------------------------------------------------
#    add new column - df
#--------------------------------------------------------------------------
"""

add_column_df_input_title               =   "Add Column Parameters"
add_column_df_input_id                  =   "addcoldfInput"
add_column_df_input_idList              =   ["addcoloutdftitle",
                                             "addcoldfcname",
                                             "addcoldfd",
                                             "addcoldftitle",
                                             "addcolddfcname",
                                             "addcolddfoindex",
                                             "addcolddfsindex",
                                             "addcolddfbafill",
                                             None,None,None,None]

add_column_df_input_labelList           =   ["output_dataframe_title",
                                             "new_output_column_name",
                                             "new_output_column_data_type",
                                             "source_dataframe_title",
                                             "source_dataframe_column_name",
                                             "output_dataframe_index_column_name",
                                             "source_dataframe_index_column_name",
                                             "na_fill_value",
                                             "Add New</br>Column</br>From df",
                                             "Clear","Return","Help"]

add_column_df_input_typeList            =   ["select","text","select","select","select","select","select","text",
                                             "button","button","button","button"]

add_column_df_input_placeholderList     =   ["enter the output dataframe title",
                                             "enter the new column name",
                                             "enter the column data type",
                                             "enter the source dataframe title",
                                             "enter the source column name",
                                             "enter the output index column name",
                                             "enter the source index column name",
                                             "enter the na fill value",
                                             None,None,None,None]

add_column_df_input_jsList              =    [None,None,None,None,None,None,None,None,
                                              "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_FROM_DF_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_df_input_reqList             =   [0,1,2,3,4]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    ytransform columns display objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#    rename column input for single column
#--------------------------------------------------------------------------
"""
rename_column_input_title               =   "Column Naming Parameters"
rename_column_input_id                  =   "renamecolInput"
rename_column_input_idList              =   ["renamecolumnname",
                                             "renameoldColumnName",
                                             "renamecolInput_inplace",
                                             "renamecolInput_resultdf",
                                             None,None,None]

rename_column_input_labelList           =   ["new_column_name",
                                             "column_to_rename",
                                             "inplace",
                                             "result_df_title",
                                             "Rename</br> Column",
                                             "Return","Help"]

rename_column_input_typeList            =   ["text","select","select","text",
                                             "button","button","button"]

rename_column_input_placeholderList     =   ["enter the new column name",
                                             "column name",
                                             "rename column inplace",
                                             "result df title (ignored if inplace = True)",
                                             None,None,None]

rename_column_input_jsList              =   [None,None,None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_RENAME_COLUMN)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "display_help_url('" + dfchelp.RENAME_COL + "')"]

rename_column_input_reqList             =   [0,1,2]




"""
#--------------------------------------------------------------------------
#    drop column
#--------------------------------------------------------------------------
"""
drop_column_input_title                 =   "Drop Column Parameters"
drop_column_input_id                    =   "dropcolInput"
drop_column_input_idList                =   ["dropcolInput_name",
                                             "dropcolInput_inplace",
                                             "dropcolInput_resultdf",
                                             "dropColumnFname",
                                             None,None,None]

drop_column_input_labelList             =   ["column_to_drop",
                                             "inplace",
                                             "result_df_title",
                                             "file_save_name",
                                             "Drop</br> Column",
                                             "Return","Help"]

drop_column_input_typeList              =   ["select","select","text","file",
                                             "button","button","button"]

drop_column_input_placeholderList       =   ["drop column name",
                                             "drop column inplace",
                                             "result df title (ignored if inplace = True)",
                                             "enter File name to save dropped column to or browse to file below (default no save)",
                                             None,None,None]

drop_column_input_jsList                =    [None,None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_DROP_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "display_help_url('" + dfchelp.DROP_COL + "')"]

drop_column_input_reqList               =   [0,1]

"""
#--------------------------------------------------------------------------
#    save column
#--------------------------------------------------------------------------
"""
save_column_input_title                 =   "Save Column Parameters"
save_column_input_id                    =   "savecolInput"
save_column_input_idList                =   ["saveColumnname",
                                             "saveColumnFname",
                                             None,None,None]

save_column_input_labelList             =   ["column_to_save",
                                             "file_save_name",
                                             "Save</br> Column",
                                             "Return","Help"]

save_column_input_typeList              =   ["select","file",
                                             "button","button","button"]

save_column_input_placeholderList       =   ["column to save",
                                             "enter File name to save dropped column to or browse to file below (default no save)",
                                             None,None,None]

save_column_input_jsList                =    [None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_SAVE_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_SAVE_ID) + ")"]

save_column_input_reqList               =   [0,1]

"""
#--------------------------------------------------------------------------
#    reorder columns
#--------------------------------------------------------------------------
"""
reorder_columns_input_title              =   "Reorder Column Parameters"
reorder_columns_input_id                 =   "reordercolInput"
reorder_columns_input_idList             =   ["moveColumnname",
                                              "moveafterColumnname",
                                              None,None,None]

reorder_columns_input_labelList          =   ["column_to_move",
                                              "column_to_move_after",
                                              "Move</br> Column",
                                              "Return","Help"]

reorder_columns_input_typeList           =   ["select","select",
                                              "button","button","button"]

reorder_columns_input_placeholderList    =   ["column to move",
                                              "column to move after", 
                                              None,None,None]

reorder_columns_input_jsList             =    [None,None,
                                               "data_transform_process_cols_callback("+str(dtm.PROCESS_REORDER_COLUMNS)+")",
                                               "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_REORDER_ID) + ")"]

reorder_columns_input_reqList            =   [0,1]

"""
#--------------------------------------------------------------------------
#    copy columns
#--------------------------------------------------------------------------
"""
copy_columns_input_title                =   "Copy Column Parameters"
copy_columns_input_id                   =   "copycolInput"
copy_columns_input_idList               =   ["copyColumnname",
                                             "copyfromColumnname",
                                             None,None,None]

copy_columns_input_labelList            =   ["column_to_copy_to",
                                             "column_to_copy_from",
                                             "Copy</br>Column",
                                             "Return","Help"]

copy_columns_input_typeList             =   ["select","select",
                                             "button","button","button"]

copy_columns_input_placeholderList      =   ["column to copy",
                                             "column to copy to", 
                                             None,None,None]

copy_columns_input_jsList               =    [None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_COPY_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_COPY_ID) + ")"]

copy_columns_input_reqList              =   [0,1]

"""
#--------------------------------------------------------------------------
#    sort by column
#--------------------------------------------------------------------------
"""
sort_column_input_title                 =   "Sort Column Parameters"
sort_column_input_id                    =   "sortcolInput"
sort_column_input_idList                =   ["sortcolname",
                                             "sortcolInput_inplace",
                                             "sortcolInput_resultdf",
                                             "sortOrder",
                                             "sortkind",
                                             "sortna",
                                             "resetRowIds",
                                             None,None,None]

sort_column_input_labelList             =   ["column_to_sort_by",
                                             "inplace",
                                             "result_df_title",
                                             "ascending_order_flag",
                                             "kind",
                                             "na_position",
                                             "reset_row_index_flag",
                                             "Sort By</br>Column",
                                             "Return","Help"]

sort_column_input_typeList              =   ["select","select","text","select","select","select","select",
                                             "button","button","button"]

sort_column_input_placeholderList       =   ["column to sort by)",
                                             "drop column inplace (default True)",
                                             "result df title (ignored if inplace = True)",
                                             "ascending sort order (default = False)",
                                             "sort method (default = quicksort)",
                                             "na position (default = last)",
                                             "reorder the row id column after the sort (default True)",
                                             None,None,None]

sort_column_input_jsList                =    [None,None,None,None,None,None,None,
                                              "data_transform_process_cols_callback("+str(dtm.PROCESS_SORT_COLUMN)+")",
                                              "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                              "display_help_url('" + dfchelp.SORT_COL + "')"]

sort_column_input_reqList               =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    apply lambda fn column
#--------------------------------------------------------------------------
"""
apply_column_lambda_input_title              =   "Apply dfc fn To Column Parameters"
apply_column_lambda_input_id                 =   "applylcolInput"
apply_column_lambda_input_idList             =   ["currentdf",
                                                  "applycolname",
                                                  "fnlfnsel",
                                                  "fntoapply",
                                                  None,None,None,None]

apply_column_lambda_input_labelList          =   ["dataframe_to_apply_fn_to",
                                                  "column_to_apply_fn_to",
                                                  "dfc_fns",
                                                  "function_code",
                                                  "Apply</br>fn To</br>Column",
                                                  "Clear","Return","Help"]

apply_column_lambda_input_typeList           =   ["select","select","select",maketextarea(5),
                                                  "button","button","button","button"]

apply_column_lambda_input_placeholderList    =   ["dataframe to apply fn to",
                                                  "column to apply fn to",
                                                  "dfc function",
                                                  "function code",
                                                  None,None,None,None]

apply_column_lambda_input_jsList             =    [None,None,None,None,
                                                   "data_transform_process_cols_callback("+str(dtm.PROCESS_APPLY_COLUMN)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.DISPLAY_CLEAR_COLUMN)+")",
                                                   "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                                   "displayhelp(" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + ")"]

apply_column_lambda_input_reqList            =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    apply fn with gf to column
#--------------------------------------------------------------------------
"""
"""
apply_column_gf_input_title              =   "Apply fn To Column Parameters"
apply_column_gf_input_id                 =   "applycolInput"
apply_column_gf_input_idList             =   ["currentdf",
                                              "applycolname",
                                              "fmodule",
                                              "fnname",
                                              "fnselect",
                                              "fntoapply",
                                              None,None,None,None,None,None]

apply_column_gf_input_labelList          =   ["dataframe to apply fn to",
                                              "column_to_apply_fn_to",
                                              "function_module",
                                              "function_name",
                                              "generic functions",
                                              "function_call",
                                              "Save as</br>Generic</br>Function",
                                              "Apply</br>fn To</br>Column",
                                              "Show</br>fn</br>Code",
                                              "Clear","Return","Help"]

apply_column_gf_input_typeList           =   ["text","text","text","text","select",maketextarea(5),
                                              "button","button","button","button","button","button"]

apply_column_gf_input_placeholderList    =   ["dataframe to apply fn to",
                                              "column to apply fn to",
                                              "function module",
                                              "function name ",
                                              "generic function",
                                              "function to apply",
                                              None,None,None,None,None,None]

apply_column_gf_input_jsList             =    [None,None,None,None,None,None,
                                               "data_transform_apply_fn_callback(1," + str(dtm.APPLY_FN_COLUMN_SAVE) + ")",
                                               "data_transform_apply_fn_callback(1," + str(dtm.APPLY_FN_COLUMN_APPLY)+")",
                                               "data_transform_apply_fn_callback(1," + str(dtm.APPLY_FN_COLUMN_SHOW)+")",
                                               "data_transform_apply_fn_callback(1," + str(dtm.APPLY_FN_COLUMN_CLEAR)+")",
                                               "data_transform_apply_fn_callback(1," + str(dtm.APPLY_FN_COLUMN_RETURN)+")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + ")"]

apply_column_gf_input_reqList            =   [0,1,2,3,4]
"""

"""
#--------------------------------------------------------------------------
#    apply fn with gf to column details
#--------------------------------------------------------------------------
"""
"""
apply_column_gf_det_input_title              =   "Apply fn To Column Parameters"
apply_column_gf_det_input_id                 =   "applydcolInput"
apply_column_gf_det_input_idList             =   ["currentdf",
                                                  "applyColumnname",
                                                  "fmodule",
                                                  "fnname",
                                                  "fndselect",
                                                  "fntoapply",
                                                  "fndesc",
                                                  None,None,None,None,None]

apply_column_gf_det_input_labelList          =   ["dataframe to apply fn to",
                                                  "column_to_apply_fn_to",
                                                  "function_module",
                                                  "function_name",
                                                  "generic functions",
                                                  "function_call",
                                                  "function_description",
                                                  "Create</br>New</br>Function",
                                                  "Apply Fn</br>To Column",
                                                  "Clear","Return","Help"]

apply_column_gf_det_input_typeList           =   ["text","text","text","text","select",maketextarea(5),maketextarea(10),
                                                  "button","button","button","button","button"]

apply_column_gf_det_input_placeholderList    =   ["dataframe to apply fn to",
                                                  "column to apply fn to",
                                                  "function module",
                                                  "function name ",
                                                  "generic function",
                                                  "function to apply",
                                                  "function description",
                                                  None,None,None,None,None,None]

apply_column_gf_det_input_jsList             =    [None,None,None,None,None,None,None,
                                                   "data_transform_apply_fn_callback(2," + str(dtm.APPLY_FN_COLUMN_SAVE) + ")",
                                                   "data_transform_apply_fn_callback(2," + str(dtm.APPLY_FN_COLUMN_APPLY)+")",
                                                   "data_transform_apply_fn_callback(2," + str(dtm.APPLY_FN_COLUMN_CLEAR)+")",
                                                   "data_transform_apply_fn_callback(2," + str(dtm.APPLY_FN_COLUMN_RETURN)+")",
                                                   "displayhelp(" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + ")"]

apply_column_gf_det_input_reqList            =   [0,1,2,3,4]

"""

"""
#--------------------------------------------------------------------------
#    data transform map input for single column
#--------------------------------------------------------------------------
"""
transform_map_input_title               =   "Column Mapping Parameters"
transform_map_input_id                  =   "maptransformInput"
transform_map_input_idList              =   ["mapcolumnname",
                                             "mapkeys",
                                             "mapvals",
                                             "handlena",
                                             "mapfn",
                                             "mapfilename",
                                             None,None,None,None,None]

transform_map_input_labelList           =   ["mapping_column_name",
                                             "mapping_keys",
                                             "mapping_values",
                                             "handle_nan",
                                             "mapping_function",
                                             "mapping_values_list_file_name",
                                             "Map</br>Column</br>from</br>File",
                                             "Map</br>Column</br>from</br>Values",
                                             "Map</br>Column</br>from</br>Function",
                                             "Return","Help"]

transform_map_input_typeList            =   ["select",maketextarea(5),maketextarea(5),
                                             "select",maketextarea(5),"file",
                                             "button","button","button","button","button"]

transform_map_input_placeholderList     = ["column to map",
                                           "mapping keys",
                                           "enter mapping values (comma separated)",
                                           "ignore Nans (default = True)",
                                           "mapping function to generate mapping values ",
                                           "enter File name containing mapping or browse to file below",
                                           None,None,None,None,None]

transform_map_input_jsList              = [None,None,None,None,None,None,
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN)+")",
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN_VALUES)+")",
                                           "data_transform_process_cols_callback("+str(dtm.PROCESS_MAP_COLUMN_FUNCTION)+")",
                                           "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                           "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MAP_ID) + ")"]

transform_map_input_reqList             =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    data transform dummy input 
#--------------------------------------------------------------------------
"""
transform_dummy_input_title             =   "Column Dummies Parameters"
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
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DUMMY_ID) + ")"]

transform_dummy_input_reqList           =   [0,1]

"""
#--------------------------------------------------------------------------
#    data transform category input 
#--------------------------------------------------------------------------
"""
transform_category_input_title          =   "Column Category Parameters"
transform_category_input_id             =   "categorytransformInput"
transform_category_input_idList         =   ["catcolumnname",
                                             "ordinalcol",
                                             "convertcol",
                                             None,None,None]

transform_category_input_labelList      =   ["categorical_column_name",
                                             "make_column_categorical_flag",
                                             "change_column_datatype_to_category_datatype_flag",
                                             "Make</br>Column</br>Categorical",
                                             "Return","Help"]

transform_category_input_typeList       =   ["select","select","select","button","button","button"]

transform_category_input_placeholderList =  ["column to make categorical",
                                             "make column categorical (default = True)",
                                             "convert column to category datatype (default = False)",
                                             None,None,None]

transform_category_input_jsList         =   [None,None,None,
                                             "data_transform_process_cols_callback("+str(dtm.PROCESS_CAT_COLUMN)+")",
                                             "data_transform_process_cols_callback("+str(dtm.RETURN_CLEAR_COLUMN)+")",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_CAT_ID) + ")"]

transform_category_input_reqList        =   [0,1,2]




"""
#--------------------------------------------------------------------------
#   datatype no nons 
#--------------------------------------------------------------------------
"""
dt_data_type_input_title                =   "Change Data Type Parameters"
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
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_data_type_input_reqList              =   [0,1]


"""
#--------------------------------------------------------------------------
#   datatype nons with fillna 
#--------------------------------------------------------------------------
"""
dt_nans_data_type_input_title           =   "Change Data Type Parameters"
dt_nans_data_type_input_id              =   "dtfndatatypeinput"
dt_nans_data_type_input_idList          =   ["dtcolname",
                                             "dtdatatype",
                                             "dtnaopt",
                                             "dtfillnavalue",
                                             "dtfillnamethod",
                                             "dtfillnalimit",
                                             None,None,None,None,None]

dt_nans_data_type_input_labelList       =   ["column_to_change_datatype",
                                             "datatype",
                                             "na_option",
                                             "fillna_value",
                                             "fillna_method",
                                             "fillna_limit",
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
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_nans_data_type_input_reqList         =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#   datatype nons with dropna 
#--------------------------------------------------------------------------
"""
dt_drop_nans_data_type_input_title           =   "Change Data Type Parameters"
dt_drop_nans_data_type_input_id              =   "dtdndatatypeinput"
dt_drop_nans_data_type_input_idList          =   ["dtcolname",
                                                  "dtdatatype",
                                                  "dtnaopt",
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
                                                  "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_drop_nans_data_type_input_reqList         =   [0,1,2,3,4]




"""
ndt_data_type_dn_input_idList           =   ["dtanyall",
                                             "dtthreshold",
                                             "inplace",
                                             None,None,None]

ndt_data_type_dn_input_labelList        =   [
                                             "inplace",
                                             "Drop</br>Nans",
                                             "Return","Help"]

ndt_data_type_dn_input_typeList         =   ["select","text","select",
                                             "button","button","button"]

ndt_data_type_dn_input_placeholderList  =   ["drop any or all",
                                             "dropna threshold (default : None)",
                                             "dropna inplace",
                                             None,None,None]

ndt_data_type_dn_input_jsList           =   [None,None,None,
                                             "process_cols_dropna_fillna_transform_callback(5)",
                                             "process_cols_dropna_fillna_transform_callback(0)",
                                             "display_help_url('" + str(dfchelp.PANDAS_DROPNA) + "')"]
"""








"""
#--------------------------------------------------------------------------
#   change data type input no buttons
#--------------------------------------------------------------------------
"""
"""
dt_data_type_nb_input_title             =   "Change Data Type Parameters"
dt_data_type_nb_input_id                =   "dtdatatypeinput"
dt_data_type_nb_input_idList            =   ["dtdatatype"]

dt_data_type_nb_input_labelList         =   ["datatype"]

dt_data_type_nb_input_typeList          =   ["select"]

dt_data_type_nb_input_placeholderList   =   ["datatype selected"]

dt_data_type_nb_input_jsList            =   [None]

dt_data_type_nb_input_reqList           =   [0]
"""

"""
#--------------------------------------------------------------------------
#   check column datatype compatability 
#--------------------------------------------------------------------------
"""
dt_check_data_type_input_title           =   "Check Column Compatability Parameters"
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
                                              "process_transform_check_compatability(2)",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_check_data_type_input_reqList         =   [0,1]


"""
#--------------------------------------------------------------------------
#   check column str datatype compatability 
#--------------------------------------------------------------------------
"""
dt_str_check_data_type_input_title           =   "Check Column Compatability Parameters"
dt_str_check_data_type_input_id              =   "checkstrdtinput"
dt_str_check_data_type_input_idList          =   ["checkdtcolname",
                                                  "checkdtdatatypes",
                                                  "checkdtdatatypesok",
                                                  "checkdtsmaplesize",
                                                  None,None,None,None]

dt_str_check_data_type_input_labelList       =   ["column_to_check_datatype_compatability",
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
                                                  "process_transform_check_compatability(1)",
                                                  "process_transform_check_compatability(2)",
                                                  "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_str_check_data_type_input_reqList         =   [0,1]









datatransform_cols_inputs   =   [rename_column_input_id,add_column_input_id,add_column_file_input_id,
                                 add_column_code_gf_input_id,add_column_df_input_id,drop_column_input_id,
                                 save_column_input_id,reorder_columns_input_id,copy_columns_input_id,
                                 sort_column_input_id,apply_column_lambda_input_id,transform_map_input_id,
                                 transform_dummy_input_id,transform_category_input_id,
                                 dt_nans_data_type_input_id,dt_drop_nans_data_type_input_id,
                                 dt_data_type_input_id,dt_check_data_type_input_id,dt_str_check_data_type_input_id]


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
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
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
        display_generic_grid("df-common-col-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-common-col-pop-up-wrapper",gridclasses,gridhtmls)

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
        
        inplacesel      =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)

    if(option == dtm.DISPLAY_DROP_COLUMN) :
        
        common_column_heading_html      =   "<div>Drop Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(rename_column_input_id,
                                                      rename_column_input_idList,
                                                      rename_column_input_labelList,
                                                      rename_column_input_typeList,
                                                      rename_column_input_placeholderList,
                                                      rename_column_input_jsList,
                                                      rename_column_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname, "list" : colslist, "size" : 10, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
        
        inplacesel      =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
        get_select_defaults(grid_input_form,
                            rename_column_input_id,
                            rename_column_input_idList,
                            rename_column_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    elif(option == dtm.DISPLAY_REORDER_COLUMNS) : 
        
        common_column_heading_html      =   "<div>Reorder Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()

        grid_input_form     =   InputForm(reorder_columns_input_id,
                                          reorder_columns_input_idList,
                                          reorder_columns_input_labelList,
                                          reorder_columns_input_typeList,
                                          reorder_columns_input_placeholderList,
                                          reorder_columns_input_jsList,
                                          reorder_columns_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname, "list" : colslist, "size" : 5}
        selectDicts.append(cnames)
        selectDicts.append(cnames)
           
        get_select_defaults(grid_input_form,
                            reorder_columns_input_id,
                            reorder_columns_input_idList,
                            reorder_columns_input_typeList,
                            selectDicts)

        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":40})
        grid_input_form.set_gridwidth(480)
        grid_input_html   =   grid_input_form.get_html()
    
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note("")
        col_names_html  =   display_column_names(df,col_names_table,None,False)
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,col_names_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_SAVE_COLUMN) :
        
        common_column_heading_html      =   "<div>Save Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(save_column_input_id,
                                                      save_column_input_idList,
                                                      save_column_input_labelList,
                                                      save_column_input_typeList,
                                                      save_column_input_placeholderList,
                                                      save_column_input_jsList,
                                                      save_column_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname, "list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)
        
        get_select_defaults(grid_input_form,
                            save_column_input_id,
                            save_column_input_idList,
                            save_column_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0}) 
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_COPY_COLUMN) :
        
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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,blank_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_SORT_COLUMN) :
        
        common_column_heading_html      =   "<div>Drop Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form                 =   InputForm(sort_column_input_id,
                                                      sort_column_input_idList,
                                                      sort_column_input_labelList,
                                                      sort_column_input_typeList,
                                                      sort_column_input_placeholderList,
                                                      sort_column_input_jsList,
                                                      sort_column_input_reqList)
        
        selectDicts     =   []
        
        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)

        inplacesel      =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(inplacesel)
        
        ordersel        =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(ordersel)
        
        kindsel         =   {"default" : "'quicksort'","list" : ["'quicksort'","'mergesort'","'heapsort'"]}
        selectDicts.append(kindsel)
        
        napossel        =   {"default" : "'last'","list" : ["'first'","'last'"]}
        selectDicts.append(napossel)
        
        resetsel        =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(resetsel)
           
        get_select_defaults(grid_input_form,
                            sort_column_input_id,
                            sort_column_input_idList,
                            sort_column_input_typeList,
                            selectDicts)
        
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(df,colname,False)
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_html     =   grid_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_APPLY_COLUMN) :
        
        df,colslist,colname             =   get_df_colslist()
        display_apply_fn_inputs(colname,None)
    
    if(option == dtm.DISPLAY_APPLY_COLUMN_UPDATE) :
        
        df,colslist,colname             =   get_df_colslist()
        display_apply_fn_inputs(colname,parms)


    if(option == dtm.DISPLAY_MAP_COLUMN) :
        
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
                keyslist = (keyslist + str(","))
        
        if(len(keyslist) > 300) :
            parmslist = ["","","mapping keys too large to define by hand","",""]
            parmsProtect = [False,False,True,True,False]
        else :
            parmslist = ["","",keyslist,"",""]
            parmsProtect = [False,False,True,False,False]
        
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
        
        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)

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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_DUMMIES_COLUMN) :
        
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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)


    if(option == dtm.DISPLAY_CAT_COLUMN) :
        
        common_column_heading_html      =   "<div>Categories for Column</div><br>"
        
        df,colslist,colname             =   get_df_colslist()
        
        grid_input_form     =   InputForm(transform_category_input_id,
                                          transform_category_input_idList,
                                          transform_category_input_labelList,
                                          transform_category_input_typeList,
                                          transform_category_input_placeholderList,
                                          transform_category_input_jsList,
                                          transform_category_input_reqList)
        
        selectDicts     =   []

        cnames          =   {"default" : colname,"list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)

        catsel          =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(catsel)
        
        catsel          =   {"default" : "False","list" : ["True","False"]}
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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        display_dct_form(gridclasses,gridhtmls)

    if(option == dtm.DISPLAY_DATATYPE_COLUMN) :
        
        df,colslist,colname             =   get_df_colslist()
        if(not (parms is None)) :
            print("dtm.DISPLAY_DATATYPE_COLUMN",parms)
            colname     =   parms[0]
        
        display_convert_datatype(df,colname,False,False,cfg.DataTransform_ID)
        
    elif(option == dtm.DISPLAY_DATATYPE_CHANGE_NA) :
        print("dtm.DISPLAY_DATATYPE_CHANGE_NA",parms)
        
        df,colslist,colname             =   get_df_colslist()

        if(parms[1] == "fillna") :
            display_convert_datatype(df,parms[0],True,False,cfg.DataTransform_ID) 
        else :
            display_convert_datatype(df,parms[0],False,True,cfg.DataTransform_ID) 
        
    if(option == dtm.DISPLAY_CHECK_COMPATABILITY) :
        
        display_check_compatability(parms,False) 
        
    if(option == dtm.DISPLAY_CHECK_COMPATABILITY_UNIQUES) :
        
        display_check_compatability(None,True)        
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display apply fn onjects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 
apply_column_lambda_parms_input_id                 =   "applylfntocolInput"

apply_fn_idList                      =   []

def get_current_apply_fn_idList() :
    return(apply_fn_idList)
def set_current_apply_fn_idList(idlist) :
    global apply_fn_idList
    apply_fn_idList = idlist


def display_apply_fn_inputs(colname,parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the apply function to column parms
    * 
    * parms :
    *  colname  -   column name
    *  genfuncs -   display generic funcs flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    if(parms is None) :
        column_name     =   colname
    else :
        column_name     =   parms[0]
        
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                          column_name,
                                          False,
                                          True)
        
    if(parms is None) :
        
        ftitle  =   None
 
        applyfn_input_form = InputForm(apply_column_lambda_input_id,
                                       apply_column_lambda_input_idList,
                                       apply_column_lambda_input_labelList,
                                       apply_column_lambda_input_typeList,
                                       apply_column_lambda_input_placeholderList,
                                       apply_column_lambda_input_jsList,
                                       apply_column_lambda_input_reqList)
        
    else :
        
        ftitle  =   parms[1]
    
        dfc_apply_idList, dfc_apply_labelList, dfc_apply_typeList          =   [],[],[]
        dfc_apply_placeholderList, dfc_apply_jsList, dfc_apply_reqList     =   [],[],[]
    
        for i in range(4)           :     
            dfc_apply_idList.append(apply_column_lambda_input_idList[i])
            dfc_apply_labelList.append(apply_column_lambda_input_labelList[i])
            dfc_apply_typeList.append(apply_column_lambda_input_typeList[i])
            dfc_apply_placeholderList.append(apply_column_lambda_input_placeholderList[i])
            dfc_apply_jsList.append(apply_column_lambda_input_jsList[i])
            dfc_apply_reqList.append(apply_column_lambda_input_reqList[i])

        from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_apply_function_parms
        kwargs  =   get_apply_function_parms(ftitle)
        
        if(not(kwargs is None)) :
            for i in range(len(kwargs)) :
                dfc_apply_idList.append("applyfnfparm"+str(i))    
                dfc_apply_labelList.append(kwargs[i])    
                dfc_apply_typeList.append("text")    
                dfc_apply_placeholderList.append(kwargs[i])    
                dfc_apply_jsList.append(None)    
                dfc_apply_reqList.append(i+4) 
        
        for i in range(4) :
            dfc_apply_idList.append(None)
            dfc_apply_typeList.append("button")    
            dfc_apply_placeholderList.append(None)
        
        for i in range(4) :
            dfc_apply_labelList.append(apply_column_lambda_input_labelList[i+4])    
            dfc_apply_jsList.append(apply_column_lambda_input_jsList[i+4])
            
        set_current_apply_fn_idList(dfc_apply_idList)

        applyfn_input_form   = InputForm(apply_column_lambda_parms_input_id,
                                         dfc_apply_idList,
                                         dfc_apply_labelList,
                                         dfc_apply_typeList,
                                         dfc_apply_placeholderList,
                                         dfc_apply_jsList,
                                         dfc_apply_reqList)
        
    selectDicts     =   []
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    current_df_name     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
    dataframes          =   {"default":current_df_name,"list":dataframes_loaded, "callback":"change_apply_df_callback"}
    selectDicts.append(dataframes)
        
    current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colnames[0],"list": colnames, "callback":"change_col_stats_callback"}
    selectDicts.append(cnames)
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import applyfns
    
    fns             =   [""]
    for i in range(len(applyfns)) :
        fns.append(applyfns[i])
        
    if(parms is None) :
        lambdas         =   {"default":"","list":fns,"callback":"get_apply_fn"}
    else :
        lambdas         =   {"default":ftitle,"list":fns,"callback":"get_apply_fn"}
        
    selectDicts.append(lambdas)
        
    get_select_defaults(applyfn_input_form,
                        apply_column_lambda_input_id,
                        apply_column_lambda_input_idList,
                        apply_column_lambda_input_typeList,
                        selectDicts)
        
    applyfn_input_form.set_buttonstyle({"font-size":13, "height":75, "width":110, "left-margin":5})
    applyfn_input_form.set_gridwidth(480)
    applyfn_input_form.set_shortForm(True)
    applyfn_input_form.set_fullparms(True)
    
    currenttransformdf  =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF) 
    
    if(parms is None) :
        cfg.set_config_value(apply_column_lambda_input_id+"Parms",[currenttransformdf,column_name,"",""])
    else :
        
        if(ftitle.find("lambda") > -1) :
            fncode  =  "df['" + column_name + "'] = df['" + column_name + "'].apply(" + ftitle + ")" 
        else :
            fncode  =   ftitle.replace("(","")
            fncode  =   fncode.replace(")","")
            fncode  =  "df['" + column_name + "'] = df['" + column_name + "'].apply(" + ftitle + ", axis=1)"

        apply_parms     =   [currenttransformdf,column_name,ftitle,fncode]
        
        if(not(kwargs is None)) :
            for i in range(len(kwargs)) :
                apply_parms.append("")
            
        cfg.set_config_value(apply_column_lambda_parms_input_id+"Parms",apply_parms)
        
    applyfn_input_html = ""
    applyfn_input_html = applyfn_input_form.get_html()
    
    applyfn_heading_html      =   "<div>" + apply_column_lambda_input_title + "</div><br>"

    dtype_mismatch  =   False

    if(not(ftitle is None)) :        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_apply_function_return_datatype
        fn_dtype    =   get_apply_function_return_datatype(ftitle)
    
        from dfcleanser.common.common_utils import is_float_col,is_int_col,is_string_col,is_object_col,is_numeric_col
        if(fn_dtype == "numeric") :
            if(not(is_numeric_col(current_df,column_name))) :
                dtype_mismatch  =   True
        elif(fn_dtype == "float") :
            if(not(is_float_col(current_df,column_name))) :
                dtype_mismatch  =   True
        elif(fn_dtype == "int") :
            if(not(is_int_col(current_df,column_name))) :
                dtype_mismatch  =   True
        else :
            if( (not(is_string_col(current_df,column_name))) and
               (not(is_object_col(current_df,column_name))) ): 
                dtype_mismatch  =   True
    
    if(dtype_mismatch) :
        help_note           =   "'column_to_apply_fn_to' datatype does not match fn datatype."
        from dfcleanser.common.common_utils import get_help_note_warning_html
        applyfn_notes_html   =   get_help_note_warning_html(help_note)
    else :
        if(parms is None) :
            help_note           =   "Select a dfc fn to run or enter function code."
        else :
            help_note           =   "The 'df' in function_code is filled in with the 'dataframe_to_apply_fn_to' value.</br>To apply the fn hit the 'Apply fn to Column' key."
            
        from dfcleanser.common.common_utils import get_help_note_html
        applyfn_notes_html   =   get_help_note_html(help_note)

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-main","dfc-footer"]
        gridhtmls       =   [applyfn_heading_html,col_stats_html,applyfn_input_html,applyfn_notes_html]
        
        display_generic_grid("generic-gf-transform-wrapper",gridclasses,gridhtmls)
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-main","dfc-footer"]
        gridhtmls       =   [applyfn_heading_html,col_stats_html,applyfn_input_html,applyfn_notes_html]
        
        display_generic_grid("generic-gf-transform-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display add column specific methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    
def parse_add_cols_option_inputs(option,parms,opstat=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : parse parms for add columns
    * 
    * parms :
    *   parms   -   add column parms
    *   opstat  -   status var
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    newcolname      =   ""
    newdatatytpe    =   ""
    fparms          =   []

    if(len(parms)>0) :
        
        if( (option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) or
            (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) or
            (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS_PARMS) or
            (option == dtm.DISPLAY_ADD_FROM_CODE_OPTION) or 
            (option == dtm.DISPLAY_ADD_FROM_DF_OPTION) ) :
            
            fparms = get_parms_for_input(parms[0],add_column_input_idList)
    
        if(len(fparms) > 0) :
            newcolname      =   fparms[0]
            if(len(fparms) > 1) :
                newdatatytpe    =   fparms[1]
       
        if(len(newcolname) > 0) :
            cfg.set_config_value(cfg.ADD_COL_COL_NAME_KEY,newcolname)

        if(len(newdatatytpe) > 0) :
            cfg.set_config_value(cfg.ADD_COL_DATATYPE_ID_KEY,newdatatytpe)
    
    # check if user entered new column name    
    if(len(newcolname) > 0) :
        
        # check if new column name already exists
        collist = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist()
        found = False
        if(newcolname in collist) :
            found = True
        if(not found) :
        
            if(option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
                cfg.set_config_value(add_column_file_input_id + "Parms",[newcolname,newdatatytpe,""]) 
            elif(option == dtm.DISPLAY_ADD_FROM_CODE_OPTION ) :
                cfg.set_config_value(add_column_code_gf_input_id + "Parms",[newcolname,newdatatytpe,"",""])
            elif(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
                cfg.set_config_value(add_column_code_gf_input_id + "Parms",[newcolname,newdatatytpe,"",""])
            elif(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS_PARMS) :
                cfg.set_config_value(add_column_code_gf_input_id + "Parms",[newcolname,newdatatytpe,"","","","","","",""]) 
            elif(option == dtm.DISPLAY_ADD_FROM_DF_OPTION ) :
                cfg.set_config_value(add_column_code_gf_input_id + "Parms",[newcolname,newdatatytpe,"",""]) 
                
        else :
            cfg.drop_config_value(add_column_file_input_id+"Parms")    
            cfg.drop_config_value(add_column_code_gf_input_id+"Parms")
            
            opstat.set_status(False)
            opstat.set_errorMsg("   [Column Name Error] : column " + newcolname + " already exists")

    return([newcolname,newdatatytpe,fparms])


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


def display_add_cols_df_funcs(parms) :
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
    
    dftitle     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
    df          =   cfg.get_dfc_dataframe_df(dftitle)
    cols_list   =   df.columns.tolist()
    dfcolname   =   cols_list[0]
    
    #form_parms  =   parms[1]
    fparms      =   get_parms_for_input(parms[1],add_column_code_dfc_funcs_input_idList)
    
    #print("fparms",fparms)
    
    if(len(fparms) > 0) :
        newcolname  =   fparms[0]
        cdatatype   =   fparms[1]
        if(len(cdatatype) == 0) :
            cdatatype   =   "str"
        ftitle      =   parms[3]
        
    else :
        newcolname  =   "USER VALUE"
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule, get_function_kwvals, get_function_kwargs
    gfmodule    =   reservedfunctionsmodule
        
    kwvals      =   get_function_kwvals(ftitle,dftitle,dfcolname)
        
    [kwargs,gfcode]      =   get_function_kwargs(gfmodule,ftitle,kwvals)
    
    gfcode      =   gfcode.replace("'",'"')
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_reserved_function_parms_datatypes
    pdtypes     =   get_reserved_function_parms_datatypes(ftitle)
    
    for i in range(len(kwargs)) :
        pval    =   kwvals.get(kwargs[i])
        if(pdtypes[i] == str) :
            if(len(pval) > 0) :
                gfcode      =   gfcode.replace(pval,"'" + pval + "'")    
        
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_generic_function_desc

    gfdesc      =   get_generic_function_desc(ftitle)
    gfdesc      =   gfdesc.replace("'",'"')
        
    dfc_add_code_idList, dfc_add_code_labelList, dfc_add_code_typeList          =   [],[],[]
    dfc_add_code_placeholderList, dfc_add_code_jsList, dfc_add_code_reqList     =   [],[],[]
    
    for i in range(len(add_column_code_dfc_funcs_parms_input_idList))           :     dfc_add_code_idList.append(add_column_code_dfc_funcs_parms_input_idList[i])
    for i in range(len(add_column_code_dfc_funcs_parms_input_labelList))        :     dfc_add_code_labelList.append(add_column_code_dfc_funcs_parms_input_labelList[i])
    for i in range(len(add_column_code_dfc_funcs_parms_input_typeList))         :     dfc_add_code_typeList.append(add_column_code_dfc_funcs_parms_input_typeList[i])
    for i in range(len(add_column_code_dfc_funcs_parms_input_placeholderList))  :     dfc_add_code_placeholderList.append(add_column_code_dfc_funcs_parms_input_placeholderList[i])
    for i in range(len(add_column_code_dfc_funcs_parms_input_jsList))           :     dfc_add_code_jsList.append(add_column_code_dfc_funcs_parms_input_jsList[i])
    for i in range(len(add_column_code_dfc_funcs_parms_input_reqList))          :     dfc_add_code_reqList.append(add_column_code_dfc_funcs_parms_input_reqList[i])

    kwarg_selects   =   []
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_function_kwval_parms_select
    for i in range(len(kwargs)) :
        kwarg_selects.append(get_function_kwval_parms_select(ftitle,kwargs[i]))

    #print("kwarg_selects\n",kwarg_selects)


    for i in range(len(kwargs)) :
        dfc_add_code_idList.append("addcolfparm"+str(i))    
        dfc_add_code_labelList.append(kwargs[i])
        
        if(kwarg_selects[i] is None) :
            dfc_add_code_typeList.append("text")
        else :
            dfc_add_code_typeList.append("select")
            
        dfc_add_code_placeholderList.append(kwvals.get(kwargs[i]))    
        dfc_add_code_jsList.append(None)    
        dfc_add_code_reqList.append(i+5) 
        
    for i in range(4) :
        dfc_add_code_idList.append(None)
        dfc_add_code_typeList.append("button")    
        dfc_add_code_placeholderList.append(None)
        
    for i in range(len(add_column_code_dfc_funcs_parms_input_labelList1)) :
        dfc_add_code_labelList.append(add_column_code_dfc_funcs_parms_input_labelList1[i])    
            
    for i in range(len(add_column_code_dfc_funcs_parms_input_jsList1)) :
        dfc_add_code_jsList.append(add_column_code_dfc_funcs_parms_input_jsList1[i])    

    #print("dfc_add_code_typeList",dfc_add_code_typeList)
    gt_input_form   = InputForm(add_column_code_dfc_funcs_parms_input_id,
                                dfc_add_code_idList,
                                dfc_add_code_labelList,
                                dfc_add_code_typeList,
                                dfc_add_code_placeholderList,
                                dfc_add_code_jsList,
                                dfc_add_code_reqList)

    selectDicts     =   []
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_function_return_datatype
    cdatatype       =   get_function_return_datatype(ftitle)
    
    
    
    dtypes          =   {"default":cdatatype,"list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                 "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                 "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
    selectDicts.append(dtypes)

    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_genfunc_list
    funcs_list  =   get_genfunc_list()
        
    funcs           =   []
    funcs.append(" ")
        
    if(not (funcs_list == None)) :
        for i in range(len(funcs_list)) :
            funcs.append(funcs_list[i])
        
    funclist    =   {"default":ftitle,"list":funcs,"callback":"get_dfc_func_value"}
    selectDicts.append(funclist)
    
    for i in range(len(kwarg_selects)) :
        if(not(kwarg_selects[i] is None)) :
            selectDicts.append(kwarg_selects[i])
            
    cfg.drop_config_value(add_column_code_dfc_funcs_parms_input_id+"Parms")
        
    get_select_defaults(gt_input_form,
                        add_column_code_dfc_funcs_parms_input_id,
                        dfc_add_code_idList,
                        dfc_add_code_typeList,
                        selectDicts)

    gt_input_form.set_shortForm(True)
    gt_input_form.set_gridwidth(480)
    gt_input_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":0})
    gt_input_form.set_fullparms(True)
    
    inputparms      =   [newcolname,cdatatype,ftitle,gfcode,gfdesc]
    inputpparms     =   [False,False,False,True,True]
    
    for i in range(len(kwargs)) :
        inputparms.append(kwvals.get(kwargs[i]))
        inputpparms.append(False)
        
    cfg.set_config_value(add_column_code_dfc_funcs_parms_input_id+"Parms",inputparms)
    cfg.set_config_value(add_column_code_dfc_funcs_parms_input_id+"ParmsProtect",inputpparms)
    
    set_current_dfc_funcs_idlist(dfc_add_code_idList)    
    
    gt_input_html   =   ""
    gt_input_html   =   gt_input_form.get_html()
    
    gt_heading_html     =   "<div>Add New Column From dfc Functions</div><br>"
    help_note           =   "After setting and reviewing parms in the above form click on 'Add New Column From Code' to add a new column."
    from dfcleanser.common.common_utils import get_help_note_html
    addcol_notes_html   =   get_help_note_html(help_note)
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
    gridhtmls       =   [gt_heading_html,gt_input_html,addcol_notes_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-add-col-code-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-add-col-code-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_add_cols_option(option,parms) :
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
    
    display_base_data_transform_columns_taskbar()

    newcolname      =   ""
    newdatatype     =   ""
    addparms        =   []
    
    opstat  =   opStatus()
    
    if(option == dtm.DISPLAY_ADD_COLUMN) :
        newcolname      =   None
        newdatatype     =   None
        addparms        =   None
        
    else :
        parsedParms = parse_add_cols_option_inputs(option,parms,opstat)
        
        print("parsedParms",parsedParms)

        newcolname      =   parsedParms[0]
        newdatatype     =   parsedParms[1]
        addparms        =   parsedParms[2]
        
    if(opstat.get_status()) :

        if(option == dtm.DISPLAY_ADD_COLUMN) :
        
            cfg.drop_config_value(cfg.ADD_COL_COL_NAME_KEY)
            cfg.drop_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
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
            
            dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                         "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                         "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
            selectDicts.append(dtypes)
        
            get_select_defaults(grid_input_form,
                                add_column_input_id,
                                add_column_input_idList,
                                add_column_input_typeList,
                                selectDicts)
        
            grid_input_form.set_buttonstyle({"font-size":12, "height":110, "width":90, "left-margin":1})
            grid_input_form.set_gridwidth(480)
            grid_input_form.set_fullparms(True) 

            grid_input_html   =   grid_input_form.get_html()

            gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-add-col-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-add-col-pop-up-wrapper",gridclasses,gridhtmls)
            
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()
                 
        elif(option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
        
            cfg.drop_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
        
            common_column_heading_html      =   "<br><div>Add New Column From File Parameters</div><br>"
            
            grid_input_form                 =   InputForm(add_column_file_input_id,
                                                          add_column_file_input_idList,
                                                          add_column_file_input_labelList,
                                                          add_column_file_input_typeList,
                                                          add_column_file_input_placeholderList,
                                                          add_column_file_input_jsList,
                                                          add_column_file_input_reqList)
        
            selectDicts     =   []
            
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
        
            cfg.set_config_value(add_column_file_input_id+"Parms",[newcolname,newdatatype,""])
    
            grid_input_html   =   grid_input_form.get_html()

            gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-add-col-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-add-col-pop-up-wrapper",gridclasses,gridhtmls)
    
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()


        elif(option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) :
        
            if(newcolname == None)  : newcolname    =   ""
            if(newdatatype == None) : newdatatype   =   ""

            print("DISPLAY_ADD_FROM_DFC_FUNCS",newcolname,newdatatype)
        
            cfg.set_config_value(add_column_code_dfc_funcs_input_id+"Parms",[newcolname,newdatatype,"","",""])
            cfg.set_config_value(add_column_code_dfc_funcs_input_id+"ParmsProtect",[False,False,False,True,True])

            display_add_cols_code(dtm.DISPLAY_FUNCTIONS)
                
        elif(option == dtm.DISPLAY_ADD_FROM_CODE_OPTION) :
        
            if(newcolname == None)  : newcolname    =   ""
            if(newdatatype == None) : newdatatype   =   ""

            cfg.set_config_value(add_column_code_gf_input_id+"Parms",[newcolname,newdatatype,"","",""])
        
            display_add_cols_code(dtm.DISPLAY_NO_FUNCTIONS)
    
        elif(option == dtm.DISPLAY_ADD_FROM_DF_OPTION) :
        
            if(newcolname == None)  : newcolname    =   ""
            if(newdatatype == None) : newdatatype   =   ""

            cfg.set_config_value(add_column_df_input_id+"Parms",["",newcolname,newdatatype,"","","","",""])
        
            common_column_heading_html      =   "<div>Add New Column From df</div><br>"
            
            grid_input_form                 =   InputForm(add_column_df_input_id,
                                                          add_column_df_input_idList,
                                                          add_column_df_input_labelList,
                                                          add_column_df_input_typeList,
                                                          add_column_df_input_placeholderList,
                                                          add_column_df_input_jsList,
                                                          add_column_df_input_reqList)

            selectDicts     =   []
        
            dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
            current_df_name     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
        
            dataframes      =   {"default":current_df_name,"list":dataframes_loaded, "callback":"add_df_col_change_df"}
            selectDicts.append(dataframes)
            
            dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                         "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                         "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
            selectDicts.append(dtypes)
        
            dataframes1     =   {"default":current_df_name,"list":dataframes_loaded, "callback":"add_df_col_change_df"}
            selectDicts.append(dataframes1)
        
            current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            colnames        =   current_df.columns.tolist()
            cnames          =   {"default":colnames[0],"list": colnames}
            selectDicts.append(cnames)
        
            cnames1         =   {"default":colnames[0],"list": colnames}
            selectDicts.append(cnames1)
        
            cnames2         =   {"default":colnames[0],"list": colnames}
            selectDicts.append(cnames2)
        
            get_select_defaults(grid_input_form,
                                add_column_df_input_id,
                                add_column_df_input_idList,
                                add_column_df_input_typeList,
                                selectDicts)

            grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":115, "left-margin":2})
            grid_input_form.set_gridwidth(480)
            grid_input_form.set_fullparms(True)
            grid_input_form.set_shortForm(True)
        
            grid_input_html   =   grid_input_form.get_html()
        
            #print(grid_input_html)

            gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
            gridhtmls       =   [common_column_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-add-col-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-add-col-pop-up-wrapper",gridclasses,gridhtmls)
    
            from dfcleanser.common.display_utils import display_pop_up_buffer
            display_pop_up_buffer()
    
            
    else :
        display_exception(opstat)


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
    
    if(option==dtm.DISPLAY_FUNCTIONS) :
        
        gt_input_form   = InputForm(add_column_code_dfc_funcs_input_id,
                                    add_column_code_dfc_funcs_input_idList,
                                    add_column_code_dfc_funcs_input_labelList,
                                    add_column_code_dfc_funcs_input_typeList,
                                    add_column_code_dfc_funcs_input_placeholderList,
                                    add_column_code_dfc_funcs_input_jsList,
                                    add_column_code_dfc_funcs_input_reqList)
    
    else :
        
        gt_input_form   = InputForm(add_column_code_gf_input_id,
                                    add_column_code_gf_input_idList,
                                    add_column_code_gf_input_labelList,
                                    add_column_code_gf_input_typeList,
                                    add_column_code_gf_input_placeholderList,
                                    add_column_code_gf_input_jsList,
                                    add_column_code_gf_input_reqList)

    selectDicts     =   []
            
    dtypes          =   {"default" : defdtype, "list": ["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                        "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                        "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
    selectDicts.append(dtypes)

    if(option == dtm.DISPLAY_FUNCTIONS) : 
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_genfunc_list
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
                            add_column_code_dfc_funcs_input_typeList,
                            selectDicts)
        
    else :
        
        get_select_defaults(gt_input_form,
                            add_column_code_gf_input_id,
                            add_column_code_gf_input_idList,
                            add_column_code_gf_input_typeList,
                            selectDicts)
        
    gt_input_form.set_shortForm(True)
    gt_input_form.set_gridwidth(480)
    gt_input_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":25})
    gt_input_form.set_fullparms(True)
    
    gt_input_html   =   ""
    gt_input_html   =   gt_input_form.get_html()
    
    if(option == dtm.DISPLAY_FUNCTIONS) : 
        gt_heading_html =   "<br><div>Add New Column From dfc Functions</div><br>"
    else :
        gt_heading_html =   "<br><div>Add New Column From User Code</div><br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [gt_heading_html,gt_input_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-add-col-code-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-add-col-code-pop-up-wrapper",gridclasses,gridhtmls)

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



def display_column_uniques(df,colname,samplesize,uniquesperrow,display=True) : 
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
                    uniqueHrefs.append(None)
                uniquerow   =   []
    
    #print("display_column_uniques",i,uniquerow,uniquesperrow,samplesize,len(uniques),samplesize % uniquesperrow)
    
    if((samplesize % uniquesperrow) != 0) :

        for k in range(uniquesperrow - (samplesize % uniquesperrow)) :
            uniquerow.append("")

        uniqueRows.append(uniquerow) 
        
        uniqueHrefs     =   []
        for k in range(uniquesperrow) :
            uniqueHrefs.append(None)
            
    #print("dcTable",uniqueHeader,uniqueRows,uniqueWidths,uniqueAligns,uniqueHrefs)
    
    uniques_table = dcTable("Sample Column Values for "+colname,"dtuniquesTable",
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
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
         uniques_html    =   display_column_uniques(df,colname,48,6,False)
    else :
         uniques_html    =   display_column_uniques(df,colname,24,4,False)
         
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
     
        
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        gridclasses     =   ["dfc-left","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [uniques_html,uniques_heading_html,find_values_html]
        
        display_generic_grid("col-change-datatype-uniques-wrapper",gridclasses,gridhtmls) 
            
    else :
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [uniques_html,uniques_heading_html,find_values_html]
        
        display_generic_grid("col-change-datatype-uniques-pop-up-wrapper",gridclasses,gridhtmls) 
    
    print("\n")
    
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(df,colname,False,True)

    nans            =   df[colname].isnull().sum()
    
    if(nans > 0) :
        change_dt_html  =   get_datatype_display(df,colname,True,False,cfg.DataTransform_ID)
        common_column_heading_html  =   "<div>Data Type Change Parameters</div><br>"
    else :
        change_dt_html  =   get_datatype_display(df,colname,False,False,cfg.DataTransform_ID)
        common_column_heading_html  =   "<br><br><div>Data Type Change Parameters</div><br>"
     
        
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
    
    #print("get_datatype_display",len(df),colname,nansflag,dfc_id)
    
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
    
    current_df      =   df#cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colname,"list": colnames, "callback":"change_dt_col_callback"}
    selectDicts.append(cnames)
    
    data_type_id    =   get_datatype_id(df[colname].dtype)
    data_type_str   =   get_datatype_str(data_type_id)
    data_type_str   =   data_type_str.lstrip("numpy.")

    from dfcleanser.common.common_utils import get_datatypes_list      
    dtypes          =   {"default":data_type_str,"list":get_datatypes_list(False)}
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
    
    #grid_input_form.dump()
        
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

    print("display_convert_datatype",len(df),colname,fillflag,dropflag,dfc_id)
    
    cfg.set_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY,colname) 
    

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
        
    common_column_heading_html      =   "<div>Data Type Change Parameters</div><br>"
     
    if(nans > 0) :    

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-middle","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,col_stats_html,dt_html]
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-middle","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,col_stats_html,dt_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("col-change-datatype-transform-wrapper",gridclasses,gridhtmls) 
            
    else :
        display_generic_grid("col-change-datatype-transform-pop-up-wrapper",gridclasses,gridhtmls) 
                    
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

    all_dtypes          =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64",
                             "np.float16","np.float32","np.float32",
                             "datetime.datetime","datetime.date","datetime.time","datetime.timedelta",
                             "np.datetime64","np.timedelta","pd.Timestamp",
                             "int","float","str","onject"]
    
    check_dtypes        =   get_check_dtypes(df,colname)
    
    compatable_dtypes   =   []
    
    for i in range(len(all_dtypes)) :
        
        if( not(all_dtypes[i] in check_dtypes)) :
            compatable_dtypes.append(all_dtypes[i])
            
    return(compatable_dtypes)

    
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
    import pandas as pd
    import datetime
    
    col_dtype           =   df[colname].dtype
    check_dtypes_list   =   []
    
    if(col_dtype == np.int8) :
        check_dtypes_list     =   ["np.uint8"]    
        
    elif(col_dtype == np.int16) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.uint16"]    
        
    elif(col_dtype == np.int32) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.uint32","np.float16","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.int64) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.int32","np.uint32","np.uint64","np.float16","np.float32","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.uint8) :
        check_dtypes_list     =   ["np.int8"]    
        
    elif(col_dtype == np.uint16) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16"]    
        
    elif(col_dtype == np.uint32) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","int","np.float16","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.uint64) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.int64","np.uint32","int","np.int64","np.float16","np.float32","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.float16) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.float32) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int","np.float16","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == np.float64) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","int","np.float16","np.float32","datetime.timedelta","np.timedelta"]    

    elif(col_dtype == object) :
        print("getting object list")
        check_dtypes_list     =  ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","datetime.datetime","datetime.date","datetime.time","np.datetime64","pd.Timestamp","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == datetime.datetime) :
        print("getting datetime.datetime")
        check_dtypes_list     =   ["np.datetime64","pd.timestamp"]    
        
    elif(col_dtype == datetime.date) :
        check_dtypes_list     =   ["datetime.datetime","np.datetime64","pd.timestamp"]    
        
    elif(col_dtype == datetime.time) :
        check_dtypes_list     =   ["datetime.datetime","np.datetime64","pd.timestamp"]    
        
    elif(col_dtype == datetime.timedelta) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64"] 
        
    elif(col_dtype == np.datetime64) :
        check_dtypes_list     =   ["datetime.datetime","pd.timestamp"]    
        
    elif(col_dtype == np.timedelta) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64"] 

    elif(col_dtype == pd.Timestamp) :
        check_dtypes_list     =   ["datetime.datetime","np.datetime64"] 

        
    elif(col_dtype == int) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.uint32","np.float16","datetime.timedelta","np.timedelta"]    
        
    elif(col_dtype == float) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","datetime.timedelta","np.timedelta"]    

        
    elif(col_dtype == str) :
        check_dtypes_list     =   ["np.int8","np.uint8","np.int16","np.uint16","np.int32","np.uint32","np.int64","np.uint64","np.float16","np.float32","np.float64","datetime.datetime","datetime.date","datetime.time","np.datetime64","pd.Timestamp","datetime.timedelta","np.timedelta"]    
        
    
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
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
    if(parms is None) :
        colname     =   cfg.get_config_value(cfg.COMPAT_COL_KEY)
    else :
        colname     =   parms[0]
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
    
    compatable_parms    =   [str(colname),str(check_dtypes[0]),compatable_str]
    
    cfg.set_config_value(dt_check_data_type_input_id + "Parms",compatable_parms)
    cfg.set_config_value(dt_check_data_type_input_id + "ParmsProtect",[False,False,True])

    check_html  =   grid_input_form.get_html()   
        
    common_column_heading_html      =   "<div>Check Datatype Compatability Parameters</div><br>"
     
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [common_column_heading_html,col_stats_html,check_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
        display_generic_grid("check-compatability-wrapper",gridclasses,gridhtmls) 
            
    else :
        display_generic_grid("check-compatability-pop-up-wrapper",gridclasses,gridhtmls) 
                    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


#








