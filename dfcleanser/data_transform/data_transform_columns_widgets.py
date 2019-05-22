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

from dfcleanser.common.html_widgets import (display_composite_form, get_button_tb_form, 
                                            get_header_form, maketextarea, ButtonGroupForm, 
                                            InputForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR)

from dfcleanser.common.common_utils import (get_datatype_id, display_status, opStatus, get_parms_for_input,
                                            is_numeric_col, display_generic_grid, get_select_defaults, 
                                            get_datatype_str, does_col_contain_nan)

from dfcleanser.common.display_utils import display_column_names

from IPython.display import (clear_output)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    global list for column values
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
NewColumnValues = []

def get_NewColumnValues() :
    return()
def set_NewColumnValues(ncv) :
    global NewColumnValues
    NewColumnValues = ncv



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

columns_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SAVE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SORT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CATS_TASKBAR)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CLEAR_COLUMN)+")",
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

columns_transform_tb1_jsList                =   ["cols_transform_tb_callback("+str(dtm.APPLY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.MAP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DUMMIES_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CAT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DATATYPE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CLEAR_COLUMN)+")",
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

columns_transform_tbA_jsList                =   ["cols_transform_tb_callback("+str(dtm.RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SAVE_COLUMN)+")"]

columns_transform_tbA_centered              =   True

columns_transform_tbB_doc_title             =   "DataFrame Columns Options"
columns_transform_tbB_title                 =   "DataFrame Columns Options"
columns_transform_tbB_id                    =   "columnstransformoptionstbB"

columns_transform_tbB_keyTitleList          =   ["Copy</br>Column",
                                                 "Sort</br>By</br>Column",
                                                 "Apply</br>fn To</br>Column",
                                                  "Map</br> Column",
                                                  "Dummies</br>For</br>Column"]

columns_transform_tbB_jsList                =   ["cols_transform_tb_callback("+str(dtm.COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SORT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.APPLY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.MAP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DUMMIES_COLUMN)+")"]

columns_transform_tbB_centered              =   True

columns_transform_tbC_doc_title             =   "DataFrame Columns Options"
columns_transform_tbC_title                 =   "DataFrame Columns Options"
columns_transform_tbC_id                    =   "columnstransformoptionstbC"

columns_transform_tbC_keyTitleList          =   ["Make</br> Column</br>Categorical",
                                                 "Change</br> Column</br>Datatype",
                                                 "Return","Help"]

columns_transform_tbC_jsList                =   ["cols_transform_tb_callback("+str(dtm.CAT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DATATYPE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CLEAR_COLUMN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MDC_ID) + ")"]

columns_transform_tbC_centered              =   True





"""
#--------------------------------------------------------------------------
#   column categorical task bar
#--------------------------------------------------------------------------
"""
cols_cat_transform_tb_doc_title              =   "DataFrame Columns Categorical Options"
cols_cat_transform_tb_title                  =   "DataFrame Columns Categorical Options"
cols_cat_transform_tb_id                     =   "colscattransformoptionstb"

cols_cat_transform_tb_keyTitleList           =   ["Apply</br>fn To</br>Column",
                                                  "Map</br> Column",
                                                  "Dummies</br>For</br>Column",
                                                  ]

cols_cat_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.APPLY_COLUMN)+")",
                                                  "cols_transform_tb_callback("+str(dtm.MAP_COLUMN)+")",
                                                  "cols_transform_tb_callback("+str(dtm.DUMMIES_COLUMN)+")",
                                                  "cols_transform_tb_callback("+str(dtm.CAT_COLUMN)+")",
                                                  "cols_transform_tb_callback("+str(dtm.DATATYPE_COLUMN)+")",
                                                  "cols_transform_tb_callback("+str(dtm.CLEAR_COLUMN)+")",
                                                  "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MDC_ID) + ")"]

"""
#--------------------------------------------------------------------------
#    rename column input for single column
#--------------------------------------------------------------------------
"""
rename_column_input_title               =   "Column Naming Parameters"
rename_column_input_id                  =   "renamecolInput"
rename_column_input_idList              =   ["newColumnName",
                                             None,None,None]

rename_column_input_labelList           =   ["new_column_name",
                                             "Rename</br> Column",
                                             "Return","Help"]

rename_column_input_typeList            =   ["text",
                                             "button","button","button"]

rename_column_input_placeholderList     = ["enter the new column name",
                                           None,None,None]

rename_column_input_jsList              =    [None,
                                              "data_transform_cols_callback(0,"+str(dtm.RENAME_COLUMN)+")",
                                              "data_transform_cols_callback(1,"+str(dtm.RENAME_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_RENAME_ID) + ")"]

rename_column_input_reqList             =   [0,1]

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
                                             None,None,None]

add_column_input_labelList              =   ["new_column_name",
                                             "new_column_data_type",
                                             "Get Column</br>Values</br>From File",
                                             "Get Column</br>Values From</br>User Code",
                                             "Return"]

add_column_input_typeList               =   ["text","select","button","button","button"]

add_column_input_placeholderList        =   ["enter the new column name",
                                             "enter the new column data type",
                                             None,None,None]

add_column_input_jsList                 =    [None,None,
                                              "data_transform_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_FILE_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_CODE_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(ADD_COLUMN_RETURN) + ")"]

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
                                              "Add New</br>Column",
                                              "Return","Help"]

add_column_file_input_typeList           =   ["text","select","file",
                                              "button","button","button"]

add_column_file_input_placeholderList    =   ["enter the new column name",
                                              "enter the new column data type",
                                              "enter the file name of list to use as values",
                                              None,None,None]

add_column_file_input_jsList             =    [None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_FILE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_FILE_ID) + ")"]

