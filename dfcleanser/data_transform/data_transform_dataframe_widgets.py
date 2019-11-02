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

from dfcleanser.common.html_widgets import (get_html_spaces, maketextarea, ButtonGroupForm, InputForm, new_line) 

from dfcleanser.common.table_widgets import dcTable

from dfcleanser.common.common_utils import (get_select_defaults, display_generic_grid)

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

dataframe_transform_tb_keyTitleList         =   ["Save </br>Column</br> Names",
                                                 "Add </br>Column</br> Names",
                                                 "Change</br>Column </br>Names",
                                                 "Set </br> Index",
                                                 "Reset</br> Index",
                                                 "Append</br>Index",
                                                 "Sort </br>Index",
                                                 "Drop</br>Duplicate</br> Rows",
                                                 "Return","Help"]

dataframe_transform_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SET_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_RESET_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_APPEND_TO_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SORT_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

dataframe_transform_tb_centered             =   True


dataframe_transform_tbA_doc_title           =   "DataFrame Transform Options"
dataframe_transform_tbA_title               =   "DataFrame Transform Options"
dataframe_transform_tbA_id                  =   "dftransformoptionstbA"

dataframe_transform_tbA_keyTitleList        =   ["Save </br>Column</br> Names",
                                                 "Add </br>Column</br> Names",
                                                 "Change</br>Column </br>Names",
                                                 "Set </br>Index",
                                                 "Reset</br>Index"]

dataframe_transform_tbA_jsList              =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SET_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_RESET_DF_INDEX)+")"]

dataframe_transform_tbA_centered            =   True

dataframe_transform_tbB_doc_title           =   "DataFrame Transform Options"
dataframe_transform_tbB_title               =   "DataFrame Transform Options"
dataframe_transform_tbB_id                  =   "dftransformoptionstbB"

dataframe_transform_tbB_keyTitleList        =   ["Append</br>Index",
                                                 "Sort</br>Index",
                                                 "Drop</br>Duplicate</br> Rows",
                                                 "Return","Help"]

