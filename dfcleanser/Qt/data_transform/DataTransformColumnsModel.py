"""
# DataTransformColumnsModel
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
#--------------------------------------------------------------------------
#    transform columns display objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


from dfcleanser.sw_utilities.dfc_qt_model import (maketextarea)


FOR_CHANGE_DATATYPE         =   0
FOR_MAP_COLUMN              =   1
FOR_MAKE_CATEGORICAL        =   2

"""
#--------------------------------------------------------------------------
#   rename columns 
#--------------------------------------------------------------------------
"""
rename_column_input_title                 =   "Rename Column"
rename_column_input_id                    =   "renamecolInput"
rename_column_input_idList                =   ["renamecolname",
                                               "renamenewcolname",
                                               None,None,None]

rename_column_input_labelList             =   ["column_name",
                                               "new_column_name",
                                               "Rename</br> Column",
                                               "Make Column</br>Names Universal",
                                               "Return"]

rename_column_input_typeList              =   ["text","text",
                                               "button","button","button"]

rename_column_input_placeholderList       =   ["old column name",
                                               "new column name",
                                               None,None,None]

rename_column_input_reqList               =   [0,1]

"""
#--------------------------------------------------------------------------
#   universal column names 
#--------------------------------------------------------------------------
"""
universal_column_input_title                 =   "Rename Column"
universal_column_input_id                    =   "renamecolInput"
universal_column_input_idList                =   ["fillcharid",
                                                   None,None,None]

universal_column_input_labelList             =   ["fill_char",
                                                 "Check</br> Column Names",
                                                 "Make Column</br>Names Universal",
                                                 "Return"]

universal_column_input_typeList              =   ["text",
                                                  "button","button","button"]

universal_column_input_placeholderList       =   ["fill char",
                                                  None,None,None]

universal_column_input_reqList               =   [0]

"""
#--------------------------------------------------------------------------
#    save column
#--------------------------------------------------------------------------
"""
save_column_input_title                 =   "Save Column"
save_column_input_id                    =   "savecolInput"
save_column_input_idList                =   ["savecolnames",
                                             "savefilename",
                                             "savefiletype",
                                             None,None,None]

save_column_input_labelList             =   ["columns_to_save_list",
                                             "save_column(s)_file_name",
                                             "save_column(s)_file_type",
                                             "Save</br> Column(s)",
                                             "Return","Help"]

save_column_input_typeList              =   ["qtlist","file","select",
                                             "button","button","button"]

save_column_input_placeholderList       =   ["column to save",
                                             "File name to save columns to",
                                             "enter File save type (default : json)",
                                             None,None,None]


save_column_input_reqList               =   [0,1,2]









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

save_colind_input_reqList               =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#   copy column
#--------------------------------------------------------------------------
"""
copy_column_input_title                 =   "Copy Column"
copy_column_input_id                    =   "copycolInput"
copy_column_input_idList                =   ["colnames",
                                             "copycolname",
                                             None,None,None]

copy_column_input_labelList             =   ["column_name",
                                             "new_column_name",
                                             "Copy</br> Column(s)",
                                             "Return","Help"]

copy_column_input_typeList              =   ["text","text",
                                             "button","button","button"]

copy_column_input_placeholderList       =   ["column nammes",
                                             "column to copy to",
                                             None,None,None]

copy_column_input_reqList               =   [0,1]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    apply fn to column variants
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""



"""
#--------------------------------------------------------------------------
#    apply dfc fn to column
#--------------------------------------------------------------------------
"""
apply_column_fn_input_title              =   "Apply dfc fn To Column"
apply_column_fn_input_id                 =   "applylcolInput"
apply_column_fn_input_idList             =   ["ap[plycolname]",
                                               None,None,None,None]

apply_column_fn_input_labelList          =   ["column_to_apply_fn_to",
                                              "Apply dfc</br>Function</br>To Column",
                                              "Apply user</br>Function</br>To Column",
                                              "Return","Help"]

apply_column_fn_input_typeList           =   ["text",
                                              "button","button","button","button"]

