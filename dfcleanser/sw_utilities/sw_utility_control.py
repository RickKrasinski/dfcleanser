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


import json 

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_widgets as swuw
import dfcleanser.sw_utilities.sw_utility_model as swum

from dfcleanser.common.table_widgets import (drop_owner_tables)

from dfcleanser.common.common_utils import (display_exception, opStatus, get_parms_for_input)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   SW Utiliities functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   process javascript requests
#--------------------------------------------------------------------------
"""
def process_sw_utilities(optionId,parms=None) :

    from IPython.display import clear_output
    clear_output()
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.SWUtilities_ID)) ) :
        define_inputs(cfg.SWUtilities_ID,swuw.SWUtility_inputs)

    if(not cfg.check_if_dc_init()) :
        swuw.get_sw_utilities_main_taskbar()
        clear_sw_utility_data()
        return
    
    opstat = opStatus()
    
    if (optionId == swum.MAIN_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        clear_sw_utility_data()
        return

    if (optionId == swum.LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.LIST_ID)
        return
        
    elif (optionId == swum.DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.DICT_ID)
        return
    
    elif (optionId == swum.FUNCS_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_funcs()
        return
    
    elif (optionId == swum.MAINT_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_maint()
        return
    
    elif (optionId == swum.MAINT_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_dict_maint()
        return

    elif (optionId == swum.SELECT_LIST_OPTION) :

        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.LIST_ID,parms[0])
        return

    elif (optionId == swum.SELECT_DICT_OPTION) :
        
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.DICT_ID,parms[0])
        return
    
    elif (optionId == swum.UPDATE_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.UPDATE_LIST_OPTION",parms)
        
        fparms = swuw.get_sw_utilities_list_inputs(parms)
        
        #print("fparms",fparms)
        
        #filename = fparms[2]
        listname        =   fparms[0]
        newlistname     =   None
        listvalues      =   fparms[2]
        newlistfname    =   None
        
        try :
                        
            newlist     =   json.loads(listvalues)
            swum.update_List(listname,newlist,swum.USER_CREATED)
                        
        except Exception as e :
            opstat.store_exception("user list is invalid ",e)
        
        if(opstat.get_status()) :
            swuw.display_list_dict(swum.LIST_ID)
             
        else :
            display_exception(opstat)
        
        return
        
    elif (optionId == swum.CLEAR_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.CLEAR_LIST_OPTION",parms)
        swuw.display_list_maint()
        return
        
        
    if (optionId == swum.ADD_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.ADD_LIST_OPTION",parms)
        
        fparms = swuw.get_sw_utilities_list_inputs(parms)
        
        #print("fparms",fparms)
        
        #filename = fparms[2]
        newlistname     =   fparms[1]
        newlistvalues   =   fparms[2]
        newlistfname    =   fparms[3]
        

        if(len(newlistname) > 0) :
            
            if(len(newlistvalues) > 0) :
                
                if(len(newlistfname) > 0) :
                    
                    swum.add_List(newlistname,None,swum.USER_CREATED,newlistfname)
                    
                else :
                    
                    try :
                        
                        newlist     =   json.loads(newlistvalues)
                        swum.add_Dict(newlistname,newlist,swum.USER_CREATED,None)
                        
                    except Exception as e :
                        opstat.store_exception("user list is invalid ",e)
                
            else :
                
                opstat.set_status(False)
                opstat.set_errorMsg("No list values defined")
            
            
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("No list Name Specified")

        
        if(opstat.get_status()) :
            swuw.display_list_dict(swum.LIST_ID)
             
        else :
            display_exception(opstat)
        
        return


    elif (optionId == swum.UPDATE_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        
        #print("swum.UPDATE_DICT_OPTION",parms)
        
        fparms = swuw.get_sw_utilities_dict_inputs(parms)
        
        #print("fparms",fparms)
        
        dictname        =   fparms[0]
        newdictname     =   None
        dictvalues      =   fparms[2]
        newdictfname    =   None
        
        try :
                        
            newdict     =   json.loads(dictvalues)
            swum.update_Dict(dictname,newdict,swum.USER_CREATED)
                        
        except Exception as e :
            opstat.store_exception("user dict is invalid ",e)
        
        if(opstat.get_status()) :
            swuw.display_dict_maint(dictname,None)
             
        else :
            display_exception(opstat)
        
        return
        
    elif (optionId == swum.CLEAR_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.CLEAR_DICT_OPTION",parms)
        swuw.display_dict_maint()
        return
        
    if (optionId == swum.ADD_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.ADD_DICT_OPTION",parms)
        
        fparms = swuw.get_sw_utilities_dict_inputs(parms)
        
        #print("fparms",fparms)
        
        newdictname     =   fparms[1]
        newdictvalues   =   fparms[2]
        newdictfname    =   fparms[3]

        if(len(newdictname) > 0) :
            
            if(len(newdictvalues) > 0) :
                
                if(len(newdictfname) > 0) :
                    
                    swum.add_Dict(newdictname,None,swum.USER_CREATED,newdictfname)
                    
                else :
                    
                    try :
                        
                        newdict     =   json.loads(newdictvalues)
                        swum.add_Dict(newdictname,newdict,swum.USER_CREATED,None)
                        
                    except Exception as e :
                        opstat.store_exception("user dict is invalid ",e)
                
            else :
                
                opstat.set_status(False)
                opstat.set_errorMsg("No dict values defined")
            
            
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("No Dict Name Specified")
        
        if(opstat.get_status()) :
            swuw.display_list_dict(swum.DICT_ID)
             
        else :
            display_exception(opstat)
        
        return
    
    if (optionId == swum.LOAD_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        
        #print("swum.LOAD_LIST_OPTION\n",parms)
        
        fparms  =   get_parms_for_input(parms,swuw.maint_list_utility_input_idList)
        #print("fparms",fparms)
        
        swuw.display_list_maint(None,fparms[3])
        
        return
    
    if (optionId == swum.DELETE_LIST_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.DELETE_LIST_OPTION",parms)
        
        fparms  =   get_parms_for_input(parms,swuw.maint_list_utility_input_idList)
        #print("fparms",fparms)

        listname    =   fparms[0]
        
        opstat  = opStatus()
        
        for i in range(len(swum.ReservedDicts)) :
            if(listname == swum.ReservedDicts[i]) :
                opstat.set_status(False)
                opstat.set_errorMsg("List to delete is a system reserved dict")
                
        if(opstat.get_status()) :
            if(len(listname) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid list name to delete")
            else :
                swum.delete_List(listname)
            
        swuw.display_list_maint()
        
        if(not (opstat.get_status())) :
            display_exception(opstat)
            
        return

    if (optionId == swum.LOAD_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        
        #print("swum.LOAD_DICT_OPTION\n",parms)
        
        fparms  =   get_parms_for_input(parms,swuw.maint_dict_utility_input_idList)
        #@print("fparms",fparms)
        
        swuw.display_dict_maint(None,fparms[3])

        return

    if (optionId == swum.DELETE_DICT_OPTION) :
        swuw.get_sw_utilities_main_taskbar()

        #print("swum.DELETE_DICT_OPTION",parms)
        
        fparms  =   get_parms_for_input(parms,swuw.maint_dict_utility_input_idList)
        #print("fparms",fparms)

        dictname    =   fparms[0]
        
        opstat  = opStatus()
        
        for i in range(len(swum.ReservedDicts)) :
            if(dictname == swum.ReservedDicts[i]) :
                opstat.set_status(False)
                opstat.set_errorMsg("Dict to delete is a system reserved dict")
                
        if(opstat.get_status()) :
            if(len(dictname) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid dict name to delete")
            else :
                swum.delete_Dict(dictname)
            
        swuw.display_dict_maint()
        
        if(not (opstat.get_status())) :
            display_exception(opstat)
            
        return

    #elif(optionId == swum.PROCESS_FUNCTION) : 
    #    process_generic_function(parms)
    #    return

    #elif(optionId == swum.SELECT_FUNCTION) : 
    #    swuw.display_generic_function_inputs(parms)
    #    return

"""
def process_generic_function(parms) :

    funcid     =   parms[0]

    if(funcid == swum.SAVE_FUNCTION) :
        
        #fparms      =   gfw.get_genfunc_input_parms(parms[1])
        
        gt_module   =   parms[1]
        newcode     =   parms[3]
        
        gt_title_start      =   newcode.find("def ")
        gt_title_end        =   newcode.find("(")
        gt_title            =   newcode[(gt_title_start+4):(gt_title_end)]

        if( (len(gt_title) > 0) ) : 
            
            if(not(gt_title in swum.reservedfunctions)) :

                if(not(swgf.get_generic_function(gt_title) == None)) :
                    swgf.delete_generic_function(gt_title)
                
                newfunc     =   swgf.genericFunction(gt_module,gt_title,newcode)
                swgf.add_generic_function(newfunc)
                #cfg.set_config_value(gfw.gen_function_input_id+"Parms",[gt_module,gt_title,newcode,""])
            
        swuw.display_generic_function_inputs(gt_title)
    
    elif(funcid == swum.DELETE_FUNCTION) :
        print("DELETE_FUNCTION",parms)        
        ftitle    =  parms[2]
        
        if(not (ftitle in swum.reservedfunctions)) :
            swgf.delete_generic_function(ftitle)
        
        cfg.drop_config_value(swuw.gen_function_input_id+"Parms")
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)

        swuw.display_generic_function_inputs(None)
        
        if(ftitle in swum.reservedfunctions) :
            print("\n")
            display_status("Can not delete system function " + ftitle)
        
    if(funcid == swum.CLEAR_FUNCTION) :
        
        print("CLEAR_FUNCTION",parms)
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    
        cfg.drop_config_value(swuw.gen_function_input_id+"Parms")
        
        swuw.display_generic_function_inputs(None)
"""




def clear_sw_utility_data() :
    
    drop_owner_tables(cfg.SWUtilities_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWUtilities_ID)
    clear_sw_utility_cfg_values()
    
def clear_sw_utility_cfg_values() :
    
    cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    

    return




    
    
    
    
    
    
    
    
    
    
    
    
    
    



