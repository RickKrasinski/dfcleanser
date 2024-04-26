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

import sys
this = sys.modules[__name__]

import pandas as pd
#import json
import numpy as np


DEBUG_GEOCODE           =   True
DEBUG_GEOCODE_UTILITY   =   True


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

supported_Geocoders         =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]

supported_Bulk_Geocoders    =   [BingId,GoogleId]
supported_Bulk_Reverses     =   [BingId,GoogleId]


INTERACTIVE                 =   0
BULK                        =   1
BULK_TUNING                 =   2

GEOCODER                    =    0
QUERY                       =    1
REVERSE                     =    2

ADDRESS                     =   0
LAT_LNG                     =   1
DATAFRAME                   =   2

USER_LOCATION               =   0
DF_CENTER_POINT_LOCATION    =   1
CENTER_POINT_LIST_LOCATION  =   2


"""
#--------------------------------------------------------------------------
#   geocode utilities commands
#--------------------------------------------------------------------------
"""

def get_geocoder_title(geoid) :
    
    if(geoid == ArcGISId)           :   return("ArcGIS")
    elif(geoid == BingId)           :   return("Bing")
    elif(geoid == GoogleId)         :   return("GoogleV3")
    elif(geoid == OpenMapQuestId)   :   return("OpenMapQuest")
    elif(geoid == NominatimId)      :   return("Nominatim")
    elif(geoid == BaiduId)          :   return("Baidu")

def get_geocoder_id(title) :
    
    if(title == "ArcGIS")           :   return(ArcGISId)
    elif(title == "Bing")           :   return(BingId)
    elif(title == "GoogleV3")       :   return(GoogleId)
    elif(title == "OpenMapQuest")   :   return(OpenMapQuestId)
    elif(title == "Nominatim")      :   return(NominatimId)
    else                            :   return(BingId)

def get_geocoder_list(for_bulk_geocoding=False) :

    if(for_bulk_geocoding) :
        num_geocoders   =   len(supported_Bulk_Geocoders)
    else :
        num_geocoders   =   len(supported_Geocoders)
    
    geocoders_list  =   []

    for i in range(num_geocoders) :
        
        if(for_bulk_geocoding) :
            geocoder_val    =   get_geocoder_title(supported_Bulk_Geocoders[i])
        else :
            geocoder_val    =   get_geocoder_title(supported_Geocoders[i])

        geocoders_list.append(geocoder_val)

    return(geocoders_list)


def get_current_geocoder_id() :

    from dfcleanser.common.cfg import get_config_value
    geocid  =   get_config_value("currentGeocoder")

    return(geocid)

def set_current_geocoder_id(geocid) :

    from dfcleanser.common.cfg import set_config_value
    set_config_value("currentGeocoder",geocid)


def get_geocoder_parms(geocid) :

    from dfcleanser.common.cfg import get_config_value

    if(geocid == ArcGISId)          :   geocoder_parms  =   get_config_value("arcgisgeocoderParms")
    elif(geocid == BingId)          :   geocoder_parms  =   get_config_value("binggeocoderParms")
    elif(geocid == GoogleId)        :   geocoder_parms  =   get_config_value("googlegeocoderParms")
    elif(geocid == OpenMapQuestId)  :   geocoder_parms  =   get_config_value("mapquestgeocoderParms")
    elif(geocid == NominatimId)     :   geocoder_parms  =   get_config_value("nomingeocoderParms")
    else                            :   geocoder_parms  =   None 

    return(geocoder_parms)     

def set_geocoder_parms(geocid, geocoder_parms) :

    from dfcleanser.common.cfg import set_config_value

    if(geocid == ArcGISId)          :   set_config_value("arcgisgeocoderParms", geocoder_parms)
    elif(geocid == BingId)          :   set_config_value("binggeocoderParms", geocoder_parms)
    elif(geocid == GoogleId)        :   set_config_value("googlegeocoderParms", geocoder_parms)
    elif(geocid == OpenMapQuestId)  :   set_config_value("mapquestgeocoderParms", geocoder_parms)
    elif(geocid == NominatimId)     :   set_config_value("nomingeocoderParms", geocoder_parms)


def get_geocoder_query_parms(geocid) :

    from dfcleanser.common.cfg import get_config_value
    geocoder_parms  =   get_config_value(get_form_id(geocid,QUERY) + "Parms")

    return(geocoder_parms)     

