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

from dfcleanser.common.html_widgets import (display_composite_form, get_button_tb_form, get_html_spaces,
                                            get_input_form, get_header_form, get_radio_button_form, 
                                            get_blank_line_form, displayHeading, maketextarea,
                                            addheading, RadioGroupForm, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR)

from dfcleanser.common.common_utils import (displayParms, get_datatype_id, display_status, 
                                            opStatus, get_datatype_str, get_parms_for_input,
                                            is_numeric_col, display_jupyter_HTML, display_grid)

from dfcleanser.common.display_utils import display_column_names

from IPython.display import (clear_output, HTML)


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
                                                 "Apply</br>fn To</br>Column",
                                                 "Map/</br>Dummies/</br>Category",
                                                 "Return","Help"]

columns_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.RENAME_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.ADD_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DROP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.REORDER_COLUMNS)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SAVE_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.COPY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.SORT_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.APPLY_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CATS_TASKBAR)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CLEAR_COLUMN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ID) + ")"]

"""
#--------------------------------------------------------------------------
#   column categorical task bar
#--------------------------------------------------------------------------
"""
cols_cat_transform_tb_doc_title              =   "DataFrame Columns Categorical Options"
cols_cat_transform_tb_title                  =   "DataFrame Columns Categorical Options"
cols_cat_transform_tb_id                     =   "colscattransformoptionstb"

cols_cat_transform_tb_keyTitleList           =   ["Map</br> Column",
                                                 "Dummies</br>For</br>Column",
                                                 "Make</br> Column</br>Categorical",
                                                 "Return","Help"]

cols_cat_transform_tb_jsList                 =   ["cols_transform_tb_callback("+str(dtm.MAP_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.DUMMIES_COLUMN)+")",
                                                 "cols_transform_tb_callback("+str(dtm.CAT_COLUMN)+")",
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
                                             None,None,None]

add_column_input_labelList              =   ["new_column_name",
                                             "Get Column</br>Values</br>From File",
                                             "Get Column</br>Values</br>From</br>User Code",
                                             "Return"]

add_column_input_typeList               =   ["text","button","button","button"]

add_column_input_placeholderList        =   ["enter the new column name",
                                             None,None,None]

add_column_input_jsList                 =    [None,
                                              "data_transform_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_FILE_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(dtm.DISPLAY_ADD_FROM_CODE_OPTION) + ")",
                                              "data_transform_add_cols_callback(" + str(ADD_COLUMN_RETURN) + ")"]

add_column_input_reqList                =   [0]

"""
#--------------------------------------------------------------------------
#    add new column - file input
#--------------------------------------------------------------------------
"""
add_column_file_input_title              =   "Add Column Parameters"
add_column_file_input_id                 =   "addcolfileInput"
add_column_file_input_idList             =   ["addColumnName",
                                              "addColumnfname",
                                              None,None,None]

add_column_file_input_labelList          =   ["new_column_name",
                                              "Column Values File",
                                              "Add New</br>Column",
                                              "Return","Help"]

add_column_file_input_typeList           =   ["text","file",
                                              "button","button","button"]

add_column_file_input_placeholderList    =   ["enter the new column name",
                                              "enter the file name of list to use as values",
                                              None,None,None]

add_column_file_input_jsList             =    [None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_FILE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_FILE_ID) + ")"]

add_column_file_input_reqList            =   [0]

"""
#--------------------------------------------------------------------------
#    add new column - user code
#--------------------------------------------------------------------------
"""
add_column_code_input_title              =   "Add Column Parameters"
add_column_code_input_id                 =   "addcolcodeInput"
add_column_code_input_idList             =   ["addColumnName",
                                              "addColumncode",
                                              None,None,None,None,None,None]

add_column_code_input_labelList          =   ["new_column_name",
                                              "Add Column Code",
                                              "Open</br>Test</br>Code Cell",
                                              "Get Code</br>from</br>Test Cell",
                                              "Save</br>Code as</br>Generic",
                                              "Add New</br>Column</br>From Code",
                                              "Return","Help"]

add_column_code_input_typeList           =   ["text",maketextarea(15),
                                              "button","button","button","button","button","button"]

add_column_code_input_placeholderList    =   ["enter the new column name",
                                              "enter python code to generate column values (default - column id values)",
                                              None,None,None,None,None,None]

add_column_code_input_jsList             =    [None,None,
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_MAKE_NEW_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_GET_NEW_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_SAVE_NEW_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.PROCESS_ADD_NEW_CODE_OPTION) + ")",
                                               "data_transform_add_cols_callback(" + str(dtm.ADD_COLUMN_RETURN) + ")",
                                               "displayhelp(" + str(dfchelp.TRANSFORM_COLS_ADD_USER_ID) + ")"]

