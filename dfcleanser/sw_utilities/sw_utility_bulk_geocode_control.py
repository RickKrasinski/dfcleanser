"""
# sw_utility_bulk_geocode_control
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import json
import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_console as subgc
import dfcleanser.sw_utilities.sw_utility_geocode_control as sugc

from dfcleanser.common.common_utils import (display_exception, display_status, displayParms, 
                                            RunningClock, get_parms_list_from_dict, opStatus,
                                            delete_a_file, rename_a_file, does_file_exist,
                                            get_parms_for_input, run_javascript,
                                            does_dir_exist, make_dir)


import googlemaps


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

    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"process_bulk_geocoding_run_cmd " + str(cmd))
    
    opstat  =   opStatus()
    
    #sugw.display_geocode_main_taskbar() 
        
    if(cmd == sugm.BULK_START_GEOCODER) :
        opstat  =   start_geocode_runner()
                
        if(not (opstat.get_status()) ) :
            send_run_report_error(cmd, opstat.get_errorMsg()) 
            
    elif(cmd == sugm.BULK_STOP_GEOCODER) :
        stop_geocode_runner()
        
    elif(cmd == sugm.BULK_PAUSE_GEOCODER) :
        pause_geocode_runner()
        
    if(cmd == sugm.BULK_RESUME_GEOCODER) :
        resume_geocode_runner()
    
    elif(cmd == sugm.BULK_VIEW_ERRORS) :
        cfg.set_current_dfc_dataframe_title(sugm.GEOCODING_ERROR_LOG_DF_TITLE)
        run_javascript("view_geocode_errors();")
        
    elif(cmd == sugm.BULK_CHECKPT_GEOCODER) :
        checkpoint_geocode_runner()    
           
    elif(cmd == sugm.BULK_RESULTS_GEOCODER) :
        subgc.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_BASE,opstat)  
        
    if(cmd == sugm.REPORT_GEOCODE_RUN_ERROR) :
        
        run_cmd     =   int(parms[0])
        err_msg     =   parms[1]
        geocid      =   get_geocode_runner_id() 
        geotype     =   get_geocode_runner_type() 
        
        if(run_cmd == sugm.BULK_START_GEOCODER) :
            
            opstat  =   validate_bulk_geocode_connect_parms(geocid)
            
            if(not (opstat.get_status()) ) :
                
                sugc.display_geocode_utility(3, [geocid,geotype,[]])
                print("\n")
                display_exception(opstat)
                
            else :
                
                sugc.display_geocode_utility(5, [7,1,1,"[]"])
                print("\n")
                opstat.set_status(False)
                opstat.set_errorMsg(err_msg)
                display_exception(opstat)
                
        else :
            
            sugc.display_geocode_utility(5, [7,1,1,"[]"])
            print("\n")
            opstat.set_status(False)
            opstat.set_errorMsg(err_msg)
            display_exception(opstat)


def send_run_report_error(cmd, err_msg) :
    
    report_error_js     =   "report_geocode_run_error(" + str(cmd) + ",'" + err_msg + "');"
    
    print(report_error_js)
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(report_error_js,
                "fail report run error : "+ str(cmd) + err_msg,
                 "ssend_run_report_error")
    
    

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

    fparms    =   cfg.get_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms")
    
    opstat  =   opStatus()
    
    if(not(fparms == None)) :
        
        print("fparms",fparms)        
        if(geocid == sugm.ArcGISId)              :
            validate_batch_arcgis_geocoder_parms(fparms,opstat)

        elif(geocid == sugm.BingId)              : 
            subgw.validate_bing_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.GoogleId)            : 
            validate_bulk_google_geocoder_parms(fparms,opstat)

        elif(geocid == sugm.OpenMapQuestId)      : 
            subgw.validate_mapquest_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.NominatimId)         : 
            subgw.validate_nominatim_geocoder_parms(fparms,opstat,False)
            
    else :
        
        if(not(geocid == sugm.ArcGISId)) :
            opstat.set_status(False)
            opstat.set_errorMsg("No geocoder connect parms defined")
        
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
        
    return()


"""
#----------------------------------------------------------------------------
#-  Common bulk geocoding control methods
#----------------------------------------------------------------------------
"""
def get_bulk_coords(geocid,inputs) :
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
    
    opstat      =   opStatus()
    
    if(not (inputs == None)) :
        runParms    =   subgw.validate_bulk_parms(geocid,sugm.QUERY,inputs,opstat) 
    else :
        if(geocid == sugm.ArcGISId) :
            parms   =   cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
        elif(geocid == sugm.GoogleId) :
            parms   =   cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
        
        runParms    =   subgw.validate_bulk_parms(geocid,sugm.QUERY,parms,opstat) 

    if(opstat.get_status()) :
        
        if(geocid == sugm.GoogleId) :
            
            cfg.set_config_value(subgw.bulk_google_query_input_id+"Parms",
                                 get_parms_list_from_dict(subgw.bulk_google_query_input_labelList[:10],runParms))
            
            address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
            subgc.display_geocoder_console(sugm.GoogleId,sugm.QUERY,runParms,opstat,sugm.LOAD)
            load_geocode_runner(sugm.GoogleId,sugm.QUERY,runParms,address_map)
            
        else :
            cfg.set_config_value(subgw.batch_arcgis_query_id+"Parms",
                                 get_parms_list_from_dict(subgw.batch_arcgis_query_labelList[:11],runParms))
            
            run_arcgis_bulk_geocode(sugm.QUERY,runParms,opstat,sugm.BULK_LOAD_GEOCODER)
        
    else :
        subgw.display_bulk_geocoding(geocid,sugm.QUERY)
        display_exception(opstat)
       
    
def get_bulk_addresses(geocid,inputs) :
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
    
    print("get_bulk_coords",geocid,"\n",inputs)
    
    opstat      =   opStatus()
    
    if(not (inputs == None)) :
        runParms    =   subgw.validate_bulk_parms(geocid,inputs,opstat) 
    else :
        if(geocid == sugm.ArcGISId) :
            parms   =   cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
        elif(geocid == sugm.GoogleId) :
            parms   =   cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
        
        runParms    =   subgw.validate_bulk_parms(geocid,parms,opstat) 
            
    #print("\nget_bulk_coords \n",runParms)
    
    if(opstat.get_status()) :
        
        if(geocid == sugm.GoogleId) :
            subgc.display_geocoder_console(sugm.GoogleId,sugm.REVERSE,runParms,opstat,sugm.LOAD)
            load_geocode_runner(sugm.GoogleId,sugm.REVERSE,runParms,None)

        else :
            run_arcgis_bulk_geocode(runParms,opstat)
        
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
    
    print("validate_batch_arcgis_geocoder_parms",connectParms) 
    
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
                    geocoder                =   get_geocoders(gis)[0]
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
        cfg.set_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,cparms[1][0])
        cfg.set_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,cparms[1][1])
        
    return(cparms[0])

"""
#------------------------------------------------------------------
#   test arcgis batch connector
#------------------------------------------------------------------
"""
def test_arcgis_batch_connector(connectParms) :

    #geotype     =   parms[1]
    #fparms      =   get_parms_for_input(connectParms,subgw.batch_arcgis_geocoder_idList)  

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
            results     =   batch_geocode(addresses,geocoder=geocoder)
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

def get_arcgis_batch_addresses(rowIndex,runParms,addressMap) :
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
    
    arcgisbatch     =   []

    batchSize   =   int(cfg.get_cfg_parm_from_input_list(subgw.batch_arcgis_query_id,"batch_size",subgw.batch_arcgis_query_labelList))
    maxAddrs    =   int(cfg.get_cfg_parm_from_input_list(subgw.batch_arcgis_query_id,"max_addresses_to_geocode",subgw.batch_arcgis_query_labelList))
    
    if((rowIndex + batchSize) > maxAddrs) :
        stopRow     =   maxAddrs - 1
    else :
        stopRow     =   (rowIndex + batchSize) - 1
        
    for i in range(rowIndex,stopRow) :
        arcgisbatch.append(sugm.get_geocode_address_string(addressMap,rowIndex))
        
    return(arcgisbatch)


def run_arcgis_bulk_geocode(runParms,opstat,state) :
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
    
    if(state == sugm.LOAD) :
        address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
    
        if(opstat.get_status()) :
            subgc.display_geocoder_console(sugm.ArcGISId,runParms,opstat)
            sugm.load_geocode_runner(sugm.ArcGISId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.RUNNING)
        opstat  =   sugm.start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.PAUSING)


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
    
    geocode_list    =   []
    get_address     =   False
    
    if(runParms.get("save_geocoder_full_address_column_name")  == "True") :
        get_address     =   True

    country         =   runParms.get("source_country",None)
    category        =   runParms.get("category",None)
    out_sr          =   runParms.get("out_sr",None)

    try :
    
        from arcgis.geocoding import batch_geocode
        results = batch_geocode(addresslist,country,category,out_sr,geocoder)
        
    except Exception as e:
        opstat.store_exception("Unable to get arcgis batch",e)
    
    if(opstat.get_status()) :

        for result in results :

            score           =   result['score']

            location        =   result['location']
            lat             =   location['x']
            long            =   location['y']
        
            attributes      =   result['attributes']
            Addr_type       =   attributes['Addr_type']
            
            if(get_address) :            
                geocode_list.append([score,lat,long,result['address'],Addr_type])
            else :
                geocode_list.append([score,lat,long,Addr_type])
        
    return(geocode_list)


def process_arcgis_geocode_batch_results(batch_results,runParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : process a single arcgis goeocode batch
    * 
    * parms :
    *  batch_results    - single arcgis batch results
    *  runParms         - run parms
    *  opstat           - run op status
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("process_arcgis_geocode_batch_results",batch_results,runParms,opstat)
    
    resultsLog    =   get_geocode_runner_results_log()
    
    


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
    
    print("process_arcgis_geocode_batch_error",batch_results,runParms,opstat)
    errorLog    =   sugm.get_geocode_runner_error_log()
    
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

def process_google_geocoding_errors(geotype,rowid,inputParms,error_msg,note=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : process a google bulk geocode error
    * 
    * parms :
    *   geotype     - geocoder cmd type
    *   geotype     - geocoder cmd type
    *   inputParms  - input parms causing error
    *   error_msg   - error message to log
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowid,"process_google_geocoding_errors : " + str(geotype) + str(rowid) + str(inputParms) + str(error_msg))

    error_log       =   get_geocode_runner_error_log()
    error_log.log_error(rowid,inputParms,error_msg,note)
    error_limit     =   error_log.get_error_limit()
    
    results_log         =   get_geocode_runner_results_log()
    total_results       =   results_log.get_results_count()
    total_errors        =   error_log.get_error_count()
    max_rows            =   get_geocode_maxrows()
    current_error_rate  =   (total_errors / max_rows) * 100   
        
    subgc.set_progress_bar_value(sugm.GoogleId,sugm.ERROR_BAR,total_errors,int(current_error_rate))
    
    if(current_error_rate > error_limit) :
        
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowid,"error limit exceeded" + str(error_limit) + str(total_results) + str(total_errors))
    
        set_geocode_runner_halt_flag(True)
        set_geocode_runner_state(sugm.STOPPING)
        subgc.set_status_bar(sugm.ERROR_LIMIT)
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocode connection methods
#--------------------------------------------------------------------------
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
            
            test_results    =   get_google_geocode_results(0,test_address,None) 
    
        except Exception as e:
            opstat.store_exception("Unable to connect to google ",e)
    
        clock.stop()
    
    subgw.display_bulk_geocoders(sugm.GoogleId)
    
    if(opstat.get_status()) :
        print("\n")
        display_status("Google bulk geocoder connected to successfully")
        if(not (test_results == None)) :
            display_google_test_results(test_address,test_results)
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 


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
#--------------------------------------------------------------------------
#   google bulk geocode query methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_google_geocode_results(rowid,address,queryParms) :
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
    
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowid,"get_google_geocode_results : "+ address)
        
    opstat          =   opStatus()
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
            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            languagedict    =   dicts.get("Language_Codes",None)
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
            opstat.set_errorMsg("UNKNOWN EXCEPTION")
        
    try :
    
        if(len(geocode_results) > 1) :  
            current_geocode_results    =  sugm.google_geocode_results(rowid,geocode_results[0],geocode_results[1],opstat)
        elif(len(geocode_results) == 1) : 
            current_geocode_results    =  sugm.google_geocode_results(rowid,None,geocode_results[0],opstat)    
        else :
            current_geocode_results    =  None
            
    except :
        current_geocode_results    =  None    
        
    return(current_geocode_results)


def process_google_geocode_results(inputParms,runParms,geocode_results) :
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
    
    #if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(geocode_results.get_row_Id(),"process_google_geocode_results")

    results_df          =   get_geocode_runner_results_log()
    #rowid               =   geocode_results.get_row_Id()
    
    lat_long_col_name   =   runParms.get(subgw.bulk_google_query_input_labelList[2])
    if(lat_long_col_name.find("]") > -1) :
        lat_long_names  =  json.loads(lat_long_col_name)
    else :
        lat_long_names  =  [lat_long_col_name]
    
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
    
    if(runParms.get(subgw.bulk_google_query_input_labelList[7]) == "True") : 
        save_location_type      =   True
    else :
        save_location_type      =   False
    
    # check if location is acceptable
    if( (accept_all_types) or (geocode_results.get_location_type() in location_list) ) :
        
        if(save_full_address) :
            
            if(save_location_type) :
                if(len(lat_long_names) == 1) :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_location_type(), geocode_results.get_formatted_address()])
                else :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_location_type(), geocode_results.get_formatted_address()])
            else :
                if(len(lat_long_names) == 1) :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_formatted_address()])
                else :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_formatted_address()])
        
        else :
            if(save_location_type) :
                if(len(lat_long_names) == 1) :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_location_type()])
                else :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_location_type()])
            else :
                if(len(lat_long_names) == 1) :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()]])
                else :
                    results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng()])
       
    else :
        
        process_google_geocoding_errors(sugm.QUERY,geocode_results.get_row_Id(),
                                        inputParms,geocode_results.get_location_type())
        
        parmsDict   =   None
        
        if(save_location_type) :
            parmsDict   =   {}
            parmsDict.update({"location_type":geocode_results.get_location_type()})
        
        results_df.add_nan_result(geocode_results.get_row_Id(),inputParms,parmsDict)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk geocode reverse methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_google_reverse_results(rowid,lat_long,reverseParms) :
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
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowid,"get_google_reverse_results" + str(lat_long) + json.dumps(reverseParms))
    
    
    opstat          =   opStatus()
    reverse_results =   None
    
    gmaps           =   get_geocode_connector() 
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
        gmaps   =   get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        set_geocode_connector(gmaps)

    if(opstat.get_status()) :   
        
        if(not (reverseParms == None)) :
            result_typeParm     =   reverseParms.get("result_type",None)
            location_typeParm   =   reverseParms.get("location_type",None)
            languageParm        =   reverseParms.get("language",None)
        else :
            result_typeParm     =   None
            location_typeParm   =   None
            languageParm        =   None

        try :
        
            reverse_results =   gmaps.reverse_geocode(lat_long,
                                                      result_type=result_typeParm,
                                                      location_type=location_typeParm,
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
            opstat.set_errorMsg("UNKNOWN EXCEPTION")

    try :
    
        if(len(reverse_results) > 1) :  
            current_reverse_results    =  sugm.google_reverse_results(rowid,reverse_results[0],reverse_results[1],opstat)
        elif(len(reverse_results) == 1) : 
            current_reverse_results    =  sugm.google_reverse_results(rowid,None,reverse_results[0],opstat)    
        else :
            current_reverse_results    =  None
            
    except :
        current_reverse_results    =  None    

    return(current_reverse_results)

    
def process_google_reverse_results(inputParms,runParms,reverse_results) :
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

    print("process_google_reverse_results",inputParms,runParms,reverse_results)
    


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
    
    results_df  =   get_geocode_runner_results_log().get_geocoding_df()
        
    geocid      =   int(cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY))
    
    if(cmd == sugm.PROCESS_BULK_RESULTS_CONCAT_PROCESS) :
        
        if(geocid == sugm.GoogleId) :
            gparms      =   cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
            source_df   =   cfg.get_dfc_df(gparms[0]).get_df()
            
            proc_parms  =   get_parms_for_input(inparms,subgc.bulk_geocode_proc_input_idList)

            if(proc_parms[2] == "True") :
                drop_addr_cols  =   True
            else :
                drop_addr_cols  =   False
                
            if(drop_addr_cols) :
        
                address_map         =   sugm.get_address_map(gparms[1])
                addr_cols_map       =   address_map.get_colindices()
                addr_cols           =   []
    
                for i in range(len(addr_cols_map)) :
                    if(not (addr_cols_map[i] == -1))  :
                        addr_cols.append(addr_cols_map[i])
                        
                try :
                    source_df.drop(addr_cols,axis=1,inplace=True)
                except Exception as e:
                    opstat.store_exception("Unable append drop address cols ",e)
                    
            if(opstat.get_status()) :
                
                paxis   =   int(proc_parms[0])
                pjoin   =   proc_parms[1]

                import pandas as pd            
                try :
                    results_df.drop(["source df rowid","input value"],axis=1,inplace=True)
                    source_df     =   pd.concat([source_df, results_df], axis=paxis, join=pjoin)

                    cfg.set_current_dfc_dataframe(source_df) 
                    
                except Exception as e:
                    opstat.store_exception("Unable append geocoding results ",e)
                
                if(opstat.get_status()) :
                    subgc.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_CONCAT_PROCESSED,opstat)
                else :
                    display_exception(opstat)
                    
            else :
                display_exception(opstat)
                    
                        
    elif(cmd == sugm.PROCESS_BULK_REVERSE_RESULTS_CONCAT_PROCESS) :
        
        if(geocid == sugm.GoogleId) :
            gparms      =   cfg.get_config_value(subgw.bulk_google_reverse_input_id+"Parms")
            source_df   =   cfg.get_dfc_df(gparms[0]).get_df()

            proc_parms  =   get_parms_for_input(inparms,subgw.bulk_google_procr_input_idList)
            
            paxis   =   int(proc_parms[0])
            pjoin   =   proc_parms[1]

            import pandas as pd            
            try :
                results_df.drop(["source df rowid","input value"],axis=1,inplace=True)
                source_df     =   pd.concat([source_df, results_df], axis=paxis, join=pjoin)
                
                cfg.set_current_dfc_dataframe(source_df)
                
            except Exception as e:
                opstat.store_exception("Unable append geocoding results ",e)
                
            if(opstat.get_status()) :
                subgc.display_geocoder_process_results(sugm.DISPLAY_BULK_RESULTS_CONCAT_PROCESSED,opstat)
            else :
                display_exception(opstat)
                    

    elif(cmd == sugm.PROCESS_BULK_RESULTS_CSV_PROCESS) :
        
        #nb_name =   get_notebookName() 
        nbpath  =   cfg.get_notebookPath()
        
        import os
        
        df_export_path = os.path.join(nbpath,"exports")
        if (not (does_dir_exist(df_export_path)) ) :
            make_dir(df_export_path)

        proc_parms  =   get_parms_for_input(inparms,subgc.bulk_geocode_export_input_idList)

        if(len(proc_parms) > 0) :
            csv_file_name   =   os.path.join(df_export_path, proc_parms[0] + ".csv")
        else :
            csv_file_name   =   None
        
        if(not (csv_file_name is None)) :
            #write out csv file 
            try :
                if(not (csv_file_name is None)) :
                    results_df.to_csv(csv_file_name)
            except Exception as e:
                opstat.store_exception("Unable to export geocoding results file ",e)
                
        if(opstat.get_status()) :
            print("\n")
            display_status("Geocode Results exported successfully to csv file ")
            
            notes   =   []
            notes.append("Results exported to : ")
            notes.append("&nbsp;&nbsp;&nbsp;&nbsp;" + csv_file_name)
    
            #display_notes(notes)
            from dfcleanser.common.common_utils import display_msgs
            display_msgs(notes,None)
            
            subgc.display_base_taskbar()
            print("\n")
            
            
        else :
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

class GeocodeTask:
    
    geocoderId          =   -1
    geocodeType         =   sugm.QUERY
    rowId               =   -1
    inputparms          =   None
    runParms            =   None
    
    geocode_results     =   None
    task_running        =   False
        
    def __init__(self, geocoderId,geocodeType,rowid,inputparms,runparms):
        self.geocoderId         =   geocoderId
        self.geocoder_type      =   geocodeType
        self.rowId              =   rowid
        self.inputParms         =   inputparms
        self.runParms           =   runparms
        self.geocode_results    =   None
        
    def run_geocoder_task(self) :
        
        try :
            self.task_running       =   True
            import time
            time.sleep(0.05)
            self.run_geocode_method()  
            self.task_running       =   False
        except :
            self.task_running       =   False
            process_google_geocoding_errors(self.geocoder_type,self.rowId,self.inputParms,"Task Excepption")
            
    def run_geocode_method(self) :
        #if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(self.rowId,"run_geocode_method")
        if(self.geocoderId == sugm.GoogleId) :
            if(self.geocoder_type == sugm.QUERY) :
                self.geocode_results    =   get_google_geocode_results(self.rowId,self.inputParms,self.runParms)
            elif(self.geocoder_type == sugm.REVERSE) :
                self.geocode_results    =   get_google_reverse_results(self.rowId,self.inputParms,self.runParms) 

            if(not (self.geocode_results is None) ) :
                # no error occurred
                if(self.geocode_results.get_status()) :
                    if(self.geocoder_type == sugm.QUERY) :
                        process_google_geocode_results(self.inputParms,self.runParms,self.geocode_results)
                    else :
                        process_google_reverse_results(self.inputParms,self.runParms,self.geocode_results)
            
                # error occurred        
                else :
                    if(self.geocode_results.get_error_message() == sugm.OverQueryLimitErrorMessage) : 
                        stop_geocode_runner()
                
                    process_google_geocoding_errors(self.geocoder_type,self.rowId,self.inputParms,self.geocode_results.get_error_message())
                    
            else :
                process_google_geocoding_errors(self.geocoder_type,self.rowId,self.inputParms,"No results returned")    
                
        else :
            self.geocode_results    =   None            

    def get_task_run_state(self) :
        return(self.task_running)    
    
    def get_task_row_id(self) :
        return(self.rowId)    


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Task Monitor Class
#----------------------------------------------------------------------------
#   geocoding task monitoring class for controlling geocode tasks
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""        
import threading
        
class GeocodeThreadsMonitor:
    
    taskdict        =   {}
    maxtasks        =   0
        
    def __init__(self, maxtasksparm):
        self.taskdict        =   {}
        self.maxtasks        =   maxtasksparm
    
    def addtask(self, geocodetask, rowindex):
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowindex,"addtask ["+ str(len(self.taskdict))+"]")
        self.taskdict.update({rowindex:geocodetask})
        threading.Thread(target=geocodetask.run_geocoder_task).start()
        
    def droptask(self, rowindex):

        if(not(self.taskdict.get(rowindex,None) is None)) :
            self.taskdict.pop(rowindex,None)
            if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowindex,"droptask : task popped : num active tasks [" + str(len(self.taskdict))+"]")
        else :
            if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowindex,"droptask : task not found")

    def more_tasks_available(self):

        if(len(self.taskdict) < self.maxtasks) :
            return(True)
        else :
            return(False)

    def clear_completed_tasks(self) :
        task_keys   =   list(self.taskdict.keys())
        
        for i in range(len(task_keys)) :
            ctask   =   self.taskdict.get(task_keys[i])

            if( not(ctask.get_task_run_state()) ) :
                self.droptask(ctask.get_task_row_id())

    def all_tasks_completed(self) :
        if(len(self.taskdict) == 0) :
            return(True)
        else :
            return(False)


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Runner Class
#----------------------------------------------------------------------------
#   class for running the current geocoding instance from dfcleanser.
#   controls tasks and updates display
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
def stop_geocode_runner() :
    dfc_Geocode_Runner.stop_run() 
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 
def checkpoint_geocode_runner() :
    dfc_Geocode_Runner.checkpoint_run() 

def get_geocode_runner_results_log() :
    return(dfc_Geocode_Runner.get_results_log())
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

def get_geocode_run_total_time() :
    return(dfc_Geocode_Runner.get_total_run_time())

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
    
    checkpoint_on           =   False
       
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
        
        self.checkpoint_on          =   False
        
    def load_run(self,geocoderId,geoType,runParms,addressParms):
        self.geocid             =   geocoderId
        self.geotype            =   geoType
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        if(self.geocid == sugm.GoogleId) :
            if(self.geotype == sugm.QUERY) :
                self.maxrows            =   int(runParms.get("max_addresses_to_geocode"))
        
        if(self.geocid == sugm.GoogleId) :
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(sugm.MAX_GOOGLE_TASKS)
        
        from dfcleanser.sw_utilities.sw_utility_geocode_model import init_geocoding_data_structures
        bulkstructures          =   init_geocoding_data_structures(self.geocid,self.geotype,self.runParms)
        self.geocodingResults   =   bulkstructures[0]
        self.geocodingErrorLog  =   bulkstructures[1]
        
        self.geocodingErrorLog.set_error_limit(self.geocid,self.geotype)
        
    def start_run(self):
        subgc.set_status_bar(sugm.STARTING)
        self.set_run_state(sugm.STARTING)

        self.set_halt_flag(False)
        self.rowindex           =   0
        
        self.start_time         =   datetime.datetime.now()
        self.syop_time          =   datetime.datetime.now()
        
        return(self.start_bulk_geocode_runner(0))
        
    def stop_run(self) :
        
        if(self.get_run_state() == sugm.PAUSED) :
            subgc.set_status_bar(sugm.STOPPED)
            self.set_run_state(sugm.STOPPED)
            
        else :    
            subgc.set_status_bar(sugm.STOPPING)
            self.set_run_state(sugm.STOPPING)
            
        self.set_halt_flag(True)
        
    def pause_run(self) :
        subgc.set_status_bar(sugm.PAUSING)
        self.set_run_state(sugm.PAUSING)
        self.set_halt_flag(True)

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
        self.state  =   runstate
    
    def start_bulk_geocode_runner(self,rowIndex) :
        
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(rowIndex,"start_bulk_geocode_runner")
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
            
            self.set_halt_flag(False)
            threading.Thread(target=self.bulk_geocode_runner_task).start()
            subgc.set_status_bar(sugm.RUNNING)
            
            return(opstat)
            
        else :
            return(opstat)
        
    def bulk_geocode_runner_task(self) :
        
        while ( (not (self.is_geocode_run_complete()))  ) :
            
            self.geocodeThreadsMonitor.clear_completed_tasks()
            
            if( not (self.get_halt_flag()) ) :
            
                if(self.geocid == sugm.ArcGISId) :
                            
                    opstat              =   opStatus()
                    next_batch_addrs    =   subgc.get_arcgis_batch_addresses(self.rowindex,self.runParms,self.addressParms)
                    geocoder = None
                    geocode_results     =   subgc.get_arcgis_geocode_batch(geocoder,next_batch_addrs,opstat)
                
                    if(opstat.get_status()) :
                    
                        # batch retrieved ok
                        self.rowindex   =   subgc.process_arcgis_geocode_batch_results(geocode_results,self.runParms,opstat)
                    
                        if(self.rowindex >= (self.maxrows-1)) :
                            self.set_halt_flag(True)   
                
                    else :
                    
                        self.set_halt_flag(True)    
                        subgc.process_arcgis_geocode_batch_error(geocode_results,self.runParms,opstat) 
                
                elif(self.geocid == sugm.GoogleId) :
                
                    opstat      =   opStatus()
                    
                    if(self.geocodeThreadsMonitor.more_tasks_available()) :
                    
                        if(self.rowindex < self.maxrows) :
                        
                            next_addr       =   sugm.get_geocode_address_string(self.addressParms,self.rowindex)
                            geocodetask     =   GeocodeTask(self.geocid,self.geotype,self.rowindex,next_addr,self.runParms)  
                            self.geocodeThreadsMonitor.addtask(geocodetask,self.rowindex)

                            self.rowindex   =   self.rowindex + 1
                    
                        else :
                            self.set_halt_flag(True)
                        
                    else :
                    
                        if(self.geocid == sugm.GoogleId) :
                            delay   =   sugm.GOOGLE_DELAY
                        elif(self.geocid == sugm.GoogleId) :
                            delay   =   sugm.BING_DELAY
                        elif(self.geocid == sugm.OpenMapQuestId) :
                            delay   =   sugm.OPENMAPQUEST_DELAY
                        else :
                            delay   =   sugm.NOMINATIM_DELAY
                    
                        import time
                        time.sleep(delay)
                        
                        #if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"task delay " + str(self.ResultsLength) + " " + str(self.geocodingResults.get_results_count()))
                        
                    self.update_status_bar()
                    
                    if( self.rowindex >= self.maxrows ) :
                        self.set_halt_flag(True)
     
                else :
                    print("geocoder not supported")
                    set_geocode_runner_halt_flag(True)    
                    self.geocoding_in_error     =   True

                self.update_status_bar() 
                self.update_state()

            else :
                
                self.update_status_bar() 
                self.update_state()
                if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"main sleep")
                
                import time
                time.sleep(0.2)

        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"geocode run task complete : rowid "+ str(self.rowindex))        
        if(self.is_geocode_run_complete()) :
            
            self.geocodingResults.finish_results_log()
            self.geocodingErrorLog.finish_error_log()
            self.stop_time         =   datetime.datetime.now()
            
            if(self.geocoding_in_error) :
                subgc.set_status_bar(sugm.STOPPED) 
            else :   
                subgc.set_status_bar(sugm.FINISHED)

        
    def is_geocode_run_complete(self) :
        if( ((self.get_halt_flag()) and 
             (self.geocodeThreadsMonitor.all_tasks_completed()) and 
             (self.geocodingResults.get_results_count() >= self.maxrows)) or
            (self.geocoding_in_error) ) :
        
            if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"geocode run is complete : state "+ str(self.state) + " halt :  " + str(self.geocodeThreadsMonitor.all_tasks_completed())+ " : results " + str(self.geocodingResults.get_results_count()))        

            return(True)
        else :
            return(False)

    def update_status_bar(self) :
        
        if(not (self.ResultsLength == self.geocodingResults.get_results_count())) :

            current_count       =   self.geocodingResults.get_results_count()
            current_percent     =   int( ( current_count / self.maxrows ) * 100 )
            if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"update status bar : current pct " + str(current_percent))
            subgc.set_progress_bar_value(self.geocid,sugm.GEOCODE_BAR,current_count,current_percent)
            self.ResultsLength  =   self.geocodingResults.get_results_count()

    def update_state(self) :
        
        if(self.get_run_state()   ==  sugm.STARTING) : 
            if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"update_state : STARTING "+ str(self.state) + " " + str(self.geocodingResults.get_results_count())+ " " + str(self.geocodeThreadsMonitor.all_tasks_completed()))        

            if( (not (self.geocodeThreadsMonitor.more_tasks_available()) )  or 
                (self.geocodingResults.get_results_count() > 0) ) : 
                subgc.set_status_bar(sugm.RUNNING)
                self.set_run_state(sugm.RUNNING)
                
        elif(self.get_run_state()   ==  sugm.STOPPING) :
            if( self.geocodeThreadsMonitor.all_tasks_completed() ) :
                subgc.set_status_bar(sugm.STOPPED)
                self.set_run_state(sugm.STOPPED)
            
        elif(self.get_run_state()   ==  sugm.PAUSING) :
            if( self.geocodeThreadsMonitor.all_tasks_completed() ) : 
                subgc.set_status_bar(sugm.PAUSED)
                self.set_run_state(sugm.PAUSED)
                
                if(self.checkpoint_on) :
                    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"checkpoint_on "+ str(self.state))        

                    self.checkpoint_results()
                    subgc.set_status_bar(sugm.CHECKPOINT_COMPLETE)
                
    def checkpoint_results(self) :
        
        opstat  =   opStatus()
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"checkpoint_results")

        subgc.set_status_bar(sugm.CHECKPOINT_STARTED)
        self.geocodingResults.finish_results_log()
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"checkpoint flush")
        
        if(self.geocid == sugm.GoogleId) :
            df_source   =   self.runParms.get(subgw.bulk_google_query_input_labelList[0]) 
        elif(self.geocid == sugm.ArcGISId) :
            df_source   =   self.runParms.get(subgw.batch_arcgis_query_labelList[0]) 
        
        file_name       =   cfg.get_notebookName() + "_" + df_source + "_checkpoint"
        
        import os
        backup_file_path_name  =   os.path.join(cfg.get_notebookPath(),file_name + "_backup.csv")
        chckpt_file_path_name  =   os.path.join(cfg.get_notebookPath(),file_name + ".csv")
        
        if(does_file_exist(backup_file_path_name)) :
            delete_a_file(backup_file_path_name,opstat)
            rename_a_file(chckpt_file_path_name,backup_file_path_name,opstat)
            
        elif(does_file_exist(chckpt_file_path_name)) :
            rename_a_file(chckpt_file_path_name,backup_file_path_name,opstat)
            
        df = self.geocodingResults.get_geocoding_df()            
        
        try :
            df.to_csv(chckpt_file_path_name)
            
        except Exception as e: 
            opstat.store_exception("Unable to export to csv file " + chckpt_file_path_name,e)
    
        subgc.set_status_bar(sugm.CHECKPOINT_COMPLETE)
        

        
    def get_results_log(self):
        return(self.geocodingResults)
    def get_error_log(self):
        return(self.geocodingErrorLog)
    def get_halt_flag(self):
        return(self.halt_all_geocoding)
    def set_halt_flag(self,fstate):
        if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"set_halt_flag "+ str(fstate))
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

    def get_total_run_time(self) :
        if(self.stop_time == 0) :
            self.stop_time =  datetime.datetime.now()  
        timedelta   =   self.stop_time  -   self.start_time
        return(timedelta.days * 24 * 3600 + timedelta.seconds)

"""
#--------------------------------------------------------------------------
#   static geocode runner object
#--------------------------------------------------------------------------
"""    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        










