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
DataBCId                    =   3
GeocoderDotUSId             =   4
GeocodeFarmId               =   5
GeoNamesId                  =   6
GoogleId                    =   7
OpenCageId                  =   8
OpenMapQuestId              =   9
PickPointId                 =   10
NominatimId                 =   11
YahooPlaceFinderId          =   12

supported_Geocoders         =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BingId,GoogleId,NominatimId]

supported_Bulk_Geocoders    =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Bulk_Reverses     =   [GoogleId]

MAX_GOOGLE_TASKS            =   10

GOOGLE_DELAY                =   0.2

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Function Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_MAIN_GEOCODING          =    0

PROCESS_GEOCODER                =    6

CLEAR_GEOCODE_FORM              =   50
DISPLAY_GEOCODER                =   51
TEST_GEOCODER                   =   52
DISPLAY_GEOCODING               =   53
GET_TABLE                       =   54
PROCESS_GEOCODING               =   55







DISPLAY_DISTANCE            =    7
PROCESS_DISTANCE            =    8
DISPLAY_DF_DISTANCE         =    9
PROCESS_DF_DISTANCE         =    10


DISPLAY_FULL_GEOCODING          =    15



BULK_GEOCODE_RUN                =    22
BULK_GEOCODE_PAUSE              =    23
BULK_GEOCODE_STOP               =    24

CHANGE_BULK_GEOCODER            =    25



DISPLAY_BULK_GEOCODER           =    27
PROCESS_BULK_GEOCODER           =    28






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


BULK_LOAD_GEOCODER          =   10
BULK_START_GEOCODER         =   11
BULK_STOP_GEOCODER          =   12
BULK_PAUSE_GEOCODER         =   13

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
STOPPING                    =   3
PAUSING                     =   4

LOAD                        =   0
START                       =   1
STOP                        =   2
PAUSE                       =   3
RESUME                      =   4


def get_geocoder_title(geoid) :
    
    if(geoid == ArcGISId) :
        return("ArcGIS")
    elif(geoid == BingId) :
        return("Bing")
    elif(geoid == DataBCId) :
        return("DataBC")
    elif(geoid == GoogleId) :
        return("GoogleV3")
    elif(geoid == OpenMapQuestId) :
        return("OpenMapQuest")
    elif(geoid == NominatimId) :
        return("Nominatim")

