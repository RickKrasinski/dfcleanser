"""
# sw_utility_genfunc_control 
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
from   dfcleanser.sw_utilities import sw_utility_genfunc_widgets as gfw
import dfcleanser.sw_utilities.sw_utility_genfunc_model as gfm

from dfcleanser.common.table_widgets import (drop_owner_tables)
from dfcleanser.common.common_utils import (display_status)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    generic functions components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_gen_function(optionId,parms=None) :

    from IPython.display import clear_output
    clear_output()
    
    from dfcleanser.common.cfg import check_if_dc_init
    if(not check_if_dc_init()) :
        gfw.get_genfunc_main_taskbar()
        clear_gen_function_cfg_values()
        return

    if(optionId == gfm.DISPLAY_GENERIC_FUNCTION_TB) :
        clear_gen_function_cfg_values()
        gfw.get_genfunc_main_taskbar()

    elif(optionId == gfm.DISPLAY_GENERIC_FUNCTION) :
        cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
        gfw.display_generic_functions() 

    elif(optionId == gfm.PROCESS_GENERIC_FUNCTION_OPTION) : 
        process_generic_function(parms)


"""
#--------------------------------------------------------------------------
#    dataframe transform process functions
#--------------------------------------------------------------------------
"""
def process_generic_function(parms) :

    funcid     =   parms[0]

    if(funcid == gfm.LOAD_FUNCTION) :
        
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)

        fmodule         =   gfm.reservedfunctionsmodule
        ftitle          =   "dfcleanser_generic_function"
        code            =   parms[1][0]
        
        cfg.set_config_value(gfw.gen_function_input_id+"Parms",[fmodule,ftitle,code,""])
       
        gfw.display_generic_function_inputs(None)
    
    if(funcid == gfm.SAVE_FUNCTION) :
        
        #fparms      =   gfw.get_genfunc_input_parms(parms[1])
        
        gt_module   =   parms[1]
        newcode     =   parms[3]
        
        gt_title_start      =   newcode.find("def ")
        gt_title_end        =   newcode.find("(")
        gt_title            =   newcode[(gt_title_start+4):(gt_title_end)]

        if( (len(gt_title) > 0) ) : 
            
            if(not(gt_title in gfm.reservedfunctions)) :

                if(not(get_generic_function(gt_title) == None)) :
                    delete_generic_function(gt_title)
                
                newfunc     =   genericFunction(gt_module,gt_title,newcode)
                add_generic_function(newfunc)
                #cfg.set_config_value(gfw.gen_function_input_id+"Parms",[gt_module,gt_title,newcode,""])
            
        gfw.display_generic_function_inputs(gt_title)
    
    if(funcid == gfm.UPDATE_FUNCTION) :
        print("UPDATE_FUNCTION",parms)
        
        fparms      =   gfw.get_genfunc_input_parms(parms[1])
        ftitle      =   cfg.get_config_value(cfg.CURRENT_GENERIC_FUNCTION)
        
        in_module   =   fparms[0]
        in_title    =   fparms[1]
        in_code     =   fparms[2]
        in_kwargs   =   fparms[3]
        
        if(not(ftitle == in_title)) :
            cfg.set_config_value(cfg.CURRENT_GENERIC_FUNCTION,in_title)
                
        newfunc     =   genericFunction(in_module,in_title,in_code,in_kwargs)
        add_generic_function(newfunc)
            
        gfw.display_generic_function_inputs(in_title)

    if(funcid == gfm.DELETE_FUNCTION) :
        print("DELETE_FUNCTION",parms)        
        fmodule   =  parms[1]  
        ftitle    =  parms[2]
        
        if(not (ftitle in gfm.reservedfunctions)) :
            delete_generic_function(ftitle)
        
        cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)

        gfw.display_generic_function_inputs(None)
        
        if(ftitle in gfm.reservedfunctions) :
            print("\n")
            display_status("Can not delete system function " + ftitle)
        
        
    elif(funcid == gfm.DISPLAY_FUNCTION) :
        
        print("DISPLAY_FUNCTION",parms)
        fparms  =   ["","","",""]
        
        fparms[0]   =  parms[1]  
        fparms[1]   =  parms[2]

        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_function_help_doc
        help_text   =   get_function_help_doc(parms[1],parms[2])
        
        if(not (help_text is None)) :
            if(len(help_text) > 0) :
                fparms[2]   =   help_text
            else :
                fparms[2]   =   "No help text found"
        else :
            fparms[2]   =   "No help text found"    
                
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    
        cfg.set_config_value(gfw.gen_function_input_id+"Parms",fparms)
        print("DISPLAY_FUNCTION",fparms)        
        gfw.display_generic_function_inputs(None)
    
    if(funcid == gfm.SELECT_FUNCTION) :
        
        print("SELECT_FUNCTION",parms)
        gfw.display_generic_function_inputs(parms[1])

    if(funcid == gfm.CLEAR_FUNCTION) :
        
        print("CLEAR_FUNCTION",parms)
        cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    
        cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
        
        gfw.display_generic_function_inputs(None)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    system generic functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 



def convert_hhmm_to_HH_MM_format(colname) :
    
    df = cfg.get_dfc_dataframe()
    newraws = []

    for i in range(len(df)) :
        raw = str(df['Time Occurred'][i])
        if(len(raw) == 1) :
            newraws.append("00:0" + raw)
        elif(len(raw) == 2) :
            newraws.append("00:" + raw)
        elif(len(raw) == 3) :
            newraws.append("0" + raw[0] + ":" + raw[1] + raw[2])
        else :
            newraws.append(raw[0] + raw[1] + ":" + raw[2] + raw[3])

    df[colname] = newraws
    cfg.set_current_dfc_dataframe(df)    
    
    
    
"""
#--------------------------------------------------------------------------
#    datetime utilities
#--------------------------------------------------------------------------
""" 
  
def get_datetime_timedelta_units(start, end, units)  :  
    
    #import datetime
    import numpy
    from dfcleanser.common.common_utils import YEARS, DAYS, HOURS, MINUTES, SECONDS, MICROSECONDS
    
    difference  =   start - end
    total_seconds   =   difference.total_seconds()

    if(units == YEARS)          :   return(numpy.int64(divmod(total_seconds, 31556926)[0]))
    elif(units == DAYS)         :   return(numpy.int64(divmod(total_seconds, 86400)[0]))
    elif(units == HOURS)        :   return(numpy.int64(divmod(total_seconds, 3600)[0]))
    elif(units == MINUTES)      :   return(numpy.int64(divmod(total_seconds, 60)[0]))
    elif(units == SECONDS)      :   return(numpy.int64(total_seconds))  
    elif(units == MICROSECONDS) :   return(numpy.int64(difference.microseconds))  
    
   
"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic functions classes
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

GENERIC_FUNCTIONS_FILE_NAME       =   "dfcleanserCommon_gfunclog.json"

"""
* -----------------------------------------------------------------------*
* generic function class
* -----------------------------------------------------------------------*
"""
class genericFunction :

    def __init__(self,fmodparm="",ftitleparm="",fcodeparm="",fkwargsparm=None) :
        
        self.fmodule     =   fmodparm
        self.ftitle      =   ftitleparm
        self.fcode       =   fcodeparm
        self.fkwargs     =   fkwargsparm

    def get_func_module(self) :
        return(self.fmodule)
    def get_func_title(self) :
        return(self.ftitle)
    def get_func_code(self) :
        return(self.fcode)
    def get_func_kwargs(self) :
        return(self.fkwargs)
        
    def set_func_module(self,module) :
        self.fmodule    =   module
    def set_func_title(self,title) :
        self.ftitle     =   title
    def set_func_code(self,code) :
        self.fcode      =   code
    def set_func_kwargs(self,kwargs) :
        self.fkwargs    =   kwargs

    def get_serial_func(self) :
        return([self.get_func_module(),
                self.get_func_title(),
                self.get_func_code(),
                self.get_func_kwargs()])

"""
* -----------------------------------------------------------------------*
* helper functions
* -----------------------------------------------------------------------*
"""

def add_generic_function(genfunc) :
    GenericFunctions.add_function(genfunc)

def get_generic_function(ftitle) :
    if(not (ftitle in gfm.reservedfunctions)) :
        return(GenericFunctions.get_function(ftitle))
    
def get_generic_function_desc(ftitle) :
    
    if(ftitle in gfm.reservedfunctions) :
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_function_help_doc
        module_name   =   "dfcleanser.sw_utilities.sw_utility_genfunc_functions"
        return(get_function_help_doc(module_name,ftitle))
        
    else :
        return(ftitle)

def delete_generic_function(title) :
    GenericFunctions.delete_function(title)

def get_total_generic_functions() :
    total_funcs     =   len(gfm.reservedfunctions)
    total_funcs     =   total_funcs + GenericFunctions.get_total_functions()
    return(total_funcs)

def get_generic_functions_names_list() :
    func_list   =   []
    for i in range(len(gfm.reservedfunctions)) :
        func_list.append(gfm.reservedfunctions[i])
        
    user_funcs  =   GenericFunctions.get_function_list()
    for i in range(len(user_funcs)) :
        func_list.append(user_funcs[i])
    
    return(func_list)

"""
* -----------------------------------------------------------------------*
* generic transforms storage class
* -----------------------------------------------------------------------*
"""
class genericFunctionsStore :

    def __init__(self) :

        # instance variables
        self.genericfunctionDict    =   {}
        self.load_generic_functions_file()
    
    def get_functions_file_name(self) :
        import os
        return(os.path.join(cfg.get_common_files_path(),GENERIC_FUNCTIONS_FILE_NAME))
    
    def load_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
        
            try :
                serial_gen_func_dict    =   {}
                
                with open(fname, 'r') as gen_func_file :
                    #print("load gen func file : ",fname)
                    serial_gen_func_dict = json.load(gen_func_file)
                    #print("load gen func dict : ",serial_gen_func_dict)
                    gen_func_file.close()
               
                if(len(serial_gen_func_dict) > 0) :
                    gf_keys         =   list(serial_gen_func_dict)
                    
                    for i in range(len(gf_keys)) :
                        gen_func_list   =   serial_gen_func_dict.get(gf_keys[i])
                        new_gf          =   genericFunction(gen_func_list[0],
                                                            gen_func_list[1],
                                                            gen_func_list[2],
                                                            gen_func_list[3])
                    
                    self.genericfunctionDict.update({gf_keys[i] : new_gf}) 
                    
            except FileNotFoundError :
                self.genericfunctionDict = {}
            except :
                print("[error load gen_func file]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
    
    def save_generic_functions_file(self) :
        
        #print("[save_generic_functions]",len(self.genericfunctionDict))
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
            
            gf_keys         =   list(self.genericfunctionDict.keys())
            #print("[save_generic_functions]",gf_keys)
            serial_gen_func_dict   =   {}
            
            if(len(gf_keys) > 0) :
                for i in range(len(gf_keys)) : 
                    serial_func     =   self.genericfunctionDict.get(gf_keys[i]).get_serial_func()
                    serial_gen_func_dict.update({gf_keys[i] : serial_func})
    
                if(len(gf_keys) > 0) :
                    try :
            
                        with open(fname, 'w') as gen_func_file :
                            json.dump(serial_gen_func_dict,gen_func_file)
                            #print("[save_generic_functions dump ok]")
                            gen_func_file.close()
                
                    except :
                        print("[save_generic_functions_file error] : " + str(sys.exc_info()[0]))
                        
            else :
                    
                import os 
                os.remove(self.get_functions_file_name())
                    
                    
                    
                    
                    
            
    def add_function(self,function) :
        
        title   =   function.get_func_title()
        
        #print("add_function",title,type(function))
        #print("add_function",function.get_func_module())
        #print("add_function",function.get_func_title())
        #print("add_function",function.get_func_code())
        #print("add_function",function.get_func_kwargs())
        
        
        self.genericfunctionDict.update({title:function})
        #print("self.genericfunctionDict",len(self.genericfunctionDict))
        self.save_generic_functions_file()
            
    def get_total_functions(self) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        return(len(self.genericfunctionDict))
    
    def get_function_list(self) :
        return(list(self.genericfunctionDict.keys()))
        
    def delete_function(self,title) :
        print("delete_function",title,len(self.genericfunctionDict))
        try :
            del self.genericfunctionDict[title]
        except :
            print("key not found"
                  )
        print("delete_function",title,len(self.genericfunctionDict))
        self.save_generic_functions_file()
        
    def get_function(self,functionTitle) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        
        return(self.genericfunctionDict.get(functionTitle,None))

GenericFunctions   =   genericFunctionsStore()
    
def clear_gen_function_data() :
    
    drop_owner_tables(cfg.GenFunction_ID)
    clear_gen_function_cfg_values()
    
def clear_gen_function_cfg_values() :
    cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
    cfg.drop_config_value(cfg.CURRENT_GENERIC_FUNCTION)    
    
    
    
    