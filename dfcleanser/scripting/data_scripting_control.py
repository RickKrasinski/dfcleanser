"""
# data_scripting_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:29:36 2017

@author: Rick
"""
import sys

this = sys.modules[__name__]

import json

import dfcleanser.common.cfg as cfg
import dfcleanser.scripting.data_scripting_widgets as dsw
import dfcleanser.scripting.data_scripting_model as dsm

from dfcleanser.common.common_utils import (display_status, RunningClock, opStatus, display_exception)

from dfcleanser.common.html_widgets import new_line
    

from dfcleanser.common.table_widgets import drop_owner_tables


def display_data_scripting(optionId,parms=None) :
    
    dsw.display_dc_data_scripting(optionId,parms)
 
    
def get_scriptlog_list() :

    if( not (DataframeCleanserScriptLog.get_ScriptLog() == None) ) :
        
        keys = DataframeCleanserScriptLog.get_ScriptLog().keys()
        for i in range(len(keys)) :
            keys[i] = int(keys[i])
            
        keys.sort()

        scripttext = ""
        
        for i in range(len(keys)) :
            scripttext = (scripttext + DataframeCleanserScriptLog.get_ScriptLog().get(str(i)))    
            
        return([scripttext])
            
    else :
        return("")


def run_scriptlog(parms,opstat) :
    
    set_current_scriptlog(dsw.get_code_from_form(parms))
    
    scriptLog = DataframeCleanserScriptLog.get_ScriptLog()
    
    if( not (scriptLog == None) ) :

        steps   =  scriptLog.split("\n\n") 
        
        display_status("Running Current Script")
        
        clock = RunningClock()
        clock.start()


        for i in range(len(steps)) :
            
            current_step    =   steps[i].replace("\n    ","\n")
            current_step    =   current_step.lstrip(" ")
            
            cstep   =   "      " + current_step
            cstep   =   cstep.replace("\n","\n      ")
            print(cstep,"\n") 
               
            try :

                exec(current_step)
                
            except Exception as e:
                opstat.store_exception("Error running script log at step : "  + str(i+1),e)
                clock.stop()
                return(i)

        clock.stop()
        return(len(steps))                    
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Current Script Log is empty")

def add_code_to_script(parms) :
    print("add_code_to_script")
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser scripting data
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   static helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def drop_current_script() :
    DataframeCleanserScriptLog.drop_ScriptLog()

def load_backup_scriptlog_to_current() :
    DataframeCleanserScriptLog.restore_ScriptLog_from_backup()
    
def save_current_scriptlog_to_backup(code) :
    DataframeCleanserScriptLog.save_ScriptLog_to_backup()

def set_current_scriptlog(code) :
    DataframeCleanserScriptLog.set_ScriptLog(code)

def get_current_scriptlog() :
    return(DataframeCleanserScriptLog.get_ScriptLog())

def set_script_logging(state=False) :

    if(state) :  DataframeCleanserScriptLog.enter_scripting_mode()
    else :       DataframeCleanserScriptLog.exit_scripting_mode()        

def isScripting() :
    return(DataframeCleanserScriptLog.is_scripting_on)
    
def add_to_script(code,opstat) :
    
    newcode = ""
    
    try     :
    
        for i in range(len(code)) :
            newcode = (newcode + "    " + code[i])
            if(i < (len(code)-1)) :
                newcode = (newcode + new_line)
        
        add_next_step(newcode)
        
    except Exception as e:
        opstat.store_exception("Error adding to script : "  + code,e)

    return(opstat)
        

def add_next_step(stepcode) :
        
    # find the last stpin the code log
    if(DataframeCleanserScriptLog.get_ScriptLog() == None) :
            
        stepid = 1
        code = ""
            
    else :
            
        code = DataframeCleanserScriptLog.get_ScriptLog() + new_line

        found       =   code.find("# step ")
        stepid      =   0
        lastfound   =   0
            
        while(found != -1) :
            nextfound = code.find("# step ",lastfound)    
            if(nextfound == -1) :
                found = -1
            else :
                lastfound = nextfound + len("# step ")
                stepid = stepid + 1
                    
        stepid = stepid + 1
        
    code = (code + new_line + "    # step " + str(stepid) + new_line)
    code = (code + stepcode)
        
    DataframeCleanserScriptLog.set_ScriptLog(code)

def enter_scripting_mode() :
    DataframeCleanserScriptLog.enter_scripting_mode()

def exit_scripting_mode() :
    DataframeCleanserScriptLog.exit_scripting_mode()

def display_script_exception(e) :
    opstat = opStatus()
    opstat.store_exception("Unable to run script",e)
    display_exception(opstat)

    return()
    
def set_scripting_status(status) :
    DataframeCleanserScriptLog.set_Scripting_status(status)    
    
