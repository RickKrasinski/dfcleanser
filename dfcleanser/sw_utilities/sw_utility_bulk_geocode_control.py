"""
# sw_utility_bulk_geocode_control
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import json
import sys
import geopy
import googlemaps

import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_console as subgc
import dfcleanser.sw_utilities.sw_utility_geocode_control as sugc

from dfcleanser.common.common_utils import (display_exception, display_status,  
                                            RunningClock, get_parms_list_from_dict, opStatus,
                                            delete_a_file, rename_a_file, does_file_exist,
                                            get_parms_for_input, run_jscript, display_notes,
                                            does_dir_exist, make_dir, log_debug_dfc, clear_dfc_debug_log)

from dfcleanser.common.display_utils import (displayParms)

from math import floor

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Common bulk geocoding control methods
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def process_bulk_geocoding_run_cmd(cmd, parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : process the bulk geocoding commands
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"process_bulk_geocoding_run_cmd " + str(cmd))
        if(not(parms is None)) :
            log_debug_dfc(-1,"process_bulk_geocoding_run_cmd " + str(parms))    
    
    opstat  =   opStatus()
    
    if(cmd == sugm.BULK_START_GEOCODER) :
        opstat  =   start_geocode_runner()
                
        if(not (opstat.get_status()) ) :
            send_run_report_error(cmd, opstat.get_errorMsg()) 
            
    elif(cmd == sugm.BULK_STOP_GEOCODER) :
        stop_geocode_runner(None)
        
    elif(cmd == sugm.BULK_PAUSE_GEOCODER) :
        pause_geocode_runner()
        
    if(cmd == sugm.BULK_RESUME_GEOCODER) :
        resume_geocode_runner()
    
    elif(cmd == sugm.BULK_VIEW_ERRORS) :
        run_jscript("view_geocode_errors();","view_geocode_errors")
        
    elif(cmd == sugm.BULK_RESULTS_GEOCODER) :
        
        error_log       =   get_geocode_runner_error_log()
        total_errors    =   error_log.get_error_count()        
        total_results   =   get_geocode_runner_results_count()  
        
        if((total_errors==0) and (total_results==0)) :
            display_status("No Bulk Geocoding Results to Process") 
        else :
            subgc.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_BASE,opstat)
        
    elif(cmd == sugm.REPORT_GEOCODE_RUN_ERROR) :
        
        run_cmd     =   int(parms[0])
        err_msg     =   parms[1]
        geocid      =   get_geocode_runner_id() 
        geotype     =   get_geocode_runner_type() 
        
        if(run_cmd==sugm.BULK_LOAD_GEOCODER) : cmd_text         =   "Load Geocoder"
        elif(run_cmd==sugm.BULK_START_GEOCODER) : cmd_text      =   "Start Geocoder"
        elif(run_cmd==sugm.BULK_STOP_GEOCODER) : cmd_text       =   "Stop Geocoder"
        elif(run_cmd==sugm.BULK_PAUSE_GEOCODER) : cmd_text      =   "Pause Geocoder"
        elif(run_cmd==sugm.BULK_RESUME_GEOCODER) : cmd_text     =   "Resume Geocoder"
        elif(run_cmd==sugm.BULK_VIEW_ERRORS) : cmd_text         =   "View Errors Geocoder"
        elif(run_cmd==sugm.BULK_RESULTS_GEOCODER) : cmd_text    =   "Get Results Geocoder"
        elif(run_cmd==sugm.PROCESS_BULK_RESULTS) : cmd_text     =   "Process Results Geocoder"
        else :                                     cmd_text     =   "Unknown command"
        
        if(geocid is None)      :   geocid      =   "None"
        if(geotype is None)     :   geotype     =   "None"
        if(err_msg is None)     :   err_msg     =   "No  details"
        
        sugw.display_geocode_main_taskbar()        
        sugc.clear_sw_utility_geocodedata()


        print("\n")

        display_status("Bulk Geocoding Runtime Error : " + cmd_text,False,True)

        notes     =   ["geocid  : " + str(geocid),
                       "geotype : " + str(geotype),
                       "Details : " + err_msg]
        
        display_notes(notes,True)

def send_run_report_error(cmd, err_msg) :
    
    report_error_js     =   "report_geocode_run_error(" + str(cmd) + ",'" + err_msg + "');"
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"send_run_report_error " + str(cmd) + " " + str(err_msg))
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(report_error_js,"fail report run error : "+ str(cmd) + err_msg)
    
    

"""
#----------------------------------------------------------------------------
#-  Common Test bulk geocoder connect
#----------------------------------------------------------------------------
"""

def validate_bulk_geocode_connect_parms(geocid) :
    """
    * ---------------------------------------------------------
    * function : validate bulk geocodr parms 
    * 
    * parms :
    *  geocid  - geocoder id
    *
    * returns : 
    *  True or False 
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    fparms  =   None
    
    if(geocid is None) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No geocoder connect parms defined for validation")
        
    else :

        fparms    =   cfg.get_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms")
    
    if(not(fparms == None)) :
        
        print("fparms",fparms)        
        if(geocid == sugm.ArcGISId)              :
            validate_batch_arcgis_geocoder_parms(fparms,opstat)

        elif(geocid == sugm.BingId)              : 
            subgw.validate_bing_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.GoogleId)            : 
            validate_bulk_google_geocoder_parms(fparms,opstat)

        elif(geocid == sugm.BaiduId)      : 
            subgw.validate_baidu_geocoder_parms(fparms,opstat,False)

    else :
        
        if(not(geocid == sugm.ArcGISId)) :
            opstat.set_status(False)
            opstat.set_errorMsg("No geocoder connect parms defined for validation")
        
    return(opstat)


