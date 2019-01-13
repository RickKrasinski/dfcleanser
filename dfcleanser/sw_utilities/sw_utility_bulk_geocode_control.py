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

import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_console as subgc
import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm

from dfcleanser.common.common_utils import (display_exception, display_status, displayParms, 
                                            RunningClock, get_parms_list_from_dict, opStatus)


import googlemaps


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
#   arcgis query methods
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
    
    resultsLog    =   sugm.get_geocode_runner_results_log()
    
    


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
#   google bulk coding methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google bulk geocoder methods
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
        display_status("Google bulk geocoder connected to successfully")
        if(not (test_results == None)) :
            display_google_test_results(test_address,test_results)
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 


def display_google_test_results(address,results) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display google test geocoder results
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
#   google bulk query methods
#--------------------------------------------------------------------------
"""
def run_google_bulk_geocode(geotype,cmd,runParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : control the arcgis bulk geocoder
    * 
    * parms :
    *  runParms     - google run parms
    *  opstat       - operation status object
    *  state        - run state
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    #print("\nrun_google_bulk_geocode :",state,"\n",runParms) 

    opstat  =   opStatus()
    
    if(cmd == sugm.BULK_LOAD_GEOCODER) :
        address_map     =   sugm.get_address_map(runParms.get("dataframe_address_columns"))
    
        if(opstat.get_status()) :
            subgc.display_geocoder_console(sugm.GoogleId,geotype,runParms,opstat,sugm.LOAD)
            sugm.load_geocode_runner(sugm.GoogleId,geotype,runParms,address_map)
   
    elif(cmd == sugm.BULK_START_GEOCODER) :
        subgc.display_geocoder_console(sugm.GoogleId,geotype,None,opstat,sugm.RUNNING)
        opstat  =   sugm.start_geocode_runner()
    
    elif(cmd == sugm.BULK_STOP_GEOCODER) :
        subgc.display_geocoder_console(sugm.GoogleId,geotype,None,opstat,sugm.STOPPING)

    elif(cmd == sugm.BULK_PAUSE_GEOCODER) :
        subgc.display_geocoder_console(sugm.GoogleId,geotype,None,opstat,sugm.PAUSING)


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
    
    print("\nget_google_geocode_results : ",rowid,address,flush=True)
        
    opstat          =   opStatus()
    geocode_results =   None
    gmaps           =   sugm.get_geocode_connector() 
    
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
        gmaps   =   get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        
        sugm.set_geocode_connector(gmaps)
    
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
    print("get_google_reverse_results",lat_long,"\n",reverseParms)
    
    
    opstat          =   opStatus()
    reverse_results =   None
    
    gmaps           =   sugm.get_geocode_connector() 
    
    if(gmaps == None) :
        cparms  =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
        gmaps   =   get_bulk_google_geocoder_connection(cparms[0],cparms[1],cparms[2],opstat)        

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

    print("\nprocess_google_geocode_results",geocode_results.get_row_Id(),inputParms)


    results_df          =   sugm.get_geocode_runner_results_log()
    rowid               =   geocode_results.get_row_Id()
    
    lat_long_col_name   =   runParms.get(subgw.bulk_google_query_input_labelList[3])
    if(lat_long_col_name.find("]") > -1) :
        lat_long_names  =  json.loads(lat_long_col_name)
    else :
        lat_long_names  =  [lat_long_col_name]
    
    save_full_address   =   True
    full_addr_col_name  =   runParms.get(subgw.bulk_google_query_input_labelList[4])
    if(full_addr_col_name == "None") :
        save_full_address   =   False
        
    location_types      =   runParms.get(subgw.bulk_google_query_input_labelList[7])
    
    if(location_types == "ALL") :
        accept_all_types   =   True
    else :
        import json
        location_list  =   json.loads(location_types)
        
    # check if location is acceptable
    if( (accept_all_types) or (geocode_results.get_location_type() in location_list) ) :
        
        if(save_full_address) :
            if(len(lat_long_names) == 1) :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()], geocode_results.get_formatted_address()])
            else :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng(), geocode_results.get_formatted_address()])
        else :
            if(len(lat_long_names) == 1) :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, [geocode_results.get_lat(),geocode_results.get_lng()]])
            else :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, geocode_results.get_lat(), geocode_results.get_lng()])
       
    else :
        
        # store nan values and put in error log
        if(save_full_address) :
            if(len(lat_long_names) == 1) :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, [float("nan"),float("nan")], ""])
            else :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, float("nan"), float("nan"), ""])
        else :
            if(len(lat_long_names) == 1) :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, [float("nan"),float("nan")]])
            else :
                results_df.add_result([geocode_results.get_row_Id(), inputParms, float("nan"), float("nan")])
    
        sugm.add_row_nan_error(rowid,geocode_results.get_location_type())

    print("process_google_geocode_results : end\n")
    
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
    


def process_google_geocoding_errors(geotype,inputParms,runParms,geocoding_results) :
    print("process_google_geocoding_errors",inputParms,runParms,geocoding_results)
    error_log   =   sugm.get_geocode_runner_error_log() 



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process bulk geocodinig common components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    

def init_geocoding_data_structures(geocid,geotype,runParms) :
    """
    * --------------------------------------------------------- 
    * function : init data structures to run geocoder
    * 
    * parms :
    *  geocid     - geocoder identifier
    *  geotype    - geocoding op type
    *  runParms   - run parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("init_geocoding_data_structures",geocid,geotype,runParms)    
    columns     =   ["rowIndex", "inputval"]

    if(geocid == sugm.GoogleId) :
        
        if(geotype == sugm.QUERY) :  
            
            lat_long_col_name   =   runParms.get(subgw.bulk_google_query_input_labelList[3])
            if(lat_long_col_name.find("[") > -1) :
                import json
                lat_long_names  =  json.loads(lat_long_col_name)
            else :
                lat_long_names  =  [lat_long_col_name]
                
            print("lat_long_names",lat_long_names)
            columns.append(lat_long_names)

            if(not (runParms.get(subgw.bulk_google_query_input_labelList[4]) == "None")) :            
                columns.append("full_address")
            
        else :
            columns.append("full_address")
            if( not (runParms[6] == None)) :
                columns.append("address_components")    
    
    if(geocid == sugm.ArcGISId) :
        
        if(geotype == sugm.QUERY) :  
            columns.append("lat_lng")
            if( not (runParms[3] == None)) :
                columns.append("full_address")
    
    BulkGeocodeResultsdf    =   sugm.BulkGeocodeResults(columns)    
    BulkGeocodeErrors       =   sugm.BulkGeocodeErrorLog()    

    return([BulkGeocodeResultsdf,BulkGeocodeErrors])


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
            run_google_bulk_geocode(sugm.QUERY,sugm.BULK_LOAD_GEOCODER,runParms,opstat)
            
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
            run_google_bulk_geocode(sugm.REVERSE,sugm.BULK_LOAD_GEOCODER,runParms,opstat)
        else :
            run_arcgis_bulk_geocode(runParms,opstat)
        
    else :
        subgw.display_bulk_geocoding(geocid,sugm.REVERSE)
        display_exception(opstat)
    

