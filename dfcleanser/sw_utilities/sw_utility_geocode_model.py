"""
# sw_utility_geocode_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)
from dfcleanser.common.common_utils import (get_dfc_dataframe)
import dfcleanser.common.cfg as cfg


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
ArcGISId                    =   0
BaiduId                     =   1
BingId                      =   2
GoogleId                    =   7
OpenMapQuestId              =   9
NominatimId                 =   11

supported_Geocoders         =   [ArcGISId,BaiduId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BaiduId,BingId,GoogleId,NominatimId]

supported_Bulk_Geocoders    =   [ArcGISId,BaiduId,BingId,GoogleId]
supported_Bulk_Reverses     =   [BaiduId,BingId,GoogleId]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Bulk Geocoder runtime settings
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
GOOGLE_DELAY                =   0.05
BING_DELAY                  =   0.5
BAIDU_DELAY                 =   1

GOOGLE_TIMEOUT              =   5
BING_TIMEOUT                =   5
BAIDU_TIMEOUT               =   5
ARCGIS_TIMEOUT              =   45

GOOGLE_RETRY_LIMIT          =   3
BING_RETRY_LIMIT            =   3
BAIDU_RETRY_LIMIT           =   3

GOOGLE_THREAD_LIMIT         =   10
BING_THREAD_LIMIT           =   15
BAIDU_THREAD_LIMIT          =   10


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Function Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_MAIN_GEOCODING          =   0

PROCESS_GEOCODER                =   1

CLEAR_GEOCODE_FORM              =   2
DISPLAY_GEOCODER                =   3
TEST_GEOCODER                   =   4
DISPLAY_GEOCODING               =   5
GET_TABLE                       =   6
PROCESS_GEOCODING               =   7


DISPLAY_FULL_GEOCODING          =   12

CHANGE_BULK_GEOCODER            =   13

DISPLAY_BULK_GEOCODER           =   14
PROCESS_BULK_GEOCODER           =   15

BULK_LOAD_GEOCODER              =   19
BULK_START_GEOCODER             =   20
BULK_STOP_GEOCODER              =   21
BULK_PAUSE_GEOCODER             =   22
BULK_RESUME_GEOCODER            =   23
BULK_VIEW_ERRORS                =   24
BULK_CHECKPT_GEOCODER           =   25
BULK_RESULTS_GEOCODER           =   26

PROCESS_BULK_RESULTS            =   30
REPORT_GEOCODE_RUN_ERROR        =   31



"""
#--------------------------------------------------------------------------
#   geocode utilities commands
#--------------------------------------------------------------------------
"""
DISPLAY_GEOUTILS                =   40

DISPLAY_DISTANCE                =   41
PROCESS_DISTANCE                =   42
DISPLAY_DF_DISTANCE             =   43
PROCESS_DF_DISTANCE             =   44

DISPLAY_CENTER                  =   45
PROCESS_CENTER                  =   46
DISPLAY_DF_CENTER               =   47
PROCESS_DF_CENTER               =   48

DISPLAY_TUNING                  =   49
PROCESS_TUNING                  =   50


"""
#--------------------------------------------------------------------------
#   bulk results commands
#--------------------------------------------------------------------------
"""

DISPLAY_BULK_RESULTS_BASE                       =   0
DISPLAY_BULK_RESULTS_CONCAT                     =   1
DISPLAY_BULK_RESULTS_EXPORT_CSV                 =   2
DISPLAY_BULK_RESULTS_EXPORT_SQL                 =   3
DISPLAY_BULK_REVERSE_RESULTS_CONCAT             =   4 

DISPLAY_BULK_RESULTS_CONCAT_PROCESSED           =   5
DISPLAY_BULK_RESULTS_CSV_PROCESSED              =   6

PROCESS_BULK_RESULTS_CONCAT_PROCESS             =   7
PROCESS_BULK_RESULTS_CONCAT_CLEAR               =   8
PROCESS_BULK_RESULTS_CONCAT_RETURN              =   9
PROCESS_BULK_RESULTS_CONCAT_HELP                =   10

PROCESS_BULK_REVERSE_RESULTS_CONCAT_PROCESS     =   11
PROCESS_BULK_REVERSE_RESULTS_CONCAT_CLEAR       =   12
PROCESS_BULK_REVERSE_RESULTS_CONCAT_RETURN      =   13
PROCESS_BULK_REVERSE_RESULTS_CONCAT_HELP        =   14

PROCESS_BULK_RESULTS_CSV_PROCESS                =   15
PROCESS_BULK_RESULTS_CSV_CLEAR                  =   16
PROCESS_BULK_RESULTS_CSV_RETURN                 =   17
PROCESS_BULK_RESULTS_CSV_HELP                   =   18

DISPLAY_BULK_RESULTS                            =   19 

DISPLAY_BULK_SOURCE_DF                          =   20 
DISPLAY_BULK_RESULTS_DF                         =   21 
DISPLAY_BULK_ERRORS_DF                          =   22 
DISPLAY_BULK_RESULTS_RETURN                     =   23 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding constants
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

GEOCODER                    =    0
QUERY                       =    1
REVERSE                     =    2

DISTANCE_HELP               =   8
DISTANCE_DF_HELP            =   8

INTERACTIVE                 =   0
BULK                        =   1
BULK_TUNING                 =   2




"""
#--------------------------------------------------------------------------
#   bulk geocoding input form table ids - tables loaded in grid
#--------------------------------------------------------------------------
"""
GEOCODERS_TABLE             =   -1
COLNAMES_TABLE              =   0
LANGUAGE_TABLE              =   1
REGION_TABLE                =   2
CATEGORIES_TABLE            =   3
ADDRESS_COMPONENTS_TABLE    =   4
RESULT_TYPES_TABLE          =   5
LOCATION_TYPES_TABLE        =   6


"""
#--------------------------------------------------------------------------
#   bulk geocoder running commands 
#--------------------------------------------------------------------------
"""

BATCH_TEST_CONNECTOR        =   14
BATCH_CLEAR                 =   15
BATCH_RETURN                =   16
BATCH_HELP                  =   17

BULK_GET_ADDRESS_COMPONENTS =   18
BULK_GET_RESULT_TYPES       =   19
BULK_GET_LOCATION_TYPES     =   20


"""
#--------------------------------------------------------------------------
#   bulk geocoder currebt state
#--------------------------------------------------------------------------
"""
RUNNING                     =   0
STOPPED                     =   1
PAUSED                      =   2
STARTING                    =   3
STOPPING                    =   4
PAUSING                     =   5
FINISHED                    =   6
ERROR_LIMIT                 =   7

CHECKPOINT_STARTED          =   8
CHECKPOINT_COMPLETE         =   9


LOAD                        =   10
START                       =   11
STOP                        =   12
PAUSE                       =   13
RESUME                      =   14


GEOCODE_BAR                 =   0
ERROR_BAR                   =   1




def get_geocoder_title(geoid) :
    
    if(geoid == ArcGISId) :
        return("ArcGIS")
    elif(geoid == BingId) :
        return("Bing")
    elif(geoid == GoogleId) :
        return("GoogleV3")
    elif(geoid == OpenMapQuestId) :
        return("OpenMapQuest")
    elif(geoid == NominatimId) :
        return("Nominatim")
    elif(geoid == BaiduId) :
        return("Baidu")




"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  BULK GEOCODING
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------
#-  Geopy geocode exceptions
#----------------------------------------------------------------------------
"""

