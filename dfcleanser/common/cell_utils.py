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

import dfcleanser.common.help_utils as dfchelp

"""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# static html for loading the dfcleanser cells into a jupyter notebook 
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
"""

CLEANSING_CODE_CELL         =   'from dfcleanser.data_cleansing.data_cleansing_control import display_data_cleansing\\ndisplay_data_cleansing(0)'
CLEANSING_HELP_CELL         =   '<div align="left" id="CleansingHelp"/><p class="DCTitleChapterstext"></p></div>'
CLEANSING_TITLE_CELL        =   '<div align="left" id="DCDataCleansing"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing1.jpg" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Cleansing : </h2><a name="DataCleansing"></a></div></div>'

EXPORT_CODE_CELL            =   'from dfcleanser.data_export.data_export_control import display_export_forms\\ndisplay_export_forms(0)'
EXPORT_HELP_CELL            =   '<div align="left" id="ExportHelp"/><p class="DCTitleChapterstext"></p></div>'
EXPORT_TITLE_CELL           =   '<div align="left" id="DCDataExport"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataExport.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Data Export</h2><a name="DataExport"></a></div></div>'

IMPORT_CODE_CELL            =   'from dfcleanser.data_import.data_import_control import display_import_forms\\ndisplay_import_forms(0)'
IMPORT_HELP_CELL            =   '<div align="left" id="ImportHelp"/><p class="DCTitleChapterstext"></p></div>'
IMPORT_TITLE_CELL           =   '<div align="left" id="DCDataImport"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataImport.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Import : </h2><a name="DataImport"></a></div></div>'

INSPECT_CODE_CELL           =   'from dfcleanser.data_inspection.data_inspection_control import display_data_inspection\\ndisplay_data_inspection(0)'
INSPECT_HELP_CELL           =   '<div align="left" id="InspectionHelp"/><p class="DCTitleChapterstext"></p></div>'
INSPECT_TITLE_CELL          =   '<div align="left" id="DCDataInspection"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataInspection.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;Data Inspection : </h2><a name="DataInspection"></a></div></div>'

PANDAS_TITLE_CELL           =   '<div><table align="center"><tr><td><img src="https://rickkrasinski.github.io/dfcleanser/graphics/pandas.png" style="width: 120px; height: 120px;"></td><td style="margin-left: 200px;"><p style="text-align: left;" id="mainTitle"><font size="6">Pandas Dataframe Cleanser</font></p><p id="titleComment"><font size="3">A utility to prepare your pandas dataframe for data analytics.</font></p></td><td><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing.png" style="width: 120px; height: 120px;"></td></tr></table></div>'

SCRIPT_SECTION_TITLE_CELL   =   '<div align="left" id="ScriptingMode"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/ScriptMode.jpg" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2 class="DCTitleChaptersh2">&nbsp;&nbsp;&nbsp;Scripting Mode</h2><a name="Script"></a></div></div></div><br>'

SCRIPTING_CODE_CELL         =   'from dfcleanser.scripting.data_scripting_control import display_data_scripting\\ndisplay_data_scripting(0)'
SCRIPTING_HELP_CELL         =   '<div align="left" id="ScriptingHelp"/><p class="DCTitleChapterstext"></p></div>'
SCRIPTING_TITLE_CELL        =   '<div align="left" id="DCDataScripting"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Script.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;Dataframe Cleanser Scripting</h3><a name="Script"></a></div></div>'

SW_UTILS_SECTION_TITLE_CELL =   '<div align="left" id="SWUtilities"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/SWUtilities.png" width="80" align="left" style="border: 0px; margin-right: 6px; margin-left: 0px"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Software Utilities</h2></div></div>'

SW_UTILS_DS_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_control import process_sw_utilities\\nprocess_sw_utilities(0)'
SW_UTILS_DS_HELP_CELL       =   '<div align="left" id="DCListUtilityHelp"/><p class="DCTitleChapterstext"></p></div>'
SW_UTILS_DS_TITLE_CELL      =   '<div align="left" id="DCSWDataStructUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/ListBuild.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Common Data Structures Utility</h3></div></div>'

SW_UTILS_DC_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_dfconcat_control import display_dfconcat_utility\\ndisplay_dfconcat_utility(0)'
SW_UTILS_DC_HELP_CELL       =   '<div align="left" id="DCDFConcatUtilityHelp"/><p class="DCTitleChapterstext"></p></div>'
SW_UTILS_DC_TITLE_CELL      =   '<div align="left" id="DCDFConcatUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataframeConcat.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Dataframe Concatenation</h3></div></div>'

