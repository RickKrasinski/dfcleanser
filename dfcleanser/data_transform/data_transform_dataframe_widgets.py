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

from dfcleanser.common.html_widgets import (get_html_spaces, maketextarea, ButtonGroupForm, InputForm, new_line) 

from dfcleanser.common.table_widgets import dcTable

from dfcleanser.common.common_utils import (get_select_defaults, display_generic_grid,
                                            display_exception, opStatus)

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
                                                 "Single Level</br>dataframe</br>Indices",
                                                 "Sort</br>df by</br>Column",
                                                 "Drop</br>Duplicate</br>Rows",
                                                 "Return","Help"]

dataframe_transform_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_COLUMN_NAMES_OPTIONS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_INDICES_OPTIONS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SORT_COLUMN)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

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
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

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
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

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
                                                 "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_SAVE_COL_NAME_ID) + ")"]

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
                                                 "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_SET_COL_NAME_ID) + ")"]

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
                                                 "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_CHANGE_COL_NAMES_ID) + ")"]

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
                                                 "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                 "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

df_cnames_row_remwhite_input_reqList        =   [0,1]


"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_index_transform_input_title            =   "Set New Index Column"
df_set_index_transform_input_id               =   "setnewindextransform"
df_set_index_transform_input_idList           =   ["setnewindex_colid",
                                                   "setnewindex_drop",
                                                   "setnewindex_verify",
                                                   None,None,None]

df_set_index_transform_input_labelList        =   ["index_column_name(s)",
                                                   "drop_index_column_name(s)_cols",
                                                   "verify_integrity",
                                                   "Set</br>Index",
                                                   "Return","Help"]

df_set_index_transform_input_typeList         =   ["selectmultiple","select","select",
                                                   "button","button","button"]

df_set_index_transform_input_placeholderList  =  ["list or single of column name(s) to use as df index",
                                                   "drop df column (default : True)",
                                                   "verify integrity",
                                                   None,None,None]

df_set_index_transform_input_jsList           =    [None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_SET_DF_INDEX) + ")",
                                                    "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                    "display_help_url('" + str(dfchelp.SET_INDEX ) + "')"]

df_set_index_transform_input_reqList          =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe reset row ids col inputs
#--------------------------------------------------------------------------
"""
df_reset_index_transform_input_title        =   "Reset Index Column"
df_reset_index_transform_input_id           =   "resetindextransform"
df_reset_index_transform_input_idList       =   ["resetindex_drop",
                                                 None,None,None]

df_reset_index_transform_input_labelList    =   ["drop",
                                                 "Reset</br>Index",
                                                 "Return","Help"]

df_reset_index_transform_input_typeList     =   ["select",
                                                 "button","button","button"]

df_reset_index_transform_input_placeholderList =  ["drop df column(default : True)",
                                                   None,None,None]

df_reset_index_transform_input_jsList       =    [None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_RESET_DF_INDEX) + ")",
                                                  "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                  "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_reset_index_transform_input_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_append_index_transform_input_title         =   "Append Index Column"
df_append_index_transform_input_id            =   "appendindextransform"
df_append_index_transform_input_idList        =   ["appendindex_colid",
                                                   "appendindex_drop",
                                                   "appendindex_verify",
                                                   None,None,None]

df_append_index_transform_input_labelList     =   ["index_column_name(s)",
                                                   "drop_index_column_name(s)_cols",
                                                   "verify_integrity",
                                                   "Append</br>Index",
                                                   "Return","Help"]

df_append_index_transform_input_typeList      =   ["selectmultiple","select","select",
                                                   "button","button","button"]

df_append_index_transform_input_placeholderList   =  ["list or single name of columns to append to index",
                                                      "drop df column (default : False)",
                                                      "verify integrity",
                                                      None,None,None]

df_append_index_transform_input_jsList        =    [None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_APPEND_TO_INDEX) + ")",
                                                    "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                    "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_append_index_transform_input_reqList       =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe sort row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_index_transform_input_title            =   "Sort Row Index Column"
df_sort_index_transform_input_id               =   "sortindextransform"
df_sort_index_transform_input_idList           =   ["sortindex_order",
                                                    "sortindex_sortkind",
                                                    "sortindex_naposition",
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

df_sort_index_transform_input_jsList           =    [None,None,None,
                                                     "df_process_cmd_callback("+str(dtm.PROCESS_SORT_DF_INDEX) +")",
                                                     "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                     "display_help_url('" + str(dfchelp.SORT_INDEX) + "')"]

df_sort_index_transform_input_reqList          =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    dataframe drop duplicate rows inputs
#--------------------------------------------------------------------------
"""
df_drop_dups_transform_input_title          =   "Drop Duplicate Rows"
df_drop_dups_transform_input_id             =   "dropduplicatetransform"
df_drop_dups_transform_input_idList         =   ["dropduplicate_colids",
                                                 "dropduplicate_cexclude",
                                                 "dropduplicate_keep",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["column_names_list",
                                                 "drop_or_save_column_names_list",
                                                 "keep",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(3),"select","select",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["enter list of columns to use as keys to identify dups (default blank -  all cols) ",
                                                 "drop or save column_names_list (default : drop ) ",
                                                 "keep occurence (default : False",
                                                 None,None,None]

df_drop_dups_transform_input_jsList         =    [None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_DROP_DUPLICATE_ROWS) +")",
                                                  "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) +")",
                                                  "display_help_url('" + str(dfchelp.DROP_DUPS) + "')"]

