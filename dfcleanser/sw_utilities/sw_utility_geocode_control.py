"""
# sw_utility_geocode_control 
"""

# -*- coding: utf-8 -*-

"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw
import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_control as subgc
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_console as subgcs

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (get_parms_for_input, display_exception, display_status, 
                                            display_notes, opStatus, RunningClock, log_debug_dfc,
                                            does_dir_exist, does_file_exist, delete_a_file,
                                            display_generic_grid)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar control function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def process_bulk_geocoding_run_cmd(command, parms=None) :
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"geocode : process_bulk_geocoding_run_cmd " + str(command) + " parms : " + str(parms))

    subgc.process_bulk_geocoding_run_cmd(command, parms)
    

def get_geocoding_connect_parms(geocid,gmode,fparms) :
    
    if(gmode == sugm.INTERACTIVE) :
            
        if(geocid == sugm.ArcGISId)         :   ids =   sugw.arcgis_geocoder_idList
        elif(geocid == sugm.BaiduId)        :   ids =   sugw.baidu_geocoder_idList
        elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
        elif(geocid == sugm.GoogleId)       :   ids =   sugw.google_geocoder_idList
        elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
        elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
        inputs  =   get_parms_for_input(fparms,ids)
                
        if(len(inputs) > 0) :
            cfg.set_config_value(sugw.get_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

    else :
            
        if(geocid == sugm.ArcGISId)         :   ids =   subgw.batch_arcgis_geocoder_idList
        elif(geocid == sugm.BaiduId)        :   ids =   sugw.baidu_geocoder_idList
        elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
        elif(geocid == sugm.GoogleId)       :   ids =   subgw.google_bulk_geocoder_idList
        elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
        elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
        inputs  =   get_parms_for_input(fparms,ids)
                
        if(len(inputs) > 0) :
            cfg.set_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

    
    return(inputs)

def get_geocid_from_formid(formid) :
    
    if( (formid == "googlegeocoder")  or (formid == "googlequery") or (formid == "googlereverse") or 
        (formid == "googlebulkgeocoder") or (formid == "googlebulkquery") or (formid ==  "googlebulkreverse") ) :   return(sugm.GoogleId)
    elif( (formid == "arcgisgeocoder")  or (formid == "arcgisquery") or (formid == "arcgisreverse") or 
          (formid == "arcgisbatchgeocoder") or (formid == "arcgisbatchquery") ) :                                   return(sugm.ArcGISId)
    elif( (formid == "baidugeocoder")  or (formid == "baiduquery") or (formid == "baidureverse") or 
          (formid == "baidubulkgeocoder") or (formid == "baidubulkquery") ) :                                       return(sugm.BaiduId)
    elif( (formid == "binggeocoder")  or (formid == "bingquery") or (formid == "bingreverse") or 
          (formid == "bingbulkgeocoder") or (formid == "bingbulkquery") ) :                                         return(sugm.BingId)
    elif( (formid == "mapquestgeocoder")  or (formid == "mapquestquery") or (formid == "mapquestreverse") ) :       return(sugm.OpenMapQuestId)
    elif( (formid == "nomingeocoder")  or (formid == "nominquery") or (formid == "nominreverse") ) :                return(sugm.NominatimId)
    else :                                                                                                          return(None)
 

def display_geocode_utility(optionId,parms=None) :
    """
    * ---------------------------------------------------------
    * function : main geocode process function
    * 
    * parms :
    *  optionId  - geocoder option to process
    *  parms     - option parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    if(1):#not( (optionId == sugm.BULK_START_GEOCODER) or (optionId == sugm.BULK_STOP_GEOCODER)  or 
            #(optionId == sugm.BULK_PAUSE_GEOCODER) or (optionId == sugm.BULK_RESUME_GEOCODER)  or 
            #(optionId == sugm.BULK_VIEW_ERRORS) ) ) :
        from IPython.display import clear_output
        clear_output()
        
    if(not (cfg.is_a_dfc_dataframe_loaded())) :
        cfg.drop_config_value(cfg.CURRENT_GEOCODE_DF)


    if(not cfg.check_if_dc_init()) :
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
    else :
        
        from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
        if(not (are_owner_inputs_defined(cfg.SWGeocodeUtility_ID)) ) :
            
            swu_geoocode_inputs     =   []
            
            for i in range(len(subgw.SWUtility_bulk_geocode_inputs)) :
                swu_geoocode_inputs.append(subgw.SWUtility_bulk_geocode_inputs[i])    
                
            for i in range(len(subgcs.SWUtility_bulk_geocode_console_inputs)) :
                swu_geoocode_inputs.append(subgcs.SWUtility_bulk_geocode_console_inputs[i])    
                
            for i in range(len(sugw.SWUtility_geocode_inputs)) :
                swu_geoocode_inputs.append(sugw.SWUtility_geocode_inputs[i])    
                
            define_inputs(cfg.SWGeocodeUtility_ID,swu_geoocode_inputs)

    if(optionId == sugm.DISPLAY_MAIN_GEOCODING) :
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
        
    # geoocode utils display
    elif(optionId == sugm.BULK_EXIT_GEOCODER) :
        
        opstat  =   opStatus()
        
        cfg.drop_dfc_dataframe(sugm.GEOCODING_RESULTS_DF_TITLE)
        cfg.drop_dfc_dataframe(sugm.GEOCODING_ERROR_LOG_DF_TITLE)
        
        # delete checkpoint files
        import os
        
        chckpt_file_path_name  =   os.path.join(cfg.get_notebookPath(),"PandasDataframeCleanser_files")
        chckpt_file_path_name  =   os.path.join(chckpt_file_path_name,"geocode_checkpoints")
        
        df_source       =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
        
        file_name       =   cfg.get_notebookName() + "_" + df_source + "_checkpoint"
        
        if(does_dir_exist(chckpt_file_path_name)) :   
            
            for i in range(100) :
                
                chckpt_file_name    =   file_name + str(i) + ".csv"
                chckpt_file_name    =   os.path.join(chckpt_file_path_name,chckpt_file_name) 
                
                if(does_file_exist(chckpt_file_name)) :
                    
                    delete_a_file(chckpt_file_name,opstat)
                    chckpt_file_name    =   chckpt_file_name.replace(".csv","_backup.csv")
                    delete_a_file(chckpt_file_name,opstat)
                    
                else :
                    break
            
        
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
        
        notes     =   ["Bulk Geocode Results, Error and Checkpoint files removed"]
        display_notes(notes,True)

         
    # geoocode utils display
    elif(optionId == sugm.DISPLAY_GEOUTILS) :
        
        from dfcleanser.common.common_utils import is_web_connected
        if(not (is_web_connected())) :
            
            sugw.display_geocode_main_taskbar()        
            clear_sw_utility_geocodedata() 
            print("\n")
            display_status("Geocoding is unavailable since web is not connected")
            
        else :

            sugw.display_geocode_utils_taskbar()        
    
    elif(optionId ==  sugm.DISPLAY_DISTANCE) :
        clear_output() 
        sugw.display_calc_distance_input_form(sugm.GEOCODE_ADDRESS)
    
    elif(optionId ==  sugm.DISPLAY_COORD_DISTANCE) :
        clear_output() 
        sugw.display_calc_distance_input_form(sugm.GEOCODE_COORDS)

    elif(optionId ==  sugm.DISPLAY_DF_DISTANCE) :
        
        if(cfg.is_a_dfc_dataframe_loaded()) :
            
            clear_output()        
            sugw.display_calc_df_distance_input_form()
            
        else :
            
            opstat  =   opStatus()
            
            sugw.display_geocode_main_taskbar() 
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe is imported which is required for df distance processing. ")
            display_exception(opstat)
    
    elif(optionId ==  sugm.REFRESH_DF_DISTANCE) :
        
        clear_output()  
        
        fparms  =   get_parms_for_input(parms,sugw.addr_df_dist_utility_input_idList)
        cfg.set_config_value(sugw.addr_df_dist_utility_input_id+"Parms",fparms)
        sugw.display_calc_df_distance_input_form()
    
    elif(optionId ==  sugm.DISPLAY_CENTER) :
        clear_output() 
        sugw.display_calc_center_input_form()
        
    elif(optionId ==  sugm.REFRESH_CENTER) :
        
        clear_output()
        
        fparms  =   get_parms_for_input(parms,sugw.addr_center_utility_input_idList)
        cfg.set_config_value(sugw.addr_center_utility_input_id+"Parms",fparms)
        sugw.display_calc_center_input_form()

    elif(optionId ==  sugm.DISPLAY_DIST_CENTER) :
        clear_output()        
        sugw.display_calc_df_center_dist_input_form()

    elif(optionId ==  sugm.REFRESH_DISTANCE_CENTER) :
        clear_output()

        sugw.display_calc_df_center_dist_input_form(parms)

    # geoocode utils process
    elif(optionId ==  sugm.PROCESS_DISTANCE) :
        sugw.display_geocode_main_taskbar() 
        print("\n")
        process_distance(parms,sugm.GEOCODE_ADDRESS)
        
    elif(optionId ==  sugm.PROCESS_COORD_DISTANCE) :
        sugw.display_geocode_main_taskbar() 
        print("\n")
        process_distance(parms,sugm.GEOCODE_COORDS)

    elif(optionId ==  sugm.PROCESS_DF_DISTANCE) :
        sugw.display_geocode_main_taskbar() 
        print("\n")
        process_df_distance(parms)
        
    elif(optionId ==  sugm.PROCESS_CENTER) :
        sugw.display_geocode_main_taskbar() 
        print("\n")
        process_center(parms)    

    elif(optionId ==  sugm.PROCESS_DIST_CENTER) :
        sugw.display_geocode_main_taskbar() 
        print("\n")
        process_df_center_dist(parms)    
        
    
    elif(optionId ==  sugm.DISPLAY_TUNING) :
        clear_output() 
        sugw.display_bulk_tune_input_form()
    
    elif(optionId ==  sugm.PROCESS_TUNING) :
        sugw.display_geocode_main_taskbar() 

    elif(optionId == sugm.PROCESS_GEOCODER) :

        geocid  =   None
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            
        elif(fid == 1)  :   
            sugw.display_geocode_inputs(parms,sugm.QUERY)
            
    
    # show full parameters for geocoding parms in a grid
    elif(optionId == sugm.DISPLAY_FULL_GEOCODING) :

        
        formid  =   parms[0]        
        geocid  =   get_geocid_from_formid(formid)

        if( (formid == "arcgisgeocoder") or 
            (formid == "googlegeocoder") or
            (formid == "binggeocoder") or
            (formid == "baidugeocoder") or
            (formid == "mapquestgeocoder") or
            (formid == "nomingeocoder") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.GEOCODER
            
        elif( (formid == "arcgisquery") or 
              (formid == "googlequery") or
              (formid == "bingquery") or
              (formid == "baiduquery") or
              (formid == "mapquestquery") or
              (formid == "nominquery") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.QUERY

        elif( (formid == "arcgisreverse") or 
              (formid == "googlereverse") or
              (formid == "bingreverse") or
              (formid == "baidureverse") or
              (formid == "mapquestreverse") or
              (formid == "nominreverse") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.REVERSE
            
        elif( (formid == "arcgisbatchgeocoder") or 
              (formid == "googlebulkgeocoder") or
              (formid == "bingbulkgeocoder") or 
              (formid == "baidubulkgeocoder") ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.GEOCODER

        elif( (formid == "arcgisbatchquery") or 
              (formid == "googlebulkquery") or
              (formid == "bingbulkquery") or
              (formid == "baidubulkquery") ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.QUERY
        
        elif( (formid == "googlebulkreverse")  or 
              (formid == "bingbulkreverse")  or
              (formid == "baidubulkreverse")  ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.REVERSE
        
        if(formid == "googlebulkquery") :
            
            tableid     =   int(parms[1]) 
            subgw.display_bulk_geocode_inputs(sugm.GoogleId,gtype,tableid,True)
        
        else :
            
            if(gtype == sugm.GEOCODER) :
                if(gmode == sugm.INTERACTIVE) :
                    sugw.display_geocoders(geocid,True,False)
                else :
                    subgw.display_bulk_geocoders(geocid,True)
                
            else :
                if(gmode == sugm.INTERACTIVE) :
                    sugw.display_geocode_inputs(geocid,gtype,True)
                else :
                    subgw.display_bulk_geocoding(geocid,gtype)

    elif(optionId == sugm.PROCESS_GEOCODING) :
        
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        fparms  =   parms[3]

        sugw.display_geocode_main_taskbar()        
        
        if(gmode == sugm.INTERACTIVE) :
            if(gtype == sugm.QUERY) :
                run_geocoder_query(geocid,fparms)
            else :
                run_geocoder_reverse(geocid,fparms)                
        else :
            if(cfg.is_a_dfc_dataframe_loaded()) :
                if(gtype == sugm.QUERY) :
                    subgc.get_bulk_coords(geocid,fparms)
                else :
                    subgc.get_bulk_addresses(geocid,fparms)
            else :
                display_status("No Dataframe Loaded to run bulk geocoding")

    elif(optionId == sugm.DISPLAY_GEOCODING) :
        
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        fparms  =   parms[3]
        
        inputs  =   get_geocoding_connect_parms(geocid,gmode,fparms)
        
        if(gmode == sugm.INTERACTIVE) :
            sugw.display_geocode_inputs(geocid,gtype)
        else :
            subgw.display_bulk_geocoding(geocid,gtype)

    elif(optionId == sugm.TEST_GEOCODER) :
        
        geocid  =   int(parms[0])
        gmode   =   int(parms[1])
        
        inputs  =   get_geocoding_connect_parms(geocid,gmode,parms[2])
        
        if(gmode == sugm.INTERACTIVE) :
            test_geocoder(geocid,inputs)
        else :
            subgc.test_bulk_geocoder(geocid,inputs)
   
    elif(optionId == sugm.CLEAR_GEOCODE_FORM) :
        
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        
        if(gmode == sugm.INTERACTIVE) :
            cfg.drop_config_value(sugw.get_form_id(geocid,gtype) + "Parms")
            
            if(gtype == sugm.GEOCODER) :
                sugw.display_geocoders(geocid)
            else :
                sugw.display_geocode_inputs(geocid,gtype)
                
        else :
            cfg.drop_config_value(subgw.get_bulk_form_id(geocid,gtype) + "Parms")
            
            if(gtype == sugm.GEOCODER) :
                subgw.display_bulk_geocoders(geocid)
            else :
                subgw.display_bulk_geocode_inputs(geocid,gtype)
                
    elif(optionId == sugm.DISPLAY_GEOCODER) :
        
        from dfcleanser.common.common_utils import is_web_connected
        if(not (is_web_connected())) :
            
            sugw.display_geocode_main_taskbar()        
            clear_sw_utility_geocodedata() 
            print("\n")
            display_status("Geocoding is unavailable since web is not connected")
            
        else :
                
            geocid  =   int(parms[0])
            if(geocid == -1) :
                geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
                if(geocid == None) :
                    geocid  =   sugm.GoogleId
        
            gmode   =   int(parms[1])
                
            if(gmode == sugm.INTERACTIVE) :
                sugw.display_geocoders(geocid)
            elif(gmode == sugm.BULK) :
                subgw.display_bulk_geocoders(geocid)
            else :
                print("display bulk tuning")
 
    elif(optionId == sugm.GET_TABLE) :
        tableid =   int(parms[0])
        geocid  =   int(parms[1])
        gtype   =   int(parms[2])
        gmode   =   int(parms[3])
        fparms  =   parms[4]
        
        if(gmode == sugm.INTERACTIVE) :
            sugw.display_geocode_inputs(geocid,gtype)

        else :
            
            showfull =  False
            
            if(geocid == sugm.GoogleId) :
                if(gtype == sugm.QUERY) :
                    inputs  =   get_parms_for_input(fparms,subgw.bulk_google_query_input_idList)
                    if(len(inputs) > 0) :
                        cfg.set_config_value(subgw.bulk_google_query_input_id + "Parms",inputs)
                        
                    if( (tableid == sugm.LOCATION_TYPES_TABLE) or (tableid == sugm.COLNAMES_TABLE) )  :
                        showfull =  True    
                else :
                    inputs  =   get_parms_for_input(fparms,subgw.bulk_google_reverse_input_idList)
                    if(len(inputs) > 0) :
                        cfg.set_config_value(subgw.bulk_google_reverse_input_id + "Parms",inputs)
            
            subgw.display_bulk_geocode_inputs(geocid,gtype,tableid,showfull)



    #"""
    #--------------------------------------------------------------------------
    #   bulk geocoding run  functions
    #--------------------------------------------------------------------------
    #"""
       
    elif(optionId == sugm.CHANGE_BULK_GEOCODER) :
        
        geocid = None
        
        if(parms != None) :
            for i in range(len(sugm.supported_Geocoders)) :
                if(sugm.get_geocoder_title(sugm.supported_Geocoders[i]) == parms) :
                    geocid = sugm.supported_Geocoders[i]
                    
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid,True)
        
        optype = cfg.get_config_value(cfg.BULK_GEOCODE_MODE_KEY)
        if(optype == None) :
            optype = sugm.QUERY
        else :
            if(optype == sugm.QUERY) :
                optype = sugm.QUERY
            else :
                optype = sugm.REVERSE 
                
        subgw.display_bulk_geocoding(geocid,optype)
                   
    elif(optionId == sugm.DISPLAY_BULK_GEOCODER) :
        
        geocid = None
        
        if(parms != None) :
            for i in range(len(sugm.supported_Bulk_Geocoders)) :
                if(sugm.get_geocoder_title(sugm.supported_Bulk_Geocoders[i]) == parms) :
                    geocid = sugm.supported_Bulk_Geocoders[i]
                    
        subgw.display_bulk_geocoders(geocid,False)
    
    elif(optionId == sugm.PROCESS_BULK_GEOCODER) :

        geocid  =   None
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            
        if(fid == 5)    :  
            
            if(geocid == sugm.ArcGISId)         :   ids =   subgw.batch_arcgis_geocoder_idList
            elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
            elif(geocid == sugm.GoogleId)       :   ids =   subgw.google_bulk_geocoder_idList
            elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
            elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
            inputs  =   get_parms_for_input(parms[2],ids)
                
            if(len(inputs) > 0) :
                cfg.set_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

            subgc.test_bulk_geocoder(geocid,inputs)
        
        elif(fid == 6)  :   
            subgw.display_bulk_geocode_inputs(geocid,sugm.QUERY)            
        
        elif(fid == 7)  : 
            sugw.display_geocoders(geocid) 
            
        elif(fid == 8)  :
            cfg.drop_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms")
            subgw.display_bulk_geocoders(geocid,False)
            
    elif(optionId == sugm.PROCESS_BULK_RESULTS) :
        
        sugw.display_geocode_main_taskbar()        

        opstat  =   opStatus()
        
        cmd     =   parms[0] 
        
        if(cmd == sugm.DISPLAY_BULK_RESULTS_RETURN) : 
            
            subgc.refresh_bulk_geocode_console()
            
        elif((cmd == sugm.DISPLAY_BULK_RESULTS_APPEND) or 
             (cmd == sugm.DISPLAY_BULK_RESULTS_EXPORT_CSV)) : 

            subgcs.display_geocoder_process_results(cmd,opstat)
            
        elif(cmd == sugm.DISPLAY_BULK_RESULTS) : 
            subgcs.display_geocoder_process_results(cmd,opstat,True)
            
        elif(cmd == sugm.DISPLAY_BULK_RESULTS_EXPORT_SQL) :
            
            from dfcleanser.data_export.data_export_widgets import pandas_export_sqltable_id
            exportParms     =   cfg.get_config_value(pandas_export_sqltable_id+"Parms")

            if(exportParms == None) :
                exportParms     =   [sugm.GEOCODING_RESULTS_DF_TITLE,"","","","","","","",""]
            else :
                exportParms[0]  =   sugm.GEOCODING_RESULTS_DF_TITLE 

            cfg.set_config_value(pandas_export_sqltable_id+"Parms",exportParms)
            
            
        elif(cmd == sugm.PROCESS_BULK_RESULTS_APPEND_CLEAR) :
            
            cfg.drop_config_value(subgcs.bulk_geocode_append_input_id + "Parms")
            subgcs.display_geocoder_process_results(cmd,opstat)
            
        elif(cmd == sugm.PROCESS_BULK_RESULTS_APPEND_RETURN) :
            
            subgcs.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_BASE,opstat)
        
        elif(cmd == sugm.PROCESS_BULK_RESULTS_CSV_CLEAR) :
            
            cfg.drop_config_value(subgcs.bulk_geocode_export_input_id + "Parms")
            subgcs.display_geocoder_process_results(cmd,opstat)
            
        elif(cmd == sugm.PROCESS_BULK_RESULTS_CSV_RETURN) :
            
            subgcs.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_BASE,opstat)
        
        elif(cmd == sugm.DISPLAY_BULK_SOURCE_DF) :
            
            subgcs.display_geocoder_process_results(sugm.DISPLAY_BULK_SOURCE_DF,opstat)
        
        elif(cmd == sugm.DISPLAY_BULK_RESULTS_DF) :
            
            subgcs.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_DF,opstat)
        
        elif(cmd == sugm.DISPLAY_BULK_ERRORS_DF) :
            
            subgcs.display_geocoder_process_results(sugm.DISPLAY_BULK_ERRORS_DF,opstat)
            
        elif(cmd == sugm.PROCESS_BULK_RESULTS_APPEND_PROCESS) :
            subgc.process_geocode_final_results(cmd,parms)
            
        elif(cmd == sugm.PROCESS_BULK_RESULTS_CSV_PROCESS) :
            subgc.process_geocode_final_results(cmd,parms)
            
        elif(cmd == sugm.PROCESS_BULK_ERRORS_CSV_PROCESS) :
            subgc.process_geocode_final_results(cmd,parms)
        
        else :
            subgcs.display_geocoder_process_results(cmd,opstat,True)
            
    elif(optionId == sugm.PROCESS_BULK_CHANGE_DF) : 
        
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid,True)
            
        cfg.set_config_value(cfg.CURRENT_GEOCODE_DF,parms[0])
            
        if(geocid   ==  sugm.GoogleId) :
            cfg.get_drop_value(subgw.bulk_google_query_input_id+"Parms")
        elif(geocid   ==  sugm.BingId) :
            cfg.drop_config_value(subgw.bulk_bing_query_input_id+"Parms")
        elif(geocid   ==  sugm.BaiduId) :
            cfg.drop_config_value(subgw.bulk_baidu_query_input_id+"Parms")
            
        geotype     =   sugm.QUERY
        
        subgw.display_bulk_geocode_inputs(geocid,geotype)
    
    elif(optionId == sugm.PROCESS_BULK_REVERSE_CHANGE_DF) : 
        
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid,True)
            
        cfg.set_config_value(cfg.CURRENT_GEOCODE_DF,parms[0])
            
        if(geocid   ==  sugm.GoogleId) :
            cfg.get_drop_value(subgw.bulk_google_reverse_input_id+"Parms")
        elif(geocid   ==  sugm.BingId) :
            cfg.drop_config_value(subgw.bulk_bing_reverse_input_id+"Parms")
        elif(geocid   ==  sugm.BaiduId) :
            cfg.drop_config_value(subgw.bulk_baidu_reverse_input_id+"Parms")
            
        geotype     =   sugm.REVERSE
        
        subgw.display_bulk_geocode_inputs(geocid,geotype)

        
         
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoder helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#  get geocoder engine
#--------------------------------------------------------------------------
"""
def get_geocoder_engine(geocid,opstat) :
    """
    * ---------------------------------------------------------
    * function : get a geocoder engine
    * 
    * parms :
    *  geocid    - geocoder id
    *  opstat    - operation status object
    *
    * returns : 
    *  geocoder engine 
    * --------------------------------------------------------
    """
    
    if(sugm.GEOCODE_DETAIL_DEBUG)  :   
        log_debug_dfc(-1,"get_geocoder_engine " + str(geocid))
    
    geolocator  =   None
    
    try :
            
        geocinitparms = sugw.get_geocoder_cmd_kwargs(sugm.GEOCODER,geocid)
        
        if(geocid == sugm.GoogleId) :
            from geopy.geocoders import GoogleV3
            if(geocinitparms == None) :
                geolocator = GoogleV3() 
            else :
                geolocator = GoogleV3(**geocinitparms)
            
        elif(geocid == sugm.BingId) :
            from geopy.geocoders import Bing
            if(geocinitparms == None) :
                geolocator = Bing() 
            else :
                geolocator = Bing(**geocinitparms)
        
        elif(geocid == sugm.BaiduId) :
            from geopy.geocoders import Baidu
            if(geocinitparms == None) :
                geolocator = Baidu() 
            else :
                geolocator = Baidu(**geocinitparms)
            
        elif(geocid == sugm.OpenMapQuestId) :
            from geopy.geocoders import OpenMapQuest
            if(geocinitparms == None) :
                geolocator = OpenMapQuest() 
            else :
                geolocator = OpenMapQuest(**geocinitparms)
                    
        elif(geocid == sugm.NominatimId) :
            from geopy.geocoders import Nominatim
            if(geocinitparms == None) :
                geolocator = Nominatim() 
            else :
                geolocator = Nominatim(**geocinitparms)
                    
        elif(geocid == sugm.ArcGISId) :
            from geopy.geocoders import ArcGIS
            if(geocinitparms == None) :
                geolocator = ArcGIS() 
            else :
                geolocator = ArcGIS(**geocinitparms)
                    
    except Exception as e:
        opstat.store_exception("Error getting geocoder service (_init) ",e)
    
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"get_geocoder_engine exception" + str(geocid))
        
    return(geolocator)    
  

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   taskbar process Utility functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def test_geocoder(geocid,gcparms,gmode=sugm.INTERACTIVE) :
    """
    * ---------------------------------------------------------
    * function : test the geocoder connection and run sample
    * 
    * parms :
    *  geocid    - geocoder id
    *  gcparms   - geocoder parms
    *
    * returns : 
    *  N?A 
    * --------------------------------------------------------
    """

    opstat      =   opStatus()
    
    if(geocid == sugm.ArcGISId)              :  
        form    =   sugw.arcgis_geocoder_id
    elif(geocid == sugm.BingId)              :  
        form    =   sugw.bing_geocoder_id
    elif(geocid == sugm.BaiduId)              :  
        form    =   sugw.baidu_geocoder_id
    elif(geocid == sugm.GoogleId)            :  
        form    =   sugw.google_geocoder_id
    elif(geocid == sugm.OpenMapQuestId)      :  
        form    =   sugw.mapquest_geocoder_id
    elif(geocid == sugm.NominatimId)         :  
        form    =   sugw.nomin_geocoder_id
        
    cfg.set_config_value(form+"Parms",gcparms)

    opstat  =   sugw.validate_geocode_connect_parms(geocid) 
    
    if( not (opstat.get_status()) ) :

        sugw.display_geocoders(geocid) 
        display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()
 
        try :
            geolocator = get_geocoder_engine(geocid,opstat)
            
        except Exception as e:
            opstat.store_exception("Error initializing geocoder service",e)

        if(opstat.get_status()) :
            
            query = "11111 Euclid Ave, Cleveland OH " 
            
            try :
                address, (latitude, longitude) = geolocator.geocode(query) 
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()
        
            
        if(opstat.get_status()) :
            
            
            statHeader      =   [""]
            statRows        =   []
            statWidths      =   [35,65]
            statAligns      =   ["left","left"]
            statHrefs       =   None


            current_row     =   ["Test Address   : ",str(query)]
            statRows.append(current_row)
            current_row     =   ["Returned Address   : ", str(address)]
            statRows.append(current_row)
            current_row     =   ["Returned Latitude  : ",str(latitude)]
            statRows.append(current_row)
            current_row     =   ["Returned Longitude : ",str(longitude)]
            statRows.append(current_row)    
    
        
            stats_table     =   None
    
            from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
        
            stats_table     =   dcTable("Geocode Test Connection Status",'geocodtestid',
                                        cfg.SWGeocodeUtility_ID,
                                        statHeader,statRows,
                                        statWidths,statAligns)
            
            stats_table.set_refList(statHrefs)
            stats_table.set_checkLength(False)
            stats_table.set_small(True)
            stats_table.set_border(True)
            stats_table.set_tabletype(ROW_MAJOR)
            stats_table.set_rowspertable(50)
    
            statsHtml = "<br>" + get_row_major_table(stats_table,SCROLL_DOWN,False)
    
            if(gmode == sugm.INTERACTIVE) :
                sugw.display_geocoders(geocid,False,True,statsHtml)
            else :
                subgw.display_bulk_geocoders(geocid)    
            
        else :
            
            if(gmode == sugm.INTERACTIVE) :
                sugw.display_geocoders(geocid) 
            else :
                subgw.display_bulk_geocoders(geocid) 
            
            display_exception(opstat)



def run_geocoder_query(geocid, parms) :
    """
    * ---------------------------------------------------------
    * function : run a geocoder query operation
    * 
    * parms :
    *  inparms   - geocoder query parms
    *
    * returns : 
    *  N?A 
    * --------------------------------------------------------
    """
    
    DEBUG_QUERY   =   True
    
    if(DEBUG_QUERY) : print("\nrun_geocoder_query : parms\n",parms)
    
    opstat  =   opStatus()
    
    #lat_lngs    =   []
    coords          =   []
    
    sugw.validate_cmd_parms(sugm.QUERY,geocid,parms,opstat)
    
    if(not opstat.get_status()) :
        
        sugw.display_geocode_inputs(None,sugm.QUERY)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)
        
        queryparms  = None
        query       = None

        numresults   =  0
        
        if(opstat.get_status()) :
            
            try :
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.QUERY,geocid)
                
                if(DEBUG_QUERY) : print("run_geocoder_query : queryparms\n",queryparms)
                
                query   =   queryparms.get("address(s)")
                query   =   query.replace("\n","")
                queryparms.pop("address(s)")
                
                if(geocid == sugm.BingId) :
                        if(queryparms.get("culture") == "United States") :
                            queryparms.pop("culture")  
                        
                        else :
                            
                            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
                            country_codes   =   get_Dict("Country_Codes")
                            cc_chars        =   country_codes.get(queryparms.get("culture"))
                            queryparms.update({"culture" : cc_chars})
                            
                elif(geocid == sugm.GoogleId) :
                    
                    if(queryparms.get("region") == "None") :
                        queryparms.pop("region")  
                    
                    if(queryparms.get("language") == "English") :
                        queryparms.pop("language") 
                        
                    else :
                            
                        from dfcleanser.sw_utilities.sw_utility_model import get_Dict
                        lang_codes  =   get_Dict("Google_Language_Codes")
                        lang        =   lang_codes.get(queryparms.get("language"))
                        queryparms.update({"language" : lang})

                
                if(DEBUG_QUERY) : print("run_geocoder_query : queryparms\n",queryparms)
                if(DEBUG_QUERY) : print("run_geocoder_query : query\n",query)
                
                import json
                
                addresses_to_geocode    =   json.loads(query)

                if(type(addresses_to_geocode) == str) :
                    addresses_to_geocode    =   [addresses_to_geocode] 
                
                numresults  =  cfg.get_config_value(sugm.get_geocoder_title(geocid)+"max_geocode_results")
                if(numresults is None) :
                    numresults  =   1
                else :
                    numresults  =   int(numresults)

                for i in range(len(addresses_to_geocode)) :
                    
                    if(len(queryparms) > 0) :
                        location = geolocator.geocode(addresses_to_geocode[i], **queryparms) 
                    else :
                        location = geolocator.geocode(addresses_to_geocode[i]) 
                        
                    if(location is None) :
                        coords.append(None)
                        
                    else :
                        
                        if(type(location) == list) :
                            if(DEBUG_QUERY) : print("run_geocoder_query : location ",len(location)) 
                            if(DEBUG_QUERY) : 
                                for k in range(len(location)) :
                                    print("run_geocoder_query : location k ",k," ",type(location[k])," ",location[k]) 
                            coords.append(location)
                            
                        else :
                            if(DEBUG_QUERY) : print("run_geocoder_query : location ",location)
                            coords.append(location)
                    
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()
        
        if(opstat.get_status()) :
            
            statHeader      =   [""]
            statRows        =   []
            statWidths      =   [50,50]
            statAligns      =   ["left","left"]
            statHrefs       =   None


            for i in range(len(coords)) :
                
                if(i>0) :
                    current_row     =   [" "," "]
                    statRows.append(current_row)
                
                current_row     =   [str(addresses_to_geocode[i])," "]
                statRows.append(current_row)
                
                if(type(coords[i]) == list) :
                    
                    if(len(coords[i]) > numresults) :
                        coordcount  =   numresults
                    else :
                        coordcount  =   len(coords[i])
                    
                    for j in range(coordcount) :
                
                        if( (geocid == sugm.BingId) or (geocid == sugm.GoogleId) or 
                            (geocid == sugm.ArcGISId) or (geocid == sugm.OpenMapQuestId) or 
                            (geocid == sugm.NominatimId) ):
                            current_row     =   [ "&nbsp;&nbsp;&nbsp;&nbsp;" + "[" + str(coords[i][j].latitude) + " , " + str(coords[i][j].longitude) + "]",str(coords[i][j].address)]
                        else :
                            current_row     =   [ "&nbsp;&nbsp;&nbsp;&nbsp;" + "[" + str(coords[i][j].latitude) + " , " + str(coords[i][j].longitude) + "]",""]
                        
                        statRows.append(current_row)
                        
                else :
                    
                    if(i>0) :
                        current_row     =   [" "," "]
                        statRows.append(current_row)
                    
                    if(coords[i] is None) :
                        current_row     =   ["&nbsp;&nbsp;&nbsp;&nbsp;" + "No coords found for address"]
                        statRows.append(current_row)
                    
                    else :
                        if( (geocid == sugm.BingId) or (geocid == sugm.GoogleId) or 
                            (geocid == sugm.ArcGISId) or (geocid == sugm.OpenMapQuestId)) :
                            current_row     =   [ "&nbsp;&nbsp;&nbsp;&nbsp;" + "[" + str(coords[i].latitude) + " , " + str(coords[i].longitude) + "]",str(coords[i].address)]
                        else :
                            current_row     =   [ "&nbsp;&nbsp;&nbsp;&nbsp;" + "[" + str(coords[i].latitude) + " , " + str(coords[i].longitude) + "]",""]
                        
                        statRows.append(current_row)
                    

            stats_table     =   None
    
            from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
        
            stats_table     =   dcTable("Address Coordinates",'geocodtestid',
                                        cfg.SWGeocodeUtility_ID,
                                        statHeader,statRows,
                                        statWidths,statAligns)
            
            stats_table.set_refList(statHrefs)
            stats_table.set_checkLength(False)
            stats_table.set_small(True)
            stats_table.set_smallwidth(80)
            stats_table.set_smallmargin(80)

            stats_table.set_border(True)
            stats_table.set_tabletype(ROW_MAJOR)
            stats_table.set_rowspertable(50)
    
            statsHtml = "<br>" + get_row_major_table(stats_table,SCROLL_DOWN,False)
            
            sugw.display_geocode_inputs(geocid,sugm.QUERY,False,statsHtml) 
            
        else :
            
            sugw.display_geocode_inputs(geocid,sugm.QUERY) 
            
            display_exception(opstat)


def get_bulk_query_parms(geocid,parms) :
    """
    * ---------------------------------------------------------
    * function : get the bulk query parms 
    * 
    * parms :
    *  geocid   - geocoder id
    *  parms    - geocoder input parms
    *
    * returns : 
    *  bulk query parms 
    * --------------------------------------------------------
    """
        
    dfform  =   sugw.get_comp_addr_conv_form(geocid) 
    fparms  =   get_parms_for_input(parms,dfform[1])
    
    dfcolsList = fparms[0].split("+")
    for i in range(len(dfcolsList)) :
        dfcolsList[i] = dfcolsList[i].strip()
            
    coltypes = []
    
    for i in range(len(dfcolsList)) :
        if(dfcolsList[i].find("'") != -1) :
            coltypes.append(False)
            staticname = dfcolsList[i].replace("'","")
            #staticname = staticname[i].lstrip("'")
            dfcolsList[i] = staticname
        else :
            coltypes.append(True)
    
    fparms[0] = [dfcolsList,coltypes]
    
    return(fparms)


def run_geocoder_reverse(geocid,parms) :
    """
    * ---------------------------------------------------------
    * function : run a geocode reverse 
    * 
    * parms :
    *  inparms  - geocoder reverse input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    DEBUG_REVERSE   =   True
    
    if(DEBUG_REVERSE) : print("run_geocoder_reverse",parms)

    opstat  =   opStatus()
    
    coords          =   []
    locations       =   []
    addresses       =   []
    
    sugw.validate_cmd_parms(sugm.REVERSE,geocid,parms,opstat)
    
    if(not opstat.get_status()) :
        sugw.display_geocode_inputs(None,sugm.REVERSE)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)
        num_results   =  0
        
        if(opstat.get_status()) :
            
            try :
                
                if(geocid == sugm.GoogleId)             :   idlist  =   sugw.google_reverse_idList
                elif(geocid == sugm.ArcGISId)           :   idlist  =   sugw.arcgis_reverse_idList
                elif(geocid == sugm.BingId)             :   idlist  =   sugw.bing_reverse_idList
                elif(geocid == sugm.OpenMapQuestId)     :   idlist  =   sugw.mapquest_reverse_idList
                elif(geocid == sugm.NominatimId)        :   idlist  =   sugw.nomin_reverse_idList
                elif(geocid == sugm.BaiduId)            :   idlist  =   sugw.baidu_reverse_idList
                else                                    :   idlist  =   ""
                
                fparms  =   get_parms_for_input(parms,idlist)
                
                if(DEBUG_REVERSE) : print("run_geocoder_reverse : fparms\n",fparms)
                
                num_results     =   fparms[1]
                if(len(num_results) > 0) :
                    num_results     =   int(num_results)
                    if(num_results > 5) :
                        num_results     =   5
                else :
                    num_results     =   1
                    
                if(DEBUG_REVERSE) : print("run_geocoder_reverse : num_results  ",num_results)
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.REVERSE,geocid)
                
                if(DEBUG_REVERSE) : print("run_geocoder_reverse : queryparms\n",queryparms)
                
                if(geocid == sugm.BingId) :
                    if( not (queryparms.get("culture") is None) ) : 
                        if(queryparms.get("culture") == "United States") :
                            queryparms.pop("culture")  
                        
                        else :
                            
                            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
                            country_codes   =   get_Dict("Country_Codes")
                            cc_chars        =   country_codes.get(queryparms.get("culture"))
                            queryparms.update({"culture" : cc_chars})
                            
                elif(geocid == sugm.GoogleId) :
                    
                    if(queryparms.get("language") == "English") :
                        queryparms.pop("language")
                        
                    else :
                            
                        from dfcleanser.sw_utilities.sw_utility_model import get_Dict
                        lang_codes  =   get_Dict("Google_Language_Codes")
                        lang        =   lang_codes.get(queryparms.get("language"))
                        queryparms.update({"language" : lang})
                
                query = queryparms.get("latitude_longitude(s)")
                queryparms.pop("latitude_longitude(s)")
                
                if(DEBUG_REVERSE) : print("run_geocoder_reverse : queryparms\n",queryparms)
                
                query   =   query.replace("\n","")
                
                if(DEBUG_REVERSE) : print("run_geocoder_reverse : query\n",query)
                
                import json
                coords  =   json.loads(query)
                
                if( not (type(coords[0]) == list) ) :
                    coords  =   [coords]
                    
                if(num_results > 1) :
                    queryparms.update({"exactly_one":False})

                for i in range(len(coords)) :
                    
                    if(DEBUG_REVERSE) : print("run_geocoder_reverse : coords",type(coords[i]),coords[i])
                    
                    if(len(queryparms) > 0) :
                        location = geolocator.reverse(coords[i],**queryparms) 
                    else :
                        location = geolocator.reverse(coords[i]) 
                        
                    if(DEBUG_REVERSE) : print("run_geocoder_reverse : location ",type(location),location)
                    
                    if(location is None) :
                        locations.append(None)
                        addresses.append("No addreses found for geocode coords")
                        
                    else :
                        
                        if(type(location) == list) :
                            if(DEBUG_REVERSE) : print("run_geocoder_reverse : location ",len(location))
                            
                            current_addresses   =   []
                            
                            for k in range(len(location)) :
                                if(DEBUG_REVERSE) : 
                                    print("run_geocoder_reverse : location k ",k," ",type(location[k])," ",location[k])
                                    print("run_geocoder_reverse : address k ",k," ",location[k].address)
                                locations.append(location[k])
                                
                                if(not (geocid == sugm.BingId)) :
                                    current_addresses.append(location[k].address)
                                    
                                else :
                                
                                    if( not (queryparms.get("include_country_code") is None) ):
                                        if(queryparms.get("include_country_code")) :
                                            country_code  =  location[k].raw["address"].get("countryRegionIso2")
                                            current_addresses.append(location[k].address + " : " + country_code)
                                        else :
                                            current_addresses.append(location[k].address)
                                    else :
                                        
                                        print("bing no cc")
                                        current_addresses.append(location[k].address)
                                        
                            addresses.append(current_addresses)
                            
                        else :
                            
                            locations.append(location)
                            if(DEBUG_REVERSE) : print("run_geocoder_reverse : location ",location) 
                            
                            if(not (geocid == sugm.BingId)) :
                                addresses.append(location.address)
                            else :
                                
                                if( not (queryparms.get("include_country_code") is None) ):
                                    if(queryparms.get("include_country_code")) :
                                        country_code  =  location.raw["address"].get("countryRegionIso2")
                                        addresses.append(location.address + " : " + country_code)
                                    else :
                                        addresses.append(location.address)
                                else :
                                    addresses.append(location.address)
                    
            except Exception as e:
                opstat.store_exception("Error getting geocoder address",e)
            
        clock.stop()

        if(opstat.get_status()) :
            
            statHeader      =   [""]
            statRows        =   []
            statWidths      =   [100]
            statAligns      =   ["left"]
            statHrefs       =   None

            for i in range(len(coords)) :
                
                if(i>0) :
                    current_row     =   [" "]
                    statRows.append(current_row)
                    
                current_row     =   [str(coords[i])]
                statRows.append(current_row)
                    
                    
                if(type(addresses[i]) == list) :
                    if(len(addresses[i]) < num_results) :
                        num_results     =  len(addresses[i]) 
                        
                    for j in range(num_results) :
                        current_row     =   ["&nbsp;&nbsp;&nbsp;&nbsp;" + str(addresses[i][j])]
                        statRows.append(current_row)
                        
                else :        
                
                    current_row     =   ["&nbsp;&nbsp;&nbsp;&nbsp;" + str(addresses[i])]
                    statRows.append(current_row)

            stats_table     =   None
    
            from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
        
            stats_table     =   dcTable("Addresses",'geocodtestid',
                                        cfg.SWGeocodeUtility_ID,
                                        statHeader,statRows,
                                        statWidths,statAligns)
            
            stats_table.set_refList(statHrefs)
            stats_table.set_checkLength(False)
            stats_table.set_small(True)
            stats_table.set_smallwidth(80)
            stats_table.set_smallmargin(80)

            stats_table.set_border(True)
            stats_table.set_tabletype(ROW_MAJOR)
            stats_table.set_rowspertable(50)
    
            statsHtml = "<br>" + get_row_major_table(stats_table,SCROLL_DOWN,False)

            sugw.display_geocode_inputs(geocid,sugm.REVERSE,False,statsHtml) 
            
        else :
            sugw.display_geocode_inputs(geocid,sugm.REVERSE) 

            display_exception(opstat)