SW_UTILS_DB_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_dfsubset_control import display_dfsubset_utility\\ndisplay_dfsubset_utility(0)'
SW_UTILS_DB_HELP_CELL       =   '<div align="left" id="DCDFSubsetUtilityHelp"/><p class="DCTitleChapterstext"></p></div>'
SW_UTILS_DB_TITLE_CELL      =   '<div align="left" id="DCDFSubsetUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataframeSubset.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Dataframe Subset</h3></div></div>'

SW_UTILS_GF_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_genfunc_control import display_gen_function\\ndisplay_gen_function(0)'
SW_UTILS_GF_HELP_CELL       =   '<div align="left" id="DCGenFunctionUtilityHelp"><p class="DCTitleChapterstext"></p></div>'
SW_UTILS_GF_TITLE_CELL      =   '<div align="left" id="DCGenFunctionUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Genfunction.jpg" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Generic Functions</h3></div></div>'

SW_UTILS_GC_CODE_CELL       =   'from dfcleanser.sw_utilities.sw_utility_geocode_control import display_geocode_utility\\ndisplay_geocode_utility(0)'
SW_UTILS_GC_HELP_CELL       =   '<div align="left" id="DCGeocodeUtilityHelp"/><p class="DCTitleChapterstext"></p></div>'
SW_UTILS_GC_TITLE_CELL      =   '<div align="left" id="DCGeocodeUtility"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/GetLongLat.png" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h3>&nbsp;&nbsp;&nbsp;Geocoding</h3></div></div>'

SYSTEM_CODE_CELL            =   "from dfcleanser.system.system_control import display_system_environment\\ndisplay_system_environment(0)"
SYSTEM__ABBR_CODE_CELL      =   'from dfcleanser.system.system_control import display_system_environment\ndisplay_system_environment(16)'
SYSTEM_HELP_CELL            =   '<div align="left" id="SystemHelp"/><p class="DCTitleChapterstext"></p></div>'
SYSTEM_TITLE_CELL           =   '<div align="left" id="DCSystem"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/systemEnvironment.png" width="80" align="left"/></div><div><image width="10"></div><div><h2>&nbsp;&nbsp;&nbsp;System Environment : </h2><a name="SystemEnvironment"></a></div></div>'

TRANSFORM_CODE_CELL         =   'from dfcleanser.data_transform.data_transform_control import display_data_transform\\ndisplay_data_transform(0)'
TRANSFORM_HELP_CELL         =   '<div align="left" id="TransformHelp"/><p class="DCTitleChapterstext"></p></div>'
TRANSFORM_TITLE_CELL        =   '<div align="left" id="DCDataTransform"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/dataTransform.jpg" width="80" align="left" style="border: 0px; margin-right: 6px; margin-left: 0px"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Data Transform</h2><a name="DataTransform"></a></div></div>'

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
DC_DATA_CUSTOM_IMPORT           =   "DCDataImportCustom"

DC_DATA_INSPECTION_TITLE        =   "DCDataInspectionTitle"
DC_DATA_INSPECTION              =   "DCDataInspection"

DC_DATA_CLEANSING_TITLE         =   "DCDataCleansingTitle"
DC_DATA_CLEANSING               =   "DCDataCleansing"

DC_DATA_TRANSFORM_TITLE         =   "DCDataTransformTitle"
DC_DATA_TRANSFORM               =   "DCDataTransform"
DC_DATA_TRANSFORM_ADD_COL       =   "DCDataTransformAddCol"

DC_DATA_EXPORT_TITLE            =   "DCDataExportTitle"
DC_DATA_EXPORT                  =   "DCDataExport"
DC_DATA_CUSTOM_EXPORT           =   "DCDataExportCustom"

DC_SW_UTILITIES                 =   "SWUtilities"

DC_LIST_UTILITY_TITLE           =   "DCListUtilityTitle"
DC_LIST_UTILITY                 =   "DCListUtility"

DC_GEN_FUNCTION_UTILITY_TITLE   =   "DCGenFunctionUtilityTitle"
DC_GEN_FUNCTION_UTILITY         =   "DCGenFunctionUtility"
DC_GEN_FUNCTION__CODE_CELL      =   "DCGenFunctionCodeCell"

DC_GEOCODE_UTILITY_TITLE        =   "DCGeocodeUtilityTitle"
DC_GEOCODE_UTILITY              =   "DCGeocodeUtility"

DC_DFSUBSET_UTILITY_TITLE       =   "DCDFSubsetUtilityTitle"
DC_DFSUBSET_UTILITY             =   "DCDFSubsetUtility"

