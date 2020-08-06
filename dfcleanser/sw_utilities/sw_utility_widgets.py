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
#import dfcleanser.sw_utilities.sw_utility_control as swuc

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
#import dfcleanser.sw_utilities.sw_utility_genfunc_functions as swgf
#import dfcleanser.sw_utilities.sw_utility_genfunc_model as swgm


from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm)
from dfcleanser.common.common_utils import (display_generic_grid, get_parms_for_input, opStatus, display_exception)
from dfcleanser.common.cfg import add_error_to_log



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

build_utility_tb_keyTitleList     =   ["Lists","Dicts","dfc Funcs","Clear","Reset","Help"]

build_utility_tb_jsList           =   ["build_utility_callback("+str(swum.LIST_OPTION)+")",
                                       "build_utility_callback("+str(swum.DICT_OPTION)+")",
                                       "build_utility_callback("+str(swum.FUNCS_OPTION)+")",
                                       "build_utility_clear_callback()",
                                       "process_pop_up_cmd(6)",
                                       "displayhelp('" + str(dfchelp.DS_UTILITY_MAIN_TASKBAR_ID) + "')"]

build_utility_tb_centered         =   True

"""
#--------------------------------------------------------------------------
#    build list utility input 
#--------------------------------------------------------------------------
"""
build_list_utility_input_title          =   "Maint List Utility"
build_list_utility_input_id             =   "buildlistparms"
build_list_utility_input_idList         =   ["buildlistname",
                                             "buildlistitems",
                                             None,None,None]

build_list_utility_input_labelList      =   ["list_name",
                                             "list_value(s)",
                                             "User Lists",
                                             "Return","Help"]

build_list_utility_input_typeList       =   ["select",maketextarea(20),
                                             "button","button","button"]

build_list_utility_input_placeholderList = ["enter list name in 'Notebook' lists (default None)",
                                            "enter new list value(s) example (&#39;1&#39;, 2, a, &#39;b&#39;, [3,4] ...)",
                                            None,None,None]

