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
                                            get_input_form, get_header_form, maketextarea, ButtonGroupForm, InputForm) 

from dfcleanser.common.table_widgets import dcTable

from dfcleanser.common.common_utils import (get_parms_for_input)

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
                                                 "Reset</br> Index</br>Column",
                                                 "Set </br> Index </br>Column",
                                                 "Drop</br> Index</br> Column",
                                                 "Sort </br>Index</br> Column",
                                                 "Drop</br>Duplicate</br> Rows",
                                                 "Return","Help"]

dataframe_transform_tb_jsList               =   ["df_transform_task_bar_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.ADD_COLUMN_NAMES_ROW)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.CHANGE_COLUMN_NAMES)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.RESET_ROW_IDS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DROP_ROW_IDS_COL)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.SORT_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DROP_DUPLICATE_ROWS)+")",
                                                 "df_transform_task_bar_callback("+str(dtm.DF_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_DF_ID) + ")"]

"""
#--------------------------------------------------------------------------
#    dataframe remove column id row inputs
#--------------------------------------------------------------------------
"""
df_save_row_transform_input_title           =   "Save Column Names Row"
df_save_row_transform_input_id              =   "savecidrowtransform"
df_save_row_transform_input_idList          =   ["filesavename",
                                                 None,None,None,None]

df_save_row_transform_input_labelList       =   ["column_names_file_name",
                                                 "Save Column</br> Names",
                                                 "Set Default</br>File Name",
                                                 "Return","Help"]

df_save_row_transform_input_typeList        =   ["file",
                                                 "button","button","button","button"]

df_save_row_transform_input_placeholderList     = ["enter File name to save column names to or browse to file below (default use default name)",
                                                 None,None,None,None]