def test_bulk_geocoder(geocid,inputs) :
    """
    * ---------------------------------------------------------
    * function : test bulk geocodr connection 
    * 
    * parms :
    *  geocid  - geocoder id
    *  inputs  - geocoder connect parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    if(geocid == sugm.ArcGISId) :
        test_arcgis_batch_connector(inputs)
    elif(geocid == sugm.GoogleId) :
        test_google_bulk_connector(inputs)  
    elif(geocid == sugm.BingId) :
        from dfcleanser.sw_utilities.sw_utility_geocode_control import test_geocoder
        test_geocoder(geocid,inputs,sugm.BULK)
    elif(geocid == sugm.BaiduId) :
        from dfcleanser.sw_utilities.sw_utility_geocode_control import test_geocoder
        test_geocoder(geocid,inputs,sugm.BULK)

    return()

    
"""
#----------------------------------------------------------------------------
#-  Common bulk geocoding control methods
#----------------------------------------------------------------------------
"""
def refresh_bulk_geocode_console() :

    geocid   =   get_geocode_runner_id() 
    geotype  =   get_geocode_runner_type() 
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"refresh_bulk_geocode_console " + str(geocid) + " " + str(geotype))
    
    if(geotype == sugm.QUERY) :
        get_bulk_coords(geocid,None,True)
    else :
        get_bulk_addresses(geocid,None,True)


def get_bulk_coords(geocid,inputs,refresh=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the bulk coords - validate parms and load job runner
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(not refresh) :
        clear_dfc_debug_log()
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"get_bulk_coords " + str(geocid) + " " + str(refresh))
 
    opstat  =   opStatus()
    parms   =   None 
    
    if(not (inputs == None)) :
        
        if(geocid == sugm.ArcGISId) :  
            
            fparms  =   get_parms_for_input(inputs,subgw.batch_arcgis_query_idList)
            cfg.set_config_value(subgw.batch_arcgis_query_id+"Parms",fparms)
            parms   =   inputs
            
        elif(geocid == sugm.GoogleId) :

            fparms  =   get_parms_for_input(inputs,subgw.bulk_google_query_input_idList)
            cfg.set_config_value(subgw.bulk_google_query_input_id+"Parms",fparms)
            parms   =   inputs
        
        elif(geocid == sugm.BingId) :

            fparms  =   get_parms_for_input(inputs,subgw.bulk_bing_query_input_idList)
            cfg.set_config_value(subgw.bulk_bing_query_input_id+"Parms",fparms)
            parms   =   inputs
        
        elif(geocid == sugm.BaiduId) :

            fparms  =   get_parms_for_input(inputs,subgw.bulk_baidu_query_input_idList)
            cfg.set_config_value(subgw.bulk_baidu_query_input_id+"Parms",fparms)
            parms   =   inputs
        
    else :
        if(geocid == sugm.ArcGISId) :
            parms   =   [subgw.batch_arcgis_query_idList,cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")]
        elif(geocid == sugm.GoogleId) :
            parms   =   [subgw.bulk_google_query_input_idList,cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")]
        elif(geocid == sugm.BingId) :
            parms   =   [subgw.bulk_bing_query_input_idList,cfg.get_config_value(subgw.bulk_bing_query_input_id+"Parms")]
        elif(geocid == sugm.BaiduId) :
            parms   =   [subgw.bulk_baidu_query_input_idList,cfg.get_config_value(subgw.bulk_baidu_query_input_id+"Parms")]
    
    if(not(parms == None)) : 
        
        runParms    =   subgw.validate_bulk_parms(geocid,sugm.QUERY,parms,opstat) 
        
        if(opstat.get_status()) :
        
            if(geocid == sugm.GoogleId) :
            
                cfg.set_config_value(subgw.bulk_google_query_input_id+"Parms",
                                     get_parms_list_from_dict(subgw.bulk_google_query_input_labelList[:11],runParms))
            
                address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.GoogleId,sugm.QUERY,runParms,address_map)

                subgc.display_geocoder_console(sugm.GoogleId,sugm.QUERY,runParms,opstat,sugm.LOAD)
            
            elif(geocid == sugm.BingId) :
            
                cfg.set_config_value(subgw.bulk_bing_query_input_id+"Parms",
                                     get_parms_list_from_dict(subgw.bulk_bing_query_input_labelList[:11],runParms))
            
                address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.BingId,sugm.QUERY,runParms,address_map)

                subgc.display_geocoder_console(sugm.BingId,sugm.QUERY,runParms,opstat,refresh,sugm.LOAD)
            
            elif(geocid == sugm.BaiduId) :
            
                cfg.set_config_value(subgw.bulk_baidu_query_input_id+"Parms",
                                     get_parms_list_from_dict(subgw.bulk_baidu_query_input_labelList[:7],runParms))
            
                address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.BaiduId,sugm.QUERY,runParms,address_map)
                
                subgc.display_geocoder_console(sugm.BaiduId,sugm.QUERY,runParms,opstat,refresh,sugm.LOAD)
            
            else :
                
                cfg.set_config_value(subgw.batch_arcgis_query_id+"Parms",
                                     get_parms_list_from_dict(subgw.batch_arcgis_query_labelList[:11],runParms))
            
                address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
                subgc.display_geocoder_console(sugm.ArcGISId,sugm.QUERY,runParms,opstat,refresh,sugm.LOAD)
                if(not (refresh)) :
                    load_geocode_runner(sugm.ArcGISId,sugm.QUERY,runParms,address_map)

                run_arcgis_bulk_geocode(runParms,sugm.BULK_LOAD_GEOCODER,opstat)
        
        else :
            subgw.display_bulk_geocoding(geocid,sugm.QUERY)
            display_exception(opstat)
       
    
def get_bulk_addresses(geocid,inputs,refresh=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the bulk coords - validate parms and load job runner
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(not refresh) :
        clear_dfc_debug_log()
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"get_bulk_addresses " + str(geocid) + " " + str(refresh))
    
    opstat  =   opStatus()
    parms   =   None
    
    if(not (inputs == None)) :
        
        if(geocid == sugm.GoogleId) :
            fparms  =   get_parms_for_input(inputs,subgw.bulk_google_reverse_input_idList)
            cfg.set_config_value(subgw.bulk_google_reverse_input_id+"Parms",fparms)
            parms   =   inputs
        elif(geocid == sugm.BingId) :
            fparms  =   get_parms_for_input(inputs,subgw.bulk_bing_reverse_input_idList)
            cfg.set_config_value(subgw.bulk_bing_reverse_input_id+"Parms",fparms)
            parms   =   inputs
        elif(geocid == sugm.BaiduId) :
            fparms  =   get_parms_for_input(inputs,subgw.bulk_baidu_reverse_input_idList)
            cfg.set_config_value(subgw.bulk_baidu_reverse_input_id+"Parms",fparms)
            parms   =   inputs
        
    else :
        
        if(geocid == sugm.GoogleId) :
            parms   =   [subgw.bulk_google_reverse_input_idList,cfg.get_config_value(subgw.bulk_google_reverse_input_id+"Parms")]
        elif(geocid == sugm.BingId) :
            parms   =   [subgw.bulk_bing_reverse_input_idList,cfg.get_config_value(subgw.bulk_bing_reverse_input_id+"Parms")]
        elif(geocid == sugm.BaiduId) :
            parms   =   [subgw.bulk_baidu_reverse_input_idList,cfg.get_config_value(subgw.bulk_baidu_reverse_input_id+"Parms")]
            
    if(not (parms == None)) :    
        runParms    =   subgw.validate_bulk_parms(geocid,sugm.REVERSE,parms,opstat) 
            
        if(opstat.get_status()) :
        
            if(geocid == sugm.GoogleId) :
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.GoogleId,sugm.REVERSE,runParms,None)

                subgc.display_geocoder_console(sugm.GoogleId,sugm.REVERSE,runParms,opstat,refresh,sugm.LOAD)
                
            elif(geocid == sugm.BingId) :
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.BingId,sugm.REVERSE,runParms,None)

                subgc.display_geocoder_console(sugm.BingId,sugm.REVERSE,runParms,opstat,refresh,sugm.LOAD)
                
            elif(geocid == sugm.BaiduId) :
                
                if(not (refresh)) :
                    load_geocode_runner(sugm.BaiduId,sugm.REVERSE,runParms,None)

                subgc.display_geocoder_console(sugm.BaiduId,sugm.REVERSE,runParms,opstat,refresh,sugm.LOAD)

        else :
            subgw.display_bulk_geocoding(geocid,sugm.REVERSE)
            display_exception(opstat)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   arcgis batch geocoding methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   arcgis connector methods
#--------------------------------------------------------------------------
"""
def validate_batch_arcgis_geocoder_parms(connectParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the arcgis batch connect parms
    * 
    * parms :
    *  connectParms - arcgis connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if( (len(connectParms[1]) == 0) or (len(connectParms[2]) == 0) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("arcGIS connect parms incomplete")


def get_arcgis_batch_geocode_connection(user,pw,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get an arcgis batch connection and return the batch parms
    * 
    * parms :
    *  user   - arcgis user id
    *  pw     - arcgis passowrd
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    from arcgis.gis import GIS
    from arcgis.geocoding import get_geocoders
    
    gis = GIS("http://www.arcgis.com", user, pw)

    geoocoder_not_found       =   True
    
    while (geoocoder_not_found) :
        for i in range(5) :
            if(geoocoder_not_found) :
                try :
                    geocoder                =   get_geocoders(gis)[i]
                    geoocoder_not_found     =   False

                except Exception as e:
                    opstat.store_exception("Unable to connect to arcgis ",e)

    if(opstat.get_status()) :
        
        arcgis_MaxBatchSize         =   geocoder.properties.locatorProperties.MaxBatchSize
        arcgis_SuggestedBatchSize   =   geocoder.properties.locatorProperties.SuggestedBatchSize
        
        return([geocoder,[arcgis_MaxBatchSize,arcgis_SuggestedBatchSize]])
    
    else :
        
        return(None)

def test_arcgis_batch_connection(user,pw,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : test the arcgis batch connection and retrieve the batch parms
    * 
    * parms :
    *  user   - arcgis user id
    *  pw     - arcgis passowrd
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    cparms  =   get_arcgis_batch_geocode_connection(user,pw,opstat)
    
    if(opstat.get_status()) :
        cfg.set_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,cparms[1][0],True)
        cfg.set_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,cparms[1][1],True)
        
    return(cparms[0])

"""
#------------------------------------------------------------------
#   test arcgis batch connector
#------------------------------------------------------------------
"""
def test_arcgis_batch_connector(connectParms) :

    opstat      =   opStatus()
    
    validate_batch_arcgis_geocoder_parms(connectParms,opstat)
    
    if(opstat.get_status()) :
    
        clock = RunningClock()
        clock.start()
    
        try :
    
            geocoder    =  test_arcgis_batch_connection(connectParms[1],connectParms[2],opstat)
            if(opstat.get_status()) :
                cfg.set_config_value(subgw.batch_arcgis_geocoder_id + "Parms",connectParms)
    
        except Exception as e:
            opstat.store_exception("Unable to connect to arcgis ",e)
    
        clock.stop()
    
    subgw.display_bulk_geocoders(sugm.ArcGISId)
    
    if(opstat.get_status()) :
        display_status("arcGIS batch geocoder connected to successfully")
        
        displayParms("arcGIS Batch Size Settings",
                     ["MaxBatchSize","SuggestedBatchSize"],
                     [str(cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)),
                      str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))],
                      cfg.SWUtilities_ID)
        
        try :
            addresses   =   ["11111 Euclid Ave, Cleveland OH "]
            from arcgis.geocoding import batch_geocode
            results     =   batch_geocode(addresses)#,geocoder=geocoder)
        except Exception as e:
            opstat.store_exception("Unable to geocode from arcgis ",e)
            
        if(opstat.get_status()) :
            
            test_results    =   results[0]
            score           =   test_results.get("score")
            attributes      =   test_results.get("attributes")
            address         =   test_results.get("address")
            location        =   test_results.get("location")
            
            displayParms("arcGIS Geocode Results",
                         ["Input Address","Lat : Long",
                          "Score","Returned Address"],
                         ["11111 Euclid Ave, Cleveland OH ",
                          str(location.get("x")) + " : " + str(location.get("y")),
                          str(score),
                          str(address)],
                          cfg.SWUtilities_ID)
            
            city            =   attributes.get("City","NA")
            subregion       =   attributes.get("Subregion","NA")
            region          =   attributes.get("Region","NA")
            postal          =   attributes.get("Postal","NA")
            country         =   attributes.get("Country","NA")
            
            displayParms("arcGIS Address Results",
                         ["City","Subregion",
                          "Region","Postal","Country"],
                         [str(city),str(subregion),str(region),
                          str(postal),
                          str(country)],
                          cfg.SWUtilities_ID)

    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 


"""
#--------------------------------------------------------------------------
#   arcgis geocode methods - only query supported
#--------------------------------------------------------------------------
"""

def get_arcgis_batch_addresses(runParms,addressMap,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the batch address list for arcgis batch geocoder
    * 
    * parms :
    *  rowIndex     - dataframe row index
    *  runParms     - batch run parms
    *  addressMap   - addres string map
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"get_arcgis_batch_addresses")
    
    start_row   =   get_geocode_runner_results_count()    
    
    try :
    
        arcgisbatch     =   []

        batchSize   =   int(cfg.get_cfg_parm_from_input_list(subgw.batch_arcgis_query_id,"batch_size",subgw.batch_arcgis_query_labelList))
        maxAddrs    =   int(cfg.get_cfg_parm_from_input_list(subgw.batch_arcgis_query_id,"max_addresses_to_geocode",subgw.batch_arcgis_query_labelList))
    
        if((start_row + batchSize) > maxAddrs) :
            stopRow     =   maxAddrs - 1
        else :
            stopRow     =   (start_row + batchSize) - 1
        
        for i in range(start_row,stopRow) :
            arcgisbatch.append(sugm.get_geocode_address_string(sugm.ArcGISId,runParms,addressMap,i))
    
    except Exception as e:
        opstat.store_exception("Unable to get arcgis batch address list",e)
        
    return(arcgisbatch)


def run_arcgis_bulk_geocode(runParms,state,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : control the arcgis bulk geocoder
    * 
    * parms :
    *  runParms     - arcgis run parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    opstat  =   opStatus()
            
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"run_arcgis_bulk_geocode")
    
    if(state == sugm.LOAD) :
        address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
    
        if(opstat.get_status()) :
            subgc.display_geocoder_console(sugm.ArcGISId,runParms,opstat)
            load_geocode_runner(sugm.ArcGISId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,False,sugm.RUNNING)
        opstat  =   sugm.start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,False,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,False,sugm.PAUSING)