GeopyErrorMessage                           =   "geopy.exc.GeopyError"
GeopyConfigurationError                     =   "geopy.exc.ConfigurationError"
GeopyGeocoderServiceErrorMessage            =   "geopy.exc.GeocoderServiceError"
GeopyGeocoderQueryErrorMessage              =   "geopy.exc.GeocoderQueryError"
GeopyGeocoderQuotaExceededMessage           =   "geopy.exc.GeocoderQuotaExceeded"
GeopyGeocoderAuthenticationFailureMessage   =   "geopy.exc.GeocoderAuthenticationFailure"
GeopyGeocoderInsufficientPrivilegesMessage  =   "geopy.exc.GeocoderInsufficientPrivileges"
GeopyGeocoderGeocoderTimedOutMessage        =   "geopy.exc.GeocoderTimedOut"
GeopyGeocoderUnavailableMessage             =   "geopy.exc.GeocoderUnavailable"
GeopyGeocoderParseErrorMessage              =   "geopy.exc.GeocoderParseError"
GeopyGeocoderNotFoundMessage                =   "geopy.exc.GeocoderNotFound"

GeopyGeocoderConnectionErrorMessage         =   "unable to get geocoder connection"



"""
#----------------------------------------------------------------------------
#-  Google maps geocode exceptions
#----------------------------------------------------------------------------
"""
ApiErrorMessage                         =   "googlemaps.exceptions.ApiError"
HTTPErrorMessage                        =   "googlemaps.exceptions.HTTPError"
TimeoutErrorMessage                     =   "googlemaps.exceptions.Timeout"
TransportErrorMessage                   =   "googlemaps.exceptions.TransportError"
RetriableRequestErrorMessage            =   "googlemaps.exceptions._RetriableRequest"
OverQueryLimitErrorMessage              =   "googlemaps.exceptions._OverQueryLimit"

