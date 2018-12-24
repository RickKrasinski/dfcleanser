"""
# sw_utility_bulk_geocode_control
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_console as subgc
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_model as subgm

from dfcleanser.common.common_utils import (get_parms_for_input, display_exception, display_notes, 
                                            display_status, displayParms, RunningClock, opStatus)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

import googlemaps
import json


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
    
            test_arcgis_batch_connection(connectParms[1],connectParms[2],opstat)
            if(opstat.get_status()) :
                cfg.set_config_value(subgw.batch_arcgis_geocoder_id + "Parms",connectParms)
                bulk_parms      =   cfg.get_config_value(subgw.batch_arcgis_query_id + "Parms")
                if(bulk_parms == None) :
                    bulk_parms  =   []
                    for i in range((len(subgw.batch_arcgis_query_idList)-5)) :
                        bulk_parms.append("")
                    
                bulk_parms[1]   =   connectParms[1] 
                bulk_parms[2]   =   connectParms[2]
                bulk_parms[11]  =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
                cfg.set_config_value(subgw.batch_arcgis_query_id + "Parms",bulk_parms)
                print("bulk_parms",bulk_parms,cfg.get_config_value(subgw.batch_arcgis_query_id + "Parms"))
    
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
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 


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

    batchSize   =   int(runParms.get(subgw.batch_arcgis_query_labelList[6]))
    maxAddrs    =   int(runParms.get(subgw.batch_arcgis_query_labelList[7]))
    
    if((rowIndex + batchSize) > maxAddrs) :
        stopRow     =   maxAddrs - 1
    else :
        stopRow     =   (rowIndex + batchSize) - 1
        
    for i in range(rowIndex,stopRow) :
        arcgisbatch.append(subgm.get_geocode_address_string(addressMap,rowIndex))
        
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
    
    #print("\nrun_arcgis_bulk_geocode :",state,"\n",runParms) 

    if(state == sugm.LOAD) :
        #print("\nrun_arcgis_bulk_geocode : LOAD\n",runParms) 
        address_map     =   subgm.get_address_map(runParms.get(subgw.batch_arcgis_query_labelList[2]))
    
        if(opstat.get_status()) :
            subgc.display_geocoder_console(sugm.ArcGISId,runParms,opstat)
            subgm.load_geocode_runner(sugm.ArcGISId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : START\n",runParms)
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.RUNNING)
        subgm.start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : STOP\n",runParms)
        subgc.display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : PAUSE\n",runParms)
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
    * returns : N/A
    * --------------------------------------------------------
    """
    
    geocode_list    =   []
    get_address     =   False
    
    if(runParms.get(subgw.batch_arcgis_query_labelList[12])  == "True") :
        get_address     =   True

    
    country         =   runParms.get(subgw.batch_arcgis_query_labelList[4],None)
    category        =   runParms.get(subgw.batch_arcgis_query_labelList[5],None)
    out_sr          =   runParms.get(subgw.batch_arcgis_query_labelList[13],None)

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
    *  geocoder         - arcgis geocoder
    *  addresslist      - lisy of addresses
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("process_arcgis_geocode_batch_results",batch_results,runParms,opstat)