def set_geocoder_query_parms(geocid,query_parms) :

    from dfcleanser.common.cfg import set_config_value
    set_config_value(get_form_id(geocid,QUERY) + "Parms",query_parms)

def get_geocoder_reverse_parms(geocid) :

    from dfcleanser.common.cfg import get_config_value
    geocoder_parms  =   get_config_value(get_form_id(geocid,REVERSE) + "Parms")

    return(geocoder_parms)     

def set_geocoder_reverse_parms(geocid,reverse_parms) :

    from dfcleanser.common.cfg import set_config_value
    set_config_value(get_form_id(geocid,REVERSE) + "Parms",reverse_parms)



def get_form_id(geocid,gtype) :
    """
    * ---------------------------------------------------------
    * function : get the form id for a geocoder
    * 
    * parms :
    *  geocid  - geocoder id
    *  gtype   - geocoder type - QUERY or REVERSE
    *
    * returns : 
    *  geocoder form id
    * --------------------------------------------------------
    """
     
    import dfcleanser.Qt.utils.Geocode.GeocodeWidgets as ggw


    if(gtype == GEOCODER)  :
         
        if(geocid == ArcGISId)            : return(ggw.arcgis_geocoder_id)   
        elif(geocid == GoogleId)          : return(ggw.google_geocoder_id)
        elif(geocid == BingId)            : return(ggw.bing_geocoder_id)
        elif(geocid == OpenMapQuestId)    : return(ggw.mapquest_geocoder_id)
        elif(geocid == NominatimId)       : return(ggw.nomin_geocoder_id)
        elif(geocid == BaiduId)           : return(ggw.baidu_geocoder_id)
         
    elif(gtype == QUERY)  :
         
        if(geocid == ArcGISId)            : return(ggw.arcgis_query_id) 
        elif(geocid == GoogleId)          : return(ggw.google_query_id)
        elif(geocid == BingId)            : return(ggw.bing_query_id)
        elif(geocid == OpenMapQuestId)    : return(ggw.mapquest_query_id)
        elif(geocid == NominatimId)       : return(ggw.nomin_query_id)
        elif(geocid == BaiduId)           : return(ggw.baidu_query_id)

    elif(gtype == REVERSE)  :
         
        if(geocid == ArcGISId)            : return(ggw.arcgis_reverse_id)   
        elif(geocid == GoogleId)          : return(ggw.google_reverse_id)
        elif(geocid == BingId)            : return(ggw.bing_reverse_id)
        elif(geocid == OpenMapQuestId)    : return(ggw.mapquest_reverse_id)
        elif(geocid == NominatimId)       : return(ggw.nomin_reverse_id)
        elif(geocid == BaiduId)           : return(ggw.baidu_reverse_id)
   
    else :
        return(None)
 


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


#DISPLAY_TUNING                  =   49
#PROCESS_TUNING                  =   50




"""
#--------------------------------------------------------------------------
#   bulk geocoder current state
#--------------------------------------------------------------------------
"""
"""
RUNNING                     =   0
STOPPED                     =   1
PAUSED                      =   2
STARTING                    =   3

PAUSING                     =   5
#FINISHED                    =   6
ERROR_LIMIT                 =   7
"""

#CHECKPOINT_STARTED          =   8
#CHECKPOINT_COMPLETE         =   9


#LOAD                        =   10
#START                       =   11
#STOP                        =   12
#PAUSE                       =   13
#RESUME                      =   14


#GEOCODE_BAR                 =   0
#ERROR_BAR                   =   1




GlobalKeys     =   ["EULARead","geocoder","GoogleV3_querykwargs",
                    "arcgisgeocoderParms","binggeocoderParms","mapquestgeocoderParms",
                    "nomingeocoderParms","googlegeocoderParms","baidu_geocoderParms",
                    "googlebulkgeocoderParms","arcgisbatchgeocoderParms",
                    "bingbulkgeocoderParms","baidubulkgeocoderParms",
                    "PostgresqldbconnectorParms","MySQLdbconnectorParms","SQLitedbconnectorParms",
                    "OracledbconnectorParms","MSSQLServerdbconnectorParms","customdbconnectorParms",
                    "currentDBID","currentDBLIBID"]




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
#-  Bing geocode results class
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
    
