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

from dfcleanser.common.html_widgets import (new_line)

from dfcleanser.common.table_widgets import (drop_owner_tables)

from dfcleanser.common.common_utils import (display_status, display_exception, opStatus)

from dfcleanser.scripting.data_scripting_control import add_to_script

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
        gfw.display_generic_function_inputs() 

    elif(optionId == gfm.PROCESS_GENERIC_FUNCTION_OPTION) : 
        process_generic_function(parms)


"""
#--------------------------------------------------------------------------
#    dataframe transform process functions
#--------------------------------------------------------------------------
"""
def process_generic_function(parms) :

    funcid     =   parms[0]#[0]

    if(funcid == gfm.NEW_FUNCTION) :

        cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
        gfw.display_generic_function_inputs()
    
    elif(funcid == gfm.RUN_FUNCTION) :
        
        opstat = opStatus()
        
        try :
            code = cfg.get_config_value(gfw.gen_function_input_id+"Parms")[1]
            exec(code)
               
        except Exception as e:
            opstat.store_exception("Unable to run generic function ",e)
            
        gfw.display_generic_function_inputs()
        
        if(opstat.get_status()) :
            display_status("Generic Function Code run Successfully and added to script log")
            add_to_script(code,opstat)
        else :
            display_exception(opstat)
            

    elif(funcid == gfm.GET_FUNCTION) :
        gt_title = parms[1]
        gt_func = get_generic_function(gt_title)

        if(not (gt_func == None)) :
            fparms = [gt_title,gt_func]
            cfg.set_config_value(gfw.gen_function_input_id+"Parms",fparms)
            
        gfw.display_generic_function_inputs()
    
    if(funcid == gfm.SAVE_FUNCTION) :
        fparms  =   gfw.get_genfunc_input_parms(parms[1])
        ttitle  =   fparms[0]
        newcode =   fparms[1]

        if( (len(ttitle) > 0) ) : #and (len(tfunction) > 0) ) :
            #ttitle = ttitle.replace("\n","")
            if(not(get_generic_function(ttitle) == None)) :
                print("should delete")
                delete_generic_function(ttitle)
                
            add_generic_function(ttitle,newcode)
            cfg.set_config_value(gfw.gen_function_input_id+"Parms",[ttitle,newcode])
            
        gfw.display_generic_function_inputs()

    if(funcid == gfm.DELETE_FUNCTION) :
        
        fparms = gfw.get_genfunc_input_parms(parms[1])
        delete_generic_function(fparms[0])
        
        newcode = ("# generic function" + new_line + 
                   '# function title' + new_line +
                   "from dfcleanser.common.cfg import get_dc_dataframe" + new_line + 
                   "df = get_dc_dataframe()" + new_line + new_line)
        
        cfg.set_config_value(gfw.gen_function_input_id+"Parms",["",newcode])
        gfw.display_generic_function_inputs()
        
    elif(funcid == gfm.CLEAR_FUNCTION) :

        cfg.drop_config_value(gfw.gen_function_input_id+"Parms")
        gfw.display_generic_function_inputs()
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    system generic functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 



def convert_hhmm_to_HH_MM_format(colname) :
    
    df = cfg.get_dc_dataframe()
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
    cfg.set_dc_dataframe(df)    
    
    
    
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
* helper functions
* -----------------------------------------------------------------------*
"""

def add_generic_function(title,code) :
    GenericFunctions.add_function(title,code)

def get_generic_function(id) :
    return(GenericFunctions.get_function(id))

def delete_generic_function(title) :
    GenericFunctions.delete_function(title)

def get_total_generic_functions() :
    return(GenericFunctions.get_total_functions())

def get_generic_functions_names_list() :
    return(GenericFunctions.get_function_list())

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
            
                with open(fname, 'r') as gen_func_file :
                    self.genericfunctionDict = json.load(gen_func_file)
                    gen_func_file.close()
            
            except :
                print("[error load gen_func file]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
    
    def save_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
    
            try :
            
                with open(fname, 'w') as gen_func_file :
                    json.dump(self.genericfunctionDict,gen_func_file)
                    gen_func_file.close()
                
            except :
                print("[save_generic_functions_file error] : " + str(sys.exc_info()[0]))
            
    def add_function(self,title,code) :
        self.genericfunctionDict.update({title:code})
        self.save_generic_functions_file()
            
    def get_total_functions(self) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        return(len(self.genericfunctionDict))
    
    def get_function_list(self) :
        return(list(self.genericfunctionDict.keys()))
        
    def delete_function(self,titleParm) :
        self.genericfunctionDict.pop(titleParm)
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
    
    
    
    
    