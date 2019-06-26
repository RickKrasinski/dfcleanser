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

from dfcleanser.common.html_widgets import (get_html_spaces, maketextarea, ButtonGroupForm, InputForm) 

from dfcleanser.common.table_widgets import dcTable

from dfcleanser.common.common_utils import (get_parms_for_input, get_select_defaults, display_generic_grid)

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
                                                 "Drop</br> Index",
                                                 "Sort </br>Index",
                                                 "Drop</br>Duplicate</br> Rows",
                                                 "Return","Help"]

dataframe_transform_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.RESET_ROW_IDS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DROP_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SORT_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DROP_DUPLICATE_ROWS)+")",
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

dataframe_transform_tbA_jsList              =   ["df_transform_task_bar_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.RESET_ROW_IDS)+")"]

dataframe_transform_tbA_centered            =   True

dataframe_transform_tbB_doc_title           =   "DataFrame Transform Options"
dataframe_transform_tbB_title               =   "DataFrame Transform Options"
dataframe_transform_tbB_id                  =   "dftransformoptionstbB"

dataframe_transform_tbB_keyTitleList        =   ["Drop</br>Index",
                                                 "Sort</br>Index",
                                                 "Drop</br>Duplicate</br> Rows",
                                                 "Return","Help"]

dataframe_transform_tbB_jsList              =   ["df_transform_task_bar_callback("+str(dtm.DROP_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SORT_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

dataframe_transform_tbB_centered            =   True


"""
#--------------------------------------------------------------------------
#    dataframe remove column id row inputs
#--------------------------------------------------------------------------
"""
df_save_row_transform_input_title           =   "Save Column Names Row"
df_save_row_transform_input_id              =   "savecidrowtransform"
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
                                                 "df_process_cmd_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+",0)",
                                                 "df_process_cmd_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+",1)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_SAVE_COL_NAME_ID) + ")"]

df_save_row_transform_input_reqList         =   [0]

"""
#--------------------------------------------------------------------------
#    dataframe add column id row inputs
#--------------------------------------------------------------------------
"""
df_add_row_transform_input_title            =   "Add Column Names Row"
df_add_row_transform_input_id               =   "addcidrowtransform"
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
                                                 "df_process_cmd_callback("+str(dtm.ADD_COLUMN_NAMES_ROW)+",0)",
                                                 "df_process_cmd_callback("+str(dtm.ADD_COLUMN_NAMES_ROW)+",1)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_SET_COL_NAME_ID) + ")"]

df_add_row_transform_input_reqList          =   [0,1]


"""
#--------------------------------------------------------------------------
#    dataframe add column id row inputs
#--------------------------------------------------------------------------
"""
df_change_row_transform_input_helpurl       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html"

df_change_row_transform_input_title         =   "Add Column Names Row"
df_change_row_transform_input_id            =   "changecidrowtransform"
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
                                                 "df_process_cmd_callback("+str(dtm.CHANGE_COLUMN_NAMES)+",0)",
                                                 "df_process_cmd_callback("+str(dtm.CHANGE_COLUMN_NAMES)+",1)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_CHANGE_COL_NAMES_ID) + ")"]

df_change_row_transform_input_reqList       =   [0]

"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_new_col_transform_input_title          =   "Set New Index Column"
df_set_new_col_transform_input_id             =   "setnewcoltransform"
df_set_new_col_transform_input_idList         =   ["setnewcolid",
                                                   "setnewdrop",
                                                   "setnewappend",
                                                   "setnewinplace",
                                                   "setnewverify",
                                                   None,None,None]

df_set_new_col_transform_input_labelList      =   ["column_name(s)",
                                                   "drop",
                                                   "append",
                                                   "inplace",
                                                   "verify_integrity",
                                                   "Set</br>Index",
                                                   "Return","Help"]

df_set_new_col_transform_input_typeList       =   ["text","select","select","select","select",
                                                   "button","button","button"]

df_set_new_col_transform_input_placeholderList =  ["select column name(s) to use as df index column ",
                                                   "drop df column ",
                                                   "append to index",
                                                   "change inplace",
                                                   "verify integrity",
                                                   None,None,None]

df_set_new_col_transform_input_jsList         =    [None,None,None,None,None,
                                                    "df_process_cmd_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+",0)",
                                                    "df_process_cmd_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+",1)",
                                                    "display_help_url('" + str(dfchelp.SET_INDEX ) + "')"]

