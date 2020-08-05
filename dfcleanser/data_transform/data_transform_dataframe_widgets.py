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
import dfcleanser.data_transform.data_transform_columns_widgets as dtcw

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm, new_line) 

from dfcleanser.common.table_widgets import dcTable

from dfcleanser.common.common_utils import (get_select_defaults, display_generic_grid,
                                            display_exception, opStatus, display_status)

from dfcleanser.common.display_utils import display_column_names

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

dataframe_transform_tb_doc_title            =   "DataFrame Transform Options"
dataframe_transform_tb_title                =   "DataFrame Transform Options"
dataframe_transform_tb_id                   =   "dftransformoptionstb"

dataframe_transform_tb_keyTitleList         =   ["Column</br>Names</br>Row",
                                                 "dataframe</br>Index",
                                                 "Sort</br>df by</br>Column",
                                                 "Drop</br>Duplicate</br>Rows",
                                                 "Return","Help"]

dataframe_transform_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SORT_COLUMN)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_TASKBAR_ID) + "')"]

dataframe_transform_tb_centered             =   True


"""
#--------------------------------------------------------------------------
#    dataframe column names row tb
#--------------------------------------------------------------------------
"""
dataframe_col_names_tb_doc_title            =   "Column Names Options"
dataframe_col_names_tb_title                =   "Column Names Options"
dataframe_col_names_tb_id                   =   "dfcolnamestb"

dataframe_col_names_tb_keyTitleList         =   ["Show</br>Column</br>Names",
                                                 "Save</br>Column</br>Names",
                                                 "Add </br>Column</br>Names",
                                                 "Change</br>Column</br>Names",
                                                 "Drop</br>Column</br>Names",
                                                 "Column</br>Names</br>Whitespace",
                                                 "Return","Help"]

dataframe_col_names_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.PROCESS_SHOW_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.PROCESS_DROP_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_WHITESPACE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_COL_NAMES_TASKBAR_ID) + "')"]

dataframe_col_names_tb_centered             =   True


"""
#--------------------------------------------------------------------------
#    dataframe indices tb
#--------------------------------------------------------------------------
"""
dataframe_indices_tb_doc_title              =   "DataFrame Indices Options"
dataframe_indices_tb_title                  =   "DataFrame Indices Options"
dataframe_indices_tb_id                     =   "dfIndicestb"

dataframe_indices_tb_keyTitleList           =   ["Show </br> Index",
                                                 "Set </br> Index",
                                                 "Reset</br> Index",
                                                 "Append</br>Index",
                                                 "Sort </br>Index",
                                                 "Return","Help"]

dataframe_indices_tb_jsList                 =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_SHOW_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SET_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_RESET_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_APPEND_TO_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SORT_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_INDEX_TASKBAR_ID) + "')"]

dataframe_indices_tb_centered               =   True


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

