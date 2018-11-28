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
                                            get_input_form, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

from dfcleanser.common.common_utils import (get_parms_for_input, display_grid, is_numeric_col, display_notes)


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

geocode_utility_tb_keyTitleList         =   ["Simple</br>Geocoding",
                                             "Bulk</br>Geocoding",
                                             "Calculate</br>Distance",
                                             "Select</br>Geocoder",
                                             "Clear","Help"]

geocode_utility_tb_jsList               =   ["process_geomain_callback(" + str(sugm.DISPLAY_GET_COORDS) + ")",
                                             "process_geomain_callback(" + str(sugm.DISPLAY_BULK_GET_COORDS) + ")",
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
                                          "agagent",
                                          "agscheme",
                                          "agtimeout",
                                          "agproxies",
                                          None,None,None,None,None,None]

arcgis_geocoder_labelList           =   ["username",
                                         "password",
                                         "referer",
                                         "scheme",
                                         "timeout",
                                         "proxies",
                                         "Test</br>Geocoder",
                                         "Simple</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


arcgis_geocoder_typeList            =   ["text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

arcgis_geocoder_placeholderList     =   ["ArcGIS username (default : None)",
                                         "ArcGIS password (default : None)",
                                         "ArcGIS referer (default : my-application)",
                                         "Desired scheme (default : https)",
                                         "Time, in seconds (default : 20)",
                                         "enter proxies dict (default : None)",
                                         None,None,None,None,None,None]

arcgis_geocoder_jsList              =   [None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.ArcGISId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.ArcGISId) + ")",
                                         "display_help_url('" + str(dfchelp.ArcGISInitHelp) + "')"]


arcgis_geocoder_reqList             =   [0,1,2]

arcgis_geocoder_form                =   [arcgis_geocoder_id,
                                         arcgis_geocoder_idList,
                                         arcgis_geocoder_labelList,
                                         arcgis_geocoder_typeList,
                                         arcgis_geocoder_placeholderList,
                                         arcgis_geocoder_jsList,
                                         arcgis_geocoder_reqList]

arcgis_user_agent	= "my-application"

"""
#--------------------------------------------------------------------------
#   google geocoder parms
#--------------------------------------------------------------------------
"""
google_geocoder_title               =   "Google V3 Geocoder"
google_geocoder_id                  =   "googlegeocoder"

google_geocoder_idList              =    ["ggapikey",
                                          "ggclient",
                                          "ggsecretkey",
                                          "ggagent",
                                          "ggdomain",
                                          "ggscheme",
                                          "ggproxies",
                                          "ggformatstr",
                                          "ggsslcontext",
                                          "ggchannel",
                                          None,None,None,None,None,None]

google_geocoder_labelList           =   ["api_key",
                                         "client_id",
                                         "secret_key",
                                         "user_agent",
                                         "domain",
                                         "scheme",
                                         "proxies",
                                         "format_string",
                                         "ssl_context",
                                         "channel",
                                         "Test</br>Geocoder",
                                         "Simple</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


google_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

google_geocoder_placeholderList     =   ["google API key",
                                         "enter account client id. (default - None) required for premier",
                                         "enter account secret key (default - None) required for premier",
                                         "enter custom User-Agent header (default - None)",
                                         "localized Google Maps domain (default - ‘maps.googleapis.com’)",
                                         "enter scheme (default https)",
                                         "enter proxies dict (default - DEFAULT_SENTINEL)",
                                         "format string (default - '%s')",
                                         "ssl_context (default - DEFAULT_SENTINEL)",
                                         "enter channel identifier (default - None)",
                                         None,None,None,None,None,None]

google_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.GoogleId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.GoogleId) + ")",
                                         "display_help_url('" + str(dfchelp.GoogleInitHelp) + "')"]


google_geocoder_reqList             =   [0,1,2]

google_geocoder_form                =   [google_geocoder_id,
                                         google_geocoder_idList,
                                         google_geocoder_labelList,
                                         google_geocoder_typeList,
                                         google_geocoder_placeholderList,
                                         google_geocoder_jsList,
                                         google_geocoder_reqList]

google_API_Key    =   "AIzaSyCAJESZO5xlryhuG_scxZ9ryaqj7140fTc"


