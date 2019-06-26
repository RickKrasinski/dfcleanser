"""
# sw_utility_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.sw_utilities.sw_utility_model as swum
import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.sw_utilities.sw_utility_genfunc_functions as swgf
import dfcleanser.sw_utilities.sw_utility_genfunc_model as swgm


from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_DOWN, ROW_MAJOR)
from dfcleanser.common.common_utils import (display_generic_grid, get_parms_for_input)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Build List Dict Utility form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    build list task bar
#--------------------------------------------------------------------------
"""
build_utility_tb_doc_title        =   "Build Utility Options"
build_utility_tb_title            =   "Build Options"
build_utility_tb_id               =   "buildutilityoptionstb"

build_utility_tb_keyTitleList     =   ["Lists","Dicts","Functions","Clear","Reset","Help"]

build_utility_tb_jsList           =   ["build_utility_callback("+str(swum.LIST_OPTION)+")",
                                       "build_utility_callback("+str(swum.DICT_OPTION)+")",
                                       "build_utility_callback("+str(swum.GENFUNC_OPTION)+")",
                                       "build_utility_clear_callback()",
                                       "process_pop_up_cmd(6)",
                                       "displayhelp(" + str(dfchelp.LIST_UTILITY_MAIN_TASKBAR_ID) + ")"]

build_utility_tb_centered         =   True

"""
#--------------------------------------------------------------------------
#    build list utility input 
#--------------------------------------------------------------------------
"""
build_list_utility_input_title          =   "Build List Utility"
build_list_utility_input_id             =   "buildlistparms"
build_list_utility_input_idList         =   ["listname","listitems","startlistfile",
                                             None,None,None,None,None]

build_list_utility_input_labelList      =   ["list_name",
                                             "list_value(s)",
                                             "list_file_to_start_with",
                                             "Delete</br>From</br>Lists",
                                             "Save</br> To </br>Lists",
                                             "Clear","Return","Help"]

build_list_utility_input_typeList       =   ["text",maketextarea(10),"file",
                                             "button","button",
                                             "button","button","button"]

build_list_utility_input_placeholderList = ["enter list name in 'Notebook' lists (default None)",
                                            "enter new list value(s) example (&#39;1&#39;, 2, a, &#39;b&#39;, [3,4] ...)",
                                            "select file to start with (default None)",
                                            None,None,None,None,None]