df_set_new_col_transform_input_reqList        =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe reset row ids col inputs
#--------------------------------------------------------------------------
"""
df_reset_col_transform_input_title          =   "Reset Index Column"
df_reset_col_transform_input_id             =   "resetridcoltransform"
df_reset_col_transform_input_idList         =   ["resetlevel",
                                                 "resetdrop",
                                                 "resetinplace",
                                                 "resetcollevel",
                                                 "resetcolfill",
                                                 None,None,None]

df_reset_col_transform_input_labelList      =   ["level",
                                                 "drop",
                                                 "inplace",
                                                 "col_level",
                                                 "col_fill",
                                                 "Reset</br>Index",
                                                 "Return","Help"]

df_reset_col_transform_input_typeList       =   ["text","select","select","text","text",
                                                 "button","button","button"]

df_reset_col_transform_input_placeholderList =  ["int, str, tuple, or list, default None) ",
                                                 "drop from df (default : False)",
                                                 "reset inplace (default : False)",
                                                 "which level the labels are inserted into (default : 0)",
                                                 "determines how the other levels are named",
                                                 None,None,None]

df_reset_col_transform_input_jsList         =    [None,None,None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.RESET_ROW_IDS)+",0)",
                                                  "df_process_cmd_callback("+str(dtm.RESET_ROW_IDS)+",1)",
                                                  "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_reset_col_transform_input_reqList        =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_drop_row_ids_transform_input_title         =   "Drop Row Index Column"
df_drop_row_ids_transform_input_title         =   "Drop Row Index Column"
df_drop_row_ids_transform_input_id            =   "dropridcoltransform"
df_drop_row_ids_transform_input_idList        =   ["dropinplace",
                                                   None,None,None]

df_drop_row_ids_transform_input_labelList     =   ["inplace",
                                                   "Drop</br>Index",
                                                   "Return","Help"]

df_drop_row_ids_transform_input_typeList      =   ["select",
                                                   "button","button","button"]

df_drop_row_ids_transform_input_placeholderList   =  ["drop inplace (default : False)",
                                                      None,None,None]

df_drop_row_ids_transform_input_jsList        =    [None,
                                                    "df_process_cmd_callback("+str(dtm.DROP_ROW_IDS_COL)+",0)",
                                                    "df_process_cmd_callback("+str(dtm.DROP_ROW_IDS_COL)+",1)",
                                                    "display_help_url('" + str(dfchelp.RESET_INDEX) + "')"]

df_drop_row_ids_transform_input_reqList       =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe sort row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_row_ids_transform_input_title          =   "Sort Row Index Column"
df_sort_row_ids_transform_input_id             =   "sortrowidcoltransform"
df_sort_row_ids_transform_input_idList         =   ["dtsortaxis",
                                                    "dtsortlevel",
                                                    "dtsortorder",
                                                    "dtsortinplace",
                                                    "dtsortkind",
                                                    "dtsortnaposition",
                                                    None,None,None]

df_sort_row_ids_transform_input_labelList      =   ["axis",
                                                    "level",
                                                    "ascending",
                                                    "inplace",
                                                    "kind",
                                                    "na_position",
                                                    "Sort</br>Index",
                                                    "Return","Help"]

df_sort_row_ids_transform_input_typeList       =   ["text","text","select","select","select","select",
                                                    "button","button","button"]

df_sort_row_ids_transform_input_placeholderList =  ["index, columns to direct sorting",
                                                    "int or level name or list of ints or list of level names",
                                                    "Order of sort : True - ascending - False - descending (default True )",
                                                    "sort in place (default - False )",
                                                    "sort method quicksort, mergesort, heapsort (default - quicksort )",
                                                    "where to put nas - first : last (default - last )",
                                                    None,None,None]

df_sort_row_ids_transform_input_jsList         =    [None,None,None,None,None,None,
                                                     "df_process_cmd_callback("+str(dtm.SORT_ROWS)+",0)",
                                                     "df_process_cmd_callback("+str(dtm.SORT_ROWS)+",1)",
                                                     "display_help_url('" + str(dfchelp.SORT_INDEX) + "')"]

df_sort_row_ids_transform_input_reqList        =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    dataframe drop duplicate rows inputs
#--------------------------------------------------------------------------
"""
df_drop_dups_transform_input_title          =   "Drop Duplicate Rows"
df_drop_dups_transform_input_id             =   "dropdridcoltransform"
df_drop_dups_transform_input_idList         =   ["dtddrcolumnids",
                                                 "dtddrincexclude",
                                                 "dtddrkeep",
                                                 "dtddrinplace",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["column_names_list",
                                                 "include_column_Ids_list",
                                                 "keep",
                                                 "inplace_dftitle",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(3),"select","select","text",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["enter list of columns to use as keys to identify dups (default blank -  all cols) ",
                                                 "include or exclude column_names_list (default True : include ) ",
                                                 "keep occurence (default : False",
                                                 "df title to return a copy (default - None : inplace)",
                                                 None,None,None]

df_drop_dups_transform_input_jsList         =    [None,None,None,None,
                                                  "df_process_cmd_callback("+str(dtm.DROP_DUPLICATE_ROWS)+",0)",
                                                  "df_process_cmd_callback("+str(dtm.DROP_DUPLICATE_ROWS)+",1)",
                                                  "display_help_url('" + str(dfchelp.DROP_DUPS) + "')"]

df_drop_dups_transform_input_reqList        =   [0]



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

    from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
    display_inspection_data()

def process_dataframe_transform(parms,display=True) :
    from dfcleanser.data_transform.data_transform_dataframe_control import process_df_transform    
    process_df_transform(parms,display=True)
    
def get_save_colnames_row_input_parms(inparms) :
    return(get_parms_for_input(inparms,df_save_row_transform_input_idList))            

def get_add_colnames_row_input_parms(inparms) :
    return(get_parms_for_input(inparms,df_add_row_transform_input_idList))            

def get_reset_colnames_row_input_parms(inparms) :
    return(get_parms_for_input(inparms,df_reset_col_transform_input_idList))            

def get_set_colnames_row_input_parms(inparms) :
    return(get_parms_for_input(inparms,df_set_new_col_transform_input_idList))            

def get_drop_duplicate_rows_input_parms(inparms) :
    return(get_parms_for_input(inparms,df_drop_dups_transform_input_idList))            


def display_common_df_options(header_html,grid_input_form) :
    
    display_dataframe_transform_taskbar()
    
    grid_input_form.set_shortForm(True)
    grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
    grid_input_form.set_gridwidth(440)
    grid_input_form.set_fullparms(True)  
    
    grid_input_html   =   grid_input_form.get_html()
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [header_html,grid_input_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-common-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-common-df-pop-up-wrapper",gridclasses,gridhtmls)

   
"""
#--------------------------------------------------------------------------
#    display dataframe main taskbar widgets
#--------------------------------------------------------------------------
"""
def display_dataframe_options(parms) :

    funcid = parms[0][0]

    if(funcid == dtm.SAVE_COLUMN_NAMES_ROW) :
        
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
    elif(funcid == dtm.ADD_COLUMN_NAMES_ROW) :
        
        common_dataframe_heading_html       =   "<div>Add Column Names </div>"
        
        grid_input_form                     =   InputForm(df_add_row_transform_input_id,
                                                          df_add_row_transform_input_idList,
                                                          df_add_row_transform_input_labelList,
                                                          df_add_row_transform_input_typeList,
                                                          df_add_row_transform_input_placeholderList,
                                                          df_add_row_transform_input_jsList,
                                                          df_add_row_transform_input_reqList)
        
        display_common_df_options(common_dataframe_heading_html,grid_input_form)            
    
 
    elif(funcid == dtm.CHANGE_COLUMN_NAMES) :
        
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
            
        display_common_df_options(common_dataframe_heading_html,grid_input_form)            
        

    elif(funcid == dtm.RESET_ROW_IDS) :
        
        common_dataframe_heading_html       =   "<div>Reset Index Column </div>"
        
        grid_input_form                     =   InputForm(df_reset_col_transform_input_id,
                                                          df_reset_col_transform_input_idList,
                                                          df_reset_col_transform_input_labelList,
                                                          df_reset_col_transform_input_typeList,
                                                          df_reset_col_transform_input_placeholderList,
                                                          df_reset_col_transform_input_jsList,
                                                          df_reset_col_transform_input_reqList)
        
        selectDicts     =   []
        dropsel         =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel)
        inplacesel      =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
        get_select_defaults(grid_input_form,
                            df_reset_col_transform_input_id,
                            df_reset_col_transform_input_idList,
                            df_reset_col_transform_input_typeList,
                            selectDicts)

        #grid_input_form.set_fullparms(False)
            
        display_common_df_options(common_dataframe_heading_html,grid_input_form)            
        

    elif(funcid == dtm.SET_NEW_ROW_IDS_COL) :
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note(get_html_spaces(10)+"<b>*</b> Select a Column to use for Index by clicking on Column Name above.")
        col_names_table.set_refParm(str(30))
            
        col_names_html  =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,"dfsnriccol",False)

    #elif(funcid == dtm.SET_NEW_ROW_IDS_COL_SEL) :

        set_index_heading_html       =   "<div>Set Index Column </div><br>"
        
        cfg.drop_config_value(df_set_new_col_transform_input_id+"Parms")        
        
        grid_input_form                     =   InputForm(df_set_new_col_transform_input_id,
                                                          df_set_new_col_transform_input_idList,
                                                          df_set_new_col_transform_input_labelList,
                                                          df_set_new_col_transform_input_typeList,
                                                          df_set_new_col_transform_input_placeholderList,
                                                          df_set_new_col_transform_input_jsList,
                                                          df_set_new_col_transform_input_reqList)
        
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
                            df_set_new_col_transform_input_id,
                            df_set_new_col_transform_input_idList,
                            df_set_new_col_transform_input_typeList,
                            selectDicts)

        grid_input_form.set_fullparms(False)
             
        display_dataframe_transform_taskbar()
    
        grid_input_form.set_shortForm(True)
        grid_input_form.set_buttonstyle({"font-size":13, "height":50, "width":100, "left-margin":0})
        grid_input_form.set_gridwidth(440)
        grid_input_form.set_fullparms(True)  
    
        grid_input_html   =   grid_input_form.get_html()
    
        gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [col_names_html,set_index_heading_html,grid_input_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-common-df-cols-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-common-df-cols-pop-up-wrapper",gridclasses,gridhtmls)

    elif(funcid == dtm.DROP_ROW_IDS_COL) :
        
        common_dataframe_heading_html       =   "<div>Drop Index Column </div>"
        
        grid_input_form                     =   InputForm(df_drop_row_ids_transform_input_id,
                                                          df_drop_row_ids_transform_input_idList,
                                                          df_drop_row_ids_transform_input_labelList,
                                                          df_drop_row_ids_transform_input_typeList,
                                                          df_drop_row_ids_transform_input_placeholderList,
                                                          df_drop_row_ids_transform_input_jsList,
                                                          df_drop_row_ids_transform_input_reqList)

        selectDicts     =   []
        inplacesel      =   {"default" : "False",
                             "list" : ["True","False"]}
        selectDicts.append(inplacesel)
           
        get_select_defaults(grid_input_form,
                            df_drop_row_ids_transform_input_id,
                            df_drop_row_ids_transform_input_idList,
                            df_drop_row_ids_transform_input_typeList,
                            selectDicts)
            
        display_common_df_options(common_dataframe_heading_html,grid_input_form)            

    elif(funcid == dtm.SORT_ROWS) :
        
        common_dataframe_heading_html       =   "<div>Sort Index Column </div>"
        
        grid_input_form                     =   InputForm(df_sort_row_ids_transform_input_id,
                                                          df_sort_row_ids_transform_input_idList,
                                                          df_sort_row_ids_transform_input_labelList,
                                                          df_sort_row_ids_transform_input_typeList,
                                                          df_sort_row_ids_transform_input_placeholderList,
                                                          df_sort_row_ids_transform_input_jsList,
                                                          df_sort_row_ids_transform_input_reqList)
    
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
                            df_sort_row_ids_transform_input_id,
                            df_sort_row_ids_transform_input_idList,
                            df_sort_row_ids_transform_input_typeList,
                            selectDicts)
        
        display_common_df_options(common_dataframe_heading_html,grid_input_form)            
        

    elif(funcid == dtm.DROP_DUPLICATE_ROWS) :
        
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
        display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,"dtdcrcol")
    
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

    elif(funcid == dtm.DF_TRANSFORM_RETURN) :
                    
        from dfcleanser.data_transform.data_transform_widgets import display_main_option,clear_data_transform_cfg_values
        display_main_option([[0,0]])
        clear_data_transform_cfg_values()

        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data()
 
    elif(funcid == dtm.DF_TRANSFORM_HELP) :
        
        from dfcleanser.data_transform.data_transform_widgets import display_main_option,clear_data_transform_cfg_values
        display_main_option([[0,0]])
        clear_data_transform_cfg_values()

        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data()


