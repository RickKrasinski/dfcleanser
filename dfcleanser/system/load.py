"""
# load 
"""
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 25 10:29:48 2018

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp

"""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# components for loading the dfcleanser cells into a jupyter notebook 
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
"""

"""
# cell metadata identifiers
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
    
DC_BLANK_LINE           =   "DCBlankline"
DC_BLANK_LINE_TEXT      =   "<br></br>"

MARKDOWN    =   0
CODE        =   1

def get_dfc_cells_text(cellid) :
    
    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()
    
    cell_text   =   ""
    file_name   =   ""
    
    if(cellid == DC_PANDAS_TITLE)                           :    file_name  =  "PandasdfcleanserTitle" 
    
    elif(cellid == DC_SYSTEM_TITLE)                         :    file_name  =  "SystemTitle"
    elif(cellid == DC_SYSTEM)                               :    file_name  =  "SystemCodeCell"

    elif(cellid == dfchelp.SYS_ENVIRONMENT_HELP_ID)         :    file_name  =  "SystemHelp"

    elif(cellid == DC_DATA_IMPORT_TITLE)                    :    file_name  =  "ImportTitle"
    elif(cellid == DC_DATA_IMPORT)                          :    file_name  =  "ImportCodeCell"
    elif(cellid == dfchelp.IMPORT_HELP_ID)                  :    file_name  =  "ImportHelp"
    
    elif(cellid == DC_DATA_INSPECTION_TITLE)                :    file_name  =  "InspectionTitle"
    elif(cellid == DC_DATA_INSPECTION)                      :    file_name  =  "InspectionCodeCell"
    elif(cellid == dfchelp.INSPECT_HELP_ID)                 :    file_name  =  "InspectionHelp"

    elif(cellid == DC_DATA_CLEANSING_TITLE)                 :    file_name  =  "CleansingTitle"
    elif(cellid == DC_DATA_CLEANSING)                       :    file_name  =  "CleansingCodeCell"
    elif(cellid == dfchelp.CLEANSE_HELP_ID)                 :    file_name  =  "CleansingHelp"

    elif(cellid == DC_DATA_TRANSFORM_TITLE)                 :    file_name  =  "TransformTitle"
    elif(cellid == DC_DATA_TRANSFORM)                       :    file_name  =  "TransformCodeCell"
    elif(cellid == dfchelp.TRANSFORM_HELP_ID)               :    file_name  =  "TransformHelp"

    elif(cellid == DC_DATA_EXPORT_TITLE)                    :    file_name  =  "ExportTitle"
    elif(cellid == DC_DATA_EXPORT)                          :    file_name  =  "ExportCodeCell"
    elif(cellid == dfchelp.EXPORT_HELP_ID)                  :    file_name  =  "ExportHelp"

    elif(cellid == DC_SW_UTILITIES)                         :    file_name  =  "SWUtilitiesSectionTitle"

    elif(cellid == DC_LIST_UTILITY_TITLE)                   :    file_name  =  "SWUtilitiesDataStructureTitle"
    elif(cellid == DC_LIST_UTILITY)                         :    file_name  =  "SWUtilitiesDataStructureCodeCell"
    elif(cellid == dfchelp.LIST_UTILITY_HELP_ID)            :    file_name  =  "SWUtilitiesDataStructureHelp"

    elif(cellid == DC_GEN_FUNCTION_UTILITY_TITLE)           :    file_name  =  "SWUtilitiesGenericFunctionTitle"
    elif(cellid == DC_GEN_FUNCTION_UTILITY)                 :    file_name  =  "SWUtilitiesGenericFunctionCodeCell"
    elif(cellid == dfchelp.GEN_FUNCTION_UTILITY_HELP_ID)    :    file_name  =  "SWUtilitiesGenericFunctionHelp"

    elif(cellid == DC_GEOCODE_UTILITY_TITLE)                :    file_name  =  "SWUtilitiesGeocodingTitle"
    elif(cellid == DC_GEOCODE_UTILITY)                      :    file_name  =  "SWUtilitiesGeocodingCodeCell"
    elif(cellid == dfchelp.GEOCODING_HELP_ID)               :    file_name  =  "SWUtilitiesGeocodingHelp"

    elif(cellid == DC_DFSUBSET_UTILITY_TITLE)               :    file_name  =  "SWUtilitiesDFSubsetTitle"
    elif(cellid == DC_DFSUBSET_UTILITY)                     :    file_name  =  "SWUtilitiesDFSubsetCodeCell"
    elif(cellid == dfchelp.DFSUBSET_HELP_ID)                :    file_name  =  "SWUtilitiesDFSubsetHelp"
    
    elif(cellid == DC_DFCONCAT_UTILITY_TITLE)               :    file_name  =  "SWUtilitiesDFConcatTitle"
    elif(cellid == DC_DFCONCAT_UTILITY)                     :    file_name  =  "SWUtilitiesDFConcatCodeCell"
    elif(cellid == dfchelp.DFCONCAT_HELP_ID)                :    file_name  =  "SWUtilitiesDFConcatHelp"
        
    elif(cellid == DC_SCRIPTING)                            :    file_name  =  "ScriptingSectionTitle"

    elif(cellid == DC_DATA_SCRIPTING_TITLE)                 :    file_name  =  "ScriptingTitle"
    elif(cellid == DC_DATA_SCRIPTING)                       :    file_name  =  "ScriptingCodeCell"
    elif(cellid == dfchelp.SCRIPTING_HELP_ID)               :    file_name  =  "ScriptingHelp"

    elif(cellid == DC_WORKING_TITLE)                        :    file_name  =  "WorkingTitle"
    elif(cellid == DC_WORKING)                              :    file_name  =  "WorkingCodeCell"

    if(cellid == DC_BLANK_LINE) :
        cell_text   =  DC_BLANK_LINE_TEXT
    else :
        from dfcleanser.common.common_utils import get_dfc_cell_file
        cell_text = get_dfc_cell_file(file_name,opstat)        
    
    return(cell_text)


def add_dfc_cell(ctype,cellid,celltext=None,afterid=-1) :
    
    if(celltext == None) :
        celltext = get_dfc_cells_text(cellid)
        
    from dfcleanser.common.common_utils import run_jscript    
    jscript     =   ("add_dfc_cell(" + str(ctype) + ",'" + celltext + "','" + cellid + "','" + str(afterid) + "')")
    run_jscript(jscript,"Error Loading dfc Cell",cellid) 

"""
# -------------------------------------------------------------
# Install the dfcleanser nmotebook cells 
# -------------------------------------------------------------
"""            
def load_dfcleanser() :

    showutilities   =   True
    
    corecbs     =   cfg.get_config_value(cfg.CORE_CBS_KEY)
    utilcbs     =   cfg.get_config_value(cfg.UTILITIES_CBS_KEY)
    scriptcbs   =   cfg.get_config_value(cfg.SCRIPTING_CBS_KEY)
    
    if(corecbs == None) :
        corecbs     =   [1,1,1,1,1]
    if(utilcbs == None) :
        showutilities     =   False
    if(scriptcbs == None) :
        scriptcbs   =   [0]
    
    from dfcleanser.common.common_utils import run_jscript
    celltext    =  "load_dfcleanser" 
    jscript     =   ("select_cell_from_text(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell","setup_dfcleanser") 
    
    # insert main title 
    add_dfc_cell(MARKDOWN,DC_PANDAS_TITLE)
    add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    # insert system cells 
    add_dfc_cell(MARKDOWN,DC_SYSTEM_TITLE)
    add_dfc_cell(MARKDOWN,dfchelp.SYS_ENVIRONMENT_HELP_ID)
    add_dfc_cell(CODE,DC_SYSTEM)
    add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

    # insert import cells
    if(corecbs[0]) :
        add_dfc_cell(MARKDOWN,DC_DATA_IMPORT_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.IMPORT_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_IMPORT)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

    # insert inspection cells
    if(corecbs[1]) :
        add_dfc_cell(MARKDOWN,DC_DATA_INSPECTION_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.INSPECT_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_INSPECTION)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

    # insert cleansing cells
    if(corecbs[2]) :
        add_dfc_cell(MARKDOWN,DC_DATA_CLEANSING_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.CLEANSE_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_CLEANSING)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    # insert transform cells
    if(corecbs[3]) :
        add_dfc_cell(MARKDOWN,DC_DATA_TRANSFORM_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.TRANSFORM_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_TRANSFORM)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    # insert export cells 
    if(corecbs[4]) :
        add_dfc_cell(MARKDOWN,DC_DATA_EXPORT_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.EXPORT_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_EXPORT)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    if(showutilities) :
        
        # insert sw utilities title 
        add_dfc_cell(MARKDOWN,DC_SW_UTILITIES)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

        # insert list utility cells 
        if(utilcbs[0]) :
            add_dfc_cell(MARKDOWN,DC_LIST_UTILITY_TITLE)
            add_dfc_cell(MARKDOWN,dfchelp.LIST_UTILITY_HELP_ID)
            add_dfc_cell(CODE,DC_LIST_UTILITY)
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
        
        # insert gen function cells 
        if(utilcbs[1]) :
            add_dfc_cell(MARKDOWN,DC_GEN_FUNCTION_UTILITY_TITLE)
            add_dfc_cell(MARKDOWN,dfchelp.GEN_FUNCTION_UTILITY_HELP_ID)
            add_dfc_cell(CODE,DC_GEN_FUNCTION_UTILITY)
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
        
        # insert geocoding utility cells 
        if(utilcbs[2]) :
            add_dfc_cell(MARKDOWN,DC_GEOCODE_UTILITY_TITLE)
            add_dfc_cell(MARKDOWN,dfchelp.GEOCODING_HELP_ID)
            add_dfc_cell(CODE,DC_GEOCODE_UTILITY)
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[3]) :
            add_dfc_cell(MARKDOWN,DC_DFSUBSET_UTILITY_TITLE)
            add_dfc_cell(MARKDOWN,dfchelp.DFSUBSET_HELP_ID)
            add_dfc_cell(CODE,DC_DFSUBSET_UTILITY)
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[4]) :
            add_dfc_cell(MARKDOWN,DC_DFCONCAT_UTILITY_TITLE)
            add_dfc_cell(MARKDOWN,dfchelp.DFCONCAT_HELP_ID)
            add_dfc_cell(CODE,DC_DFCONCAT_UTILITY)
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
        
    if(scriptcbs[0]) :
        
        # insert scripting title 
        add_dfc_cell(MARKDOWN,DC_SCRIPTING)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

        # insert scripting cells 
        add_dfc_cell(MARKDOWN,DC_DATA_SCRIPTING_TITLE)
        add_dfc_cell(MARKDOWN,dfchelp.SCRIPTING_HELP_ID)
        add_dfc_cell(CODE,DC_DATA_SCRIPTING)
        add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

    # insert working cell 
    add_dfc_cell(MARKDOWN,DC_WORKING_TITLE)
    add_dfc_cell(CODE,DC_WORKING)
    add_dfc_cell(MARKDOWN,DC_BLANK_LINE)

    cfg.set_config_value(cfg.DFC_CURRENTLY_LOADED_KEY,True)
    cfg.get_loaded_cells()  
    
"""
# -------------------------------------------------------------
# unload the dfcleanser nmotebook cells 
# -------------------------------------------------------------
"""            
def unload_dfcleanser() :

    from dfcleanser.common.common_utils import run_jscript    
    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser","Error UnLoading dfcleanser")
    
    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser","Error UnLoading dfcleanser")

    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser","Error UnLoading dfcleanser")
    
    cfg.drop_config_value(cfg.DFC_CURRENTLY_LOADED_KEY)
    cfg.drop_config_value(cfg.DFC_CHAPTERS_LOADED_KEY)
    


DO_NOT_LOAD_CHAPTER             =   0
LOAD_CHAPTER                    =   1

CHAPTER_NOT_LOADED              =   0
CHAPTER_LOADED                  =   1

DF_UTILS_DATA_STRUCTURE         =   0
DF_UTILS_GEN_FUNCTION           =   1
DF_UTILS_GEOCODING              =   2
DF_UTILS_SUBSET                 =   3
DF_UTILS_CONCAT                 =   4

DF_CORES                        =   0
DF_UTILS                        =   1
DF_SCRIPT                       =   2

"""
# -------------------------------------------------------------
# reload a single chapter
# -------------------------------------------------------------
"""            
def reload_chapter(chapter_to_load_flag,chapter_loaded_flag,chapterTitle,chapterstart,chapterlist,offset=3) :

    from dfcleanser.common.common_utils import run_jscript    
    
    print("reload_chapter",chapter_to_load_flag,chapter_loaded_flag,chapterTitle,chapterstart)
    
    if(chapter_to_load_flag == DO_NOT_LOAD_CHAPTER) :
        if(chapter_loaded_flag == CHAPTER_LOADED) :
            
            jscript     =   ("delete_dfc_chapter('" + chapterTitle + "')")
            run_jscript(jscript,"Error UnLoading dfcleanser Chapter",chapterTitle)
                
    else :
        if(chapter_loaded_flag == CHAPTER_NOT_LOADED) :
            jscript     =   ("select_cell_from_metadata('" + chapterstart + "'," + str(offset) + ")")
            run_jscript(jscript,"Error ReLoading dfcleanser Chapter",chapterTitle)
                
            add_dfc_cell(MARKDOWN,chapterTitle)
            add_dfc_cell(MARKDOWN,chapterlist[0])
            add_dfc_cell(CODE,chapterlist[1])
            add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
"""
# -------------------------------------------------------------
# reload the existing dfcleanser nmotebook cells 
# -------------------------------------------------------------
"""            
def reload_dfcleanser() :
    
    from dfcleanser.common.common_utils import run_jscript    
    
    print("reload_dfcleanser")
    
    
    dfc_loaded = cfg.get_config_value(cfg.DFC_CURRENTLY_LOADED_KEY)
    print("reload_dfcleanser loaded : ",dfc_loaded)
    
    if(not (dfc_loaded)) :
        load_dfcleanser()
    else :
            
        cells_loaded = cfg.get_chapters_loaded_cbs()
        print("reload_dfcleanser loaded : ",cells_loaded)
        corecbs     =   cfg.get_config_value(cfg.CORE_CBS_KEY)
        utilscbs    =   cfg.get_config_value(cfg.UTILITIES_CBS_KEY)
        scriptcbs   =   cfg.get_config_value(cfg.SCRIPTING_CBS_KEY)
        print("corecbs : ",corecbs)
        print("utilscbs : ",utilscbs)
        print("scriptcbs : ",scriptcbs)
        # check the core chapters
        for i in range(len(corecbs)) :
        
            if(i==0)    :  reload_chapter(corecbs[i],cells_loaded[0][0],DC_DATA_IMPORT_TITLE,DC_SYSTEM_TITLE,[dfchelp.IMPORT_HELP_ID,DC_DATA_IMPORT]) 
            elif(i==1)  :  reload_chapter(corecbs[i],cells_loaded[0][1],DC_DATA_INSPECTION_TITLE,DC_DATA_IMPORT_TITLE,[dfchelp.INSPECT_HELP_ID,DC_DATA_INSPECTION]) 
            elif(i==2)  :  reload_chapter(corecbs[i],cells_loaded[0][2],DC_DATA_CLEANSING_TITLE,DC_DATA_INSPECTION_TITLE,[dfchelp.CLEANSE_HELP_ID,DC_DATA_CLEANSING]) 
            elif(i==3)  :  reload_chapter(corecbs[i],cells_loaded[0][3],DC_DATA_TRANSFORM_TITLE,DC_DATA_CLEANSING_TITLE,[dfchelp.TRANSFORM_HELP_ID,DC_DATA_TRANSFORM]) 
            elif(i==4)  :  reload_chapter(corecbs[i],cells_loaded[0][4],DC_DATA_EXPORT_TITLE,DC_DATA_TRANSFORM_TITLE,[dfchelp.EXPORT_HELP_ID,DC_DATA_EXPORT]) 
                    
        # check the if need to load utilities heading
        last_util   =   -1
        for i in range(len(utilscbs)) :
            if(utilscbs[i] == LOAD_CHAPTER) :  last_util = i
        
        if(last_util == -1) :
            # assume utilities header load so delete it
            reload_chapter(DO_NOT_LOAD_CHAPTER,CHAPTER_LOADED,DC_SW_UTILITIES,None,[None,None],-1) 
        else :
            # no utilities currently loadeed 
            if( not ((cells_loaded[DF_UTILS][DF_UTILS_DATA_STRUCTURE]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_GEOCODING]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_SUBSET]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_CONCAT])) ) : 
                jscript     =   ("select_cell_from_metadata('" + DC_DATA_EXPORT_TITLE + "'," + str(3) + ")")
                run_jscript(jscript,"Error ReLoading dfcleanser Chapter",DC_SW_UTILITIES)
                add_dfc_cell(MARKDOWN,DC_SW_UTILITIES)
                add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
       
        # check if need to reload utils
        for i in range(len(utilscbs)) :     
        
            if(i==DF_UTILS_DATA_STRUCTURE)    :  reload_chapter(utilscbs[DF_UTILS_DATA_STRUCTURE],cells_loaded[DF_UTILS][DF_UTILS_DATA_STRUCTURE],
                                                                DC_LIST_UTILITY_TITLE,
                                                                DC_SW_UTILITIES,[dfchelp.LIST_UTILITY_HELP_ID,DC_LIST_UTILITY],1)
            
            elif(i==DF_UTILS_GEN_FUNCTION)  :  
                if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_GEN_FUNCTION],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION],
                                   DC_GEN_FUNCTION_UTILITY_TITLE,DC_LIST_UTILITY_TITLE,
                                   [dfchelp.GEN_FUNCTION_UTILITY_HELP_ID,DC_GEN_FUNCTION_UTILITY])
                else :
                    reload_chapter(utilscbs[DF_UTILS_GEN_FUNCTION],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION],
                                   DC_GEN_FUNCTION_UTILITY_TITLE,DC_SW_UTILITIES,
                                   [dfchelp.GEN_FUNCTION_UTILITY_HELP_ID,DC_GEN_FUNCTION_UTILITY],1)
                    
            elif(i==DF_UTILS_GEOCODING)  :  
                
                if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                   DC_GEOCODE_UTILITY_TITLE,DC_GEN_FUNCTION_UTILITY_TITLE,
                                   [dfchelp.GEOCODING_HELP_ID,DC_GEOCODE_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                       cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                       DC_GEOCODE_UTILITY_TITLE,DC_LIST_UTILITY_TITLE,
                                       [dfchelp.GEOCODING_HELP_ID,DC_GEOCODE_UTILITY])
                    else :
                        reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                       cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                       DC_GEOCODE_UTILITY_TITLE,DC_SW_UTILITIES,
                                       [dfchelp.GEOCODING_HELP_ID,DC_GEOCODE_UTILITY],1)
            
            elif(i==DF_UTILS_SUBSET)  :  
                
                if(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                   cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                   DC_DFSUBSET_UTILITY_TITLE,DC_GEOCODE_UTILITY_TITLE,
                                   [dfchelp.DFSUBSET_HELP_ID,DC_DFSUBSET_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                       cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                       DC_DFSUBSET_UTILITY_TITLE,DC_GEN_FUNCTION_UTILITY_TITLE,
                                       [dfchelp.DFSUBSET_HELP_ID,DC_DFSUBSET_UTILITY])
                    else :
                        if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                            reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                           cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                           DC_DFSUBSET_UTILITY_TITLE,DC_LIST_UTILITY_TITLE,
                                           [dfchelp.DFSUBSET_HELP_ID,DC_DFSUBSET_UTILITY])
                        else :
                            reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                           cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                           DC_DFSUBSET_UTILITY_TITLE,DC_SW_UTILITIES,
                                           [dfchelp.DFSUBSET_HELP_ID,DC_DFSUBSET_UTILITY],1)
            
            elif(i==DF_UTILS_CONCAT)  :  
                
                if(utilscbs[DF_UTILS_SUBSET] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                   cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                   DC_DFCONCAT_UTILITY_TITLE,DC_DFSUBSET_UTILITY_TITLE,
                                   [dfchelp.DFCONCAT_HELP_ID,DC_DFCONCAT_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                       cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                       DC_DFCONCAT_UTILITY_TITLE,DC_GEOCODE_UTILITY_TITLE,
                                       [dfchelp.DFCONCAT_HELP_ID,DC_DFCONCAT_UTILITY])
                    else :
                        if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :    
                            reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                           cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                           DC_DFCONCAT_UTILITY_TITLE,DC_GEN_FUNCTION_UTILITY_TITLE,
                                           [dfchelp.DFCONCAT_HELP_ID,DC_DFCONCAT_UTILITY])
                        else :
                            if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                                reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                               cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                               DC_DFCONCAT_UTILITY_TITLE,DC_LIST_UTILITY_TITLE,
                                               [dfchelp.DFCONCAT_HELP_ID,DC_DFCONCAT_UTILITY])
                            else :
                                reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                               cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                               DC_DFCONCAT_UTILITY_TITLE,DC_SW_UTILITIES,
                                               [dfchelp.DFCONCAT_HELP_ID,DC_DFCONCAT_UTILITY],1)
                
        # check the scripting chapters
        if(scriptcbs[0] == LOAD_CHAPTER) :
            if(cells_loaded[DF_SCRIPT][0] == CHAPTER_NOT_LOADED) :

                if(last_util > -1) :
                    if(utilscbs[DF_UTILS_CONCAT] == LOAD_CHAPTER)               :   prevtitle   =   DC_DFCONCAT_UTILITY_TITLE 
                    elif(utilscbs[DF_UTILS_SUBSET] == LOAD_CHAPTER)             :   prevtitle   =   DC_DFSUBSET_UTILITY_TITLE  
                    elif(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER)          :   prevtitle   =   DC_GEOCODE_UTILITY_TITLE
                    elif(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER)       :   prevtitle   =   DC_GEN_FUNCTION_UTILITY_TITLE
                    elif(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER)     :   prevtitle   =   DC_LIST_UTILITY_TITLE
                    else                                                        :   prevtitle   =   DC_SW_UTILITIES
                else :
                    prevtitle   =   DC_DATA_EXPORT_TITLE    
                
                if(prevtitle == DC_SW_UTILITIES) :
                    jscript     =   ("select_cell_from_metadata('" + prevtitle + "',1)")
                else :
                    jscript     =   ("select_cell_from_metadata('" + prevtitle + "',3)")
                run_jscript(jscript,"Error ReLoading dfcleanser Chapter",DC_SCRIPTING)
        
                # insert sw utilities title 
                add_dfc_cell(MARKDOWN,DC_SCRIPTING)
                add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
                reload_chapter(LOAD_CHAPTER,CHAPTER_NOT_LOADED,DC_DATA_SCRIPTING_TITLE,DC_SCRIPTING,[dfchelp.SCRIPTING_HELP_ID,DC_DATA_SCRIPTING],1) 
       
        else :
            reload_chapter(DO_NOT_LOAD_CHAPTER,cells_loaded[DF_SCRIPT][0],DC_DATA_SCRIPTING_TITLE,DC_SCRIPTING,[dfchelp.SCRIPTING_HELP_ID,DC_DATA_SCRIPTING],1)
            reload_chapter(DO_NOT_LOAD_CHAPTER,cells_loaded[DF_SCRIPT][0],DC_SCRIPTING,None,[None,None],-1)     
                

        cfg.get_loaded_cells()

    