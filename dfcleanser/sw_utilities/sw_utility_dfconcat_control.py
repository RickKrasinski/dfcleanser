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
import dfcleanser.common.help_utils as dfchelp
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
    
    if(optionId == dfcm.DISPLAY_MAIN) :
        
        dfcw.get_concat_main_taskbar()
        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data()
            
        dfchelp.clear_help_text(dfchelp.DFCONCAT_HELP_BASE)
        clear_sw_utility_dfconcatdata()
    
    elif(optionId == dfcm.DISPLAY_SIMPLE_CONCAT) :
        parmslist = dfcw.get_simple_concat_input_parms(parms)
        cfg.set_config_value(dfcw.df_concat_input_id+"Parms",parmslist)
        dfcw.display_simple_concat() 
        
    elif(optionId ==  dfcm.DISPLAY_FULL_CONCAT) :
        parmslist = dfcw.get_full_concat_input_parms(parms)
        cfg.set_config_value(dfcw.df_fconcat_input_id+"Parms",parmslist)
        dfcw.display_full_concat()
            
    elif(optionId ==  dfcm.PROCESS_SIMPLE_CONCAT) :
        process_simple_concat(parms)
        
    elif(optionId ==  dfcm.PROCESS_FULL_CONCAT) :
        print("dfcw.PROCESS_FULL_CONCAT")

def process_simple_concat(parms,display=True) :

    opstat  =   opStatus()
    dfcw.get_concat_main_taskbar()
    
    # dataframe 1 : fparms[0] dataframe 2 : fparms[1] axis : fparms[2] join : fparms[3]
    fparms = dfcw.get_simple_concat_input_parms(parms)
    
    dflist      =   []
    caxis       =   0
    cjoin       =   0
    creset      =   False
    
    dflist  =   fparms[0].lstrip("[")
    dflist  =   dflist.rstrip("]")
    dflist  =   dflist.split(",")

    if( (len(dflist) < 2) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Invalid dataframes list specified : " + str(dflist))
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
            opstat.set_status(False)
            opstat.set_errorMsg("Invalid dataframe to store result in specified : ",fparms[3])
            
        if(len(fparms[4]) == 0) :
            creset   =   False
        else :
            if(fparms[4]=="True") :
                creset = True
            else :
                creset = True
            
    if(opstat.get_status()) :
        
        try :
            cdflist     =   []
            for i in range(len(dflist)) :
                cdflist.append(cfg.get_dc_dataframe(dflist[i]))

            import pandas as pd
            tmp = pd.concat(cdflist,axis=caxis,join=cjoin)
            
            if(creset) :
                print("reset row index")
                
            cfg.set_dc_dataframe(tmp,fparms[3])
        except Exception as e:
            opstat.store_exception("Error concatenating dataframes : ",e)
                
    if(opstat.get_status()) :
            
        if(display) :
        
            #make scriptable
            add_to_script(["# concatenate dataframes ",
                           "from dfcleanser.sw_utilities.sw_utility_dfconcat_control import process_simple_concat",
                           "process_simple_concat(" + json.dumps(parms) + ",False)"],opstat)
            
            print("\n")
            display_status(" dataframes concatenated successfully and stored in " + fparms[3])
            displayParms("dataframe Concatenation Parms",dfcw.df_concat_input_labelList[:5],fparms,cfg.SWDFConcatUtility_ID,None,True)
                
    else :
        display_exception(opstat)           

def process_full_concat(parms,display=True) :

    opstat  =   opStatus()
    dfcw.get_concat_main_taskbar()
    
    # dataframe 1 : fparms[0] dataframe 2 : fparms[1] axis : fparms[2] join : fparms[3]
    fparms = dfcw.get_full_concat_input_parms(parms)
    
    try :
        if(len(fparms[1]) == 0) :   axis = 0
        else :                      axis = int(fparms[1])
            
        if(len(fparms[2]) == 0) :   join = 'outer'
        else :                      join = fparms[2]
        
        if(len(fparms[3]) == 0) :   joinaxes = []
        else :                      
            joinaxes    =   fparms[3].lstrip("[")
            joinaxes    =   joinaxes.rstrip("]")
            joinaxes    =   joinaxes.split(",")
            
        if(len(fparms[4]) == 0) :   ignoreindex = False
        else : 
            if(fparms[4] == "True") : ignoreindex = True
            else                    : ignoreindex = False
            
        if(len(fparms[5]) == 0) :   keys = None
        else :                      keys = json.loads(fparms[5])
            
        if(len(fparms[6]) == 0) :   levels = None
        else :                      levels = json.loads(fparms[6])
        
        if(len(fparms[7]) == 0) :   names = None
        else :                      names = json.loads(fparms[7])
        
        if(len(fparms[8]) == 0) :   vintegrity = False
        else :                      
            if(fparms[8] == "True") : vintegrity = True
            else                    : vintegrity = False
        
        if(len(fparms[9]) == 0) :   sort = None
        else :                      
            if(fparms[9] == "True") : sort = True
            else                    : sort = False
        
        if(len(fparms[10]) == 0) :   copy = None
        else :                      
            if(fparms[10] == "True")    : copy = True
            else                        : copy = False
        
        if(len(fparms[11]) == 0) :  dfname = 'full_Concat'
        else                     :  dfname = fparms[11]
        
        if(len(fparms[12]) == 0) :   adds = False
        else :                      
            if(fparms[12] == "True")    : adds = True
            else                        : adds = False
            
    except Exception as e:
        opstat.store_exception("Error concatenating dataframes : ",e)
    
    if(opstat.get_status()) :
        
        try :
            
            import pandas as pd

            cdf     =   pd.concat(json.loads(fparms[0]),axis,join,joinaxes,ignoreindex,
                                             keys,levels,names,vintegrity,sort,copy)
            
            cfg.set_dc_dataframe(dfname,cdf) 
            
        except Exception as e:
            opstat.store_exception("Error concatenating dataframes : ",e)
    
    if(opstat.get_status()) :
            
        if(display) :
        
            if(adds) :
                #make scriptable
                add_to_script(["# concatenate dataframes ",
                               "from dfcleanser.sw_utilities.sw_utility_dfconcat_control import process_full_concat",
                               "process_full_concat(" + json.dumps(parms) + ",False)"],opstat)
            
            print("\n")
            display_status(" dataframes concatenated successfully and stored in " + dfname)
            displayParms("dataframe Concatenation Parms",dfcw.df_fconcat_input_labelList[:13],fparms,cfg.SWDFConcatUtility_ID,None,True)
                
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
 
    #drop_config_value(ADDR_CONV_COL_LIST_PARM)
    return




    
    
    
    
    
    
    
    
    
    
    
    



