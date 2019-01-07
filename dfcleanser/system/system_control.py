"""
# system_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import os

import dfcleanser.common.cfg as cfg
import dfcleanser.system.system_widgets as sysw
import dfcleanser.system.system_model as sysm

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (display_status, run_jscript, opStatus,
                                            does_dir_exist, does_file_exist, read_json_file,
                                            remove_files_from_dir, delete_a_file, write_json_file,
                                            display_exception)

def isEULA_read() :
    
    if(cfg.get_config_value(cfg.EULA_FLAG_KEY) == 'true') :
        return(True)
    else :
        return(False)

def display_main_tb() :

    sysw.display_system_main_taskbar()
        
def load_dfcleanser_from_toolbar() :
    from dfcleanser.system.load import load_dfcleanser_from_toolbar
    load_dfcleanser_from_toolbar()
    
def load_dfCleanser() :
    from dfcleanser.system.load import load_dfcleanser
    load_dfcleanser()

def install_common_css() :
    from dfcleanser.system.install import install_dfc_custom_css
    install_dfc_custom_css()
    
"""            
#------------------------------------------------------------------
#   display_system_environment
#
#   chapters    -   chapters option flag
#
#------------------------------------------------------------------
"""
def display_system_environment(funcId,parms=None) :

    if(not (cfg.check_if_dc_init()) ) :
        if(funcId == sysm.DISPLAY_ABBR_MAIN) :
            sysw.display_system_main_abbr_taskbar()
        else :
            sysw.display_system_main_taskbar()

        return
        
    else :
        
        if(funcId == sysm.DISPLAY_ABBR_MAIN) :
            sysw.display_system_main_abbr_taskbar()
            return
        
        if(funcId == sysm.DISPLAY_MAIN) :
            display_main_tb()
    
        if( not (funcId == sysm.PROCESS_EULA ) ) :
            
            if( not isEULA_read()) :
                #display_system_main_taskbar()
                sysw.display_EULA()
                return
        
        if(funcId == sysm.DISPLAY_CHAPTERS) :
            sysw.display_system_chapters_taskbar()
        
        if(funcId == sysm.RESET_CHAPTERS) :
            sysw.display_system_main_taskbar()

            initialize_notebook()
        
        if(funcId == sysm.PROCESS_CHAPTERS) :
            #display_main_tb()
            
            parms[0]    =   parms[0].replace("[","") 
            parms[0]    =   parms[0].replace("]","")
            parms[1]    =   parms[1].replace("[","") 
            parms[1]    =   parms[1].replace("]","")
            parms[2]    =   parms[2].replace("[","") 
            parms[2]    =   parms[2].replace("]","")
            
            core_cbs    =   parms[0].split(",")
            utils_cbs   =   parms[1].split(",")
            script_cbs  =   parms[2].split(",")
            
            corecbs     =   []
            utilscbs    =   []
            scriptcbs   =   []
            
            for i in range(len(core_cbs)) :
                if(core_cbs[i] == '"True"') :
                    corecbs.append(1)
                else :
                    corecbs.append(0)
            
            for i in range(len(utils_cbs)) :
                if(utils_cbs[i] == '"True"') :
                    utilscbs.append(1)
                else :
                    utilscbs.append(0)
            
            for i in range(len(script_cbs)) :
                if(script_cbs[i] == '"True"') :
                    scriptcbs.append(1)
                else :
                    scriptcbs.append(0)
            
            cfg.set_config_value(cfg.CORE_CBS_KEY,corecbs)
            cfg.set_config_value(cfg.UTILITIES_CBS_KEY,utilscbs)
            cfg.set_config_value(cfg.SCRIPTING_CBS_KEY,scriptcbs)
            
            from dfcleanser.system.load import reload_dfcleanser
            reload_dfcleanser()
            
            clear_cell()
        
        elif(funcId == sysm.DISPLAY_DATAFRAMES) :
            if(not(parms is None)) :
                title = parms[0]
            else :
                title = None
                
            sysw.display_system_main_taskbar()
            sysw.display_df_dataframes(title)
            
        elif(funcId == sysm.PROCESS_DATAFRAME) :
            
            fid     =   parms[0]
            from dfcleanser.common.common_utils import get_parms_for_input
            fparms  =   get_parms_for_input(parms[1],sysw.dfmgr_input_idList)
            
            dftitle     =   None
            
            if(fid == sysm.DROP_DATAFRAME) :
                cfg.drop_dfc_dataframe(fparms[0])
                
            elif(fid == sysm.SET_DATAFRAME) :    
                cfg.set_current_dfc_dataframe_title(fparms[0]) 
                
            elif(fid == sysm.UPDATE_DATAFRAME) :    
                cfg.set_dfc_dataframe_notes(fparms[3],fparms[0])
                dftitle     =   fparms[0]
            
            elif(fid == sysm.RENAME_DATAFRAME) :    
                cfg.rename_dfc_dataframe(cfg.get_config_value(cfg.CURRENT_DF_DISPLAYED_KEY),fparms[0])
                dftitle     =   fparms[0]
                
            sysw.display_system_main_taskbar()
            sysw.display_df_dataframes(dftitle)
            
        elif(funcId == sysm.DISPLAY_SYSTEM) :
            display_main_tb()
            sysw.show_sys_info()
            
        elif(funcId == sysm.DISPLAY_ABOUT) :
            sysw.display_system_main_taskbar()
            sysw.show_about_info()
            
        elif(funcId == sysm.DISPLAY_DFC_FILES) :
            sysw.display_system_main_taskbar()
            sysw.display_dfc_files_form()

        elif(funcId == sysm.PROCESS_DFC_FILES) :
            fid = int(parms[0])
            fparms = sysw.get_dcf_files_parms(parms[1])
            sysw.display_system_main_taskbar()
            process_dfc_files(fid,fparms)
        
        elif(funcId == sysm.DISPLAY_EULA) :
            display_main_tb() 
            sysw.display_EULA()
            
        elif(funcId == sysm.DISPLAY_README) :
            display_main_tb()            
            sysw.display_README()
            
        elif(funcId == sysm.PROCESS_EULA) :
            display_main_tb()
            cfg.set_config_value(cfg.EULA_FLAG_KEY,"true",cfg.GLOBAL)
            
        elif(funcId == sysm.EXIT_SETUP) :
            from dfcleanser.system.load import unload_dfcleanser
            unload_dfcleanser()
        
        return
    
def clear_cell() :  
    run_jscript("process_system_tb_callback(0)","Javascript Error","Unable to clear cell")
     
     

"""            
#------------------------------------------------------------------
#   initialize_notebook
#
#   initialize the current notebook to default screens - leave dataframe
#------------------------------------------------------------------
"""
def initialize_notebook() :
    
    from dfcleanser.data_cleansing.data_cleansing_control import clear_data_cleansing_data
    clear_data_cleansing_data()
    from dfcleanser.data_export.data_export_control import clear_data_export_data
    clear_data_export_data()
    from dfcleanser.data_import.data_import_control import clear_data_import_data
    clear_data_import_data()
    from dfcleanser.data_inspection.data_inspection_control import clear_data_inspection_data
    clear_data_inspection_data()
    from dfcleanser.scripting.data_scripting_control import clear_data_scripting_data
    clear_data_scripting_data()
    from dfcleanser.data_transform.data_transform_control import clear_data_transform_data
    clear_data_transform_data()
    from dfcleanser.sw_utilities.sw_utility_control import clear_sw_utility_data
    clear_sw_utility_data()
    from dfcleanser.sw_utilities.sw_utility_geocode_control import clear_sw_utility_geocodedata
    clear_sw_utility_geocodedata()
    from dfcleanser.sw_utilities.sw_utility_dfsubset_control import clear_sw_utility_dfsubsetdata
    clear_sw_utility_dfsubsetdata()
    
    clear_system_data()
    
    import matplotlib.pyplot as plt
"""            
#------------------------------------------------------------------
#   drop_dataframe
#
#   drop the current datframe and release memory
#------------------------------------------------------------------
"""
def clear_data() :
    
    cfg.drop_dfc_dataframe()
    from dfcleanser.scripting.data_scripting_widgets import drop_current_script, set_script_logging 
    
    set_script_logging()
    drop_current_script()
    #print("dropped scripting")
    initialize_notebook()
    
    reset_js = "window.initialize_dc();"
    
    run_jscript(reset_js,
                "fail to clear data : ",
                 "system clear data")

""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   process dfc files functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
 


def verify_file_parms(parms,opstat) :
    
    if(len(parms[0]) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("Notebook Name is invalid")
    else :
        if(len(parms[1]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("New Notebook Name is invalid")

""" 
#------------------------------------------------------------------
#   copy dfc files and _files dir
#------------------------------------------------------------------
"""
def copy_dfc_files(parms,opstat) :

    cfg_data        =   {}  
    script_data     =   {}
    
    nbname      =   parms[0]
    newnbname   =   parms[1]
    
    verify_file_parms(parms,opstat)
     
    if(opstat.get_status()) :
        
        dfc_files_path = os.path.join(cfg.get_notebook_path(),nbname+"_files")

        # check if dcf javascript exists 
        if(does_dir_exist(dfc_files_path)) :
            
            config_file_path = os.path.join(dfc_files_path,nbname + "_config.json")
            if(does_file_exist(config_file_path)) :
                cfg_data = read_json_file(config_file_path,opstat)
                
                if(opstat.get_status()) :
                    scipt_file_path = os.path.join(dfc_files_path,nbname + "_scriptlog.json")    
                    if(does_file_exist(scipt_file_path)) :
                        script_data = read_json_file(scipt_file_path,opstat)
                        
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("No dfc cfg file for "+nbname)
        
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("No dfc files directory for "+nbname)

    # we have good cfg and script files
    if(opstat.get_status()) :

        os.chdir(cfg.get_notebook_path())
        new_files_path = os.path.join(cfg.get_notebook_path(),newnbname+"_files")

        if(does_dir_exist(new_files_path)) :
                        
            # remove old files in the dfc_js dir
            remove_files_from_dir(new_files_path,opstat)
                        
        else : 
        
            if(does_file_exist(new_files_path)) :
                delete_a_file(new_files_path,opstat)
                        
            # make a _files dir
            try :
                os.makedirs(new_files_path)
                os.chdir(new_files_path)
            except Exception as e:
                opstat.store_exception("[error creating directory][" + new_files_path +"]",e)

    # if we have good cfg and script files abd new directory
    if(opstat.get_status()) :

        #update cfg with new notebook name 
        from dfcleanser.common.cfg import NOTEBOOK_TITLE
        cfg_data.update({NOTEBOOK_TITLE:newnbname})

        # write out dicts to files
        new_config_file_path = os.path.join(cfg.get_notebook_path(),newnbname + "_files",newnbname + "_config.json")
        write_json_file(new_config_file_path,cfg_data,opstat)
        
        if(opstat.get_status()) :
            script_file_path = os.path.join(cfg.get_notebook_path(),newnbname + "_files",newnbname + "_scriptlog.json")
            write_json_file(script_file_path,script_data,opstat)

""" 
#------------------------------------------------------------------
#   rebame dfc files and _files dir
#------------------------------------------------------------------
"""
def rename_dfc_files(parms,opstat) :

    cfg_data            =   {}
    config_file_path    =   ""
    script_file_path    =   ""
    
    nbname      =   parms[0]
    newnbname   =   parms[1]
    
    verify_file_parms(parms,opstat)
    
    # check if files exist
    if(opstat.get_status()) :
        
        dfc_files_path = os.path.join(cfg.get_notebook_path(),nbname+"_files")

        # check if notebook _files exists 
        if(does_dir_exist(dfc_files_path)) : 
            
            config_file_path = os.path.join(dfc_files_path,nbname + "_config.json")
            if(does_file_exist(config_file_path)) : 
                cfg_data = read_json_file(config_file_path,opstat)
            
            if(opstat.get_status()) :
                script_file_path = os.path.join(dfc_files_path,nbname + "_scriptlog.json")
                if(not (does_file_exist(script_file_path)) ) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("[no _scriptlog.json file for ][" + nbname +"]")    
                
        else :
            opstat.set_status(False)
            opstat.opstat.set_errorMsg("[no _files dir for ][" + dfc_files_path +"]")    
        
    if(opstat.get_status()) :
        
        #update cfg with new notebook name 
        cfg_data.update({cfg.NOTEBOOK_TITLE:newnbname})
        
        #new_config_file_path = os.path.join(dfc_files_path,newnbname + "_config.json")
        os.chdir(dfc_files_path)
        os.rename(nbname + "_config.json",newnbname + "_config.json")  
        
        #new_script_file_path = os.path.join(dfc_files_path,newnbname + "_scriptlog.json")
        os.rename(nbname + "_scriptlog.json",newnbname + "_scriptlog.json")  
        os.chdir(cfg.get_notebook_path())
        #new_dfc_files_path = os.path.join(get_notebook_path(),newnbname +"_files")
        os.rename(nbname +"_files",newnbname +"_files")  
        
""" 
#------------------------------------------------------------------
#   delete dfc files and _files dir
#------------------------------------------------------------------
"""
def delete_dfc_files(parms,opstat) :

    nbname      =   parms[0]
    
    if(len(nbname) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("Notebook Name is invalid")
    
    # check if files exist
    if(opstat.get_status()) :
        
        dfc_files_path = os.path.join(cfg.get_notebook_path(),nbname+"_files")

        # check if notebook _files exists 
        if(does_dir_exist(dfc_files_path)) : 
            remove_files_from_dir(dfc_files_path,opstat)
            
            if(opstat.get_status()) :
                os.chdir(cfg.get_notebook_path())
                os.rmdir(dfc_files_path)

        else :
            opstat.set_status(False)
            opstat.opstat.set_errorMsg("[no _files dir for ][" + dfc_files_path +"]")    
        
""" 
#------------------------------------------------------------------
#   process dfc files and _files dir
#------------------------------------------------------------------
"""    
def process_dfc_files(funcid,parms) :

    opstat          =   opStatus()

    print("\n")
    
    if(funcid == sysm.COPY_FILES) :
               
        copy_dfc_files(parms,opstat) 
        if(opstat.get_status()) :
            display_status(parms[0] + " Dir and Cfg and Script files copied to " + cfg.get_notebook_path() + "\\" + parms[1] + "_files")            
        else :
            display_exception(opstat)
        
    elif(funcid == sysm.RENAME_FILES) :
    
        rename_dfc_files(parms,opstat) 
        if(opstat.get_status()) :
            display_status(parms[0] + " Dir and Cfg and Script files renamed to " + cfg.get_notebook_path() + "\\" + parms[1])            
        else :
            display_exception(opstat)
        
    elif(funcid == sysm.DELETE_FILES) :

        delete_dfc_files(parms,opstat) 
        if(opstat.get_status()) :
            display_status(parms[0] + " Dir and Cfg and Script files deleted for " + cfg.get_notebook_path() + "\\" + parms[0])            
        else :
            display_exception(opstat)
        
  
""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   system housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
def clear_system_data() :
    
    drop_owner_tables(cfg.System_ID)
    clear_system_cfg_values()
    
def clear_system_cfg_values() :
    
    cfg.drop_config_value(sysw.dfc_files_input_id+"Parms")
    cfg.drop_config_value(sysw.dfmgr_input_id+"Parms")
    cfg.drop_config_value(sysw.dfc_files_input_id+"Parms")
    cfg.drop_config_value(sysw.dfmgr_input_id+"ParmsProtect")
    
    return(True)
    
    
    





