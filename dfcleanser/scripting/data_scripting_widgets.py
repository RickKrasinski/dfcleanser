"""
# data_scripting_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:29:36 2017

@author: Rick
"""
import sys
#import os

this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.scripting.data_scripting_model as dsm

from dfcleanser.common.html_widgets import (maketextarea, get_input_form, new_line,
                                            display_composite_form, get_button_tb_form,
                                            ButtonGroupForm, InputForm)

from dfcleanser.common.common_utils import (display_status, get_parms_for_input, 
                                            opStatus, display_exception, display_notes)


from dfcleanser.common.help_utils import (SCRIPTING_MAIN_TASKBAR_ID, SCRIPTING_SHOW_CURRENT_ID)

"""
#--------------------------------------------------------------------------
#    scripting taskbar
#--------------------------------------------------------------------------
"""

dc_script_tb_doc_title                 =   "Scripting Options"
dc_script_tb_title                     =   "Scripting Options"
dc_script_tb_id                        =   "scriptingoptionstb"

dc_script_tb_keyTitleList              =   ["Show Current Script",
                                            "Add to Current Script",
                                            "Clear Current Script",
                                            "Clear ","Help"]

dc_script_tb_jsList                    =   ["scripting_tb_callback(" + str(dsm.SHOW_CURRENT_SCRIPT) + ")",
                                            "scripting_tb_callback(" + str(dsm.ADD_TO_CURRENT_SCRIPT) + ")",
                                            "scripting_tb_callback(" + str(dsm.DELETE_CURRENT_SCRIPT) + ")",
                                            "scripting_tb_callback(" + str(dsm.RETURN_CURRENT_SCRIPT) + ")",
                                            "displayhelp(" + str(SCRIPTING_MAIN_TASKBAR_ID) + ")"]

"""
#--------------------------------------------------------------------------
#    scripting inputs
#--------------------------------------------------------------------------
"""

dc_script_input_title        =   "Data Scripting"
dc_script_input_id           =   "dcscripting"
dc_script_input_idList       =   ["dscode",
                                   None,None,None,None,None]

dc_script_input_labelList    =   ["current_script ",
                                  "Run</br>Current</br> Script",
                                  "Load</br>Backup</br> Script",
                                  "Backup</br>Current </br>Script",
                                  "Return","Help"]

dc_script_input_typeList     =   [maketextarea(20),
                                  "button","button","button","button","button"]

dc_script_input_placeholderList = ["current script python code",
                                   None,None,None,None,None]

dc_script_input_jsList       =    [None,
                                   "process_script_callback("+str(dsm.RUN_CURRENT_SCRIPT)+")",
                                   "process_script_callback("+str(dsm.LOAD_BACKUP_SCRIPT)+")",
                                   "process_script_callback("+str(dsm.SAVE_BACKUP_SCRIPT)+")",
                                   "process_script_callback("+str(dsm.RETURN_SCRIPT)+")",
                                   "displayhelp(" + str(SCRIPTING_SHOW_CURRENT_ID) + ")"]

dc_script_input_reqList      =   [0]

"""
#--------------------------------------------------------------------------
#    scripting add code inputs
#--------------------------------------------------------------------------
"""
dc_add_code_input_title        =   "Data Scripting Add Code"
dc_add_code_input_id           =   "dcacscripting"
dc_add_code_input_idList       =   ["dsaccode",
                                    None,None,None]

dc_add_code_input_labelList    =   ["code_to_add_to_script",
                                    "Add Code to</br>Current Script",
                                    "Return","Help"]

dc_add_code_input_typeList     =   [maketextarea(10),
                                    "button","button","button"]

dc_add_code_input_placeholderList = ["new script python code",
                                     None,None,None]

dc_add_code_input_jsList       =    [None,
                                     "process_script_add_code_callback("+str(dsm.ADD_CODE_SCRIPT)+")",
                                     "process_script_add_code_callback("+str(dsm.ADD_CODE_RETURN_SCRIPT)+")",
                                     "displayhelp(" + str(SCRIPTING_SHOW_CURRENT_ID) + ")"]

dc_add_code_input_reqList      =   [0]
 
