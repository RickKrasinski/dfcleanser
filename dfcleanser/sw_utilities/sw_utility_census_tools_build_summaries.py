"""
# sw_utility_census_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue June 6 16:00:00 2019

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_census_model as swcm
import dfcleanser.sw_utilities.sw_utility_census_widgets as swcw


from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (display_exception, display_status, opStatus, get_parms_for_input,  
                                            is_numeric_col, is_int_col, single_quote, RunningClock,
                                            get_dtype_str_for_datatype)



toc_html    =   """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0042)file:///C:/Downloads/dfcleanser_index.html -->
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=Edge">

    <!--<title>pandas.to_datetime — pandas 0.25.3 documentation</title>-->
    <title>Pandas Dataframe Cleanser System Environment</title>
    <link rel="stylesheet" href="https://rickkrasinski.github.io/dfcleanser/help/nature.css" type="text/css">
    <link rel="stylesheet" href="https://rickkrasinski.github.io/dfcleanser/help/pygments.css" type="text/css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="https://rickkrasinski.github.io/dfcleanser/dfcleanser/static/dfc_styles.css" type="text/css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://rickkrasinski.github.io/dfcleanser/dfcleanser/static/help.js"></script>
</head>

<body>
    <div id="MathJax_Message" style="display: none;"></div>

    <div class="content-wrapper">
        <div class="content">
            <div class="document">

                <div class="sphinxsidebar">
                    <h3>Table Of Contents</h3>
                    <ul class="current">
                        <li class="toctree-l1"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-index.html">Dataframe Cleanser Intro</a></li>
                        <li class="toctree-l1"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-index.html#pandas_dfc_install">Installation</a></li>
                        <li class="toctree-l1"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-index.html#pandas_dfc_get_started">Getting started</a></li>
                        <li class="toctree-l1 current">User Guide</li>
                        <ul class="current">
                            <li class="toctree-l2"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html">System Environment</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html#dfc_Utilities_manager">Utilities Manager</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html#dfc_dataframe_manager">dataframe Manager</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html#dfc_system_system">System</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html#dfc_system_about">About</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html#dfc_system_eula">EULA</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2 current"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html">Data Import</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_files">Files</a></li>
                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_csv">CSV File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_fwf">Fixed Width File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_excel">Excel File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_json">JSON  File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_html">HTML File</a></li>
                                    </ul>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql">SQL</a></li>

                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql_libs">SQL Libs</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql_connect">SQL Connections</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql_table">SQL Table</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql_query">SQL Query</a></li>
                                    </ul>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_custom_import">Custom</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html">Data Inspection</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html#dfc_data_inspection_datatypes">Data Types</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html#dfc_data_inspection_nans">Nans</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html#dfc_data_inspection_rows">Rows</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html#dfc_data_inspection_categories">Columns</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-inspection.html#dfc_data_inspection_categories">Categories</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-cleansing.html">Data Cleansing</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-cleansing.html#dfc_data_cleansing_numeric">Cleanse Numeric Column</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-cleansing.html#dfc_data_cleansing_non_numeric">Cleanse Non Numeric Columns</a></li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-cleansing.html#dfc_data_cleansing_row">Cleanse Row</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html">Data Transform</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dataframe_transform">dataframe Transform</a>
                                        <ul class="current">
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_dataframe_transform_column_names_row">Column Names Row</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_dataframe_transform_index">Single Level dataframe Indices</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_dataframe_transform_sort">Sort df by Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_dataframe_transform_drop_duplicates">Drop Duplicate Rows</a></li>
                                        </ul>
                                    </li>
                                    <li class="toctree-l3"><a class="reference internal" href="./dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform">columns Transform</a>
                                        <ul class="current">
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_rename">Rename Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_add">Add Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_drop">Drop Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_reorder">Reorder Columns</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_save">Save Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_copy">Copy Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_apply_fn">Apply fn To Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_map">Map Columns</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_dummies">Dummies For Column</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_categorical">Make Column Categorical</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform-columns.html#dfc_data_transform_columns_transform_change_datatype">Change Column Datatype</a></li>
                                        </ul>
                                    </li>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime">datetime Transform</a>
                                        <ul class="current">
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_convert">Convert Column to datetime</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_convert_timedelta">Convert Column to timedelta</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_convert_timedelta">Calculate timedelta Cloumn</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_merge">Split Column to date, time Columns</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_merge">Merge Column from date, time Columns</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-transform.html#dfc_data_transform_columns_transform_datetime_components">Get datetime Components Column</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="toctree-l2 current"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-export.html">Data Export</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_files">Files</a></li>
                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_csv">CSV File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_excel">Excel File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_json">JSON  File</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_html">HTML File</a></li>
                                    </ul>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_import_pandas_sql">SQL</a></li>

                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_sql_libs">SQL Libs</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_sql_connect">SQL Connections</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_sql_table">SQL Table</a></li>
                                    </ul>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html#dfc_data_export_pandas_custom_import">Custom</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html">Software Utilities</a>
                                <ul class="current">
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_data_structures">Common Data Structures</a></li>
                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_data_structures_lists">Lists</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_data_structures_dicts">Dicts</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_data_structures_dfc_funcs">Functions</a></li>
                                    </ul>
                                    <li class="toctree-l3"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding">Geocoding</a></li>
                                    <ul class="current">
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_select_geocoder">Geocoder Service</a></li>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_interactive">Interactive Geoocoding</a></li>
                                        <ul class="current">
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_interactive">Geocoding</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_interactive_reverse">Reverse Geocoding</a></li>
                                        </ul>
                                        <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk">Bulk Geocoding</a></li>
                                        <ul class="current">
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_geocoding_geocoding">Geocoding</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_geocoding_reverse">Reverse Geocoding</a></li>
                                            <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console">Console</a></li>
                                            <ul class="current">
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_states">States</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_progress_bars">Progress</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_checkpoint">Checkpointing</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_errors">Errors</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_limits">Limits</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_results">Results</a></li>
                                                <li class="toctree-l4"><a class="reference internal" href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_bulk_console_pricing">Pricing</a></li>
                                            </ul>
                                        </ul>
                                        <li class="toctree-l4">
                                            <a class="reference internal" href=https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_utilities ">Geocode Utilities</a></li>
                                        <ul class="current ">
                                            <li class="toctree-l4 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_utilities_interactive_distance ">Geocode Distance</a></li>
                                            <li class="toctree-l4 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_utilities_interactive_center ">Center Point</a></li>
                                            <li class="toctree-l4 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_geocoding_utilities_distance_from_center ">Distance From Center Point</a></li>
                                        </ul>
                                    </ul>
                                    <li class="toctree-l3 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset ">Dataframe Subset</a></li>
                                    <ul class="current ">
                                        <li class="toctree-l4 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset_define ">Get Dataframe Subset</a></li>
                                        <li class="toctree-l4 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset_filters ">Define Subset Filter</a></li>
                                    </ul>
                                    <li class="toctree-l3 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_census ">Census</a></li>
                                    <li class="toctree-l3 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_scripting ">Scripting</a></li>
                                </ul>
                            </li>
                            <li class="toctree-l2 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-index.html#pandas_dfc_restrict ">Restricted</a></li>
                        </ul>
                        </li>
                        <li class="toctree-l1 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/development/index.html ">Development</a></li>
                        <li class="toctree-l1 "><a class="reference internal " href="https://rickkrasinski.github.io/dfcleanser/help/whatsnew/index.html ">Release Notes</a></li>
                    </ul>
                </div>
"""

doc_body_html = """
                <div class="documentwrapper ">
                    <div class="bodywrapper ">
                        <div class="body ">

                            <div class="section ">
                                <h1>dfCleanser Census Data Economic Fields</h1>
                                <dl class="function ">
                                    <dt id='dfcleanser_census_economic'></dt>
"""

doc_subdata_start_html = """
                                    <dd>
                                        <h2>General Income</h2>
                                        <ul class="current ">
                                            <li class="toctree-l3 ">economic_income</li> 
                                            <br>
                                            <ul class="current ">
"""

doc_subdata_end_html = """
                                            </ul>
                                        </ul>
                                    </dd>
"""

doc_subdata_colname_html = """
                                                <li class="toctree-l3 ">XXXX</li>

"""

doc_end_html = """
                                </dl>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>



</body>

