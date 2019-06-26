"""
# sw_utility_genfunc_widgets
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg 
import dfcleanser.common.help_utils as dfchelp
from dfcleanser.sw_utilities import sw_utility_genfunc_control as gfc
import dfcleanser.sw_utilities.sw_utility_genfunc_model as gfm

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (SCROLL_DOWN, dcTable, ROW_MAJOR, get_row_major_table)

from dfcleanser.common.common_utils import (display_generic_grid, get_parms_for_input)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    generic functions components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#    generic functions task bar
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#    data transform task bar
#--------------------------------------------------------------------------
"""
gen_function_tb_doc_title                 =   "Generic Functions"
gen_function_tb_title                     =   "Generic Functions"
gen_function_tb_id                        =   "genfunctiontb"

gen_function_tb_keyTitleList              =   ["Generic Functions",
                                               "Clear","Reset","Help"]

gen_function_tb_jsList                    =   ["genfunction_task_bar_callback("+str(gfm.DISPLAY_GENERIC_FUNCTION)+")",
                                               "genfunction_task_bar_callback(0)",
                                               "process_pop_up_cmd(6)",
                                               "displayhelp(" + str(dfchelp.GENFUNC_GEN_ID) + ")"]

gen_function_tb_centered                  =   True

"""
#--------------------------------------------------------------------------
#    generic functions inputs
#--------------------------------------------------------------------------
"""
gen_function_input_title         =   "Generic Function"
gen_function_input_id            =   "genfuncform"
gen_function_input_idList        =   ["gtmodule",
                                      "gttitle",
                                      "gtcode",
                                      None,None,None,None,None,None,None]

gen_function_input_labelList     =   ["function_module",
                                      "function_title",
                                      "function_code",
                                      "Open Test</br>Code Cell",
                                      "Grab Test</br>Cell Code",
                                      "Save</br>Current",
                                      "Delete</br>Current",
                                      "Clear","Return","Help"]

gen_function_input_typeList      =   ["text","text",
                                      maketextarea(20),
                                     "button","button","button","button","button","button","button"]

gen_function_input_placeholderList  = ["enter function module",
                                       "enter function title",
                                      "# Generic Function",
                                      None,None,None,None,None]

gen_function_input_jsList        =    [None,None,None,
                                      "generic_function_callback("+str(gfm.LOAD_FUNCTION)+")",
                                      "generic_function_callback("+str(gfm.SAVE_FUNCTION)+")",
                                      "generic_function_callback("+str(gfm.UPDATE_FUNCTION)+")",
                                      "generic_function_callback("+str(gfm.DELETE_FUNCTION)+")",
                                      "generic_function_callback("+str(gfm.CLEAR_FUNCTION)+")",
                                      "generic_function_callback("+str(gfm.RETURN_FUNCTION)+")",
                                      "displayhelp(" + str(dfchelp.GENFUNC_GEN_NEW_ID) + ")"]

gen_function_input_reqList       =   [0,1,2]

gen_function_input_form          =   [gen_function_input_id,
                                      gen_function_input_idList,
                                      gen_function_input_labelList,
                                      gen_function_input_typeList,
                                      gen_function_input_placeholderList,
                                      gen_function_input_jsList,
                                      gen_function_input_reqList]  


"""
#--------------------------------------------------------------------------
#    generic functions display functions
#--------------------------------------------------------------------------
"""
def get_genfunc_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(gen_function_tb_id,
                                               gen_function_tb_keyTitleList,
                                               gen_function_tb_jsList,
                                               gen_function_tb_centered),False)


def get_genfunc_input_parms(parms) :
    return(get_parms_for_input(parms,gen_function_input_idList))


def display_generic_function_inputs(ftitle,notes = False) :
    
    print("display_generic_function_inputs",ftitle)

    if(not(ftitle is None)) :
        
        cfg.set_config_value(cfg.CURRENT_GENERIC_FUNCTION,ftitle)
        gt_func = gfc.get_generic_function(ftitle)

        if(not (gt_func == None)) :
            
            if(type(gt_func) == str) :
                fparms = [gfm.reservedfunctionsmodule,
                          ftitle,
                          gt_func]
                
            else :
                fparms = [gt_func.get_func_module(),
                          gt_func.get_func_title(),
                          gt_func.get_func_code()]
                
            cfg.set_config_value(gen_function_input_id+"Parms",fparms)

    display_generic_functions()
    print("\n")


def get_genfunc_list() :
    
    if(gfc.get_total_generic_functions() == 0) :
        return(None)
    else :
        gtfuncs = gfc.get_generic_functions_names_list()
        gtfuncs.sort()
        return(gtfuncs)


