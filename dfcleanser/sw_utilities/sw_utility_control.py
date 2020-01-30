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

from dfcleanser.common.html_widgets import (new_line)
from dfcleanser.common.table_widgets import (drop_owner_tables)

from dfcleanser.common.common_utils import (display_exception, opStatus)


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
        print("swum.UPDATE_LIST_OPTION",parms)
        return()
        
    elif (optionId == swum.CLEAR_LIST_OPTION) :
        print("swum.CLEAR_LIST_OPTION",parms)
        return()
        
        
    if (optionId == swum.ADD_LIST_OPTION) :
        print("swum.ADD_LIST_OPTION",parms)
        return()

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

    elif (optionId == swum.UPDATE_DICT_OPTION) :
        print("swum.UPDATE_DICT_OPTION",parms)
        return()
        
    elif (optionId == swum.CLEAR_DICT_OPTION) :
        print("swum.CLEAR_DICT_OPTION",parms)
        return()
        
    if (optionId == swum.ADD_DICT_OPTION) :
        print("swum.ADD_DICT_OPTION",parms)
        return()

        
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
        print("swum.DELETE_LIST_OPTION",parms)
        return()
        
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
        print("swum.DELETE_DICT_OPTION",parms)
        return()

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

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   DictList class static helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DFC_CREATED         =   0
USER_CREATED        =   1

def get_Dict(dictname,creator=DFC_CREATED) :
    return(DataframeCleanserDataStructures.get_Item(swum.DICT_ID,dictname,creator))
    
def add_Dict(dictname,newdict,creator) :
   DataframeCleanserDataStructures.add_Item(swum.DICT_ID,dictname,creator,newdict)

def delete_Dict(dictname,creator) :
    DataframeCleanserDataStructures.delete_Item(swum.DICT_ID,dictname,creator) 

def get_dicts_names(creator) :
    return(DataframeCleanserDataStructures.get_dict_names(creator))
    
def get_pretty_dict(indict,inkeys) :
    
    dicttext = "{" 
    for i in range(len(inkeys)) :
        dicttext = (dicttext + '"' + str(inkeys[i]) + '" : ' + '"' + str(indict.get(inkeys[i])) + '"')   
        if(i != (len(inkeys) -1)) :
            dicttext = (dicttext + "," + new_line)
        else :
            dicttext = (dicttext + "}")
        
    return(dicttext)


def get_List(listname,creator=DFC_CREATED) :
    return(DataframeCleanserDataStructures.get_Item(swum.LIST_ID,listname,creator))
    
def add_List(listname,newlist,creator) :
    DataframeCleanserDataStructures.add_Item(swum.LIST_ID,listname,creator,newlist)

def delete_List(listname,creator) :
    DataframeCleanserDataStructures.delete_Item(swum.LIST_ID,listname,creator) 

def get_lists_names(creator) :
    return(DataframeCleanserDataStructures.get_list_names(creator))
    

def get_Listlog() :
    return(DataframeCleanserDataStructures.get_log(swum.LIST_ID)) 

COMMON_DICTS_FILE_NAME      =   "\dfcleanserCommon_dictlog.json"
COMMON_LISTS_FILE_NAME      =   "\dfcleanserCommon_listlog.json"