add_column_file_input_reqList            =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    add new column - user code
#--------------------------------------------------------------------------
"""

add_column_code_gf_input_title           =   "Add Column Parameters"
add_column_code_gf_input_id              =   "addcolcodeInput"
add_column_code_gf_input_idList          =   ["addColumnName",
                                              "addColumndtype",
                                              "addcolfuncs",
                                              "addcolmodule",
                                              "addcolname",
                                              "addcolcodefcode",
                                              "addcoldesc",
                                              None,None,None,None]

add_column_code_gf_input_labelList       =   ["new_column_name",
                                              "column_data_type",
                                              "generic_function",
                                              "function_module",
                                              "function_name",
                                              "function_code",
                                              "function_description",
                                              "Add New</br>Column</br>From Code",
                                              "Clear","Return","Help"]

add_column_code_gf_input_typeList        =   ["text","select","select","text","text",
                                              maketextarea(5),maketextarea(10),
                                              "button","button","button","button"]

add_column_code_gf_input_placeholderList =   ["enter the new column name",
                                              "enter the column data type",
                                              "generic function",
                                              "function module",
                                              "function name",
                                              "function code",
                                              "function description",
                                              None,None,None,None]

add_column_code_gf_input_jsList          =    [None,None,None,None,None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_NEW_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_CLEAR) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_code_gf_input_reqList         =   [0,1,3,4,5]


"""
#--------------------------------------------------------------------------
#    drop column
#--------------------------------------------------------------------------
"""
drop_column_input_title                 =   "Drop Column Parameters"
drop_column_input_id                    =   "dropcolInput"
drop_column_input_idList                =   ["dropColumnFname",
                                             None,None,None]

drop_column_input_labelList             =   ["file_save_name",
                                             "Drop</br> Column",
                                             "Return","Help"]

drop_column_input_typeList              =   ["file",
                                             "button","button","button"]

drop_column_input_placeholderList       =   ["enter File name to save dropped column to or browse to file below (default no save)",
                                             None,None,None]

drop_column_input_jsList                =    [None,
                                              "data_transform_cols_callback(0,"+str(dtm.DROP_COLUMN)+")",
                                              "data_transform_cols_callback(2,"+str(dtm.DROP_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DROP_ID) + ")"]

drop_column_input_reqList               =   [0]

"""
#--------------------------------------------------------------------------
#    save column
#--------------------------------------------------------------------------
"""
save_column_input_title                 =   "Save Column Parameters"
save_column_input_id                    =   "savecolInput"
save_column_input_idList                =   ["saveColumnFname",
                                             None,None,None]

save_column_input_labelList             =   ["file_save_name",
                                             "Save</br> Column",
                                             "Return","Help"]

save_column_input_typeList              =   ["file",
                                             "button","button","button"]

save_column_input_placeholderList       =   ["enter File name to save dropped column to or browse to file below (default no save)",
                                             None,None,None]

save_column_input_jsList                =    [None,
                                              "data_transform_cols_callback(0,"+str(dtm.SAVE_COLUMN)+")",
                                              "data_transform_cols_callback(2,"+str(dtm.SAVE_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_SAVE_ID) + ")"]

save_column_input_reqList               =   [0]

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

reorder_columns_input_typeList           =   ["text","text",
                                              "button","button","button"]

reorder_columns_input_placeholderList    =   ["column to move",
                                              "column to move after", 
                                              None,None,None]

reorder_columns_input_jsList             =    [None,None,
                                               "data_transform_cols_callback(0,"+str(dtm.REORDER_COLUMNS)+")",
                                               "data_transform_cols_callback(2,"+str(dtm.REORDER_COLUMNS)+")",
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

copy_columns_input_typeList             =   ["text","text",
                                             "button","button","button"]

copy_columns_input_placeholderList      =   ["column to move",
                                             "column to move after", 
                                             None,None,None]

copy_columns_input_jsList               =    [None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.COPY_COLUMN)+")",
                                              "data_transform_cols_callback(2,"+str(dtm.COPY_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_COPY_ID) + ")"]

copy_columns_input_reqList              =   [0,1]

"""
#--------------------------------------------------------------------------
#    sort by column
#--------------------------------------------------------------------------
"""
sort_column_input_title                 =   "Sort Column Parameters"
sort_column_input_id                    =   "sortcolInput"
sort_column_input_idList                =   ["sortColumnname",
                                             "sortOrder",
                                             "resetRowIds",
                                             None,None,None]

sort_column_input_labelList             =   ["column_to_sort_by",
                                             "ascending_order_flag",
                                             "reset_row_index_flag",
                                             "Sort By</br>Column",
                                             "Return","Help"]

sort_column_input_typeList              =   ["text","select","select",
                                             "button","button","button"]

sort_column_input_placeholderList       =   ["column to sort by",
                                             "ascending sort order (default = False)",
                                             "reorder the row id column after the sort (default True)",
                                             None,None,None]

sort_column_input_jsList                =    [None,None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.SORT_COLUMN)+")",
                                              "data_transform_cols_callback(2,"+str(dtm.SORT_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_SORT_BY_COL_ID) + ")"]

sort_column_input_reqList               =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    apply fn with gfs to column
#--------------------------------------------------------------------------
"""
apply_column_gf_input_title              =   "Apply fn To Column Parameters"
apply_column_gf_input_id                 =   "applycolInput"
apply_column_gf_input_idList             =   ["applyColumnname",
                                              "fmodule",
                                              "fnname",
                                              "fnlambda",
                                              "fnselect",
                                              "fntoapply",
                                              "fndesc",
                                              None,None,None,None,None]

apply_column_gf_input_labelList          =   ["column_to_apply_fn_to",
                                              "function_module",
                                              "function_name",
                                              "run_as_lamda",
                                              "generic functions",
                                              "function_code",
                                              "function_description",
                                              "Create</br>New</br>Function",
                                              "Apply Fn</br>To Column",
                                              "Clear","Return","Help"]

apply_column_gf_input_typeList           =   ["text","text","text","select","select",maketextarea(5),maketextarea(10),
                                              "button","button","button","button","button"]

apply_column_gf_input_placeholderList    =   ["column to sort by",
                                              "function module",
                                              "function name ",
                                              "run as lambda",
                                              "generic function",
                                              "function to apply",
                                              "function description",
                                              None,None,None,None,None,None]

apply_column_gf_input_jsList             =    [None,None,None,None,None,None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_MAKE_NEW_CODE_OPTION) + ")",
                                               "data_transform_cols_callback(0,"+str(dtm.APPLY_COLUMN)+")",
                                               "data_transform_cols_callback(1,"+str(dtm.APPLY_COLUMN)+")",
                                               "data_transform_cols_callback(2,"+str(dtm.APPLY_COLUMN)+")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + ")"]

apply_column_gf_input_reqList            =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    data transform map input for single column
#--------------------------------------------------------------------------
"""
transform_map_input_title               =   "Column Mapping Parameters"
transform_map_input_id                  =   "maptransformInput"
transform_map_input_idList              =   ["mapfilename","handlena","mapkeys","mapvals",
                                             None,None,None]

transform_map_input_labelList           =   ["mapping_values_list_file_name",
                                             "handle_nan",
                                             "mapping_keys","mapping_values",
                                             "Map Column",
                                             "Return","Help"]

transform_map_input_typeList            =   ["file","select",
                                             maketextarea(5),maketextarea(5),
                                             "button","button","button"]

transform_map_input_placeholderList     = ["enter File name containing mapping or browse to file below",
                                           "ignore Nans (default = True)",
                                           "mapping keys ** see List Utiltity below",
                                           "enter mapping values {comma separated) ** see List Utiltity below",
                                           None,None,None]

transform_map_input_jsList              =    [None,None,None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.MAP_COLUMN)+")",
                                              "data_transform_cols_callback(2,"+str(dtm.MAP_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MAP_ID) + ")"]

transform_map_input_reqList             =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    data transform dummy input 
#--------------------------------------------------------------------------
"""
transform_dummy_input_title             =   "Column Dummies Parameters"
transform_dummy_input_id                =   "dummytransformInput"
transform_dummy_input_idList            =   ["removecol",
                                             None,None,None]