apply_column_fn_input_placeholderList    =   ["column name",
                                              None,None,None,None]

apply_column_fn_input_reqList            =   [0,1]


"""
#--------------------------------------------------------------------------
#    apply dfc fn to column
#--------------------------------------------------------------------------
"""
apply_column_dfc_fn_input_title              =   "Apply dfc fn To Column"
apply_column_dfc_fn_input_id                 =   "applyldfccolInput"
apply_column_dfc_fn_input_idList             =   ["fnlfnsel",
                                                  "fnparms",
                                                  None,None,None]

apply_column_dfc_fn_input_labelList          =   ["dfc_fns",
                                                  "dfc_fn_parms",
                                                  "Apply dfc</br>Function",
                                                  "Return","Help"]

apply_column_dfc_fn_input_typeList           =   ["select",maketextarea(2),
                                                  "button","button","button"]

apply_column_dfc_fn_input_placeholderList    =   ["dfc function",
                                                  "dfc function parms",
                                                  None,None,None]

apply_column_dfc_fn_input_reqList            =   [0,1]


"""
#--------------------------------------------------------------------------
#    apply user fn to column
#--------------------------------------------------------------------------
"""
apply_user_fn_input_title           =   "Apply User fn"
apply_user_fn_input_id              =   "dfcuserfn"
apply_user_fn_input_idList          =   ["dfcuserfncode",
                                         None,None,None]

apply_user_fn_input_labelList       =   ["user_fn_code",
                                        "Apply</br>User fn</br>To Column",
                                         "Return","Help"]

apply_user_fn_input_typeList        =   [maketextarea(11),
                                         "button","button","button"]

apply_user_fn_input_placeholderList =   [" ",
                                         None,None,None]


