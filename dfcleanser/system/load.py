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
import dfcleanser.common.cell_utils as cells

from dfcleanser.common.common_utils import run_jscript 

DO_NOT_LOAD_CHAPTER             =   0
LOAD_CHAPTER                    =   1

CHAPTER_NOT_LOADED              =   0
CHAPTER_LOADED                  =   1


"""
# -------------------------------------------------------------
# Load and Unload the notebook cells 
# -------------------------------------------------------------
""" 
def add_dfc_cell(ctype,cellid,celltext=None,afterid=-1) :
    """
    * -------------------------------------------------------------------------- 
    * function : load the dfcleanser from the toolar - load cell before working cell
    * 
    * parms :
    *   cytpe       - cell type MARKDOW/CODE/
    *   cellid      - cell identifier
    *   celltext    - cell text
    *   afterid     - after cell id
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    if(celltext == None) :
        celltext = cells.get_dfc_cells_text(cells.get_cells_title_index(cellid))
        
    jscript     =   ("add_dfc_cell(" + str(ctype) + ",'" + celltext + "','" + str(cellid) + "','" + str(afterid) + "')")
    run_jscript(jscript,"Error Loading dfc Cell " + str(cellid)) 


def load_dfcleanser_from_toolbar(nbname, dfcmode) :
    """
    * -------------------------------------------------------------------------- 
    * function : load the dfcleanser from the toolar - load cell before working cell
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    cfg.set_dfc_mode(dfcmode)
    
    # select starting cell
    celltext    =  "DCWorkingTitle" 
    jscript     =   ("select_before_cell(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell " + "load_dfcleanser_from_toolbar") 
    
    import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm       
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"load_dfcleanser_from_toolbar " + nbname + " " + str(dfcmode))        
    
    cfg.set_notebookName(nbname)
    
    try :
        run_jscript("preloaddfcleanser();","Unable to preload dfcleanser")
    except :
        print("get_notebook_path error")



panda_title   =   """<div align="center" id="DCLogopubtn">
    <img src="https://rickkrasinski.github.io/dfcleanser/graphics/dfcLogoSmall.png" height="81px" width="440px">
</div>'
"""

system_html          =   """<div id="DCSystem" />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/SystemPopUp.png" width="60px" height="60px" align="left" title="System Environment" onclick="process_pop_up_cmd(0)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;System Environment</h3>
        <a name="SystemEnvironment"></a>
    </div>
    </div>
"""

import_html          =   """<div align="left" id="DCDataImport"  />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/ImportPopUp.png" width="60px" height="60px" align="left" title="Data Import" onclick="process_pop_up_cmd(1)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;Data Import</h3>
        <a name="DataImport"></a>
    </div>
    </div>
"""

inspect_html          =   """<div align="left" id="DCDataInspection" />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/InspectionPopUp.png" width="60px" height="60px" align="left" title="Data Inspection" onclick="process_pop_up_cmd(2)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;Data Inspection</h3>
        <a name="DataInspection"></a>
    </div>
    </div>
"""

cleansing_html          =   """<div align="left" id="DCDataCleansing" />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/CleansingPopUp.png" width="60px" height="60px" align="left" title="Data Cleansing" onclick="process_pop_up_cmd(3)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;Data Cleansing</h3>
        <a name="DataCleansing"></a>
    </div>
    </div>
"""

transform_html          =   """<div align="left" id="DCDataTransform" />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/TransformPopUp.png" width="60px" height="60px" align="left" title="Data Transform" onclick="process_pop_up_cmd(4)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;Data Transform</h3>
        <a name="DataTransform"></a>
    </div>
    </div>
"""

export_html          =   """<div align="left" id="DCDataExport" />
    <div style="margin-left:60px;"><img src="https://rickkrasinski.github.io/dfcleanser/graphics/ExportPopUp.png" width="60px" height="60px" align="left" title="Data Export" onclick="process_pop_up_cmd(5)" /></div>
    <div>
        <image width="10">
    </div>
    <div>
        <h3>&nbsp;&nbsp;&nbsp;Data Export</h3>
        <a name="DataExport"></a>
    </div>
    </div>
"""


def load_pop_up_startup() :

    from dfcleanser.common.common_utils import display_generic_grid
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[panda_title])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[system_html])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[import_html])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[inspect_html])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[cleansing_html])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[transform_html])
    display_generic_grid("dfcleanser-main-pop-up-title-wrapper",["dfc-header"],[export_html])

         
