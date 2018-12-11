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

import dfcleanser.common.help_utils as dfchelp

from dfcleanser.common.common_utils import (opStatus, get_parms_for_input, display_exception, 
                                            get_dfc_dataframe, display_status, displayParms)

import time
import googlemaps
import json




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   arcgis bulk coding
#--------------------------------------------------------------------------
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
        

"""
#------------------------------------------------------------------
#   test arcgis batch connector
#------------------------------------------------------------------
"""
def test_arcgis_connector(parms) :

    #geotype     =   parms[1]
    fparms      =   get_parms_for_input(parms[2],sugw.arcgis_geocoder_idList)  

    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()
    
    from dfcleanser.common.common_utils import RunningClock
    clock = RunningClock()
    clock.start()
    
    try :
    
        if(len(fparms) == 2) :
            test_arcgis_batch_connection(fparms[0],fparms[1],opstat)
            if(opstat.get_status()) :
                cfg.set_config_value(sugw.batch_arcgis_geocoder_id + "Parms",fparms)
                bulk_parms      =   cfg.get_config_value(subgw.batch_arcgis_query_id + "Parms")
                if(bulk_parms == None) :
                    bulk_parms  =   []
                    for i in range((len(subgw.batch_arcgis_query_idList)-7)) :
                        bulk_parms.append("")
                    
                bulk_parms[0]   =   fparms[0] 
                bulk_parms[1]   =   fparms[1]
                bulk_parms[6]   =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
                cfg.set_config_value(subgw.batch_arcgis_query_id + "Parms",bulk_parms)
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("arcGIS connect parms incomplete")
    
    except Exception as e:
        opstat.store_exception("Unable to connect to arcgis ",e)
    
    clock.stop()
    
    sugw.display_geocoders(sugm.ArcGISId,showfull=False,showNotes=False)
    
    if(opstat.get_status()) :
        displayParms("arcGIS Batch Size Settings",
                     ["MaxBatchSize","SuggestedBatchSize"],
                     [str(cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)),
                      str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))],
                     cfg.SWUtilities_ID)
        display_status("arcGIS batch geocoder connected to successfully")
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   arcgis batch geocoding
#--------------------------------------------------------------------------
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

    batchSize   =   int(runParms.get(subgw.batch_arcgis_query_labelList[6]))
    maxAddrs    =   int(runParms.get(subgw.batch_arcgis_query_labelList[7]))
    
    if((rowIndex + batchSize) > maxAddrs) :
        stopRow     =   maxAddrs - 1
    else :
        stopRow     =   (rowIndex + batchSize) - 1
        
    for i in range(rowIndex,stopRow) :
        arcgisbatch.append(get_geocode_address_string(addressMap,rowIndex))
        
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
        address_map     =   get_address_map(runParms.get(subgw.batch_arcgis_query_labelList[2]))
    
        if(opstat.get_status()) :
            display_geocoder_console(sugm.ArcGISId,runParms,opstat)
            load_geocode_runner(sugm.ArcGISId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : START\n",runParms)
        display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.RUNNING)
        start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : STOP\n",runParms)
        display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : PAUSE\n",runParms)
        display_geocoder_console(sugm.ArcGISId,None,opstat,sugm.PAUSING)


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
#   google bulk coding
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google query and reverse status codes
#--------------------------------------------------------------------------
"""
OK_STATUS                   =   "OK"
ZERO_RESULTS_STATUS         =   "ZERO_RESULTS"
OVER_DAILY_LIMIT_STATUS     =   "OVER_DAILY_LIMIT"
OVER_QUERY_LIMIT_STATUS     =   "OVER_QUERY_LIMIT"
REQUEST_DENIED_STATUS       =   "REQUEST_DENIED"
INVALID_REQUEST_STATUS      =   "INVALID_REQUEST"
UNKNOWN_ERROR_STATUS        =   "UNKNOWN_ERROR"


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
        address_map     =   get_address_map(runParms.get(subgw.bulk_google_query_input_labelList[2]))
    
        if(opstat.get_status()) :
            display_geocoder_console(sugm.GoogleId,runParms,opstat)
            load_geocode_runner(sugm.GoogleId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : START\n",runParms)
        display_geocoder_console(sugm.GoogleId,None,opstat,sugm.RUNNING)
        start_geocode_runner()
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : STOP\n",runParms)
        display_geocoder_console(sugm.GoogleId,None,opstat,sugm.STOPPING)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : PAUSE\n",runParms)
        display_geocoder_console(sugm.GoogleId,None,opstat,sugm.PAUSING)




def get_google_geocode_results(address,runParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a single google goeocode result
    * 
    * parms :
    *  address          - address to geocode
    *  runParms         - google geocode parms
    *  opstat           - status variable
    *
    * returns : 
    *    google geocode results
    * --------------------------------------------------------
    """
    geocode_results =   None
    
    client_id       =   runParms.get(subgw.bulk_google_query_input_labelList[0])
    client_secret   =   runParms.get(subgw.bulk_google_query_input_labelList[1])
    gmaps           =   googlemaps.Client(client_id=client_id, client_secret=client_secret)

    # Geocoding an address
    geocode_results =   gmaps.geocode(address)
    
    return(geocode_results)