GoogleGeocoderConnectionErrorMessage    =   "unable to get google geocoder connection"

"""
#----------------------------------------------------------------------------
#-  Google geocode status codes
#----------------------------------------------------------------------------
"""
OK_STATUS                               =   "OK"
ZERO_RESULTS_STATUS                     =   "ZERO_RESULTS"
OVER_DAILY_LIMIT_STATUS                 =   "OVER_DAILY_LIMIT"
OVER_QUERY_LIMIT_STATUS                 =   "OVER_QUERY_LIMIT"
REQUEST_DENIED_STATUS                   =   "REQUEST_DENIED"
INVALID_REQUEST_STATUS                  =   "INVALID_REQUEST"
UNKNOWN_ERROR_STATUS                    =   "UNKNOWN_ERROR"


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
#-  Google geocode results class
#----------------------------------------------------------------------------
#   google geocode results received from google geocode call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class geopy_geocode_results:
    
    rowId           =   -1
    full_address    =   None
    lat             =   None
    lng             =   None
    opstat          =   None
    
    def __init__(self,rowid,address,glat,glng,opstat) :
        self.rowId          =   rowid
        self.full_address   =   address
        self.lat            =   glat
        self.lng            =   glng
        self.opstat         =   opstat

    def get_lat(self) :
        return(self.lat)
    def get_lng(self) :
        return(self.lng)
    def get_full_address(self) :
        return(self.full_address)
    
    def get_row_Id(self) :
        return(self.rowId)
    def get_status(self) :
        return(self.opstat.get_status())
    def get_error_message(self) :
        return(self.opstat.get_errorMsg())
    
    
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
    
    rowId           =   -1
    status          =   None
    results         =   None
    
    def __init__(self,rowid,status,geocode_results) :
        self.rowId      =   rowid
        self.status     =   status
        self.results    =   geocode_results

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
    
    def get_address_components(self) :
        return(self.results.get("address_components"))
    
    def get_row_Id(self) :
        return(self.rowId)
    def get_status(self) :
        return(self.opstat.get_status())


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
    
    rowId           =   -1
    status          =   None
    results         =   None
    opstat          =   None
    
    def __init__(self,rowid,status,reverse_results,opstat) :
        self.rowId      =   rowid
        self.status     =   status
        self.results    =   reverse_results
        self.opstat     =   opstat

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

    def get_address_components(self) :
        return(self.results.get("address_components"))
        
    def get_row_Id(self) :
        return(self.rowId)
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
    """
    * --------------------------------------------------------------------
    * function : get a complete address from google address components 
    * 
    * parms :
    *  addr_comps  - address components
    *  addr_map    - address parms map
    *  short       - get short values boolean
    *
    * returns : 
    *  full adddress defined by map from address components
    * -------------------------------------------------------------------
    """
    
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

    def __init__(self,addr_comps) :
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
                                
                return("")
                
            else :
                return("") 
                
        else :
            return("")
        
    def get_full_custom_address_from_components(self,addr_format,shortName=True) :
        
        out_address     =   ""
        
        if(addr_format != None) :
            if(len(addr_format) > 0) :
                for i in range(len(addr_format)) :
                    out_address     =   out_address + self.get_address_component(addr_format[i],shortName)
                    
        return(out_address)
        
                    
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding data components 
#------------------------------------------------------------------
#------------------------------------------------------------------
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

    columns     =   ["source df rowid", "input value"]

    from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import (bulk_google_query_input_labelList,
                                                                         bulk_google_reverse_input_labelList,
                                                                         batch_arcgis_query_labelList,
                                                                         bulk_bing_query_input_labelList,
                                                                         bulk_bing_reverse_input_labelList)
                                                                         
    max_geocodes  =   0
    
    if(geocid == GoogleId) :
        
        if(geotype == QUERY) :  
            
            lat_long_col_name   =   runParms.get(bulk_google_query_input_labelList[2])
            if(lat_long_col_name.find("[") > -1) :
                lat_long_col_name = lat_long_col_name.replace("[","")
                lat_long_col_name = lat_long_col_name.replace("]","")
                lat_long_cols  =  lat_long_col_name.split(",")
                for i in range(len(lat_long_cols)) :
                    columns.append(lat_long_cols[i])    
            else :
                columns.append(lat_long_col_name)
            
            if(runParms.get(bulk_google_query_input_labelList[7]) == "True") :            
                columns.append("location_type")

            if(not (runParms.get(bulk_google_query_input_labelList[3]) == "None")) :            
                columns.append(runParms.get(bulk_google_query_input_labelList[3]))
            
            max_geocodes   =   int(runParms.get(bulk_google_query_input_labelList[8]))
            
        else :
            
            addr_comps   =   runParms.get(bulk_google_reverse_input_labelList[4])
            
            if(len(addr_comps) > 0) :
                if(addr_comps.find("[") > -1) :
                    addr_comps = addr_comps.replace("[","")
                    addr_comps = addr_comps.replace("]","")
                    addr_comps_cols  =  addr_comps.split(",")
                    for i in range(len(addr_comps_cols)) :
                        columns.append(addr_comps_cols[i])    

                else :
                    columns.append("full_address")                    
            else :
                columns.append("full_address")    
                
            columns.append("location_type")

            max_geocodes   =   int(runParms.get(bulk_google_reverse_input_labelList[7]))

    elif(geocid == ArcGISId) :
        
        if(geotype == QUERY) :  
            columns.append("lat_lng")
            if( not (runParms.get(batch_arcgis_query_labelList[3]) == None)) :
                columns.append("full_address")
                
            max_geocodes   =   int(runParms.get(batch_arcgis_query_labelList[10])) 
            
        else :
            return(None)
            
    elif(geocid == BingId) :
        
        if(geotype == QUERY) :  
            
            lat_long_col_name   =   runParms.get(bulk_bing_query_input_labelList[2])
            if(lat_long_col_name.find("[") > -1) :
                lat_long_col_name = lat_long_col_name.replace("[","")
                lat_long_col_name = lat_long_col_name.replace("]","")
                lat_long_cols  =  lat_long_col_name.split(",")
                for i in range(len(lat_long_cols)) :
                    columns.append(lat_long_cols[i])    
            else :
                columns.append(lat_long_col_name)
                
            f_address   =   runParms.get(bulk_bing_query_input_labelList[3])
            if(not (f_address is None)) :
                if(len(f_address) > 0) :
                    columns.append(f_address)
            
            max_geocodes   =   int(runParms.get(bulk_bing_query_input_labelList[8]))
            
        else :
            
            columns.append("full_address")                    

            max_geocodes   =   int(runParms.get(bulk_bing_reverse_input_labelList[5]))
        
                
    else :
        print("init geocoder data stores : bad gheocoder")
    
    BulkGeocodeResultsdf    =   BulkGeocodeResults(geocid,geotype,max_geocodes,columns)    
    BulkGeocodeErrors       =   BulkGeocodeErrorLog()    

    return([BulkGeocodeResultsdf,BulkGeocodeErrors])


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding results log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_RESULTS_DF_TITLE          =   "Current_Geocoding_Results_df"
GEOCODING_RESULTS_DF_NOTES          =   "Bulk Geocoding Results df"

