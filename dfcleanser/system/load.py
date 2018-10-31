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
import dfcleanser.common.help_utils as dfchelp


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

def add_dfc_cell(ctype,cellid,celltext=None,afterid=-1) :
    
    if(celltext == None) :
        celltext = cells.get_dfc_cells_text(cellid)
        
    from dfcleanser.common.common_utils import run_jscript    
    jscript     =   ("add_dfc_cell(" + str(ctype) + ",'" + celltext + "','" + cellid + "','" + str(afterid) + "')")
    run_jscript(jscript,"Error Loading dfc Cell",cellid) 



def load_dfcleanser_from_toolbar() :

    # select starting cell
    from dfcleanser.common.common_utils import run_jscript
    celltext    =  "<br></br>" 
    jscript     =   ("select_before_cell(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell","load_dfcleanser_from_toolbar") 

    load_dfcleanser_cells()

"""
# -------------------------------------------------------------
# Install the dfcleanser nmotebook cells 
# -------------------------------------------------------------
"""            
def load_dfcleanser() :

    from dfcleanser.common.common_utils import run_jscript
    celltext    =  "load_dfcleanser" 
    jscript     =   ("select_cell_from_text(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell","setup_dfcleanser") 
    
    load_dfcleanser_cells() 
    
    # insert working cell 
    add_dfc_cell(cells.MARKDOWN,cells.DC_WORKING_TITLE)
    add_dfc_cell(cells.CODE,cells.DC_WORKING)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
