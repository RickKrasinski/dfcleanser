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
#import geopy
import googlemaps

import dfcleanser.common.cfg as cfg

import dfcleanser.Qt.utils.Geocode.BulkGeocodeModel as BGM
import dfcleanser.Qt.utils.Geocode.GeocodeModel as GM
import dfcleanser.Qt.utils.Geocode.GeocodeControl as GC
import dfcleanser.Qt.utils.Geocode.BulkGeocode as BG

from dfcleanser.common.common_utils import (opStatus, get_parms_for_input, run_jscript, display_blank_line, log_debug_dfc)

from dfcleanser.sw_utilities.DisplayUtils import (get_exception_html, display_status_note, display_notes, displayParms)

from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import (GEOCODE_TRACE_GET_GEOCODE, GEOCODE_TRACE_GET_GEOCODE_LOAD, 
                                                          GEOCODE_TRACE_GET_GEOCODE_VALUES, GEOCODE_TRACE_PROCESS_RESULTS)

from math import floor

DEBUG_MERGE     =   False
"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Common bulk geocoding control methods
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def process_bulk_geocoding_run_cmd(cmd, parms=None) :
    """
    * -------------------------------------------------------
    * function : process the bulk geocoding commands
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(GEOCODE_TRACE_GET_GEOCODE)  :   
        log_debug_dfc(-1,"[process_bulk_geocoding_run_cmd] " + str(cmd))
    
    opstat  =   opStatus()
    
    if(cmd == BGM.BULK_START_GEOCODER) :

        opstat  =   BGM.start_geocode_runner()
                
        if(not (opstat.get_status()) ) :
            send_run_report_error(cmd, opstat.get_errorMsg())
    
        if(GEOCODE_TRACE_GET_GEOCODE)  :
            log_debug_dfc(-1,"[process_bulk_geocoding_run_cmd][BULK_START_GEOCODER] status : " + str(opstat.get_status()))  
            
    elif(cmd == BGM.BULK_STOP_GEOCODER) :
        BGM.stop_geocode_runner(None)
        
    elif(cmd == BGM.BULK_PAUSE_GEOCODER) :
        BGM.pause_geocode_runner()
        
    if(cmd == BGM.BULK_RESUME_GEOCODER) :
        BGM.resume_geocode_runner()
    
    elif(cmd == BGM.BULK_VIEW_ERRORS) :
        run_jscript("view_geocode_errors();","view_geocode_errors")
        
    elif(cmd == BGM.BULK_RESULTS_GEOCODER) :
        
        error_log       =   BGM.get_geocode_runner_error_log()
        total_errors    =   error_log.get_error_count()        
        total_results   =   BGM.get_geocode_runner_results_count()  
        
        if((total_errors==0) and (total_results==0)) :
            display_status_note("No Bulk Geocoding Results to Process") 
        else :
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_RESULTS_BASE,opstat)
        
    elif(cmd == BGM.REPORT_GEOCODE_RUN_ERROR) :
        
        run_cmd     =   int(parms[0])
        err_msg     =   parms[1]
        geocid      =   BGM.get_geocode_runner_id() 
        geotype     =   BGM.get_geocode_runner_type() 
        
        if(run_cmd==BGM.BULK_LOAD_GEOCODER) : cmd_text         =   "Load Geocoder"
        elif(run_cmd==BGM.BULK_START_GEOCODER) : cmd_text      =   "Start Geocoder"
        elif(run_cmd==BGM.BULK_STOP_GEOCODER) : cmd_text       =   "Stop Geocoder"
        elif(run_cmd==BGM.BULK_PAUSE_GEOCODER) : cmd_text      =   "Pause Geocoder"
        elif(run_cmd==BGM.BULK_RESUME_GEOCODER) : cmd_text     =   "Resume Geocoder"
        elif(run_cmd==BGM.BULK_VIEW_ERRORS) : cmd_text         =   "View Errors Geocoder"
        elif(run_cmd==BGM.BULK_RESULTS_GEOCODER) : cmd_text    =   "Get Results Geocoder"
        elif(run_cmd==BGM.PROCESS_BULK_RESULTS) : cmd_text     =   "Process Results Geocoder"
        else :                                     cmd_text    =   "Unknown command"
        
        if(geocid is None)      :   geocid      =   "None"
        if(geotype is None)     :   geotype     =   "None"
        if(err_msg is None)     :   err_msg     =   "No  details"
        
        display_geocode_main_taskbar()        
        sugc.clear_sw_utility_geocodedata()

        display_blank_line()

        display_status_note("Bulk Geocoding Runtime Error : " + cmd_text,False,None,None)

        notes     =   ["geocid  : " + str(geocid),
                       "geotype : " + str(geotype),
                       "Details : " + err_msg]
        
        display_notes(notes,True)

def send_run_report_error(cmd, err_msg) :
    
    report_error_js     =   "report_geocode_run_error(" + str(cmd) + ",'" + err_msg + "');"
    if(BGM.DEBUG_GEOCODE_BULK_UTILS)  :   
        log_debug_dfc(-1,"send_run_report_error " + str(cmd) + " " + str(err_msg))
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(report_error_js,"fail report run error : "+ str(cmd) + err_msg)
    
    

    
"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Common bulk geocoding control methods
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

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
    * --------------------------------------------------------------------------
    """
    
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
        log_debug_dfc(-1,"[get_bulk_coords] " + str(geocid) + " " + str(refresh))
    
    opstat  =   opStatus()
    parms   =   None 
    
    if(not (inputs == None)) :
        
        if(geocid == GM.GoogleId) :

            fparms  =   get_parms_for_input(inputs,BG.bulk_google_query_input_idList)
            cfg.set_config_value(BG.bulk_google_query_input_id+"Parms",fparms)
    
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(-1,"[get_bulk_coords][cfg.set_config_value] " + str(BG.bulk_google_query_input_id+"Parms") + " " + str(cfg.get_config_value(BG.bulk_google_query_input_id+"Parms")))

            parms   =   inputs
        
        elif(geocid == GM.BingId) :

            fparms  =   get_parms_for_input(inputs,BG.bulk_bing_query_input_idList)
            cfg.set_config_value(BG.bulk_bing_query_input_id+"Parms",fparms)
            
            if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
                log_debug_dfc(-1,"[get_bulk_coords][cfg.set_config_value] " + str(BG.bulk_bing_query_input_id+"Parms") + " " + str(cfg.get_config_value(BG.bulk_bing_query_input_id+"Parms")))

            parms   =   inputs
        
    else :

        if(geocid == GM.GoogleId) :
            parms   =   [BG.bulk_google_query_input_idList,cfg.get_config_value(BG.bulk_google_query_input_id+"Parms")]
        elif(geocid == GM.BingId) :
            parms   =   [BG.bulk_bing_query_input_idList,cfg.get_config_value(BG.bulk_bing_query_input_id+"Parms")]
    
    if(not(parms == None)) : 
        
        runParms    =   validate_bulk_parms(geocid,GM.QUERY,parms,opstat) 
        
        if(opstat.get_status()) :
        
            if(geocid ==GM.GoogleId) :

                df_title        =  runParms.get("dataframe_to_geocode_from")
                columns         =  runParms.get("dataframe_address_columns")  

                address_map     =   BGM.get_address_map(df_title,columns)
                
                if(not (refresh)) :
                    BGM.load_geocode_runner(GM.GoogleId,GM.QUERY,runParms,address_map)
                
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_console
                display_geocoder_console(GM.GoogleId,GM.QUERY,runParms,opstat,refresh,BGM.LOAD)
            
            elif(geocid == GM.BingId) :

                if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
                    log_debug_dfc(-1,"[get_bulk_coords][runParms] \n        " + str(runParms))

                df_title    =  runParms.get("dataframe_to_geocode")
                columns     =  runParms.get("dataframe_address_columns")  

                address_map     =   BGM.get_address_map(df_title,columns)
                
                if(not (refresh)) :
                    BGM.load_geocode_runner(GM.BingId,GM.QUERY,runParms,address_map)

                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_console
                display_geocoder_console(GM.BingId,GM.QUERY,runParms,opstat,refresh,BGM.LOAD)
        
        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[get_bulk_coords] : " + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            BG.display_bulk_query_geocoding(geocid)
       
    
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
    
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
        log_debug_dfc(-1,"[get_bulk_addresses] " + str(geocid) + " " + str(refresh))
        log_debug_dfc(-1,"[get_bulk_addresses] inputs \n              " + str(inputs))
    
    opstat  =   opStatus()
    parms   =   None
    fparms  =   None
    
    if(not (inputs == None)) :
        
        if(geocid == GM.GoogleId) :
            fparms  =   get_parms_for_input(inputs,BG.bulk_google_reverse_input_idList)
            cfg.set_config_value(BG.bulk_google_reverse_input_id+"Parms",fparms)

            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(-1,"[get_bulk_coords][cfg.set_config_value] " + str(BG.bulk_google_reverse_input_id+"Parms") + " " + str(cfg.get_config_value(BG.bulk_google_reverse_input_id+"Parms")))

            parms   =   inputs
        elif(geocid == GM.BingId) :
            fparms  =   get_parms_for_input(inputs,BG.bulk_bing_reverse_input_idList)
            cfg.set_config_value(BG.bulk_bing_reverse_input_id+"Parms",fparms)

            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(-1,"[get_bulk_coords][cfg.set_config_value] " + str(BG.bulk_bing_reverse_input_id+"Parms") + " " + str(cfg.get_config_value(BG.bulk_bing_reverse_input_id+"Parms")))

            parms   =   inputs
        
    else :
        
        if(geocid == GM.GoogleId) :
            parms   =   [BG.bulk_google_reverse_input_idList,cfg.get_config_value(BG.bulk_google_reverse_input_id+"Parms")]
        elif(geocid == GM.BingId) :
            parms   =   [BG.bulk_bing_reverse_input_idList,cfg.get_config_value(BG.bulk_bing_reverse_input_id+"Parms")]
    
    
    if(not (parms == None)) : 
        
        runParms    =   validate_bulk_parms(geocid,GM.REVERSE,parms,opstat) 
        
        if(opstat.get_status()) :
        
            if(geocid == GM.GoogleId) :
                
                if(not (refresh)) :
                    BGM.load_geocode_runner(GM.GoogleId,GM.REVERSE,runParms,None)
                
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_console
                display_geocoder_console(GM.GoogleId,GM.REVERSE,runParms,opstat,refresh,BGM.LOAD)
                
            elif(geocid == GM.BingId) :
                
                if(not (refresh)) :
                    BGM.load_geocode_runner(GM.BingId,GM.REVERSE,runParms,None)

                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_console
                display_geocoder_console(GM.BingId,GM.REVERSE,runParms,opstat,refresh,BGM.LOAD)
                
        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[gget_bulk_addresses] : " + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            BG.display_bulk_reverse_geocoding(geocid)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocoding components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def process_bulk_geocoding_errors(geocid,geotype,rowid,inputParms,error_msg,note=None) :
    """
    * -------------------------------------------------------
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
    * ------------------------------------------------------
    """

    if(BGM.GEOCODE_TRACE_PROCESS_ERRORS) :
        log_debug_dfc(rowid,"[process_bulk_geocoding_errors]  : " + str(inputParms))
        log_debug_dfc(rowid,"[process_bulk_geocoding_errors] error msg : " + str(error_msg) + " : " + str(note))

    error_limit         =   BGM.get_geocode_runner_error_log().get_error_limit() * 0.01
    total_errors        =   BGM.get_geocode_runner_error_log().get_error_count()
    max_rows            =   BGM.get_geocode_maxrows()
    current_error_rate  =   (total_errors / max_rows) 
    total_results       =   BGM.get_geocode_runner_results_log().get_results_count()
    
    dfc_error_log       =  BGM.get_geocode_runner_error_log() 

    if(BGM.GEOCODE_TRACE_PROCESS_ERRORS)  :   
        log_debug_dfc(rowid,"[process_bulk_geocoding_errors] : " + str(geotype) + " state : " + str(BGM.get_geocode_runner_state()) + " error_count : " + str(BGM.get_geocode_runner_error_log().get_error_count()) + " error_limit : " + str(error_limit) + " current_error_rate : " + str(current_error_rate))

    opstat  =   opStatus()
    
    if( (BGM.get_geocode_runner_state() == BGM.ERROR_LIMIT) ):
        return
    
    try :
        
        dfc_error_log.log_error(rowid,inputParms,error_msg,note,opstat)
    
        BGM.set_progress_bar_value(geocid,geotype,BGM.ERROR_BAR,total_errors,int(current_error_rate))
    
        if(BGM.GEOCODE_TRACE_PROCESS_ERRORS) :
            log_debug_dfc(rowid,"[process_bulk_geocoding_errors] : current_error_rate : error_limit : " + str(inputParms) + str(current_error_rate) + " : " + str(error_limit))

        if(current_error_rate > error_limit) :
            
            if(not(BGM.get_geocode_runner_state() == BGM.ERROR_LIMIT)) :
                BGM.set_geocode_runner_halt_flag(True)  
                
                from threading import Thread 
                state_change     =   Thread(target=set_error_limit_shutoff)
                state_change.start()
                
                #set_geocode_runner_state(sugm.ERROR_LIMIT)
                BGM.set_status_bar(BGM.ERROR_LIMIT)
                BGM.get_geocode_runner_error_log().flush_errors_to_dataframe(opstat)
                
                if(total_errors > 0) :
                    BGM.get_geocode_runner_results_log().flush_results_to_dataframe(opstat)
                
                BGM.control_bulk_keys([BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.ENABLE,BGM.ENABLE],"F")
            
            if(BGM.GEOCODE_TRACE_PROCESS_ERRORS)  :   
                log_debug_dfc(rowid,"[process_bulk_geocoding_errors] : error limit exceeded : error_limit : " + str(error_limit) + " total_results : " + str(total_results) + " total_errors : " + str(total_errors))
            
    except :
        if(BGM.GEOCODE_TRACE_PROCESS_ERRORS)  : 
            log_debug_dfc(rowid,"[process_bulk_geocoding_errors] Exception : " + str(geocid) + " " + str(geotype) + " " + str(rowid) + " " + str(sys.exc_info()[0].__name__))


