"""
# sw_utility_census_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue June 6 22:00:00 2019

@author: Rick
"""


import sys
import os

this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp

import dfcleanser.sw_utilities.sw_utility_census_model as swcm

from dfcleanser.common.html_widgets import (ButtonGroupForm, maketextarea)

from dfcleanser.common.common_utils import (display_generic_grid, get_select_defaults, display_notes,
                                            does_dir_exist, does_file_exist)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dfc census data widh=gets
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dfcensus main task bar
#--------------------------------------------------------------------------
"""
census_tb_doc_title               =   "Census"
census_tb_title                   =   "Census"
census_tb_id                      =   "census"

census_tb_keyTitleList            =   ["Download</br>Census</br>Datasets",
                                       "Setup</br>Census</br>Datasets",
                                       "Load</br>Census</br>Datasets</br>To Memory",
                                       "Insert</br>Census</br>Datasets</br>To User df(s)",
                                       "Export</br>Census</br>df(s)",
                                       "Load</br>Census</br>Datasets</br>to db(s)",
                                       "Clear","Reset","Help"]

census_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_CENSUS_DATASETS_FOR_INSERT)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_EXPORT_CENSUS_DFS)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_DATA_TO_DB)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                       "process_pop_up_cmd(6)",
                                       "displayhelp('" + str(dfchelp.DF_CENSUS_MAIN_TASKBAR_ID) + "')"]

census_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dfcensus download datasets task bars
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dfcensus confirm data download none task bar
#--------------------------------------------------------------------------
"""
data_confirm_download_none_tb_doc_title               =   "Census Confirm Data Download None"
data_confirm_download_none_tb_title                   =   "Census Confirm Data Download None"
data_confirm_download_none_tb_id                      =   "censusconfirmdatadownloadnone"

data_confirm_download_none_tb_keyTitleList            =   ["Return"]

data_confirm_download_none_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")"]

data_confirm_download_none_tb_centered                =   True
 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dfcensus drop/connfigure datasets task bars
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dfcensus configure task bar
#--------------------------------------------------------------------------
"""
data_configure_tb_doc_title               =   "Census Data Configure"
data_configure_tb_title                   =   "Census Data Configure"
data_configure_tb_id                      =   "censusdataconfigure"

data_configure_tb_keyTitleList            =   ["Add/Drop</br>Selected</br>Subsets",
                                               "Clear","Return","Help"]

data_configure_tb_jsList                  =   ["get_census_callback("+str(swcm.PROCESS_CONFIGURE_CENSUS_DATA)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                               "displayhelp('" + str(dfchelp.DF_CENSUS_CONFIGURE_ID) + "')"]

data_configure_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure no datasets task bar
#--------------------------------------------------------------------------
"""
data_configure_no_datasets_tb_title                   =   "Census Data Configure None"
data_configure_no_datasets_tb_title                   =   "Census Data Configure None"
data_configure_no_datasets_tb_id                      =   "censusdataconfigurenone"

data_configure_no_datasets_tb_keyTitleList            =   ["Add</br>Subsets",
                                                           "Return","Help"]

data_configure_no_datasets_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp('" + str(dfchelp.DF_CENSUS_CONFIGURE_NO_CHANGE_ID) + "')"]

data_configure_no_datasets_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure verification task bar
#--------------------------------------------------------------------------
"""
data_configure_verify_tb_doc_title               =   "Census Data Verify"
data_configure_verify_tb_title                   =   "Census Data Verify"
data_configure_verify_tb_id                      =   "censusdataverify"

data_configure_verify_tb_keyTitleList            =   ["Add/Drop</br>Selected</br>Datasets",
                                                      "Return","Help"]

data_configure_verify_tb_jsList                  =   ["get_census_callback("+str(swcm.DROP_CENSUS_DATA)+")",
                                                      "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                      "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_configure_verify_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus process data load complete task bar
#--------------------------------------------------------------------------
"""
data_process_load_complete_tb_doc_title               =   "Census Confirm Data Load"
data_process_load_complete_tb_title                   =   "Census Confirm Data Load"
data_process_load_complete_tb_id                      =   "censusconfirmdataload"

data_process_load_complete_tb_keyTitleList            =   ["Get</br>Subset Data",
                                                           "Return"]

data_process_load_complete_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")"]

data_process_load_complete_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus load datasets to df task bar
#--------------------------------------------------------------------------
"""
data_load_datasets_to_df_tb_doc_title                 =   "Census Confirm Data Load"
data_load_datasets_to_df_tb_title                     =   "Census Confirm Data Load"
data_load_datasets_to_df_tb_id                        =   "censusdfload"

data_load_datasets_to_df_tb_keyTitleList              =   ["Load/Unload</br>Census</br>Data to Memory",
                                                           "Clear","Return","Help"]

data_load_datasets_to_df_tb_jsList                    =   ["get_census_callback("+str(swcm.VERIFY_LOAD_CENSUS_TO_DFC_DFS)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_TO_DF_ID) + "')"]

data_load_datasets_to_df_tb_centered                  =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure no datasets task bar
#--------------------------------------------------------------------------
"""
load_datasets_to_df_no_datasets_tb_title              =   "Census Data Load None"
load_datasets_to_df_no_datasets_tb_title              =   "Census Data Load None"
load_datasets_to_df_no_datasets_tb_id                 =   "censusdataloaddfnone"

load_datasets_to_df_no_datasets_tb_keyTitleList       =   ["Insert Census</br>Datasets</br>To User df(s)",
                                                           "Return","Help"]