MAX_RESULTS_DISPLAYED               =   200
DISPLAY_RESULTS_SIZE                =   20

MAX_RESULTS_CACHED                  =   1000

class BulkGeocodeResults:
    
    geocode_results_df      =   None
    geocode_results_list    =   []
    geocoderid              =   None
    geotype                 =   None
    max_geocodes            =   0
    column_headers_list     =   []
    last_percent            =   0
    
    def __init__(self,geocid,geotype,maxgeocodes,column_headers,dftitle=None):
        
        #self.column_headers         =   column_headers
        self.geocoderid             =   geocid 
        self.geotype                =   geotype 
        self.max_geocodes           =   maxgeocodes 
        self.geocode_results_list   =   []
        self.column_headers_list    =   column_headers
        
        for i in range(len(self.column_headers_list)) :
            self.column_headers_list[i]     =   self.column_headers_list[i].lstrip(" ") 
            self.column_headers_list[i]     =   self.column_headers_list[i].rstrip(" ")

        
        if(dftitle == None) :
            
            import pandas as pd
            self.geocode_results_df =   pd.DataFrame(columns=self.column_headers_list)
            
            if( (self.geocoderid == GoogleId) or (self.geocoderid == ArcGISId) ) :
                
                import numpy as np
                if(len(self.column_headers_list) == 4) :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : str,
                                                                                 self.column_headers_list[2] : list,
                                                                                 self.column_headers_list[3] : str})
                else :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : str,
                                                                                 self.column_headers_list[2] : np.float64,
                                                                                 self.column_headers_list[3] : np.float64,
                                                                                 self.column_headers_list[4] : str})
    
            elif(self.geocoderid == BingId) :
                
                import numpy as np
                if(len(self.column_headers_list) == 2) :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : list})
                else :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : np.float64,
                                                                                 self.column_headers_list[2] : np.float64})

            dfc_geocode_results_df  =   cfg.dfc_dataframe(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df,GEOCODING_RESULTS_DF_NOTES)
            
            cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)
            cfg.add_dfc_dataframe(dfc_geocode_results_df)

        else :
            self.geocode_results_df  = cfg.get_dfc_dataframe(dftitle)

    def add_result(self,rowResults,opstat) :
        
        #import json
        if(GEOCODE_DETAIL_DEBUG)  :   log_dfc(rowResults[0],"add_result [start] : [" + str(self.get_results_count()) + "] " + str(len(rowResults)))

        try :
            if(self.load_results()) :
                self.geocode_results_list.append(tuple(rowResults))
            
            if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :
                self.flush_results_to_dataframe(opstat)
        
            cfg.get_dfc_df(GEOCODING_RESULTS_DF_TITLE).set_df(self.geocode_results_df)
            
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("add_result exception : "  + str(sys.exc_info()[0].__name__))

        
    def show_results(self, startrowindex) :

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

        return(listHtml)


    def flush_results_to_dataframe(self,opstat) :
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"flush_results_to_dataframe - df len : " + str(len(self.geocode_results_df)) + " result list len : " + str(len(self.geocode_results_list)))
        
        if(len(self.geocode_results_list) > 0) :
           
            try :
                
                import pandas as pd
                self.geocode_results_df = self.geocode_results_df.append(pd.DataFrame(self.geocode_results_list, columns=self.column_headers_list))
            
                cfg.get_dfc_df(GEOCODING_RESULTS_DF_TITLE).set_df(self.geocode_results_df)
                self.geocode_results_list   =   []
                
            except :
                opstat.set_status(False)
                import sys
                opstat.set_errormsg("flush_results_to_dataframe Exception : "  + str(sys.exc_info()[0].__name__))
        
        
    def load_results(self) :
        
        retry_count     =   0
        
        if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :  
            while( (len(self.geocode_results_list) >= MAX_RESULTS_CACHED) and 
                   (retry_count < 20) ) :
                
                retry_count     =   retry_count + 1
                import time
                time.sleep(0.05)
                
        if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :  
            return(False)
        else :
            return(True)
        
        
    def get_results_count(self) :    
        return(len(self.geocode_results_df) + len(self.geocode_results_list))

    def clear_geocoding_results(self) :    
        self.geocode_results_df = None
        cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)

    def get_geocoding_results_df(self) :    
        return(self.geocode_results_df)

    def add_nan_result(self,rowid,inputparms,parmsDict,opstat) :
        
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"add_nan_result " + str(inputparms))  

        try :
            
            row_result  =   []
            row_result.append(rowid)
            row_result.append(inputparms)
        
            import numpy as np
            for i in range(2,len(self.column_headers_list)) :
            
                if(not (parmsDict is None)) :
                    parmsValue  =   parmsDict.get(self.column_headers_list[i],None)
                else :
                    parmsValue  =   None
            
                if(GEOCODE_DETAIL_DEBUG)  :   log_dfc(-1,"add_nan_result " + str(parmsValue))
            
                if(not (parmsValue is None)) :
                    row_result.append(str(parmsValue))    
                else :
                    row_result.append(np.NaN)
            
            self.add_result(row_result)
            
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("add_nan_result Exception : "  + str(sys.exc_info()[0].__name__))
            
        
    def finish_results_log(self,opstat) : 
        
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"finish_results_log")
        
        try :
            self.flush_results_to_dataframe(opstat)
            self.geocode_results_df = self.geocode_results_df.sort_values("source df rowid")
            self.geocode_results_df.index = range(0,len(self.geocode_results_df.index))
            cfg.get_dfc_df(GEOCODING_RESULTS_DF_TITLE).set_df(self.geocode_results_df)
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("afinish_results_log : "  + str(sys.exc_info()[0].__name__))
            
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"end : finish_results_log")


    def get_column_headers_list(self) :
        return(self.column_headers_list)
        
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding error log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_ERROR_LOG_DF_TITLE            =   "Current_Geocoding_Error_Log_df"
GEOCODING_ERROR_LOG_DF_NOTES            =   "Geocoding Error Logging Dataframe"