DC_DFCONCAT_UTILITY_TITLE       =   "DCDFConcatUtilityTitle"
DC_DFCONCAT_UTILITY             =   "DCDFConcatUtility"

DC_SCRIPTING                    =   "ScriptingMode"
DC_DATA_SCRIPTING_TITLE         =   "DCDataScriptingTitle"
DC_DATA_SCRIPTING               =   "DCDataScripting"

DC_WORKING_TITLE                =   "DCWorkingTitle"
DC_WORKING                      =   "DCWorking"


DC_BLANK_LINE                   =   "DCBlankline"
DC_BLANK_LINE_TEXT              =   "<br></br>"

MARKDOWN    =   0
CODE        =   1


def get_cells_title_index(cellTitle) :

    if (DC_PANDAS_TITLE == cellTitle)                     :   return(0)
    elif (DC_SYSTEM_TITLE == cellTitle)                   :   return(1)
    elif (DC_SYSTEM == cellTitle)                         :   return(2)
    elif (DC_DATA_IMPORT_TITLE == cellTitle)              :   return(3)
    elif (DC_DATA_IMPORT == cellTitle)                    :   return(4)
    elif (DC_DATA_CUSTOM_IMPORT == cellTitle)             :   return(5)
    elif (DC_DATA_INSPECTION_TITLE == cellTitle)          :   return(6)
    elif (DC_DATA_INSPECTION == cellTitle)                :   return(7)
    elif (DC_DATA_CLEANSING_TITLE == cellTitle)           :   return(8)
    elif (DC_DATA_CLEANSING == cellTitle)                 :   return(9)
    elif (DC_DATA_TRANSFORM_TITLE == cellTitle)           :   return(10)
    elif (DC_DATA_TRANSFORM == cellTitle)                 :   return(11)
    elif (DC_DATA_TRANSFORM_ADD_COL == cellTitle)         :   return(12)
    elif (DC_DATA_EXPORT_TITLE == cellTitle)              :   return(13)
    elif (DC_DATA_EXPORT == cellTitle)                    :   return(14)
    elif (DC_DATA_CUSTOM_EXPORT == cellTitle)             :   return(15)
    elif (DC_SW_UTILITIES == cellTitle)                   :   return(16)
    elif (DC_LIST_UTILITY_TITLE == cellTitle)             :   return(17)
    elif (DC_LIST_UTILITY == cellTitle)                   :   return(18)
    elif (DC_GEN_FUNCTION_UTILITY_TITLE == cellTitle)     :   return(19)
    elif (DC_GEN_FUNCTION_UTILITY == cellTitle)           :   return(20)
    elif (DC_GEN_FUNCTION__CODE_CELL == cellTitle)        :   return(21)
    elif (DC_GEOCODE_UTILITY_TITLE == cellTitle)          :   return(22)
    elif (DC_GEOCODE_UTILITY == cellTitle)                :   return(23)
    elif (DC_DFSUBSET_UTILITY_TITLE == cellTitle)         :   return(24)
    elif (DC_DFSUBSET_UTILITY == cellTitle)               :   return(25)
    elif (DC_DFCONCAT_UTILITY_TITLE == cellTitle)         :   return(26)
    elif (DC_DFCONCAT_UTILITY == cellTitle)               :   return(27)
    elif (DC_SCRIPTING == cellTitle)                      :   return(28)
    elif (DC_DATA_SCRIPTING_TITLE == cellTitle)           :   return(29)
    elif (DC_DATA_SCRIPTING == cellTitle)                 :   return(30)
    elif (DC_WORKING_TITLE == cellTitle)                  :   return(31)
    elif (DC_WORKING == cellTitle)                        :   return(32)

    return(None)
    