def set_error_limit_shutoff() :

    BGM.set_geocode_runner_state(BGM.ERROR_LIMIT) 
    
    if(GEOCODE_TRACE_GET_GEOCODE)  : 
        log_debug_dfc(-1,"[set_error_limit_shutoff] : geocoder state : " + str(BGM.get_geocode_runner_state()))

    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocode methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    


def display_google_test_results(address,results) : 
    """
    * ---------------------------------------------------------------------
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
    
    address_results    =   GM.google_address_components(results.get_address_components())
    
    displayParms("Google Address Components",
                 [GM.GOOGLE_GEOCODER_STREET_NUMBER_ID,
                  GM.GOOGLE_GEOCODER_ROUTE_ID,
                  GM.GOOGLE_GEOCODER_NEIGHBORHOOD_ID,
                  GM.GOOGLE_GEOCODER_LOCALITY_ID,
                  GM.GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID,
                  GM.GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID,
                  GM.GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID,
                  GM.GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID,
                  GM.GOOGLE_GEOCODER_COUNTRY_ID,
                  GM.GOOGLE_GEOCODER_POSTAL_CODE_ID],
                  [address_results.get_address_component(GM.GOOGLE_GEOCODER_STREET_NUMBER_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_ROUTE_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_NEIGHBORHOOD_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_LOCALITY_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_COUNTRY_ID),
                   address_results.get_address_component(GM.GOOGLE_GEOCODER_POSTAL_CODE_ID)],
                  cfg.SWUtilities_ID)
 

"""
#--------------------------------------------------------------------------
#   google bulk geocode methods
#--------------------------------------------------------------------------
"""

def get_google_query_results(rowid,address,queryParms,opstat) :
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
    
    if(GEOCODE_TRACE_GET_GEOCODE)  :   
        log_debug_dfc(rowid," [get_google_query_results] : " + address)
        
    geocode_results =   None
    gmaps           =   BGM.get_geocode_connector() 
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(BG.google_bulk_geocoder_id+"Parms")

        if(GEOCODE_TRACE_GET_GEOCODE)  :   
            log_debug_dfc(rowid,"[got_google_connection] : " + str(cparms))

        gmaps   =   BG.get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        BGM.set_geocode_connector(gmaps)
    
    if(opstat.get_status()) :   

        if(not (queryParms == None)) :
            
            """
            bounds_parm          =   queryParms.get("bounds")
            if(bounds_parm == "None") :
                bounds_parm    =   None

            regionParm      =   queryParms.get("region")
            colon_char      =   regionParm.find(":")

            regionParm      =   regionParm[(colon_char + 1) :]

            languageParm    =   queryParms.get("language")
            """

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
            api_parms   = dfc_Geocode_Runner.get_api_parms()

            bounds_parm     =   None#api_parms.get_api_parm("bounds_parm")
            regionParm      =   api_parms.get_api_parm("regionParm")
            languageParm    =   api_parms.get_api_parm("languageParm")

        
        else :

            bounds_parm     =   None

            regionParm      =   None
            languageParm    =   None

        try :
            
            if(not (queryParms == None)) :

                try :
 
                    geocode_results =   gmaps.geocode(address, 
                                                  bounds=bounds_parm,
                                                  region=regionParm,
                                                  language=languageParm)
                except Exception as e :

                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        log_debug_dfc(rowid,"[unable to get  geocode_results] : ")


                    opstat.set_status(False)
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[unable to get  geocode_results] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    #display_exception(title,status_msg,e)

            else :

                geocode_results =   gmaps.geocode(address)
        
        except googlemaps.exceptions.ApiError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(get_parms_for_input.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsgug(GM.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.OverQueryLimitErrorMessage)

        except Exception as e:
            opstat.set_status(False)
            opstat.store_exception("Unable to get geocode results ",e)
            log_debug_dfc(-1, "[gmaps.geocode]  error : "+ str(sys.exc_info()[0].__name__) + " : " + str(sys.exc_info()[1])) 

    if(opstat.get_status()) :  

        if(GEOCODE_TRACE_GET_GEOCODE)  :
            log_debug_dfc(-1,"[get_google_query_results] ok location : " + str(address) + " : " + str(len(geocode_results)))
        
        try :
    
            if(len(geocode_results) > 1) :  
                current_geocode_results    =  GM.google_geocode_results(rowid,geocode_results[0],geocode_results[1])
            elif(len(geocode_results) == 1) : 
                current_geocode_results    =  GM.google_geocode_results(rowid,None,geocode_results[0])    
            else :
                current_geocode_results    =  None
            
        except :
            current_geocode_results    =  None 

    else :
        
        if(GEOCODE_TRACE_GET_GEOCODE)  :
            log_debug_dfc(-1,"[get_google_query_results] exception : " + opstat.getErrorMsg())


    return(current_geocode_results)


def process_google_query_results(rowid,inputParms,runParms,geocode_results,opstat,error_rowid=None) :
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
    
    results_df          =   BGM.get_geocode_runner_results_log()

    if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
        log_debug_dfc(rowid,"[process_google_query_results]  : " + str(inputParms) ) 
    
    if(not(error_rowid is None)):
        
        if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
            log_debug_dfc(-1,"[add_nan_result for None]")        

        results_df.add_nan_result(error_rowid,inputParms,geocode_results,opstat)
        
    else :
        
        try :
            
            lat_long_merged     =   False
        
            lat_long_col        =   runParms.get("new_dataframe_lat_long_column_name(s)")
            
            if(lat_long_col.find("]") > -1) :
                lat_long_merged    =   True
    
            save_full_address   =   True
            full_addr_col_name  =   runParms.get("save_geocoder_full_address_column_name")

            if(full_addr_col_name == "None") :
                save_full_address   =   False
     
            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_query_results]  : lat_long_merged " + str(lat_long_merged) ) 
                log_debug_dfc(rowid,"[process_google_query_results]  : save_full_address " + str(save_full_address) ) 

            georunParms     =   [GM.QUERY,GM.GoogleId,inputParms,lat_long_merged,save_full_address]
            results_df.add_result(rowid,georunParms,geocode_results,opstat)
       
        except :

            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("process_google_results exception" + str(sys.exc_info()[0].__name__))
 
           
"""
#--------------------------------------------------------------------------
#   google bulk geocode reverse methods
#--------------------------------------------------------------------------
"""

def find_best_google_reverse_result(rowid,reverse_results,reverseParms) :
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
    
    locations       =   reverseParms.get("valid_location_type(s)",None)
    
    location_types  =   locations.replace("[","")
    location_types  =   location_types.replace("]","")
    location_types  =   location_types.split(",")
    
    if(len(reverse_results) > 0) :
    
        if("ROOFTOP" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "ROOFTOP") :
                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        log_debug_dfc(rowid,"[find_best_google_reverse_result][ROOFTOP] " + str(i))
                    return(reverse_results[i])
        elif("GEOMETRIC_CENTER" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "GEOMETRIC_CENTER") :
                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        log_debug_dfc(rowid,"[find_best_google_reverse_result][GEOMETRIC_CENTER] " + str(i))
                    return(reverse_results[i])
        elif("RANGE_INTERPOLATED" in location_types) :
            for i in range(len(reverse_results)) :
                if(reverse_results[i].get("geometry").get("location_type") == "RANGE_INTERPOLATED") :
                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        log_debug_dfc(rowid,"[find_best_google_reverse_result][RANGE_INTERPOLATED] " + str(i))
                    return(reverse_results[i])
        elif("APPROXIMATE" in location_types) :
            return(reverse_results[0])
        else :
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(rowid,"[find_best_google_reverse_result][NOT FOUND] " + str(i))

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
    if(GEOCODE_TRACE_GET_GEOCODE)  :   
        log_debug_dfc(rowid,"[get_google_reverse_results] : lat_lng " + str(lat_long))
    
    reverse_results =   None
    
    cparms  =   [" "," "," "]
    
    gmaps   =   BGM.get_geocode_connector() 
    
    if(gmaps == None) :

        cparms  =   cfg.get_config_value(BG.google_bulk_geocoder_id+"Parms")
        gmaps   =   BG.get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        BGM.set_geocode_connector(gmaps)

    if(opstat.get_status()) :  
        
        lat_lng_parm    =   lat_long.replace("[","")
        lat_lng_parm    =   lat_lng_parm.replace("]","")
        lat_lng_list    =   lat_lng_parm.split(",")
        
        if(not (reverseParms == None)) :

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
            api_parms   = dfc_Geocode_Runner.get_api_parms()

            loc_type_parm   =   api_parms.get_api_parm("loc_type_parm")
            languageParm    =   api_parms.get_api_parm("languageParm")

        else :

            loc_type_parm   =   None
            languageParm    =   None

        try :
        
            reverse_results =   gmaps.reverse_geocode(lat_lng_list,
                                                      result_type=None,
                                                      location_type=loc_type_parm,
                                                      language=languageParm)
   
        except googlemaps.exceptions.ApiError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.OverQueryLimitErrorMessage)
        except  :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("get_google_reverse_results exception : " + str(sys.exc_info()[0].__name__))
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(rowid,"[get_google_reverse_results] exception : " + str(sys.exc_info()[0].__name__))

            
        if(opstat.get_status()) :
            try :

                best_results                =   find_best_google_reverse_result(rowid,reverse_results,reverseParms)
                current_reverse_results     =   GM.google_reverse_results(rowid,None,best_results,opstat)
            
            except :
                current_reverse_results    =  None
                opstat.set_status(False)
                opstat.set_errorMsg("get_google_reverse_results assign results exception : ")
                if(GEOCODE_TRACE_GET_GEOCODE)  :   
                    log_debug_dfc(rowid,"[find_best_google_reverse_result] exception : " + str(sys.exc_info()[0].__name__))

    
    if(GEOCODE_TRACE_GET_GEOCODE)  :
        if(current_reverse_results is None) :
            log_debug_dfc(rowid,"[get_google_reverse_results None] : ")
        else :
            log_debug_dfc(rowid,"[get_google_reverse_results]  : " + " lat " + str(current_reverse_results.get_lat()) + " lng " + str(current_reverse_results.get_lng()) + " \n                  addr " +  str(current_reverse_results.get_formatted_address()))
    
    return(current_reverse_results)

    
def process_google_reverse_results(rowid,inputParms,runParms,reverse_results,opstat,error_rowid=None) :
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
    if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
        log_debug_dfc(rowid,"[process_google_reverse_results] inparms : " + str(inputParms))
    
    results_df          =   BGM.get_geocode_runner_results_log()
    
    if(not(error_rowid is None)):
        
        if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
            log_debug_dfc(rowid,"[process_google_reverse_results] add_nan_result for None")        

        parmsDict   =   None
        results_df.add_nan_result(error_rowid,inputParms,parmsDict,opstat)
        
    else :
    
        try :
            
            address_components      =   GM.google_address_components(reverse_results.get_address_components())
            requested_addr_comps    =   runParms.get("address_components_list")
            user_addr_comps         =   GM.get_google_address_components(requested_addr_comps)

            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_reverse_results] user_addr_comps : \n      " + str(user_addr_comps))
            
            addr_length             =   runParms.get("address_components_length_flag")
            if(addr_length == "short") :
                addr_length     =   True
            else :
                addr_length     =   False
        
            import numpy as np
        
            addr_comps  =   []

            for i in range(len(user_addr_comps)) :

                if(len(user_addr_comps[i]) > 0) :

                    addr_comp  =  address_components.get_address_component(user_addr_comps[i],addr_length)
                    
                    if(addr_comp == "") :
                        addr_comps.append(np.NaN) 
                    else :
                        addr_comps.append(addr_comp)
                
            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_reverse_results] retrieved addr_comps : \n     " + str(addr_comps))
                    
            row_reverse_results     =   []
            row_reverse_results.append(reverse_results.get_row_Id())
            row_reverse_results.append(inputParms)
            row_reverse_results.append(reverse_results.get_formatted_address())
            
            for i in range(len(addr_comps)) :
                row_reverse_results.append(addr_comps[i])    
            
            row_reverse_results.append(reverse_results.get_location_type())
            
            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_reverse_results] row_reverse_results : \n    " + str(row_reverse_results))

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import REVERSE,GoogleId
            georunParms  =   [REVERSE,GoogleId,inputParms,runParms]

            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_reverse_results] georunParms : " + str(georunParms))

            #results_df          =   BGM.get_geocode_runner_results_log()
            results_df.add_result(rowid,georunParms,row_reverse_results,opstat)
        
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("process_google_reverse_results exception " + str(sys.exc_info()[0].__name__))
            if(GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_google_reverse_results] exception : " + str(inputParms))


"""
#--------------------------------------------------------------------------
##--------------------------------------------------------------------------
#   geopy bulk geocode methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_geopy_geocoder_results(geocid,geotype,geolocator,rowid,geoparm,queryParms) :
    """
    * --------------------------------------------------------
    * function : get geocoder results 
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

    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import bulk_geocodes_sent_out
    bulk_geocodes_sent_out.append(rowid)

    if(GEOCODE_TRACE_GET_GEOCODE)  :   
        log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : address " + str(geocid) + " " + str(geotype) + " " + str(geoparm))  
        #log_debug_dfc(rowid,"[get_geopy_geocoder_results] : queryParms " + str(queryParms) )  

    if(geotype == GM.QUERY) :

        location    =   None
        
        if(geocid == GM.BingId) :

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
            api_parms   = dfc_Geocode_Runner.get_api_parms()

            user_location_parm          =   api_parms.get_api_parm("user_location_parm")
            culture_parm                =   api_parms.get_api_parm("culture_parm")
            include_neighborhood_parm   =   api_parms.get_api_parm("include_neighborhood_parm")
            include_country_code_parm   =   api_parms.get_api_parm("include_country_code_parm")


            if(GEOCODE_TRACE_GET_GEOCODE_VALUES)  :   
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : query : " + geoparm)
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : user_location_parm : " + str(user_location_parm) + str(type(user_location_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : culture_parm : " + str(culture_parm) + str(type(culture_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : include_neighborhood_parm : " + str(include_neighborhood_parm) + str(type(include_neighborhood_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : include_country_code_parm : " + str(include_country_code_parm) + str(type(include_country_code_parm)))


            try :

                location    =    geolocator.geocode(query=geoparm,
                                                    user_location=user_location_parm,
                                                    culture=culture_parm,
                                                    include_neighborhood=include_neighborhood_parm,
                                                    include_country_code=include_country_code_parm)

            except Exception as e:

                title       =   "dfcleanser error"       
                status_msg  =   "[get_geopy_geocoder_results] invalid user_location "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : query : " + geoparm)
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : user_location_parm : " + str(user_location_parm) + str(type(user_location_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : culture_parm : " + str(culture_parm) + str(type(culture_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : include_neighborhood_parm : " + str(include_neighborhood_parm) + str(type(include_neighborhood_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : include_country_code_parm : " + str(include_country_code_parm) + str(type(include_country_code_parm)))

                location    =   None
 
        return(location)
            
    else : # geocode REVERSE

        address     =   None

        if(geocid == GM.BingId) :
            
            if(GEOCODE_TRACE_GET_GEOCODE_VALUES)  :   
                log_debug_dfc(rowid,"[get_geopy_geocoder_results] : bing reverse : " + str(geoparm))

            lat_lng                     =   geoparm.replace("[","")
            lat_lng                     =   lat_lng.replace("]","")
            lat_lng                     =   lat_lng.split(",")
            
            lat                         =   float(lat_lng[0])
            lng                         =   float(lat_lng[1])
            
            geo_lat_lng                 =   [lat,lng]
            
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : geo_lat_lng : " + str(geo_lat_lng) )
            
            import geopy.point    
            qpoint  =   geopy.point.Point(geo_lat_lng[0],geo_lat_lng[1],0)

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
            api_parms   = dfc_Geocode_Runner.get_api_parms()

            culture_parm                =   api_parms.get_api_parm("culture_parm")
            include_country_code_parm   =   api_parms.get_api_parm("include_country_code_parm")

            if(GEOCODE_TRACE_GET_GEOCODE_VALUES)  :   
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : query : " + geoparm)
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : culture_parm : " + str(culture_parm) + str(type(culture_parm)))
                log_debug_dfc(rowid,"  [get_geopy_geocoder_results] : include_country_code_parm : " + str(include_country_code_parm) + str(type(include_country_code_parm)))

            location     =   geolocator.reverse(query=qpoint,
                                               culture=culture_parm,
                                               include_country_code=include_country_code_parm)
            
            reverse_geocode_results     =  GM.geopy_reverse_results(rowid,geoparm,location) 

        return(reverse_geocode_results)


def get_geopy_geocode_results(geocid,geotype,rowid,address,queryParms,opstat) :
    """
    * -------------------------------------------------------
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
    
    import geopy
    current_geocode_results =   None

    if(0):#GEOCODE_TRACE_GET_GEOCODE) :
        log_debug_dfc(rowid,"    [get_geopy_geocode_results] address : " + str(address))

    geolocator = GC.get_geocoder_engine(geocid,opstat)
    
    if(not(opstat.get_status())) :
        opstat.set_errorMsg(GC.GeopyGeocoderConnectionErrorMessage)
        if(GEOCODE_TRACE_GET_GEOCODE) :
            log_debug_dfc(rowid,"\n    [get_geopy_geocode_results] [get_geocoder_engine-failure] : " + str(opstat.get_status()) )  

    if(opstat.get_status()) :   

        try :

            geocode_results    =   get_geopy_geocoder_results(geocid,geotype,geolocator,rowid,address,queryParms) 

            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                log_debug_dfc(rowid,"  [get_geopy_geocode_results] : location : " + str(geocode_results))

        except geopy.exc.GeopyError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyErrorMessage)
        except geopy.exc.ConfigurationError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyConfigurationErrorMessage)
        except geopy.exc.GeocoderServiceError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderServiceErrorMessage)
        except geopy.exc.GeocoderQueryError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderQueryErrorMessage)
        except geopy.exc.GeocoderQuotaExceeded :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderQuotaExceededMessage)
        except geopy.exc.GeocoderAuthenticationFailure :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderAuthenticationFailureMessage)
        except geopy.exc.GeocoderInsufficientPrivileges :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderInsufficientPrivilegesMessage)
        except geopy.exc.GeocoderTimedOut :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderTimedOutMessage)
        except geopy.exc.GeocoderUnavailable :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderUnavailableMessage)
        except geopy.exc.GeocoderParseError :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderParseErrorMessage)
        except geopy.exc.GeocoderNotFound :
            opstat.set_status(False)
            opstat.set_errorMsg(GM.GeopyGeocoderNotFoundMessage)
        except Exception as e:
            opstat.set_status(False)
            opstat.store_exception("[Unable to get geocode results] ",e)
            log_debug_dfc(-1, "[Bing query]  error : "+ str(sys.exc_info()[0].__name__) + " : " + str(sys.exc_info()[1])) 

        if(opstat.get_status()) :  
            
            if(geotype == GM.QUERY) :
            
                if( not (geocode_results == None)) :
                    full_address    =   geocode_results.address
                    latitude        =   geocode_results.latitude
                    longitude       =   geocode_results.longitude
                    
                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        log_debug_dfc(rowid,"  [get_geopy_geocode_results] : " + str(latitude) + " : " + str(longitude))
            
                    try :
                        current_geocode_results    =  GM.geopy_geocode_results(rowid,full_address,latitude,longitude,opstat)
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Error getting geopy geocoder " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))
                    
            else :
            
                if( not (geocode_results is None)) :

                    if(GEOCODE_TRACE_GET_GEOCODE) :
                        log_debug_dfc(rowid,"   [get_geopy_geocode_results] got geocode results : " + str(type(geocode_results)))


                    full_address    =   geocode_results.get_location()#

                    if(GEOCODE_TRACE_GET_GEOCODE) :
                        log_debug_dfc(rowid,"    [get_geopy_geocode_results] full_address : " + str(type(full_address)))

                    try :
                        current_geocode_results    =  geocode_results
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Error getting geopy reverse " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))
                
        else :
            current_geocode_results    =  None            
    
    return(current_geocode_results)


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#   Common geoociding components
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def process_geopy_geocode_results(rowid,geocid,geotype,inputParms,runParms,geopy_results,opstat,error_rowid=None) :
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

    if(GEOCODE_TRACE_PROCESS_RESULTS) :
        log_debug_dfc(rowid,"[process_geopy_geocode_results] : " + str(inputParms) + " error : " + str(error_rowid))
    
    results_df          =   BGM.get_geocode_runner_results_log()
    
    if(error_rowid is None) :
        
        try :
        
            if(not (geopy_results is None)) :

                if(geotype == GM.QUERY) :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                    separate_lat_lng     =   False
            
                    if(geocid == GM.BingId) :
                        lat_long_colname    =   runParms.get("new_dataframe_lat_long_column_name(s)")
                        full_addr_col_name  =   runParms.get("save_geocoder_full_address_column_name")
                    else :
                        lat_long_colname    =   runParms.get("new_dataframe_lat_long_column_name(s)")
                        full_addr_col_name  =   runParms.get("save_geocoder_full_address_column_name")

                    separate_lat_lng    =   False

                    #if(GEOCODE_TRACE_PROCESS_RESULTS) :
                    #    log_debug_dfc(rowid,"[process_geopy_geocode_results] lat_long_colname : " + str(lat_long_colname) + " full_addr_col_name : " + str(full_addr_col_name))

                    if( (lat_long_colname.find("]") > -1) and (lat_long_colname.find("[") > -1) ) :
                        separate_lat_lng    =   True 
                    else :
                        if( (lat_long_colname.find("(") > -1) and (lat_long_colname.find(")") > -1) ) :
                            separate_lat_lng    =   True 
                    
                    save_full_address   =   True

                    #if(GEOCODE_TRACE_PROCESS_RESULTS) :
                    #    log_debug_dfc(rowid,"[process_geopy_geocode_results] separate_lat_lng : " + str(separate_lat_lng) + " save_full_address : " + str(save_full_address))
        
                    georunParms     =   [GM.QUERY,GM.BingId,inputParms,separate_lat_lng,save_full_address]
                    results_df.add_result(rowid,georunParms,geopy_results,opstat)

                else : # geopy reverse
                
                    if(geocid == GM.BingId) :
                        
                        addrcompsflag   =   runParms.get("address_components_to_retrieve")
                            
                        if(GEOCODE_TRACE_PROCESS_RESULTS) :
                            log_debug_dfc(rowid,"[process_geopy_geocode_results] addrcompsflag : " + str(addrcompsflag))

                        if( (addrcompsflag is None) or (addrcompsflag == "Full Address Only") ) : 
                            georunParms     =   [GM.REVERSE,GM.BingId,inputParms,addrcompsflag]
                            results_df.add_result(rowid,georunParms,geopy_results,opstat)

                        else :
                            georunParms     =   [GM.REVERSE,GM.BingId,inputParms,addrcompsflag]
                            results_df.add_result(rowid,georunParms,geopy_results,opstat)

                    else :
                        
                        results_df.add_result(rowid,[geopy_results.get_row_Id(),
                                               inputParms, 
                                               geopy_results.get_full_address()],opstat)
                        
            else :
        
                process_bulk_geocoding_errors(geocid,geotype,geopy_results.get_row_Id(),inputParms,None,"[process_geopy_geocode_results] ewaults none")
                results_df.add_nan_result(geopy_results.get_row_Id(),inputParms,None,opstat)

        except :
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("Error getting geopy " + str(geocid) + " results : " + str(sys.exc_info()[0].__name__))
            
            if(BGM.GEOCODE_TRACE_PROCESS_RESULTS)  :   
                log_debug_dfc(rowid,"[process_geopy_geocode_results][Error getting geopy] " + str(sys.exc_info()[0].__name__))        

    
    else : # error row
        
        if(BGM.GEOCODE_TRACE_PROCESS_RESULTS)  :   
            log_debug_dfc(rowid,"[add_nan_result] for None")        

        results_df.add_nan_result(error_rowid,inputParms,None,opstat)



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
    
        results_df  =   BGM.get_geocode_runner_results_log().get_geocoding_results_df()
        errors_df   =   BGM.get_geocode_runner_error_log().get_error_log_df()
        
        if(cmd == GM.PROCESS_BULK_RESULTS_APPEND_PROCESS) :
        
            from dfcleanserQt.utils.Geocode.BulkGeocodeConsole import bulk_geocode_append_input_idList
            proc_parms                  =   get_parms_for_input(inparms[1],bulk_geocode_append_input_idList)
        
            if(len(proc_parms) > 0) :
            
                append_to_csv_file_name     =   proc_parms[0]
                from dfcleanserQt.utils.Geocode.BulkGeocodeConsole import bulk_geocode_append_input_id
                cfg.set_config_value(bulk_geocode_append_input_id+"Parms",[append_to_csv_file_name])
        
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
            
                display_blank_line()
                display_status_note("Geocode Results appended successfully to csv file " + append_to_csv_file_name)
            
                cfg.set_config_value(cfg.BULK_GEOCODE_APPENDED_CSV_ID,append_to_csv_file_name,True)
            
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_bulkgeocode_openexcel_taskbar
                display_bulkgeocode_openexcel_taskbar(0) 
                display_blank_line()
                
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_base_taskbar
                display_base_taskbar()
                display_blank_line()
            
            else :
                get_exception_html(opstat,width=90,left=40,display=True)
                display_blank_line()
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_base_taskbar
                display_base_taskbar()
                    
                
        elif(cmd == GM.PROCESS_BULK_ERRORS_CSV_PROCESS) :
        
            import os
        
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import bulk_geocode_export_error_input_idList
            proc_parms  =   get_parms_for_input(inparms[1],bulk_geocode_export_error_input_idList)
            
            if(len(proc_parms) > 0) :
            
                if(len(proc_parms) > 0) :
                    csv_file_name   =   proc_parms[0]
                else :
                    csv_file_name   =   None
        
                if(not (csv_file_name is None)) :
                    #write out csv file 
                    try :
                        errors_df.to_csv(csv_file_name,index=False)
                    except Exception as e:
                        opstat.store_exception("Unable to export geocoding errors file ",e)
                        
                else :
                    opstat.set_errorMsg("No file path defined")
                    opstat.set_status(False)
        
            else :
                opstat.set_errorMsg("Invalid csv file to export to")
                opstat.set_status(False)
        
            if(opstat.get_status()) :
                
                display_blank_line()
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_base_taskbar
                display_base_taskbar()
            
                display_blank_line()
                display_status_note("Geocode Errors exported successfully to csv file ")
            
                cfg.set_config_value(cfg.BULK_ERRORS_EXPORTED_CSV_ID ,csv_file_name,True)

                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_bulkgeocode_openexcel_taskbar
                display_bulkgeocode_openexcel_taskbar(2) 
                display_blank_line()
            
            else :
                get_exception_html(opstat,width=90,left=40,display=True)
                display_blank_line()

                from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_base_taskbar
                display_base_taskbar()
 

    except Exception as e:
        opstat.store_exception("Unable to export geocoding results file ",e)
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_base_taskbar
        display_base_taskbar()
        display_blank_line()
        get_exception_html(opstat,width=90,left=40,display=True)



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding run parms validation methods 
#------------------------------------------------------------------
#------------------------------------------------------------------
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
        fparms    =   cfg.get_config_value(BGM.get_bulk_form_id(geocid,BGM.GEOCODER) + "Parms")
    
    if(not(fparms == None)) :
        
        if(geocid == GM.BingId)              : 
            GC.validate_bing_geocoder_parms(fparms,opstat,False)

        elif(geocid == GM.GoogleId)            :
            BG.validate_bulk_google_geocoder_parms(fparms,opstat)

    else :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No geocoder connect parms defined for validation")
        
    return(opstat)