"""
#------------------------------------------------------------------
#   get the generic functions table
#------------------------------------------------------------------
"""
def get_genfunc_html(forfunc=gfm.FOR_GEN_FUNC) :

    genTranslistHeader      =   [""]
    genTranslistRows        =   []
    genTranslistWidths      =   [100]
    genTranslistAligns      =   ["left"]
    genTranslistHrefs       =   []

    colorList               =   []
    
    if(gfc.get_total_generic_functions() == 0) :
        genTranslistRows.append(["No Generic Functions"])
    else :

        gtfuncs = gfc.get_generic_functions_names_list()
        gtfuncs.sort()
        
        for i in range(len(gtfuncs)) :

            genTranslistRows.append([gtfuncs[i]])

            if(forfunc==gfm.FOR_ADD_COLUMNS) :
                genTranslistHrefs.append(["select_addcol_gen_function"])
            elif(forfunc==gfm.FOR_APPLY_FN) :
                genTranslistHrefs.append(["select_applyfn_gen_function"])
            else :
                genTranslistHrefs.append(["select_gen_function"])
                
            colorRow = []
            found = False
                
            for j in range(len(gfm.reservedfunctions)) :
                if(gtfuncs[i] == gfm.reservedfunctions[j]) :
                    found = True
                        
            if(found) :
                colorRow.append(gfm.Yellow)
            else :
                colorRow.append(None)
                        
            colorList.append(colorRow)

    gt_table = dcTable("Generic Functions","gtTable",
                       cfg.GenFunction_ID,
                       genTranslistHeader,genTranslistRows,
                       genTranslistWidths,genTranslistAligns)

    
    if(len(genTranslistHrefs) > 0) :
        gt_table.set_refList(genTranslistHrefs)
        
    gt_table.set_small(True)
    gt_table.set_smallwidth(95)
    gt_table.set_smallmargin(5)
    gt_table.set_border(True)
    
    if(not (forfunc == gfm.FOR_APPLY_FN)) :
        gt_table.set_checkLength(True)
        gt_table.set_textLength(32)
    else :
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            gt_table.set_checkLength(True)
            gt_table.set_textLength(32)
        else :
            gt_table.set_checkLength(True)
            gt_table.set_textLength(20)
    
    gt_table.set_html_only(True) 
    
    gt_table.set_tabletype(ROW_MAJOR)
    gt_table.set_rowspertable(14)
    
    if(len(colorList) > 0) :
        gt_table.set_color(True)
        gt_table.set_colorList(colorList)
    
    gt_table.set_note("&nbsp;&nbsp;&nbsp;reserved system functions")
    gt_table.set_notecolor(gfm.Yellow)
    
    #gt_table.dump()
    listHtml = get_row_major_table(gt_table,SCROLL_DOWN,False)
    
    return(listHtml)

        
def get_genfunc_module(ftitle) :
    
    if(ftitle in gfm.reservedfunctions) :
        return(gfm.reservedfunctionsmodule) 
    else :
        gt_func     =   gfc.get_generic_function(ftitle)
        
        if(not (gt_func is None)) :
            return(gt_func.get_func_module()) 
        else :
            return("None")


"""
#------------------------------------------------------------------
#   display the gneric transforms
#------------------------------------------------------------------
"""
def display_generic_functions(forAddColumn=False):

    gtlistHtml = get_genfunc_html()

    ftitle  =  cfg.get_config_value(cfg.CURRENT_GENERIC_FUNCTION) 

    if(not (ftitle is None)) :

        code        =   gfc.get_generic_function(ftitle)
        
        if(not(code is None)) :
            if(not (type(code) == str)) :
                code    =   code.get_func_code()
                fmodule     =   get_genfunc_module(ftitle)
            else :
                fmodule     =   gfm.reservedfunctionsmodule
                
            parms = [fmodule,ftitle,code]
            cfg.set_config_value(gen_function_input_id+"Parms",parms)
    
    gt_input_form = InputForm(gen_function_input_form[0],
                              gen_function_input_form[1],
                              gen_function_input_form[2],
                              gen_function_input_form[3],
                              gen_function_input_form[4],
                              gen_function_input_form[5],
                              gen_function_input_form[6],
                              shortForm=False)
    
    gt_input_form.set_gridwidth(700)
    gt_input_form.set_custombwidth(90)
    
    gt_input_html = ""
    gt_input_html = gt_input_form.get_html()
    
    cfg.drop_config_value(gen_function_input_id+"Parms")
        
    gt_heading_html =   "<div>" + gen_function_input_title + "</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [gt_heading_html,gtlistHtml,gt_input_html]
    
    print("\n")
    display_generic_grid("sw-utils-wrapper",gridclasses,gridhtmls)