apply_user_fn_input_reqList         =   [0]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    add new column variants
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    add new column
#--------------------------------------------------------------------------
"""
add_column_input_title                  =   "Add Column"
add_column_input_id                     =   "addcolInput"
add_column_input_idList                 =   ["addColumnName",
                                             "addNewColumnName",
                                             None,None,None,None]

add_column_input_labelList              =   ["column(s)_to_use",
                                             "new_column_name",
                                             "Get Column</br>Values From</br> dfc fns",
                                             "Get Column</br>Values From</br>User Code",
                                             "Return",
                                             "Help"]

add_column_input_typeList               =   ["text","text","button","button","button","button"]

add_column_input_placeholderList        =   ["enter the column name",
                                             "enter the new column name",
                                            None,None,None,None]

add_column_input_reqList                =   [0,1]

"""
#--------------------------------------------------------------------------
#    add new column - from dfc funcs applied to col
#--------------------------------------------------------------------------
"""

add_column_dfc_fn_input_title              =     "Add dfc fn To Column"
add_column_dfc_fn_input_id                 =     "applyldfccolInput"
add_column_dfc_fn_input_idList             =     ["newcolname",
                                                  "fnlfnsel",
                                                  "fnparms",
                                                  None,None,None]

add_column_dfc_fn_input_labelList          =     ["new_column_name",
                                                  "dfc_fns",
                                                  "dfc_fn_parms",
                                                  "Add Column</br>From dfc fn",
                                                  "Return","Help"]

add_column_dfc_fn_input_typeList           =     ["text",
                                                  "select",maketextarea(2),
                                                  "button","button","button"]

add_column_dfc_fn_input_placeholderList    =     ["new column name",
                                                  "dfc function",
                                                  "dfc function parms",
                                                  None,None,None]

add_column_dfc_fn_input_reqList            =     [0,1,2]


"""
#--------------------------------------------------------------------------
#    add new column - from user defined code
#--------------------------------------------------------------------------
"""

add_column_user_fn_input_title           =   "Add Column User fn"
add_column_user_fn_input_id              =   "addcoluserfn"
add_column_user_fn_input_idList          =   ["addcolusercolname",
                                              "addcoluserfncode",
                                              None,None,None]

add_column_user_fn_input_labelList       =   ["new_column_name",
                                              "user_fn_code",
                                              "Add</br>Column From</br>User Code",
                                              "Return","Help"]

add_column_user_fn_input_typeList        =   ["text",maketextarea(10),
                                              "button","button","button"]

add_column_user_fn_input_placeholderList =   [" "," ",None,None,None]


add_column_user_fn_input_reqList         =   [0]


"""
#--------------------------------------------------------------------------
#    add new column - from dataframe merge
#--------------------------------------------------------------------------
"""

how_select_list             =   ["left","right","outer","inner","cross"]
how_select_default          =   "‘inner’"

left_index_default          =   False
right_index_default         =   False
sort_default                =   False
suffixes_default            =   ["_x", "_y"]
copy_default                =   True
indicator_default           =   False

validate_select_list        =   ["one_to_one","one_to_many","many_to_one","many_to_many"]
validate_select_default     =   None

merge_help_html             =   "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html"

add_column_merge_input_title            =   "Add Column User fn"
add_column_merge_input_id               =   "addcolmerge"
add_column_merge_input_idList           =   ["dftomergewith",
                                             "dfmergecols",
                                             "dfmergecolslist",
                                             "mergetype",
                                             "onmergelist",
                                             "onleftmergelist",
                                             "onrightmergelist",
                                             None,None]

add_column_merge_input_labelList        =   ["dataframe_to_merge_with",
                                             "columns_to merge",
                                             "dataframe_to_merge_with_columns_list",
                                             "merge_type(how)",
                                             "on",
                                             "left_on",
                                             "right_on",
                                             "Add</br>Column(s) From</br>Merge",
                                             "Clear"]

add_column_merge_input_typeList         =   ["select","text","select","select","text","text","text","button","button"]

add_column_merge_input_placeholderList  =   ["dataframe to merge with","columns to merge","columns list","merge type","on","left on","right on",None,None]

add_column_merge_input_reqList          =   [0,1,2,3,4,5,6]


add_column_mergeA_input_title            =   "Add Column User fn"
add_column_mergeA_input_id               =   "addcolAmerge"
add_column_mergeA_input_idList           =   ["leftindexmergelist",
                                             "rightindexmergelist",
                                             "mergesortflag",
                                             "mergesuffixes",
                                             "mergeindicatorflag",
                                             "mergevalidate",
                                             "mergecopyflag",
                                             "mergecopydftitle",
                                             None,None]

add_column_mergeA_input_labelList        =   ["left_index",
                                             "right_index",
                                             "sort",
                                             "suffixes",
                                             "indicator",
                                             "validate",
                                             "copy",
                                             "copy_df_title",
                                             "</br>Return</br>","</br>Help</br>"]

add_column_mergeA_input_typeList         =   ["select","select","select","text","text","select","select","text",
                                              "button","button"]

add_column_mergeA_input_placeholderList  =   ["left index","right index","sort","suffixes","indicator","validate","copy","df copy title",
                                              None,None]

add_column_mergeA_input_reqList          =   [0,1,2,3,4,5,6,7,8]

"""
#--------------------------------------------------------------------------
#    add new column - from dataframe join
#--------------------------------------------------------------------------
"""
join_on_default             =   None

join_how_select_list        =   ["left","right","outer","inner","cross"]
join_how_select_default     =   "left"

join_left_index_default     =   ""
join_right_index_default    =   ""


join_sort_default           =   False

join_help_html              =   "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html"

add_column_join_input_title             =   "Add Column User fn"
add_column_join_input_id                =   "addcoljoin"
add_column_join_input_idList            =   ["dftojoinwith",
                                             "dfjoincols",
                                             "dfjoincolslist",
                                             "jointype",
                                             "howjoint",
                                             "joinlsufffix",
                                             "joinlsufffix",
                                             "joinsortflag",
                                             "joincopyflag",
                                             "joincopydftitle",

                                             None,None,None,None]

add_column_join_input_labelList         =   ["dataframe_to_join_with",
                                             "columns_to join",
                                             "dataframe_to_join_with_columns_list",
                                             "on",
                                             "how",
                                             "left_suffix",
                                             "right_suffix",
                                             "sort",
                                             "copy",
                                             "copy_df_title",
                                             "Add</br>Column(s) From</br>Join",
                                             "Clear","Return","Help"]

add_column_join_input_typeList          =   ["select","text","select","text","select", "text","text","select","select","text",
                                              "button","button","button","button"]
 
add_column_join_input_placeholderList   =   ["dataframe to join with","columns to merge","columns list","on",
                                             "how","left suffix","right suffix","sort","copy","df copy title",
                                              None,None,None,None]

add_column_join_input_reqList           =   [0,1,2,3,4,5,6,7,8,9]



"""
#--------------------------------------------------------------------------
#    data transform map input for single column
#--------------------------------------------------------------------------
"""
transform_map_input_title               =   "Column Mapping"
transform_map_input_id                  =   "maptransformInput"
transform_map_input_idList              =   ["mapcolumn",
                                             "mapfn",
                                             None,None,None]

transform_map_input_labelList           =   ["column_to_map",
                                             "mapping_function",
                                             "Map</br> Column",
                                             "Return","Help"]

transform_map_input_typeList            =   ["text",maketextarea(12),
                                             "button","button","button"]

transform_map_input_placeholderList     =   ["","",
                                             None,None,None]

transform_map_input_reqList             =   [0,1]



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

transform_dummy_input_typeList          =   ["text","select","button","button","button"]

transform_dummy_input_placeholderList   =   ["column to set dummies for",
                                             "remove original column (default = True)",
                                             None,None,None]
 
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
                                             "excludeuniques",
                                             None,None,None]

transform_category_input_labelList      =   ["categorical_column_name",
                                             "categorical_column_ordered",
                                             "categorical_column_categories_uniques_option",
                                             "uniques_to_include_or_exclude",
                                             "Make</br>Column</br>Categorical",
                                             "Return","Help"]

transform_category_input_typeList       =   ["text","select","select",maketextarea(4),"button","button","button"]

transform_category_input_placeholderList =  ["column to make categorical",
                                             "oredered categorical (default = False)",
                                             "all uniques as categories (default = True)",
                                             " uniques to exclude",
                                             None,None,None]

transform_category_input_reqList        =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   datatype variants 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   datatype no nans 
#--------------------------------------------------------------------------
"""
dt_data_type_input_title                =   "Change Data Type"
dt_data_type_input_id                   =   "dtdatatypeinput"
dt_data_type_input_idList               =   ["dtcolname",
                                             "dtdatatype",
                                             None,None,None]