load_datasets_to_df_no_datasets_tb_jsList             =   ["get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_TO_DF_ID) + "')"]

load_datasets_to_df_no_datasets_tb_centered           =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure verification task bar
#--------------------------------------------------------------------------
"""
load_datasets_to_df_verify_tb_doc_title               =   "Census Data Verify"
load_datasets_to_df_verify_tb_title                   =   "Census Data Verify"
load_datasets_to_df_verify_tb_id                      =   "censusdataverify"

load_datasets_to_df_verify_tb_keyTitleList            =   ["Load/Unload</br>Datasets</br>to Memory",
                                                           "Return","Help"]

load_datasets_to_df_verify_tb_jsList                  =   ["get_census_callback("+str(swcm.PROCESS_LOAD_TO_DFC_DFS)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_TO_DF_SELECT_ID) + "')"]

load_datasets_to_df_verify_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus load datasets to db task bar
#--------------------------------------------------------------------------
"""
data_load_datasets_none_tb_doc_title                 =   "Census Confirm Data Load"
data_load_datasets_none_tb_title                     =   "Census Confirm Data Load"
data_load_datasets_none_tb_id                        =   "censusdfload"

data_load_datasets_none_tb_keyTitleList              =   ["Download</br>Datasets",
                                                          "Return","Help"]

data_load_datasets_none_tb_jsList                    =   ["get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                                          "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                          "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_load_datasets_none_tb_centered                  =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get columns select subdata tb
#--------------------------------------------------------------------------
"""
get_dataset_columns_tb_doc_title                    =   "Census Confirm Data Load"
get_dataset_columns_tb_title                        =   "Census Confirm Data Load"
get_dataset_columns_tb_id                           =   "censusdfload"

get_dataset_columns_tb_keyTitleList                 =   ["Select Census</br>Columns To Insert</br>Into User df(s)","Return","Help"]

get_dataset_columns_tb_jsList                       =   ["get_census_callback("+str(swcm.SHOW_SELECTED_COLUMNS)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_COL_TO_DF_SELECT_ID) + "')"]

get_dataset_columns_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get columns select subdata tb
#--------------------------------------------------------------------------
"""
get_dataset_columns_no_df_tb_doc_title              =   "Census Confirm Data Load"
get_dataset_columns_no_df_tb_title                  =   "Census Confirm Data Load"
get_dataset_columns_no_df_tb_id                     =   "censusdfload"

get_dataset_columns_no_df_tb_keyTitleList           =   ["Load</br>Census</br>Data to Memory",
                                                         "Return","Help"]

get_dataset_columns_no_df_tb_jsList                 =   ["get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_DATA)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_COL_TO_DF_SELECT_ID) + "')"]

get_dataset_columns_no_df_tb_centered               =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get subdata list tb
#--------------------------------------------------------------------------
"""
get_subdata_columns_tb_doc_title                    =   "Census Confirm Data Load"
get_subdata_columns_tb_title                        =   "Census Confirm Data Load"
get_subdata_columns_tb_id                           =   "censusdfload"

get_subdata_columns_tb_keyTitleList                 =   ["Change</br>Dataset","Show</br>Selected</br>Columns","Return","Help"]

get_subdata_columns_tb_jsList                       =   ["get_census_callback("+str(swcm.DISPLAY_CENSUS_DATASETS_FOR_INSERT)+")",
                                                         "get_census_callback("+str(swcm.SHOW_SELECTED_COLUMNS)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_COL_TO_DF_COLS_ID) + "')"]

get_subdata_columns_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get col names list tb
#--------------------------------------------------------------------------
"""
get_col_names_list_tb_doc_title                    =   "Census Confirm Data Load"
get_col_names_list_tb_title                        =   "Census Confirm Data Load"
get_col_names_list_tb_id                           =   "censusdfload"

get_col_names_list_tb_keyTitleList                 =   ["Select</br>More</br>Columns","Show</br>Selected</br>Columns","Return","Help"]

get_col_names_list_tb_jsList                       =   ["get_census_callback("+str(swcm.MORE_COLS_SUBDATA_DETAILS)+")",
                                                        "get_census_callback("+str(swcm.SHOW_SELECTED_COLUMNS)+")",
                                                        "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                        "displayhelp('" + str(dfchelp.DF_CENSUS_LOAD_COL_TO_DF_MORE_COLS_ID) + "')"]

get_col_names_list_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   insert columns into df input 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#    insert cols into df inputs
#--------------------------------------------------------------------------
"""
insert_cols_in_df_input_title                   =   "Insert Columns in df"
insert_cols_in_df_input_id                      =   "insertcoldf"
insert_cols_in_df_input_idList                  =   ["censusdfstoload",
                                                     "censusdfsinmemory",
                                                     "userdfstoloadtolist",
                                                     "userdfcolslist",
                                                     "keycolumnname",
                                                     "userdfsindexkeys",
                                                    None,None,None]

insert_cols_in_df_input_labelList               =   ["census_df(s)_to_load_cols_from",
                                                     "census_df(s)_in_memory",
                                                     "user_df(s)_to_insert_into",
                                                     "user_df(s)",
                                                     "user_df_column_names",
                                                     "key_column_in_user_df",
                                                     "Insert</br>Columns</br>into df",
                                                     "Return",
                                                     "Help"]

insert_cols_in_df_input_typeList               =   ["text","select","text","select","select","text",
                                                     "button","button","button"]

insert_cols_in_df_input_placeholderList        =   ["census datasets to insert from",
                                                    "census datasets in memory",
                                                     "user dfs to insert into",
                                                     "user dfs",
                                                     "user df index column",
                                                     "user df columns",
                                                     None,None,None]

insert_cols_in_df_input_jsList                 =   [None,None,None,None,None,None,
                                                    "get_census_callback("+str(swcm.PROCESS_INSERT_CENSUS_COLS)+")",
                                                    "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                    "displayhelp('" + str(dfchelp.DF_CENSUS_INSERT_COL_TO_DF_ID) + "')"]

insert_cols_in_df_input_reqList                =   [0,1,2,3,4,5]


"""
#--------------------------------------------------------------------------
#    cols to insert into df inputs
#--------------------------------------------------------------------------
"""
cols_to_insert_in_df_input_title                =   "Columns To Insert List"
cols_to_insert_in_df_input_id                   =   "colstoinsertlist"
cols_to_insert_in_df_input_idList               =   ["colstoinsert",
                                                     "coltoinsertminval",
                                                     "coltoinsertmaxval",
                                                     "coltoinsertdtype",
                                                     "newcoldtype",
                                                     "currentcolnanval",
                                                     "newcolnanval",
                                                     None,None]

cols_to_insert_in_df_input_labelList            =   ["census_columns_selected_to_insert_into_user_df",
                                                     "current_column_min_val",
                                                     "current_column_max_val",
                                                     "current_census_column_data_type",
                                                     "new_census_column_data_type",
                                                     "current_col_nan_value",
                                                     "new_column_nan_value",
                                                     "Change Column</br>Attributes",
                                                     "Select More</br>Subsets"]

cols_to_insert_in_df_input_typeList            =   ["select","text","text","text","select","text","text",
                                                    "button","button","button"]

cols_to_insert_in_df_input_placeholderList     =   ["cols to insert into user df",
                                                    "current columns min_val",
                                                    "current columns max_val",
                                                    "current columns data type",
                                                    "new column data type",
                                                    "current columns nan value",
                                                    "new column nan value",
                                                     None,None]

cols_to_insert_in_df_input_jsList              =   [None,None,None,None,None,None,None,
                                                    "get_census_callback("+str(swcm.PROCESS_CHANGE_COL_FOR_ATTRS) +")",
                                                    "get_census_callback("+str(swcm.SHOW_DATASET_SUBSETS) +")"]

cols_to_insert_in_df_input_reqList             =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    dfcensus get columns for df taskbar
#--------------------------------------------------------------------------
"""
data_cols_load_tb_doc_title               =   "Get Columns For Load"
data_cols_load_tb_title                   =   "Get Columns For Load"
data_cols_load_tb_id                      =   "censusdataloadcolstb"

data_cols_load_tb_keyTitleList            =   ["Insert Census</br>Dataset(s)</br>In User df(s)",
                                               "Return","Help"]

data_cols_load_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_CENSUS_DATASETS_FOR_INSERT)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                               "displayhelp('" + str(dfchelp.DF_CENSUS_CONFIGURE_ID) + "')"]

data_cols_load_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get columns for df taskbar
#--------------------------------------------------------------------------
"""
insert_cols_tb_doc_title                  =   "Get Columns For Load"
insert_cols_tb_title                      =   "Get Columns For Load"
insert_cols_tb_id                         =   "censusdataloadcolstb"

insert_cols_tb_keyTitleList               =   ["Insert Census</br>Dataset(s)</br>In User df(s)",
                                               "Return","Help"]

insert_cols_tb_jsList                     =   ["get_census_callback("+str(swcm.DISPLAY_INSERT_COLS_TO_DF)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_CENSUS_DATASETS_FOR_INSERT
                                                                          )+")",
                                               "displayhelp('" + str(dfchelp.DF_CENSUS_CONFIGURE_ID) + "')"]

insert_cols_tb_centered                   =   True


"""
#--------------------------------------------------------------------------
#   subdata columns select  
#--------------------------------------------------------------------------
"""
get_subdata_cols_select_input_title             =   "Get Census Subset Columns"
get_subdata_cols_select_input_id                =   "swcscolssel"
get_subdata_cols_select_input_idList            =   ["censuscolssellist",
                                                     "censuscolnameslist",
                                                     None,None,None]

get_subdata_cols_select_input_labelList         =   ["census_subset_columns_to_get_or_drop",
                                                     "census_subset_column_names_list",
                                                     "Get</br>Columns</br>Selected",
                                                     "Drop</br>Columns</br>Selected",
                                                     "Help"]

get_subdata_cols_select_input_typeList          =   [maketextarea(10,True),"select",
                                                     "button","button","button"]

get_subdata_cols_select_input_placeholderList   =   ["census subdata columns to get or drop",
                                                     "census subdata columnslist",
                                                     None,None,None]

get_subdata_cols_select_input_jsList            =   [None,None,
                                                    "get_subset_col_names_callback("+str(swcm.PROCESS_INSERT_COLS_GET)+")",
                                                    "get_subset_col_names_callback("+str(swcm.PROCESS_INSERT_COLS_DROP)+")",
                                                    "displayhelp('" + str(dfchelp.DF_CENSUS_CONFIGURE_ID) + "')"]

get_subdata_cols_select_input_reqList           =   [0,1]

get_subdata_cols_select_input_form              =   [get_subdata_cols_select_input_id,
                                                     get_subdata_cols_select_input_idList,
                                                     get_subdata_cols_select_input_labelList,
                                                     get_subdata_cols_select_input_typeList,
                                                     get_subdata_cols_select_input_placeholderList,
                                                     get_subdata_cols_select_input_jsList,
                                                     get_subdata_cols_select_input_reqList]  




SWUtility_census_inputs                          =   [get_subdata_cols_select_input_id, insert_cols_in_df_input_id]





"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                         Census Data Utilities
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def get_census_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(census_tb_id,
                                               census_tb_keyTitleList,
                                               census_tb_jsList,
                                               census_tb_centered))

def display_get_cols_tb() :

    get_cols_tb        =   ButtonGroupForm(data_cols_load_tb_id,
                                           data_cols_load_tb_keyTitleList,
                                           data_cols_load_tb_jsList,
                                           data_cols_load_tb_centered)
            
    get_cols_tb.set_customstyle({"font-size":13, "height":75, "width":140, "left-margin":30})
        
    get_cols_tb_html   =   get_cols_tb.get_html()


    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [get_cols_tb_html]
        
    display_generic_grid("dfcensus-short-note-wrapper",gridclasses,gridhtmls)
    print("\n")


def any_datasets_processed(files_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : see if any Trues in a list of datasets processed
    * 
    * parms :
    *
    * returns : 
    *  list of processed datasets
    * --------------------------------------------------------
    """
    
    for i in range(len(files_processed)) :
        for j in range(len(files_processed[i])) :
            if(files_processed[i][j]) :
                return(True)
    
    return(False)

def get_datasets_processed() :
    """
    * -------------------------------------------------------------------------- 
    * function : get list of datasets processed
    * 
    * parms :
    *
    * returns : 
    *  list of processed datasets
    * --------------------------------------------------------
    """
    
    import os
    from dfcleanser.common.common_utils import does_file_exist
    
    dfc_census_dataset_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_dataset_path     =   (dfc_census_dataset_path + "\\datasets\\")
    
    files_processed     =   []
    
    for i in range(len(swcm.zip_file_names) ) :
        
        dataset_csvs    =   []
        
        for j in range(4) :
            
            if(j==0)        :   ctype   =   "zipcode"
            elif(j==1)      :   ctype   =   "cities"
            elif(j==2)      :   ctype   =   "counties"
            else            :   ctype   =   "states"
            
            csvfname    =   swcm.zip_file_names[i][0].replace(".zip","_" + ctype + ".csv")
            if(does_file_exist(dfc_census_dataset_path+csvfname)) :
                dataset_csvs.append(True)
            else :
                dataset_csvs.append(False)
                
        files_processed.append(dataset_csvs)
        
    return(files_processed)

def any_datasets_loaded_to_dfs(datasets_loaded_to_dfs) :
    """
    * -------------------------------------------------------------------------- 
    * function : see if any Trues in a list of datasets loaded to dfs
    * 
    * parms :
    *
    * returns : 
    *  list of processed datasets
    * --------------------------------------------------------
    """
    
    for i in range(len(datasets_loaded_to_dfs)) :
        for j in range(len(datasets_loaded_to_dfs[i])) :
            if(datasets_loaded_to_dfs[i][j]) :
                return(True)
    
    return(False)
    
def any_dataframes_for_any_datasets() :
    """
    * -------------------------------------------------------------------------- 
    * function : check if any dataframes for census datasets have been built
    * 
    * parms :
    *
    * returns : 
    *  boolean flag
    * --------------------------------------------------------
    """
    
    for i in range(len(swcm.census_data_dirs)) :  
        
        dfs_flag    =   any_dataframes_loaded_for_dataset(swcm.census_data_dirs[i])
        
        if(dfs_flag) :
            return(True)
            
    return(False)


def any_dataframes_loaded_for_dataset(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : check if any dataframes for specific dataset have been built
    * 
    * parms :
    *
    * returns : 
    *  boolean flag
    * --------------------------------------------------------
    """
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list() 
    
    if(dataframes_loaded is None) :
        
        return(False)
        
    else :
    
        for i in range(len(dataframes_loaded)) :
            if(dataframes_loaded[i].find(datasetid) > -1) :
                return(True)
            
    return(False)
   

short_note_html="<div style='text-align:center; margin-left:1px; width:540px; background-color: #F8F5E1; color:#67a1f3; border: 1px solid #67a1f3; word-wrap:break-word'>XXXNote</div>"

def display_short_note(msg) :
    
    note_html   =   short_note_html.replace("XXXNote",msg)
    
    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [note_html]
    
    display_generic_grid("dfcensus-short-note-wrapper",gridclasses,gridhtmls)


def any_datasets_to_drop(datasets_to_configure,datasets_processed) :
    
    for i in range(len(datasets_to_configure)) :
        for j in range(4) :
            if(datasets_to_configure[i][j] == "False") :
                if(datasets_processed[i][j]) :
                    return(True)
                    
    return(False)                

    
def any_datasets_to_add(datasets_to_configure,datasets_processed) :
    
    for i in range(len(datasets_to_configure)) :
        for j in range(4) :
            if(datasets_to_configure[i][j] == "True") :
                if(not (datasets_processed[i][j])) :
                    return(True)
                    
    return(False)                

    
def get_datasets_downloaded_list() :
    """
    * -------------------------------------------------------------------------- 
    * function : get the list of downloaded datasets
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\working\\")
    
    datasets_downloaded     =   []
    
    if(does_dir_exist(dfc_census_path)) :

        for i in range(len(swcm.census_datasets)) :   
            
            dataset_zip     =   dfc_census_path + swcm.census_data_dirs[i] + ".zip"
            
            if(does_file_exist(dataset_zip)) :
                datasets_downloaded.append(True) 
            else :
                datasets_downloaded.append(False) 

    else :
        
        for i in range(len(swcm.census_datasets)) :   
            datasets_downloaded.append(False) 

    return(datasets_downloaded)    


def get_datasets_loaded_to_memory() :
    """
    * -------------------------------------------------------------------------- 
    * function : get the list of census datasets loaded to mempry
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
    dfs_loaded  =   get_dfc_dataframes_titles_list()  
    
    census_dfs_in_memory    =   []

    for i in range(len(swcm.index_fnames)) :
        
        index_type_dfs  =   []
    
        for j in range(len(swcm.census_data_dirs)) :
            if( (swcm.census_data_dirs[j] + "_" + swcm.index_fnames[i] + "_df") in dfs_loaded) :
                index_type_dfs.append(True)
            else :
                index_type_dfs.append(False)
                
        census_dfs_in_memory.append(index_type_dfs)
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("census_dfs_in_memory",census_dfs_in_memory)
                
    return(census_dfs_in_memory)       


def get_user_dfs(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the list of user dfs in memry
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    all_dfs     =   cfg.get_dfc_dataframes_titles_list()
    user_dfs    =   []
    
    for i in range(len(all_dfs)) :
        
        if( (not (all_dfs[i] == datasetid.lower() + "_zipcode_df")) and 
            (not (all_dfs[i] == datasetid.lower() + "_cities_df")) and
            (not (all_dfs[i] == datasetid.lower() + "_counties_df")) and
            (not (all_dfs[i] == datasetid.lower() + "_states_df")) ) :
            
            user_dfs.append(all_dfs[i])
            
    return(user_dfs)
    


            

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                       Census Info Notes
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

mult_line_separator="&nbsp;&nbsp;<font color='#67a1f3'>-------------------------------------------------------------------------------------------------------------------- </font><br>"

"""
#  Download datasets
"""
download_notes_info_html="<div class='dfcleanser-common-grid-note'>To get detailed info on the datasets click on the details icons.<br><br>Select which datasets to download and process by checking the appropriate checkboxes above and clicking on the Download Selected Datasets button.</div>"
download_notes_subdata_info_html="<div class='dfcleanser-common-grid-note'>Once you review dataset details and decide which datasets to buid by checking the appropriate checkboxes above then click on the Build Selected Datasets button.</div>"
download_notes_html="<br><div style='text-align:center; margin-left:50px; width:720px; background-color: #F8F5E1; color:#67a1f3; border: 1px solid #67a1f3; word-wrap:break-word'>Please download the zip files highlighted above via clicking on the download links above or go to the <a href='https://github.com/RickKrasinski/dfc_census_zips' target='_blank'>dfc_census_repository</a> directly.<br><br>Download zips to the XXXCensusWorkingDir location. To learn how to change your browser download location click <a href='https://support.google.com/chrome/answer/95759?co=GENIE.Platform%3DDesktop&hl=en' target='_blank'>here.</a></div><br><br><br><br><br>"


configure_notes_info_html="<br><div class='dfcleanser-common-grid-note'>To drop a dataset unselect the checked dataset(s) to drop.<br>To add a dataset select the unchecked dataset(s) you want to add.</div>"
configure_no_select_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:'60%;'>No datasets to configure were selected.<br>To go back and select datasets to configure click on 'Configure Datasets'.</div>"
configure_no_datasets_notes_info_html="<br><div class='dfcleanser-common-grid-note'>No datasets are currently downloaded and processed.</div><br>"


load_datasets_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Load Census Data to Memory button to laod the datasets as dfc datframes..</div>"
load_datasets_db_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Define db Connector button to define a db connector and laod the datasets to your database.</div>"
load_datasets_none_html="<br><div class='dfcleanser-common-grid-note'>No census datasets are downloaded for loading into dataframes.</div><br>"


"""
#  Get Census Columns Dataset and Subdata Selects
"""

get_dataset_columns_notes_html="<br><div class='dfcleanser-common-grid-note'>Select Census dataset(s) to get columns from for inserting into user df(s).</div><br>"
get_dataset_cols_subdata_list_notes_html="<br><div class='dfcleanser-common-grid-note'>Select a dataset subset to select columns from via clicking on the Columns button above.</div><br>"
get_dataset_cols_columns_list_notes_html="<br><div class='dfcleanser-common-grid-note'>Once you select all the columns to retrieve click on the 'Show Selected Columns' button to review and put the columns in a df.<br><br>To select more columns click on the 'Select More Columns' button.</div><br>"


"""
#  Get Census Columns Notes
"""

get_dataset_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the zip_code_column value in the output dataframe is nan or if there is no zipcode in the census zipcode dataset that matches the zipcode in the zip_code_name column.</div><br>"
get_dataset_city_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the city_column value in the output dataframe is nan or if there is a nan in the census city dataset that matches the city in the city_name column.</div><br>"
get_dataset_county_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the census_column_names_list above.<br><br>The na_fill_value is used if the county_column value in the output dataframe is nan or if there is no county in the census county dataset that matches the county in the county_name column.</div><br>"
get_dataset_state_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the state_column value in the output dataframe is nan or if there is no state in the census state dataset that matches the state in the state_name column.<br><br>Use a state value of US to get columns for the United States.</div><br>"

get_dataset_columns_no_datasetid_notes_html="<br><div class='dfcleanser-common-grid-note'>No dataset selected yet.</div><br>"
get_dataset_columns_no_dfs_loaded_html="<br><div class='dfcleanser-common-grid-note'>No Census df(s) are loaded. Go back to Load Census df(s) to load df(s) for column retrieval.</div><br>"

get_dataset_loaded_html="<br><div class='dfcleanser-common-grid-note'>To export a df click on the df name above.</div><br>"

datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>To Add/Drop datasets selected click on the Add/Drop Selected Datasets.</div><br>"
verify_datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>To Load/Unload datasets selected click on the Load/Unload Selected Datasets.</div><br>"
verify_no_datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>No datasets selected to Load or Unload.</div><br>"

configure_process_html="<div class='dfcleanser-common-grid-note'>To Add/Drop datasets selected click on the Add/Drop Selected Datasets.<br>Any datasets highlighted must be downloaded before being added.</div><br>"

datasets_in_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To load a dataset to a df check the dataset that is not currently checked.<br>To delete a dataset df uncheck a currently checked box.</div>"
export_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To export a dataset click on the export icon above.</div>"
load_to_db_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To load a dataset to a db click on the load to db icon above.</div>"

no_export_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>No census datasets loaded to memory for export.</div>"
no_load_to_db_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>No census datasets loaded to memory for load to a db.</div>"

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                     census data display objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   DOWNLOAD CENSUS DATASETS objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#                  Census Datasets Downloads Main Table html
#--------------------------------------------------------------------------
"""
datasets_downloaded_start_html  =   """
        <div style="width:240px;">
            <div class='container dc-tbl-container' id="dfCensusLoadOptions" style="width:360px;">
                <div class="row">
                    <div class="panel panel-primary" style="border:0;">
                        <div class="panel-heading clearfix dc-table-panel-heading">
                            <div class="input-group">
                                <div class="input-group-btn">
                                    <div class="input-group-btn">
                                        <p class="panel-title dc-search-panel-title pull-left" style="padding-right:20px">Census Datasets</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <table class="table dc-table" id="DIsamplerows">
                                <thead>
                                    <tr class="dcrowhead" id="DIsamplerows_thr">
                                        <th style=" width:54%; text-align:left;" class="dcleftcolhead">Dataset</th>
                                        <th style=" width:30%; " class="dccolhead">Download</th>
                                        <th style=" width:14%; " class="dccolhead">Details</th>
                                        <th style=" width:2%; text-align:left;" class="dcleftcolhead"></th>
                                    </tr>
                                </thead>
                                <tbody>
"""    
    
datasets_downloaded_end_html  =   """
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

datasets_download_row_html  =   """
                                    <tr class="dc-describe-table-body-row">
                                        <td style=" width:54%; font-size:12px;" class="dccolleft">XXXDataset</td>
                                        <td style=" width:30%; " class="dccolwrap">
                                            <div class="input-group-btn" style="padding-right:0px; padding-left:0px">
                                                <a class="dc-table-row-link" style="text-decoration:none;" href="https://github.com/RickKrasinski/dfc_census_zips/raw/master/XXXdsfname.zip">
                                                    <img title="Download XXXDataset" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_download.png' height="25px" width="77px" id="CDXXXDataset"></img>
                                                </a>
                                            </div>
                                        </td>
                                        <td style=" width:14%; font-size:11px; text-align:center;">
                                            <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                                <a  onclick="get_df_census_dataset_details('0','XXXDataset')">
                                                    <img style='margin: 0px auto; text-align:center;' title="XXXDataset Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="15px" width="15px"></img>
                                                </a>
                                            </div>
                                        </td>
                                        <td style=" width:2%; font-size:12px;" class="dccolleft"></td>
                                    </tr>
"""

datasets_no_download_row_html  =   """
                                    <tr class="dc-describe-table-body-row">
                                        <td style=" width:70%; font-size:12px;" class="dccolleft">XXXDataset</td>
                                        <td style=" width:30%; " class="dccolwrap"><span style="font-weight:bold">Downloaded</span></td>
                                        <td style=" width:14%; font-size:11px; text-align:center;">
                                            <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                                <a  onclick="get_df_census_dataset_details('0','XXXDataset')">
                                                    <img style='margin: 0px auto; text-align:center;' title="XXXDataset Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="15px" width="15px"></img>
                                                </a>
                                            </div>
                                        </td>
                                        <td style=" width:2%; font-size:12px;" class="dccolleft"></td>

                                    </tr>
"""
    
    
def get_downloaded_census_data_html() :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for datasets downloaded
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    downloaded_census_html  =   ""
    downloaded_census_html  =   (downloaded_census_html + datasets_downloaded_start_html)
    
    datasets_downloaded     =   get_datasets_downloaded_list()
        
    for i in range(len(datasets_downloaded)) :
        
        if(not (datasets_downloaded[i])) :
            
            row_html    =   datasets_download_row_html
            row_html    =   row_html.replace("XXXDataset",swcm.census_datasets[i])
            row_html    =   row_html.replace("XXXdsfname",swcm.census_data_dirs[i]) 
            row_html    =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i]) 
            
        else :
            
            row_html    =   datasets_no_download_row_html
            row_html    =   row_html.replace("XXXDataset",swcm.census_datasets[i])
            row_html    =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i]) 
            
        downloaded_census_html  =   (downloaded_census_html + row_html)
        
    downloaded_census_html  =   (downloaded_census_html + datasets_downloaded_end_html)
                   
    return(downloaded_census_html)


def display_downloaded_census_data(datasetid=None,subdataid=None,height=None,width=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the datasets download census screen
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    print("display_downloaded_census_data",datasetid,subdataid,height,width)
    
    datasets_loaded_html        =   get_downloaded_census_data_html()
    
    load_details_html           =   get_load_datasets_details_html(datasetid,subdataid,height,width)

    load_details_heading_html   =   "<div>Census Datasets Downloaded</div><br>"
        
    dfc_census_path             =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path             =   (dfc_census_path + "\\working\\")
    new_download_notes_html     =   download_notes_html.replace("XXXCensusWorkingDir",dfc_census_path)

    #print(datasets_loaded_html)
    #print(new_download_notes_html)
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-main","dfc-right"]
    gridhtmls       =   [load_details_heading_html,datasets_loaded_html,new_download_notes_html,load_details_html]
        
    
    print("\n")
    display_generic_grid("dfcensus-datasets-loaded-wrapper",gridclasses,gridhtmls)
    print("\n")
        

"""
#--------------------------------------------------------------------------
#                  Census Datasets Details Description objects
#--------------------------------------------------------------------------
"""

census_datasets_description_head = """                        <thead>
                            <tr class="dcrowhead" id="DIsamplerows_thr">
                                <th style=" width:85%; font-size:13px; text-align:left;" class="dcleftcolhead">Datasets</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Num</br>Cols</th>
                            </tr>
                        </thead>
                        <div style="width:480px; height:360px; overflow:auto;">
                        <tbody>
"""

census_datasets_description_row_html ="""                            <tr class="dc-describe-table-body-row">
                                <td style=" width:85%; text-align:left;" class="dccolwrap"><b>XXXDatasetID</b></br>XXXDatasetText</td>
                                <td style=" width:15%; " class="dccolwrap">XXXDatasetNumCols</td>
                            </tr>
"""

census_load_details_html ="""
    <div class='container dc-tbl-container' id="dfCensusDetails">
        <div class="row">
            <div class="panel panel-primary" style="border:0; width:480px;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:480px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title dc-search-panel-title pull-left" id="SubdataHeading" style="padding-right:20px">XXXdatasetid</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="width:480px; height:360px; overflow:auto;">
                    <table class="table dc-table">
"""

census_load_details_table_end_html ="""
                        </tbody>
                    </table>
"""
census_load_details_end_html ="""
                </div>
            </div>
        </div>
    </div>
"""

census_load_subdata_end_html ="""
            </div>
        </div>
    </div>
"""

census_zip_size_head = """
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:20%; font-size:13px;">&nbsp;Zip</br>Code</br>Size</th>
                                <th style=" width:20%; font-size:13px;">City</br>Size</th>
                                <th style=" width:20%; font-size:13px;">County</br>Size</th>
                                <th style=" width:20%; font-size:13px;">State</br>Size</th>
                                <th style=" width:20%; font-size:13px;">Total</br>Size</th>
                            </tr>
                        </thead>
                        <tbody>"""


census_zip_size_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:20%; font-size:13px;" class="dcleftcolhead">XXXZipCodeSize</td>
                                <td style=" width:20%; font-size:13px;">XXXCitySize</td>
                                <td style=" width:20%; font-size:13px;">XXXCountySize</td>
                                <td style=" width:20%; font-size:13px;">XXXStateSize</td>
                                <td style=" width:20%; font-size:13px;">XXXTotalSize</td>
                            </tr>"""


    
    
def get_load_datasets_details_html(datasetid=None,subdataid=None,height=None,width=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get display datasets details html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *   colnameid     -   column name id
    *   direction     -   scroll direction
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("get_load_datasets_details_html",datasetid,subdataid,height,width)
    
    load_datasets_details_html  =   ""
    
    if(datasetid is None) :
        
        header_html                 =   census_load_details_html
        header_html                 =   header_html.replace("XXXdatasetid","Description")
        load_datasets_details_html  =   (load_datasets_details_html + header_html) 
        
        load_datasets_details_html  =   (load_datasets_details_html + census_datasets_description_head) 
        
        if(not (height is None)) :
            load_datasets_details_html     =   load_datasets_details_html.replace('height:360px;','height:' + str(height) + 'px;')  
        else :
            load_datasets_details_html     =   load_datasets_details_html.replace('height:360px;','') 
                
        if(not (width is None)) :
            load_datasets_details_html     =   load_datasets_details_html.replace('width:480px;','width:' + str(width) + 'px;')  

        for i in range(len(swcm.census_datasets)) : 
        
            dsid     =  swcm.census_datasets[i].replace("_"," ")
            row_html =  census_datasets_description_row_html.replace("XXXDatasetID",dsid)
            row_html =  row_html.replace("XXXDatasetText",swcm.census_dataset_details[i])
            row_html =  row_html.replace("XXXDatasetNumCols",str(swcm.census_datasets_num_cols[i]))
        
            load_datasets_details_html  =   (load_datasets_details_html + row_html)

        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_table_end_html)
        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_end_html)
            
    else :
        
        load_datasets_details_html  =   get_census_datasets_details_table(datasetid,subdataid,height,width)
        
    #print(load_datasets_details_html)
    
    return(load_datasets_details_html)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   SETUP CENSUS DATASETS objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

setup_datasets_html ="""
        <div class='container dc-tbl-container' style='width:360px;' id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style='width:360px;'>
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style='width:360px;'>
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:30%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:10%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;Zip</br>Code</th>
                                <th style=" width:10%; font-size:13px; text-align:center;" class="dccolhead">City</th>
                                <th style=" width:17%; font-size:13px; text-align:center;" class="dccolhead">County</th>
                                <th style=" width:10%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;&nbsp;US</br>State</th>
                                <th style=" width:13%; font-size:13px; text-align:center;" class="dccolhead"></th>
                            </tr>
                        </thead>
                        <tbody>
"""

setup_datasets_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

setup_datasets_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:10%; font-size:13px;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:12px;' for="cb1XXXDatasetID">
                                            <input type='checkbox' id="cb1XXXDatasetID" onclick="set_census_cbs('cb1XXXDatasetID')" cb1flag cb1disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:10%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:12px;' for="cb2XXXDatasetID">
                                            <input type='checkbox' style="text-align:center" id="cb2XXXDatasetID" onclick="set_census_cbs('cb2XXXDatasetID')" cb2flag cb2disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:17%; text-align:center;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:12px;' for="cb3XXXDatasetID">
                                            <input  type='checkbox' id="cb3XXXDatasetID" onclick="set_census_cbs('cb3XXXDatasetID')" cb3flag cb3disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:10%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:12px;' for="cb4XXXDatasetID">
                                            <input type='checkbox' id="cb4XXXDatasetID" onclick="set_census_cbs('cb4XXXDatasetID')" cb4flag cb4disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:13%; text-align:center;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_dataset_details('0','XXXDatasetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXTDatasetID Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>
"""


"""
#--------------------------------------------------------------------------
#                              Datasets Add/Drop Objects
#--------------------------------------------------------------------------
"""

add_drop_datasets_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Data Subsets To Drop</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:65%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:35%; font-size:13px; text-align:left;" class="dccolheadleft">Downloaded</th>
                            </tr>
                        </thead>
                        <tbody>
"""

add_drop_datasets_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


add_drop_datasets_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:65%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>
                                <td style=" width:35%; font-size:13px; text-align:left;" class="dccolleft">XXXFileName</td>               
                            </tr>
"""

def get_add_drop_datasets_html(datasets_to_configure,datasets_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the drop / add datasets list
    * 
    * parms :
    *   datasets_to_configure     -   datasets to setup
    *   datasets_processed        -   datasets processed
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    #print("get_configure_datasets_verification_html\n",datasets_to_configure,"\n\n",datasets_processed)
    
    add_ds_html     =   add_drop_datasets_html
    add_ds_html     =   add_ds_html.replace("To Drop","To Add")
    drop_ds_html    =   add_drop_datasets_html 
    
    add_datasets    =   []
    drop_datasets   =   []
    
    datasets_downloaded     =   get_datasets_downloaded_list()

    
    for i in range(len(datasets_to_configure)) :
        
        for j in range(4) :
            
            if(datasets_to_configure[i][j] == "True") :
                
                if(not (datasets_processed[i][j])) :
                    
                    row_html    =   add_drop_datasets_row_html
                    row_html    =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                    
                    
                    
                    if(datasets_downloaded[i]) :
                        row_html    =   row_html.replace("XXXFileName","True")
                        add_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                    else :
                        row_html    =   row_html.replace('<tr class="dc-describe-table-body-row">','<tr class="dc-describe-table-body-row" style="background-color:#ffffcc">')
                        row_html    =   row_html.replace("XXXFileName","False")
                                    
                    add_ds_html   =   (add_ds_html + row_html)
                    
            else :
                
                drop_ds_html  =   drop_ds_html.replace("Downloaded","")
                
                if(datasets_processed[i][j]) :
                    
                    row_html    =   add_drop_datasets_row_html
                    row_html    =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                    
                    row_html    =   row_html.replace("XXXFileName"," ") 
                                    
                    drop_ds_html   =   (drop_ds_html + row_html)
                    
                    drop_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                
    
    add_ds_html   =   (add_ds_html + add_drop_datasets_end_html)  
    #print(add_ds_html)
    drop_ds_html  =   (drop_ds_html + add_drop_datasets_end_html)
    
    if(len(add_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_ADD_DATASETS_LIST,add_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)

    if(len(drop_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_DROP_DATASETS_LIST,drop_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
    
    return([add_ds_html,drop_ds_html])    


def display_add_drop_datasets(datasets_to_configure) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the screen to ad or drop datasets
    * 
    * parms :
    *   datasets_to_configure     -   datasets to add or drop
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    datasets_processed  =   get_datasets_processed()
    
    if(swcm.DEBUG_CENSUS) :
        print("display_add_drop_datasets\n",datasets_to_configure,"\n",datasets_processed)
    
    [configure_drop_datset_html,configure_add_datset_html]    =   get_add_drop_datasets_html(datasets_to_configure,datasets_processed)
    
    if( (any_datasets_to_drop(datasets_to_configure,datasets_processed)) or 
        (any_datasets_to_add(datasets_to_configure,datasets_processed)) ) :
        
        configure_drop_notes_html       =   configure_process_html
        
        configure_data_tb               =   ButtonGroupForm(data_configure_verify_tb_id,
                                                            data_configure_verify_tb_keyTitleList,
                                                            data_configure_verify_tb_jsList,
                                                            data_configure_verify_tb_centered)
    
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":240})
        configure_data_tb_html          =   configure_data_tb.get_html()

        
    else :
        
        configure_drop_notes_html       =   configure_no_select_notes_info_html
        
        configure_data_tb               =   ButtonGroupForm(data_configure_no_datasets_tb_id,
                                                            data_configure_no_datasets_tb_keyTitleList,
                                                            data_configure_no_datasets_tb_jsList,
                                                            data_configure_no_datasets_tb_centered)
    
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":240})
        configure_data_tb_html          =   configure_data_tb.get_html()
        
        
    configure_heading_html          =   "<div>Configure Datasets</div><br></br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-main","dfc-footer"]
    gridhtmls       =   [configure_heading_html,configure_drop_datset_html,configure_add_datset_html,configure_drop_notes_html,configure_data_tb_html]
    
    #print(configure_drop_datset_html)
    #print(configure_add_datset_html)
    #print(configure_add_datset_html)
    
    print("\n")
    display_generic_grid("dfcensus-configure-data-wrapper",gridclasses,gridhtmls)
    print("\n")


        












"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                  Census Data Subset Details html
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

census_subdata_table_html = """
                 <div  style="width:480px; height:360px; overflow:auto;">
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:55%; font-size:13px; text-align:left;" class="dcleftcolhead">Subset</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Num Cols</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Nan Pct</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Details</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
census_subdata_table_html_end = """
                        </tbody>
                    </table>
                </div>"""

census_subdata_table_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:55%; font-size:13px; text-align:left;">XXXsubdatatitle</td>
                                <td style=" width:15%; font-size:13px;">XXXsubdatacols</td>
                                <td style=" width:15%; font-size:13px;">XXXsubdatanans</td>
                                <td style=" width:15%; font-size:13px;">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_subData_details('XXXDatasetID','XXXSubDataID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXSubDataText Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="15px" width="15px"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>"""
                          
                            
"""                           
#--------------------------------------------------------------------------
#              Census Data Subset Details For Load df Columns
#--------------------------------------------------------------------------
"""

load_cols_subdata_table_html = """
        <div class='container dc-tbl-container' style="width:540px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:540px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">XXXDatasetID Subsets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="width:540px;">
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:55%; font-size:13px; text-align:left;" class="dcleftcolhead">Subset</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Num Cols</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Nan Pct</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Columns</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
load_cols_subdata_table_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""                        
                        









""""
#--------------------------------------------------------------------------
#          Census Data columns Subset Column Names Table html
#--------------------------------------------------------------------------
"""

get_cols_colnames_table_html = """

                <div style="margin-left:auto; margin-right:auto; width:540px">
                    <div class="container" style="padding:5px; margin:auto; width:100%; border:0px" id="subdatacolnamescontainer">
                        <div class="container" style="padding:5px; margin:auto; width:100%"  id="subdatacolnamesselectdiv">
                            <div class="container dc-container dc-default-input-inner-div">
                                <div class="form-group-sm">
                                    <label  for="subdatacolnames" style="text-align:left; font-size: 13px">XXXColumnsTitle</label>
                                    <select id="subdatacolnames" multiple="multiple" size="30" style="margin-left:1px; font-size: 11px" class="form-control" enabled>
"""

get_cols_colnames_table_row_html = """                              <option style='text-align:left; font-size:11px;' value="XXXColname">XXXSColname</option>
"""

get_cols_colnames_table_end_html = """
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
"""

get_cols_colnames_table_selects_end_html = """
                                    </select>
                                </div>
                            </div>
                            <div style="margin-top: 10px"  id="censusdfinsertcols">
                                <div class="container dc-container dc-default-input-button-container btn-grp-center">
                                    <div class="btn-group btn-center"   style="width: 100%">
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  margin-left: 58px;  height: 75px;  width: 80px ' onclick="get_census_callback(33)">Insert</br>Columns</br>Into df(s)</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px ' onclick="get_census_callback(29)">Select</br>More</br>Columns</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px ' onclick="get_census_callback(0)">Return</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px ' onclick="displayhelp(https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset)">Help</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
"""


configure_drop_notes_html="""
        <div style="margin-left:30px;">
            <p>To drop the data selected above click on the Drop Data button.</p>
        </div>
"""



"""
#--------------------------------------------------------------------------
#                   Census Get Dataset Columns 
#--------------------------------------------------------------------------
"""

census_get_cols_for_df_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:32%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">Zip</br>Code</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">City</th>
                                <th style=" width:18%; font-size:13px;" class="dccolhead">County</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">&nbsp;US</br>State</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">Columns</th>
                            </tr>
                        </thead>
                        <div style="width:480px; height:360px; overflow:auto;">
                            <tbody>
"""

census_get_cols_for_df_end_html ="""
                            </tbody>
                        </div>
                    </table>
                </div>
            </div>
        </div>
"""


census_get_cols_for_df_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:32%; font-size:13px; text-align:left;" class="dccolleft">XXXKeyTypeID</td>
                                <td style=" width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID0" rb0checked disabled>&nbsp;&nbsp;</input>
                                    </div>
                                </td>               
                                <td style="width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID1" rb1checked disabled></input>
                                    </div>
                                </td>               
                                <td style="width:18%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID2" rb2checked disabled></input>
                                    </div>
                                </td>               
                                <td style="width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID3" rb3checked disabled></input>
                                    </div>
                                </td> 
                                <td style=" width:14%; font-size:11px; text-align:center;">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a  onclick="get_df_census_dataset_details('0','XXXDatasetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXDatasetID subsets" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="15px" width="15px"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>
"""


census_get_cols_for_df_blank_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:100%; font-size:13px; text-align:left;" class="dccolleft">
                                    <div
                                        <br><div id='addfilternote' style='text-align:center; margin-left:1px; width:100%px; border: 1px solid #67a1f3;'>No dataset selected yet.</div><br>"
                                    </div>
                                </td>
                            </tr>
"""




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Datasets Details Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""  










""""
#--------------------------------------------------------------------------
#                Census Subset Column Names Table html
#--------------------------------------------------------------------------
"""

census_colnames_table_html = """
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:85%; font-size:13px; text-align:left;" class="dcleftcolhead">Column Name</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Nan Pct</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
census_colnames_table_html_end = """
                        </tbody>
                    </table>
                </div>"""

census_colnames_table_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:85%; font-size:11px; text-align:left;" class="dccolleft">XXXcolname</td>
                                <td style=" width:15%; font-size:11px;">XXXcnamenans</td>
                            </tr>"""

census_colnames_scroll_html = """
                <div style="margin-top: 10px; width:480px; background-color:#F8F5E1;" id="censuscolscroll ">
                    <div class="container dc-container dc-default-input-button-container btn-grp-center">
                        <div class="btn-group btn-center"   style="width: 100%">
                            <button type="button" class="btn btn-primary" style = ' font-size: 11px;  margin-left: 130px;  height: 30px;  width: 80px; ' onclick="scroll_census_cols('XXXDatasetID','XXXSubDataID','XXXcolid','0')">More</button>
                            <button type="button" class="btn btn-primary" style = ' font-size: 11px;  height: 30px;  width: 80px; ' onclick="scroll_census_cols('XXXDatasetID','XXXSubDataID','XXXcolid','1')">Previous</button>
                        </div>
                    </div>
                </div>
"""

    
    









    
    
"""
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
* -------------------------- Downloaded datasets objects -------------------------------
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
"""
   

    





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Datasets To Configure Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""  


def get_configure_datasets_html(forconfigure=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("get_download_datasets_html",forconfigure)  
        
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + setup_datasets_html)  

    datasets_processed  =   get_datasets_processed()
    datasets_downloaded =   get_datasets_downloaded_list()
    
    if(swcm.DEBUG_CENSUS) :
        print("datasets_processed",datasets_processed)
        print("datasets_downloaded",datasets_downloaded)
    
    for i in range(len(swcm.census_datasets)) : 
        
        dsid                =   swcm.census_datasets[i]
        dsid                =   dsid.replace("_"," ")
        row_html            =   setup_datasets_row_html.replace("XXXTDatasetID",dsid)
        row_html            =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
            
        if(forconfigure) :
            row_html            =   row_html.replace("get_census_dataset_details","get_configure_dataset_details") 
            
        for j in range(len(datasets_processed[i])) :
                
            cbflg   =   "cb" + str(j+1) + "flag"
            cbdis   =   "cb" + str(j+1) + "disabled"
                
            if(datasets_processed[i][j]) :
                row_html            =   row_html.replace(cbflg,"checked") 
                row_html            =   row_html.replace(cbdis,"")
                    
            else :
                
                if(forconfigure) :

                    if(not (datasets_downloaded[i])) :

                        row_html            =   row_html.replace(cbflg,"")         
                        row_html            =   row_html.replace(cbdis,"disabled") 
                    
                else :
                
                    row_html            =   row_html.replace(cbflg,"") 
                    row_html            =   row_html.replace(cbdis,"")
                    
                    
            cbdis   =   "cb" + str(j+1) + "disabled"
            
        if(forconfigure) :
            row_html            =   row_html.replace("cb5flag","")         
            row_html            =   row_html.replace("cb5disabled","disabled")         
            
        load_datasets_html  =   (load_datasets_html + row_html)
    
    load_datasets_html  =   (load_datasets_html + setup_datasets_end_html)
    
    return(load_datasets_html)

    
def display_configure_census_data(datasetid=None,forconfigure=False,subdataid=None,height=None,width=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the main download census screen
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *   colnameid     -   column name id
    *   direction     -   scroll direction
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("display_configure_census_data",datasetid,forconfigure,subdataid,height,width)
    
    
    configure_census_html    =   get_configure_datasets_html(forconfigure)
    
    if(forconfigure) :
        dropsubs    =   cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
        
        if(any_datasets_processed(get_datasets_processed())) :
            
            if( not (dropsubs is None)) :
                if(dropsubs =="NO DATASETS SELECTED") :
                    configure_notes_html     =   configure_no_select_notes_info_html
                    cfg.drop_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
                
            else :
                configure_notes_html     =   configure_notes_info_html
                    
        else :
            configure_notes_html     =   configure_no_datasets_notes_info_html    
                
        configure_details_heading_html       =   "<div>Get Census Data Subsets</div><br>"
                
    else :
        
        if(not(subdataid is None)) :
            configure_notes_html     =   download_notes_subdata_info_html
        else :
            configure_notes_html     =   download_notes_info_html
            
        configure_details_heading_html       =   "<div>Get Census Data Subsets</div>"
    
    
    
    configure_details_html      =   get_load_datasets_details_html(datasetid,subdataid,height,width)
    


    if(forconfigure) :
        
        #print("get_datasets_processed",get_datasets_processed())
        
        if(any_datasets_processed(get_datasets_processed())) :
        
            configure_data_tb        =   ButtonGroupForm(data_configure_tb_id,
                                                    data_configure_tb_keyTitleList,
                                                    data_configure_tb_jsList,
                                                    data_configure_tb_centered)
    
            configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":225})
        
            #configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Add/Drop")
            
        else :
            
            configure_data_tb        =   ButtonGroupForm(data_configure_no_datasets_tb_id,
                                                    data_configure_no_datasets_tb_keyTitleList,
                                                    data_configure_no_datasets_tb_jsList,
                                                    data_configure_no_datasets_tb_centered)
            
            configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":100, "left-margin":32})
        
            #configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Add/Drop")
            
        
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":210})
        
        configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Add/Drop")
                        
    configure_data_tb_html           =   configure_data_tb.get_html()
    
    
    
    

    if( (forconfigure) and (not (any_datasets_processed(get_datasets_processed()))) ) :   
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
        gridhtmls       =   [configure_details_heading_html,configure_census_html,configure_notes_html,configure_data_tb_html]
        
        #print(load_census_html)
        #print(load_notes_html)
        #print(load_data_tb_html)        
    
        print("\n")
        display_generic_grid("dfcensus-datasets-none-data-wrapper",gridclasses,gridhtmls)
        print("\n")
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-main","dfc-right","dfc-footer"]
        gridhtmls       =   [configure_details_heading_html,configure_census_html,configure_notes_html,configure_details_html,configure_data_tb_html]
        
   
    
        print("\n")
        display_generic_grid("dfcensus-download-data-wrapper",gridclasses,gridhtmls)
        print("\n")
        

























"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Datasets To Load In dfs Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""  

census_no_details_download_html ="""
        <div class='container dc-tbl-container' style='width:360px;' id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style='width:360px;'>
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style='width:360px;'>
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:37%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:14%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;Zip</br>Code</th>
                                <th style=" width:14%; font-size:13px; text-align:center;" class="dccolhead">City</th>
                                <th style=" width:21%; font-size:13px; text-align:center;" class="dccolhead">County</th>
                                <th style=" width:14%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;&nbsp;US</br>State</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_no_details_download_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

census_no_details_download_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:37%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:14%; font-size:13px;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb1XXXDatasetID">
                                            <input type='checkbox' id="cb1XXXDatasetID" onclick="set_census_cbs('cb1XXXDatasetID')" cb1flag cb1disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:14%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb2XXXDatasetID">
                                            <input type='checkbox' style="text-align:center" id="cb2XXXDatasetID" onclick="set_census_cbs('cb2XXXDatasetID')" cb2flag cb2disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:21%; text-align:center;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb3XXXDatasetID">
                                            <input  type='checkbox' id="cb3XXXDatasetID" onclick="set_census_cbs('cb3XXXDatasetID')" cb3flag cb3disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:14%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb4XXXDatasetID">
                                            <input type='checkbox' id="cb4XXXDatasetID" onclick="set_census_cbs('cb4XXXDatasetID')" cb4flag cb4disabled></input>
                                        </label>
                                    </div>
                                </td>               
                            </tr>
"""


datasets_to_load_verification_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Dataset df(s) To Unload From Memory</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                            </tr>
                        </thead>
                        <tbody>
"""

datasets_to_load_verification_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


datasets_to_load_verification_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>
                            </tr>
"""





def get_datasets_loaded_to_dfs_html() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("get_datasets_loaded_to_dfs_html") 
        
    datasets_loaded_html    =   ""
    datasets_loaded_html    =   (datasets_loaded_html + census_no_details_download_html)  

    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()
    datasets_processed      =   get_datasets_processed()
    
    for i in range(len(swcm.census_datasets)) : 
        
        dsid                =   swcm.census_datasets[i]
        dsid                =   dsid.replace("_"," ")
        
        
        row_html            =   census_no_details_download_row_html.replace("XXXTDatasetID",dsid)
        row_html            =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
            
        row_html            =   row_html.replace("get_census_dataset_details","get_load_to_df_dataset_details") 
            
        for j in range(len(datasets_loaded_to_dfs[i])) :
                
            cbflg   =   "cb" + str(j+1) + "flag"
            cbdis   =   "cb" + str(j+1) + "disabled"
            
            if(datasets_loaded_to_dfs[i][j]) :
                
                row_html            =   row_html.replace(cbflg,"checked") 
                row_html            =   row_html.replace(cbdis,"")
                    
            else :
                
                if(datasets_processed[i][j]) :
                    
                    row_html            =   row_html.replace(cbflg,"") 
                    row_html            =   row_html.replace(cbdis,"")
                
                else :
                    
                    row_html            =   row_html.replace(cbflg,"") 
                    row_html            =   row_html.replace(cbdis,"disabled")
                
        datasets_loaded_html  =   (datasets_loaded_html + row_html)
    
    datasets_loaded_html  =   (datasets_loaded_html + census_no_details_download_end_html)
    
    return(datasets_loaded_html)






def display_datasets_loaded_to_dfs() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """

    #if(swcm.DEBUG_CENSUS) :
    #    print("display_datasets_loaded_to_dfs")    

    loaded_dfs_html             =   get_datasets_loaded_to_dfs_html()
    loaded_dfs_html             =   loaded_dfs_html.replace('Census Datasets','Census Datasets Downloaded And Available To Load Into Memory')
    loaded_dfs_html             =   loaded_dfs_html.replace("dc-tbl-container' style='width:360px;","dc-tbl-container' style='width:540px;")
    loaded_dfs_html             =   loaded_dfs_html.replace('width:360px;','width:540px;')

    loaded_dfs_heading_html     =   "<div>Load Census Datasets To Working dfc df(s)</div><br>"
    
    loaded_dfs_notes_html       =   datasets_in_dfs_notes_info_html
    
    loaded_dfs_tb               =   ButtonGroupForm(data_load_datasets_to_df_tb_id,
                                                    data_load_datasets_to_df_tb_keyTitleList,
                                                    data_load_datasets_to_df_tb_jsList,
                                                    data_load_datasets_to_df_tb_centered)
            
    loaded_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":60})
    loaded_dfs_tb_html          =   loaded_dfs_tb.get_html()

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom","dfc-footer"]
    gridhtmls       =   [loaded_dfs_heading_html,loaded_dfs_html,loaded_dfs_notes_html,loaded_dfs_tb_html]
        
    print("\n")
    display_generic_grid("dfcensus-datasets-in-dfs-wrapper",gridclasses,gridhtmls)
    print("\n")


def get_datasets_to_load_verification_html(datasets_to_load_to_dfs) :
    """
    * -------------------------------------------------------------------------- 
    * function : verify datasets to load
    * 
    * parms :
    *   datasets_to_load     -   datasets to load
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    add_ds_html     =   datasets_to_load_verification_html
    add_ds_html     =   add_ds_html.replace("df(s) To Unload From Memory","To Load To Memory")
    drop_ds_html    =   datasets_to_load_verification_html 
    
    add_datasets    =   []
    drop_datasets   =   []
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()

    for i in range(len(datasets_to_load_to_dfs)) :
        
        for j in range(4) :
            
            if(datasets_to_load_to_dfs[i][j] == "True") :
                
                if(not (datasets_loaded_to_dfs[i][j])) :
                
                    row_html        =   datasets_to_load_verification_row_html
                    row_html        =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                                    
                    add_ds_html     =   (add_ds_html + row_html)
                
                    add_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                    
            else :
                
                if(datasets_loaded_to_dfs[i][j]) :
                
                    drop_ds_html  =   drop_ds_html.replace("Downloaded","")
                
                    row_html        =   datasets_to_load_verification_row_html
                    row_html        =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j) + "_df")
                                    
                    drop_ds_html    =   (drop_ds_html + row_html)
                    
                    drop_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                
    
    add_ds_html   =   (add_ds_html + datasets_to_load_verification_end_html)  
    drop_ds_html  =   (drop_ds_html + datasets_to_load_verification_end_html)
    
    if(len(add_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_ADD_DATASETS_LIST,add_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)

    if(len(drop_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_DROP_DATASETS_LIST,drop_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
        
    return([add_ds_html,drop_ds_html])    


def any_datasets_to_load_to_dfs(datasets_to_load_to_dfs) :
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()

    for i in  range(len(datasets_to_load_to_dfs)) :
        for j in range(4) :
            
            if(datasets_to_load_to_dfs[i][j] == "True") :
                if(not (datasets_loaded_to_dfs[i][j])) :
                    return(True)

    return(False)
    
    
def any_datasets_to_unload_from_dfs(datasets_to_load_to_dfs) :
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()

    for i in  range(len(datasets_to_load_to_dfs)) :
        for j in range(4) :
            
            if(datasets_loaded_to_dfs[i][j]) :
                if(datasets_to_load_to_dfs[i][j] == "False") :
                    return(True)

    return(False)
    

def display_load_to_df_verification_data(datasets_to_load_to_dfs) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the verify load unload dtatsets yo df
    * 
    * parms :
    *   datasets_to_load_to_df   -   dataset to load
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("display_load_to_df_verification_data",datasets_to_load_to_dfs)
    
    [datasets_to_load_to_df_html,datasets_to_unload_to_df_html]    =   get_datasets_to_load_verification_html(datasets_to_load_to_dfs)
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("any_datasets_to_load_to_dfs",any_datasets_to_load_to_dfs(datasets_to_load_to_dfs),any_datasets_to_unload_from_dfs(datasets_to_load_to_dfs))
    
    if( (any_datasets_to_load_to_dfs(datasets_to_load_to_dfs)) or 
        (any_datasets_to_unload_from_dfs(datasets_to_load_to_dfs)) ) :
        
        loaded_to_dfs_notes_html       =   verify_datasets_to_load_process_html
        
        loaded_to_dfs_tb               =   ButtonGroupForm(load_datasets_to_df_verify_tb_id,
                                                           load_datasets_to_df_verify_tb_keyTitleList,
                                                           load_datasets_to_df_verify_tb_jsList,
                                                           load_datasets_to_df_verify_tb_centered)
    
        loaded_to_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":250})
        loaded_to_dfs_tb_html          =   loaded_to_dfs_tb.get_html()

        
    else :
        
        loaded_to_dfs_notes_html       =   verify_no_datasets_to_load_process_html
        
        loaded_to_dfs_tb               =   ButtonGroupForm(load_datasets_to_df_no_datasets_tb_id,
                                                           load_datasets_to_df_no_datasets_tb_keyTitleList,
                                                           load_datasets_to_df_no_datasets_tb_jsList,
                                                           load_datasets_to_df_no_datasets_tb_centered)
    
        loaded_to_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":250})
        loaded_to_dfs_tb_html          =   loaded_to_dfs_tb.get_html()
        
        
    loaded_to_dfs_heading_html          =   "<div>Load Datasets To df(s)</div><br></br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-main","dfc-footer"]
    gridhtmls       =   [loaded_to_dfs_heading_html,datasets_to_load_to_df_html,datasets_to_unload_to_df_html,loaded_to_dfs_notes_html,loaded_to_dfs_tb_html]
    
    #print(configure_drop_datset_html)
    #print(configure_add_datset_html)
    #print(configure_add_datset_html)
    
    print("\n")
    display_generic_grid("dfcensus-configure-data-wrapper",gridclasses,gridhtmls)
    print("\n")








#TODO no onw calling 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Census dfs Loaded objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

census_loaded_to_dfs_html ="""
        <div class='container dc-tbl-container' style="width:520px;" id="dfCensusLoadedDfs">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left">Census dfs Loaded</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:30%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:60%; font-size:13px; text-align:left;" class="dccolhead">Census df Loaded</th>
                                <th style=" width:10%; font-size:13px; text-align:left;" class="dccolhead">&nbsp;</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_loaded_to_dfs_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

census_loaded_to_dfs_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXXDatasetID</td>              
                                <td style=" width:60%; font-size:12px; text-align:left;" class="dccolwrap">XXXXdfname</td>
                                <td style=" width:10%; font-size:12px; text-align:left;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="XXXXcallback('XXXXdfname')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXXdfname df" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="20px" width="20px" id="CXXXXdfname"></img>
                                        </a>
                                    </div>
                                </td>               
                            </tr>
"""

def get_census_dfs_loaded_html(fordbexport=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the list of currently loaded census dfs
    * 
    * parms :
    *   fordbexport  -   for db export flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("get_census_dfs_loaded_html",fordbexport)
    
    dfc_loaded_datasets_html  =   ""
    
    dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + census_loaded_to_dfs_html) 
    
    dfs_loaded  =   cfg.get_dfc_dataframes_titles_list()
    dfs_dict    =   {} 
    
    if(not(dfs_loaded) is None) :
        
        dfs_loaded.sort()
    
        for i in range(len(swcm.census_data_dirs)) : 
        
            dfs_list    =   []
        
            for j in range(len(dfs_loaded)) :
            
                if(dfs_loaded[j].find(swcm.census_data_dirs[i]) > -1 ) :
                    dfs_list.append(dfs_loaded[j])
                
            if(len(dfs_list) > 0) :
                dfs_dict.update({swcm.census_datasets[i] : dfs_list})
                
    else :
        
        row_html    =   ""
        row_html    =   (row_html + census_loaded_to_dfs_row_html)
        row_html    =   row_html.replace("XXXXDatasetID","&nbsp;")
        row_html    =   row_html.replace("XXXXfilename","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No Census df(s) currently loaded")
        
        dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + row_html) 
    
    if(swcm.DEBUG_CENSUS) :
        print("dfs_dict",dfs_dict)

    if(len(dfs_dict) == 0) :
        
        row_html    =   ""
        row_html    =   (row_html + census_loaded_to_dfs_row_html)
        row_html    =   row_html.replace("XXXXDatasetID","&nbsp;")
        row_html    =   row_html.replace("XXXXfilename","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No Census df(s) currently loaded")
        
        dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + row_html) 

    else :
        
        dfs_dict_list   =  list(dfs_dict.keys()) 
        
        for i in range(len(dfs_dict_list)) :
            
            current_dfs_list    =   dfs_dict.get(dfs_dict_list[i])
            
            if(swcm.DEBUG_CENSUS) :
                print("current_dfs_list",current_dfs_list)
            
            for j in range(len(current_dfs_list)) :
                
                row_html    =   ""
                row_html    =   (row_html + census_loaded_to_dfs_row_html)
                
                if(j==0) :
                    row_html    =   row_html.replace("XXXXDatasetID",dfs_dict_list[i])
                else :
                    row_html    =   row_html.replace("XXXXDatasetID","&nbsp;")
                    
                row_html    =   row_html.replace("XXXXdfname",current_dfs_list[j])
                
                if(fordbexport) :
                    row_html    =   row_html.replace("XXXXcallback","export_census_to_db")
                else :
                    row_html    =   row_html.replace("XXXXcallback","export_census_to_df")

                
                dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + row_html) 
            
            
    dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + census_loaded_to_dfs_end_html) 
            
    return(dfc_loaded_datasets_html)


def display_census_dfs_loaded(fordbexport=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the loaded census dfs
    * 
    * parms :
    *   NA
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    dfs_loaded_html     =   get_census_dfs_loaded_html(fordbexport) 
    dfs_loaded_note     =   get_dataset_loaded_html    
    
    gridclasses         =   ["dfc-top","dfc-bottom"]
    gridhtmls           =   [dfs_loaded_html,dfs_loaded_note]
    
    if(swcm.DEBUG_CENSUS) :
        print(dfs_loaded_html)
        print(dfs_loaded_note)
    
    print("\n")
    display_generic_grid("dfcensus-loaded-dfs-wrapper",gridclasses,gridhtmls)
    print("\n")




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               dfs Loaded Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

census_load_df_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:9%; font-size:13px; text-align:left;" class="dccolheadleft">Key Type</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Economic</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Education</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">Employment</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Insurance</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Housing</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Immigration</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Internet</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Population</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Social</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Transportation</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_load_df_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""





def get_load_datasets_html() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """
    
    print("get_load_datasets_html")
    
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + census_load_df_html)  
    
    datasets_built      =   get_datasets_processed()
    #print("datasets_built",datasets_built)

    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    #print("dataframes_loaded",dataframes_loaded)
    
    for i in range(len(datasets_built)) : 
        
        if(len(datasets_built[i]) > 0) :
            
            if(swcm.is_any_part_of_dataset_processed(i,datasets_built)) :
            
                dsid                =   swcm.census_datasets[i]
                dsid                =   dsid.replace("_"," ")
                row_html            =   census_load_df_row_html.replace("XXXTDatasetID",dsid)
                row_html            =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
            
                for j in range(4)  : 
                        
                    if(j==0)        :   
                        dftype  =   "zipcode"
                        cbdis   =   "cb1disabled"
                        cbflag  =   "cb1flag"
                            
                    elif(j==1)      :   
                        dftype  =   "cities" 
                        cbdis   =   "cb2disabled"
                        cbflag  =   "cb2flag"

                    elif(j==2)      :   
                        dftype  =   "counties" 
                        cbdis   =   "cb3disabled"
                        cbflag  =   "cb3flag"

                    elif(j==3)      :   
                        dftype  =   "states"
                        cbdis   =   "cb4disabled"
                        cbflag  =   "cb4flag"
                    
                    if(datasets_built[i][j]) :

                        if(not(dataframes_loaded is None)) :
                            
                            if((swcm.census_data_dirs[i] + "_" + dftype) in dataframes_loaded) :
                                row_html            =   row_html.replace(cbdis,"disabled") 
                                row_html            =   row_html.replace(cbflag,"checked")
                            
                            else :
                                row_html            =   row_html.replace(cbdis,"") 
                                row_html            =   row_html.replace(cbflag,"")
                                
                    else :
                        row_html            =   row_html.replace(cbdis,"disabled") 
                        row_html            =   row_html.replace(cbflag,"")
                            
                load_datasets_html  =   (load_datasets_html + row_html)  
                
            else :
                print("no part built",i)                
    
    load_datasets_html  =   (load_datasets_html + census_load_df_end_html)

    return(load_datasets_html)


def display_load_datasets() :
    """
    * -------------------------------------------------------------------------- 
    * function : display the load datasets screen
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    load_datasets_to_df_html    =   get_load_datasets_html()
    
    load_datasets_to_df_html    =   load_datasets_to_df_html.replace("Census Datasets","Census Datasets Ready To Load to df(s)")
    
    load_datasets_to_df_tb      =   ButtonGroupForm(data_load_datasets_to_df_tb_id,
                                                    data_load_datasets_to_df_tb_keyTitleList,
                                                    data_load_datasets_to_df_tb_jsList,
                                                    data_load_datasets_to_df_tb_centered)
        
    load_datasets_to_df_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":40})
    load_datasets_to_df_tb_html          =   load_datasets_to_df_tb.get_html()
    
    dsbuilt     =   False
    datasets_built      =   get_datasets_processed()
    for i in range(len(datasets_built)) :
        for j in range(len(datasets_built[i])) :
            if(datasets_built[i][j]) :
                dsbuilt     =   True

    if(dsbuilt) :
        
        load_notes  =   load_datasets_html
            
    else :
        
        load_notes  =   load_datasets_none_html
        
        load_datasets_none_tb       =   ButtonGroupForm(data_load_datasets_none_tb_id,
                                                        data_load_datasets_none_tb_keyTitleList,
                                                        data_load_datasets_none_tb_jsList,
                                                        data_load_datasets_none_tb_centered)
        
        load_datasets_none_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":95})
        load_datasets_to_df_tb_html          =   load_datasets_none_tb.get_html()
        
    gridclasses     =   ["dfc-main","dfc-footer","dfc-bottom"]
    gridhtmls       =   [load_datasets_to_df_html,load_notes,load_datasets_to_df_tb_html]
    
    
    #print(load_datasets_to_df_html)
    #print(load_notes)
    
    print("\n")
    display_generic_grid("dfcensus-load-data-wrapper",gridclasses,gridhtmls)
    print("\n")





   
"""
#--------------------------------------------------------------------------
#                   Dataset Subset Details Display objects
#--------------------------------------------------------------------------
"""

def get_dataset_columns_subdata_table_html(datasetid,excludes=None,forloadcols=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset details html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
            
    if(swcm.DEBUG_CENSUS) :
        print("get_dataset_columns_subdata_table_html",datasetid,excludes,forloadcols)
    
    load_datasets_details_table     =   ""
    
    if(not forloadcols) :
        load_datasets_details_table     =   (load_datasets_details_table + census_subdata_table_html)
    else :
        load_datasets_details_table     =   (load_datasets_details_table + load_cols_subdata_table_html)
        load_datasets_details_table     =   load_datasets_details_table.replace("XXXDatasetID",datasetid)
        
    if(not(datasetid is None)) :
        
        subdata_data        =   swcm.get_subset_data_lists(datasetid)
        
        subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
        subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
        subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]
    
        if(excludes is None) :
            excludes    =   []
            
        for i in range(len(subdatacols)) :

            if( (not (i==0)) and (not(i in excludes)) ):
            
                row_html    =   census_subdata_table_row_html
                    
                row_html    =   row_html.replace("XXXsubdatatitle",subdatacolstext[i])
                row_html    =   row_html.replace("XXXsubdatacols",str(len(subdatacols[i])))
            
                nanindices  =   swcm.get_census_subdata_indices(datasetid,i)
                total_nans  =   0
            
                for j in range(len(nanindices)) :
                    total_nans  =   total_nans + subdatacolsnans[nanindices[j]]
            
                nanpct      =   100 * (total_nans / (swcm.total_zips_count * len(nanindices)))   
                pct_str     =   '{:4.2f}'.format(nanpct)
            
                row_html    =   row_html.replace("XXXsubdatanans",pct_str + "%")
                row_html    =   row_html.replace("XXXSubDataText",subdatacolstext[i])
                row_html    =   row_html.replace("XXXSubDataID",str(i))
            
                cbid        =   "CS" + datasetid + str(i)
                row_html    =   row_html.replace("CSXXXDatasetID",cbid)
                row_html    =   row_html.replace("XXXDatasetID",datasetid)
                
                load_datasets_details_table     =   (load_datasets_details_table + row_html)
                
        if(not forloadcols) :        
            load_datasets_details_table     =   (load_datasets_details_table + census_subdata_table_html_end)
        else :
            load_datasets_details_table     =   load_datasets_details_table.replace("get_census_subData_details","get_load_cols_subData_details")
            load_datasets_details_table     =   (load_datasets_details_table + load_cols_subdata_table_end_html)
                
    else :
        load_datasets_details_table     =   (get_dataset_columns_no_datasetid_notes_html)
    

    print(load_datasets_details_table)  
    
    return(load_datasets_details_table)















"""
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
* ----------------- INSERT CENSUS DATASETS TO USER DF(S) objects -----------------------
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#                 Census Datasets in Memory to get columns from
#--------------------------------------------------------------------------
"""

census_load_col_sizes    =   [9,9,10,9,8,9,8,8,8,13]

census_datasets_to_load_to_df_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:9%; font-size:13px; text-align:left;" class="dccolheadleft">Key Type</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Economic</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Education</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">Employment</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Insurance</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Housing</th>
                                <th style=" width:9%; font-size:13px;" class="dccolhead">Immigration</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Internet</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Population</th>
                                <th style=" width:8%; font-size:13px;" class="dccolhead">Social</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Transportation</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_datasets_to_load_to_df_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

census_datasets_to_load_to_df_row_html_start ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:9%; font-size:13px; text-align:left;" class="dccolleft">XXXTKeyTypeID</td>
"""

census_datasets_to_load_to_df_row_html_col ="""
                                <td style=" width:XXXWidth%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="radioXXXDatasetIDXXXTKeyTypeID">
                                            <input type='radio' name="XXXTKeyTypeIDgroup" id="radioXXXDatasetIDXXXTKeyTypeID" onclick="select_dataset_radio('XXXDatasetID')" radioxxdisabled></input>
                                        </label>
                                    </div>
                                </td>               
"""

census_datasets_to_load_to_df_row_html_end ="""
                            </tr>
"""

def get_datasets_in_memory_html() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the get dataset columns table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """

    datasets_to_get_columns_from_html   =   ""
    datasets_to_get_columns_from_html   =   (datasets_to_get_columns_from_html + census_datasets_to_load_to_df_html)  
    
    datasets_loaded                     =   get_datasets_loaded_to_memory()
    
    if(0):#swcm.DEBUG_CENSUS) :
        print("get_datasets_in_memory_html")
        print("get_datasets_in_memory_html : datasets_loaded : \n",datasets_loaded)
        print("get_datasets_in_memory_html : census_data_dirs : \n",swcm.census_data_dirs)  
        print("get_datasets_in_memory_html : census_datasets : \n",swcm.census_datasets)  
    
    if(not(datasets_loaded is None)) :
    
        for i in range(4)  :#for i in range(len(swcm.census_data_dirs)) : 
            
            if(i==0)        :   rowtitle   =   swcm.ZIP_CODE_KEY_TITLE
            elif(i==1)      :   rowtitle   =   swcm.CITY_KEY_TITLE
            elif(i==2)      :   rowtitle   =   swcm.COUNTY_KEY_TITLE
            elif(i==3)      :   rowtitle   =   swcm.STATE_KEY_TITLE

            row_html       =   census_datasets_to_load_to_df_row_html_start.replace("XXXTKeyTypeID",rowtitle)            
                        
            for j in range(len(datasets_loaded[0])) : #for j in range(4)  : 
                    
                dsid        =   swcm.census_datasets[j]
                dsid        =   dsid.replace(" ","_")
                    
                col_html    =   census_datasets_to_load_to_df_row_html_col
                col_html    =   col_html.replace("XXXWidth",str(census_load_col_sizes[j]))
                rowtitle    =   rowtitle.replace(" ","")
                #col_html    =   col_html.replace("cbxxXXXDatasetID","cb" + str(j) + rowtitle)                    
                col_html    =   col_html.replace("XXXDatasetID",dsid) 
                col_html    =   col_html.replace("XXXTKeyTypeID",rowtitle) 
                   
                if(not (datasets_loaded[i][j])) :
                    col_html            =   col_html.replace("radioxxdisabled","disabled")
                else :
                    col_html            =   col_html.replace("radioxxdisabled","")
                        
                row_html    =   (row_html + col_html)
                        
            datasets_to_get_columns_from_html  =   (datasets_to_get_columns_from_html + row_html)
            datasets_to_get_columns_from_html  =   (datasets_to_get_columns_from_html + census_datasets_to_load_to_df_row_html_end)
    
    datasets_to_get_columns_from_html  =   (datasets_to_get_columns_from_html + census_datasets_to_load_to_df_end_html)
                    
    #if(swcm.DEBUG_CENSUS) :
    #    print(datasets_to_get_columns_from_html)

    return(datasets_to_get_columns_from_html)


def display_get_datasets_in_memory() :
    """
    * ------------------------------------------------------- 
    * function : display the get datasets or columns to insert
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("display_get_datasets_in_memory : ",datasetid,excludes,subdataid)
    
    if(any_dataframes_for_any_datasets()) :
        
        get_dataset_cols_html       =   get_datasets_in_memory_html()
        get_dataset_cols_html       =   get_dataset_cols_html.replace("Census Datasets","Census Datasets Loaded to df(s)") 
        
        get_dataset_notes_html      =   get_dataset_columns_notes_html 
            
        get_dataset_columns_tb      =   ButtonGroupForm(get_dataset_columns_tb_id,
                                                        get_dataset_columns_tb_keyTitleList,
                                                        get_dataset_columns_tb_jsList,
                                                        get_dataset_columns_tb_centered)
            
        get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":180, "left-margin":200})
        get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
    else :
            
        print("no census dfs are loaded into memory")
            
        return()
            
    
        
    get_cols_heading_html       =   "<div>Select Census Dataset(s) To Get Census Column(s) from</div><br></br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
    gridhtmls       =   [get_cols_heading_html,get_dataset_cols_html,get_dataset_notes_html,get_dataset_columns_tb_html]

    print("\n")
    display_generic_grid("dfcensus-get-cols-load-full-data-wrapper",gridclasses,gridhtmls)
    print("\n")
        


"""
#--------------------------------------------------------------------------
#                   Census Datasets to insert columns from
#--------------------------------------------------------------------------
"""

census_datasets_to_insert_cols_from_row_html_start ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
"""
                                
census_datasets_to_insert_cols_from_row_html_end ="""
                            </tr>
"""

census_datasets_to_insert_cols_from_blank_col_html ="""
                                <td style=" width:xxxwidth%; text-align:center;" class="dccolwrap"></td>
"""

census_datasets_to_insert_cols_from_details_col_html ="""
                                <td style=" width:xxwidth10%; " class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_dataset_columns('XXXDatasetID','xxid')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXxCols Subsets" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>               
"""

census_datasets_to_insert_cols_from_html ="""
        <div class='container dc-tbl-container' style='width:360px;' id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style='width:320px;'>
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style='width:320px;'>
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:32%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:12%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;Zip</br>Code</th>
                                <th style=" width:12%; font-size:13px; text-align:center;" class="dccolhead">City</th>
                                <th style=" width:19%; font-size:13px; text-align:center;" class="dccolhead">County</th>
                                <th style=" width:13%; font-size:13px; text-align:center;" class="dccolhead">&nbsp;&nbsp;US</br>State</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_datasets_to_insert_cols_from_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

census_insert_cols_col_widths   =   [12,12,19,13]
census_insert_cols_col_titles   =   [swcm.ZIP_CODE_KEY_TITLE, swcm.ZIP_CODE_KEY_TITLE, swcm.COUNTY_KEY_TITLE, swcm.STATE_KEY_TITLE ]


def get_datasets_for_insert_cols_html(datasets_to_get_columns_from) :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets to insert columns from
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """
            
    if(swcm.DEBUG_CENSUS) :
        print("get_datasets_for_insert_cols_html",datasets_to_get_columns_from) 
        
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + census_datasets_to_insert_cols_from_html)
    load_datasets_html  =   (load_datasets_html.replace("Census Datasets","Census Datasets Loaded Into Memory"))
    
    print(load_datasets_html)

    for i in range(len(swcm.census_datasets)) : 
        
        row_html            =   census_datasets_to_insert_cols_from_row_html_start
        
        dsid                =   swcm.census_datasets[i]
        dsid                =   dsid.replace("_"," ")
        row_html            =   row_html.replace("XXXTDatasetID",dsid)
            
        for j in range(len(census_insert_cols_col_widths)) :
                
            if(datasets_to_get_columns_from[j][i] == "True") :
                row_html            =   (row_html + census_datasets_to_insert_cols_from_details_col_html) 
                row_html            =   row_html.replace("xxwidth",str(census_insert_cols_col_widths[j]))
                row_html            =   row_html.replace("xxid",str(j))
                row_html            =   row_html.replace("XXXDatasetID",str(i))
                row_html            =   row_html.replace("XXXxCols",dsid + " " + census_insert_cols_col_titles[j])
                    
            else :
                row_html            =   (row_html + census_datasets_to_insert_cols_from_blank_col_html) 
                row_html            =   row_html.replace("xxwidth",str(census_insert_cols_col_widths[j]))
                    
        row_html            =   (row_html + census_datasets_to_insert_cols_from_row_html_end)        
            
        load_datasets_html  =   (load_datasets_html + row_html)
    
    load_datasets_html  =   (load_datasets_html + census_datasets_to_insert_cols_from_end_html)
    
    return(load_datasets_html)


"""
#--------------------------------------------------------------------------
#                   Census Subsets to insert columns from
#--------------------------------------------------------------------------
"""

census_subsets_to_insert_cols_from_table_html = """
                <div  style="width:480px; height:360px; overflow:auto;">
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:50%; font-size:13px; text-align:left;" class="dcleftcolhead">xxxDatasetId</br>   Subsets</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Num Cols</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Nan Pct</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Select Cols</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
census_subsets_to_insert_cols_from_table_html_end = """
                        </tbody>
                    </table>
                </div>"""

census_subsets_to_insert_cols_from_table_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:59%; font-size:13px; text-align:left;">XXXsubdatatitle</td>
                                <td style=" width:13%; font-size:13px;">XXXsubdatacols</td>
                                <td style=" width:13%; font-size:13px;">XXXsubdatanans</td>
                                <td style=" width:15%; font-size:13px;">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_cols_details('XXXDatasetID','XXXSubDataID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXSubDataText Columns" src='xxxbuttonurl' height="40px" width="109px"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>"""


cols_none_button    =   "https://rickkrasinski.github.io/dfcleanser/graphics/cols_none_button.png"
cols_all_button     =   "https://rickkrasinski.github.io/dfcleanser/graphics/cols_all_button.png"
cols_list_button    =   "https://rickkrasinski.github.io/dfcleanser/graphics/cols_list_button.png"


census_subsets_to_insert_header_html = """
        <div class='container dc-tbl-container' style='width:540px;' id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style='width:540px;'>
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title" style="padding-right:20px;">xxxDatasetID</p>
                            </div>
                            <div class="input-group-btn">
                                <p class="panel-title" style="padding-right:20px;"></br>xxxSubsetID</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""



def get_cols_subdata_table_html(datasetid,subdataid=None,height=None,width=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset details html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *   colnameid     -   column name id
    *   direction     -   scroll direction
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("\n\nget_cols_subdata_table_html",datasetid,subdataid,height,width)
    
    census_datasets_details_table     =   ""
    
    subdata_data        =   swcm.get_subset_data_lists(datasetid)
    subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
    subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]
    
    if(subdataid is None) :
        
        census_datasets_details_table     =   (census_datasets_details_table + census_subsets_to_insert_cols_from_table_html)
        census_datasets_details_table     =   (census_datasets_details_table.replace("xxxDatasetId",datasetid))
        
        if(not (height is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','height:' + str(height) + 'px;')  
        else :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','') 
                
        if(not (width is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('width:480px;','width:' + str(width) + 'px;')  
        
        #print("subdatacols",len(subdatacols))
        
        for i in range(len(subdatacols)) :

            row_html    =   census_subsets_to_insert_cols_from_table_row_html
                    
            row_html    =   row_html.replace("XXXsubdatatitle",subdatacolstext[i])
            row_html    =   row_html.replace("XXXsubdatacols",str(len(subdatacols[i])))
            
            nanindices  =   swcm.get_census_subdata_indices(datasetid,i)
            total_nans  =   0
            
            for j in range(len(nanindices)) :
                total_nans  =   total_nans + subdatacolsnans[nanindices[j]]
            
            #print("swcm.total_zips_count",i,swcm.total_zips_count,len(nanindices))
            nanpct      =   100 * (total_nans / (swcm.total_zips_count * len(nanindices)))  
            pct_str     =   '{:4.2f}'.format(nanpct)
            
            row_html    =   row_html.replace("XXXsubdatanans",pct_str + "%")
                
            row_html    =   row_html.replace("XXXDatasetID",datasetid)
            row_html    =   row_html.replace("XXXSubDataID",str(i))
            row_html    =   row_html.replace("XXXSubDataText",subdatacolstext[i])
                
            #insert_type =   swcm.current_dataset_inserting_from.get_subdata_insert_type(i-1)  
            subdata_attributes  =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(i)
            insert_type         =   subdata_attributes.get_column_insert_type()
                
            if(insert_type == "All") :
                row_html    =   row_html.replace("xxxbuttonurl",cols_all_button)
            elif(insert_type == "None") :
                row_html    =   row_html.replace("xxxbuttonurl",cols_none_button)
            else :
                row_html    =   row_html.replace("xxxbuttonurl",cols_list_button)

            census_datasets_details_table     =   (census_datasets_details_table + row_html)
        
        census_datasets_details_table     =   (census_datasets_details_table + census_subsets_to_insert_cols_from_table_html_end)

    else :
        
        census_datasets_details_table     =   get_subset_colnames_select_html(datasetid,subdataid)
        """
        
        #print("census_datasets_details_table",census_datasets_details_table)
        
        census_datasets_details_table   =   (census_datasets_details_table + census_colnames_table_html)
        
        if(not (height is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','height:' + str(height) + 'px;')  
        else :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','') 
                
        if(not (width is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('width:480px;','width:' + str(width) + 'px;')  
            
        subdata_col_names               =   subdatacols[subdataid]
        nanindices                      =   swcm.get_census_subdata_indices(datasetid,subdataid)

        rowcount    =   len(subdata_col_names)
        rowstart    =   0
        
        for i in range(rowcount) :

            row_html    =   census_colnames_table_row_html
            
            colname     =   swcm.get_colname(subdata_col_names[i+rowstart],70)
                
            row_html    =   row_html.replace("XXXcolname",colname)
            pct_str     =   '{:4.2f}'.format(100 * (subdatacolsnans[nanindices[i+rowstart]]/swcm.total_zips_count))
            row_html    =   row_html.replace("XXXcnamenans",pct_str + "%")
                                             
            census_datasets_details_table     =   (census_datasets_details_table + row_html)

        census_datasets_details_table     =   (census_datasets_details_table + census_colnames_table_html_end)
        """
    
    #print(census_datasets_details_table) 
    
    return(census_datasets_details_table)







def get_subset_colnames_select(datasetid,subdataid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset columns list
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    #if(swcm.DEBUG_CENSUS) :
    #    print("get_subset_colnames_select",datasetid,subdataid)

    subdata_data        =   swcm.get_subset_data_lists(datasetid)
    subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
    subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    #subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]
    
    subdata_col_names   =   subdatacols[subdataid]
    subdata_col_text    =   subdatacolstext[subdataid]

    #rowcount    =   len(subdata_col_names)
    #rowstart    =   0
        
    if(0):#swcm.DEBUG_CENSUS) :
        print("get_subset_colnames : subdata_col_names \n",subdata_col_names)
        print("get_subset_colnames : subdata_col_text \n",subdata_col_text)
        
    subset_col_names_list  =   ["None","All"]
    subset_col_names_vals  =   [-2,-1]  
    
    for i in range(len(subdata_col_names)) :
        subset_col_names_list.append(subdata_col_names[i])
        subset_col_names_vals.append(i)
        
    cnames          =   {"default":subset_col_names_list[0],"list": subset_col_names_list, "size" : 10,  "values" : subset_col_names_vals, "callback" : "change_subset_col_names_lists"}
    return(cnames)


def set_subdata_cols_vals(col_vals) :
    
    js_array    =   "["
    
    for i in range(len(col_vals)) :
        js_array    =   (js_array + str(col_vals[i]))
        
        if(i < (len(col_vals) -1)) :
            js_array    =   (js_array + ", ") 
        else :
            js_array    =   (js_array + "]")
        
   
    from dfcleanser.common.common_utils import run_jscript
    set_current_value_js  =   "set_select_subdata_cols(" + js_array + ");"
    run_jscript(set_current_value_js,"fail to change col stats html : ")
    
    
    
        

def get_subset_colnames_select_html(datasetid,subdataid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset select columns html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) : 
        print("get_subset_colnames_select_html ",datasetid,subdataid)
        
    from dfcleanser.common.html_widgets import InputForm
    subdata_cols_input_form = InputForm(get_subdata_cols_select_input_id,
                                        get_subdata_cols_select_input_idList,
                                        get_subdata_cols_select_input_labelList,
                                        get_subdata_cols_select_input_typeList,
                                        get_subdata_cols_select_input_placeholderList,
                                        get_subdata_cols_select_input_jsList,
                                        get_subdata_cols_select_input_reqList)
    
    selectDicts     =   []
    
    colnames_sel    =   get_subset_colnames_select(datasetid,subdataid)
    selectDicts.append(colnames_sel)
        
    get_select_defaults(subdata_cols_input_form,
                        get_subdata_cols_select_input_form[0],
                        get_subdata_cols_select_input_form[1],
                        get_subdata_cols_select_input_form[3],
                        selectDicts)
        
    subdata_cols_input_form.set_shortForm(False)
    subdata_cols_input_form.set_gridwidth(520)
    subdata_cols_input_form.set_custombwidth(127)
    subdata_cols_input_form.set_fullparms(True)
    
    #insert_type     =   swcm.current_dataset_inserting_from.get_subdata_insert_type(subdataid)
    subdata_attributes  =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
    insert_type         =   subdata_attributes.get_column_insert_type()

    if(not ((insert_type == "All") or (insert_type == "None")) ) :
        
        sub_attrs           =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
        sub_cols_list       =   sub_attrs.get_columns_list() 
        
        subdata_data        =   swcm.get_subset_data_lists(datasetid)
        subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
        subdata_col_names   =   subdatacols[subdataid]
        
        subset_col_names_str  =   ""
    
        for i in range(len(sub_cols_list)) :
        
            if(i < (len(sub_cols_list) - 1)) :
                subset_col_names_str    =   (subset_col_names_str + subdata_col_names[sub_cols_list[i]] + "\n") 
            else :
                subset_col_names_str    =   (subset_col_names_str + subdata_col_names[sub_cols_list[i]])
        
        insert_type = subset_col_names_str
        
        set_subdata_cols_vals(sub_cols_list)
        
        
        
        print("insert_type",insert_type)
        
    cfg.set_config_value(get_subdata_cols_select_input_id+"Parms",[insert_type,""])
        
    subdata_cols_input_form_html = subdata_cols_input_form.get_html() 
    
    return(subdata_cols_input_form_html)
            

"""
* --------------------------------------------------------------------------------------
* -------------------- Census Select Columns to load to df -----------------------------
* --------------------------------------------------------------------------------------
"""

def get_load_subdata_table_html(datasetid,subdataid=None,height=None,width=None,scrollbars=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get load subdata table
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *   height        -   dataset height
    *   width         -   dataset width 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("get_load_subdata_table_html",datasetid,subdataid,height,width,scrollbars)
    
    census_datasets_details_table     =   ""
    
    subdata_data        =   swcm.get_subset_data_lists(datasetid)
    subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
    subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]
    
    if(subdataid is None) :
        
        census_datasets_details_table     =   (census_datasets_details_table + census_subdata_table_html)
        
        for i in range(len(subdatacols)) :

            row_html    =   census_subdata_table_row_html
                    
            row_html    =   row_html.replace("XXXsubdatatitle",subdatacolstext[i])
            row_html    =   row_html.replace("XXXsubdatacols",str(len(subdatacols[i])))
            
            nanindices  =   swcm.get_census_subdata_indices(datasetid,i)
            total_nans  =   0
            
            for j in range(len(nanindices)) :
                total_nans  =   total_nans + subdatacolsnans[nanindices[j]]
            
            nanpct      =   100 * (total_nans / (swcm.total_zips_count * len(nanindices)))   
            pct_str     =   '{:4.2f}'.format(nanpct)
            
            row_html    =   row_html.replace("XXXsubdatanans",pct_str + "%")
            row_html    =   row_html.replace("XXXSubDataText",subdatacolstext[i])
            row_html    =   row_html.replace("XXXSubDataID",str(i))
            
            row_html    =   row_html.replace("XXXDatasetID",datasetid)
                
            census_datasets_details_table     =   (census_datasets_details_table + row_html)
        
        census_datasets_details_table     =   (census_datasets_details_table + census_subdata_table_html)

    else :
        
        
        census_datasets_details_table   =   (census_datasets_details_table + census_colnames_table_html)
        
        if(not (height is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','height:' + str(height) + 'px;')  
        else :
            census_datasets_details_table     =   census_datasets_details_table.replace('height:360px;','') 
                
        if(not (width is None)) :
            census_datasets_details_table     =   census_datasets_details_table.replace('width:480px;','width:' + str(width) + 'px;')  
            
        subdata_col_names               =   subdatacols[subdataid]
        nanindices                      =   swcm.get_census_subdata_indices(datasetid,subdataid)

        rowcount    =   len(subdata_col_names)
        rowstart    =   0
        
        if(swcm.DEBUG_CENSUS) :
            print("get_load_subdata_table_html : subdata_col_names \n",subdata_col_names)
        
        for i in range(rowcount) :

            row_html    =   census_colnames_table_row_html
            
            colname     =   swcm.get_colname(subdata_col_names[i+rowstart],70)
                
            row_html    =   row_html.replace("XXXcolname",colname)
            pct_str     =   '{:4.2f}'.format(100 * (subdatacolsnans[nanindices[i+rowstart]]/swcm.total_zips_count))
            row_html    =   row_html.replace("XXXcnamenans",pct_str + "%")
                                             
            census_datasets_details_table     =   (census_datasets_details_table + row_html)

        census_datasets_details_table     =   (census_datasets_details_table + census_colnames_table_html_end)
        
    return(census_datasets_details_table)


def get_census_datasets_details_table(datasetid,subdataid,height,width) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset columns selected html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *   height        -   dataset height
    *   width         -   dataset width 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("get_census_datasets_details_table",datasetid,subdataid,height,width)
    
    load_datasets_details_html  =   ""

    if(subdataid is None) :
        
        header_html                 =   census_load_details_html
        dsid                        =   datasetid.replace("_"," ")
        header_html                 =   header_html.replace("XXXdatasetid",dsid)
        load_datasets_details_html  =   (load_datasets_details_html + header_html) 
    
        load_datasets_details_html  =   (load_datasets_details_html + census_zip_size_head) 
            
        dsinndex    =   swcm.get_dataset_index(datasetid)
            
        zcsize      =   swcm.get_subset_size(0,dsinndex)
        citysize    =   swcm.get_subset_size(1,dsinndex)
        countysize  =   swcm.get_subset_size(2,dsinndex)
        statesize   =   swcm.get_subset_size(3,dsinndex)
        totalsize   =   swcm.get_subset_size(4,dsinndex)
        
        row_html =  census_zip_size_row_html.replace("XXXZipCodeSize",zcsize)
        row_html =  row_html.replace("XXXCitySize",citysize)
        row_html =  row_html.replace("XXXCountySize",countysize)
        row_html =  row_html.replace("XXXStateSize",statesize)
        row_html =  row_html.replace("XXXTotalSize",totalsize)
        
        load_datasets_details_html  =   (load_datasets_details_html + row_html)
        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_table_end_html)

    else :
        
        header_html                 =   census_load_details_html
        header_html                 =   header_html.replace("XXXdatasetid",swcm.get_subdata_name(datasetid,subdataid))
        load_datasets_details_html  =   (load_datasets_details_html + header_html) 
            
    if(not (height is None)) :
        load_datasets_details_html     =   load_datasets_details_html.replace('height:360px;','height:' + str(height) + 'px;')  
    else :
        load_datasets_details_html     =   load_datasets_details_html.replace('height:360px;','') 
                
    if(not (width is None)) :
        load_datasets_details_html     =   load_datasets_details_html.replace('width:480px;','width:' + str(width) + 'px;')  

    # append the details table
    load_datasets_details_html  =   (load_datasets_details_html + get_load_subdata_table_html(datasetid,subdataid,height,width))
    
    if(subdataid is None) :
        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_end_html)
    else :
        load_datasets_details_html  =   (load_datasets_details_html + census_load_subdata_end_html)     
    
    return(load_datasets_details_html)    


def get_cols_to_insert_heading_html(datasetid,subdataid) :
    
    heading_html    =   census_subsets_to_insert_header_html    
    heading_html    =   heading_html.replace("xxxDatasetID",datasetid)
    heading_html    =   heading_html.replace("xxxSubsetID",datasetid)

    return(heading_html)


def display_select_dataset_columns_to_insert(datasetid,subdataid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset columns selected html
    * 
    * parms :
    *   datasetid     -   dataset id
    *   subdataid     -   data subset id 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("\ndisplay_select_dataset_columns_to_insert",datasetid,subdataid)
    
    get_selected_cols_heading_html      =   "<div>Select Census Column(s) To Insert Into User df(s)</div><br></br>"
    
    if(subdataid is None) :
        subdataid   =   0
        swcm.current_dataset_inserting_from.set_subdatasetid(0)
    else :
        swcm.current_dataset_inserting_from.set_subdatasetid(subdataid)        
    
    columns_html                        =   get_subset_colnames_select_html(datasetid,subdataid)
    
    subdata_data                        =   swcm.get_subset_data_lists(datasetid)
    subdatacolstext                     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    columns_list_heading_html           =   "<div>" + subdatacolstext[subdataid] + " Columns</div>"
    
    if(not (subdataid is None)) :
        
        subdata_html    =   get_cols_subdata_table_html(datasetid,None,520,480)
        
        insert_cols_tb  =   ButtonGroupForm(insert_cols_tb_id,
                                            insert_cols_tb_keyTitleList,
                                            insert_cols_tb_jsList,
                                            insert_cols_tb_centered)
            
        insert_cols_tb.set_customstyle({"font-size":13, "height":75, "width":140, "left-margin":22})
        
        insert_cols_tb_html   =   insert_cols_tb.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-bottom","dfcleanser-common-grid-header-small","dfc-right"]
        gridhtmls       =   [get_selected_cols_heading_html,subdata_html,insert_cols_tb_html,columns_list_heading_html,columns_html]
    
        print("\n")
        display_generic_grid("dfcensus-show-select-cols-wrapper",gridclasses,gridhtmls)
        print("\n")

        
    else :
        
        subdata_html    =   get_cols_subdata_table_html(datasetid,subdataid,500,520)  
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [get_selected_cols_heading_html,columns_html,subdata_html]
    
        print("\n")
        display_generic_grid("dfcensus-show-selects-wrapper",gridclasses,gridhtmls)
        print("\n")




"""
#--------------------------------------------------------------------------
#                   Insert Columns into dfs objects
#--------------------------------------------------------------------------
"""
NO_USER_DFS             =   0
NO_DATASETS_LOADED      =   1


def get_census_dfs_for_dataset(datasetid) :
    
    all_dfs         =   cfg.get_dfc_dataframes_titles_list()
    census_dfs      =   []
    
    for i in range(len(all_dfs)) :
        
        if( (all_dfs[i] == datasetid.lower() + "_zipcode_df") or 
            (all_dfs[i] == datasetid.lower() + "_cities_df") or
            (all_dfs[i] == datasetid.lower() + "_counties_df") or
            (all_dfs[i] == datasetid.lower() + "_states_df") ) :
            
            census_dfs.append(all_dfs[i])
            
    return(census_dfs)


def get_non_census_dfs() :
    
    all_dfs             =   cfg.get_dfc_dataframes_titles_list()
    non_census_dfs      =   []
    
    all_census_dfs      =   []
    
    for i in range(len(swcm.census_data_dirs)) :
        
        all_census_dfs.append(swcm.census_data_dirs[i].lower() + "_zipcode_df")
        all_census_dfs.append(swcm.census_data_dirs[i].lower() + "_cities_df")
        all_census_dfs.append(swcm.census_data_dirs[i].lower() + "_counties_df")
        all_census_dfs.append(swcm.census_data_dirs[i].lower() + "_states_df")
        
    
    for i in range(len(all_dfs)) :
        
        if(not (all_dfs[i] in all_census_dfs)) :
            non_census_dfs.append(all_dfs[i])
            
    return(non_census_dfs)






def get_columns_to_insert_nan_html(datasetid,subdataid,colslist,colid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset columns to insert select display
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("get_columns_to_insert_nan_html",datasetid,subdataid,"\n",colslist)

    from dfcleanser.common.html_widgets import InputForm
    cols_to_insert_input_form = InputForm(cols_to_insert_in_df_input_id,
                                          cols_to_insert_in_df_input_idList,
                                          cols_to_insert_in_df_input_labelList,
                                          cols_to_insert_in_df_input_typeList,
                                          cols_to_insert_in_df_input_placeholderList,
                                          cols_to_insert_in_df_input_jsList,
                                          cols_to_insert_in_df_input_reqList)
    selectDicts             =   []

    select_cols_list        =   []
    select_cols_vals_list   =   []
    
    if( (len(colslist) == 1) and ((colslist[0] == -2) or (colslist[0] == -1)) ) :
        if(colslist[0] == -2) : 
            select_cols_list.append("None")
            select_cols_vals_list.append(-2)
        else :
            select_cols_list.append("All")
            select_cols_vals_list.append(-1)
    else :
        
        subdata_data        =   swcm.get_subset_data_lists(datasetid)
        subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS] 
        subdata_col_names   =   subdatacols[subdataid]
        
        for i in range(len(colslist)) :
            select_cols_list.append(subdata_col_names[colslist[i]])
            select_cols_vals_list.append(colslist[i])
    
    if(colid is None) :
        default_col     =   select_cols_list[0]
    else :
        default_col     =   select_cols_list[colid]
    
    dtypes_select           =   {"default":default_col,"list": select_cols_list, "size" : 15,  "values" : select_cols_vals_list, "callback" : "change_subset_col_selected_attrs"}
    selectDicts.append(dtypes_select) 
    
    from dfcleanser.common.common_utils import get_str_of_datatypes
    dtypes_list     =   get_str_of_datatypes()
    
    dtypes_select           =   {"default":dtypes_list[0],"list": dtypes_list, "callback" : "change_insert_col_dtype"}
    selectDicts.append(dtypes_select) 
    
    get_select_defaults(cols_to_insert_input_form,
                        cols_to_insert_in_df_input_id,
                        cols_to_insert_in_df_input_idList,
                        cols_to_insert_in_df_input_typeList,
                        selectDicts)
    
    cols_to_insert_input_form.set_shortForm(True)
    cols_to_insert_input_form.set_gridwidth(480)
    cols_to_insert_input_form.set_custombwidth(150)
    cols_to_insert_input_form.set_fullparms(True)
    
    
    subdata_attributes =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
    
    print("subdata_attributes",type(subdata_attributes),subdata_attributes)
    col_dtype          =   swcm.current_dataset_inserting_from.get_col_dtype(0)
    
    if(col_dtype is None) :
        
        dataset_dfs =   get_census_dfs_for_dataset(datasetid)
        df_ds       =   swcm.get_dfs_for_dataset(swcm.current_dataset_inserting_from.get_datasetid())
        
        ds_df_offset    =   0
        
        for i in range(len(dataset_dfs)) : 
            for j in range(len(df_ds)) :
                if(dataset_dfs[i] == df_ds[j]) :
                    ds_df_offset    =   i
        
        if(len(dataset_dfs) > 0) :
            
            df          =   cfg.get_dfc_dataframe_df(dataset_dfs[ds_df_offset])
            dfdtypes    =   df.dtypes.tolist()
            col_dtype   =   str(dfdtypes[colslist[0]])
            
        else :    
            col_dtype   =   str("TBD")
        
    col_nanvalue       =   swcm.current_dataset_inserting_from.get_col_nanvalue(0)
    if(col_nanvalue is None) :
        col_nanvalue    =   "nan"
     
    ds_dfs          =   swcm.get_dfs_for_dataset(datasetid)
    ds_dfs_loaded   =   swcm.get_datasets_loaded_to_dfs() 

    for i in range(len(ds_dfs)) :
        if(ds_dfs[i] in ds_dfs_loaded) :
            df  =   cfg.get_dfc_dataframe_df(ds_dfs[i])
            break
        
    from dfcleanser.common.common_utils import is_numeric_col
    if(is_numeric_col(df,default_col)) :        
        minval      =   str(df[default_col].min())    
        maxval      =   str(df[default_col].max())
    else :
        minval      =   "NA"    
        maxval      =   "NA"
   
    cfg.set_config_value(cols_to_insert_in_df_input_id+"Parms",[select_cols_list[0],str(minval),str(maxval),str(col_dtype),dtypes_list[0],str(col_nanvalue),""]) 
    cfg.set_config_value(cols_to_insert_in_df_input_id+"ParmsProtect",[False,True,True,False,False,False,False]) 
    
    cols_to_insert_input_html  =   cols_to_insert_input_form.get_html()
    
    return(cols_to_insert_input_html)



"""
#--------------------------------------------------------------------------
#                   Insert Columns Stats Objects
#--------------------------------------------------------------------------
"""
census_subsets_to_insert_cols_stats_table_html = """
                <div  style="width:480px; overflow:auto;">
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:70%; font-size:13px; text-align:left;" class="dcleftcolhead">xxxDatasetId</br>   Subsets</th>
                                <th style=" width:30%; font-size:13px;" class="dccolhead">Num Cols</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
census_subsets_to_insert_cols_stats_table_html_end = """
                        </tbody>
                    </table>
                </div>"""

census_subsets_to_insert_cols_stats_table_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:70%; font-size:13px; text-align:left;">XXXsubdatatitle</td>
                                <td style=" width:30%; font-size:13px;">XXXsubdatacols</td>
                            </tr>"""


def get_subdata_to_insert_table_html() :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset coluns count
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    datasetid           =   swcm.current_dataset_inserting_from.get_datasetid()
    
    subdata_data        =   swcm.get_subset_data_lists(datasetid)
    subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
    subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    
    census_datasets_details_table   =   ""
    
    census_datasets_details_table     =   (census_datasets_details_table + census_subsets_to_insert_cols_stats_table_html)
    census_datasets_details_table     =   (census_datasets_details_table.replace("xxxDatasetId",datasetid))

    total_cols  =   0
        
    for i in range(len(subdatacols)) :

        row_html        =   census_subsets_to_insert_cols_stats_table_row_html
        row_html        =   row_html.replace("XXXsubdatatitle",subdatacolstext[i])
        
        current_attrs   =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(i)
        
        insert_type     =   current_attrs.get_column_insert_type()
        
        if(insert_type == "All") :
            num_cols    =   len(subdatacols[i])
        elif(insert_type == "None") :
            num_cols    =   0
        else :

            cols_list   =   current_attrs.get_columns_list() 
            num_cols    =   len(cols_list)
        
        row_html    =   row_html.replace("XXXsubdatacols",str(num_cols))
        total_cols  =   (total_cols + num_cols)
            
        census_datasets_details_table     =   (census_datasets_details_table + row_html)
        
    row_html    =   census_subsets_to_insert_cols_stats_table_row_html
    row_html    =   row_html.replace("XXXsubdatatitle","Total Columns To Insert Into User df(s)")
    row_html    =   row_html.replace("XXXsubdatacols",str(total_cols))
    
    census_datasets_details_table     =   (census_datasets_details_table + row_html)
        
    census_datasets_details_table     =   (census_datasets_details_table + census_subsets_to_insert_cols_stats_table_html_end)
    
    #print(census_datasets_details_table)
    
    return(census_datasets_details_table)    



def display_columns_to_insert_dfs(census_df=None,user_df=None,keys=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get user dataframes to insert columns into
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    datasetid   =   swcm.current_dataset_inserting_from.get_datasetid()

    if(swcm.DEBUG_CENSUS) :
        print("display_columns_to_insert_dfs",datasetid)
    
    stats_table_html    =   get_subdata_to_insert_table_html()
    
    from dfcleanser.common.html_widgets import InputForm
    insert_cols_in_df_input_form = InputForm(insert_cols_in_df_input_id,
                                             insert_cols_in_df_input_idList,
                                             insert_cols_in_df_input_labelList,
                                             insert_cols_in_df_input_typeList,
                                             insert_cols_in_df_input_placeholderList,
                                             insert_cols_in_df_input_jsList,
                                             insert_cols_in_df_input_reqList)
    selectDicts         =   []
    
    dfs_in_memory       =   get_datasets_loaded_to_memory()
    
    dfs_to_load_from    =   [" "]   
    
    for i in range(len(dfs_in_memory)) :
        if(dfs_in_memory[i][swcm.get_dataset_index(datasetid)]) :
            dfs_to_load_from.append(swcm.census_data_dirs[swcm.get_dataset_index(datasetid)] + "_" + swcm.index_fnames[i] + "_df")

    if(census_df == None) :
        default_df  =   " "
    else :
        default_df  =   census_df

    dfs_to_load_from_select     =   {"default":default_df,"list": dfs_to_load_from, "callback" : "change_census_df"}
    selectDicts.append(dfs_to_load_from_select)
    
    user_dfs        =   get_user_dfs(datasetid)
    user_df_list    =   [" "]
    
    for i in range(len(user_dfs)) :
        user_df_list.append(user_dfs[i])
        
    if(user_df == None) :
        default_user_df     =   " "
    else :
        default_user_df     =   user_df
    
    user_dfs_select     =   {"default":default_user_df,"list": user_df_list, "callback" : "change_user_df"}
    selectDicts.append(user_dfs_select)
    
    
    if(user_df == None) :
        
        user_df_cols            =   [" "]
        
    else :
        
        df              =   cfg.get_dfc_dataframe_df(user_df)
        user_df_cols    =   list(df.columns)
    
    user_df_cols_select     =   {"default":user_df_cols[0],"list": user_df_cols, "callback" : "change_user_df_col"}
    selectDicts.append(user_df_cols_select)
    
    get_select_defaults(insert_cols_in_df_input_form,
                        insert_cols_in_df_input_id,
                        insert_cols_in_df_input_idList,
                        insert_cols_in_df_input_typeList,
                        selectDicts)
    
    insert_cols_in_df_input_form.set_shortForm(True)
    insert_cols_in_df_input_form.set_gridwidth(480)
    insert_cols_in_df_input_form.set_custombwidth(119)
    insert_cols_in_df_input_form.set_fullparms(True)
    
    if(keys  is None) :
        
        if(not (default_df == " ")) :
            keys   =   swcm.get_index_keys_for_census_df(default_df,True)
            
        else :
            keys    =   ""
    
    cfg.set_config_value(insert_cols_in_df_input_id+"Parms",[default_df,default_df,default_user_df,default_user_df,user_df_cols[0],keys])
                         
    insert_cols_in_df_input_html  =   insert_cols_in_df_input_form.get_html()
    
    insert_cols_heading_html      =   "<div>Insert Census Column(s) Into User df(s)</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [insert_cols_heading_html,stats_table_html,insert_cols_in_df_input_html]
    
    print("\n")
    display_generic_grid("dfcensus-insert-cols-df-wrapper",gridclasses,gridhtmls)
    print("\n")






def display_columns_to_insert(datasetid,subdataid,colslist,colid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset columns to insert
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    #datasetid           =   swcm.current_dataset_inserting_from.get_datasetid()
    #subsetid            =   cfg.get_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)
    
    if(swcm.DEBUG_CENSUS) :
        print("display_columns_to_insert",datasetid,subdataid,"\n",colslist)
    
    subdata_html    =   get_cols_subdata_table_html(datasetid,None,520,480)
    
    #print(subdata_html)
    cols_list_html  =   get_columns_to_insert_nan_html(datasetid,subdataid,colslist,colid)
    
    columns_list_heading_html           =   "<div> Selected Column(s) Attributes</div>"    
    get_selected_cols_heading_html      =   "<div>Select Census Column(s) To Insert Into User df(s)</div><br></br>"
            
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfcleanser-common-grid-header-small","dfc-right"]
    gridhtmls       =   [get_selected_cols_heading_html,subdata_html,columns_list_heading_html,cols_list_html]
    
    print("\n")
    display_generic_grid("dfcensus-show-selects-attrs-wrapper",gridclasses,gridhtmls)
    print("\n")











"""
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
* ------------------ EXPORT CENSUS DF(S) objects -----------------------
* --------------------------------------------------------------------------------------
* --------------------------------------------------------------------------------------
"""

census_export_dfs_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:37%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:14%; font-size:13px;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_df_from_census('XXXsubsetID1')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXsubsetID1" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>               
                                <td style=" width:14%; " class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_df_from_census('XXXsubsetID2')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXsubsetID2" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>               
                                <td style=" width:21%; text-align:center;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_df_from_census('XXXsubsetID3')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXsubsetID3" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>               
                                <td style=" width:14%; " class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_df_from_census('XXXsubsetID4')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXsubsetID4" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>               
                            </tr>
"""






LOAD_DFC_DFS            =   0
EXPORT_DFC_DFS          =   1
EXPORT_TO_DC            =   2



census_export_dfs_row_start_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:37%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>
"""

census_export_dfs_row_html ="""
                                <td style=" width:XXXWidth%; font-size:13px;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_df_from_census('XXXsubsetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="export XXXsubsetID" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df.png' height="20px" width="20px" id="CXXXsubsetID"></img>
                                        </a>
                                    </div>
                                </td>"""
                                
census_export_dfs_to_db_row_html ="""
                                <td style=" width:XXXWidth%; font-size:13px;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="export_to_db_from_census('XXXsubsetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="load XXXsubsetID to db" src='https://rickkrasinski.github.io/dfcleanser/graphics/export_df_to_db.png' height="20px" width="20px" id="CXXXsubsetID"></img>
                                        </a>
                                    </div>
                                </td>"""

census_export_no_dfs_row_html ="""
                                <td style=" width:XXXWidth%; font-size:13px;" class="dccolwrap"></td>"""

census_export_dfs_row_end_html ="""
                            </tr>
"""


def get_datasets_to_export_html(to_db=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the export of dfs
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :
        print("get_datasets_to_export_html",to_db)
    
    datasets_to_export_html     =   ""
    datasets_to_export_html     =   (datasets_to_export_html + census_no_details_download_html)  

    datasets_loaded_to_dfs      =   swcm.get_datasets_loaded_to_dfs()
    
    for i in range(len(swcm.census_datasets)) : 
    
        row_html    =   census_export_dfs_row_start_html  
        row_html    =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
        
        for j in range(4) :
                
            if(datasets_loaded_to_dfs[i][j]) :
                
                if(to_db) :
                    row_html    =   (row_html + census_export_dfs_to_db_row_html)
                else :
                    row_html    =   (row_html + census_export_dfs_row_html) 
                
                if((j==2)) :
                    row_html    =   row_html.replace("XXXWidth","21")  
                else :
                    row_html    =   row_html.replace("XXXWidth","14")
                
                subsetid    =   swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j)
                row_html    =   row_html.replace('CXXXsubsetID',subsetid + "id")                
                row_html    =   row_html.replace('XXXsubsetID',subsetid)
                    
            else :
                
                row_html    =   (row_html + census_export_no_dfs_row_html)
                
                if((j==2)) :
                    row_html    =   row_html.replace("XXXWidth","21")  
                else :
                    row_html    =   row_html.replace("XXXWidth","14")
                    
        row_html    =   (row_html + census_export_dfs_row_end_html)
        datasets_to_export_html  =   (datasets_to_export_html + row_html)
    
    datasets_to_export_html  =   (datasets_to_export_html + census_no_details_download_end_html)
    
    return(datasets_to_export_html)


def display_datasets_to_export() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("display_datasets_to_export")    

    export_dfs_html             =   get_datasets_to_export_html()
    
    export_dfs_html             =   export_dfs_html.replace('Census Datasets','Datasets To Export')
    export_dfs_html             =   export_dfs_html.replace("dc-tbl-container' style='width:360px;","dc-tbl-container' style='width:540px;")
    export_dfs_html             =   export_dfs_html.replace('width:360px;','width:540px;')

    export_dfs_heading_html     =   "<div>Export Census df(s)</div><br>"
    
    datasets_loaded_to_dfs      =   swcm.get_datasets_loaded_to_dfs()
    dataset_loaded_to_df        =   False
    
    for i in range(len(datasets_loaded_to_dfs)) :
        for j in range(4) :
            if(datasets_loaded_to_dfs[i][j]) :
                dataset_loaded_to_df    =   True    

    if(dataset_loaded_to_df) :
        export_dfs_notes_html       =   export_dfs_notes_info_html
    else :
        export_dfs_notes_html       =   no_export_dfs_notes_info_html
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
    gridhtmls       =   [export_dfs_heading_html,export_dfs_html,export_dfs_notes_html]
        
    print("\n")
    display_generic_grid("dfcensus-datasets-to-export-wrapper",gridclasses,gridhtmls)
    print("\n")


def display_datasets_to_load_to_db() :
    """
    * -------------------------------------------------------------------------- 
    * function : get html for the load datasets table
    * 
    * parms :
    *
    * returns : 
    *  html
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("display_datasets_to_load_to_db")    

    export_dfs_html             =   get_datasets_to_export_html(True)
    
    export_dfs_html             =   export_dfs_html.replace('Census Datasets','Datasets To Load To db')
    export_dfs_html             =   export_dfs_html.replace("dc-tbl-container' style='width:360px;","dc-tbl-container' style='width:540px;")
    export_dfs_html             =   export_dfs_html.replace('width:360px;','width:540px;')
    
    export_dfs_heading_html     =   "<div>Load Census df(s) to db(s)</div><br>"
    
    datasets_loaded_to_dfs      =   swcm.get_datasets_loaded_to_dfs()
    dataset_loaded_to_df        =   False
    
    for i in range(len(datasets_loaded_to_dfs)) :
        for j in range(4) :
            if(datasets_loaded_to_dfs[i][j]) :
                dataset_loaded_to_df    =   True    

    if(dataset_loaded_to_df) :
        export_dfs_notes_html       =   load_to_db_notes_info_html
    else :
        export_dfs_notes_html       =   no_load_to_db_notes_info_html

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer"]
    gridhtmls       =   [export_dfs_heading_html,export_dfs_html,export_dfs_notes_html]
        
    print("\n")
    display_generic_grid("dfcensus-datasets-to-export-wrapper",gridclasses,gridhtmls)
    print("\n")
























selected_columns_table_html = """
        <div class='dc-tbl-container' style="width:360px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:360px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;  font-size:15px;">Columns Selected To Add To df</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="width:360px;">
                    <table class="table dc-table">
                        <thead>
                        </thead>
                        <tbody>
"""

selected_columns_dataset_row_html = """
                            <tr class="dcrowhead"  style="color: white; background-color:#6FA6DA;">
                                <td style=" width:60%; font-size:12px; text-align:left;" class="dcleftcolhead">&nbsp;&nbsp;XXXXDATASET Subsets</td>
                                <td style=" width:20%; font-size:12px; text-align:center;" class="dccolhead">Columns</br>Count</td>
                                <td style=" width:20%; font-size:12px; text-align:center;" class="dccolhead">Columns</br>Details</td>
                            </tr>
"""

selected_columns_subset_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:60%; font-size:12px; text-align:left;">&nbsp;&nbsp;&nbsp;&nbsp;XXXXSUBSET</td>
                                <td style=" width:20%; font-size:11px; text-align:center;">XXXXSUBSETCOUNT</td>
                                <td style=" width:20%; font-size:11px; text-align:center;">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_select_cols_subData_details('XXXXDATASETID','XXXXSUBSETID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXXSUBSETTITLE" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="15px" width="15px"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>
"""
                        
selected_columns_table_html_end = """
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

selected_columns_blank_line_html = """
                            <tr>
                                <td style=" width:60%; font-size:11px; text-align:left;">&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td style=" width:20%; font-size:11px; text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td style=" width:20%; font-size:11px;">&nbsp;&nbsp;&nbsp;&nbsp;</td>
                            </tr>
"""

selected_columns_no_selects_html = """
                            <tr>
                                <td style=" width:60%; font-size:11px; text-align:left;">No columns selected to load in df(s)</td>
                                <td style=" width:20%; font-size:11px; text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td style=" width:20%; font-size:11px;">&nbsp;&nbsp;&nbsp;&nbsp;</td>
                            </tr>
"""



    

















    




    