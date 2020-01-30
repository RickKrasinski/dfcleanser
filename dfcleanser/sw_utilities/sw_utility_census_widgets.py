"""
# sw_utility_census_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue June 6 22:00:00 2019

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp

import dfcleanser.sw_utilities.sw_utility_census_model as swcm
import dfcleanser.sw_utilities.sw_utility_census_control as swcc

from dfcleanser.common.html_widgets import (ButtonGroupForm, maketextarea)

from dfcleanser.common.common_utils import (display_generic_grid, get_select_defaults)

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

census_tb_keyTitleList            =   ["Build</br>Census Data",
                                       "Configure</br>Census Data",
                                       "Load</br>Census Data</br>to df(s)",
                                       "Load</br>Census Data</br>to db(s)",
                                       "Get Census</br>Column</br>for df",
                                       "Clear","Reset","Help"]

census_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_DATA_TO_DB)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                       "process_pop_up_cmd(6)",
                                       "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

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
#    dfcensus data download task bar
#--------------------------------------------------------------------------
"""
data_download_tb_doc_title               =   "Census Data Download"
data_download_tb_title                   =   "Census Data Download"
data_download_tb_id                      =   "censusdatadownload"

data_download_tb_keyTitleList            =   ["Build</br>Selected</br>Datasets",
                                              "Clear","Return","Help"]

data_download_tb_jsList                  =   ["get_census_callback("+str(swcm.PROCESS_DOWNLOAD_CENSUS_DATA)+")",
                                              "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                              "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                              "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_download_tb_centered                =   True

"""
#--------------------------------------------------------------------------
#    dfcensus confirm data download task bar
#--------------------------------------------------------------------------
"""
data_confirm_download_tb_doc_title               =   "Census Confirm Data Download"
data_confirm_download_tb_title                   =   "Census Confirm Data Download"
data_confirm_download_tb_id                      =   "censusconfirmdatadownload"

data_confirm_download_tb_keyTitleList            =   ["Verify Census Zip Files</br>Are Downloaded",
                                                      "Return"]

data_confirm_download_tb_jsList                  =   ["get_census_callback("+str(swcm.VERIFY_DOWNLOAD_CENSUS_DATA)+")",
                                                      "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")"]

data_confirm_download_tb_centered                =   True

"""
#--------------------------------------------------------------------------
#    dfcensus confirm data download task bar
#--------------------------------------------------------------------------
"""
data_confirm_download_complete_tb_doc_title               =   "Census Confirm Data Download Complete"
data_confirm_download_complete_tb_title                   =   "Census Confirm Data Download Complete"
data_confirm_download_complete_tb_id                      =   "censusconfirmdatadownloadcomplete"

data_confirm_download_complete_tb_keyTitleList            =   ["Process Downloaded</br>Census Zip Files",
                                                               "Return"]

data_confirm_download_complete_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_PROCESSED_ZIP_FILES)+")",
                                                               "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")"]

data_confirm_download_complete_tb_centered                =   True

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

data_configure_tb_keyTitleList            =   ["Configure</br>Selected</br>Dataset",
                                               "Clear","Return","Help"]