USER_DICTS_FILE_NAME        =   "\dfcleanserUser_dictlog.json"
USER_LISTS_FILE_NAME        =   "\dfcleanserUser_listlog.json"



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data strucrures storage class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
class dfcDataStructureStore :

    # full constructor
    def __init__(self) :
        
        # instance variables
        self.dictStore          =   {}
        self.listStore          =   {}
        
        self.userdictStore      =   {}
        self.userlistStore      =   {}

        self.load_datastructures_file(swum.DICT_ID,DFC_CREATED)
        self.load_datastructures_file(swum.LIST_ID,DFC_CREATED)
        
        self.load_datastructures_file(swum.DICT_ID,USER_CREATED)
        self.load_datastructures_file(swum.LIST_ID,USER_CREATED)
        

    def get_datastructures_file_name(self,dstype,creator) :
        
        if(dstype == swum.DICT_ID) :
            if(creator == DFC_CREATED) :
                path = cfg.get_common_files_path() + COMMON_DICTS_FILE_NAME
            else :
                path = cfg.get_common_files_path() + USER_DICTS_FILE_NAME
                
            return(path)
            
        else :
            
            if(creator == DFC_CREATED) :
                path = cfg.get_common_files_path() + COMMON_LISTS_FILE_NAME
            else :
                path = cfg.get_common_files_path() + USER_LISTS_FILE_NAME
                
            return(path)

    def load_datastructures_file(self,dstype,creator) :

        try :
            with open(self.get_datastructures_file_name(dstype,creator), 'r') as datastructures_file :
                if(dstype == swum.DICT_ID) :
                    if(creator == DFC_CREATED) :
                        self.dictStore = json.load(datastructures_file)
                    else :
                        self.userdictStore = json.load(datastructures_file) 
                else :
                    if(creator == DFC_CREATED) :
                        self.listStore = json.load(datastructures_file)
                    else :
                        self.userlistStore = json.load(datastructures_file)
                   
                datastructures_file.close()
                
        except Exception as e:
            
            if(dstype == swum.DICT_ID) :
                
                if(creator == DFC_CREATED) :
                    self.dictStore          =   {}
                else :
                    self.userdictStore      =   {}
                    
            else :
                
                if(creator == DFC_CREATED) :
                    self.listStore          =   {}
                else :
                    self.userlistStore      =   {}

            opstat = opStatus()
            opstat.store_exception("Unable to load common file :  " + self.get_datastructures_file_name(dstype,creator),e)
            display_exception(opstat)
    
    def save_datastructures_file(self,dstype,creator) :
        
        try :
            with open(self.get_datastructures_file_name(dstype,creator), 'w') as datastructures_file :
                if(dstype == swum.DICT_ID) :
                    if(creator == DFC_CREATED) :
                        json.dump(self.dictStore,datastructures_file)
                    else :
                        json.dump(self.userdictStore,datastructures_file)
                else :
                    if(creator == DFC_CREATED) :                    
                        json.dump(self.listStore,datastructures_file)
                    else :
                        json.dump(self.userlistStore,datastructures_file)
                    
                datastructures_file.close()
                
        except Exception as e:
            opstat = opStatus()
            opstat.store_exception("Unable to save file " + self.get_datastructures_file_name(dstype,creator),e)
            display_exception(opstat)


    def get_dict_from_file(dictObject) :
                        
        fname    =   dictObject.get("filename",None)#"suck my dick"
        if(not (fname is None)) :
            
            try :                
                with open(fname, 'r') as dict_file :
                    dictitem = json.load(dict_file)
                    dict_file.close()
                    
                return(dictitem)
            except :
                return(None)    
                
        else :
            return(None)
        
    def get_list_from_file(listObject) :
                        
        fname    =   listObject.get("filename",None)

        if(not (fname is None)) :
            
            try :                
                with open(fname, 'r') as list_file :
                    listitem = json.load(list_file)
                    list_file.close()
                    
                return(listitem)
            except :
                return(None)    
                
        else :
            return(None)
        

    def get_Item(self,dstype,itemname,creator) :

        if(dstype == swum.DICT_ID) :
            
            if(creator == DFC_CREATED) : 
                
                if(self.dictStore == {}) :    self.load_datastructures_file(dstype,creator)  
                dictitem    =  self.dictStore.get(itemname,None)
                
                if(not (dictitem is None)) :
                    
                    if(len(dictitem) == 1) :
                        return(self.get_dict_from_file(dictitem))
                    else :
                        return(dictitem)
                else :    
                    return(None)
            else :
                if(self.userdictStore == {}) :    self.load_datastructures_file(dstype,creator) 
                dictitem    =  self.userdictStore.get(itemname,None)
                
                if(not (dictitem is None)) :
                    
                    if(len(dictitem) == 1) :
                        return(self.get_dict_from_file(dictitem))
                    else :
                        return(dictitem)
                else :    
                    return(None)
                
        else :
            
            if(creator == DFC_CREATED) :    
                if(self.listStore == {}) :    self.load_datastructures_file(dstype,creator) 
                listitem    =  self.listStore.get(itemname,None)
                
                if(not (listitem is None)) :
                    
                    if(len(listitem) == 1) :
                        return(self.get_list_from_file(listitem))
                    else :
                        return(listitem)
                else :    
                    return(None)
                
            else :
                
                if(self.userlistStore == {}) :    self.load_datastructures_file(dstype,creator) 
                listitem    =  self.userlistStore.get(itemname,None)
                
                if(not (listitem is None)) :
                    
                    if(len(listitem) == 1) :
                        return(self.get_list_from_file(listitem))
                    else :
                        return(listitem)
                else :    
                    return(None)
            
    def add_Item(self,dstype,name,creator,newitem,filename=None) :
        
        if(dstype == swum.DICT_ID) : 
            if(creator == DFC_CREATED) :  
                if(filename is None) :
                    self.dictStore.update({name:newitem})
                else :
                    self.dictStore.update({name:filename})
            else :
                if(filename is None) :
                    self.userdictStore.update({name:newitem})
                else :
                    self.userdictStore.update({name:filename})
        else :
            if(creator == DFC_CREATED) : 
                if(filename is None) :
                    self.listStore.update({name:newitem})
                else :
                    self.listStore.update({name:filename})                    
            else :
                if(filename is None) :
                    self.userlistStore.update({name:newitem})
                else :
                    self.userlistStore.update({name:filename})
            
        self.save_datastructures_file(dstype,creator)

    def delete_Item(self,dstype,creator,name) :
        if(dstype == swum.DICT_ID) :  
            if(creator == DFC_CREATED) :
                self.dictStore.pop(name,None)
            else :
                self.userdictStore.pop(name,None)
        else :
            if(creator == DFC_CREATED) :
                self.listStore.pop(name,None) 
            else :
                self. userlistStore.pop(name,None) 
            
        self.save_datastructures_file(dstype,creator)

    def get_dict_names(self,creator) :
        if(creator == DFC_CREATED) :
            return(swum.ReservedDicts)
        else :
            names   =   self.userdictStore.keys()
            if(not (names is None)) :
                names   =   list(names)
                names.sort()
            
            if(len(names) > 0) :
                return(names)
            else :
                return(None)

    def get_list_names(self,creator) :
        if(creator == DFC_CREATED) :
            return(swum.ReservedLists)
        else :
            names   =   self.userlistStore.keys()
            if(not (names is None)) :
                names   =   list(names)
                names.sort()
                
            if(len(names) > 0) :
                return(names)
            else :
                return(None)

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
DataframeCleanserDataStructures    =   dfcDataStructureStore()




def clear_sw_utility_data() :
    
    drop_owner_tables(cfg.SWUtilities_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWUtilities_ID)
    clear_sw_utility_cfg_values()
    
def clear_sw_utility_cfg_values() :
    
    cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    

    return




    
    
    
    
    
    
    
    
    
    
    
    
    
    