def get_distance(from_loc,to_loc,distance_units,algorithm,elipsoid,opstat) :
    
    from geopy import distance
    
    calc_distance   =   0
    
    if(algorithm == "geodesic")  :
            
        if(distance_units == "km") :
            if(not(elipsoid == "WGS-84")) :
                calc_distance    =   distance.geodesic(from_loc,to_loc, elipsoid=elipsoid).km
            else :
                calc_distance    =   distance.geodesic(from_loc,to_loc).km
        else :
            if(not(elipsoid == "WGS-84")) :
                calc_distance    =   distance.geodesic(from_loc,to_loc, elipsoid=elipsoid).miles
            else :
                calc_distance    =   distance.geodesic(from_loc,to_loc).miles
            
    elif(algorithm == "great_circle") :
            
        if(distance_units == "km") :
            calc_distance    =   distance.great_circle(from_loc,to_loc).km
        else :
            calc_distance    =   distance.great_circle(from_loc,to_loc).miles
                    
    else :
                
        opstat.set_status(False)
        opstat.set_errorMsg("Invalid geocoding algorithm : " + str(algorithm))
    
    return(calc_distance)
    


def calculate_geocode_distances(from_locs_list,to_locs_list,distance_units,algorithm,elipsoid,opstat) :
    
    distances       =   []
    
    try :
        
        if(type(from_locs_list[0]) == list) :
            
            for i in range(len(from_locs_list)) :
                calc_distance    =   get_distance(from_locs_list[i],to_locs_list[i],distance_units,algorithm,elipsoid,opstat)
                distances.append(calc_distance)
                
        else :
            
            calc_distance    =   get_distance(from_locs_list,to_locs_list,distance_units,algorithm,elipsoid,opstat) 
            distances.append(calc_distance)
            
                    
    except Exception as e:
        opstat.set_status(False)
        opstat.store_exception("Error calculating distances",e)

    return(distances)