def process_arcgis_geocode_batch_error(batch_results,runParms,opstat) :
    print("process_arcgis_geocode_batch_error",batch_results,runParms,opstat)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk coding methods
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
        
    #client_id       =   "dfcleanser"#runParms.get(subgw.bulk_google_query_input_labelList[0])
    #client_secret   =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"#runParms.get(subgw.bulk_google_query_input_labelList[1])
    #gmaps           =   googlemaps.Client(client_id=client_id, client_secret=client_secret)

    print("get_bulk_google_geocoder_connection",apikey,cid,csecret)
    
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
    
    print("validate_bulk_google_geocoder_parms",connectParms)    
    
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
    test_address    =   "11111 Euclid Ave, Cleveland OH "
    #geotype     =   parms[1]
    #fparms      =   get_parms_for_input(connectParms,subgw.google_bulk_geocoder_idList)  

    opstat      =   opStatus()
    validate_bulk_google_geocoder_parms(connectParms,opstat) 
    
    if(opstat.get_status()) :
    
        clock = RunningClock()
        clock.start()
    
        try :
            gmaps           =   get_bulk_google_geocoder_connection(connectParms[0],connectParms[1],connectParms[2],opstat)
            
            queryParms      =   [None,connectParms[0],connectParms[1],connectParms[2],None,None,None,None,None,None]
            test_results    =   get_google_geocode_results(test_address,gmaps,queryParms)            
            
            if(opstat.get_status()) :
                cfg.set_config_value(subgw.google_bulk_geocoder_id + "Parms",connectParms)
                bulk_parms      =   cfg.get_config_value(subgw.bulk_google_query_input_id + "Parms")
                if(bulk_parms == None) :
                    bulk_parms  =   []
                    for i in range((len(subgw.bulk_google_query_idList)-6)) :
                        bulk_parms.append("")
                    
                bulk_parms[1]   =   connectParms[0] 
                bulk_parms[2]   =   connectParms[1]
                bulk_parms[3]   =   connectParms[2]
                cfg.set_config_value(subgw.bulk_google_query_input_id + "Parms",bulk_parms)
    
        except Exception as e:
            opstat.store_exception("Unable to connect to google ",e)
    
        clock.stop()
    
    subgw.display_bulk_geocoders(sugm.GoogleId)
    
    if(opstat.get_status()) :
        display_status("Google bulk geocoder connected to successfully")
        display_google_test_results(test_address,test_results)
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 

def display_google_test_results(address,results) : 
    
    notes = []
    notes.append("Starting Address   : " + address)
    notes.append("  ")
    notes.append("Returned Address   : " + results.get_formatted_address())
    notes.append("Returned Latitude  : " + str(results.get_lat()))
    notes.append("Returned Longitude : " + str(results.get_lng()))
            
    display_notes(notes)
    
    print(results.get_results())