transform_dummy_input_labelList         =   ["remove_original_column",
                                             "Make </br>Dummies</br> for Column",
                                             "Return","Help"]

transform_dummy_input_typeList          =   ["select","button","button","button"]

transform_dummy_input_placeholderList   =   ["remove original column (default = True)",
                                             None,None,None]
 
transform_dummy_input_jsList            =   [None,
                                             "data_transform_cols_callback(0,"+str(dtm.DUMMIES_COLUMN)+")",
                                             "data_transform_cols_callback(2,"+str(dtm.DUMMIES_COLUMN)+")",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DUMMY_ID) + ")"]

transform_dummy_input_reqList           =   [0]

"""
#--------------------------------------------------------------------------
#    data transform category input 
#--------------------------------------------------------------------------
"""
transform_category_input_title          =   "Column Category Parameters"
transform_category_input_id             =   "categorytransformInput"
transform_category_input_idList         =   ["ordinalcol","convertcol",
                                             None,None,None]

transform_category_input_labelList      =   ["make_column_categorical_flag",
                                             "change_column_datatype_to_category_datatype_flag",
                                             "Transform</br>Column",
                                             "Return","Help"]

transform_category_input_typeList       =   ["select","select","button","button","button"]

transform_category_input_placeholderList =  ["make column categorical (default = True)",
                                             "convert column to category datatype (default = False)",
                                             None,None,None]

transform_category_input_jsList         =   [None,None,
                                             "data_transform_cols_callback(0,"+str(dtm.CAT_COLUMN)+")",
                                             "data_transform_cols_callback(2,"+str(dtm.CAT_COLUMN)+")",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_CAT_ID) + ")"]

transform_category_input_reqList        =   [0,1]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data type components 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   data type input 
#--------------------------------------------------------------------------
"""
dt_data_type_input_title                =   "Change Data Type Parameters"
dt_data_type_input_id                   =   "dtdatatypeinput"
dt_data_type_input_idList               =   ["dtdatatype",
                                             "dtdropflag",
                                             "dtfilmethod",
                                             "dtfillna",
                                             None,None,None]

dt_data_type_input_labelList            =   ["datatype",
                                             "dropna",
                                             "fillna_method",
                                             "fillna_value",
                                             "Change</br> DataType",
                                             "Return","Help"]

dt_data_type_input_typeList             =   ["select","select","select","text","button","button","button"]

dt_data_type_input_placeholderList      =   ["datatype selected",
                                             "dropna flag",
                                             "fillna method selected",
                                             "fillna value is required",
                                             None,None,None]

dt_data_type_input_jsList               =   [None,None,None,None,
                                             "process_cols_datatype_transform_callback(0)",
                                             "process_cols_datatype_transform_callback(2)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_data_type_input_reqList              =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   no nans data type input 
#--------------------------------------------------------------------------
"""
dt_nn_data_type_input_title             =   "Change Data Type Parameters"
dt_nn_data_type_input_id                =   "dtdatatypeinput"
dt_nn_data_type_input_idList            =   ["dtnndatatype",
                                             None,None,None]

dt_nn_data_type_input_labelList         =   ["datatype",
                                             "Change</br> DataType",
                                             "Return","Help"]

dt_nn_data_type_input_typeList          =   ["select","button","button","button"]

dt_nn_data_type_input_placeholderList   =   ["datatype selected",
                                             None,None,None]

