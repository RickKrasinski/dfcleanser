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
import dfcleanser.sw_utilities.sw_utility_census_control as swcc

from dfcleanser.common.html_widgets import (ButtonGroupForm)

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

census_tb_keyTitleList            =   ["Download</br>Census</br>Data",
                                       "Configure</br>Census</br>Data",
                                       "Load</br>Census Data</br>to df(s)",
                                       "Get Census</br>Column</br>for df",
                                       "Export</br>Census</br>df(s)",
                                       "Load</br>Census Data</br>to db(s)",
                                       
                                       "Clear","Reset","Help"]

census_tb_jsList                  =   ["get_census_callback("+str(swcm.DISPLAY_DOWNLOAD_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_CONFIGURE_CENSUS_DATA)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS)+")",
                                       "get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
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

data_configure_tb_keyTitleList            =   ["Configure</br>Selected</br>Dataset",
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

data_configure_no_datasets_tb_keyTitleList            =   ["Configure</br>Datasets",
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

data_load_datasets_to_df_tb_keyTitleList              =   ["Load/Unload</br>Census</br>Data to df(s)",
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

load_datasets_to_df_no_datasets_tb_keyTitleList       =   ["Load/Unload</br>Datasets</br>to df(s)",
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

load_datasets_to_df_verify_tb_keyTitleList            =   ["Load/Unload</br>Datasets</br>to df(s)",
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

get_dataset_columns_tb_keyTitleList                 =   ["Show</br>Selected</br>Columns","Return","Help"]

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

get_dataset_columns_no_df_tb_keyTitleList           =   ["Load</br>Census</br>Data to df(s)",
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

get_subdata_columns_tb_jsList                       =   ["get_census_callback("+str(swcm.DISPLAY_GET_CENSUS_DATA)+")",
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
insert_cols_in_df_input_idList                  =   ["censusindextype",
                                                     "censusdftoinsertinto",
                                                     "censusdftoinsertintocols",
                                                     "censusindexcols",
                                                     "censusnanvalue",
                                                     None,None,None,None]

insert_cols_in_df_input_labelList               =   ["census_index_type",
                                                     "df_to_insert_into",
                                                     "df_to_insert_into_columns",
                                                     "df_to_insert_index_column(s)",
                                                     "nan_value",
                                                     "Insert</br>Columns</br>into df",
                                                     "Show</br>Selected</br>Columns",
                                                     "Return",
                                                     "Help"]

insert_cols_in_df_input_typeList               =   ["select","select","selectmultiple","text","text",
                                                     "button","button","button","button"]

insert_cols_in_df_input_placeholderList        =   ["census index type",
                                                     "df to insert into",
                                                     "df to insert into columns",
                                                     "census index type",
                                                     "enter the nan vakue eo use (Default : Nan)",
                                                     None,None,None,None]

insert_cols_in_df_input_jsList                 =   [None,None,None,None,None,
                                                    "get_census_callback("+str(swcm.PROCESS_INSERT_CENSUS_COLS)+")",
                                                    "get_census_callback("+str(swcm.SHOW_SELECTED_COLUMNS)+")",
                                                    "get_census_callback("+str(swcm.DISPLAY_MAIN)+")",
                                                    "displayhelp('" + str(dfchelp.DF_CENSUS_INSERT_COL_TO_DF_ID) + "')"]

insert_cols_in_df_input_reqList                =   [0,1,2,3,4]


SWUtility_census_inputs                        =   [insert_cols_in_df_input_id]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                     census data display html
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Census Download Datasets html
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

census_download_html ="""
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

census_download_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

census_download_row_html ="""
                            <tr class="dc-describe-table-body-row">
                                <td style=" width:30%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
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
                                <td style=" width:17%; text-align:center;" class="dccolwrap">
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
                                <td style=" width:13%; text-align:center;" class="dccolwrap">
                                    <div class="input-group-btn" style="padding-right:0px; padding-left:0px; text-align:center;">
                                        <a onclick="get_census_dataset_details('0','XXXDatasetID')">
                                            <img style='margin: 0px auto; text-align:center;' title="XXXTDatasetID Details" src='https://rickkrasinski.github.io/dfcleanser/graphics/census_details.png' height="20px" width="20px" id="CXXXDatasetID"></img>
                                        </a>
                                    </div>
                                </td>
                            </tr>
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









"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                  Census Subset Details html
#--------------------------------------------------------------------------
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


 




                       
                        

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                  Configure Subset Table html
#--------------------------------------------------------------------------
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
                                    <select id="subdatacolnames" multiple="multiple" size="30" style="margin-left:1px; font-size: 11px;" class="form-control" enabled>
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
                            <div style="margin-top:10px;"  id="censusdfinsertcols">
                                <div class="container dc-container dc-default-input-button-container btn-grp-center">
                                    <div class="btn-group btn-center"   style=" width: 100%; ">
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  margin-left: 58px;  height: 75px;  width: 80px; ' onclick="get_census_callback(33)">Insert</br>Columns</br>Into df(s)</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px; ' onclick="get_census_callback(29)">Select</br>More</br>Columns</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px; ' onclick="get_census_callback(0)">Return</button>
                                        <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 80px; ' onclick="displayhelp(https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset)">Help</button>
                                    </div>
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
                                <td style=" width:40%; font-size:12px; text-align:left;" class="dccolwrap"><a href="https://github.com/RickKrasinski/dfc_census_zips/raw/master/housing.zip/XXXfilename" target="_blank">XXXfilename</a></td>               
                                <td style=" width:20%; font-size:12px;" class="dccolwrap">XXXtotalsize</td>
                            </tr>
"""


"""
#--------------------------------------------------------------------------
#                   Configure Verification html
#--------------------------------------------------------------------------
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
#--------------------------------------------------------------------------
#                   Census dfs Loaded html
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

census_loaded_html ="""
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

census_loaded_end_html ="""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""


census_loaded_row_html ="""
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


"""
#--------------------------------------------------------------------------
#                   Census Load Datasets to dfc dfs html
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
                                <th style=" width:32%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">Zip</br>Code</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">City</th>
                                <th style=" width:18%; font-size:13px;" class="dccolhead">County</th>
                                <th style=" width:12%; font-size:13px;" class="dccolhead">&nbsp;US</br>State</th>
                                <th style=" width:14%; font-size:13px;" class="dccolhead">Columns</th>
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
                                <td style=" width:32%; font-size:13px; text-align:left;" class="dccolleft">XXXTDatasetID</td>
                                <td style=" width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" rb0checked disabled>&nbsp;&nbsp;</input>
                                    </div>
                                </td>               
                                <td style="width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" rb1checked disabled></input>
                                    </div>
                                </td>               
                                <td style="width:18%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" rb2checked disabled></input>
                                    </div>
                                </td>               
                                <td style="width:12%;" class="dccolwrap text-center align-middle">
                                    <div class='row'>
                                        <input type='radio' style="padding-left:10px;" name="rbXXXDatasetID" rb3checked disabled></input>
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

configure_notes_info_html="<br><div class='dfcleanser-common-grid-note'>To drop a dataset unselect the checked dataset(s) to drop.<br>To add a dataset select the unchecked dataset(s) you want to add.</div>"
configure_no_select_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:'60%;'>No datasets to configure were selected.<br>To go back and select datasets to configure click on 'Configure Datasets'.</div>"
configure_no_datasets_notes_info_html="<br><div class='dfcleanser-common-grid-note'>No datasets are currently downloaded and processed.</div><br>"


load_datasets_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Load Census Data to df(s) button to laod the datasets as dfc datframes..</div>"
load_datasets_db_html="<br><div class='dfcleanser-common-grid-note'>Once you select datasets to load click on the Define db Connector button to define a db connector and laod the datasets to your database.</div>"
load_datasets_none_html="<br><div class='dfcleanser-common-grid-note'>No census datasets are downloaded for loading into dataframes.</div><br>"


"""
#  Get Census Columns Dataset and Subdata Selects
"""

get_dataset_columns_notes_html="<br><div class='dfcleanser-common-grid-note'>Select a dataset to show subset columns for by ckicking on the correspondng 'Columns' button.</div><br>"
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


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Datasets Details Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""  

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

    
def get_load_datasets_details_html(datasetid=None,subdataid=None,colnameid=None,direction=None) :
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
    
    
    print("get_load_datasets_details_html",datasetid,subdataid,colnameid,direction)
    
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
    

        # append the details table
        load_datasets_details_html  =   (load_datasets_details_html + get_load_subdata_table_html(datasetid,subdataid,colnameid,direction))
        if(subdataid is None) :
            load_datasets_details_html  =   (load_datasets_details_html + census_load_details_end_html)
        else :
            load_datasets_details_html  =   (load_datasets_details_html + census_load_subdata_end_html)        
    
    return(load_datasets_details_html)
    

def get_load_subdata_table_html(datasetid,subdataindex=None,colnameid=None,direction=None) :
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
    
    print("get_load_subdata_table_html",datasetid,subdataindex,colnameid,direction)
    
    census_datasets_details_table     =   ""
    
    subdata_data        =   swcm.get_subset_data_lists(datasetid)
    subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
    subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
    subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]
    
    if(subdataindex is None) :
        
        census_datasets_details_table     =   (census_datasets_details_table + configure_subdata_table_html)

        for i in range(len(subdatacols)) :

            if(not (i==0)) :
            
                row_html    =   configure_subdata_table_row_html
                    
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
        
        census_datasets_details_table     =   (census_datasets_details_table + configure_subdata_table_html_end)

    else :
        
        census_datasets_details_table     =   (census_datasets_details_table + census_colnames_table_html)
        
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
            
            colname     =   swcm.get_colname(subdata_col_names[i+rowstart],70)
                
            row_html    =   row_html.replace("XXXcolname",colname)
            pct_str     =   '{:4.2f}'.format(100 * (subdatacolsnans[nanindices[i+rowstart]]/swcm.total_zips_count))
            row_html    =   row_html.replace("XXXcnamenans",pct_str + "%")
                                             
            census_datasets_details_table     =   (census_datasets_details_table + row_html)

        census_datasets_details_table     =   (census_datasets_details_table + census_colnames_table_html_end)
        
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
            
            census_datasets_details_table     =   (census_datasets_details_table + scroll_html)
            
        #print(load_datasets_details_table)
 
    return(census_datasets_details_table)

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Datasets Download Display functions
#--------------------------------------------------------------------------
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

download_notes_html="<br><div style='text-align:center; margin-left:50px; width:720px; background-color: #F8F5E1; color:#67a1f3; border: 1px solid #67a1f3; word-wrap:break-word'>Please download the zip files highlighted above via clicking on the download links above or go to the <a href='https://github.com/RickKrasinski/dfc_census_zips' target='_blank'>dfc_census_repository</a> directly.<br><br>Download zips to the XXXCensusWorkingDir location. To learn how to change your browser download location click <a href='https://support.google.com/chrome/answer/95759?co=GENIE.Platform%3DDesktop&hl=en' target='_blank'>here.</a></div><br><br><br><br><br>"

def get_datasets_downloaded_list() :
    
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


def display_downloaded_census_data(datasetid=None,subdataid=None,colnameid=None,direction=None) :
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

    print("display_downloaded_census_data",datasetid,subdataid,colnameid,direction)
    
    datasets_loaded_html        =   get_downloaded_census_data_html()
    
    load_details_html           =   get_load_datasets_details_html(datasetid,subdataid,colnameid,direction)

    #load_details_html           =   get_load_datasets_details_html()
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

    print("get_download_datasets_html",forconfigure)    
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

    
def display_configure_census_data(datasetid=None,forconfigure=False,subdataid=None,colnameid=None,direction=None) :
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
    
    print("display_configure_census_data",datasetid,forconfigure,subdataid,colnameid,direction)
    
    
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
                
        configure_details_heading_html       =   "<div>Configure Census Data</div><br>"
                
    else :
        
        if(not(subdataid is None)) :
            configure_notes_html     =   download_notes_subdata_info_html
        else :
            configure_notes_html     =   download_notes_info_html
            
        configure_details_heading_html       =   "<div>Build Census Datasets</div>"
    
    
    
    configure_details_html               =   get_load_datasets_details_html(datasetid,subdataid,colnameid,direction)
    


    if(forconfigure) :
        
        #print("get_datasets_processed",get_datasets_processed())
        
        if(any_datasets_processed(get_datasets_processed())) :
        
            configure_data_tb        =   ButtonGroupForm(data_configure_tb_id,
                                                    data_configure_tb_keyTitleList,
                                                    data_configure_tb_jsList,
                                                    data_configure_tb_centered)
    
            configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":225})
        
            configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Configure")
            
        else :
            
            configure_data_tb        =   ButtonGroupForm(data_configure_no_datasets_tb_id,
                                                    data_configure_no_datasets_tb_keyTitleList,
                                                    data_configure_no_datasets_tb_jsList,
                                                    data_configure_no_datasets_tb_centered)
            
            configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":100, "left-margin":32})
        
            configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Configure")
            
        
        configure_data_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":210})
        
        configure_census_html    =   configure_census_html.replace("Census Datasets","Census Datasets To Build")
                        
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
        
        """
        import os,json
        cfgdir = os.path.join(cfg.get_notebook_path(),cfg.get_notebook_name()+"_files")
        cfgfilename = os.path.join(cfgdir,cfg.get_notebook_name()+"_load_details.html")
        with open(cfgfilename, 'w') as cfg_file :
            json.dump(load_details_html,cfg_file)
            cfg_file.close()
        """
        
        #print(load_census_html)
        #print(load_notes_html)
        #print(load_details_html)
        #print(load_data_tb_html)        
    
    
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

datasets_to_load_verification_html ="""
        <div class='container dc-tbl-container' style="width:100%;" id="dfCensusLoadOptions">
            <div class="panel panel-primary" style="border:0;">
                <div class="panel-heading clearfix dc-table-panel-heading" style="width:100%;">
                    <div class="input-group">
                        <div class="input-group-btn">
                            <div class="input-group-btn">
                                <p class="panel-title pull-left" style="padding-right:20px;">Census Datasets df(s) To Unload</p>
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

datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>To Add/Drop datasets selected click on the Add/Drop Selected Datasets.</div><br>"
verify_datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>To Load/Unload datasets selected click on the Load/Unload Selected Datasets.</div><br>"
verify_no_datasets_to_load_process_html="<div class='dfcleanser-common-grid-note'>No datasets selected to Load or Unload.</div><br>"


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



datasets_in_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To load a dataset to a df check the dataset that is not currently checked.<br>To delete a dataset df uncheck a currently checked box.</div>"
export_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To export a dataset click on the export icon above.</div>"
load_to_db_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>To load a dataset to a db click on the load to db icon above.</div>"

no_export_dfs_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>No census datasets loaded to df(s) for export.</div>"
no_load_to_db_notes_info_html="<div class='dfcleanser-common-grid-note' style='width:480px; margin-left:45px;'>No census datasets loaded to df(s) for load to a db.</div>"



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

    print("display_datasets_loaded_to_dfs")    

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

    print("display_datasets_loaded_to_dfs")    

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

    print("get_datasets_loaded_to_dfs_html")    
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

    print("display_datasets_loaded_to_dfs")    

    loaded_dfs_html             =   get_datasets_loaded_to_dfs_html()
    loaded_dfs_html             =   loaded_dfs_html.replace('Census Datasets','Datasets Loaded To df(s)')
    loaded_dfs_html             =   loaded_dfs_html.replace("dc-tbl-container' style='width:360px;","dc-tbl-container' style='width:540px;")
    loaded_dfs_html             =   loaded_dfs_html.replace('width:360px;','width:540px;')

    loaded_dfs_heading_html     =   "<div>Load Census Datasets To df(s)</div><br>"
    
    loaded_dfs_notes_html       =   datasets_in_dfs_notes_info_html
    
    loaded_dfs_tb               =   ButtonGroupForm(data_load_datasets_to_df_tb_id,
                                                    data_load_datasets_to_df_tb_keyTitleList,
                                                    data_load_datasets_to_df_tb_jsList,
                                                    data_load_datasets_to_df_tb_centered)
            
    loaded_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":100, "left-margin":75})
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

    #print("get_configure_datasets_verification_html\n",datasets_to_configure,"\n\n",datasets_processed)
    
    add_ds_html     =   datasets_to_load_verification_html
    add_ds_html     =   add_ds_html.replace("df(s) To Unload","To Load to df(s)")
    drop_ds_html    =   datasets_to_load_verification_html 
    
    add_datasets    =   []
    drop_datasets   =   []
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()
    
    print("datasets_loaded_to_dfs",datasets_loaded_to_dfs)
    
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
    print("display_load_to_df_verification_data",datasets_to_load_to_dfs)
    
    [datasets_to_load_to_df_html,datasets_to_unload_to_df_html]    =   get_datasets_to_load_verification_html(datasets_to_load_to_dfs)
    
    print("any_datasets_to_load_to_dfs",any_datasets_to_load_to_dfs(datasets_to_load_to_dfs),any_datasets_to_unload_from_dfs(datasets_to_load_to_dfs))
    
    if( (any_datasets_to_load_to_dfs(datasets_to_load_to_dfs)) or 
        (any_datasets_to_unload_from_dfs(datasets_to_load_to_dfs)) ) :
        
        loaded_to_dfs_notes_html       =   verify_datasets_to_load_process_html
        
        loaded_to_dfs_tb               =   ButtonGroupForm(load_datasets_to_df_verify_tb_id,
                                                           load_datasets_to_df_verify_tb_keyTitleList,
                                                           load_datasets_to_df_verify_tb_jsList,
                                                           load_datasets_to_df_verify_tb_centered)
    
        loaded_to_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":240})
        loaded_to_dfs_tb_html          =   loaded_to_dfs_tb.get_html()

        
    else :
        
        loaded_to_dfs_notes_html       =   verify_no_datasets_to_load_process_html
        
        loaded_to_dfs_tb               =   ButtonGroupForm(load_datasets_to_df_no_datasets_tb_id,
                                                           load_datasets_to_df_no_datasets_tb_keyTitleList,
                                                           load_datasets_to_df_no_datasets_tb_jsList,
                                                           load_datasets_to_df_no_datasets_tb_centered)
    
        loaded_to_dfs_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":240})
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







"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#           Census Datasets Loaded into dfs Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
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
    
    print("get_census_dfs_loaded_html",fordbexport)
    
    dfc_loaded_datasets_html  =   ""
    
    dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + census_loaded_html) 
    
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
        row_html    =   (row_html + census_loaded_row_html)
        row_html    =   row_html.replace("XXXXDatasetID","&nbsp;")
        row_html    =   row_html.replace("XXXXfilename","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No Census df(s) currently loaded")
        
        dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + row_html) 
            
    print("dfs_dict",dfs_dict)

    if(len(dfs_dict) == 0) :
        
        row_html    =   ""
        row_html    =   (row_html + census_loaded_row_html)
        row_html    =   row_html.replace("XXXXDatasetID","&nbsp;")
        row_html    =   row_html.replace("XXXXfilename","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No Census df(s) currently loaded")
        
        dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + row_html) 

    else :
        
        dfs_dict_list   =  list(dfs_dict.keys()) 
        
        for i in range(len(dfs_dict_list)) :
            
            current_dfs_list    =   dfs_dict.get(dfs_dict_list[i]) 
            
            print("current_dfs_list",current_dfs_list)
            
            for j in range(len(current_dfs_list)) :
                
                row_html    =   ""
                row_html    =   (row_html + census_loaded_row_html)
                
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
            
            
    dfc_loaded_datasets_html  =   (dfc_loaded_datasets_html + census_loaded_end_html) 
            
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
    
    print(dfs_loaded_html)
    print(dfs_loaded_note)
    
    print("\n")
    display_generic_grid("dfcensus-loaded-dfs-wrapper",gridclasses,gridhtmls)
    print("\n")











"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#           Datasets Configuration Verification Display functions
#--------------------------------------------------------------------------
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
                                <th style=" width:65%; font-size:13px; text-align:left;" class="dccolheadleft">Dataset</th>
                                <th style=" width:35%; font-size:13px; text-align:left;" class="dccolheadleft">Downloaded</th>
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
                                <td style=" width:65%; font-size:13px; text-align:left;" class="dccolleft">XXXDatasetID</td>
                                <td style=" width:35%; font-size:13px; text-align:left;" class="dccolleft">XXXFileName</td>               
                            </tr>
"""

configure_process_html="<div class='dfcleanser-common-grid-note'>To Add/Drop datasets selected click on the Add/Drop Selected Datasets.<br>Any datasets highlighted must be downloaded before being added.</div><br>"




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

    #print("get_configure_datasets_verification_html\n",datasets_to_configure,"\n\n",datasets_processed)
    
    add_ds_html     =   configure_verification_html
    add_ds_html     =   add_ds_html.replace("To Drop","To Add")
    drop_ds_html    =   configure_verification_html 
    
    add_datasets    =   []
    drop_datasets   =   []
    
    datasets_downloaded     =   get_datasets_downloaded_list()

    
    for i in range(len(datasets_to_configure)) :
        
        for j in range(4) :
            
            if(datasets_to_configure[i][j] == "True") :
                
                if(not (datasets_processed[i][j])) :
                    
                    row_html    =   configure_verification_row_html
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
                    
                    row_html    =   configure_verification_row_html
                    row_html    =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                    
                    row_html    =   row_html.replace("XXXFileName"," ") 
                                    
                    drop_ds_html   =   (drop_ds_html + row_html)
                    
                    drop_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
                
    
    add_ds_html   =   (add_ds_html + configure_verification_end_html)  
    #print(add_ds_html)
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
    #print("display_configure_verification_data\n",datasets_to_configure,"\n",datasets_processed)
    
    [configure_drop_datset_html,configure_add_datset_html]    =   get_configure_datasets_verification_html(datasets_to_configure,datasets_processed)
    
    
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
#--------------------------------------------------------------------------
#                   Get Dataset Columns Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_colnames_for_get_cols_html(datasetid,subdataindex,forselects=False,forinserts=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get colnames for a subset
    * 
    * parms :
    *
    *   datasetid       -   dataset id
    *   subdataindex    -   subset id
    *   forselects      -   for selects flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    print("\n\nget_colnames_for_get_cols_html",datasetid,subdataindex,forselects,forinserts)
    
    get_cols_colnames_html  =   ""
    get_cols_colnames_html  =   (get_cols_colnames_html + get_cols_colnames_table_html)
    
    if(datasetid is None) :
        
        row_html    =   get_cols_colnames_table_row_html
        row_html    =   row_html.replace("XXXColname","&nbsp;")
        row_html    =   row_html.replace("XXXSColname","No columns selected")
            
        get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)       
        
    else :
    
        subdata_data            =   swcm.get_subset_data_lists(datasetid)
        subdatacols             =   subdata_data[swcm.SUBSET_COLUMNS] 
        
        #print("subdatacols",subdatacols)
    
        if( (forinserts) or (forselects) ):
            get_cols_colnames_html  =   get_cols_colnames_html.replace("width:540px;","width:480px;")

        if( (forinserts) or (forselects) ):
            
            all_subdata_col_names   =   subdatacols[subdataindex]
            subdata_col_names       =   [] 
            
            
            print("all_subdata_col_names",all_subdata_col_names)
            
            #old versioninsert_cols_dict        =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID)
            #old versioninsert_dataset_dict     =   insert_cols_dict.get(datasetid,None)
            
            insert_dataset_dict     =   swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_dataset(datasetid)
            
            print("insert_dataset_dict",insert_dataset_dict)
            
            if(not (insert_dataset_dict is None)) :
                insert_cols_list    =   insert_dataset_dict.get(int(subdataindex),None)
                
                print("insert_cols_list",insert_cols_list)
                
                if(not (insert_cols_list is None)) :
                    if(insert_cols_list[0] == -1):#"All") :
                        subdata_col_names.append("All") 
                        get_cols_colnames_html  =   get_cols_colnames_html.replace('multiple="multiple" size="30"','multiple="multiple" size="2"')
                    else :
                        for i in range(len(insert_cols_list)) :
                            subdata_col_names.append(all_subdata_col_names[i])    
            
        else :
            subdata_col_names       =   subdatacols[subdataindex]
            
        print("\nsubdata_col_names",subdata_col_names,"\n")

        get_cols_colnames_html  =   get_cols_colnames_html.replace("XXXColumnsTitle",("* " + datasetid + " : " + swcm.get_subdata_name(datasetid,int(subdataindex)) + " column names")) 

        if(forselects)   :
        
            # old version dataset_cols_dict    =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID)
            dataset_cols_dict    =   swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_to_load_in_df()
            print("get_colnames_for_get_cols_html - dataset_cols_dict : start",dataset_cols_dict)
        
            if(dataset_cols_dict is None) :
                selects     =   []
            else :
        
                # old versioin subdata_cols_dict    =  dataset_cols_dict.get(datasetid)
                subdata_cols_dict    =  swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_dataset(datasetid)
                
                if(subdata_cols_dict is None) :
                    selects     =   []
                else :
                    selects     =   subdata_cols_dict.get(subdataindex,[])
        
            print("selects",selects)
            
        else :
            
            if(not (forinserts)) :
                row_html    =   get_cols_colnames_table_row_html
                row_html    =   row_html.replace("XXXColname",str(-1))#subdata_col_names[i])
                row_html    =   row_html.replace("XXXSColname","All")
        
                get_cols_colnames_html     =   (get_cols_colnames_html +  row_html) 
            
    
        print("\nget_colnames_for_get_cols_html subdata_col_names",subdata_col_names,len(subdata_col_names))
        #print("\nget_colnames_for_get_cols_html selects",selects,len(selects))
        
        if( (forselects) or (forinserts) ) :
                
            sellen  =   len(subdata_col_names) + 1
            if(sellen > 30) :
                sellen = 30
            get_cols_colnames_html  =   get_cols_colnames_html.replace('multiple="multiple" size="30"','multiple="multiple" size="' + str(sellen) +'"')
            get_cols_colnames_html  =   get_cols_colnames_html.replace("enabled","disabled")
        
        
        for i in range(len(subdata_col_names)) :
        
            if(forselects) :
                
                if(len(selects) == 0) :
        
                    row_html    =   get_cols_colnames_table_row_html
                    colname     =   swcm. get_colname(subdata_col_names[i],70)
                    row_html    =   row_html.replace("XXXColname",str(i))#subdata_col_names[i])
                    row_html    =   row_html.replace("XXXSColname",colname)
            
                    get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)       
                
                else :
                
                    if( (len(selects) == 1) and (selects[0] == -1)) :
                    
                        row_html    =   get_cols_colnames_table_row_html
                        colname     =   "All"
                        row_html    =   row_html.replace("XXXColname",str(i))#subdata_col_names[i])
                        row_html    =   row_html.replace("XXXSColname",colname)
            
                        get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)       
                    
                    else :
                
                        if(1):#i in selects) :
                            
                            print("i in selects",i)

                            row_html    =   get_cols_colnames_table_row_html
                            colname     =   swcm.get_colname(subdata_col_names[i],70)
                            row_html    =   row_html.replace("XXXColname",str(i))#subdata_col_names[i])
                            row_html    =   row_html.replace("XXXSColname",colname)
            
                            get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)  
                            
                
                
            else :  
                
                if(forinserts) :
                    print("forinserts : ",subdata_col_names[i])
                    colname     =   swcm.get_colname(subdata_col_names[i],70)
                    
                else :
                    colname     =   swcm.get_colname(subdata_col_names[i],90)
                    

                row_html    =   get_cols_colnames_table_row_html

                if(forinserts) :
                    
                    if(colname == "All") :
                        row_html    =   row_html.replace("XXXColname",str(-1))
                    else :
                        row_html    =   row_html.replace("XXXColname",str(i))
                        
                else :
                    row_html    =   row_html.replace("XXXColname",str(i))#subdata_col_names[i])
                    
                row_html    =   row_html.replace("XXXSColname",colname)
        
                get_cols_colnames_html     =   (get_cols_colnames_html +  row_html)       

    if(forselects) :
        get_cols_colnames_html     =   (get_cols_colnames_html + get_cols_colnames_table_selects_end_html) 
    else :
        get_cols_colnames_html     =   (get_cols_colnames_html + get_cols_colnames_table_end_html)
     
    return(get_cols_colnames_html)




def display_dataset_columns_selected(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get dataset columns selected html
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    print("get_dataset_columns_selected_table_html",parms)
    
    get_selected_cols_heading_html       =   "<div>Census Column(s) Selected</div><br></br>"

    subsets_html    =   ""
    subsets_html    =   (subsets_html + selected_columns_table_html)
    
    # old version dataset_cols_dict    =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID)
    dataset_cols_dict    =   swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_to_load_in_df()
        
    print("get_dataset_columns_selected_table_html - dataset_cols_dict : start",dataset_cols_dict)
        
    if(dataset_cols_dict is None) :
        
        loadnotes = ["No subset columns defined"]
        display_notes(loadnotes,display=True)
        
        cfg.drop_config_value(cfg.CENSUS_SELECTED_DATASET_ID)
        cfg.drop_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)
        
    else :
        
        # old version select_columns_datasets    =   list(dataset_cols_dict.keys())
        select_columns_datasets    =   swcm.dfc_census_columns_selected.get_datasets_selected_to_load_in_df_list()
        print("\nselect_columns_datasets",select_columns_datasets,len(select_columns_datasets))
        
        if(parms is None) :
            
            datasetid   =   select_columns_datasets[0]
            subsetid    =   1
            
        else :
            
            datasetid   =   parms[0]
            subsetid    =   int(parms[1])
            
        print("\ndisplay_dataset_columns_selected",datasetid,subsetid)
        
        for i in range(len(select_columns_datasets)) : 
            
            if(not (i == 0)) :
                subsets_html   =   (subsets_html + selected_columns_blank_line_html)  
                
            subsets_html    =   (subsets_html + selected_columns_dataset_row_html)
            subsets_html    =   subsets_html.replace("XXXXDATASET",select_columns_datasets[i]) 
                
            # old version select_columns_subsets_dict     =   dataset_cols_dict.get(select_columns_datasets[i])
            select_columns_subsets_dict     =   swcm.dfc_census_columns_selected.get_dataset_subsets_selected_to_load_in_df_list(select_columns_datasets[i])
            select_columns_subsets_keys     =   list(select_columns_subsets_dict.keys())
                        
            print("\nselect_columns_datasets : ",i,select_columns_datasets[i])

            print("\nselect_columns_subsets_dict",select_columns_subsets_dict)
            print("\nselect_columns_subsets_keys",select_columns_subsets_keys)
            select_columns_subsets_keys.sort()
            
            subdata_lists   =   swcm.get_subset_data_lists(select_columns_datasets[i])
            
            #print("subdata_lists",subdata_lists)
            
            subdata_titles  =   subdata_lists[swcm.SUBSET_COLUMN_NAMES]
            
            print("subdata_titles",subdata_titles)
            
            for j in range(len(select_columns_subsets_keys)) :
                
                subset_columns_list     =    select_columns_subsets_dict.get(select_columns_subsets_keys[j]) 
                
                print("\nsubset_columns_list : ",select_columns_subsets_keys[j],subset_columns_list)
            
                subsets_html    =   (subsets_html + selected_columns_subset_row_html)
                
                if(subset_columns_list[0] == -1) :
                    subsets_html    =   subsets_html.replace("XXXXSUBSETCOUNT","All")            
                else :
                    subsets_html    =   subsets_html.replace("XXXXSUBSETCOUNT",str(len(subset_columns_list)))
                
                subsets_html    =   subsets_html.replace("XXXXSUBSETTITLE",subdata_titles[select_columns_subsets_keys[j]])
                
                subsets_html    =   subsets_html.replace("XXXXSUBSETID",str(select_columns_subsets_keys[j]))
                    
                subsets_html    =   subsets_html.replace("XXXXSUBSET",subdata_titles[select_columns_subsets_keys[j]])
                    
                subsets_html    =   subsets_html.replace("XXXXDATASETID",select_columns_datasets[i])
    
        subsets_html    =   (subsets_html + selected_columns_table_html_end) 
    
        select_columns_subsets_dict     =   dataset_cols_dict.get(select_columns_datasets[0]) 
        select_columns_subsets_keys     =   list(select_columns_subsets_dict.keys())
    
        colnames_html   =   get_colnames_for_get_cols_html(datasetid,subsetid,forselects=True)
    
        cfg.set_config_value(cfg.CENSUS_SELECTED_DATASET_ID,datasetid)
        cfg.set_config_value(cfg.CENSUS_SELECTED_SUBSET_ID,subsetid)
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [get_selected_cols_heading_html,subsets_html,colnames_html]
    
        print(subsets_html)
        print(colnames_html)
    
        print("\n")
        display_generic_grid("dfcensus-show-selects-wrapper",gridclasses,gridhtmls)
        print("\n")



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Insert Columns Display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
NO_USER_DFS             =   0
NO_DATASETS_LOADED      =   1


def display_columns_to_insert(dftitle=None) :
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
    
    datasetid           =   cfg.get_config_value(cfg.CENSUS_SELECTED_DATASET_ID)
    subsetid            =   cfg.get_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)

    print("display_columns_to_insert",datasetid,subsetid,dftitle)    
    invalid_cfg_code    =   None
    
    from dfcleanser.common.html_widgets import InputForm
    insert_cols_input_form = InputForm(insert_cols_in_df_input_id,
                                       insert_cols_in_df_input_idList,
                                       insert_cols_in_df_input_labelList,
                                       insert_cols_in_df_input_typeList,
                                       insert_cols_in_df_input_placeholderList,
                                       insert_cols_in_df_input_jsList,
                                       insert_cols_in_df_input_reqList)
    
    selectDicts             =   []
    
    index_types  =   []   
    
    datasets_processed  =   get_datasets_processed()
        
    print("datasets_processed",datasets_processed)
    
    if(datasets_processed[swcm.get_datasetid_offset(datasetid)][0]) :
        index_types.append("[zipcode]")
    if(datasets_processed[swcm.get_datasetid_offset(datasetid)][1]) :
        index_types.append("[city,state]")
    if(datasets_processed[swcm.get_datasetid_offset(datasetid)][2]) :
        index_types.append("[county,state]")
    if(datasets_processed[swcm.get_datasetid_offset(datasetid)][3]) :
        index_types.append("[state]")

    print("\nindex_types",index_types) 
    
    if(len(index_types) > 0) :
        
        index_types_list    =   index_types
        index_types_default =   None
        subdata_name        =   swcm.get_subdata_name(datasetid,subsetid)
        
    else :
        
        invalid_cfg_code    =   NO_DATASETS_LOADED

    if(invalid_cfg_code is None) :
    
        index_types_dict    =   {"default":index_types_default,"list":index_types_list,"callback":"select_new_insert_df_index_type"}
        selectDicts.append(index_types_dict)
    
        non_census_df_titles    =   []
    
        df_titles   =   cfg.get_dfc_dataframes_titles_list()
    
        if(not (df_titles is None)) :
    
            for i in range(len(df_titles)) :
        
                if(not( ((swcm.census_data_dirs[i] + "_zipcode" + "_df") in df_titles) or 
                        ((swcm.census_data_dirs[i] + "_cities" + "_df") in df_titles) or 
                        ((swcm.census_data_dirs[i] + "_counties" + "_df") in df_titles) or 
                        ((swcm.census_data_dirs[i] + "_states" + "_df") in df_titles)  )) :
            
                    non_census_df_titles.append(df_titles[i])
        
        print("\nnon_census_df_titles",non_census_df_titles)
    
        #if(df_titles is None) :
        if(len(non_census_df_titles) > 0) :
        
            if(dftitle is None) :
                df_default          =   non_census_df_titles[0]
            else :
                df_default          =   dftitle
            
            dfs                 =   non_census_df_titles
            df                  =   cfg.get_dfc_dataframe_df(non_census_df_titles[0])
            colslist            =   df.columns.tolist()
            cols_default        =   None
        
        else : 
        
            invalid_cfg_code    =   NO_USER_DFS
        
        if(invalid_cfg_code is None) :
        
            dfs_dict        =   {"default":df_default,"list":dfs,"callback":"select_new_insert_df"}
            selectDicts.append(dfs_dict)
    
            df_cols_dict    =   {"default":cols_default,"list":colslist,"callback":"select_new_insert_df_col"}
            selectDicts.append(df_cols_dict)
    
            print("\ndfs_dict",dfs_dict)
            print("\ndf_cols_dict",df_cols_dict)
            print("\ndf_titles",df_titles)    
            
            get_select_defaults(insert_cols_input_form,
                                insert_cols_in_df_input_id,
                                insert_cols_in_df_input_idList,
                                insert_cols_in_df_input_typeList,
                                selectDicts)
                    
            insert_cols_input_form.set_shortForm(True)
            insert_cols_input_form.set_gridwidth(360)
            insert_cols_input_form.set_custombwidth(85)
            insert_cols_input_form.set_fullparms(True)
    
            cfg.set_config_value(insert_cols_in_df_input_id+"Parms",[subdata_name,df_default,cols_default,index_types_default,"",""])
    
            if(invalid_cfg_code) :
                cfg.set_config_value(insert_cols_in_df_input_id+"ParmsProtect",["True","True","True","True","True","True"])
            else :
                cfg.set_config_value(insert_cols_in_df_input_id+"ParmsProtect",["True","False","False","False","False","False"])
        
            insert_cols_input_html = insert_cols_input_form.get_html()
    
            insert_cols_heading_html       =   "<div>Insert Census Columns into df</div>"
    
            colnames_html   =   get_colnames_for_get_cols_html(datasetid,subsetid,forselects=False,forinserts=True)
    
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
            gridhtmls       =   [insert_cols_heading_html,insert_cols_input_html,colnames_html]
    
            print(insert_cols_input_html)
            print(colnames_html)
    
            print("\n")
            display_generic_grid("dfcensus-show-selects-wrapper",gridclasses,gridhtmls)
            print("\n")
            
    if( not (invalid_cfg_code is None)) :
        
        if(invalid_cfg_code == NO_USER_DFS) :
            loadnotes = ["No user dfs defined to load census columns into"]
        elif(invalid_cfg_code == NO_DATASETS_LOADED) :
            loadnotes = ["No census datasets downloaded and built for " + datasetid]
        
        display_notes(loadnotes,display=True)
            
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                   Dataset Details Display functions
#--------------------------------------------------------------------------
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
    print("get_dataset_columns_html")
    
    load_datasets_html  =   ""
    load_datasets_html  =   (load_datasets_html + census_get_cols_for_df_html)  
    
    datasets_loaded     =   get_datasets_processed()
    
    print("get_dataset_columns_html",datasets_loaded)
    
    if(not(datasets_loaded is None)) :
    
        for i in range(len(swcm.census_data_dirs)) : 
            
            #print("any_dataframes_loaded_for_dataset",datasets_loaded)
            
            if(1):#any_dataframes_loaded_for_dataset(swcm.census_data_dirs[i])) :
                
                dsid                =   swcm.census_datasets[i]
                dsid                =   dsid.replace("_"," ")
                row_html            =   census_get_cols_for_df_row_html.replace("XXXTDatasetID",dsid)
                row_html            =   row_html.replace("XXXDatasetID",swcm.census_data_dirs[i])
            
                for j in range(4)  : 
                
                    if(j==0)        :   
                        #dftype  =   "zipcode"
                        cbchk   =   "rb0checked"
                            
                    elif(j==1)      :   
                        #dftype  =   "cities" 
                        cbchk   =   "rb1checked"
                            
                    elif(j==2)      :   
                        #dftype  =   "counties" 
                        cbchk   =   "rb2checked"
                            
                    elif(j==3)      :   
                        #dftype  =   "states"
                        cbchk   =   "rb3checked"
                        
                    if(not (datasets_loaded[i][j])) :
                        row_html            =   row_html.replace(cbchk,"")
                    else :
                        row_html            =   row_html.replace(cbchk,"checked")

                load_datasets_html  =   (load_datasets_html + row_html)    
    
    load_datasets_html  =   (load_datasets_html + census_get_cols_for_df_end_html)

    return(load_datasets_html)


def display_get_dataset_columns(datasetid=None,excludes=None,subdataid=None) :
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
    print("display_get_dataset_columns",datasetid,excludes,subdataid)
    
    if(datasetid is None) :
        
        get_dataset_cols_html       =   get_dataset_columns_html()
        get_dataset_cols_html       =   get_dataset_cols_html.replace("Census Datasets","Census Datasets Loaded") 
        
        get_dataset_notes_html      =   get_dataset_columns_notes_html 
            
        get_dataset_columns_tb      =   ButtonGroupForm(get_dataset_columns_tb_id,
                                                        get_dataset_columns_tb_keyTitleList,
                                                        get_dataset_columns_tb_jsList,
                                                        get_dataset_columns_tb_centered)
            
        get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":110, "left-margin":100})
        get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
    else :
        
        if(subdataid is None) :
            
            print("display_get_dataset_columns : all subset ids",datasetid,excludes,subdataid)
       
            get_dataset_cols_subdata_html   =   get_dataset_columns_subdata_table_html(datasetid,excludes,True)
        
            get_dataset_notes_html          =   get_dataset_cols_subdata_list_notes_html 
            
            get_dataset_columns_tb          =   ButtonGroupForm(get_subdata_columns_tb_id,
                                                                get_subdata_columns_tb_keyTitleList,
                                                                get_subdata_columns_tb_jsList,
                                                                get_subdata_columns_tb_centered)
                        
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":85, "left-margin":100})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            
        else :
            
            print("display_get_dataset_columns : subset ids",datasetid,excludes,subdataid)
            
            get_dataset_cols_subdata_html   =   get_colnames_for_get_cols_html(datasetid,subdataid)
        
            get_dataset_notes_html          =   get_dataset_cols_columns_list_notes_html 
            
            get_dataset_columns_tb          =   ButtonGroupForm(get_col_names_list_tb_id,
                                                                get_col_names_list_tb_keyTitleList,
                                                                get_col_names_list_tb_jsList,
                                                                get_col_names_list_tb_centered)
                        
            get_dataset_columns_tb.set_customstyle({"font-size":13, "height":75, "width":85, "left-margin":100})
            get_dataset_columns_tb_html =   get_dataset_columns_tb.get_html()
            

    if(datasetid is None) :
        
        get_cols_heading_html       =   "<div>Select Census Dataset To Get Census Column(s) from</div><br></br>"

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main","dfc-footer","dfc-bottom"]
        gridhtmls       =   [get_cols_heading_html,get_dataset_cols_html,get_dataset_notes_html,get_dataset_columns_tb_html]
        
        #print(get_dataset_cols_html)
        #print(get_dataset_notes_html)
        
    else :
        
        if(subdataid is None) :
            get_cols_heading_html       =   "<div>Select Census Dataset Columns</div><br></br>"
        else :
            get_cols_heading_html       =   "<div>Select Column Names from Census Subset</div><br></br>"

        #print(get_dataset_cols_subdata_html)
        #print(get_dataset_notes_html)


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
    print("display_get_census_columns",datasetid,dsdtype,subdataid,colslist)
    """
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
    """    


short_note_html="<div style='text-align:center; margin-left:40px; width:360px; background-color: #F8F5E1; color:#67a1f3; border: 1px solid #67a1f3; word-wrap:break-word'>XXXNote</div>"

def display_short_note(msg) :
    
    note_html   =   short_note_html.replace("XXXNote",msg)
    
    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [note_html]
    
    display_generic_grid("dfcensus-short-note-wrapper",gridclasses,gridhtmls)
        


    
    
    