def get_arcgis_geocode_batch(geocoder,addresslist,runParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a single arcgis goeocode batch
    * 
    * parms :
    *  geocoder         - arcgis geocoder
    *  addresslist      - lisy of addresses
    *
    * returns : 
    *   list of batch geocode results
    * --------------------------------------------------------
    """
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"get_arcgis_geocode_batch"+ str(len(addresslist)))
    
    geocode_list        =   []
    
    address_col_name     =   runParms.get(subgw.batch_arcgis_query_labelList[3],None)
    if(address_col_name == "") : address_col_name     =   None
    
    country         =   runParms.get(subgw.batch_arcgis_query_labelList[4],None)
    if(country == "None") : country     =   None
    
    category        =   runParms.get(subgw.batch_arcgis_query_labelList[5],None)
    if(category == "None") : category     =   None
    
    out_sr          =   runParms.get(subgw.batch_arcgis_query_labelList[6],None)
    if(out_sr == "None") : out_sr     =   None
    
    if(sugm.GEOCODE_DEBUG)  : 
        if(country == None) :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " country : None")
        else :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " country : " + str(country))
        if(category == None) :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " category : None")
        else :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " category : " + str(category))
        if(out_sr == None) :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " out_sr : None")
        else :
            log_debug_dfc(-1,"get_arcgis_geocode_batch  : " + " out_sr : " + str(out_sr))
            
        for i in range(len(addresslist)) :
            log_debug_dfc(-1,"[" + str(i) + "]" + str(addresslist[i]))            

    try :
        from arcgis.geocoding import batch_geocode
        results = batch_geocode(addresslist,country,category,out_sr,None)
        
    except RuntimeError as e :
        opstat.set_status(False)
        opstat.set_errorMsg("ArcGIS batch_geocode : " + e.message)
    except :
        opstat.set_status(False)
        import sys
        opstat.set_errorMsg("ArcGIS batch_geocode : " + str(sys.exc_info()[0].__name__))
    
    if(opstat.get_status()) :

        for result in results :

            score           =   result['score']

            location        =   result['location']
            lat             =   location['x']
            long            =   location['y']
        
            attributes      =   result['attributes']
            Addr_type       =   attributes['Addr_type']
            
            if(not (address_col_name is None)) : 
                address     =   result['address']
                geocode_list.append([score,lat,long,address,Addr_type])
            else :
                geocode_list.append([score,lat,long,Addr_type])
    
    else :
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"get_arcgis_geocode_batch"+ opstat.get_errorMsg())
    
    return(geocode_list)


def process_arcgis_geocode_batch_results(batch_results,batch_addresses,runParms,opstat,error_rowid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : process a single arcgis goeocode batch
    * 
    * parms :
    *  batch_results    - single arcgis batch results
    *  batch_addresses  - batch addresses geocoded
    *  runParms         - geocoder run parms
    *  opstat           - run op status
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    results_df          =   get_geocode_runner_results_log()

    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"process_arcgis_geocode_batch_results " + str(len(batch_results)))        

    
    if(not(error_rowid is None)):
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"add_nan_result for None")        

        parmsDict   =   None
        
        results_df.add_nan_result(error_rowid,batch_addresses[error_rowid],parmsDict,opstat)
        
    else :
        
        try :
            
            accept_score    =   float(runParms.get(subgw.batch_arcgis_query_labelList[8])) 
        
            lat_long_col_name   =   runParms.get(subgw.batch_arcgis_query_labelList[2])
            if(lat_long_col_name.find("]") > -1) :
                lat_long_names  =  json.loads(lat_long_col_name)
            else :
                lat_long_names  =  [lat_long_col_name]
                
            address_col_name     =   runParms.get(subgw.batch_arcgis_query_labelList[3],None)
            if(address_col_name == "") : address_col_name     =   None
        
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"process_arcgis_geocode_batch_results : " + str(accept_score) + " " + address_col_name)        
    
            for i in range(len(batch_results)) :
                
                df_row_id   =   get_geocode_runner_results_count() + i
                
                current_score   =   batch_results[i][0]
                current_lat     =   batch_results[i][1]
                current_lng     =   batch_results[i][2]
                
                if(not (address_col_name is None)) :
                    current_address =   batch_results[i][3]
        
            # check if score is acceptable
            if(current_score >=  accept_score) :
                
                if(not (address_col_name is None)) :
                    if(len(lat_long_names) == 1) :
                        results_df.add_result([df_row_id, batch_addresses[i], [current_lat,current_lng], current_address], opstat)
                    else :
                        results_df.add_result([df_row_id, batch_addresses[i], current_lat, current_lng, current_address], opstat)
                
                else :
                    
                    if(len(lat_long_names) == 1) :
                        results_df.add_result([df_row_id, batch_addresses[i], [current_lat,current_lng]], opstat)
                    else :
                        results_df.add_result([df_row_id, batch_addresses[i], current_lat, current_lng], opstat)
       
            else :
        
                process_bulk_geocoding_errors(sugm.ArcGisId,sugm.QUERY,df_row_id,
                                              batch_addresses[i],current_score)
        
                parmsDict   =   None
        
                results_df.add_nan_result(df_row_id,batch_addresses[i],parmsDict,opstat)

        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("process_google_results exception : " + str(sys.exc_info()[0].__name__))
 

def process_arcgis_geocode_batch_error(batch_results,runParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : process a arcgis goeocode error
    * 
    * parms :
    *  batch_results    - single arcgis batch results
    *  runParms         - run parms
    *  opstat           - run op status
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc("process_arcgis_geocode_batch_error")

    errorLog    =   sugm.get_geocode_runner_error_log(opstat)
    
    batchindex  =   errorLog.get_error_count() + 1
    inputValue  =   runParms[0]
    errorMsg    =   opstat.get_errorMsg()

    
    errorLog.log_error(batchindex,inputValue,errorMsg)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocoding components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def process_bulk_geocoding_errors(geocid,geotype,rowid,inputParms,error_msg,note=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : process a google bulk geocode error
    * 
    * parms :
    *   geocid      - geocoder id
    *   geotype     - geocoder cmd type
    *   rowid       - row id
    *   inputParms  - input parms causing error
    *   error_msg   - error message to log
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    error_limit         =   get_geocode_runner_error_log().get_error_limit()
    total_errors        =   get_geocode_runner_error_log().get_error_count()
    max_rows            =   get_geocode_maxrows()
    current_error_rate  =   (total_errors / max_rows) * 100   
    total_results       =   get_geocode_runner_results_log().get_results_count()

    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(rowid,"process_bulk_geocoding_errors : " + str(geotype) + " row : " + str(rowid) + " state : " + str(get_geocode_runner_state()) + " error_count : " + str(get_geocode_runner_error_log().get_error_count()) + " error_limit : " + str(error_limit) + " current_error_rate : " + str(current_error_rate))

    opstat  =   opStatus()
    
    if( (get_geocode_runner_state() == sugm.ERROR_LIMIT) ):
        return
    
    try :
        
        get_geocode_runner_error_log().log_error(rowid,inputParms,error_msg,note,opstat)
     
        subgc.set_progress_bar_value(geocid,geotype,sugm.ERROR_BAR,total_errors,int(current_error_rate))
    
        if(current_error_rate > error_limit) :
            
            if(not(get_geocode_runner_state() == sugm.ERROR_LIMIT)) :
                set_geocode_runner_halt_flag(True)  
                
                from threading import Thread 
                state_change     =   Thread(target=set_error_limit_shutoff)
                state_change.start()
                
                #set_geocode_runner_state(sugm.ERROR_LIMIT)
                subgc.set_status_bar(sugm.ERROR_LIMIT)
                get_geocode_runner_error_log().flush_errors_to_dataframe(opstat)
                
                if(total_errors > 0) :
                    get_geocode_runner_results_log().flush_results_to_dataframe(opstat)
                
                subgc.control_bulk_keys([subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.ENABLE,subgc.ENABLE])
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(rowid,"error limit exceeded : error_limit : " + str(error_limit) + " total_results : " + str(total_results) + " total_errors : " + str(total_errors))
            
    except :
        if(sugm.GEOCODE_DEBUG)  : 
            log_debug_dfc(rowid,"process_bulk_geocoding_errors Exception : " + str(geocid) + " " + str(geotype) + " " + str(rowid) + " " + str(sys.exc_info()[0].__name__))


def set_error_limit_shutoff() :
    set_geocode_runner_state(sugm.ERROR_LIMIT) 
    
    if(sugm.GEOCODE_DEBUG)  : 
        log_debug_dfc(-1,"set_error_limit_shutoff : geocoder state : " + str(get_geocode_runner_state()))

    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocode methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    
"""
#--------------------------------------------------------------------------
#   google bulk geocode connection methods
#--------------------------------------------------------------------------
"""
def get_bulk_google_geocoder_connection(apikey,cid,csecret,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a google bulk geocode connection
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    api_key     =   None
    gmaps       =   None
    
    if(len(apikey) == 0) : 
        client_ID       =  cid   
        client_Secret   =  csecret
    else :
        api_key     =   apikey
        
    try :
        if(api_key == None) :
            gmaps           =   googlemaps.Client(client_id=client_ID,client_secret=client_Secret)
        else :
            gmaps           =   googlemaps.Client(key=api_key)
        
    except ValueError :
        opstat.set_status(False)
        opstat.set_errorMsg("CLIENT CREDENTIALS INVALID")
    except NotImplementedError :
        opstat.set_status(False)
        opstat.set_errorMsg("NotImplementedError")
        
    return(gmaps)
        

def validate_bulk_google_geocoder_parms(connectParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the google connect parms
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if( len(connectParms[0]) == 0 ) :
        if( (len(connectParms[1]) == 0) or (len(connectParms[2]) == 0) ) :        
            opstat.set_status(False)
            opstat.set_errorMsg("google connect parms incomplete")
    

def test_google_bulk_connector(connectParms) :
    """
    * -------------------------------------------------------------------------- 
    * function : control the arcgis bulk geocoder
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    test_address    =   "1111 Euclid Ave, Cleveland OH "

    opstat      =   opStatus()
    validate_bulk_google_geocoder_parms(connectParms,opstat) 
    
    if(opstat.get_status()) :
    
        clock = RunningClock()
        clock.start()
    
        try :
            get_bulk_google_geocoder_connection(connectParms[0],connectParms[1],connectParms[2],opstat)
            
            if(opstat.get_status()) :
                cfg.set_config_value(subgw.google_bulk_geocoder_id + "Parms",connectParms)
            
                test_results    =   get_google_geocode_results(0,test_address,None,opstat) 
    
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("Test Google Geocoder exception" + str(sys.exc_info()[0].__name__))
    
        clock.stop()
    
    subgw.display_bulk_geocoders(sugm.GoogleId)
    
    if(opstat.get_status()) :
        
        print("\n")
        display_status("Google bulk geocoder connected to successfully")
        if(not (test_results == None)) :
            display_google_test_results(test_address,test_results)
    
    else :
        
        print("\n")
        display_status(opstat.get_errorMsg()) 


def display_google_test_results(address,results) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display google test geocoder connector results
    * 
    * parms :
    *  address - address to test with
    *  results - results returned
    *
    * returns : N/A
    * --------------------------------------------------------
    """
            
    displayParms("Google Geocode Results",
                 ["Input Address",
                  "Lat : Long",
                  "Location_Type",
                  "Returned Address"],
                  [address,
                   str(results.get_lat()) + " : " + str(results.get_lng()),
                   str(results.get_location_type()),
                   str(results.get_formatted_address())],
                   cfg.SWUtilities_ID)
    
    address_results    =   sugm.google_address_components(results.get_address_components())
    
    displayParms("Google Address Components",
                 [sugm.GOOGLE_GEOCODER_STREET_NUMBER_ID,
                  sugm.GOOGLE_GEOCODER_ROUTE_ID,
                  sugm.GOOGLE_GEOCODER_NEIGHBORHOOD_ID,
                  sugm.GOOGLE_GEOCODER_LOCALITY_ID,
                  sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID,
                  sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID,
                  sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID,
                  sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID,
                  sugm.GOOGLE_GEOCODER_COUNTRY_ID,
                  sugm.GOOGLE_GEOCODER_POSTAL_CODE_ID],
                  [address_results.get_address_component(sugm.GOOGLE_GEOCODER_STREET_NUMBER_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_ROUTE_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_NEIGHBORHOOD_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_LOCALITY_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_COUNTRY_ID),
                   address_results.get_address_component(sugm.GOOGLE_GEOCODER_POSTAL_CODE_ID)],
                  cfg.SWUtilities_ID)
 

"""
#--------------------------------------------------------------------------
#   google bulk geocode methods
#--------------------------------------------------------------------------
"""

def get_google_geocode_results(rowid,address,queryParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a single google goeocode result
    * 
    * parms :
    *  address          - address to geocode
    *  geocodeParms     - google geocode parms
    *
    * returns : 
    *    google geocode results
    * --------------------------------------------------------
    """
    
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(rowid,"get_google_geocode_results : "+ address)
        
    geocode_results =   None
    gmaps           =   get_geocode_connector() 
    
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
        gmaps   =   get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        set_geocode_connector(gmaps)
    
    if(opstat.get_status()) :   

        compParm    =   None
        boundsParm  =   None
        
        if(not (queryParms == None)) :
            
            from dfcleanser.common.common_utils import get_parms_list_from_dict 
            fparms   =   get_parms_list_from_dict(subgw.bulk_google_query_input_labelList,queryParms) 

            regionParm      =   fparms[5]
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            languagedict    =   get_Dict("Language_Codes")
            languageParm    =   languagedict.get(fparms[6])
        else :
            regionParm      =   None
            languageParm    =   None
    
        try :
            
            if(not (queryParms == None)) :
                geocode_results =   gmaps.geocode(address,
                                                  components=compParm,
                                                  bounds=boundsParm,
                                                  region=regionParm,
                                                  language=languageParm)
                
            else :
                geocode_results =   gmaps.geocode(address)
                
        except googlemaps.exceptions.ApiError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.OverQueryLimitErrorMessage)
        except  :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("get_google_geocode_results exception : " + str(sys.exc_info()[0].__name__))
        
    try :
    
        if(len(geocode_results) > 1) :  
            current_geocode_results    =  sugm.google_geocode_results(rowid,geocode_results[0],geocode_results[1])
        elif(len(geocode_results) == 1) : 
            current_geocode_results    =  sugm.google_geocode_results(rowid,None,geocode_results[0])    
        else :
            current_geocode_results    =  None
            
    except :
        current_geocode_results    =  None    
        
    return(current_geocode_results)