dt_data_type_input_labelList            =   ["column_to_change",
                                             "datatype_to_change_to",
                                             "Change</br>DataType",
                                             "Return","Help"]

dt_data_type_input_typeList             =   ["text","select","button","button","button"]

dt_data_type_input_placeholderList      =   ["column name",
                                             "datatype selected",
                                             None,None,None]

dt_data_type_input_reqList              =   [0,1]


"""
#--------------------------------------------------------------------------
#   datatype nans with fillna 
#--------------------------------------------------------------------------
"""
dt_nans_data_type_input_title           =   "Change Data Type"
dt_nans_data_type_input_id              =   "dtnansdatatypeinput"
dt_nans_data_type_input_idList          =   ["dtcolname",
                                             "dtdatatype",
                                             "dtfillnavalue",
                                             "dtfillnamethod",
                                             "dtfillnalimit",
                                             None,None,None]

dt_nans_data_type_input_labelList       =   ["column_to_change",
                                             "datatype_to_change_to",
                                             "fillna_value",
                                             "fillna_method",
                                             "fillna_threshold_pct",
                                             "Change</br>DataType",
                                             "Return","Help"]

dt_nans_data_type_input_typeList        =   ["text","select","text","select","text","button","button","button"]

dt_nans_data_type_input_placeholderList =   ["column name",
                                             "datatype selected",
                                             "fillna value",
                                             "fillna method",
                                             "limit (default = None)",
                                             None,None,None]

dt_nans_data_type_input_reqList         =   [0,1,2,3,4]


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


dt_str_check_data_type_input_reqList         =   [0,1]