def load_dfcleanser_cells() : 
    
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
    
    # insert main title 
    add_dfc_cell(cells.MARKDOWN,cells.DC_PANDAS_TITLE)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    # insert system cells 
    add_dfc_cell(cells.MARKDOWN,cells.DC_SYSTEM_TITLE)
    add_dfc_cell(cells.MARKDOWN,dfchelp.SYS_ENVIRONMENT_HELP_ID)
    add_dfc_cell(cells.CODE,cells.DC_SYSTEM)
    add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

    # insert import cells
    if(corecbs[0]) :
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_IMPORT_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.IMPORT_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_IMPORT)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

    # insert inspection cells
    if(corecbs[1]) :
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_INSPECTION_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.INSPECT_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_INSPECTION)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

    # insert cleansing cells
    if(corecbs[2]) :
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_CLEANSING_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.CLEANSE_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_CLEANSING)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    # insert transform cells
    if(corecbs[3]) :
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_TRANSFORM_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.TRANSFORM_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_TRANSFORM)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    # insert export cells 
    if(corecbs[4]) :
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_EXPORT_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.EXPORT_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_EXPORT)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
    if(showutilities) :
        
        # insert sw utilities title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SW_UTILITIES)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert list utility cells 
        if(utilcbs[0]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_LIST_UTILITY_TITLE)
            add_dfc_cell(cells.MARKDOWN,dfchelp.LIST_UTILITY_HELP_ID)
            add_dfc_cell(cells.CODE,cells.DC_LIST_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert gen function cells 
        if(utilcbs[1]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_GEN_FUNCTION_UTILITY_TITLE)
            add_dfc_cell(cells.MARKDOWN,dfchelp.GEN_FUNCTION_UTILITY_HELP_ID)
            add_dfc_cell(cells.CODE,cells.DC_GEN_FUNCTION_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert geocoding utility cells 
        if(utilcbs[2]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_GEOCODE_UTILITY_TITLE)
            add_dfc_cell(cells.MARKDOWN,dfchelp.GEOCODING_HELP_ID)
            add_dfc_cell(cells.CODE,cells.DC_GEOCODE_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[3]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DFSUBSET_UTILITY_TITLE)
            add_dfc_cell(cells.MARKDOWN,dfchelp.DFSUBSET_HELP_ID)
            add_dfc_cell(cells.CODE,cells.DC_DFSUBSET_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
        # insert dfsubset utility cells 
        if(utilcbs[4]) :
            add_dfc_cell(cells.MARKDOWN,cells.DC_DFCONCAT_UTILITY_TITLE)
            add_dfc_cell(cells.MARKDOWN,dfchelp.DFCONCAT_HELP_ID)
            add_dfc_cell(cells.CODE,cells.DC_DFCONCAT_UTILITY)
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
        
    if(scriptcbs[0]) :
        
        # insert scripting title 
        add_dfc_cell(cells.MARKDOWN,cells.DC_SCRIPTING)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

        # insert scripting cells 
        add_dfc_cell(cells.MARKDOWN,cells.DC_DATA_SCRIPTING_TITLE)
        add_dfc_cell(cells.MARKDOWN,dfchelp.SCRIPTING_HELP_ID)
        add_dfc_cell(cells.CODE,cells.DC_DATA_SCRIPTING)
        add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)

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
                
            add_dfc_cell(cells.MARKDOWN,chapterTitle)
            add_dfc_cell(cells.MARKDOWN,chapterlist[0])
            add_dfc_cell(cells.CODE,chapterlist[1])
            add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
    
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
        
            if(i==0)    :  reload_chapter(corecbs[i],cells_loaded[0][0],cells.DC_DATA_IMPORT_TITLE,cells.DC_SYSTEM_TITLE,[dfchelp.IMPORT_HELP_ID,cells.DC_DATA_IMPORT]) 
            elif(i==1)  :  reload_chapter(corecbs[i],cells_loaded[0][1],cells.DC_DATA_INSPECTION_TITLE,cells.DC_DATA_IMPORT_TITLE,[dfchelp.INSPECT_HELP_ID,cells.DC_DATA_INSPECTION]) 
            elif(i==2)  :  reload_chapter(corecbs[i],cells_loaded[0][2],cells.DC_DATA_CLEANSING_TITLE,cells.DC_DATA_INSPECTION_TITLE,[dfchelp.CLEANSE_HELP_ID,cells.DC_DATA_CLEANSING]) 
            elif(i==3)  :  reload_chapter(corecbs[i],cells_loaded[0][3],cells.DC_DATA_TRANSFORM_TITLE,cells.DC_DATA_CLEANSING_TITLE,[dfchelp.TRANSFORM_HELP_ID,cells.DC_DATA_TRANSFORM]) 
            elif(i==4)  :  reload_chapter(corecbs[i],cells_loaded[0][4],cells.DC_DATA_EXPORT_TITLE,cells.DC_DATA_TRANSFORM_TITLE,[dfchelp.EXPORT_HELP_ID,cells.DC_DATA_EXPORT]) 
                    
        # check the if need to load utilities heading
        last_util   =   -1
        for i in range(len(utilscbs)) :
            if(utilscbs[i] == LOAD_CHAPTER) :  last_util = i
        
        if(last_util == -1) :
            # assume utilities header load so delete it
            reload_chapter(DO_NOT_LOAD_CHAPTER,CHAPTER_LOADED,cells.DC_SW_UTILITIES,None,[None,None],-1) 
        else :
            # no utilities currently loadeed 
            if( not ((cells_loaded[DF_UTILS][DF_UTILS_DATA_STRUCTURE]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_GEOCODING]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_SUBSET]) or 
                     (cells_loaded[DF_UTILS][DF_UTILS_CONCAT])) ) : 
                jscript     =   ("select_cell_from_metadata('" + cells.DC_DATA_EXPORT_TITLE + "'," + str(3) + ")")
                run_jscript(jscript,"Error ReLoading dfcleanser Chapter",cells.DC_SW_UTILITIES)
                add_dfc_cell(cells.MARKDOWN,cells.DC_SW_UTILITIES)
                add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
       
        # check if need to reload utils
        for i in range(len(utilscbs)) :     
        
            if(i==DF_UTILS_DATA_STRUCTURE)    :  reload_chapter(utilscbs[DF_UTILS_DATA_STRUCTURE],cells_loaded[DF_UTILS][DF_UTILS_DATA_STRUCTURE],
                                                                cells.DC_LIST_UTILITY_TITLE,
                                                                cells.DC_SW_UTILITIES,[dfchelp.LIST_UTILITY_HELP_ID,cells.DC_LIST_UTILITY],1)
            
            elif(i==DF_UTILS_GEN_FUNCTION)  :  
                if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_GEN_FUNCTION],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION],
                                   cells.DC_GEN_FUNCTION_UTILITY_TITLE,cells.DC_LIST_UTILITY_TITLE,
                                   [dfchelp.GEN_FUNCTION_UTILITY_HELP_ID,cells.DC_GEN_FUNCTION_UTILITY])
                else :
                    reload_chapter(utilscbs[DF_UTILS_GEN_FUNCTION],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEN_FUNCTION],
                                   cells.DC_GEN_FUNCTION_UTILITY_TITLE,cells.DC_SW_UTILITIES,
                                   [dfchelp.GEN_FUNCTION_UTILITY_HELP_ID,cells.DC_GEN_FUNCTION_UTILITY],1)
                    
            elif(i==DF_UTILS_GEOCODING)  :  
                
                if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                   cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                   cells.DC_GEOCODE_UTILITY_TITLE,cells.DC_GEN_FUNCTION_UTILITY_TITLE,
                                   [dfchelp.GEOCODING_HELP_ID,cells.DC_GEOCODE_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                       cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                       cells.DC_GEOCODE_UTILITY_TITLE,cells.DC_LIST_UTILITY_TITLE,
                                       [dfchelp.GEOCODING_HELP_ID,cells.DC_GEOCODE_UTILITY])
                    else :
                        reload_chapter(utilscbs[DF_UTILS_GEOCODING],
                                       cells_loaded[DF_UTILS][DF_UTILS_GEOCODING],
                                       cells.DC_GEOCODE_UTILITY_TITLE,cells.DC_SW_UTILITIES,
                                       [dfchelp.GEOCODING_HELP_ID,cells.DC_GEOCODE_UTILITY],1)
            
            elif(i==DF_UTILS_SUBSET)  :  
                
                if(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                   cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                   cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_GEOCODE_UTILITY_TITLE,
                                   [dfchelp.DFSUBSET_HELP_ID,cells.DC_DFSUBSET_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                       cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                       cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_GEN_FUNCTION_UTILITY_TITLE,
                                       [dfchelp.DFSUBSET_HELP_ID,cells.DC_DFSUBSET_UTILITY])
                    else :
                        if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                            reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                           cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                           cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_LIST_UTILITY_TITLE,
                                           [dfchelp.DFSUBSET_HELP_ID,cells.DC_DFSUBSET_UTILITY])
                        else :
                            reload_chapter(utilscbs[DF_UTILS_SUBSET],
                                           cells_loaded[DF_UTILS][DF_UTILS_SUBSET],
                                           cells.DC_DFSUBSET_UTILITY_TITLE,cells.DC_SW_UTILITIES,
                                           [dfchelp.DFSUBSET_HELP_ID,cells.DC_DFSUBSET_UTILITY],1)
            
            elif(i==DF_UTILS_CONCAT)  :  
                
                if(utilscbs[DF_UTILS_SUBSET] == LOAD_CHAPTER) :
                    reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                   cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                   cells.DC_DFCONCAT_UTILITY_TITLE,cells.DC_DFSUBSET_UTILITY_TITLE,
                                   [dfchelp.DFCONCAT_HELP_ID,cells.DC_DFCONCAT_UTILITY])
                else :
                    if(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER) :    
                        reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                       cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                       cells.DC_DFCONCAT_UTILITY_TITLE,cells.DC_GEOCODE_UTILITY_TITLE,
                                       [dfchelp.DFCONCAT_HELP_ID,cells.DC_DFCONCAT_UTILITY])
                    else :
                        if(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER) :    
                            reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                           cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                           cells.DC_DFCONCAT_UTILITY_TITLE,cells.DC_GEN_FUNCTION_UTILITY_TITLE,
                                           [dfchelp.DFCONCAT_HELP_ID,cells.DC_DFCONCAT_UTILITY])
                        else :
                            if(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER) :
                                reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                               cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                               cells.DC_DFCONCAT_UTILITY_TITLE,cells.DC_LIST_UTILITY_TITLE,
                                               [dfchelp.DFCONCAT_HELP_ID,cells.DC_DFCONCAT_UTILITY])
                            else :
                                reload_chapter(utilscbs[DF_UTILS_CONCAT],
                                               cells_loaded[DF_UTILS][DF_UTILS_CONCAT],
                                               cells.DC_DFCONCAT_UTILITY_TITLE,cells.DC_SW_UTILITIES,
                                               [dfchelp.DFCONCAT_HELP_ID,cells.DC_DFCONCAT_UTILITY],1)
                
        # check the scripting chapters
        if(scriptcbs[0] == LOAD_CHAPTER) :
            if(cells_loaded[DF_SCRIPT][0] == CHAPTER_NOT_LOADED) :

                if(last_util > -1) :
                    if(utilscbs[DF_UTILS_CONCAT] == LOAD_CHAPTER)               :   prevtitle   =   cells.DC_DFCONCAT_UTILITY_TITLE 
                    elif(utilscbs[DF_UTILS_SUBSET] == LOAD_CHAPTER)             :   prevtitle   =   cells.DC_DFSUBSET_UTILITY_TITLE  
                    elif(utilscbs[DF_UTILS_GEOCODING] == LOAD_CHAPTER)          :   prevtitle   =   cells.DC_GEOCODE_UTILITY_TITLE
                    elif(utilscbs[DF_UTILS_GEN_FUNCTION] == LOAD_CHAPTER)       :   prevtitle   =   cells.DC_GEN_FUNCTION_UTILITY_TITLE
                    elif(utilscbs[DF_UTILS_DATA_STRUCTURE] == LOAD_CHAPTER)     :   prevtitle   =   cells.DC_LIST_UTILITY_TITLE
                    else                                                        :   prevtitle   =   cells.DC_SW_UTILITIES
                else :
                    prevtitle   =   cells.DC_DATA_EXPORT_TITLE    
                
                if(prevtitle == cells.DC_SW_UTILITIES) :
                    jscript     =   ("select_cell_from_metadata('" + prevtitle + "',1)")
                else :
                    jscript     =   ("select_cell_from_metadata('" + prevtitle + "',3)")
                run_jscript(jscript,"Error ReLoading dfcleanser Chapter",cells.DC_SCRIPTING)
        
                # insert sw utilities title 
                add_dfc_cell(cells.MARKDOWN,cells.DC_SCRIPTING)
                add_dfc_cell(cells.MARKDOWN,cells.DC_BLANK_LINE)
                reload_chapter(LOAD_CHAPTER,CHAPTER_NOT_LOADED,cells.DC_DATA_SCRIPTING_TITLE,cells.DC_SCRIPTING,[dfchelp.SCRIPTING_HELP_ID,cells.DC_DATA_SCRIPTING],1) 
       
        else :
            reload_chapter(DO_NOT_LOAD_CHAPTER,cells_loaded[DF_SCRIPT][0],cells.DC_DATA_SCRIPTING_TITLE,cells.DC_SCRIPTING,[dfchelp.SCRIPTING_HELP_ID,cells.DC_DATA_SCRIPTING],1)
            reload_chapter(DO_NOT_LOAD_CHAPTER,cells_loaded[DF_SCRIPT][0],cells.DC_SCRIPTING,None,[None,None],-1)     
                

        cfg.get_loaded_cells()

    