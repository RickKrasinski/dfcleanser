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
import dfcleanser.sw_utilities.sw_utility_genfunc_functions as swgf

from dfcleanser.common.html_widgets import (new_line)
from dfcleanser.common.table_widgets import (drop_owner_tables)

from dfcleanser.common.common_utils import (display_exception, opStatus, display_status)


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

    elif (optionId == swum.GENFUNC_OPTION) :
        swuw.get_sw_utilities_main_taskbar()
        cfg.drop_config_value(swuw.gen_function_input_id+"Parms")
        swuw.display_generic_functions()
        return

    elif (optionId == swum.SELECT_LIST_OPTION) :

        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.LIST_ID,parms[0])
        
        return

    elif (optionId == swum.SELECT_DICT_OPTION) :
        
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.DICT_ID,parms[0])
        
        return
        
    if (optionId == swum.ADD_LIST_OPTION) :
        fparms = swuw.get_sw_utilities_list_inputs(parms)

        filename = fparms[2]
        listname = fparms[0]
        
        if(len(listname) > 0) :
            
            newlist = []
        
            if(filename != "") :
                try :
                    with open(filename, 'r') as list_file :
                        newlist = json.load(list_file)
                    list_file.close()
                
                except Exception as e:
                    opstat.store_exception("Unable to open list file" + str(id),e)
            else :
                inlist  =   fparms[1].lstrip("[")
                inlist  =   inlist.rstrip("]")
                newlist =   inlist.split(",") 
            
            if(opstat.get_status()) :
            
                try :
                    add_List(listname,newlist) 
                except Exception as e:
                    opstat.store_exception("Unable to save list " + str(id),e)
            
            swuw.get_sw_utilities_main_taskbar()
            swuw.display_list_dict(swum.LIST_ID)
            
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("Invalid List Name")

        if(not (opstat.get_status())) :
            display_exception(opstat)
            
        return
        
    if (optionId == swum.ADD_DICT_OPTION) :
        fparms = swuw.get_sw_utilities_dict_inputs(parms)
        
        filename = fparms[2]
        dictname = fparms[0]

        if(len(dictname) > 0) :
            
            newdict = {}
        
            if(filename != "") :
                try :
                    with open(filename, 'r') as dict_file :
                        newdict = json.load(dict_file)
                    dict_file.close()
                
                except Exception as e:
                    opstat.store_exception("Unable to open dict file" + str(id),e)
            else :
                newdict =  fparms[1]
                
                if(len(fparms[1]) > 0) :
                    try :
                        newdict = newdict.replace("'", "\"")
                        sdict = json.loads(newdict)
                        newdict = sdict
                    except Exception as e:
                        opstat.store_exception("Unable to convert dict via json " + str(id),e)
                        
                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dict dat defined")
                
            if(opstat.get_status()) :
            
                try :
                    add_Dict(dictname,newdict) 
                except Exception as e:
                    opstat.store_exception("Unable to save dict " + str(id),e)
            
            swuw.get_sw_utilities_main_taskbar()
            swuw.display_list_dict(swum.DICT_ID)
            
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("Invalid Dict Name")
            
        if(not (opstat.get_status())) :
            display_exception(opstat)
        
        return
    
    if (optionId == swum.DELETE_LIST_OPTION) :
        
        opstat  = opStatus()
        
        for i in range(len(swum.ReservedLists)) :
            if(parms == swum.ReservedLists[i]) :
                opstat.set_status(False)
                opstat.set_errorMsg("List to delete is a system reserved list")

        if(opstat.get_status()) :
            if((parms=="")) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid list name to delete")
            else :
                delete_List(parms)

        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.LIST_ID)
        
        if(not (opstat.get_status())) :
            display_exception(opstat)
       
        return

    if (optionId == swum.DELETE_DICT_OPTION) :

        opstat  = opStatus()
        
        for i in range(len(swum.ReservedDicts)) :
            if(parms == swum.ReservedDicts[i]) :
                opstat.set_status(False)
                opstat.set_errorMsg("Dict to delete is a system reserved dict")
                
        if(opstat.get_status()) :
            if(len(parms) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid dict name to delete")
            else :
                delete_Dict(parms)
                
        swuw.get_sw_utilities_main_taskbar()
        swuw.display_list_dict(swum.DICT_ID)
        
        if(not (opstat.get_status())) :
            display_exception(opstat)
            
        return

    elif(optionId == swum.PROCESS_FUNCTION) : 
        process_generic_function(parms)
        return

    elif(optionId == swum.SELECT_FUNCTION) : 
        swuw.display_generic_function_inputs(parms)
        return


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
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   DictList class static helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_Dict(dictname) :
    return(DataframeCleanserDictLog.get_Item(swum.DICT_ID,dictname))
    
def add_Dict(dictname,newdict) :
    DataframeCleanserDictLog.add_Item(swum.DICT_ID,dictname,newdict)

def delete_Dict(dictname) :
    DataframeCleanserDictLog.delete_Item(swum.DICT_ID,dictname) 

def get_Dictlog() :
    return(DataframeCleanserDictLog.get_log(swum.DICT_ID))
    
def get_pretty_dict(indict,inkeys) :
    
    dicttext = "{" 
    for i in range(len(inkeys)) :
        dicttext = (dicttext + '"' + str(inkeys[i]) + '" : ' + '"' + str(indict.get(inkeys[i])) + '"')   
        if(i != (len(inkeys) -1)) :
            dicttext = (dicttext + "," + new_line)
        else :
            dicttext = (dicttext + "}")
        
    return(dicttext)


def get_List(listname) :
    return(DataframeCleanserDictLog.get_Item(swum.LIST_ID,listname))
    
def add_List(listname,newdict) :
    DataframeCleanserDictLog.add_Item(swum.LIST_ID,listname,newdict)

def delete_List(listname) :
    DataframeCleanserDictLog.delete_Item(swum.LIST_ID,listname) 

def get_Listlog() :
    return(DataframeCleanserDictLog.get_log(swum.LIST_ID)) 

def get_filenames() :
    print("DICT ID",DataframeCleanserDictLog.get_Log_file_name(swum.DICT_ID),get_Dictlog())
    print("LIST ID",DataframeCleanserDictLog.get_Log_file_name(swum.LIST_ID),get_Listlog())

COMMON_DICTS_FILE_NAME       =   "\dfcleanserCommon_dictlog.json"
COMMON_LISTS_FILE_NAME       =   "\dfcleanserCommon_listlog.json"

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Notebook dict class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
class DCDictListLog :

    # full constructor
    def __init__(self) :
        
        # instance variables
        self.dictlog          =   {}
        self.listlog          =   {}

        self.load_Log_file(swum.DICT_ID)
        self.load_Log_file(swum.LIST_ID)
        

    def get_Log_file_name(self,id) :
        if(id == swum.DICT_ID) :
            path = cfg.get_common_files_path() + COMMON_DICTS_FILE_NAME
            return(path)
        else :
            path = cfg.get_common_files_path() + COMMON_LISTS_FILE_NAME
            return(path)

    def load_Log_file(self,id) :

        try :
            with open(self.get_Log_file_name(id), 'r') as log_file :
                if(id == swum.DICT_ID) :
                    self.dictlog = json.load(log_file)
                else :
                     self.listlog = json.load(log_file)
                   
                log_file.close()
                
        except Exception as e:
            if(id == swum.DICT_ID) :
                self.dictlog          =   {}
            else :
                self.listlog          =   {}

            opstat = opStatus()
            opstat.store_exception("Unable to load common file :  " + self.get_Log_file_name(id),e)
            display_exception(opstat)
    
    def save_Log_file(self,id) :
        
        try :
            with open(self.get_Log_file_name(id), 'w') as log_file :
                if(id == swum.DICT_ID) :
                    json.dump(self.dictlog,log_file)
                else :
                    json.dump(self.listlog,log_file)
                    
                log_file.close()
                
        except Exception as e:
            opstat = opStatus()
            opstat.store_exception("Unable to save file " + self.get_Log_file_name(id),e)
            display_exception(opstat)


    def get_Item(self,id,itemname) :
        
        if(id == swum.DICT_ID) :
            if(self.dictlog == {}) :    self.load_Log_file(id)    
            return(self.dictlog.get(itemname,None))
        else :
            if(self.listlog == {}) :    self.load_Log_file(id) 
            return(self.listlog.get(itemname,None))
            
    def add_Item(self,id,name,newitem) :
        if(id == swum.DICT_ID) :        
            self.dictlog.update({name:newitem})
        else :
            self.listlog.update({name:newitem})
            
        self.save_Log_file(id)

    def delete_Item(self,id,name) :
        if(id == swum.DICT_ID) :        
            self.dictlog.pop(name,None) 
        else :
            self.listlog.pop(name,None) 
            
        self.save_Log_file(id)

    def get_log(self,id) :
        if(id == swum.DICT_ID) : 
            if(self.dictlog == {}) :    self.load_Log_file(id)    
            return(self.dictlog) 
        else :
            if(self.listlog == {}) :    self.load_Log_file(id)    
            return(self.listlog) 
            

"""
* ----------------------------------------------------
# instantiation of the dict data object
* ----------------------------------------------------
"""    
DataframeCleanserDictLog    =   DCDictListLog()




def clear_sw_utility_data() :
    
    drop_owner_tables(cfg.SWUtilities_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    define_inputs(cfg.SWUtilities_ID,swuw.dfswutils_inputs)
    delete_all_inputs(cfg.SWUtilities_ID)
    clear_sw_utility_cfg_values()
    
def clear_sw_utility_cfg_values() :
    
    cfg.drop_config_value(swuw.build_list_utility_input_id+"Parms")
    cfg.drop_config_value(swuw.build_dict_utility_input_id+"Parms")
    cfg.drop_config_value(swuw.gen_function_input_id+"Parms")
    cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    

    return




    
    
    
    
    
    
    
    
    
    
    
    
    
    



