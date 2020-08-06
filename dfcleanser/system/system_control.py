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

import dfcleanser.common.cfg as cfg
import dfcleanser.system.system_widgets as sysw
import dfcleanser.system.system_model as sysm

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (display_status, run_jscript, opStatus)

def isEULA_read() :
    
    if(cfg.get_config_value(cfg.EULA_FLAG_KEY) == 'true') :
        return(True)
    else :
        return(False)

def display_main_tb() :

    sysw.display_system_main_taskbar()
    
        
def load_dfcleanser_from_toolbar(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : load dfcleanser from a notebook toolbar
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    nbname      =   parms[0]
    dfcmode     =   parms[1]
    
    from dfcleanser.system.load import load_dfcleanser_from_toolbar
    load_dfcleanser_from_toolbar(nbname,dfcmode)

    
def load_dfCleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : load dfcleanser from a code cell
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from dfcleanser.system.load import load_dfcleanser
    load_dfcleanser()
    

def unload_dfCleanser() :
    
    from dfcleanser.system.load import unload_dfcleanser
    unload_dfcleanser()
    
    jscript     =   ("complete_unload_dfcleanser()")
    run_jscript(jscript,"Error Loading dfcleanser " + "Error unLoading dfcleanser")
    
    
def display_system_environment(funcId,parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : display system environment screens
    * 
    * parms :
    *  funcId   - display func id
    *  parms    - associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    

    if(not (cfg.check_if_dc_init()) ) :
        sysw.display_system_main_taskbar()

        return
        
    else :
        
        from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
        if(not (are_owner_inputs_defined(cfg.System_ID)) ) :
            define_inputs(cfg.System_ID,sysw.system_inputs)
        
        if(funcId == sysm.DISPLAY_MAIN) :
            display_main_tb()
            clear_system_data()            
    
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
            
            parms[0]    =   parms[0].replace("[","") 
            parms[0]    =   parms[0].replace("]","")
            
            utils_cbs   =   parms[0].split(",")
            
            utilscbs    =   []
            
            for i in range(len(utils_cbs)) :
                if(utils_cbs[i] == '"True"') :
                    utilscbs.append(1)
                else :
                    utilscbs.append(0)
            
            from dfcleanser.system.load import reload_dfcleanser
            reload_dfcleanser([utilscbs])
            
            clear_cell()
            
            sysw.display_system_main_taskbar()
        
        elif(funcId == sysm.DISPLAY_DATAFRAMES) :
            
            if(not(parms is None)) :
                title = parms[0]
            else :
                title = None
                
            sysw.display_system_main_taskbar()
            sysw.display_df_dataframes(title)

        elif(funcId == sysm.DISPLAY_ADD_DATAFRAME) :
                
            sysw.display_system_main_taskbar()
            cfg.drop_config_value(sysw.dfmgr_add_input_id+"Parms")
            sysw.display_add_df_input()
            
        elif(funcId == sysm.PROCESS_DATAFRAME) :
            
            fid     =   parms[0]
            from dfcleanser.common.common_utils import get_parms_for_input
            fparms  =   get_parms_for_input(parms[1],sysw.dfmgr_input_idList)
            
            dftitle     =   None
            
            if(fid == sysm.DROP_DATAFRAME) :
                cfg.drop_dfc_dataframe(fparms[0])
                
            elif(fid == sysm.SET_DATAFRAME) :  
                print("sysm.SET_DATAFRAME")
                
            elif(fid == sysm.UPDATE_DATAFRAME) :    
                cfg.set_dfc_dataframe_notes(fparms[0],fparms[3])
                dftitle     =   fparms[0]
            
            elif(fid == sysm.RENAME_DATAFRAME) :    
                cfg.rename_dfc_dataframe(cfg.get_config_value(cfg.CURRENT_DF_DISPLAYED_KEY),fparms[0])
                dftitle     =   fparms[0]
                
            sysw.display_system_main_taskbar()
            sysw.display_df_dataframes(dftitle)
            
        elif(funcId == sysm.PROCESS_ADD_DATAFRAME) :
            
            opstat  =   opStatus()
            
            from dfcleanser.common.common_utils import get_parms_for_input
            fparms  =   get_parms_for_input(parms[1],sysw.dfmgr_add_input_idList)
            
            dftitle     =   fparms[0]
            dfobject    =   fparms[1]
            dfnotes     =   fparms[2]
            
            if(not (len(dftitle)) > 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid df title parm")
            
            else :
                
                if(len(dfobject) > 0) :

                    try :

                        add_df_js = ("add_new_dfc_df('" + dftitle + "', '" +  dfobject + "', '" + dfnotes + "');")
                        run_jscript(add_df_js,"fail to add dataframe : ")
                        
                    except Exception :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Unable to add df to dfc manager : " + str(sys.exc_info()[0].__name__))
               
                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid df name parm")
            
            if(opstat.get_status()) :
                sysw.display_df_dataframes(dftitle)
            else :
                display_status(opstat.get_errorMsg())
                sysw.display_add_df_input()
            
        elif(funcId == sysm.DISPLAY_SYSTEM) :
            display_main_tb()
            sysw.show_sys_info()
            
        elif(funcId == sysm.DISPLAY_OFFLINE) :
            display_main_tb()
            sysw.display_offline()
            
        elif(funcId == sysm.DISPLAY_ABOUT) :
            sysw.display_system_main_taskbar()
            sysw.show_about_info()
            
        elif(funcId == sysm.DISPLAY_DFC_FILES) :
            sysw.display_system_main_taskbar()
            sysw.display_dfc_files_form()

        elif(funcId == sysm.DISPLAY_EULA) :
            display_main_tb() 
            sysw.display_EULA()
            
        elif(funcId == sysm.DISPLAY_README) :
            display_main_tb()            
            sysw.display_README()
            
        elif(funcId == sysm.PROCESS_EULA) :
            display_main_tb()
            cfg.set_config_value(cfg.EULA_FLAG_KEY,"true")
            
        elif(funcId == sysm.EXIT_SETUP) :
            from dfcleanser.system.load import unload_dfcleanser
            unload_dfcleanser()
        
        return
    
def clear_cell() :  
    run_jscript("process_system_tb_callback(0)","Javascript Error : clear_cell")
     


def initialize_notebook() :
    """
    * -------------------------------------------------------------------------- 
    * function : initialize dfcleanser notebooj cells
    * 
    * parms :
    *  funcId   - display func id
    *  parms    - associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
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
    
    
def clear_data() :
    """
    * -------------------------------------------------------------------------- 
    * function : clear data
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.scripting.data_scripting_widgets import drop_current_script, set_script_logging 
    
    set_script_logging()
    drop_current_script()

    initialize_notebook()
    
    reset_js = "window.initialize_dc();"
    
    run_jscript(reset_js,
                "fail to clear data : ",
                 "system clear data")




    
""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   system housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
def clear_system_data() :
    
    drop_owner_tables(cfg.System_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.System_ID)
    clear_system_cfg_values()
    
def clear_system_cfg_values() :
    
    cfg.drop_config_value(sysw.dfmgr_input_id+"Parms")
    cfg.drop_config_value(sysw.dfmgr_input_id+"ParmsProtect") 

    return(True)
    
    
"""
* ----------------------------------------------------
# dfcleanser crypto class 
* ----------------------------------------------------
""" 

#from Crypto.Cipher import AES
import base64
     
def encode(clear_text) :
    
    key     =   crypto_key.get_cryptokey()
    enc     =   []
    for i in range(len(clear_text)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear_text[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(enc_text) :   
    
    key     =   crypto_key.get_cryptokey()
    dec     =   []
    enc = base64.urlsafe_b64decode(enc_text).decode()
    for i in range(len(enc_text)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
    

class Crypto_Key :
    
    # instance variables
    cryptokey                   =   None
    
    # full constructor
    def __init__(self) :
        self.cryptokey          =   None
        
    def set_cryptokey(self,cryptokey) :
        self.cryptokey  =   cryptokey

    def get_cryptokey(self) :
        return(self.cryptokey)
   

crypto_key     =   Crypto_Key()        





