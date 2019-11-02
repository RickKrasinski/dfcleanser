"""
# cell_utils
"""
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 25 10:29:48 2018

@author: Rick
"""

import sys
this = sys.modules[__name__]


DC_TITLE_ID                         =   0
DC_SYSTEM_ID                        =   1
DC_DATA_IMPORT_ID                   =   2
DC_DATA_INSPECTION_ID               =   3
DC_DATA_CLEANSING_ID                =   4
DC_DATA_TRANSFORM_ID                =   5
DC_DATA_EXPORT_ID                   =   6
DC_SW_UTILITIES_ID                  =   7
DC_DATASTRUCT_UTILITY_ID            =   8
DC_GEOCODE_UTILITY_ID               =   9
DC_DFSUBSET_UTILITY_ID              =   10
DC_CENSUS_UTILITY_ID                =   11
DC_DATA_SCRIPT_ID                   =   12
DC_WORKING_ID                       =   13

SYSTEM_TASK_BAR_ID                  =   14
IMPORT_TASK_BAR_ID                  =   15
INSPECTION_TASK_BAR_ID              =   16
CLEANSING_TASK_BAR_ID               =   17
TRANSFORM_TASK_BAR_ID               =   18
EXPORT_TASK_BAR_ID                  =   19
SW_UTILS_DATASTRUCT_TASK_BAR_ID     =   20
SW_UTILS_GEOCODE_TASK_BAR_ID        =   21
SW_UTILS_DFSUBSET_TASK_BAR_ID       =   22
SW_UTILS_CENSUS_TASK_BAR_ID         =   23
SCRIPT_TASK_BAR_ID                  =   24
WORKING_CELL_ID                     =   25


"""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# static html for loading the dfcleanser cells into a jupyter notebook 
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
"""

CLEANSING_CODE_CELL         =   'from dfcleanser.data_cleansing.data_cleansing_control import display_data_cleansing\\ndisplay_data_cleansing(0)'
CLEANSING_TITLE_CELL        =   '<div align="left" id="DCDataCleansing"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing1.jpg" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Cleansing : </h2><a name="DataCleansing"></a></div></div>'

EXPORT_CODE_CELL            =   'from dfcleanser.data_export.data_export_control import display_export_forms\\ndisplay_export_forms(0)'
EXPORT_TITLE_CELL           =   '<div align="left" id="DCDataExport"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataExport.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Data Export</h2><a name="DataExport"></a></div></div>'

IMPORT_CODE_CELL            =   'from dfcleanser.data_import.data_import_control import display_import_forms\\ndisplay_import_forms(0)'
IMPORT_TITLE_CELL           =   '<div align="left" id="DCDataImport"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataImport.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Import : </h2><a name="DataImport"></a></div></div>'

INSPECT_CODE_CELL           =   'from dfcleanser.data_inspection.data_inspection_control import display_data_inspection\\ndisplay_data_inspection(0)'
INSPECT_TITLE_CELL          =   '<div align="left" id="DCDataInspection"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataInspection.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Inspection : </h2><a name="DataInspection"></a></div></div>'

PANDAS_TITLE_CELL           =   '<div><table align="center"><tr><td><img src="https://rickkrasinski.github.io/dfcleanser/graphics/pandas.png" style="width: 120px ; height: 120px"></td><td style="margin-left: 200px"><p style="text-align: left" id="mainTitle"><font size="6">Pandas Dataframe Cleanser</font></p><p id="titleComment"><font size="3">A utility to prepare your pandas dataframe for data analytics.</font></p></td><td><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing.png" style="width: 120px ; height: 120px"></td></tr></table></div>'

SCRIPTING_CODE_CELL         =   'from dfcleanser.scripting.data_scripting_control import display_data_scripting\\ndisplay_data_scripting(0)'
SCRIPTING_TITLE_CELL        =   '<div align="left" id="DCDataScripting"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Script.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;Dataframe Cleanser Scripting</h3><a name="Script"></a></div></div>'

SW_UTILS_SECTION_TITLE_CELL =   '<div align="left" id="SWUtilities"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/SWUtilities.png" width="80" align="left" style="border: 0px ; margin-right: 6px ; margin-left: 0px"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Software Utilities</h2></div></div>'

SW_UTILS_DS_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_control import process_sw_utilities\\nprocess_sw_utilities(0)'
SW_UTILS_DS_TITLE_CELL      =   '<div align="left" id="DCSWDataStructUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/ListBuild.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Common Data Structures Utility</h3></div></div>'

SW_UTILS_DB_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_dfsubset_control import display_dfsubset_utility\\ndisplay_dfsubset_utility(0)'
SW_UTILS_DB_TITLE_CELL      =   '<div align="left" id="DCDFSubsetUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataframeSubset.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Dataframe Subset</h3></div></div>'

SW_UTILS_GC_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_geocode_control import display_geocode_utility\\ndisplay_geocode_utility(0)'
SW_UTILS_GC_TITLE_CELL      =   '<div align="left" id="DCGeocodeUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/GetLongLat.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Geocoding</h3></div></div>'

SW_UTILS_DM_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_census_control import display_census_utility\\ndisplay_census_utility(0)'
SW_UTILS_DM_TITLE_CELL      =   '<div align="left" id="DCCensusUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/census.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Census</h3></div></div>'

SYSTEM_CODE_CELL            =   "from dfcleanser.system.system_control import display_system_environment\\ndisplay_system_environment(0)"
SYSTEM_TITLE_CELL           =   '<div align="left" id="DCSystem"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/systemEnvironment.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;System Environment : </h2><a name="SystemEnvironment"></a></div></div>'

TRANSFORM_CODE_CELL         =   'from dfcleanser.data_transform.data_transform_control import display_data_transform\\ndisplay_data_transform(0)'
TRANSFORM_TITLE_CELL        =   '<div align="left" id="DCDataTransform"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataTransform.jpg" width="80" align="left" style="border: 0px ; margin-right: 6px ; margin-left: 0px"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Data Transform</h2><a name="DataTransform"></a></div></div>'

WORKING_CODE_CELL           =   '# working cell- please do not remove'
WORKING_TITLE_CELL          =   '<div align="left" id="Restricted"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Restricted.jpg" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Restricted</h2></div></div>'


"""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# cell metadata identifiers
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
"""

DC_PANDAS_TITLE                 =   "PandasdfcleanserTitle"

DC_SYSTEM_TITLE                 =   "DCSystemTitle"
DC_SYSTEM                       =   "DCSystem"

DC_DATA_IMPORT_TITLE            =   "DCDataImportTitle"
DC_DATA_IMPORT                  =   "DCDataImport"

DC_DATA_INSPECTION_TITLE        =   "DCDataInspectionTitle"
DC_DATA_INSPECTION              =   "DCDataInspection"

DC_DATA_CLEANSING_TITLE         =   "DCDataCleansingTitle"
DC_DATA_CLEANSING               =   "DCDataCleansing"

DC_DATA_TRANSFORM_TITLE         =   "DCDataTransformTitle"
DC_DATA_TRANSFORM               =   "DCDataTransform"

DC_DATA_EXPORT_TITLE            =   "DCDataExportTitle"
DC_DATA_EXPORT                  =   "DCDataExport"

DC_SW_UTILITIES                 =   "SWUtilities"

DC_LIST_UTILITY_TITLE           =   "DCListUtilityTitle"
DC_LIST_UTILITY                 =   "DCListUtility"

DC_GEOCODE_UTILITY_TITLE        =   "DCGeocodeUtilityTitle"
DC_GEOCODE_UTILITY              =   "DCGeocodeUtility"

DC_CENSUS_UTILITY_TITLE         =   "DCCensusUtilityTitle"
DC_CENSUS_UTILITY               =   "DCCensusUtility"

DC_DFSUBSET_UTILITY_TITLE       =   "DCDFSubsetUtilityTitle"
DC_DFSUBSET_UTILITY             =   "DCDFSubsetUtility"

DC_DATA_SCRIPTING_TITLE         =   "DCDataScriptingTitle"
DC_DATA_SCRIPTING               =   "DCDataScripting"

DC_WORKING_TITLE                =   "DCWorkingTitle"
DC_WORKING                      =   "DCWorking"


DC_BLANK_LINE                   =   "DCBlankline"
DC_BLANK_LINE_TEXT              =   "<br></br>"

MARKDOWN    =   0
CODE        =   1

def get_chapter_code_cell_id(chapter) :

    if (DC_SYSTEM_TITLE == chapter)                     :   return(SYSTEM_TASK_BAR_ID)
    elif (DC_DATA_IMPORT_TITLE == chapter)              :   return(IMPORT_TASK_BAR_ID)
    elif (DC_DATA_INSPECTION_TITLE == chapter)          :   return(INSPECTION_TASK_BAR_ID)
    elif (DC_DATA_CLEANSING_TITLE == chapter)           :   return(CLEANSING_TASK_BAR_ID)
    elif (DC_DATA_TRANSFORM_TITLE == chapter)           :   return(TRANSFORM_TASK_BAR_ID)
    elif (DC_DATA_EXPORT_TITLE == chapter)              :   return(EXPORT_TASK_BAR_ID)
    elif (DC_LIST_UTILITY_TITLE == chapter)             :   return(SW_UTILS_DATASTRUCT_TASK_BAR_ID)
    elif (DC_GEOCODE_UTILITY_TITLE == chapter)          :   return(SW_UTILS_GEOCODE_TASK_BAR_ID)
    elif (DC_DFSUBSET_UTILITY_TITLE == chapter)         :   return(SW_UTILS_DFSUBSET_TASK_BAR_ID)
    elif (DC_CENSUS_UTILITY_TITLE == chapter)           :   return(SW_UTILS_CENSUS_TASK_BAR_ID)
    elif (DC_DATA_SCRIPTING_TITLE == chapter)           :   return(SCRIPT_TASK_BAR_ID)
    elif (DC_WORKING_TITLE == chapter)                  :   return(WORKING_CELL_ID)

    return(None)

def get_cells_title_index(cellTitle) :

    if (DC_PANDAS_TITLE == cellTitle)                     :   return(DC_TITLE_ID)
    elif (DC_SYSTEM_TITLE == cellTitle)                   :   return(DC_SYSTEM_ID)
    elif (DC_SYSTEM == cellTitle)                         :   return(SYSTEM_TASK_BAR_ID)
    elif (DC_DATA_IMPORT_TITLE == cellTitle)              :   return(DC_DATA_IMPORT_ID)
    elif (DC_DATA_IMPORT == cellTitle)                    :   return(IMPORT_TASK_BAR_ID)
    elif (DC_DATA_INSPECTION_TITLE == cellTitle)          :   return(DC_DATA_INSPECTION_ID)
    elif (DC_DATA_INSPECTION == cellTitle)                :   return(INSPECTION_TASK_BAR_ID)
    elif (DC_DATA_CLEANSING_TITLE == cellTitle)           :   return(DC_DATA_CLEANSING_ID)
    elif (DC_DATA_CLEANSING == cellTitle)                 :   return(CLEANSING_TASK_BAR_ID)
    elif (DC_DATA_TRANSFORM_TITLE == cellTitle)           :   return(DC_DATA_TRANSFORM_ID)
    elif (DC_DATA_TRANSFORM == cellTitle)                 :   return(TRANSFORM_TASK_BAR_ID)
    elif (DC_DATA_EXPORT_TITLE == cellTitle)              :   return(DC_DATA_EXPORT_ID)
    elif (DC_DATA_EXPORT == cellTitle)                    :   return(EXPORT_TASK_BAR_ID)
    elif (DC_SW_UTILITIES == cellTitle)                   :   return(DC_SW_UTILITIES_ID)
    elif (DC_LIST_UTILITY_TITLE == cellTitle)             :   return(DC_DATASTRUCT_UTILITY_ID)
    elif (DC_LIST_UTILITY == cellTitle)                   :   return(SW_UTILS_DATASTRUCT_TASK_BAR_ID)
    elif (DC_GEOCODE_UTILITY_TITLE == cellTitle)          :   return(DC_GEOCODE_UTILITY_ID)
    elif (DC_GEOCODE_UTILITY == cellTitle)                :   return(SW_UTILS_GEOCODE_TASK_BAR_ID)
    elif (DC_DFSUBSET_UTILITY_TITLE == cellTitle)         :   return(DC_DFSUBSET_UTILITY_ID)
    elif (DC_DFSUBSET_UTILITY == cellTitle)               :   return(SW_UTILS_DFSUBSET_TASK_BAR_ID)
    elif (DC_CENSUS_UTILITY_TITLE == cellTitle)           :   return(DC_CENSUS_UTILITY_ID)
    elif (DC_CENSUS_UTILITY == cellTitle)                 :   return(SW_UTILS_CENSUS_TASK_BAR_ID)
    elif (DC_DATA_SCRIPTING_TITLE == cellTitle)           :   return(DC_DATA_SCRIPT_ID)
    elif (DC_DATA_SCRIPTING == cellTitle)                 :   return(SCRIPT_TASK_BAR_ID)
    elif (DC_WORKING_TITLE == cellTitle)                  :   return(DC_WORKING_ID)
    elif (DC_WORKING == cellTitle)                        :   return(WORKING_CELL_ID)

    return(None)
    

def get_dfc_cells_text(cellid) :
    
    if(cellid == DC_TITLE_ID)                           :    return(PANDAS_TITLE_CELL) 
    
    elif(cellid == DC_SYSTEM_ID)                        :    return(SYSTEM_TITLE_CELL)
    elif(cellid == SYSTEM_TASK_BAR_ID)                  :    return(SYSTEM_CODE_CELL)

    elif(cellid == DC_DATA_IMPORT_ID)                   :    return(IMPORT_TITLE_CELL)
    elif(cellid == IMPORT_TASK_BAR_ID)                  :    return(IMPORT_CODE_CELL)
    
    elif(cellid == DC_DATA_INSPECTION_ID)               :    return(INSPECT_TITLE_CELL)
    elif(cellid == INSPECTION_TASK_BAR_ID)              :    return(INSPECT_CODE_CELL)

    elif(cellid == DC_DATA_CLEANSING_ID)                :    return(CLEANSING_TITLE_CELL)
    elif(cellid == CLEANSING_TASK_BAR_ID)               :    return(CLEANSING_CODE_CELL)

    elif(cellid == DC_DATA_TRANSFORM_ID)                :    return(TRANSFORM_TITLE_CELL)
    elif(cellid == TRANSFORM_TASK_BAR_ID)               :    return(TRANSFORM_CODE_CELL)

    elif(cellid == DC_DATA_EXPORT_ID)                   :    return(EXPORT_TITLE_CELL)
    elif(cellid == EXPORT_TASK_BAR_ID)                  :    return(EXPORT_CODE_CELL)

    elif(cellid == DC_SW_UTILITIES_ID)                  :    return(SW_UTILS_SECTION_TITLE_CELL)

    elif(cellid == DC_DATASTRUCT_UTILITY_ID)            :    return(SW_UTILS_DS_TITLE_CELL)
    elif(cellid == SW_UTILS_DATASTRUCT_TASK_BAR_ID)     :    return(SW_UTILS_DS_CODE_CELL)

    elif(cellid == DC_GEOCODE_UTILITY_ID)               :    return(SW_UTILS_GC_TITLE_CELL)
    elif(cellid == SW_UTILS_GEOCODE_TASK_BAR_ID)        :    return(SW_UTILS_GC_CODE_CELL)

    elif(cellid == DC_DFSUBSET_UTILITY_ID)              :    return(SW_UTILS_DB_TITLE_CELL)
    elif(cellid == SW_UTILS_DFSUBSET_TASK_BAR_ID)       :    return(SW_UTILS_DB_CODE_CELL)
    
    elif(cellid == DC_CENSUS_UTILITY_ID)                :    return(SW_UTILS_DM_TITLE_CELL)
    elif(cellid == SW_UTILS_CENSUS_TASK_BAR_ID)         :    return(SW_UTILS_DM_CODE_CELL)
    
    elif(cellid == DC_DATA_SCRIPT_ID)                   :    return(SCRIPTING_TITLE_CELL)
    elif(cellid == SCRIPT_TASK_BAR_ID)                  :    return(SCRIPTING_CODE_CELL)

    elif(cellid == DC_WORKING_ID)                       :    return(WORKING_TITLE_CELL)
    elif(cellid == WORKING_CELL_ID)                     :    return(WORKING_CODE_CELL)

    elif(cellid == DC_BLANK_LINE)                       :    return(DC_BLANK_LINE_TEXT)

    return(DC_BLANK_LINE_TEXT)

    