def validate_bulk_parms(geocid,geotype,inputs,opstat) :
    """
    * --------------------------------------------------------
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geocid       - geocoder id
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}
    
    if(geocid == GM.GoogleId) :
        bulk_geocode_kwargs     =   validate_google_bulk_parms(geotype,inputs,opstat)       
                
    elif(geocid == GM.BingId) :
        bulk_geocode_kwargs     =   validate_bing_bulk_parms(geotype,inputs,opstat)  
    
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def validate_google_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}

    if(geotype == GM.QUERY) :

        try :
        
            fparms = get_parms_for_input(inputs,BG.bulk_google_query_input_idList)

            if(len(fparms[0]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No dataframe selected defined")

            else :

                if(opstat.get_status()) :
                    if(len(fparms[1]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No start row defined")

                if(opstat.get_status()) :

                    df_title    =   fparms[0]
                    df          =   cfg.get_dfc_dataframe_df(df_title)
            
                    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
                    cfg.set_config_value(BULK_GEOCODING_DF_TITLE,df_title)

                    cfg.set_current_chapter_df(cfg.SWBulkGeocodeUtility_ID,df,opstat)

                    # check if row id is in range
                    num_rows    =   len(df)
                    row_id      =   fparms[1]

                    if(len(row_id) > 0) :
                        try :
                            row_id  =   int(row_id)
                        except :
                            row_id  =   0

                        if((row_id < 0) or (row_id > num_rows)) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("starting row id is invalid")
                    else :
                        row_id = 0

                    if(opstat.get_status()) :
                        if(len(fparms[2]) == 0) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("No dataframe address column name(s) defined")
                
                    if(opstat.get_status()) :
                        if(len(fparms[3]) == 0) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("No lat lng column name(s) defined")

                    if(opstat.get_status()) :
            
                        bulk_geocode_kwargs.update({"dataframe_to_geocode_from" : fparms[0]})
                        bulk_geocode_kwargs.update({"starting_row_id" : fparms[1]})
                        bulk_geocode_kwargs.update({"dataframe_address_columns" : fparms[2]})
                        bulk_geocode_kwargs.update({"new_dataframe_lat_long_column_name(s)" : fparms[3]})
            
                        if(len(fparms[4]) > 0) :
                            bulk_geocode_kwargs.update({"save_geocoder_full_address_column_name" : fparms[4]})
                        else :
                            bulk_geocode_kwargs.update({"save_geocoder_full_address_column_name" : ""})
                
                        if(len(fparms[5]) > 0) :
                            bulk_geocode_kwargs.update({"region" : fparms[5]}) 
                        else :
                            bulk_geocode_kwargs.update({"region" : "US"})
                
                        if(len(fparms[6]) > 0) :
                            bulk_geocode_kwargs.update({"language" : fparms[6]}) 
                        else :
                            bulk_geocode_kwargs.update({"language" : "en"})

                        if(len(fparms[7]) > 0) :
                            if(int(fparms[7]) > len(df)) :
                                bulk_geocode_kwargs.update({"max_addresses_to_geocode" : len(df)}) 
                            else :
                                bulk_geocode_kwargs.update({"max_addresses_to_geocode" : fparms[7]})
                        else :
                            bulk_geocode_kwargs.update({"max_addresses_to_geocode" : len(df)}) 
                    
                        if(len(fparms[8]) > 0) :
                            if(int(fparms[8]) > 100) :
                                bulk_geocode_kwargs.update({"failure_limit_percent" : "2"}) 
                            else :
                                bulk_geocode_kwargs.update({"failure_limit_percent" : fparms[8]})
                        else :
                            bulk_geocode_kwargs.update({"failure_limit_percent" : "2"}) 
            
                        if(len(fparms[9]) > 0) :
                            if(int(fparms[9]) < 0) :
                                bulk_geocode_kwargs.update({"checkpoint_interval" : "10000"}) 
                            else :
                                bulk_geocode_kwargs.update({"checkpoint_interval" : fparms[9]})
                        else :
                            bulk_geocode_kwargs.update({"checkpoint_interval" : "10000"}) 

        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error validating parms")

                    
    else : # REVERSE

        try :
                
            # check the required reverse parms
            fparms = get_parms_for_input(inputs,BG.bulk_google_reverse_input_idList)
        
            if( (len(fparms[0]) == 0) and (len(fparms[1]) == 0) and (len(fparms[2]) == 0) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("No api key or client id and secret parm(s) defined")
            else :

                if(opstat.get_status()) :
                    if(len(fparms[1]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No start row defined")

                if(opstat.get_status()) :

                    df_title    =   fparms[0]
                    df          =   cfg.get_dfc_dataframe_df(df_title)
            
                    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
                    cfg.set_config_value(BULK_GEOCODING_DF_TITLE,df_title)

                    cfg.set_current_chapter_df(cfg.SWBulkGeocodeUtility_ID,df,opstat)

                    # check if row id is in range
                    num_rows    =   len(df)
                    row_id      =   fparms[1]

                    if(len(row_id) > 0) :
                        try :
                            row_id  =   int(row_id)
                        except :
                            row_id  =   0

                        if((row_id < 0) or (row_id > num_rows)) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("starting row id is invalid")
                    else :
                        row_id = 0

                    if(opstat.get_status()) :
                        if(len(fparms[2]) == 0) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("No dataframe address column name(s) defined")
                

                    if(opstat.get_status()) :
  
                
                        bulk_geocode_kwargs.update({"dataframe_to_geocode_from" : fparms[0]})
                        bulk_geocode_kwargs.update({"starting_row_id" : fparms[1]})
                        bulk_geocode_kwargs.update({"dataframe_lat_long_column_name(s)" : fparms[2]})

                        if(len(fparms[3]) > 0) :
                            bulk_geocode_kwargs.update({"full_address_column_name" : fparms[3]})
                        else :
                            bulk_geocode_kwargs.update({"full_address_column_name" : ""})
                        
                        if(len(fparms[4]) > 0) :
                            bulk_geocode_kwargs.update({"address_components_list" : fparms[4]})
                        else :
                            bulk_geocode_kwargs.update({"address_components_list" : ""})    

                        if(len(fparms[5]) > 0) :
                            bulk_geocode_kwargs.update({"address_components_length_flag" : fparms[5]})
                        else :
                            bulk_geocode_kwargs.update({"address_components_length_flag" : "short"})    
            
                        if(len(fparms[6]) > 0) :
                            bulk_geocode_kwargs.update({"valid_location_type(s)" : fparms[6]})
                        else :
                            bulk_geocode_kwargs.update({"valid_location_type(s)" : "[ROOFTOP]"})    
            
                        if(len(fparms[7]) > 0) :
                            bulk_geocode_kwargs.update({"language" : fparms[7]})
                        else :
                            bulk_geocode_kwargs.update({"language" : "en"})    
   
                        if(len(fparms[8]) > 0) :
                            bulk_geocode_kwargs.update({"max_lat_longs" : fparms[8]}) 
                        else :
                            bulk_geocode_kwargs.update({"max_lat_longs" : len(df)}) 
                
                        if(len(fparms[9]) > 0) :
                            bulk_geocode_kwargs.update({"failure_limit_percent" : fparms[9]}) 
                        else :
                            bulk_geocode_kwargs.update({"failure_limit_percent" : "2"})
                
                        if(len(fparms[10]) > 0) :
                            bulk_geocode_kwargs.update({"checkpoint_interval" : fparms[10]}) 
                        else :
                            bulk_geocode_kwargs.update({"checkpoint_interval" : "10000"}) 
    
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error validating parms")
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def validate_bing_bulk_parms(geotype,inputs,opstat) :
    """
    * --------------------------------------------------------
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}
    df_title                =   ""

    if(geotype == GM.REVERSE) :
        
        try :

            fparms = get_parms_for_input(inputs,BG.bulk_bing_reverse_input_idList)

            if(len(fparms[0]) == 0) :

                opstat.set_status(False)
                opstat.set_errorMsg("No dataframe selected defined")

            else :
                
                if(opstat.get_status()) :
                    if(len(fparms[1]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No start row defined")

                if(opstat.get_status()) :

                    df_title    =   fparms[0]
                    df          =   cfg.get_dfc_dataframe_df(df_title)
            
                    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
                    cfg.set_config_value(BULK_GEOCODING_DF_TITLE,df_title)

                    cfg.set_current_chapter_df(cfg.SWBulkGeocodeUtility_ID,df,opstat)

                    # check if row id is in range
                    num_rows    =   len(df)
                    row_id      =   fparms[1]

                    if(len(row_id) > 0) :
                        try :
                            row_id  =   int(row_id)
                        except :
                            row_id  =   0

                        if((row_id < 0) or (row_id > num_rows)) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("starting row id is invalid")
                    else :
                        row_id = 0

                    if(opstat.get_status()) :
                        if(len(fparms[2]) == 0) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("No dataframe coords column name(s) defined")
                
                    if(opstat.get_status()) :
                        if(len(fparms[3]) == 0) :
                            opstat.set_status(False)
                            opstat.set_errorMsg("No dataframe address column name(s) defined")


                    if(opstat.get_status()) :
                
                        bulk_geocode_kwargs.update({"dataframe_to_geocode" : fparms[0]})
                        bulk_geocode_kwargs.update({"starting_row_id" : fparms[1]})
                        bulk_geocode_kwargs.update({"dataframe_lat_long_column_name(s)" : fparms[2]})
                        bulk_geocode_kwargs.update({"dataframe_column_name_for_geocode_address" : fparms[3]})

                        # addr components 
                        if(len(fparms[4]) > 0) :
                            bulk_geocode_kwargs.update({"address_components_to_retrieve" : fparms[4]}) 
                        else :
                            bulk_geocode_kwargs.update({"address_components_to_retrieve" : "Full Address Only"})

                        # culture    
                        if( (len(fparms[5]) > 0) and (not(fparms[5] == "None")) ) :
                            culture     =  fparms[5] 
                            bulk_geocode_kwargs.update({"culture" : culture})
                        else :
                            bulk_geocode_kwargs.update({"culture" : 'None'})
                
                        # country code
                        if(len(fparms[6]) > 0) :
                            countrycode    =   fparms[6]
                            bulk_geocode_kwargs.update({"include_country_code" : countrycode})    
                        else :
                            bulk_geocode_kwargs.update({"include_country_code" : 'None'}) 
                
                        # num geocodes
                        if(len(fparms[7]) > 0) :
                            bulk_geocode_kwargs.update({"max_lat_longs" : fparms[7]}) 
                        else :
                            df  =   cfg.get_dfc_dataframe_df(fparms[0])
                            bulk_geocode_kwargs.update({"max_lat_longs" : len(df)})
            
                        # error limit
                        if(len(fparms[8]) > 0) :
                            bulk_geocode_kwargs.update({"failure_limit_percent" : int(fparms[8])}) 
                        else :
                            bulk_geocode_kwargs.update({"failure_limit_percent" : 5})
                
                        # checkpoint interval
                        if(len(fparms[9]) > 0) :
                            bulk_geocode_kwargs.update({"checkpoint_interval" : int(fparms[9])}) 
                        else :
                            bulk_geocode_kwargs.update({"checkpoint_interval" : 10000})

        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error validating parms")
                    
    else : # QUERY
        
        try :
                
            # check the required query parms
            fparms = get_parms_for_input(inputs,BG.bulk_bing_query_input_idList)

            if(len(fparms[0]) == 0) :

                opstat.set_status(False)
                opstat.set_errorMsg("No dataframe selected defined")
            
            else :
                
                if(opstat.get_status()) :
                    if(len(fparms[1]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No start row defined")
      
            # validate non required parms            
            if(opstat.get_status()) :

                df_title    =   fparms[0]
                df          =   cfg.get_dfc_dataframe_df(df_title)
            
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
                cfg.set_config_value(BULK_GEOCODING_DF_TITLE,df_title)

                cfg.set_current_chapter_df(cfg.SWBulkGeocodeUtility_ID,df,opstat)

                # check if row id is in range
                num_rows    =   len(df)
                row_id      =   fparms[1]

                if(len(row_id) > 0) :
                    try :
                        row_id  =   int(row_id)
                    except :
                        row_id  =   0

                    if((row_id < 0) or (row_id > num_rows)) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("starting row id is invalid")
                else :
                    row_id = 0

                if(opstat.get_status()) :
                
                    bulk_geocode_kwargs.update({"dataframe_to_geocode" : fparms[0]})
                    bulk_geocode_kwargs.update({"starting_row_id" : fparms[1]})
                    bulk_geocode_kwargs.update({"dataframe_address_columns" : fparms[2]})
                    bulk_geocode_kwargs.update({"new_dataframe_lat_long_column_name(s)" : fparms[3]})

                    # full address
                    if(len(fparms[4]) > 0) :
                        bulk_geocode_kwargs.update({"save_geocoder_full_address_column_name" : fparms[4]}) 
                    else :
                        bulk_geocode_kwargs.update({"save_geocoder_full_address_column_name" : "None"})
            
                    # user location
                    if(len(fparms[5]) > 0) :
                        bulk_geocode_kwargs.update({"user_location" : fparms[5]}) 
                    else :
                        bulk_geocode_kwargs.update({"user_location" : "None"})
                
                    # culture
                    if(len(fparms[6]) > 0) :
                        sep     =  fparms[6].find(":") 
                        bulk_geocode_kwargs.update({"culture" : fparms[6][(sep +1):]}) 
                    else :
                        bulk_geocode_kwargs.update({"culture" : "en"})

                    # neighborhood
                    if(len(fparms[7]) > 0) :
                        bulk_geocode_kwargs.update({"include_neighborhood" : fparms[7]}) 
                    else :
                        bulk_geocode_kwargs.update({"include_neighborhood" : "False"})
                
                    # country code
                    if(len(fparms[8]) > 0) :
                        bulk_geocode_kwargs.update({"include_country_code" : fparms[8]}) 
                    else :
                        bulk_geocode_kwargs.update({"include_country_code" : "False"})

                    # num geocodes
                    if(len(fparms[9]) > 0) :
                        bulk_geocode_kwargs.update({"max_addresses_to_geocode" : fparms[9]}) 
                    else :
                        df  =   cfg.get_dfc_dataframe_df(fparms[0])
                        bulk_geocode_kwargs.update({"max_addresses_to_geocode" : len(df)})

                    # error limit
                    if(len(fparms[10]) > 0) :
                        bulk_geocode_kwargs.update({"failure_limit_percent" : int(fparms[10])}) 
                    else :
                        bulk_geocode_kwargs.update({"failure_limit_percent" : 5})
                
                    # checkpoint interval
                    if(len(fparms[11]) > 0) :
                        bulk_geocode_kwargs.update({"checkpoint_interval" : fparms[11]}) 
                    else :
                        bulk_geocode_kwargs.update({"checkpoint_interval" : str(10000)})

        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error validating parms")
                
    if(opstat.get_status()) :  

        if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
            log_debug_dfc(-1,"[validate_bing_bulk_parms] \n    " + str(bulk_geocode_kwargs))

        return(bulk_geocode_kwargs)
    else :
        return(None)

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding display geocode run stats 
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def refresh_bulk_geocode_console() :

    geocid   =   BGM.get_geocode_runner_id() 
    geotype  =   BGM.get_geocode_runner_type() 
    
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
        log_debug_dfc(-1,"[refresh_bulk_geocode_console] " + str(geocid) + " " + str(geotype))
    
    if(geotype == BGM.QUERY) :
        get_bulk_coords(geocid,None,True)
    else :
        get_bulk_addresses(geocid,None,True)



def display_bulk_geocode_run_stats(width=None,left=None) :
    """
    * --------------------------------------------------------
    * function : display bulk geocode run stats
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    run_time    =   BGM.get_geocode_run_total_time()
        
    if(run_time > 0) :
        geocodes_per_sec    =   str(round(BGM.get_geocode_runner_results_log().get_results_count()/run_time,2))
    else :
        geocodes_per_sec    =   0

    labels      =   ["Total Geocode Results","Total Geocode Errors","Total Run Time - Seconds","Geocodes/Second"]
    values      =   [str(BGM.get_geocode_runner_results_log().get_results_count()),
                         str(BGM.get_geocode_runner_error_log().get_error_count()),
                         str(BGM.get_geocode_run_total_time()),
                         str(geocodes_per_sec)]
        
    stats_html  =   displayParms("Bulk Geocoding Run Stats",labels,values,"gstat",width,left)

    return(stats_html)

def display_bulk_geocode_run_parms(geocoderid,geotype,runparms,width=None,left=None) :
    """
    * --------------------------------------------------------
    * function : display bulk geocode run parms
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    labels      =   list(runparms.keys())
    values      =   []
    for i in range(len(labels)) :
        if(labels[i] == "failure_limit_percent") :
            values.append(str(runparms.get(labels[i])))
        else :
            values.append(runparms.get(labels[i]))


    if(geocoderid == BGM.BingId) :
        if(geotype == BGM.QUERY) :
            parms_title     =   "Bing Bulk Geocode Query Run Parameters"
        else :
            parms_title     =   "Bing Bulk Geocode Reverse Run Parameters"
    else :
        if(geotype == BGM.QUERY) :
            parms_title     =   "Google Bulk Geocode Query Run Parameters"
        else :
            parms_title     =   "Google Bulk Geocode Reverse Run Parameters"

    parms_html  =   displayParms(parms_title,labels,values,"gstat",width,left)

    return(parms_html)

def display_bulk_geocode_df_parms(width=None,left=None) :
    """
    * --------------------------------------------------------
    * function : display bulk geocode df data
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
    df_title    =   cfg.get_config_value(BULK_GEOCODING_DF_TITLE)

    labels      =   ["user df to generate geocodes for","df to store retrieved geocode data","df to store geocode errors"]
    values      =   [df_title,BGM.GEOCODING_RESULTS_DF_TITLE,BGM.GEOCODING_ERROR_LOG_DF_TITLE]
    dfs_html    =   displayParms("dfs used in geocoding",labels,values,"gstat",width,left)

    return(dfs_html)

def add_geocode_results_to_user_df(geotype) :
    """
    * --------------------------------------------------------
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    current_geocoder            =   cfg.get_config_value(BGM.BULK_GEOCODE_CURRENT_GEOCODER)
    current_geocode_type        =   cfg.get_config_value(BGM.BULK_GEOCODE_CURRENT_GEOTYPE)
    current_geocode_runparms    =   cfg.get_config_value(BGM.BULK_GEOCODE_CURRENT_RUNPARMS)
    current_geocode_addrparms   =   cfg.get_config_value(BGM.BULK_GEOCODE_CURRENT_ADDRPARMS)

    # get geocoding results 
    results_df          =   cfg.get_dfc_dataframe_df(BGM.GEOCODING_RESULTS_DF_TITLE)
    reults_df_columns   =   results_df.columns.tolist()

    # get geocoding results 
    errors_df           =   cfg.get_dfc_dataframe_df(BGM.GEOCODING_ERROR_LOG_DF_TITLE)
    errors_df_columns   =   errors_df.columns.tolist()
    
    from dfcleanser.common.common_utils import displayHTML, display_blank_line
    display_blank_line()

    if(current_geocoder == BGM.BingId) :

        if(current_geocode_type == BGM.QUERY) :

            geocoding_adjust_title_html      =   "<div class='dfcleanser-common-grid-header'>Merge Retrieved Geocode Results</div>"


            from dfcleanser.common.html_widgets import (InputForm)

 
            from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_bing_query_adjust_input_id,bulk_bing_query_adjust_input_idList,bulk_bing_query_adjust_input_labelList,
                                                                 bulk_bing_query_adjust_input_typeList,bulk_bing_query_adjust_input_placeholderList,
                                                                 bulk_bing_query_adjust_input_jsList,bulk_bing_query_adjust_input_reqList)
            

            cfg.set_config_value(bulk_bing_query_adjust_input_id+"Parms",[current_geocode_runparms.get("new_dataframe_lat_long_column_name(s)"),
                                                                          "nan","",
                                                                          current_geocode_runparms.get("save_geocoder_full_address_column_name")])
            
            geocoding_input_form   =  InputForm(bulk_bing_query_adjust_input_id,
                                                bulk_bing_query_adjust_input_idList,
                                                bulk_bing_query_adjust_input_labelList,
                                                bulk_bing_query_adjust_input_typeList,
                                                bulk_bing_query_adjust_input_placeholderList,
                                                bulk_bing_query_adjust_input_jsList,
                                                bulk_bing_query_adjust_input_reqList)
            
            geocoding_input_form.set_gridwidth(640)
            geocoding_input_form.set_custombwidth(240)
    
            geocoding_input_form.set_fullparms(True)

            geocoding_input_html = ""
            geocoding_input_html = geocoding_input_form.get_html() 

            msg     =   "You can now adjust the above parms bfore merging the retrieved geocoding data."
            from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html
            adjust_notes_html    =   get_status_note_msg_html(msg, width=640, left=0, fontsize=12, display=False)

            from dfcleanser.common.common_utils import display_generic_grid
            gridclasses     =   ["dfc-top","dfc-middle","dfc-bottom"]
            gridhtmls       =   [geocoding_adjust_title_html,geocoding_input_html,adjust_notes_html]
                    
            display_generic_grid("df-geocode-bing-bulk-query-adjust-wrapper",gridclasses,gridhtmls)

        else :

            geocoding_adjust_title_html      =   "<div class='dfcleanser-common-grid-header'>Merge Retrieved Geocode Results</div>"


            from dfcleanser.common.html_widgets import (InputForm)

 
            from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_bing_reverse_adjust_input_id,bulk_bing_reverse_adjust_input_idList,bulk_bing_reverse_adjust_input_labelList,
                                                                 bulk_bing_reverse_adjust_input_typeList,bulk_bing_reverse_adjust_input_placeholderList,
                                                                 bulk_bing_reverse_adjust_input_jsList,bulk_bing_reverse_adjust_input_reqList)
            
            addr_comps_option   =   BGM.dfc_Geocode_Runner.get_runParms().get("address_components_to_retrieve",None)

            if(addr_comps_option == "Full Address And Components") :
                addr_comps  =   "[locality,state,county,zipcode]"
            else :
                addr_comps  =   "[]"

            cfg.set_config_value(bulk_bing_reverse_adjust_input_id+"Parms",[current_geocode_runparms.get("dataframe_column_name_for_geocode_address"),
                                                                            "nan","",addr_comps])
            
            geocoding_input_form   =  InputForm(bulk_bing_reverse_adjust_input_id,
                                                bulk_bing_reverse_adjust_input_idList,
                                                bulk_bing_reverse_adjust_input_labelList,
                                                bulk_bing_reverse_adjust_input_typeList,
                                                bulk_bing_reverse_adjust_input_placeholderList,
                                                bulk_bing_reverse_adjust_input_jsList,
                                                bulk_bing_reverse_adjust_input_reqList)
            
            geocoding_input_form.set_gridwidth(640)
            geocoding_input_form.set_custombwidth(240)
    
            geocoding_input_form.set_fullparms(True)

            geocoding_input_html = ""
            geocoding_input_html = geocoding_input_form.get_html() 

            msg     =   "You can now adjust the above parms bfore merging the retrieved geocoding data."
            from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html
            adjust_notes_html    =   get_status_note_msg_html(msg, width=640, left=0, fontsize=12, display=False)

            from dfcleanser.common.common_utils import display_generic_grid
            gridclasses     =   ["dfc-top","dfc-middle","dfc-bottom"]
            gridhtmls       =   [geocoding_adjust_title_html,geocoding_input_html,adjust_notes_html]
                    
            display_generic_grid("df-geocode-bing-bulk-query-adjust-wrapper",gridclasses,gridhtmls)


    else :

        if(current_geocode_type == BGM.QUERY) :

            geocoding_adjust_title_html      =   "<div class='dfcleanser-common-grid-header'>Merge Retrieved Geocode Results</div>"


            from dfcleanser.common.html_widgets import (InputForm)

 
            from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_google_query_adjust_input_id,bulk_google_query_adjust_input_idList,bulk_google_query_adjust_input_labelList,
                                                                 bulk_google_query_adjust_input_typeList,bulk_google_query_adjust_input_placeholderList,
                                                                 bulk_google_query_adjust_input_jsList,bulk_google_query_adjust_input_reqList)
            

            cfg.set_config_value(bulk_google_query_adjust_input_id+"Parms",[current_geocode_runparms.get("new_dataframe_lat_long_column_name(s)"),
                                                                            "nan","",  
                                                                            current_geocode_runparms.get("save_geocoder_full_address_column_name")])
            
            geocoding_input_form   =  InputForm(bulk_google_query_adjust_input_id,
                                                bulk_google_query_adjust_input_idList,
                                                bulk_google_query_adjust_input_labelList,
                                                bulk_google_query_adjust_input_typeList,
                                                bulk_google_query_adjust_input_placeholderList,
                                                bulk_google_query_adjust_input_jsList,
                                                bulk_google_query_adjust_input_reqList)
            
            geocoding_input_form.set_gridwidth(640)
            geocoding_input_form.set_custombwidth(240)
    
            geocoding_input_form.set_fullparms(True)

            geocoding_input_html = ""
            geocoding_input_html = geocoding_input_form.get_html() 

            msg     =   "You can now adjust the above parms bfore merging the retrieved geocoding data."
            from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html
            adjust_notes_html    =   get_status_note_msg_html(msg, width=640, left=0, fontsize=12, display=False)

            from dfcleanser.common.common_utils import display_generic_grid
            gridclasses     =   ["dfc-top","dfc-middle","dfc-bottom"]
            gridhtmls       =   [geocoding_adjust_title_html,geocoding_input_html,adjust_notes_html]
                    
            display_generic_grid("df-geocode-bing-bulk-query-adjust-wrapper",gridclasses,gridhtmls)

        else :

            geocoding_adjust_title_html      =   "<div class='dfcleanser-common-grid-header'>Merge Retrieved Geocode Results</div>"


            from dfcleanser.common.html_widgets import (InputForm)

 
            from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_google_reverse_adjust_input_id,bulk_google_reverse_adjust_input_idList,bulk_google_reverse_adjust_input_labelList,
                                                                 bulk_google_reverse_adjust_input_typeList,bulk_google_reverse_adjust_input_placeholderList,
                                                                 bulk_google_reverse_adjust_input_jsList,bulk_google_reverse_adjust_input_reqList)
            

            cfg.set_config_value(bulk_google_reverse_adjust_input_id+"Parms",[current_geocode_runparms.get("full_address_column_name"),
                                                                              "nan","",
                                                                              current_geocode_runparms.get("address_components_list")])
            
            geocoding_input_form   =  InputForm(bulk_google_reverse_adjust_input_id,
                                                bulk_google_reverse_adjust_input_idList,
                                                bulk_google_reverse_adjust_input_labelList,
                                                bulk_google_reverse_adjust_input_typeList,
                                                bulk_google_reverse_adjust_input_placeholderList,
                                                bulk_google_reverse_adjust_input_jsList,
                                                bulk_google_reverse_adjust_input_reqList)
            
            geocoding_input_form.set_gridwidth(640)
            geocoding_input_form.set_custombwidth(240)
    
            geocoding_input_form.set_fullparms(True)

            geocoding_input_html = ""
            geocoding_input_html = geocoding_input_form.get_html() 

            msg     =   "You can now adjust the above parms bfore merging the retrieved geocoding data."
            from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html
            adjust_notes_html    =   get_status_note_msg_html(msg, width=640, left=0, fontsize=12, display=False)

            from dfcleanser.common.common_utils import display_generic_grid
            gridclasses     =   ["dfc-top","dfc-middle","dfc-bottom"]
            gridhtmls       =   [geocoding_adjust_title_html,geocoding_input_html,adjust_notes_html]
                    
            display_generic_grid("df-geocode-bing-bulk-query-adjust-wrapper",gridclasses,gridhtmls)


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  merge results objects
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def merge_bulk_results(geocode_id,geocode_type,parms) :
    """
    * -----------------------------------------------------------
    * function : merge the retrived bulk results in user df
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    if(GEOCODE_TRACE_GET_GEOCODE)  :   
        log_debug_dfc(-1,"[merge_bulk_results] : " + str(geocode_id) + " " + str(geocode_type))
        log_debug_dfc(-1,"[merge_bulk_results] : " + str(parms))

    if(DEBUG_MERGE) :
        print("merge_bulk_results : geocode_id ",geocode_id)
        print("merge_bulk_results : geocode_type ",geocode_type)
        print("merge_bulk_results : parms ",parms)
    
    runParms    =   BGM.dfc_Geocode_Runner.get_runParms()
    if(geocode_id == GM.GoogleId) :
        user_df_title   =   runParms.get("dataframe_to_geocode_from")
    else :
        user_df_title   =   runParms.get("dataframe_to_geocode")

    display_merge_console(0,user_df_title)

    df_results_log_title    =   BGM.GEOCODING_RESULTS_DF_TITLE
    df_error_log_title      =   BGM.GEOCODING_ERROR_LOG_DF_TITLE
    
    user_df         =   cfg.get_dfc_dataframe_df(user_df_title)
    results_df      =   cfg.get_dfc_dataframe_df(df_results_log_title)
    error_df        =   cfg.get_dfc_dataframe_df(df_error_log_title)

    if(geocode_id == GM.GoogleId) :

        if(geocode_type == GM.QUERY) :
            process_google_bulk_query_merge(parms,runParms,user_df,results_df,error_df)
        else : #reverse
            process_google_bulk_reverse_merge(parms,runParms,user_df,results_df,error_df)

    else :

        if(geocode_type == GM.QUERY) :
            process_bing_bulk_query_merge(parms,runParms,user_df,results_df,error_df)
        else : #reverse
            process_bing_bulk_reverse_merge(parms,runParms,user_df,results_df,error_df)


def process_google_bulk_query_merge(parms,runParms,user_df,results_df,error_df) :
    """
    * --------------------------------------------------------
    * function : store bulk results from google query 
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fparms  =   get_parms_for_input(parms,BG.bulk_google_query_adjust_input_idList)

    results_lat_lng_col_name        =   runParms.get("new_dataframe_lat_long_column_name(s)") 
    results_full_address_col_name   =   runParms.get("save_geocoder_full_address_column_name") 

    merge_lat_lng_col_name          =   fparms[0]
    merge_error_value               =   fparms[1]
    merge_empty_value               =   fparms[2]
    merge_full_address_col_name     =   fparms[3]

    results_lat_lng_col_name_list   =   get_lat_lng_col_names(results_lat_lng_col_name)
    merge_lat_lng_col_name_list     =   get_lat_lng_col_names(merge_lat_lng_col_name)

    if(DEBUG_MERGE) :

        print("results_lat_lng_col_name",results_lat_lng_col_name)
        print("results_full_address_col_name",results_full_address_col_name)
        print("merge_lat_lng_col_name",merge_lat_lng_col_name)
        print("merge_error_value",merge_error_value)
        print("merge_empty_value",merge_empty_value)
        print("merge_full_address_col_name",merge_full_address_col_name)
        print("results_lat_lng_col_name_list",results_lat_lng_col_name_list)
        print("merge_lat_lng_col_name_list",merge_lat_lng_col_name_list)

    
    user_df_col_names   =   list(user_df.columns)

    # Check if lat lang columns already exist
    for i in range(len(merge_lat_lng_col_name_list)) :
        if(not(merge_lat_lng_col_name_list[i] in user_df_col_names)) :
            new_column_values   =   []
            for j in range(len(user_df)) :
                new_column_values.append(merge_empty_value)
            user_df[merge_lat_lng_col_name_list[i]]     =   new_column_values

    # Check if full address column exists
    if(not(merge_full_address_col_name in user_df_col_names)) :
        new_column_values   =   []
        for j in range(len(user_df)) :
            new_column_values.append(merge_empty_value)
        user_df[merge_full_address_col_name]     =   new_column_values
    
    # get indices of new columns
    user_df_col_names   =   list(user_df.columns)

    full_address_index  =   -1
    for j in range(len(user_df_col_names)) :
        if(user_df_col_names[j] == merge_full_address_col_name) :
            full_address_index  =   j
            break

    error_indices   =   []

    if(len(merge_lat_lng_col_name_list) == 1) :

        lat_lng_index  =   -1
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[0]) :
                lat_lng_index  =   j
                break

        error_indices.append(lat_lng_index)

    else :

        lat_index  =   -1 
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[0]) :
                lat_index  =   j
                break

        lng_index  =   -1 
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[1]) :
                lng_index  =   j
                break

        error_indices.append(lat_index)
        error_indices.append(lng_index)

    if(DEBUG_MERGE) :

        print("\n[process_bing_bulk_query_merge][full_address_index]",full_address_index)
        if(len(merge_lat_lng_col_name_list) == 1) :
            print("\n[process_bing_bulk_query_merge][lat_lng_index]",lat_lng_index)
        else:
            print("\n[process_bing_bulk_query_merge][lat_index]",lat_index)
            print("\n[process_bing_bulk_query_merge][lng_index]",lng_index)

    # insert values into columns
    for i in range(len(results_df)) :

        row_id      =   results_df.iloc[i,0]

        if(len(results_lat_lng_col_name_list) == 1) :

            if(len(merge_lat_lng_col_name_list) == 1) :
                
                lat_lng_value       =   results_df.iloc[i,2]
            
            else :

                split_values    =   split_lat_lng_col_values(results_df.iloc[i,2]) 
                lat_value       =   split_values[0]
                lng_value       =   split_values[1]

            full_address_value  =   results_df.iloc[i,3]

        else:

            lat_value           =   results_df.iloc[i,2]
            lng_value           =   results_df.iloc[i,3]

            if(len(merge_lat_lng_col_name_list) == 1) :
                
                lat_lng_value       =   (lat_value,lng_value)

            full_address_value  =   results_df.iloc[i,4]

        # add value to the user df
        user_df.iloc[row_id,full_address_index]     =   full_address_value

        if(len(merge_lat_lng_col_name_list) == 1) :
            user_df.iloc[row_id,lat_lng_index]     =   lat_lng_value 
        else :
            user_df.iloc[row_id,lat_index]     =   lat_value 
            user_df.iloc[row_id,lng_index]     =   lng_value 

        current_count       =   (i + 1)
        current_percent     =   int( ( current_count / len(results_df) ) * 100 )
        set_merge_bar_value(current_count,current_percent) 

    merge_errors(user_df,error_df,error_indices,merge_error_value) 

    current_count       =   len(results_df) + len(error_df)
    current_percent     =   int( ( current_count / (len(results_df) + len(error_df)) ) * 100 )
    set_merge_bar_value(current_count,current_percent)        