def get_google_reverse_results(lat_long,runParms,opstat) :
    """
    * --------------------------------------------------------
    * function : get a single google reverse result
    * 
    * parms :
    *  lat_long         - [lat,long] to reverse
    *  runParms         - google reverse parms
    *  opstat           - status variable
    *
    * returns : 
    *    google geocode results
    * --------------------------------------------------------
    """
    reverse_results =   None
    
    client_id       =   runParms.get(subgw.bulk_google_query_input_labelList[0])
    client_secret   =   runParms.get(subgw.bulk_google_query_input_labelList[1])
    gmaps           =   googlemaps.Client(client_id=client_id, client_secret=client_secret)
    
    reverse_results =   gmaps.reverse_geocode((lat_long[0], lat_long[1]))
    
    return(reverse_results)



def process_google_geocode_status(geotype,results,opstat) :
    """
    * ----------------------------------------------------------
    * function : process the return status to determine state
    * 
    * parms :
    *  geotype          - geocode operation
    *  results          - run results
    *  opstat           - status variable
    *
    * returns : 
    *    True or False to continue running
    * --------------------------------------------------------
    """
    status  =   False

    if(geotype == sugm.GEOCODE_QUERY) :
        status  =   results.get_status()   

    else :
        status  =   results.get_status()   
    
    return(status)


def process_google_geocode_results(geotype,runparms,results,opstat) :
    """
    * ----------------------------------------------------------
    * function : process the geocode results
    * 
    * parms :
    *  geotype          - geocode operation
    *  runparms         - run parms
    *  results          - run results
    *  opstat           - status variable
    *
    * returns : 
    *    True or False to continue running
    * --------------------------------------------------------
    """

    status  =   False

    if(geotype == sugm.GEOCODE_QUERY) :
        status  =   results.get_status()   

    else :
        status  =   results.get_status()   
    
    return(status)


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
    status          =   None
    
    def init_(self,geocode_response) :
        self.results = geocode_response.get("results",None)
        self.status  = geocode_response.get("status",None)

    def get_status(self) :
        return(self.status)
    
    def get_error_message(self) :
        return(self.results.get("error_message",None))

    def get_lat_long(self) :
        
        lat_long    =   None
        
        geom        =   self.results.get("geometry",None)
        if(not(geom==None)) :
            loc         =   geom.get("location",None)
            if(not(loc==None)) :
                lat_long    =   [loc.get("lat"),loc.get("long",None)]
        
        # check values and return None if error
        return(lat_long)
        
    def get_address(self) :
        addr    = self.results.get("formatted_address",None)
        
        #check error codes
        return(addr)
 



       
"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google reverse results class
#----------------------------------------------------------------------------
#   google geocode results received from google reverse call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class google_reverse_results:
    
    results         =   None
    status          =   None
    
    def init_(self,reverse_response) :
        self.results = reverse_response.get("results",None)
        self.status  = reverse_response.get("status",None)

    def get_status(self) :
        return(self.status)

    def get_long_lat(self) :
        
        lat_long    =   None
        
        geom        =   self.results.get("geometry",None)
        if(not(geom==None)) :
            loc         =   geom.get("location",None)
            if(not(loc==None)) :
                lat_long    =   [loc.get("lat"),loc.get("long",None)]
        
        # check values and return None if error
        return(lat_long)
        
    def get_address(self) :
        addr    = self.results.get("formatted_address",None)
        
        #check error codes
        return(addr)
        
    def get_address_fields(self) :
        addr        =   self.results.get("address_components",None)
        addrcomps   =   google_address_components(addr)
        return(addrcomps) 

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google address components class
#----------------------------------------------------------------------------
#   google geocode results address received from google geocode call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