df_save_row_transform_input_jsList          =    [None,
                                                 "df_process_cmd_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+",0)",
                                                 "df_process_cmd_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+",1)",
                                                 "df_process_cmd_callback("+str(dtm.SAVE_COLUMN_NAMES_ROW)+",2)",
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
df_change_row_transform_input_id            =   "addcidrowtransform"
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
#    dataframe reset row ids col inputs
#--------------------------------------------------------------------------
"""
df_reset_col_transform_input_title          =   "Reset Index Column"
df_reset_col_transform_input_id             =   "resetridcoltransform"
df_reset_col_transform_input_idList         =   ["startrowid",
                                                 None,None,None]

df_reset_col_transform_input_labelList      =   ["starting_row_Id",
                                                 "Reset</br> Index Column",
                                                 "Return","Help"]

df_reset_col_transform_input_typeList       =   ["text",
                                                 "button","button","button"]

df_reset_col_transform_input_placeholderList =  ["enter starting value to reset row index with (default blank - 0) ",
                                                 None,None,None]

df_reset_col_transform_input_jsList         =    [None,
                                                  "df_process_cmd_callback("+str(dtm.RESET_ROW_IDS)+",0)",
                                                  "df_process_cmd_callback("+str(dtm.RESET_ROW_IDS)+",1)",
                                                  "displayhelp(" + str(dfchelp.TRANSFORM_DF_RESET_ROW_ID_ID) + ")"]

df_reset_col_transform_input_reqList        =   [0]

"""
#--------------------------------------------------------------------------
#    dataframe set row ids col inputs
#--------------------------------------------------------------------------
"""
df_set_new_col_transform_input_title          =   "Set New Index Column"
df_set_new_col_transform_input_id             =   "setnewcoltransform"
df_set_new_col_transform_input_idList         =   ["setnewcolid",
                                                   None,None,None]

df_set_new_col_transform_input_labelList      =   ["column_name",
                                                   "Set Row</br> Index Column",
                                                   "Return","Help"]

df_set_new_col_transform_input_typeList       =   ["text",
                                                   "button","button","button"]

df_set_new_col_transform_input_placeholderList =  ["enter column name to use as row index column ",
                                                   None,None,None]

df_set_new_col_transform_input_jsList         =    [None,
                                                    "df_process_cmd_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+",0)",
                                                    "df_process_cmd_callback("+str(dtm.SET_NEW_ROW_IDS_COL)+",1)",
                                                    "displayhelp(" + str(dfchelp.TRANSFORM_DF_SET_ROW_ID_ID) + ")"]

df_set_new_col_transform_input_reqList        =   [0]

"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_drop_row_ids_transform_input_title          =   "Drop Row Index Column"
df_drop_row_ids_transform_input_id             =   "droprowidcoltransform"
df_drop_row_ids_transform_input_idList         =   ["dtdroprowids",
                                                    None,None,None]

df_drop_row_ids_transform_input_labelList      =   ["row_IDs_file_name",
                                                    "Drop Row</br> Index Column",
                                                    "Return","Help"]

df_drop_row_ids_transform_input_typeList       =   ["file",
                                                    "button","button","button"]

df_drop_row_ids_transform_input_placeholderList =  ["enter File name to save row ids to or browse to file (default blank - don't save)",
                                                    None,None,None]

df_drop_row_ids_transform_input_jsList         =    [None,
                                                     "df_process_cmd_callback("+str(dtm.DROP_ROW_IDS_COL)+",0)",
                                                     "df_process_cmd_callback("+str(dtm.DROP_ROW_IDS_COL)+",1)",
                                                     "displayhelp(" + str(dfchelp.TRANSFORM_DF_DROP_ROW_ID_ID) + ")"]

df_drop_row_ids_transform_input_reqList        =   [0]


"""
#--------------------------------------------------------------------------
#    dataframe drop row ids column inputs
#--------------------------------------------------------------------------
"""
df_sort_row_ids_help_url                       =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html"

df_sort_row_ids_transform_input_title          =   "Sort Row Index Column"
df_sort_row_ids_transform_input_id             =   "sortrowidcoltransform"
df_sort_row_ids_transform_input_idList         =   ["dtsortorder",
                                                    "dtsortinplace",
                                                    "dtsortkind",
                                                    "dtsortnaposition",
                                                    None,None,None]

df_sort_row_ids_transform_input_labelList      =   ["ascending",
                                                    "inplace",
                                                    "kind",
                                                    "na_position",
                                                    "Sort Row</br> Index Column",
                                                    "Return","Help"]

df_sort_row_ids_transform_input_typeList       =   ["text","text","text","text",
                                                    "button","button","button"]

df_sort_row_ids_transform_input_placeholderList =  ["Order of sort : True - ascending - False - descending (default True )",
                                                    "sort in place (default - False )",
                                                    "sort method quicksort, mergesort, heapsort (default - quicksort )",
                                                    "where to put nas - first : last (default - last )",
                                                    None,None,None]

df_sort_row_ids_transform_input_jsList         =    [None,None,None,None,
                                                     "df_process_cmd_callback("+str(dtm.SORT_ROWS)+",0)",
                                                     "df_process_cmd_callback("+str(dtm.DROP_ROW_IDS_COL)+",1)",
                                                     "display_help_url('" + df_sort_row_ids_help_url + "')"]

df_sort_row_ids_transform_input_reqList        =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    dataframe drop duplicate rows inputs
#--------------------------------------------------------------------------
"""
df_drop_dups_transform_input_title          =   "Drop Duplicate Rows"
df_drop_dups_transform_input_id             =   "dropdridcoltransform"
df_drop_dups_transform_input_idList         =   ["dtddrcolumnids",
                                                 "dtddrincexclude",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["column_names_list",
                                                 "include_or_exclude_column_Ids_list_flag",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(3),"text",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["enter list of columns to use as keys to identify dups (default blank -  all cols) ",
                                                 "include or exclude Column Names List (default True : include ) ",
                                                 None,None,None]

df_drop_dups_transform_input_jsList         =    [None,None,
                                                  "df_process_cmd_callback("+str(dtm.DROP_DUPLICATE_ROWS)+",0)",
                                                  "df_process_cmd_callback("+str(dtm.DROP_DUPLICATE_ROWS)+",1)",
                                                  "displayhelp(" + str(dfchelp.TRANSFORM_DF_DROP_DUP_ID) + ")"]

df_drop_dups_transform_input_reqList        =   [0]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_dataframe_transform_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                               dataframe_transform_tb_keyTitleList,
                                                               dataframe_transform_tb_jsList,
                                                               False))])

def display_save_colnames_row_input() :
    display_composite_form([get_input_form(InputForm(df_save_row_transform_input_id,
                                                     df_save_row_transform_input_idList,
                                                     df_save_row_transform_input_labelList,
                                                     df_save_row_transform_input_typeList,
                                                     df_save_row_transform_input_placeholderList,
                                                     df_save_row_transform_input_jsList,
                                                     df_save_row_transform_input_reqList))])

