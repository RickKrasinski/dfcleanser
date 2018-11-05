"""
# sw_utility_geocode_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm

from dfcleanser.common.html_widgets import (get_button_tb_form, display_composite_form, maketextarea, 
                                            get_html_spaces, get_input_form, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

from dfcleanser.common.common_utils import (get_parms_for_input, display_grid, opStatus, is_numeric_col)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

from dfcleanser.common.help_utils import GEOCODING_MAIN_TASKBAR_ID

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    address conversion main task bar
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
geocode_utility_tb_doc_title            =   "Address Conversion Options"
geocode_utility_tb_title                =   "Address Conversion"
geocode_utility_tb_id                   =   "addrconverttb"

geocode_utility_tb_keyTitleList         =   ["Convert Address</br>to Coords",
                                              "Convert Coords</br>to Address",
                                              "Calculate</br>Distance",
                                              "Select</br>Geocoder",
                                              "Clear","Help"]

geocode_utility_tb_jsList               =   ["process_geomain_callback(" + str(sugm.DISPLAY_GET_COORDS) + ")",
                                              "process_geomain_callback(" + str(sugm.DISPLAY_GET_ADDRESS) + ")",
                                              "process_geomain_callback(" + str(sugm.DISPLAY_DISTANCE) + ")",
                                              "process_geomain_callback(" + str(sugm.DISPLAY_GEOCODER) + ")",
                                              "process_geomain_callback(0)",
                                              "displayhelp(" + str(GEOCODING_MAIN_TASKBAR_ID) + ")"]

geocode_utility_tb_centered             =   False

"""
#--------------------------------------------------------------------------
#   geocoder init forms
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#   arcGIS geocoder parms
#--------------------------------------------------------------------------
"""
arcgis_geocoder_title               =   "arcGIS Geocoder"
arcgis_geocoder_id                  =   "arcgisgeocoder"

arcgis_geocoder_idList              =    ["aguser",
                                          "agpw",
                                          "agreferer",
                                          "agtoken",
                                          "agscheme",
                                          "agtimeout",
                                          "agproxies",
                                          "agagent",
                                          None,None,None,None,None,None]

arcgis_geocoder_labelList           =   ["username",
                                         "password",
                                         "referer",
                                         "token_lifetime",
                                         "scheme",
                                         "timeout",
                                         "proxies",
                                         "user_agent",
                                         "Test</br>Geocoder",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Clear","Return","Help"]


arcgis_geocoder_typeList            =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

arcgis_geocoder_placeholderList     =   ["ArcGIS username (default : None)",
                                         "ArcGIS password (default : None)",
                                         "‘Referer’ HTTP header to send with each request (default : None)",
                                         "Desired lifetime, in minutes, of an ArcGIS-issued token (default : 60)",
                                         "Desired scheme (default : https)",
                                         "Time, in seconds (default : 1)",
                                         "enter proxies dict (default : None)",
                                         "enter custom User-Agent header (default : None)",
                                         None,None,None,None,None,None]

arcgis_geocoder_jsList              =   [None,None,None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.ArcGISId) + ")",
                                         "display_help_url('" + str(dfchelp.ArcGISInitHelp) + "')"]


arcgis_geocoder_reqList             =   []

arcgis_geocoder_form                =   [arcgis_geocoder_id,
                                         arcgis_geocoder_idList,
                                         arcgis_geocoder_labelList,
                                         arcgis_geocoder_typeList,
                                         arcgis_geocoder_placeholderList,
                                         arcgis_geocoder_jsList,
                                         arcgis_geocoder_reqList]

"""
#--------------------------------------------------------------------------
#   google geocoder parms
#--------------------------------------------------------------------------
"""
google_geocoder_title               =   "Google V3 Geocoder"
google_geocoder_id                  =   "googlegeocoder"

google_geocoder_idList              =    ["ggapikey",
                                          "ggdomain",
                                          "ggscheme",
                                          "ggclient",
                                          "ggsecretkey",
                                          "ggproxies",
                                          "ggagent",
                                          "ggchannel",
                                          None,None,None,None,None,None]

google_geocoder_labelList           =   ["api_key",
                                         "domain",
                                         "scheme",
                                         "client_id",
                                         "secret_key",
                                         "proxies",
                                         "user_agent",
                                         "channel",
                                         "Test</br>Geocoder",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Clear","Return","Help"]


google_geocoder_typeList            =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

google_geocoder_placeholderList     =   ["google API key",
                                         "localized Google Maps domain default(‘maps.googleapis.com’)",
                                         "enter scheme (default https)",
                                         "enter account client id.",
                                         "enter account secret key",
                                         "enter proxies dict)",
                                         "enter custom User-Agent header",
                                         "enter channel identifier",
                                         None,None,None,None,None,None]

google_geocoder_jsList              =   [None,None,None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.GoogleId) + ")",
                                         "display_help_url('" + str(dfchelp.GoogleInitHelp) + "')"]


google_geocoder_reqList             =   [0]

google_geocoder_form                =   [google_geocoder_id,
                                         google_geocoder_idList,
                                         google_geocoder_labelList,
                                         google_geocoder_typeList,
                                         google_geocoder_placeholderList,
                                         google_geocoder_jsList,
                                         google_geocoder_reqList]

"""
#--------------------------------------------------------------------------
#   bing geocoder parms
#--------------------------------------------------------------------------
"""
bing_geocoder_title                 =   "Bing Geocoder"
bing_geocoder_id                    =   "binggeocoder"

bing_geocoder_idList                =    ["bingapikey",
                                          "bingfstring",
                                          "bingscheme",
                                          "bingtimeout",
                                          "bingproxies",
                                          "bingagent",
                                          None,None,None,None,None,None]

bing_geocoder_labelList             =   ["api_key",
                                         "format_string",
                                         "scheme",
                                         "timeout",
                                         "proxies",
                                         "user_agent",
                                         "Test</br>Geocoder",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Clear","Return","Help"]


bing_geocoder_typeList              =   ["text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

bing_geocoder_placeholderList       =   ["enter Bing Maps API key",
                                         "enter formar string",
                                         "enter scheme (default https)",
                                         "enter timeout in seconds (default 1)",
                                         "proxies dict (default None)",
                                         "user agent)",
                                         None,None,None,None,None,None]

bing_geocoder_jsList                =   [None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.BingId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.BingId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.BingId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.BingId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.BingId) + ")",
                                         "display_help_url('" + str(dfchelp.BingInitHelp) + "')"]


bing_geocoder_reqList               =   [0]

bing_geocoder_form                  =   [bing_geocoder_id,
                                         bing_geocoder_idList,
                                         bing_geocoder_labelList,
                                         bing_geocoder_typeList,
                                         bing_geocoder_placeholderList,
                                         bing_geocoder_jsList,
                                         bing_geocoder_reqList]

"""
#--------------------------------------------------------------------------
#   DataBC geocoder parms
#--------------------------------------------------------------------------
"""
databc_geocoder_title                 =   "DataBC Geocoder"
databc_geocoder_id                    =   "databcgeocoder"

databc_geocoder_idList                =    ["databcscheme",
                                            "databctimeout",
                                            "databcproxies",
                                            "databcagent",
                                            None,None,None,None,None]

databc_geocoder_labelList             =   ["scheme",
                                           "timeout",
                                           "proxies",
                                           "user_agent",
                                           "Test</br>Geocoder",
                                           "Get</br>Coords",
                                           "Clear","Return","Help"]


databc_geocoder_typeList              =   ["text","text","text","text",
                                           "button","button","button","button","button"]

databc_geocoder_placeholderList       =   ["enter scheme (default https)",
                                           "enter timeout in seconds (default 1)",
                                           "proxies dict (default None)",
                                           "user agent)",
                                            None,None,None,None,None]


databc_geocoder_jsList                =   [None,None,None,None,
                                           "process_geocoder_callback(0," + str(sugm.DataBCId) + ")",
                                           "process_geocoder_callback(1," + str(sugm.DataBCId) + ")",
                                           "process_geocoder_callback(2," + str(sugm.DataBCId) + ")",
                                           "process_geocoder_callback(3," + str(sugm.DataBCId) + ")",
                                           "display_help_url('" + str(dfchelp.DataBCInitHelp) + "')"]


databc_geocoder_reqList               =   []

databc_geocoder_form                  =   [databc_geocoder_id,
                                           databc_geocoder_idList,
                                           databc_geocoder_labelList,
                                           databc_geocoder_typeList,
                                           databc_geocoder_placeholderList,
                                           databc_geocoder_jsList,
                                           databc_geocoder_reqList]


"""
#--------------------------------------------------------------------------
#   OpenMapQuest geocoder parms
#--------------------------------------------------------------------------
"""
mapquest_geocoder_title                 =   "OpenMapQuest Geocoder"
mapquest_geocoder_id                    =   "mapquestgeocoder"

mapquest_geocoder_idList                =    ["mapquestapikey",
                                              "mapquestfstring",
                                              "mapquestscheme",
                                              "mapquesttimeout",
                                              "mapquestproxies",
                                              "mapquestagent",
                                              None,None,None,None,None,None]

mapquest_geocoder_labelList             =   ["api_key",
                                             "format_string",
                                             "scheme ",
                                             "timeout",
                                             "proxies",
                                             "user_agent",
                                             "Test</br>Geocoder",
                                             "Get</br>Coords",
                                             "Get</br>Address",
                                             "Clear","Return","Help"]


mapquest_geocoder_typeList              =   ["text","text","text","text","text","text",
                                             "button","button","button","button","button","button"]

mapquest_geocoder_placeholderList       =   ["enter MapQuest API Key",
                                             "enter format string",
                                             "enter scheme (default https)",
                                             "enter timeout in seconds (default 1)",
                                             "enter proxies dict (default None)",
                                             "enter user agent",
                                             None,None,None,None,None,None]


mapquest_geocoder_jsList                =   [None,None,None,None,None,None,
                                             "process_geocoder_callback(0," + str(sugm.OpenMapQuestId) + ")",
                                             "process_geocoder_callback(1," + str(sugm.OpenMapQuestId) + ")",
                                             "process_geocoder_callback(2," + str(sugm.OpenMapQuestId) + ")",
                                             "process_geocoder_callback(3," + str(sugm.OpenMapQuestId) + ")",
                                             "process_geocoder_callback(4," + str(sugm.OpenMapQuestId) + ")",
                                             "display_help_url('" + str(dfchelp.OpenMapQuestInitHelp) + "')"]


mapquest_geocoder_reqList               =   [0]

mapquest_geocoder_form                  =   [mapquest_geocoder_id,
                                             mapquest_geocoder_idList,
                                             mapquest_geocoder_labelList,
                                             mapquest_geocoder_typeList,
                                             mapquest_geocoder_placeholderList,
                                             mapquest_geocoder_jsList,
                                             mapquest_geocoder_reqList]

"""
#--------------------------------------------------------------------------
#   Nominatim geocoder parms
#--------------------------------------------------------------------------
"""
nomin_geocoder_title                =   "Nominatim Geocoder"
nomin_geocoder_id                   =   "nomingeocoder"

nomin_geocoder_idList               =    ["nominformat",
                                          "nominview",
                                          "nominbias",
                                          "nomintimeout",
                                          "nominproxies",
                                          "nomindomain",
                                          "nominscheme",
                                          "nominagent",
                                           None,None,None,None,None]

nomin_geocoder_labelList            =   ["format_string",
                                         "view_box",
                                         "country_bias",
                                         "timeout",
                                         "proxies",
                                         "domain",
                                         "scheme",
                                         "user_agent",
                                         "Test</br>Geocoder",
                                         "Get</br>Coords",
                                         "Clear","Return","Help"]


nomin_geocoder_typeList             =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button"]

nomin_geocoder_placeholderList      =   ["enter format string (default %s)",
                                         "Coordinates to restrict search within. (default None)",
                                         "enter country to bias results",
                                         "enter timeout in secs (default 1)",
                                         "enter proxies dict)",
                                         "enter domain)",
                                         "enter scheme (default https))",
                                         "enter custom User-Agent",
                                         None,None,None,None,None]

nomin_geocoder_jsList               =   [None,None,None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.NominatimId) + ")",
                                         "display_help_url('" + str(dfchelp.NominatimInitHelp) + "')"]


nomin_geocoder_reqList              =   []

nomin_geocoder_form                 =   [nomin_geocoder_id,
                                         nomin_geocoder_idList,
                                         nomin_geocoder_labelList,
                                         nomin_geocoder_typeList,
                                         nomin_geocoder_placeholderList,
                                         nomin_geocoder_jsList,
                                         nomin_geocoder_reqList]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoder get coords forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   arcGIS get coords forms
#--------------------------------------------------------------------------
"""
arcgis_query_title                  =   "arcGIS Geocoder Get Coordinates"
arcgis_query_id                     =   "arcgisquery"