"""
#   address field identifiers
"""
ADDRESS             =   0
NEIGHBORHOOD        =   1
CITY                =   2
COUNTY              =   3
STATE               =   4
COUNTRY             =   5
ZIPCODE             =   6

"""
#   google address field keys
"""
ADDRESS_1_KEY       =   "street_number"
ADDRESS_2_KEY       =   "route"
NEIGHBORHOOD_KEY    =   "neighborhood"
CITY_KEY            =   "sublocality"
COUNTY_KEY          =   "administrative_area_level_2"
STATE_KEY           =   "administrative_area_level_1"
COUNTRY_KEY         =   "country"
ZIPCODE_KEY         =   "postal_code"


"""
#--------------------------------------------------------------------------
#  google address components class for getting individual address fields
#--------------------------------------------------------------------------
"""
class google_address_components:
    
    full_address_components  =   None
    long_address_components  =   None

    def init_(self,addr_comps) :
        self.address_components = addr_comps
        
        self.long_address_components = {}
        
        for i in len(self.full_address_components) :
            self.long_address_components.update({self.full_address_components(i).get("types")[0] : self.full_address_components(i).get("long_name")})

    def get_street_addr(self) :
        
        street_number   =   ""
        street          =   ""
        
        if(not(self.long_address_components.get(ADDRESS_1_KEY) == None)) :
            street_number = self.long_address_components.get(ADDRESS_1_KEY)
        if(not(self.long_address_components.get(ADDRESS_2_KEY) == None)) :
            street = self.long_address_components.get(ADDRESS_2_KEY)
        
        if( (len(street_number)>0) or (len(street)>0) ) :
            return(street_number + " " + street) 
        else :
            return(None)
        
    def get_neighborhood(self) :
        return(self.long_address_components.get(NEIGHBORHOOD_KEY,None))

    def get_city(self) :
        return(self.long_address_components.get(CITY_KEY,None))
        
    def get_county(self) :
        return(self.long_address_components.get(COUNTY_KEY,None))
        
    def get_state(self) :
        return(self.long_address_components.get(STATE_KEY,None))

    def get_country(self) :
        return(self.long_address_components.get(COUNTRY_KEY,None))
        
    def get_zip_code(self) :
        return(self.long_address_components.get(ZIPCODE_KEY,None))
        





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process bulk geocodinig common components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""



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
        subgw.display_bulk_geocoding(sugm.DISPLAY_BULK_GEOCODE_QUERY)
        display_exception(opstat)
       
    