add_column_code_input_reqList            =   [0,1]

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
                                              "data_transform_cols_callback(1,"+str(dtm.DROP_COLUMN)+")",
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
                                              "data_transform_cols_callback(1,"+str(dtm.SAVE_COLUMN)+")",
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
                                               "data_transform_cols_callback(1,"+str(dtm.REORDER_COLUMNS)+")",
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
                                             "Copy Column",
                                             "Return","Help"]

copy_columns_input_typeList             =   ["text","text",
                                             "button","button","button"]

copy_columns_input_placeholderList      =   ["column to move",
                                             "column to move after", 
                                             None,None,None]

copy_columns_input_jsList               =    [None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.COPY_COLUMN)+")",
                                              "data_transform_cols_callback(1,"+str(dtm.COPY_COLUMN)+")",
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

sort_column_input_typeList              =   ["text","text","text",
                                             "button","button","button"]

sort_column_input_placeholderList       =   ["column to sort by",
                                             "ascending sort order (default = False)",
                                             "reorder the row id column after the sort (default True)",
                                             None,None,None]

sort_column_input_jsList                =    [None,None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.SORT_COLUMN)+")",
                                              "data_transform_cols_callback(1,"+str(dtm.SORT_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_SORT_BY_COL_ID) + ")"]

sort_column_input_reqList               =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    apply fn to column
#--------------------------------------------------------------------------
"""
apply_column_input_title                 =   "Apply fn To Column Parameters"
apply_column_input_id                    =   "applycolInput"
apply_column_input_idList                =   ["applyColumnname",
                                             "simpleflag",
                                             "fnname",
                                             "fntoapply",
                                             None,None,None]

apply_column_input_labelList             =   ["column_to_apply_fn_to",
                                              "lambda_fn_flag",
                                             "function_name",
                                             "function_code",
                                             "Apply Fn</br>To Column",
                                             "Return","Help"]

apply_column_input_typeList              =   ["text","text","text",maketextarea(10),
                                             "button","button","button"]

apply_column_input_placeholderList       =   ["column to sort by",
                                              "function lambda flag (True - lambda : False - non lamda (default : True))",
                                             "function name ",
                                             "function to apply",
                                             None,None,None]

apply_column_input_jsList                =    [None,None,None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.APPLY_COLUMN)+")",
                                              "data_transform_cols_callback(1,"+str(dtm.APPLY_COLUMN)+")",
                                              "displayhelp(" + str(dfchelp.TRANSFORM_COLS_APPLY_FN_ID) + ")"]

apply_column_input_reqList               =   [0,1,2,3]

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

transform_map_input_typeList            =   ["file","text",
                                             maketextarea(3),maketextarea(3),
                                             "button","button","button"]

transform_map_input_placeholderList     = ["enter File name containing mapping or browse to file below",
                                           "ignore Nans (default = True)",
                                           "mapping keys ** see List Utiltity below",
                                           "enter mapping values {comma separated) ** see List Utiltity below",
                                           None,None,None]

transform_map_input_jsList              =    [None,None,None,None,
                                              "data_transform_cols_callback(0,"+str(dtm.MAP_COLUMN)+")",
                                              "data_transform_cols_callback(1,"+str(dtm.MAP_COLUMN)+")",
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
                                             "Make Dummies</br> for Column",
                                             "Return","Help"]

transform_dummy_input_typeList          =   ["text","button","button","button"]

transform_dummy_input_placeholderList   =   ["remove original column (default = True)",
                                             None,None,None]
 
transform_dummy_input_jsList            =   [None,
                                             "data_transform_cols_callback(0,"+str(dtm.DUMMIES_COLUMN)+")",
                                             "data_transform_cols_callback(1,"+str(dtm.DUMMIES_COLUMN)+")",
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

transform_category_input_typeList       =   ["text","text","button","button","button"]

transform_category_input_placeholderList =  ["make column categorical (default = True)",
                                             "convert column to category datatype (default = False)",
                                             None,None,None]

transform_category_input_jsList         =   [None,None,
                                             "data_transform_cols_callback(0,"+str(dtm.CAT_COLUMN)+")",
                                             "data_transform_cols_callback(1,"+str(dtm.CAT_COLUMN)+")",
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
#   data type radio 
#--------------------------------------------------------------------------
"""
dt_data_type_radio_id                   =   "dtconvertdatatype"
dt_data_type_radio_idList               =   ["uint8rcid","uint16rcid",
                                             "uint32rcid","uint64rcid",
                                             "int8rcid","int16rcid","int32rcid","int64rcid",
                                             "float16rcid","float32rcid","float64rcid",
                                             "datetimercid","strrcid","objectrcid",
                                             "intrcid","floatrcid"]