arcgis_query_idList                 =    ["aqquery",
                                          "aqcount",
                                          "aqtimeout",
                                          "aqoutfields",
                                          None,None,None,None,None,None]

arcgis_query_labelList              =   ["query",
                                         "number_of_results",
                                         "timeout",
                                         "out_fields",
                                         "Get</br>Coords",
                                         "Display</br>Bulk</br>Coords",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


arcgis_query_typeList               =   ["text","text","text","text",
                                         "button","button","button","button","button","button"]

arcgis_query_placeholderList        =   ["address string",
                                         "max number of results (default 1) ",
                                         "enter timeout in seconds (default 1)",
                                         "a list or tuple of out fields",
                                         None,None,None,None,None,None]

arcgis_query_jsList                 =   [None,None,None,None,
                                         "process_query_callback(0," + str(sugm.ArcGISId) + ")",
                                         "process_query_callback(1," + str(sugm.ArcGISId) + ")",
                                         "process_query_callback(2," + str(sugm.ArcGISId) + ")",
                                         "process_query_callback(3," + str(sugm.ArcGISId) + ")",
                                         "process_query_callback(4," + str(sugm.ArcGISId) + ")",
                                         "display_help_url('" + str(dfchelp.ArcGISQueryHelp) + "')"]


arcgis_query_reqList                =   [0]

arcgis_query_form                   =   [arcgis_query_id,
                                         arcgis_query_idList,
                                         arcgis_query_labelList,
                                         arcgis_query_typeList,
                                         arcgis_query_placeholderList,
                                         arcgis_query_jsList,
                                         arcgis_query_reqList]



"""
#--------------------------------------------------------------------------
#   google get coords forms
#--------------------------------------------------------------------------
"""
google_query_title                  =   "Google V3 Geocoder Get Coordinates"
google_query_id                     =   "googlequery"

google_query_idList                 =    ["gqquery",
                                          "gqcount",
                                          "gqtimeout",
                                          "gqbounds",
                                          "gqregion",
                                          "gqcomps",
                                          "gqlang",
                                          "gqsensor",
                                          None,None,None,None,None,None]

google_query_labelList              =   ["query",
                                         "number_of_results",
                                         "timeout",
                                         "bounds",
                                         "region",
                                         "components",
                                         "language",
                                         "sensor",
                                         "Get</br>Coords",
                                         "Display</br>Bulk</br>Coords",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


google_query_typeList               =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

google_query_placeholderList        =   ["address string",
                                         "max number of results (default 1) ",
                                         "enter timeout in seconds (default 1)",
                                         "enter bounding box of the viewport (default None)",
                                         "enter the ccTLD region code (default None)",
                                         "enter components dict) (default None)",
                                         "enter the language (default None)",
                                         "enter sensor flag (default False)",
                                         None,None,None,None,None,None]

google_query_jsList                 =   [None,None,None,None,None,None,None,None,
                                         "process_query_callback(0," + str(sugm.GoogleId) + ")",
                                         "process_query_callback(1," + str(sugm.GoogleId) + ")",
                                         "process_query_callback(2," + str(sugm.GoogleId) + ")",
                                         "process_query_callback(3," + str(sugm.GoogleId) + ")",
                                         "process_query_callback(4," + str(sugm.GoogleId) + ")",
                                         "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

google_query_reqList                =   [0]

google_query_form                   =   [google_query_id,
                                         google_query_idList,
                                         google_query_labelList,
                                         google_query_typeList,
                                         google_query_placeholderList,
                                         google_query_jsList,
                                         google_query_reqList]

"""
#--------------------------------------------------------------------------
#   bing get coords form
#--------------------------------------------------------------------------
"""
bing_query_title                    =   "Bing Geocoder Get Coordinates"
bing_query_id                       =   "bingquery"

bing_query_idList                   =    ["bqquery",
                                          "bqcount",
                                          "bqloc",
                                          "bqtimeout",
                                          "bqculture",
                                          "bqnbc",
                                          "bqcc",
                                          None,None,None,None,None,None]

bing_query_labelList                =   ["query",
                                         "number_of_results",
                                         "user_location",
                                         "timeout",
                                         "culture ",
                                         "include_neighborhood",
                                         "include_country_code",
                                         "Get</br>Coords",
                                         "Display</br>Bulk</br>Coords",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


bing_query_typeList                 =   ["text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

bing_query_placeholderList          =   ["address string",
                                         "max number of results (default 1) ",
                                         "enter coords to prioritize to (default None)",
                                         "enter timeout in seconds (default 1)",
                                         "enter two-letter country code (default None) ",
                                         "return neighborhood field (default False)",
                                         "return 2 digit country code (default False)",
                                         None,None,None,None,None,None]

bing_query_jsList                   =   [None,None,None,None,None,None,None,
                                         "process_query_callback(0," + str(sugm.BingId) + ")",
                                         "process_query_callback(1," + str(sugm.BingId) + ")",
                                         "process_query_callback(2," + str(sugm.BingId) + ")",
                                         "process_query_callback(3," + str(sugm.BingId) + ")",
                                         "process_query_callback(4," + str(sugm.BingId) + ")",
                                         "display_help_url('" + str(dfchelp.BingQueryHelp) + "')"]


bing_query_reqList                  =   [0]

bing_query_form                     =   [bing_query_id,
                                         bing_query_idList,
                                         bing_query_labelList,
                                         bing_query_typeList,
                                         bing_query_placeholderList,
                                         bing_query_jsList,
                                         bing_query_reqList]


"""
#--------------------------------------------------------------------------
#   databc get coords form
#--------------------------------------------------------------------------
"""
databc_query_title                    =   "DataBC Geocoder Get Coordinates"
databc_query_id                       =   "databcquery"

databc_query_idList                   =  ["dbqquery",
                                          "dbqmax",
                                          "dbqsetback",
                                          "dbqloc",
                                          "dbqcount",
                                          "dbqtimeout",
                                          None,None,None,None,None,None]

databc_query_labelList                =  ["query",
                                          "number_of_results",
                                          "set_back",
                                          "location_descriptor",
                                          "exactly_one",
                                          "timeout",
                                          "Get</br>Coords",
                                          "Display</br>Bulk</br>Coords",
                                          "Change</br> Geocoder",
                                          "Clear","Return","Help"]


databc_query_typeList                 =   ["text","text","text","text","text","text",
                                           "button","button","button","button","button","button"]

databc_query_placeholderList          =   ["address string",
                                           "max number of results (default 1) ",
                                           "The distance to move the accessPoint (default None)",
                                           "the type of point requested (default 1)",
                                           "number of results (default 1) ",
                                           "timeout in secs (default 1)",
                                            None,None,None,None,None,None]

databc_query_jsList                   =   [None,None,None,None,None,None,
                                           "process_query_callback(0," + str(sugm.DataBCId) + ")",
                                           "process_query_callback(1," + str(sugm.DataBCId) + ")",
                                           "process_query_callback(2," + str(sugm.DataBCId) + ")",
                                           "process_query_callback(3," + str(sugm.DataBCId) + ")",
                                           "process_query_callback(4," + str(sugm.DataBCId) + ")",
                                           "display_help_url('" + str(dfchelp.DataBCQueryHelp) + "')"]


databc_query_reqList                  =   [0]

databc_query_form                     =   [databc_query_id,
                                           databc_query_idList,
                                           databc_query_labelList,
                                           databc_query_typeList,
                                           databc_query_placeholderList,
                                           databc_query_jsList,
                                           databc_query_reqList]

"""
#--------------------------------------------------------------------------
#   OpenMapQuest get coords form
#--------------------------------------------------------------------------
"""
mapquest_query_title                     =   "OpenMapQuest Get Coordinates"
mapquest_query_id                        =   "mapquestquery"

mapquest_query_idList                    =  ["mqquery",
                                             "mqcount",
                                             "mqtimeout",
                                             None,None,None,None,None,None]

mapquest_query_labelList                 =  ["query",
                                             "number_of_results",
                                             "timeout",
                                             "Get</br>Coords",
                                             "Display</br>Bulk</br>Coords",
                                             "Change</br> Geocoder",
                                             "Clear","Return","Help"]


mapquest_query_typeList                  =   ["text","text","text",
                                              "button","button","button","button","button","button"]

mapquest_query_placeholderList           =   ["address string",
                                              "max number of results (default 1) ",
                                              "timeout in secs (default 1)",
                                              None,None,None,None,None,None]

mapquest_query_jsList                    =    [None,None,None,
                                               "process_query_callback(0," + str(sugm.OpenMapQuestId) + ")",
                                               "process_query_callback(1," + str(sugm.OpenMapQuestId) + ")",
                                               "process_query_callback(2," + str(sugm.OpenMapQuestId) + ")",
                                               "process_query_callback(3," + str(sugm.OpenMapQuestId) + ")",
                                               "process_query_callback(4," + str(sugm.OpenMapQuestId) + ")",
                                               "display_help_url('" + str(dfchelp.OpenMapQuestQueryHelp) + "')"]


mapquest_query_reqList                   =   [0]

mapquest_query_form                      =   [mapquest_query_id,
                                              mapquest_query_idList,
                                              mapquest_query_labelList,
                                              mapquest_query_typeList,
                                              mapquest_query_placeholderList,
                                              mapquest_query_jsList,
                                              mapquest_query_reqList]

"""
#--------------------------------------------------------------------------
#   Nominatim get coords form
#--------------------------------------------------------------------------
"""
nomin_query_title                        =   "Nominatim Get Coordinates"
nomin_query_id                           =   "nominquery"

nomin_query_idList                       =  ["nqquery",
                                             "nqcount",
                                             "nqtimeout",
                                             "nqlimit",
                                             "nqaddr",
                                             "nqlang",
                                             "nqgeom",
                                             None,None,None,None,None,None]

nomin_query_labelList                    =  ["query",
                                             "number_of_results",
                                             "timeout",
                                             "limit",
                                             "addressdetails",
                                             "language",
                                             "geometry",
                                             "Get</br>Coords",
                                             "Display</br>Bulk</br>Coords",
                                             "Change</br> Geocoder",
                                             "Clear","Return","Help"]


nomin_query_typeList                     =   ["text","text","text","text","text","text","text",
                                              "button","button","button","button","button","button"]

nomin_query_placeholderList              =   ["address string",
                                              "max number of results (default 1) ",
                                              "timeout in secs (default None)",
                                              "limit Maximum amount of results to return (default None)",
                                              "Location.raw to include addressdetails  (default False)",
                                              "language in which to return results  (default False)",
                                              "return the result’s geometry in wkt, svg, kml, or geojson formats (default None)",
                                              None,None,None,None,None,None]

nomin_query_jsList                       =    [None,None,None,None,None,None,None,
                                               "process_query_callback(0," + str(sugm.NominatimId) + ")",
                                               "process_query_callback(1," + str(sugm.NominatimId) + ")",
                                               "process_query_callback(2," + str(sugm.NominatimId) + ")",
                                               "process_query_callback(3," + str(sugm.NominatimId) + ")",
                                               "process_query_callback(4," + str(sugm.NominatimId) + ")",
                                               "display_help_url('" + str(dfchelp.NominatimQueryHelp) + "')"]


nomin_query_reqList                      =   [0]

nomin_query_form                         =   [nomin_query_id,
                                              nomin_query_idList,
                                              nomin_query_labelList,
                                              nomin_query_typeList,
                                              nomin_query_placeholderList,
                                              nomin_query_jsList,
                                              nomin_query_reqList]

"""
#--------------------------------------------------------------------------
#   geocoder get address forms
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google get address forms
#--------------------------------------------------------------------------
"""
google_reverse_title                   =   "Google V3 Geocoder Get Address"
google_reverse_id                      =   "googlereverse"

google_reverse_idList                  =    ["grquery",
                                             "grcount",
                                             "grtimeout",
                                             "grlang",
                                             "grsensor",
                                             None,None,None,None,None,None]

google_reverse_labelList               =   ["query",
                                            "number_of_results",
                                            "timeout",
                                            "language",
                                            "sensor",
                                            "Get</br>Address",
                                            "Display</br>Bulk</br>Address",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


google_reverse_typeList                =   ["text","text","text","text","text",
                                            "button","button","button","button","button","button"]

google_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default 1) ",
                                            "enter timeout in seconds (default 1)",
                                             "enter the language (default None)",
                                             "enter sensor flag (default False)",
                                             None,None,None,None,None,None]

google_reverse_jsList                  =   [None,None,None,None,None,
                                            "process_reverse_callback(0," + str(sugm.GoogleId) + ")",
                                            "process_reverse_callback(1," + str(sugm.GoogleId) + ")",
                                            "process_reverse_callback(2," + str(sugm.GoogleId) + ")",
                                            "process_reverse_callback(3," + str(sugm.GoogleId) + ")",
                                            "process_reverse_callback(4," + str(sugm.GoogleId) + ")",
                                            "display_help_url('" + str(dfchelp.GoogleReverseHelp) + "')"]


google_reverse_reqList                 =   [0]

google_reverse_form                    =   [google_reverse_id,
                                            google_reverse_idList,
                                            google_reverse_labelList,
                                            google_reverse_typeList,
                                            google_reverse_placeholderList,
                                            google_reverse_jsList,
                                            google_reverse_reqList]

"""
#--------------------------------------------------------------------------
#   ArcGIS get address forms
#--------------------------------------------------------------------------
"""
arcgis_reverse_title                   =   "ArcGIS Geocoder Get Address"
arcgis_reverse_id                      =   "arcgisreverse"

arcgis_reverse_idList                  =    ["arquery",
                                             "arcount",
                                             "artimeout",
                                             "ardistance",
                                             "arwkid",
                                             None,None,None,None,None,None]

arcgis_reverse_labelList               =   ["query",
                                            "number_of_results",
                                            "timeout",
                                            "distance",
                                            "wkid",
                                            "Get</br>Address",
                                            "Display</br>Bulk</br>Address",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


arcgis_reverse_typeList                =   ["text","text","text","text","text",
                                            "button","button","button","button","button","button"]

arcgis_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default 1) ",
                                            "enter timeout in seconds (default None)",
                                            "Distance from the query location (default None)",
                                            "WKID to use for both input and output coordinates (default 4236)",
                                            None,None,None,None,None,None]

arcgis_reverse_jsList                  =   [None,None,None,None,None,
                                            "process_reverse_callback(0," + str(sugm.ArcGISId) + ")",
                                            "process_reverse_callback(1," + str(sugm.ArcGISId) + ")",
                                            "process_reverse_callback(2," + str(sugm.ArcGISId) + ")",
                                            "process_reverse_callback(3," + str(sugm.ArcGISId) + ")",
                                            "process_reverse_callback(4," + str(sugm.ArcGISId) + ")",
                                            "display_help_url('" + str(dfchelp.ArcGISReverseHelp) + "')"]


arcgis_reverse_reqList                 =   [0]

arcgis_reverse_form                    =   [arcgis_reverse_id,
                                            arcgis_reverse_idList,
                                            arcgis_reverse_labelList,
                                            arcgis_reverse_typeList,
                                            arcgis_reverse_placeholderList,
                                            arcgis_reverse_jsList,
                                            arcgis_reverse_reqList]

"""
#--------------------------------------------------------------------------
#   Bing get address forms
#--------------------------------------------------------------------------
"""
bing_reverse_title                     =   "Bing Geocoder Get Address"
bing_reverse_id                        =   "bingreverse"

bing_reverse_idList                    =    ["brquery",
                                             "brcount",
                                             "brtimeout",
                                             "brculture",
                                             "brcc",
                                             None,None,None,None,None,None]

bing_reverse_labelList                 =   ["query",
                                            "number_of_results",
                                            "timeout",
                                            "culture",
                                            "include_country_code",
                                            "Get</br>Address",
                                            "Display</br>Bulk</br>Address",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


bing_reverse_typeList                  =   ["text","text","text","text","text",
                                            "button","button","button","button","button","button"]

bing_reverse_placeholderList           =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default 1) ",
                                            "enter timeout in seconds (default None)",
                                            "two-letter country code (default None)",
                                            "whether to include the two-letter ISO code of the country (default False)",
                                            None,None,None,None,None,None]

bing_reverse_jsList                    =   [None,None,None,None,None,
                                            "process_reverse_callback(0," + str(sugm.BingId) + ")",
                                            "process_reverse_callback(1," + str(sugm.BingId) + ")",
                                            "process_reverse_callback(2," + str(sugm.BingId) + ")",
                                            "process_reverse_callback(3," + str(sugm.BingId) + ")",
                                            "process_reverse_callback(4," + str(sugm.BingId) + ")",
                                            "display_help_url('" + str(dfchelp.BingReverseHelp) + "')"]


bing_reverse_reqList                   =   [0]

bing_reverse_form                      =   [bing_reverse_id,
                                            bing_reverse_idList,
                                            bing_reverse_labelList,
                                            bing_reverse_typeList,
                                            bing_reverse_placeholderList,
                                            bing_reverse_jsList,
                                            bing_reverse_reqList]

"""
#--------------------------------------------------------------------------
#   Nominatim get address forms
#--------------------------------------------------------------------------
"""
nomin_reverse_title                        =   "Nominatim Geocoder Get Address"
nomin_reverse_id                           =   "nominreverse"

nomin_reverse_idList                       =    ["nrquery",
                                                 "nrcount",
                                                 "nrtimeout",
                                                 "nrlanguage",
                                                 None,None,None,None,None,None]

nomin_reverse_labelList                    =   ["query",
                                                "number_of_results",
                                                "timeout",
                                                "language",
                                                "Get</br>Address",
                                                "Get</br>Bulk</br>Address",
                                                "Change</br> Geocoder",
                                                "Clear","Return","Help"]


nomin_reverse_typeList                     =   ["text","text","text","text",
                                                "button","button","button","button","button","button"]

nomin_reverse_placeholderList              =   ["list or tuple of (latitude, longitude)",
                                                "max number of results (default 1) ",
                                                "enter timeout in seconds (default None)",
                                                "Preferred language in which to return results (default False)",
                                                None,None,None,None,None,None]

nomin_reverse_jsList                       =   [None,None,None,None,
                                                "process_reverse_callback(0," + str(sugm.NominatimId) + ")",
                                                "process_reverse_callback(1," + str(sugm.NominatimId) + ")",
                                                "process_reverse_callback(2," + str(sugm.NominatimId) + ")",
                                                "process_reverse_callback(3," + str(sugm.NominatimId) + ")",
                                                "process_reverse_callback(4," + str(sugm.NominatimId) + ")",
                                                "display_help_url('" + str(dfchelp.NominatimReverseHelp) + "')"]


nomin_reverse_reqList                      =   [0]

nomin_reverse_form                         =   [nomin_reverse_id,
                                                nomin_reverse_idList,
                                                nomin_reverse_labelList,
                                                nomin_reverse_typeList,
                                                nomin_reverse_placeholderList,
                                                nomin_reverse_jsList,
                                                nomin_reverse_reqList]

"""
#--------------------------------------------------------------------------
#    composite address input 
#--------------------------------------------------------------------------
"""
comp_addr_utility_input_title             =   "Address Conversion Columns"
comp_addr_utility_input_id                =   "dfaddresscols"
comp_addr_utility_input_idList            =   ["dfaddress",
                                               "newaddrcol",
                                               "deladdrcol",
                                               None,None,None,None,None]

comp_addr_utility_input_labelList         =   ["composite_address",
                                               "new_column_name",
                                               "drop_Address_column_flag",
                                               "Convert</br> Composite </br>Address",
                                               "Change</br> Geocoder",
                                               "Clear","Return","Help"]

comp_addr_utility_input_typeList          =   [maketextarea(4),"text","text",
                                               "button","button","button","button","button"]

comp_addr_utility_input_placeholderList   =  ["select from 'Column Names' for constant value use 'val' ie.. 'Buffalo'",
                                              "single name : [lat,long] - two cols enter list [latname,longname]",
                                              "drop address fileds used in composite address (default = False)",
                                              None,None,None,None,None]

comp_addr_utility_input_jsList            =    [None,None,None,
                                                "process_comp_addr(0)",
                                                "process_comp_addr(1)",
                                                "process_comp_addr(2)",
                                                "process_comp_addr(3)",
                                                "process_comp_addr(4)"]

comp_addr_utility_input_reqList           =   [0,1]

comp_addr_utility_input_form              =   [comp_addr_utility_input_id,
                                               comp_addr_utility_input_idList,
                                               comp_addr_utility_input_labelList,
                                               comp_addr_utility_input_typeList,
                                               comp_addr_utility_input_placeholderList,
                                               comp_addr_utility_input_jsList,
                                               comp_addr_utility_input_reqList]  

"""
#--------------------------------------------------------------------------
#    get df address input 
#--------------------------------------------------------------------------
"""
df_reverse_input_title             =   "Coordinate Conversion Columns"
df_reverse_input_id                =   "dfcoordcols"
df_reverse_input_idList            =   ["dfcoordscols","dfaddresscol"]

df_reverse_input_labelList         =   ["coords_columns",
                                        "new_column_name"]

df_reverse_input_typeList          =   ["text","text"]

df_reverse_input_placeholderList   =   ["enter Latitude and Longitude Column Names : if one lat long column enter single col name",
                                        "enter the column name the address is stored in"]

df_reverse_input_jsList            =   [None,None]

df_reverse_input_reqList           =   [0,1]

df_reverse_input_form              =   [df_reverse_input_id,
                                        df_reverse_input_idList,
                                        df_reverse_input_labelList,
                                        df_reverse_input_typeList,
                                        df_reverse_input_placeholderList,
                                        df_reverse_input_jsList,
                                        df_reverse_input_reqList]  


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    address distance input form
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
addr_dist_utility_input_title             =   "Address Distance Columns"
addr_dist_utility_input_id                =   "addrdist"
addr_dist_utility_input_idList            =   ["fromaddr",
                                               "toaddr",
                                               "disunits",
                                               "distalg",
                                               "elipsoid",
                                               None,None,None,None,None]

addr_dist_utility_input_labelList         =   ["from_location ",
                                               "to_location",
                                               "distance_units",
                                               "distance_algorithm",
                                               "elipsoid",
                                               "Calculate</br>Distance",
                                               "Display</br>Dataframe</br>Distance",
                                               "Clear","Return","Help"]

addr_dist_utility_input_typeList          =   ["text","text","text","text","text",
                                               "button","button","button","button","button"]

addr_dist_utility_input_placeholderList   =  ["enter From location : as string for address or [list] or (tuple) of floats for coords",
                                              "enter to location : as string for address or [list] or (tuple) of floats for coords",
                                              "result in km - True : km, False : miles (default = True) ",
                                              "select algorithm - 0 : Geodisc 1 : Vincenty 2 : Great_Circle (default = 0) ",
                                              "select elipsoid (default = 'WGS-84') ",
                                              None,None,None,None,None]

addr_dist_utility_input_jsList            =    [None,None,None,None,None,
                                                "process_addr_dist("+str(sugm.PROCESS_DISTANCE)+")",
                                                "process_addr_dist("+str(sugm.DISPLAY_DF_DISTANCE)+")",
                                                "process_addr_dist("+str(sugm.DISPLAY_DISTANCE)+")",
                                                "process_addr_dist("+str(sugm.DISPLAY_GEOCODING)+")",
                                                "displayhelp(" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + ")"]

addr_dist_utility_input_reqList           =   [0,1]

"""
#--------------------------------------------------------------------------
#    address dataframer distance input form
#--------------------------------------------------------------------------
"""
addr_df_dist_utility_input_title             =   "Address Distance Columns"
addr_df_dist_utility_input_id                =   "addrdist"
addr_df_dist_utility_input_idList            =   ["fromcol",
                                                  "tocol",
                                                  "newcol",
                                                  "dfdisunits",
                                                  "dfdistalg",
                                                  "dfelipsoid",
                                                  None,None,None,None,None]

addr_df_dist_utility_input_labelList         =   ["from_column ",
                                                  "to_column",
                                                  "new_distance_column",
                                                  "distance_units",
                                                  "distance_algorithm",
                                                  "elipsoid",
                                                  "Display</br>Distance",
                                                  "Calculate</br>Dataframe</br>Distance",
                                                  "Clear","Return","Help"]

addr_df_dist_utility_input_typeList          =   ["text","text","text","text","text","text",
                                                  "button","button","button","button","button"]

addr_df_dist_utility_input_placeholderList   =  ["enter From column name",
                                                 "enter to column name",
                                                 "enter column name to store distance",
                                                 "result in km - True : km, False : miles (default = True) ",
                                                 "select algorithm - 0 : Geodisc 1 : Vincenty 2 : Great_Circle (default = 0) ",
                                                 "select elipsoid (default = 'WGS-84') ",
                                                 None,None,None,None,None]

addr_df_dist_utility_input_jsList            =    [None,None,None,None,None,None,
                                                   "process_addr_dist("+str(sugm.DISPLAY_DISTANCE)+")",
                                                   "process_addr_dist("+str(sugm.PROCESS_DF_DISTANCE)+")",
                                                   "process_addr_dist("+str(sugm.DISPLAY_DF_DISTANCE)+")",
                                                   "process_addr_dist("+str(sugm.DISPLAY_GEOCODING)+")",
                                                   "displayhelp(" + str(dfchelp.GEOCODING_CALC_DF_DISTANCE_ID) + ")"]

addr_df_dist_utility_input_reqList           =   [0,1,2]

           
def get_num_input_ids(idList) :
    
    count = 0
    for i in range(len(idList)) :
        if(idList[i] != None) :
            count = count + 1
            
    return(count)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar display and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_geocode_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(geocode_utility_tb_id,
                                                               geocode_utility_tb_keyTitleList,
                                                               geocode_utility_tb_jsList,
                                                               geocode_utility_tb_centered))]) 