class geopy_reverse_results:
    
    rowId           =   -1
    geopoint        =   None
    location        =   None
    opstat          =   None
    
    def __init__(self,rowid,geopoint,location) :
        self.rowId          =   rowid
        self.geopoint       =   geopoint
        self.location       =   location

    def get_geopoint(self) :
        return(self.geopoint)
    def get_location(self) :
        return(self.location)
    def get_row_Id(self) :
        return(self.rowId)
   
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

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import GEOCODE_TRACE_GET_GEOCODE_DETAILS
        from dfcleanser.common.common_utils import log_debug_dfc 
        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
            #log_debug_dfc(-1,"[google_address_components] addr_comps : " + str(addr_comps))
            log_debug_dfc(-1,"[google_address_components] addr_comps : " + str(type(addr_comps)) + " : " + str(len(addr_comps)))
            for i in range(len(addr_comps)) :
                log_debug_dfc(-1,"[google_address_components] addr_comps : " + str(addr_comps[i]))
               

    def get_address_component(self,address_component_id,shortName=True) :

        if(self.address_components != None) :
            if(len(self.address_components) > 0) :
                for i in range(len(self.address_components)) :
                    ctypes  =   self.address_components[i].get("types",None)

                    if(address_component_id == "state") :       component_id        =   "administrative_area_level_1"
                    elif(address_component_id == "county") :    component_id        =   "administrative_area_level_2"
                    elif(address_component_id == "city") :      component_id        =   "administrative_area_level_3"
                    else :                                      component_id        =   address_component_id 

                    if(ctypes != None) :
                        if(component_id in ctypes) :

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
#--------------------------------------------------------------------------
#  google address components class for getting individual address fields
#--------------------------------------------------------------------------
"""
def get_google_address_components(requested_addr_comps) :

    if(not (requested_addr_comps is None)) :
            
        addr_comps    =   requested_addr_comps.replace("[","")
        addr_comps    =   addr_comps.replace("]","")
        addr_comps    =   addr_comps.split(",")
        for i in range(len(addr_comps)) :
            addr_comps[i]     =   addr_comps[i].lstrip(" ") 
            addr_comps[i]     =   addr_comps[i].rstrip(" ")

    else :

        addr_comps  =   []

    return(addr_comps)


"""
#--------------------------------------------------------------------------
#  utility to get geopoint tuple from string
#--------------------------------------------------------------------------
"""
def get_geopoint_from_string(geo_str) :

    try :

        current_lat_lng     =   geo_str.replace("[","")
        current_lat_lng     =   current_lat_lng.replace("]","")
        current_lat_lng     =   current_lat_lng.replace("(","")
        current_lat_lng     =   current_lat_lng.replace(")","")
        current_lat_lng     =   current_lat_lng.replace("\\n","")
        current_lat_lng     =   current_lat_lng.split(",")
        new_lat             =   float(current_lat_lng[0])
        new_lng             =   float(current_lat_lng[1])
        new_lat_lng         =   (new_lat,new_lng)
        return(new_lat_lng)
            
    except :
                
        return(None)


"""
#--------------------------------------------------------------------------
#  utility to split in two geocode address
#--------------------------------------------------------------------------
"""
def split_geocode_address(geo_addr) :

    try :

        col_width   =   40
        addr_len    =   len(geo_addr)

        if(addr_len < col_width) :
            return([geo_addr,""])
        
        else : 

            first_comma     =   geo_addr.find(",") 
            if(first_comma > -1) :
                print("cm1 ",geo_addr[(first_comma+1):])
                second_comma    =   geo_addr[(first_comma+1):].find(",") 
                print("second_comma ",second_comma)
                if(second_comma > -1) :
                    return([geo_addr[:(second_comma+first_comma)+1],geo_addr[((second_comma+first_comma)+2):]]) 
                else :
                    return([geo_addr[:first_comma],geo_addr[(first_comma+1):]]) 
          
    except Exception as e:

        title       =   "dfcleanser exception"       
        status_msg  =   "[invalid address] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

                
        return(geo_addr)


class GeocodePointsListData :
    
    # instance variables
    
    # notebook specific import history data
    locations                   =   []
    names                       =   []
    
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self) :
        
        self.locations      =   None
        self.names          =   None

    def set_locations(self,points) :
        self.locations  =   points
    def get_locations(self) :
        return(self.locations)
        
    def set_names(self,pt_names) :
        self.names  =   pt_names
    def get_names(self) :
        return(self.names)


"""
* ----------------------------------------------------
# static instantiation of the points list
* ----------------------------------------------------
"""    
GeocodePointsList   =   GeocodePointsListData()