def process_bulk_geocoding(optionId,parms) :
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
    print("\nprocess_bulk_geocoding",optionId,parms)
    
    sugw.display_geocode_main_taskbar() 
        
    fid     =   int(parms[0])
    geocid  =   int(parms[1])
    geotype =   int(parms[2])
    inputs  =   parms[3]
    
    if(not (inputs == None)) :
        inputs  =   json.loads(inputs)
        inputs  =   subgw.get_bulk_input_parms(geocid,inputs)
    #else :
        #inputs  =   cfg.get_config_value("arcgisbatchquery"+"Parms")
            
        if(geocid == sugm.GoogleId) :
            cfg.set_config_value(subgw.bulk_google_query_input_id+"Parms",inputs)
        else :
            cfg.set_config_value(subgw.batch_arcgis_query_id+"Parms",inputs)
           
    #print("process_bulk_geocoding",fid,geocid,inputs) 
        
    if(fid == sugm.BULK_GET_COORDS) :
        get_bulk_coords(geocid,inputs)           
    elif(fid == sugm.BULK_GET_ADDRESS_COLS) :
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)
    elif(fid == sugm.BULK_GET_LANGUAGES) :
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.LANGUAGE_TABLE)
    elif(fid == sugm.BULK_GET_REGIONS) :
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.REGION_TABLE)
    elif(fid == sugm.BULK_GET_COUNTRIES) :
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.REGION_TABLE)
    elif(fid == sugm.BULK_GET_CATEGORIES) :
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.CATEGORIES_TABLE)
        
    elif(fid == sugm.BULK_CLEAR) :
        if(geocid == sugm.GoogleId) :
            bparms = cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
            for i in range(len(bparms)) :
                if(i>0) : bparms[i] = ""
            cfg.set_config_value(subgw.bulk_google_query_input_id+"Parms",bparms)
        else :
            bparms = cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
            for i in range(len(bparms)) :
                if(i>0) : bparms[i] = ""
            cfg.set_config_value(subgw.batch_arcgis_query_id+"Parms",bparms)

        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)
        
    elif(fid == sugm.BULK_RETURN) :
        from dfcleanser.sw_utilities.sw_utility_geocode_control import display_geocode_utility
        display_geocode_utility(sugm.DISPLAY_GEOCODING)
                
    elif(fid == sugm.BULK_HELP) :
        if(geocid == sugm.GoogleId) :
            bparms = cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
        else :
            bparms = cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
            
        print("BULK_HELP",bparms)
        subgw.display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)

    elif(fid == sugm.BULK_START_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)

    elif(fid == sugm.BULK_PAUSE_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)
        
    elif(fid == sugm.BULK_STOP_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)



def process_test_bulk_connector(parms) :
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

    fid     =   int(parms[0]) 
        
    if(fid == sugm.BATCH_TEST_CONNECTOR) :
        test_arcgis_connector(parms)
            
    if(fid == sugm.BULK_GET_COORDS) :
        geocid  = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        geotype = int(parms[1])
        subgw.display_bulk_geocode_inputs(geocid,geotype)            
            
    if(fid == sugm.BATCH_CLEAR)     :
        cfg.drop_config_value("arcgisbatchgeocoder"+"Parms")
        cfg.drop_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)
        cfg.drop_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)            
            
        geotype = int(parms[1])
        sugw.display_geocoders(sugm.ArcGISId,showfull=False,showNotes=False)
            
    if(fid == sugm.BATCH_RETURN)    :
        geotype = int(parms[1])
        if(geotype == sugm.DISPLAY_GEOCODE_QUERY) :
            sugw.display_geocode_inputs(parms,sugm.GEOCODE_QUERY)
        else :
            sugw.display_geocode_inputs(parms,sugm.GEOCODE_REVERSE)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""

#--------------------------------------------------------------------------
#   bulk geocoding console html
#--------------------------------------------------------------------------
"""

bulk_start = """<div class="dfc-console-container" width='100%' style='overflow-x: hidden; overflow-y: hidden;'>"""
bulk_console_title = """<div class="dfc-console-title">
    <p class="dfc-console-title" style='text-align: center; font-size: 20px; font-family: Arial; font-weight: bold; margin: auto; overflow-x: hidden; overflow-y: hidden;'>Bulk Geocoding Run Console</p>
</div>
<br>
"""
    
bulk_console_container = """<div class="dfc-console-container" style=' width: 60%; text-align: center; margin: auto; border: 1px solid #428bca; overflow-x: hidden; overflow-y: hidden;'>
    <div style="text-align: center; margin:auto; margin-top:20px;">
        <table class="tableRowHoverOff" id="geocodeStatusBars" style="margin:auto; width: 90%;">
            <tbody>
"""
                
bulk_console_progress_row = """                    <tr class='dfc-progress-row' style='height: 30px;'>
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;'>"""

bulk_console_progress_col = """                        <td class='dfc-progress-col' style='width: 55%;'>
                            <div class='progress md-progress dfc-progress-div' style='height: 20px; '>
                                <div """

bulk_console_progress_col1 = """ class='progress-bar dfc-progress-bar' role='progressbar' style='height: 20px;'"""

bulk_console_progress_row_end = """                            </div>
                        </td>
                    </tr>
"""
                    
bulk_console_container_end = """            </tbody>
        </table>
    </div>
"""

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:100%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(22)">Run</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(23)">Pause</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(24)">Stop</button>
            </div>
        </div>
