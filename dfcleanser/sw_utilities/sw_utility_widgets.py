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
import dfcleanser.common.help_utils as dfchelp
from dfcleanser.common.html_widgets import (display_composite_form, maketextarea,
                                            get_html_spaces, get_button_tb_form, ButtonGroupForm)

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

from dfcleanser.common.common_utils import (display_grid, get_parms_for_input)

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

build_utility_tb_keyTitleList     =   ["Lists","Dicts","Clear","Help"]

build_utility_tb_jsList           =   ["build_utility_callback("+str(swum.LIST_OPTION)+")",
                                       "build_utility_callback("+str(swum.DICT_OPTION)+")",
                                       "build_utility_clear_callback()",
                                       "displayhelp(" + str(dfchelp.LIST_UTILITY_MAIN_TASKBAR_ID) + ")"]

build_utility_tb_centered         =   False

"""
#--------------------------------------------------------------------------
#    build list utility input 
#--------------------------------------------------------------------------
"""
build_list_utility_input_title          =   "Build List Utility"
build_list_utility_input_id             =   "buildlistparms"
build_list_utility_input_idList         =   ["startlistfile","listname","listitems",
                                             None,None,None,None,None]

build_list_utility_input_labelList      =   ["list_file_to_start_With",
                                             "list_name",
                                             "list_value(s)",
                                             "Delete</br>From</br>Lists",
                                             "Save</br> To </br>Lists",
                                             "Clear","Return","Help"]

build_list_utility_input_typeList       =   ["file","text",maketextarea(10),
                                             "button","button",
                                             "button","button","button"]

build_list_utility_input_placeholderList = ["select file to start with (default None)",
                                            "enter list name in 'Notebook' lists (default None)",
                                            "enter new list value(s) example (&#39;1&#39;, 2, a, &#39;b&#39;, [3,4] ...)",
                                            None,None,None,None,None]

build_list_utility_input_jsList         =    [None,None,None,
                                              "sw_utilities_delete_callback("+str(swum.DELETE_LIST_OPTION)+")",
                                              "sw_utilities_list_add_callback()",
                                              "build_utility_callback("+str(swum.LIST_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp(" + str(dfchelp.LIST_UTILITY_BUILD_LIST_ID) + ")"]

build_list_utility_input_reqList        =   [0,1,2]

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
build_dict_utility_input_idList         =   ["startdictfile",
                                             "dictname",
                                             "dictpairs",
                                             None,None,None,None,None]

build_dict_utility_input_labelList      =   ["dict_file_to_start_With",
                                             "dict_name",
                                             "dict_values",
                                             "Delete</br>From</br>Dicts",
                                             "Save</br> To </br>Dicts",
                                             "Clear","Return","Help"]

build_dict_utility_input_typeList       =   ["file","text",maketextarea(10),
                                             "button","button",
                                             "button","button","button"]

build_dict_utility_input_placeholderList = ["select file to start with (default None)",
                                            "enter dict name in 'Notebook' dicts (default None)",
                                            "enter new dict pairs(s) (&#39;&#39;{key:value}&#39;&#39;,&#39;&#39;.....{key:value})",
                                            None,None,None,None,None]

build_dict_utility_input_jsList         =    [None,None,None,
                                              "sw_utilities_delete_callback("+str(swum.DELETE_DICT_OPTION)+")",
                                              "sw_utilities_dict_add_callback()",
                                              "build_utility_callback("+str(swum.DICT_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp(" + str(dfchelp.LIST_UTILITY_BUILD_DICT_ID) + ")"]

build_dict_utility_input_reqList        =   [0,1,2]

build_dict_utility_input_form           =   [build_dict_utility_input_id,
                                             build_dict_utility_input_idList,
                                             build_dict_utility_input_labelList,
                                             build_dict_utility_input_typeList,
                                             build_dict_utility_input_placeholderList,
                                             build_dict_utility_input_jsList,
                                             build_dict_utility_input_reqList]  


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   SW Utilities display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_sw_utilities_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(build_utility_tb_id,
                                                               build_utility_tb_keyTitleList,
                                                               build_utility_tb_jsList,
                                                               build_utility_tb_centered))])

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
      
    list_dict_input_form.set_gridwidth(660)

    list_dictcustom_html = ""
    list_dictcustom_html = list_dict_input_form.get_html()
        
    if(id==swum.DICT_ID)  :
        list_title_html = "<p class='grid_title'>" + get_html_spaces(1) + build_dict_utility_input_title + "</p>"
        wrapper = "dict_table_wrapper"
    else :   
        list_title_html = "<p class='grid_title'>" + get_html_spaces(1) + build_list_utility_input_title + "</p>"
        wrapper = "list_table_wrapper"

    display_grid(wrapper,
                 list_title_html,
                 list_html,
                 list_dictcustom_html,
                 None)


Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#FAFB95"

"""
#--------------------------------------------------------------------------
#   get the grid list tables
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
                        colorRow.append(Yellow)
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
                        colorRow.append(Yellow)
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
        grid_table.set_textLength(20)
        grid_table.set_html_only(True) 
        
        grid_table.set_color(True)
        grid_table.set_colorList(colorList)
        
        grid_table.set_tabletype(ROW_MAJOR)
        grid_table.set_rowspertable(10)

        listHtml = get_row_major_table(grid_table,SCROLL_NEXT,False)
    
        return(listHtml)