def process_google_bulk_reverse_merge(parms,runParms,user_df,results_df,error_df) :
    """
    * --------------------------------------------------------
    * function : store bulk results from google query 
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fparms  =   get_parms_for_input(parms,BG.bulk_google_reverse_adjust_input_idList)
            
    results_full_address_col_name   =  runParms.get("full_address_column_name") 
    results_addr_comps              =  runParms.get("address_components_list")  

    merge_full_address_col_name     =   fparms[0]
    merge_error_value               =   fparms[1]
    merge_empty_value               =   fparms[2]
    merge_addr_comps                =   fparms[3]

    if(DEBUG_MERGE) :

        print("results_addr_comps",results_addr_comps)
        print("results_full_address_col_name",results_full_address_col_name)
        print("merge_addr_comps",type(merge_addr_comps),merge_addr_comps)
        print("merge_error_value",merge_error_value)
        print("merge_empty_value",merge_empty_value)
        print("merge_full_address_col_name",merge_full_address_col_name)


    # Check if lat lang columns already exist
    user_df_col_names   =   list(user_df.columns)

    # Check if full address column exists
    if(not(merge_full_address_col_name in user_df_col_names)) :
        new_column_values   =   []
        for j in range(len(user_df)) :
            new_column_values.append(merge_empty_value)
        user_df[merge_full_address_col_name]     =   new_column_values

    merge_addr_comps    =   get_google_addr_comps(merge_addr_comps)
    
    if(DEBUG_MERGE) :
        print("\nmerge_addr_comps",type(merge_addr_comps),merge_addr_comps)
        print("user_df_col_names\n",user_df_col_names)


    if( (type(merge_addr_comps) == list)  and (len(merge_addr_comps) > 0) ):
        
        for j in range(len(merge_addr_comps)) :
            if(len(merge_addr_comps[j]) > 0) :
                if(not(merge_addr_comps[j] in user_df_col_names)) :
                    new_column_values   =   []
                    for k in range(len(user_df)) :
                        new_column_values.append(merge_empty_value)

                    user_df[merge_addr_comps[j]]     =   new_column_values

    # get indices of new olumn values
    user_df_col_names   =   list(user_df.columns)

    if(DEBUG_MERGE) :
        print("\nmerge_addr_comps",type(merge_addr_comps),merge_addr_comps)
        print("user_df_col_names",user_df_col_names)

    error_indices   =   []

    full_address_index  =   -1
    for i in range(len(user_df_col_names)) :
        if(user_df_col_names[i] == merge_full_address_col_name) :
            full_address_index  =   i
            break

    error_indices.append(full_address_index)

    if( (type(merge_addr_comps) == list)  and (len(merge_addr_comps) > 0) ):

        merge_addr_comps_indices    =   []

        for i in range(len(merge_addr_comps)) :
            for j in range(len(user_df_col_names)) :
                if(user_df_col_names[j] == merge_addr_comps[i]) :
                    merge_addr_comps_indices.append(j)
                    break
   
    if(DEBUG_MERGE) :
        print("\ncols list",user_df_col_names)
        print("[process_google_bulk_query_merge][full_address_index]",full_address_index)
        if(len(merge_addr_comps) > 1) :
            print("[process_google_bulk_query_merge][merge_addr_comps_indices]",merge_addr_comps_indices)

    # insert values into columns
    for i in range(len(results_df)) :

        row_id              =   results_df.iloc[i,0]
        full_address_value  =   results_df.iloc[i,2]

        addr_comp_values    =   []

        if(type(merge_addr_comps) == list) :
            for j in range(len(merge_addr_comps)) :
                addr_comp_values.append(results_df.iloc[i,(3+j)])

        if(DEBUG_MERGE) :
            print("\naddr_comp_values",addr_comp_values)
        
        # add value to the user df
        user_df.iloc[row_id,full_address_index]     =   full_address_value

        if(len(merge_addr_comps) > 0) :
            for i in range(len(merge_addr_comps)) :
                user_df.iloc[row_id,merge_addr_comps_indices[i]]     =   addr_comp_values[i] 
        
        current_count       =   (i + 1)
        current_percent     =   int( ( current_count / len(results_df) ) * 100 )
        set_merge_bar_value(current_count,current_percent)        
    
    merge_errors(user_df,error_df,error_indices,merge_error_value) 

    current_count       =   len(results_df) + len(error_df)
    current_percent     =   int( ( current_count / (len(results_df) + len(error_df)) ) * 100 )
    set_merge_bar_value(current_count,current_percent)        


def process_bing_bulk_query_merge(parms,runParms,user_df,results_df,error_df) :
    """
    * --------------------------------------------------------
    * function : store bulk results from google query 
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fparms  =   get_parms_for_input(parms,BG.bulk_bing_query_adjust_input_idList)

    results_lat_lng_col_name        =  runParms.get("new_dataframe_lat_long_column_name(s)") 
    results_full_address_col_name   =  runParms.get("save_geocoder_full_address_column_name") 

    merge_lat_lng_col_name          =   fparms[0]
    merge_error_value               =   fparms[1]
    merge_empty_value               =   fparms[2]
    merge_full_address_col_name     =   fparms[3]

    results_lat_lng_col_name_list   =   get_lat_lng_col_names(results_lat_lng_col_name)
    merge_lat_lng_col_name_list     =   get_lat_lng_col_names(merge_lat_lng_col_name)

    if(DEBUG_MERGE) :
        print("[results_lat_lng_col_name]",results_lat_lng_col_name)
        print("[merge_lat_lng_col_name]",merge_lat_lng_col_name)
        print("[results_lat_lng_col_name_list]",results_lat_lng_col_name_list)
        print("[merge_lat_lng_col_name_list]",merge_lat_lng_col_name_list)

    # Check if lat lang columns already exist
    user_df_col_names   =   list(user_df.columns)
    
    # Check if full address column exists
    if(not(merge_full_address_col_name in user_df_col_names)) :
        new_column_values   =   []
        for j in range(len(user_df)) :
            new_column_values.append(merge_empty_value)
        user_df[merge_full_address_col_name]     =   new_column_values

    for i in range(len(merge_lat_lng_col_name_list)) :
        if(not(merge_lat_lng_col_name_list[i] in user_df_col_names)) :
            new_column_values   =   []
            for j in range(len(user_df)) :
                new_column_values.append(merge_empty_value)
            user_df[merge_lat_lng_col_name_list[i]]     =   new_column_values

    # get indices of new columns
    user_df_col_names   =   list(user_df.columns)

    error_indices   =   []

    full_address_index  =   -1
    for j in range(len(user_df_col_names)) :
        if(user_df_col_names[j] == merge_full_address_col_name) :
            full_address_index  =   j
            break

    if(len(merge_lat_lng_col_name_list) == 1) :

        lat_lng_index  =   -1
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[0]) :
                lat_lng_index  =   j
                break

        error_indices.append(lat_lng_index)

    else :

        lat_index  =   -1 
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[0]) :
                lat_index  =   j
                break

        lng_index  =   -1 
        for j in range(len(user_df_col_names)) :
            if(user_df_col_names[j] == merge_lat_lng_col_name_list[1]) :
                lng_index  =   j
                break

        error_indices.append(lat_index)
        error_indices.append(lng_index)

    if(DEBUG_MERGE) :

        print("\n[process_bing_bulk_query_merge][full_address_index]",full_address_index)
        if(len(merge_lat_lng_col_name_list) == 1) :
            print("\n[process_bing_bulk_query_merge][lat_lng_index]",lat_lng_index)
        else:
            print("\n[process_bing_bulk_query_merge][lat_index]",lat_index)
            print("\n[process_bing_bulk_query_merge][lng_index]",lng_index)

    # insert values into columns
    for i in range(len(results_df)) :

        row_id      =   results_df.iloc[i,0]

        if(len(results_lat_lng_col_name_list) == 1) :

            if(len(merge_lat_lng_col_name_list) == 1) :
                
                lat_lng_value       =   results_df.iloc[i,2]
            
            else :

                split_values    =   split_lat_lng_col_values(results_df.iloc[i,2]) 
                lat_value       =   split_values[0]
                lng_value       =   split_values[1]

            full_address_value  =   results_df.iloc[i,3]

        else:

            lat_value           =   results_df.iloc[i,2]
            lng_value           =   results_df.iloc[i,3]

            if(len(merge_lat_lng_col_name_list) == 1) :
                
                lat_lng_value       =   (lat_value,lng_value)

            full_address_value  =   results_df.iloc[i,4]

        if(DEBUG_MERGE):
            print("\n[process_google_bulk_query_merge][rowid]",type(row_id),row_id)
            if(len(merge_lat_lng_col_name_list) == 1) :
                print("[process_google_bulk_query_merge][lat_lng_value]",type(lat_lng_value),lat_lng_value)
            else :
                print("[process_google_bulk_query_merge][lat_value]",type(lat_value),lat_value)
                print("[process_google_bulk_query_merge][lng_value]",type(lng_value),lng_value)
            print("[process_google_bulk_query_merge][full_address_value]",type(full_address_value),full_address_value)  
        
        # add value to the user df
        user_df.iloc[row_id,full_address_index]     =   full_address_value

        if(len(merge_lat_lng_col_name_list) == 1) :
            user_df.iloc[row_id,lat_lng_index]     =   lat_lng_value 
        else :
            user_df.iloc[row_id,lat_index]     =   lat_value 
            user_df.iloc[row_id,lng_index]     =   lng_value 

        current_count       =   (i + 1)
        current_percent     =   int( ( current_count / len(results_df) ) * 100 )
        set_merge_bar_value(current_count,current_percent)        
    
    merge_errors(user_df,error_df,error_indices,merge_error_value) 
  
    current_count       =   len(results_df) + len(error_df)
    current_percent     =   int( ( current_count / (len(results_df) + len(error_df)) ) * 100 )
    set_merge_bar_value(current_count,current_percent)        