def load_dfcleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : load the dfcleanser from the notebook - after cell calling
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    celltext    =  "load_dfcleanser" 
    jscript     =   ("select_cell_from_text(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell " + "load_dfcleanser") 
    
    load_dfcleanser_cells() 
    
    # insert working cell 
    add_dfc_cell(cells.MARKDOWN,cells.DC_WORKING_TITLE)
    add_dfc_cell(cells.CODE,cells.DC_WORKING)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    print("* dfcleanser successfully loaded below")
    print("\n")
    
    
def load_dfcleanser_cells() : 
    """
    * -------------------------------------------------------------------------- 
    * function : load the dfcleanser cells
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm       
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"load_dfcleanser_cells "  + str(cfg.get_dfc_mode()))        
    
    showutilities   =   False
    
    utilcbs     =   cfg.get_config_value(cfg.UTILITIES_CBS_KEY)
    
    corecbs     =   [1,1,1,1,1]
    
    if(utilcbs == None) :
        showutilities     =   False
    else :
        for i in range(len(utilcbs)) :
            if(utilcbs[i] == LOAD_CHAPTER) :
                showutilities   =   True
            
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
    
    
        # insert main title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_PANDAS_TITLE)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
        # insert system cells 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SYSTEM_TITLE)
        add_dfc_cell(cells.CODE,cells.DC_SYSTEM)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        #print("DC_SYSTEM")

        # insert import cells
        if(corecbs[0]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_IMPORT_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_IMPORT)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert inspection cells
        if(corecbs[1]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_INSPECTION_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_INSPECTION)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert cleansing cells
        if(corecbs[2]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_CLEANSING_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_CLEANSING)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
        # insert transform cells
        if(corecbs[3]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_TRANSFORM_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_TRANSFORM)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
        # insert export cells 
        if(corecbs[4]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_EXPORT_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_EXPORT)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
            
    else :
        
        jscript     =   ("loaddfcleanserpopup();")
        run_jscript(jscript,"Error loading dfc cleanser popup ") 
        
    
    if(showutilities) :
        
        # insert sw utilities title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SW_UTILITIES)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert list utility cells 
        if(utilcbs[0]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_LIST_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_LIST_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert geocoding utility cells 
        if(utilcbs[1]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_GEOCODE_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_GEOCODE_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[2]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DFSUBSET_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DFSUBSET_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[3]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_CENSUS_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_CENSUS_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
            
            
        if(utilcbs[4]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_SCRIPTING_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DATA_SCRIPTING)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
            
    #cfg.sync_with_js()
    
    jscript     =   ("sync_notebook()")
    run_jscript(jscript,"Error Loading dfcleanser " + "Error Loading dfcleanser")

    cfg.set_config_value(cfg.DFC_CURRENTLY_LOADED_KEY,"True")
    cfg.get_loaded_cells()  
    

def unload_dfcleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : unload the dfcleanser cells
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    cfg.drop_config_value(cfg.DFC_CURRENTLY_LOADED_KEY)
    cfg.drop_config_value(cfg.DFC_CHAPTERS_LOADED_KEY)
    cfg.drop_config_value(cfg.UTILITIES_CBS_KEY)

    return()


def delete_chapter(chid) :
    """
    * -------------------------------------------------------------------------- 
    * function : delete a chapter
    * 
    * parms :
    *  chid     - chapter id
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    jscript     =   ("delete_dfc_chapter('" + chid + "')")
    run_jscript(jscript,"Error UnLoading dfcleanser Chapter " + chid)


def add_chapter(titleid,chid) :
    """
    * -------------------------------------------------------------------------- 
    * function : add a chapter
    * 
    * parms :
    *  chid         - chapter id
    *  afterid      - load after chapter id
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    add_dfc_cell(cells.MARKDOWN,titleid)
    add_dfc_cell(cells.CODE,chid)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)


def add_title_cell(titleid,afterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : add a title cell
    * 
    * parms :
    *  titleid      - title id
    *  afterid      - load after chapter id
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    jscript     =   ("select_cell_from_metadata('" + str(afterid) + "'," + str(1) + ")")
    run_jscript(jscript,"Error ReLoading dfcleanser Chapter " + str(titleid))
                
    add_dfc_cell(cells.MARKDOWN,titleid)


def delete_title_cell(titleid) :
    """
    * -------------------------------------------------------------------------- 
    * function : delete a title cell
    * 
    * parms :
    *  titleid      - title id
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    jscript     =   ("delete_dfc_cell('" + titleid + "')")
    run_jscript(jscript,"Error ReLoading dfcleanser Chapter " + str(titleid))
                
   