"""
#--------------------------------------------------------------------------
#   bing geocoder parms
#--------------------------------------------------------------------------
"""
bing_geocoder_title                 =   "Bing Geocoder"
bing_geocoder_id                    =   "binggeocoder"

bing_geocoder_idList                =    ["bingapikey",
                                          "bingagent",
                                          "bingtimeout",
                                          "bingfstring",
                                          "bingscheme",
                                          "bingproxies",
                                          None,None,None,None,None,None]

bing_geocoder_labelList             =   ["api_key",
                                         "user_agent",
                                         "timeout",
                                         "format_string",
                                         "scheme",
                                         "proxies",
                                         "Test</br>Geocoder",
                                         "Simple</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


bing_geocoder_typeList              =   ["text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

bing_geocoder_placeholderList       =   ["enter Bing Maps API key",
                                         "user agent (default - my-application)",
                                         "enter timeout in seconds (default 20)",
                                         "enter format string (default %s)",
                                         "enter scheme (default https)",
                                         "proxies dict (default None)",
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

bing_API_Key    =   "AhwVfAKfw8CF4K2cwNgfj61-jYzQll4N92sjC6d3Hz-9O4HdCB34MwGObvhoJwB4"



"""
#--------------------------------------------------------------------------
#   OpenMapQuest geocoder parms
#--------------------------------------------------------------------------
"""
mapquest_geocoder_title                 =   "OpenMapQuest Geocoder"
mapquest_geocoder_id                    =   "mapquestgeocoder"

mapquest_geocoder_idList                =    ["mapquestapikey",
                                              "mapquestagent",
                                              "mapquesttimeout",
                                              "mapquestfstring",
                                              "mapquestscheme",
                                              "mapquestproxies",
                                              None,None,None,None,None,None]

mapquest_geocoder_labelList             =   ["api_key",
                                             "user_agent",
                                             "timeout",
                                             "format_string",
                                             "scheme ",
                                             "proxies",
                                             "user_agent",
                                             "Test</br>Geocoder",
                                             "Simple</br>Geocoding",
                                             "Bulk</br>Geocoding",
                                             "Clear","Return","Help"]

mapquest_geocoder_typeList              =   ["text","text","text","text","text","text",
                                             "button","button","button","button","button","button"]

mapquest_geocoder_placeholderList       =   ["enter MapQuest API Key",
                                             "enter user agent (default 'my-application'",
                                             "enter timeout in seconds (default 20)",
                                             "enter format string (default '%s'",
                                             "enter scheme (default 'https')",
                                             "enter proxies dict (default None)",
                                             
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


Consumer_Key	= "o9GNTP0ut9TNSutr6oDBCk78YWbl4feJ"
Consumer_Secret	= "X88Lt57EztVhijrs"

"""
#--------------------------------------------------------------------------
#   Nominatim geocoder parms
#--------------------------------------------------------------------------
"""
nomin_geocoder_title                =   "Nominatim Geocoder"
nomin_geocoder_id                   =   "nomingeocoder"

nomin_geocoder_idList               =    ["nominagent",
                                          "nomintimeout",
                                          "nominformat",
                                          "nominview",
                                          "nominbias",
                                          "nominproxies",
                                          "nomindomain",
                                          "nominscheme",
                                           None,None,None,None,None,None]

nomin_geocoder_labelList            =   ["user_agent",
                                         "timeout",
                                         "format_string",
                                         "view_box",
                                         "country_bias",
                                         "proxies",
                                         "domain",
                                         "scheme",
                                         "Test</br>Geocoder",
                                         "Simple</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


nomin_geocoder_typeList             =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

nomin_geocoder_placeholderList      =   ["enter custom User-Agent (default - my-application)",
                                         "enter timeout in secs (default 20)",
                                         "enter format string (default %s)",
                                         "Coordinates to restrict search within. (default None)",
                                         "enter country to bias results (default - United States)",
                                         "enter proxies dict)",
                                         "enter domain (default None)",
                                         "enter scheme (default https)",
                                         None,None,None,None,None,None]

nomin_geocoder_jsList               =   [None,None,None,None,None,None,None,None,
                                         "process_geocoder_callback(0," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(1," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(2," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(3," + str(sugm.NominatimId) + ")",
                                         "process_geocoder_callback(4," + str(sugm.NominatimId) + ")",
                                         "display_help_url('" + str(dfchelp.NominatimInitHelp) + "')"]


nomin_geocoder_reqList              =   [0]

nomin_geocoder_form                 =   [nomin_geocoder_id,
                                         nomin_geocoder_idList,
                                         nomin_geocoder_labelList,
                                         nomin_geocoder_typeList,
                                         nomin_geocoder_placeholderList,
                                         nomin_geocoder_jsList,
                                         nomin_geocoder_reqList]

nomin_user_agent	= "my-application"

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
                                          None,None,None,None,None,None]

arcgis_query_labelList              =   ["address(s)",
                                         "number_of_results",
                                         "timeout",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


arcgis_query_typeList               =   [maketextarea(6),"text","text",
                                         "button","button","button","button","button","button"]

arcgis_query_placeholderList        =   ["single address string or [] list of address strings",
                                         "max number of results per address (default - 1) ",
                                         "enter timeout in seconds (default - 10 seconds)",
                                         None,None,None,None,None,None]

arcgis_query_jsList                 =   [None,None,None,
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

google_query_labelList              =   ["address(s)",
                                         "number_of_results",
                                         "timeout",
                                         "bounds",
                                         "region",
                                         "components",
                                         "language",
                                         "sensor",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


google_query_typeList               =   [maketextarea(6),"text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

google_query_placeholderList        =   ["single address string or [] list of address strings",
                                         "max number of results per address (default - 1) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter bounding box of the viewport (default - None)",
                                         "enter the ccTLD region code (default - None)",
                                         "enter components dict) (default - None)",
                                         "enter the language (default - None)",
                                         "enter sensor flag (default - False)",
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
                                          "bqtimeout",
                                          "bqloc",
                                          "bqculture",
                                          "bqnbc",
                                          "bqcc",
                                          None,None,None,None,None,None]

bing_query_labelList                =   ["address(s)",
                                         "number_of_results",
                                         "timeout",
                                         "user_location",
                                         "culture ",
                                         "include_neighborhood",
                                         "include_country_code",
                                         "Get</br>Coords",
                                         "Get</br>Address",
                                         "Change</br> Geocoder",
                                         "Clear","Return","Help"]


bing_query_typeList                 =   [maketextarea(6),"text","text","text","text","text","text",
                                         "button","button","button","button","button","button"]

bing_query_placeholderList          =   ["single address string or [] list of address strings",
                                         "max number of results per address (default - 1) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter coords to prioritize to (default - None)",
                                         "enter two-letter country code (default - None) ",
                                         "return neighborhood field (default - False)",
                                         "return 2 digit country code (default - False)",
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
#   OpenMapQuest get coords form
#--------------------------------------------------------------------------
"""
mapquest_query_title                     =   "OpenMapQuest Get Coordinates"
mapquest_query_id                        =   "mapquestquery"

mapquest_query_idList                    =  ["mqquery",
                                             "mqcount",
                                             "mqtimeout",
                                             None,None,None,None,None,None]

mapquest_query_labelList                 =  ["address(s)",
                                             "number_of_results",
                                             "timeout",
                                             "Get</br>Coords",
                                             "Get</br>Address",
                                             "Change</br> Geocoder",
                                             "Clear","Return","Help"]


mapquest_query_typeList                  =   [maketextarea(6),"text","text",
                                              "button","button","button","button","button","button"]

mapquest_query_placeholderList           =   ["single address string or [] list of address strings",
                                              "max number of results per address (default - 1) ",
                                              "timeout in secs (default - 1)",
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
                                             "nqaddr",
                                             "nqlang",
                                             "nqgeom",
                                             None,None,None,None,None,None]

nomin_query_labelList                    =  ["address(s)",
                                             "number_of_results",
                                             "timeout",
                                             "addressdetails",
                                             "language",
                                             "geometry",
                                             "Get</br>Coords",
                                             "Get</br>Address",
                                             "Change</br> Geocoder",
                                             "Clear","Return","Help"]


nomin_query_typeList                     =   [maketextarea(6),"text","text","text","text","text",
                                              "button","button","button","button","button","button"]

nomin_query_placeholderList              =   ["single address string or [] list of address strings",
                                              "max number of results per address (default - 1) ",
                                              "timeout in secs (default - 20)",
                                              "Location.raw to include address details  (default - False)",
                                              "language in which to return results  (default - English)",
                                              "return the result’s geometry in wkt, svg, kml, or geojson formats (default - None)",
                                              None,None,None,None,None,None]

nomin_query_jsList                       =    [None,None,None,None,None,None,
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

google_reverse_labelList               =   ["latitude_longitude(s)",
                                            "number_of_results",
                                            "timeout",
                                            "language",
                                            "sensor",
                                            "Get</br>Address",
                                            "Get</br>Coordinates",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


google_reverse_typeList                =   [maketextarea(6),"text","text","text","text",
                                            "button","button","button","button","button","button"]

google_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default - 1) ",
                                            "enter timeout in seconds (default - 5)",
                                            "enter the language (default - English)",
                                            "enter sensor flag (default - False)",
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

arcgis_reverse_labelList               =   ["latitude_longitude(s)",
                                            "number_of_results",
                                            "timeout",
                                            "distance",
                                            "wkid",
                                            "Get</br>Address",
                                            "Get</br>Coordinates",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


arcgis_reverse_typeList                =   [maketextarea(6),"text","text","text","text",
                                            "button","button","button","button","button","button"]

arcgis_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default - 1) ",
                                            "enter timeout in seconds (default - 5)",
                                            "Distance from the query location (default - None)",
                                            "WKID to use for both input and output coordinates (default - 4236)",
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

bing_reverse_labelList                 =   ["latitude_longitude(s)",
                                            "number_of_results",
                                            "timeout",
                                            "culture",
                                            "include_country_code",
                                            "Get</br>Address",
                                            "Get</br>Coordinates",
                                            "Change</br> Geocoder",
                                            "Clear","Return","Help"]


bing_reverse_typeList                  =   [maketextarea(6),"text","text","text","text",
                                            "button","button","button","button","button","button"]

bing_reverse_placeholderList           =   ["list or tuple of (latitude, longitude)",
                                            "max number of results (default - 1) ",
                                            "enter timeout in seconds (default - 5)",
                                            "two-letter country code (default - None)",
                                            "whether to include the two-letter ISO code of the country (default - False)",
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
#   OpenMapQuest get address forms
#--------------------------------------------------------------------------
"""
mapquest_reverse_title                     =   "OpenMapQuest Geocoder Get Address"
mapquest_reverse_id                        =   "nominreverse"

mapquest_reverse_idList                    =    ["mrquery",
                                                 "mrcount",
                                                 "mrtimeout",
                                                 "mrlanguage",
                                                 "mradetails",
                                                 None,None,None,None,None,None]

mapquest_reverse_labelList                 =   ["latitude_longitude(s)",
                                                "number_of_results",
                                                "timeout",
                                                "language",
                                                "addressdetails",
                                                "Get</br>Address",
                                                "Get</br>Coordinates",
                                                "Change</br> Geocoder",
                                                "Clear","Return","Help"]


mapquest_reverse_typeList                  =   [maketextarea(6),"text","text","text","text",
                                                "button","button","button","button","button","button"]

mapquest_reverse_placeholderList           =   ["list or tuple of (latitude, longitude)",
                                                "max number of results (default - 1) ",
                                                "enter timeout in seconds (default - 5)",
                                                "Preferred language in which to return results (default - English)",
                                                "include address details such as city, county ... (default - True)",
                                                None,None,None,None,None,None]

mapquest_reverse_jsList                    =   [None,None,None,None,None,
                                                "process_reverse_callback(0," + str(sugm.OpenMapQuestId) + ")",
                                                "process_reverse_callback(1," + str(sugm.OpenMapQuestId) + ")",
                                                "process_reverse_callback(2," + str(sugm.OpenMapQuestId) + ")",
                                                "process_reverse_callback(3," + str(sugm.OpenMapQuestId) + ")",
                                                "process_reverse_callback(4," + str(sugm.OpenMapQuestId) + ")",
                                                "display_help_url('" + str(dfchelp.OpenMapQuestReverseHelp) + "')"]


mapquest_reverse_reqList                   =   [0]

mapquest_reverse_form                      =   [mapquest_reverse_id,
                                                mapquest_reverse_idList,
                                                mapquest_reverse_labelList,
                                                mapquest_reverse_typeList,
                                                mapquest_reverse_placeholderList,
                                                mapquest_reverse_jsList,
                                                mapquest_reverse_reqList]

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

nomin_reverse_labelList                    =   ["latitude_longitude(s)",
                                                "number_of_results",
                                                "timeout",
                                                "language",
                                                "Get</br>Address",
                                                "Get</br>Coordinates",
                                                "Change</br> Geocoder",
                                                "Clear","Return","Help"]


nomin_reverse_typeList                     =   [maketextarea(6),"text","text","text",
                                                "button","button","button","button","button","button"]

nomin_reverse_placeholderList              =   ["list or tuple of (latitude, longitude)",
                                                "max number of results (default - 1) ",
                                                "enter timeout in seconds (default - 5)",
                                                "Preferred language in which to return results (default - English)",
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
                                              "result in km - True : km, False : miles (default - True) ",
                                              "select algorithm - 0 : Geodisc 1 : Vincenty 2 : Great_Circle (default - 0) ",
                                              "select elipsoid (default - 'WGS-84') ",
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

def get_form_id(geocid,gtype) :
     
    if(gtype == sugm.GEOCODERPARMS)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_geocoder_id)   
         elif(geocid == sugm.GoogleId)          : return(google_geocoder_id)
         elif(geocid == sugm.BingId)            : return(bing_geocoder_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_geocoder_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_geocoder_id)
    elif(gtype == sugm.QUERYPARMS)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_query_id)   
         elif(geocid == sugm.GoogleId)          : return(google_query_id)
         elif(geocid == sugm.BingId)            : return(bing_query_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_query_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_query_id)
    elif(gtype == sugm.REVERSEPARMS)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_reverse_id)   
         elif(geocid == sugm.GoogleId)          : return(google_reverse_id)
         elif(geocid == sugm.BingId)            : return(bing_reverse_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_reverse_id)
         
 
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
    elif(geocid == sugm.GoogleId)            : labelList  =   google_geocoder_labelList
    elif(geocid == sugm.OpenMapQuestId)      : labelList  =   mapquest_geocoder_labelList
    elif(geocid == sugm.NominatimId)         : labelList  =   nomin_geocoder_labelList
    
    #geocparms = get_geocoder_parms(geocid)
    geocparms = get_geocoder_form_parms_list(sugm.GEOCODERPARMS,geocid)
    
    row_added = 2
    
    georow = ["Geocoder"]
    geoRows.append(georow)
    geoHrefs.append([None])
            
    georow = ["&nbsp;&nbsp;" + sugm.get_geocoder_title(geocid)]
    geoRows.append(georow)
    geoHrefs.append([None])
    
    row_added = 2


    print("get_geocoder_parms_table",geocparms)
    
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
#--------------------------------------------------------------------------
#  Geocoding Validation methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 

"""
#--------------------------------------------------------------------------
#  arcgis geocoding valiudation method
#--------------------------------------------------------------------------
"""  
def validate_arcgis_geocoder_parms(gparms,opstat) :
    
    fparms  =   get_parms_for_input(gparms,arcgis_geocoder_idList)
    
    if(len(fparms) > 0) :
        # if autheticated user,pw and agent must be defined
        # else all need to be blank
        if( (len(fparms[0]) > 0) or (len(fparms[1]) > 0) or (len(fparms[2]) > 0) ) :
            if(len(fparms[2]) == 0) :
                fparms[2] = "my-application"
            
            if( (len(fparms[0]) == 0) or (len(fparms[1]) == 0) ) :
                opstat.set_status(False)
                opstat.set_error_msg("Missing authentication parameter")
            
            cfg.set_config_value(arcgis_geocoder_id + "Parms",fparms)
            
    else :
        cfg.drop_config_value(arcgis_geocoder_id + "Parms")    

"""
#--------------------------------------------------------------------------
#  google geocoding valiudation method
#--------------------------------------------------------------------------
"""    
def validate_google_geocoder_parms(gparms,opstat) :
    
    fparms  =   get_parms_for_input(gparms,google_geocoder_idList)
    
    if(len(fparms) > 0) :
        if(len(fparms[0]) > 0) :
            if( (len(fparms[1]) > 0) or (len(fparms[2]) > 0) ) :
                opstat.set_status(False)
                opstat.set_errormsg("API Key defined and client_id or secret_key defined")
                
        else :
            if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :
                opstat.set_status(False)
                opstat.set_errormsg("if no API Key then both client_id and secret_key must be defined for premier")
            
    else :
        opstat.set_status(False)
        opstat.set_errormsg("No API Key or client_id and secret_key defined")
        cfg.drop_config_value(arcgis_geocoder_id + "Parms")    

"""
#--------------------------------------------------------------------------
#  nominatim geocoding valiudation method
#--------------------------------------------------------------------------
"""
def validate_nominatim_geocoder_parms(gparms,opstat) :
    
    fparms  =   get_parms_for_input(gparms,google_geocoder_idList)
    
    if(len(fparms[0]) == 0) :
        fparms[0] = "my-application"
        cfg.set_config_value(nomin_geocoder_id + "Parms",fparms)
        
    if(len(fparms) > 0) :
        if(len(fparms[0]) > 0) :
            if( (len(fparms[1]) > 0) or (len(fparms[2]) > 0) ) :
                opstat.set_status(False)
                opstat.set_errormsg("API Key defined and client_id or secret_key defined")
                
        else :
            if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :
                opstat.set_status(False)
                opstat.set_errormsg("if no API Key then both client_id and secret_key must be defined for premier")
            
    else :
        opstat.set_status(False)
        opstat.set_errormsg("No API Key or client_id and secret_key defined")
        cfg.drop_config_value(arcgis_geocoder_id + "Parms")    

"""
#--------------------------------------------------------------------------
#  generic geocoding valiudation method
#--------------------------------------------------------------------------
""" 
def validate_cmd_parms(ptype,geocid,gqparms,opstat) :
    
    if(ptype == sugm.GEOCODERPARMS) :
    
        if(geocid == sugm.ArcGISId) :
            return(validate_arcgis_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.GoogleId) :
            return(validate_google_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.NominatimId) :
            return(validate_nominatim_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_geocoder_idList 
            reqList         =   bing_geocoder_reqList 

        elif(geocid == sugm.OpenMapQuestId) :
            idList          =   mapquest_geocoder_idList 
            reqList         =   mapquest_geocoder_reqList 
        
    elif(ptype == sugm.QUERYPARMS) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_query_idList 
            reqList         =   google_query_reqList 
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_query_idList 
            reqList         =   bing_query_reqList 

        elif(geocid == sugm.OpenMapQuestId) :
            idList          =   mapquest_query_idList 
            reqList         =   mapquest_query_reqList 
        
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_query_idList 
            reqList         =   nomin_query_reqList 
        
        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_query_idList 
            reqList         =   arcgis_query_reqList 
            
    elif(ptype == sugm.REVERSEPARMS) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_reverse_idList 
            reqList         =   google_reverse_reqList 
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_reverse_idList 
            reqList         =   bing_reverse_reqList 

        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_reverse_idList 
            reqList         =   arcgis_reverse_reqList 
        
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_reverse_idList 
            reqList         =   nomin_reverse_reqList 
            
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("Reverse not supportd")
        
    if(not opstat.get_status()) :
        return(opstat)
        
    fparms = get_parms_for_input(gqparms,idList)
    #print("validate_cmd_parms",fparms)
    missingParm     =   False
        
    if(ptype == sugm.GEOCODERPARMS)      : cfg_key = get_form_id(geocid,sugm.GEOCODERPARMS) + "Parms"
    elif(ptype == sugm.QUERYPARMS)       : cfg_key = get_form_id(geocid,sugm.QUERYPARMS) + "Parms"
    elif(ptype == sugm.REVERSEPARMS)     : cfg_key = get_form_id(geocid,sugm.REVERSEPARMS) + "Parms"
    
    if(len(fparms) > 0) :
    
        for i in range(len(reqList)) :
            if(not missingParm) :
                if(len(fparms[i]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Required parm not defined")
                    missingParm = True

    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No query parms defined")
        
        cfg.drop_config_value(cfg_key)
        
    if(opstat.get_status()) :
        
        if(len(fparms) > 0) :
            cfg.set_config_value(cfg_key,fparms)
        else :
            cfg.drop_config_value(cfg_key)
                
    else :    
        cfg.drop_config_value(cfg_key)
        

"""
#--------------------------------------------------------------------------
#  get geocoder kwargs for init
#--------------------------------------------------------------------------
"""
def get_geocoder_form_parms_list(ptype,geocid) :
    
    #print("get_geocoder_form_parms_list",ptype,geocid)
    
    if(ptype == sugm.GEOCODERPARMS)      : plist = cfg.get_config_value(get_form_id(geocid,sugm.GEOCODERPARMS) + "Parms")    
    elif(ptype == sugm.QUERYPARMS)       : plist = cfg.get_config_value(get_form_id(geocid,sugm.QUERYPARMS) + "Parms")    
    elif(ptype == sugm.REVERSEPARMS)     : plist = cfg.get_config_value(get_form_id(geocid,sugm.REVERSEPARMS) + "Parms") 

    #print("get_geocoder_form_parms_list\n",plist)

    return(plist)
        
  
"""
#--------------------------------------------------------------------------
#  get command kwargs stored in config
#--------------------------------------------------------------------------
"""
def get_geocoder_cmd_kwargs(ptype,geocid) :
    #print("get_geocoder_cmd_kwargs",ptype,geocid)
        
    if(ptype == sugm.GEOCODERPARMS)     : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.GEOCODERPARMS) + "Parms")
    elif(ptype == sugm.QUERYPARMS)      : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.QUERYPARMS) + "Parms")
    elif(ptype == sugm.REVERSEPARMS)    : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.REVERSEPARMS) + "Parms")
    
    if(ptype == sugm.GEOCODERPARMS) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_geocoder_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_geocoder_labelList 
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_geocoder_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_geocoder_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_geocoder_labelList 
    elif(ptype == sugm.QUERYPARMS) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_query_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_query_labelList 
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_query_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_query_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_query_labelList 
    elif(ptype == sugm.REVERSEPARMS) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_reverse_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_reverse_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_reverse_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_reverse_labelList 
 
    #print("get_geocoder_cmd_kwargs\n",geoparms,"\n",labelList)

    geokwargs = {}

    if(geoparms != None) :
        for i in range(len(geoparms)) : 
            if(len(geoparms[i]) > 0) :
                geokwargs.update({labelList[i]:geoparms[i]})

    #print("get_geocoder_cmd_kwargs : geokwargs\n",geokwargs)
    if(len(geokwargs) == 0) :
        return(None)
    else :
        
        if(ptype == sugm.QUERYPARMS) :
            return(customize_query_kwargs(geocid,geokwargs)) 
        else :
            return(geokwargs)

"""
#--------------------------------------------------------------------------
#  override kwargs stored in config
#--------------------------------------------------------------------------
"""
def customize_query_kwargs(geocid,geokwargs) :

    cfg.drop_config_value(sugm.get_geocoder_title(geocid)+"max_geocode_results")
    if(not(geokwargs.get("number_of_results") == None)) :
        max_geocode_results     =   int(geokwargs.get("number_of_results"))
        geokwargs.pop("number_of_results")
        geokwargs.update({"exactly_one":False})
        cfg.set_config_value(sugm.get_geocoder_title(geocid)+"max_geocode_results",max_geocode_results)

    if(geokwargs.get("timeout") == None) :
        geokwargs.update({"timeout":20})
        
    return(geokwargs)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  quer and reverse display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#  get datafrane column names table
#--------------------------------------------------------------------------
"""
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
#   display input forms for query and reverse
#------------------------------------------------------------------
"""
def display_geocode_inputs(formid,parms,ptype,showfull=False) :
    
    #print("display_geocode_inputs",formid,parms,ptype)

    if(parms == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
        inparms =   None
    else :
        geocid  =    parms[1]
        inparms =    parms[2]
    
    geo_parms_html = get_geocoder_parms_table(geocid)
        
    if(formid == sugm.ADDRESS_CONVERSION) :
        if(geocid == sugm.ArcGISId)              : form    =   arcgis_query_form
        elif(geocid == sugm.BingId)              : form    =   bing_query_form
        elif(geocid == sugm.GoogleId)            : form    =   google_query_form
        elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_query_form
        elif(geocid == sugm.NominatimId)         : form    =   nomin_query_form
    else :
        if(geocid == sugm.ArcGISId)              : form    =   arcgis_reverse_form
        elif(geocid == sugm.BingId)              : form    =   bing_reverse_form
        elif(geocid == sugm.GoogleId)            : form    =   google_reverse_form
        elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_reverse_form
        elif(geocid == sugm.NominatimId)         : form    =   nomin_reverse_form
    
    if(inparms != None) :
        parmslist = get_parms_for_input(inparms,form[1]) 
    else :
        parmslist = get_geocoder_form_parms_list(ptype,geocid)

    #print("display_geocode_inputs parmslist",parmslist)
    
    if(not(parmslist == None)) :
        cfg.set_config_value(form[0]+"Parms",parmslist)

    #print("parms",cfg.get_config_value(form[0]+"Parms"))

    
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
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Simple Geocoding Parameters</h4>"
    else :
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Simple Reverse Geocoding Parameters</h4>"
        
    display_grid("acconv_wrapper",
                 geofunc_heading_html,
                 geo_parms_html,
                 geofunc_input_html,
                 None)
    
    notes = [] 
    
    if(formid == sugm.ADDRESS_CONVERSION) :
        notes.append("To retrieve coords for a single address just enter address as single string.  Example : 1600 Pennsylvania Ave Washington, DC")
        notes.append("To retrieve coords for multiple addresses enter each address enclosed in [ ] separated by a comma.  Example : [addr],[addr1], ...[addrn]")
    else :
        notes.append("To retrieve an address for a single set of coords just enter coords as single list of coords. Example : [lat,long] ")
        notes.append("To retrieve multiple addresses enter each coords enclosed in [] separated by a comma.  Example : [lat,long],[lat1,long1], ...[latn,longn]")

    #display_notes(notes)
    from dfcleanser.common.common_utils import display_msgs
    display_msgs(notes,None)


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoder display methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

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
    
    listHtml = geocs_names_table.get_html()
    
    return(listHtml)

"""
#------------------------------------------------------------------
#   display geocoder inputs form
#------------------------------------------------------------------
"""     
def display_geocoders(geocodeid,showfull=False,showNotes=True) :

    print("display_geocoders",geocodeid,showfull,showNotes) 
    
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

    #parmsList = get_geocoder_parms(geocodeid)
    #parmsList = get_geocoder_form_parms_list(sugm.GEOCODERPARMS,geocodeid) 
    
    #if(parmsList != None) :
    #    cfg.set_config_value(geocoder_input_form[0]+"Parms",parmsList) 

    #print("display_geocoders parmsList",parmsList)    
    #print("cfg",cfg.get_config_value(geocoder_input_form[0]+"Parms"))    
    #print("display_geocoders",geocoder_input_form) 
    
    
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
    
    if(showNotes) :
        notes = [] 
    
        if(geocodeid == sugm.ArcGISId) :
            notes.append("For ArcGis simple geocoding authenticated mode enter values for username, password and referer.")
            notes.append("For ArcGis simple geocoding non-authenticated mode leave username, password and referer blank.")
            notes.append("For ArcGis bulk geocoding enter values for username and password.")
            notes.append("The rest of the parameters are used as default values for any subsequent simple geocoding calls of this connector.")
        elif(geocodeid == sugm.GoogleId) :
            notes.append("For Google enter values for client_id and secret_key or enter a value for the api_key.")
            notes.append("You must use a client_id and secret_key to do Google bulk geocoding.")
            notes.append("Entering just an api_key is for simple geocoding")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.BingId) :        
            notes.append("Bing geoocoding requires an api_key for all Bing geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.OpenMapQuestId) :
            notes.append("OpenMapQuest geoocoding requires an api_key for all OpenMapQuest geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.NominatimId) :        
            notes.append("Nominatim geoocoding requires a user-agent for all Nominatim geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")

        from dfcleanser.common.common_utils import display_msgs
        display_msgs(notes,None)



