def display_calc_distance_input_form() :
    display_composite_form([get_input_form(InputForm(addr_dist_utility_input_id,
                                                     addr_dist_utility_input_idList,
                                                     addr_dist_utility_input_labelList,
                                                     addr_dist_utility_input_typeList,
                                                     addr_dist_utility_input_placeholderList,
                                                     addr_dist_utility_input_jsList,
                                                     addr_dist_utility_input_reqList,
                                                     shortForm=False),
                                            "Calculate Distance")])

def display_calc_df_distance_input_form() :
    display_composite_form([get_input_form(InputForm(addr_df_dist_utility_input_id,
                                                     addr_df_dist_utility_input_idList,
                                                     addr_df_dist_utility_input_labelList,
                                                     addr_df_dist_utility_input_typeList,
                                                     addr_df_dist_utility_input_placeholderList,
                                                     addr_df_dist_utility_input_jsList,
                                                     addr_df_dist_utility_input_reqList,
                                                     shortForm=False),
                                            "Calculate Dataframe Distance")])


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoder helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

 

"""
#------------------------------------------------------------------
#   get geocoder parms table
#------------------------------------------------------------------
"""
def get_geocoder_parms_table(geocid) :

    geoHeader    =   [""]
    geoRows      =   []
    geoWidths    =   [100]
    geoAligns    =   ["left"]
    geoHrefs     =   []

    if(geocid == sugm.ArcGISId)              : labelList  =   arcgis_geocoder_labelList
    elif(geocid == sugm.BingId)              : labelList  =   bing_geocoder_labelList
    elif(geocid == sugm.DataBCId)            : labelList  =   databc_geocoder_labelList
    elif(geocid == sugm.GoogleId)            : labelList  =   google_geocoder_labelList
    elif(geocid == sugm.OpenMapQuestId)      : labelList  =   mapquest_geocoder_labelList
    elif(geocid == sugm.NominatimId)         : labelList  =   nomin_geocoder_labelList
    
    geocparms = get_geocoder_parms(geocid)

    row_added = 2
    
    georow = ["Geocoder"]
    geoRows.append(georow)
    geoHrefs.append([None])
            
    georow = ["&nbsp;&nbsp;" + sugm.get_geocoder_title(geocid)]
    geoRows.append(georow)
    geoHrefs.append([None])
    
    row_added = 2
    
    if(geocparms != None) :
        
        for i in range(len(geocparms)) :
            if(len(geocparms[i]) > 0) :
                georow = ["&nbsp;" +labelList[i]]
                geoRows.append(georow)
                geoHrefs.append([None])
            
                georow = ["&nbsp;&nbsp;&nbsp;" + geocparms[i]]
                geoRows.append(georow)
                geoHrefs.append([None])
                
                row_added = row_added + 2

    geo_parms_table = dcTable("Geocoder Parms","geocparmsTable",
                              cfg.SWGeocodeUtility_ID,
                              geoHeader,geoRows,
                              geoWidths,geoAligns)
    
    geo_parms_table.set_refList(geoHrefs)
    
    #print(geoRows)
    
    geo_parms_table.set_rowspertable(row_added)
    geo_parms_table.set_small(True)
    geo_parms_table.set_smallwidth(98)
    geo_parms_table.set_smallmargin(10)
    geo_parms_table.set_border(True)
    geo_parms_table.set_checkLength(True)
    geo_parms_table.set_textLength(22)
    geo_parms_table.set_html_only(True) 

    #geo_parms_table.dump()
    geo_parms_table_html = ""
    geo_parms_table_html = geo_parms_table.get_html()
    
    return(geo_parms_table_html)    