def display_dataframe_transform_main() :

    display_dataframe_transform_taskbar()    
    display_composite_form([get_header_form("&nbsp;&nbsp;&nbsp;Data")])

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

    
"""
#--------------------------------------------------------------------------
#    display dataframe main taskbar widgets
#--------------------------------------------------------------------------
"""
def display_dataframe_options(parms) :

    funcid = parms[0][0]

    if(funcid == dtm.SAVE_COLUMN_NAMES_ROW) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
        
        filename = cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY)
        filename = filename.replace('.','_')
        filename = filename.replace('datasets/','')
        
        print("\n              * Default File Name is " + filename + "_" + "column_names.json")
        
        display_composite_form([get_input_form(InputForm(df_save_row_transform_input_id,
                                                         df_save_row_transform_input_idList,
                                                         df_save_row_transform_input_labelList,
                                                         df_save_row_transform_input_typeList,
                                                         df_save_row_transform_input_placeholderList,
                                                         df_save_row_transform_input_jsList,
                                                         df_save_row_transform_input_reqList))])

    # add column names row
    elif(funcid == dtm.ADD_COLUMN_NAMES_ROW) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])

        display_composite_form([get_input_form(InputForm(df_add_row_transform_input_id,
                                                         df_add_row_transform_input_idList,
                                                         df_add_row_transform_input_labelList,
                                                         df_add_row_transform_input_typeList,
                                                         df_add_row_transform_input_placeholderList,
                                                         df_add_row_transform_input_jsList,
                                                         df_add_row_transform_input_reqList))])
    
    elif(funcid == dtm.CHANGE_COLUMN_NAMES) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
    
        colslist    =   cfg.get_dc_dataframe().columns.tolist()
        cliststr    =   str(colslist)
        cliststr    =   cliststr.replace(","," , ")
        
        cfg.set_config_value(df_change_row_transform_input_id+"Parms",cliststr)
        display_composite_form([get_input_form(InputForm(df_change_row_transform_input_id,
                                                         df_change_row_transform_input_idList,
                                                         df_change_row_transform_input_labelList,
                                                         df_change_row_transform_input_typeList,
                                                         df_change_row_transform_input_placeholderList,
                                                         df_change_row_transform_input_jsList,
                                                         df_change_row_transform_input_reqList))])

    elif(funcid == dtm.RESET_ROW_IDS) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
        
        display_composite_form([get_input_form(InputForm(df_reset_col_transform_input_id,
                                                         df_reset_col_transform_input_idList,
                                                         df_reset_col_transform_input_labelList,
                                                         df_reset_col_transform_input_typeList,
                                                         df_reset_col_transform_input_placeholderList,
                                                         df_reset_col_transform_input_jsList,
                                                         df_reset_col_transform_input_reqList))])

    elif(funcid == dtm.SET_NEW_ROW_IDS_COL) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
        
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note(get_html_spaces(10)+"<b>*</b> Select a Column to use for Row Ids by clicking on Column Name above.")
        col_names_table.set_refParm(str(30))
            
        display_column_names(cfg.get_dc_dataframe(),col_names_table,"dfsnriccol")

    elif(funcid == dtm.SET_NEW_ROW_IDS_COL_SEL) :

        print("SET_NEW_ROW_IDS_COL_SEL",parms)
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
        
        cfg.set_config_value(df_set_new_col_transform_input_id+"Parms",parms[1])        
        display_composite_form([get_input_form(InputForm(df_set_new_col_transform_input_id,
                                                         df_set_new_col_transform_input_idList,
                                                         df_set_new_col_transform_input_labelList,
                                                         df_set_new_col_transform_input_typeList,
                                                         df_set_new_col_transform_input_placeholderList,
                                                         df_set_new_col_transform_input_jsList,
                                                         df_set_new_col_transform_input_reqList))])

    elif(funcid == dtm.DROP_ROW_IDS_COL) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
        
        display_composite_form([get_input_form(InputForm(df_drop_row_ids_transform_input_id,
                                                         df_drop_row_ids_transform_input_idList,
                                                         df_drop_row_ids_transform_input_labelList,
                                                         df_drop_row_ids_transform_input_typeList,
                                                         df_drop_row_ids_transform_input_placeholderList,
                                                         df_drop_row_ids_transform_input_jsList,
                                                         df_drop_row_ids_transform_input_reqList))])

    elif(funcid == dtm.SORT_ROWS) :
        
        print("SORT_ROWS")
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])
    
        #cfg.set_config_value(df_sort_row_ids_transform_input_id+"Parms",["True"])        
        display_composite_form([get_input_form(InputForm(df_sort_row_ids_transform_input_id,
                                                         df_sort_row_ids_transform_input_idList,
                                                         df_sort_row_ids_transform_input_labelList,
                                                         df_sort_row_ids_transform_input_typeList,
                                                         df_sort_row_ids_transform_input_placeholderList,
                                                         df_sort_row_ids_transform_input_jsList,
                                                         df_sort_row_ids_transform_input_reqList))])

    elif(funcid == dtm.DROP_DUPLICATE_ROWS) :
        
        display_composite_form([get_button_tb_form(ButtonGroupForm(dataframe_transform_tb_id,
                                                                   dataframe_transform_tb_keyTitleList,
                                                                   dataframe_transform_tb_jsList,
                                                                   False))])

        print("\n")
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_note(get_html_spaces(10)+"<b>*</b> To select columns for duplicate key definition click on the column name in the table above.")
        display_column_names(cfg.get_dc_dataframe(),col_names_table,"dtdcrcol")
        
        display_composite_form([get_input_form(InputForm(df_drop_dups_transform_input_id,
                                                         df_drop_dups_transform_input_idList,
                                                         df_drop_dups_transform_input_labelList,
                                                         df_drop_dups_transform_input_typeList,
                                                         df_drop_dups_transform_input_placeholderList,
                                                         df_drop_dups_transform_input_jsList,
                                                         df_drop_dups_transform_input_reqList))])

        #from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        #display_inspection_data()


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