</html>
"""






def build_colnames_html() :
    
    
    from dfcleanser.sw_utilities.sw_utility_census_model import education_col_names, education_subdata_names, employment_col_names, employment_subdata_names
    from dfcleanser.sw_utilities.sw_utility_census_model import health_insurance_col_names, health_insurance_subdata_names, housing_col_names, housing_subdata_names
    from dfcleanser.sw_utilities.sw_utility_census_model import immigration_col_names, immigration_subdata_names, internet_col_names, internet_subdata_names
    from dfcleanser.sw_utilities.sw_utility_census_model import population_col_names, population_subdata_names
    from dfcleanser.sw_utilities.sw_utility_census_model import social_col_names, social_subdata_names, transportation_col_names, transportation_subdata_names

    page_titles     =   ["Pandas Dataframe Cleanser Census Education Columns",
                         "Pandas Dataframe Cleanser Census Employment Columns",
                         "Pandas Dataframe Cleanser Census Insurance Columns",
                         "Pandas Dataframe Cleanser Census Housing Columns",
                         "Pandas Dataframe Cleanser Census Immigration Columns",
                         "Pandas Dataframe Cleanser Census Internet Columns",
                         "Pandas Dataframe Cleanser Census Population Columns",
                         "Pandas Dataframe Cleanser Census Social Columns",
                         "Pandas Dataframe Cleanser Census Transportation Columns"]
    
    h1_titles     =   ["dfCleanser Census Education Data Fields",
                         "dfCleanser Census Employment Data Fields",
                         "dfCleanser Census Insurance Data Fields",
                         "dfCleanser Census Housing Data Fields",
                         "dfCleanser Census Immigration Data Fields",
                         "dfCleanser Census Internet Data Fields",
                         "dfCleanser Census Population Data Fields",
                         "dfCleanser Census Social Data Fields",
                         "dfCleanser Census Transportation Data Fields"]
    
    h1_ids     =   ["education",
                         "employment",
                         "insurance",
                         "housing",
                         "immigration",
                         "internet",
                         "population",
                         "social",
                         "transportation"]
    
    for i in range(len(page_titles)) :
        
        print("build_colnames_html",i)
        
        current_html    =   ""
        current_html    =   (current_html + toc_html)
        current_html    =   current_html.replace("Pandas Dataframe Cleanser System Environment",page_titles[i])    
        current_html    =   (current_html + doc_body_html)
        current_html    =   current_html.replace("dfCleanser Census Data Economic Fields",h1_titles[i])
        current_html    =   current_html.replace("dfcleanser_census_economic","dfcleanser_census_" + h1_ids[i])
        
        if(i==0) :
            cnames  =   education_col_names
            snames  =   education_subdata_names
        elif(i==1) :
            cnames  =   employment_col_names
            snames  =   employment_subdata_names
        elif(i==2) :
            cnames  =   health_insurance_col_names
            snames  =   health_insurance_subdata_names
        elif(i==3) :
            cnames  =   housing_col_names
            snames  =   housing_subdata_names
        elif(i==4) :
            cnames  =   immigration_col_names
            snames  =   immigration_subdata_names
        elif(i==5) :
            cnames  =   internet_col_names
            snames  =   internet_subdata_names
        elif(i==6) :
            cnames  =   population_col_names
            snames  =   population_subdata_names
        elif(i==7) :
            cnames  =   social_col_names
            snames  =   social_subdata_names
        else :
            cnames  =   transportation_col_names
            snames  =   transportation_subdata_names
            
        for j in range(len(snames)) :
            
            if(j>0) :
                
                print("snames",j,snames[j])
                
                current_html    =   (current_html + doc_subdata_start_html)
                current_html    =   current_html.replace("General Income",snames[j])
                        
                tsname          =   snames[j]
                tsname          =   tsname.replace(" ","_")
                current_html    =   current_html.replace("economic_income",tsname)
                
                print("cnames",j,len(cnames[j]))
                
                for l in range(len(cnames[j])) :
                    
                    current_html    =   (current_html + doc_subdata_colname_html)
                    current_html    =   current_html.replace("XXXX",cnames[j][l])
                            
                current_html    =   (current_html + doc_subdata_end_html)
                        
        current_html    =   (current_html + doc_end_html) 
        
        import os,json
        cfgdir = os.path.join(cfg.get_notebook_path(),cfg.get_notebook_name()+"_files")
        cfgfilename = os.path.join(cfgdir,"dfcleanser-census-" + h1_ids[i] + ".html")
        with open(cfgfilename, 'w') as cfg_file :
            json.dump(current_html,cfg_file)
            cfg_file.close()


   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""





def is_valid_input(numerator,denominator) :
    import numpy as np
    
    if( (np.isnan(numerator)) or (np.isnan(denominator)) or (denominator == 0) ) :
        return(False)
    else :
        return(True)


missing_city_counties = {'AK': ['Auke Bay', 'Ester', 'Fort Greely', 'Karluk', 'Kongiganak', 'Nikiski', 'Takotna', 'Two Rivers', 'Ward Cove'], 
                         'AL': ['Abernant', 'Alton', 'Annemanie', 'Booth', 'Brooklyn', 'Burnwell', 'Bynum', 'Capshaw', 'Cardiff', 'Carlton', 'Chapman', 'Choccolocco', 
                                'Clay', 'Clinton', 'Cloverdale', 'Coaling', 'Cottonton', 'De Armanville', 'Delmar', 'Douglas', 'East Tallassee', 'Edwardsville', 'Furman', 
                                'Goodsprings', 'Goodway', 'Jefferson', 'Kansas', 'Kellerman', 'Kent', 'Malvern', 'Maylene', 'Mc Shan', 'Megargel', 'Mexia', 'Morvin', 
                                'Mount Meigs', 'Nanafalia', 'Normal', 'Palmerdale', 'Perote', 'Peterson', 'Petrey', 'Pine Level', 'Ryland', 'Saginaw', 'Samantha', 
                                'Shannon', 'Siluria', 'Spanish Fort', 'Spring Garden', 'Watson', 'Wattsville', 'West Greene', 'Westover'], 
                         'AR': ['Alix', 'Alpine', 'Armorel', 'Avoca', 'Barton', 'Bassett', 'Beaver', 'Beirne', 'Bergman', 'Board Camp', 'Cale', 'Centerville', 'Choctaw', 
                                'College Station', 'Columbus', 'Curtis', 'Diaz', 'Elm Springs', 'Friendship', 'Garner', 'Gateway', 'Genoa', 'Goshen', 'Gosnell', 'Greenland', 
                                'Hickory Plains', 'Ivan', 'Jacksonport', 'Johnson', 'Jones Mill', 'La Grange', 'Laneburg', 'Lawson', 'Light', 'Oneida', 'Reydell', 'Salado', 
                                'Sedgwick', 'Sweet Home', 'Tontitown', 'Vanndale', 'Walcott', 'Waldenburg', 'West Point', 'West Ridge', 'Willisville', 'Woodson', 'Wright', 
                                'Wrightsville', 'Yorktown'], 'AS': ['Pago Pago'], 
                         'AZ': ['Cashion', 'Catalina', 'Chandler Heights', 'Claypool', 'Cortaro', 'Glendale Luke Afb', 'Higley', 'Hualapai', 'Lake Montezuma', 'Topawa', 
                                'Tortilla Flat', 'Valley Farms'], 
                         'CA': ['Altaville', 'Artois', 'Atwood', 'Bell', 'Blairsden-graeagle', 'Blue Jay', 'Boyes Hot Springs', 'Bryn Mawr', 'Burrel', 'Calpella', 'Camp Meeker', 
                                'Cedar Ridge', 'Chicago Park', 'Chinese Camp', 'Cima', 'City Of Industry', 'Clearlake Park', 'Coloma', 'Crest Park', 'Cutten', 'Douglas Flat', 
                                'East Irvine', 'El Granada', 'El Toro', 'El Verano', 'Feather Falls', 'Fort Dick', 'Goshen', 'Guasti', 'Harmony', 'Holy City', 'Kaweah', 'Kentfield', 
                                'Kit Carson', 'Lincoln Acres', 'Little Lake', 'Martell', 'Moccasin', 'Mono Hot Springs', 'Mount Aukum', 'Mount Wilson', 'Mountain Pass', 'Nelson', 
                                'New Almaden', 'Oakville', 'Obrien', 'Patton', 'Piedmont', 'Piedra', 'Proberta', 'Rackerby', 'Redwood Estates', 'Represa', 'Robbins', 'San Luis Rey', 
                                'Santa Rita Park', 'Standard', 'Stewarts Point', 'Storrie', 'Sun City', 'Talmage', 'Toluca Lake', 'Victor', 'Vineburg', 'Waukena', 'Whiskeytown', 'Yettem'], 
                         'CO': ['Battlement Mesa', 'Chimney Rock', 'Climax', 'Coalmont', 'Cory', 'Eastlake', 'Granite', 'Hereford', 'Hoehne', 'Homelake', 'Hygiene', 'Lazear', 
                                'Lucerne', 'Marvel', 'Masonville', 'Rollinsville', 'San Pablo', 'U S A F Academy'], 
                         'CT': ['Abington', 'Ballouville', 'Botsford', 'Cornwall', 'East Glastonbury', 'East Windsor Hill', 'East Woodstock', 'Fabyan', 'Georgetown', 'Greens Farms', 
                                'Grosvenor Dale', 'Hadlyme', 'Hawleyville', 'Mansfield Depot', 'Mashantucket', 'North Westchester', 'Old Mystic', 'Pequabuck', 'Pomfret', 'Poquonock', 
                                'Redding Center', 'Redding Ridge', 'Somersville', 'South Britain', 'South Willington', 'South Woodstock', 'Stafford', 'Staffordville', 'Stevenson', 
                                'Taconic', 'Versailles', 'West Mystic', 'Winchester Center'], 
                         'DE': ['Kirkwood', 'Little Creek', 'Nassau', 'Woodside'], 
                         'FL': ['Alturas', 'Argyle', 'Barberville', 'Bostwick', 'Bradley', 'Candler', 'Cassadaga', 'Clarcona', 'Coconut Creek', 'Crystal Springs', 'Day', 'Doctors Inlet', 
                                'Durant', 'Eaton Park', 'Edgar', 'El Jobean', 'Elfers', 'Evinston', 'Fairfield', 'Ferndale', 'Fort Ogden', 'Glenwood', 'Goldenrod', 'Gonzalez', 'Graham', 
                                'Grandin', 'Highland City', 'Holmes Beach', 'Homosassa Springs', 'Island Grove', 'Istachatta', 'Killarney', 'Lacoochee', 'Lake Geneva', 'Lake Harbor', 'Lake Monroe', 'Laurel', 'Lloyd', 'Lochloosa', 'Loughman', 'Lowell', 'Mango', 'Marathon Shores', 'Mid Florida', 'Milligan', 'Minneola', 'Mossy Head', 'Murdock', 'Nichols', 'Noma', 'Oneco', 'Orange Springs', 'Ozona', 'Paxton', 'Plymouth', 'Point Washington', 'Port Salerno', 'Putnam Hall', 'Roseland', 'Rosemary Beach', 'Saint Leo', 'Scottsmoor', 'Shady Grove', 'Sharpes', 'Sparr', 'Sumatra', 'Sun City', 'Sydney', 'Tallevast', 'Tangerine', 'Telogia', 'Terra Ceia', 'Trilby', 'Winter Beach', 'Woodville'], 
                         'GA': ['Bellville', 'Bolingbroke', 'Boneville', 'Bowdon Junction', 'Brookfield', 'Calvary', 'Cassville', 'Cedar Springs', 'Chestnut Mountain', 'Clarkdale', 
                                'Clinchfield', 'Coosa', 'Cotton', 'Dover', 'East Ellijay', 'Esom Hill', 'Eton', 'Experiment', 'Farmington', 'Felton', 'Fowlstown', 'Franklin Springs', 
                                'Funston', 'Glenn', 'Gough', 'Haralson', 'Hardwick', 'Helena', 'High Shoals', 'Holly Springs', 'Ila', 'Irwinville', 'Jersey', 'Lebanon', 
                                'Maxeys', 'Mc Rae', 'Meridian', 'Mesena', 'Moody A F B', 'Mount Zion', 'Mystic', 'Nelson', 'Norristown', 'North Metro', 'Oakman', 'Orchard Hill', 
                                'Putney', 'Red Oak', 'Redan', 'Shannon', 'Smarr', 'Toccoa Falls', 'Walthourville', 'Waresboro'], 
                         'GU': ['Agana Heights', 'Agat', 'Barrigada', 'Dededo', 'Hagatna', 'Inarajan', 'Mangilao', 'Merizo', 'Santa Rita', 'Tamuning', 'Yigo'], 
                         'HI': ['Camp H M Smith', 'Fort Shafter', 'Hanamaulu', 'Hawaii National Park', 'Keauhou', 'M C B H Kaneohe Bay', 'Pukalani', 'Puunene', 'Wake Island', 'Wheeler Army Airfield'], 
                         'IA': ['Arispe', 'Aspinwall', 'Austinville', 'Beaver', 'Boxholm', 'Buckeye', 'Chapin', 'Climbing Hill', 'Cooper', 'Delaware', 'Dewar', 'Fostoria', 
                                'Frederika', 'Gifford', 'Gray', 'Hayesville', 'Highlandville', 'Houghton', 'Kesley', 'Killduff', 'Knierim', 'Langworthy', 'Liberty Center', 'Lidderdale', 
                                'Luther', 'Luxemburg', 'Martinsburg', 
                                'Montpelier', 'Morrison', 'North Washington', 'Oakdale', 'Oyens', 'Pilot Grove', 'Ricketts', 'Rome', 'Saint Donatus', 'Saint Marys', 'Shambaugh', 'Springbrook', 'Swedesburg', 'Teeds Grove', 'Toeterville', 'Troy Mills', 'Truesdale', 'Viola', 'West Grove', 'Whitten'], 
                         'ID': ['Atlanta', 'Cobalt', 'Colburn', 'Conda', 'Fenn', 'Huston', 'Lake Fork', 'Minidoka', 'Moreland', 'Mountain Home A F B', 'Parker', 'Porthill'], 
                         'IL': ['Akin', 'Alden', 'Andover', 'Bedford Park', 'Boles', 'Buffalo Prairie', 'Colusa', 'Emma', 'Fort Sheridan', 'Fox Valley', 'Frankfort Heights', 'Goodwine', 'Hagarstown', 'Hopkins Park', 'Huey', 'Janesville', 'Karbers Ridge', 'Lafox', 'Lancaster', 'Lincolns New Salem', 'Literberry', 'Loogootee', 'Lowder', 'Maeystown', 'Menard', 'Merna', 'Nason', 'National Stock Yards', 'Oraville', 'Papineau', 'Perks', 'Plato Center', 'Russell', 'Scottville', 'Stockland', 'Stoy', 'Techny', 'Triumph', 'Unity', 'Wasco'], 
                         'IN': ['Advance', 'Athens', 'Bellmore', 'Bentonville', 'Bippus', 'Blanford', 'Boone Grove', 'Bradford', 'Buckskin', 'Burrows', 'Clarksburg', 'Clear Creek', 
                                'Coalmont', 'Cortland', 'Deedsville', 'Donaldson', 'East Enterprise', 'Finly', 'Folsomville', 'Fontanet', 'Fort Ritner', 'Friendship', 'Grammer', 
                                'Grass Creek', 'Graysville', 'Grissom Arb', 'Hatfield', 'Hayden', 'Helmsburg', 'Hemlock', 'Inglefield', 'Ireland', 'Judson', 'Koleen', 'Kurtz', 
                                'Lake Cicott', 'Leiters Ford', 'Leroy', 'Little York', 'Mariah Hill', 'Maxwell', 'Mc Cordsville', 'Midland', 'Millhousen', 'Montmorenci', 'Morris', 'Mount Saint Francis', 'New Lisbon', 'Oakford', 'Pershing', 'Petroleum', 'Pierceville', 'Pleasant Mills', 'Prairieton', 'Preble', 'Putnamville', 'Ragsdale', 'Rockfield', 'Roselawn', 'Saint Bernice', 'Sedalia', 'Seelyville', 'Servia', 'Stanford', 'Stroh', 'Sulphur', 'Talbot', 'Tefft', 'Templeton', 'Tyner', 'Wallace', 'Webster', 'West Middleton', 'Wolflake'], 
                         'KS': ['Catharine', 'Clearview City', 'Dover', 'Edwardsville', 'Fostoria', 'Gas', 'Hillsdale', 'Lacygne', 'Lamont', 'Maple City', 'Mcconnell Afb', 'New Albany', 'Norway', 'Potter', 'Roxbury', 'Saint John', 'Shawnee Mission', 'Yoder'], 
                         'KY': ['Aberdeen', 'Asher', 'Athol', 'Baskett', 'Bays', 'Bethany', 'Bighill', 'Blackford', 'Bryantsville', 'Bush', 'Cane Valley', 'Carter', 'Clifty', 'Crayne', 
                                'Crockett', 'Curdsville', 'Dewitt', 'Dice', 'Dorton', 'Drake', 'Dubre', 'Dunbar', 'Eastwood', 'Elizaville', 'Elliottville', 'Emlyn', 'Eriline', 'Etoile', 
                                'Fairview', 'Falcon', 'Fall Rock', 'Farmers', 'Fisty', 'Goose Rock', 'Gradyville', 'Hardburly', 'Harrods Creek', 'Heidelberg', 'Hillview', 'Hima', 
                                'Hiseville', 'Ingram', 'Island City', 'Jetson', 'Kenton', 'Lone', 'Lookout', 'Lynnville', 'Malone', 'Marrowbone', 'Mason', 'Mazie', 'Mc Quady', 
                                'Milburn', 'Milford', 'Minnie', 'Mistletoe', 'Mitchellsburg', 'Muses Mills', 'Myra', 'Nevisdale', 'New Liberty', 'North Middletown', 'Ophir', 'Pellville', 
                                'Pittsburg', 'Plummers Landing', 'Poole', 'Preston', 'Primrose', 'Renfro Valley', 'Ricetown', 'Rockhouse', 'Saint Catharine', 'Saint Helens', 'Saul', 
                                'Smith Mills', 'Soldier', 'South Union', 'Stanley', 'Sullivan', 'Tateville', 'Tolu', 'Vincent', 'Waneta', 'Washington', 'Welchs Creek', 'West Louisville', 
                                'West Somerset', 'Wildie', 'Willard', 'Winston', 'Woodbury', 'Wrigley', 'Yerkes'], 
                         'LA': ['Akers', 'Archibald', 'Ashland', 'Blanchard', 'Bordelonville', 'Brittany', 'Burnside', 'Cecilia', 'Centerville', 'Chase', 'Clarks', 'Crowville', 
                                'Duplessis', 'Dupont', 'Echo', 'Fairbanks', 'Flora', 'Forest', 'Garden City', 'Gardner', 'Gorum', 'Jigger', 'Joyce', 'Kraemer', 'Kurthwood', 'Leonville', 'Libuse', 'Longleaf', 'Longstreet', 'Lydia', 'Negreet', 'New Sarpy', 'Pilottown', 'Powhatan', 'Rhinehart', 'Ruby', 'Saint Benedict', 'Saint Maurice', 'Slagle', 'Swartz', 'Taylor', 'Tioga', 'Uncle Sam', 'Varnado', 'Wakefield', 'Watson'], 
                         'MA': ['Accord', 'Arlington Heights', 'Brant Rock', 'Brookline Village', 'Bryantville', 'Charlton City', 'Charlton Depot', 'Chartley', 'Dartmouth', 
                                'East Mansfield', 'East Princeton', 'Easton', 'Elmwood', 'Green Harbor', 'Greenbush', 'Hamilton', 'Lanesboro', 'Manchaug', 'Manomet', 'Marshfield Hills', 'Menemsha', 'Milton Village', 'Minot', 'Monponsett', 'New Town', 'Nonantum', 'North Amherst', 'North Carver', 'North Egremont', 'North Marshfield', 'North Pembroke', 'North Scituate', 'North Uxbridge', 'North Waltham', 'Nutting Lake', 'Ocean Bluff', 'Pinehurst', 'Prides Crossing', 'Raynham Center', 'Readville', 'Sheldonville', 'Silver Beach', 'South Harwich', 'South Orleans', 'Village Of Nagog Woods', 'Waverley', 'Wendell Depot', 'West Boxford', 'West Chop', 'West Falmouth', 'West Groton', 'West Medford', 'West Millbury', 'White Horse Beach', 'Winchendon Springs', 'Woodville'], 
                         'MD': ['Barstow', 'Benson', 'Bethlehem', 'Boring', 'Brooklandville', 'Brownsville', 'Butler', 'Cavetown', 'Chase', 'Chewsville', 'Compton', 'Eckhart Mines', 'Helen', 'Ironsides', 'Ladiesburg', 'Lineboro', 'Lisbon', 'Long Green', 'Loveville', 'Manokin', 'Mayo', 'Mount Victoria', 'New Midway', 'Pinto', 'Powellville', 'Price', 'Rehobeth', 'Riderwood', 'Rock Point', 'Simpsonville', 'Southern Md Facility', 'Spring Gap', 'Suburb Maryland Fac', 'Templeville', 'Unionville'], 
                         'ME': ['Bar Mills', 'Bustins Island', 'Cape Porpoise', 'Center Lovell', 'Clayton Lake', 'Coopers Mills', 'Crouseville', 'Danville', 'Dryden', 'East Parsonsfield', 'East Poland', 'East Vassalboro', 'Fort Kent Mills', 'Glen Cove', 'Isle Of Springs', 'Lincolnville Center', 'Moody', 'North Jay', 'North Turner', 'Olamon', 'Salsbury Cove', 'Sandy Point', 'Sebago Lake', 'Sebasco Estates', 'Sheridan', 'South Casco', 'South Freeport', 'South Windham', 'West Kennebunk', 'West Minot', 'West Poland', 'West Rockport'], 
                         'MI': ['Acme', 'Anchorville', 'Argyle', 'Azalia', 'Bay Shore', 'Bedford', 'Bradley', 'Bridgewater', 'Burnips', 'Cannonsburg', 'Cedar Lake', 'Cloverdale', 'Comstock', 'Cross Village', 'Drayton Plains', 'Edenville', 'Elm Hall', 'Eureka', 'Ferrysburg', 'Frontier', 'Gilford', 'Glenn', 'Good Hart', 'Hagar Shores', 'Harris', 'Jamestown', 'Kendall', 'Lacota', 'Lakeville', 'Lamont', 'Moscow', 'Mosherville', 'Mullett Lake', 'National Mine', 'North Star', 'Old Mission', 'Oshtemo', 'Richville', 'Salem', 'Shaftsburg', 'Smyrna', 'Somerset', 'Stambaugh', 'Sylvan Beach', 'Tower', 'Union Lake', 'Waters'], 
                         'MN': ['Adolph', 'Ah Gwah Ching', 'Almelund', 'Bowstring', 'Buckman', 'Castle Rock', 'Crystal Bay', 'Essig', 'Gilman', 'Holmes City', 'Homer', 'Lake Hubert', 'Lastrup', 'Minnetonka Beach', 'Navarre', 'Nimrod', 'Norwood', 'Noyes', 'Rock Creek', 'Santiago', 'Searles', 'Silver Creek', 'South International Falls', 'Stockton', 'Swift', 'Trosky', 'Twig', 'Winton'], 
                         'MO': ['Allenton', 'Brandsville', 'Brazeau', 'Briar', 'Caplinger Mills', 'Cascade', 'Cottleville', 'Deering', 'Diggins', 'Dutzow', 'Eudora', 'Fagus', 'Farley', 'Flinthill', 'Gasconade', 'Glencoe', 'Gordonville', 'Granger', 'Grayridge', 'Grover', 'Hardenville', 'High Point', 'Hurley', 'Knob Lick', 'Lake Spring', 'Laurie', 'Lodi', 'Mapaville', 'Mc Bride', 'Mc Clurg', 'Mc Girk', 'Milford', 'Montier', 'Morse Mill', 'Mosby', 'New Melle', 'Newtonia', 'Plevna', 'Pocahontas', 'Point Lookout', 'Rives', 'Rockbridge', 'Saginaw', 'Saint Patrick', 'Shook', 'South Fork', 'Stet', 'Tiff City', 'Treloar', 'Turners', 'Waco', 'Wolf Island'], 'MP': ['Rota', 'Saipan', 'Tinian'], 
                         'MS': ['Algoma', 'Arkabutla', 'Becker', 'Belen', 'Chatawa', 'Clara', 'Derma', 'Dublin', 'Eastabuchie', 'Elliott', 'Escatawpa', 'Falcon', 'Gallman', 'Harperville', 'Harriston', 'Hillsboro', 'Holly Ridge', 'Hurley', 'Independence', 'Lakeshore', 'Ludlow', 'Madden', 'Mayhew', 'Mc Adams', 'Mc Neill', 'Money', 'Montpelier', 'Moss', 'Mount Pleasant', 'Nicholson', 'Piney Woods', 'Pocahontas', 'Puckett', 'Sandhill', 'Sharon', 'Sherard', 'Sibley', 'Slate Spring', 'Stennis Space Center', 'Stoneville', 'Swiftown', 'Thomastown', 'Tie Plant', 'Tinsley', 'Toccopola', 'Trebloc', 'Tula', 'Van Vleet', 'Victoria', 'Washington', 'Wayside', 'Wheeler', 'Winterville'], 
                         'MT': ['Boyes', 'Capitol', 'Ethridge', 'Grantsdale', 'Lake Mc Donald', 'Malmstrom A F B', 'Mildred', 'Powderville', 'Radersburg', 'Sumatra', 'Teigen', 'Vandalia'], 
                         'NC': ['Alliance', 'Altamahaw', 'Barium Springs', 'Barnesville', 'Bat Cave', 'Bellarthur', 'Bethania', 'Bonlee', 'Buies Creek', 'Bynum', 'Cedar Falls', 'Cliffside', 
                                'Comfort', 'Connellys Springs', 'Culberson', 'Cumberland', 'Cumnock', 'Dana', 'Durants Neck', 'Earl', 'Edneyville', 'Enka', 'Ether', 'Faith', 'Fallston', 
                                'Glenwood', 'Gulf', 'Harris', 'Hazelwood', 'Highfalls', 'Jonas Ridge', 'Kipling', 'Lemon Springs', 'Lynn', 'Mamers', 'Marietta', 'Mccutcheon Field', 
                                'Micaville', 'Montezuma', 'Mount Mourne', 'Mountain Home', 'Naples', 'Newell', 'Olivia', 'Patterson', 'Paw Creek', 'Penland', 'Plumtree', 'Polkville', 
                                'Potecasi', 'Red Oak', 'Rex', 'Ridgecrest', 'Ridgeway', 'Roduco', 'Scotts', 'Sedalia', 'Severn', 'Skyland', 'Southmont', 'Swepsonville', 'Tillery', 
                                'Toast', 'Townsville', 'Turnersburg', 'Tuxedo', 'Valle Crucis', 'Vaughan', 'Wallburg', 'Webster', 'Welcome', 'Wentworth', 'White Plains', 'Wilsons Mills', 
                                'Wise'], 
                         'ND': ['Agate', 'Balta', 'Bremen', 'Glasston', 'Maida', 'Marshall'], 'NE': ['Cordova', 'Hadar', 'Offutt A F B', 'Reynolds', 'St Columbans'], 
                         'NH': ['Center Strafford', 'East Candia', 'East Derry', 'Enfield Center', 'Lochmere', 'Lyme Center', 'Mount Washington', 'Newington', 'Newton Junction', 
                                'North Salem', 'South Newbury', 'Stinson Lake', 'West Peterborough', 'West Swanzey', 'Winnisquam', 'Wolfeboro Falls', 'Wonalancet'], 
                         'NJ': ['Adelphia', 'Baptistown', 'Blawenburg', 'Buttzville', 'Cedar Brook', 'Changewater', 'Cologne', 'Deerfield Street', 'Dennisville', 'Dividing Creek', 
                                'Ewan', 'Fort Dix', 'Glasser', 'Goshen', 'Green Creek', 'Greendell', 'Grenloch', 'Hope', 'Imlaystown', 'Ironia', 'Leeds Point', 'Liberty Corner', 
                                'Little York', 'Mc Afee', 'Middleville', 'Mizpah', 'Navesink', 'Norma', 'Normandy Beach', 'Oceanville', 'Picatinny Arsenal', 'Pluckemin', 'Quakertown', 
                                'Readington', 'Rosemont', 'Sergeantsville', 'South Dennis', 'Stanton', 'Stillwater', 'Swartswood', 'Tennent', 'Tranquility', 'Tuckahoe', 'Whitehouse', 'Whitesboro', 'Wickatunk'], 
                         'NM': ['Caprock', 'Cedarvale', 'Fort Bayard', 'Kenna', 'Lingo', 'Quay', 'Radium Springs', 'Saint Vrain', 'San Miguel', 'Tome', 'Trampas', 
                                'Trementina'], 
                         'NV': ['Halleck', 'Mercury', 'The Lakes'], 
                         'NY': ['Adams Basin', 'Alton', 'Athol Springs', 'Auriesville', 'Bangall', 'Belleville', 'Bellvale', 'Bible School Park', 'Billings', 'Blodgett Mills', 
                                'Brainardsville', 'Brant', 'Castle Point', 'Centerville', 'Chenango Bridge', 'Clarendon', 'Clarkson', 'Cleverdale', 'Clockville', 'Cochecton Center', 
                                'Colliersville', 'Columbiaville', 'Corbettsville', 'Crittenden', 'Deer River', 'Denmark', 'Depauville', 'Dormansville', 'East Bloomfield', 'East Homer', 
                                'East Pembroke', 'East Pharsalia', 'East Randolph', 'East Williamson', 'Endwell', 'Fancher', 'Fayette', 'Fishers', 'Gallupville', 'Gorham', 'Grafton', 
                                'Hailesboro', 'Hall', 'Helena', 'Hughsonville', 'Hume', 'Java Village', 'Knox', 'Lakemont', 'Lawrenceville', 'Leon', 'Limerick', 'Lincolndale', 
                                'Livingston', 'Livonia Center', 'Lycoming', 'Mahopac Falls', 'Maple View', 'Mc Connellsville', 'Mecklenburg', 'Mellenville', 'Middle Falls', 'Model City', 
                                'Morton', 'Mottville', 'New Haven', 'New Milford', 'Newtonville', 'Niobe', 'North Boston', 'North Granville', 'North Greece', 'North Hoosick', 'North Norwich',
                                'Oaks Corners', 'Ontario Center', 'Orwell', 'Otto', 'Oxbow', 'Plainville', 'Plattekill', 'Poplar Ridge', 'Pultneyville', 'Quaker Street', 'Reading Center', 
                                'Rooseveltown', 'Sandusky', 'Sangerfield', 'Schuyler Lake', 'Seneca Castle', 'Shenorock', 'Shinhopple', 'Smithboro', 'Solsville', 'Sonyea', 'South Butler', 'South Byron', 'South Lima', 'Spring Brook', 'Stella Niagara', 'Stow', 'Sugar Loaf', 'Tallman', 'Tunnel', 'Tyrone', 'Union Hill', 'Vails Gate', 'Van Buren Point', 'Walker Valley', 'Washington Mills', 'West Burlington', 'West Clarksville', 'West Copake', 'Whippleville'], 
                         'OH': ['Bakersville', 'Barlow', 'Bartlett', 'Bath', 'Belmore', 'Bentonville', 'Blaine', 'Brady Lake', 'Broadway', 'Buford', 'Carbondale', 'Charm', 'Chester', 'Colerain', 'Collinsville', 'Colton', 'Cuba', 'Damascus', 'Dunbridge', 'Dupont', 'East Claridon', 'Elkton', 'Ellsworth', 'Etna', 'Fairlawn', 'Farmer', 'Feesburg', 'Glandorf', 'Green', 'Greenford', 'Greentown', 'Hallsville', 'Harlem Springs', 'Hartford', 'Hockingport', 'Homer', 'Iberia', 'Isle Saint George', 'Jewell', 'Keene', 'Kerr', 'Kidron', 'Laings', 'Lees Creek', 'Leesville', 'Lemoyne', 'Malaga', 'Marathon', 'Martel', 'Maximo', 'Maynard', 'Melmore', 'Mingo', 'Mount Hope', 'Mount Liberty', 'Nankin', 'New Athens', 'New Rumley', 'North Georgetown', 'North Kingsville', 'Oceola', 'Okolona', 'Ontario', 'Orangeville', 'Overpeck', 'Piney Fork', 'Rock Camp', 'Ross', 'Roundhead', 'Scioto Furnace', 'Shandon', 'Sharpsburg', 'Shauck', 'Sparta', 'Stillwater', 'Stockdale', 'Summit Station', 'Sycamore Valley', 'Tuppers Plains', 'Unionville', 'Vaughnsville', 'Wakefield', 'West Point', 'West Rushville', 'Westville', 'White Cottage'], 
                         'OK': ['Albany', 'Albert', 'Altus Afb', 'Blocker', 'Cardin', 'Concho', 'Dibble', 'Fox', 'Foyil', 'Gene Autry', 'Golden', 'Gowen', 'Hoyt', 'Kiamichi Christian Mission', 'Leonard', 'Meers', 'Monroe', 'Moodys', 'Oscar', 'Panola', 'Pickens', 'Saint Louis', 'Southard', 'Stidham', 'Texola', 'Tussy', 'Washita'], 'OR': ['Allegany', 'Alvadore', 'Arock', 'Bridal Veil', 'Crabtree', 'Crawfordsville', 'Crescent Lake', 'Culp Creek', 'Curtin', 'Dillard', 'Keizer', 'Marylhurst', 'Mikkalo', 'Murphy', 'Netarts', 'Odell', 'Ophir', 'Riverside', 'Rose Lodge', 'Thurston', 'Wedderburn'], 
                         'PA': ['Ackermanville', 'Alba', 'Analomink', 'Antes Fort', 'Aquashicola', 'Arcola', 'Arendtsville', 'Audubon', 'Bart', 'Bausman', 'Beach Haven', 'Bedminster', 'Birchrunville', 'Blooming Glen', 'Blue Ball', 'Bovard', 'Bowmansdale', 'Branchton', 'Brandy Camp', 'Brier Hill', 'Brooklyn', 'Brownfield', 'Brush Valley', 'Cambra', 'Camptown', 'Cashtown', 'Castanea', 'Cedars', 'Centerport', 'Chatham', 'Chinchilla', 'Cocolamus', 'Concordville', 'Coupon', 'Cowanesque', 'Craley', 'Cranberry Twp', 'Creamery', 'Crown', 'Curllsville', 'Curtisville', 'Dagus Mines', 'Danboro', 'Devault', 'Durham', 'Eagleville', 'Earlington', 'Edgemont', 'Elgin', 'Elm', 'Elmhurst', 'Fairview Village', 'Ferndale', 'Fisher', 'Flicksville', 'Forest Grove', 'Franconia', 'Franklintown', 'Frostburg', 'Gans', 'Gardenville', 'Gastonville', 'Gibson', 'Glasgow', 'Glen Riddle Lima', 'Goodville', 'Gradyville', 'Grover', 'Hendersonville', 'Herman', 'Hilltown', 'Holicong', 'Hopeland', 'Hummels Wharf', 'Idaville', 'Ingomar', 'Intercourse', 'Kantner', 'Kelton', 'Kemblesville', 'Kreamer', 'Kulpsville', 'La Plume', 'Lahaska', 'Lamartine', 'Lampeter', 'Landingville', 'Lanesboro', 'Lecontes Mills', 'Lederach', 'Lehigh Valley', 'Lehman', 'Lemasters', 'Lenni', 'Lewisville', 'Lightstreet', 'Limeport', 'Limestone', 'Lionville', 'Listie', 'Loganville', 'Lumberville', 'Lurgan', 'Lyndell', 'Mainland', 'Mammoth', 'Marchand', 'Martindale', 'Mattawana', 'Mc Connellstown', 'Mechanicsville', 'Mendenhall', 'Mingoville', 'Minisink Hills', 'Monocacy Station', 'Morann', 'Mount Braddock', 'Neffs', 'New Baltimore', 'New London', 'North Springfield', 'Northpoint', 'Norvelt', 'Numidia', 'Orson', 'Orviston', 'Peach Glen', 'Penns Park', 'Penryn', 'Pine Forge', 'Pineville', 'Plumsteadville', 'Pocono Lake Preserve', 'Pocopson', 'Porters Sideling', 'Ravine', 'Reamstown', 'Refton', 'Revere', 'Rexmont', 'Riceville', 'Rossville', 'Rushland', 'Sadsburyville', 'Saint Boniface', 'Saint Johns', 'Saint Peters', 'Salford', 'Salfordville', 'Salona', 'Schenley', 'Shawanese', 'Shawville', 'Silver Spring', 'Slate Run', 'Smokerun', 'Snydersburg', 'Snydertown', 'Solebury', 'Southeastern', 'Southwest', 'Spinnerstown', 'Spring Mount', 'Sumneytown', 'Suplee', 'Sylvania', 'Talmage', 'Taylorstown', 'Tipton', 'Tire Hill', 'Troxelville', 'Turkey City', 'Tylersport', 'Tylersville', 'Unity House', 'Ursina', 'Uwchland', 'Valley Forge', 'Vicksburg', 'Wagontown', 'Waltersburg', 'West Point', 'West Salisbury', 'West Willow', 'Westtown', 'Widnoon', 'Wildwood', 'Williamson', 'Witmer', 'Worcester', 'Woxall', 'Zionhill'], 
                         'PR': ['Angeles', 'Palmer', 'Rio Blanco', 'Roosevelt Roads', 'Rosario', 'Saint Just'], 
                         'RI': ['Adamsville', 'Fiskeville', 'Forestdale', 'Harmony', 'Peace Dale', 'Slocum'], 
                         'SC': ['Ballentine', 'Bethera', 'Bowling Green', 'Canadys', 'Clearwater', 'Conestee', 'Crocketville', 'Dale', 'Davis Station', 'Fairforest', 'Gramling', 'Grover', 'Hilda', 'La France', 'Ladys Island', 'Lobeco', 'Miley', 'Minturn', 'Montmorenci', 'Rains', 'Richland', 'Rion', 'Russellville', 'Sandy Springs', 'Sardinia', 'Shaw A F B', 'Sycamore', 'Tigerville', 'Van Wyck', 'White Rock', 'White Stone'], 'SD': ['Enning', 'Kaylor', 'Rowena', 'Walker'], 
                         'TN': ['Arthur', 'Bakewell', 'Braden', 'Brunswick', 'Campaign', 'Chewalla', 'Clarksburg', 'Como', 'Conasauga', 'Eaton', 'Fosterville', 
                                'Fruitvale', 'Gibson', 'Gladeville', 'Idlewild', 'Laconia', 'Lake City', 'Lone Mountain', 'Lowland', 'Macon', 'Mitchellville', 'Mountain Home', 'Norene', 'Ridgetop', 'Shawanee', 'Silerton', 'Smartt', 'Spring Creek', 'Summitville', 'Tipton', 'Woodland Mills', 'Yorkville'], 
                         'TX': ['Aiken', 'Alanreed', 'Alief', 'Barker', 'Belmont', 'Bluegrove', 'Bula', 'Cason', 'Cee Vee', 'Centralia', 'Chapman Ranch', 'Chicota', 'Chriesman', 'Clayton', 
                                'Concord', 'Copeville', 'Cunningham', 'Dallardsville', 'Danciger', 'Deanville', 'Dennis', 'Dinero', 'Dobbin', 'Dunn', 'Ecleto', 'Elmo', 'Flat', 
                                'Garciasville', 'Geronimo', 'Girvin', 'Gober', 'Golden', 'Greenwood', 'Guerra', 'Heidenheimer', 'Hochheim', 'Hufsmith', 'Joinerville', 'Jonesville', 
                                'Judson', 'Kamay', 'Kenney', 'Kurten', 'Laguna Park', 'Laird Hill', 'Laughlin A F B', 'Lingleville', 'Lodi', 'Lowake', 'Lozano', 'Lyons', 'Macdona', 
                                'Martinsville', 'Mauriceville', 'Maydelle', 'Mc Neil', 'Merit', 'Millican', 'Minden', 'Morgan Mill', 'Mound', 'Naval Air Station/ Jrb', 'New Baden', 
                                'New Home', 'North Houston', 'Old Ocean', 'Orangefield', 'Ottine', 'Paluxy', 'Panola', 'Peaster', 'Peggy', 'Pendleton', 'Penwell', 'Plum', 'Poynor', 
                                'Price', 'Proctor', 'Raywood', 'Roans Prairie', 'Ross', 'Sam Norwood', 'Scottsville', 'Selman City', 'Slidell', 'Star', 'Sublime', 'Telegraph', 'Thomaston', 
                                'Toyahvale', 'Veribest', 'Walburg', 'Warda', 'Waring', 'Warrenton', 'Weir', 'Wellborn', 'Westminster', 'Weston', 'Wheelock', 'Woodlake', 'Woodlawn'],
                                
                         'UT': ['Aneth', 'Bonanza', 'Meadow'], 
                         'VA': ['Achilles', 'Ammon', 'Andover', 'Arcola', 'Ark', 'Batesville', 'Beaumont', 'Ben Hur', 'Bena', 'Brooke', 'Brucetown', 
                               'Burkes Garden', 'Calverton', 'Christchurch', 'Clifford', 'Cluster Springs', 'Coles Point', 'Corbin', 'Craddockville', 'Davis Wharf', 'Dogue', 
                               'Dulles', 'Edwardsville', 'Emory', 'Evergreen', 'Fishers Hill', 'Fort Mitchell', 'Garrisonville', 'Glen Wilton', 'Graves Mill', 'Greenway', 'Hadensville', 
                               'Hartwood', 'Haynesville', 'Horsepen', 'Ivy', 'Jamestown', 'Jenkins Bridge', 'Jersey', 'Keen Mountain', 'Lacey Spring', 'Lackey', 'Ladysmith', 
                               'Leon', 'Lightfoot', 'Lincoln', 'Lively', 'Locustville', 'Macon', 'Mannboro', 'Maryus', 'Mavisdale', 'Mc Coy', 'Meredithville', 'Merrifield', 'Merry Point', 
                               'Mint Spring', 'Modest Town', 'Mollusk', 'Montpelier Station', 'Morattico', 'Mount Holly', 'Mount Vernon', 'Mustoe', 'Naruna', 'New Hope', 'New River', 
                               'Newbern', 'Newington', 'Ninde', 'Norge', 'Nottoway', 'Nuttsville', 'Ordinary', 'Orlean', 'Oyster', 'Philomont', 'Pleasant Valley', 'Quinque', 'Rectortown', 
                               'Red Ash', 'Redwood', 'Rollins Fork', 'Ruby', 'Ruthville', 'Sandy Point', 'Schley', 'Sealston', 'Seaview', 'Severn', 'Shortt Gap', 'Somerville', 
                               'Sparta', 'Stratford', 'Studley', 'Thornburg', 'Townsend', 'Trevilians', 'Vesta', 'Viewtown', 'Village', 'Villamont', 'Wardtown', 
                               'Ware Neck', 'Wattsville', 'West Mclean', 'White Hall', 'White Marsh', 'Wicomico', 'Wolford', 'Wolftown', 'Woods Cross Roads', 'Zacata'], 
                         'VI': ['Christiansted', 'Frederiksted', 'Kingshill', 'St John', 'St Thomas'], 
                         'VT': ['Ascutney', 'Beebe Plain', 'Benson', 'Chester Depot', 'East Poultney', 'East Saint Johnsbury', 'Essex', 'Forest Dale', 'Gaysville', 'Granby', 'Hartford', 'Hartland Four Corners', 'Highgate Springs', 'Hydeville', 'Jonesville', 'Lower Waterford', 'Lyndon', 'Marlboro', 'Monkton', 'Montgomery', 'Moscow', 'North Hyde Park', 'North Montpelier', 'North Thetford', 'Passumpsic', 'Rupert', 'Saint Johnsbury Center', 'South Barre', 'South Newfane', 'Taftsville', 'Thetford', 'Underhill Center', 'West Dummerston', 'West Glover', 'West Newbury', 'Westminster Station', 'Wilder'], 
                         'WA': ['Adna', 'Belmont', 'Boyds', 'Brownstown', 'Burley', 'Burton', 'Carlsborg', 'Carrolls', 'Doty', 'East Olympia', 'Four Lakes', 'Heisson', 'Hobart', 'Husum', 'Joyce', 'Kapowsin', 'La Grande', 'Lebam', 'Littlerock', 'Longmire', 'Menlo', 'Mill Creek', 'Nahcotta', 'Neilton', 'North Lakewood', 'Paradise Inn', 'Redondo', 'Retsil', 'Rollingbay', 'Seahurst', 'Silvana', 'South Colby', 'Southworth', 'Startup', 'Tracyton', 'Tumwater', 'Wauna'], 
                         'WI': ['Bassett', 'Benet Lake', 'Benoit', 'Big Falls', 'Blenker', 'Brill', 'Camp Lake', 'Cataract', 'De Forest', 'Dellwood', 'Downsville', 'East Ellsworth', 'Edgewater', 'Edmund', 'Elderon', 'Eureka', 'Freedom', 'Galloway', 'Genesee Depot', 'Gilmanton', 'Greenbush', 'Hannibal', 'Hanover', 'Heafford Junction', 'Honey Creek', 'Jump River', 'Kellnersville', 'Kieler', 'Lake Delton', 'Lime Ridge', 'Lynxville', 'Lyons', 'Maplewood', 'Mc Naughton', 'Merton', 'New Munster', 'Newburg', 'Nichols', 'North Lake', 'Oakdale', 'Pell Lake', 'Phlox', 'Powers Lake', 'Readfield', 'Rock Falls', 'Saxeville', 'Sextonville', 'Sinsinawa', 'Somers', 'Springfield', 'Thiensville', 'Tilleda', 'Tisch Mills', 'Tunnel City', 'Union Center', 'Wascott', 'Woodland', 'Woodworth', 'Zachow'], 
                         'WV': ['Adrian', 'Advent', 'Bakerton', 'Big Run', 'Blue Creek', 'Borderland', 'Bretz', 'Cassville', 'Chattaroy', 'Chauncey', 'Colfax', 'Cora', 'Dellslow', 'Dothan', 'Drennen', 'Eckman', 'Elton', 'Fairlea', 'Falling Rock', 'Frenchton', 'Gilboa', 'Glengary', 'Grassy Meadows', 'Green Sulphur Springs', 'Halltown', 'Harper', 'Hemphill', 'Kellysville', 'Keslers Cross Lanes', 'Kingmont', 'Kyle', 'Lanark', 'Lochgelly', 'Lorentz', 'Marianna', 'Milam', 'Myra', 'Naugatuck', 'Newtown', 'Onego', 'Pentress', 'Porters Falls', 'Prosperity', 'Pursglove', 'Rawl', 'Red Creek', 'Ridgeway', 'Rippon', 'Shirley', 'Shoals', 'Short Creek', 'Skelton', 'Spring Dale', 'Stanaford', 'Teays', 'Wayside', 'Wilcoe', 'Wilsonburg', 'Wolfcreek', 'Wolfe', 'Woodville', 'Wyatt', 'Wyco'], 
                         'WY': ['Huntley', 'Jeffrey City', 'Saddlestring', 'Saint Stephens', 'Shirley Basin']}







def build_zip_code_mappings() :
    
    print("build_zip_code_mappings")
    fix_missing_counties()
    
    return()

    import pandas as pd
    opstat          =   opStatus()
    
    import os
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\")
    
    State_City_Zips_file_name       =   "State-City-Zips.csv"
    State_City_Zips_column_names    =   ["State","City","Zips_List"]

    County_City_Zips_file_name      =   "County-City-Zips.csv"
    County_City_Zips_column_names   =   ["zip","lat","lng","city","state_id","state_name","county_fips","county_name"]
    
    State_City_Zips_df              =   pd.read_csv(dfc_census_path+State_City_Zips_file_name)
    County_City_Zips_df             =   pd.read_csv(dfc_census_path+County_City_Zips_file_name)

    state_county_zips_file_name     =   "state_county_zips.csv"
    state_county_cities_file_name   =   "state_county_cities.csv"

    states_list     =   County_City_Zips_df["state_id"].unique().tolist()
    states_list.sort()
    
    state_county_zips   =   pd.DataFrame(columns=["state","county","zips"])
    state_county_cities =   pd.DataFrame(columns=["state","county","cities"])

    for i in range(len(states_list)) :
        
        criteria    =   County_City_Zips_df["state_id"] == states_list[i]
        counties    =   County_City_Zips_df[criteria]["county_name"].unique().tolist()
        counties.sort()
        
        for j in range(len(counties)) :
            
            criteria    =   (County_City_Zips_df["state_id"] == states_list[i]) & (County_City_Zips_df["county_name"] == counties[j])
            zips    =   County_City_Zips_df[criteria]["zip"].unique().tolist()
            zips.sort()
            state_county_zips = state_county_zips.append(pd.DataFrame([[states_list[i],counties[j],zips]],columns=["state","county","zips"]),ignore_index=True)
            
            criteria    =   (County_City_Zips_df["state_id"] == states_list[i]) & (County_City_Zips_df["county_name"] == counties[j])
            cities    =   County_City_Zips_df[criteria]["city"].unique().tolist()
            cities.sort()
            state_county_cities = state_county_cities.append(pd.DataFrame([[states_list[i],counties[j],cities]],columns=["state","county","cities"]),ignore_index=True)
         
        print("state id",states_list[i],len(counties))
        
    state_county_zips.to_csv(dfc_census_path+state_county_zips_file_name,index=False)
    state_county_cities.to_csv(dfc_census_path+state_county_cities_file_name,index=False)
    
    
    
    states_list     =   State_City_Zips_df["State"].unique().tolist()
    states_list.sort()
    
    missing_cities = {}
    
    for i in range(len(states_list)) :

        criteria    =   State_City_Zips_df["State"] == states_list[i]
        cities      =   State_City_Zips_df[criteria]["City"].unique().tolist()
        cities.sort()
    
        criteria    =   County_City_Zips_df["state_id"] == states_list[i]
        cities1     =   County_City_Zips_df[criteria]["city"].unique().tolist()
        cities1.sort()
        
        cities_not_found    =   []
        for j in range(len(cities)) :
            
            found = False

            for k in range(len(cities1)) :
                
                if(cities[j] == cities1[k].upper()) :
                    
                    criteria        =   (State_City_Zips_df["State"] == states_list[i]) & (State_City_Zips_df["City"] == cities[j])
                    state_city      =   State_City_Zips_df[criteria]
                    
                    State_City_Zips_df.iloc[state_city.index,1] =   cities1[k]
                    
                    found=True
                    break;
    
            if(not found) :
                cities_not_found.append(cities[j])
                
        missing_cities.update({states_list[i]:cities_not_found})
                
                
        print("state",states_list[i])

    missing_cities_states   =   list(missing_cities.keys())
    missing_cities_states.sort()
    
    fixed_missing_cities     =   {}
    
    for i in range(len(missing_cities_states)) :
        
        current_cities  =   missing_cities.get(missing_cities_states[i])
        
        for j in range(len(current_cities)) :
            
            city        =   current_cities[j]
            city_split  =   city.split(" ")
            
            for k in range(len(city_split)) :
                capchar         =   city_split[k][0]
                city_lower      =   city_split[k].lower()
                #city_lower[0]   =   capchar
                city_split[k]   =   capchar + city_lower[1:]
                
            current_cities[j] = city_split[0]
            
            if(len(city_split) > 1) :
                
                for m in  range(len(city_split)) :
                    if(m>0) :
                        current_cities[j] = current_cities[j] + " " + city_split[m]    
            
        fixed_missing_cities.update({missing_cities_states[i]:current_cities})
                
            
    states   =   list(fixed_missing_cities.keys())
    states.sort()
    
    for i in range(len(states)) :
        
        cities  =   fixed_missing_cities.get(states[i])
        
        for j in range(len(cities)) :
            
            oldcity     =   cities[j].upper()
            
            criteria        =   (State_City_Zips_df["State"] == states[i]) & (State_City_Zips_df["City"] == oldcity)
            state_city      =   State_City_Zips_df[criteria]
                    
            State_City_Zips_df.iloc[state_city.index,1] =   cities[j]
            

    State_City_Zips_df.to_csv(dfc_census_path + "final_cleaned_" + State_City_Zips_file_name,index=False)
    
    #print(missing_cities)
    
    print(fixed_missing_cities)

    
def fix_missing_counties() :
    
    print("fix_missing_counties")
    
    import pandas as pd
    import os
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\")
    state_county_cities_file_name   =   "state_county_cities.csv"
    
    state_county_cities     =   pd.read_csv(dfc_census_path+state_county_cities_file_name)
    
    #from dfcleanser.sw_utilities.county_city_list import state_ids, city_county

    city_county_df   =   pd.DataFrame(columns=["city_id","state_id","city","county","lat","long"])
    
    #for i in range(len(city_county)) :
        #city_county_df = city_county_df.append(pd.DataFrame([city_county[i]],columns=["city_id","state_id","city","county","lat","long"]),ignore_index=True)
    #    city_county_df = city_county_df.append(pd.Series(city_county[i],index=["city_id","state_id","city","county","lat","long"]),ignore_index=True)
        
    print("city_county_df",len(city_county_df),"\n\n",city_county_df.dtypes,"\n")

    for i in range(0):#len(state_ids)) :
        
        #state_index     =   state_ids[i][0]
        #state_id        =   state_ids[i][1]
        
        #print("state_id",state_id)
    
        missing_cities  =   missing_city_counties.get(state_id) 
        
        if(0):#not (missing_cities is None)) :
        
            for j in range(len(missing_cities)) :
            
                #print("state city",state_index,missing_cities[j])
            
                criteria        =   (city_county_df["state_id"] == state_index) & (city_county_df["city"] == missing_cities[j])
                state_city      =   city_county_df[criteria]
                #print("\nstate_city",type(state_city),state_city)        
            
                if(len(state_city) > 0) :
                
                    new_county     =   state_city.iloc[0,3]
                    #print("new_county",type(new_county),new_county)
            
                    criteria        =   (state_county_cities["state"] == state_id) 
                    criteria1       =   (state_county_cities["county"] == new_county)
                    county_city     =   state_county_cities[criteria & criteria1]

                    city_list_s     =   state_county_cities.iloc[county_city.index,2]
            
                    #print("\ncity_list_s",type(city_list_s),city_list_s)
            
                    if(len(city_list_s) > 0) :
                
                        city_list       =   city_list_s.tolist()[0]
                        city_list       =   city_list.strip("[")
                        city_list       =   city_list.strip("]")
                        city_list       =   city_list.split(", ")
            
                        #print("\ncity_list",type(city_list),city_list)
            
                        for l in range(len(city_list)) :
                            city_list[l]    =   city_list[l].replace('"',' ')
                
                
                        #print("missing_cities[j]",type(missing_cities[j]),missing_cities[j])
            
                        missing_city    =   "'" + missing_cities[j] + "'"

                        city_list.append(missing_city)
                        city_list.sort()
            
                        #print("\ncity_list",type(city_list),city_list)
            
                        city_list   =   str(city_list)
                        city_list   =   city_list.replace('"','')
            
            
                        #print("\nnew city_list",type(city_list),city_list)
            
                        state_county_cities.iloc[county_city.index,2]   =   city_list
                
                    else :
                
                        print("missing county for city ")#,state_id,new_county,missing_cities[j])
                    
                else :
                
                    print("missing city in county list ")#,state_id,missing_cities[j]) 


            
    state_county_cities.to_csv(dfc_census_path+ "last_" + state_county_cities_file_name,index=False)
            
            
        
        

        
    return()






















    
    
    
    clock = RunningClock()
    clock.start()

    try :
        zipcode_map     =   pd.read_csv(dfc_census_path+swcm.ZIPCODE_MAPPING_FILE)
    except Exception as e:
        opstat.set_status(False)
        opstat.store_exception("error importing xipcode data",e)
                                            
    if(opstat.get_status()) :
            
        new_dfcnotes    =   "zip code mappings"
        new_dfcdf       =   cfg.dfc_dataframe("zipcode_mapings",zipcode_map,new_dfcnotes)
        cfg.add_dfc_dataframe(new_dfcdf)
        
        dtime   =   clock.stop()
        print("Total Zipcode Mapping Import Time : ",dtime)
        print("Zipcode Mapping : [",len(zipcode_map),",",len(zipcode_map.columns),"]")
                
    else :
                
        clock.stop()
        print("Unable to import Zipcode Data : ")
        display_exception(opstat)          



statecities = ['Adak', 'Akiachak', 'Akiak', 'Akutan', 'Alakanuk', 'Aleknagik', 'Allakaket', 'Ambler', 'Anaktuvuk Pass', 'Anchor Point', 'Anchorage', 'Anderson', 'Angoon', 
                'Aniak', 'Anvik', 'Arctic Village', 'Atka', 'Atqasuk', 'Auke Bay', 'Barrow', 'Beaver', 'Bethel', 'Bettles Field', 'Big Lake', 'Brevig Mission', 'Buckland', 
                'Cantwell', 'Central', 'Chalkyitsik', 'Chefornak', 'Chevak', 'Chicken', 'Chignik', 'Chignik Lagoon', 'Chignik Lake', 'Chitina', 'Chugiak', 'Circle', 'Clam Gulch', 
                'Clarks Point', 'Clear', 'Coffman Cove', 'Cold Bay', 'Cooper Landing', 'Copper Center', 'Cordova', 'Craig', 'Crooked Creek', 'Deering', 'Delta Junction', 
                'Denali National Park', 'Dillingham', 'Douglas', 'Dutch Harbor', 'Eagle', 'Eagle River', 'Eek', 'Egegik', 'Eielson AFB', 'Ekwok', 'Elfin Cove', 'Elim', 
                'Emmonak', 'Ester', 'Fairbanks', 'False Pass', 'Fort Greely', 'Fort Wainwright', 'Fort Yukon', 'Gakona', 'Galena', 'Gambell', 'Girdwood', 'Glennallen', 
                'Goodnews Bay', 'Grayling', 'Gustavus', 'Haines', 'Healy', 'Holy Cross', 'Homer', 'Hoonah', 'Hooper Bay', 'Hope', 'Houston', 'Hughes', 'Huslia', 'Hydaburg', 
                'Hyder', 'Iliamna', 'Indian', 'Jber', 'Juneau', 'Kake', 'Kaktovik', 'Kalskag', 'Kaltag', 'Karluk', 'Kasigluk', 'Kasilof', 'Kenai', 'Ketchikan', 'Kiana', 
                'King Cove', 'King Salmon', 'Kipnuk', 'Kivalina', 'Klawock', 'Kobuk', 'Kodiak', 'Kongiganak', 'Kotlik', 'Kotzebue', 'Koyuk', 'Koyukuk', 'Kwethluk', 'Kwigillingok', 
                'Lake Minchumina', 'Larsen Bay', 'Levelock', 'Lower Kalskag', 'Manley Hot Springs', 'Manokotak', 'Marshall', 'Mc Grath', 'Mekoryuk', 'Metlakatla', 'Meyers Chuck', 
                'Minto', 'Moose Pass', 'Mountain Village', 'Naknek', 'Napakiak', 'Nenana', 'New Stuyahok', 'Nightmute', 'Nikiski', 'Nikolai', 'Nikolski', 'Ninilchik', 'Noatak', 
                'Nome', 'Nondalton', 'Noorvik', 'North Pole', 'Northway', 'Nuiqsut', 'Nulato', 'Nunam Iqua', 'Nunapitchuk', 'Old Harbor', 'Ouzinkie', 'Palmer', 'Pedro Bay', 
                'Pelican', 'Perryville', 'Petersburg', 'Pilot Point', 'Pilot Station', 'Platinum', 'Point Baker', 'Point Hope', 'Point Lay', 'Port Alexander', 'Port Alsworth', 
                'Port Heiden', 'Port Lions', 'Prudhoe Bay', 'Quinhagak', 'Rampart', 'Red Devil', 'Ruby', 'Russian Mission', 'Saint George Island', 'Saint Marys', 
                'Saint Michael', 'Saint Paul Island', 'Salcha', 'Sand Point', 'Savoonga', 'Scammon Bay', 'Selawik', 'Seldovia', 'Seward', 'Shageluk', 'Shaktoolik', 
                'Shishmaref', 'Shungnak', 'Sitka', 'Skagway', 'Skwentna', 'Sleetmute', 'Soldotna', 'South Naknek', 'Stebbins', 'Sterling', 'Stevens Village', 'Sutton', 
                'Takotna', 'Talkeetna', 'Tanacross', 'Tanana', 'Tatitlek', 'Teller', 'Tenakee Springs', 'Thorne Bay', 'Togiak', 'Tok', 'Toksook Bay', 'Trapper Creek', 'Tuluksak', 
                'Tuntutuliak', 'Tununak', 'Two Rivers', 'Tyonek', 'Unalakleet', 'Unalaska', 'Valdez', 'Venetie', 'Wainwright', 'Wales', 'Ward Cove', 'Wasilla', 'White Mountain', 
                'Whittier', 'Willow', 'Wrangell', 'Yakutat']


df_statecities =['Adak', 'Akiachak', 'Akiak', 'Akutan', 'Alakanuk', 'Aleknagik', 'Allakaket', 'Ambler', 'Anaktuvuk Pass', 'Anchor Point', 'Anchorage', 'Anderson', 'Angoon', 'Aniak', 
                  'Anvik', 'Arctic Village', 'Atka', 'Atqasuk', 'Auke Bay', 'Barrow', 'Beaver', 'Bethel', 'Bettles Field', 'Big Lake', 'Brevig Mission', 'Buckland', 'Cantwell', 'Central', 
                  'Chalkyitsik', 'Chefornak', 'Chevak', 'Chicken', 'Chignik', 'Chignik Lagoon', 'Chignik Lake', 'Chitina', 'Chugiak', 'Circle', 'Clam Gulch', 'Clarks Point', 'Clear', 
                  'Coffman Cove', 'Cold Bay', 'Cooper Landing', 'Copper Center', 'Cordova', 'Craig', 'Crooked Creek', 'Deering', 'Delta Junction', 'Denali National Park', 'Dillingham', 
                  'Douglas', 'Dutch Harbor', 'Eagle', 'Eagle River', 'Eek', 'Egegik', 'Eielson AFB', 'Ekwok', 'Elfin Cove', 'Elim', 'Emmonak', 'Fairbanks', 'False Pass', 'Fort Wainwright', 
                  'Fort Yukon', 'Gakona', 'Galena', 'Gambell', 'Girdwood', 'Glennallen', 'Goodnews Bay', 'Grayling', 'Gustavus', 'Haines', 'Healy', 'Holy Cross', 'Homer', 'Hoonah', 
                  'Hooper Bay', 'Hope', 'Houston', 'Hughes', 'Huslia', 'Hydaburg', 'Hyder', 'Iliamna', 'Indian', 'Jber', 'Juneau', 'Kake', 'Kaktovik', 'Kalskag', 'Kaltag', 'Karluk', 
                  'Kasigluk', 'Kasilof', 'Kenai', 'Ketchikan', 'Kiana', 'King Cove', 'King Salmon', 'Kipnuk', 'Kivalina', 'Klawock', 'Kobuk', 'Kodiak', 'Kotlik', 'Kotzebue', 'Koyuk', 
                  'Koyukuk', 'Kwethluk', 'Kwigillingok', 'Lake Minchumina', 'Larsen Bay', 'Levelock', 'Lower Kalskag', 'Manley Hot Springs', 'Manokotak', 'Marshall', 'Mc Grath', 
                  'Mekoryuk', 'Metlakatla', 'Meyers Chuck', 'Minto', 'Moose Pass', 'Mountain Village', 'Naknek', 'Napakiak', 'Nenana', 'New Stuyahok', 'Nightmute', 'Nikolai', 'Nikolski', 
                  'Ninilchik', 'Noatak', 'Nome', 'Nondalton', 'Noorvik', 'North Pole', 'Northway', 'Nuiqsut', 'Nulato', 'Nunam Iqua', 'Nunapitchuk', 'Old Harbor', 'Ouzinkie', 'Palmer', 
                  'Pedro Bay', 'Pelican', 'Perryville', 'Petersburg', 'Pilot Point', 'Pilot Station', 'Platinum', 'Point Baker', 'Point Hope', 'Point Lay', 'Port Alexander', 'Port Alsworth', 
                  'Port Heiden', 'Port Lions', 'Prudhoe Bay', 'Quinhagak', 'Rampart', 'Red Devil', 'Ruby', 'Russian Mission', 'Saint George Island', 'Saint Marys', 'Saint Michael', 
                  'Saint Paul Island', 'Salcha', 'Sand Point', 'Savoonga', 'Scammon Bay', 'Selawik', 'Seldovia', 'Seward', 'Shageluk', 'Shaktoolik', 'Shishmaref', 'Shungnak', 'Sitka', 
                  'Skagway', 'Skwentna', 'Sleetmute', 'Soldotna', 'South Naknek', 'Stebbins', 'Sterling', 'Stevens Village', 'Sutton', 'Talkeetna', 'Tanacross', 'Tanana', 'Tatitlek', 
                  'Teller', 'Tenakee Springs', 'Thorne Bay', 'Togiak', 'Tok', 'Toksook Bay', 'Trapper Creek', 'Tuluksak', 'Tuntutuliak', 'Tununak', 'Tyonek', 'Unalakleet', 'Unalaska', 
                  'Valdez', 'Venetie', 'Wainwright', 'Wales', 'Wasilla', 'White Mountain', 'Whittier', 'Willow', 'Wrangell', 'Yakutat']




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               get summary lists 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_city_zips(state,city,zips_df) :
    
    criteria        =   (zips_df["State"] == state) 
    criteria1       =   (zips_df["City"] == city)
    state_city      =   zips_df[criteria & criteria1]
    
    city_zip_list   =   state_city.iloc[0,2]
            
    zips_list       =   city_zip_list.strip("[")
    zips_list       =   zips_list.strip("]")
    zips_list       =   zips_list.split(", ")
            
    return(zips_list)
    

def get_county_cities(state,county,cities_df) :
    
    criteria            =   (cities_df["State"] == state) 
    criteria1           =   (cities_df["County"] == county)
    state_county        =   cities_df[criteria & criteria1]

    county_city_list    =   state_county.iloc[0,2]
            
    city_list       =   county_city_list.strip("[")
    city_list       =   city_list.strip("]")
    city_list       =   city_list.replace("'","")
    city_list       =   city_list.split(", ")
            
    for l in range(len(city_list)) :
        city_list[l]    =   city_list[l].replace('"',' ')

    city_list.sort()
        
    return(city_list)


def get_state_cities(state_city_df) :
    
    states  =    state_city_df["State"].unique().tolist()
    states.sort()
    
    print("get_state_cities states ",states)
    
    state_cities    =   {}
    
    for i in range(len(states)) :
        
        city_list           =   state_city_df.loc[state_city_df["State"] == states[i],["City"]]["City"].unique().tolist()
        city_list.sort()
        
        state_cities.update({states[i]:city_list})
        
    return(state_cities)


def get_state_counties(state_county_df) :
    
    states  =    state_county_df["State"].unique().tolist()
    states.sort()
    
    print("get_state_counties states ",states)
    
    state_counties    =   {}
    
    for i in range(len(states)) :
        
        county_list           =   state_county_df.loc[state_county_df["State"] == states[i],["County"]]["County"].unique().tolist()
        county_list.sort()
        
        state_counties.update({states[i]:county_list})
        
    return(state_counties)


def get_states(state_county_df) :
    
    states  =    state_county_df["State"].unique().tolist()
    states.sort()
    
    print("get_states ",states)
    
    return(states)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               summary roll ups 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def sum_city_zips_cols(city_zips_df) :

    #print("summing")
    import pandas as pd
    
    city_zip_df_cols    =   city_zips_df.columns.tolist()
    nans_list           =   city_zips_df.isnull().sum(axis = 0)
    num_rows            =   len(city_zips_df)
    
    divisors            =   []
    
    for i in range(len(city_zip_df_cols)) :
        if(city_zip_df_cols[i].endswith("_total")) :
            divisors.append(1.0)
        else :
            divisors.append(num_rows-nans_list[i])
    
    city_zips_df.fillna(0,inplace=True)
                        
    divisor_series          =   pd.Series(divisors, index=city_zip_df_cols)
    city_data_summary       =   city_zips_df.sum(axis=0,skipna=True,level=None,numeric_only=True)
    city_data_summary       =   city_data_summary.divide(divisor_series)
    city_data_summary_df    =   pd.DataFrame([city_data_summary])
    
    return(city_data_summary_df)
        

import datetime
last_timestamp  =   0

def display_time_diff(title) :
    
    global last_timestamp
    
    time_now    =   datetime.datetime.now()
    
    if(last_timestamp == 0) :
        last_timestamp   =   datetime.datetime.now()
        timedelta  =  time_now - last_timestamp
    else :
        timedelta  =  time_now - last_timestamp
        last_timestamp  =   time_now
        
    #print(title," : ",(timedelta.days * 86400000) + (timedelta.seconds * 1000) + (timedelta.microseconds / 1000))
    print(title," : ",(timedelta.seconds))
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               build summary datasets 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def build_city_summary_dataset(zipcodes_df,state_city_df,state_cities,ds_path) :
    
    print("\nbuild_city_summary_dataset",ds_path)
    display_time_diff("build_city_summary_dataset : start ")
    import pandas as pd
    
    states          =   list(state_cities.keys())
    states.sort()
    
    
    zip_df_cols     =   zipcodes_df.columns.tolist()
    zip_df_cols.remove("Zip Code")
    
    city_summary_col_names  =   [swcm.STATE_KEY,swcm.CITY_KEY]
    
    for i in range(len(zip_df_cols)) :
        city_summary_col_names.append(zip_df_cols[i])    
    
    city_summary_df =   pd.DataFrame(columns=city_summary_col_names)
    
    for i in range(len(states)) :
        
        cities  =   state_cities.get(states[i])
        
        for j in range(len(cities)) :
            
            zips    =   get_city_zips(states[i],cities[j],state_city_df)
            
            criteria        =   (zipcodes_df["Zip Code"].isin(zips)) 
            city_zips_df    =   zipcodes_df[criteria]
                
            city_zips_df.drop(swcm.ZIP_CODE_KEY,axis=1,inplace=True)
            
            if(len(city_zips_df) > 1) :
                current_city_df     =   sum_city_zips_cols(city_zips_df)
                
            else :
                current_city_df     =   city_zips_df
                
            if(len(current_city_df) > 0) :
                current_city_df.insert(0,swcm.STATE_KEY,states[i])
                current_city_df.insert(1,swcm.CITY_KEY,cities[j])
            
                current_row     =   current_city_df.iloc[0]
                
                city_summary_df.loc[len(city_summary_df)] = current_row

        if( (not(i == 0)) and ((i%5) == 0)) :
            csv_path    =   ds_path.replace(".csv","_" + str(i) + "_.csv")
            city_summary_df.to_csv(csv_path,index=False)    
            city_summary_df =   pd.DataFrame(columns=city_summary_col_names)
            print("write csv",csv_path)

        display_time_diff("state [" + str(i) + "] " + states[i] + " " + str(len(cities)) + " df : " + str(len(city_summary_df)))

    if(len(city_summary_df) > 0) :   
        city_summary_df.to_csv(ds_path,index=False)
    


def build_county_summary_dataset(cities_df,state_county_cities_df,state_counties,ds_path) :
    
    print("\nbuild_county_summary_dataset",ds_path)
    display_time_diff("build_county_summary_dataset : start ")
    import pandas as pd
    
    states          =   list(state_counties.keys())
    states.sort()
    
    
    cities_df_cols     =   cities_df.columns.tolist()
    cities_df_cols.remove(swcm.STATE_KEY)
    cities_df_cols.remove(swcm.CITY_KEY)
    
    
    county_summary_col_names  =   [swcm.STATE_KEY,swcm.COUNTY_KEY]
    
    for i in range(len(cities_df_cols)) :
        county_summary_col_names.append(cities_df_cols[i])    
    
    county_summary_df =   pd.DataFrame(columns=county_summary_col_names)
    
    for i in range(len(states)) :
        
        counties  =   state_counties.get(states[i])
        
        for j in range(len(counties)) :
            
            cities    =   get_county_cities(states[i],counties[j],state_county_cities_df)

            criteria        =   (cities_df["State"] == states[i]) 
            criteria1       =   (cities_df["City"].isin(cities)) 
            
            county_cities_df    =   cities_df[criteria & criteria1]
            
            county_cities_df.drop(swcm.STATE_KEY,axis=1,inplace=True)
            county_cities_df.drop(swcm.CITY_KEY,axis=1,inplace=True)
            
            if(len(county_cities_df) > 1) :
                current_county_df     =   sum_city_zips_cols(county_cities_df)
                
            else :
                current_county_df     =   county_cities_df
                
            if(len(current_county_df) > 0) :
                
                #print("add county city row")
                current_county_df.insert(0,swcm.STATE_KEY,states[i])
                current_county_df.insert(1,swcm.COUNTY_KEY,counties[j])
            
                current_row     =   current_county_df.iloc[0]
            
                county_summary_df.loc[len(county_summary_df)] = current_row

        if( (not(i == 0)) and ((i%5) == 0)) :
            csv_path    =   ds_path.replace(".csv","_" + str(i) + "_.csv")
            county_summary_df.to_csv(csv_path,index=False)    
            county_summary_df =   pd.DataFrame(columns=county_summary_col_names)
            print("write csv",csv_path)

        display_time_diff("state [" + str(i) + "] " + states[i] + " " + str(len(counties)) + " df : " + str(len(county_summary_df)))

        
    county_summary_df.to_csv(ds_path,index=False)


    
def build_state_summary_dataset(counties_df,states,ds_path)  : 
    
    print("\nbuild_county_summary_dataset",ds_path)
    display_time_diff("build_county_summary_dataset : start ")
    import pandas as pd
    
    counties_df_cols     =   counties_df.columns.tolist()
    counties_df_cols.remove(swcm.STATE_KEY)
    counties_df_cols.remove(swcm.COUNTY_KEY)
    
    
    state_summary_col_names  =   [swcm.STATE_KEY]
    
    for i in range(len(counties_df_cols)) :
        state_summary_col_names.append(counties_df_cols[i])    
    
    state_summary_df =   pd.DataFrame(columns=state_summary_col_names)
    
    for i in range(len(states)) :
        
        criteria        =   (counties_df["State"] == states[i]) 
            
        state_counties_df    =   counties_df[criteria]
            
        state_counties_df.drop(swcm.STATE_KEY,axis=1,inplace=True)
        state_counties_df.drop(swcm.COUNTY_KEY,axis=1,inplace=True)
            
        if(len(state_counties_df) > 1) :
            current_state_df     =   sum_city_zips_cols(state_counties_df)
                
        else :
            current_state_df     =   state_counties_df
                
        if(len(current_state_df) > 0) :
                
            current_state_df.insert(0,swcm.STATE_KEY,states[i])
            
            current_row     =   current_state_df.iloc[0]
            
            state_summary_df.loc[len(state_summary_df)] = current_row
    
        if( (not(i == 0)) and ((i%20) == 0)) :
            csv_path    =   ds_path.replace(".csv","_" + str(i) + "_.csv")
            state_summary_df.to_csv(csv_path,index=False)    
            state_summary_df =   pd.DataFrame(columns=state_summary_col_names)
            print("write csv",csv_path)

    state_summary_df.to_csv(ds_path,index=False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               split and merge summary datasets 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def calc_city_stats() :
    
    import os
    import pandas as pd
        
    import json
    
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\final\\cities\\")
    
    dfc_census_stats_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_stats_path    =   (dfc_census_stats_path + "\\datasets\\intermediate\\dataset_stats\\cities\\")

    fnames   =   ["economic","education","employment","health_insurance","housing",
                  "immigration","internet","population","social","social","transportation"]
    
    dfnansA     =   []
    
    for i in range(len(fnames)) :
        
        if(i==8) :
            current_df  =   pd.read_csv(dfc_census_path + fnames[i] + "_cities_A.csv")
        elif(i==9) :
            current_df  =   pd.read_csv(dfc_census_path + fnames[i] + "_cities_B.csv")
        else :    
            current_df  =   pd.read_csv(dfc_census_path + fnames[i] + "_cities.csv")
            
        colnames    =   current_df.columns.tolist()

        if(not (i==9)) :
            with open(dfc_census_stats_path + fnames[i] +'_cities_colnames.txt', 'w') as outfile:
                json.dump(colnames, outfile)
                
            dftypes      =  current_df.dtypes.tolist() 
            dftypes_str  =   []
            
            print("get dtypes",i)

            for p in range(len(dftypes)) :
                dtstr   =   get_dtype_str_for_datatype(dftypes[p])
                dftypes_str.append(dtstr)
                
            with open(dfc_census_stats_path+"\\"+ fnames[i] +'_cities_dtypes.txt', 'w') as outfile:
                json.dump(dftypes_str, outfile)
                
        
        dfnans  =   current_df.isnull().sum(axis = 0).tolist()
        
        if(i==8) :
            dfnansA     =   dfnans
        elif(i==9) :
            for k in range(len(dfnans)) :
                dfnans[k]   =   dfnans[k] + dfnansA[k]
        
        with open(dfc_census_stats_path+"\\"+ fnames[i] +'_cities_nanscount.txt', 'w') as outfile:
            json.dump(dfnans, outfile)

def calc_county_stats() :
    
    import os
    import pandas as pd
        
    import json
    
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\final\\counties\\")
    
    dfc_census_stats_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_stats_path    =   (dfc_census_stats_path + "\\datasets\\intermediate\\dataset_stats\\counties\\")

    fnames   =   ["economic","education","employment","health_insurance","housing",
                  "immigration","internet","population","social","social","transportation"]
    
    for i in range(len(fnames)) :
        
        current_df  =   pd.read_csv(dfc_census_path + fnames[i] + "_counties.csv")
            
        colnames    =   current_df.columns.tolist()

        with open(dfc_census_stats_path + fnames[i] +'_counties_colnames.txt', 'w') as outfile:
            json.dump(colnames, outfile)
                
        dftypes      =  current_df.dtypes.tolist() 
        dftypes_str  =   []
            
        print("get dtypes",i)
            
        for p in range(len(dftypes)) :
            dtstr   =   get_dtype_str_for_datatype(dftypes[p])
            dftypes_str.append(dtstr)
                
        with open(dfc_census_stats_path+"\\"+ fnames[i] +'_counties_dtypes.txt', 'w') as outfile:
            json.dump(dftypes_str, outfile)
                
        
        dfnans  =   current_df.isnull().sum(axis = 0).tolist()
        with open(dfc_census_stats_path+"\\"+ fnames[i] +'_counties_nanscount.txt', 'w') as outfile:
            json.dump(dfnans, outfile)


def calc_state_stats() :
    
    import os
    import pandas as pd
        
    import json
    
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\final\\states\\")
    
    dfc_census_stats_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_stats_path    =   (dfc_census_stats_path + "\\datasets\\intermediate\\dataset_stats\\states\\")

    fnames   =   ["economic","education","employment","health_insurance","housing",
                  "immigration","internet","population","social","social","transportation"]
    
    for i in range(len(fnames)) :
        
        current_df  =   pd.read_csv(dfc_census_path + fnames[i] + "_states.csv")
            
        colnames    =   current_df.columns.tolist()

        with open(dfc_census_stats_path + fnames[i] +'_states_colnames.txt', 'w') as outfile:
            json.dump(colnames, outfile)
                
        dftypes      =  current_df.dtypes.tolist() 
        dftypes_str  =   []
            
        print("get dtypes",i)
            
        for p in range(len(dftypes)) :
            dtstr   =   get_dtype_str_for_datatype(dftypes[p])
            dftypes_str.append(dtstr)
                
        with open(dfc_census_stats_path+"\\"+ fnames[i] +'_states_dtypes.txt', 'w') as outfile:
            json.dump(dftypes_str, outfile)
                
        
        dfnans  =   current_df.isnull().sum(axis = 0).tolist()
        with open(dfc_census_stats_path+"\\"+ fnames[i] +'_states_nanscount.txt', 'w') as outfile:
            json.dump(dfnans, outfile)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#               split and merge summary datasets 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def split_zipcode_datasets() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")

    fnames   =   ["employment"]#"economic","education","housing","social"]
   
    for i in range(len(fnames)) :
        
        current_df   =   pd.read_csv(dfc_census_path + fnames[i] + "_zipcode.csv")
        
        criteria    =   (current_df[swcm.ZIP_CODE_KEY] < int("58000")) 
        split_df    =   current_df[criteria]
        
        split_df.to_csv(dfc_census_path + fnames[i] + "_zipcode_A.csv",index=False) 

        criteria    =   (current_df[swcm.ZIP_CODE_KEY] > int("58000")) 
        split_df    =   current_df[criteria]
        
        split_df.to_csv(dfc_census_path + fnames[i] + "_zipcode_B.csv",index=False) 


def split_city_datasets() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")

    fnames   =   ["education"]
   
    for i in range(len(fnames)) :
        
        current_df   =   pd.read_csv(dfc_census_path + fnames[i] + "_cities.csv")
        
        criteria    =   (current_df[swcm.STATE_KEY] < "NY") 
        split_df    =   current_df[criteria]
        
        split_df.to_csv(dfc_census_path + fnames[i] + "_cities_A.csv",index=False) 

        criteria    =   (current_df[swcm.STATE_KEY] >= "NY") 
        split_df    =   current_df[criteria]
        
        split_df.to_csv(dfc_census_path + fnames[i] + "_cities_B.csv",index=False) 


def merge_county_dfs() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    

    filenames   =   ["economic","education","employment","health_insurance","housing","immigration","internet","population","social","transportation"]
    
    files       =   ["10","15","20","25","30","35","40","45","50"]
    
    for i in range(len(filenames)) :
    
        current_counties_df             =   pd.read_csv(dfc_census_path + filenames[i] + "_counties_5_.csv")
        print("current " + filenames[i] + " counties : ",len(current_counties_df))
        
        for j in range(len(files)) :

            work_counties_df        =   pd.read_csv(dfc_census_path + filenames[i] + "_counties_" + files[j] + "_.csv")
            current_counties_df     =   current_counties_df.append(work_counties_df,ignore_index=True)
            print("current " + filenames[i] + " counties : ",len(current_counties_df))
            
        work_counties_df        =   pd.read_csv(dfc_census_path + filenames[i] + "_counties.csv")
        current_counties_df     =   current_counties_df.append(work_counties_df,ignore_index=True)
        print("current " + filenames[i] + " counties : ",len(current_counties_df))
            
        current_counties_df.to_csv(dfc_census_path + filenames[i] + "_counties_final.csv",index=False)    
       


def merge_city_dfs() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    

    fnames   =   ["economic","education","employment","health_insurance","housing"]
    
    frevs    =   ["10","20","30","40","50"]
    
    for i in range(len(fnames)) :
    
        last_cities_df   =   pd.read_csv(dfc_census_path + fnames[i] + "_cities.csv")
        colnames    =   last_cities_df.columns.tolist()
        current_cities_df =   pd.DataFrame(columns=colnames)
        
        for j in range(len(frevs)) :

            work_cities_df        =   pd.read_csv(dfc_census_path + fnames[i] + "_cities_" + frevs[j] + "_.csv")
            current_cities_df     =   current_cities_df.append(work_cities_df,ignore_index=True)
            print("current " + fnames[i] + " cities : ",len(current_cities_df))
            
        current_cities_df     =   current_cities_df.append(last_cities_df,ignore_index=True)
        
        current_cities_df.to_csv(dfc_census_path + fnames[i] + "_cities_final.csv",index=False) 

    filenames   =   ["immigration","internet","population","social","transportation"]
    
    files       =   ["10","15","20","25","30","35","40","45","50","55"]
    
    for i in range(len(filenames)) :
    
        current_cities_df             =   pd.read_csv(dfc_census_path + filenames[i] + "_cities_5_.csv")
        print("current " + filenames[i] + " cities : ",len(current_cities_df))
        
        for j in range(len(files)) :

            work_cities_df        =   pd.read_csv(dfc_census_path + filenames[i] + "_cities_" + files[j] + "_.csv")
            current_cities_df     =   current_cities_df.append(work_cities_df,ignore_index=True)
            print("current " + filenames[i] + " cities : ",len(current_cities_df))
            
            if( (i==3) and (j==5) ):
                current_cities_df.to_csv(dfc_census_path + filenames[i] + "_cities_A.csv",index=False) 
                colnames    =   current_cities_df.columns.tolist()
                current_cities_df =   pd.DataFrame(columns=colnames)
                
            
        if(i==3) :    
            current_cities_df.to_csv(dfc_census_path + filenames[i] + "_cities_B.csv",index=False) 
        else :
            current_cities_df.to_csv(dfc_census_path + filenames[i] + "_cities.csv",index=False)    

def merge_state_dfs() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    

    filenames   =   ["economic","education","employment","health_insurance","housing","immigration","internet","population","social","transportation"]
    
    for i in range(len(filenames)) :
    
        current_states_df             =   pd.read_csv(dfc_census_path + filenames[i] + "_states_20_.csv")
        
        work_states_df        =   pd.read_csv(dfc_census_path + filenames[i] + "_states_40_.csv")
        current_states_df     =   current_states_df.append(work_states_df,ignore_index=True)
            
        work_states_df        =   pd.read_csv(dfc_census_path + filenames[i] + "_states.csv")
        current_states_df     =   current_states_df.append(work_states_df,ignore_index=True)
        print("current " + filenames[i] + " states : ",len(current_states_df))
            
        current_states_df.to_csv(dfc_census_path + filenames[i] + "_states_final.csv",index=False)    
 
      
def build_us_dfs() :
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\final\\states\\")
    

    filenames   =   ["economic","education","employment","health_insurance","housing","immigration","internet","population","social","transportation"]
    
    for i in range(len(filenames)) :
    
        states_df       =   pd.read_csv(dfc_census_path + filenames[i] + "_states.csv")
        criteria        =   (states_df["State"].isnull()) 
            
        current_states_df       =   states_df[~criteria]
            
        current_states_df.drop(swcm.STATE_KEY,axis=1,inplace=True)
            
        if(len(current_states_df) > 1) :
            current_us_df     =   sum_city_zips_cols(current_states_df)
            current_us_df.insert(0,swcm.STATE_KEY,"US")
            current_row     =   current_us_df.iloc[0]
            states_df.loc[len(states_df)] = current_row
    
        print("us summary for ",filenames[i])
        states_df.to_csv(dfc_census_path + filenames[i] + "_states.csv",index=False)




       
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                       summary builds 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def build_county_datasets(state_county_cities_df,dfc_census_path) :
    
    import pandas as pd

    state_counties        =   get_state_counties(state_county_cities_df)
    
    for i in range(len(swcm.census_data_dirs)) :
        
        print("summing counties for ",swcm.census_data_dirs[i])
        
        if(i==8) :
            cities_df       =   pd.read_csv(dfc_census_path + "final\\cities\\" + swcm.census_data_dirs[i] + "_cities_A.csv")
            cities_2_df     =   pd.read_csv(dfc_census_path + "final\\cities\\" + swcm.census_data_dirs[i] + "_cities_B.csv")
            cities_df       =   cities_df.append(cities_2_df,ignore_index=True)
            
        else :
    
            cities_df       =   pd.read_csv(dfc_census_path + "final\\cities\\" + swcm.census_data_dirs[i] + "_cities.csv")
            
        
        build_county_summary_dataset(cities_df,state_county_cities_df,state_counties,dfc_census_path + swcm.census_data_dirs[i] + "_counties.csv") 


def build_state_datasets(state_county_cities_df,dfc_census_path) :
    
    import pandas as pd
    
    states        =   get_states(state_county_cities_df)
    
    for i in range(len(swcm.census_data_dirs)) :
        
        counties_df       =   pd.read_csv(dfc_census_path + "final\\counties\\" + swcm.census_data_dirs[i] + "_counties.csv")
        build_state_summary_dataset(counties_df,states,dfc_census_path + swcm.census_data_dirs[i] + "_states.csv") 
    
    







    


def build_summary_datasets() :
    
    """
    for i in range(len(statecities)) :
        
        if(not(statecities[i] in df_statecities)) :
        
            print("not found",statecities[i])
                
    
    return()
    """

    
    
    
    import os
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    
    dfc_index_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_index_path     =   (dfc_index_path + "\\indices\\")
    
    state_county_cities_file_name   =   "state_county_cities.csv"
    state_county_cities_df          =   pd.read_csv(dfc_index_path + state_county_cities_file_name)
    #state_county_cities_df.set_index(["State","County"],inplace=True)
    
    state_city_zips_file_name       =   "state_city_zips.csv"
    state_city_zips_df              =   pd.read_csv(dfc_index_path + state_city_zips_file_name)
    state_city_zips_df.set_index(["State","City"])
    
    #split_zipcode_datasets()
    
    build_us_dfs()
    
    return()
    
    
def process_census_load(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : load the census data into dataframes
    * 
    * parms :
    *  parms      - associated data selected parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    clean_raw()
    return()
    opstat          =   opStatus()
    
    content_cbs     =   parms[0]  
    keys_cbs        =   parms[1]
    
    print(content_cbs,keys_cbs)
    
    import os
    import pandas
    
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\")
    
    if(0):    
        build_census_percent_dfs(parms)
        
    if(0):# (keys_cbs[1] == "True") or (keys_cbs[2] == "True") or (keys_cbs[3] == "True") ) :
    
        build_zip_code_mappings()
    
    
    pct_df     =   pandas.read_csv(dfc_census_path+swcm.DEMOGRAPHICS_PERCENT_FILE)
    new_dfcnotes    =   "demo pct"
    new_dfcdf       =   cfg.dfc_dataframe(swcm.DEMOGRAPHICS_PERCENT_DF_TITLE,pct_df,new_dfcnotes)
    cfg.add_dfc_dataframe(new_dfcdf)

    pct_df     =   pandas.read_csv(dfc_census_path+swcm.ECONOMICS_PERCENT_FILE)
    new_dfcnotes    =   "econ pct"
    new_dfcdf       =   cfg.dfc_dataframe(swcm.ECONOMICS_PERCENT_DF_TITLE,pct_df,new_dfcnotes)
    cfg.add_dfc_dataframe(new_dfcdf)

    pct_df     =   pandas.read_csv(dfc_census_path+swcm.HOUSING_PERCENT_FILE)
    new_dfcnotes    =   "housing pct"
    new_dfcdf       =   cfg.dfc_dataframe(swcm.HOUSING_PERCENT_DF_TITLE,pct_df,new_dfcnotes)
    cfg.add_dfc_dataframe(new_dfcdf)

    pct_df     =   pandas.read_csv(dfc_census_path+swcm.SOCIAL_PERCENT_FILE)
    new_dfcnotes    =   "social pct"
    new_dfcdf       =   cfg.dfc_dataframe(swcm.SOCIAL_PERCENT_DF_TITLE,pct_df,new_dfcnotes)
    cfg.add_dfc_dataframe(new_dfcdf)






    if(0):# not(opstat.get_status()) ) :
        
        #clock.stop()
        print("Unable to import Data : ")
        #display_exception(opstat)          
                


    else :    
    
        if( (keys_cbs[1] == "True") or (keys_cbs[2] == "True") or (keys_cbs[3] == "True") ) :
        
            clock = RunningClock()
            clock.start()

            try :
                zipcode_map     =   pandas.read_csv(dfc_census_path+swcm.CITY_COUNTY_FILE)
            except Exception as e:
                opstat.set_status(False)
                opstat.store_exception("error importing xipcode data",e)
                                            
            if(opstat.get_status()) :
            
                new_dfcnotes    =   "zip code mappings"
                new_dfcdf       =   cfg.dfc_dataframe("zipcode_mapings",zipcode_map,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfcdf)
        
                dtime   =   clock.stop()
                print("Total Zipcode Mapping Import Time : ",dtime)
                print("Zipcode Mapping : [",len(zipcode_map),",",len(zipcode_map.columns),"]")
                
            else :
                
                clock.stop()
                print("Unable to import Zipcode Data : ")
                display_exception(opstat)          

    build_zipcode_summary_tables([swcm.DEMOGRAPHICS,swcm.ECONOMICS,swcm.HOUSING,swcm.SOCIAL],
                                 cfg.get_dfc_dataframe_df("zipcode_mapings"))

def get_zc_subset_df(dataId,zclist)  :
    
    import pandas as pd
    
    if(dataId == swcm.DEMOGRAPHICS)  :
        zipcodedf   =   cfg.get_dfc_dataframe_df(swcm.DEMOGRAPHICS_PERCENT_DF_TITLE)
    elif(dataId == swcm.ECONOMICS) :
        zipcodedf   =   cfg.get_dfc_dataframe_df(swcm.ECONOMICS_PERCENT_DF_TITLE)
    elif(dataId == swcm.HOUSING)  :
        zipcodedf   =   cfg.get_dfc_dataframe_df(swcm.HOUSING_PERCENT_DF_TITLE)
    elif(dataId == swcm.SOCIAL) :
        zipcodedf   =   cfg.get_dfc_dataframe_df(swcm.SOCIAL_PERCENT_DF_TITLE)

    truth_table     =   pd.Series()
    truth_table     =   zipcodedf[swcm.ZIP_CODE_KEY].isin(zclist)
    zc_subset_df    =   zipcodedf[truth_table].copy()
   
    #print("zc_subset_df",zc_subset_df.shape)
    
    return(zc_subset_df)        

    
    
def build_summary_divisor_lists(dataid):


    # demographic summary divisors
    if(dataid   ==  swcm.DEMO_DATA) :  
        
        demodf              =   cfg.get_dfc_dataframe_df(swcm.DEMOGRAPHICS_PERCENT_DF_TITLE)
        demo_colnames_list  =   demodf.columns.tolist()
        del demo_colnames_list[0]
    
        demo_divisor_list   =   []
    
        for i in range(len(demo_colnames_list)) : 
            if(not(demo_colnames_list[i] == "Zip Code")) :
                if (demo_colnames_list[i].endswith("_total")) :
                    demo_divisor_list.append(1)
                else :
                    demo_divisor_list.append(0)
                    
        return([demo_colnames_list,demo_divisor_list])

    # economic summary divisors
    elif(dataid   ==  swcm.ECONOMIC_DATA) :  
    
        econdf              =   cfg.get_dfc_dataframe_df(swcm.ECONOMICS_PERCENT_DF_TITLE)
        econ_colnames_list  =   econdf.columns.tolist()
        del econ_colnames_list[0]

        econ_divisor_list   =   []
    
        for i in range(len(econ_colnames_list)) : 
            if(not(econ_colnames_list[i] == "Zip Code")) :
                if(econ_colnames_list[i].endswith("_total")) :
                    econ_divisor_list.append(1)
                else :
                    econ_divisor_list.append(0)
                    
        return([econ_colnames_list,econ_divisor_list])
    
    # housing summary divisors
    elif(dataid   ==  swcm.HOUSING_DATA) :  
    
        housingdf   =   cfg.get_dfc_dataframe_df(swcm.HOUSING_PERCENT_DF_TITLE)
    
        housing_colnames_list   =   housingdf.columns.tolist()
        del housing_colnames_list[0]
    
        housing_divisor_list    =   []
    
        for i in range(len(housing_colnames_list)) : 
            if(not(housing_colnames_list[i] == "Zip Code")) :
                if(housing_colnames_list[i].endswith("_total")) :
                    housing_divisor_list.append(1)
                else :
                    housing_divisor_list.append(0)
                
        return([housing_colnames_list,housing_divisor_list])
    
    # social summary divisors
    elif(dataid   ==  swcm.SOCIAL_DATA) :  

        socialdf    =   cfg.get_dfc_dataframe_df(swcm.SOCIAL_PERCENT_DF_TITLE)
   
        social_colnames_list   =   socialdf.columns.tolist()
        social_colnames_list[0]
        del social_colnames_list[0]
    
        social_divisor_list    =   []
    
        for i in range(len(social_colnames_list)) : 
            if(not(social_colnames_list[i] == "Zip Code")) :
                if(social_colnames_list[i].endswith("_total")) :
                    social_divisor_list.append(1)
                else :
                    social_divisor_list.append(0)
    
        return([social_colnames_list,social_divisor_list])
    
    
    else :
        
        return(None,None)
    
  
def build_city_summary_table(datakeylist,citystatedf,stateIds):
    
    import pandas as pd
    
    city_demographics_summary_df    =   pd.DataFrame()   
    city_economics_summary_df       =   pd.DataFrame()   
    city_social_summary_df          =   pd.DataFrame()   
    city_housing_summary_df         =   pd.DataFrame()

    missing_zipcodes_df             =   pd.DataFrame()    
    
    demo_data                       =   build_summary_divisor_lists(swcm.DEMO_DATA)
    demo_colnames_list              =   demo_data[0]
    demo_divisor_list               =   demo_data[1]
    
    econ_data                       =   build_summary_divisor_lists(swcm.ECONOMIC_DATA)
    econ_colnames_list              =   econ_data[0]
    econ_divisor_list               =   econ_data[1]
    
    housing_data                    =   build_summary_divisor_lists(swcm.HOUSING_DATA)
    housing_colnames_list           =   housing_data[0]
    housing_divisor_list            =   housing_data[1]
    
    social_data                     =   build_summary_divisor_lists(swcm.SOCIAL_DATA)
    social_colnames_list            =   social_data[0]
    social_divisor_list             =   social_data[1]
    
    import os
    
    dfc_census_path                 =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path                 =   (dfc_census_path + "\\")
    
    """
    " -----------------------------------------------------------
    " ---------------- City summary dataframes ------------------
    " -----------------------------------------------------------
    """
    clock = RunningClock()
    clock.start()
   
    for i in range(len(stateIds)) :
        
        state_truth     =   pd.Series()
        state_truth     =   citystatedf[swcm.STATE_KEY] == stateIds[i]
        state_df        =   citystatedf[state_truth].copy()
        
        city_uniques    =   state_df[swcm.CITY_KEY].unique()
        city_uniques.sort()
        print("state_df : ",state_df.shape,stateIds[i]," Num Cities ",len(city_uniques)," ",
              len(city_demographics_summary_df)," ",len(city_economics_summary_df),
              " ",len(city_housing_summary_df)," ",len(city_social_summary_df))
        
        for j in range(len(city_uniques)) :
            
            city_criteria   =   pd.Series()
            city_criteria   =   citystatedf[swcm.STATE_KEY] == stateIds[i]
            city_criteria1  =   pd.Series()
            city_criteria1  =   citystatedf[swcm.CITY_KEY] == city_uniques[j]
            city_truth      =   city_criteria & city_criteria1
            
            city_df         =   citystatedf[city_truth].copy()
            zc_uniques      =   city_df.iloc[0,5].split(' ')
            zc_uniques.sort()
            
            for k in range(len(datakeylist)) :
            
                city_data_df    =   get_zc_subset_df(datakeylist[k],zc_uniques)
                
                city_data_df.fillna(0,inplace=True)
                city_data_df.drop(swcm.ZIP_CODE_KEY,axis=1,inplace=True)
                
                if(len(city_data_df) > 1) :

                    if(k==0) :          
                        divisor_list    =   list(map(lambda x: 1 if x != 0 else len(city_data_df), demo_divisor_list))
                        colnames_list   =   demo_colnames_list
                    elif(k==1) :        
                        divisor_list    =   list(map(lambda x: 1 if x != 0 else len(city_data_df), econ_divisor_list))
                        colnames_list   =   econ_colnames_list
                    elif(k==2) :        
                        divisor_list    =   list(map(lambda x: 1 if x != 0 else len(city_data_df), housing_divisor_list))
                        colnames_list   =   housing_colnames_list
                    elif(k==3) :        
                        divisor_list    =   list(map(lambda x: 1 if x != 0 else len(city_data_df), social_divisor_list))
                        colnames_list   =   social_colnames_list
                    
                    divisor_series          =   pd.Series(divisor_list, index=colnames_list)
                    city_data_summary       =   city_data_df.sum(axis=0,skipna=True,level=None,numeric_only=True)
                    city_data_summary       =   city_data_summary.divide(divisor_series)
                    city_data_summary_df    =   pd.DataFrame([city_data_summary])

                else :
                    city_data_summary_df    =   city_data_df.copy()

                city_data_summary_df.insert(0,swcm.STATE_KEY,stateIds[i],True)
                city_data_summary_df.insert(1,swcm.CITY_KEY,city_uniques[j],True)
                
                if(datakeylist[k] == swcm.DEMOGRAPHICS) :
                    if(len(city_demographics_summary_df) == 0) :
                        city_demographics_summary_df    =   city_data_summary_df.copy() 
                    else :
                        city_demographics_summary_df    =   city_demographics_summary_df.append(city_data_summary_df,ignore_index=True)
                    
                elif(datakeylist[k] == swcm.ECONOMICS) :
                    if(len(city_economics_summary_df) == 0) :
                        city_economics_summary_df    =   city_data_summary_df.copy() 
                    else :
                        city_economics_summary_df    =   city_economics_summary_df.append(city_data_summary_df,ignore_index=True)
                    
                elif(datakeylist[k] == swcm.HOUSING) :
                    if(len(city_housing_summary_df) == 0) :
                        city_housing_summary_df    =   city_data_summary_df.copy() 
                    else :
                        city_housing_summary_df    =   city_housing_summary_df.append(city_data_summary_df,ignore_index=True)
                     
                elif(datakeylist[k] == swcm.SOCIAL) :
                    if(len(city_social_summary_df) == 0) :
                        city_social_summary_df    =   city_data_summary_df.copy() 
                    else :
                        city_social_summary_df    =   city_social_summary_df.append(city_data_summary_df,ignore_index=True)

         
                if(datakeylist[k] == swcm.DEMOGRAPHICS) :
                
                    sum_city_names      =   city_data_summary_df[swcm.CITY_KEY].tolist()
                    not_found_cities    =   []
                    for m in range (len(city_uniques)) :
                        if(not (city_uniques[m] in sum_city_names)) : 
                            not_found_cities.append(city_uniques[m])
        
                    missing_criteria      =   pd.Series()
                    missing_criteria      =   citystatedf[swcm.STATE_KEY] == stateIds[i]
                    missing_criteria1     =   pd.Series()
                    missing_criteria1     =   citystatedf[swcm.CITY_KEY].isin(not_found_cities)
                    missing_truth         =   missing_criteria & missing_criteria1
                    missing_df            =   citystatedf[missing_truth].copy()
        
                    if(len(missing_zipcodes_df) == 0) :
                        missing_zipcodes_df    =   missing_df.copy() 
                    else :
                        missing_zipcodes_df    =   missing_zipcodes_df.append(missing_df,ignore_index=True)
   

        
        city_demographics_summary_df.to_csv(dfc_census_path + stateIds[i] + "_" + swcm.DEMOGRAPHICS_CITY_FILE,index=False)
        city_economics_summary_df.to_csv(dfc_census_path + stateIds[i] + "_" + swcm.ECONOMICS_CITY_FILE,index=False)
        city_housing_summary_df.to_csv(dfc_census_path + stateIds[i] + "_" + swcm.HOUSING_CITY_FILE,index=False)
        city_social_summary_df.to_csv(dfc_census_path + stateIds[i] + "_" + swcm.SOCIAL_CITY_FILE,index=False)

        missing_zipcodes_df.to_csv(dfc_census_path + stateIds[i] + "_" + "Missing_Cities.csv",index=False)

         
    missing_zipcodes_df.to_csv(dfc_census_path + "Missing_Cities.csv",index=False)
            
    dtime   =   clock.stop()
    print("Total City Summary Build Time : ",dtime)
    print("Demographics : [",len(city_demographics_summary_df),"]")
    print("Econimics : [",len(city_economics_summary_df),"]")
    print("Housing : [",len(city_housing_summary_df),"]")
    print("Social : [",len(city_social_summary_df),"]")
    
            
    city_demographics_summary_df.to_csv(dfc_census_path + swcm.DEMOGRAPHICS_CITY_FILE,index=False)
    city_economics_summary_df.to_csv(dfc_census_path + swcm.ECONOMICS_CITY_FILE,index=False)
    city_housing_summary_df.to_csv(dfc_census_path + swcm.HOUSING_CITY_FILE,index=False)
    city_social_summary_df.to_csv(dfc_census_path + swcm.SOCIAL_CITY_FILE,index=False)


 
def build_state_summary_table(datakeylist,stateIds):
    
    import pandas as pd
    
    state_demographics_summary_df   =   pd.DataFrame()   
    state_economics_summary_df      =   pd.DataFrame()   
    state_social_summary_df         =   pd.DataFrame()   
    state_housing_summary_df        =   pd.DataFrame()

    demo_data                       =   build_summary_divisor_lists(swcm.DEMO_DATA)
    demo_colnames_list              =   demo_data[0]
    demo_divisor_list               =   demo_data[1]
    
    econ_data                       =   build_summary_divisor_lists(swcm.ECONOMIC_DATA)
    econ_colnames_list              =   econ_data[0]
    econ_divisor_list               =   econ_data[1]
    
    housing_data                    =   build_summary_divisor_lists(swcm.HOUSING_DATA)
    housing_colnames_list           =   housing_data[0]
    housing_divisor_list            =   housing_data[1]
    
    social_data                     =   build_summary_divisor_lists(swcm.SOCIAL_DATA)
    social_colnames_list            =   social_data[0]
    social_divisor_list             =   social_data[1]
    
    import os
    
    dfc_census_path                 =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path                 =   (dfc_census_path + "\\")
    
    city_demographics_summary_df    =   pd.read_csv(dfc_census_path + swcm.DEMOGRAPHICS_CITY_FILE,index=False)
    city_economics_summary_df       =   pd.read_csv(dfc_census_path + swcm.ECONOMICS_CITY_FILE,index=False)
    city_housing_summary_df         =   pd.read_csv(dfc_census_path + swcm.HOUSING_CITY_FILE,index=False)
    city_social_summary_df          =   pd.read_csv(dfc_census_path + swcm.SOCIAL_CITY_FILE,index=False)

    
    """
    " -----------------------------------------------------------
    " --------------- State summary dataframes ------------------
    " -----------------------------------------------------------
    """

    clock = RunningClock()
    clock.start()
    
    for i in range(len(stateIds)) :
        
        for j in range(len(datakeylist)) :
            
            if(datakeylist[j] == swcm.DEMOGRAPHICS) :
                city_df     =   city_demographics_summary_df        
            elif(datakeylist[j] == swcm.ECONOMICS) :
                city_df     =   city_economics_summary_df.append        
            elif(datakeylist[j] == swcm.HOUSING) :
                city_df     =   city_housing_summary_df.append        
            elif(datakeylist[j] == swcm.SOCIAL) :
                city_df     =   city_social_summary_df.appendcity_df       
            
            state_truth     =   pd.Series()
            state_truth     =   city_df[swcm.STATE_KEY] == stateIds[i]
            state_df        =   city_df[state_truth].copy()
        
            state_df.fillna(0,inplace=True)
            state_df.drop(swcm.STATE_KEY,axis=1,inplace=True)
            state_df.drop(swcm.CITY_KEY,axis=1,inplace=True)
            
            if(len(state_df) > 1) :
                    
                if(j==0) :          
                    divisor_list    =   list(map(lambda x: 1 if x != 0 else len(state_df), demo_divisor_list))
                    colnames_list   =   demo_colnames_list
                elif(j==1) :        
                    divisor_list    =   list(map(lambda x: 1 if x != 0 else len(state_df), econ_divisor_list))
                    colnames_list   =   econ_colnames_list
                elif(j==2) :        
                    divisor_list    =   list(map(lambda x: 1 if x != 0 else len(state_df), housing_divisor_list))
                    colnames_list   =   housing_colnames_list
                elif(j==3) :        
                    divisor_list    =   list(map(lambda x: 1 if x != 0 else len(state_df), social_divisor_list))
                    colnames_list   =   social_colnames_list
                        
                divisor_series      =   pd.Series(divisor_list, index=colnames_list)
                state_data_summary  =   state_df.sum(axis=0,skipna=True,level=None,numeric_only=True)
                state_data_summary  =   state_data_summary.divide(divisor_series)
                state_summary_df    =   pd.DataFrame([state_data_summary])
    
            else :
                state_summary_df    =   state_df.copy()

            state_summary_df.insert(0,swcm.STATE_KEY,stateIds[i],True)
            
            if(datakeylist[j] == swcm.DEMOGRAPHICS) :
                if(len(state_demographics_summary_df) == 0) :
                    state_demographics_summary_df    =   state_summary_df.copy() 
                else :
                    state_demographics_summary_df    =   city_demographics_summary_df.append(state_summary_df,ignore_index=True)
                
            elif(datakeylist[j] == swcm.ECONOMICS) :
                if(len(state_economics_summary_df) == 0) :
                    state_economics_summary_df    =   state_summary_df.copy() 
                else :
                    state_economics_summary_df    =   city_demographics_summary_df.append(state_summary_df,ignore_index=True)
                
            elif(datakeylist[j] == swcm.HOUSING) :
                if(len(state_housing_summary_df) == 0) :
                    state_housing_summary_df    =   state_summary_df.copy() 
                else :
                    state_housing_summary_df    =   city_demographics_summary_df.append(state_summary_df,ignore_index=True)
                
            elif(datakeylist[j] == swcm.SOCIAL) :
                if(len(state_social_summary_df) == 0) :
                    state_social_summary_df    =   state_summary_df.copy() 
                else :
                    state_social_summary_df    =   city_demographics_summary_df.append(state_summary_df,ignore_index=True)
                
    dtime   =   clock.stop()
    print("Total State Summary Build Time : ",dtime)
    print("Demographics : [",len(state_demographics_summary_df),"]")
    print("Econimics : [",len(state_economics_summary_df),"]")
    print("Housing : [",len(state_housing_summary_df),"]")
    print("Social : [",len(state_social_summary_df),"]")

    state_demographics_summary_df.to_csv(dfc_census_path + swcm.DEMOGRAPHICS_STATE_FILE,index=False)
    state_economics_summary_df.to_csv(dfc_census_path + swcm.ECONOMICS_STATE_FILE,index=False)
    state_housing_summary_df.to_csv(dfc_census_path + swcm.HOUSING_STATE_FILE,index=False)
    state_social_summary_df.to_csv(dfc_census_path + swcm.SOCIAL_STATE_FILE,index=False)


def build_us_summary_table(datakeylist):

    import pandas as pd
    
    """
    " -----------------------------------------------------------
    " ---------------- US summary dataframes --------------------
    " -----------------------------------------------------------
    """
    
    demo_data                       =   build_summary_divisor_lists(swcm.DEMO_DATA)
    demo_colnames_list              =   demo_data[0]
    demo_divisor_list               =   demo_data[1]
    
    econ_data                       =   build_summary_divisor_lists(swcm.ECONOMIC_DATA)
    econ_colnames_list              =   econ_data[0]
    econ_divisor_list               =   econ_data[1]
    
    housing_data                    =   build_summary_divisor_lists(swcm.HOUSING_DATA)
    housing_colnames_list           =   housing_data[0]
    housing_divisor_list            =   housing_data[1]
    
    social_data                     =   build_summary_divisor_lists(swcm.SOCIAL_DATA)
    social_colnames_list            =   social_data[0]
    social_divisor_list             =   social_data[1]
    
    import os
    
    dfc_census_path                 =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path                 =   (dfc_census_path + "\\")
    
    clock = RunningClock()
    clock.start()
    
    for i in range(len(datakeylist)) :
            
        if(datakeylist[i] == swcm.DEMOGRAPHICS) :
            us_df   =   pd.read_csv(dfc_census_path + swcm.DEMOGRAPHICS_STATE_FILE,index=False)
        elif(datakeylist[i] == swcm.ECONOMICS) :
            us_df   =   pd.read_csv(dfc_census_path + swcm.ECONOMICS_STATE_FILE,index=False)        
        elif(datakeylist[i] == swcm.HOUSING) :
            us_df   =   pd.read_csv(dfc_census_path + swcm.HOUSING_STATE_FILE,index=False)        
        elif(datakeylist[i] == swcm.SOCIAL) :
            us_df   =   pd.read_csv(dfc_census_path + swcm.SOCIAL_STATE_FILE,index=False) 
        
        us_df.fillna(0,inplace=True)
        us_df.drop(swcm.STATE_KEY,axis=1,inplace=True)
            
        if(len(us_df) > 1) :
                    
            if(i==0) :          
                divisor_list    =   list(map(lambda x: 1 if x != 0 else len(us_df), demo_divisor_list))
                colnames_list   =   demo_colnames_list
            elif(i==1) :        
                divisor_list    =   list(map(lambda x: 1 if x != 0 else len(us_df), econ_divisor_list))
                colnames_list   =   econ_colnames_list
            elif(i==2) :        
                divisor_list    =   list(map(lambda x: 1 if x != 0 else len(us_df), housing_divisor_list))
                colnames_list   =   housing_colnames_list
            elif(i==3) :        
                divisor_list    =   list(map(lambda x: 1 if x != 0 else len(us_df), social_divisor_list))
                colnames_list   =   social_colnames_list
                        
            divisor_series   =   pd.Series(divisor_list, index=colnames_list)
            us_data_summary  =   us_df.sum(axis=0,skipna=True,level=None,numeric_only=True)
            us_data_summary  =   us_data_summary.divide(divisor_series)
            us_summary_df    =   pd.DataFrame([us_data_summary])
    
        else :
            us_summary_df    =   us_df.copy()

        if(datakeylist[i] == swcm.DEMOGRAPHICS) :
            us_summary_df.to_csv(dfc_census_path + swcm.DEMOGRAPHICS_US_FILE,index=False)
        elif(datakeylist[i] == swcm.ECONOMICS) :
            us_summary_df.to_csv(dfc_census_path + swcm.ECONOMICS_US_FILE,index=False)        
        elif(datakeylist[i] == swcm.HOUSING) :
            us_summary_df.to_csv(dfc_census_path + swcm.HOUSING_US_FILE,index=False)        
        elif(datakeylist[i] == swcm.SOCIAL) :
            us_summary_df.to_csv(dfc_census_path + swcm.SOCIAL_US_FILE,index=False) 

    dtime   =   clock.stop()
    print("Total US Summary Build Time : ",dtime)
    

def build_zipcode_summary_tables(datakeylist,citystatedf) :
    
    #resolve_city_zipcodes()

    #return()    
    from dfcleanser.sw_utilities.sw_utility_control import get_Dict
    stateNamesDict  =   get_Dict("US_States_and_Territories")
    stateIds        =   list(stateNamesDict.keys())
    stateIds.sort()
    
    print("stateIds",stateIds)
    print("citystatedf",citystatedf.shape)
    
    build_city_summary_table(datakeylist,citystatedf,stateIds)

    build_state_summary_table(datakeylist,stateIds)   

    build_us_summary_table(datakeylist)
            

def get_city_zips1(stateIds) :
    
    import pands as pd
    
    import os
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\")
    
    city_zip_df         =   pd.read_csv(dfc_census_path + swcm.CITY_ZIP_FILE)
    state_city_df       =   pd.DataFrame()   
    
    clock = RunningClock()
    clock.start()

    for i in range(len(stateIds)) :
        
        print("state Processing : ",stateIds[i])
        
        state_truth     =   pd.Series()
        state_truth     =   city_zip_df[swcm.STATE_KEY] == stateIds[i]
        state_df        =   city_zip_df[state_truth].copy()
        
        cities  =   list(state_df[swcm.CITY_KEY].unique())
        cities.sort()
        
        for j in range(len(cities)) :
            
            city_truth  =   pd.Series()
            city_truth  =   state_df[swcm.CITY_KEY] == cities[j]
            city_df     =   state_df[city_truth].copy()
            
            zips        =   list(city_df[swcm.ZIP_CODE_KEY])
            zips.sort()
            
            import json
            city_zips_vals  =   [stateIds[i],cities[j],json.dumps(zips)]
            city_zips_cols  =   [swcm.STATE_KEY,swcm.CITY_KEY,swcm.ZIP_CODES_KEY]
            
            city_zips_df   =   pd.DataFrame(data=[city_zips_vals],columns=city_zips_cols) 
        
            if(len(state_city_df) == 0) :
                state_city_df   =    city_zips_df.copy() 
            else :
                state_city_df   =   state_city_df.append(city_zips_df)
        
        print("state_city_df",state_city_df.shape)
            
            
    state_city_df.to_csv(dfc_census_path + swcm.CITY_STATE_FILE,index=False)
    
    dtime   =   clock.stop()
    print("Total resolve zip codes Time : ",dtime)
    


            
def resolve_city_zipcodes() :
    
    import pandas as pd
            
    import os
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\")
        
        
    from dfcleanser.sw_utilities.sw_utility_control import get_Dict
    stateNamesDict  =   get_Dict("US_States_and_Territories")
    stateIds        =   list(stateNamesDict.keys())
    stateIds.sort()
    
    #get_city_zips(stateIds) 
    
    missing_zips_df   =   pd.DataFrame()   

    clock = RunningClock()
    clock.start()
            
    city_state_df       =   pd.read_csv(dfc_census_path + swcm.CITY_STATE_FILE)
    city_county_df      =   pd.read_csv(dfc_census_path + swcm.CITY_COUNTY_FILE)

    #for i in range(len(city_county_df)) :
    #    city_county_df.iloc[i,0]    =    city_county_df.iloc[i,0].upper()       
    city_county_df[[swcm.ZIP_CODES_KEY]] = city_county_df[[swcm.ZIP_CODES_KEY]].fillna(value=0)
    city_county_df.to_csv(dfc_census_path + swcm.CITY_COUNTY_FILE,index=False)

    for i in range(1):#len(stateIds)) :

        city_truth  =   pd.Series()
        city_truth  =   city_county_df[swcm.STATE_KEY] == stateIds[i]
        city_df     =   city_county_df[city_truth].copy()
            
        cities      =   list(city_df[swcm.CITY_KEY])
        cities.sort()
        
        print("stateIds[i] ",stateIds[i])
        city_criteria   =   pd.Series()
        city_criteria   =   city_state_df[swcm.STATE_KEY] == stateIds[i]
        cities1         =   list(city_state_df[city_criteria]).copy()
        cities1.sort()
        
        print("cities : ",len(cities))
        
        for j in range(len(cities)) :
        
            print("city : ",cities[j])
            
            zip_truth   =   pd.Series()
            zip_truth   =   city_df[swcm.CITY_KEY] == cities[j]
            zip_df      =   city_df[zip_truth].copy()
        
            zips        =   zip_df[swcm.ZIP_CODES_KEY]
            zips_list   =   zips.tolist()
            zips_list   =   zips_list[0].split()
            zips_list.sort()
            
            zip1_truth   =   pd.Series()
            zip1_truth   =   city_state_df[swcm.CITY_KEY] == cities[j]#.upper()
            zip1_df      =   city_state_df[zip1_truth].copy()
            
            print("city : ",cities[j],zips_list)
            
            if(zip1_df.empty) :
                
                missing_zip_vals    =   [stateIds[i],cities[j],0]
                missing_zip_cols    =   [swcm.STATE_KEY,swcm.CITY_KEY,swcm.ZIP_CODE_KEY]
                missing_zip_df      =   pd.DataFrame(data=[missing_zip_vals],columns=missing_zip_cols) 
                 
                if(len(missing_zips_df) == 0) :
                    missing_zips_df    =   missing_zip_df.copy() 
                else :
                    missing_zips_df    =   missing_zips_df.append(missing_zip_df,ignore_index=True)
                    
                print("missing city : ",missing_zip_vals)
            
            else :
                
                ziplist             =   zip1_df.iloc[0,2].strip('][').split(', ')
                zip1_df.iloc[0,2]   =   ziplist
                zips1               =   zip1_df[swcm.ZIP_CODES_KEY]
            
                zips1_list   =   zips1.iloc[0]
                zips1_list.sort()
            
                missing_zip_df  =   pd.DataFrame()
            
                if(len(zips_list) > 1) :
                    print("multiple zips : ",stateIds[i],cities[j],len(zips_list),zips_list)
                    
                for k in range(len(zips_list)) :
                    
                    if( not(zips_list[k] in zips1_list)) :
                    
                        missing_zip_vals    =   [stateIds[i],cities[j],zips_list[k]]
                        print("missing zip",missing_zip_vals,zips_list[k])
                        missing_zip_cols    =   [swcm.STATE_KEY,swcm.CITY_KEY,swcm.ZIP_CODE_KEY]
                        missing_zip_df      =   pd.DataFrame(data=[missing_zip_vals],columns=missing_zip_cols) 
                 
                        if(len(missing_zips_df) == 0) :
                            missing_zips_df    =   missing_zip_df.copy() 
                        else :
                            missing_zips_df    =   missing_zips_df.append(missing_zip_df,ignore_index=True)


    missing_zips_df.to_csv(dfc_census_path + swcm.CITY_STATE_FILE,index=False)

    dtime   =   clock.stop()
    print("Total missing zip codes Time : ",dtime)



def is_valid_input(numerator,denominator) :
    import numpy as np
    
    if( (np.isnan(numerator)) or (np.isnan(denominator)) or (denominator == 0) ) :
        return(False)
    else :
        return(True)




def download_extract_zip(url,filename):
    
    #import requests
    #import io
    #import zipfile
    
    #import shutil
    
    #clock = RunningClock()
    #clock.start()

    print("download_extract_zip",url,filename)
    return()

    """    
    local_filename = filename
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    
    return()
    """
    #return()
    """
    Download a ZIP file and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    
    print(response.status_code)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield zipinfo.filename, thefile
                
            f= open(filename,"w+")
            f.write(thefile)
            f.close() 
            
    print("download_extract_zip done",url,filename)
    #clock.stop()

def what_the_fuck(url,filename):
    print("what_the_fuck",url,filename)
    
    response = requests.get(url, stream=True, verify=False)
    
    print("status code",response.status_code)
    print("headers",response.headers)
    
    return()
    print("length",int(response.headers['content-length']))
    
    
    local_filename = filename
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    
    print("what_the_fuck : done",url,filename)








    
    
    
    
    
    
    
    
    
    
    
    