def reload_dfcleanser(chaptersToLoad) :
    """
    * -------------------------------------------------------------------------- 
    * function : reload dfcleanser based on cbs
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    print("reload_dfcleanser",chaptersToLoad)
    
    dfc_loaded = cfg.get_config_value(cfg.DFC_CURRENTLY_LOADED_KEY)
    
    if(dfc_loaded is None) :
        load_dfcleanser()
    else :
        
        utilscbs        =   chaptersToLoad[0]
        #scriptcbs       =   chaptersToLoad[1]
        
        chapters_loaded         =   cfg.get_config_value(cfg.DFC_CHAPTERS_LOADED_KEY)
        
        
        print("reload_dfcleanser",chaptersToLoad,utilscbs,chapters_loaded)
        
        load_utils  =   False
        for i in range(len(utilscbs)) :
            if(utilscbs[i]  == LOAD_CHAPTER) :
                load_utils  =   True
        
        # check if need to reload utils
        if(load_utils) :
            
            # check if utilities heading displayed
            if(chapters_loaded[cells.DC_SW_UTILITIES_ID] == CHAPTER_LOADED) :
                
                #delete currrent utilities chapters
                delete_title_cell(cells.DC_SW_UTILITIES)
                if(chapters_loaded[cells.DC_DATASTRUCT_UTILITY_ID] == CHAPTER_LOADED)   :    delete_chapter(cells.DC_LIST_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_GEOCODE_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEOCODE_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DFSUBSET_UTILITY_ID] == CHAPTER_LOADED)     :    delete_chapter(cells.DC_DFSUBSET_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_CENSUS_UTILITY_ID] == CHAPTER_LOADED)       :    delete_chapter(cells.DC_CENSUS_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DATA_SCRIPT_ID] == CHAPTER_LOADED)          :    delete_chapter(cells.DC_DATA_SCRIPTING_TITLE)
            
            # add the utilities title bar
            add_title_cell(cells.DC_SW_UTILITIES,cells.DC_DATA_EXPORT)
            
            # add the new utilities
            if(utilscbs[0] == LOAD_CHAPTER) :   add_chapter(cells.DC_LIST_UTILITY_TITLE,cells.DC_LIST_UTILITY)   
            if(utilscbs[1] == LOAD_CHAPTER) :   add_chapter(cells.DC_GEOCODE_UTILITY_TITLE,cells.DC_GEOCODE_UTILITY)   
            if(utilscbs[2] == LOAD_CHAPTER) :   add_chapter(cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_DFSUBSET_UTILITY)   
            if(utilscbs[3] == LOAD_CHAPTER) :   add_chapter(cells.DC_CENSUS_UTILITY_TITLE,cells.DC_CENSUS_UTILITY)   
            if(utilscbs[4] == LOAD_CHAPTER) :   add_chapter(cells.DC_DATA_SCRIPTING_TITLE,cells.DC_DATA_SCRIPTING)   
                    
        # no utils cbs to display
        else :
            
            # check if utilities heading displayed
            if(chapters_loaded[cells.DC_SW_UTILITIES_ID] == CHAPTER_LOADED) :
            
                #delete currrent utilities chapters
                delete_title_cell(cells.DC_SW_UTILITIES)
                if(chapters_loaded[cells.DC_DATASTRUCT_UTILITY_ID] == CHAPTER_LOADED)   :    delete_chapter(cells.DC_LIST_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_GEOCODE_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEOCODE_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DFSUBSET_UTILITY_ID] == CHAPTER_LOADED)     :    delete_chapter(cells.DC_DFSUBSET_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_CENSUS_UTILITY_ID] == CHAPTER_LOADED)       :    delete_chapter(cells.DC_CENSUS_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DATA_SCRIPT_ID] == CHAPTER_LOADED)          :    delete_chapter(cells.DC_DATA_SCRIPTING_TITLE)
            
        cfg.get_loaded_cells()

        cfg.set_config_value(cfg.UTILITIES_CBS_KEY,utilscbs)

    