GEOCODING_ERROR_LOG_COLUMN_NAME_LIST    =   ['source df rowid','geocode input value','error message','Note']

MAX_ERRORS_DISPLAYED                    =   200
ERRORS_TABLE_SIZE                       =   20

MAX_ERRORS_CACHED                       =   200

class BulkGeocodeErrorLog:
    
    error_log_df        =   None
    error_log_list      =   [] 
    error_limit         =   0.0 
    
    def __init__(self):
        import pandas as pd
        self.error_log_df = pd.DataFrame(columns=GEOCODING_ERROR_LOG_COLUMN_NAME_LIST)
        dfc_geocode_error_log = cfg.dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df,GEOCODING_ERROR_LOG_DF_NOTES)
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
        cfg.add_dfc_dataframe(dfc_geocode_error_log)
        
        self.error_log_list     =   []
        self.error_limit        =   0.0

    def log_error(self,rowindex,inputValue,errorMsg,note,opstat):
        
        if(self.load_errors()) :
            if(note is None) :
                self.error_log_list.append(tuple([rowindex,inputValue,errorMsg," "]))
            else :
                self.error_log_list.append(tuple([rowindex,inputValue,errorMsg,note]))
            
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :
            self.flush_errors_to_dataframe(opstat)
        
        cfg.get_dfc_df(GEOCODING_ERROR_LOG_DF_TITLE).set_df(self.error_log_df)

    def show_errors(self, startrowindex) :
        
        if(GEOCODE_DEBUG)  :   log_dfc("get_geocode_error_log_table",startrowindex)

        errorsHeader      =   ["rowid","input value","error message"]
        errorsRows        =   []
        errorsWidths      =   [10,35,55]
        errorsAligns      =   ["center","left","left"]

        for i in range(MAX_ERRORS_DISPLAYED) :
            df      =   cfg.get_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
            cerror  =   df.loc[df[GEOCODING_ERROR_LOG_COLUMN_NAME_LIST[0]] == startrowindex+i] 
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

        return(listHtml)
        

    def flush_errors_to_dataframe(self,opstat) :
        
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"flush_errors_to_dataframe : " + str(type(self.error_log_df)) + str(self.get_error_count()))
        
        try :
            
            if(len(self.error_log_list) > 0) :
                import pandas as pd
                self.error_log_df = self.error_log_df.append(pd.DataFrame(self.error_log_list, columns=GEOCODING_ERROR_LOG_COLUMN_NAME_LIST))
                cfg.get_dfc_df(GEOCODING_ERROR_LOG_DF_TITLE).set_df(self.error_log_df)
                self.error_log_list   =   []
                
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("flush_errors_to_dataframe Exception : "  + str(sys.exc_info()[0].__name__))
        
        
    def load_errors(self) :
        retry_count     =   0
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :  
            while( (len(self.error_log_list) >= MAX_ERRORS_CACHED) and 
                   (retry_count < 20) ) :
                
                retry_count     =   retry_count + 1
                import time
                time.sleep(0.05)
                
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :  
            return(False)
        else :
            return(True)

 
    def get_error_count(self) :    
        return(len(self.error_log_df) + len(self.error_log_list))

    def clear_error_log(self) :    
        self.error_log_df = None
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)

    def set_error_limit(self,geocoderid,geotype) :
        
        if(geocoderid == GoogleId) :
            
            if(geotype == QUERY) :
                
                from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import bulk_google_query_input_id
                parms   =   cfg.get_config_value(bulk_google_query_input_id+"Parms")
                limit   =   float(parms[9])
                
            else :
                
                from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import bulk_google_reverse_input_id
                parms   =   cfg.get_config_value(bulk_google_reverse_input_id+"Parms")
                limit   =   float(parms[8])
                
        elif(geocoderid == ArcGISId) :
        
            if(geotype == QUERY) :
                
                from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import batch_arcgis_query_id
                parms   =   cfg.get_config_value(batch_arcgis_query_id+"Parms")
                limit   =   float(parms[9])
        
        elif(geocoderid == BingId) :
            
            if(geotype == QUERY) :
                
                from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import bulk_bing_query_input_id
                parms   =   cfg.get_config_value(bulk_bing_query_input_id+"Parms")
                limit   =   float(parms[8])
                
            else :
                
                from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import bulk_google_reverse_input_id
                parms   =   cfg.get_config_value(bulk_google_reverse_input_id+"Parms")
                limit   =   float(parms[8])
        
        self.error_limit    =   limit
        
    def get_error_limit(self) :
        return(self.error_limit)
        
    def finish_error_log(self,opstat) :    
        self.flush_errors_to_dataframe(opstat)
        self.error_log_df = self.error_log_df.sort_values("source df rowid")
        self.error_log_df.index = range(0,len(self.error_log_df.index))
        cfg.get_dfc_df(GEOCODING_ERROR_LOG_DF_TITLE).set_df(self.error_log_df)
        

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
        
    def get_colindices(self): 
        return(self.colIndices)
    
    def get_colValues(self): 
        return(self.colValues)

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
    
    address_cols        =   address_cols.replace(","," ")
    address_components  =   address_cols.split("+")
    
    for i in range(len(address_components)) :
        address_components[i]   =   address_components[i].lstrip(" ")
        address_components[i]   =   address_components[i].rstrip(" ")
        
    colnames            =   cfg.get_dfc_dataframe().columns.values.tolist() 
    
    for i in range(len(address_components)) :

        if(address_components[i] in colnames) :
            colIndices.append(address_components[i])
            colValues.append(None)
            
        else :
            colIndices.append(-1)
            colValues.append(address_components[i])
    
    addressMap  =    AddressMap(colIndices,colValues)       
    
    return(addressMap)