def process_google_geocode_results(inputParms,runParms,geocode_results,opstat,error_rowid=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : process google goeocode results
    * 
    * parms :
    *  inputParms       - input address parms
    *  runParms         - run time parms
    *  geocode_results  - google geocode results
    *  opstat           - op status var
    *  error_rowid      - row id of error
    *
    * returns : 
    *    google geocode results
    * --------------------------------------------------------
    """
    
    results_df          =   get_geocode_runner_results_log()
    
    if(runParms.get(subgw.bulk_google_query_input_labelList[7]) == "True") : 
        save_location_type      =   True
    else :
        save_location_type      =   False
    
    if(not(error_rowid is None)):
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"add_nan_result for None")        

        parmsDict   =   None
        
        if(save_location_type) :
            parmsDict   =   {}
            parmsDict.update({"location_type":"None"})
        
        results_df.add_nan_result(error_rowid,inputParms,parmsDict,opstat)
        
    else :
        
        try :
            
            lat_long_merged     =   False
        
            lat_long_col   =   runParms.get(subgw.bulk_google_query_input_labelList[2])
            if(lat_long_col.find("]") > -1) :
                lat_long_merged    =   True
    
            save_full_address   =   True
            full_addr_col_name  =   runParms.get(subgw.bulk_google_query_input_labelList[3])
            if(full_addr_col_name == "None") :
                save_full_address   =   False
        
            location_types      =   runParms.get(subgw.bulk_google_query_input_labelList[6])

            accept_all_types   =   False
    
            if(location_types == "ALL") :
                accept_all_types   =   True
            else :
                import json
                location_list  =   json.dumps(location_types)
        
            # check if location is acceptable
            if( (accept_all_types) or (geocode_results.get_location_type() in location_list) ) :
        
                if(save_full_address) :
            
                    if(save_location_type) :
                        if(lat_long_merged) :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_location_type(), geocode_results.get_formatted_address()],opstat)
                        else :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_location_type(), geocode_results.get_formatted_address()],opstat)
                    else :
                        if(lat_long_merged) :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_formatted_address()],opstat)
                        else :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_formatted_address()],opstat)
        
                else :
                    if(save_location_type) :
                        if(lat_long_merged) :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_location_type()],opstat)
                        else :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_location_type()],opstat)
                    else :
                        if(lat_long_merged) :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()]],opstat)
                        else :
                            results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng()],opstat)
       
            else :
        
                process_bulk_geocoding_errors(sugm.GoogleId,sugm.QUERY,geocode_results.get_row_Id(),
                                              inputParms,geocode_results.get_location_type())
        
                parmsDict   =   None
        
                if(save_location_type) :
                    parmsDict   =   {}
                    parmsDict.update({"location_type":geocode_results.get_location_type()})
        
                results_df.add_nan_result(geocode_results.get_row_Id(),inputParms,parmsDict,opstat)

        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("process_google_results exception" + str(sys.exc_info()[0].__name__))
 
           
"""
#--------------------------------------------------------------------------
#   google bulk geocode reverse methods
#--------------------------------------------------------------------------
"""

def find_best_google_reverse_result(reverse_results,reverseParms) :
    """
    * --------------------------------------------------------
    * function : find the best google reverse result 
    * 
    * parms :
    *  reverse_results  - reverse result set
    *  reverseParms     - run time parms
    *
    * returns : 
    *    NA stored in results df
    * --------------------------------------------------------
    """
    
    locations       =   reverseParms.get(subgw.bulk_google_reverse_input_labelList[5],None)
    
    location_types  =   locations.replace("[","")
    location_types  =   location_types.replace("]","")
    location_types  =   location_types.split(",")
    
    if(len(reverse_results) > 0) :
    
        if("ROOFTOP" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "ROOFTOP") :
                    if(sugm.GEOCODE_DEBUG)  :   
                        log_debug_dfc(-1,"found best fit at " + str(i))# + json.dumps(reverseParms))
                    
                    return(reverse_results[i])
        elif("GEOMETRIC_CENTER" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "GEOMETRIC_CENTER") :
                    return(reverse_results[i])
        elif("RANGE_INTERPOLATED" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "RANGE_INTERPOLATED") :
                    return(reverse_results[i])
        elif("APPROXIMATE" in location_types) :
            return(reverse_results[0])
        else :
            return(None)
            
    else :
        
        return(None)


def get_google_reverse_results(rowid,lat_long,reverseParms,opstat) :
    """
    * --------------------------------------------------------
    * function : get a single google reverse result
    * 
    * parms :
    *  lat_long         - [lat,long] to reverse
    *  reverseParms     - google reverse parms
    *  opstat           - status variable
    *
    * returns : 
    *    google geocode results
    * --------------------------------------------------------
    """
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(rowid,"get_google_reverse_results rowid : " + str(rowid) + " lat_lng " + str(lat_long))# + json.dumps(reverseParms))
    
    reverse_results =   None
    
    cparms  =   [" "," "," "]
    
    gmaps   =   get_geocode_connector() 
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
        gmaps   =   get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        set_geocode_connector(gmaps)

    if(opstat.get_status()) :  
        
        lat_lng_parm    =   lat_long.replace("[","")
        lat_lng_parm    =   lat_lng_parm.replace("]","")
        lat_lng_list    =   lat_lng_parm.split(",")
        
        if(not (reverseParms == None)) :
            location_typeParm   =   reverseParms.get(subgw.bulk_google_reverse_input_labelList[5],None)
            
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            languagedict    =   get_Dict("Language_Codes")
            languageParm    =   languagedict.get(reverseParms.get(subgw.bulk_google_reverse_input_labelList[6],None))
            
        else :
            location_typeParm   =   None
            languageParm        =   None

        if(not (location_typeParm is None)) :
            loc_type_parm   =  location_typeParm.replace("[","") 
            loc_type_parm   =  loc_type_parm.replace("]","")
            loc_type_parm   =  loc_type_parm.split()
        else :
            loc_type_parm   =  None    
            
        try :
        
            reverse_results =   gmaps.reverse_geocode(lat_lng_list,
                                                      result_type=None,
                                                      location_type=None,
                                                      language=languageParm)
   
        except googlemaps.exceptions.ApiError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.OverQueryLimitErrorMessage)
        except  :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("get_google_reverse_results exception : " + str(sys.exc_info()[0].__name__))
            
        if(opstat.get_status()) :
            try :
                
                best_results                =   find_best_google_reverse_result(reverse_results,reverseParms)
                current_reverse_results     =   sugm.google_reverse_results(rowid,None,best_results,opstat)
            
            except :
                current_reverse_results    =  None
                opstat.set_status(False)
                opstat.set_errorMsg("get_google_reverse_results assign results exception : ")
    
    if(sugm.GEOCODE_DEBUG)  :
        if(current_reverse_results is None) :
            log_debug_dfc(rowid,"get_google_reverse_results None : ")
        else :
            log_debug_dfc(rowid,"get_google_reverse_results  : " + " lat " + str(current_reverse_results.get_lat()) + " lng " + str(current_reverse_results.get_lng()) + " addr " +  str(current_reverse_results.get_formatted_address()))
    
    return(current_reverse_results)

    
def process_google_reverse_results(inputParms,runParms,reverse_results,opstat,error_rowid=None) :
    """
    * --------------------------------------------------------
    * function : process google reverse results 
    * 
    * parms :
    *  inputParms       - input parms
    *  runParms         - run time parms
    *  reverse_results  - reverse results
    *
    * returns : 
    *    NA stored in results df
    * --------------------------------------------------------
    """
    if(sugm.GEOCODE_DEBUG)  :   
        log_debug_dfc(-1,"process_google_reverse_results inparms : " + str(inputParms))
    
    results_df          =   get_geocode_runner_results_log()
    
    if(not(error_rowid is None)):
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"add_nan_result for None")        

        parmsDict   =   None
        results_df.add_nan_result(error_rowid,inputParms,parmsDict,opstat)
        
    else :
    
        try :
            address_components      =   sugm.google_address_components(reverse_results.get_address_components())
    
            requested_addr_comps    =   runParms.get(subgw.bulk_google_reverse_input_labelList[2])

            requested_addr_comps    =   requested_addr_comps.replace("[","")
            requested_addr_comps    =   requested_addr_comps.replace("]","")
            requested_addr_comps    =   requested_addr_comps.split(",")
            for i in range(len(requested_addr_comps)) :
                requested_addr_comps[i]     =   requested_addr_comps[i].lstrip(" ") 
                requested_addr_comps[i]     =   requested_addr_comps[i].rstrip(" ")
            
            addr_length             =   runParms.get(subgw.bulk_google_reverse_input_labelList[3])
            if(addr_length == "short") :
                addr_length     =   True
            else :
                addr_length     =   False
        
            import numpy as np
        
            addr_comps  =   []
            for i in range(len(requested_addr_comps)) :
                if(requested_addr_comps[i] == "full_address") :
                    addr_comp  =  reverse_results.get("formatted_address"," ")
                else :
                    addr_comp  =  address_components.get_address_component(requested_addr_comps[i],addr_length)
                    
                if(addr_comp == "") :
                    addr_comps.append(np.NaN) 
                else :
                    addr_comps.append(addr_comp)
                    
            row_reverse_results     =   []
            row_reverse_results.append(reverse_results.get_row_Id())
            row_reverse_results.append(inputParms)
            
            for i in range(len(addr_comps)) :
                row_reverse_results.append(addr_comps[i])    
            
            row_reverse_results.append(reverse_results.get_location_type())

            results_df.add_result(row_reverse_results,opstat)
        
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("process_google_reverse_results exception " + str(sys.exc_info()[0].__name__))





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geopy bulk geocode methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_geopy_geocoder_results(geocid,geotype,geolocator,rowid,geoparm,queryParms) :

    if(sugm.GEOCODE_THREAD_DEBUG)  :   
        log_debug_dfc(rowid,"get_geopy_geocoder_results : " + geoparm + " : " + str(geocid) + " : " + str(geotype) )
    
    if(geotype == sugm.QUERY) :
        
        if(geocid == sugm.BingId) :
            
            exactly_one_parm            =   True
            user_location_parm          =   None
            timeout_parm                =   sugm.BING_TIMEOUT
            culture_parm                =   None
            include_neighborhood_parm   =   None
            include_country_code_parm   =   False

            location    =   geolocator.geocode(geoparm,
                                               exactly_one_parm,
                                               user_location_parm,
                                               timeout_parm,
                                               culture_parm,
                                               include_neighborhood_parm,
                                               include_country_code_parm)
        
        if(geocid == sugm.BaiduId) :
            
            exactly_one_parm            =   True
            timeout_parm                =   sugm.BING_TIMEOUT

            location    =   geolocator.geocode(geoparm,
                                               exactly_one_parm,
                                               timeout_parm)
            
        return(location)
            
    else :

        if(geocid == sugm.BingId) :
            
            if(sugm.GEOCODE_THREAD_DEBUG)  :   
                log_debug_dfc(rowid,"get_geopy_geocoder_results : bing reverse")

            address                     =   None
            
            lat_lng                     =   geoparm.replace("[","")
            lat_lng                     =   lat_lng.replace("]","")
            lat_lng                     =   lat_lng.split(",")
            
            lat                         =   float(lat_lng[0])
            lng                         =   float(lat_lng[1])
            
            geo_lat_lng                 =   [lat,lng]
            
            exactly_one_parm            =   True
            timeout_parm                =   sugm.BING_TIMEOUT
            culture_parm                =   None
            include_country_code_parm   =   False
    
            address     =   geolocator.reverse(geo_lat_lng,
                                               exactly_one_parm,
                                               timeout_parm,
                                               culture_parm,
                                               include_country_code_parm)
            
        if(geocid == sugm.BaiduId) :
            
            if(sugm.GEOCODE_THREAD_DEBUG)  :   
                log_debug_dfc(rowid,"get_geopy_geocoder_results : bing reverse")

            address                     =   None
            
            lat_lng                     =   geoparm.replace("[","")
            lat_lng                     =   lat_lng.replace("]","")
            lat_lng                     =   lat_lng.split(",")
            
            lat                         =   float(lat_lng[0])
            lng                         =   float(lat_lng[1])
            
            geo_lat_lng                 =   [lat,lng]
            
            exactly_one_parm            =   True
            timeout_parm                =   sugm.BING_TIMEOUT
    
            address     =   geolocator.reverse(geo_lat_lng,
                                               exactly_one_parm,
                                               timeout_parm)
            
        return(address)


def get_geopy_geocode_results(geocid,geotype,rowid,address,queryParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a single goeocode result
    * 
    * parms :
    *  eowid            - dataframe row id
    *  address          - address to geocode
    *  geocodeParms     - google geocode parms
    *
    * returns : 
    *    bing geocode results
    * --------------------------------------------------------
    """
    
    current_geocode_results =   None

    geolocator = sugc.get_geocoder_engine(geocid,opstat)
    
    if(not(opstat.get_status())) :
        opstat.set_errorMsg(sugm.GeopyGeocoderConnectionErrorMessage)

    if(opstat.get_status()) :   

        try :
            location    =   get_geopy_geocoder_results(geocid,geotype,geolocator,rowid,address,queryParms)            
            
        except geopy.exc.GeopyError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyErrorMessage)
        except geopy.exc.ConfigurationError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyConfigurationErrorMessage)
        except geopy.exc.GeocoderServiceError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderServiceErrorMessage)
        except geopy.exc.GeocoderQueryError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderQueryErrorMessage)
        except geopy.exc.GeocoderQuotaExceeded :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderQuotaExceededMessage)
        except geopy.exc.GeocoderAuthenticationFailure :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderAuthenticationFailureMessage)
        except geopy.exc.GeocoderInsufficientPrivileges :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderInsufficientPrivilegesMessage)
        except geopy.exc.GeocoderTimedOut :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderTimedOutMessage)
        except geopy.exc.GeocoderUnavailable :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderUnavailableMessage)
        except geopy.exc.GeocoderParseError :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderParseErrorMessage)
        except geopy.exc.GeocoderNotFound :
            opstat.set_status(False)
            opstat.set_errorMsg(sugm.GeopyGeocoderNotFoundMessage)
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("get_geopy_geocode_results : Other Exception : "+ " " + str(sys.exc_info()[0].__name__))

        if(opstat.get_status()) :  
            
            if(geotype == sugm.QUERY) :
            
                if( not (location == None)) :
                    full_address    =   location.address
                    latitude        =   location.latitude
                    longitude       =   location.longitude
                    
                    if(sugm.GEOCODE_THREAD_DEBUG)  :   
                        log_debug_dfc(-1,"get_geopy_geocode_results for : " + address)
                        log_debug_dfc(-1,str(full_address) + " : " + str(latitude) + " : " + str(longitude))

            
                    try :
                        current_geocode_results    =  sugm.geopy_geocode_results(rowid,full_address,latitude,longitude,opstat)
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Error getting geopy geocoder " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))
                    
            else :
            
                if( not (location == None)) :
                    full_address    =   location.address
                    latitude        =   location.latitude
                    longitude       =   location.longitude
            
                    try :
                        current_geocode_results    =  sugm.geopy_geocode_results(rowid,full_address,latitude,longitude,opstat)
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Error getting geopy reverse " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))
                
        else :
            current_geocode_results    =  None            
        
    return(current_geocode_results)