build_list_utility_input_jsList         =    [None,None,
                                              "build_utility_callback(" + str(swum.MAINT_LIST_OPTION) + ")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_LIST_UTILITY_ID) + "')"]

build_list_utility_input_reqList        =   [0,1]

build_list_utility_input_form           =   [build_list_utility_input_id,
                                             build_list_utility_input_idList,
                                             build_list_utility_input_labelList,
                                             build_list_utility_input_typeList,
                                             build_list_utility_input_placeholderList,
                                             build_list_utility_input_jsList,
                                             build_list_utility_input_reqList]  


maint_list_utility_input_title          =   "Maint List Utility"
maint_list_utility_input_id             =   "maintlistparms"
maint_list_utility_input_idList         =   ["maintlistname",
                                             "maintnewlistname",
                                             "maintlistitems",
                                             "maintstartlistfile",
                                             None,None,None,None,None,None,None]

maint_list_utility_input_labelList      =   ["user_list_name",
                                             "new_user_list_name",
                                             "user_list_value(s)",
                                             "user_list_file_to_load_user_list_values(s)_from",
                                             "Load</br>From</br>File",
                                             "Delete</br>User</br>List",
                                             "Update</br>User</br>List",
                                             "Add</br>User</br>List",
                                             "Clear","Return","Help"]

maint_list_utility_input_typeList       =   ["select","text",maketextarea(20),"file",
                                             "button","button","button","button",
                                             "button","button","button"]

maint_list_utility_input_placeholderList = ["enter list name in 'Notebook' lists (default None)",
                                            "enter new user list name ",
                                            "enter new user list value(s) example ( [3,4] ...)",
                                            "select file to load from (default None)",
                                            None,None,None,None,None,None,None]

maint_list_utility_input_jsList         =    [None,None,None,None,
                                              "build_utility_callback("+str(swum.LOAD_LIST_OPTION)+")",
                                              "build_utility_callback("+str(swum.DELETE_LIST_OPTION)+")",
                                              "build_utility_callback("+str(swum.UPDATE_LIST_OPTION)+")",
                                              "build_utility_callback("+str(swum.ADD_LIST_OPTION)+")",
                                              "build_utility_callback("+str(swum.CLEAR_LIST_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_LIST_UTILITY_USER_ID) + "')"]

maint_list_utility_input_reqList        =   [0,1,2]


maint_list_file_utility_input_form      =   [maint_list_utility_input_id,
                                             maint_list_utility_input_idList,
                                             maint_list_utility_input_labelList,
                                             maint_list_utility_input_typeList,
                                             maint_list_utility_input_placeholderList,
                                             maint_list_utility_input_jsList,
                                             maint_list_utility_input_reqList]  

maint_list_file_utility_input_title     =   "Maint List Utility"
maint_list_file_utility_input_id        =   "maintlistparms"
maint_list_file_utility_input_idList    =   ["maintlistname",
                                             "maintnewlistname",
                                             "maintlistitems",
                                             "maintstartlistfile",
                                             None,None,None]

maint_list_file_utility_input_labelList =   ["user_list_name",
                                             "new_user_list_name",
                                             "user_list_value(s)",
                                             "user_list_file_to_load_user_list_values(s)_from",
                                             "Add</br>User</br>List",
                                             "Return","Help"]

maint_list_file_utility_input_typeList  =   ["select","text",maketextarea(20),"file",
                                             "button","button","button"]

maint_list_file_utility_input_placeholderList = ["enter list name in 'Notebook' lists (default None)",
                                                 "enter new user list name ",
                                                 "enter new user list value(s) example ( [3,4] ...)",
                                                 "select file to load from (default None)",
                                                 None,None,None]

maint_list_file_utility_input_jsList    =    [None,None,None,None,
                                              "build_utility_callback("+str(swum.ADD_LIST_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_LIST_UTILITY_USER_ID) + "')"]

maint_list_file_utility_input_reqList   =   [0,1,2]

"""
#--------------------------------------------------------------------------
#    build dict utility input 
#--------------------------------------------------------------------------
"""
build_dict_utility_input_title          =   "Build Dict Utility"
build_dict_utility_input_id             =   "builddictparms"
build_dict_utility_input_idList         =   ["builddictname",
                                             "builddictpairs",
                                             None,None,None]

build_dict_utility_input_labelList      =   ["dict_name",
                                             "dict_values",
                                             "User</br>Dicts",
                                             "Return","Help"]

build_dict_utility_input_typeList       =   ["select",maketextarea(20),
                                             "button","button","button"]

build_dict_utility_input_placeholderList = ["enter dict name in 'Notebook' dicts (default None)",
                                            "enter new dict pairs(s) (&#39;&#39;{key:value}&#39;&#39;,&#39;&#39;.....{key:value})",
                                            None,None,None]

build_dict_utility_input_jsList         =    [None,None,
                                              "build_utility_callback(" + str(swum.MAINT_DICT_OPTION) + ")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_DICT_UTILITY_ID) + "')"]

build_dict_utility_input_reqList        =   [0,1]

build_dict_utility_input_form           =   [build_dict_utility_input_id,
                                             build_dict_utility_input_idList,
                                             build_dict_utility_input_labelList,
                                             build_dict_utility_input_typeList,
                                             build_dict_utility_input_placeholderList,
                                             build_dict_utility_input_jsList,
                                             build_dict_utility_input_reqList]  



maint_dict_utility_input_title          =   "Maint Dict Utility"
maint_dict_utility_input_id             =   "maintdictparms"
maint_dict_utility_input_idList         =   ["maintdictname",
                                             "maintnewdictname",
                                             "maintdictitems",
                                             "maintstartdictfile",
                                             None,None,None,None,None,None,None]

maint_dict_utility_input_labelList      =   ["user_dict_name",
                                             "new_user_dict_name",
                                             "user_dict_value(s)",
                                             "user_dict_file_to_load_user_dict_values(s)_from",
                                             "Load</br>From</br>File",
                                             "Delete</br>User</br>Dict",
                                             "Update</br>User</br>Dict",
                                             "Add</br>User</br>Dict",
                                             "Clear","Return","Help"]

maint_dict_utility_input_typeList       =   ["select","text",maketextarea(20),"file",
                                             "button","button","button","button",
                                             "button","button","button"]

maint_dict_utility_input_placeholderList = ["enter dict name in 'Notebook' lists (default None)",
                                            "enter new user dict name ",
                                            "enter new dict pairs(s) (&#39;&#39;{key:value}&#39;&#39;,&#39;&#39;.....{key:value})",
                                            "select file to start with (default None)",
                                            None,None,None,None,None,None,None]

maint_dict_utility_input_jsList         =    [None,None,None,None,
                                              "build_utility_callback("+str(swum.LOAD_DICT_OPTION)+")",
                                              "build_utility_callback("+str(swum.DELETE_DICT_OPTION)+")",
                                              "build_utility_callback("+str(swum.UPDATE_DICT_OPTION)+")",
                                              "build_utility_callback("+str(swum.ADD_DICT_OPTION)+")",
                                              "build_utility_callback("+str(swum.CLEAR_DICT_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_LIST_UTILITY_USER_ID) + "')"]

maint_dict_utility_input_reqList        =   [0,1,2]

maint_dict_utility_input_form           =   [maint_dict_utility_input_id,
                                             maint_dict_utility_input_idList,
                                             maint_dict_utility_input_labelList,
                                             maint_dict_utility_input_typeList,
                                             maint_dict_utility_input_placeholderList,
                                             maint_dict_utility_input_jsList,
                                             maint_dict_utility_input_reqList]  



maint_dict_file_utility_input_title     =   "Maint Dict Utility"
maint_dict_file_utility_input_id        =   "maintdictparms"
maint_dict_file_utility_input_idList    =   ["maintdictname",
                                             "maintnewdictname",
                                             "maintdictitems",
                                             "maintstartdictfile",
                                             None,None,None]

maint_dict_file_utility_input_labelList =   ["user_dict_name",
                                             "new_user_dict_name",
                                             "user_dict_value(s)",
                                             "user_dict_file_to_load_user_dict_values(s)_from",
                                             "Add</br>User</br>Dict",
                                             "Return","Help"]

maint_dict_file_utility_input_typeList  =   ["select","text",maketextarea(20),"file",
                                             "button","button","button"]

maint_dict_file_utility_input_placeholderList = ["enter dict name in 'Notebook' lists (default None)",
                                                 "enter new user dict name ",
                                                 "enter new dict pairs(s) (&#39;&#39;{key:value}&#39;&#39;,&#39;&#39;.....{key:value})",
                                                 "select file to start with (default None)",
                                                 None,None,None]

maint_dict_file_utility_input_jsList    =    [None,None,None,None,
                                              "build_utility_callback("+str(swum.ADD_DICT_OPTION)+")",
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_LIST_UTILITY_USER_ID) + "')"]

maint_dict_file_utility_input_reqList        =   [0,1,2]




"""
#--------------------------------------------------------------------------
#    build funcs utility input 
#--------------------------------------------------------------------------
"""
build_funcs_utility_input_title          =   "Show funcs Utility"
build_funcs_utility_input_id             =   "showduncsparms"
build_funcs_utility_input_idList         =   ["funcname",
                                             "funcmodule",
                                             "funccode",
                                             None,None]

build_funcs_utility_input_labelList      =   ["function_name",
                                             "function_module",
                                             "function_code",
                                             "Return","Help"]

build_funcs_utility_input_typeList       =   ["select","text",maketextarea(20),
                                             "button","button"]

build_funcs_utility_input_placeholderList = ["select function name",
                                            "function module",
                                            "function code",
                                            None,None]

build_funcs_utility_input_jsList         =    [None,None,None,
                                              "build_utility_clear_callback()",
                                              "displayhelp('" + str(dfchelp.DS_FN_UTILITY_ID) + "')"]

build_funcs_utility_input_reqList        =   [0,1,2]

SWUtility_inputs                        =   [build_list_utility_input_id, build_dict_utility_input_id, build_funcs_utility_input_id]



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
        return(get_parms_for_input(parms,maint_list_utility_input_idList))


def get_sw_utilities_dict_inputs(parms) :
        return(get_parms_for_input(parms,maint_dict_utility_input_idList))


"""
#--------------------------------------------------------------------------
#   display the list and dict screens
#--------------------------------------------------------------------------
"""
def display_list_dict(stype,keyValue=None) :
    """
    * ------------------------------------------------------------------------
    * function : display the dict or list start form
    * 
    * parms :
    *  id         - list or dict
    *  keyValue   - dict or list name
    *
    * -------------------------------------------------------------------------
    """
    
    #print("display_list_dict",stype,keyValue)
    
    if(stype==swum.DICT_ID) :
        list_dict_form = build_dict_utility_input_form
        
    else :
        list_dict_form = build_list_utility_input_form
        
    list_dict_input_form    =   InputForm(list_dict_form[0],
                                          list_dict_form[1],
                                          list_dict_form[2],
                                          list_dict_form[3],
                                          list_dict_form[4],
                                          list_dict_form[5],
                                          list_dict_form[6]) 
    
    selectDicts     =   []  
    
    if(stype==swum.DICT_ID) :
        
        
        from dfcleanser.sw_utilities.sw_utility_model import get_dicts_names, DFC_CREATED
        dict_names  =   get_dicts_names(DFC_CREATED)
        
        if(keyValue is None) :
            def_dict    =   dict_names[0]
        else :
            def_dict    =   keyValue
        #print("def_dict",def_dict,keyValue)
            
        dictssel    =   {"default":def_dict,"list": dict_names, "callback":"select_dict"}
        seldict     =   swum.get_Dict(def_dict,DFC_CREATED)
        
        keys = list(seldict.keys())
        if( (def_dict == "Country_Codes") or (def_dict == "Language_Codes") ):
            keys.sort()

        seldict    =   swum.get_pretty_dict(seldict,keys)
        
    else :
        
        from dfcleanser.sw_utilities.sw_utility_model import get_lists_names, DFC_CREATED
        list_names  =   get_lists_names(DFC_CREATED)
        
        if(keyValue is None) :
            def_list    =   list_names[0]
        else :
            def_list    =   keyValue

        dictssel    =   {"default":def_list,"list": list_names, "callback":"select_list"}
        sellist     =   str(swum.get_List(def_list,DFC_CREATED))
        
    selectDicts.append(dictssel)
    
    from dfcleanser.common.common_utils import get_select_defaults
        
    get_select_defaults(list_dict_input_form,
                        list_dict_form[0],
                        list_dict_form[1],
                        list_dict_form[3],
                        selectDicts)
        
    list_dict_input_form.set_gridwidth(700)
    list_dict_input_form.set_custombwidth(120)
    list_dict_input_form.set_fullparms(True)
    
    if(stype==swum.DICT_ID) :
        
        selparms = [def_dict, seldict]
        cfg.set_config_value(build_dict_utility_input_id+"Parms",selparms)
        cfg.set_config_value(build_dict_utility_input_id+"ParmsProtect",[False,True])
        
        help_note           =   "To retrieve a dict in python from dfcleanser.sw_utiliities.sw_utility.model call 'get_Dict(dictname)'.</br>To add a dict in python from dfcleanser.sw_utiliities.sw_utility.model call 'add_Dict(dictname,newdict)'"
        
        
    else :
    
        selparms = [def_list,sellist]
        cfg.set_config_value(build_list_utility_input_id+"Parms",selparms)
        cfg.set_config_value(build_list_utility_input_id+"ParmsProtect",[False,True])
        
        help_note           =   "To retrieve a list in python from dfcleanser.sw_utiliities.sw_utility.model call 'get_List(listname)'.</br>To add a list in python from dfcleanser.sw_utiliities.sw_utility.model call 'add_List(listtname,newlist)'"
        
    from dfcleanser.common.common_utils import get_help_note_html
    listdict_notes_html   =   get_help_note_html(help_note,100,None,None)
    
    
    list_dictcustom_html = ""
    list_dictcustom_html = list_dict_input_form.get_html()
    
    if(stype==swum.DICT_ID)  :
        list_title_html =   "<div>dfc Dicts</div><br></br>"
        cfg.drop_config_value(build_dict_utility_input_id+"Parms")
        
    else : 
        list_title_html =   "<div>dfc Lists</div><br></br>"
        cfg.drop_config_value(build_list_utility_input_id+"Parms")
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
    gridhtmls       =   [list_title_html,list_dictcustom_html,listdict_notes_html]
    
    print("\n")
    display_generic_grid("sw-utils-listdict-wrapper",gridclasses,gridhtmls)


def display_funcs() :
    """
    * ------------------------------------------------------------------------
    * function : display the dfc funcs start form
    * 
    * parms :
    *
    * -------------------------------------------------------------------------
    """
    
    list_funcs_input_form   =   InputForm(build_funcs_utility_input_id,
                                          build_funcs_utility_input_idList,
                                          build_funcs_utility_input_labelList,
                                          build_funcs_utility_input_typeList,
                                          build_funcs_utility_input_placeholderList,
                                          build_funcs_utility_input_jsList,
                                          build_funcs_utility_input_reqList) 
    
    selectDicts     =   []  
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_genfunc_list
    gen_funcs       =   get_genfunc_list()
    default_func    =   gen_funcs[0]
    
    funcssel    =   {"default":default_func,"list": gen_funcs, "callback":"select_gen_func"}
    selectDicts.append(funcssel)
    
    from dfcleanser.common.common_utils import get_select_defaults
        
    get_select_defaults(list_funcs_input_form,
                        build_funcs_utility_input_id,
                        build_funcs_utility_input_idList,
                        build_funcs_utility_input_typeList,
                        selectDicts)
        
    list_funcs_input_form.set_gridwidth(700)
    list_funcs_input_form.set_custombwidth(120)
    list_funcs_input_form.set_fullparms(True)
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_generic_function_code
    func_code   =   get_generic_function_code(default_func)
    
    cfg.set_config_value(build_funcs_utility_input_id+"Parms",[default_func,reservedfunctionsmodule,func_code])
    cfg.set_config_value(build_funcs_utility_input_id+"ParmsProtect",[False,True,True])
        
    help_note   =   "Generic functions help note'"
        
    from dfcleanser.common.common_utils import get_help_note_html
    list_funcs_notes_html   =   get_help_note_html(help_note,100,None,None)
    
    list_funcs_html         =   ""
    list_funcs_html         =   list_funcs_input_form.get_html()
    
    list_funcs_title_html   =   "<div>Generic dfc Functions</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
    gridhtmls       =   [list_funcs_title_html,list_funcs_html,list_funcs_notes_html]
    
    print("\n")
    display_generic_grid("sw-utils-listdict-wrapper",gridclasses,gridhtmls)


def display_dict_maint(keyValue=None,loadfile=None) :
    """
    * ------------------------------------------------------------------------
    * function : display the user dicts maintenance form
    * 
    * parms :
    *  keyValue   - dict name
    *
    * -------------------------------------------------------------------------
    """
    #print("display_dict_maint",keyValue,loadfile)
    
    opstat  =   opStatus()
    
    if(loadfile is None) :
        
        dict_maint_input_form   =   InputForm(maint_dict_utility_input_id,
                                              maint_dict_utility_input_idList,
                                              maint_dict_utility_input_labelList,
                                              maint_dict_utility_input_typeList,
                                              maint_dict_utility_input_placeholderList,
                                              maint_dict_utility_input_jsList,
                                              maint_dict_utility_input_reqList) 
        
    else :
        
        dict_maint_input_form   =   InputForm(maint_dict_file_utility_input_id,
                                              maint_dict_file_utility_input_idList,
                                              maint_dict_file_utility_input_labelList,
                                              maint_dict_file_utility_input_typeList,
                                              maint_dict_file_utility_input_placeholderList,
                                              maint_dict_file_utility_input_jsList,
                                              maint_dict_file_utility_input_reqList) 
        
    selectDicts     =   []  

    from dfcleanser.sw_utilities.sw_utility_model import get_dicts_names, USER_CREATED
    dict_names  =   get_dicts_names(USER_CREATED)
    
    #print("dict_names",dict_names)
    if(not (dict_names is None)) :
        
        if(keyValue is None) :
            def_dict    =   dict_names[0]
        else :
            def_dict    =   keyValue
            
        seldict     =   swum.get_Dict(def_dict,USER_CREATED)
        
        keys = list(seldict.keys())
        if( (def_dict == "Country_Codes") or (def_dict == "Language_Codes") ):
            keys.sort()

        seldict    =   swum.get_pretty_dict(seldict,keys)
            
    else :
        dict_names  =   ["No User dicts defined"]
        def_dict    =   "No User dicts defined"
        
        seldict     =   "User defined dict"
            
    dictssel    =   {"default":def_dict,"list": dict_names, "callback":"select_dict"}
    selectDicts.append(dictssel)
    
    from dfcleanser.common.common_utils import get_select_defaults
        
    get_select_defaults(dict_maint_input_form,
                        maint_dict_utility_input_id,
                        maint_dict_utility_input_idList,
                        maint_dict_utility_input_typeList,
                        selectDicts)
    
    dict_maint_input_form.set_gridwidth(700)
    #dict_maint_input_form.set_custombwidth(110)
    if(loadfile is None) :
        dict_maint_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":20})
    else :
        dict_maint_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":205})
     
    dict_maint_input_form.set_fullparms(True)
    
    cfg.drop_config_value(maint_dict_utility_input_id+"Parms")
    cfg.drop_config_value(maint_dict_utility_input_id+"ParmsProtect")
    
    if(not (loadfile is None)) :
        
        import json
        
        #from dfcleanser.common.common_utils import does_file_exist
        #print("does_file_exist",does_file_exist(loadfile))
        
        try :                
            with open(loadfile, 'r') as ds_file :
                ds = json.load(ds_file)
                ds_file.close()
                    
                keys = list(ds.keys()) 
                seldict    =   swum.get_pretty_dict(ds,keys)
                
                #print(seldict)
                    
        except Exception as e:
            opstat.set_errorMsg("invalid user file to load " + loadfile)
            opstat.set_exception(e)
    
    
    if(opstat.get_status()) :
    
        if(loadfile is None) :
            cfg.set_config_value(maint_dict_utility_input_id+"Parms",[def_dict,"",seldict,""])
        else :
            cfg.set_config_value(maint_dict_utility_input_id+"Parms",[def_dict,"",seldict,loadfile])
            cfg.set_config_value(maint_dict_utility_input_id+"ParmsProtect",[True,False,True,True])
        
        
        help_note   =   "To add a user dict enter parms and values above and click on 'Add User Dict'.</br>To update the current dict change values and click on 'Update User Dict'"
        
        from dfcleanser.common.common_utils import get_help_note_html
        dict_maint_notes_html   =   get_help_note_html(help_note,80,75,None)
    
        dict_maint_html         =   "Fill in new user dict parms or update currently displayed user dict."
        dict_maint_html         =   dict_maint_input_form.get_html()
    
        dict_maint_title_html   =   "<div>User Dicts</div><br></br>"
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
        gridhtmls       =   [dict_maint_title_html,dict_maint_html,dict_maint_notes_html]
    
        #print(dict_maint_html)
        #print(dict_maint_notes_html)
        print("\n")
        display_generic_grid("sw-utils-listdict-wrapper",gridclasses,gridhtmls)
        
    else :
        
        display_exception(opstat)
        add_error_to_log("[Get User Dict from File] " + loadfile + str(sys.exc_info()[0].__name__))
        


def display_list_maint(keyValue=None,loadfile=None) :
    """
    * ------------------------------------------------------------------------
    * function : display the user lists maintenance form
    * 
    * parms :
    *  keyValue   - list name
    *
    * -------------------------------------------------------------------------
    """
    opstat  =   opStatus()
    
    if(loadfile is None) :
        
    
        list_maint_input_form   =   InputForm(maint_list_utility_input_id,
                                              maint_list_utility_input_idList,
                                              maint_list_utility_input_labelList,
                                              maint_list_utility_input_typeList,
                                              maint_list_utility_input_placeholderList,
                                              maint_list_utility_input_jsList,
                                              maint_list_utility_input_reqList) 
        
    else :
        
        list_maint_input_form   =   InputForm(maint_list_file_utility_input_id,
                                              maint_list_file_utility_input_idList,
                                              maint_list_file_utility_input_labelList,
                                              maint_list_file_utility_input_typeList,
                                              maint_list_file_utility_input_placeholderList,
                                              maint_list_file_utility_input_jsList,
                                              maint_list_file_utility_input_reqList) 
        
    
    selectDicts     =   []  
    
    from dfcleanser.sw_utilities.sw_utility_model import get_lists_names, USER_CREATED
    list_names  =   get_lists_names(USER_CREATED)
    
    #print("list_names",list_names)
    if(not (list_names is None)) :
        
        if(keyValue is None) :
            def_list    =   list_names[0]
        else :
            def_list    =   keyValue
            
        sellist     =   swum.get_List(def_list,USER_CREATED)
        
        dsstr   =   "["
        for i in range(len(sellist)) :
            dsstr   =   dsstr + str(sellist[i])
            if(i == (len(sellist) - 1))  :
                dsstr   =   dsstr + "]" 
            else :
                dsstr   =   dsstr + ","
        
        
    else :
        list_names  =   ["No User lists defined"]
        def_list    =   "No User lists defined"
        
        sellist     =   "User defined list"
            
    listssel    =   {"default":def_list,"list": list_names, "callback":"select_list"}
    selectDicts.append(listssel)
    
    from dfcleanser.common.common_utils import get_select_defaults
        
    get_select_defaults(list_maint_input_form,
                        maint_list_utility_input_id,
                        maint_list_utility_input_idList,
                        maint_list_utility_input_typeList,
                        selectDicts)
        
    list_maint_input_form.set_gridwidth(700)
    
    if(loadfile is None) :
        list_maint_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":20})    
    else :
        list_maint_input_form.set_buttonstyle({"font-size":13, "height":75, "width":90, "left-margin":205})
    
    list_maint_input_form.set_fullparms(True)
    
    cfg.drop_config_value(maint_list_utility_input_id+"Parms")
    cfg.drop_config_value(maint_list_utility_input_id+"ParmsProtect")
    
    if(not (loadfile is None)) :
        
        import json
        
        from dfcleanser.common.common_utils import does_file_exist
        if(does_file_exist(loadfile)) :
            
            try :                
                with open(loadfile, 'r') as ds_file :
                    ds = json.load(ds_file)
                    ds_file.close()
                    
                dsstr   =   "["
                for i in range(len(ds)) :
                    dsstr   =   dsstr + str(ds[i])
                    if(i == (len(ds) - 1))  :
                        dsstr   =   dsstr + "]" 
                    else :
                        dsstr   =   dsstr + ","
                        
            except Exception as e:
                opstat.set_status(False)
                opstat.set_errorMsg("Error processing user file to load" + loadfile)
                opstat.set_exception(e)
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("invalid user file to load" + loadfile)

            
    if(opstat.get_status()) :
    
        if(loadfile is None) :
            cfg.set_config_value(maint_list_utility_input_id+"Parms",[def_list,"",dsstr,""])
        else :
            cfg.set_config_value(maint_list_utility_input_id+"Parms",[def_list,"",dsstr,loadfile])
            cfg.set_config_value(maint_list_utility_input_id+"ParmsProtect",[True,False,True,True])
    
        help_note   =   "To add a user list enter parms and values above and click on 'Add User List'.</br>To update the current list change values and click on 'Update User List'"
        
        from dfcleanser.common.common_utils import get_help_note_html
        list_maint_notes_html   =   get_help_note_html(help_note,80,75,None)
    
        list_maint_html         =   ""
        list_maint_html         =   list_maint_input_form.get_html()
    
        list_maint_title_html   =   "<div>User Lists</div><br></br>"
    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
        gridhtmls       =   [list_maint_title_html,list_maint_html,list_maint_notes_html]
        #print(list_maint_html)
        #print(list_maint_notes_html)
    
        print("\n")
        display_generic_grid("sw-utils-listdict-wrapper",gridclasses,gridhtmls)


    else :
        
        display_exception(opstat)
        add_error_to_log("[Get User Dict from File] " + loadfile + str(sys.exc_info()[0].__name__))