"""
#--------------------------------------------------------------------------
#    data scripting display functions
#--------------------------------------------------------------------------
"""
def display_scripting_forms() :
    
    from dfcleanser.scripting.data_scripting_control import get_current_scriptlog 
    if( not (get_current_scriptlog() == None) ) :
        cfg.set_config_value(dc_script_input_id+"Parms",
                             [get_current_scriptlog()])
    
    print("\n")
    
    notes = []
    notes.append("You can manually edit the script log as desired")
    notes.append("The step numbers are cmmentary only and order is insignificant")
    display_notes(notes)
        
    display_composite_form([get_input_form(InputForm(dc_script_input_id,
                                                     dc_script_input_idList,
                                                     dc_script_input_labelList,
                                                     dc_script_input_typeList,
                                                     dc_script_input_placeholderList,
                                                     dc_script_input_jsList,
                                                     dc_script_input_reqList))])
    
    cfg.drop_config_value(dc_script_input_id+"Parms")
    
    print("\n")

def get_code_from_form(parms) :
    
    code        =   get_parms_for_input(parms[1],dc_script_input_idList)
    script_code =   code[0].split("\\n")
                
    save_code = ""
    
    for i in range(len(script_code)) :
        save_code = (save_code + script_code[i])
        
        if(i < (len(script_code) - 1)) :
            save_code = (save_code + new_line)
    
    return(save_code) 

def display_dc_data_scripting(optionId,parms=None) :

    from IPython.display import clear_output
    clear_output()
    
    from dfcleanser.common.cfg import check_if_dc_init
    if(not check_if_dc_init()) :
        display_composite_form([get_button_tb_form(ButtonGroupForm(dc_script_tb_id,
                                                                   dc_script_tb_keyTitleList,
                                                                   dc_script_tb_jsList,
                                                                   False))])
        from dfcleanser.scripting.data_scripting_control import clear_data_scripting_data
        clear_data_scripting_data()

        return
    
    display_composite_form([get_button_tb_form(ButtonGroupForm(dc_script_tb_id,
                                                               dc_script_tb_keyTitleList,
                                                               dc_script_tb_jsList,
                                                               False))])
 
    if(parms == None ) :
        from dfcleanser.scripting.data_scripting_control import clear_data_scripting_data
        clear_data_scripting_data()
        
    else :

        funcid = int(parms[0])
        
        if(funcid == dsm.SHOW_CURRENT_SCRIPT) :
            display_scripting_forms()
        
        if(funcid == dsm.ADD_TO_CURRENT_SCRIPT) :
            display_composite_form([get_input_form(InputForm(dc_add_code_input_id,
                                                             dc_add_code_input_idList,
                                                             dc_add_code_input_labelList,
                                                             dc_add_code_input_typeList,
                                                             dc_add_code_input_placeholderList,
                                                             dc_add_code_input_jsList,
                                                             dc_add_code_input_reqList))])

        if(funcid == dsm.ADD_CODE_SCRIPT) :
            from dfcleanser.scripting.data_scripting_control import add_code_to_script
            add_code_to_script(parms)
            display_status("Code added to Current Script succesfully ")

        elif(funcid == dsm.DELETE_CURRENT_SCRIPT) :
            from dfcleanser.scripting.data_scripting_control import drop_current_script
            drop_current_script()
            display_status("Current Script Cleared succesfully ")
            
        elif(funcid == dsm.LOAD_BACKUP_SCRIPT) :
            from dfcleanser.scripting.data_scripting_control import load_backup_scriptlog_to_current
            load_backup_scriptlog_to_current()
            display_scripting_forms()        
            
            display_status("Current Script Loaded from Backup ")
        
        elif(funcid == dsm.SAVE_BACKUP_SCRIPT) :
            
            codeparms = get_parms_for_input(parms[1],dc_script_input_idList)
            save_code = get_code_from_form(codeparms)
            
            from dfcleanser.scripting.data_scripting_control import (set_current_scriptlog,save_current_scriptlog_to_backup)
            set_current_scriptlog(save_code)
            save_current_scriptlog_to_backup(save_code)
            display_scripting_forms()
        
            display_status("Current Script Backed up successfully ")

        elif(funcid == dsm.RUN_CURRENT_SCRIPT) :
            
            opstat  =   opStatus()
            from dfcleanser.scripting.data_scripting_control import run_scriptlog
            run_scriptlog(parms,opstat)            
            
            if(opstat.get_status())  :
                display_status("Current Script Run successfully ")    
            else :
                display_exception(opstat)    