def process_geopy_geocode_results(geocid,geotype,inputParms,runParms,geopy_results,opstat,error_rowid=None) :
    """
    * --------------------------------------------------------
    * function : process google geocode results 
    * 
    * parms :
    *  inputParms       - input parms
    *  runParms         - run time parms
    *  geocode_results  - geocode results
    *
    * returns : 
    *    NA stored in results df
    * --------------------------------------------------------
    """

    results_df          =   get_geocode_runner_results_log()
    
    if(error_rowid is None) :
        
        try :
        
            if(not (geopy_results is None)) :

                if(geotype == sugm.QUERY) :
            
                    lat_long_colname    =   runParms.get(subgw.bulk_google_query_input_labelList[2])
                    lat_long_merged     =   False
            
                    if(geocid == sugm.BingId) :
                        lat_long_colname   =   runParms.get(subgw.bulk_bing_query_input_labelList[2])
                        full_addr_col_name  =   runParms.get(subgw.bulk_bing_query_input_labelList[3]) 
                
                    elif(geocid == sugm.BaiduId) :
                        lat_long_colname   =   runParms.get(subgw.bulk_bing_query_input_labelList[2])
                        full_addr_col_name  =   runParms.get(subgw.bulk_bing_query_input_labelList[3])                
            
                    if(lat_long_colname.find("]") > -1) :
                        lat_long_merged     =   True
    
                    save_full_address   =   True
                    if(full_addr_col_name == "None") :
                        save_full_address   =   False
        
                    if(save_full_address) :
                        if(not (lat_long_merged)) :
                            results_df.add_result([geopy_results.get_row_Id(),
                                                   inputParms, 
                                                   geopy_results.get_lat(), 
                                                   geopy_results.get_lng(), 
                                                   geopy_results.get_full_address()],opstat)
                        else :
                            results_df.add_result([geopy_results.get_row_Id(),
                                                   inputParms, 
                                                   [geopy_results.get_lat(),geopy_results.get_lng()], 
                                                   geopy_results.get_full_address()],opstat)
                            
                    else :
                        if(not (lat_long_merged)) :
                            results_df.add_result([geopy_results.get_row_Id(),
                                                   inputParms, 
                                                   geopy_results.get_lat(),
                                                   geopy_results.get_lng()],opstat)
                        else :
                            results_df.add_result([geopy_results.get_row_Id(),
                                                   inputParms, 
                                                   [geopy_results.get_lat(),geopy_results.get_lng()]],opstat)

                else : # geopy reverse

                    results_df.add_result([geopy_results.get_row_Id(),
                                           inputParms, 
                                           geopy_results.get_full_address()],opstat)
      
            else :
        
                process_bulk_geocoding_errors(geocid,geotype,geopy_results.get_row_Id(),inputParms)
                results_df.add_nan_result(geopy_results.get_row_Id(),inputParms,None,opstat)

        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("Error getting geopy " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))            
    
    else : # error row
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"add_nan_result for None")        

        results_df.add_nan_result(error_rowid,inputParms,None,opstat)


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#   Common geoociding components
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def process_geocode_final_results(cmd,inparms) :
    """
    * --------------------------------------------------------
    * function : process google reverse results 
    * 
    * parms :
    *  inparms      - input parms
    *  cmd          - command
    *  opstat       - op status var
    *
    * returns : 
    *    NA stored in results df
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    try :
    
        results_df  =   get_geocode_runner_results_log().get_geocoding_results_df()
        errors_df   =   get_geocode_runner_error_log().get_error_log_df()
        
        if(cmd == sugm.PROCESS_BULK_RESULTS_APPEND_PROCESS) :
        
            proc_parms                  =   get_parms_for_input(inparms[1],subgc.bulk_geocode_append_input_idList)
        
            if(len(proc_parms) > 0) :
            
                append_to_csv_file_name     =   proc_parms[0]
                cfg.set_config_value(subgc.bulk_geocode_append_input_id+"Parms",[append_to_csv_file_name])
        
                import pandas as pd
                try :
            
                    append_to_csv_df        =   pd.read_csv(append_to_csv_file_name) 
            
                except Exception as e:
                    opstat.store_exception("Unable to open csv file to append to ",e)
            
                if(opstat.get_status()) :
            
                    try :
            
                        append_to_csv_df        =   append_to_csv_df.append(results_df,sort=False)
                        append_to_csv_df.to_csv(append_to_csv_file_name,index=False)
            
                    except Exception as e:
                        opstat.store_exception("Unable to open csv file to append to ",e)
                    
            else :
               opstat.set_errorMsg("Invalid csv file to append to")
               opstat.set_status(False)
            
            if(opstat.get_status()) :
            
                print("\n")
                display_status("Geocode Results appended successfully to csv file " + append_to_csv_file_name)
            
                cfg.set_config_value(cfg.BULK_GEOCODE_APPENDED_CSV_ID,append_to_csv_file_name,True)
            
                subgc.display_bulkgeocode_openexcel_taskbar(0) 
                print("\n")
                subgc.display_base_taskbar()
                print("\n")
            
            else :
                display_exception(opstat)
                print("\n")
                subgc.display_base_taskbar()
                    

        elif(cmd == sugm.PROCESS_BULK_RESULTS_CSV_PROCESS) :
        
            #nb_name =   get_notebookName() 
            nbpath  =   cfg.get_notebookPath()
        
            import os
        
            df_export_path = os.path.join(nbpath,"exports")
            if (not (does_dir_exist(df_export_path)) ) :
                make_dir(df_export_path)

            proc_parms  =   get_parms_for_input(inparms[1],subgc.bulk_geocode_export_input_idList)
        
            if(len(proc_parms) >0) :
            
                if(len(proc_parms) > 0) :
                    csv_file_name   =   os.path.join(df_export_path, proc_parms[0])
                else :
                    csv_file_name   =   None
        
                if(not (csv_file_name is None)) :
                    #write out csv file 
                    try :
                        if(not (csv_file_name is None)) :
                            results_df.to_csv(csv_file_name,index=False)
                    except Exception as e:
                        opstat.store_exception("Unable to export geocoding results file ",e)
        
            else :
                opstat.set_errorMsg("Invalid csv file to export to")
                opstat.set_status(False)
        
            if(opstat.get_status()) :
            
                print("\n")
                display_status("Geocode Results exported successfully to csv file " + csv_file_name)
            
                cfg.set_config_value(cfg.BULK_GEOCODE_EXPORTED_CSV_ID,csv_file_name,True)
            
                subgc.display_bulkgeocode_openexcel_taskbar(1) 
                print("\n")
                subgc.display_base_taskbar()
                print("\n")
            
            else :
                display_exception(opstat)
                print("\n")
                subgc.display_base_taskbar()
                
        elif(cmd == sugm.PROCESS_BULK_ERRORS_CSV_PROCESS) :
        
            #nb_name =   get_notebookName() 
            #nbpath  =   cfg.get_notebookPath()
        
            import os
        
            proc_parms  =   get_parms_for_input(inparms[1],subgc.bulk_geocode_export_error_input_idList)
            
            if(len(proc_parms) >0) :
            
                if(len(proc_parms) > 0) :
                    csv_file_name   =   proc_parms[0]
                else :
                    csv_file_name   =   None
        
                if(not (csv_file_name is None)) :
                    #write out csv file 
                    try :
                        if(not (csv_file_name is None)) :
                            errors_df.to_csv(csv_file_name,index=False)
                    except Exception as e:
                        opstat.store_exception("Unable to export geocoding errors file ",e)
                        
                else :
                    opstat.set_errorMsg("No file path define")
                    opstat.set_status(False)
        
            else :
                opstat.set_errorMsg("Invalid csv file to export to")
                opstat.set_status(False)
        
            if(opstat.get_status()) :
            
                print("\n")
                display_status("Geocode Errors exported successfully to csv file " + csv_file_name)
            
                cfg.set_config_value(cfg.BULK_ERRORS_EXPORTED_CSV_ID ,csv_file_name,True)
            
                subgc.display_bulkgeocode_openexcel_taskbar(2) 
                print("\n")
                
                subgc.display_geopy_exceptions_taskbar() 
                print("\n")
                
                subgc.display_base_taskbar()
                print("\n")
            
            else :
                display_exception(opstat)
                print("\n")
                subgc.display_base_taskbar()
 

    except Exception as e:
        opstat.store_exception("Unable to export geocoding results file ",e)
        
        subgc.display_base_taskbar()
        print("\n")
        display_exception(opstat)












"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Task Class
#----------------------------------------------------------------------------
#   geocoding task class for retrieving gecoding results
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

class GeocodeThread :
    
    geocoderId          =   -1
    geocodeType         =   sugm.QUERY
    rowId               =   -1
    inputparms          =   None
    runParms            =   None
    
    geocode_results     =   None
    task_running        =   False
    
    thread_start_time   =   None
    
    opstat              =   None
        
    def __init__(self, geocoderId,geocodeType,rowid,inputparms,runparms):
        
        self.geocoderId         =   geocoderId
        self.geocoder_type      =   geocodeType
        self.rowId              =   rowid
        self.inputParms         =   inputparms
        self.runParms           =   runparms
        self.geocode_results    =   None
        self.task_running       =   False
        
        self.opstat             =   opStatus()
        
        if(geocoderId == sugm.ArcGISId) :
            import datetime;
            self.thread_start_time = datetime.datetime.now().timestamp()
        
    def run_geocoder_thread(self) :
        
        try :
            self.task_running       =   True
            self.run_geocode_method(self.opstat)  
        except :
            process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,"run_geocoder_thread Task Excepption : " + self.opstat.get_errorMsg())
            
        self.task_running       =   False

        import time
        time.sleep(0.02)
        
            
    def run_geocode_method(self,opstat) :
        
        retry_count     =   0
        
        if(self.geocoderId == sugm.ArcGISId) :
            
            if(sugm.GEOCODE_DEBUG)  :
                log_debug_dfc(-1,"ArcGIS run_geocode_method " + str(len(self.inputParms)))

            geocoder = None
            geocode_results     =   get_arcgis_geocode_batch(geocoder,self.inputParms,self.runParms,self.opstat)

            if(opstat.get_status()) :
                    
                # batch retrieved ok
                process_arcgis_geocode_batch_results(geocode_results,self.inputParms,self.runParms,opstat)
                    
                if(self.get_results_log_count() >= (self.maxrows-1)) :
                    self.set_halt_flag(True)   
                    if(sugm.GEOCODE_DEBUG)  :   
                        log_debug_dfc(self.rowIndex,"halt arcgis"+str(self.maxrows-1))

        elif(self.geocoderId == sugm.GoogleId) :
            
            while(retry_count < sugm.GOOGLE_RETRY_LIMIT) :
                
                if(self.geocoder_type == sugm.QUERY) :
                    self.geocode_results    =   get_google_geocode_results(self.rowId,self.inputParms,self.runParms,opstat)
                elif(self.geocoder_type == sugm.REVERSE) :
                    self.geocode_results    =   get_google_reverse_results(self.rowId,self.inputParms,self.runParms,opstat) 

                if(not (self.geocode_results is None) ) :
                    # no error occurred
                    if(opstat.get_status()) :
                        if(self.geocoder_type == sugm.QUERY) :
                            process_google_geocode_results(self.inputParms,self.runParms,self.geocode_results,opstat)
                        else :
                            process_google_reverse_results(self.inputParms,self.runParms,self.geocode_results,opstat)
                            
                        retry_count     =   sugm.GOOGLE_RETRY_LIMIT
            
                    else :
                        if( (opstat.get_error_message() == sugm.OverQueryLimitErrorMessage) or 
                            (opstat.get_error_message() == sugm.GoogleGeocoderConnectionErrorMessage) ): 
                        
                            stop_geocode_runner(opstat.get_error_message())
                            retry_count     =   sugm.GOOGLE_RETRY_LIMIT
                        
                        elif(opstat.get_error_message() == sugm.TimeoutErrorMessage) :     
                            retry_count     =   retry_count + 1
                        
                        elif(opstat.get_error_message() == sugm.RetriableRequestErrorMessage) :     
                            retry_count     =   retry_count + 1
                            
                        if(retry_count == sugm.GOOGLE_RETRY_LIMIT) :   
                            process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,opstat.get_error_message())
                    
                else :
                    process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,"No results returned") 
                
                    if(self.geocoder_type == sugm.QUERY) :
                        process_google_geocode_results(self.inputParms,self.runParms,None,opstat,opstat,self.rowId)
                    else :
                        process_google_reverse_results(self.inputParms,self.runParms,None,self.rowId)
                    
                    retry_count     =   sugm.GOOGLE_RETRY_LIMIT
                    
        elif( (self.geocoderId == sugm.BingId) or 
              (self.geocoderId == sugm.BaiduId) ):
            
            if(self.geocoderId == sugm.BingId)      :   retry_limit    =   sugm.BING_RETRY_LIMIT
            elif(self.geocoderId == sugm.BaiduId)   :   retry_limit    =   sugm.BAIDU_RETRY_LIMIT
            else                                    :   retry_limit    =   0

            while(retry_count < retry_limit) :

                self.geocode_results    =   get_geopy_geocode_results(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,self.runParms,opstat)

                if(opstat.get_status()) :
                
                    if(self.geocode_results is None) :
                        process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,opstat.get_error_message())
                    else :
                        process_geopy_geocode_results(self.geocoderId,self.geocoder_type,self.inputParms,self.runParms,self.geocode_results,opstat)
                        
                    retry_count     =   retry_limit
            
                else :
                
                    if( (opstat.get_errorMsg() == sugm.GeopyGeocoderConnectionErrorMessage) or
                        (opstat.get_error_message() == sugm.GeopyGeocoderQuotaExceededMessage) or 
                        (opstat.get_error_message() == sugm.GeopyErrorMessage) or 
                        (opstat.get_error_message() == sugm.GeopyConfigurationError) or 
                        (opstat.get_error_message() == sugm.GeopyGeocoderServiceErrorMessage) ) : 
    
                        stop_geocode_runner(opstat.get_error_message())
                        retry_count     =   sugm.retry_limit
                    
                    elif(opstat.get_errorMsg() == sugm.GeopyGeocoderGeocoderTimedOutMessage) :
                        retry_count     =   retry_count + 1  
                        
                    else :
                        stop_geocode_runner(opstat.get_error_message())
                        retry_count     =   sugm.retry_limit
                
                    if(retry_count == sugm.retry_limit) :
                        process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,opstat.get_error_message())
                        process_geopy_geocode_results(self.geocoderId,self.geocoder_type,self.inputParms,self.runParms,self.geocode_results,opstat,self.rowId)
 
               
    def get_thread_run_state(self) :
        return(self.task_running)    
    
    def get_thread_row_id(self) :
        return(self.rowId)    

    def get_thread_start_time(self) :
        return(self.thread_start_time)    


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Thread Monitor Class
#----------------------------------------------------------------------------
#   geocoding thread monitoring class for controlling geocode threads
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""        
import threading
        
class GeocodeThreadsMonitor:
    
    threaddict      =   {}
    maxthreads      =   0
        
    def __init__(self, maxthreadsparm):
        self.threaddict      =   {}
        self.maxthreads      =   maxthreadsparm
    
    def addthread(self, geocodetask, rowindex):
        if(sugm.GEOCODE_THREAD_DEBUG)  :   
            log_debug_dfc(-1,"addthread ["+ str(len(self.threaddict))+"]")
        self.threaddict.update({rowindex:geocodetask})
        threading.Thread(target=geocodetask.run_geocoder_thread).start()
        
    def dropthread(self, rowindex):

        if(not(self.threaddict.get(rowindex,None) is None)) :
            self.threaddict.pop(rowindex,None)
            if(sugm.GEOCODE_THREAD_DEBUG)  :   
                log_debug_dfc(rowindex,"dropthread : thread popped : num active threads [" + str(len(self.threaddict))+"]")
        else :
            if(sugm.GEOCODE_THREAD_DEBUG)  :   
                log_debug_dfc(rowindex,"dropthread : thread not found")

    def more_threads_available(self):

        if(len(self.threaddict) < self.maxthreads) :
            return(True)
        else :
            return(False)

    def clear_completed_threads(self) :
        task_keys   =   list(self.threaddict.keys())
        
        for i in range(len(task_keys)) :
            ctask   =   self.threaddict.get(task_keys[i])

            if( not(ctask.get_thread_run_state()) ) :
                self.dropthread(ctask.get_thread_row_id())

    def all_threads_completed(self) :
        if(len(self.threaddict) == 0) :
            return(True)
        else :
            return(False)


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Runner Class
#----------------------------------------------------------------------------
#   class for running the current geocoding instance from dfcleanser.
#   controls threads and updates display
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#   common helper methopds
#--------------------------------------------------------------------------
"""
def load_geocode_runner(geocoderId,geotype,runParms,address_map) :
    dfc_Geocode_Runner.load_run(geocoderId,geotype,runParms,address_map)    