df_drop_dups_transform_input_reqList        =   [0,1,2]

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
                                              "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                              "display_help_url('" + dfchelp.SORT_COL + "')"]

sort_column_input_reqList               =   [0,1,2]


datatransform_dataframe_inputs          =   [df_save_row_transform_input_id, df_add_row_transform_input_id, df_change_row_transform_input_id,
                                             df_cnames_row_remwhite_input_id, df_set_index_transform_input_id, df_reset_index_transform_input_id,
                                             df_append_index_transform_input_id, df_sort_index_transform_input_id, df_drop_dups_transform_input_id,
                                             sort_column_input_id]


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

def get_current_df_index(df) :
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
        
    #indices = f.getvalue()   
    
    indices = df.index
    index_names = indices.names
    
    if(index_names is None) :
        index_string     =   "No indices defined"
    else :
        
        index_string    =   "["
        
        if((len(index_names) == 1) and (index_names[0] is None)) :
            index_string     =   "No indices defined"
            
        else :
            
            for i in range(len(index_names)) :
            
                if(not (index_names[i] is None)) :
                    
                    index_string    =   index_string + index_names[i]
                    if(i < (len(index_names) - 1)) :
                        index_string    =   index_string + "," 
                        
        index_string    =   index_string + "]"
    
    indices_html        =   "<br>" + new_line
    indices_html        =   (indices_html + "<div style='text-align:left; width:480px; font-size:12px; font-weight:bold; font-family:arial;'>Current Index Columns : </div>")
    indices_html        =   (indices_html + "<div style='text-align:center; width:480px; border: 1px solid #67a1f3; font-size:11px; font-family:arial;'>" + str(index_string) + "</div>")
    indices_html        =   (indices_html + "<br>" + new_line)
    
    from dfcleanser.common.common_utils import DUMP_HTML
    if(DUMP_HTML) :
        print(indices_html)
    
    return(indices_html)

    
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
        df_index_html       =   get_current_df_index(df)
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