dt_data_type_radio_labelList            =   ["&nbsp;uint8&nbsp;","&nbsp;uint16&nbsp;",
                                             "&nbsp;uint32&nbsp;","&nbsp;uint64&nbsp;",
                                             "&nbsp;&nbsp;int8&nbsp;","&nbsp;&nbsp;int16&nbsp;",
                                             "&nbsp;int32&nbsp;","&nbsp;int64&nbsp;",
                                             "float16","float32","float64",
                                             "datetime","&nbsp;&nbsp;&nbsp;str&nbsp;&nbsp;&nbsp;",
                                             "object",
                                             "&nbsp;&nbsp;&nbsp;int&nbsp;&nbsp;&nbsp;",
                                             "&nbsp;float&nbsp;"]

"""
#--------------------------------------------------------------------------
#   data type input 
#--------------------------------------------------------------------------
"""
dt_data_type_input_title                =   "Change Data Type Parameters"
dt_data_type_input_id                   =   "dtdatatypeinput"
dt_data_type_input_idList               =   ["dtfillna",
                                             None,None,None,None]

dt_data_type_input_labelList            =   ["fillna_value",
                                             "Change</br> DataType",
                                             "Cleanse</br> Column",
                                             "Return","Help"]

dt_data_type_input_typeList             =   ["text","button","button","button","button"]

dt_data_type_input_placeholderList      =   ["fillna value is required",
                                             None,None,None,None]

dt_data_type_input_jsList               =   [None,
                                             "process_cols_datatype_transform_callback(0)",
                                             "process_cols_datatype_transform_callback(1)",
                                             "process_cols_datatype_transform_callback(2)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_COLS_DTYPE_ID) + ")"]

dt_data_type_input_reqList              =   [0]