def start_geocode_runner() :
    return(dfc_Geocode_Runner.start_run()) 
def stop_geocode_runner(error_msg=None) :
    dfc_Geocode_Runner.stop_run(error_msg) 
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 
def checkpoint_geocode_runner() :
    dfc_Geocode_Runner.checkpoint_run() 

def get_geocode_runner_results_log() :
    return(dfc_Geocode_Runner.get_results_log())
def get_geocode_runner_results_count() :
    return(dfc_Geocode_Runner.get_results_log_count())
def get_geocode_runner_error_log() :
    return(dfc_Geocode_Runner.get_error_log())

def get_geocode_runner_state() :
    return(dfc_Geocode_Runner.get_run_state())
def set_geocode_runner_state(state) :
    dfc_Geocode_Runner.set_run_state(state)
    
def get_geocode_runner_halt_flag() :
    return(dfc_Geocode_Runner.get_halt_flag())
def set_geocode_runner_halt_flag(state) :
    dfc_Geocode_Runner.set_halt_flag(state)

def get_geocode_runner_id() :
    return(dfc_Geocode_Runner.get_geocode_id())
def get_geocode_runner_type() :
    return(dfc_Geocode_Runner.get_geocode_type())
def get_geocode_runParms() :
    return(dfc_Geocode_Runner.get_runParms())
def get_geocode_connector() :
    return(dfc_Geocode_Runner.get_geocode_connector())
def set_geocode_connector(connector) :
    return(dfc_Geocode_Runner.set_geocode_connector(connector))
def get_geocode_maxrows() :
    return(dfc_Geocode_Runner.get_geocode_maxrows())
def get_geocode_checkpoint_interval() :
    return(dfc_Geocode_Runner.get_geocode_checkpoint_interval())

def get_geocode_run_total_time() :
    return(dfc_Geocode_Runner.get_total_run_time())

def get_geocode_lat_long_map() :
    return(dfc_Geocode_Runner.get_geocode_lat_long_map())

"""
#----------------------------------------------------------------------------
#-  Bulk Geocoding Runner Class
#----------------------------------------------------------------------------
"""

import datetime