def process_bulk_geocoding_run_cmd(cmd) :
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
    
    opstat  =   opStatus()
    
    #sugw.display_geocode_main_taskbar() 
        
    if(cmd == sugm.BULK_START_GEOCODER) :
        print("process_bulk_geocoding_run_cmd : START",cmd)
        opstat  =   sugm.start_geocode_runner()
        
        if(not (opstat.get_status()) ) :
            display_exception(opstat)
    
    elif(cmd == sugm.BULK_STOP_GEOCODER) :
        print("process_bulk_geocoding_run_cmd : STOP",cmd)
        sugm.stop_geocode_runner()
        
    elif(cmd == sugm.BULK_PAUSE_GEOCODER) :
        print("process_bulk_geocoding_run_cmd : PAUSE",cmd)
        sugm.pause_geocode_runner()
        
    if(cmd == sugm.BULK_RESUME_GEOCODER) :
        print("process_bulk_geocoding_run_cmd : RESUME",cmd)
        sugm.pause_geocode_runner()
    
    elif(cmd == sugm.BULK_VIEW_ERRORS) :
        print("process_bulk_geocoding_run_cmd : ERRORS",cmd)
        errors  =   sugm.get_geocode_runner_error_log()
        print("error log",type(errors))

    elif(cmd == sugm.BULK_CHECKPT_GEOCODER) :
        print("process_bulk_geocoding_run_cmd : CHKPT",cmd)
        results  =   sugm.get_geocode_runner_results_log    
        print("results",type(results))
           



def run_bulk_geocoder_query(geocid, parms) :
    """
    * ---------------------------------------------------------
    * function : run the bulk geocode query 
    * 
    * parms :
    *  inparms  - bulk geocoder query input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    print("run_bulk_geocoder_query",geocid, "\n",parms)    
    
    #geocid  =   parms[0]
    inputs  =   parms[1]
    #get_bulk_coords(geocid,parms,state=sugm.LOAD)    
    return()

    
def run_bulk_geocoder_reverse(geocid, parms) :
    """
    * ---------------------------------------------------------
    * function : run a bulk geocode reverse 
    * 
    * parms :
    *  inparms  - geocoder reverse input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    print("run_bulk_geocoder_reverse",geocid, parms)
    return() 
    
    
    
"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Common Test bulk geocoders
#----------------------------------------------------------------------------
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