df_save_row_transform_input_jsList          =    [None,
                                                 "df_process_cmd_callback("+str(dtm.PROCESS_SAVE_COLUMN_NAMES_ROW) + ")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_SAVE_COL_NAME_ID) + "')"]

df_save_row_transform_input_reqList         =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe add column id row inputs
#--------------------------------------------------------------------------
"""
df_add_row_transform_input_title            =   "Add Column Names Row"
df_add_row_transform_input_id               =   "addcolnamestransform"
df_add_row_transform_input_idList           =   ["filereadname",
                                                 "dfcolsidlist",
                                                 None,None,None]

df_add_row_transform_input_labelList        =   ["column_names_file_name",
                                                 "column_names_list",
                                                 "Add Column</br> Names Row",
                                                 "Return","Help"]

df_add_row_transform_input_typeList         =   ["file",maketextarea(3),
                                                 "button","button","button"]

df_add_row_transform_input_placeholderList  =   ["enter File name to read or browse to file (default blank - no file)",
                                                 "enter the Column Names (default blank - auto generated) ",
                                                 None,None,None]

df_add_row_transform_input_jsList           =   [None,None,
                                                 "df_process_cmd_callback("+str(dtm.PROCESS_ADD_COLUMN_NAMES_ROW) + ")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_SET_COL_NAME_ID) + "')"]

df_add_row_transform_input_reqList          =   [0,1]


"""
#--------------------------------------------------------------------------
#    dataframe add column id row inputs
#--------------------------------------------------------------------------
"""
df_change_row_transform_input_helpurl       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html"

df_change_row_transform_input_title         =   "Add Column Names Row"
df_change_row_transform_input_id            =   "changecolnamestransform"
df_change_row_transform_input_idList        =   ["ccolname",
                                                 "ncolname",
                                                 None,None,None]

df_change_row_transform_input_labelList     =   ["current_column_name",
                                                 "new_column_name",
                                                 "Change Column </br>Name",
                                                 "Return","Help"]

df_change_row_transform_input_typeList      =   ["text","text",
                                                 "button","button","button"]

df_change_row_transform_input_placeholderList  =   ["current column name",
                                                    "new column name",
                                                    None,None,None]

df_change_row_transform_input_jsList        =   [None,None,
                                                 "df_process_cmd_callback("+str(dtm.PROCESS_CHANGE_COLUMN_NAMES) + ")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_CHANGE_COL_NAMES_ID) + "')"]

df_change_row_transform_input_reqList       =   [0,1]


"""
#--------------------------------------------------------------------------
#    df columns row remove whitespace input 
#--------------------------------------------------------------------------
"""
df_cnames_row_remwhite_input_title          =   "Remove Whitespace"
df_cnames_row_remwhite_input_id             =   "remwhitetransformInput"
df_cnames_row_remwhite_input_idList         =   ["wschars",
                                                 "leadtrailflag",
                                                 None,None,None]

df_cnames_row_remwhite_input_labelList      =   ["whitespace_chars",
                                                 "remove_type_flag",
                                                 "Remove</br>Whitspace",
                                                 "Return","Help"]

df_cnames_row_remwhite_input_typeList       =   ["selectmultiple","select","button","button","button"]

df_cnames_row_remwhite_input_placeholderList =  ["whitespace chars",
                                                "remove leading and trailing",
                                                None,None,None]

df_cnames_row_remwhite_input_jsList         =   [None,None,
                                                 "df_process_cmd_callback("+str(dtm.PROCESS_WHITESPACE_COLUMN_NAMES) + ")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DF_WHITESPACE_COL_NAMES_ID) + "')"]

df_cnames_row_remwhite_input_reqList        =   [0,1]


"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_index_transform_input_title            =   "Set New Index Column"
df_set_index_transform_input_id               =   "setnewindextransform"
df_set_index_transform_input_idList           =   ["setnewindexcolid",
                                                   "setnewindexcolnames",
                                                   "setnewindexdrop",
                                                   "setnewindexverify",
                                                   None,None,None]

df_set_index_transform_input_labelList        =   ["index_column_name(s)",
                                                   "df_column_name(s)",
                                                   "drop_index_column_name(s)_cols",
                                                   "verify_integrity",
                                                   "Set</br>Index",
                                                   "Return","Help"]

df_set_index_transform_input_typeList         =   ["text","select","select","select",
                                                   "button","button","button"]

df_set_index_transform_input_placeholderList  =  ["list or single of column name(s) to use as df index",
                                                  "dfcolumn name(s) list",
                                                   "drop df column (default : True)",
                                                   "verify integrity",
                                                   None,None,None]

df_set_index_transform_input_jsList           =    [None,None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_SET_DF_INDEX) + ")",
                                                    "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                    "displayhelp('" + str(dfchelp.TRANSFORM_DF_SET_INDEX) + "')"]

df_set_index_transform_input_reqList          =   [0,1,2,3]


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

df_reset_index_transform_input_labelList    =   ["index_levels_to_drop",
                                                 "index_levels",
                                                 "insert_dropped_columns_into_df",
                                                 "Reset</br>Index",
                                                 "Return","Help"]

df_reset_index_transform_input_typeList     =   ["text","select","select",
                                                 "button","button","button"]

df_reset_index_transform_input_placeholderList =  ["index ;evels to drop",
                                                   "index llevels list",
                                                   "insert df levels to df flag (default : True)",
                                                   None,None,None]

df_reset_index_transform_input_jsList       =    [None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_RESET_DF_INDEX) + ")",
                                                  "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                  "displayhelp('" + str(dfchelp.TRANSFORM_DF_RESET_INDEX) + "')"]

df_reset_index_transform_input_reqList      =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_append_index_transform_input_title         =   "Append Index Column"
df_append_index_transform_input_id            =   "appendindextransform"
df_append_index_transform_input_idList        =   ["appendindexcolid",
                                                   "appendindexcolnames",
                                                   "appendindexdrop",
                                                   "appendindexverify",
                                                   None,None,None]

df_append_index_transform_input_labelList     =   ["index_column_name(s)",
                                                   "df_column_name(s)",
                                                   "drop_index_column_name(s)_cols_from_df",
                                                   "verify_integrity",
                                                   "Append</br>Index",
                                                   "Return","Help"]

df_append_index_transform_input_typeList      =   ["text","select","select","select",
                                                   "button","button","button"]

df_append_index_transform_input_placeholderList   =  ["list or single name of columns to append to index",
                                                      "list of columns namesx",
                                                      "drop df column (default : False)",
                                                      "verify integrity",
                                                      None,None,None]

df_append_index_transform_input_jsList        =    [None,None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_APPEND_TO_INDEX) + ")",
                                                    "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                    "displayhelp('" + str(dfchelp.TRANSFORM_DF_RESET_INDEX) + "')"]

df_append_index_transform_input_reqList       =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    dataframe sort row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_index_transform_input_title            =   "Sort Row Index Column"
df_sort_index_transform_input_id               =   "sortindextransform"
df_sort_index_transform_input_idList           =   ["sortindexlevels",
                                                    "sortindexlevelslist",
                                                    "sortindexorder",
                                                    "sortindexsortkind",
                                                    "sortindexnaposition",
                                                    None,None,None]

df_sort_index_transform_input_labelList        =   ["index_levels_to_sort_by",
                                                    "index_levels_list",
                                                    "ascending",
                                                    "kind",
                                                    "na_position",
                                                    "Sort</br>Index",
                                                    "Return","Help"]

df_sort_index_transform_input_typeList         =   ["text","select","select","select","select",
                                                    "button","button","button"]

df_sort_index_transform_input_placeholderList  =   ["index levels to sort",
                                                    "index levels list",
                                                    "Order of sort : True - ascending - False - descending (default True )",
                                                    "sort method quicksort, mergesort, heapsort (default - quicksort )",
                                                    "where to put nas - first : last (default - last )",
                                                    None,None,None]

df_sort_index_transform_input_jsList           =    [None,None,None,None,None,
                                                     "df_process_cmd_callback("+str(dtm.PROCESS_SORT_DF_INDEX) +")",
                                                     "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                     "displayhelp('" + str(dfchelp.TRANSFORM_DF_SORT_INDEX) + "')"]

df_sort_index_transform_input_reqList          =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    dataframe drop duplicate rows inputs
#--------------------------------------------------------------------------
"""
df_drop_dups_transform_input_title          =   "Drop Duplicate Rows"
df_drop_dups_transform_input_id             =   "dropduplicatetransform"
df_drop_dups_transform_input_idList         =   ["dropduplicatecolids",
                                                 "dropduplicatedfcolnames",
                                                 "dropduplicatedrop",
                                                 "dropduplicatekeep",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["column_drop_keys_list",
                                                 "column_names_list",
                                                 "action_for_columns_in_column_drop_keys_list",
                                                 "keep_duplicates_flag",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(3),"select","select","select",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["enter list of columns to use as keys to identify dups (default blank -  all cols) ",
                                                 "df column names list",
                                                 "drop or keep column_drop_keys_list (default : keep ) ",
                                                 "whihc duplicates to drop (default : False ) ",
                                                 None,None,None]

df_drop_dups_transform_input_jsList         =    [None,None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_DROP_DUPLICATE_ROWS) +")",
                                                  "transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                  "displayhelp('" + str(dfchelp.TRANSFORM_DF_DROP_DUPS) + "')"]

df_drop_dups_transform_input_reqList        =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    sort by column
#--------------------------------------------------------------------------
"""
sort_column_input_title                 =   "Sort Column"
sort_column_input_id                    =   "sortcolInput"
sort_column_input_idList                =   ["sortcolname",
                                             "sortOrder",
                                             "sortkind",
                                             "sortna",
                                             "resetRowIds",
                                             None,None,None]

sort_column_input_labelList             =   ["column_to_sort_by",
                                             "ascending_order_flag",
                                             "kind",
                                             "na_position",
                                             "reset_row_index_flag",
                                             "Sort By</br>Column",
                                             "Return","Help"]

sort_column_input_typeList              =   ["select","select","select","select","select",
                                             "button","button","button"]

sort_column_input_placeholderList       =   ["column to sort by)",
                                             "ascending sort order (default = False)",
                                             "sort method (default = quicksort)",
                                             "na position (default = last)",
                                             "reorder the row id column after the sort (default True)",
                                             None,None,None]

sort_column_input_jsList                =    [None,None,None,None,None,
                                              "df_process_cmd_callback("+str(dtm.PROCESS_SORT_COLUMN)+")",
                                              "transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                              "displayhelp('" + dfchelp.TRANSFORM_DF_SORT_BY_COL_ID + "')"]

sort_column_input_reqList               =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    remote df rows display
#--------------------------------------------------------------------------
"""
remote_display_tb_doc_title           =   "Remote Display df"
remote_display_tb_doc_id              =   "remotedisplaydf"
remote_display_tb_title               =   None

remote_display_tb_keyTitleList        =   ["Display df Rows"]

remote_display_tb_jsList              =   ["display_remote_df_rows('XXXX')"]

remote_display_tb_centered            =   True


datatransform_dataframe_inputs          =   [df_save_row_transform_input_id, df_add_row_transform_input_id, df_change_row_transform_input_id,
                                             df_cnames_row_remwhite_input_id, df_set_index_transform_input_id, df_reset_index_transform_input_id,
                                             df_append_index_transform_input_id, df_sort_index_transform_input_id, df_drop_dups_transform_input_id,
                                             sort_column_input_id, remote_display_tb_doc_id]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_dataframe_transform_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(dataframe_transform_tb_id,
                                               dataframe_transform_tb_keyTitleList,
                                               dataframe_transform_tb_jsList,
                                               dataframe_transform_tb_centered))

def display_dataframe_transform_main() :

    display_dataframe_transform_taskbar() 
    
def display_dataframe_col_names_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(dataframe_col_names_tb_id,
                                               dataframe_col_names_tb_keyTitleList,
                                               dataframe_col_names_tb_jsList,
                                               dataframe_col_names_tb_centered))
    
def display_dataframe_indices_taskbar() :

    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(dataframe_indices_tb_id,
                                               dataframe_indices_tb_keyTitleList,
                                               dataframe_indices_tb_jsList,
                                               dataframe_indices_tb_centered))