class BulkGeocodeRunner:
    
    geocid                  =   None
    geotype                 =   None
    runParms                =   None
    addressParms            =   None
    
    rowindex                =   0
    maxrows                 =   0

    state                   =   sugm.STOPPED
    halt_all_geocoding      =   True
    geocoding_in_error      =   False
    
    geocoder                =   None
    
    geocodeThreadsMonitor   =   None
    geocodingResults        =   None
    geocodingErrorLog       =   None
    
    ResultsLength           =   0
    ErrorsLength            =   0
    
    start_time              =   0
    stop_time               =   0
    
    stop_error_msg          =   None
    
    checkpoint_on           =   False
    checkpoint_interval     =   10000
    last_checkpoint_rowid   =   0
    
    lat_long_map            =   []
       
    def __init__(self):
        
        self.geocid                 =   None
        self.geotype                =   None
        self.runParms               =   None
        self.addressParms           =   None

        self.rowindex               =   0
        self.maxrows                =   0

        self.state                  =   sugm.STOPPED
        self.halt_all_geocoding     =   True
        self.geocoding_in_error     =   False
        
        self.geocoder               =   None
        
        self.geocodeThreadsMonitor  =   None
        self.geocodingResults       =   None
        self.geocodingErrorLog      =   None
        
        self.ResultsLength          =   0
        self.ErrorsLength           =   0
        
        self.start_time             =   0
        self.stop_time              =   0
        self.stop_error_msg         =   None
        
        self.checkpoint_on          =   False
        self.checkpoint_interval    =   10000 
        self.last_checkpoint_rowid  =   0

        self.lat_long_map           =   []
        
        
    def load_run(self,geocoderId,geoType,runParms,addressParms):
        
        if(sugm.GEOCODE_DEBUG)  :  
            log_debug_dfc(-1,"load_run  : geocid : " + str(geocoderId) + " geotype : " + str(geoType)) 
            log_debug_dfc(-1,"load_run  : runParms : " + str(runParms))
            log_debug_dfc(-1,"load_run  : addressParms : " + str(type(addressParms)))
                    
        self.geocid             =   geocoderId
        self.geotype            =   geoType
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        
        if(self.geotype == sugm.REVERSE) :
            self.lat_long_map   =   sugm.get_lat_longs_map(self.geocid,self.runParms)
        
        if(self.geocid == sugm.GoogleId) :
            if(self.geotype == sugm.QUERY) :
                self.maxrows                =   int(runParms.get("max_addresses_to_geocode"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
            else :
                self.maxrows                =   int(runParms.get("max_lat_longs"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
                
        elif(self.geocid == sugm.BingId) :
            if(self.geotype == sugm.QUERY) :
                self.maxrows                =   int(runParms.get("max_addresses_to_geocode"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))

            else :
                self.maxrows                =   int(runParms.get("max_lat_longs"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
        
        elif(self.geocid == sugm.BaiduId) :
            if(self.geotype == sugm.QUERY) :
                self.maxrows                =   int(runParms.get("max_addresses_to_geocode"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
            else :
                self.maxrows                =   int(runParms.get("max_lat_longs"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
                
        elif(self.geocid == sugm.ArcGISId) :
            self.maxrows            =   int(runParms.get("max_addresses_to_geocode"))
        
        if(self.geocid == sugm.GoogleId):
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(sugm.GOOGLE_THREAD_LIMIT)
        elif(self.geocid == sugm.BingId):
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(sugm.BING_THREAD_LIMIT)
        elif(self.geocid == sugm.BaiduId):
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(sugm.BAIDU_THREAD_LIMIT)
        
        from dfcleanser.sw_utilities.sw_utility_geocode_model import init_geocoding_data_structures
        bulkstructures          =   init_geocoding_data_structures(self.geocid,self.geotype,self.runParms)
        self.geocodingResults   =   bulkstructures[0]
        self.geocodingErrorLog  =   bulkstructures[1]
        
        if(sugm.GEOCODE_DEBUG)  :  
            log_debug_dfc(-1,"load_run  : checkpoint_interval : " + str(self.checkpoint_interval)) 
        
        subgc.control_bulk_keys([subgc.ENABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE])
        
        
        
    def start_run(self):
        subgc.set_status_bar(sugm.STARTING)
        self.set_run_state(sugm.STARTING)

        self.set_halt_flag(False)
        self.rowindex           =   0
        
        self.start_time         =   datetime.datetime.now()
        self.stop_time          =   datetime.datetime.now()
        
        return(self.start_bulk_geocode_runner(0))
        
    def stop_run(self,error_msg=None) :
        
        if(self.get_run_state() == sugm.PAUSED) :
            subgc.set_status_bar(sugm.STOPPED)
            self.set_run_state(sugm.STOPPED)
            
        else :    
            subgc.set_status_bar(sugm.STOPPING)
            self.set_run_state(sugm.STOPPING)
            
        self.set_halt_flag(True)
        self.stop_time          =   datetime.datetime.now()
        
        if(sugm.GEOCODE_DEBUG)  :   
            if(self.stop_error_msg == None) :
                log_debug_dfc(self.rowIndex,"stop_run")
            else :
                log_debug_dfc(self.rowIndex,"stop_run : " + self.stop_error_msg)
        
    def pause_run(self) :
        subgc.set_status_bar(sugm.PAUSING)
        self.set_run_state(sugm.PAUSING)
        self.set_halt_flag(True)
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(self.rowIndex,"pause_run : halt PAUSE")

    def resume_run(self):
        subgc.set_status_bar(sugm.RUNNING)
        self.set_run_state(sugm.RUNNING)
        self.set_halt_flag(False)
        self.rowindex           =   self.geocodingResults.get_results_count()
        self.start_bulk_geocode_runner(self.rowindex)        
        
    def checkpoint_run(self) :
        self.checkpoint_on  =   True
        self.pause_run()
        
    def get_run_state(self):
        return(self.state)
    
    def set_run_state(self,runstate):
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"set_run_state : " + str(runstate))
        
        self.state  =   runstate
    
    def start_bulk_geocode_runner(self,rowIndex) :
        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(rowIndex,"start_bulk_geocode_runner : " + "geocid : " + str(self.geocid) + " geotype " + str(self.geotype) + " maxrows " + str(self.maxrows) + " rowindex " + str(rowIndex))

        self.rowindex   =   rowIndex
        opstat          =   opStatus()
        
        try :
            if(self.geocid == sugm.ArcGISId) :
                geocoderparms   =   cfg.get_config_value(subgw.batch_arcgis_geocoder_id+"Parms")
                self.geocoder   =   get_arcgis_batch_geocode_connection(geocoderparms[1],geocoderparms[2],opstat)
            
            elif(self.geocid == sugm.GoogleId) :   
                geocoderparms   =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
                self.geocoder   =   get_bulk_google_geocoder_connection(geocoderparms[0],geocoderparms[1],geocoderparms[2],opstat)
            else :  
                self.geocoder   =   sugc.get_geocoder_engine(self.geocid,opstat)
                
        except Exception as e:
            opstat.store_exception("Unable to establish " + sugm.get_geocoder_title(self.geocid) + " geocoder connection ",e)
        
        if(opstat.get_status()) :
        
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"start_bulk_geocode_runner got connection")
            
            self.set_halt_flag(False)
            threading.Thread(target=self.bulk_geocode_runner_task).start()
            subgc.set_status_bar(sugm.RUNNING)
            
            subgc.control_bulk_keys([subgc.DISABLE,subgc.ENABLE,subgc.ENABLE,subgc.DISABLE,subgc.ENABLE,subgc.DISABLE])
            
            return(opstat)
            
        else :
            return(opstat)
        
    def bulk_geocode_runner_task(self) :
        
        opstat                  =   opStatus()
        arcgis_geocodethread    =   None   
        
        while ( (not (self.is_geocode_run_complete()))  ) :
            
            if(not (self.geocid == sugm.ArcGISId) ) :
                self.geocodeThreadsMonitor.clear_completed_threads()
                
            if(self.is_checkpoint_needed())  :
                
                if(self.geocid == sugm.GoogleId) :
                    delay   =   sugm.GOOGLE_DELAY
                elif(self.geocid == sugm.BingId) :
                    delay   =   sugm.BING_DELAY
                elif(self.geocid == sugm.BaiduId) :
                    delay   =   sugm.BAIDU_DELAY
                        
                import time
                time.sleep(delay)
                
                if(self.geocodeThreadsMonitor.all_threads_completed()) :
                    self.checkpoint_results(opstat)
                    
                    if(opstat.get_status()) :
                        subgc.set_status_bar(sugm.RUNNING)
                        subgc.control_bulk_keys([subgc.DISABLE,subgc.ENABLE,subgc.ENABLE,subgc.DISABLE,subgc.ENABLE,subgc.DISABLE])
                    else :
                        self.geocodingErrorLog.log_error(self.last_checkpoint_rowid,"NA",opstat.get_errorMsg(),"",opstat)
                        self.pause_run()                        
                
            else :
            
                if( not (self.get_halt_flag()) ) :
            
                    if(self.geocid == sugm.ArcGISId) :
                        if(sugm.GEOCODE_DEBUG)  :   
                            log_debug_dfc(-1,"bulk_geocode_runner_task start : arcgis ")
                        
                        if(arcgis_geocodethread is None) :
                            next_batch_addrs        =   get_arcgis_batch_addresses(self.runParms,self.addressParms,opstat)
                            
                            if(opstat.get_status()) :
                                arcgis_geocodethread    =   GeocodeThread(self.geocid,self.geotype,self.rowindex,next_batch_addrs,self.runParms)
                                arcgis_geocodethread.run_geocoder_thread()
                        
                            else :
                                self.geocoding_in_error     =   True
                                self.set_halt_flag(True) 
                                if(sugm.GEOCODE_DEBUG)  :   
                                    log_debug_dfc(self.rowIndex,"bulk_geocode_runner_task : halt arcgis : " + opstat.get_errorMsg())
                                
                        else :
                        
                            if(arcgis_geocodethread.get_thread_run_state()) :
                                import datetime
                                current_date_time = datetime.datetime.now().timestamp()

                                time_diff       =   current_date_time - arcgis_geocodethread.get_thread_start_time()
                                import numpy as np
                                diff_seconds    =   time_diff/np.timedelta64(1,'s')
                                
                                if(diff_seconds > sugm.ARCGIS_TIMEOUT) :
                                
                                    self.geocoding_in_error     =   True  
                                    self.set_halt_flag(True)    
                                    if(sugm.GEOCODE_DEBUG)  :   
                                        log_debug_dfc(-1,"bulk_geocode_runner_task halt : stop arcgis : " + opstat.get_errorMsg())
                                
                            else :
                                arcgis_geocodethread    =   None                            
                
                    elif( (self.geocid == sugm.GoogleId) or 
                          (self.geocid == sugm.BingId) or 
                          (self.geocid == sugm.BaiduId) ):
                    
                        if(self.geocodeThreadsMonitor.more_threads_available()) :
                        
                            if(self.rowindex < self.maxrows) :
                            
                                if(self.geotype == sugm.QUERY) :
                                
                                    next_addr       =   sugm.get_geocode_address_string(self.geocid,self.runParms,self.addressParms,self.rowindex)
                                
                                    if(sugm.GEOCODE_THREAD_DEBUG)  :
                                        log_debug_dfc(-1,"next_addr to geocode : " + str(next_addr) + " : " + str(self.geocid))
                                    
                                    geocodethread   =   GeocodeThread(self.geocid,self.geotype,self.rowindex,next_addr,self.runParms)  
                                    self.geocodeThreadsMonitor.addthread(geocodethread,self.rowindex)
                                else :
                                    try :
                                        next_lat_lng    =   sugm.get_geocode_reverse_lat_lng_string(self.geocid,self.runParms,self.rowindex)
                                        geocodethread   =   GeocodeThread(self.geocid,self.geotype,self.rowindex,next_lat_lng,self.runParms)  
                                        self.geocodeThreadsMonitor.addthread(geocodethread,self.rowindex)
                                    except  :
                                        import sys
                                        #str(sys.exc_info()[0].__name__)
                                        if(sugm.GEOCODE_DEBUG)  :   
                                            log_debug_dfc(-1,"add reverse thread exception " + str(sys.exc_info()[0].__name__))
                                    
                                self.rowindex   =   self.rowindex + 1
                    
                            else :
                                if(sugm.GEOCODE_DEBUG)  : 
                                    log_debug_dfc(-1,"bulk_geocode_runner_task halt no threads available")
                                self.set_halt_flag(True)
                            
                        else :
                    
                            if(self.geocid == sugm.GoogleId) :
                                delay   =   sugm.GOOGLE_DELAY
                            elif(self.geocid == sugm.BingId) :
                                delay   =   sugm.BING_DELAY
                            elif(self.geocid == sugm.BaiduId) :
                                delay   =   sugm.BAIDU_DELAY
                        
                            import time
                            time.sleep(delay)
                        
                        self.update_status_bar()
                    
                        if( self.rowindex >= self.maxrows ) :
                            self.set_halt_flag(True)
                            if(sugm.GEOCODE_DEBUG)  :   
                                log_debug_dfc(self.rowindex,"bulk_geocode_runner_task halt max rows : halt - google " + str(self.rowindex) + " " + str(self.maxrows))

     
                    else :
                        print("geocoder not supported")
                        set_geocode_runner_halt_flag(True)    
                        self.geocoding_in_error     =   True

                    self.update_status_bar() 
                    self.update_state()

                else :
                
                    self.update_status_bar() 
                    self.update_state()
                
                    import time
                    time.sleep(0.2)


        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"geocode run task complete : rowid " + str(self.rowindex) + " : " + str(self.is_geocode_run_complete())) 
        
        if(self.is_geocode_run_complete()) :
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"geocode run is complete : self.geocoding_in_error " + str(self.geocoding_in_error)) 
                
            self.update_status_bar() 
            self.update_state()            
            
            self.geocodingResults.finish_results_log(opstat)
            
            self.geocodingErrorLog.finish_error_log(opstat)

            import datetime
            self.stop_time         =   datetime.datetime.now()
            
            if(self.geocoding_in_error) :
                subgc.set_status_bar(sugm.STOPPED) 
            else :   
                subgc.set_status_bar(sugm.FINISHED)
                set_geocode_runner_state(sugm.FINISHED)
                
                subgc.control_bulk_keys([subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.ENABLE])

        
    def is_geocode_run_complete(self) :
        
        if(sugm.GEOCODE_DETAIL_DEBUG)  :   
            log_debug_dfc(-1,"is_geocode_run_complete : state "+ str(self.state) + " thread completed :  " + str(self.geocodeThreadsMonitor.all_threads_completed()) + " results : " + str(self.geocodingResults.get_results_count()) + " errors : " + str(self.geocodingErrorLog.get_error_count()))
        
        if(self.geocodeThreadsMonitor.all_threads_completed()) :
            if((self.geocodingErrorLog.get_error_count() + self.geocodingResults.get_results_count()) >= self.maxrows) :
                return(True)
                
        return(False)

    def update_status_bar(self) :
        
        if(not (self.ResultsLength == self.geocodingResults.get_results_count())) :

            current_count       =   self.geocodingResults.get_results_count()
            current_percent     =   int( ( current_count / self.maxrows ) * 100 )
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"update_status_bar current_percent " + str(current_percent)) 

            subgc.set_progress_bar_value(self.geocid,self.geotype,sugm.GEOCODE_BAR,current_count,current_percent)
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"update_status_bar current_percent after " + str(current_percent)) 
            
            self.ResultsLength  =   self.geocodingResults.get_results_count()

    def update_state(self) :
        
        opstat  =   opStatus()
        
        if(self.geocid == sugm.ArcGISId) :
            more_threads    =   False
            all_threads     =   True
            
        else :
            more_threads    =   self.geocodeThreadsMonitor.more_threads_available()
            all_threads     =   self.geocodeThreadsMonitor.all_threads_completed()
            
        if(self.get_run_state()   ==  sugm.STARTING) : 
            if( (not (more_threads) )  or 
                (self.geocodingResults.get_results_count() > 0) ) : 
                subgc.set_status_bar(sugm.RUNNING)
                self.set_run_state(sugm.RUNNING)
                
        elif(self.get_run_state()   ==  sugm.STOPPING) :
            if(all_threads) :
                subgc.set_status_bar(sugm.STOPPED)
                self.set_run_state(sugm.STOPPED)
            
        elif(self.get_run_state()   ==  sugm.PAUSING) :
            if(all_threads) : 
                subgc.set_status_bar(sugm.PAUSED)
                self.set_run_state(sugm.PAUSED)
                get_geocode_runner_results_log().flush_results_to_dataframe(opstat)
                
                subgc.control_bulk_keys([subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.ENABLE,subgc.ENABLE,subgc.ENABLE])
                
                if(self.checkpoint_on) :
                    if(sugm.GEOCODE_DEBUG)  :   
                        log_debug_dfc(-1,"checkpoint_on "+ str(self.state))        

                    self.checkpoint_results()
                    subgc.set_status_bar(sugm.CHECKPOINT_COMPLETE)


    def is_checkpoint_needed(self) :
        
        if((self.rowindex - self.last_checkpoint_rowid) >= self.checkpoint_interval) :
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"is_checkpoint_needed : True  : rowindex : " + str(self.rowindex) + " interval : " + str(self.checkpoint_interval) + " last_checkpoint_rowid :  " + str(self.last_checkpoint_rowid))
            return(True)
            
        else :
            return(False)
            
    def checkpoint_results(self,opstat) :
        
        self.update_status_bar()
        subgc.set_status_bar(sugm.CHECKPOINT_STARTED)
        subgc.control_bulk_keys([subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.DISABLE,subgc.ENABLE,subgc.DISABLE])

        
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"checkpoint_results : flush_results_to_dataframe")
        
        self.geocodingResults.flush_results_to_dataframe(opstat)
        
        if(self.geotype == sugm.QUERY) :
        
            if(self.geocid == sugm.GoogleId) :
                df_source   =   self.runParms.get(subgw.bulk_google_query_input_labelList[0]) 
            elif(self.geocid == sugm.BingId) :
                df_source   =   self.runParms.get(subgw.bulk_bing_query_input_labelList[0]) 
            elif(self.geocid == sugm.ArcGISId) :
                df_source   =   self.runParms.get(subgw.batch_arcgis_query_labelList[0]) 
                
        else :
            
            if(self.geocid == sugm.GoogleId) :
                df_source   =   self.runParms.get(subgw.bulk_google_reverse_input_labelList[0]) 
            elif(self.geocid == sugm.BingId) :
                df_source   =   self.runParms.get(subgw.bulk_bing_reverse_input_labelList[0]) 
        
        file_name       =   cfg.get_notebookName() + "_" + df_source + "_checkpoint"
        
        import os

        chckpt_file_path_name  =   os.path.join(cfg.get_notebookPath(),"PandasDataframeCleanser_files")
        chckpt_file_path_name  =   os.path.join(chckpt_file_path_name,"geocode_checkpoints")
        
        if(not (does_dir_exist(chckpt_file_path_name)) ) :   
            
            if( not(make_dir(chckpt_file_path_name)) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("Checkpoint dir " + chckpt_file_path_name + " not created successfully ")
                
        if(opstat.get_status()) :
            
            if(self.last_checkpoint_rowid == 0) :
                start_row_id    =   0
                file_number     =   0
            else :
                start_row_id    =   self.last_checkpoint_rowid
                file_number     =   floor(start_row_id / self.checkpoint_interval)
            
            chckpt_file_name    =   file_name + str(file_number) + ".csv"
            chckpt_file_name    =   os.path.join(chckpt_file_path_name,chckpt_file_name)
            
            if(sugm.GEOCODE_DEBUG)  :   
                log_debug_dfc(-1,"checkpoint_results : chckpt_file_name " + str(chckpt_file_name)) 
        
            if(does_file_exist(chckpt_file_name)) :
                backup_checkpoint_file_name     =   chckpt_file_name.replace(".csv","_backup.csv")
                delete_a_file(backup_checkpoint_file_name,opstat)
                rename_a_file(chckpt_file_name,backup_checkpoint_file_name,opstat)
        
            if(opstat.get_status()) :
        
                if(sugm.GEOCODE_DEBUG)  :   
                    log_debug_dfc(-1,"checkpoint_results : write to csv : " + str( self.last_checkpoint_rowid))
                
                try :
                
                    df = self.geocodingResults.get_geocoding_results_df() 
                    checkpoint_df   =   df.iloc[start_row_id:(len(df))] 
                    checkpoint_df   =   checkpoint_df.sort_values('source_df_rowid')
                    checkpoint_df.to_csv(chckpt_file_name,index=False)
                    self.last_checkpoint_rowid  =   len(df)
            
                except Exception as e: 
                    opstat.store_exception("Unable to export to csv file " + chckpt_file_name,e)
                    if(sugm.GEOCODE_DEBUG)  :
                        log_debug_dfc(-1,"Unable to export to csv file " + str(sys.exc_info()[0].__name__))
                    
                    self.last_checkpoint_rowid  =   len(df)                        
                        
            else :
                if(sugm.GEOCODE_DEBUG)  :   
                    log_debug_dfc(-1,"checkpoint_results : incomplete : " + str(opstat.get_errorMsg()))
                
                self.last_checkpoint_rowid  =   len(df)
            
            
                    
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"checkpoint_results : complete : " + str( self.last_checkpoint_rowid))
        
    
        subgc.set_status_bar(sugm.CHECKPOINT_COMPLETE)

        
    def get_results_log(self):
        return(self.geocodingResults)
    def get_results_log_count(self):
        if(not(self.geocodingResults is None)) :
            return(self.geocodingResults.get_results_count())
        else :
            return(0)
    def get_error_log(self):
        if(not(self.geocodingErrorLog is None)) :
            return(self.geocodingErrorLog)
        else :
            return(None)
    def get_halt_flag(self):
        return(self.halt_all_geocoding)
    def set_halt_flag(self,fstate):
        if(sugm.GEOCODE_DEBUG)  :   
            log_debug_dfc(-1,"set_halt_flag : " + str(fstate) + " " + " " + str(self.maxrows) + " " + str(self.rowindex))
        self.halt_all_geocoding     =   fstate
    def get_geocode_id(self):
        return(self.geocid)
    def get_geocode_type(self):
        return(self.geotype)
    def get_runParms(self):
        return(self.runParms)
        
    def get_geocode_connector(self):
        return(self.geocoder)
    def set_geocode_connector(self,connector):
        self.geocoder = connector
    def get_geocode_maxrows(self):
        return(self.maxrows)
    def get_geocode_checkpoint_interval(self):
        return(self.checkpoint_interval)

    def get_total_run_time(self) :
        if(self.stop_time == 0) :
            self.stop_time =  datetime.datetime.now()
        timedelta   =   self.stop_time  -   self.start_time
        return(timedelta.days * 24 * 3600 + timedelta.seconds)
        
    def get_geocode_lat_long_map(self):
        return(self.lat_long_map )
     

"""
#--------------------------------------------------------------------------
#   static geocode runner object
#--------------------------------------------------------------------------
"""    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        