def process_bing_bulk_reverse_merge(parms,runParms,user_df,results_df,error_df) :
    """
    * --------------------------------------------------------
    * function : store bulk results from bing query 
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fparms  =   get_parms_for_input(parms,BG.bulk_bing_reverse_adjust_input_idList)
            
    results_full_address_col_name   =  runParms.get("dataframe_column_name_for_geocode_address") 
    results_addr_comps              =  runParms.get("address_components_to_retrieve")  

    merge_full_address_col_name     =   fparms[0]
    merge_error_value               =   fparms[1]
    merge_empty_value               =   fparms[2]
    merge_addr_comps                =   fparms[3]

    if(DEBUG_MERGE) :
        print("[process_bing_bulk_reverse_merge][results_full_address_col_name]",results_full_address_col_name)
        print("[process_bing_bulk_reverse_merge][results_addr_comps]",results_addr_comps)
        print("[process_bing_bulk_reverse_merge][merge_full_address_col_name]",merge_full_address_col_name)
        print("[process_bing_bulk_reverse_merge][merge_nan_value]",merge_error_value)
        print("[process_bing_bulk_reverse_merge][merge_empty_value]",merge_empty_value)
        print("[process_bing_bulk_reverse_merge][merge_addr_comps]",merge_addr_comps)

    # Check if lat lang columns already exist
    user_df_col_names   =   list(user_df.columns)

    # Check if full address column exists
    if(not(merge_full_address_col_name in user_df_col_names)) :
        new_column_values   =   []
        for j in range(len(user_df)) :
            new_column_values.append(merge_empty_value)

        if(DEBUG_MERGE) :
            print("new merge_full_address_col_name",merge_full_address_col_name)

        user_df[merge_full_address_col_name]     =   new_column_values

    user_df_col_names   =   list(user_df.columns)
        
    if(DEBUG_MERGE) :
        print("\nuser_df_col_names",user_df_col_names)

    if(results_addr_comps == "Full Address And Components") :

        if(DEBUG_MERGE) :
            print("\nmerge_addr_comps",type(merge_addr_comps),merge_addr_comps)

        merge_addr_comps_list    =  get_google_addr_comps(merge_addr_comps) 
        
        if(DEBUG_MERGE) :
            print("\nmerge_addr_comps_list",type(merge_addr_comps_list),merge_addr_comps_list)
            for l in range(len(merge_addr_comps_list)) :
                print("[merge_addr_comps_list]",type(merge_addr_comps_list[l]),len(merge_addr_comps_list[l]))

        for j in range(len(merge_addr_comps_list)) :
            if(not(merge_addr_comps_list[j] in user_df_col_names)) :
                new_column_values   =   []
                for k in range(len(user_df)) :
                    new_column_values.append(merge_empty_value)

                if(DEBUG_MERGE) :
                    print("new merge_addr_comps_list[j]",merge_addr_comps_list[j])

                user_df[merge_addr_comps_list[j]]     =   new_column_values

    else :

        merge_addr_comps_list   =   []    
    
    user_df_col_names   =   list(user_df.columns)

    if(DEBUG_MERGE) :
        print("\ncols list",user_df_col_names)

    error_indices   =   []

    full_address_index  =   -1
    for i in range(len(user_df_col_names)) :
        if(user_df_col_names[i] == merge_full_address_col_name) :
            full_address_index  =   i
            break
    
    error_indices.append(full_address_index)

    if(len(merge_addr_comps_list) > 0) :

        merge_addr_comps_indices    =   []

        for i in range(len(merge_addr_comps_list)) :
            for j in range(len(user_df_col_names)) :
                if(user_df_col_names[j] == merge_addr_comps_list[i]) :
                    merge_addr_comps_indices.append(j)
                    break
   
    if(DEBUG_MERGE) :
        print("\ncols list",user_df_col_names)
        print("[process_bing_bulk_query_merge][full_address_index]",full_address_index)
        if(len(merge_addr_comps_list) > 0) :
            print("[process_bing_bulk_query_merge][merge_addr_comps_indices]",merge_addr_comps_indices)

    # insert values into columns
    for i in range(len(results_df)) :

        row_id              =   results_df.iloc[i,0]
        full_address_value  =   results_df.iloc[i,2]

        addr_comp_values    =   []

        if(len(merge_addr_comps_list) > 0) :
            for j in range(len(merge_addr_comps_list)) :
                addr_comp_values.append(results_df.iloc[i,(3+j)])

        if(DEBUG_MERGE) :
            print("\n[process_bing_bulk_reverse_merge][rowid]",type(row_id),row_id)
            print("[process_bing_bulk_reverse_merge][full_address_value]",type(full_address_value),full_address_value)    
            print("[process_bing_bulk_reverse_merge][addr_comp_values]",type(addr_comp_values),addr_comp_values)

         # add value to the user df
        user_df.iloc[row_id,full_address_index]     =   full_address_value

        if(len(merge_addr_comps_list) > 0) :
            for i in range(len(merge_addr_comps_list)) :
                user_df.iloc[row_id,merge_addr_comps_indices[i]]     =   addr_comp_values[i] 
        
        current_count       =   (i + 1)
        current_percent     =   int( ( current_count / (len(results_df) + len(error_df)) ) * 100 )
        set_merge_bar_value(current_count,current_percent)        
    
    merge_errors(user_df,error_df,error_indices,merge_error_value) 

    current_count       =   len(results_df) + len(error_df)
    current_percent     =   int( ( current_count / len(results_df) ) * 100 )
    set_merge_bar_value(current_count,current_percent)        
       
        
"""
#----------------------------------------------------------------------------
#-  merge results console methods
#----------------------------------------------------------------------------
"""

merge_results_bar_text     =   "Total Results Merged &nbsp;&nbsp;&nbsp;: &nbsp;"

merge_console = """
    <br>
    <div class='dfcleanser-common-grid-header-large' width='400' >Geocoding Merge Console</div></br>
    <div class="dfc-console-container" width='100%' style='overflow-x: hidden; overflow-y: hidden;'>
        <br>
        <div class="dfc-console-container" style=' text-align: center; margin: auto; border: 0px solid #428bca; overflow-x: hidden; overflow-y: hidden;'>
            <div style="text-align: center; margin:auto; margin-top:20px;">
                <table class="tableRowHoverOff" id="geocodeStatusBars" style="margin:auto;">
                    <tbody>
                        <tr class='dfc-progress-row' style='height: 30px;'>
                            <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;' id="geocoderesults">Total Results Merged &nbsp;&nbsp;&nbsp;: &nbsp;0</td>
                        </tr>
                        <tr>
                            <td class='dfc-progress-col' style='width: 55%;'>
                                <div class='progress md-progress dfc-progress-div' style='height: 20px; '>
                                    <div id="resultlimit" class='progress-bar dfc-progress-bar' role='progressbar' style='height: 20px;' style=" width: 100%; " aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">100%</div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" id="dfc_run_parms" class="btn btn-primary" style="  width:400px;  height:40px;" onclick="browse_bulk_geocoding_df(XXXDISPLAY_BULK_SOURCE_DF)">Browse Merged user df</button>
            </div>

            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" id="dfc_run_parms" class="btn btn-primary" style="  width:400px;  height:40px;" onclick="controlbulkrun(26)">Return to Process Results</button>
            </div>

            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" id="dfc_run_parms" class="btn btn-primary" style="  width:400px;  height:40px;" onclick="exit_bulk_geocoding()">Exit Current Bulk Run </button>
            </div>
        </div>
    </div>