def build_distance_entry(distanceRows,from_lat_lngs,from_addresses,to_lat_lngs,to_addresses,distances,distance_unit,add_blank_line=False) :    
    
    if(add_blank_line) :
        current_row     =   [" "," "," "]
        distanceRows.append(current_row)
        
    if(to_lat_lngs is None) :
            
        current_row     =   ["Address : ",str(from_lat_lngs),str(from_addresses)]
        distanceRows.append(current_row)
            
    else :
            
        current_row     =   ["From : ",str(from_lat_lngs),str(from_addresses)]
        distanceRows.append(current_row)
            
        current_row     =   ["To : ",str(to_lat_lngs),str(to_addresses)]
        distanceRows.append(current_row)
        current_row     =   ["Distance : ","{:10.4f}".format(distances),str(distance_unit)]
        distanceRows.append(current_row)
    
    
   
def get_distances_table(from_lat_lngs,from_addresses,to_lat_lngs=None,to_addresses=None,distances=None,distance_unit=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    distanceHeader      =   [""]
    distanceRows        =   []
    distanceWidths      =   [11,30,59]
    distanceAligns      =   ["left","left","left"]
    distanceHrefs       =   None

    
    if(type(from_lat_lngs[0]) == list) :
    
        for i in range(len(from_lat_lngs)) :
            
            if(i>0) :
                build_distance_entry(distanceRows,from_lat_lngs[i],from_addresses[i],to_lat_lngs[i],to_addresses[i],distances[i],distance_unit,True) 
            else :
                build_distance_entry(distanceRows,from_lat_lngs[i],from_addresses[i],to_lat_lngs[i],to_addresses[i],distances[i],distance_unit,False) 
                
    else :
        
        build_distance_entry(distanceRows,from_lat_lngs,from_addresses[0],to_lat_lngs,to_addresses[0],distances[0],distance_unit,False) 
        
    distances_table     =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    if(to_lat_lngs is None) :
        title   =   "Geocode Addresses"
    else :
        title   =   "Geocode Distances"
        
    distances_table     =   dcTable(title,'geocodedistid',
                                    cfg.SWGeocodeUtility_ID,
                                    distanceHeader,distanceRows,
                                    distanceWidths,distanceAligns)
            
    distances_table.set_refList(distanceHrefs)
     
    distances_table.set_small(True)
    distances_table.set_checkLength(False)

    distances_table.set_border(True)
    distances_table.set_tabletype(ROW_MAJOR)
    distances_table.set_rowspertable(50)
    distancesHtml = get_row_major_table(distances_table,SCROLL_DOWN,False)
 
    return(distancesHtml)
    
    

def process_distance(parms,parmtype=sugm.GEOCODE_ADDRESS) :
    """
    * ---------------------------------------------------------
    * function : calculate the dist betweern coords 
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    geocid      =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)        
    geolocator  =   get_geocoder_engine(geocid,opstat)
    
    if(not opstat.get_status()) :
        display_exception(opstat)

    if(parmtype == sugm.GEOCODE_ADDRESS) :
        fparms  =   get_parms_for_input(parms,sugw.addr_dist_utility_input_idList)
    else :
        fparms  =   get_parms_for_input(parms,sugw.addr_dist_utility_input_idList)
        
    from_loc    =   fparms[0]  
    
    if(len(from_loc) > 0) :
        
        try :

            import json
            from_locs_list  =   json.loads(from_loc)

            if(parmtype == sugm.GEOCODE_COORDS) :
                
                if(type(from_locs_list[0]) == list) :
                
                    for i in range(len(from_locs_list)) :
                        from_locs_list[i][0]     =   float(from_locs_list[i][0])
                        from_locs_list[i][1]     =   float(from_locs_list[i][1])
            
                else :
                
                    from_locs_list[0]     =   float(from_locs_list[0])
                    from_locs_list[1]     =   float(from_locs_list[1])
                    
            else :
                
                if(type(from_locs_list) == list) :
                
                    for i in range(len(from_locs_list)) :
                        from_locs_list[i]   =  str(from_locs_list[i])
                        #from_locs_list[i]   =  from_locs_list[i].replace("'","") 
                        #from_locs_list[i]   =  from_locs_list[i].replace('"','')
                        
                else :
                    
                    from_locs_list  =   str(from_locs_list)
                    from_locs_list  =   from_locs_list.replace("'","") 
                    from_locs_list  =   from_locs_list.replace('"','')
                
        except : 
            opstat.set_status(False)
            opstat.set_errorMsg("from_locations is invalid " + str(fparms[0]))
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("from_locations are not defined ")
    
    if(opstat.get_status()) :
        
        to_loc    =   fparms[1]
        
        if(len(to_loc) > 0) :
        
            try :

                import json
                to_locs_list  =   json.loads(to_loc)
                
                if(parmtype == sugm.GEOCODE_COORDS) :
            
                    if(type(to_locs_list[0]) == list) :
                    
                        for i in range(len(to_locs_list)) :
                            to_locs_list[i][0]     =   float(to_locs_list[i][0])
                            to_locs_list[i][1]     =   float(to_locs_list[i][1])
                        
                    else :
                    
                        to_locs_list[0]     =   float(to_locs_list[0])
                        to_locs_list[1]     =   float(to_locs_list[1])
                        
                else :
                    
                    if(type(to_locs_list) == list) :
                
                        for i in range(len(to_locs_list)) :
                            
                            to_locs_list[i]   =  str(to_locs_list[i])
                            #to_locs_list[i]   =  to_locs_list[i].replace("'","") 
                            #to_locs_list[i]   =  to_locs_list[i].replace('"','')
            
                    else :
                
                        to_locs_list    =   str(to_locs_list)
                        to_locs_list    =   to_locs_list.replace("'","") 
                        to_locs_list    =   to_locs_list.replace('"','')
                   
            except : 
                opstat.set_status(False)
                opstat.set_errorMsg("to_locations is invalid " + str(fparms[1]))
    
    if(opstat.get_status()) :
        
        distance_units  =   fparms[2]
        algorithm       =   fparms[3]
        elipsoid        =   fparms[4]
        
        if(parmtype == sugm.GEOCODE_ADDRESS) :   
            
            from_locations  =   []
            to_locations    =   []
            
            try :
                
                if(type(from_locs_list) == list) :
            
                    for i in range(len(from_locs_list)) :
                
                        from_location   =   geolocator.geocode(from_locs_list[i]) 
                        to_location     =   geolocator.geocode(to_locs_list[i]) 
                
                        from_new_loc    =   [float(from_location.latitude)]
                        from_new_loc.append(float(from_location.longitude))
                        to_new_loc      =   [float(to_location.latitude)]
                        to_new_loc.append(float(to_location.longitude))
                        
                        from_locations.append(from_new_loc)
                        to_locations.append(to_new_loc)
                        
                    from_locs_list  =  from_locations 
                    to_locs_list    =  to_locations 
                    
                else :
                    
                    from_location   =   geolocator.geocode(from_locs_list) 
                    to_location     =   geolocator.geocode(to_locs_list) 
                    
                    from_locs_list  =   [float(from_location.latitude)]
                    from_locs_list.append(float(from_location.longitude))
                    to_locs_list    =   [float(to_location.latitude)]
                    to_locs_list.append(float(to_location.longitude))
            
            except : 
                opstat.set_status(False)
                opstat.set_errorMsg("unable to get coords for addresses " + str(fparms[1]))
           
        distances       =   calculate_geocode_distances(from_locs_list,to_locs_list,distance_units,algorithm,elipsoid,opstat)
        
    if(opstat.get_status()) :

        print("\n")
        
        if(opstat.get_status()) :
            
            from_addresses  =   []
            to_addresses    =   []
            
            try :
                
                if(type(from_locs_list[0]) == list) :
                
                    for i in range(len(from_locs_list)) :
            
                        from_location   =  geolocator.reverse(from_locs_list[i],exactly_one=True) 
                        to_location     =  geolocator.reverse(to_locs_list[i],exactly_one=True) 
            
                        from_addresses.append(from_location.address)
                        to_addresses.append(to_location.address)
                        
                else :
                    
                    from_location   =  geolocator.reverse(from_locs_list,exactly_one=True) 
                    to_location     =  geolocator.reverse(to_locs_list,exactly_one=True) 
                    
                    from_addresses.append(from_location.address)
                    to_addresses.append(to_location.address)
                    
                    
            except Exception as e:
                opstat.store_exception("Unable to get geocoding address for " + str(from_locs_list[0]),e)
            
    if(opstat.get_status()) :
        
        distance_html   =   get_distances_table(from_locs_list,from_addresses,to_locs_list,to_addresses,distances,distance_units)  

        gridclasses     =   ["dfc-top"]
        gridhtmls       =   [distance_html]
    
        display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)
        
    else :
        display_exception(opstat)            


def process_df_distance(parms) :
    """
    * ---------------------------------------------------------
    * function : calculate the dist betweern coords in a column
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    DEBUG_PROCESS_DF_DISTANCE   =   False
    
    if(DEBUG_PROCESS_DF_DISTANCE) :
        print("process_df_distance parms \n",parms)
        
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms,sugw.addr_df_dist_utility_input_idList)

    if(DEBUG_PROCESS_DF_DISTANCE) :
        print("\nprocess_df_distance fparms \n",fparms)
    
    from_dftitle        =   fparms[0]
    from_df             =   cfg.get_dataframe(from_dftitle)
    from_lat_lng_cols   =   fparms[1]  
    
    if(len(from_lat_lng_cols) > 0) :
        
        try :
    
            from_cols_list  =   []
            
            from_cols_list    =   from_lat_lng_cols.lstrip("[")
            from_cols_list    =   from_cols_list.rstrip("]")
            from_cols_list    =   from_cols_list.split(",")
    
            if(len(from_cols_list) > 2) :
                
                opstat.set_status(False)
                opstat.set_errorMsg("from_columns : too many column names " + str(from_cols_list))
            
            else :
                
                from dfcleanser.common.common_utils import is_column_in_df
                for i in range(len(from_cols_list))  :
                
                    if(not (is_column_in_df(from_df,from_cols_list[i]))) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("from_columns column name is invalid " + str(from_cols_list[i]))
                        break
                
        except Exception as e:
            opstat.store_exception("from_columns is invalid " + str(fparms[1]),e)
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("from_columns are not defined ")
        
    if(opstat.get_status()) :
        
        if(not ((fparms[3] == "get to coords from to_coords(s)_list") or 
                (fparms[3] == "get to address(s) from to_address(s)_list") )) :
            
            static_to_coords_list   =   None
    
            to_dftitle        =   fparms[3]
            to_df             =   cfg.get_dataframe(to_dftitle)
            to_lat_lng_cols   =   fparms[4]  
    
            if(len(to_lat_lng_cols) > 0) :
        
                try :
    
                    to_cols_list  =   []
                    
                    to_cols_list    =   to_lat_lng_cols.lstrip("[")
                    to_cols_list    =   to_cols_list.rstrip("]")
                    to_cols_list    =   to_cols_list.split(",")
            
                    if(len(to_cols_list) > 2) :
                
                        opstat.set_status(False)
                        opstat.set_errorMsg("to_columns : too many column names " + str(from_cols_list))
            
                    else :
                    
                        from dfcleanser.common.common_utils import is_column_in_df
                        for i in range(len(to_cols_list))  :
                
                            if(not (is_column_in_df(to_df,to_cols_list[i]))) :
                                opstat.set_status(False)
                                opstat.set_errorMsg("to_columns column name is invalid " + str(to_cols_list[i]))
                                break
                
                except Exception as e:
                    opstat.store_exception("to columns is invalid " + str(fparms[4]),e)
            
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("to_columns are not defined ")
                
        elif(fparms[3] == "get to coords from to_coords(s)_list") :
            
            static_to_coords_list   =   []
            to_cols_list            =   None
            
            try :
                
                import json
                static_to_coords_list  =   json.loads(fparms[6])
                
                if(type(static_to_coords_list[0]) == list) :
                    
                    for i in range(len(static_to_coords_list)) :
                        static_to_coords_list[i][0]     =   float(static_to_coords_list[i][0]) 
                        static_to_coords_list[i][1]     =   float(static_to_coords_list[i][1])
                        
                else :
                    
                    static_to_coords_list[0]     =   float(static_to_coords_list[0]) 
                    static_to_coords_list[1]     =   float(static_to_coords_list[1])
                
            except Exception as e:
                opstat.store_exception("static to coords is invalid " + str(fparms[6]),e)
                
        else :
            
            static_to_coords_list   =   []
            to_cols_list            =   None
            
            try :
                
                address_list    =   fparms[6].lstrip("[")
                address_list    =   address_list.rstrip("]")
                address_list    =   address_list.split(",")
                
                geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    
                if(geocid is None) :
                    geocid  =   sugm.GoogleId
        
                geolocator  =   geolocator  =   get_geocoder_engine(geocid,opstat)
                
                for i in range(len(address_list)) :
                    
                    location    =   geolocator.geocode(address_list[i]) 
                    
                    if(type(location) == list) :
                        current_coord   =   [location[0].latitude,location[0].longitude]
                    else :
                        current_coord   =   [location.latitude,location.longitude]
                    
                    static_to_coords_list.append(current_coord)
                    
            except Exception as e:
                opstat.store_exception("address list is invalid " + str(fparms[6]),e)
            
                
    if(opstat.get_status()) :
        
        distance_col_names   =   fparms[7] 
        
        if(DEBUG_PROCESS_DF_DISTANCE) :
            print("distance_col_names",type(distance_col_names),len(distance_col_names),distance_col_names)
        
        if(distance_col_names.find("[") > -1) :
            
            try :
                
                distance_col_names_list    =   distance_col_names.lstrip("[")
                distance_col_names_list    =   distance_col_names_list.rstrip("]")
                distance_col_names_list    =   distance_col_names_list.split(",")

            except Exception as e:
                opstat.store_exception("distance col names are invalid " + str(fparms[7]),e)
                
        else :
            
            distance_col_names_list     =   [distance_col_names]
        
        if(opstat.get_status()) :
            
            for i in range(len(distance_col_names_list))  :
                
                if(is_column_in_df(from_df,distance_col_names_list[i])) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("distance column name is already defined " + str(distance_col_names_list[i]))
                    break
                
            if(opstat.get_status()) :
                
                if(static_to_coords_list is None) :
                    if(len(distance_col_names_list) > 1) :
                    
                        opstat.set_status(False)
                        opstat.set_errorMsg("multiple distance column names not allowed for to_df " + str(distance_col_names_list))
                        
                else :
                    
                    if(type(static_to_coords_list[0]) == list) :
                        num_static_coords   =   len(static_to_coords_list)
                    else :
                        num_static_coords   =   1
                        
                    if(not (len(distance_col_names_list) == num_static_coords) ) :
                    
                        opstat.set_status(False)
                        opstat.set_errorMsg("number of distance column names : " + str(len(distance_col_names_list)) + " does not match number of static coords  : " + str(len(static_to_coords_list)) + "\n distance_col_names_list : " + str(distance_col_names_list) + "\n static_to_coords_list : " + str(static_to_coords_list))
            
    if(opstat.get_status()) :
        
        if(not (to_cols_list is None)) :
            if(not (len(from_df) == len(to_df)) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("length of from_df does not match length of to_df " + str(len(from_df)) + " " + str(len(to_df)))


    if(opstat.get_status()) :
        
        distance_units  =   fparms[8]
        algorithm       =   fparms[9]
        elipsoid        =   fparms[10]

        from_lat_list   =   from_df[from_cols_list[0]].tolist()
        from_lng_list   =   from_df[from_cols_list[1]].tolist()
        
        distance_multiple_list  =   []
        
        if(not (to_cols_list is None)) :
            
            distance_list   =   []
            
            to_lat_list   =   to_df[to_cols_list[0]].tolist()
            to_lng_list   =   to_df[to_cols_list[1]].tolist()
            
            for i in range(len(from_lat_list)) :
                
                current_from_coord  =   [float(from_lat_list[i]),float(from_lng_list[i])]
                current_to_coord    =   [float(to_lat_list[i]),float(to_lng_list[i])]
                
                distances     =   calculate_geocode_distances(current_from_coord,current_to_coord,distance_units,algorithm,elipsoid,opstat)
                distance_list.append(distances)
                
            distance_multiple_list.append(distance_list)
                
        else :
            
            if(type(static_to_coords_list[0]) == list) :
            
                for i in range(len(static_to_coords_list)) :
            
                    distance_list           =   []
                
                    for j in range(len(from_lat_list)) :
                
                        current_from_coord  =   [float(from_lat_list[j]),float(from_lng_list[j])]
                        current_to_coord    =   [float(static_to_coords_list[i][0]),float(static_to_coords_list[i][1])]
                
                        distance     =   calculate_geocode_distances(current_from_coord,current_to_coord,distance_units,algorithm,elipsoid,opstat)
                        distance_list.append(round(distance[0],4))
                    
                    distance_multiple_list.append(distance_list)
                    
            else :
                
                distance_list           =   []
                
                for j in range(len(from_lat_list)) :
                
                    current_from_coord  =   [float(from_lat_list[j]),float(from_lng_list[j])]
                    current_to_coord    =   [float(static_to_coords_list[0]),float(static_to_coords_list[1])]
                
                    distance            =   calculate_geocode_distances(current_from_coord,current_to_coord,distance_units,algorithm,elipsoid,opstat)
                    
                    distance_list.append(round(distance[0],4))
                
                distance_multiple_list.append(distance_list)
        
    if(opstat.get_status()) :
        
        display_status("distances calculated successfully")

        for i in range(len(distance_multiple_list)) :
            
            distance_col_name   =  distance_col_names_list[i]
            
            from dfcleanser.data_transform.data_transform_columns_control import add_column_to_df
            from_df     =   add_column_to_df(from_df,distance_col_name,distance_multiple_list[i],opstat,False) 
            from_df[distance_col_name] = from_df[distance_col_name].astype(float,copy=False)            
            
            cfg.set_dfc_dataframe_df(from_dftitle,from_df)
            
            if(not(opstat.get_status())) :
                break
        
    if(opstat.get_status()) :

        notes = []
        for i in range(len(distance_col_names_list)) :
            notes.append("New Column : '" + str(distance_col_names_list[i]) + "' added to '" + str(from_dftitle) + "' dataframe")
        display_notes(notes)
        
    else :
        display_exception(opstat)        
    
    
    
    


def process_center(parms) :
    """
    * ---------------------------------------------------------
    * function : calculate the center point of a list 
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    clock   =   RunningClock()
    
    fparms  =   get_parms_for_input(parms,sugw.addr_center_utility_input_idList)

    center_dftitle  =   fparms[0]
    coords_list     =   None
    
    center_cols_list  =   []


    if(center_dftitle == "get coords from coord(s)_list") :
        
        try :
    
            import json
            coords_list     =   json.loads(fparms[3])
            
        except Exception as e:
            opstat.store_exception("center coord(s)_list is invalid " + str(fparms[1]),e)
            
    elif(center_dftitle == "get coords from address(s)_list") :
        
        try :

            addrs_list  =   fparms[3].lstrip("[")
            addrs_list  =   addrs_list.rstrip("]")
            addrs_list  =   addrs_list.replace("'","") 
            addrs_list  =   addrs_list.split(",")
            
            for i in range(len(addrs_list)) :
                addrs_list[i]  =   addrs_list[i].lstrip(" ")
                addrs_list[i]  =   addrs_list[i].rstrip(" ")    
            
            geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    
            if(geocid is None) :
                geocid  =   sugm.GoogleId
        
            geolocator      =   None
            coords_list     =   []
    
            try :
        
                geolocator  =   get_geocoder_engine(geocid,opstat) 
                
                for i in range(len(addrs_list)) :
                
                    location    =   geolocator.geocode(addrs_list[i]) 
                    
                    if(type(location) == list) :
                        
                        coords  =   [location[0].latitude,location[0].longitude]
                    else :
                        coords  =   [location.latitude,location.longitude]  
                        
                    coords_list.append(coords)
        
            except Exception as e:
        
                geolocator      =   None
                center_address  =   None
                opstat.store_exception("Unable to run geocoder to get coordinates for addresses " + str(fparms[3]),e)
            
        except Exception as e:
            opstat.store_exception("center address(s)_list is invalid " + str(fparms[1]),e)
        
    
    else :
        
        center_df             =   cfg.get_dataframe(center_dftitle)
        
        if(not (center_df is None)) :
            
            center_lat_lng_cols     =   fparms[1] 
            center_cols_list        =   center_lat_lng_cols.lstrip("[")
            center_cols_list        =   center_cols_list.rstrip("]")
            center_cols_list        =   center_cols_list.split(",")

            if(len(center_cols_list) > 0) :
        
                try :
    
                    if(len(center_cols_list) > 2) :
                
                        opstat.set_status(False)
                        opstat.set_errorMsg("dataframe_lat_lng_columns : too many column names " + str(center_cols_list))
            
                    else :
                
                        from dfcleanser.common.common_utils import is_column_in_df
                        for i in range(len(center_cols_list))  :
                
                            if(not (is_column_in_df(center_df,center_cols_list[i]))) :
                                opstat.set_status(False)
                                opstat.set_errorMsg("dataframe_lat_lng_columns column name is invalid " + str(center_cols_list[i]))
                                break
                
                except Exception as e:
                    opstat.store_exception("dataframe_lat_lng_columns " + str(fparms[1]),e)
            
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("dataframe_lat_lng_columns are not defined ") 
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("center dataframe is invalid " + str(center_dftitle)) 
            
    if(opstat.get_status())  :
        
        clock.start()
        
        if(coords_list is None) :
            
            geocoords_list  =   []
            
            if(len(center_lat_lng_cols) == 1) :
                geocoords_list  =   list(center_df[center_cols_list[0]])
                
            else :
                
                geocords_lats   =   list(center_df[center_cols_list[0]])
                geocords_lngs   =   list(center_df[center_cols_list[1]])
                
                for i in range(len(geocords_lats)) :
                    geocoords_list.append([float(geocords_lats[i]),float(geocords_lngs[i])]) 
                    
            center  =   sugm.get_geocode_center(geocoords_list,opstat)
            
        else :
            center  =   sugm.get_geocode_center(coords_list,opstat)  
    
    if(opstat.get_status()) :
 
        geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    
        if(geocid is None) :
            geocid  =   sugm.GoogleId
        
        geolocator  =   None
    
        try :
        
            geolocator  =   get_geocoder_engine(geocid,opstat) 
            location    =   geolocator.reverse(center) 
            if(type(location) == list) :
                center_address  =   location[0].address
            else :
                center_address  =   location.address        
        
        except :
        
            geolocator      =   None
            center_address  =   None
           
        centerHeader        =   [""]
        centerRows          =   []
        centerWidths        =   [30,70]
        centerAligns        =   ["left","left"]
    
        centerRows.append(["Center Pt Coords ",str(center)])
    
        if(not (center_address is None)) :
            centerRows.append(["Center Pt Address ",str(center_address)])

        if(not ((center_dftitle == "get coords from coord(s)_list") or 
                (center_dftitle == "get coords from address(s)_list") )) :
            
            centerRows.append(["Points ",str(center_dftitle) + " dataframe"])  
        
        else :
            
            if(len(coords_list) < 10) :
        
                for i in range(len(coords_list)) :
                    if(i==0) :
                        centerRows.append(["Points ",""]) 
                
                    if(not(geolocator is None)) :
                
                        try :
        
                            location    =   geolocator.reverse(coords_list[i]) 
                            if(type(location) == list) :
                                point_address  =   location[0].address
                            else :
                                point_address  =   location.address        
        
                        except :
        
                            point_address  =   " "
                
                        centerRows.append([str(coords_list[i]),point_address])   
            
                    else :
                        centerRows.append([str(coords_list[i])," "])
                        
            else :
                
                centerRows.append(["Points ",str(coords_list)])    
                
                

        center_table        =   None
    
        from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
        center_table        =   dcTable("Center Point",'geocodecenterid',
                                        cfg.SWGeocodeUtility_ID,
                                        centerHeader,centerRows,
                                        centerWidths,centerAligns)
            
        center_table.set_small(True)
        center_table.set_checkLength(False)

        center_table.set_border(True)
        center_table.set_tabletype(ROW_MAJOR)
        center_table.set_rowspertable(50)
        centerHtml = get_row_major_table(center_table,SCROLL_DOWN,False)
    
        gridclasses     =   ["dfc-top"]
        gridhtmls       =   [centerHtml]
    
        display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)
        
        clock.stop() 
        
    else :
        
        clock.stop() 
        
        display_exception(opstat)
    
    
def process_df_center_dist(parms) :
    """
    * ---------------------------------------------------------
    * function : calculate the distance from center point of a column of coords 
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    DEBUG_DF_CENTER_DIST    =   False

    if(DEBUG_DF_CENTER_DIST) :
        print("process_df_center_dist : parms\n",parms)

    opstat  =   opStatus()
    clock   =   RunningClock()
    
    fparms  =   get_parms_for_input(parms,sugw.addr_df_center_dist_utility_input_idList)
    
    if(DEBUG_DF_CENTER_DIST) :
        print("\nprocess_df_center_dist : fparms\n",fparms,"\n")
    
    cfg.set_config_value(sugw.addr_df_center_dist_utility_input_id+"Parms",fparms)

    center_dftitle      =   fparms[0]
    center_points_list  =   None
    center_cols_list    =   []
    
    if(not (center_dftitle == "get center point from coords_for_center_point")) :
        
        center_df             =   cfg.get_dataframe(center_dftitle)
        
        if(not (center_df is None)) :
            
            center_lat_lng_cols   =   fparms[1] 
        
            if(len(center_lat_lng_cols) > 0) :
        
                try :
    
                    center_cols_list    =   center_lat_lng_cols.lstrip("[")
                    center_cols_list    =   center_cols_list.rstrip("]")
                    center_cols_list    =   center_cols_list.split(",")
    
                    if(len(center_cols_list) > 2) :
                
                        opstat.set_status(False)
                        opstat.set_errorMsg("dataframe_lat_lng_columns : too many column names " + str(center_cols_list))
            
                    else :
                
                        from dfcleanser.common.common_utils import is_column_in_df
                        for i in range(len(center_cols_list))  :
                
                            if(not (is_column_in_df(center_df,center_cols_list[i]))) :
                                opstat.set_status(False)
                                opstat.set_errorMsg("dataframe_lat_lng_columns column name is invalid " + str(center_cols_list[i]))
                                break
                
                except Exception as e:
                    opstat.store_exception("dataframe_lat_lng_columns " + str(fparms[1]),e)
            
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("dataframe_lat_lng_columns are not defined ") 
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("center dataframe is invalid " + str(center_dftitle)) 
            
    else :
        
        try :
    
            import json
            center_points_list     =   json.loads(fparms[3])
            
        except Exception as e:
            opstat.store_exception("center coord(s)_list is invalid " + str(fparms[3]),e)

    if(DEBUG_DF_CENTER_DIST) :
        print("\ncenter_cols_list",center_cols_list)
        print("\ncenter_points_list",center_points_list,"\n")

    coords_dftitle      =   fparms[7]
    coords_list         =   None
    coords_cols_list    =   []
    
    if(coords_dftitle == "get distance from coord(s) from distance_from_coord(s)_list") :
        
        try :
    
            import json
            coords_list     =   json.loads(fparms[10])
            
        except Exception as e:
            opstat.store_exception("distance_from_coord(s)_list " + str(fparms[10]),e)
    
    elif(coords_dftitle == "get distance from address(s) from distance_from_address(s)_list") :

        try :

            addrs_list  =   fparms[10].lstrip("[")
            addrs_list  =   addrs_list.rstrip("]")
            addrs_list  =   addrs_list.replace("'","") 
            addrs_list  =   addrs_list.split(",")
            
            for i in range(len(addrs_list)) :
                addrs_list[i]  =   addrs_list[i].lstrip(" ")
                addrs_list[i]  =   addrs_list[i].rstrip(" ")    
            
            geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    
            if(geocid is None) :
                geocid  =   sugm.GoogleId
        
            geolocator      =   None
            coords_list     =   []
    
            try :
        
                geolocator  =   get_geocoder_engine(geocid,opstat) 
                
                for i in range(len(addrs_list)) :
                
                    location    =   geolocator.geocode(addrs_list[i]) 
                    
                    if(type(location) == list) :
                        
                        coords  =   [location[0].latitude,location[0].longitude]
                    else :
                        coords  =   [location.latitude,location.longitude]  
                        
                    coords_list.append(coords)
        
            except Exception as e:
        
                geolocator      =   None
                opstat.store_exception("Unable to run geocoder to get coordinates for addresses " + str(fparms[10]),e)
            
        except Exception as e:
            opstat.store_exception("from distance_from_address(s)_list is invalid " + str(fparms[10]),e)
    
    else :
        
        coords_df             =   cfg.get_dataframe(coords_dftitle)
        
        if(not (coords_df is None) ) :
            
            coords_lat_lng_cols   =   fparms[8] 
        
            if(len(coords_lat_lng_cols) > 0) :
        
                try :
                    
                    coords_cols_list    =   coords_lat_lng_cols.lstrip("[")
                    coords_cols_list    =   coords_cols_list.rstrip("]")
                    coords_cols_list    =   coords_cols_list.split(",")
                    
                    if(len(coords_cols_list) > 2) :
                
                        opstat.set_status(False)
                        opstat.set_errorMsg("dataframe_lat_lng_columns : too many column names " + str(coords_cols_list))
            
                    else :
                
                        from dfcleanser.common.common_utils import is_column_in_df
                        for i in range(len(coords_cols_list))  :
                
                            if(not (is_column_in_df(coords_df,coords_cols_list[i]))) :
                                opstat.set_status(False)
                                opstat.set_errorMsg("dataframe_for_distance_lat_lng_columns column name is invalid " + str(coords_cols_list[i]))
                                break
                
                except Exception as e:
                    opstat.store_exception("dataframe_for_distance_lat_lng_columns is invalid" + str(fparms[8]),e)
            
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("dataframe_for_distance_lat_lng_columns are not defined ") 
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("coords dataframe is invalid : " + str(coords_dftitle)) 
            
            
    if(opstat.get_status()) :
        
        clock.start()
        
        dist_from_center_pt_col_names_list  =   []
        
        if(not ((coords_dftitle == "get distance from address(s) from distance_from_address(s)_list") or 
                (coords_dftitle == "get distance from coord(s) from distance_from_coord(s)_list")) ) :
        
            dist_from_center_pt_col_names       =   fparms[11]
            dist_from_center_pt_col_names       =   dist_from_center_pt_col_names.lstrip("[")
            dist_from_center_pt_col_names       =   dist_from_center_pt_col_names.rstrip("]")
            dist_from_center_pt_col_names       =   dist_from_center_pt_col_names.replace("'","")
            dist_from_center_pt_col_names_list  =   dist_from_center_pt_col_names.split(",")
                
            if(DEBUG_DF_CENTER_DIST) :
                print("dist_from_center_pt_col_names_list",type(dist_from_center_pt_col_names_list),dist_from_center_pt_col_names_list)
            
        # get center points
        if(len(center_cols_list) > 0) :
            
            import json
            
            lat_lngs_center_list    =   []
             
            if(len(center_cols_list) == 1)   :
                
                joint_lats_lngs     =   list(center_df[center_cols_list[0]])
                
                for i in range(len(joint_lats_lngs)) :
                    
                    current_lat_lng     =   json.loads(joint_lats_lngs[i])
                    current_lat_lng[0]  =   float(current_lat_lng[0])
                    current_lat_lng[1]  =   float(current_lat_lng[1])
                    lat_lngs_center_list.append(current_lat_lng)
                    
            else :
                
                lats_list   =   list(center_df[center_cols_list[0]])
                lngs_list   =   list(center_df[center_cols_list[1]])
                
                for i in range(len(lats_list)) :
                    current_lat_lng     =   [float(lats_list[i]),float(lngs_list[i])]  
                    lat_lngs_center_list.append(current_lat_lng)
                    
            center_points_list   =   [sugm.get_geocode_center(lat_lngs_center_list,opstat)]            
                    

    if(opstat.get_status()) :
        
        if(DEBUG_DF_CENTER_DIST) :
            print("\ncenter_points_list",center_points_list)
            print("\ncoords_cols_list",coords_cols_list)
        
        if(len(coords_cols_list) > 0) :
            
            if(DEBUG_DF_CENTER_DIST) :
                print("coords_cols_list",coords_cols_list)
            
            import json
            
            try :
            
                lat_lngs_coords_list    =   []
             
                if(len(coords_cols_list) == 1)   :
                
                    joint_lats_lngs     =   list(coords_df[coords_cols_list[0]])
                
                    for i in range(len(joint_lats_lngs)) :
                    
                        current_lat_lng     =   json.loads(joint_lats_lngs[i])
                        current_lat_lng[0]  =   float(current_lat_lng[0])
                        current_lat_lng[1]  =   float(current_lat_lng[1])
                        lat_lngs_coords_list.append(current_lat_lng)
                    
                else :
                
                    lats_list   =   list(coords_df[coords_cols_list[0]])
                    lngs_list   =   list(coords_df[coords_cols_list[1]])
                
                    for i in range(len(lats_list)) :
                    
                        current_lat_lng     =   [float(lats_list[i]),float(lngs_list[i])]  
                        lat_lngs_coords_list.append(current_lat_lng)
                    
                coords_list     =   lat_lngs_coords_list
            
            except Exception as e:
                opstat.store_exception("coords_list is invalid" + str(coords_list),e)


            
    if(opstat.get_status()) :
        
        if(DEBUG_DF_CENTER_DIST) :
            print("\ncenter_points_list",len(center_points_list),center_points_list)
        
            if(len(coords_list) > 10) :
                print("coords_list",len(coords_list))
            else :
                print("coords_list",coords_list)
        
        # calculate distances
        
        distance_units  =   fparms[4]
        algorithm       =   fparms[5]
        elipsoid        =   fparms[6]
        
        if(not ((coords_dftitle == "get distance from address(s) from distance_from_address(s)_list") or 
                (coords_dftitle == "get distance from coord(s) from distance_from_coord(s)_list")) ) :
        
            if(not (len(center_points_list) == len(dist_from_center_pt_col_names_list))) :
                opstat.set_status(False)
                opstat.set_errorMsg("Number of distance_from_center_point_column_name(s) does not match number of center points")
                
        if(opstat.get_status()) :
            
            distance_multiple_list  =   [] 
            
            for i in range(len(center_points_list)) :
                
                distances   =   []
                
                for j in range(len(coords_list)) :
                    current_distance     =   calculate_geocode_distances(center_points_list[i],coords_list[j],distance_units,algorithm,elipsoid,opstat)
                    
                    if(opstat.get_status()) :
                        distances.append(round(current_distance[0],4))
                    else :
                        distances   =   []
                        break
                    
                if(opstat.get_status()) :
                    distance_multiple_list.append(distances)
                else :
                    distance_multiple_list   =   []
                    break
                
            if(opstat.get_status())   :     
                
                if(DEBUG_DF_CENTER_DIST) :
                    print("\ndistance_multiple_list",len(distance_multiple_list))
                    for i in range(len(distance_multiple_list)) :
                        print("distance_multiple_list[i]",i,len(distance_multiple_list[i]))
                    
                cpoints     =   []
                frompoints  =   []
                cdists      =   []
                    
                for i in range(len(distance_multiple_list)) :
                    
                    if(len(dist_from_center_pt_col_names_list) > 0) :
                        
                        from dfcleanser.data_transform.data_transform_columns_control import add_column_to_df
                        coords_df     =   add_column_to_df(coords_df,dist_from_center_pt_col_names_list[i],distance_multiple_list[i],opstat,False) 
                        
                        if(DEBUG_DF_CENTER_DIST) :
                            print("astype",type(dist_from_center_pt_col_names_list[i]),dist_from_center_pt_col_names_list[i])
                            
                        coords_df[dist_from_center_pt_col_names_list[i]] = coords_df[dist_from_center_pt_col_names_list[i]].astype(float,copy=False)            
                        
                        cfg.set_dfc_dataframe_df(coords_dftitle,coords_df)
                        
                    else :
                        
                        cpoints.append(center_points_list[i])
                        frompoints.append(coords_list[i])
                        cdists.append(distance_multiple_list[i])

        
    if(opstat.get_status())  : 
        
        if(DEBUG_DF_CENTER_DIST) :
            print("After Run\n",center_dftitle,center_cols_list,center_points_list,"\n",coords_dftitle,coords_cols_list,len(coords_list),"\n",dist_from_center_pt_col_names_list)
            print("\ndistance_multiple_list",distance_multiple_list)

        centerdistHeader        =   [""]
        centerdistRows          =   []
        centerdistWidths        =   [30,70]
        centerdistAligns        =   ["left","left"]
        
        
        centerdistRows.append(["Center Pt Coords ",""]) 
        
        center_addresses    =   []
        
        geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    
        if(geocid is None) :
            geocid  =   sugm.GoogleId
        
        geolocator  =   None
    
        try :
                
            for i in range(len(center_points_list)) :
        
                geolocator  =   get_geocoder_engine(geocid,opstat) 
                location    =   geolocator.reverse(center_points_list[i]) 
                if(type(location) == list) :
                    center_address  =   location[0].address
                else :
                    center_address  =   location.address 
                        
                center_addresses.append(center_address)
        
        except :
        
            geolocator          =   None
            center_addresses    =   []
            
        if(DEBUG_DF_CENTER_DIST) :
            print("center_addresses",center_addresses,"\n")
        
        for i in range(len(center_points_list)) :
            
            center_point    =   [round(center_points_list[i][0],7),round(center_points_list[i][1],7)]
            
            if(center_addresses is None) :
                centerdistRows.append(["&nbsp;&nbsp;" + str(center_point),""]) 
            else :
                if(not (len(center_addresses) == 0)) :
                    centerdistRows.append(["&nbsp;&nbsp;" + str(center_point),str(center_addresses[i])]) 
                else :
                    centerdistRows.append(["&nbsp;&nbsp;" + str(center_point),""]) 
                
        dist_addresses  =   []
        
        if(coords_dftitle == "get distance from address(s) from distance_from_address(s)_list") :
            
            dist_addresses    =   addrs_list    
            
        elif(coords_dftitle == "get distance from coord(s) from distance_from_coord(s)_list") :
            
            try :
                
                for i in range(len(coords_list)) :
        
                    geolocator  =   get_geocoder_engine(geocid,opstat) 
                    location    =   geolocator.reverse(coords_list[i]) 
                    if(type(location) == list) :
                        dist_address  =   location[0].address
                    else :
                        dist_address  =   location.address 
                        
                    dist_addresses.append(dist_address)
        
            except :
        
                geolocator        =   None
                dist_addresses    =   []
        
        else :
            dist_addresses    =   []   

        if(DEBUG_DF_CENTER_DIST) :
            print("\ndist_addresses",dist_addresses)    
        
        
        if(not ((coords_dftitle == "get distance from address(s) from distance_from_address(s)_list") or 
                (coords_dftitle == "get distance from coord(s) from distance_from_coord(s)_list") )) :
            
            centerdistRows.append(["Dist From Coords",str(coords_dftitle) + " dataframe"]) 
            
            for i in range(len(dist_from_center_pt_col_names_list)) :
                
                if(i==0) :
                    centerdistRows.append(["New Col Names","Center Point Coords"]) 
                    
                centerdistRows.append(["&nbsp;&nbsp;" + str(dist_from_center_pt_col_names_list[i]),str(center_points_list[i])])
        
        else :
            
            if(len(center_points_list) < 10) :
        
                for i in range(len(center_points_list)) :
                    
                    for j in range(len(coords_list)) :
                        
                        if(j==0) :
                            
                            center_point    =   [round(center_points_list[i][0],7),round(center_points_list[i][1],7)]
                            
                            centerdistRows.append(["",""])
                            centerdistRows.append(["Center Point ",str(center_point)]) 
                            centerdistRows.append(["&nbsp;&nbsp;Distance (" + str(distance_units) + ")","&nbsp;&nbsp;From Point "])
                
                        coords_point    =   [round(coords_list[j][0],7),round(coords_list[j][1],7)]
                        centerdistRows.append(["&nbsp;&nbsp;&nbsp;" + str(cdists[i][j]),"&nbsp;&nbsp;&nbsp;" + str(coords_point) + " : " + str(dist_addresses[j])])   
                        
            else :
                
                centerdistRows.append(["Center Points",str(center_points_list)])  
                centerdistRows.append(["Distances (" + str(distance_units) + ")",""])
                for i in range(len(center_points_list)) :
                    centerdistRows.append(cdists[i])
                
        from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
        centerdist_table        =   dcTable("Distance From Center Points",'geocodecenterid',
                                            cfg.SWGeocodeUtility_ID,
                                            centerdistHeader,centerdistRows,
                                            centerdistWidths,centerdistAligns)
            
        centerdist_table.set_small(True)
        centerdist_table.set_checkLength(False)

        centerdist_table.set_border(True)
        centerdist_table.set_tabletype(ROW_MAJOR)
        centerdist_table.set_rowspertable(50)
        centerdistHtml = get_row_major_table(centerdist_table,SCROLL_DOWN,False)
    
        gridclasses     =   ["dfc-top"]
        gridhtmls       =   [centerdistHtml]
    
        display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)

        clock.stop()

    else :
        
        display_exception(opstat)
        clock.stop()
            

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoders utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_sw_utility_geocodedata() :
    
    drop_owner_tables(cfg.SWGeocodeUtility_ID)
    
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWGeocodeUtility_ID)
    
    clear_sw_utility_geocode_cfg_values()