"""
#--------------------------------------------------------------------------
#    datatype taskbar 
#--------------------------------------------------------------------------
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
    display_composite_form([get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                               columns_transform_tb_keyTitleList,
                                                               columns_transform_tb_jsList,
                                                               False))])

def displpay_datatype_input_forms(cdtype) :
    
    change_data_type    =   RadioGroupForm(dt_data_type_radio_id,
                                           dt_data_type_radio_idList,
                                           dt_data_type_radio_labelList)
    change_data_type.set_checked(cdtype)

    display_composite_form([get_radio_button_form(change_data_type),
                            get_input_form(InputForm(dt_data_type_input_id,
                                                     dt_data_type_input_idList,
                                                     dt_data_type_input_labelList,
                                                     dt_data_type_input_typeList,
                                                     dt_data_type_input_placeholderList,
                                                     dt_data_type_input_jsList,
                                                     dt_data_type_input_reqList))])

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
   return(get_parms_for_input(parms[3],apply_column_input_idList))

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
    
    clear_output()
    
    if( (refparm == dtm.MAPPING_DETAILS) or 
        (refparm == dtm.DUMMIES_DETAILS) or 
        (refparm == dtm.CATEGORIES_DETAILS) ) :
        
        data_transform_forms  =   [get_button_tb_form(ButtonGroupForm(cols_cat_transform_tb_id,
                                                                      cols_cat_transform_tb_keyTitleList,
                                                                      cols_cat_transform_tb_jsList,
                                                                      False))]   
    else :
        data_transform_forms  =   [get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                                      columns_transform_tb_keyTitleList,
                                                                      columns_transform_tb_jsList,
                                                                      False))]

    display_composite_form(data_transform_forms)

    print("\n") 
    
    if(len(status)> 0) :
        display_status(status)
     
    if(displaycollist) :
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note("<b>*</b> Select a Column for " + note + " by clicking on Column Name above.")
        col_names_table.set_refParm(str(refparm))
    
        if(callbacks) :
            display_column_names(cfg.get_dc_dataframe(),col_names_table,"dtctcol")
        else :
            display_column_names(cfg.get_dc_dataframe(),col_names_table,None)    
    else :
        displayHeading("  " + note,4)
 
"""
#--------------------------------------------------------------------------
#    display cols table to map from 
#--------------------------------------------------------------------------
"""
def display_mapping_col(df,colname) :
    
    cfg.set_config_value(cfg.MAP_TRANSFORM_COL_NAME_KEY,colname)
    
    counts  =   df[colname].value_counts().to_dict()
    uniques =   list(counts.keys())

    if(is_numeric_col(cfg.get_dc_dataframe(),colname)) :
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

    display_composite_form([get_input_form(InputForm(transform_map_input_id,
                                                     transform_map_input_idList,
                                                     transform_map_input_labelList,
                                                     transform_map_input_typeList,
                                                     transform_map_input_placeholderList,
                                                     transform_map_input_jsList,
                                                     transform_map_input_reqList),
                                           "Column " + str(colname) + "  Mapping Parameters")])


"""
#--------------------------------------------------------------------------
#    display add column specific methods
#--------------------------------------------------------------------------
"""    
"""
#    parse parms for add columns 
"""    
def parse_add_cols_option_inputs(parms,opstat=None) :
    
    #print("parse_add_cols_option",parms)
    optionid    =   -1
    dtid        =   -1
    dtypes      =   ""
    newcolname  =   ""
    fparms      =   []
    
    labels      =   []
    values      =   []
    
    if(len(parms[0]) > 1) :
        optionid    =   int(parms[0][2])

    if(len(parms)>1) :
        
        if(optionid == dtm.PROCESS_FILE_OPTION) :
            fparms = get_parms_for_input(parms[2],add_column_file_input_idList)
        elif(optionid == dtm.PROCESS_MAKE_NEW_CODE_OPTION) :
            fparms = get_parms_for_input(parms[2],add_column_code_input_idList)
        elif(optionid == dtm.PROCESS_ADD_NEW_CODE_OPTION) :
            fparms = get_parms_for_input(parms[2],add_column_code_input_idList)
        elif(optionid == dtm.DISPLAY_ADD_FROM_CODE_OPTION) :
            fparms = get_parms_for_input(parms[2],add_column_input_idList)
        
        if(len(fparms) > 0) :
            newcolname = fparms[0]
            cfg.set_config_value(cfg.ADD_COL_COL_NAME_KEY,newcolname)
        
        # check if datatype selection is being returned
        if(cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY) == None) :
            dtypes = parms[1]
            if(len(dtypes) > 0) :
                dtid = int(dtypes)
            if(dtid != -1) :
                cfg.set_config_value(cfg.ADD_COL_DATATYPE_ID_KEY,dtid)
        else :
            dtid = cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
    
    if(not (cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY) == None) ) :                            
        labels.append("New Column Data Type")
        values.append(str(get_datatype_str(cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY))))

    # check if user entered new column name    
    if(len(newcolname) > 0) :
        
        # check if new column name already exists
        collist = cfg.get_dc_dataframe().columns.tolist()
        found = False
        for i in range(len(collist)) :
            if(collist[i] == newcolname) :
                found = True
        
        if(not found) :
        
            if(optionid == dtm.PROCESS_FILE_OPTION) :
                cfg.set_config_value(add_column_file_input_id+"Parms",[newcolname,""]) 
            elif(optionid == dtm.PROCESS_MAKE_NEW_CODE_OPTION) :
                cfg.set_config_value(add_column_code_input_id+"Parms",[newcolname,fparms[1]]) 
            elif(optionid == dtm.PROCESS_MAKE_NEW_CODE_OPTION) :
                cfg.set_config_value(add_column_code_input_id+"Parms",[newcolname,""])
                
                print("cfg\n",cfg.get_config_value(add_column_code_input_id+"Parms"))
                
                
            labels.append("New Column Name")
            values.append(newcolname)
                
        else :
            cfg.drop_config_value(add_column_file_input_id+"Parms")    
            cfg.drop_config_value(add_column_code_input_id+"Parms")
            
            opstat.set_status(False)
            opstat.set_errorMsg("   [Column Name Error] : column ",newcolname," already exists")

    # if no parse errors display parms and fields
    if(opstat.get_status()) :
        
        # display the user entered parms    
        if((len(labels) > 0) and (len(values) > 0)) :
            displayParms("Add Column Parameters",labels,values,cfg.DataTransform_ID)

        # if user did not enter data type selection redisplay data types        
        if(cfg.get_config_value(cfg.ADD_COL_DATATYPE_ID_KEY) == None) :
             
            display_jupyter_HTML(HTML(addheading(get_html_spaces(27) + "Select the datatype of the New Column",5))) 
            display_composite_form([get_radio_button_form(RadioGroupForm(dt_data_type_radio_id,
                                                                         dt_data_type_radio_idList,
                                                                         dt_data_type_radio_labelList))])
            
    return([optionid,dtid,newcolname,fparms])

"""
#   display the gneric for add code 
"""
def display_add_cols_code() :

    from dfcleanser.sw_utilities.sw_utility_genfunc_widgets import get_genfunc_html, FOR_ADD_COLUMNS
    gtlistHtml = get_genfunc_html(FOR_ADD_COLUMNS)

    gt_input_form = InputForm(add_column_code_input_id,
                              add_column_code_input_idList,
                              add_column_code_input_labelList,
                              add_column_code_input_typeList,
                              add_column_code_input_placeholderList,
                              add_column_code_input_jsList,
                              add_column_code_input_reqList)
    
    gt_input_form.set_shortForm(False)
    gt_input_form.set_gridwidth(700)
    gt_input_form.set_fullparms(True)
    
    gt_input_html = ""
    gt_input_html = gt_input_form.get_html()
        
    gt_heading_html = "<h4>" + get_html_spaces(4) + add_column_code_input_title + "</h4>"

    display_grid("generic_transform_wrapper",
                 gt_heading_html,
                 gtlistHtml,
                 gt_input_html,
                 None)

"""
#    display add column options 
"""
def display_add_cols_option(parms) :
    

    display_col_transform_columns(22,"Add Column","",False)
    #print("display_add_cols_option",parms)
    
    optionid    =   -1
    code        =   ""
    newcolname  =   ""
    nparms      =   []
    
    opstat  =   opStatus()
    
    parsedParms = parse_add_cols_option_inputs(parms,opstat)
 
    optionid    =   parsedParms[0]
    newcolname  =   parsedParms[2]
    nparms      =   parsedParms[3]

    if(optionid == dtm.DISPLAY_BASE_ADD_OPTION) :
        display_composite_form([get_input_form(InputForm(add_column_input_id,
                                                         add_column_input_idList,
                                                         add_column_input_labelList,
                                                         add_column_input_typeList,
                                                         add_column_input_placeholderList,
                                                         add_column_input_jsList,
                                                         add_column_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Add Column Parameters")])
            
    elif(optionid == dtm.DISPLAY_ADD_FROM_FILE_OPTION) :
        display_composite_form([get_input_form(InputForm(add_column_file_input_id,
                                                         add_column_file_input_idList,
                                                         add_column_file_input_labelList,
                                                         add_column_file_input_typeList,
                                                         add_column_file_input_placeholderList,
                                                         add_column_file_input_jsList,
                                                         add_column_file_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Add Column Parameters")])
            
    elif(optionid == dtm.DISPLAY_ADD_FROM_CODE_OPTION) :
        
        if(cfg.get_config_value(cfg.ADD_COL_CODE_KEY) == None) :
            cfg.set_config_value(add_column_code_input_id+"Parms",
                             [newcolname,"# function title\n" + 
                                         "from dfcleanser.common.cfg import get_dc_dataframe\n" + 
                                         "from dfcleanser.data_transform.data_transform_columns_widgets import set_NewColumnValues\n" +
                                         "# add new column code\n" +
                                         "NewColumnValues = []\n\n\n" + 
                                         "set_NewColumnValues(NewColumnValues)\n"])
        else :
            cfg.set_config_value(add_column_code_input_id+"Parms",
                             [newcolname,cfg.get_config_value(cfg.ADD_COL_CODE_KEY)])
            
        display_add_cols_code()
    
    elif(optionid == dtm.PROCESS_FILE_OPTION) :
        from dfcleanser.data_transform.data_transform_columns_control import process_add_column
        process_add_column([optionid,nparms])

    elif(optionid == dtm.PROCESS_MAKE_NEW_CODE_OPTION) :
        
        if(not (cfg.get_config_value(cfg.ADD_COL_CODE_KEY) == None) ) :
            cfg.set_config_value(add_column_code_input_id+"Parms",[newcolname,cfg.get_config_value(cfg.ADD_COL_CODE_KEY)])
        
        display_add_cols_code()
        
    elif(optionid == dtm.PROCESS_GET_NEW_CODE_OPTION) :
        
        fparms = get_parms_for_input(parms[2],add_column_code_input_idList)
        newcode = fparms[1]
        
        code = "# new column code" + newcode
        cfg.set_config_value(add_column_code_input_id+"Parms",[newcolname,code])
        cfg.set_config_value(cfg.ADD_COL_CODE_KEY,code)
        
        display_add_cols_code()
                
    elif(optionid == dtm.PROCESS_SAVE_NEW_CODE_OPTION) :
        
        fparms = get_parms_for_input(parms[2],add_column_code_input_idList)
        newcode = fparms[1]
        
        startcode = newcode.find("from dfcleanser.common.cfg import get_dc_dataframe")
        title = newcode[2:startcode-1]
        newcode = newcode[startcode:len(newcode)]
        from dfcleanser.data_transform.data_transform_widgets import add_generic_function
        add_generic_function(title,newcode)
        
        display_add_cols_code()
        
    elif(optionid == dtm.PROCESS_ADD_NEW_CODE_OPTION) :
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_control import process_add_column
        process_add_column([optionid,nparms])
        
    elif(optionid == dtm.PROCESS_SELECT_FUNC_OPTION) :
        
        title = parms[1]
        
        cparms      =   cfg.get_config_value(add_column_code_input_id+"Parms")
        newcolname  =   cparms[0]
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_control import get_generic_function
        gf = get_generic_function(title)
        
        cfg.set_config_value(add_column_code_input_id+"Parms",[newcolname,gf])
        
        display_add_cols_code()
        
"""
#--------------------------------------------------------------------------
#    end display add column specific methods
#--------------------------------------------------------------------------
"""    

        
"""
#------------------------------------------------------------------
#   display the apply function to column parms
#------------------------------------------------------------------
"""
def display_apply_fn_inputs(colname) :
    
    from dfcleanser.common.common_utils import is_numeric_col
    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    display_col_stats(cfg.get_dc_dataframe(),colname,is_numeric_col(cfg.get_dc_dataframe(),colname))
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_widgets import get_genfunc_html, FOR_APPLY_FN
    gtlistHtml = get_genfunc_html(FOR_APPLY_FN)

    applyfn_input_form = InputForm(apply_column_input_id,
                                   apply_column_input_idList,
                                   apply_column_input_labelList,
                                   apply_column_input_typeList,
                                   apply_column_input_placeholderList,
                                   apply_column_input_jsList,
                                   apply_column_input_reqList)
    
    applyfn_input_form.set_shortForm(False)
    applyfn_input_form.set_gridwidth(700)
    applyfn_input_form.set_fullparms(True)
    
    applyfn_input_html = ""
    applyfn_input_html = applyfn_input_form.get_html()
        
    applyfn_heading_html = "<h4>" + get_html_spaces(4) + apply_column_input_title + "</h4>"

    display_grid("generic_transform_wrapper",
                 applyfn_heading_html,
                 gtlistHtml,
                 applyfn_input_html,
                 None)


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
        display_composite_form([get_button_tb_form(ButtonGroupForm(cols_cat_transform_tb_id,
                                                                   cols_cat_transform_tb_keyTitleList,
                                                                   cols_cat_transform_tb_jsList,
                                                                   False))])
        
        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data() 
        
    elif(funcid == dtm.RENAMING) :
        display_col_transform_columns(dtm.RENAMING_DETAILS,"renaming","") 
    elif(funcid == dtm.ADDING) :
        
        print("display_transform_cols_option",parms)
        display_add_cols_option(parms)
    elif(funcid == dtm.DROPPING) :
        display_col_transform_columns(dtm.DROPPING_DETAILS,"dropping","")
    elif(funcid == dtm.MOVING) :
        display_col_transform_columns(dtm.MOVING_DETAILS,"moving","")
        display_composite_form([get_input_form(InputForm(reorder_columns_input_id,
                                                         reorder_columns_input_idList,
                                                         reorder_columns_input_labelList,
                                                         reorder_columns_input_typeList,
                                                         reorder_columns_input_placeholderList,
                                                         reorder_columns_input_jsList,
                                                         reorder_columns_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Reorder Columns Parameters")])
    
    elif(funcid == dtm.MAPPING) :
        display_col_transform_columns(dtm.MAPPING_DETAILS,"setting mapping","") 
    elif(funcid == dtm.DUMMIES) :
        display_col_transform_columns(dtm.DUMMIES_DETAILS,"setting dummies","") 
    elif(funcid == dtm.CATEGORIES) :
        display_col_transform_columns(dtm.CATEGORIES_DETAILS,"setting categories","") 
    elif(funcid == dtm.DATATYPE) :
        display_col_transform_columns(dtm.DATATYPE_DETAILS,"data types","")

    #    display_col_transform_columns(30,"display help","")
    elif(funcid == dtm.SAVING) :
        display_col_transform_columns(dtm.SAVING_DETAILS,"saving","") 
    elif(funcid == dtm.COPYING) :
        display_col_transform_columns(dtm.COPYING_DETAILS,"copying","")
        display_composite_form([get_input_form(InputForm(copy_columns_input_id,
                                                         copy_columns_input_idList,
                                                         copy_columns_input_labelList,
                                                         copy_columns_input_typeList,
                                                         copy_columns_input_placeholderList,
                                                         copy_columns_input_jsList,
                                                         copy_columns_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Copy Column Parameters")])

    elif(funcid == dtm.SORTING) : 
        display_col_transform_columns(dtm.SORTING_DETAILS,"sorting","")

    elif(funcid == dtm.APPLYING) :
        display_col_transform_columns(dtm.APPLYING_DETAILS,"applying function","")
    

    #####
    # final processing of column functions
    ####
    
    # display column transform details input
    elif(funcid == dtm.RENAMING_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Rename Column",colid,False) 
        display_composite_form([get_input_form(InputForm(rename_column_input_id,
                                                         rename_column_input_idList,
                                                         rename_column_input_labelList,
                                                         rename_column_input_typeList,
                                                         rename_column_input_placeholderList,
                                                         rename_column_input_jsList,
                                                         rename_column_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Column " + str(colid) + "  Renaming Parameters")])
    
    elif(funcid == dtm.DROPPING_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Drop Column",colid,True) 
        display_composite_form([get_input_form(InputForm(drop_column_input_id,
                                                         drop_column_input_idList,
                                                         drop_column_input_labelList,
                                                         drop_column_input_typeList,
                                                         drop_column_input_placeholderList,
                                                         drop_column_input_jsList,
                                                         drop_column_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Drop Column " + str(colid) + "  Parameters")])
            
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

        #display_col_options_header("moving",colid,True) 
        display_col_transform_columns(dtm.MOVING_DETAILS,"moving "+colid+" after ","")

        display_composite_form([get_input_form(InputForm(reorder_columns_input_id,
                                                         reorder_columns_input_idList,
                                                         reorder_columns_input_labelList,
                                                         reorder_columns_input_typeList,
                                                         reorder_columns_input_placeholderList,
                                                         reorder_columns_input_jsList,
                                                         reorder_columns_input_reqList,
                                                         True),
                                               get_html_spaces(53) + "Reorder Columns Parameters")])

    elif(funcid == dtm.MAPPING_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Map Column",colid,True) 
        display_mapping_col(cfg.get_dc_dataframe(),colid) 

    elif(funcid == dtm.DUMMIES_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Dummies For Column",colid,True) 
        display_composite_form([get_input_form(InputForm(transform_dummy_input_id,
                                                         transform_dummy_input_idList,
                                                         transform_dummy_input_labelList,
                                                         transform_dummy_input_typeList,
                                                         transform_dummy_input_placeholderList,
                                                         transform_dummy_input_jsList,
                                                         transform_dummy_input_reqList),
                                               "Column " + str(colid) + "  Dummies Parameters")])
                
    elif(funcid == dtm.CATEGORIES_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Make Column Categorical",colid,True)
        
        display_composite_form([get_input_form(InputForm(transform_category_input_id,
                                                         transform_category_input_idList,
                                                         transform_category_input_labelList,
                                                         transform_category_input_typeList,
                                                         transform_category_input_placeholderList,
                                                         transform_category_input_jsList,
                                                         transform_category_input_reqList),
                                               "Column " + str(colid) + "  Category Parameters")])

    elif(funcid == dtm.DATATYPE_DETAILS) :

        display_composite_form([get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                                   columns_transform_tb_keyTitleList,
                                                                   columns_transform_tb_jsList,
                                                                   False)),
                                get_header_form("&nbsp;&nbsp;&nbsp;&nbsp;Change Column Data Type")])
        
        print("\n") 
        
        display_column_transform_status(cfg.get_dc_dataframe(),colid)
        display_column_uniques(cfg.get_dc_dataframe(),colid)        
        
        data_type_radio     =   RadioGroupForm(dt_data_type_radio_id,
                                               dt_data_type_radio_idList,
                                               dt_data_type_radio_labelList)
        
        data_type_radio.set_checked(get_datatype_id(cfg.get_dc_dataframe()[colid].dtype))
        display_composite_form([get_radio_button_form(data_type_radio)])
        
        nans      =     cfg.get_dc_dataframe()[colid].isnull().sum()
        if(nans > 0) :
            print("\n")
            display_composite_form([get_input_form(InputForm(dt_data_type_input_id,
                                                             dt_data_type_input_idList,
                                                             dt_data_type_input_labelList,
                                                             dt_data_type_input_typeList,
                                                             dt_data_type_input_placeholderList,
                                                             dt_data_type_input_jsList,
                                                             dt_data_type_input_reqList,
                                                                  True),
                                                    get_html_spaces(78) + "Data Type Change Parameters")])
        else :
            display_composite_form([get_button_tb_form(ButtonGroupForm(dt_data_type_tb_id,
                                                                       dt_data_type_tb_keyTitleList,
                                                                       dt_data_type_tb_jsList,
                                                                       False))])

    elif(funcid == dtm.SAVING_DETAILS) :
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Save Column",colid,True) 
        display_composite_form([get_input_form(InputForm(save_column_input_id,
                                                         save_column_input_idList,
                                                         save_column_input_labelList,
                                                         save_column_input_typeList,
                                                         save_column_input_placeholderList,
                                                         save_column_input_jsList,
                                                         save_column_input_reqList,
                                                         True),
                                               get_html_spaces(63) + "Save Column " + str(colid) + "  Parameters")])

    elif(funcid == dtm.COPYING_DETAILS) :

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

        display_col_transform_columns(dtm.COPYING_DETAILS,"copying","")

        display_composite_form([get_input_form(InputForm(copy_columns_input_id,
                                                         copy_columns_input_idList,
                                                         copy_columns_input_labelList,
                                                         copy_columns_input_typeList,
                                                         copy_columns_input_placeholderList,
                                                         copy_columns_input_jsList,
                                                         copy_columns_input_reqList),
                                                         "Copy Column Parameters")])
    
    
    elif(funcid == dtm.SORTING_DETAILS) :
        cfg.set_config_value(sort_column_input_id+"Parms",[colid,"",""])
        display_col_options_header("&nbsp;&nbsp;&nbsp;&nbsp;Sorting By Column",colid,False) 
        display_composite_form([get_input_form(InputForm(sort_column_input_id,
                                                         sort_column_input_idList,
                                                         sort_column_input_labelList,
                                                         sort_column_input_typeList,
                                                         sort_column_input_placeholderList,
                                                         sort_column_input_jsList,
                                                         sort_column_input_reqList,
                                                         True),None)])

    elif(funcid == dtm.APPLYING_DETAILS) :
        display_composite_form([get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                                   columns_transform_tb_keyTitleList,
                                                                   columns_transform_tb_jsList,
                                                                   False))])
        
        print("\n")
    
        cfg.set_config_value(apply_column_input_id+"Parms",[colid,"True","",""])
        display_apply_fn_inputs(colid)
    
    elif(funcid == dtm.APPLYING_SEL_FUN) :

        title = parms[1]
        cparms      =   cfg.get_config_value(apply_column_input_id+"Parms")
        newcolname  =   cparms[0]
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_control import get_generic_function
        gf = get_generic_function(title)
        
        cfg.set_config_value(apply_column_input_id+"Parms",[newcolname,title,gf])
        display_apply_fn_inputs(newcolname)

    else :
        from dfcleanser.data_transform.data_transform_widgets import display_main_option
        display_main_option(None)
        

"""            
#--------------------------------------------------------------------------
#    display column transform status
#--------------------------------------------------------------------------
"""
def display_column_transform_status(df,colname) :
    

    from dfcleanser.data_transform.data_transform_widgets import display_col_data    
    display_col_data(df,colname)
    

def display_col_options_header(title,colid,displayStats=True) :
    
    display_composite_form([get_button_tb_form(ButtonGroupForm(columns_transform_tb_id,
                                                               columns_transform_tb_keyTitleList,
                                                               columns_transform_tb_jsList,
                                                               False)),
                            get_header_form(title),
                            get_blank_line_form()])
    
    if(displayStats) :           
        display_column_transform_status(cfg.get_dc_dataframe(),colid)


"""            
#------------------------------------------------------------------
#   display col uniques  
#
#       df          -   data frame
#       colname     -   column name
#
#------------------------------------------------------------------
""" 
def display_column_uniques(df,colname) : 
 
    uniques         =   df[colname].unique().tolist()
    uniques.sort()

    uniqueHeader    =   ["Value","Value","Value","Value","Value",
                         "Value","Value","Value","Value","Value"]
    uniqueRows      =   []
    uniqueWidths    =   [10,10,10,10,10,10,10,10,10,10]
    uniqueAligns    =   ["center","center","center","center","center",
                         "center","center","center","center","center"]
    uniqueHrefs     =   []
    
    uniquerow       =   []
 
    uniquesamplesize    =   30
    uniquesperrow       =   10
    
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

    uniques_table.display_table()

"""
#--------------------------------------------------------------------------
#    display datetime datatype change inputs
#--------------------------------------------------------------------------
"""    
def display_dt_convert(df,dtid,colname,nanvalue) :
    
    
    dtconvparms = [dtid,colname,nanvalue]
    
    from dfcleanser.data_transform.data_transform_widgets import display_datetime_convert
    display_datetime_convert(dtconvparms)
    
    