"""

def display_merge_console(merge_count,df_title) :

    merge_results_console   =   merge_console
    merge_results_console   =   merge_results_console.replace("XXXDISPLAY_BULK_SOURCE_DF","'"+df_title+"'")

    from dfcleanser.common.common_utils import displayHTML
    displayHTML(merge_results_console)

def set_merge_bar_value(countvalue,barvalue) :
    """
    * -------------------------------------------------------
    * function : update status bars
    * 
    * parms :
    *  geocid   - geocoder id
    *  barid    - progress bar id
    *  barvalue - bar value
    *
    * returns : 
    *  progress bar updated
    * --------------------------------------------------------
    """

    #from dfcleanser.Qt.utils.Geocode.GeocodeModel import (QUERY, BingId, GoogleId)
    
    bid         =   "resultlimit"
    countid     =   "geocoderesults"
    bhtml       =   merge_results_bar_text + str(countvalue)

    try :
        
        set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
        run_jscript(set_progress_bar_js,"fail to set progress bar : ")

        set_progress_count_js = "$('#" + countid + "').html('" + bhtml +"');"
        run_jscript(set_progress_count_js,"fail to set count value : ")
        
    except :

        #TODOD
        
        log_debug_dfc(-1,"set_merge_bar_value exception ") 
    

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  merge results common methods
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

def merge_errors(user_df,error_df,user_df_col_names_indices,error_value) :

    import numpy as np

    if(error_value == "nan") :
        error_value     =   np.NaN

    for i in range(len(error_df)) :

        row_id  =   error_df.iloc[i,0]

        for j in range(len(user_df_col_names_indices)) :
            user_df.iloc[row_id,user_df_col_names_indices[j]]   =   error_value


def get_google_addr_comps(addr_comps) :

    addr_comps_list     =   addr_comps.replace("[","")
    addr_comps_list     =   addr_comps_list.replace("]","")
    addr_comps_list     =   addr_comps_list.split(",")

    if(len(addr_comps_list[0]) == 0) :
        addr_comps_list     =   []    
    
    return(addr_comps_list)


def split_lat_lng_col_values(lat_lng_value) :

    lat_lng_cols    =   lat_lng_value.split(",")
    return(lat_lng_cols)


def get_lat_lng_col_names(col_defs) :

    col_name_list   =   col_defs.replace("[","")
    col_name_list   =   col_name_list.replace("]","")
    if(col_name_list.find(",") > -1) :
        col_name_list   =   col_name_list.split(",")  
    else :
        col_name_list   =   [col_name_list] 

    return(col_name_list)  