data_configure_tb_jsList                  =   ["get_census_callback("+str(swcm.PROCESS_CONFIGURE_CENSUS_DATA)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                               "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                               "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_configure_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure no datasets task bar
#--------------------------------------------------------------------------
"""
data_configure_no_datasets_tb_title                   =   "Census Data Configure None"
data_configure_no_datasets_tb_title                   =   "Census Data Configure None"
data_configure_no_datasets_tb_id                      =   "censusdataconfigurenone"

data_configure_no_datasets_tb_keyTitleList            =   ["Configure</br>Datasets",
                                                           "Return","Help"]

data_configure_no_datasets_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_configure_no_datasets_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus configure verification task bar
#--------------------------------------------------------------------------
"""
data_configure_verify_tb_doc_title               =   "Census Data Verify"
data_configure_verify_tb_title                   =   "Census Data Verify"
data_configure_verify_tb_id                      =   "censusdataverify"

data_configure_verify_tb_keyTitleList            =   ["Configure</br>Selected</br>Datasets",
                                                      "Clear","Return","Help"]

data_configure_verify_tb_jsList                  =   ["get_census_callback("+str(swcm.DROP_CENSUS_DATA)+")",
                                                      "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                                      "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                      "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_configure_verify_tb_centered                =   True





   
"""
#--------------------------------------------------------------------------
#    dfcensus process data load task bar
#--------------------------------------------------------------------------
"""
data_process_load_tb_doc_title               =   "Census Confirm Data Load"
data_process_load_tb_title                   =   "Census Confirm Data Load"
data_process_load_tb_id                      =   "censusconfirmdataload"

data_process_load_tb_keyTitleList            =   ["Process Downloaded</br>Census Zip Files",
                                                  "Return"]

data_process_load_tb_jsList                  =   ["get_census_callback("+str(swcm.PROCESS_DOWNLOADED_ZIP_FILES)+")",
                                                  "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")"]

data_process_load_tb_centered                =   True


"""
#--------------------------------------------------------------------------
#    dfcensus process data load complete task bar
#--------------------------------------------------------------------------
"""
data_process_load_complete_tb_doc_title               =   "Census Confirm Data Load"
data_process_load_complete_tb_title                   =   "Census Confirm Data Load"
data_process_load_complete_tb_id                      =   "censusconfirmdataload"

data_process_load_complete_tb_keyTitleList            =   ["Configure</br>Census Data",
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

data_load_datasets_to_df_tb_keyTitleList              =   ["Load</br>Census</br>Data to df(s)",
                                                           "Clear","Return","Help"]

data_load_datasets_to_df_tb_jsList                    =   ["get_census_callback("+str(swcm.PROCESS_LOAD_CENSUS_DATA_TO_DF)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_load_datasets_to_df_tb_centered                  =   True


"""
#--------------------------------------------------------------------------
#    dfcensus load datasets to db task bar
#--------------------------------------------------------------------------
"""
data_load_datasets_to_db_tb_doc_title                 =   "Census Confirm Data Load"
data_load_datasets_to_db_tb_title                     =   "Census Confirm Data Load"
data_load_datasets_to_db_tb_id                        =   "censusdfload"

data_load_datasets_to_db_tb_keyTitleList              =   ["Load</br>Census</br>Data to db(s)",
                                                          "Clear","Return","Help"]

data_load_datasets_to_db_tb_jsList                    =   ["get_census_callback("+str(swcm.PROCESS_LOAD_CENSUS_DATA_TO_DB)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                                           "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                           "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

data_load_datasets_to_db_tb_centered                  =   True


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

get_dataset_columns_tb_keyTitleList                 =   ["Return","Help"]

get_dataset_columns_tb_jsList                       =   ["get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_dataset_columns_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get columns select subdata tb
#--------------------------------------------------------------------------
"""
get_dataset_columns_no_df_tb_doc_title              =   "Census Confirm Data Load"
get_dataset_columns_no_df_tb_title                  =   "Census Confirm Data Load"
get_dataset_columns_no_df_tb_id                     =   "censusdfload"

get_dataset_columns_no_df_tb_keyTitleList           =   ["Load</br>Census</br>Data to df(s)",
                                                         "Return","Help"]

get_dataset_columns_no_df_tb_jsList                 =   ["get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_DATA)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_dataset_columns_no_df_tb_centered               =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get subdata list tb
#--------------------------------------------------------------------------
"""
get_subdata_columns_tb_doc_title                    =   "Census Confirm Data Load"
get_subdata_columns_tb_title                        =   "Census Confirm Data Load"
get_subdata_columns_tb_id                           =   "censusdfload"

get_subdata_columns_tb_keyTitleList                 =   ["Clear","Return","Help"]

get_subdata_columns_tb_jsList                       =   ["get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_subdata_columns_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#    dfcensus get col names list tb
#--------------------------------------------------------------------------
"""
get_col_names_list_tb_doc_title                    =   "Census Confirm Data Load"
get_col_names_list_tb_title                        =   "Census Confirm Data Load"
get_col_names_list_tb_id                           =   "censusdfload"

get_col_names_list_tb_keyTitleList                 =   ["Get </br>Columns","Clear","Return","Help"]

get_col_names_list_tb_jsList                       =   ["get_census_callback("+str(swcm.PROCESS_COLS_SUBDATA_DETAILS)+")",
                                                        "get_census_callback("+str(swcm.DISPLAY_COLS_SUBDATA_DETAILS)+")",
                                                         "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_col_names_list_tb_centered                     =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   get census columns input 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   zip codes 
#--------------------------------------------------------------------------
"""
get_census_cols_input_title                     =   "Get Census Columns"
get_census_cols_input_id                        =   "dcdfcensusgetcolsinput"
get_census_cols_input_idList                    =   ["swcgetcolsdataframe",
                                                     "swcgetcolsdfzipcodecolumn",
                                                     "swcgetcolscolnames",
                                                     "swcgetcolsdfnafill",
                                                     None,None,None,None]

get_census_cols_input_labelList                 =   ["dataframe_to_add_to",
                                                     "zip_code_column",
                                                     "census_column_names_list",
                                                     "na_fill_value",
                                                     "Add</br>Column(s)</br>to df",
                                                     "Clear","Return","Help"]

get_census_cols_input_typeList                  =   ["select","select",maketextarea(6),"text",
                                                     "button","button","button","button"]

get_census_cols_input_placeholderList           =   ["dataframe to add columns to",
                                                     "dataframe zipcode column",
                                                     "census column names list",
                                                     "nan fill value",
                                                     None,None,None,None]

get_census_cols_input_jsList                    =   [None,None,None,None,
                                                     "get_census_cols(0)",
                                                     "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                                     "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                     "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_census_cols_input_reqList                   =   [0,1,2,3]

get_census_cols_input_form                      =   [get_census_cols_input_id,
                                                     get_census_cols_input_idList,
                                                     get_census_cols_input_labelList,
                                                     get_census_cols_input_typeList,
                                                     get_census_cols_input_placeholderList,
                                                     get_census_cols_input_jsList,
                                                     get_census_cols_input_reqList]  

"""
#--------------------------------------------------------------------------
#   cities 
#--------------------------------------------------------------------------
"""
get_city_census_cols_input_title                =   "Get Census Columns"
get_city_census_cols_input_id                   =   "dcdfcensusgetcolscityinput"
get_city_census_cols_input_idList               =   ["swcgetcolscitydataframe",
                                                     "swcgetcolscitydfcitycolumn",
                                                     "swcgetcolscitydfstatecolumn",
                                                     "swcgetcolscitycolnames",
                                                     "swcgetcolscitydfnafill",
                                                     None,None,None,None]

get_city_census_cols_input_labelList            =   ["dataframe_to_add_to",
                                                     "city_column",
                                                     "state_column",
                                                     "census_column_names_list",
                                                     "na_fill_value",
                                                     "Add</br>Column(s)</br>to df",
                                                     "Clear","Return","Help"]

get_city_census_cols_input_typeList             =   ["select","select","select",maketextarea(6),"text",
                                                     "button","button","button","button"]

get_city_census_cols_input_placeholderList      =   ["dataframe to add columns to",
                                                     "dataframe city column",
                                                     "dataframe state column",
                                                     "census column names list",
                                                     "nan fill value",
                                                     None,None,None,None]

get_city_census_cols_input_jsList               =   [None,None,None,None,None,
                                                     "get_census_cols(1)",
                                                     "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                                     "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                     "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_city_census_cols_input_reqList              =   [0,1,2,3,4]

get_city_census_cols_input_form                 =   [get_city_census_cols_input_id,
                                                     get_city_census_cols_input_idList,
                                                     get_city_census_cols_input_labelList,
                                                     get_city_census_cols_input_typeList,
                                                     get_city_census_cols_input_placeholderList,
                                                     get_city_census_cols_input_jsList,
                                                     get_city_census_cols_input_reqList]  

"""
#--------------------------------------------------------------------------
#   counties 
#--------------------------------------------------------------------------
"""
get_county_census_cols_input_title              =   "Get Census Columns"
get_county_census_cols_input_id                 =   "dcdfcensusgetcolscountyinput"
get_county_census_cols_input_idList             =   ["swcgetcolscountydataframe",
                                                     "swcgetcolscountydfcountycolumn",
                                                     "swcgetcolscountydfstatecolumn",
                                                     "swcgetcolscountycolnames",
                                                     "swcgetcolscountydfnafill",
                                                     None,None,None,None]

get_county_census_cols_input_labelList          =   ["dataframe_to_add_to",
                                                     "county_column",
                                                     "state_column",
                                                     "census_column_names_list",
                                                     "na_fill_value",
                                                     "Add</br>Column(s)</br>to df",
                                                     "Clear","Return","Help"]

get_county_census_cols_input_typeList           =   ["select","select","select",maketextarea(6),"text",
                                                     "button","button","button","button"]

get_county_census_cols_input_placeholderList    =   ["dataframe to add columns to",
                                                     "dataframe county column",
                                                     "dataframe state column",
                                                     "census column names list",
                                                     "nan fill value",
                                                     None,None,None,None]

get_county_census_cols_input_jsList             =   [None,None,None,None,None,
                                                     "get_census_cols(2)",
                                                     "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                                     "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                     "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_county_census_cols_input_reqList            =   [0,1,2,3,4]

get_county_census_cols_input_form               =   [get_county_census_cols_input_id,
                                                     get_county_census_cols_input_idList,
                                                     get_county_census_cols_input_labelList,
                                                     get_county_census_cols_input_typeList,
                                                     get_county_census_cols_input_placeholderList,
                                                     get_county_census_cols_input_jsList,
                                                     get_county_census_cols_input_reqList]  


"""
#--------------------------------------------------------------------------
#   states 
#--------------------------------------------------------------------------
"""
get_states_census_cols_input_title              =   "Get Census Columns"
get_states_census_cols_input_id                 =   "dcdfcensusgetcolsstatesinput"
get_states_census_cols_input_idList             =   ["swcgetcolsstatesdataframe",
                                                     "swcgetcolsstatesdfstatecolumn",
                                                     "swcgetcolsstatescolnames",
                                                     "swcgetcolsstatesdfnafill",
                                                     None,None,None,None]

get_states_census_cols_input_labelList          =   ["dataframe_to_add_to",
                                                     "state_column",
                                                     "census_column_names_list",
                                                     "na_fill_value",
                                                     "Add</br>Column(s)</br>to df",
                                                     "Clear","Return","Help"]

get_states_census_cols_input_typeList           =   ["select","select",maketextarea(6),"text",
                                                     "button","button","button","button"]

get_states_census_cols_input_placeholderList    =   ["dataframe to add columns to",
                                                     "dataframe state column",
                                                     "census column names list",
                                                     "nan fill value",
                                                     None,None,None,None]

get_states_census_cols_input_jsList             =   [None,None,None,None,
                                                     "get_census_cols(3)",
                                                     "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
                                                     "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                     "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

get_states_census_cols_input_reqList            =   [0,1,2,3]

get_states_census_cols_input_form               =   [get_states_census_cols_input_id,
                                                     get_states_census_cols_input_idList,
                                                     get_states_census_cols_input_labelList,
                                                     get_states_census_cols_input_typeList,
                                                     get_states_census_cols_input_placeholderList,
                                                     get_states_census_cols_input_jsList,
                                                     get_states_census_cols_input_reqList]  

SWUtility_census_inputs                         =   [get_census_cols_input_id, get_city_census_cols_input_id, get_county_census_cols_input_id, get_states_census_cols_input_id]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                     census data display html
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#                   Census Download Datasets html
#--------------------------------------------------------------------------
"""

census_download_html ="""
        <div class='container dc-tbl-container' style="width:360px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:360px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:360px;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:22%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">&nbsp;Zip</br>Code</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">City</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">County</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">&nbsp;&nbsp;US</br>State</th>
                                <th style=" width:10%; font-size:13px;" class="dccolhead">All</th>
                                <th style=" width:13%; font-size:13px; text-align:center;" class="dccolhead"></th>
                            </tr>
                        </thead>
                        <tbody>
"""


census_download_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


census_download_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:22%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:10%; font-size:13px;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb1XXXDatasetID">
                                            <input type='checkbox' id="cb1XXXDatasetID" onclick="set_census_cbs('cb1XXXDatasetID')" cb1flag cb1disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:10%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb2XXXDatasetID">
                                            <input type='checkbox' style="text-align:center" id="cb2XXXDatasetID" onclick="set_census_cbs('cb2XXXDatasetID')" cb2flag cb2disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:15%; text-align:center;" class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb3XXXDatasetID">
                                            <input  type='checkbox' id="cb3XXXDatasetID" onclick="set_census_cbs('cb3XXXDatasetID')" cb3flag cb3disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:10%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb4XXXDatasetID">
                                            <input type='checkbox' id="cb4XXXDatasetID" onclick="set_census_cbs('cb4XXXDatasetID')" cb4flag cb4disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:10%; " class="dccolwrap">
                                    <div class='row text-left' style='margin: 0px auto; text-align:center;'>
                                        <label class='btn' style='font-family:arial; font-size:13px;' for="cb5XXXDatasetID">
                                            <input type='checkbox' id="cb5XXXDatasetID" onclick="set_census_cbs('cb5XXXDatasetID')" cb5flag cb5disabled></input>
                                        </label>
                                    </div>
                                </td>               
                                <td style=" width:13%; text-align:center;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_dataset_details('XXXDatasetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXTDatasetID Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>
"""

"""
#--------------------------------------------------------------------------
#                  Census Subset Table html
#--------------------------------------------------------------------------
"""

census_subdata_table_html = """
                <div style="background-color:#F8F5E1;">
                    <br>
                </div>
                <div style="width:480px;">
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

load_cols_subdata_table_html = """
        <div class='container dc-tbl-container' style="width:540px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:540px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">XXXDatasetID Datasets</p>
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
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Details</th>
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
                        
                        
                        

"""
#--------------------------------------------------------------------------
#                  Configure Subset Table html
#--------------------------------------------------------------------------
"""

configure_subdata_table_html = """
                <div style="background-color:#F8F5E1;">
                    <br>
                </div>
                <div style="width:480px;">
                    <table class="table dc-table">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:59%; font-size:13px; text-align:left;" class="dcleftcolhead">Subset</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Num Cols</th>
                                <th style=" width:13%; font-size:13px;" class="dccolhead">Nan Pct</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Details</th>
                            </tr>
                        </thead>
                        <tbody>"""
                        
configure_subdata_table_html_end = """
                        </tbody>
                    </table>
                </div>"""

configure_subdata_table_row_html = """
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:59%; font-size:13px; text-align:left;">XXXsubdatatitle</td>
                                <td style=" width:13%; font-size:13px;">XXXsubdatacols</td>
                                <td style=" width:13%; font-size:13px;">XXXsubdatanans</td>
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
#              Census Datasets Details and Subdata Table html
#--------------------------------------------------------------------------
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
                <div style="width:480px;">
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


"""
#--------------------------------------------------------------------------
#                  Census Datasets Description Table html
#--------------------------------------------------------------------------
"""

census_datasets_description_head = """                        <thead>
                            <tr class="dcrowhead" id="DIsamplerows_thr">
                                <th style=" width:85%; font-size:13px; text-align:left;" class="dcleftcolhead">Subsets</th>
                                <th style=" width:15%; font-size:13px;" class="dccolhead">Num</br>Cols</th>
                            </tr>
                        </thead>
                        <tbody>"""

census_datasets_description_row_html ="""                            <tr class="dc-describe-table-body-row">
                                <td style=" width:85%; text-align:left;" class="dccolwrap"><b>XXXDatasetID</b></br>XXXDatasetText</td>
                                <td style=" width:15%; " class="dccolwrap">XXXDatasetNumCols</td>
                            </tr>
"""

"""
#--------------------------------------------------------------------------
#                  Census Datasets Zip Sizes Table html
#--------------------------------------------------------------------------
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
                <div style="margin-top:10px; width:480px; background-color:#F8F5E1;" id="censuscolscroll ">
                    <div class="container dc-container dc-default-input-button-container btn-grp-center">
                        <div class="btn-group btn-center"   style=" width: 100%; ">
                            <button type="button" class="btn btn-primary" style = ' font-size: 11px;  margin-left: 130px;  height: 30px;  width: 80px; ' onclick="scroll_census_cols('XXXDatasetID','XXXSubDataID','XXXcolid','0')">More</button>
                            <button type="button" class="btn btn-primary" style = ' font-size: 11px;  height: 30px;  width: 80px; ' onclick="scroll_census_cols('XXXDatasetID','XXXSubDataID','XXXcolid','1')">Previous</button>
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

                <div style="margin-left:auto; margin-right:auto; width:540px;">
                    <div class="container" style="padding:5px; margin:auto; width:100%; border:0px;" id="subdatacolnamescontainer">
                        <div class="container" style="padding:5px; margin:auto; width:100%;"  id="subdatacolnamesselectdiv">
                            <div class="container dc-container dc-default-input-inner-div">
                                <div class="form-group-sm">
                                    <label  for="subdatacolnames" style="text-align:left; font-size: 13px;">XXXColumnsTitle</label>
                                    <select id="subdatacolnames" multiple="multiple" size="30" style="margin-left:1px; font-size: 11px;" class="form-control">
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


"""
#--------------------------------------------------------------------------
#                   Census Download Confirmation html
#--------------------------------------------------------------------------
"""

census_confirm_html ="""
        <div class='container dc-tbl-container' style="width:620px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:620px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left">Census Datasets To Build</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" style="width:620px;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:40%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:40%; font-size:13px; text-align:left;" class="dccolhead">Zip FIle To Download</th>
                                <th style=" width:20%; font-size:13px;" class="dccolhead">Download</br>Size</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_confirm_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


census_confirm_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:40%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>              
                                <td style=" width:40%; font-size:12px; text-align:left;" class="dccolwrap">XXXfilename</td>               
                                <td style=" width:20%; font-size:12px;" class="dccolwrap">XXXtotalsize</td>
                            </tr>
"""

census_confirm_row_highlighted_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:40%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>              
                                <td bgcolor="#e6ffe6" style=" width:40%; font-size:12px; text-align:left;" class="dccolwrap"><a href="https://github.com/RickKrasinski/dfc_census_zips.git/XXXfilename" target="_blank">XXXfilename</a></td>               
                                <td style=" width:20%; font-size:12px;" class="dccolwrap">XXXtotalsize</td>
                            </tr>
"""


"""
#--------------------------------------------------------------------------
#                   Configure Verification html
#--------------------------------------------------------------------------
"""

configure_verification_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets To Drop</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:35%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:65%; font-size:13px; text-align:left;" class="dccolheadleft">File</th>
                            </tr>
                        </thead>
                        <tbody>
"""

configure_verification_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


configure_verification_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:35%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>
                                <td style=" width:65%; font-size:13px; text-align:left;" class="dccolleft">XXXFileName</td>               
                            </tr>
"""


configure_subdata_verification_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">XXXDatasetId</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" id="DIsamplerows" style="width:100%;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:60%; font-size:13px; text-align:left;" class="dccolheadleft">Subset</th>
                                <th style=" width:20%; font-size:13px; text-align:center;" class="dccolhead">Num</br>Cols</th>
                                <th style=" width:20%; font-size:13px; text-align:center;" class="dccolhead">Nan</br>Pct</th>
                            </tr>
                        </thead>
                        <tbody>
"""

configure_subdata_verification_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


configure_subdata_verification_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <th style=" width:60%; font-size:13px; text-align:left; font-weight:normal;" class="dccolleft">XXXSubset</th>
                                <th style=" width:20%; font-size:13px; text-align:center; font-weight:normal;" class="dccolwrap">XXXNumCols</th>
                                <th style=" width:20%; font-size:13px; text-align:center; font-weight:normal;" class="dccolwrap">XXXNanPct</th>
                            </tr>
"""

configure_drop_notes_html="""
        <div style="margin-left:30px;">
            <p>To drop the data selected above click on the Drop Data button.</p>
        </div>
"""




"""
#--------------------------------------------------------------------------
#                   Census Download File To Process html
#--------------------------------------------------------------------------
"""

census_process_html ="""
        <div class='container dc-tbl-container' style="width:620px;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:620px;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left">Downloaded Census Files To Process</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <table class="table dc-table" style="width:620px;">
                        <thead>
                            <tr class="dcrowhead">
                                <th style=" width:30%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:70%; font-size:13px; text-align:left;" class="dccolhead">Census FIle To Process</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_process_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


census_process_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>              
                                <td style=" width:70%; font-size:12px; text-align:left;" class="dccolwrap">XXXfilename</td>               
                            </tr>
"""

census_process_row_highlighted_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>              
                                <td bgcolor="#99ffcc" style=" width:70%; font-size:12px; text-align:left;" class="dccolwrap">XXXfilename</td>               
                            </tr>
"""


"""
#--------------------------------------------------------------------------
#                   Census Load Datasets to memory html
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
                                <th style=" width:38%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">&nbsp;Zip</br>Code</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">City</th>
                                <th style=" width:20%; font-size:13px;" class="dccolhead">County</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">&nbsp;&nbsp;US</br>State</th>
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


census_load_df_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:38%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
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
                                <td style=" width:20%; text-align:center;" class="dccolwrap">
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
                                <th style=" width:38%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">Zip</br>Code</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">City</th>
                                <th style=" width:20%; font-size:13px;" class="dccolhead">County</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">&nbsp;US</br>State</th>
                            </tr>
                        </thead>
                        <tbody>
"""

census_get_cols_for_df_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


census_get_cols_for_df_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:38%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:14%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" onclick="get_df_census_dataset_details('0','XXXDatasetID')" rb0checked rb0disabled>&nbsp;&nbsp;</input>
                                    </div>
                                </td>               
                                <td style="width:14%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" onclick="get_df_census_dataset_details('1','XXXDatasetID')" rb1checked rb1disabled></input>
                                    </div>
                                </td>               
                                <td style="width:20%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" onclick="get_df_census_dataset_details('2','XXXDatasetID')" rb2checked rb2disabled></input>
                                    </div>
                                </td>               
                                <td style="width:14%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" onclick="get_df_census_dataset_details('3','XXXDatasetID')" rb3checked rb3disabled></input>
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



confirm_download_notes_html="<br><div class='dfcleanser-common-grid-note' >Please download the zip files highlighted above via clicking on the highlighted links above or go to the <a href='https://github.com/RickKrasinski/dfc_census_zips.git' target='_blank'>dfc_census_repository</a> directly.<br><br>Download zips to the XXXCensusWorkingDir location. To learn how to change your browser download location click <a href='https://support.google.com/chrome/answer/95759?co=GENIE.Platform%3DDesktop&hl=en' target='_blank'>here.</a></div><br>"
confirm_download_none_notes_html="<br><div class='dfcleanser-common-grid-note'>Please return and select datasets to download.</div><br>"
confirm_download_incomplete_notes_html="<br><div class='dfcleanser-common-grid-note'>Not all selected datasets have been downloaded.<br>Please download the zip files highlighted above via clicking on the highlighted links above or go to the <a href='https://github.com/RickKrasinski/dfc_census.git' target='_blank'>dfc_census_repository</a> directly.<br>Download zips to the XXXCensusWorkingDir location.</div><br>"
confirm_download_complete_notes_html="<br><div class='dfcleanser-common-grid-note'>All selected datasets have been downloaded. Please process downloaded census files.</div><br>"


process_notes_html="<br><div class='dfcleanser-common-grid-note'>Please click on the Process Downloaded Files key to process zip files.</div>"
process_notes_complete_html="<br><div class='dfcleanser-common-grid-note'>All census datasets have been processed successfully.<br>Click on Configure Selected Datasets to configure census datasets.<br>Click on Load Census Data to df(s) to load datasets to df(s).</div>"


configure_notes_info_html="<br><div class='dfcleanser-common-grid-note'>To drop a dataset unselect the checked dataset(s) to drop.<br><br>To add a dataset select the unchecked dataset(s) you want to add.</div>"
configure_no_select_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:'60%;'>No datasets to configure were selected.<br><br>To go back and select datasets to configure click on Clear.</div>"
configure_no_datasets_notes_info_html="<br><div class='dfcleanser-common-grid-note'>No datasets are currently downloaded and processed.</div><br>"
configure_process_html="<div class='dfcleanser-common-grid-note'>To process datasets selected click on the Configure Selected Datasets.</div><br>"

only_datasets_to_drop_html="<br><div class='dfcleanser-common-grid-note'>To drop the selected datasets click on Drop Selected Data.</div>"
only_subdatas_to_drop_html="<br><div class='dfcleanser-common-grid-note'>To drop the selected data subsets click on Drop Selected Data.</div><br>"
both_subdatas_to_drop_html="<br><div class='dfcleanser-common-grid-note'>To drop the selected data click on Drop Selected Data.</div><br>"



load_datasets_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Load Census Data to df(s) button to laod the datasets as dfc datframes..</div>"
load_datasets_db_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Define db Connector button to define a bd connector and laod the datasets to your database.</div>"
load_datasets_none_html="<br><div class='dfcleanser-common-grid-note'>No census datasets are downloaded for loading into dataframes.</div><br>"


"""
#  Get Census Columns Dataset and Subdata Selects
"""

get_dataset_columns_notes_html="<br><div class='dfcleanser-common-grid-note'>Select a dataset to show subdata columns for.</div><br>"
get_dataset_cols_subdata_list_notes_html="<br><div class='dfcleanser-common-grid-note'>Select a subdata set to select columns from via clicking on the details button above.</div><br>"
get_dataset_cols_columns_list_notes_html="<br><div class='dfcleanser-common-grid-note'>Once you select the columns to retrieve hit the Get Columns button.</div><br>"


"""
#  Get Census Columns Notes
"""

get_dataset_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the zip_code_column value in the output dataframe is nan or if there is no zipcode in the census zipcode dataset that matches the zipcode in the zip_code_name column.</div><br>"
get_dataset_city_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the city_column value in the output dataframe is nan or if there is a nan in the census city dataset that matches the city in the city_name column.</div><br>"
get_dataset_county_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the census_column_names_list above.<br><br>The na_fill_value is used if the county_column value in the output dataframe is nan or if there is no county in the census county dataset that matches the county in the county_name column.</div><br>"
get_dataset_state_cols_to_add_notes_html="<br><div style ='margin-left:130px;' class='dfcleanser-common-grid-note'>You can change the column names used in the df by editing the columns names list above.<br><br>The na_fill_value is used if the state_column value in the output dataframe is nan or if there is no state in the census state dataset that matches the state in the state_name column.<br><br>Use a state value of US to get columns for the United States.</div><br>"





get_dataset_columns_no_datasetid_notes_html="<br><div class='dfcleanser-common-grid-note'>No dataset selected yet.</div><br>"

get_dataset_columns_no_dfs_loaded_html="<br><div class='dfcleanser-common-grid-note'>No Census df(s) are loaded. Go back to Load Census df(s) to load df(s) for column retrieval.</div><br>"


    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_census_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(census_tb_id,
                                               census_tb_keyTitleList,
                                               census_tb_jsList,
                                               census_tb_centered))

"""
#--------------------------------------------------------------------------
#                   Display Helper Functions
#--------------------------------------------------------------------------
"""

def get_datasets_downloaded() :
    """
    * -------------------------------------------------------------------------- 
    * function : get list of datasets downloaded
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
    dfc_census_dataset_path     =   (dfc_census_dataset_path + "\\working\\")
    
    files_loaded     =   []
    
    for i in range(len(swcm.zip_file_names) ) :
            
        if(does_file_exist(dfc_census_dataset_path+swcm.zip_file_names[i][0])) :
            files_loaded.append(swcm.zip_file_names[i])
        else :
            files_loaded.append(None)
        
    return(files_loaded)


def any_datasets_processed(files_processed) :
    
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


def is_complete_dataset_processed(datasetid, files_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : determine if the complete dataset is processed
    * 
    * parms :
    *
    * returns : 
    *  True or False
    * --------------------------------------------------------
    """
    
    for i in range(len(files_processed[datasetid])) :   
        if(not (files_processed[datasetid][i]) ) :
            return(False)
            
    return(True)
    

def is_any_part_of_dataset_processed(datasetid, files_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : determine if any dataset type is processed
    * 
    * parms :
    *
    * returns : 
    *  True or False
    * --------------------------------------------------------
    """
    
    for i in range(len(files_processed[datasetid])) :   
        if(files_processed[datasetid][i]) :
            return(True)
            
    return(False)


def get_subset_size(subdataid,datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the subset size of of subdata
    * 
    * parms :
    *   subdataid       -   subset key (ziocode,city,county,state,all)
    *   datasetid       -   dataset id
    *
    * returns : 
    *  dataset size
    * --------------------------------------------------------
    """
    
    totalsize   =   0
    
    if(subdataid == 4) :
        
        for i in range(len(swcm.census_datasets_csvs_size_mb[datasetid])) :
            totalsize   =   totalsize + swcm.census_datasets_csvs_size_mb[datasetid][i]
            
    else :
        
        totalsize   =   totalsize + swcm.census_datasets_csvs_size_mb[datasetid][subdataid]
            
    displaysize      =   "{:,d}".format(totalsize)
            
    return(displaysize)        


def get_colname(cname,maxlen) :
    """
    * --------------------------------------------------------- 
    * function : get the column name shortened if necessary
    * 
    * parms :
    *   cname       -   column name
    *   maxlen      -   max length of name
    *
    * returns : 
    *  column name
    * --------------------------------------------------------
    """

    if(len(cname) > maxlen) :
        halflength = int(maxlen/2) - 2
        shortelement = cname[0:halflength] + "...." + cname[(len(cname)-halflength) : (len(cname))]
        shortelement = '<a href="#" data-toggle="tooltip" data-placement="top" title="' + cname + '">' + shortelement + '</a>' 
            
    else :
        shortelement = cname
            
    return(shortelement)


"""
#--------------------------------------------------------------------------
#                   Downoad Datasets Display functions
#--------------------------------------------------------------------------
"""
def get_download_datasets_html(forconfigure=False) :
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
    
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + census_download_html)  

    #datasets_downloaded =   get_datasets_downloaded()
    #download_lists      =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
    datasets_processed  =   get_datasets_processed()
    
    #print("datasets_downloaded",datasets_downloaded)
    #print("download_lists",download_lists)
    #print("datasets_processed",datasets_processed)
    
    for i in range(len(swcm.census_datasets)) : 
        
        dsid                =   swcm.census_datasets[i]
        dsid                =   dsid.replace("_"," ")
        row_html            =   census_download_row_html.replace("XXXTDatasetID",dsid)
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
                row_html            =   row_html.replace(cbflg,"") 
                row_html            =   row_html.replace(cbdis,"")
                    
                    
            cbdis   =   "cb" + str(j+1) + "disabled"
            
        if(forconfigure) :
            row_html            =   row_html.replace("cb5flag","")         
            row_html            =   row_html.replace("cb5disabled","disabled")         
            
        load_datasets_html  =   (load_datasets_html + row_html)
    
    load_datasets_html  =   (load_datasets_html + census_download_end_html)
    
    return(load_datasets_html)


def get_dataset_index(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get list index for a dataset id
    * 
    * parms :
    *   datasetid     -   dataset id
    *
    * returns : 
    *  index in lists
    * --------------------------------------------------------
    """
    
    if(datasetid == swcm.census_datasets[0])    :       return(0)
    elif(datasetid == swcm.census_datasets[1])  :       return(1)
    elif(datasetid == swcm.census_datasets[2])  :       return(2)
    elif( (datasetid == swcm.census_datasets[3]) or 
          (datasetid == "Health Insurance") )   :       return(3)
    elif(datasetid == swcm.census_datasets[4])  :       return(4)
    elif(datasetid == swcm.census_datasets[5])  :       return(5)
    elif(datasetid == swcm.census_datasets[6])  :       return(6)
    elif(datasetid == swcm.census_datasets[7])  :       return(7)
    elif(datasetid == swcm.census_datasets[8])  :       return(8)
    elif(datasetid == swcm.census_datasets[9])  :       return(9)
    else :                                              return(-1)    
    
    
def get_load_datasets_details_html(datasetid=None,forconfigure=False,subdataid=None,colnameid=None,direction=None) :
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
    
    
    #print("get_load_datasets_details_html",datasetid,forconfigure,subdataid,colnameid,direction)
    
    load_datasets_details_html  =   ""
    
    if(datasetid is None) :
        
        header_html                 =   census_load_details_html
        header_html                 =   header_html.replace("XXXdatasetid","Description")
        load_datasets_details_html  =   (load_datasets_details_html + header_html) 
        
        load_datasets_details_html  =   (load_datasets_details_html + census_datasets_description_head)        
    
        for i in range(len(swcm.census_datasets)) : 
        
            dsid     =  swcm.census_datasets[i].replace("_"," ")
            row_html =  census_datasets_description_row_html.replace("XXXDatasetID",dsid)
            row_html =  row_html.replace("XXXDatasetText",swcm.census_dataset_details[i])
            row_html =  row_html.replace("XXXDatasetNumCols",str(swcm.census_datasets_num_cols[i]))
        
            load_datasets_details_html  =   (load_datasets_details_html + row_html)

        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_table_end_html)
        load_datasets_details_html  =   (load_datasets_details_html + census_load_details_end_html)
            
    else :
        
        if(subdataid is None) :
        
            header_html                 =   census_load_details_html
            dsid                        =   datasetid.replace("_"," ")
            header_html                 =   header_html.replace("XXXdatasetid",dsid)
            load_datasets_details_html  =   (load_datasets_details_html + header_html) 
    
            load_datasets_details_html  =   (load_datasets_details_html + census_zip_size_head) 
            
            dsinndex    =   get_dataset_index(datasetid)
            
            zcsize      =   get_subset_size(0,dsinndex)
            citysize    =   get_subset_size(1,dsinndex)
            countysize  =   get_subset_size(2,dsinndex)
            statesize   =   get_subset_size(3,dsinndex)
            totalsize   =   get_subset_size(4,dsinndex)
        
            row_html =  census_zip_size_row_html.replace("XXXZipCodeSize",zcsize)
            row_html =  row_html.replace("XXXCitySize",citysize)
            row_html =  row_html.replace("XXXCountySize",countysize)
            row_html =  row_html.replace("XXXStateSize",statesize)
            row_html =  row_html.replace("XXXTotalSize",totalsize)
        
            load_datasets_details_html  =   (load_datasets_details_html + row_html)
            load_datasets_details_html  =   (load_datasets_details_html + census_load_details_table_end_html)

        else :
        
            header_html                 =   census_load_details_html
            header_html                 =   header_html.replace("XXXdatasetid",swcm.get_subdata_name(datasetid,subdataid))#datasetid)
            load_datasets_details_html  =   (load_datasets_details_html + header_html) 
    

        # append the details table
        load_datasets_details_html  =   (load_datasets_details_html + get_load_subdata_table_html(datasetid,forconfigure,subdataid,colnameid,direction))
        if(subdataid is None) :
            load_datasets_details_html  =   (load_datasets_details_html + census_load_details_end_html)
        else :
            load_datasets_details_html  =   (load_datasets_details_html + census_load_subdata_end_html)        
    
    
    return(load_datasets_details_html)


def get_subdata_lists(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset subset lists of cols, colnames and nans
    * 
    * parms :
    *   datasetid     -   dataset id
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    if( (datasetid == swcm.census_datasets[0]) or (datasetid == swcm.census_data_dirs[0]) ) :      
        subdatacols         =   swcm.economic_col_names
        subdatacolstext     =   swcm.economic_subdata_names
        subdatacolsnans     =   swcm.economic_nan_counts

    elif( (datasetid == swcm.census_datasets[1]) or (datasetid == swcm.census_data_dirs[1]) ) :
        subdatacols         =   swcm.education_col_names
        subdatacolstext     =   swcm.education_subdata_names
        subdatacolsnans     =   swcm.education_nan_counts

    elif( (datasetid == swcm.census_datasets[2]) or (datasetid == swcm.census_data_dirs[2]) ) :
        subdatacols         =   swcm.employment_col_names
        subdatacolstext     =   swcm.employment_subdata_names
        subdatacolsnans     =   swcm.employment_nan_counts
    
    elif( (datasetid == swcm.census_datasets[3]) or (datasetid == "Health Insurance") or 
           (datasetid == swcm.census_data_dirs[3]) ) :
        subdatacols         =   swcm.health_insurance_col_names
        subdatacolstext     =   swcm.health_insurance_subdata_names
        subdatacolsnans     =   swcm.health_insurance_nan_counts

    elif( (datasetid == swcm.census_datasets[4]) or (datasetid == swcm.census_data_dirs[4]) ) :
        subdatacols         =   swcm.housing_col_names
        subdatacolstext     =   swcm.housing_subdata_names
        subdatacolsnans     =   swcm.housing_nan_counts

    elif( (datasetid == swcm.census_datasets[5]) or (datasetid == swcm.census_data_dirs[5]) ) :
        subdatacols         =   swcm.immigration_col_names
        subdatacolstext     =   swcm.immigration_subdata_names
        subdatacolsnans     =   swcm.immigration_nan_counts

    elif( (datasetid == swcm.census_datasets[6]) or (datasetid == swcm.census_data_dirs[6]) ) :
        subdatacols         =   swcm.internet_col_names
        subdatacolstext     =   swcm.internet_subdata_names
        subdatacolsnans     =   swcm.internet_nan_counts

    elif( (datasetid == swcm.census_datasets[7]) or (datasetid == swcm.census_data_dirs[7]) ) :
        subdatacols         =   swcm.population_col_names
        subdatacolstext     =   swcm.population_subdata_names
        subdatacolsnans     =   swcm.population_nan_counts

    elif( (datasetid == swcm.census_datasets[8]) or (datasetid == swcm.census_data_dirs[8]) ) :
        subdatacols         =   swcm.social_col_names
        subdatacolstext     =   swcm.social_subdata_names
        subdatacolsnans     =   swcm.social_nan_counts

    elif( (datasetid == swcm.census_datasets[9]) or (datasetid == swcm.census_data_dirs[9]) ) :
        subdatacols         =   swcm.transportation_col_names
        subdatacolstext     =   swcm.transportation_subdata_names
        subdatacolsnans     =   swcm.transportation_nan_counts
    
    
    return([subdatacols,subdatacolstext,subdatacolsnans])    
    
    
    

def get_load_subdata_table_html(datasetid,forconfigure=False,subdataindex=None,colnameid=None,direction=None) :
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
    
    #print("get_load_subdata_table_html",datasetid,forconfigure,subdataindex,colnameid,direction)
    
    load_datasets_details_table     =   ""
    
    subdata_data        =   get_subdata_lists(datasetid)
    subdatacols         =   subdata_data[0]    
    subdatacolstext     =   subdata_data[1]
    subdatacolsnans     =   subdata_data[2]
    
    if(subdataindex is None) :
        
        if(forconfigure) :
            load_datasets_details_table     =   (load_datasets_details_table + configure_subdata_table_html)
        else :
            load_datasets_details_table     =   (load_datasets_details_table + census_subdata_table_html)

        for i in range(len(subdatacols)) :

            if(not (i==0)) :
            
                if(forconfigure) :
                    row_html    =   configure_subdata_table_row_html
                else :
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
                
                load_datasets_details_table     =   (load_datasets_details_table + row_html)
        
        if(forconfigure) :
            load_datasets_details_table     =   (load_datasets_details_table + configure_subdata_table_html_end)
        else :
            load_datasets_details_table     =   (load_datasets_details_table + census_subdata_table_html_end)
            

    else :
        
        load_datasets_details_table     =   (load_datasets_details_table + census_colnames_table_html)
        
        subdata_col_names               =   subdatacols[subdataindex]
        nanindices                      =   swcm.get_census_subdata_indices(datasetid,subdataindex)

        if(len(subdata_col_names) > 15) :
            
            if(colnameid is None) :
                rowcount    =   15 
            else :
                
                if(direction == 0) :
                
                    if((colnameid + 15) > len(subdata_col_names)) :
                        rowcount    =   len(subdata_col_names) - colnameid
                    else :
                        rowcount    =   15
                        
                else :
                    rowcount    =   15
                
            if(colnameid is None) :
                rowstart    =   0
                
            else :
                
                if(direction == 0) :
                    rowstart    =   colnameid
                else :
                    rowstart    =   colnameid - (2*15)
                    if(rowstart < 0) :
                        rowstart    =   0
                
        else :
            rowcount    =   len(subdata_col_names)
            rowstart    =   0
        
        for i in range(rowcount) :

            row_html    =   census_colnames_table_row_html
            
            colname     =   get_colname(subdata_col_names[i+rowstart],70)
                
            row_html    =   row_html.replace("XXXcolname",colname)
            pct_str     =   '{:4.2f}'.format(100 * (subdatacolsnans[nanindices[i+rowstart]]/swcm.total_zips_count))
            row_html    =   row_html.replace("XXXcnamenans",pct_str + "%")
                                             
            load_datasets_details_table     =   (load_datasets_details_table + row_html)

        load_datasets_details_table     =   (load_datasets_details_table + census_colnames_table_html_end)
        
        if(len(subdata_col_names) > 15) :
            
            scroll_html    =   census_colnames_scroll_html
            scroll_html    =   scroll_html.replace("XXXDatasetID",datasetid)
            scroll_html    =   scroll_html.replace("XXXSubDataID",str(subdataindex))
            
            if(colnameid is None) :
                colid   =   15
            else :
                
                if(direction == 0) :
                    
                    if((colnameid + 15) > len(subdata_col_names)) :
                        colid   =   0
                    else :
                        colid   =   colnameid + 15
                        
                else :
                    
                    if((colnameid - (2*15)) < 0) :
                        colid   =   15
                    else :
                        colid   =   colnameid - (2*15)
                    
            scroll_html    =   scroll_html.replace("XXXcolid",str(colid))
            
            load_datasets_details_table     =   (load_datasets_details_table + scroll_html)
    
    
    return(load_datasets_details_table)

    
def display_load_census_data(datasetid=None,forconfigure=False,subdataid=None,colnameid=None,direction=None) :
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
    
    #print("display_load_census_data",datasetid,forconfigure,subdataid,colnameid,direction)
    
    
    load_census_html    =   get_download_datasets_html(forconfigure)
    
    if(forconfigure) :
        dropsubs    =   cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
        
        if(any_datasets_processed(get_datasets_processed())) :
            
            if( not (dropsubs is None)) :
                if(dropsubs =="NO DATASETS SELECTED") :
                    load_notes_html     =   configure_no_select_notes_info_html
                    cfg.drop_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
                
            else :
                load_notes_html     =   configure_notes_info_html
                    
        else :
            load_notes_html     =   configure_no_datasets_notes_info_html    
                
        load_details_heading_html       =   "<div>Configure Census Data</div><br>"
                
    else :
        
        if(not(subdataid is None)) :
            load_notes_html     =   download_notes_subdata_info_html
        else :
            load_notes_html     =   download_notes_info_html
            
        load_details_heading_html       =   "<div>Build Census Datasets</div>"
    
    load_details_html               =   get_load_datasets_details_html(datasetid,forconfigure,subdataid,colnameid,direction)
    


    if(forconfigure) :
        
        #print("get_datasets_processed",get_datasets_processed())
        
        if(any_datasets_processed(get_datasets_processed())) :
        
            load_data_tb        =   ButtonGroupForm(data_configure_tb_id,
                                                    data_configure_tb_keyTitleList,
                                                    data_configure_tb_jsList,
                                                    data_configure_tb_centered)
    
            load_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":225})
        
            load_census_html    =   load_census_html.replace("Census Datasets","Census Datasets To Configure")
            
        else :
            
            load_data_tb        =   ButtonGroupForm(data_configure_no_datasets_tb_id,
                                                    data_configure_no_datasets_tb_keyTitleList,
                                                    data_configure_no_datasets_tb_jsList,
                                                    data_configure_no_datasets_tb_centered)
            
            load_data_tb.set_customstyle({"font-size":13, "height":75, "width":100, "left-margin":32})
        
            load_census_html    =   load_census_html.replace("Census Datasets","Census Datasets To Configure")
            
        
    else :
        
        load_data_tb        =   ButtonGroupForm(data_download_tb_id,
                                                data_download_tb_keyTitleList,
                                                data_download_tb_jsList,
                                                data_download_tb_centered)
        
        load_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":210})
        
        load_census_html    =   load_census_html.replace("Census Datasets","Census Datasets To Build")
                        
    load_data_tb_html           =   load_data_tb.get_html()

    if( (forconfigure) and (not (any_datasets_processed(get_datasets_processed()))) ) :   
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
        gridhtmls       =   [load_details_heading_html,load_census_html,load_notes_html,load_data_tb_html]
    
        print("\n")
        display_generic_grid("dfcensus-datasets-none-data-wrapper",gridclasses,gridhtmls)
        print("\n")
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-main","dfc-right","dfc-footer"]
        gridhtmls       =   [load_details_heading_html,load_census_html,load_notes_html,load_details_html,load_data_tb_html]
    
        print("\n")
        display_generic_grid("dfcensus-download-data-wrapper",gridclasses,gridhtmls)
        print("\n")
        
    

"""
#--------------------------------------------------------------------------
#           Download Datasets Confirmation Display functions
#--------------------------------------------------------------------------
"""

def get_confirm_load_datasets_html(downloadlists) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the main download confirmation census screen
    * 
    * parms :
    *   downloadlists  -   list of downloads selected
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    confirm_load_datasets_html  =   ""
    confirm_load_datasets_html  =   (confirm_load_datasets_html + census_confirm_html) 
    
    census_files        =   swcc.verify_downloads(downloadlists)
    files_missing       =   census_files[0]
    
    files_to_flag       =   []
    
    if(not (files_missing is None)) :
    
        for i in range(len(swcm.census_data_dirs)) : 
        
            downlds     =   False
            
            for j in range(5) :
                if(downloadlists[i][j] == "True") :
                    downlds    =   True
                    
            if(downlds) :
                if( (swcm.census_data_dirs[i]+".zip") in files_missing) :
                    files_to_flag.append([swcm.census_data_dirs[i]+".zip",swcm.census_datasets_zips_size_mb[i]]) 
                else :
                    files_to_flag.append(None)
            else :
                files_to_flag.append(None)
                
        for i  in range(len(files_to_flag)) :
            
            if(not (files_to_flag[i] is None)) :
            
                dsid                        =   swcm.census_datasets[i]
                dsid                        =   dsid.replace(" ","_")
                row_html                    =   census_confirm_row_highlighted_html.replace("XXXDatasetID",dsid)
                row_html                    =   row_html.replace("XXXfilename",files_to_flag[i][0])
                row_html                    =   row_html.replace("XXXtotalsize","{:,d}".format(files_to_flag[i][1]))
                confirm_load_datasets_html  =   (confirm_load_datasets_html + row_html) 

    
    confirm_load_datasets_html  =   (confirm_load_datasets_html + census_confirm_end_html)
    
    return(confirm_load_datasets_html)


def display_download_census_confirmation(downloadlists,verify=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the main download census screen
    * 
    * parms :
    *   downloadlists  -   list of downloads selected
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    print("display_load_census_data",downloadlists,verify)
    
    confirm_load_census_html            =   get_confirm_load_datasets_html(downloadlists)

    import os
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\working\\")
    
    no_downloads_found  =   False
    
    if(swcc.are_downloads_selected(downloadlists)) :
        
        census_files        =   swcc.verify_downloads(downloadlists)
    
        files_missing       =   census_files[0]
        #files_found         =   census_files[1]
        
        if(len(files_missing) > 0) :
        
            if(not(verify)) :
                confirm_load_census_notes_html      =   confirm_download_notes_html
            else :
                vfiles = swcc.verify_downloads(downloadlists)
                if(len(vfiles[0]) > 0) :
                    confirm_load_census_notes_html      =   confirm_download_incomplete_notes_html
                else :
                    confirm_load_census_notes_html      =   confirm_download_complete_notes_html
            
            confirm_load_census_notes_html      =   confirm_load_census_notes_html.replace("XXXCensusWorkingDir",dfc_census_path)
            
        else :
            confirm_load_census_notes_html      =   confirm_download_complete_notes_html

    else :
        confirm_load_census_notes_html      =   confirm_download_none_notes_html
        no_downloads_found  =   True
        
    if(no_downloads_found) :
        
        confirm_load_data_tb                =   ButtonGroupForm(data_confirm_download_none_tb_id,
                                                                data_confirm_download_none_tb_keyTitleList,
                                                                data_confirm_download_none_tb_jsList,
                                                                data_confirm_download_none_tb_centered)
        
        confirm_load_data_tb.set_customstyle({"font-size":13, "height":50, "width":180, "left-margin":220})
        
    else :
        
        if(len(files_missing) > 0) :

            confirm_load_data_tb                =   ButtonGroupForm(data_confirm_download_tb_id,
                                                                    data_confirm_download_tb_keyTitleList,
                                                                    data_confirm_download_tb_jsList,
                                                                    data_confirm_download_tb_centered)
        
            confirm_load_data_tb.set_customstyle({"font-size":13, "height":50, "width":180, "left-margin":130})
        
        else :
        
            confirm_load_data_tb                =   ButtonGroupForm(data_confirm_download_complete_tb_id,
                                                                    data_confirm_download_complete_tb_keyTitleList,
                                                                    data_confirm_download_complete_tb_jsList,
                                                                    data_confirm_download_complete_tb_centered)
        
            confirm_load_data_tb.set_customstyle({"font-size":13, "height":50, "width":180, "left-margin":130})
        
    confirm_load_data_tb_html           =   confirm_load_data_tb.get_html()    
    
    gridclasses     =   ["dfc-main","dfc-bottom","dfc-footer"]
    gridhtmls       =   [confirm_load_census_html,confirm_load_census_notes_html,confirm_load_data_tb_html]
    
    print("\n")
    display_generic_grid("dfcensus-confirm-load-data-wrapper",gridclasses,gridhtmls)
    print("\n")
    

"""
#--------------------------------------------------------------------------
#           Process Datasets Confirmation Display functions
#--------------------------------------------------------------------------
"""

def get_process_download_datasets_html(zips_not_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the main download confirmation census screen
    * 
    * parms :
    *   downloadlists  -   list of downloads selected
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    confirm_process_datasets_html  =   ""
    
    confirm_process_datasets_html  =   (confirm_process_datasets_html + census_process_html) 
    
    if(len(zips_not_processed) > 0) :
    
        for i in range(len(zips_not_processed)) : 
        
            for j in range(len(zips_not_processed[i])) :
                
                if(type(zips_not_processed[i][j]) == list) :
                    
                    for k in range(len(zips_not_processed[i][j])) :
                        dsid                            =   swcm.census_datasets[i]
                        dsid                            =   dsid.replace(" ","_")
                        row_html                        =   census_process_row_html.replace("XXXDatasetID",dsid)
                        row_html                        =   row_html.replace("XXXfilename",zips_not_processed[i][j][k])
                        confirm_process_datasets_html   =   (confirm_process_datasets_html + row_html)
                    
                else :
                    dsid                            =   swcm.census_datasets[i]
                    dsid                            =   dsid.replace(" ","_")
                    row_html                        =   census_process_row_html.replace("XXXDatasetID",dsid)
                    row_html                        =   row_html.replace("XXXfilename",zips_not_processed[i][j])
                    confirm_process_datasets_html   =   (confirm_process_datasets_html + row_html)
    
    confirm_process_datasets_html  =   (confirm_process_datasets_html + census_process_end_html)
    
    return(confirm_process_datasets_html)


def display_process_downloaded_files(downloadlists) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the process downloaded zip files
    * 
    * parms :
    *   NA
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    print("display_process_downloaded_files",downloadlists)
    

    import os
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\working\\")
    
    #download_files      =   swcc.verify_downloads(downloadlists)
    #zips_to_process     =   swcc.get_zips_to_process(download_files[1],downloadlists)
    zips_not_processed  =   swcc.get_zips_not_processed()
    
    print("display_process_downloaded_files\n",zips_not_processed)
    
    process_load_census_html            =   get_process_download_datasets_html(zips_not_processed)
    
    if(swcc.any_zips_not_processed(zips_not_processed)) :
        process_load_census_notes_html  =   process_notes_html
        
    else :
        process_load_census_notes_html  =   process_notes_complete_html
        
    if(swcc.any_zips_not_processed(zips_not_processed)) :

        process_load_data_tb                =   ButtonGroupForm(data_process_load_tb_id,
                                                                data_process_load_tb_keyTitleList,
                                                                data_process_load_tb_jsList,
                                                                data_process_load_tb_centered)
        
    else :
        
        process_load_data_tb                =   ButtonGroupForm(data_process_load_complete_tb_id,
                                                                data_process_load_complete_tb_keyTitleList,
                                                                data_process_load_complete_tb_jsList,
                                                                data_process_load_complete_tb_centered)
                        
    process_load_data_tb.set_customstyle({"font-size":13, "height":50, "width":180, "left-margin":130})
    process_load_data_tb_html           =   process_load_data_tb.get_html()    
    
    gridclasses     =   ["dfc-main","dfc-bottom","dfc-footer"]
    gridhtmls       =   [process_load_census_html,process_load_census_notes_html,process_load_data_tb_html]
    
    print("\n")
    display_generic_grid("dfcensus-confirm-load-data-wrapper",gridclasses,gridhtmls)
    print("\n")


def get_dataset_type_name(index) :
    
    if(index == 0)      :   return("zipcode")
    elif(index == 1)    :   return("cities")
    elif(index == 2)    :   return("counties")
    elif(index == 3)    :   return("states")
    else                :   return("")


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
    

def get_configure_datasets_verification_html(datasets_to_configure,datasets_processed) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the configure datasets html
    * 
    * parms :
    *   datasets_to_drop     -   dataset to drop
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    print("get_configure_datasets_verification_html\n",datasets_to_configure,"\n\n",datasets_processed)
    
    add_ds_html     =   configure_verification_html
    add_ds_html     =   add_ds_html.replace("To Drop","To Add")
    drop_ds_html    =   configure_verification_html 
    
    add_datasets    =   []
    drop_datasets   =   []
    
    for i in range(len(datasets_to_configure)) :
        
        for j in range(4) :
            
            if(datasets_to_configure[i][j] == "True") :
                
                if(not (datasets_processed[i][j])) :
                    
                    row_html    =   configure_verification_row_html
                    row_html    =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
                    
                    filename    =   swcm.census_data_dirs[i] + "_" + get_dataset_type_name(j) + ".csv"
                    row_html    =   row_html.replace("XXXFileName",filename)
                                    
                    add_ds_html   =   (add_ds_html + row_html)
                    
                    add_datasets.append(filename)
                    
            else :
                
                if(datasets_processed[i][j]) :
                    
                    row_html    =   configure_verification_row_html
                    row_html    =   row_html.replace("XXXDatasetID",swcm.census_datasets[i])
                    
                    filename    =   swcm.census_data_dirs[i] + "_" + get_dataset_type_name(j) + ".csv"
                    row_html    =   row_html.replace("XXXFileName",filename) 
                                    
                    drop_ds_html   =   (drop_ds_html + row_html)
                    
                    drop_datasets.append(filename)
                
    
    add_ds_html   =   (add_ds_html + configure_verification_end_html)   
    drop_ds_html  =   (drop_ds_html + configure_verification_end_html)
    
    if(len(add_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_ADD_DATASETS_LIST,add_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)

    if(len(drop_datasets) > 0) :
        cfg.set_config_value(cfg.CENSUS_DROP_DATASETS_LIST,drop_datasets)
    else :
        cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
    
    return([add_ds_html,drop_ds_html])    


def display_configure_verification_data(datasets_to_configure) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the main configure census screen
    * 
    * parms :
    *   datasets_to_drop     -   dataset to drop
    *   subdata_dsid         -   dataset for subdatas
    *   subdatas_to_drop     -   data subsets to drop 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    datasets_processed  =   get_datasets_processed()
    print("display_configure_verification_data\n",datasets_to_configure,"\n",datasets_processed)
    
    [configure_drop_datset_html,configure_add_datset_html]    =   get_configure_datasets_verification_html(datasets_to_configure,datasets_processed)
    
    
    if( (any_datasets_to_drop(datasets_to_configure,datasets_processed)) or 
        (any_datasets_to_add(datasets_to_configure,datasets_processed)) ) :
        
        configure_drop_notes_html       =   configure_process_html
        
        configure_data_tb        =   ButtonGroupForm(data_configure_verify_tb_id,
                                                     data_configure_verify_tb_keyTitleList,
                                                     data_configure_verify_tb_jsList,
                                                     data_configure_verify_tb_centered)
    
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":195})
        configure_data_tb_html          =   configure_data_tb.get_html()

        
    else :
        
        configure_drop_notes_html       =   configure_no_select_notes_info_html
        
        configure_data_tb        =   ButtonGroupForm(data_configure_no_datasets_tb_id,
                                                     data_configure_no_datasets_tb_keyTitleList,
                                                     data_configure_no_datasets_tb_jsList,
                                                     data_configure_no_datasets_tb_centered)
    
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":240})
        configure_data_tb_html          =   configure_data_tb.get_html()
        
        
    configure_heading_html          =   "<div>Configure Datasets</div><br></br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-main","dfc-footer"]
    gridhtmls       =   [configure_heading_html,configure_drop_datset_html,configure_add_datset_html,configure_drop_notes_html,configure_data_tb_html]
    
    print("\n")
    display_generic_grid("dfcensus-configure-data-wrapper",gridclasses,gridhtmls)
    print("\n")
        

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Load Datasets Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
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
    
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + census_load_df_html)  
    
    datasets_built      =   get_datasets_processed()
    #print("datasets_built",datasets_built)

    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    #print("dataframes_loaded",dataframes_loaded)
    
    for i in range(len(datasets_built)) : 
        
        if(len(datasets_built[i]) > 0) :
            
            if(is_any_part_of_dataset_processed(i,datasets_built)) :
            
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


def display_load_datasets(for_dataframes=True) :
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
    
    if(for_dataframes) :
    
        load_datasets_to_df_tb      =   ButtonGroupForm(data_load_datasets_to_df_tb_id,
                                                        data_load_datasets_to_df_tb_keyTitleList,
                                                        data_load_datasets_to_df_tb_jsList,
                                                        data_load_datasets_to_df_tb_centered)
        
    else :
        
        load_datasets_to_df_tb      =   ButtonGroupForm(data_load_datasets_to_db_tb_id,
                                                        data_load_datasets_to_db_tb_keyTitleList,
                                                        data_load_datasets_to_db_tb_jsList,
                                                        data_load_datasets_to_db_tb_centered)
        

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
    
    print("\n")
    display_generic_grid("dfcensus-load-data-wrapper",gridclasses,gridhtmls)
    print("\n")


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Get Dataset Columns Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_colnames_for_get_cols_html(datasetid,subdataindex) :
    
    get_cols_colnames_html  =   ""
    
    subdata_data            =   get_subdata_lists(datasetid)
    subdatacols             =   subdata_data[0]    

    get_cols_colnames_html  =   (get_cols_colnames_html + get_cols_colnames_table_html)

    subdata_col_names       =   subdatacols[subdataindex]

    get_cols_colnames_html  =   get_cols_colnames_html.replace("XXXColumnsTitle",("* " + datasetid + " : " + swcm.get_subdata_name(datasetid,int(subdataindex)) + " column names"))        
    
    for i in range(len(subdata_col_names)) :

        row_html    =   get_cols_colnames_table_row_html
        colname     =   get_colname(subdata_col_names[i],90)
        row_html    =   row_html.replace("XXXColname",str(i))#subdata_col_names[i])
        row_html    =   row_html.replace("XXXSColname",colname)
        
        get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)       
        
    get_cols_colnames_html     =   (get_cols_colnames_html + get_cols_colnames_table_end_html)
     
    return(get_cols_colnames_html)


def get_dataset_columns_subdata_table_html(datasetid,forloadcols=False) :
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
    
    load_datasets_details_table     =   ""
    
    if(not forloadcols) :
        load_datasets_details_table     =   (load_datasets_details_table + census_subdata_table_html)
    else :
        load_datasets_details_table     =   (load_datasets_details_table + load_cols_subdata_table_html)
        load_datasets_details_table     =   load_datasets_details_table.replace("XXXDatasetID",datasetid)
        
    if(not(datasetid is None)) :
        
        subdata_data        =   get_subdata_lists(datasetid)
        
        subdatacols         =   subdata_data[0]    
        subdatacolstext     =   subdata_data[1]
        subdatacolsnans     =   subdata_data[2]
    

        for i in range(len(subdatacols)) :

            if(not (i==0)) :
            
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
        
    return(load_datasets_details_table)


def any_dataframes_loaded_for_dataset(datasetid) :
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list() 
    
    for i in range(len(dataframes_loaded)) :
        if(dataframes_loaded[i].find(datasetid) > -1) :
            return(True)
            
    return(False)
            

def get_dataset_columns_html() :
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
    #print("get_dataset_columns_html")
    
    load_datasets_html  =   ""
    
    load_datasets_html  =   (load_datasets_html + census_get_cols_for_df_html)  
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    
    print("get_dataset_columns_html",dataframes_loaded)
    
    if(not(dataframes_loaded is None)) :
    
        for i in range(len(swcm.census_data_dirs)) : 
            
            print("any_dataframes_loaded_for_dataset",any_dataframes_loaded_for_dataset(swcm.census_data_dirs[i]))
            
            if(any_dataframes_loaded_for_dataset(swcm.census_data_dirs[i])) :
                
                dsid                =   swcm.census_datasets[i]
                dsid                =   dsid.replace("_"," ")
                row_html            =   census_get_cols_for_df_row_html.replace("XXXTDatasetID",dsid)
                row_html            =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i])
            
                for j in range(4)  : 
                
                    if(j==0)        :   
                        dftype  =   "zipcode"
                        cbdis   =   "rb0disabled"
                        cbchk   =   "rb0checked"
                            
                    elif(j==1)      :   
                        dftype  =   "cities" 
                        cbdis   =   "rb1disabled"
                        cbchk   =   "rb1checked"
                            
                    elif(j==2)      :   
                        dftype  =   "counties" 
                        cbdis   =   "rb2disabled"
                        cbchk   =   "rb2checked"
                            
                    elif(j==3)      :   
                        dftype  =   "states"
                        cbdis   =   "rb3disabled"
                        cbchk   =   "rb3checked"
                        
                    print("swcm.census_data_dirs[i] + '_' + dftype",swcm.census_data_dirs[i] + "_" + dftype + "_df")
            
                    if((swcm.census_data_dirs[i] + "_" + dftype + "_df") in dataframes_loaded) :
                            
                        row_html            =   row_html.replace(cbdis,"")
                        row_html            =   row_html.replace(cbchk,"")
                                
                    else :
                        row_html            =   row_html.replace(cbdis,"disabled") 
                        row_html            =   row_html.replace(cbchk,"")

                load_datasets_html  =   (load_datasets_html + row_html)    
    
    load_datasets_html  =   (load_datasets_html + census_get_cols_for_df_end_html)

    return(load_datasets_html)


def display_get_dataset_columns(datasetid=None,datasettype=None,subdataid=None) :
    """
    * ------------------------------------------------------- 
    * function : display the get dataset columnss screen
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    print("display_get_dataset_columns",datasetid,datasettype,subdataid)
    
    dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
    print("dataframes_loaded",dataframes_loaded)
        
    if( (datasetid is None) or (dataframes_loaded is None) ) :

        get_dataset_cols_html       =   get_dataset_columns_html()
        get_dataset_cols_html       =   get_dataset_cols_html.replace("Census Datasets","dfc Census Datasets Loaded to df(s)") 
        
        if(dataframes_loaded is None) :
        
            get_dataset_notes_html      =   get_dataset_columns_no_dfs_loaded_html 
    
            get_dataset_columns_tb      =   ButtonGroupForm(get_dataset_columns_no_df_tb_id,
                                                            get_dataset_columns_no_df_tb_keyTitleList,
                                                            get_dataset_columns_no_df_tb_jsList,
                                                            get_dataset_columns_no_df_tb_centered)
            
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":100})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
        else :
            
            get_dataset_notes_html      =   get_dataset_columns_notes_html 
            
            get_dataset_columns_tb      =   ButtonGroupForm(get_dataset_columns_tb_id,
                                                            get_dataset_columns_tb_keyTitleList,
                                                            get_dataset_columns_tb_jsList,
                                                            get_dataset_columns_tb_centered)
            
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":160})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
    else :
        
        if(subdataid is None) :
        
            get_dataset_cols_subdata_html   =   get_dataset_columns_subdata_table_html(datasetid,True)
        
            get_dataset_notes_html          =   get_dataset_cols_subdata_list_notes_html 
            
            get_dataset_columns_tb          =   ButtonGroupForm(get_subdata_columns_tb_id,
                                                                get_subdata_columns_tb_keyTitleList,
                                                                get_subdata_columns_tb_jsList,
                                                                get_subdata_columns_tb_centered)
                        
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":110})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
        else :
            
            get_dataset_cols_subdata_html   =   get_colnames_for_get_cols_html(datasetid,subdataid)
        
            get_dataset_notes_html          =   get_dataset_cols_columns_list_notes_html 
            
            get_dataset_columns_tb          =   ButtonGroupForm(get_col_names_list_tb_id,
                                                                get_col_names_list_tb_keyTitleList,
                                                                get_col_names_list_tb_jsList,
                                                                get_col_names_list_tb_centered)
                        
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":40})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            

    if(datasetid is None) :
        
        get_cols_heading_html       =   "<div>Select dfc Dataframe To Get Census Column(s) from</div><br></br>"

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
        gridhtmls       =   [get_cols_heading_html,get_dataset_cols_html,get_dataset_notes_html,get_dataset_columns_tb_html]
        
    else :
        
        if(subdataid is None) :
            get_cols_heading_html       =   "<div>Select Subdata Columns</div><br></br>"
        else :
            get_cols_heading_html       =   "<div>Select Column Names from Census Dataset</div><br></br>"

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
        gridhtmls       =   [get_cols_heading_html,get_dataset_cols_subdata_html,get_dataset_notes_html,get_dataset_columns_tb_html]
    
    print("\n")
    display_generic_grid("dfcensus-get-cols-load-data-wrapper",gridclasses,gridhtmls)
    print("\n")
        

def display_get_census_columns(datasetid,dsdtype,subdataid,colslist) :
    """
    * ------------------------------------------------------- 
    * function : display the get dataset columns screen
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    #print("display_get_census_columns",datasetid,dsdtype,subdataid,colslist)
    
    from dfcleanser.common.html_widgets import InputForm
    
    if(dsdtype == 0) :
        get_cols_input_form = InputForm(get_census_cols_input_form[0],
                                        get_census_cols_input_form[1],
                                        get_census_cols_input_form[2],
                                        get_census_cols_input_form[3],
                                        get_census_cols_input_form[4],
                                        get_census_cols_input_form[5],
                                        get_census_cols_input_form[6])
        
        get_cols_form_id            =   get_census_cols_input_form[0]
        get_census_cols_notes_html  =   get_dataset_cols_to_add_notes_html 
        
    elif(dsdtype == 1) :
        get_cols_input_form = InputForm(get_city_census_cols_input_form[0],
                                        get_city_census_cols_input_form[1],
                                        get_city_census_cols_input_form[2],
                                        get_city_census_cols_input_form[3],
                                        get_city_census_cols_input_form[4],
                                        get_city_census_cols_input_form[5],
                                        get_city_census_cols_input_form[6])
        
        get_cols_form_id            =   get_city_census_cols_input_form[0]
        get_census_cols_notes_html  =   get_dataset_city_cols_to_add_notes_html
        
    elif(dsdtype == 2) :
        get_cols_input_form = InputForm(get_county_census_cols_input_form[0],
                                        get_county_census_cols_input_form[1],
                                        get_county_census_cols_input_form[2],
                                        get_county_census_cols_input_form[3],
                                        get_county_census_cols_input_form[4],
                                        get_county_census_cols_input_form[5],
                                        get_county_census_cols_input_form[6])
        
        get_cols_form_id            =   get_county_census_cols_input_form[0]
        get_census_cols_notes_html  =   get_dataset_county_cols_to_add_notes_html

    else :
        get_cols_input_form = InputForm(get_states_census_cols_input_form[0],
                                        get_states_census_cols_input_form[1],
                                        get_states_census_cols_input_form[2],
                                        get_states_census_cols_input_form[3],
                                        get_states_census_cols_input_form[4],
                                        get_states_census_cols_input_form[5],
                                        get_states_census_cols_input_form[6])
        
        get_cols_form_id            =   get_states_census_cols_input_form[0]
        get_census_cols_notes_html  =   get_dataset_state_cols_to_add_notes_html
    
    selectDicts     =   []
        
    alldfs          =   cfg.get_dfc_dataframes_titles_list()
    dataframes      =   []
    
    if(not (alldfs is None)) :
        
        for i in range(len(alldfs)) :
        
            if(not (swcm.is_dfc_census_dataset_name(alldfs[i])) ) :
                dataframes.append(alldfs[i])
    
    if(len(dataframes) > 0) :
        subssel         =   {"default":dataframes[0],"list":dataframes, "callback":"select_new_get_cols_df"}
        df              =   cfg.get_dfc_dataframe_df(dataframes[0])
        dfcols          =   df.columns.tolist()
    else :
        subssel         =   {"default":"No dfs defined","list":["No dfs defined"]}
        dfcols          =   ["no df selected"]
        
    selectDicts.append(subssel)
        
    subssel         =   {"default":dfcols[0],"list":dfcols}
    selectDicts.append(subssel)
    
    if((dsdtype == 1) or (dsdtype == 2)) :
        subssel         =   {"default":dfcols[0],"list":dfcols}
        selectDicts.append(subssel)
        
    if(dsdtype == 0) :
        
        get_select_defaults(get_cols_input_form,
                            get_census_cols_input_form[0],
                            get_census_cols_input_form[1],
                            get_census_cols_input_form[3],
                            selectDicts)
        
    elif(dsdtype == 1) :

        get_select_defaults(get_cols_input_form,
                            get_city_census_cols_input_form[0],
                            get_city_census_cols_input_form[1],
                            get_city_census_cols_input_form[3],
                            selectDicts)
        
    elif(dsdtype == 2) :

        get_select_defaults(get_cols_input_form,
                            get_county_census_cols_input_form[0],
                            get_county_census_cols_input_form[1],
                            get_county_census_cols_input_form[3],
                            selectDicts)
    
    else :

        get_select_defaults(get_cols_input_form,
                            get_states_census_cols_input_form[0],
                            get_states_census_cols_input_form[1],
                            get_states_census_cols_input_form[3],
                            selectDicts)
        

    colnames    =   swcm.get_subdata_colnames(datasetid,subdataid)
    
    cnamestext  =   ""
    
    for i in range(len(colslist)) :
        cnamestext  =   cnamestext + colnames[int(colslist[i])] + "\n"
        
    if((dsdtype == 1) or (dsdtype == 2)) :
        fparms  =   ["","","",cnamestext,"nan"]
        
    else :
        fparms  =   ["","",cnamestext,"nan"]
        
    cfg.set_config_value(get_cols_form_id+"Parms",fparms)
        
        
    get_cols_input_form.set_shortForm(False)
    get_cols_input_form.set_gridwidth(680)
    get_cols_input_form.set_custombwidth(100)
    get_cols_input_form.set_fullparms(True)
        
    get_cols_input_html         =   get_cols_input_form.get_html() 
    get_cols_heading_html       =   "<div>Add Census Column(s) to df</div><br></br>"

    #print(get_cols_input_html)

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-bottom"]
    gridhtmls       =   [get_cols_heading_html,get_cols_input_html,get_census_cols_notes_html]
        
    print("\n")
    display_generic_grid("dfcensus-get-cols-wrapper",gridclasses,gridhtmls)
        


short_note_html="<div style='text-align:center; margin-left:1px; width:360px; background-color: #F8F5E1; border: 1px solid #67a1f3; word-wrap:break-word'>XXXNote</div>"

def display_short_note(msg) :
    
    note_html   =   short_note_html.replace("XXXNote",msg)
    
    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [note_html]
    
    display_generic_grid("dfcensus-short-note-wrapper",gridclasses,gridhtmls)
        


    
    
    