def clear_sw_utility_geocode_cfg_values() :
 
    cfg.drop_config_value(cfg.BULK_GEOCODE_MODE_KEY)
    cfg.drop_config_value("geocodeprocresultsParms")
    cfg.drop_config_value("geocodeprocresultsParmsProtect") 
    
    cfg.drop_config_value("bingqueryParms")
    cfg.drop_config_value("bingqueryParmsProtect")
    cfg.drop_config_value("bingmax_geocode_results")
    cfg.drop_config_value("bingreverseParms")
    cfg.drop_config_value("bingreverseParmsProtect")

    cfg.drop_config_value("googlequeryParms")
    cfg.drop_config_value("googlequeryParmsProtect")
    cfg.drop_config_value("googlemax_geocode_results")
    cfg.drop_config_value("googlereverseParms")
    cfg.drop_config_value("googlereverseParmsProtect")

    cfg.drop_config_value("baiduqueryParms")
    cfg.drop_config_value("baiduqueryParmsProtect")
    cfg.drop_config_value("baidumax_geocode_results")
    cfg.drop_config_value("baidureverseParms")
    cfg.drop_config_value("baidureverseParmsProtect")

    
    
    
    #cfg.drop_config_value(sugw.addr_df_dist_utility_input_id+"Parms")
    cfg.drop_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)
    cfg.drop_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)
    cfg.drop_config_value(cfg.BULK_GEOCODE_MODE_KEY)    
    
    return




