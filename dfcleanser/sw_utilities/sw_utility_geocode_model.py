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


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Function Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_GEOCODING           =    0

DISPLAY_GET_COORDS          =    1
DISPLAY_GET_ADDRESS         =    2

PROCESS_GET_COORDS          =    3
PROCESS_GET_ADDRESS         =    4

DISPLAY_GEOCODER            =    5
PROCESS_GEOCODER            =    6

DISPLAY_DISTANCE            =    7
PROCESS_DISTANCE            =    8

DISPLAY_DF_DISTANCE         =    9
PROCESS_DF_DISTANCE         =    10

DISPLAY_BULK_GET_COORDS     =    11
DISPLAY_BULK_GET_ADDRESS    =    12

PROCESS_BULK_GET_COORDS     =    13
PROCESS_BULK_GET_ADDRESS    =    14

"""
#--------------------------------------------------------------------------
#   Geocoder Full Parameters Flags
#--------------------------------------------------------------------------
"""
DISPLAY_FULL_GEOCODING          =    15
DISPLAY_FULL_QUERY              =    16
DISPLAY_FULL_REVERSE            =    17
DISPLAY_FULL_BULK_GOOGLE_QUERY  =    18
DISPLAY_FULL_BULK_ARCGIS_QUERY  =    19

PROCESS_TEST_BULK_CONNECTOR     =    20

CLEAR_GEOCODE_PARMS             =    21

BULK_GEOCODE_RUN                =    22
BULK_GEOCODE_PAUSE              =    23
BULK_GEOCODE_STOP               =    24




ADDRESS_CONVERSION          =    0
COORDS_CONVERSION           =    1

GEOCODER                    =    0
QUERY                       =    1
REVERSE                     =    2

GEOCODERPARMS               =   0
QUERYPARMS                  =   1
REVERSEPARMS                =   2

QUERYDFPARMS                =   3
REVERSEDFPARMS              =   4

DISTANCE_HELP               =   8
DISTANCE_DF_HELP            =   8


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding constants
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

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


"""
#--------------------------------------------------------------------------
#   bulk geocoder running commands 
#--------------------------------------------------------------------------
"""
BULK_GET_COORDS             =   0
BULK_GET_ADDRESS_COLS       =   1
BULK_GET_LANGUAGES          =   2
BULK_GET_REGIONS            =   3
BULK_CLEAR                  =   4
BULK_RETURN                 =   5
BULK_HELP                   =   6
BULK_GET_ADDRESS            =   7
BULK_GET_COUNTRIES          =   8
BULK_GET_CATEGORIES         =   9
BULK_LOAD_GEOCODER          =   10
BULK_START_GEOCODER         =   11
BULK_STOP_GEOCODER          =   12
BULK_PAUSE_GEOCODER         =   13

BATCH_TEST_CONNECTOR        =   14
BATCH_CLEAR                 =   15
BATCH_RETURN                =   16
BATCH_HELP                  =   17


"""
#--------------------------------------------------------------------------
#   bulk geocoder currebt state
#--------------------------------------------------------------------------
"""
RUNNING                     =   0
STOPPED                     =   1
PAUSED                      =   2

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