build_list_utility_input_jsList         =    [None,None,None,
                                              "sw_utilities_delete_callback("+str(swum.DELETE_LIST_OPTION)+")",
                                              "sw_utilities_list_add_callback()",
                                              "build_utility_callback("+str(swum.LIST_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp(" + str(dfchelp.LIST_UTILITY_BUILD_LIST_ID) + ")"]

build_list_utility_input_reqList        =   [0,1]

build_list_utility_input_form           =   [build_list_utility_input_id,
                                             build_list_utility_input_idList,
                                             build_list_utility_input_labelList,
                                             build_list_utility_input_typeList,
                                             build_list_utility_input_placeholderList,
                                             build_list_utility_input_jsList,
                                             build_list_utility_input_reqList]  


"""
#--------------------------------------------------------------------------
#    build dict utility input 
#--------------------------------------------------------------------------
"""
build_dict_utility_input_title          =   "Build Dict Utility"
build_dict_utility_input_id             =   "builddictparms"
build_dict_utility_input_idList         =   ["dictname",
                                             "dictpairs",
                                             "startdictfile",
                                             None,None,None,None,None]

build_dict_utility_input_labelList      =   ["dict_name",
                                             "dict_values",
                                             "dict_file_to_start_with",
                                             "Delete</br>From</br>Dicts",
                                             "Save</br> To </br>Dicts",
                                             "Clear","Return","Help"]

build_dict_utility_input_typeList       =   ["text",maketextarea(10),"file",
                                             "button","button",
                                             "button","button","button"]

build_dict_utility_input_placeholderList = ["enter dict name in 'Notebook' dicts (default None)",
                                            "enter new dict pairs(s) (&#39;&#39;{key:value}&#39;&#39;,&#39;&#39;.....{key:value})",
                                            "select file to start with (default None)",
                                            None,None,None,None,None]

build_dict_utility_input_jsList         =    [None,None,None,
                                              "sw_utilities_delete_callback("+str(swum.DELETE_DICT_OPTION)+")",
                                              "sw_utilities_dict_add_callback()",
                                              "build_utility_callback("+str(swum.DICT_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp(" + str(dfchelp.LIST_UTILITY_BUILD_DICT_ID) + ")"]

build_dict_utility_input_reqList        =   [0,1]

build_dict_utility_input_form           =   [build_dict_utility_input_id,
                                             build_dict_utility_input_idList,
                                             build_dict_utility_input_labelList,
                                             build_dict_utility_input_typeList,
                                             build_dict_utility_input_placeholderList,
                                             build_dict_utility_input_jsList,
                                             build_dict_utility_input_reqList]  


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
                                      None,None,None,None,None]

gen_function_input_labelList     =   ["function_module",
                                      "function_title",
                                      "function_code",
                                      "Save</br>Current</br>Function",
                                      "Delete</br>Current</br>Function",
                                      "Clear</br>Current</br>Function",
                                      "Return","Help"]

gen_function_input_typeList      =   ["text","text",
                                      maketextarea(20),
                                     "button","button","button","button","button"]

gen_function_input_placeholderList  = ["enter function module",
                                       "enter function title",
                                      "# Generic Function",
                                      None,None,None,None,None]

gen_function_input_jsList        =    [None,None,None,
                                      "generic_function_callback("+str(swum.SAVE_FUNCTION)+")",
                                      "generic_function_callback("+str(swum.DELETE_FUNCTION)+")",
                                      "generic_function_callback("+str(swum.CLEAR_FUNCTION)+")",
                                      "generic_function_callback("+str(swum.RETURN_FUNCTION)+")",
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
#--------------------------------------------------------------------------
#   SW Utilities display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_sw_utilities_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(build_utility_tb_id,
                                               build_utility_tb_keyTitleList,
                                               build_utility_tb_jsList,
                                               build_utility_tb_centered),False)


def get_sw_utilities_list_inputs(parms) :
        return(get_parms_for_input(parms,build_list_utility_input_idList))


def get_sw_utilities_dict_inputs(parms) :
        return(get_parms_for_input(parms,build_dict_utility_input_idList))


"""
#--------------------------------------------------------------------------
#   display the list and dict screens
#--------------------------------------------------------------------------
"""
def display_list_dict(id) :

    list_html = get_grid_list_html(id)
    
    if(id==swum.DICT_ID) :
        list_dict_form = build_dict_utility_input_form
        
    else :
        list_dict_form = build_list_utility_input_form
        
    from dfcleanser.common.html_widgets import InputForm
    list_dict_input_form    =   InputForm(list_dict_form[0],
                                          list_dict_form[1],
                                          list_dict_form[2],
                                          list_dict_form[3],
                                          list_dict_form[4],
                                          list_dict_form[5],
                                          list_dict_form[6],
                                          shortForm=False) 
      
    list_dict_input_form.set_gridwidth(700)
    list_dict_input_form.set_custombwidth(120)
    
    list_dictcustom_html = ""
    list_dictcustom_html = list_dict_input_form.get_html()
        
    if(id==swum.DICT_ID)  :
        list_title_html =   "<div>" + build_dict_utility_input_title + "</div><br></br>"
    else : 
        list_title_html =   "<div>" + build_list_utility_input_title + "</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [list_title_html,list_html,list_dictcustom_html]
    
    print("\n")
    display_generic_grid("sw-utils-wrapper",gridclasses,gridhtmls)



#Red     = "#FAA78F"
#Green   = "#8FFAC0"
#Yellow  = "#FAFB95"

"""
#--------------------------------------------------------------------------
#   get the dict or list tables
#--------------------------------------------------------------------------
"""
def get_grid_list_html(id) :
    
    grid_tablelistHeader    =   [""]
    grid_tablelistRows      =   []
    grid_tablelistWidths    =   [100]
    grid_tablelistAligns    =   ["left"]
    grid_tablelistHrefs     =   []
        
    colorList               =   []
        
    rowslist    =   []
        
    if(id == swum.DICT_ID) :
        from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
        dictlog = get_Dictlog()
        if(not (dictlog == None)) :
            dictlogkeys = list(dictlog)
            for i in range(len(dictlogkeys)) :
                rowslist.append(dictlogkeys[i])
                colorRow = []
                found = False
                    
                for j in range(len(swum.ReservedDicts)) :
                    if(dictlogkeys[i] == swum.ReservedDicts[j]) :
                        found = True
                            
                if(found) :
                    colorRow.append(swum.Yellow)
                else :
                    colorRow.append(None)
                        
                colorList.append(colorRow)

    else :
        from dfcleanser.sw_utilities.sw_utility_control import get_Listlog
        listlog = get_Listlog()
        if(not (listlog == None)) :
            listlogkeys = list(listlog)
            for i in range(len(listlogkeys)) :
                rowslist.append(listlogkeys[i])
                colorRow = []
                found = False
                    
                for j in range(len(swum.ReservedLists)) :
                    if(listlogkeys[i] == swum.ReservedLists[j]) :
                        found = True
                            
                if(found) :        
                    colorRow.append(swum.Yellow)
                else :
                    colorRow.append(None)
                        
                colorList.append(colorRow)
    
    for i in range(len(rowslist)) :
        grid_tablelistrow = [rowslist[i]]
        grid_tablelistRows.append(grid_tablelistrow)
        if(id == swum.DICT_ID) :
            grid_tablelistHrefs.append(["select_dict"])
        else :
            grid_tablelistHrefs.append(["select_list"])
    
    grid_table = None
                
    if(id == swum.DICT_ID) :
        grid_table = dcTable("Dicts","dictnamesTable","grid_table",
                             grid_tablelistHeader,grid_tablelistRows,
                             grid_tablelistWidths,grid_tablelistAligns)
    else :
        grid_table = dcTable("Lists","listnamesTable","grid_table",
                             grid_tablelistHeader,grid_tablelistRows,
                             grid_tablelistWidths,grid_tablelistAligns)
    
    grid_table.set_refList(grid_tablelistHrefs)
    
    grid_table.set_rowspertable(len(rowslist))
    grid_table.set_small(True)
    grid_table.set_smallwidth(90)
    grid_table.set_smallmargin(10)

    grid_table.set_border(True)
    grid_table.set_checkLength(True)
    grid_table.set_textLength(30)
    grid_table.set_html_only(True) 
        
    grid_table.set_color(True)
    grid_table.set_colorList(colorList)
        
    grid_table.set_tabletype(ROW_MAJOR)
    grid_table.set_rowspertable(10)

    listHtml = get_row_major_table(grid_table,SCROLL_DOWN,False)
    
    return(listHtml)


"""
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#                       Generic Functions
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
"""


def get_genfunc_input_parms(parms) :
    return(get_parms_for_input(parms,gen_function_input_idList))


def display_generic_function_inputs(ftitle,notes = False) :
    
    if(not(ftitle is None)) :
        
        cfg.set_config_value(cfg.CURRENT_GENERIC_FUNCTION,ftitle)
        gt_func = swgm.get_generic_function(ftitle)

        if(not (gt_func == None)) :
            
            #if(type(gt_func) == str) :
            #    fparms = [swgm.reservedfunctionsmodule,
            #              ftitle,
            #              gt_func]
                
            fparms = [gt_func.get_func_module(),
                      gt_func.get_func_title(),
                      gt_func.get_func_code()]
            
        else :
            
            fparms = [swgm.reservedfunctionsmodule,
                      ftitle,
                      swgm.get_df_function_source(ftitle,False)]
                
        cfg.set_config_value(gen_function_input_id+"Parms",fparms)
    
    display_generic_functions()
    print("\n")


def get_genfunc_list() :
    
    if(swgf.get_total_generic_functions() == 0) :
        return(None)
    else :
        gtfuncs = swgf.get_generic_functions_names_list()
        gtfuncs.sort()
        return(gtfuncs)


"""
#------------------------------------------------------------------
#   get the generic functions table
#------------------------------------------------------------------
"""
def get_genfunc_html(forfunc=swum.FOR_GEN_FUNC) :

    genTranslistHeader      =   [""]
    genTranslistRows        =   []
    genTranslistWidths      =   [100]
    genTranslistAligns      =   ["left"]
    genTranslistHrefs       =   []

    colorList               =   []
    
    if(swgm.get_total_generic_functions() == 0) :
        genTranslistRows.append(["No Generic Functions"])
    else :

        gtfuncs = swgm.get_generic_functions_names_list()
        gtfuncs.sort()

        for i in range(len(gtfuncs)) :
            
            genTranslistRows.append([gtfuncs[i]])

            if(forfunc==swum.FOR_ADD_COLUMNS) :
                genTranslistHrefs.append(["select_addcol_gen_function"])
            elif(forfunc==swum.FOR_APPLY_FN) :
                genTranslistHrefs.append(["select_applyfn_gen_function"])
            else :
                genTranslistHrefs.append(["select_gen_function"])
                
            colorRow = []
            found = False
              
            if(gtfuncs[i] in swgm.reservedfunctions) :
                found = True

            if(found) :
                colorRow.append(swum.Yellow)
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
    
    if(not (forfunc == swum.FOR_APPLY_FN)) :
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
    
    #gt_table.dump()
    listHtml = get_row_major_table(gt_table,SCROLL_DOWN,False)
    
    return(listHtml)


"""
#------------------------------------------------------------------
#   get the generic functions table
#------------------------------------------------------------------
"""
def get_genfunc_types_html() :

    genfunctypesHeader      =   [None,None]
    genfunctypesRows        =   []
    genfunctypesWidths      =   [30,70]
    genfunctypesAligns      =   ["left","left"]

    colorList               =   []

    crow        =   ["","reserved function"]
    colorRow    =   [swum.Yellow,None]
    genfunctypesRows.append(crow)
    colorList.append(colorRow)
    
    gt_table = dcTable(None,"gftypes",
                       cfg.GenFunction_ID,
                       genfunctypesHeader,genfunctypesRows,
                       genfunctypesWidths,genfunctypesAligns)
    
    
    gt_table.set_small(True)
    gt_table.set_smallwidth(95)
    gt_table.set_smallmargin(5)
    gt_table.set_border(False)
    
    #gt_table.set_table_column_parms({"font":12})
    gt_table.set_checkLength(True)
    gt_table.set_textLength(32)
    
    gt_table.set_html_only(True) 
    
    gt_table.set_color(True)
    gt_table.set_colorList(colorList)
    gt_table.set_rowspertable(2)
        
    #gt_table.dump()
    listHtml = gt_table.get_html()

    return(listHtml)




        
def get_genfunc_module(ftitle) :
    
    if(ftitle in swum.reservedfunctions) :
        return(swum.reservedfunctionsmodule) 
    else :
        gt_func     =   swgf.get_generic_function(ftitle)
        
        if(not (gt_func is None)) :
            return(gt_func.get_func_module()) 
        else :
            return("None")


"""
#------------------------------------------------------------------
#   display the generic transforms
#------------------------------------------------------------------
"""
def display_generic_functions(forAddColumn=False):

    gtlistHtml      =   get_genfunc_html()
    gftypes_html    =   get_genfunc_types_html()
    
    ftitle  =  cfg.get_config_value(cfg.CURRENT_GENERIC_FUNCTION) 

    if(not (ftitle is None)) :

        code        =   swgm.get_generic_function(ftitle)
        
        if(not(code is None)) :
            if(not (type(code) == str)) :
                code    =   code.get_func_code()
                fmodule     =   get_genfunc_module(ftitle)
            else :
                fmodule     =   swum.reservedfunctionsmodule
                
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
    gt_input_form.set_custombwidth(120)
    
    gt_input_html = ""
    gt_input_html = gt_input_form.get_html()
    
    cfg.drop_config_value(gen_function_input_id+"Parms")
        
    gt_heading_html =   "<div>" + gen_function_input_title + "</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-bottom","dfc-right"]
    gridhtmls       =   [gt_heading_html,gtlistHtml,gftypes_html,gt_input_html]
    
    print("\n")
    display_generic_grid("sw-utils-wrapper",gridclasses,gridhtmls)