def get_geocode_address_string(geocid,runparms,address_map,rowIndex) : 
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
    
    from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import (batch_arcgis_query_labelList,
                                                                         bulk_google_query_input_labelList,
                                                                         bulk_bing_query_input_labelList)
    
    if(geocid   ==  ArcGISId) :
        df_name     =   runparms.get(batch_arcgis_query_labelList[0]) 
    elif(geocid   ==  GoogleId) :
        df_name     =   runparms.get(bulk_google_query_input_labelList[0]) 
    elif(geocid   ==  BingId) :
        df_name     =   runparms.get(bulk_bing_query_input_labelList[0]) 
        
    df  =   get_dfc_dataframe(df_name)
    
    for i in range(len(address_map.get_colindices())) :
        
        if(not (address_map.get_colindices()[i] == -1) ) :
            geocode_address     =   geocode_address + df.loc[rowIndex,address_map.get_colindices()[i]] + " "
        else :
            geocode_address     =   geocode_address + address_map.get_colValues()[i] + " "
        
    return(geocode_address)




def get_geocode_reverse_lat_lng_string(geocid,runparms,rowIndex) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get lat,lng string from address cols input parms
    * 
    * parms :
    *  runparms   - reverse run parms
    *  rowIndex   - dataframe row index
    *
    * returns : 
    *  address string to feed geocoder
    * --------------------------------------------------------
    """
    
    if(GEOCODE_DEBUG)  :   log_dfc(-1,"get_geocode_reverse_lat_lng_string : geocid " + str(geocid) + " rowid " + str(rowIndex))  

    try :  
        from dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets import (bulk_google_reverse_input_labelList,
                                                                             bulk_bing_reverse_input_labelList)
        
        if(geocid   ==  GoogleId) :
            df_name         =   runparms.get(bulk_google_reverse_input_labelList[0]) 
            lat_lng_cols    =   runparms.get(bulk_google_reverse_input_labelList[1])
        elif(geocid   ==  BingId) :
            df_name         =   runparms.get(bulk_bing_reverse_input_labelList[0])
            lat_lng_cols    =   runparms.get(bulk_bing_reverse_input_labelList[1])
        
        df  =   get_dfc_dataframe(df_name)

        lat_lng_cols        =   runparms.get(bulk_google_reverse_input_labelList[1])
        lat_lng_cols        =   lat_lng_cols.replace("[","")
        lat_lng_cols        =   lat_lng_cols.replace("]","")
    
        lat_lng_cols_list   =  lat_lng_cols.split(",")
        
        if(len(lat_lng_cols_list) == 1) :
        
            df_lat_lng          =   df.loc[rowIndex,lat_lng_cols_list[0]]
            
            df_lat_lng          =   df_lat_lng.replace("[","")
            df_lat_lng          =   df_lat_lng.replace("[","")
            df_lat_lng          =   df_lat_lng.replace("(","")
            df_lat_lng          =   df_lat_lng.replace(")","")
            df_lat_lng_list     =   df_lat_lng.split(",")
            df_lat              =   df_lat_lng_list[0]
            df_lng              =   df_lat_lng_list[1]
        
        else :
            df_lat              =   df.loc[rowIndex,lat_lng_cols_list[0]]
            df_lng              =   df.loc[rowIndex,lat_lng_cols_list[1]]
            
    except :
        if(GEOCODE_DEBUG)  :   log_dfc(-1,"get_geocode_reverse_lat_lng_string exception "  + str(sys.exc_info()[0].__name__))
        return(None)         
    
    lat_lng     =   "[" + str(df_lat) + "," + str(df_lng) + "]" 

    return(lat_lng)


"""
#--------------------------------------------------------------------------
#   static geocode debug log
#--------------------------------------------------------------------------
"""

GEOCODE_DEBUG           =   True
GEOCODE_DETAIL_DEBUG    =   False

def log_dfc(rowid,text) :
    dfc_debug_log.append([rowid,text])  
    
def clear_dfc_log() :
    if(len(dfc_debug_log) > 0) :
        for i in range(len(dfc_debug_log)) :
            dfc_debug_log.pop()    
    
def dump_dfc_debug_log(index=None,text=None) :
    for i in range(len(dfc_debug_log)) :
        if(index == None) :
            if(text == None) :
                print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])
            else :
                if(dfc_debug_log[i][1].find(text) > -1) :
                    print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
                
        else :
            if(dfc_debug_log[i][0] == index) :
                if(text == None) :
                    print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])
                else :
                    if(dfc_debug_log[i][1].find(text) > -1) :
                        print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
            else :
                if(not (text == None) ) :
                    if(dfc_debug_log[i][1].find(text) > -1) :
                        print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
                
    
    
dfc_debug_log  =   []


        
        
        
    
    
    
    
    



  