dt_nn_data_type_input_jsList            =   [None,
                                             "process_cols_datatype_transform_callback(0)",
                                             "process_cols_datatype_transform_callback(2)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_nn_data_type_input_reqList           =   [0]


"""
#--------------------------------------------------------------------------
#    datatype taskbar 
#--------------------------------------------------------------------------
"""
"""
dt_data_type_tb_doc_title                   =   "Change Data Type Parameters"
dt_data_type_tb_title                       =   "Change Data Type Parameters"
dt_data_type_tb_id                          =   "changedatatypetb"

dt_data_type_tb_keyTitleList                =   ["Change</br>DataType",
                                                 "Cleanse</br>Column",
                                                 "Return","Help"]

dt_data_type_tb_jsList                      =   ["process_cols_datatype_transform_callback(0)",
                                                 "process_cols_datatype_transform_callback(1)",
                                                 "process_cols_datatype_transform_callback(2)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Column transform display components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_data_transform_columns_taskbar() : 
    display_composite_form([get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                               columns_transform_tb_keyTitleList,
                                                               columns_transform_tb_jsList,
                                                               False)),
                            get_header_form("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Column Transform")])

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
        

def display_cats_transform_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(columns_transform_tb1_id,
                                               columns_transform_tb1_keyTitleList,
                                               columns_transform_tb1_jsList,
                                               True))
    
    
"""
#--------------------------------------------------------------------------
#    Column transform get input form helper methods
#--------------------------------------------------------------------------
"""
def get_rename_column_inputs(parms) :
    return(get_parms_for_input(parms[3],rename_column_input_idList))

def get_drop_column_inputs(parms) :
    return(get_parms_for_input(parms[3],drop_column_input_idList))

def get_save_column_inputs(parms) :
    return(get_parms_for_input(parms[3],save_column_input_idList))

def get_reorder_column_inputs(parms) :
    return(get_parms_for_input(parms[3],reorder_columns_input_idList))

def get_copy_column_inputs(parms) :
   return(get_parms_for_input(parms[3],copy_columns_input_idList))
   
def get_sort_by_column_inputs(parms) :
   return(get_parms_for_input(parms[3],sort_column_input_idList))
   
def get_apply_fn_to_column_inputs(parms) :
   return(get_parms_for_input(parms[3],apply_column_gf_input_idList))

def get_map_column_inputs(parms) :
    return(get_parms_for_input(parms[3],transform_map_input_idList))

def get_dummies_column_inputs(parms) :
    return(get_parms_for_input(parms[3],transform_dummy_input_idList))

def get_cat_column_inputs(parms) :
    return(get_parms_for_input(parms[3],transform_category_input_idList))

def get_datatype_column_inputs(parms) :
    return(get_parms_for_input(parms[4],dt_data_type_input_idList))


"""
#--------------------------------------------------------------------------
#    display cols table to select column to work on from 
#--------------------------------------------------------------------------
"""
def display_col_transform_columns(refparm,note,status,displaycollist=True,callbacks=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display cols table to select column to work on from
    * 
    * parms :
    *   refparm         -   add column parms
    *   note            -   note to display
    *   status          -   display status value
    *   displaycollist  -   display col list flag
    *   callbacks       -   set callback flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    clear_output()
    
    if( (refparm == dtm.MAPPING_DETAILS) or 
        (refparm == dtm.DUMMIES_DETAILS) or 
        (refparm == dtm.CATEGORIES_DETAILS) ) :
        
        display_cats_transform_taskbar()
        
    else :
        display_base_data_transform_columns_taskbar()

    print("\n") 
    
    if(len(status)> 0) :
        display_status(status)
     
    if(displaycollist) :
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note("<b>*</b> Select a Column for " + note + " by clicking on Column Name above.")
        col_names_table.set_refParm(str(refparm))
    
        if(callbacks) :
            col_names_html  =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                                     col_names_table,"dtctcol",False)
        else :
            col_names_html  =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                                     col_names_table,None,False)
            
        gridclasses     =   ["dfc-top-"]
        gridhtmls       =   [col_names_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-transform-col-nammes-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-transform-col-nammes-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_df_column_parms(cmd,colid) :
    """
    * -------------------------------------------------------- 
    * function : display grid cols parms
    * 
    * parms :
    *
    *   cmd     - command type
    *   colid   - column id
    *    
    * returns : operators html
    * --------------------------------------------------------
    """

    if(( (not(cmd == dtm.MOVING_DETAILS)) and (not(cmd == dtm.COPYING_DETAILS)))) :
        display_base_data_transform_columns_taskbar() 
        print("\n")
    
    if(not(colid is None)) :
        from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
        colstats_html       =   display_transform_col_data(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                                           colid,False)

    if(cmd == dtm.RENAMING_DETAILS) :
    
        common_column_heading_html      =   "<div>Rename Column '" + str(colid) + "'</div>"
        
        grid_input_form                 =   InputForm(rename_column_input_id,
                                                      rename_column_input_idList,
                                                      rename_column_input_labelList,
                                                      rename_column_input_typeList,
                                                      rename_column_input_placeholderList,
                                                      rename_column_input_jsList,
                                                      rename_column_input_reqList,
                                                      True)
                
    elif(cmd == dtm.DROPPING_DETAILS) :
        
        common_column_heading_html      =   "<div>Drop Column '" + str(colid) + "'</div>"

        grid_input_form     =   InputForm(drop_column_input_id,
                                          drop_column_input_idList,
                                          drop_column_input_labelList,
                                          drop_column_input_typeList,
                                          drop_column_input_placeholderList,
                                          drop_column_input_jsList,
                                          drop_column_input_reqList,
                                          True)
         
        
    elif(cmd == dtm.MOVING_DETAILS) : 
        
        common_column_heading_html      =   "<div>Moving Column Parameters</div>"

        grid_input_form     =   InputForm(reorder_columns_input_id,
                                          reorder_columns_input_idList,
                                          reorder_columns_input_labelList,
                                          reorder_columns_input_typeList,
                                          reorder_columns_input_placeholderList,
                                          reorder_columns_input_jsList,
                                          reorder_columns_input_reqList,
                                          True)
       
        grid_input_form.set_custombwidth(90)
        grid_input_form.set_gridwidth(280)
    
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("col-narrow-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("col-narrow-pop-up-wrapper",gridclasses,gridhtmls)
    
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
        
        return()
       
    elif(cmd == dtm.SAVING_DETAILS) : 
        
        common_column_heading_html      =   "<div>Save Column '" + str(colid) + "'</div>"

        grid_input_form     =   InputForm(save_column_input_id,
                                          save_column_input_idList,
                                          save_column_input_labelList,
                                          save_column_input_typeList,
                                          save_column_input_placeholderList,
                                          save_column_input_jsList,
                                          save_column_input_reqList,
                                          True)
    
    elif(cmd == dtm.SORTING_DETAILS) : 
        
        cfg.set_config_value(sort_column_input_id+"Parms",[colid,"",""])
        
        common_column_heading_html      =   "<div>Sort By Column '" + str(colid) + "'</div>"
        
        grid_input_form     =   InputForm(sort_column_input_id,
                                          sort_column_input_idList,
                                          sort_column_input_labelList,
                                          sort_column_input_typeList,
                                          sort_column_input_placeholderList,
                                          sort_column_input_jsList,
                                          sort_column_input_reqList,
                                          True)   

        selectDicts     =   []
        sortsel         =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(sortsel)
        sortsel         =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(sortsel)
           
        get_select_defaults(grid_input_form,
                            sort_column_input_id,
                            sort_column_input_idList,
                            sort_column_input_typeList,
                            selectDicts)

    elif(cmd == dtm.DUMMIES_DETAILS) :
        
        common_column_heading_html      =   "<div>Dummies For Column '" + str(colid) + "'</div>"

        grid_input_form     =   InputForm(transform_dummy_input_id,
                                          transform_dummy_input_idList,
                                          transform_dummy_input_labelList,
                                          transform_dummy_input_typeList,
                                          transform_dummy_input_placeholderList,
                                          transform_dummy_input_jsList,
                                          transform_dummy_input_reqList)
        
        selectDicts     =   []
        dummysel        =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(dummysel)
           
        get_select_defaults(grid_input_form,
                            transform_dummy_input_id,
                            transform_dummy_input_idList,
                            transform_dummy_input_typeList,
                            selectDicts)

    elif(cmd == dtm.CATEGORIES_DETAILS) :
        
        common_column_heading_html      =   "<div>Make Column '" + str(colid) + "' Categorical</div>"

        grid_input_form     =   InputForm(transform_category_input_id,
                                          transform_category_input_idList,
                                          transform_category_input_labelList,
                                          transform_category_input_typeList,
                                          transform_category_input_placeholderList,
                                          transform_category_input_jsList,
                                          transform_category_input_reqList)
        
        selectDicts     =   []
        catsel          =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(catsel)
        catsel          =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(catsel)
           
        get_select_defaults(grid_input_form,
                            transform_category_input_id,
                            transform_category_input_idList,
                            transform_category_input_typeList,
                            selectDicts)

    elif(cmd == dtm.MAPPING_DETAILS) :
        
        common_column_heading_html      =   "<div>Map Column '" + str(colid) + "'</div>"

        grid_input_form     =   display_mapping_col(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colid) 
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
    
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-map-col-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-map-col-pop-up-wrapper",gridclasses,gridhtmls)
        
        return()


    elif(cmd == dtm.COPYING_DETAILS) :

        common_column_heading_html      =   "<div>Copying Column</div>"

        grid_input_form     =   InputForm(copy_columns_input_id,
                                          copy_columns_input_idList,
                                          copy_columns_input_labelList,
                                          copy_columns_input_typeList,
                                          copy_columns_input_placeholderList,
                                          copy_columns_input_jsList,
                                          copy_columns_input_reqList,
                                          True)
        
        #grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":0})
        #grid_input_form.set_gridwidth(280)
        grid_input_form.set_custombwidth(90)
        grid_input_form.set_gridwidth(280)
    
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [common_column_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-inspection-wrapper",gridclasses,gridhtmls)
        else :
            print(grid_input_html)
            display_generic_grid("col-narrow-pop-up-wrapper",gridclasses,gridhtmls)
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
        
        return()

    

    grid_input_form.set_gridwidth(480)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0}) 
   
    grid_input_html   =   grid_input_form.get_html()
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
    gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-common-col-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-common-col-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


"""
#--------------------------------------------------------------------------
#    display transform column options 
#--------------------------------------------------------------------------
"""
def display_transform_cols_option(parms) : 
 
    
    colid = "None"
    if(len(parms[0]) == 1) :
        funcid     =   parms[0][0]
    else :
        colid      =   parms[0][0]
        funcid     =   int(parms[0][1])
        
    if(colid == "DCCleanser") :
        colid = cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
      
        
    cfg.set_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY,colid)
    
    if(funcid == dtm.CATS_TASKBAR) :
        clear_output()
        display_cats_transform_taskbar() 
        
    elif(funcid == dtm.RENAMING) :
        display_col_transform_columns(dtm.RENAMING_DETAILS,"renaming","") 
    
    elif(funcid == dtm.ADDING) :
        display_base_data_transform_columns_taskbar()       
        print("\n")

        cmdparms    =   parms[0]
        if(len(cmdparms) == 1) :
            display_add_cols_option(None)
        else :
            display_add_cols_option(parms)
    
    elif(funcid == dtm.DROPPING) :
        display_col_transform_columns(dtm.DROPPING_DETAILS,"dropping","")
    
    elif(funcid == dtm.MOVING) :
        display_col_transform_columns(dtm.MOVING_DETAILS,"moving","")
        display_df_column_parms(dtm.MOVING_DETAILS,None)
    
    elif(funcid == dtm.MAPPING) :
        display_col_transform_columns(dtm.MAPPING_DETAILS,"setting mapping","") 
    
    elif(funcid == dtm.DUMMIES) :
        display_col_transform_columns(dtm.DUMMIES_DETAILS,"setting dummies","") 
    
    elif(funcid == dtm.CATEGORIES) :
        display_col_transform_columns(dtm.CATEGORIES_DETAILS,"setting categories","") 
    
    elif(funcid == dtm.DATATYPE) :
        display_col_transform_columns(dtm.DATATYPE_DETAILS,"changing datatype","")
    
    elif(funcid == dtm.SAVING) :
        display_col_transform_columns(dtm.SAVING_DETAILS,"saving","") 
    
    elif(funcid == dtm.COPYING) :
        display_col_transform_columns(dtm.COPYING_DETAILS,"copying","")
        display_copy_column_parms(colid)
        
    elif(funcid == dtm.SORTING) : 
        display_col_transform_columns(dtm.SORTING_DETAILS,"sorting","")

    elif(funcid == dtm.APPLYING) :
        display_col_transform_columns(dtm.APPLYING_DETAILS,"applying function","")
    
        
    #"""
    #* -------------------------------------------------------- 
    #* final display column operations details routing
    #* --------------------------------------------------------
    #"""
    
    # display column transform details input
    elif(funcid == dtm.RENAMING_DETAILS) :
        display_df_column_parms(dtm.RENAMING_DETAILS,colid)

    elif(funcid == dtm.DROPPING_DETAILS) :
        display_df_column_parms(dtm.DROPPING_DETAILS,colid)
            
    elif(funcid == dtm.MOVING_DETAILS) :
                
        if(cfg.get_config_value(cfg.MOVE_COL_ID_KEY) == None) :
            cfg.set_config_value(cfg.MOVE_COL_ID_KEY,colid)
            cfg.drop_config_value(cfg.MOVE_AFTER_COL_ID_KEY)
        else :
            cfg.set_config_value(cfg.MOVE_AFTER_COL_ID_KEY,colid)

        moveParms = []
        if(not(cfg.get_config_value(cfg.MOVE_COL_ID_KEY) == None)) : 
            moveParms.append(cfg.get_config_value(cfg.MOVE_COL_ID_KEY))
        else :
            moveParms.append("")
                    
        if(not(cfg.get_config_value(cfg.MOVE_AFTER_COL_ID_KEY) == None)) : 
            moveParms.append(cfg.get_config_value(cfg.MOVE_AFTER_COL_ID_KEY))
        else :
            moveParms.append("")

        if( (len(moveParms[0]) > 0) or (len(moveParms[1])) ) :  
            cfg.set_config_value(reorder_columns_input_id+"Parms",moveParms)

        display_col_transform_columns(dtm.MOVING_DETAILS,"moving "+colid+" after ","")

        display_df_column_parms(dtm.MOVING_DETAILS,colid)

    elif(funcid == dtm.MAPPING_DETAILS) :
        display_df_column_parms(dtm.MAPPING_DETAILS,colid)
    
    elif(funcid == dtm.DUMMIES_DETAILS) :
        display_df_column_parms(dtm.DUMMIES_DETAILS,colid)
    
    elif(funcid == dtm.CATEGORIES_DETAILS) :
        display_df_column_parms(dtm.CATEGORIES_DETAILS,colid)
    
    elif(funcid == dtm.DATATYPE_DETAILS) :
        display_convert_datatype(colid)
    
    elif(funcid == dtm.SAVING_DETAILS) :
        display_df_column_parms(dtm.SAVING_DETAILS,colid)

    elif(funcid == dtm.COPYING_DETAILS) :
        display_copy_column_parms(colid)    
    
    elif(funcid == dtm.SORTING_DETAILS) :
        display_df_column_parms(dtm.SORTING_DETAILS,colid)
        
    elif( (funcid == dtm.APPLYING_DETAILS)  or (funcid == dtm.APPLYING_DETAILS_GF) ) :
        display_base_data_transform_columns_taskbar()        
        print("\n")
        display_apply_fn_inputs(colid)
    
    elif(funcid == dtm.APPLYING_SEL_FUN) :
        display_apply_fn_sel_inputs(parms)

    else :
        from dfcleanser.data_transform.data_transform_widgets import display_main_option
        display_main_option(None)
        

def display_column_transform_status(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display column transform status
    * 
    * parms :
    *  df          -   data frame
    *  colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
    display_transform_col_data(df,colname)
    

def display_column_uniques(df,colname,display=True) : 
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
    
    uniquesamplesize    =   24
    uniquesperrow       =   8
    
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
        uniquesamplesize    =   len(uniques)
        
    colwidth    =   int(100/uniquesperrow)
    
    for i in range(uniquesperrow) :
        uniqueHeader.append("Value")
        uniqueWidths.append(colwidth)
        uniqueAligns.append("center")
        
    uniqueRows      =   []
    uniqueHrefs     =   []
    
    uniquerow       =   []
    
    for i in range(uniquesamplesize) :
        
        if(i < len(uniques)) :
            uniquerow.append(uniques[i])

            if((i+1) % uniquesperrow == 0) :
                uniqueRows.append(uniquerow)
                uniqueHrefs.append([None,None,None,None,None,None,None,None,None,None])
                uniquerow   =   []
        
    if(((i+1) % uniquesperrow) != 0) :

        for k in range(uniquesperrow - ((i) % uniquesperrow)) :
            uniquerow.append("")

        uniqueRows.append(uniquerow) 
    
    uniques_table = dcTable("Sample Column Values for "+colname,"dtuniquesTable",
                            cfg.DataTransform_ID,
                            uniqueHeader,uniqueRows,
                            uniqueWidths,uniqueAligns)
    
    uniques_table.set_tabletype(ROW_MAJOR)
    uniques_table.set_rowspertable(3)
    uniques_table.set_refList(uniqueHrefs)

    if(display) :
        uniques_table.display_table()
    else :
        return(uniques_table.get_html())


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display add column specific methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    
def parse_add_cols_option_inputs(parms,opstat=None) :
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
    
    optionid        =   -1
    newcolname      =   ""
    newdatatytpe    =   ""
    fparms          =   []
    
    if(len(parms[0]) > 1) :
        optionid    =   int(parms[0][2])

    if(len(parms)>1) :
        
        if(optionid == dtm.PROCESS_FILE_OPTION) :
            fparms = get_parms_for_input(parms[1],add_column_file_input_idList)
        elif(optionid == dtm.PROCESS_ADD_NEW_CODE_OPTION) :
            fparms = get_parms_for_input(parms[1],add_column_code_gf_input_idList)
        elif(optionid == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
            fparms = get_parms_for_input(parms[1],add_column_input_idList)
        elif(optionid == dtm.DISPLAY_ADD_FROM_CODE_OPTION) :
            fparms = get_parms_for_input(parms[1],add_column_input_idList)
    
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
        for i in range(len(collist)) :
            if(collist[i] == newcolname) :
                found = True
        
        if(not found) :
        
            if(optionid == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
                cfg.set_config_value(add_column_file_input_id + "Parms",[newcolname,newdatatytpe,""]) 
            elif(optionid == dtm.DISPLAY_ADD_FROM_CODE_OPTION ) :
                cfg.set_config_value(add_column_code_gf_input_id + "Parms",[newcolname,newdatatytpe,"",""]) 
                
        else :
            cfg.drop_config_value(add_column_file_input_id+"Parms")    
            cfg.drop_config_value(add_column_code_gf_input_id+"Parms")
            
            opstat.set_status(False)
            opstat.set_errorMsg("   [Column Name Error] : column ",newcolname," already exists")

    return([optionid,newcolname,newdatatytpe,fparms])


def display_add_cols_option(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : parse parms for add columns
    * 
    * parms :
    *   parms   -   add column parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    optionid        =   -1
    newcolname      =   ""
    newdatatype     =   ""
    nparms          =   []
    
    opstat  =   opStatus()
    
    if(parms == None) :
        optionid        =   dtm.DISPLAY_BASE_ADD_OPTION
        newcolname      =   None
        newdatatype     =   None
        nparms          =   None
        
    else :
        parsedParms = parse_add_cols_option_inputs(parms,opstat)

        optionid        =   parsedParms[0]
        newcolname      =   parsedParms[1]
        newdatatype     =   parsedParms[2]
        nparms          =   parsedParms[3]

    if(optionid == dtm.DISPLAY_BASE_ADD_OPTION) :
        
        cfg.drop_config_value(cfg.ADD_COL_COL_NAME_KEY)
        cfg.drop_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
        cfg.drop_config_value(add_column_input_id + "Parms")
        
        common_column_heading_html      =   "<div>Add New Column </div>"
            
        grid_input_form                 =   InputForm(add_column_input_id,
                                                      add_column_input_idList,
                                                      add_column_input_labelList,
                                                      add_column_input_typeList,
                                                      add_column_input_placeholderList,
                                                      add_column_input_jsList,
                                                      add_column_input_reqList,
                                                      True)
        
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
        
        grid_input_form.set_buttonstyle({"font-size":13, "height":75, "width":110, "left-margin":0})
        grid_input_form.set_gridwidth(340)
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
                 
    elif(optionid == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
        
        cfg.drop_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
        
        common_column_heading_html      =   "<div>Add New Column From File Parameters</div>"
            
        grid_input_form                 =   InputForm(add_column_file_input_id,
                                                      add_column_file_input_idList,
                                                      add_column_file_input_labelList,
                                                      add_column_file_input_typeList,
                                                      add_column_file_input_placeholderList,
                                                      add_column_file_input_jsList,
                                                      add_column_file_input_reqList,
                                                      True)
        
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
            
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":90, "left-margin":0})
        grid_input_form.set_gridwidth(280)
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
                
    elif(optionid == dtm.DISPLAY_ADD_FROM_CODE_OPTION) :
        
        if(newcolname == None)  : newcolname    =   ""
        if(newdatatype == None) : newdatatype   =   ""

        #print("DISPLAY_ADD_FROM_CODE_OPTION",newcolname,newdatatype)
        
        cfg.set_config_value(add_column_code_gf_input_id+"Parms",[newcolname,newdatatype,"","","","",""])
        display_add_cols_code(dtm.DISPLAY_FUNCTIONS)
    
    elif(optionid == dtm.PROCESS_FILE_OPTION) :
        from dfcleanser.data_transform.data_transform_columns_control import process_add_column
        process_add_column([optionid,nparms])

    elif(optionid == dtm.PROCESS_MAKE_NEW_CODE_OPTION) :
        
        if(not (cfg.get_config_value(cfg.ADD_COL_CODE_KEY) == None) ) :
            cfg.set_config_value(add_column_code_gf_input_id+"Parms",[newcolname,cfg.get_config_value(cfg.ADD_COL_CODE_KEY)])
        
        display_add_cols_code()
        
    elif(optionid == dtm.PROCESS_ADD_NEW_CODE_OPTION) :
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_control import process_add_column
        process_add_column([optionid,nparms])
        
    elif(optionid == dtm.PROCESS_SELECT_FUNC_OPTION) :
        ftitle  =   parms[1]
        
        newcolname      =   cfg.get_config_value(cfg.ADD_COL_COL_NAME_KEY)
        newdatatype     =   cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
        
        if(newcolname == None)  : newcolname    =   ""
        if(newdatatype == None) : newdatatype   =   ""
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_control import get_generic_function_desc, get_generic_function
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_function_call,is_lambda_function
        gt_func         =   get_generic_function(ftitle)
        gt_func_desc    =   get_generic_function_desc(ftitle)
        
        if(not (gt_func_desc is None)) :
            
            lambda_flag     =   is_lambda_function(ftitle)
            if(lambda_flag) :   lambda_val      =   "True"
            else :              lambda_val      =   "False"
        
            func_parms_dict     =   {}
            func_parms_dict.update({"dftitle":cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)})
            func_parms_dict.update({"newcolname":newcolname})
            
            func_call   =   get_function_call(ftitle,func_parms_dict)
            
            import dfcleanser.sw_utilities.sw_utility_genfunc_model as gfm
            if(ftitle in gfm.reservedfunctions) :
                from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule
                fparms = [newcolname,
                          newdatatype,
                          lambda_val,
                          reservedfunctionsmodule,
                          ftitle,
                          func_call,
                          gt_func_desc]
                
            else :
                fparms = [newcolname,
                          newdatatype,
                          "",
                          gt_func.get_func_module(),
                          gt_func.get_func_title(),
                          "",
                          gt_func.get_func_code()]
                
            cfg.set_config_value(add_column_code_gf_input_id+"Parms",fparms)

        display_add_cols_code(dtm.DISPLAY_FUNCTIONS)


def display_add_cols_code(option) :
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
    
    gt_input_form   = InputForm(add_column_code_gf_input_id,
                                add_column_code_gf_input_idList,
                                add_column_code_gf_input_labelList,
                                add_column_code_gf_input_typeList,
                                add_column_code_gf_input_placeholderList,
                                add_column_code_gf_input_jsList,
                                add_column_code_gf_input_reqList)

    selectDicts     =   []
            
    dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                 "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                 "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
    selectDicts.append(dtypes)
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_widgets import get_genfunc_list
    funcs_list  =   get_genfunc_list()
        
    funcs           =   []
    funcs.append(" ")
        
    if(not (funcs_list == None)) :
        for i in range(len(funcs_list)) :
            funcs.append(funcs_list[i])
        
    funclist    =   {"default":" ","list":funcs,"callback":"get_selected_value"}
    selectDicts.append(funclist)
        
    get_select_defaults(gt_input_form,
                        add_column_code_gf_input_id,
                        add_column_code_gf_input_idList,
                        add_column_code_gf_input_typeList,
                        selectDicts)
    
    gt_input_form.set_shortForm(True)
    gt_input_form.set_gridwidth(480)
    gt_input_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":0})
    gt_input_form.set_fullparms(True)
    
    gt_input_html   =   ""
    gt_input_html   =   gt_input_form.get_html()
        
    gt_heading_html =   "<div>Add New Column From User Code</div><br>"

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
        

def display_convert_datatype(colid) : 
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
  
    display_base_data_transform_columns_taskbar()
    
    dftitle     =   cfg.get_config_value(cfg.CURRENT_CLEANSE_DF)  
    cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,dftitle)
    
    uniques_html    =   display_column_uniques(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colid,False)        
        
    nans            =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colid].isnull().sum()

    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                          colid,
                                          False,
                                          True)
        
    data_type_id    =   get_datatype_id(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colid].dtype)
    data_type_str   =   get_datatype_str(data_type_id)
    data_type_str   =   data_type_str.replace("numpy.","")
            
    selectDicts     =   []
    dtypes          =   {"default":"str","list":["str","numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64","numpy.int8",
                                                 "numpy.int16","numpy.int32","numpy.int64","numpy.float16","numpy.float32","numpy.float64",
                                                 "datetime.datetime","datetime.date","datetime.time","datetime.timedelta","object","int","float"]}
    
    selectDicts.append(dtypes)
    
    if(nans > 0) :
        
        dropnas         =   {"default" : "False", "list" : ["True","False"],"callback":"dtselect_dropna_change"}
        selectDicts.append(dropnas)
        
        
        fillnas         =   {"default" : "None - use fillna_value", "list" : ["None - use fillna_value","mean","bfill","ffill"]}
        selectDicts.append(fillnas)
        
    common_column_heading_html      =   "<div>Data Type Change Parameters</div><br>"
     
    print("\n")
    
    if(nans > 0) :

        grid_input_form     =   InputForm(dt_data_type_input_id,
                                          dt_data_type_input_idList,
                                          dt_data_type_input_labelList,
                                          dt_data_type_input_typeList,
                                          dt_data_type_input_placeholderList,
                                          dt_data_type_input_jsList,
                                          dt_data_type_input_reqList,
                                          True)
           
        get_select_defaults(grid_input_form,
                            dt_data_type_input_id,
                            dt_data_type_input_idList,
                            dt_data_type_input_typeList,
                            selectDicts)
        
        grid_input_form.set_custombwidth(80)
        grid_input_form.set_gridwidth(340)
    
        grid_input_html     =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-col-sample-top","dfc-left","dfc-right"]
        gridhtmls       =   [common_column_heading_html,uniques_html,col_stats_html,grid_input_html]
    
        display_generic_grid("col-change_datatype-wrapper",gridclasses,gridhtmls)
                    
    else :
            
        grid_input_form     =   InputForm(dt_nn_data_type_input_id,
                                          dt_nn_data_type_input_idList,
                                          dt_nn_data_type_input_labelList,
                                          dt_nn_data_type_input_typeList,
                                          dt_nn_data_type_input_placeholderList,
                                          dt_nn_data_type_input_jsList,
                                          dt_nn_data_type_input_reqList,
                                          True)
           
        get_select_defaults(grid_input_form,
                            dt_nn_data_type_input_id,
                            dt_nn_data_type_input_idList,
                            dt_nn_data_type_input_typeList,
                            selectDicts)
        
        grid_input_form.set_custombwidth(90)
        grid_input_form.set_gridwidth(340)
        
        grid_input_html     =   grid_input_form.get_html()
        #grid_input_html     =   ("<br><br><br><br>"+grid_input_html)
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-col-sample-top","dfc-left","dfc-right"]
        gridhtmls       =   [common_column_heading_html,uniques_html,col_stats_html,grid_input_html]
    
        display_generic_grid("col-change_datatype-wrapper",gridclasses,gridhtmls)
    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

    
def display_copy_column_parms(colid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display copy column parms
    * 
    * parms :
    *  colid      -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(cfg.get_config_value(cfg.COPY_COL_TO_KEY) == None) :
        cfg.set_config_value(cfg.COPY_COL_TO_KEY,colid)
        cfg.drop_config_value(cfg.COPY_COL_FROM_KEY)
    else :
        cfg.set_config_value(cfg.COPY_COL_FROM_KEY,colid)

    copyParms = []
    if(not(cfg.get_config_value(cfg.COPY_COL_TO_KEY) == None)) : 
        copyParms.append(cfg.get_config_value(cfg.COPY_COL_TO_KEY))
    else :
        copyParms.append("")
                    
    if(not(cfg.get_config_value(cfg.COPY_COL_FROM_KEY) == None)) : 
        copyParms.append(cfg.get_config_value(cfg.COPY_COL_FROM_KEY))
    else :
        copyParms.append("")

    if( (len(copyParms[0]) > 0) or (len(copyParms[1])) ) :  
        cfg.set_config_value(copy_columns_input_id+"Parms",copyParms)


    common_column_heading_html      =   "<div>Copy Column Parameters</div>"
        
    grid_input_form     =   InputForm(copy_columns_input_id,
                                      copy_columns_input_idList,
                                      copy_columns_input_labelList,
                                      copy_columns_input_typeList,
                                      copy_columns_input_placeholderList,
                                      copy_columns_input_jsList,
                                      copy_columns_input_reqList,
                                      True)
           
    grid_input_form.set_custombwidth(80)
    grid_input_form.set_gridwidth(280)
    
    grid_input_html   =   grid_input_form.get_html()
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [common_column_heading_html,grid_input_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("col-narrow-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("col-narrow-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_mapping_col(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display cols table to map from
    * 
    * parms :
    *  df       -   dataframe
    *  colname  -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    cfg.set_config_value(cfg.MAP_TRANSFORM_COL_NAME_KEY,colname)
    
    counts  =   df[colname].value_counts().to_dict()
    uniques =   list(counts.keys())

    if(is_numeric_col(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)) :
        uniques.sort()

    keyslist = ""
            
    for i in range(len(uniques)) :
        keyslist = (keyslist + str(uniques[i])) 
        if(not((i+1) == len(uniques))) :
            keyslist = (keyslist + str(","))
            
    parmslist = []
            
    parmslist.append("")
    parmslist.append("")
    parmslist.append(keyslist)
    parmslist.append("")
        
    parmsProtect = [False,False,True,False]
        
    cfg.set_config_value(transform_map_input_id+"Parms",parmslist)
    cfg.set_config_value(transform_map_input_id+"ParmsProtect",parmsProtect)

    map_form    =   InputForm(transform_map_input_id,
                              transform_map_input_idList,
                              transform_map_input_labelList,
                              transform_map_input_typeList,
                              transform_map_input_placeholderList,
                              transform_map_input_jsList,
                              transform_map_input_reqList)
    
    selectDicts     =   []
    mapsel     =   {"default" : "True",
                    "list" : ["True","False"]}
    selectDicts.append(mapsel)
           
    get_select_defaults(map_form,
                        transform_map_input_id,
                        transform_map_input_idList,
                        transform_map_input_typeList,
                        selectDicts)

    return(map_form)

        
def display_apply_fn_inputs(colname,fromSelect=False) :
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
    
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    col_stats_html  =   display_col_stats(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                          colname,
                                          False,
                                          True)
        
    selectDicts     =   []
    lambdaflag      =   {"default":"False","list":["True","False"]}
    selectDicts.append(lambdaflag)
    
    #if(genfuncs) :
        
    from dfcleanser.sw_utilities.sw_utility_genfunc_widgets import get_genfunc_list
    funcs_list  =   get_genfunc_list()
        
    funcs           =   []
    funcs.append(" ")
        
    if(not (funcs_list == None)) :
        for i in range(len(funcs_list)) :
            funcs.append(funcs_list[i])
        
    funclist    =   {"default":" ","list":funcs, "callback":"get_selected_value"}
    selectDicts.append(funclist)

    applyfn_input_form = InputForm(apply_column_gf_input_id,
                                   apply_column_gf_input_idList,
                                   apply_column_gf_input_labelList,
                                   apply_column_gf_input_typeList,
                                   apply_column_gf_input_placeholderList,
                                   apply_column_gf_input_jsList,
                                   apply_column_gf_input_reqList)
        
    get_select_defaults(applyfn_input_form,
                        apply_column_gf_input_id,
                        apply_column_gf_input_idList,
                        apply_column_gf_input_typeList,
                        selectDicts)
        
    applyfn_input_form.set_buttonstyle({"font-size":13, "height":75, "width":75, "left-margin":0})
    applyfn_input_form.set_gridwidth(480)
    applyfn_input_form.set_shortForm(True)
    applyfn_input_form.set_fullparms(True)
    
    if(not (fromSelect)) :
        cfg.set_config_value(apply_column_gf_input_id+"Parms",[colname,"","","","","",""])
        
    applyfn_input_html = ""
    applyfn_input_html = applyfn_input_form.get_html()
        
    applyfn_heading_html      =   "<div>" + apply_column_gf_input_title + "</div><br>"

    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [col_stats_html,applyfn_heading_html,applyfn_input_html]
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("generic-gf-transform-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("generic-gf-transform-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()


def display_apply_fn_sel_inputs(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the selected apply function
    * 
    * parms :
    *  parms    -   transform parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    print("APPLYING_SEL_FUN",parms)
    ftitle = parms[1]
    cparms      =   cfg.get_config_value(apply_column_gf_input_id+"Parms")
    colname     =   cparms[0]
        
    from dfcleanser.sw_utilities.sw_utility_genfunc_control import get_generic_function, get_generic_function_desc
    from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_function_call,is_lambda_function
    gt_func         =   get_generic_function(ftitle)
    gt_func_desc    =   get_generic_function_desc(ftitle)
        
    if(not (gt_func == None)) :
            
        lambda_flag     =   is_lambda_function(ftitle)
        if(lambda_flag) :   lambda_val      =   "True"
        else :              lambda_val      =   "False"
        
        func_parms_dict     =   {}
        func_parms_dict.update({"dftitle":cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)})
        func_parms_dict.update({"dfcolname":colname})
        func_parms_dict.update({"newcolname":None})
            
        func_call   =   get_function_call(ftitle,func_parms_dict)
          
        import dfcleanser.sw_utilities.sw_utility_genfunc_model as gfm
        if(ftitle in gfm.reservedfunctions) :
            from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule
            fparms = [colname,
                      reservedfunctionsmodule,
                      ftitle,
                      lambda_val,
                      func_call,
                      gt_func_desc]
                
        else :
            fparms = [colname,
                      gt_func.get_func_module(),
                      gt_func.get_func_title(),
                      "",
                      "",
                      gt_func.get_func_code()]
                
    cfg.set_config_value(apply_column_gf_input_id+"Parms",fparms)

    display_apply_fn_inputs(colname,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()















