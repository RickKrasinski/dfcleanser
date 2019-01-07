"""
# sw_utility_dfconcat_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
import json

this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_dfconcat_widgets as dfcw
import dfcleanser.sw_utilities.sw_utility_dfconcat_model as dfcm

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (opStatus, display_status, displayParms, display_exception)

from dfcleanser.scripting.data_scripting_control import add_to_script   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_dfconcat_utility(optionId,parms=None) :

    from IPython.display import clear_output
    clear_output()

    if(cfg.is_a_dfc_dataframe_loaded()) :  
        
        if(optionId == dfcm.DISPLAY_MAIN) :
        
            dfcw.get_concat_main_taskbar()
            #from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            #display_inspection_data()
            
            clear_sw_utility_dfconcatdata()
    
        elif(optionId == dfcm.DISPLAY_SIMPLE_CONCAT) :
            parmslist = dfcw.get_simple_concat_input_parms(parms)
            cfg.set_config_value(dfcw.df_concat_input_id+"Parms",parmslist)
            dfcw.display_simple_concat() 
        
        elif(optionId ==  dfcm.PROCESS_SIMPLE_CONCAT) :
            process_simple_concat(parms)
        
            
    else :
        
        dfcw.get_concat_main_taskbar()
        if(not(optionId == dfcm.DISPLAY_MAIN)) :
            from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            display_inspection_data()


def process_simple_concat(parms,display=True) :

    opstat  =   opStatus()
    dfcw.get_concat_main_taskbar()
    
    dfparms     =   dfcw.get_simple_concat_input_df_parms([parms[0],parms[1]])
    df1title    =   dfparms[0][0]
    df2title    =   dfparms[1][0]
    
    fparms = dfcw.get_simple_concat_input_parms(parms[2])
    
    dftoconcatto    =   fparms[0]
    caxis           =   0
    cjoin           =   0
    creset          =   False
    

    if( (len(dftoconcatto) == 0) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Invalid dataframes list specified : " + str(dftoconcatto))
    else :
        
        if(len(fparms[1]) == 0) :
            caxis   =   0
        else :
            if(fparms[1]=="1") :
                caxis = 1
            else :
                caxis = 0
        
        if(len(fparms[2]) == 0) :
            cjoin   =   'outer'
        else :
            if(fparms[2]=="inner") :
                cjoin = 'inner'
            else :
                cjoin = 'outer'
       
        if(len(fparms[3]) == 0) :
            creset   =   False
        else :
            if(fparms[4]=="True") :
                creset = True
            else :
                creset = True
            
    if(opstat.get_status()) :
        
        try :
            cdflist     =   []
            cdflist.append(cfg.get_dfc_dataframe(df1title))
            cdflist.append(cfg.get_dfc_dataframe(df2title))            
            
            import pandas as pd
            tmp = pd.concat(cdflist,axis=caxis,join=cjoin)
            
            if(creset) :
                print("reset row index")
                
            cfg.set_current_dfc_dataframe(tmp,fparms[0])
            
        except Exception as e:
            opstat.store_exception("Error concatenating dataframes : ",e)
                
    if(opstat.get_status()) :
            
        if(display) :
        
            #make scriptable
            add_to_script(["# concatenate dataframes ",
                           "from dfcleanser.sw_utilities.sw_utility_dfconcat_control import process_simple_concat",
                           "process_simple_concat(" + json.dumps(parms) + ",False)"],opstat)
            
            print("\n")
            display_status(" dataframes concatenated successfully and stored in " + fparms[0])
            displayParms("dataframe Concatenation Parms",dfcw.df_concat_input_labelList[:4],fparms,cfg.SWDFConcatUtility_ID,None,True)
                
    else :
        display_exception(opstat)           

    

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoders utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_sw_utility_dfconcatdata() :
    
    drop_owner_tables(cfg.SWDFConcatUtility_ID)
    clear_sw_utility_dfconcat_cfg_values()


def clear_sw_utility_dfconcat_cfg_values() :
 
    cfg.drop_config_value(dfcw.df_concat_df1_input_id+"Parms")
    cfg.drop_config_value(dfcw.df_concat_df2_input_id+"Parms")
    cfg.drop_config_value(dfcw.df_concat_input_id+"Parms")




    
    
    
    
    
    
    
    
    
    
    
    