def run_google_bulk_geocode(runParms,opstat,state) :
    """
    * -------------------------------------------------------------------------- 
    * function : control the arcgis bulk geocoder
    * 
    * parms :
    *  runParms     - google run parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    #print("\nrun_arcgis_bulk_geocode :",state,"\n",runParms) 

    if(state == sugm.LOAD) :
        #print("\nrun_arcgis_bulk_geocode : LOAD\n",runParms) 
        address_map     =   subgm.get_address_map(runParms.get(subgw.bulk_google_query_input_labelList[2]))
    
        if(opstat.get_status()) :
            subgc.display_geocoder_console(sugm.GoogleId,runParms,opstat)
            subgm.load_geocode_runner(sugm.GoogleId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : START\n",runParms)
        subgc.display_geocoder_console(sugm.GoogleId,None,opstat,sugm.RUNNING)
        subgm.start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : STOP\n",runParms)
        subgc.display_geocoder_console(sugm.GoogleId,None,opstat,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : PAUSE\n",runParms)
        subgc.display_geocoder_console(sugm.GoogleId,None,opstat,sugm.PAUSING)




def get_google_geocode_results(address,geocodeConnector,queryParms) :
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
    
    print("get_google_geocode_results",address,len(address),"\n",queryParms)
    opstat          =   opStatus()
    geocode_results =   None
    gmaps           =   geocodeConnector 
    
    if(gmaps == None) :
        gmaps   =   get_bulk_google_geocoder_connection(queryParms[1],queryParms[2],
                                                        queryParms[3],opstat)        
    
    #client_id       =   "dfcleanser"#runParms.get(subgw.bulk_google_query_input_labelList[0])
    #client_secret   =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"#runParms.get(subgw.bulk_google_query_input_labelList[1])
    #gmaps           =   googlemaps.Client(client_id=client_id, client_secret=client_secret)
    
    if(opstat.get_status()) :   
        
        compParm    =   None
        boundsParm  =   None
        if(not (queryParms == None)) :
            regionParm      =   queryParms[8]
            languageParm    =   queryParms[9]
        else :
            regionParm      =   None
            languageParm    =   None
        
        try :
            geocode_results =   gmaps.geocode(address,
                                              components=compParm,
                                              bounds=boundsParm,
                                              region=regionParm,
                                              language=languageParm)
        
        except googlemaps.exceptions.ApiError :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.OverQueryLimitErrorMessage)
        except  :
            opstat.set_status(False)
            opstat.set_errorMsg("UNKNOWN EXCEPTION")
        
    current_geocode_results    =   google_geocode_results(geocode_results,opstat)
    return(current_geocode_results)


def get_google_reverse_results(lat_long,reverseParms) :
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
    
    #client_id       =   runParms.get(subgw.bulk_google_query_input_labelList[0])
    #client_secret   =   runParms.get(subgw.bulk_google_query_input_labelList[1])
    
    #client_id       =   "dfcleanser"#runParms.get(subgw.bulk_google_query_input_labelList[0])
    client_secret   =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"#runParms.get(subgw.bulk_google_query_input_labelList[1])
    #gmaps           =   googlemaps.Client(client_id=client_id, client_secret=client_secret)
    
    try :
        gmaps           =   googlemaps.Client(key=client_secret)
    
    except ValueError :
        opstat.set_status(False)
        opstat.set_errorMsg("CLIENT CREDENTIALS INVALID")
    except NotImplementedError :
        opstat.set_status(False)
        opstat.set_errorMsg("NotImplementedError")

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
            opstat.set_errorMsg(subgm.ApiErrorMessage)
        except googlemaps.exceptions.HTTPError :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.HTTPErrorMessage)
        except googlemaps.exceptions.Timeout :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.TimeoutErrorMessage)
        except googlemaps.exceptions.TransportError :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.TransportErrorMessage)
        except googlemaps.exceptions._RetriableRequest :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.RetriableRequestErrorMessage)
        except googlemaps.exceptions._OverQueryLimit :
            opstat.set_status(False)
            opstat.set_errorMsg(subgm.OverQueryLimitErrorMessage)
        except  :
            opstat.set_status(False)
            opstat.set_errorMsg("UNKNOWN EXCEPTION")
    
    current_reverse_results  =   google_reverse_results(reverse_results,opstat)
    return(current_reverse_results)


def process_google_geocode_results(inputParms,runParms,geocode_results) :
    print("process_google_geocode_results",inputParms,runParms,geocode_results)
    
def process_google_reverse_results(inputParms,runParms,reverse_results) :
    print("process_google_reverse_results",inputParms,runParms,reverse_results)
    
def process_google_geocoding_errors(geotype,inputParms,runParms,geocoding_results) :
    print("process_google_geocoding_errors",inputParms,runParms,geocoding_results)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process bulk geocodinig common components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""    
def get_header_columns_map(geocid,geotype,runParms) :
    print("get_header_columns",geocid,geotype,runParms)
    
    columns     =   ["rowIndex", "inputval"]
    widths      =   []

    if(geocid == sugm.GoogleId) :
        
        if(geotype == sugm.QUERY) :  
            columns.append("lat_lng")
            if( not (runParms[7] == None)) :
                columns.append("full_address")
                widths  =   [10,30,20,40]
            else :
                widths  =   [10,60,30]
            
        else :
            columns.append("full_address")
            if( not (runParms[6] == None)) :
                columns.append("address_components")    
                widths  =   [10,20,35,35]
            else :
                widths  =   [10,30,60]
    
    if(geocid == sugm.ArcGISId) :
        
        if(geotype == sugm.QUERY) :  
            columns.append("lat_lng")
            if( not (runParms[13] == None)) :
                columns.append("full_address")
                widths  =   [10,30,20,40]
            else :
                widths  =   [10,60,30]
            
    return([columns,widths])           


def init_geocoding_data_structures(geocid,geotype,runParms) :
    
    column_headers_map      =   get_header_columns_map(geocid,geotype,runParms)   
    BulkGeocodeResultsdf    =   BulkGeocodeResults(column_headers_map)    

    BulkGeocodeErrors       =   BulkGeocodeErrorLog()    

    return([BulkGeocodeResultsdf,BulkGeocodeErrors])


def get_bulk_coords(geocid,inputs,state=sugm.LOAD) :
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
    
    print("get_bulk_coords",geocid,state,"\n",inputs)
    
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
            run_google_bulk_geocode(runParms,opstat,state)
        else :
            run_arcgis_bulk_geocode(runParms,opstat,state)
        
    else :
        subgw.display_bulk_geocoding(geocid,sugm.QUERY)
        display_exception(opstat)
       
    
def get_bulk_addresses(geocid,inputs,state=sugm.LOAD) :
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
    
    print("get_bulk_coords",geocid,state,"\n",inputs)
    
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
            run_google_bulk_geocode(runParms,opstat,state)
        else :
            run_arcgis_bulk_geocode(runParms,opstat,state)
        
    else :
        subgw.display_bulk_geocoding(geocid,sugm.REVERSE)
        display_exception(opstat)
    

def process_bulk_geocoding_run_cmd(geocid, geotype, cmd,parms) :
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
    print("\nprocess_bulk_geocoding_run_cmd",geocid,cmd,parms)
    
    sugw.display_geocode_main_taskbar() 
        
    #geocid  =   int(parms[1])
    #inputs  =   parms[3]
    
    if(cmd == sugm.BULK_START_GEOCODER) :
        get_bulk_addresses(geocid,parms,cmd)

    elif(cmd == sugm.BULK_PAUSE_GEOCODER) :
        get_bulk_addresses(geocid,parms,cmd)
        
    elif(cmd == sugm.BULK_STOP_GEOCODER) :
        get_bulk_addresses(geocid,parms,cmd)
    
            
                



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
    
    return()

    """    
    #geocid  =   inparms[1]
    #parms   =   inparms[2]
    opstat  =   opStatus()
    
    opstat = sugw.validate_cmd_parms(sugm.QUERY,geocid,parms)
    
    if(not opstat.get_status()) :
        
        sugw.display_comp_addr_geocode_inputs(inparms)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)

        if(opstat.get_status()) :
            
            try :
                
                queryparms = get_bulk_query_parms(geocid,parms)
                
                #print("get_geocoder_df_addresses",queryparms)
                
                cols        =   queryparms[0]
                
                colnames    =   []
                
                if(queryparms[1].find(",") > 1) :
                    cnames = queryparms[1].split(",")
                    for i in range(len(cnames)) :
                        colnames.append(cnames[i])
                else :
                    colnames.append(queryparms[1])

                if(len(queryparms[2]) > 0) :
                    deloldcols  =   True
                else :
                    deloldcols  =   False
                
                qparms  =   sugw.get_geocoder_cmd_kwargs(sugm.QUERY,geocid)
                
                if(len(qparms) > 3) :
                    qparms  =   qparms[3:]
                
                invalidaddr     =   []
                timeoutaddr     =   []
                parseerror      =   []
                
                stopRun         =   False
                
                totalTimeouts   =   0
                MAX_TIMEOUTS    =   100
                
                totalParseErrors   =   0
                MAX_PARSEERRORS    =   200
                
                addresses       =   []
                latitudes       =   []
                longitudes      =   []
                latlongs        =   []
                
                # for each row in the dataframe
                for i in range(len(cfg.get_dfc_dataframe())) :
                    
                    if(stopRun) :  
                        i = len(cfg.get_dfc_dataframe()) + 1
                    else :
                        
                        query = ""
                        for j in range(len(cols[0])) :
                            if(cols[1][j]) :
                                val = cfg.get_dfc_dataframe().iloc[i][cols[0][j]]
                                import pandas as pd
                                if(not pd.isnull(val)) :
                                    query = query + " " + str(val) 
                            else :
                                query = query + " " + str(cols[0][j])
                
                        if(len(query > 0)) :
                        
                            import geopy as gp
                        
                            try :    
                                if(len(qparms) > 0) :
                                    address, (latitude, longitude) = geolocator.geocode(query, **qparms) 
                                else :
                                    address, (latitude, longitude) = geolocator.geocode(query)
                                
                                    if(len(colnames) == 1) :
                                        latlongs.append((latitude, longitude)) 
                                    else :
                                        latitudes.append(latitude)
                                        longitudes.append(longitude)
                                        if(len(colnames) == 3) :
                                            addresses.append(address)
                                        
                                addresses.append(address)
                                latitudes.append(latitude)
                                longitudes.append(longitude)
                                
                            except gp.exc.ConfigurationError as e:
                                opstat.store_exception("ConfigurationError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderServiceError as e:
                                opstat.store_exception("GeocoderServiceError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderQueryError as e:
                                opstat.store_exception("GeocoderQueryError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderQuotaExceeded as e:
                                opstat.store_exception("GeocoderQuotaExceeded Error",e)
                                stopRun = True
                            except gp.exc.GeocoderAuthenticationFailure as e:
                                opstat.store_exception("GeocoderAuthenticationFailure",e)
                                stopRun = True
                            except gp.exc.GeocoderInsufficientPrivileges as e:
                                opstat.store_exception("GeocoderInsufficientPrivileges Error",e)
                                stopRun = True
                            except gp.exc.GeocoderTimedOut as e:
                                
                                totalTimeouts = totalTimeouts + 1
                                
                                if(totalTimeouts > MAX_TIMEOUTS) :
                                    stopRun = True
                                    opstat.store_exception("GeocoderTimedOut Error",e)
                                else :
                                    addresses.append(None)
                                    latitudes.append(None)
                                    longitudes.append(None)
                                    timeoutaddr.append(i)
    
                            except gp.exc.GeocoderUnavailable as e:
                                opstat.store_exception("GeocoderUnavailable Error",e)
                                stopRun = True
                            except gp.exc.GeocoderParseError as e:
                                
                                totalParseErrors = totalParseErrors + 1
                                
                                if(totalParseErrors > MAX_PARSEERRORS) :
                                    stopRun = True
                                    opstat.store_exception("GeocoderParseError Error",e)
                                else :
                                    addresses.append(None)
                                    latitudes.append(None)
                                    longitudes.append(None)
                                    parseerror.append(i)
                                    
                            except gp.exc.GeocoderNotFound as e:
                                opstat.store_exception("GeocoderNotFound Error",e)
                                stopRun = True
    
                        else :
                            invalidaddr.append(i)
                            
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()

        if(opstat.get_status()) :
            
            try :
                
                # create new lat long cols
                from dfcleanser.data_transform.data_transform_columns_widgets import add_column
                
                if(len(colnames) == 1) :
                    add_column(colnames[0],latlongs,opstat) 
                else :
                    add_column(colnames[0],latitudes,opstat)
                    add_column(colnames[1],longitudes,opstat)
                    if(len(colnames) == 3) :
                        add_column(colnames[2],addresses,opstat)
                
                # delete old cols
                if(deloldcols) :
                    for i in range(len(queryparms[1])) :
                        if(queryparms[1][i]) :
                            cfg.set_current_dfc_dataframe(cfg.get_dfc_dataframe().drop([queryparms[0][i]],axis=1))
                
            except Exception as e:
                opstat.store_exception("Unable to save coors columns",e)

            print("\n")
            display_status("dataframe coordinates loaded successfully")
            
            notes = []
            notes.append("Total Coords Loaded   : " + str(len(cfg.get_dfc_dataframe())))
            notes.append("  ")
            notes.append("Total Timeouts        : " + str(len(timeoutaddr)))
            notes.append("Total Parse Errors    : " + str(len(parseerror)))
            
            display_notes(notes)
            
        else :
            display_exception(opstat)
    """
    
def run_bulk_geocoder_reverse(inparms) :
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

    print("run_bulk_geocoder_reverse",inparms)
    return() 
    
    
    

def validate_bulk_geocode_connect_parms(geocid) :

    print("validate_geocode_connect_parms",geocid) 
    fparms    =   cfg.get_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms")
    
    print("connectparms",fparms)
    
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


def process_test_bulk_connector(geocid,gcparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : process commands from test the bulk geocoder
    * 
    * parms :
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("process_test_bulk_connector",geocid,gcparms)
    
     
    
    return()



def test_bulk_geocoder(geocid,inputs) :
    print("test_bulk_geocoder",geocid,inputs)

    if(geocid == sugm.ArcGISId) :
        test_arcgis_batch_connector(inputs)
    elif(geocid == sugm.GoogleId) :
        test_google_bulk_connector(inputs)    


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google geocode results class
#----------------------------------------------------------------------------
#   google geocode results received from google geocode call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class google_geocode_results:
    
    results         =   None
    opstat          =   None
    
    def __init__(self,geocode_results,opstat) :
        self.results = geocode_results[0]
        self.opstat  = opstat

    def get_lat(self) :
        return(self.results.get("geometry").get("location").get("lat"))
    def get_lng(self) :
        return(self.results.get("geometry").get("location").get("lng"))
    def get_formatted_address(self) :
        return(self.results.get("formatted_address"))
    def get_location_type(self) :
        return(self.results.get("geometry").get("location_type"))
    def get_place_id(self) :
        return(self.results.get("place_id"))
    def get_types(self) :
        return(self.results.get("types"))

    def get_results(self) :
        return(self.results)
 
    def get_status(self) :
        return(self.opstat.get_status())
    def get_error_message(self) :
        return(self.opstat.get_errorMsg())


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google reverse results class
#----------------------------------------------------------------------------
#   google reverse results received from google reverse call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class google_reverse_results:
    
    results         =   None
    opstat          =   None
    
    def __init__(self,reverse_results,opstat) :
        self.results = reverse_results[0]
        self.opstat  = opstat

    def get_lat(self) :
        return(self.results.get("geometry").get("location").get("lat"))
    def get_lng(self) :
        return(self.results.get("geometry").get("location").get("lng"))
    def get_formatted_address(self) :
        return(self.results.get("formatted_address"))
    def get_location_type(self) :
        return(self.results.get("geometry").get("location_type"))
    def get_place_id(self) :
        return(self.results.get("place_id"))
    def get_types(self) :
        return(self.results.get("types"))

    def get_results(self) :
        return(self.results)
 
    def get_status(self) :
        return(self.opstat.get_status())
    def get_error_message(self) :
        return(self.opstat.get_errorMsg())


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google address components class
#----------------------------------------------------------------------------
#   google geocode results address received from google geocode/reverse call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------
#-  Google geocode address component types
#----------------------------------------------------------------------------
"""
GOOGLE_GEOCODER_STREET_NUMBER_ID        =   'street_number'
GOOGLE_GEOCODER_ROUTE_ID                =   'route'
GOOGLE_GEOCODER_NEIGHBORHOOD_ID         =   'neighborhood'
GOOGLE_GEOCODER_LOCALITY_ID             =   'locality'
GOOGLE_GEOCODER_SUBLOCALITY_ID          =   'sublocality'
GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID        =   'administrative_area_level_1'
GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID        =   'administrative_area_level_2'
GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID        =   'administrative_area_level_3'
GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID        =   'administrative_area_level_4'
GOOGLE_GEOCODER_COUNTRY_ID              =   'country'
GOOGLE_GEOCODER_POSTAL_CODE_ID          =   'postal_code'

"""
#----------------------------------------------------------------------------
#   google address components common us field defs
#----------------------------------------------------------------------------
"""
google_address_components_comments  =   {GOOGLE_GEOCODER_STREET_NUMBER_ID: "STREET NUMBER",
                                         GOOGLE_GEOCODER_ROUTE_ID: "STREET",
                                         GOOGLE_GEOCODER_NEIGHBORHOOD_ID: "NEIGHBORHOOD",
                                         GOOGLE_GEOCODER_LOCALITY_ID: "LOCALITY",
                                         GOOGLE_GEOCODER_SUBLOCALITY_ID: "CITY",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID: "STATE",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID: "COUNTY",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID: "AREA 3",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID: "AREA 4",
                                         GOOGLE_GEOCODER_COUNTRY_ID: "COUNTRY",
                                         GOOGLE_GEOCODER_POSTAL_CODE_ID: "ZIPCODE"}

"""
#----------------------------------------------------------------------------
#   default address for googl;e address components
#----------------------------------------------------------------------------
"""
default_address_format                  =  [GOOGLE_GEOCODER_STREET_NUMBER_ID,
                                            GOOGLE_GEOCODER_ROUTE_ID,
                                            GOOGLE_GEOCODER_NEIGHBORHOOD_ID,
                                            GOOGLE_GEOCODER_LOCALITY_ID,
                                            GOOGLE_GEOCODER_SUBLOCALITY_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID,
                                            GOOGLE_GEOCODER_COUNTRY_ID,
                                            GOOGLE_GEOCODER_POSTAL_CODE_ID]


def get_address_from_components(addr_comps,addr_map,short=True) :
    
    out_address     =   ""
    
    if(addr_comps != None) :
        if(len(addr_comps) > 0) :
            for i in range(len(addr_map)) :
                for j in range(len(addr_comps)) :
                    ctypes  =   addr_comps[j].get("types",None)
                    if(ctypes != None) :
                        if(addr_map[i] in ctypes) :
                            if(short) :
                                out_address     =   out_address + addr_comps[j].get("short_name"," ") + " "
                            else :
                                out_address     =   out_address + addr_comps[j].get("long_name"," ") + " "    
                            break
    
    return(out_address)                    
                        

"""
#--------------------------------------------------------------------------
#  google address components class for getting individual address fields
#--------------------------------------------------------------------------
"""
class google_address_components:
    
    address_components  =   None

    def init_(self,addr_comps) :
        self.address_components = addr_comps
        

    def get_address_component(self,address_component_id,shortName=True) :
        
        if(self.address_components != None) :
            if(len(self.address_components) > 0) :
                for i in range(len(self.address_components)) :
                    ctypes  =   self.address_components[i].get("types",None)
                    if(ctypes != None) :
                        if(address_component_id in ctypes) :
                            if(shortName) :
                                return(self.address_components[i].get("short_name"," "))
                            else :
                                return(self.address_components[i].get("long_name"," "))  
        
    def get_full_address_from_components(self,addr_format,shortName=True) :
        
        out_address     =   ""
        
        if(addr_format != None) :
            if(len(addr_format) > 0) :
                for i in range(len(addr_format)) :
                    out_address     =   out_address + self.get_address_component(addr_format[i],shortName)
                    
        

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding results class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_RESULTS_DF_TITLE          =   "Current_Geocoding_Results_df"
GEOCODING_RESULTS_DF_NOTES          =   "Bulk Geocoding Results dataframe"

MAX_RESULTS_DISPLAYED               =   200
DISPLAY_RESULTS_SIZE                =   20


class BulkGeocodeResults:
    
    geocode_results_df      =   None
    column_headers_map      =   []
    
    def __init__(self,column_headers_mapParm,dftitle=None):
        self.column_headers_map = column_headers_mapParm
        
        if(dftitle == None) :
            import pandas as pd
            self.geocode_results_df = pd.DataFrame(columns=column_headers_mapParm[0])
            dfc_geocode_results_df  = cfg.dfc_dataframe(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df,GEOCODING_RESULTS_DF_NOTES)
            cfg.add_dfc_dataframe(dfc_geocode_results_df)
        
        else :
            self.geocode_results_df  = cfg.get_dfc_dataframe(dftitle)

    def add_result(self,rowResults):
        import pandas as pd
        new_results_df   =   pd.Dataframe([rowResults],columns=self.column_headers)
        self.geocode_results_df.append(new_results_df)
        
    def show_results(self, startrowindex) :
        print("show_results",startrowindex)

        resultsHeader      =   self.column_headers_map[0]
        resultsRows        =   []
        resultsWidths      =   self.column_headers_map[1]
        resultsAligns      =   ["center"]
        for i in range((len(self.column_headers_map[0])-1)) :
            resultsAligns.append("left")    

        for i in range(MAX_RESULTS_DISPLAYED) :
            df      =   cfg.get_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
            result  =   df.loc[df[self.column_headers_map[0]] == startrowindex+i] 
            result  =   result.tolist()
        
            resultrow   =   []
            for i in range(len(self.column_headers_map[0])) :
                resultrow.append(result[i])
            resultsRows.append(resultrow)
        
        results_table = None
                
        results_table = dcTable("Geocode Results","geoocoderreslstable",
                                cfg.SWGeocodeUtility_ID,
                                resultsHeader,resultsRows,
                                resultsWidths,resultsAligns)
            
        results_table.set_tabletype(ROW_MAJOR)
        results_table.set_rowspertable(ERRORS_TABLE_SIZE)

        listHtml = get_row_major_table(results_table,SCROLL_NEXT,False)

        #print(listHtml)        
        return(listHtml)

    def get_results_count(self) :    
        return(len(self.geocode_results_df))

    def clear_results(self) :    
        self.geocode_results_df = None
        cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)

    def get_geocoding_df(self) :    
        return(self.geocode_results_df)


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding error log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_ERROR_LOG_DF_TITLE            =   "Current_Geocoding_Error_Log_df"
GEOCODING_ERROR_LOG_DF_NOTES            =   "Geocoding Error Logging Dataframe"

GEOCODING_ERROR_LOG_COULUMN_NAME_LIST   =   ['rowid','geocode_input_value','error_message']

MAX_ERRORS_DISPLAYED                    =   200
ERRORS_TABLE_SIZE                       =   20


class BulkGeocodeErrorLog:
    
    error_log_df    =   None
        
    def __init__(self):
        import pandas as pd
        self.error_log_df = pd.DataFrame(columns=GEOCODING_ERROR_LOG_COULUMN_NAME_LIST)
        dfc_geocode_error_log = cfg.dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df,GEOCODING_ERROR_LOG_DF_NOTES)
        cfg.add_dfc_dataframe(dfc_geocode_error_log)

    def log_error(self,rowindex,inputValue,errorMsg):
        import pandas as pd
        new_error_df   =   pd.Dataframe([rowindex,inputValue,errorMsg],columns=GEOCODING_ERROR_LOG_COULUMN_NAME_LIST)
        self.error_log_df.append(new_error_df)
        
    def show_errors(self, startrowindex) :
        
        print("get_geocode_error_log_table",startrowindex)

        errorsHeader      =   ["rowid","input value","error message"]
        errorsRows        =   []
        errorsWidths      =   [10,35,55]
        errorsAligns      =   ["center","left","left"]

        for i in range(MAX_ERRORS_DISPLAYED) :
            df      =   cfg.get_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
            cerror  =   df.loc[df[GEOCODING_ERROR_LOG_COULUMN_NAME_LIST[0]] == startrowindex+i] 
            cerror  =   cerror.tolist()
        
            cerrorrow = [cerror[0],cerror[1],cerror[2]]
            errorsRows.append(cerrorrow)
        
        errors_table = None
                
        errors_table = dcTable("Geocode Errors","geoocodererrortable",
                               cfg.SWGeocodeUtility_ID,
                               errorsHeader,errorsRows,
                               errorsWidths,errorsAligns)
            
        errors_table.set_tabletype(ROW_MAJOR)
        errors_table.set_rowspertable(ERRORS_TABLE_SIZE)

        listHtml = get_row_major_table(errors_table,SCROLL_NEXT,False)

        #print(listHtml)        
        return(listHtml)
 
    def get_error_count(self) :    
        return(len(self.error_log_df))

    def clear_error_log(self) :    
        self.error_log_df = None
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)