"""

bulk_console_status = """        <div style=' width: 30%; text-align: center; height: 30px; margin: auto;'>
            <p id='bulkstatus' style='height: 30px; padding-top: 5px; text-align: center; font-size: 14px; font-family: Arial; color: #474747; font-weight: bold; """
bulk_console_status1 = """ : margin: auto;'>"""
bulk_console_status2 = """</p>
        </div>
        <br>
"""

bulk_console_end = """</div>
"""
bulk_end = """</div>"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding console methods
#--------------------------------------------------------------------------
"""

def set_progress_bar_value(geocid,barid,barvalue) :
    
    if(geocid == sugm.ArcGISId) :
        
        if(barid == 0)  :   bid = "arcgistotaladdrs"
        else            :   bid = "arcgiserrorrate"
        
    elif(geocid == sugm.GoogleId) :

        if(barid == 0)  :   bid = "googletotaladdrs"
        else            :   bid = "googleerrorrate"

    set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(set_progress_bar_js,
                "fail to set progress bar : ",
                 str(bid))

"""
def set_status_bar(status) :
    
    btext   =   ""
    
    from dfcleanser.system.system_model import Green,Red,Yellow
    if(status == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(status == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(status == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"

    if(len(btext) > 0) :
        set_status_bar_js = "set_bulk_progress_status('" + str(btext) + "', '" + str(bcolor) + "');"
    
        print("set_status_bar_js",set_status_bar_js)
        from dfcleanser.common.common_utils import run_jscript
        run_jscript(set_status_bar_js,
                    "fail to set progress status color : ",
                    str(btext))
"""