"""
#--------------------------------------------------------------------------
#   script log class
#--------------------------------------------------------------------------
"""
class DCScriptLog :
    
    

    # full constructor
    def __init__(self) :
        
        # instance variables
        self.scriptlog          =   {}
        self.load_ScriptLog_file()
        self.scripting_status   =   False
        
    def set_Scripting_status(self,status) :
        
        if(status) :
            self.scripting_status   =   True
        else :
            self.scripting_status   =   False

    def get_ScriptLog_file_name(self) :
        
        import os        
        path_name   =   os.path.join(cfg.get_notebookPath(),cfg.get_notebookName() + "_files")
        path_name   =   os.path.join(path_name,cfg.get_notebookName() + "_scriptlog.json")
        
        #print("get_ScriptLog_file_name",path_name)
        if(len(cfg.get_notebookName()) > 0)  :
            return(path_name)
        else :
            return(None)

    def load_ScriptLog_file(self) :
        
        fname   =    self.get_ScriptLog_file_name() 
        if(not (fname == None)) :
            try :
                with open(fname, 'r') as scriptlog_file :
                    self.scriptlog = json.load(scriptlog_file)
            
            except :
                self.scriptlog          =   {}
                #print(self.get_ScriptLog_file_name())
                #print("no scriptlog")
        
    def save_ScriptLog_file(self,init=False) :
        
        if(init) :
            self.scriptlog.update({cfg.SCRIPT_LOG_KEY:{}})
            self.scriptlog.update({cfg.BACKUP_SCRIPT_LOG_KEY:{}})

        fname   =    self.get_ScriptLog_file_name() 
        if(not (fname == None)) :
        
            try :
                with open(fname, 'w') as scriptlog_file :
                    json.dump(self.scriptlog,scriptlog_file)
            except :
                from dfcleanser.common.common_utils import user_alert
                user_alert("Unable to save_scriptlog_file " + self.get_ScriptLog_file_name() + str(sys.exc_info()[2]))
                scriptlog_file.close()

    def get_ScriptLog(self) :
        
       
        if(len(self.scriptlog) == 0) :
            self.load_ScriptLog_file()    
        return(self.scriptlog.get(cfg.SCRIPT_LOG_KEY,None))
    
    def set_ScriptLog(self,scriptlogparm) :
        self.scriptlog.update({cfg.SCRIPT_LOG_KEY:scriptlogparm})
        self.save_ScriptLog_file()

    def save_ScriptLog_to_backup(self) :
       self.scriptlog.pop(cfg.BACKUP_SCRIPT_LOG_KEY,None) 
       self.scriptlog.update({cfg.BACKUP_SCRIPT_LOG_KEY:self.scriptlog.get(cfg.SCRIPT_LOG_KEY)})
       self.save_ScriptLog_file() 
       
    def restore_ScriptLog_from_backup(self) :
       self.scriptlog.pop(cfg.SCRIPT_LOG_KEY,None)
       backup = self.scriptlog.get(cfg.BACKUP_SCRIPT_LOG_KEY)
       
       if(not(backup == None)) :
           self.scriptlog.update({cfg.SCRIPT_LOG_KEY:backup})
           
       self.save_ScriptLog_file()
           
    def drop_ScriptLog(self) :

        try :
            self.scriptlog.pop(cfg.SCRIPT_LOG_KEY,None)
            self.save_ScriptLog_file() 
        except :
            print("[error drop script log]",self.scriptlog,str(sys.exc_info()[0]))
        
    def backup_ScriptLog(self) :

        try :
            self.scriptlog.pop(cfg.BACKUP_SCRIPT_LOG_KEY,None)
            self.scriptlog.update(cfg.BACKUP_SCRIPT_LOG_KEY,{})
            self.save_ScriptLog_file() 
        except :
            print("[error drop backup script file]",self.scriptlog,str(sys.exc_info()[0]))
        
    def enter_scripting_mode(self) :
        #cfg.set_config_value(cfg.SCRIPTING_FLAG_KEY,True)
        self.scripting_status = True  
        
    def exit_scripting_mode(self) :
        #cfg.drop_config_value(cfg.SCRIPTING_FLAG_KEY)
        self.scripting_status = False
        
    def is_scripting_on(self) :
        return(self.scripting_status)
        #if( (cfg.get(config_value(cfg.SCRIPTING_FLAG_KEY,None))) is None) :
        #@    return(False)
        #else :
        #    return(True)

"""
* ----------------------------------------------------
# instantiation of the config data object
* ----------------------------------------------------
"""    
DataframeCleanserScriptLog    =   DCScriptLog()


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general scripting housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_data_scripting_data() :
    
    drop_owner_tables(cfg.DataScripting_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    define_inputs(cfg.DataScripting_ID,dsw.datascripting_inputs)
    delete_all_inputs(cfg.DataScripting_ID)
    clear_data_scripting_cfg_values()
    
def clear_data_scripting_cfg_values() :
    
    cfg.drop_config_value(cfg.SCRIPT_LOG_KEY)
    cfg.drop_config_value(cfg.BACKUP_SCRIPT_LOG_KEY)
    cfg.drop_config_value(cfg.SCRIPTING_FLAG_KEY)

    return()