def get_dfc_cells_text(cellid) :
    
    if(cellid == DC_PANDAS_TITLE)                           :    return(PANDAS_TITLE_CELL) 
    
    elif(cellid == DC_SYSTEM_TITLE)                         :    return(SYSTEM_TITLE_CELL)
    elif(cellid == DC_SYSTEM)                               :    return(SYSTEM_CODE_CELL)
    elif(cellid == dfchelp.SYS_ENVIRONMENT_HELP_ID)         :    return(SYSTEM_HELP_CELL)

    elif(cellid == DC_DATA_IMPORT_TITLE)                    :    return(IMPORT_TITLE_CELL)
    elif(cellid == DC_DATA_IMPORT)                          :    return(IMPORT_CODE_CELL)
    elif(cellid == dfchelp.IMPORT_HELP_ID)                  :    return(IMPORT_HELP_CELL)
    
    elif(cellid == DC_DATA_INSPECTION_TITLE)                :    return(INSPECT_TITLE_CELL)
    elif(cellid == DC_DATA_INSPECTION)                      :    return(INSPECT_CODE_CELL)
    elif(cellid == dfchelp.INSPECT_HELP_ID)                 :    return(INSPECT_HELP_CELL)

    elif(cellid == DC_DATA_CLEANSING_TITLE)                 :    return(CLEANSING_TITLE_CELL)
    elif(cellid == DC_DATA_CLEANSING)                       :    return(CLEANSING_CODE_CELL)
    elif(cellid == dfchelp.CLEANSE_HELP_ID)                 :    return(CLEANSING_HELP_CELL)

    elif(cellid == DC_DATA_TRANSFORM_TITLE)                 :    return(TRANSFORM_TITLE_CELL)
    elif(cellid == DC_DATA_TRANSFORM)                       :    return(TRANSFORM_CODE_CELL)
    elif(cellid == dfchelp.TRANSFORM_HELP_ID)               :    return(TRANSFORM_HELP_CELL)

    elif(cellid == DC_DATA_EXPORT_TITLE)                    :    return(EXPORT_TITLE_CELL)
    elif(cellid == DC_DATA_EXPORT)                          :    return(EXPORT_CODE_CELL)
    elif(cellid == dfchelp.EXPORT_HELP_ID)                  :    return(EXPORT_HELP_CELL)

    elif(cellid == DC_SW_UTILITIES)                         :    return(SW_UTILS_SECTION_TITLE_CELL)

    elif(cellid == DC_LIST_UTILITY_TITLE)                   :    return(SW_UTILS_DS_TITLE_CELL)
    elif(cellid == DC_LIST_UTILITY)                         :    return(SW_UTILS_DS_CODE_CELL)
    elif(cellid == dfchelp.LIST_UTILITY_HELP_ID)            :    return(SW_UTILS_DS_HELP_CELL)

    elif(cellid == DC_GEN_FUNCTION_UTILITY_TITLE)           :    return(SW_UTILS_GF_TITLE_CELL)
    elif(cellid == DC_GEN_FUNCTION_UTILITY)                 :    return(SW_UTILS_GF_CODE_CELL)
    elif(cellid == dfchelp.GEN_FUNCTION_UTILITY_HELP_ID)    :    return(SW_UTILS_GF_HELP_CELL)

    elif(cellid == DC_GEOCODE_UTILITY_TITLE)                :    return(SW_UTILS_GC_TITLE_CELL)
    elif(cellid == DC_GEOCODE_UTILITY)                      :    return(SW_UTILS_GC_CODE_CELL)
    elif(cellid == dfchelp.GEOCODING_HELP_ID)               :    return(SW_UTILS_GC_HELP_CELL)

    elif(cellid == DC_DFSUBSET_UTILITY_TITLE)               :    return(SW_UTILS_DB_TITLE_CELL)
    elif(cellid == DC_DFSUBSET_UTILITY)                     :    return(SW_UTILS_DB_CODE_CELL)
    elif(cellid == dfchelp.DFSUBSET_HELP_ID)                :    return(SW_UTILS_DB_HELP_CELL)
    
    elif(cellid == DC_DFCONCAT_UTILITY_TITLE)               :    return(SW_UTILS_DC_TITLE_CELL)
    elif(cellid == DC_DFCONCAT_UTILITY)                     :    return(SW_UTILS_DC_CODE_CELL)
    elif(cellid == dfchelp.DFCONCAT_HELP_ID)                :    return(SW_UTILS_DC_HELP_CELL)
        
    elif(cellid == DC_SCRIPTING)                            :    return(SCRIPT_SECTION_TITLE_CELL)

    elif(cellid == DC_DATA_SCRIPTING_TITLE)                 :    return(SCRIPTING_TITLE_CELL)
    elif(cellid == DC_DATA_SCRIPTING)                       :    return(SCRIPTING_CODE_CELL)
    elif(cellid == dfchelp.SCRIPTING_HELP_ID)               :    return(SCRIPTING_HELP_CELL)

    elif(cellid == DC_WORKING_TITLE)                        :    return(WORKING_TITLE_CELL)
    elif(cellid == DC_WORKING)                              :    return(WORKING_CODE_CELL)

    elif(cellid == DC_BLANK_LINE)                           :    return(DC_BLANK_LINE_TEXT)

    return(DC_BLANK_LINE_TEXT)
    


