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

supported_Geocoders         =   [ArcGISId,BingId,DataBCId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BingId,GoogleId,NominatimId]

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

DISPLAY_DF_GET_COORDS       =    11
DISPLAY_DF_GET_ADDRESS      =    12

PROCESS_DF_GET_COORDS       =    13
PROCESS_DF_GET_ADDRESS      =    14


ADDRESS_CONVERSION          =    0
COORDS_CONVERSION           =    1

DISPLAY_FULL_GEOCODING      =    15
DISPLAY_FULL_QUERY          =    16
DISPLAY_FULL_REVERSE        =    17

INITPARMS                   =   0
QUERYPARMS                  =   1
QUERYDFPARMS                =   2
REVERSEPARMS                =   3
REVERSEDFPARMS              =   4

DISTANCE_HELP               =   8
DISTANCE_DF_HELP            =   8

COLNAMES_TABLE              =   0
LANGUAGE_TABLE              =   1
REGION_TABLE                =   2
CATEGORIES_TABLE            =   3



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

