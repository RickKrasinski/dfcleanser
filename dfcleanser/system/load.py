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

DF_UTILS_DATA_STRUCTURE         =   0
DF_UTILS_GEN_FUNCTION           =   1
DF_UTILS_GEOCODING              =   2
DF_UTILS_SUBSET                 =   3

DF_CORES                        =   0
DF_UTILS                        =   1
DF_SCRIPT                       =   2




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


def load_dfcleanser_from_toolbar(nbname) :
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

    # select starting cell
    celltext    =  "DCWorkingTitle" 
    jscript     =   ("select_before_cell(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell " + "load_dfcleanser_from_toolbar") 
    
    import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm       
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"load_dfcleanser_from_toolbar " + nbname)        
    
    cfg.set_notebookName(nbname)
    
    try :
        run_jscript("window.getNotebookPathBeforeLoad();","Unable to get notebook path")
    except :
        print("get_notebook_path error")

           
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
    run_jscript(jscript,"Error setting dfc Cell " + "setup_dfcleanser") 
    
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
    
    showutilities   =   False
    
    corecbs     =   cfg.get_config_value(cfg.CORE_CBS_KEY)
    utilcbs     =   cfg.get_config_value(cfg.UTILITIES_CBS_KEY)
    scriptcbs   =   cfg.get_config_value(cfg.SCRIPTING_CBS_KEY)
    
    #if(corecbs == None) :
    corecbs     =   [1,1,1,1,1]
    if(utilcbs == None) :
        showutilities     =   False
    else :
        for i in range(len(utilcbs)) :
            if(utilcbs[i] == LOAD_CHAPTER) :
                showutilities   =   True
            
    if(scriptcbs == None) :
        scriptcbs   =   [0]
    
    # insert main title 
    add_dfc_cell(cells.MARKDOWN,cells.DC_PANDAS_TITLE)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    # insert system cells 
    add_dfc_cell(cells.MARKDOWN,cells.DC_SYSTEM_TITLE)
    add_dfc_cell(cells.CODE,cells.DC_SYSTEM)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

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
    
    if(showutilities) :
        
        # insert sw utilities title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SW_UTILITIES)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert list utility cells 
        if(utilcbs[0]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_LIST_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_LIST_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert gen function cells 
        if(utilcbs[1]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_GEN_FUNCTION_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_GEN_FUNCTION_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert geocoding utility cells 
        if(utilcbs[2]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_GEOCODE_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_GEOCODE_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[3]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DFSUBSET_UTILITY_TITLE)
            add_dfc_cell(cells.CODE,cells.DC_DFSUBSET_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
    if(scriptcbs[0]) :
        
        # insert scripting title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SCRIPTING)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert scripting cells 
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_SCRIPTING_TITLE)
        add_dfc_cell(cells.CODE,cells.DC_DATA_SCRIPTING)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    cfg.sync_js()
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

    return()

    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser " + "Error UnLoading dfcleanser")
    
    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser " + "Error UnLoading dfcleanser")

    jscript     =   ("unload_dfcleanser()")
    run_jscript(jscript,"Error UnLoading dfcleanser " + "Error UnLoading dfcleanser")



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
    
    dfc_loaded = cfg.get_config_value("dfcleanserCurrentlyLoaded")
    
    if(dfc_loaded is None) :
        load_dfcleanser()
    else :
        
        corecbs         =   chaptersToLoad[0]
        utilscbs        =   chaptersToLoad[1]
        scriptcbs       =   chaptersToLoad[2]
        
        chapters_loaded         =   cfg.get_config_value(cfg.DFC_CHAPTERS_LOADED_KEY)
        
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
                if(chapters_loaded[cells.DC_GENFUNC_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEN_FUNCTION_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_GEOCODE_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEOCODE_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DFSUBSET_UTILITY_ID] == CHAPTER_LOADED)     :    delete_chapter(cells.DC_DFSUBSET_UTILITY_TITLE)
            
            # add the utilities title bar
            if(chapters_loaded[cells.EXPORT_CUSTOM_CODE_ID] == CHAPTER_NOT_LOADED) :
                add_title_cell(cells.DC_SW_UTILITIES,cells.DC_DATA_EXPORT)
            else :
                add_title_cell(cells.DC_SW_UTILITIES,cells.DC_DATA_CUSTOM_EXPORT)
            
            # add the new utilities
            if(utilscbs[0] == LOAD_CHAPTER) :   add_chapter(cells.DC_LIST_UTILITY_TITLE,cells.DC_LIST_UTILITY)   
            if(utilscbs[1] == LOAD_CHAPTER) :   add_chapter(cells.DC_GEN_FUNCTION_UTILITY_TITLE,cells.DC_GEN_FUNCTION_UTILITY)   
            if(utilscbs[2] == LOAD_CHAPTER) :   add_chapter(cells.DC_GEOCODE_UTILITY_TITLE,cells.DC_GEOCODE_UTILITY)   
            if(utilscbs[3] == LOAD_CHAPTER) :   add_chapter(cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_DFSUBSET_UTILITY)   
                    
        # no utils cbs to display
        else :
            
            # check if utilities heading displayed
            if(chapters_loaded[cells.DC_SW_UTILITIES_ID] == CHAPTER_LOADED) :
            
                #delete currrent utilities chapters
                delete_title_cell(cells.DC_SW_UTILITIES)
                if(chapters_loaded[cells.DC_DATASTRUCT_UTILITY_ID] == CHAPTER_LOADED)   :    delete_chapter(cells.DC_LIST_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_GENFUNC_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEN_FUNCTION_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_GEOCODE_UTILITY_ID] == CHAPTER_LOADED)      :    delete_chapter(cells.DC_GEOCODE_UTILITY_TITLE)
                if(chapters_loaded[cells.DC_DFSUBSET_UTILITY_ID] == CHAPTER_LOADED)     :    delete_chapter(cells.DC_DFSUBSET_UTILITY_TITLE)
            
        # check the scripting chapters
        if(scriptcbs[0] == LOAD_CHAPTER) :
            if(chapters_loaded[cells.DC_SCRIPTING_ID] == CHAPTER_NOT_LOADED) :

                if(len(utilscbs) > 0) :
                    if(utilscbs[3]   == LOAD_CHAPTER)    :   afterid   =   cells.DC_DFSUBSET_UTILITY  
                    elif(utilscbs[2] == LOAD_CHAPTER)    :   afterid   =   cells.DC_GEOCODE_UTILITY
                    elif(utilscbs[1] == LOAD_CHAPTER)    :   afterid   =   cells.DC_GEN_FUNCTION_UTILITY
                    elif(utilscbs[0] == LOAD_CHAPTER)    :   afterid   =   cells.DC_LIST_UTILITY
                    
                else :
                    if(chapters_loaded[cells.EXPORT_CUSTOM_CODE_ID] == CHAPTER_NOT_LOADED) :
                        afterid   =   cells.DC_DATA_EXPORT
                    else :
                        afterid   =   cells.DC_DATA_CUSTOM_EXPORT
                
                add_title_cell(cells.DC_SCRIPTING,afterid)
                add_chapter(cells.DC_DATA_SCRIPTING_TITLE,cells.DC_DATA_SCRIPTING)
                
        else :
            if(chapters_loaded[cells.DC_SCRIPTING_ID] == CHAPTER_LOADED) :
                delete_title_cell(cells.DC_SCRIPTING)
                delete_chapter(cells.DC_DATA_SCRIPTING_TITLE)                

        cfg.get_loaded_cells()

        cfg.set_config_value(cfg.CORE_CBS_KEY,corecbs)
        cfg.set_config_value(cfg.UTILITIES_CBS_KEY,utilscbs)
        cfg.set_config_value(cfg.SCRIPTING_CBS_KEY,scriptcbs)

    