def process_dataframe_transform(parms,display=True) :
    from dfcleanser.data_transform.data_transform_dataframe_control import process_df_transform    
    process_df_transform(parms,display=True)


    
def display_common_df_options(df,header_html,grid_input_form,display_index=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display common dataframe transform inputs
    * 
    * parms :
    *   df                  - dataframe
    *   header_html         - input header
    *   grid_input_form     - input form
    *   display_index       - display indices flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    display_dataframe_transform_taskbar()
    
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":25})
    grid_input_form.set_gridwidth(440)
    grid_input_form.set_fullparms(True)  
    
    grid_input_html     =   grid_input_form.get_html()
    
    if(display_index) :
        
        df_index_html       =   display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                                         cfg.get_current_chapter_dfc_df_title(cfg.CURRENT_TRANSFORM_DF),0,False)

    else :
        df_index_html       =   ""        
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
    gridhtmls       =   [header_html,grid_input_html,df_index_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-common-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-common-df-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()

   
def get_collist_without_indices() :

    df,colslist,colname             =   dtcw.get_df_colslist()
    
    indices = df.index.name
    if(not (indices is None)) :
        
        print("indices",indices,type(indices))

    return(colslist)


 
    
def get_no_df_index(df,left_margin) :
    """
    * -------------------------------------------------------------------------- 
    * function : get displayable df indices
    * 
    * parms :
    *   df  - dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
        
    index_string     =   "No indices defined"
    
    indices_html        =   ("<br>" + new_line)
    if(not (left_margin == 0)) :
        indices_html        =   (indices_html + "<div style='text-align:center; width:480px;" + " margin-left: " + str(left_margin) + "px'>" + new_line)
    else :    
        indices_html        =   (indices_html + "<div style='text-align:center; width:480px'>" + new_line)
        
    indices_html        =   (indices_html + "    <div style='text-align:left; width:480px; font-size:12px; font-weight:bold; font-family:arial;'>Current Index Columns</div>" + new_line)
    indices_html        =   (indices_html + "    <div style='text-align:center; width:480px; border: 1px solid #67a1f3; font-size:11px; font-family:arial;'>" + str(index_string) + "</div>" + new_line)
    indices_html        =   (indices_html + "</div>" + new_line)
    indices_html        =   (indices_html + "<br>" + new_line)
    
    return(indices_html)
    
    
def get_index_stats_table(df_title,df,small=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get col stats for df index columns
    * 
    * parms :
    *  df_title -   dataframe title
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    colstatsHeader        =   ["Column Name","Dtype","Max","Min","Num Uniques"]
    colstatsRows          =   []
    colstatsWidths        =   [30,15,20,20,15]
    colstatsAligns        =   ["left","left","left","left","center"]
    
    rowColors             =   []
    
    index_columns   =   df.index.names
    
    if(len(index_columns) > 0) :
        for i in range(len(index_columns)) :
            if( not (index_columns[i] is None) ) :
                colstatsRows.append([index_columns[i],
                                     str(df.index.levels[i].dtype),
                                     str(df.index.levels[i].max()),
                                     str(df.index.levels[i].min()),
                                     str(len(df.index.levels[i].unique()))])
                
                rowColors.append("#ffffcc")
                                 
    colstats_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    colstats_table        =   dcTable("Index Column Stats For dataframe '" + str(df_title) + "'",'indexstatsid',
                                      cfg.DataTransform_ID,
                                      colstatsHeader,colstatsRows,
                                      colstatsWidths,colstatsAligns)
            
    colstats_table.set_small(True)
    
    if(len(rowColors) > 0) :
       colstats_table.set_row_color_list(rowColors)     
    
    if(small) :
        colstats_table.set_smallwidth(60)
        colstats_table.set_smallmargin(200)
    else :   
        colstats_table.set_smallwidth(90)
        colstats_table.set_smallmargin(30)
    
    colstats_table.set_checkLength(True)

    colstats_table.set_border(True)
    colstats_table.set_tabletype(ROW_MAJOR)
    colstats_table.set_rowspertable(50)
    colstatsHtml = get_row_major_table(colstats_table,SCROLL_DOWN,False)
    
    return(colstatsHtml+"<br>")
    

def display_current_df_index(df,df_title,left_margin=0,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display current df indices
    * 
    * parms :
    *  df_title -   dataframe title
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(dtm.is_df_index_defined(df)) :
        
        df_index_html   =     get_index_stats_table(df_title,df,small=False)      
    
    else :
        
        df_index_html   =     get_no_df_index(df,left_margin)      
     
    if(display) :
        
        gridclasses     =   ["dfc-main"]
        gridhtmls       =   [df_index_html]
        display_generic_grid("dfc-short-note-wrapper",gridclasses,gridhtmls)
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
        
    else :
        
        return(df_index_html)

   
"""
#--------------------------------------------------------------------------
#    display dataframe main taskbar widgets
#--------------------------------------------------------------------------
"""
def display_dataframe_options(funcid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display dataframe transform inputs
    * 
    * parms :
    *   funcid   -  function to display id
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    #funcid = parms[0][0]

    if(funcid == dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW) :
        
        display_dataframe_transform_taskbar()
        
        common_dataframe_heading_html       =   "<div>Save Column Names </div><br>"
        
        filename = cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)

        grid_input_form                     =   InputForm(df_save_row_transform_input_id,
                                                          df_save_row_transform_input_idList,
                                                          df_save_row_transform_input_labelList,
                                                          df_save_row_transform_input_typeList,
                                                          df_save_row_transform_input_placeholderList,
                                                          df_save_row_transform_input_jsList,
                                                          df_save_row_transform_input_reqList)
        
        cfg.set_config_value(df_save_row_transform_input_id+"Parms",[filename + "_" + "column_names.json"])
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(True)  
        
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    # add column names row
    elif(funcid == dtm.DISPLAY_ADD_COLUMN_NAMES_ROW) :
        
        display_dataframe_col_names_taskbar()
        print("\n")
        
        df  =   cfg.get_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)) 
        
        if(len(df.columns) > 0) :
            
            opstat  =   opStatus()
            opstat.set_errorMsg("Column Names Are already defined for the df")
            
            
            display_exception(opstat)
            
            col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
            col_names_table.set_table_column_parms({"font":12})
            col_names_table.set_note("None")
            display_column_names(cfg.get_current_chapter_df(cfg.DataTransform_ID),col_names_table,None) 
            
        else :
        
            common_dataframe_heading_html       =   "<div>Add Column Names </div>"
        
            grid_input_form                     =   InputForm(df_add_row_transform_input_id,
                                                              df_add_row_transform_input_idList,
                                                              df_add_row_transform_input_labelList,
                                                              df_add_row_transform_input_typeList,
                                                              df_add_row_transform_input_placeholderList,
                                                              df_add_row_transform_input_jsList,
                                                              df_add_row_transform_input_reqList)
            
            filename    =   cfg.get_notebookPath()

            cfg.set_config_value(df_save_row_transform_input_id+"Parms",[filename + "_" + "column_names.json"])
        
            grid_input_form.set_shortForm(True)
            grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
            grid_input_form.set_gridwidth(480)
            grid_input_form.set_fullparms(True)  
        
            grid_input_html   =   grid_input_form.get_html()
    
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
            gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
    
 
    elif(funcid == dtm.DISPLAY_CHANGE_COLUMN_NAMES) :
        
        display_dataframe_col_names_taskbar()

        print("\n") 
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_table_column_parms({"font":12})
        col_names_table.set_note(" ")
        
        display_column_names(cfg.get_current_chapter_df(cfg.DataTransform_ID),col_names_table,"chcolname")
        

        common_dataframe_heading_html       =   "<div>Change Column Names </div>"
        
        grid_input_form                     =   InputForm(df_change_row_transform_input_id,
                                                          df_change_row_transform_input_idList,
                                                          df_change_row_transform_input_labelList,
                                                          df_change_row_transform_input_typeList,
                                                          df_change_row_transform_input_placeholderList,
                                                          df_change_row_transform_input_jsList,
                                                          df_change_row_transform_input_reqList)
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":50})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(True)  
        
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)


    elif(funcid == dtm.DISPLAY_WHITESPACE_COLUMN_NAMES) :
        
        display_dataframe_col_names_taskbar()

        print("\n") 
        
        common_dataframe_heading_html       =   "<div>Remove Column Names Whitespace</div>"
        
        grid_input_form                     =   InputForm(df_cnames_row_remwhite_input_id,
                                                          df_cnames_row_remwhite_input_idList,
                                                          df_cnames_row_remwhite_input_labelList,
                                                          df_cnames_row_remwhite_input_typeList,
                                                          df_cnames_row_remwhite_input_placeholderList,
                                                          df_cnames_row_remwhite_input_jsList,
                                                          df_cnames_row_remwhite_input_reqList)
        selectDicts         =   []
    
        wschars             =   {"default":"All","list":["All","Horizontal Tab","Linefeed","Formfeed","Cariage Return","Backspace","Vertical Tab"]}
        selectDicts.append(wschars)

        typesflag           =   {"default":"All","list":["Leading and Trailing","Leading Only","Trailing Only","All"]}
        selectDicts.append(typesflag)

        get_select_defaults(grid_input_form,
                            df_cnames_row_remwhite_input_id,
                            df_cnames_row_remwhite_input_idList,
                            df_cnames_row_remwhite_input_typeList,
                            selectDicts)
        
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":50})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(True)  
        
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

        
    elif(funcid == dtm.DISPLAY_SHOW_DF_INDEX) :

        display_dataframe_indices_taskbar()
        display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                 cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID))

    elif(funcid == dtm.DISPLAY_RESET_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        if(not (dtm.is_df_index_defined(cfg.get_current_chapter_df(cfg.DataTransform_ID)))) :
            display_status("No index currently defined for '" + cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID) + "'")
            return()
        
        df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
        
        common_dataframe_heading_html       =   "<div>Reset dataframe Index</div>"
        
        df_index_html                       =   display_current_df_index(df,cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID),0,False)
        
        grid_input_form                     =   InputForm(df_reset_index_transform_input_id,
                                                          df_reset_index_transform_input_idList,
                                                          df_reset_index_transform_input_labelList,
                                                          df_reset_index_transform_input_typeList,
                                                          df_reset_index_transform_input_placeholderList,
                                                          df_reset_index_transform_input_jsList,
                                                          df_reset_index_transform_input_reqList)
        
        selectDicts     =   []
        
        index_levels    =   [" ","All"]
        index_columns   =   df.index.names
        if(len(index_columns) > 0) :
            for i in range(len(index_columns)) :
                if( not (index_columns[i] is None) ) :
                    index_levels.append(index_columns[i])
        cnames          =   {"default" : index_levels[0], "list" : index_levels, "size" : 5, "callback" : "change_reset_index_callback"}
        selectDicts.append(cnames)
        
        dropsel1        =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel1)
           
        get_select_defaults(grid_input_form,
                            df_reset_index_transform_input_id,
                            df_reset_index_transform_input_idList,
                            df_reset_index_transform_input_typeList,
                            selectDicts)

        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
        
        grid_input_html   =   grid_input_form.get_html()
        
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [df_index_html,common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)
        

    elif(funcid == dtm.DISPLAY_SET_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        df_index_html           =   display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                                             cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID),0,False)
        
        set_index_heading_html  =   "<div>Set dataframe Index</div><br>"
        
        cfg.drop_config_value(df_set_index_transform_input_id+"Parms")        
        
        grid_input_form                     =   InputForm(df_set_index_transform_input_id,
                                                          df_set_index_transform_input_idList,
                                                          df_set_index_transform_input_labelList,
                                                          df_set_index_transform_input_typeList,
                                                          df_set_index_transform_input_placeholderList,
                                                          df_set_index_transform_input_jsList,
                                                          df_set_index_transform_input_reqList)
        
        
        selectDicts     =   []
        
        colnames        =   [" "]
        colslist            =   get_collist_without_indices()
        for i in range(len(colslist)) :
            colnames.append(colslist[i])
        cnames              =   {"default" : colnames[0], "list" : colnames, "size" : 5, "callback" : "change_set_index_callback"}
        selectDicts.append(cnames)
        
        dropsel             =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(dropsel)
        
        verifysel           =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(verifysel)
           
        get_select_defaults(grid_input_form,
                            df_set_index_transform_input_id,
                            df_set_index_transform_input_idList,
                            df_set_index_transform_input_typeList,
                            selectDicts)

        grid_input_form.set_fullparms(False)
             
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
        
        grid_input_html   =   grid_input_form.get_html()
        
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [df_index_html,set_index_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()


    elif(funcid == dtm.DISPLAY_APPEND_TO_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        if(not (dtm.is_df_index_defined(cfg.get_current_chapter_df(cfg.DataTransform_ID)))) :
            display_status("No index currently defined for '" + cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID) + "'")
            return()
        
        df_index_html                   =   display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                                                     cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID),0,False)
        common_dataframe_heading_html   =   "<div>Append to dataframe Index </div>"
        
        grid_input_form                 =   InputForm(df_append_index_transform_input_id,
                                                      df_append_index_transform_input_idList,
                                                      df_append_index_transform_input_labelList,
                                                      df_append_index_transform_input_typeList,
                                                      df_append_index_transform_input_placeholderList,
                                                      df_append_index_transform_input_jsList,
                                                      df_append_index_transform_input_reqList)

        selectDicts     =   []
        
        colnames        =   [" "]
        colslist            =   get_collist_without_indices()
        for i in range(len(colslist)) :
            colnames.append(colslist[i])
        cnames              =   {"default" : colnames[0], "list" : colnames, "size" : 5, "callback" : "change_append_index_callback"}
        selectDicts.append(cnames)
        
        dropsel         =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(dropsel)
        
        verifysel           =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(verifysel)

        get_select_defaults(grid_input_form,
                            df_append_index_transform_input_id,
                            df_append_index_transform_input_idList,
                            df_append_index_transform_input_typeList,
                            selectDicts)
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
        
        grid_input_html   =   grid_input_form.get_html()
            
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [df_index_html,common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)

 
    elif(funcid == dtm.DISPLAY_SORT_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        if(not (dtm.is_df_index_defined(cfg.get_current_chapter_df(cfg.DataTransform_ID)))) :
            display_status("No index currently defined for '" + cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID) + "'")
            return()
        
        df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
        
        common_dataframe_heading_html   =   "<div>Sort dataframe Index </div>"
        
        df_index_html                   =   display_current_df_index(df,cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID),0,False)

        grid_input_form                     =   InputForm(df_sort_index_transform_input_id,
                                                          df_sort_index_transform_input_idList,
                                                          df_sort_index_transform_input_labelList,
                                                          df_sort_index_transform_input_typeList,
                                                          df_sort_index_transform_input_placeholderList,
                                                          df_sort_index_transform_input_jsList,
                                                          df_sort_index_transform_input_reqList)
    
        selectDicts     =   []
        
        index_levels    =   [" ","All"]
        index_columns   =   df.index.names
        if(len(index_columns) > 0) :
            for i in range(len(index_columns)) :
                if( not (index_columns[i] is None) ) :
                    index_levels.append(index_columns[i])
        cnames          =   {"default" : index_levels[0], "list" : index_levels, "size" : 5, "callback" : "change_sort_index_callback"}
        selectDicts.append(cnames)

        ascsel          =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(ascsel)
        methodsel       =   {"default":"quicksort","list":["quicksort","mergesort","heapsort"]}
        selectDicts.append(methodsel)
        nasel           =   {"default":"last","list":["first","last"]}
        selectDicts.append(nasel)
          
        get_select_defaults(grid_input_form,
                            df_sort_index_transform_input_id,
                            df_sort_index_transform_input_idList,
                            df_sort_index_transform_input_typeList,
                            selectDicts)
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
        
        grid_input_html   =   grid_input_form.get_html()
            
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [df_index_html,common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)
        

    elif(funcid == dtm.DISPLAY_DROP_DUPLICATE_ROWS) :
        
        common_dataframe_heading_html       =   "<div>Drop Duplicate Rows </div><br>"
        
        grid_input_form                     =   InputForm(df_drop_dups_transform_input_id,
                                                          df_drop_dups_transform_input_idList,
                                                          df_drop_dups_transform_input_labelList,
                                                          df_drop_dups_transform_input_typeList,
                                                          df_drop_dups_transform_input_placeholderList,
                                                          df_drop_dups_transform_input_jsList,
                                                          df_drop_dups_transform_input_reqList)
        
        selectDicts     =   []
        
        current_df      =   cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID)
        colnames        =   current_df.columns.tolist()
        cols_name_list  =   [" "]
        for i in range(len(colnames)) :
            cols_name_list.append(colnames[i])
            
        cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_drop_cols"}
        selectDicts.append(cnames)
        
        subssel         =   {"default":"Keep","list":["Keep","Drop"]}
        selectDicts.append(subssel)
        
        subssel         =   {"default":"first","list":["first","last","False"]}
        selectDicts.append(subssel)
        
        get_select_defaults(grid_input_form,
                            df_drop_dups_transform_input_id,
                            df_drop_dups_transform_input_idList,
                            df_drop_dups_transform_input_typeList,
                            selectDicts)

        display_dataframe_transform_taskbar()
        
        print("\n")
        
        """
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            col_names_table.set_note(get_html_spaces(10)+"<b>*</b> To select columns for duplicate key definition click on the column name in the table above.")
        else :
            col_names_table.set_note(get_html_spaces(3)+"<b>*</b> To select columns for duplicate key definition click on the column<br>" + get_html_spaces(6) + " name in the table above.")
        display_column_names(cfg.get_current_chapter_df(cfg.DataTransform_ID),col_names_table,"dropduplicatescol")
        """
        
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":120, "left-margin":50})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(True)  
    
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-common-df-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-common-df-pop-up-wrapper",gridclasses,gridhtmls)
        
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()
        
    elif(funcid == dtm.DISPLAY_SORT_COLUMN) :
        
        display_dataframe_transform_taskbar()
        
        print("\n")
        
        common_column_heading_html      =   "<div>Sort df by Column</div><br>"
        
        df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
        colslist    =   df.columns.tolist()
        colname     =   colslist[0]
        
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

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
        gridhtmls       =   [common_column_heading_html,colstats_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-3-vert-wrapper",gridclasses,gridhtmls,True)

        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()

    elif(funcid == dtm.DF_TRANSFORM_RETURN) :
                    
        from dfcleanser.data_transform.data_transform_widgets import display_main_option
        from dfcleanser.data_transform.data_transform_control import clear_data_transform_cfg_values
        display_main_option([[0,0]])
        clear_data_transform_cfg_values()

    elif(funcid == dtm.DF_TRANSFORM_HELP) :
        
        from dfcleanser.data_transform.data_transform_widgets import display_main_option
        from dfcleanser.data_transform.data_transform_control import clear_data_transform_cfg_values
        display_main_option([[0,0]])
        clear_data_transform_cfg_values()


def display_remote_df(chapterid)  : 
    
    remote_display_tb_jsList[0]     =   remote_display_tb_jsList[0].replace("XXXX",chapterid)
    
    dfc_remote_display_tb           =   ButtonGroupForm(remote_display_tb_doc_id,
                                                        remote_display_tb_keyTitleList,
                                                        remote_display_tb_jsList,
                                                        remote_display_tb_centered)
    
    dfc_remote_display_tb.set_gridwidth(480)
    dfc_remote_display_tb.set_custombwidth(240)
    
    dfc_remote_display_tb_html      =   dfc_remote_display_tb.get_html()

    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [dfc_remote_display_tb_html]
    
    display_generic_grid("dfcleanser-chapters-tb-wrapper",gridclasses,gridhtmls)