dataframe_transform_tbB_jsList              =   ["df_transform_task_bar_callback("+str(dtm.DISPLAY_APPEND_TO_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_SORT_DF_INDEX)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DISPLAY_DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

dataframe_transform_tbB_centered            =   True


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
df_add_row_transform_input_idList           =   ["filereadname","dfcolsidlist",
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
df_change_row_transform_input_idList        =   ["dfcolsidlist",
                                                 None,None,None]

df_change_row_transform_input_labelList     =   ["column_names_list",
                                                 "Change Column </br>Names ",
                                                 "Return","Help"]

df_change_row_transform_input_typeList      =   [maketextarea(10),
                                                 "button","button","button"]

df_change_row_transform_input_placeholderList  =   ["modify the current Column Names",
                                                    None,None,None]

df_change_row_transform_input_jsList        =   [None,
                                                 "df_process_cmd_callback("+str(dtm.PROCESS_CHANGE_COLUMN_NAMES) + ")",
                                                 "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_CHANGE_COL_NAMES_ID) + ")"]

df_change_row_transform_input_reqList       =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_index_transform_input_title            =   "Set New Index Column"
df_set_index_transform_input_id               =   "setnewindextransform"
df_set_index_transform_input_idList           =   ["newindex_colid",
                                                   "setnewindex_drop",
                                                   "setnewindex_inplace",
                                                   "setnewindex_resultdf",
                                                   "setnewindex_verify",
                                                   None,None,None]

df_set_index_transform_input_labelList        =   ["column_name(s)",
                                                   "drop",
                                                   "inplace",
                                                   "result_df_title",
                                                   "verify_integrity",
                                                   "Set</br>Index",
                                                   "Return","Help"]

df_set_index_transform_input_typeList         =   ["text","select","select","text","select",
                                                   "button","button","button"]

df_set_index_transform_input_placeholderList  =  ["list or single of column name(s) to use as df index",
                                                   "drop df column (default : False)",
                                                   "set index inplace (default True)",
                                                   "result df title (ignored if inplace = True)",
                                                   "verify integrity",
                                                   None,None,None]

df_set_index_transform_input_jsList           =    [None,None,None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_SET_DF_INDEX) + ")",
                                                    "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                    "display_help_url('" + str(dfchelp.SET_INDEX ) + "')"]

df_set_index_transform_input_reqList          =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    dataframe reset row ids col inputs
#--------------------------------------------------------------------------
"""
df_reset_index_transform_input_title        =   "Reset Index Column"
df_reset_index_transform_input_id           =   "resetindextransform"
df_reset_index_transform_input_idList       =   ["resetindex_drop",
                                                 "resetindex_inplace",
                                                 "resetindex_resultdf",
                                                 None,None,None]

df_reset_index_transform_input_labelList    =   ["drop",
                                                 "inplace",
                                                 "result_df_title",
                                                 "Reset</br>Index",
                                                 "Return","Help"]

df_reset_index_transform_input_typeList     =   ["select","select","text",
                                                 "button","button","button"]

df_reset_index_transform_input_placeholderList =  ["drop df column(default : True)",
                                                   "reset inplace (default : False)",
                                                   "result df title (ignored if inplace = True)",
                                                   None,None,None]

df_reset_index_transform_input_jsList       =    [None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_RESET_DF_INDEX) + ")",
                                                  "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                  "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_reset_index_transform_input_reqList      =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_append_index_transform_input_title         =   "Append Index Column"
df_append_index_transform_input_id            =   "appendindextransform"
df_append_index_transform_input_idList        =   ["appendindex_colid",
                                                   "appendindex_drop",
                                                   "appendindex_inplace",
                                                   "appendindex_resultdf",
                                                   None,None,None]

df_append_index_transform_input_labelList     =   ["colnames",
                                                   "drop",
                                                   "inplace",
                                                   "result_df_title",
                                                   "Drop</br>Index",
                                                   "Return","Help"]

df_append_index_transform_input_typeList      =   ["text","select","select","text",
                                                   "button","button","button"]

df_append_index_transform_input_placeholderList   =  ["list or single name of columns to append to index",
                                                      "drop df column (default : False)",
                                                      "append inplace (default : True)",
                                                      "result df title (ignored if inplace = True)",
                                                      None,None,None]

df_append_index_transform_input_jsList        =    [None,None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.PROCESS_APPEND_TO_INDEX) + ")",
                                                    "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                    "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_append_index_transform_input_reqList       =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    dataframe sort row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_index_transform_input_title            =   "Sort Row Index Column"
df_sort_index_transform_input_id               =   "sortindextransform"
df_sort_index_transform_input_idList           =   ["sortindex_axis",
                                                    "sortindex_order",
                                                    "sortindex_inplace",
                                                    "sortindex_resultdf",
                                                    "sortindex_sortkind",
                                                    "sortindex_naposition",
                                                    None,None,None]

df_sort_index_transform_input_labelList        =   ["axis",
                                                    "ascending",
                                                    "inplace",
                                                    "result_df_title",
                                                    "kind",
                                                    "na_position",
                                                    "Sort</br>Index",
                                                    "Return","Help"]

df_sort_index_transform_input_typeList         =   ["text","select","select","text","select","select",
                                                    "button","button","button"]

df_sort_index_transform_input_placeholderList  =   ["index, columns to direct sorting",
                                                    "Order of sort : True - ascending - False - descending (default True )",
                                                    "sort inplace (default : True)",
                                                    "result df title (ignored if inplace = True)",
                                                    "sort method quicksort, mergesort, heapsort (default - quicksort )",
                                                    "where to put nas - first : last (default - last )",
                                                    None,None,None]

df_sort_index_transform_input_jsList           =    [None,None,None,None,None,None,
                                                     "df_process_cmd_callback("+str(dtm.PROCESS_SORT_DF_INDEX) +")",
                                                     "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) + ")",
                                                     "display_help_url('" + str(dfchelp.SORT_INDEX) + "')"]

df_sort_index_transform_input_reqList          =   [0,1,2,3,4]


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
                                                 "dropduplicate_inplace",
                                                 "dropduplicate_resultdf",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["column_names_list",
                                                 "drop_or_save_columns_in_column_names_list",
                                                 "keep",
                                                 "inplace",
                                                 "result_df_title",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(3),"select","select","select","text",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["enter list of columns to use as keys to identify dups (default blank -  all cols) ",
                                                 "drop or save column_names_list (default : drop ) ",
                                                 "keep occurence (default : False",
                                                 "drop dups inplace (default : True)",
                                                 "result df title (ignored if inplace = True)",
                                                 None,None,None]

df_drop_dups_transform_input_jsList         =    [None,None,None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.PROCESS_DROP_DUPLICATE_ROWS) +")",
                                                  "df_process_cmd_callback("+str(dtm.DF_TRANSFORM_RETURN) +")",
                                                  "display_help_url('" + str(dfchelp.DROP_DUPS) + "')"]

df_drop_dups_transform_input_reqList        =   [0,1,2,3,4]


datatransform_df_inputs     =   [df_save_row_transform_input_id,df_add_row_transform_input_id,df_change_row_transform_input_id,
                                 df_set_index_transform_input_id,df_reset_index_transform_input_id,df_append_index_transform_input_id,
                                 df_sort_index_transform_input_id,df_drop_dups_transform_input_id]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_dataframe_transform_taskbar() :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :

        from dfcleanser.common.display_utils import display_dfcleanser_taskbar
        display_dfcleanser_taskbar(ButtonGroupForm(dataframe_transform_tb_id,
                                                   dataframe_transform_tb_keyTitleList,
                                                   dataframe_transform_tb_jsList,
                                                   dataframe_transform_tb_centered))
    else :
        
        transform_tb_A     =   ButtonGroupForm(dataframe_transform_tbA_id,
                                               dataframe_transform_tbA_keyTitleList,
                                               dataframe_transform_tbA_jsList,
                                               dataframe_transform_tbA_centered)
        
        transform_tb_A.set_gridwidth(480)
        transform_tb_A_html    =   transform_tb_A.get_html()
        
        transform_tb_B     =   ButtonGroupForm(dataframe_transform_tbB_id,
                                               dataframe_transform_tbB_keyTitleList,
                                               dataframe_transform_tbB_jsList,
                                               dataframe_transform_tbB_centered)
        
        transform_tb_B.set_gridwidth(480)
        transform_tb_B_html    =   transform_tb_B.get_html()
        
        gridclasses     =   ["dfc-top-","dfc-footer"]
        gridhtmls       =   [transform_tb_A_html,transform_tb_B_html]
    
        display_generic_grid("dfcleanser-system-tb-pop-up-wrapper",gridclasses,gridhtmls)


def display_dataframe_transform_main() :

    display_dataframe_transform_taskbar()    

def process_dataframe_transform(parms,display=True) :
    from dfcleanser.data_transform.data_transform_dataframe_control import process_df_transform    
    process_df_transform(parms,display=True)

def get_current_df_index(df) :
    
    #from contextlib import redirect_stdout
    #import io
    
    #f = io.StringIO()
    #with redirect_stdout(f):
    #    print(df.index)
        
    #indices = f.getvalue()   
    indices = df.index.name
    if(indices is None) :
        indices     =   "No indices defined"
    
    indices_html        =   "<br>" + new_line
    indices_html        =   (indices_html + "<div style='text-align:left; width:480px; font-size:12px; font-weight:bold; font-family:arial;'>Current Indices : </div>")
    indices_html        =   (indices_html + "<div style='text-align:center; width:480px; border: 1px solid #67a1f3; font-size:11px; font-family:arial;'>" + indices + "</div>")
    indices_html        =   (indices_html + "<br>" + new_line)
    
    return(indices_html)

    
def display_common_df_options(df,header_html,grid_input_form) :
    
    display_dataframe_transform_taskbar()
    
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
    grid_input_form.set_gridwidth(440)
    grid_input_form.set_fullparms(True)  
    
    grid_input_html     =   grid_input_form.get_html()
    
    df_index_html       =   get_current_df_index(df)
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
    gridhtmls       =   [header_html,grid_input_html,df_index_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-common-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-common-df-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
   
   
"""
#--------------------------------------------------------------------------
#    display dataframe main taskbar widgets
#--------------------------------------------------------------------------
"""
def display_dataframe_options(funcid) :

    #funcid = parms[0][0]

    if(funcid == dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW) :
        
        display_dataframe_transform_taskbar()
        
        common_dataframe_heading_html       =   "<div>Save Column Names </div><br>"
        
        filename = cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
        filename = filename.replace('.','_')
        filename = filename.replace('datasets/','')

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
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [common_dataframe_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-save-col-names-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-save-col-names-pop-up-wrapper",gridclasses,gridhtmls)

    # add column names row
    elif(funcid == dtm.DISPLAY_ADD_COLUMN_NAMES_ROW) :
        
        common_dataframe_heading_html       =   "<div>Add Column Names </div>"
        
        grid_input_form                     =   InputForm(df_add_row_transform_input_id,
                                                          df_add_row_transform_input_idList,
                                                          df_add_row_transform_input_labelList,
                                                          df_add_row_transform_input_typeList,
                                                          df_add_row_transform_input_placeholderList,
                                                          df_add_row_transform_input_jsList,
                                                          df_add_row_transform_input_reqList)
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        display_common_df_options(df,common_dataframe_heading_html,grid_input_form)            
    
 
    elif(funcid == dtm.DISPLAY_CHANGE_COLUMN_NAMES) :
        
        colslist    =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist()
        import json
        cliststr    =   json.dumps(colslist)#str(colslist)
        cfg.set_config_value(df_change_row_transform_input_id+"Parms",[cliststr])
        
        common_dataframe_heading_html       =   "<div>Change Column Names </div>"
        
        grid_input_form                     =   InputForm(df_change_row_transform_input_id,
                                                          df_change_row_transform_input_idList,
                                                          df_change_row_transform_input_labelList,
                                                          df_change_row_transform_input_typeList,
                                                          df_change_row_transform_input_placeholderList,
                                                          df_change_row_transform_input_jsList,
                                                          df_change_row_transform_input_reqList)
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        display_common_df_options(df,common_dataframe_heading_html,grid_input_form)            
        

    elif(funcid == dtm.DISPLAY_RESET_DF_INDEX) :
        
        common_dataframe_heading_html       =   "<div>Reset dataframe Index</div>"
        
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
        inplacesel      =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
        get_select_defaults(grid_input_form,
                            df_reset_index_transform_input_id,
                            df_reset_index_transform_input_idList,
                            df_reset_index_transform_input_typeList,
                            selectDicts)

        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        display_common_df_options(df,common_dataframe_heading_html,grid_input_form)            
        

    elif(funcid == dtm.DISPLAY_SET_DF_INDEX) :
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note(get_html_spaces(10)+"<b>*</b> Select a Column to use for Index by clicking on Column Name above.")
        col_names_table.set_refParm(str(30))
            
        col_names_html          =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,"setindexcol",False)
        df_index_html           =   get_current_df_index(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))
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
        dropsel         =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel)
        appendsel       =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(appendsel)
        inplacesel      =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(inplacesel)
        verifysel       =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(verifysel)
           
        get_select_defaults(grid_input_form,
                            df_set_index_transform_input_id,
                            df_set_index_transform_input_idList,
                            df_set_index_transform_input_typeList,
                            selectDicts)

        grid_input_form.set_fullparms(False)
             
        display_dataframe_transform_taskbar()
        print("\n")
    
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(480)
        grid_input_form.set_fullparms(False)  
    
        grid_input_html   =   grid_input_form.get_html()
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            colsclasses     =   ["dfc-top"]
            colshtmls       =   [col_names_html]
            display_generic_grid("df-column-names-wrapper",colsclasses,colshtmls)
            
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
            gridhtmls       =   [set_index_heading_html,grid_input_html,df_index_html]
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            
            gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main","dfc-footer"]
            gridhtmls       =   [col_names_html,set_index_heading_html,grid_input_html,df_index_html]
            display_generic_grid("df-index-common-pop-up-wrapper",gridclasses,gridhtmls)
            
        from dfcleanser.common.display_utils import display_pop_up_buffer
        display_pop_up_buffer()

    elif(funcid == dtm.DISPLAY_APPEND_TO_INDEX) :
        
        display_dataframe_transform_taskbar()
        print("\n")
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note(get_html_spaces(10)+"<b>*</b> Select a Column to use for Index by clicking on Column Name above.")
        col_names_table.set_refParm(str(30))
            
        col_names_html                  =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,"appendindexcol",False)
        df_index_html                   =   get_current_df_index(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))
        common_dataframe_heading_html   =   "<div>Append to dataframe Index </div>"
        
        grid_input_form                     =   InputForm(df_append_index_transform_input_id,
                                                          df_append_index_transform_input_idList,
                                                          df_append_index_transform_input_labelList,
                                                          df_append_index_transform_input_typeList,
                                                          df_append_index_transform_input_placeholderList,
                                                          df_append_index_transform_input_jsList,
                                                          df_append_index_transform_input_reqList)

        selectDicts     =   []
        dropsel         =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel)

        inplacesel      =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
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
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            colsclasses     =   ["dfc-top"]
            colshtmls       =   [col_names_html]
            display_generic_grid("df-column-names-wrapper",colsclasses,colshtmls)
            
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
            gridhtmls       =   [common_dataframe_heading_html,grid_input_html,df_index_html]
            display_generic_grid("df-index-common-wrapper",gridclasses,gridhtmls)
            
        else :
            
            gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-main","dfc-footer"]
            gridhtmls       =   [col_names_html,common_dataframe_heading_html,grid_input_html,df_index_html]
            display_generic_grid("df-index-common-pop-up-wrapper",gridclasses,gridhtmls)

        
        #df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            
        #display_common_df_options(df,common_dataframe_heading_html,grid_input_form)            

    elif(funcid == dtm.DISPLAY_SORT_DF_INDEX) :
        
        common_dataframe_heading_html       =   "<div>Sort Index Column </div>"
        
        grid_input_form                     =   InputForm(df_sort_index_transform_input_id,
                                                          df_sort_index_transform_input_idList,
                                                          df_sort_index_transform_input_labelList,
                                                          df_sort_index_transform_input_typeList,
                                                          df_sort_index_transform_input_placeholderList,
                                                          df_sort_index_transform_input_jsList,
                                                          df_sort_index_transform_input_reqList)
    
        selectDicts     =   []
        sortsel         =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(sortsel)
        sortsel         =   {"default" : "False", "list" : ["True","False"]}
        selectDicts.append(sortsel)
        sortsel         =   {"default":"quicksort","list":["quicksort","mergesort","heapsort"]}
        selectDicts.append(sortsel)
        sortsel         =   {"default":"last","list":["first","last"]}
        selectDicts.append(sortsel)
          
        get_select_defaults(grid_input_form,
                            df_sort_index_transform_input_id,
                            df_sort_index_transform_input_idList,
                            df_sort_index_transform_input_typeList,
                            selectDicts)
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)

        display_common_df_options(df,common_dataframe_heading_html,grid_input_form)            
        

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
        display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,"dropduplicatescol")
    
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
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