def display_current_df_index() :
    
    df_index_html   =   get_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID))
    
    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [df_index_html]
    display_generic_grid("dfc-short-note-wrapper",gridclasses,gridhtmls)
            
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
   
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
            
            filename    =   cfg.get_notebook_path()

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
        display_current_df_index()

    elif(funcid == dtm.DISPLAY_RESET_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        common_dataframe_heading_html       =   "<div>Reset dataframe Index</div>"
        
        df_index_html   =   get_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID))
        
        grid_input_form                     =   InputForm(df_reset_index_transform_input_id,
                                                          df_reset_index_transform_input_idList,
                                                          df_reset_index_transform_input_labelList,
                                                          df_reset_index_transform_input_typeList,
                                                          df_reset_index_transform_input_placeholderList,
                                                          df_reset_index_transform_input_jsList,
                                                          df_reset_index_transform_input_reqList)
        
        selectDicts     =   []
        dropsel         =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel)
           
        get_select_defaults(grid_input_form,
                            df_reset_index_transform_input_id,
                            df_reset_index_transform_input_idList,
                            df_reset_index_transform_input_typeList,
                            selectDicts)

        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
        
        grid_input_form.dump()
        
        grid_input_html   =   grid_input_form.get_html()
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html,df_index_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)
        

    elif(funcid == dtm.DISPLAY_SET_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        df_index_html           =   get_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID))
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
        
        colslist            =   get_collist_without_indices()
        cnames              =   {"default" : colslist[0], "list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
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
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
        gridhtmls       =   [set_index_heading_html,grid_input_html,df_index_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()


    elif(funcid == dtm.DISPLAY_APPEND_TO_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        df_index_html                   =   get_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID))
        common_dataframe_heading_html   =   "<div>Append to dataframe Index </div>"
        
        grid_input_form                     =   InputForm(df_append_index_transform_input_id,
                                                          df_append_index_transform_input_idList,
                                                          df_append_index_transform_input_labelList,
                                                          df_append_index_transform_input_typeList,
                                                          df_append_index_transform_input_placeholderList,
                                                          df_append_index_transform_input_jsList,
                                                          df_append_index_transform_input_reqList)

        selectDicts     =   []
        
        colslist            =   get_collist_without_indices()
        cnames              =   {"default" : colslist[0], "list" : colslist, "size" : 5, "callback" : "change_col_stats_callback"}
        selectDicts.append(cnames)

        dropsel         =   {"default" : "False","list" : ["True","False"]}
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
            
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html,df_index_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls,True)

 
    elif(funcid == dtm.DISPLAY_SORT_DF_INDEX) :
        
        display_dataframe_indices_taskbar()
        print("\n")
        
        common_dataframe_heading_html       =   "<div>Sort dataframe Index </div>"
        df_index_html   =   get_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID))
        
        grid_input_form                     =   InputForm(df_sort_index_transform_input_id,
                                                          df_sort_index_transform_input_idList,
                                                          df_sort_index_transform_input_labelList,
                                                          df_sort_index_transform_input_typeList,
                                                          df_sort_index_transform_input_placeholderList,
                                                          df_sort_index_transform_input_jsList,
                                                          df_sort_index_transform_input_reqList)
    
        selectDicts     =   []

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
            
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html,df_index_html]
    
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
        dropsel         =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(dropsel)
        keepsel         =   {"default" : "False", "list" : ["first","last","False"]}
        selectDicts.append(keepsel)
        inplacesel      =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(inplacesel)
        
        get_select_defaults(grid_input_form,
                            df_drop_dups_transform_input_id,
                            df_drop_dups_transform_input_idList,
                            df_drop_dups_transform_input_typeList,
                            selectDicts)

        display_dataframe_transform_taskbar()
        
        print("\n")
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            col_names_table.set_note(get_html_spaces(10)+"<b>*</b> To select columns for duplicate key definition click on the column name in the table above.")
        else :
            col_names_table.set_note(get_html_spaces(3)+"<b>*</b> To select columns for duplicate key definition click on the column<br>" + get_html_spaces(6) + " name in the table above.")
        display_column_names(cfg.get_current_chapter_df(cfg.DataTransform_ID),col_names_table,"dropduplicatescol")
    
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



