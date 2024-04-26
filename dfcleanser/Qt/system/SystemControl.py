"""
# SystemControl
 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

DEBUG_SYSTEM    =   False


import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg

from dfcleanser.common.common_utils import (run_jscript)

def isEULA_read() :
    
    if(cfg.get_config_value(cfg.EULA_FLAG_KEY) == 'true') :
        return(True)
    else :
        return(False)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Load the dfcleanser extension                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def load_dfcleanser_from_toolbar(parms) :
    """
    * --------------------------------------------------------
    * function : add the dfcleanser console cell
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    nbname      =   parms[0]
    
    cfg.set_notebookName(nbname)
    
    jscript     =   ("add_dfcleanser_chapter(" + str(cfg.DC_CONSOLE_ID) + ");")
    run_jscript(jscript,"Error Loading dfcleanser console")
    


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Load the dfcleanser extension end              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


    
def display_dfc_console() :
    
    from dfcleanser.sw_utilities.DisplayUtils import get_chapter_console_html
    console_htmls   =  get_chapter_console_html(cfg.DC_CONSOLE_ID)

    gridclasses     =   ["dfc-top","dfc-left","dfc-right"]
    gridhtmls       =   [console_htmls[0],console_htmls[1],console_htmls[2]]
      
    from dfcleanser.common.common_utils import display_generic_grid
    display_generic_grid("dfcleanser-console-wrapper",gridclasses,gridhtmls)



def display_system_environment(funcId,parms=None) :
    """
    * ------------------------------------------------------------------------- 
    * function : display system environment screens
    * 
    * parms :
    *  funcId   - display func id
    *  parms    - associated parms
    *
    * returns : 
    *  N/A
    * -------------------------------------------------------------------------
    """
    
    try :

        option_string   =   str(funcId) 

    except :

        #display_system_console()
        #clear_system_data()  
 
        if(DEBUG_SYSTEM) :
            print("[SystemControl][display_system_environment] Invalid option for  display_system_environment : ",funcId,parms)
 
        return


    if(DEBUG_SYSTEM) :
        print("[SystemControl][display_system_environment]",funcId,parms,cfg.check_if_dc_init())
    
    DISPLAY_DFC_CONSOLE = -1
    if(funcId == DISPLAY_DFC_CONSOLE) :
        display_dfc_console()
        return


def initialize_notebook() :
    """
    * ------------------------------------------------------------------------- 
    * function : initialize dfcleanser notebooj cells
    * 
    * parms :
    *  funcId   - display func id
    *  parms    - associated parms
    *
    * returns : 
    *  N/A
    * -------------------------------------------------------------------------
    """
     
    clear_system_data()
    
    import matplotlib.pyplot as plt
    
    
def clear_data() :
    """
    * ------------------------------------------------------------------------- 
    * function : clear data
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * ------------------------------------------------------------------------
    """
    
    initialize_notebook()
    
    
""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   system housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
def clear_system_data() :
    
    clear_system_cfg_values()
    
def clear_system_cfg_values() :
    
    cfg.drop_config_value(cfg.CURRENT_DFC_DF_DFTITLE)
    cfg.drop_config_value(cfg.CURRENT_DFC_DF_RUN_STEP)
    cfg.drop_config_value(cfg.CURRENT_DFC_DF_RUN_TSTAMPS)
   


    return(True)
    
    
"""
* ----------------------------------------------------
# dfcleanser crypto class 
* ----------------------------------------------------
""" 

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