"""
#--------------------------------------------------------------------------
#  validate geocoder kwargs
#--------------------------------------------------------------------------
"""    
def validate_cmd_parms(ptype,geocid,gqparms) :
    
    kwargs      =   []
    opstat      =   opStatus()
    
    if(ptype == sugm.INITPARMS) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_geocoder_idList 
            labelList       =   google_geocoder_labelList 
            reqList         =   google_geocoder_reqList 
        
        if(geocid == sugm.BingId) :
            idList          =   bing_geocoder_idList 
            labelList       =   bing_geocoder_labelList 
            reqList         =   bing_geocoder_reqList 

        elif(geocid == sugm.DataBCId) :
            idList          =   databc_geocoder_idList 
            labelList       =   databc_geocoder_labelList 
            reqList         =   databc_geocoder_reqList 
        
        elif(geocid == sugm.OpenMapQuestId) :
            idList          =   mapquest_geocoder_idList 
            labelList       =   mapquest_geocoder_labelList 
            reqList         =   mapquest_geocoder_reqList 
        
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_geocoder_idList 
            labelList       =   nomin_geocoder_labelList 
            reqList         =   nomin_geocoder_reqList 
        
        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_geocoder_idList 
            labelList       =   arcgis_geocoder_labelList 
            reqList         =   arcgis_geocoder_reqList 
        
    elif(ptype == sugm.QUERYPARMS) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_query_idList 
            labelList       =   google_query_labelList 
            reqList         =   google_query_reqList 
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_query_idList 
            labelList       =   bing_query_labelList 
            reqList         =   bing_query_reqList 

        elif(geocid == sugm.DataBCId) :
            idList          =   databc_query_idList 
            labelList       =   databc_query_labelList 
            reqList         =   databc_query_reqList 
        
        elif(geocid == sugm.OpenMapQuestId) :
            idList          =   mapquest_query_idList 
            labelList       =   mapquest_query_labelList 
            reqList         =   mapquest_query_reqList 
        
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_query_idList 
            labelList       =   nomin_query_labelList 
            reqList         =   nomin_query_reqList 
        
        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_query_idList 
            labelList       =   arcgis_query_labelList 
            reqList         =   arcgis_query_reqList 
            
    elif(ptype == sugm.QUERYDFPARMS) :
        comp_form = get_comp_addr_conv_form(geocid)

        idList          =   comp_form[1] 
        labelList       =   comp_form[2] 
        reqList         =   comp_form[6] 

    elif(ptype == sugm.REVERSEPARMS) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_reverse_idList 
            labelList       =   google_reverse_labelList 
            reqList         =   google_reverse_reqList 
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_reverse_idList 
            labelList       =   bing_reverse_labelList 
            reqList         =   bing_reverse_reqList 

        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_reverse_idList 
            labelList       =   arcgis_reverse_labelList 
            reqList         =   arcgis_reverse_reqList 
        
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_reverse_idList 
            labelList       =   nomin_reverse_labelList 
            reqList         =   nomin_reverse_reqList 
            
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("Reverse not supportd")
        
    missingParm     =   False
    
    if(not opstat.get_status()) :
        return(opstat)
        
    inparms = get_parms_for_input(gqparms,idList)
    
    if(len(inparms) > 0) :
    
        for i in range(len(reqList)) :
            if(not missingParm) :
                if(len(inparms[i]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Required parm not defined")
                    missingParm = True
                else : 
                    kwargs.append({"key":labelList[0], "value":inparms[0]})
        
        if(opstat.get_status()) :
            
            for i in range(len(reqList),get_num_input_ids(idList)) :
                if(i < len(inparms)) :
                    if(len(inparms[i]) > 0) :
                        kwargs.append({"key":labelList[i], "value":inparms[i]})
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No query parms defined")
        
        if(ptype == sugm.INITPARMS)          : cfg_key = sugm.get_geocoder_title(geocid) + "_geocoderkwargs"
        elif(ptype == sugm.QUERYPARMS)       : cfg_key = sugm.get_geocoder_title(geocid) + "_querykwargs"
        elif(ptype == sugm.QUERYDFPARMS)     : cfg_key = sugm.get_geocoder_title(geocid) + "_df_querykwargs"
        elif(ptype == sugm.REVERSEPARMS)     : cfg_key = sugm.get_geocoder_title(geocid) + "_reversekwargs"
        cfg.drop_config_value(cfg_key)
        
    if(opstat.get_status()) :   
        if(ptype == sugm.INITPARMS)          : cfg_key = sugm.get_geocoder_title(geocid) + "_geocoderkwargs"
        elif(ptype == sugm.QUERYPARMS)       : cfg_key = sugm.get_geocoder_title(geocid) + "_querykwargs"
        elif(ptype == sugm.QUERYDFPARMS)     : cfg_key = sugm.get_geocoder_title(geocid) + "_df_querykwargs"
        elif(ptype == sugm.REVERSEPARMS)     : cfg_key = sugm.get_geocoder_title(geocid) + "_reversekwargs"
    
        if(ptype == sugm.INITPARMS) :
            cfgvaltype =    cfg.GLOBAL
        else :
            cfgvaltype =    cfg.LOCAL
        
        if(opstat.get_status()) :
            if(len(kwargs) > 0) :
                cfg.set_config_value(cfg_key,kwargs,cfgvaltype)
            else :
                cfg.drop_config_value(cfg_key)
        else :    
            cfg.drop_config_value(cfg_key)
        
    return(opstat)   

"""
#--------------------------------------------------------------------------
#  get geocoder kwargs for init
#--------------------------------------------------------------------------
"""
def get_geocoder_form_parms_list(ptype,geocid) :
    
    if(ptype == sugm.INITPARMS)          : geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_geocoderkwargs",cfg.GLOBAL)    
    elif(ptype == sugm.QUERYPARMS)       : geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_querykwargs")    
    elif(ptype == sugm.QUERYDFPARMS)     : geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_df_querykwargs")    
    elif(ptype == sugm.REVERSEPARMS)     : geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_reversekwargs")    
    elif(ptype == sugm.REVERSEDFPARMS)   : geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_df_reversekwargs")    
    
    if(ptype == sugm.QUERYPARMS) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_query_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_query_labelList 
        elif(geocid == sugm.DataBCId)            : labelList       =   databc_query_labelList 
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_query_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_query_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_query_labelList 
    elif(ptype == sugm.REVERSEPARMS) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_reverse_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_reverse_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_reverse_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_reverse_labelList 

    geoplist = []

    if(geokwargs == None) :
        return(geoplist)
    else :
        for i in range(len(labelList)) :
            found = False
            for j in range(len(geokwargs)) :
                if(geokwargs[j].get("key") == labelList[i]) :
                    geoplist.append(geokwargs[j].get("value"))
                    found = True
            if(not found) :
                geoplist.append("")
        
        return(geoplist)

  
"""
#--------------------------------------------------------------------------
#  get command kwargs stored in config
#--------------------------------------------------------------------------
"""
def get_geocoder_cmd_parms(ptype,geocid) :

        
    if(ptype == sugm.INITPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_geocoderkwargs",cfg.GLOBAL)
    elif(ptype == sugm.QUERYPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_querykwargs")
    elif(ptype == sugm.QUERYDFPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_df_querykwargs")
    elif(ptype == sugm.REVERSEPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_reversekwargs")
 
    #print("get_geocoder_cmd_parms",geokwargs)
    geocparms = {}

    if(geokwargs != None) :
        for i in range(len(geokwargs)) : 
            geoparm = geokwargs[i]
        
            if( (geoparm.get("value") != None) and (geoparm.get("value") != "" )) :
                geocparms.update({geoparm.get("key"):geoparm.get("value")})

    if(len(geocparms) == 0) :
        return(None)
    else :
        return(geocparms)

def get_df_col_names_table(tableid,owner,callback,colsList=None,nonnumericOnly=False) :

    if(not (colsList == None)) :
        colnames = colsList
    else :
        colnames            =   cfg.get_dc_dataframe().columns.values.tolist() 
    
    colnamesHeader      =   [""]
    colnamesRows        =   []
    colnamesWidths      =   [100]
    colnamesAligns      =   ["left"]
    colnamesHrefs       =   []
    
    for i in range(len(colnames)) :
        
        if( (nonnumericOnly)  and (colsList == None) ): 

            if( not (is_numeric_col(cfg.get_dc_dataframe(),colnames[i])) ) :
                colnamesrow = [colnames[i]]
                colnamesRows.append(colnamesrow)
                colnamesHrefs.append([callback])
                
        else :        
            colnamesrow = [colnames[i]]
            colnamesRows.append(colnamesrow)
            colnamesHrefs.append([callback])
        
    colnames_table = None
                
    colnames_table = dcTable("Column Names",tableid,owner,
                              colnamesHeader,colnamesRows,
                              colnamesWidths,colnamesAligns)
            
    colnames_table.set_refList(colnamesHrefs)
    
    colnames_table.set_small(True)
    colnames_table.set_smallwidth(98)
    colnames_table.set_smallmargin(10)

    colnames_table.set_border(True)
        
    colnames_table.set_checkLength(True)
            
    colnames_table.set_textLength(26)
    colnames_table.set_html_only(True) 
    
    colnames_table.set_tabletype(ROW_MAJOR)
    colnames_table.set_rowspertable(14)

    listHtml = get_row_major_table(colnames_table,SCROLL_NEXT,False)
        
    return(listHtml)


"""
#------------------------------------------------------------------
#   display input froms for query and reverse
#------------------------------------------------------------------
"""
def display_geocode_inputs(formid,parms,ptype,fulldf=False,showfull=False) :

    if(parms == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
        inparms =   None
    else :
        geocid  =    parms[1]
        inparms =    parms[2]
    
    if(fulldf) :
        if (formid == sugm.ADDRESS_CONVERSION) :
            geo_parms_html = get_df_col_names_table("gedfcolnamesTable",cfg.SWGeocodeUtility_ID,"add_df_column")
            form = get_comp_addr_conv_form(geocid)
        else :
            geo_parms_html = get_geocoder_parms_table(geocid)
            form = get_df_coords_conv_form(geocid)
    else :
        geo_parms_html = get_geocoder_parms_table(geocid)
        
        if(formid == sugm.ADDRESS_CONVERSION) :
            if(geocid == sugm.ArcGISId)              : form    =   arcgis_query_form
            elif(geocid == sugm.BingId)              : form    =   bing_query_form
            elif(geocid == sugm.DataBCId)            : form    =   databc_query_form
            elif(geocid == sugm.GoogleId)            : form    =   google_query_form
            elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_query_form
            elif(geocid == sugm.NominatimId)         : form    =   nomin_query_form
        else :
            if(geocid == sugm.ArcGISId)              : form    =   arcgis_reverse_form
            elif(geocid == sugm.BingId)              : form    =   bing_reverse_form
            elif(geocid == sugm.GoogleId)            : form    =   google_reverse_form
            elif(geocid == sugm.NominatimId)         : form    =   nomin_reverse_form
 
    
    if(inparms != None) :
        parmslist = get_parms_for_input(inparms,form[1]) 
    else :
        parmslist = get_geocoder_form_parms_list(ptype,geocid)
    
    if(len(parmslist) > 0) : 
        if(len(parmslist[0]) > 0) :   
            cfg.set_config_value(form[0]+"Parms",parmslist)
    
    from dfcleanser.common.html_widgets import InputForm
    geofunc_input_form = InputForm(form[0],
                                   form[1],
                                   form[2],
                                   form[3],
                                   form[4],
                                   form[5],
                                   form[6],
                                   shortForm=False)
    
    geofunc_input_form.set_gridwidth(600)
    if(showfull) :
        geofunc_input_form.set_fullparms(True)    
    
    geofunc_input_html = ""
    geofunc_input_html = geofunc_input_form.get_html()
    
    if (formid == sugm.ADDRESS_CONVERSION) :
        if(fulldf) :
            geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Dataframe Address(s) To Coordinates</h4>" 
        else :
            geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Address To Coordinates</h4>"
    else :
        if(fulldf) :
            geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Dataframe Coordinates To Address</h4>"
        else :
            geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Coordinates To Address</h4>"
        
    display_grid("acconv_wrapper",
                 geofunc_heading_html,
                 geo_parms_html,
                 geofunc_input_html,
                 None)


"""
#------------------------------------------------------------------
#   get the composite address input form
#------------------------------------------------------------------
"""
def get_comp_addr_conv_form(geocid) :

    if(geocid == sugm.ArcGISId)              : form    =   arcgis_query_form
    elif(geocid == sugm.BingId)              : form    =   bing_query_form
    elif(geocid == sugm.DataBCId)            : form    =   databc_query_form
    elif(geocid == sugm.GoogleId)            : form    =   google_query_form
    elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_query_form
    elif(geocid == sugm.NominatimId)         : form    =   nomin_query_form


    comp_addr_form                  =   []
    comp_addr_form_idList           =   []
    comp_addr_form_labelList        =   []
    comp_addr_form_typeList         =   []
    comp_addr_form_placeholderList  =   []
    comp_addr_form_jsList           =   []
    
    comp_addr_form_idList = []
    for i in range (3) :
        comp_addr_form_idList.append(comp_addr_utility_input_idList[i])
        comp_addr_form_labelList.append(comp_addr_utility_input_labelList[i])
        comp_addr_form_typeList.append(comp_addr_utility_input_typeList[i])
        comp_addr_form_placeholderList.append(comp_addr_utility_input_placeholderList[i])
        comp_addr_form_jsList.append(comp_addr_utility_input_jsList[i])
        
    for i in range (1,len(form[1])) :
        comp_addr_form_idList.append(form[1][i])
        comp_addr_form_labelList.append(form[2][i])
        comp_addr_form_typeList.append(form[3][i])
        comp_addr_form_placeholderList.append(form[4][i])
        comp_addr_form_jsList.append(form[5][i])
    

    for i in range(len(comp_addr_form_labelList)) :
        if(comp_addr_form_labelList[i] == "Get</br>Coords") : comp_addr_form_labelList[i] = "Display</br>Get</br>Coords"
        if(comp_addr_form_labelList[i] == "Display</br>Bulk</br>Coords") : comp_addr_form_labelList[i] = "Get</br>Bulk</br>Coords"
        
    for i in range(len(comp_addr_form_jsList)) :
        if(not (comp_addr_form_jsList[i] == None)) :
            if(comp_addr_form_jsList[i].find("process_query_callback(0,") > -1)   :   
                comp_addr_form_jsList[i] = comp_addr_form_jsList[i].replace("process_query_callback(0,","process_query_callback(6,")
            if(comp_addr_form_jsList[i].find("process_query_callback(1,") > -1)   :   
                comp_addr_form_jsList[i] = comp_addr_form_jsList[i].replace("process_query_callback(1,","process_query_callback(7,")
        
    comp_addr_form          =   [form[0]+"DF",
                                 comp_addr_form_idList,
                                 comp_addr_form_labelList,
                                 comp_addr_form_typeList,
                                 comp_addr_form_placeholderList,
                                 comp_addr_form_jsList,
                                 comp_addr_utility_input_reqList]
    
    return(comp_addr_form)


"""
#------------------------------------------------------------------
#   get the cf coordinates input form
#------------------------------------------------------------------
"""
def get_df_coords_conv_form(geocid) :

    if(geocid == sugm.ArcGISId)              : form    =   arcgis_reverse_form
    elif(geocid == sugm.BingId)              : form    =   bing_reverse_form
    elif(geocid == sugm.GoogleId)            : form    =   google_reverse_form
    elif(geocid == sugm.NominatimId)         : form    =   nomin_reverse_form


    df_coords_form                  =   []
    df_coords_form_idList           =   []
    df_coords_form_labelList        =   []
    df_coords_form_typeList         =   []
    df_coords_form_placeholderList  =   []
    df_coords_form_jsList           =   []
    
    df_coords_form_idList = []
    for i in range (2) :
        df_coords_form_idList.append(df_reverse_input_idList[i])
        df_coords_form_labelList.append(df_reverse_input_labelList[i])
        df_coords_form_typeList.append(df_reverse_input_typeList[i])
        df_coords_form_placeholderList.append(df_reverse_input_placeholderList[i])
        df_coords_form_jsList.append(None)
        
    for i in range (1,len(form[1])) :
        df_coords_form_idList.append(form[1][i])
        df_coords_form_labelList.append(form[2][i])
        df_coords_form_typeList.append(form[3][i])
        df_coords_form_placeholderList.append(form[4][i])
        df_coords_form_jsList.append(form[5][i])
    

    for i in range(len(df_coords_form_labelList)) :
        if(df_coords_form_labelList[i] == "Get</br>Address") : df_coords_form_labelList[i] = "Display</br>Get</br>Address"
        if(df_coords_form_labelList[i] == "Display</br>Bulk</br>Address") : df_coords_form_labelList[i] = "Get</br>Bulk</br>Address"
        
    for i in range(len(df_coords_form_jsList)) :
        if(not (df_coords_form_jsList[i] == None)) :
            if(df_coords_form_jsList[i].find("process_reverse_callback(0,") > -1)   :   
                df_coords_form_jsList[i] = df_coords_form_jsList[i].replace("process_reverse_callback(0,","process_reverse_callback(8,")
            if(df_coords_form_jsList[i].find("process_reverse_callback(1,") > -1)   :   
                df_coords_form_jsList[i] = df_coords_form_jsList[i].replace("process_reverse_callback(1,","process_reverse_callback(9,")
        
    df_coords_form          =   [form[0]+"DF",
                                 df_coords_form_idList,
                                 df_coords_form_labelList,
                                 df_coords_form_typeList,
                                 df_coords_form_placeholderList,
                                 df_coords_form_jsList,
                                 df_reverse_input_reqList]
    
    return(df_coords_form)
    
"""
#------------------------------------------------------------------
#   display composite address form
#------------------------------------------------------------------
"""
def display_comp_addr_geocode_inputs(parms) :
    #return()
    print("display_comp_addr_geocode_inputs",parms)
    df_cols         =   cfg.get_dc_dataframe().columns
    
    if(parms == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
    else :
        geocid = parms[1]
    
    collistHeader    =   [""]
    collistRows      =   []
    collistWidths    =   [100]
    collistAligns    =   ["left"]
    collistHrefs     =   []

    reflist          =   ["acselcol"]
        
    for i in range(len(df_cols)) :
        collistrow = [df_cols[i]]
        collistRows.append(collistrow)
        collistHrefs.append(reflist)
        
    col_names_table = dcTable("Column Names","accolnamesTable",
                              cfg.SWGeocodeUtility_ID,
                              collistHeader,collistRows,
                              collistWidths,collistAligns)
    
    col_names_table.set_refList(collistHrefs)
    
    col_names_table.set_rowspertable(len(df_cols))
    col_names_table.set_small(True)
    col_names_table.set_smallwidth(98)
    col_names_table.set_smallmargin(10)
    #col_names_table.set_smallfsize(12)
    col_names_table.set_border(True)
    col_names_table.set_checkLength(False)
    col_names_table.set_html_only(True) 
    
    acconv_table_html = ""
    col_names_table.set_tabletype(ROW_MAJOR)
    col_names_table.set_rowspertable(9)

    acconv_table_html = get_row_major_table(col_names_table,SCROLL_NEXT,False)

    comp_addr_form  =   get_comp_addr_conv_form(geocid)
    
    from dfcleanser.common.html_widgets import InputForm
    acconv_input_form = InputForm(comp_addr_form[0],
                                  comp_addr_form[1],
                                  comp_addr_form[2],
                                  comp_addr_form[3],
                                  comp_addr_form[4],
                                  comp_addr_form[5],
                                  comp_addr_form[6],
                                  shortForm=False)
    
    acconv_input_form.set_gridwidth(580)
    
    acconv_input_html = ""
    acconv_input_html = acconv_input_form.get_html() 
        
    acconv_heading_html = "<h4>" + get_html_spaces(6) + "Get Address Coords (dataframe) : "+ sugm.get_geocoder_title(geocid) + "</h4>"

    display_grid("compaddr_wrapper",
                 acconv_heading_html,
                 acconv_table_html,
                 acconv_input_html,
                 None)



"""
#------------------------------------------------------------------
#   get a table for the geocoder options
#------------------------------------------------------------------
""" 
def get_geocoder_table() :
    
    geocslistHeader     =   [""]
    geocslistRows       =   []
    geocslistWidths     =   [100]
    geocslistAligns     =   ["left"]
    geocslistHrefs      =   []

    geocstexts          =   []
    geocshrefs          =   []
    
    for i in range(len(sugm.supported_Geocoders)) :
        geocstexts.append("&nbsp;&nbsp;" + sugm.get_geocoder_title(sugm.supported_Geocoders[i]))
        geocshrefs.append("select_geocoder")

    for i in range(len(geocstexts)) :
        geocslistRows.append([geocstexts[i]])    
        geocslistHrefs.append([geocshrefs[i]])
        
    geocs_names_table = dcTable("Geocoders","geocoderssTable",
                                cfg.SWGeocodeUtility_ID,
                                geocslistHeader,geocslistRows,
                                geocslistWidths,geocslistAligns)

    geocs_names_table.set_refList(geocslistHrefs)
        
    geocs_names_table.set_rowspertable(len(geocstexts))
    geocs_names_table.set_small(True)
    geocs_names_table.set_smallwidth(98)
    geocs_names_table.set_smallmargin(10)

    geocs_names_table.set_border(True)
    geocs_names_table.set_checkLength(False)
    geocs_names_table.set_html_only(True) 
    
    #table_names_table.dump()
     
    listHtml = geocs_names_table.get_html()
    
    return(listHtml)


"""
#--------------------------------------------------------------------------
#  get geocoder input parms from geocoder kwargs
#--------------------------------------------------------------------------
"""
def get_geocoder_parms(geocid)  :

    #print("get_geocoder_parms",geocid)    
    parmsList = []
    
    if(geocid == None)                       : geocid          =   sugm.GoogleId 
    elif(geocid == sugm.GoogleId)            : labelList       =   google_geocoder_labelList 
    elif(geocid == sugm.BingId)              : labelList       =   bing_geocoder_labelList 
    elif(geocid == sugm.DataBCId)            : labelList       =   databc_geocoder_labelList 
    elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_geocoder_labelList 
    elif(geocid == sugm.NominatimId)         : labelList       =   nomin_geocoder_labelList 
    elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_geocoder_labelList 
    
    cfg_key = sugm.get_geocoder_title(geocid) + "_geocoderkwargs"   
    kwargs = cfg.get_config_value(cfg_key,cfg.GLOBAL)

    if(kwargs == None) :
        parmsList = None
    else : 
        kwdict = {}
        for i in range(len(kwargs)) :
            kwdict.update({kwargs[i].get("key"):kwargs[i].get("value")})

        for i in range(len(labelList)) :
            if(labelList[i] != None) :
                pval = kwdict.get(labelList[i])
                if(pval == None) :
                    parmsList.append("")
                else :    
                    parmsList.append(pval)

    return(parmsList)
    
    
"""
#------------------------------------------------------------------
#   display geocoder inputs form
#------------------------------------------------------------------
"""     
def display_geocoders(geocodeid,showfull=False) :
    
    listHtml = get_geocoder_table()
    
    if(geocodeid == None) :
        geocodeid       =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocodeid == None) : 
            geocodeid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocodeid)

    geocoder_input_form = None
    
    if( (geocodeid == None) or (geocodeid == sugm.GoogleId) ) :

        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.GoogleId)
        geocoder_input_form   =   [google_geocoder_id,
                                   google_geocoder_idList,
                                   google_geocoder_labelList,
                                   google_geocoder_typeList,
                                   google_geocoder_placeholderList,
                                   google_geocoder_jsList,
                                   google_geocoder_reqList]
        
    elif(geocodeid == sugm.BingId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BingId)
        geocoder_input_form   =   [bing_geocoder_id,
                                   bing_geocoder_idList,
                                   bing_geocoder_labelList,
                                   bing_geocoder_typeList,
                                   bing_geocoder_placeholderList,
                                   bing_geocoder_jsList,
                                   bing_geocoder_reqList]

    elif(geocodeid == sugm.DataBCId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.DataBCId)
        geocoder_input_form   =   [databc_geocoder_id,
                                   databc_geocoder_idList,
                                   databc_geocoder_labelList,
                                   databc_geocoder_typeList,
                                   databc_geocoder_placeholderList,
                                   databc_geocoder_jsList,
                                   databc_geocoder_reqList]

    elif(geocodeid == sugm.OpenMapQuestId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.OpenMapQuestId)
        geocoder_input_form   =   [mapquest_geocoder_id,
                                   mapquest_geocoder_idList,
                                   mapquest_geocoder_labelList,
                                   mapquest_geocoder_typeList,
                                   mapquest_geocoder_placeholderList,
                                   mapquest_geocoder_jsList,
                                   mapquest_geocoder_reqList]

    elif(geocodeid == sugm.NominatimId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.NominatimId)
        geocoder_input_form   =   [nomin_geocoder_id,
                                   nomin_geocoder_idList,
                                   nomin_geocoder_labelList,
                                   nomin_geocoder_typeList,
                                   nomin_geocoder_placeholderList,
                                   nomin_geocoder_jsList,
                                   nomin_geocoder_reqList]

    elif(geocodeid == sugm.ArcGISId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.ArcGISId)
        geocoder_input_form   =   [arcgis_geocoder_id,
                                   arcgis_geocoder_idList,
                                   arcgis_geocoder_labelList,
                                   arcgis_geocoder_typeList,
                                   arcgis_geocoder_placeholderList,
                                   arcgis_geocoder_jsList,
                                   arcgis_geocoder_reqList]
    
    geocode_heading_html = "<h4>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Geocoder Parms - " + sugm.get_geocoder_title(geocodeid) + "</h4>"

    parmsList = get_geocoder_parms(geocodeid)
    
    if(parmsList != None) :
        cfg.set_config_value(geocoder_input_form[0]+"Parms",parmsList)    
    
    from dfcleanser.common.html_widgets import InputForm
    geocode_input_form = InputForm(geocoder_input_form[0],
                                   geocoder_input_form[1],
                                   geocoder_input_form[2],
                                   geocoder_input_form[3],
                                   geocoder_input_form[4],
                                   geocoder_input_form[5],
                                   geocoder_input_form[6],
                                   shortForm=False)
    
    geocode_input_form.set_gridwidth(640)
    
    if(showfull) :
        geocode_input_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = geocode_input_form.get_html() 
    
    display_grid("sql_connector_wrapper",
                 geocode_heading_html,
                 listHtml,
                 geocode_input_html,None)