def get_progress_bar_html(barParms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for a progress bar
    * 
    * parms :
    *  barParms   - [bartitle,barid,barmin,barmax,currentvalue]
    *
    * returns : 
    *  progress bar html
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import addattribute, addstyleattribute, new_line
    
    bar_html = ""
    bar_html = (bar_html + bulk_console_progress_row)
    bar_html = (bar_html + barParms[0] + "</td>" + new_line)
    bar_html = (bar_html + bulk_console_progress_col)
    bar_html = (bar_html + addattribute("id",barParms[1]))
    bar_html = (bar_html + bulk_console_progress_col1)    
    bar_html = (bar_html + addattribute("style",addstyleattribute("width",str(barParms[4])+"%")))
    bar_html = (bar_html + addattribute("aria-valuenow",str(barParms[4])))
    bar_html = (bar_html + addattribute("aria-valuemin",str(barParms[2])))
    bar_html = (bar_html + addattribute("aria-valuemax",str(barParms[3])))
    bar_html = (bar_html + ">" + str(barParms[4]) + "%" + "</div>" + new_line)
    bar_html = (bar_html + bulk_console_progress_row_end)
    
    return(bar_html)

def get_bulk_geocode_console_html(progressbarList,state) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for the bulk geocoding console
    * 
    * parms :
    *  progressbarList   - list of progress bars
    *  state             - state of console
    *
    * returns : console html
    * --------------------------------------------------------
    """
    
    console_html = ""
    console_html = (console_html + bulk_start)
    console_html = (console_html + bulk_console_title)
    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))    
    
    console_html = (console_html + bulk_console_container_end)  
    console_html = (console_html + bulk_console_commands)
    
    from dfcleanser.system.system_model import Green,Red,Yellow    
    if(state == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(state == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(state == sugm.STOPPING) :
        bcolor  =   Red
        btext   =   "Stopping"
    elif(state == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"
    elif(state == sugm.PAUSING) :
        bcolor  =   Yellow
        btext   =   "Pausing"
    
    console_html = (console_html + bulk_console_status)
    from dfcleanser.common.html_widgets import addstyleattribute
    console_html = (console_html + addstyleattribute("background-color",str(bcolor)))
    console_html = (console_html + bulk_console_status1 + btext)
    console_html = (console_html + bulk_console_status2)
    
    console_html = (console_html + bulk_console_end)  
    console_html = (console_html + bulk_end)
        
    return(console_html)     
        
        
def display_geocoder_console(geocid,runParms,opstat,state=sugm.STOPPED) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the bulk geocoding console
    * 
    * parms :
    *  geocid       - geocoder identifier
    *  runParms     - run parameters
    *  address_set  - address col names
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(geocid == sugm.ArcGISId) :
        
        if(not(runParms == None)) :
            from dfcleanser.common.common_utils import displayParms, get_parms_list_from_dict 
            parms   =   get_parms_list_from_dict(subgw.batch_arcgis_query_labelList,runParms) 
            displayParms("arcGIS Bulk Geocoding Parms",subgw.batch_arcgis_query_labelList,parms,"arcgisbulkparms")

        bar0 = ["Total Addresses Geocoded","arcgistotaladdrs",0,100,0]
        bar1 = ["Geocode Error Rate","arcgiserrorrate",0,100,0]
        
        progressBars    =   [bar0,bar1]
        
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
        from dfcleanser.common.common_utils import displayHTML
        
        displayHTML(console_html)
        
        print("\n")
        
    elif(geocid == sugm.GoogleId) :
        print("google console")




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding classes and helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Address Maps
#----------------------------------------------------------------------------
#   geocode address map for creating address string from dataframe columns
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

class AddressMap:
    
    def __init__(self, colindices,colvalues):
        self.colIndices     =   colindices
        self.colValues      =   colvalues

def get_geocode_address_string(address_map,rowIndex) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get address string from address cols input parms
    * 
    * parms :
    *  address_vector   - address vector of names and name types
    *  rowIndex         - dataframe row index
    *
    * returns : 
    *  address string to feed geocoder
    * --------------------------------------------------------
    """
    
    geocode_address     =   ""
    
    df  =   get_dfc_dataframe()
    
    for i in range(len(address_map.colsIndices)) :
        
        if(address_map.colsIndices[i] > -1) :
            geocode_address.append(df.iloc[rowIndex,address_map.colIndices[i]] + " ")
        else :
            geocode_address.append(address_map.colValues[i] + " ")
        
    return(geocode_address)



def get_address_map(address_cols) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get address object from address cols input parms
    * 
    * parms :
    *  address_cols       - address column names input parm
    *
    * returns : 
    *  address vector of names and name types
    * --------------------------------------------------------
    """
    
    colIndices  =   []
    colValues   =   []
    
    address_cols        =   address_cols.replace(",","")
    address_components  =   address_cols.split("+")
    
    colnames            =   cfg.get_dfc_dataframe().columns.values.tolist() 
   
    for i in range(len(address_components)) :

        if(address_components[i] in colnames) :
            colIndices.append(colnames.get_loc())
            colValues.append(None)
            
        else :
            colIndices.append(-1)
            colValues.append(address_components[i])
    
    addressMap  =    AddressMap(colIndices,colValues)       
            
    return(addressMap)

        
"""
#--------------------------------------------------------------------------
#   geocoding factory class to monitor and control threads
#--------------------------------------------------------------------------
"""
class BulkGeocodingFactory :
    
    # stsic class variables
    total_geocode_runs      =   0
    total_elapsed_run_time  =   0
    halt_all_geocoding      =   False
    bulkgeocodeparms        =   []
    starttime               =   0
    
    # stsic class methods
    @staticmethod
    def init_() :
        BulkGeocodingFactory.total_geocode_runs      =   0
        BulkGeocodingFactory.total_elapsed_run_time  =   0
        BulkGeocodingFactory.halt_all_geocoding      =   False 
    
    @staticmethod
    def increment_goecode_runs() :
        BulkGeocodingFactory.total_geocode_runs  =   BulkGeocodingFactory.total_geocode_runs + 1
        
    @staticmethod
    def increment_run_times(elapsed_time) :
        BulkGeocodingFactory.total_elapsed_run_time  =   BulkGeocodingFactory.total_elapsed_run_time + elapsed_time
        
    @staticmethod
    def get_total_geocode_runs() :
        return(BulkGeocodingFactory.total_geocode_runs)
        
    @staticmethod
    def get_geocode_runs_rate() :
        return(BulkGeocodingFactory.total_geocode_runs / BulkGeocodingFactory.total_elapsed_run_time)
        
    @staticmethod
    def process_error_code(geocoderid,results) :
        
        # check if stoppable error
        if(0) :
            return(True)    
        else :
            return(False)
        
    @staticmethod
    def set_halt_flag(halt_state) :
        BulkGeocodingFactory.halt_all_geocoding  =   halt_state       
 
    def __init__(self):
        BulkGeocodingFactory.total_geocode_runs      =   0
        BulkGeocodingFactory.total_elapsed_run_time  =   0
        BulkGeocodingFactory.halt_all_geocoding      =   False
        BulkGeocodingFactory.bulkgeocodeparms        =   []
        BulkGeocodingFactory.starttime               =   0
    
    def bulk_geocoder_controller_task(self):
        while (not(BulkGeocodingFactory.halt_all_geocoding)) :
            
            # check geocoder task stats 
            # and update control as needed
            # and display the run statistics
            
            # clean up any tasks and start new ones
            
            # delay 1/10 second
            time.sleep(0.1)
            
            
    def start_bulk_geocoder_controller(self,bulkgeocodeparms) :
        self.bulkgeocodeparms   =   bulkgeocodeparms
        threading.Thread(target=self.bulk_geocoder_controller_task).start()
        self.starttime = time.time()

    def stop_bulk_geocoder_controller(self):
        self.runGeocoder = False





"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Task Class
#----------------------------------------------------------------------------
#   geocoding task class for retrieving gecoding results
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
import threading

class GeocodeTask:
    
    geocoderId          =   -1
    geocoder_type       =   sugm.GEOCODE_QUERY
    runParms            =   None
    addressParms        =   None
    rowId               =   -1
    
    geocode_results     =   None
    opstat              =   None
        
    def __init__(self, geocoderId,geocodeType,rowid,runparms,addressparms):
        self.geocoderId         =   geocoderId
        self.geocoder_type      =   geocodeType
        self.runParms           =   runparms
        self.addressParms       =   addressparms
        self.rowId              =   rowid
        self.opstat             =   opStatus()
        self.geocode_results    =   None
        
        threading.Thread(target=self.geocoder_task).start()

    def geocoder_task(self):
        self.run_geocode_method()            

    def get_task_run_results(self) :
        return([self.rowId,self.geocode_results,self.opstat])
 
    def run_geocode_method(self) :
        
        
        
        if(self.geocoderId == sugm.GoogleId) :
            if(self.geocoder_type == sugm.GEOCODE_QUERY) :
                self.geocode_results    =   get_google_geocode_results(self.addressParms,self.runParms,self.opstat)
            elif(self.geocoder_type == sugm.GEOCODE_REVERSE) :
                self.geocode_results    =   get_google_reverse_results(self.addressParms,self.runParms,self.opstat) 

            if(self.opstat.get_status()) :
                if(not (process_google_geocode_status(self.geocoder_type,self.geocode_results,self.opstat))) :
                    stop_geocode_runner()
            else :
                stop_geocode_runner()    

        else :
            self.geocode_results    =   None            


class GeocodeTaskListMonitor:
    
    taskdict        =   {}
    maxtasks        =   0
    activetasks     =   0
        
    def __init__(self, maxtasksparm):
        self.taskdict        =   {}
        self.maxtasks        =   maxtasksparm
        self.activetasks     =   0
    
    def addtask(self, geocodetask, rowindex):
        self.taskdict.update({rowindex:geocodetask})
        self.activetasks     =   self.activetasks + 1
        
    def droptask(self, rowindex):
        self.taskdict.pop(rowindex)
        self.activetasks     =   self.activetasks - 1

    def more_tasks_available(self):
        if(self.activetasks < self.maxtasks) :
            return(True)
        else :
            return(False)
    
    def get_task_results(self):
        
        tlist   =   list(self.taskdict.keys())
        if(len(tlist) > 0) :
            tlist   =   tlist.sort()
            for i in range(len(tlist)) :
                gtask           =   self.taskdict.get(tlist[i]).get_task_run_results()
                gtask_results   =   gtask.get_task_run_results()
                if(not(gtask_results == None)) :
                    return(gtask_results)
                    
        return(None)

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
def load_geocode_runner(geocoderId,runParms,address_set) :
    dfc_Geocode_Runner.load_run(geocoderId,runParms,address_set)    

def start_geocode_runner() :
    dfc_Geocode_Runner.start_run() 
    
def stop_geocode_runner() :
    dfc_Geocode_Runner.stop_run() 
    
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
    
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 

def arcgis_run_next_batch(runParms) :
    print("arcgis_run_next_batch")

def google_run_next_geocode(runParms) :
    print("google_run_next_geocode")


       
class BulkGeocodeRunner:
    
    geocoder            =   None
    runParms            =   None
    addressParms        =   None
    
    rowindex            =   0
    state               =   sugm.STOPPED
    halt_all_geocoding  =   True
 
    geocodeTaskMonitor  =   None
       
    def __init__(self):
        self.geocoder           =   None
        self.runParms           =   None
        self.addressParms       =   None
        self.rowindex           =   0
        self.state              =   sugm.STOPPED
        self.halt_all_geocoding =   True
        
        self.geocodeTaskMonitor =   None

        
    def load_run(self,geocoderId,runParms,addressParms):
        self.geocoder           =   geocoderId
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        
        if(geocoderId == sugm.GoogleId) :
            self.geocodeTaskListMonitor  =   GeocodeTaskListMonitor(sugm.MAX_GOOGLE_TASKS)
        
    def start_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.rowindex           =   0
        self.start_bulk_geocode_runner(0)        

    def stop_run(self):
        self.state              =   sugm.STOPPING
        BulkGeocodeRunner.halt_all_geocoding = True
            
    def pause_run(self):
        self.state              =   sugm.PAUSING
        BulkGeocodeRunner.halt_all_geocoding = True
    
    def resume_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.start_bulk_geocode_runner(self.rowindex)        
        
    def get_run_state(self):
        return(self.state)
        
    def bulk_geocode_runner_task(self):
        while (not(BulkGeocodeRunner.halt_all_geocoding)) :
            
            if(self.geocoder == sugm.ArcGISId) :
                
                opstat              =   opStatus()
                next_batch_addrs    =   get_arcgis_batch_addresses(self.rowindex,self.runParms,self.addressParms)
                geocoder = None
                geocode_results     =   get_arcgis_geocode_batch(geocoder,next_batch_addrs,opstat)
                
                if(opstat.get_status()) :
                    
                    # batch retrieved ok
                    self.rowindex   =   process_arcgis_geocode_batch_results(geocode_results,self.runParms,opstat)
                    
                    if(self.rowindex >= int(self.runParms.get(subgw.batch_arcgis_query_labelList[7]))) :
                        BulkGeocodeRunner.halt_all_geocoding    =   True    
                
                else :
                    
                    BulkGeocodeRunner.halt_all_geocoding    =   True    
                    process_arcgis_geocode_batch_error(geocode_results,self.runParms,opstat) 

                
            elif(self.geocoder == sugm.GoogleId) :
                
                opstat      =   opStatus()
                
                if(self.geocodeTaskListMonitor.more_tasks_available()) :
                    next_addr       =   get_geocode_address_string(self.addressParms,self.rowindex)
                    geocodetask     =   GeocodeTask(sugm.GoogleId,sugm.GEOCODE_QUERY,self.runParms,next_addr)  
                    self.geocodeTaskListMonitor.addtask(geocodetask,self.rowindex)
                    
                    self.rowindex   =   self.rowindex + 1
                    
                    geocode_task_results    =   self.geocodeTaskMonitor.get_task_results()
                    if(not(geocode_task_results == None)) :
                        process_google_geocode_results(sugm.GEOCODE_QUERY,self.runparms,geocode_task_results,opstat)
                    
                    time.sleep(sugm.GOOGLE_DELAY)
                    
                else :
                    
                    if(not(geocode_task_results == None)) :
                        process_google_geocode_results(sugm.GEOCODE_QUERY,self.runparms,geocode_task_results,opstat)
                    
                    time.sleep(sugm.GOOGLE_DELAY)
                    
                if(self.rowindex > int(self.runParms.get(sugm.bulk_google_query_input_labelList[6]))) :
                    BulkGeocodeRunner.halt_all_geocoding = True    
                    
            else :
                BulkGeocodeRunner.halt_all_geocoding = True    
            
            
    def start_bulk_geocode_runner(self,rowIndex) :
        self.rowindex   =   rowIndex
        threading.Thread(target=self.bulk_geocode_runner_task).start()
    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        
