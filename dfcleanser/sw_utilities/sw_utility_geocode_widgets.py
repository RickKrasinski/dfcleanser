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

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable)

from dfcleanser.common.common_utils import (get_parms_for_input, display_generic_grid, 
                                            display_exception, opStatus, get_select_defaults)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    geocoding main task bar
#--------------------------------------------------------------------------
"""
geocode_main_tb_doc_title               =   "Geocoding"
geocode_main_tb_title                   =   "Geocoding"
geocode_main_tb_id                      =   "geocodemaintb"

geocode_main_tb_keyTitleList            =   ["Select</br>Geocoder",
                                             "Interactive</br>Geocoding",
                                             "Bulk</br>Geocoding",
                                             "Geocode</br>Utilities",
                                             "Clear","Reset","Help"]

geocode_main_tb_jsList                  =   ["display_geocoders(-1," + str(sugm.INTERACTIVE) + ")",
                                             "display_geocoders(-1," + str(sugm.INTERACTIVE) + ")",
                                             "display_geocoders(-1," + str(sugm.BULK) + ")",
                                             "process_geoutils_callback(" + str(sugm.DISPLAY_GEOUTILS) + ")",
                                             "geocode_return()",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.GEOCODING_MAIN_TASKBAR_ID) + "')"]

geocode_main_tb_centered                =   False


"""
#--------------------------------------------------------------------------
#    geocoding utilities task bar
#--------------------------------------------------------------------------
"""
geocode_utilities_tb_doc_title          =   "Geocoding Utilities"
geocode_utilities_tb_title              =   "Geocoding Utilities"
geocode_utilities_tb_id                 =   "geocodeutilstb"

geocode_utilities_tb_keyTitleList       =   ["Calculate</br>Distance",
                                             "Calculate</br>df</br>Distance",
                                             "Calculate</br>Center",
                                             "Calculate</br>Distance</br>From</br>Center",
                                             "Return","Help"]

geocode_utilities_tb_jsList             =   ["process_geoutils_callback(" + str(sugm.DISPLAY_DISTANCE) + ")",
                                             "process_geoutils_callback(" + str(sugm.DISPLAY_DF_DISTANCE) + ")",
                                             "process_geoutils_callback(" + str(sugm.DISPLAY_CENTER) + ")",
                                             "process_geoutils_callback(" + str(sugm.DISPLAY_DIST_CENTER) + ")",
                                             "geocode_return()",
                                             "displayhelp('" + str(dfchelp.GEOCODING_MAIN_TASKBAR_ID) + "')"]

geocode_utilities_tb_centered           =   False


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
                                          None,None,None,None,None,None,None]

arcgis_geocoder_labelList           =   ["username",
                                         "password",
                                         "referer",
                                         "scheme",
                                         "timeout",
                                         "proxies",
                                         "Test</br>Geocoder</br>Connection",
                                         "Interactive</br>Geocoding",
                                         "Interactive</br>Reverse</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]

arcgis_geocoder_typeList            =   ["text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

arcgis_geocoder_placeholderList     =   ["ArcGIS username (default : None)",
                                         "ArcGIS password (default : None)",
                                         "ArcGIS referer (default : my-application)",
                                         "Desired scheme (default : https)",
                                         "Time, in seconds (default : 20)",
                                         "enter proxies dict (default : None)",
                                         None,None,None,None,None,None,None]

arcgis_geocoder_jsList              =   [None,None,None,None,None,None,
                                         "test_geocoder(" + str(sugm.ArcGISId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.ArcGISId) + ","  +  str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.ArcGISId) + ","  +  str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.GEOCODER) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.ArcGISInitHelp) + "')"]


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
                                          "ggsignature",
                                          "ggagent",
                                          "ggdomain",
                                          "ggscheme",
                                          "ggproxies",
                                          "ggformatstr",
                                          "ggsslcontext",
                                          "ggchannel",
                                          None,None,None,None,None,None,None]

google_geocoder_labelList           =   ["api_key",
                                         "client_id",
                                         "signature",
                                         "user_agent",
                                         "domain",
                                         "scheme",
                                         "proxies",
                                         "format_string",
                                         "ssl_context",
                                         "channel",
                                         "Test</br>Geocoder</br>Connection",
                                         "Interactive</br>Geocoding",
                                         "Interactive</br>Reverse</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


google_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

google_geocoder_placeholderList     =   ["enter account api key.",
                                         "enter account client id. (default - None) required for premier",
                                         "enter account signature (default - None) required for premier",
                                         "enter custom User-Agent header (default - None)",
                                         "localized Google Maps domain (default - ‘maps.googleapis.com’)",
                                         "enter scheme (default https)",
                                         "enter proxies dict (default - DEFAULT_SENTINEL)",
                                         "format string (default - '%s')",
                                         "ssl_context (default - DEFAULT_SENTINEL)",
                                         "enter channel identifier (default - None)",
                                         None,None,None,None,None,None,None]

google_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,
                                         "test_geocoder(" + str(sugm.GoogleId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.GoogleId) + ","  + str(sugm.QUERY) + ","  + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.GoogleId) + ","  + str(sugm.REVERSE) + ","  + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.GEOCODER) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.GoogleInitHelp) + "')"]

google_geocoder_reqList             =   [0,1]

google_geocoder_form                =   [google_geocoder_id,
                                         google_geocoder_idList,
                                         google_geocoder_labelList,
                                         google_geocoder_typeList,
                                         google_geocoder_placeholderList,
                                         google_geocoder_jsList,
                                         google_geocoder_reqList]

google_API_Key    =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"


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
                                          None,None,None,None,None,None,None]

bing_geocoder_labelList             =   ["api_key",
                                         "user_agent",
                                         "timeout",
                                         "format_string",
                                         "scheme",
                                         "proxies",
                                         "Test</br>Geocoder</br>Connection",
                                         "Interactive</br>Geocoding",
                                         "Interactive</br>Reverse</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


bing_geocoder_typeList              =   ["text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

bing_geocoder_placeholderList       =   ["enter Bing api key",
                                         "user agent (default - my-application)",
                                         "enter timeout in seconds (default 20)",
                                         "enter format string (default %s)",
                                         "enter scheme (default https)",
                                         "proxies dict (default None)",
                                         None,None,None,None,None,None,None]

bing_geocoder_jsList                =   [None,None,None,None,None,None,
                                         "test_geocoder(" + str(sugm.BingId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.BingId) + ","  + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.BingId) + ","  + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.GEOCODER) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.BingInitHelp) + "')"]

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
                                              "mapquestcountry",
                                              "mapquestdomain",
                                              None,None,None,None,None,None,None]

mapquest_geocoder_labelList             =   ["api_key",
                                             "user_agent",
                                             "timeout",
                                             "format_string",
                                             "scheme ",
                                             "proxies",
                                             "country_bias",
                                             "domain",
                                             "Test</br>Geocoder</br>Connection",
                                             "Interactive</br>Geocoding",
                                             "Interactive</br>Reverse</br>Geocoding",
                                             "Bulk</br>Geocoding",
                                             "Clear","Return","Help"]

mapquest_geocoder_typeList              =   ["text","text","text","text","text","text","text","text",
                                             "button","button","button","button","button","button","button"]

mapquest_geocoder_placeholderList       =   ["enter MapQuest API Key",
                                             "enter user agent (default 'my-application'",
                                             "enter timeout in seconds (default 20)",
                                             "enter format string (default '%s'",
                                             "enter scheme (default 'https')",
                                             "enter proxies dict (default None)",
                                             "country to bias results to (default None)",
                                             "Domain where the target service is hosted. (default open.mapquestapi.com')",
                                             None,None,None,None,None,None,None]

mapquest_geocoder_jsList                =   [None,None,None,None,None,None,None,None,
                                             "test_geocoder(" + str(sugm.OpenMapQuestId) + "," + str(sugm.INTERACTIVE) + ")",
                                             "display_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                             "display_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                             "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.BULK) + ")",
                                             "clear_geocode_form(" + str(sugm.OpenMapQuestId) + "," + str(sugm.GEOCODER) + "," + str(sugm.INTERACTIVE) + ")",
                                             "geocode_return()",
                                             "displayhelp('" + str(dfchelp.OpenMapQuestInitHelp) + "')"]


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
                                          "nominbias",
                                          "nominproxies",
                                          "nomindomain",
                                          "nominscheme",
                                           None,None,None,None,None,None,None]

nomin_geocoder_labelList            =   ["user_agent",
                                         "timeout",
                                         "format_string",
                                         "country_bias",
                                         "proxies",
                                         "domain",
                                         "scheme",
                                         "Test</br>Geocoder</br>Connection",
                                         "Interactive</br>Geocoding",
                                         "Interactive</br>Reverse</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


nomin_geocoder_typeList             =   ["text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

nomin_geocoder_placeholderList      =   ["enter custom User-Agent (required)",
                                         "enter timeout in secs (default 20)",
                                         "enter format string (default %s)",
                                         "enter country to bias results (default - None)",
                                         "enter proxies dict)",
                                         "enter domain (default nominatim.openstreetmap.org)",
                                         "enter scheme (default https)",
                                         None,None,None,None,None,None,None]

nomin_geocoder_jsList               =   [None,None,None,None,None,None,None,
                                         "test_geocoder(" + str(sugm.NominatimId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.NominatimId) + "," + str(sugm.GEOCODER) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.NominatimInitHelp) + "')"]


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
#   Baidu geocoder parms
#--------------------------------------------------------------------------
"""
baidu_geocoder_title                =   "Baidu Geocoder Connector"
baidu_geocoder_id                   =   "baidugeocoder"

baidu_geocoder_idList               =    ["baiduapikey",
                                          "baiduscheme",
                                          "baidutimeout",
                                          "baiduproxies",
                                          "baiduagent",
                                          "baidufstring",
                                          "baidssl",
                                          "baiduseckey",
                                          None,None,None,None,None,None,None]

baidu_geocoder_labelList            =   ["api_key",
                                         "scheme",
                                         "timeout",
                                         "proxies",
                                         "user_agent",
                                         "format_string",
                                         "ssl_context",
                                         "security_key", 
                                         "Test</br>Geocoder</br>Connection",
                                         "Interactive</br>Geocoding",
                                         "Interactive</br>Reverse</br>Geocoding",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


baidu_geocoder_typeList             =   ["text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

baidu_geocoder_placeholderList      =   ["enter Baidu api key",
                                         "enter scheme (default https)",
                                         "enter timeout in seconds (default 1)",
                                         "proxies dict (default None)",
                                         "user agent (default - 'geopy/x.xx.x')",
                                         "enter format string (default %s)",
                                         "enter ssl context (default None)",
                                         "enter authentication security key (default None)",
                                         None,None,None,None,None,None,None]

baidu_geocoder_jsList               =   [None,None,None,None,None,None,None,None,
                                         "test_geocoder(" + str(sugm.BaiduId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.BingInitHelp) + "')"]

baidu_geocoder_reqList              =   [0]


baidu_APP_Name      =   "MyTestGeocoder"
baidu_ID            =   "15870017"
baidu_API_Key       =   "GISxFUnzA8jFfzYF7pVcKWig"
baidu_Secret_Key    =   "d3UWh3WGWTxvmm897KQoczVfHmZzyMOR"

baidu_second_key    =   "NaKYPfQCGqrGdX8pR77rdWLuGyiGCu4E"
baidu_second_SK     =   "1KMkueNu8jycuv45fShY6FgZK8BdAty0"

baidu_third_key     =   "vt0XM0d6t28kDS9Rm9Bf7nNF9kE5lOfh"
baidu_third_SK      =   "ltseOWxtoa2Mz3odxSUTovgGPSGLU3EZ"


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
                                         "Change</br>Geocoder",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


arcgis_query_typeList               =   [maketextarea(6),"text","text",
                                         "button","button","button","button","button","button"]

arcgis_query_placeholderList        =   ["single address string or [] list of address strings",
                                         "max number of results per address (default - 1) ",
                                         "enter timeout in seconds (default - 10 seconds)",
                                         None,None,None,None,None,None]

arcgis_query_jsList                 =   [None,None,None,
                                         "process_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.ArcGISQueryHelp) + "')"]


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
                                         "Change</br>Geocoder",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


google_query_typeList               =   [maketextarea(6),"text","text",maketextarea(2),"select",maketextarea(3),"select","select",
                                         "button","button","button","button","button","button"]

google_query_placeholderList        =   ["single address string or [] list of address strings",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter bounding box of the viewport (default - None)",
                                         "enter the ccTLD region code (default - None)",
                                         "enter components dict) (default - None)",
                                         "enter the language (default - None)",
                                         "enter sensor flag (default - False)",
                                         None,None,None,None,None,None]

google_query_jsList                 =   [None,None,None,None,None,None,None,None,
                                         "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

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
                                         "culture",
                                         "include_neighborhood",
                                         "include_country_code",
                                         "Get</br>Coords",
                                         "Change</br> Geocoder",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


bing_query_typeList                 =   [maketextarea(6),"text","text","text","select","select","select",
                                         "button","button","button","button","button","button"]

bing_query_placeholderList          =   ["single quote enclosed address string or [] list of quote enclosed address strings",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter coords to prioritize to (default - None)",
                                         "enter two-letter country code (default - None) ",
                                         "return neighborhood field (default - False)",
                                         "return 2 digit country code (default - False)",
                                         None,None,None,None,None,None]

bing_query_jsList                   =   [None,None,None,None,None,None,None,
                                         "process_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.BingQueryHelp) + "')"]


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
                                             "Change</br> Geocoder",
                                             "Bulk</br>Geocoding",
                                             "Clear","Return","Help"]


mapquest_query_typeList                  =   [maketextarea(6),"text","text",
                                              "button","button","button","button","button","button"]

mapquest_query_placeholderList           =   ["single address string or [] list of address strings",
                                              "max number of results displayed per address (default - 1 : max 5) ",
                                              "enter timeout in seconds (default - 20)",
                                              None,None,None,None,None,None]

mapquest_query_jsList                    =    [None,None,None,
                                               "process_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                               "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.INTERACTIVE) + ")",
                                               "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.OpenMapQuestQueryHelp) + "')"]


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
                                             "Change</br> Geocoder",
                                             "Bulk</br>Geocoding",
                                             "Clear","Return","Help"]


nomin_query_typeList                     =   [maketextarea(6),"text","text","select","text","text",
                                              "button","button","button","button","button","button"]

nomin_query_placeholderList              =   ["single address string or [] list of address strings",
                                              "max number of results displayed per address (default - 1 : max 5) ",
                                              "enter timeout in seconds (default - 20)",
                                              "Location.raw to include address details  (default - False)",
                                              "language in which to return results  (default - English)",
                                              "return the result’s geometry in wkt, svg, kml, or geojson formats (default - None)",
                                              None,None,None,None,None,None]

nomin_query_jsList                       =    [None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                               "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.INTERACTIVE) + ")",
                                               "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.NominatimQueryHelp) + "')"]


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
#   baidu get coords form
#--------------------------------------------------------------------------
"""
baidu_query_title                   =   "Baidu Geocoder Get Coordinates"
baidu_query_id                      =   "baiduquery"

baidu_query_idList                  =    ["baiduqquery",
                                          "baiduqcount",
                                          "baiduqtimeout",
                                          None,None,None,None,None,None]

baidu_query_labelList               =   ["address(s)",
                                         "number_of_results",
                                         "timeout",
                                         "Get</br>Coords",
                                         "Change</br> Geocoder",
                                         "Bulk</br>Geocoding",
                                         "Clear","Return","Help"]


baidu_query_typeList                =   [maketextarea(6),"text","text",
                                         "button","button","button","button","button","button"]

baidu_query_placeholderList         =   ["single address string or [] list of address strings",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         None,None,None,None,None,None]

baidu_query_jsList                  =   [None,None,None,
                                         "process_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.INTERACTIVE) + ")",
                                         "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.INTERACTIVE) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + str(dfchelp.BingQueryHelp) + "')"]


baidu_query_reqList                 =   [0]

baidu_query_form                    =   [baidu_query_id,
                                         baidu_query_idList,
                                         baidu_query_labelList,
                                         baidu_query_typeList,
                                         baidu_query_placeholderList,
                                         baidu_query_jsList,
                                         baidu_query_reqList]

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
                                            "Change</br> Geocoder",
                                            "Bulk</br>Geocoding",
                                            "Clear","Return","Help"]


google_reverse_typeList                =   [maketextarea(6),"text","text","select","select",
                                            "button","button","button","button","button","button"]

google_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "enter the language (default - English)",
                                            "enter sensor flag (default - False)",
                                            None,None,None,None,None,None]

google_reverse_jsList                  =   [None,None,None,None,None,
                                            "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.BULK) + ")",
                                            "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "geocode_return()",
                                            "displayhelp('" + str(dfchelp.GoogleReverseHelp) + "')"]


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
                                            "Change</br> Geocoder",
                                            "Bulk</br>Geocoding",
                                            "Clear","Return","Help"]


arcgis_reverse_typeList                =   [maketextarea(6),"text","text","text","text",
                                            "button","button","button","button","button","button"]

arcgis_reverse_placeholderList         =   ["list or tuple of (latitude, longitude)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "Distance from the query location (default - None)",
                                            "WKID to use for both input and output coordinates (default - 4236)",
                                            None,None,None,None,None,None]

arcgis_reverse_jsList                  =   [None,None,None,None,None,
                                            "process_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.BULK) + ")",
                                            "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "geocode_return()",
                                            "displayhelp('" + str(dfchelp.ArcGISReverseHelp) + "')"]


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
                                            "Change</br> Geocoder",
                                            "Bulk</br>Geocoding",
                                            "Clear","Return","Help"]


bing_reverse_typeList                  =   [maketextarea(6),"text","text","select","select",
                                            "button","button","button","button","button","button"]

bing_reverse_placeholderList           =   ["list or tuple of (latitude, longitude)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "two-letter country code (default - None)",
                                            "whether to include the two-letter ISO code of the country (default - False)",
                                            None,None,None,None,None,None]

bing_reverse_jsList                    =   [None,None,None,None,None,
                                            "process_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.BULK) + ")",
                                            "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "geocode_return()",
                                            "displayhelp('" + str(dfchelp.BingReverseHelp) + "')"]


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
mapquest_reverse_id                        =   "mapquestreverse"

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
                                                "Change</br>Geocoder",
                                                "Bulk</br>Geocoding",
                                                "Clear","Return","Help"]


mapquest_reverse_typeList                  =   [maketextarea(6),"text","text","text","select",
                                                "button","button","button","button","button","button"]

mapquest_reverse_placeholderList           =   ["list or tuple of (latitude, longitude)",
                                                "max number of results displayed per address (default - 1 : max 5) ",
                                                "enter timeout in seconds (default - 20)",
                                                "Preferred language in which to return results (default - English)",
                                                "include address details such as city, county ... (default - True)",
                                                None,None,None,None,None,None]

mapquest_reverse_jsList                    =   [None,None,None,None,None,
                                                "process_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                                "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.INTERACTIVE) + ")",
                                                "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.BULK) + ")",
                                                "clear_geocode_form(" + str(sugm.OpenMapQuestId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                                "geocode_return()",
                                                "displayhelp('" + str(dfchelp.OpenMapQuestReverseHelp) + "')"]


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
                                                "Change</br> Geocoder",
                                                "Bulk</br>Geocoding",
                                                "Clear","Return","Help"]


nomin_reverse_typeList                     =   [maketextarea(6),"text","text","text",
                                                "button","button","button","button","button","button"]

nomin_reverse_placeholderList              =   ["list or tuple of (latitude, longitude)",
                                                "max number of results displayed per address (default - 1 : max 5) ",
                                                "enter timeout in seconds (default - 20)",
                                                "Preferred language in which to return results (default - English)",
                                                None,None,None,None,None,None]

nomin_reverse_jsList                       =   [None,None,None,None,
                                                "process_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                                "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.INTERACTIVE) + ")",
                                                "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.BULK) + ")",
                                                "clear_geocode_form(" + str(sugm.NominatimId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                                "geocode_return()",
                                                "displayhelp('" + str(dfchelp.NominatimReverseHelp) + "')"]


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
#   Baidu get address forms
#--------------------------------------------------------------------------
"""
baidu_reverse_title                    =   "Baidu Geocoder Get Address"
baidu_reverse_id                       =   "baidureverse"

baidu_reverse_idList                   =    ["baidurquery",
                                             "baidurcount",
                                             "baidurtimeout",
                                             None,None,None,None,None,None]

baidu_reverse_labelList                =   ["latitude_longitude(s)",
                                            "number_of_results",
                                            "timeout",
                                            "Get</br>Address",
                                            "Change</br> Geocoder",
                                            "Bulk</br>Geocoding",
                                            "Clear","Return","Help"]


baidu_reverse_typeList                 =   [maketextarea(6),"text","text",
                                            "button","button","button","button","button"]

baidu_reverse_placeholderList          =   ["list or tuple of (latitude, longitude)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            None,None,None,None,None,None]

baidu_reverse_jsList                   =   [None,None,None,
                                            "process_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.INTERACTIVE) + ")",
                                            "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.BULK) + ")",
                                            "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.INTERACTIVE) + ")",
                                            "geocode_return()",
                                            "displayhelp('" + str(dfchelp.BingReverseHelp) + "')"]


baidu_reverse_reqList                  =   [0]

baidu_reverse_form                     =   [baidu_reverse_id,
                                            baidu_reverse_idList,
                                            baidu_reverse_labelList,
                                            baidu_reverse_typeList,
                                            baidu_reverse_placeholderList,
                                            baidu_reverse_jsList,
                                            baidu_reverse_reqList]





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    geocoding utilities input form
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    address distance input form
#--------------------------------------------------------------------------
"""
addr_dist_utility_input_title             =   "Address Distance Columns"
addr_dist_utility_input_id                =   "addrdist"
addr_dist_utility_input_idList            =   ["fromaddr",
                                               "toaddr",
                                               "disunits",
                                               "distalg",
                                               "elipsoid",
                                               None,None,None,None,None,None]

addr_dist_utility_input_labelList         =   ["from_address(s) ",
                                               "to_address(s)",
                                               "distance_units",
                                               "distance_algorithm",
                                               "elipsoid",
                                               "Calculate</br>Address</br>Distance",
                                               "Display</br>Coord</br>Distance",
                                               "Display</br>Dataframe</br>Distance",
                                               "Clear","Return","Help"]

addr_dist_utility_input_labelList1        =   ["from_lat_lng_coords(s) ",
                                               "to_lat_lng_coords(s)",
                                               "distance_units",
                                               "distance_algorithm",
                                               "elipsoid",
                                               "Calculate</br>Address</br>Distance",
                                               "Display</br>Coord</br>Distance",
                                               "Display</br>Dataframe</br>Distance",
                                               "Clear","Return","Help"]

addr_dist_utility_input_typeList          =   [maketextarea(6),maketextarea(6),"select","select","select",
                                               "button","button","button","button","button","button"]

addr_dist_utility_input_placeholderList   =  ["To calculate distance between single addresses just enter address as single string in quotes - 'address 1'\n" + 
                                              "To calculate distance for multiple addresses enter a list of addresses in single quotes - ['address 1' , 'address 2']",
                                              "use same format as from address(s) \n" +
                                              "number and format of to addresses must match number and format of from addresses",
                                              "result in km - True : km, False : miles (default - True) ",
                                              "geocode algorithm (default - geodesic) ",
                                              "select elipsoid (default - 'WGS-84') ",
                                              None,None,None,None,None,None]

addr_dist_utility_input_placeholderList1  =  ["To calculate distance between single coords just enter coords as [lat,lng] single list \n" + 
                                              "To calculate distance for multiple coords enter a list of coord pairs as list of pairs - [[lat,lng] , [lat1,lng1]]",
                                              "use same format as from coords(s) \n" +
                                              "number and format of to coords must match number and format of from coords",
                                              "result in km - True : km, False : miles (default - True) ",
                                              "geocode algorithm (default - geodesic) ",
                                              "select elipsoid (default - 'WGS-84') ",
                                              None,None,None,None,None,None]

addr_dist_utility_input_jsList            =    [None,None,None,None,None,
                                                "process_geoutils_callback("+str(sugm.PROCESS_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.DISPLAY_COORD_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.DISPLAY_DF_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.DISPLAY_DISTANCE)+")",
                                                "geocode_return()",
                                                "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

addr_dist_utility_input_jsList1           =    [None,None,None,None,None,
                                                "process_geoutils_callback("+str(sugm.DISPLAY_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.PROCESS_COORD_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.DISPLAY_DF_DISTANCE)+")",
                                                "process_geoutils_callback("+str(sugm.DISPLAY_DISTANCE)+")",
                                                "geocode_return()",
                                                "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

addr_dist_utility_input_reqList           =   [0,1]

"""
#--------------------------------------------------------------------------
#    address dataframer distance input form
#--------------------------------------------------------------------------
"""
addr_df_dist_utility_input_title             =   "Address Distance Columns"
addr_df_dist_utility_input_id                =   "addrdfdist"
addr_df_dist_utility_input_idList            =   ["addrdffromdistdf",
                                                  "fromlatlngcolumns",
                                                  "fromcolnames",
                                                  "addrdftodistdf",
                                                  "tolatlngcolumns",
                                                  "tocolnames",
                                                  "tocoords",
                                                  "newcol",
                                                  "dfdisunits",
                                                  "dfdistalg",
                                                  "dfelipsoid",
                                                  None,None,None,None,None]

addr_df_dist_utility_input_labelList         =   ["from_dataframe",
                                                  "from_dataframe_lat_lng_columns",
                                                  "from_dataframe_column_name(s)",
                                                  "to_coord_source",
                                                  "to_dataframe_lat_lng_columns",
                                                  "to_dataframe_column_name(s)",
                                                  "to_coord(s)_list",
                                                  "new_distance_column_name(s)_list",
                                                  "distance_units",
                                                  "distance_algorithm",
                                                  "elipsoid",
                                                  "Calculate</br>Dataframe</br>Distance",
                                                  "Display</br>Distance",
                                                  "Clear","Return","Help"]

addr_df_dist_utility_input_labelList1         =   ["from_dataframe",
                                                  "from_dataframe_lat_lng_columns",
                                                  "from_dataframe_column_name(s)",
                                                  "to_coord_source",
                                                  "to_dataframe_lat_lng_columns",
                                                  "to_dataframe_column_name(s)",
                                                  "to_address(s)_list",
                                                  "new_distance_column_name(s)_list",
                                                  "distance_units",
                                                  "distance_algorithm",
                                                  "elipsoid",
                                                  "Calculate</br>Dataframe</br>Distance",
                                                  "Dispay</br>Distance",
                                                  "Clear","Return","Help"]

addr_df_dist_utility_input_typeList          =   ["select","text","select",
                                                  "select","text","select",
                                                  "text","text",
                                                  "select","select","select",
                                                  "button","button","button","button","button"]

addr_df_dist_utility_input_typeList1         =   ["select","text","select",
                                                  "select","text","select",
                                                  maketextarea(3),maketextarea(3),
                                                  "select","select","select",
                                                  "button","button","button","button","button"]

addr_df_dist_utility_input_placeholderList   =  ["enter from dataframe",
                                                 "from df {lat,lng] column names - select from from_dataframe_column_name(s)",
                                                 "from dataframe column names",
                                                 "enter to dataframe",
                                                 "select to_column_names",
                                                 "to column names",
                                                 "enter to coord(s) list",
                                                 "enter column name(s) to store distance(s) in",
                                                 "result in km - True : km, False : miles (default = True) ",
                                                 "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                 "select elipsoid (default = 'WGS-84') ",
                                                 None,None,None,None,None]

addr_df_dist_utility_input_placeholderList1  =  ["enter from dataframe",
                                                 "from df {lat,lng] column names - select from from_dataframe_column_name(s)",
                                                 "from dataframe column names",
                                                 "enter to dataframe",
                                                 "select to_column_names",
                                                 "to column names",
                                                 "enter to address(s) as single quote enclosed values.\n  For multiple addresses define them as a list",
                                                 "enter column name(s) to store distance(s) in",
                                                 "result in km - True : km, False : miles (default = True) ",
                                                 "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                 "select elipsoid (default = 'WGS-84') ",
                                                 None,None,None,None,None]

addr_df_dist_utility_input_jsList            =    [None,None,None,None,None,None,None,None,None,None,None,
                                                   "process_geoutils_callback("+str(sugm.PROCESS_DF_DISTANCE)+")",
                                                   "process_geoutils_callback("+str(sugm.DISPLAY_DISTANCE)+")",
                                                   "process_geoutils_callback("+str(sugm.DISPLAY_DF_DISTANCE)+")",
                                                   "geocode_return()",
                                                   "displayhelp('" + str(dfchelp.GEOCODING_CALC_DF_DISTANCE_ID) + "')"]

addr_df_dist_utility_input_reqList           =   [0,1,2,3,4,5,6,7,8]

           
"""
#--------------------------------------------------------------------------
#    address center input form
#--------------------------------------------------------------------------
"""
addr_center_utility_input_title             =   "Address Center Columns"
addr_center_utility_input_id                =   "addrcenter"
addr_center_utility_input_idList            =   ["centerdf",
                                                 "centerdflatlng",
                                                 "centerdfcols",
                                                 "centercoords",
                                                 None,None,None,None]

addr_center_utility_input_labelList         =   ["dataframe",
                                                 "dataframe_lat_lng_columns",
                                                 "dataframe_column_name(s)",
                                                 "coord(s) list",
                                                 "Calculate</br>Center</br>Point",
                                                 "Clear","Return","Help"]

addr_center_utility_input_labelList1        =   ["dataframe",
                                                 "dataframe_lat_lng_columns",
                                                 "dataframe_column_name(s)",
                                                 "address(s) list",
                                                 "Calculate</br>Center</br>Point",
                                                 "Clear","Return","Help"]

addr_center_utility_input_typeList          =   ["select","text","select",maketextarea(6),
                                                 "button","button","button","button"]

addr_center_utility_input_placeholderList   =   ["select df to get coords from",
                                                 "df [lat,lng] columns names - select from dataframe_column_name(s)",
                                                 "select df column name",
                                                 "To calculate the center between coords just enter coords as a list of [lat,lng] coords.\n" + 
                                                 "  Example - [[lat1,lng1], [lat2,lng2]....]",
                                                 None,None,None,None]

addr_center_utility_input_placeholderList1  =   ["select df to get coords from",
                                                 "df [lat,lng] columns names - select from dataframe_column_name(s)",
                                                 "select df column name",
                                                 "To calculate the center between addresses just enter addresses as a list of single quote enclosed addresses.\n" + 
                                                 "  Example - ['address 1' , 'address 2'....]",
                                                 None,None,None,None]

addr_center_utility_input_jsList            =    [None,None,None,None,
                                                  "process_geoutils_callback("+str(sugm.PROCESS_CENTER)+")",
                                                  "process_geoutils_callback("+str(sugm.DISPLAY_CENTER)+")",
                                                  "geocode_return()",
                                                  "displayhelp('" + str(dfchelp.GEOCODING_CALC_CENTER_ID) + "')"]

addr_center_utility_input_reqList           =   [0,1,2,3]



"""
#--------------------------------------------------------------------------
#    address dataframe center distance input form
#--------------------------------------------------------------------------
"""
addr_df_center_dist_utility_input_title             =   "Address Distance Tp Center"
addr_df_center_dist_utility_input_id                =   "addrdfcenterdist"
addr_df_center_dist_utility_input_idList            =   ["addrdfcenterptdf",
                                                         "addrdfcenterptlatlngs",
                                                         "addrdfcenterptcols",
                                                         "centerpt",
                                                         "dfdisunits",
                                                         "dfdistalg",
                                                         "dfelipsoid",
                                                         "addrdfdistdf",
                                                         "addrdfdistlatlngs",
                                                         "addrdfdistcols",
                                                         "coordslist",
                                                         "distcollist",
                                                         
                                                         None,None,None,None]

addr_df_center_dist_utility_input_labelList         =   ["source_for_center_point",
                                                         "dataframe_for_center_point_lat_lng_columns",
                                                         "dataframe_for_center_point_column_name(s)",
                                                         "coords_for_center_point",
                                                         "distance_units",
                                                         "distance_algorithm",
                                                         "elipsoid",
                                                         "source_for_distance_from_coord(s)",
                                                         "dataframe_for_distance_from_lat_lng_columns",
                                                         "dataframe_for_distance_from_column_name(s)",
                                                         "distance_from_coord(s)_list",
                                                         "distance_from_center_point_column_name(s)",
                                                         "Calculate</br>Distance</br>From</br>Center",
                                                         "Clear","Return","Help"]

addr_df_center_dist_utility_input_labelList1        =   ["source_for_center_point",
                                                         "dataframe_for_center_point_lat_lng_columns",
                                                         "dataframe_for_center_point_column_name(s)",
                                                         "coords_for_center_point",
                                                         "distance_units",
                                                         "distance_algorithm",
                                                         "elipsoid",
                                                         "source_for_distance_from_coord(s)",
                                                         "dataframe_for_distance_from_lat_lng_columns",
                                                         "dataframe_for_distance_from_column_name(s)",
                                                         "distance_from_address(s)_list",
                                                         "distance_from_center_point_column_name(s)",
                                                         "Calculate</br>Distance</br>From</br>Center",
                                                         "Clear","Return","Help"]

addr_df_center_dist_utility_input_typeList          =   ["select","text","select",maketextarea(3),
                                                         "select","select","select",
                                                         "select","text","select",maketextarea(3),
                                                          maketextarea(3),
                                                          "button","button","button","button"]

addr_df_center_dist_utility_input_placeholderList   =   ["select centerpoint source",
                                                         "[Latitude,Longitude] column names for center point calc",
                                                         "select centerpoint dataframe column",
                                                         "enter coord(s) list to calculate center point from",
                                                         "result in km - True : km, False : miles (default = True) ",
                                                         "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                         "select elipsoid (default = 'WGS-84') ",
                                                         "select distance from coords source",
                                                         "[Latitude,Longitude] column names for distance from points",
                                                         "select distance from dataframe columns",
                                                         "enter coord(s) list to calc distance(s) from center point",
                                                         "enter column names to store distance(s) from center points",
                                                         None,None,None,None]

addr_df_center_dist_utility_input_placeholderList1  =   ["select centerpoint source",
                                                         "[Latitude,Longitude] column names for center point calc",
                                                         "select centerpoint dataframe column",
                                                         "enter coord(s) list to calculate center point from",
                                                         "result in km - True : km, False : miles (default = True) ",
                                                         "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                         "select elipsoid (default = 'WGS-84') ",
                                                         "select distance from coords source",
                                                         "[Latitude,Longitude] column names for distance from points",
                                                         "select distance from dataframe columns",
                                                         "enter address(s) list to calc distance(s) from center point",
                                                         "enter column names to store distance(s) from center points",
                                                         None,None,None,None]


addr_df_center_dist_utility_input_jsList            =    [None,None,None,None,None,None,None,None,None,None,None,None,
                                                          "process_geoutils_callback("+str(sugm.PROCESS_DIST_CENTER)+")",
                                                          "process_geoutils_callback("+str(sugm.DISPLAY_DIST_CENTER)+")",
                                                          "geocode_return()",
                                                          "displayhelp('" + str(dfchelp.GEOCODING_CALC_CENTER_DIST_ID) + "')"]

addr_df_center_dist_utility_input_reqList           =    [0,1,2,3,7,8,9,10,11]


"""
#--------------------------------------------------------------------------
#    address dataframe center input form
#--------------------------------------------------------------------------
"""
bulk_tune_utility_input_title                   =   "Bulk Geocoding Tuning"
bulk_tune_utility_input_id                      =   "bulktune"
bulk_tune_utility_input_idList                  =   ["tunegeocid",
                                                     "tunemaxthreads",
                                                     None,None,None,None]

bulk_tune_utility_input_labelList               =   ["geocoder_Id",
                                                     "max_threads",
                                                     "Set</br>Bulk</br>Parameters",
                                                     "Clear","Return","Help"]

bulk_tune_utility_input_typeList                =   ["select","text",
                                                     "button","button","button","button"]

bulk_tune_utility_input_placeholderList         =   ["select lat_lng column name",
                                                     "max concurrent geocode threads -- see Help",
                                                     None,None,None,None]

bulk_tune_utility_input_jsList                  =    [None,None,
                                                      "process_geoutils_callback("+str(sugm.PROCESS_TUNING)+")",
                                                      "process_geoutils_callback("+str(sugm.DISPLAY_TUNING)+")",
                                                      "geocode_return()",
                                                      "displayhelp('" + str(dfchelp.GEOCODING_UTILITIES_TASKBAR_ID) + "')"]

bulk_tune_utility_input_reqList                 =   [0,1]


SWUtility_geocode_inputs            =   [arcgis_geocoder_id, google_geocoder_id, bing_geocoder_id, mapquest_geocoder_id, nomin_geocoder_id,
                                         baidu_geocoder_id, arcgis_query_id, google_query_id, bing_query_id, mapquest_query_id, nomin_query_id,
                                         baidu_query_id, google_reverse_id, arcgis_reverse_id, bing_reverse_id, mapquest_reverse_id,
                                         nomin_reverse_id, baidu_reverse_id, addr_dist_utility_input_id, addr_df_dist_utility_input_id, addr_center_utility_input_id,
                                         bulk_tune_utility_input_id]


 
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar display and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_geocode_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(geocode_main_tb_id,
                                               geocode_main_tb_keyTitleList,
                                               geocode_main_tb_jsList,
                                               geocode_main_tb_centered),False)


def display_geocode_utils_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(geocode_utilities_tb_id,
                                               geocode_utilities_tb_keyTitleList,
                                               geocode_utilities_tb_jsList,
                                               geocode_utilities_tb_centered),False)
    
    
def display_calc_distance_input_form(ptype=sugm.GEOCODE_ADDRESS) :
    """
    * ---------------------------------------------------------
    * function : display the calculate distance form 
    * 
    * parms :
    *  pytype  - address or coords
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    
    if(ptype == sugm.GEOCODE_ADDRESS) :

        dist_addr_form  =   InputForm(addr_dist_utility_input_id,
                                      addr_dist_utility_input_idList,
                                      addr_dist_utility_input_labelList,
                                      addr_dist_utility_input_typeList,
                                      addr_dist_utility_input_placeholderList,
                                      addr_dist_utility_input_jsList,
                                      addr_dist_utility_input_reqList)   
        
    else :
        
        dist_addr_form  =   InputForm(addr_dist_utility_input_id,
                                      addr_dist_utility_input_idList,
                                      addr_dist_utility_input_labelList1,
                                      addr_dist_utility_input_typeList,
                                      addr_dist_utility_input_placeholderList1,
                                      addr_dist_utility_input_jsList1,
                                      addr_dist_utility_input_reqList)   
        
    
    selectDicts     =   []
            
    distsel         =   {"default":"km","list":["km","miles"]}
    selectDicts.append(distsel)
    geocsel         =   {"default":"geodesic","list":["geodesic","great_circle"]}
    selectDicts.append(geocsel)
    elipsel         =   {"default":"WGS-84","list":['WGS-84','GRS-80','Airy (1830)','Intl 1924','Clarke (1880)','GRS-67']}
    selectDicts.append(elipsel)

    get_select_defaults(dist_addr_form,
                        addr_dist_utility_input_id,
                        addr_dist_utility_input_idList,
                        addr_dist_utility_input_typeList,
                        selectDicts)

    dist_addr_form.set_gridwidth(720)
    dist_addr_form.set_custombwidth(100)
    
    dist_addr_form.set_fullparms(True)
    
    
   
    geocode_input_html = ""
    geocode_input_html = dist_addr_form.get_html() 
    
    geocode_heading_html =   "<div>Interactive Get Distance</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [geocode_heading_html,geocode_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)


def display_calc_df_distance_input_form() :
    """
    * ---------------------------------------------------------
    * function : display the calculate dataframe distance form 
    * 
    * parms :
    *  N/A
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    # clear out col names drop dows
    cparms  =   cfg.get_config_value(addr_df_dist_utility_input_id+"Parms")
    
    print("display_calc_df_distance_input_form",cparms)
    
    if(cparms is None) :
        
        dist_addr_form  =   InputForm(addr_df_dist_utility_input_id,
                                      addr_df_dist_utility_input_idList,
                                      addr_df_dist_utility_input_labelList,
                                      addr_df_dist_utility_input_typeList1,
                                      addr_df_dist_utility_input_placeholderList,
                                      addr_df_dist_utility_input_jsList,
                                      addr_df_dist_utility_input_reqList)  
    else :
        
        if(cparms[3] == "get to coords from to_coords(s)_list") :
            
            dist_addr_form  =   InputForm(addr_df_dist_utility_input_id,
                                          addr_df_dist_utility_input_idList,
                                          addr_df_dist_utility_input_labelList,
                                          addr_df_dist_utility_input_typeList1,
                                          addr_df_dist_utility_input_placeholderList,
                                          addr_df_dist_utility_input_jsList,
                                          addr_df_dist_utility_input_reqList)
            
        elif(cparms[3] == "get to address(s) from to_address(s)_list") :
            
            dist_addr_form  =   InputForm(addr_df_dist_utility_input_id,
                                          addr_df_dist_utility_input_idList,
                                          addr_df_dist_utility_input_labelList1,
                                          addr_df_dist_utility_input_typeList1,
                                          addr_df_dist_utility_input_placeholderList1,
                                          addr_df_dist_utility_input_jsList,
                                          addr_df_dist_utility_input_reqList)
            
            
        else :
            
             dist_addr_form  =   InputForm(addr_df_dist_utility_input_id,
                                          addr_df_dist_utility_input_idList,
                                          addr_df_dist_utility_input_labelList,
                                          addr_df_dist_utility_input_typeList,
                                          addr_df_dist_utility_input_placeholderList,
                                          addr_df_dist_utility_input_jsList,
                                          addr_df_dist_utility_input_reqList)
 
    selectDicts     =   []
    
    
    #dataframes      =   cfg.get_dfc_dataframes_select_list(cfg.SWGeocodeUtility_ID)
    dfs             =   cfg.get_dfc_dataframes_titles_list()
    
    if(not (cparms is None)) :
        
        geocode_df          =   cfg.get_dfc_dataframe_df(cparms[0])
        
        if(not(geocode_df is None)) :
            
            default_df  =   cparms[0]
        else :
            
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            geocode_df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
            cparms[0]   =   default_df
            cparms[1]   =   ""
            cparms[2]   =   ""
            
    else :
        
        cparms  =   ["","","","","","","","","km","geodesic","WGS-84"]

        default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
        geocode_df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
        cparms[0]   =   default_df
        cparms[1]   =   ""
        cparms[2]   =   ""
        
    dffrom_sel    =   {"default":default_df,"list":dfs, "callback" : "get_df_dist_to_cols"}
    selectDicts.append(dffrom_sel)
     
    geocode_df_cols     =   [" "]
    
    geocode_cols        =  list(geocode_df.columns)
    for i in range(len(geocode_cols)) :
        geocode_df_cols.append(geocode_cols[i])    
    
    print("geocode_df_cols : from ",geocode_df_cols)
    cols_list           =   {"default":" ","list":geocode_df_cols, "callback" : "select_from_df_dist_col"}
    selectDicts.append(cols_list)


    # do to df columns data

    
    if(not (cparms is None)) :
        to_df = cparms[3]
    else :
        to_df  =   "get to coords from to_coords(s)_list"
        
    dfs         =   cfg.get_dfc_dataframes_titles_list()
    df_list     =   ["get to coords from to_coords(s)_list","get to address(s) from to_address(s)_list"]
    for i in range(len(dfs)) :
        df_list.append(dfs[i])
        
    if(not( (to_df  ==   "get to coords from to_coords(s)_list") or 
            (to_df  ==   "get to address(s) from to_address(s)_list") ) ) :
        
        geocode_df    =   cfg.get_dfc_dataframe_df(to_df)
        
        if(geocode_df is None) :
            to_df  =   "get to coords from to_coords(s)_list"
            cparms[3]   =   to_df
            cparms[4]   =   ""
            cparms[5]   =   ""
            
    else :
        geocode_df    =   None 

    df_to_sel    =   {"default":default_df,"list":df_list, "callback" : "get_df_dist_to_cols"}
    selectDicts.append(df_to_sel)
    
    geocode_df_cols     =   [" "]
    
    if(not(geocode_df is None)) :
        
        geocode_cols        =  list(geocode_df.columns)
        for i in range(len(geocode_cols)) :
            geocode_df_cols.append(geocode_cols[i])
            
    else :
        
        if(not (cparms[3] == "get to address(s) from to_address(s)_list") ) :
            cparms[3]   =   "get to coords from to_coords(s)_list"
            
        cparms[4]   =   ""
        cparms[5]   =   ""

    cols_list           =   {"default":geocode_df_cols[0],"list":geocode_df_cols, "callback" : "select_to_df_dist_col"}
    selectDicts.append(cols_list)
            
    distsel         =   {"default":"km","list":["km","miles"]}
    selectDicts.append(distsel)
    geocsel         =   {"default":"geodesic","list":["geodesic","great_circle"]}
    selectDicts.append(geocsel)
    elipsel         =   {"default":"WGS-84","list":['WGS-84','GRS-80','Airy (1830)','Intl 1924','Clarke (1880)','GRS-67']}
    selectDicts.append(elipsel)
    
    print("cparms",cparms)
    
    if(cparms is None) :
        
        cfg.set_config_value(addr_df_dist_utility_input_id+"Parms",["","","","","","","","","km","geodesic","WGS-84"])
        cfg.set_config_value(addr_df_dist_utility_input_id+"ParmsProtect",[False,False,False,False,True,True,False,False,False,False,False]) 
    
    else :
        
        if( (cparms[3] == "get to coords from to_coords(s)_list") or 
            (cparms[3] == "get to address(s) from to_address(s)_list") ) :
            
            cparms[4]   =   " "
            cparms[5]   =   " "
            cfg.set_config_value(addr_df_dist_utility_input_id+"Parms",cparms)
            cfg.set_config_value(addr_df_dist_utility_input_id+"ParmsProtect",[False,False,False,False,True,True,False,False,False,False,False])
            
        else :
            
            cfg.set_config_value(addr_df_dist_utility_input_id+"Parms",cparms)
            cfg.set_config_value(addr_df_dist_utility_input_id+"ParmsProtect",[False,False,False,False,False,False,True,False,False,False,False])

    
    get_select_defaults(dist_addr_form,
                        addr_df_dist_utility_input_id,
                        addr_df_dist_utility_input_idList,
                        addr_df_dist_utility_input_typeList,
                        selectDicts)

    dist_addr_form.set_gridwidth(720)
    dist_addr_form.set_custombwidth(120)
    
    dist_addr_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = dist_addr_form.get_html()
    
    
    
    geocode_heading_html =   "<div>Get Distance(s) from dataframe</div>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [geocode_heading_html,geocode_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)




def display_calc_center_input_form() :
    """
    * ---------------------------------------------------------
    * function : display the calculate center form 
    * 
    * parms :
    *  N/A
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    DEBUG_DISPLAY_CALC_CENTER   =   False
    
    cparms  =   cfg.get_config_value(addr_center_utility_input_id+"Parms")
    
    if(DEBUG_DISPLAY_CALC_CENTER) :
        print("display_calc_df_distance_input_form",cparms)
    
    if(not(cparms is None)) :
        cparms[1]   =   " "
        cparms[2]   =   " "
        cfg.set_config_value(addr_center_utility_input_id+"Parms",cparms)
        
    else :
        cparms      =   ["","","",""]
        cparms[0]   =   "get coords from coord(s)_list"
        
    if(cparms[0] == "get coords from address(s)_list") :
        
        center_addr_form  =   InputForm(addr_center_utility_input_id,
                                        addr_center_utility_input_idList,
                                        addr_center_utility_input_labelList1,
                                        addr_center_utility_input_typeList,
                                        addr_center_utility_input_placeholderList1,
                                        addr_center_utility_input_jsList,
                                        addr_center_utility_input_reqList)
        
        
    else :
        
        center_addr_form  =   InputForm(addr_center_utility_input_id,
                                        addr_center_utility_input_idList,
                                        addr_center_utility_input_labelList,
                                        addr_center_utility_input_typeList,
                                        addr_center_utility_input_placeholderList,
                                        addr_center_utility_input_jsList,
                                        addr_center_utility_input_reqList)

    selectDicts     =   []
    
    dfs             =   ["get coords from coord(s)_list","get coords from address(s)_list"]
    
    if(DEBUG_DISPLAY_CALC_CENTER) :
        print("cfg.is_a_dfc_dataframe_loaded()",cfg.is_a_dfc_dataframe_loaded())
        
    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        dfslist         =   cfg.get_dfc_dataframes_titles_list()
        for i in range(len(dfslist)) :
            dfs.append(dfslist[i])
    
        if(not (cparms is None)) :
            
            if(cparms[0] == "get coords from coord(s)_list") :
        
                default_df  =   "get coords from coord(s)_list"
                geocode_df  =   None
                
            elif(cparms[0] == "get coords from address(s)_list") :
        
                default_df  =   "get coords from address(s)_list"
                geocode_df  =   None
        
            else :
        
                geocode_df          =   cfg.get_dfc_dataframe_df(cparms[0])
        
                if(not(geocode_df is None)) :
                    
                    default_df  =   cparms[0]
                    
                else :
                    
                    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
                    geocode_df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                
        else :
            
            default_df  =   "get coords from coord(s)_list"
            geocode_df  =   None
            
    else :
        
        if(cparms[0] == "get coords from coord(s)_list") :
        
            default_df  =   "get coords from coord(s)_list"
            geocode_df  =   None
                
        elif(cparms[0] == "get coords from address(s)_list") :
        
            default_df  =   "get coords from address(s)_list"
            geocode_df  =   None

       
    dffrom_sel    =   {"default":default_df,"list":dfs, "callback" : "get_df_center_cols"}
    selectDicts.append(dffrom_sel)
     
    geocode_df_cols     =   [" "]
    
    if(not(geocode_df is None)) :
        
        geocode_cols        =  list(geocode_df.columns)
        for i in range(len(geocode_cols)) :
            geocode_df_cols.append(geocode_cols[i])
            
    if(DEBUG_DISPLAY_CALC_CENTER) :
        print("geocode_df_cols : from ",geocode_df_cols)
        
    cols_list           =   {"default":" ","list":geocode_df_cols, "callback" : "select_df_center_col"}
    selectDicts.append(cols_list)
            
    if(cparms is None) :
        
        cfg.set_config_value(addr_center_utility_input_id+"Parms",[default_df,"","",""])
        cfg.set_config_value(addr_center_utility_input_id+"ParmsProtect",[False,True,True,False]) 
    
    else :
        cfg.set_config_value(addr_center_utility_input_id+"Parms",[default_df,"","",""])
        
        if( (default_df == "get coords from coord(s)_list") or 
            (default_df == "get coords from address(s)_list") ):
            
            cfg.set_config_value(addr_center_utility_input_id+"ParmsProtect",[False,True,True,False])
            
        else :
            
            cfg.set_config_value(addr_center_utility_input_id+"ParmsProtect",[False,False,False,True])
    
    get_select_defaults(center_addr_form,
                        addr_center_utility_input_id,
                        addr_center_utility_input_idList,
                        addr_center_utility_input_typeList,
                        selectDicts)
    
    center_addr_form.set_gridwidth(720)
    center_addr_form.set_custombwidth(120)
    center_addr_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = center_addr_form.get_html() 
    
    geocode_heading_html =   "<div>Get Center Point</div>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [geocode_heading_html,geocode_input_html]

    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)


    
def display_calc_df_center_dist_input_form(parms=None) :
    """
    * ---------------------------------------------------------
    * function : display the calculate distance from center form 
    * 
    * parms :
    *  N/A
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    DEBUG_DISPLAY_DF_CENTER_DIST    =   False
    
    if(parms is None) :
        fparms  =   None
    else :
        fparms  =   get_parms_for_input(parms,addr_df_center_dist_utility_input_idList)
    
    cparms  =   cfg.get_config_value(addr_df_center_dist_utility_input_id+"Parms")
    
    
    if(DEBUG_DISPLAY_DF_CENTER_DIST) :
        print("display_calc_df_center_dist_input_form : fparms\n",fparms)
    
    if(not (fparms is None)) :
        
        cparms  =   fparms    
        cfg.set_config_value(addr_center_utility_input_id+"Parms",cparms)
        
    if(DEBUG_DISPLAY_DF_CENTER_DIST) :    
        print("display_calc_df_center_dist_input_form : cparms\n",cparms) 
    
    if(cparms is None) :
        
        cparms  =   ["get center point from coords_for_center_point","","","","","","","get distance from coord(s) from distance_from_coord(s)_list","","","",""]
        
        center_addr_form  =   InputForm(addr_df_center_dist_utility_input_id,
                                        addr_df_center_dist_utility_input_idList,
                                        addr_df_center_dist_utility_input_labelList,
                                        addr_df_center_dist_utility_input_typeList,
                                        addr_df_center_dist_utility_input_placeholderList,
                                        addr_df_center_dist_utility_input_jsList,
                                        addr_df_center_dist_utility_input_reqList)  
        
    else :
        
        if(cparms[7] == "get distance from address(s) from distance_from_address(s)_list") :
        
            center_addr_form  =   InputForm(addr_df_center_dist_utility_input_id,
                                            addr_df_center_dist_utility_input_idList,
                                            addr_df_center_dist_utility_input_labelList1,
                                            addr_df_center_dist_utility_input_typeList,
                                            addr_df_center_dist_utility_input_placeholderList1,
                                            addr_df_center_dist_utility_input_jsList,
                                            addr_df_center_dist_utility_input_reqList)  
        
        else :
        
            center_addr_form  =   InputForm(addr_df_center_dist_utility_input_id,
                                            addr_df_center_dist_utility_input_idList,
                                            addr_df_center_dist_utility_input_labelList,
                                            addr_df_center_dist_utility_input_typeList,
                                            addr_df_center_dist_utility_input_placeholderList,
                                            addr_df_center_dist_utility_input_jsList,
                                            addr_df_center_dist_utility_input_reqList)  

    selectDicts     =   []
    
    dfs             =   ["get center point from coords_for_center_point"]
    
    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        dfslist         =   cfg.get_dfc_dataframes_titles_list()
        for i in range(len(dfslist)) :
            dfs.append(dfslist[i])
    
        if(not (cparms is None)) :
        
            if(not((cparms[0] == "get center point from coords_for_center_point") or (cparms[0] == ""))) :
        
                geocode_df          =   cfg.get_dfc_dataframe_df(cparms[0])
        
                if(not(geocode_df is None)) :
                    
                    default_df  =   cparms[0]
                    
                else :
                    
                    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
                    geocode_df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                
            else :
            
                default_df  =   "get center point from coords_for_center_point"
                geocode_df  =   None
            
        else :
            
            default_df  =   "get center point from coords_for_center_point"
            geocode_df  =   None
            
    else :
        
        default_df  =   "get center point from coords_for_center_point"
        geocode_df  =   None
       
    dffrom_sel    =   {"default":default_df,"list":dfs, "callback" : "get_df_center_dist_cols"}
    selectDicts.append(dffrom_sel)

    geocode_df_cols     =   [" "]
    
    if(not(geocode_df is None)) :
        
        geocode_cols        =  list(geocode_df.columns)
        for i in range(len(geocode_cols)) :
            geocode_df_cols.append(geocode_cols[i])
    
    #print("geocode_df_cols : from ",geocode_df_cols)
    cols_list           =   {"default":" ","list":geocode_df_cols, "callback" : "select_df_center_dist_col"}
    selectDicts.append(cols_list)
    
    cparms[0]   =   default_df
    
    if(DEBUG_DISPLAY_DF_CENTER_DIST) :
        print("cparms[0]",cparms[0])
        print("cparms[7]",cparms[7])
    
    distsel         =   {"default":"km","list":["km","miles"]}
    selectDicts.append(distsel)
    geocsel         =   {"default":"geodesic","list":["geodesic","great_circle"]}
    selectDicts.append(geocsel)
    elipsel         =   {"default":"WGS-84","list":['WGS-84','GRS-80','Airy (1830)','Intl 1924','Clarke (1880)','GRS-67']}
    selectDicts.append(elipsel)

    # set up from distance coords    
    dfs             =   ["get distance from coord(s) from distance_from_coord(s)_list",
                         "get distance from address(s) from distance_from_address(s)_list"]
    
    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        dfslist         =   cfg.get_dfc_dataframes_titles_list()
        for i in range(len(dfslist)) :
            dfs.append(dfslist[i])
    
        if(not (cparms is None)) :
            
            if(cparms[7] == "get distance from coord(s) from distance_from_coord(s)_list") :
                
                default_df  =   "get distance from coord(s) from distance_from_coord(s)_list"
                geocode_df  =   None 
                
            elif(cparms[7] == "get distance from address(s) from distance_from_address(s)_list") :
                
                default_df  =   "get distance from address(s) from distance_from_address(s)_list"
                geocode_df  =   None 
        
            else :
        
                geocode_df          =   cfg.get_dfc_dataframe_df(cparms[5])
        
                if(not(geocode_df is None)) :
                    
                    default_df  =   cparms[5]
                    
                else :
                    
                    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
                    geocode_df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                
            
        else :
            
            default_df  =   "get distance from coord(s) from distance_from_coord(s)_list"
            geocode_df  =   None
            
    else :
        
        if(cparms[7] == "get distance from address(s) from distance_from_address(s)_list") :
                
            default_df  =   "get distance from address(s) from distance_from_address(s)_list"
            geocode_df  =   None 
            
        else :
            
            default_df  =   "get distance from coord(s) from distance_from_coord(s)_list"
            geocode_df  =   None 
       
    dffrom_sel    =   {"default":default_df,"list":dfs, "callback" : "get_df_center_dist_coords_cols"}
    selectDicts.append(dffrom_sel)

    geocode_df_cols     =   [" "]
    
    if(not(geocode_df is None)) :
        
        geocode_cols        =  list(geocode_df.columns)
        for i in range(len(geocode_cols)) :
            geocode_df_cols.append(geocode_cols[i])
    
    #print("geocode_df_cols : from ",geocode_df_cols)
    cols_list           =   {"default":" ","list":geocode_df_cols, "callback" : "select_df_center_dist_coords_col"}
    selectDicts.append(cols_list)
    
    cparms[7]   =   default_df
    
    
    parmsprotect    =   [False,False,False,False,False,False,False,False,False,False,False,False]
    
    if(DEBUG_DISPLAY_DF_CENTER_DIST) :
        print("cparms[0]",cparms[0])
        print("cparms[7]",cparms[7])
    
    if(cparms[0] == "get center point from coords_for_center_point") :
        
        parmsprotect[0] = False
        parmsprotect[1] = True
        parmsprotect[2] = True
        parmsprotect[3] = False
        
        if( (cparms[7] == "get distance from coord(s) from distance_from_coord(s)_list") or 
            (cparms[7] == "get distance from address(s) from distance_from_address(s)_list") ) :
            
            parmsprotect[8] =   True 
            parmsprotect[9] =   True
            cparms[8]       =   ""
            cparms[9]       =   ""
            
        else :
            
            parmsprotect[10] =   True 
        
    else :
        
        parmsprotect[0]     =   False
        parmsprotect[1]     =   False
        parmsprotect[2]     =   False
        parmsprotect[3]     =   True
        
    if( (cparms[7] == "get distance from coord(s) from distance_from_coord(s)_list") or 
        (cparms[7] == "get distance from address(s) from distance_from_address(s)_list") ) :
        
        parmsprotect[8]     =   True
        parmsprotect[9]     =   True
        parmsprotect[10]    =   False
        
        parmsprotect[11]    =   True 
        cparms[8]           =   ""
        cparms[9]           =   "" 
        
    else :
        
        parmsprotect[8]     =   False
        parmsprotect[9]     =   False
        parmsprotect[10]    =   True
        cparms[10]          =   ""
        
        parmsprotect[11]    =   False
        
    get_select_defaults(center_addr_form,
                        addr_df_center_dist_utility_input_id,
                        addr_df_center_dist_utility_input_idList,
                        addr_df_center_dist_utility_input_typeList,
                        selectDicts)
    
    cfg.set_config_value(addr_df_center_dist_utility_input_id+"Parms",cparms)
    cfg.set_config_value(addr_df_center_dist_utility_input_id+"ParmsProtect",parmsprotect)
        
    center_addr_form.set_gridwidth(720)
    center_addr_form.set_custombwidth(120)
    center_addr_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = center_addr_form.get_html() 
    
    geocode_heading_html =   "<div>Calculate Distance From Center Point</div>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [geocode_heading_html,geocode_input_html]

    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)




def display_bulk_tune_input_form() :

    bulk_tune_form  =   InputForm(bulk_tune_utility_input_id,
                                    bulk_tune_utility_input_idList,
                                    bulk_tune_utility_input_labelList,
                                    bulk_tune_utility_input_typeList,
                                    bulk_tune_utility_input_placeholderList,
                                    bulk_tune_utility_input_jsList,
                                    bulk_tune_utility_input_reqList)       
    
    selectDicts     =   []
    geocoders       =   [] 

    geocoders.append(sugm.get_geocoder_title(sugm.ArcGISId))  
    geocoders.append(sugm.get_geocoder_title(sugm.BaiduId))  
    geocoders.append(sugm.get_geocoder_title(sugm.BingId))  
    geocoders.append(sugm.get_geocoder_title(sugm.GoogleId))  

    geocid  =   cfg.get_config_value("currentGeocoder")
    if(geocid == None) :
        geocdefault     =   sugm.get_geocoder_title(sugm.GoogleId)
    else :
        geocdefault     =   sugm.get_geocoder_title(geocid)
    
    geocsel         =   {"default":geocdefault,"list":geocoders}
    selectDicts.append(geocsel)

    get_select_defaults(bulk_tune_form,
                        bulk_tune_utility_input_id,
                        bulk_tune_utility_input_idList,
                        bulk_tune_utility_input_typeList,
                        selectDicts)
        
    bulk_tune_form.set_gridwidth(720)
    bulk_tune_form.set_custombwidth(120)
    bulk_tune_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = bulk_tune_form.get_html() 
    
    geocode_heading_html =   "<div>df Bulk Geoociding Tuning Parameters</div>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [geocode_heading_html,geocode_input_html]

    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoder helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

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
     
    if(gtype == sugm.GEOCODER)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_geocoder_id)   
         elif(geocid == sugm.GoogleId)          : return(google_geocoder_id)
         elif(geocid == sugm.BingId)            : return(bing_geocoder_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_geocoder_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_geocoder_id)
         elif(geocid == sugm.BaiduId)           : return(baidu_geocoder_id)
         
    elif(gtype == sugm.QUERY)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_query_id) 
         elif(geocid == sugm.GoogleId)          : return(google_query_id)
         elif(geocid == sugm.BingId)            : return(bing_query_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_query_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_query_id)
         elif(geocid == sugm.BaiduId)           : return(baidu_query_id)

    elif(gtype == sugm.REVERSE)  :
         if(geocid == sugm.ArcGISId)            : return(arcgis_reverse_id)   
         elif(geocid == sugm.GoogleId)          : return(google_reverse_id)
         elif(geocid == sugm.BingId)            : return(bing_reverse_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_reverse_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_reverse_id)
         elif(geocid == sugm.BaiduId)           : return(baidu_reverse_id)
   
    else :
        return(None)
 

def get_geocoder_parms_table(geocid) :
    """
    * ---------------------------------------------------------
    * function : get the html parms table a geocoder
    * 
    * parms :
    *  geocid  - geocoder id
    *
    * returns : 
    *  html geocoder parms table
    * --------------------------------------------------------
    """

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
    elif(geocid == sugm.BaiduId)             : labelList  =   baidu_geocoder_labelList
    
    #geocparms = get_geocoder_parms(geocid)
    geocparms = get_geocoder_form_parms_list(sugm.GEOCODER,geocid)
    
    row_added = 2
    
    georow = ["Geocoder"]
    geoRows.append(georow)
    geoHrefs.append([None])
            
    georow = ["&nbsp;&nbsp;" + sugm.get_geocoder_title(geocid)]
    geoRows.append(georow)
    geoHrefs.append([None])
    
    row_added = 2


    #print("get_geocoder_parms_table",geocparms)
    
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

def validate_geocode_connect_parms(geocid) :

    if(geocid == sugm.ArcGISId)              :  
        form    =   arcgis_geocoder_id
    elif(geocid == sugm.BingId)              :  
        form    =   bing_geocoder_id
    elif(geocid == sugm.GoogleId)            :  
        form    =   google_geocoder_id
    elif(geocid == sugm.OpenMapQuestId)      :  
        form    =   mapquest_geocoder_id
    elif(geocid == sugm.NominatimId)         :  
        form    =   nomin_geocoder_id
    elif(geocid == sugm.BaiduId)         :  
        form    =   baidu_geocoder_id
        
    fparms    =   cfg.get_config_value(form+"Parms")
    
    opstat  =   opStatus()
    
    if(not(fparms == None)) :
        
        if(geocid == sugm.ArcGISId)              :
            validate_arcgis_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.BingId)              : 
            validate_bing_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.GoogleId)            : 
            validate_google_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.OpenMapQuestId)      : 
            validate_mapquest_geocoder_parms(fparms,opstat,False)

        elif(geocid == sugm.NominatimId)         : 
            validate_nominatim_geocoder_parms(fparms,opstat,False)
        
        elif(geocid == sugm.BaiduId)              :
            validate_baidu_geocoder_parms(fparms,opstat,False)
            
    else :
        
        if(not(geocid == sugm.ArcGISId)) :
            opstat.set_status(False)
            opstat.set_errorMsg("No geocoder connect parms defined")
        
    return(opstat)


def validate_baidu_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate baidu geocoder parms
    * 
    * parms :
    *  gparms  - baidu geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """

    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,baidu_geocoder_idList)
    else :
        fparms  =   gparms
    
    if(len(fparms) > 0) :
            
        if( len(fparms[0]) == 0 ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Missing baidu api_key parameter")
            
        cfg.set_config_value(bing_geocoder_id + "Parms",fparms)
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Missing baidu api_key parameter")

        cfg.drop_config_value(baidu_geocoder_id + "Parms")    


def validate_arcgis_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate arcgis geocoder parms
    * 
    * parms :
    *  gparms  - arcgis geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,arcgis_geocoder_idList)
    else :
        fparms  =   gparms

    if(len(fparms) > 0) :
        # if autheticated user,pw and agent must be defined
        # else all need to be blank
        if( (len(fparms[0]) > 0) or (len(fparms[1]) > 0) or (len(fparms[2]) > 0) ) :
            
            if(len(fparms[0]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Missing username parameter")
            elif(len(fparms[1]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Missing password parameter")
            else :
                if(len(fparms[2]) == 0) :
                    fparms[2] = "my-application"
                
            cfg.set_config_value(arcgis_geocoder_id + "Parms",fparms)
            
    else :
        cfg.drop_config_value(arcgis_geocoder_id + "Parms")    


def validate_bing_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate bing geocoder parms
    * 
    * parms :
    *  gparms  - bing geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """

    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,bing_geocoder_idList)
    else :
        fparms  =   gparms
    
    if(len(fparms) > 0) :
            
        if( len(fparms[0]) == 0 ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Missing bing api_key parameter")
            
        cfg.set_config_value(bing_geocoder_id + "Parms",fparms)
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Missing bing api_key parameter")

        cfg.drop_config_value(bing_geocoder_id + "Parms")    


def validate_google_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate google geocoder parms
    * 
    * parms :
    *  gparms  - google geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,google_geocoder_idList)
    else :
        fparms  =   gparms
    
    if(len(fparms) > 0) :
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No google api key defined")
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No google api key defined")
        cfg.drop_config_value(google_geocoder_id + "Parms")    


def validate_mapquest_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate mapquest geocoder parms
    * 
    * parms :
    *  gparms  - bing geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,mapquest_geocoder_idList)
    else :
        fparms  =   gparms
    
    print("validate_mapquest_geocoder_parms",fparms) 
    
    if(len(fparms) > 0) :
            
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("Missing mapquest api_key parameter")
            
            cfg.set_config_value(mapquest_geocoder_id + "Parms",fparms)
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Missing mapquest api_key parameter")

        cfg.drop_config_value(mapquest_geocoder_id + "Parms")    


def validate_nominatim_geocoder_parms(gparms,opstat,getfparms=True) :
    """
    * ---------------------------------------------------------
    * function : validate nominatim geocoder parms
    * 
    * parms :
    *  gparms  - nominatim geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """

    if(getfparms) :
        fparms  =   get_parms_for_input(gparms,google_geocoder_idList)
    else :
        fparms  =   gparms
    
    if(len(fparms) > 0) :
    
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No Nominatum user_agent defined")
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No Nominatum user_agent defined")
        cfg.drop_config_value(arcgis_geocoder_id + "Parms")    



def validate_cmd_parms(ptype,geocid,gqparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate command parms
    * 
    * parms :
    *  ptype   - geocode type QUERY or REVERSE
    *  geocid  - geocoder id
    *  gqparms - geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(ptype == sugm.GEOCODER) :
    
        if(geocid == sugm.ArcGISId) :
            return(validate_arcgis_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.GoogleId) :
            return(validate_google_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.NominatimId) :
            return(validate_nominatim_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.BingId) :
            return(validate_bing_geocoder_parms(gqparms,opstat))
            
        elif(geocid == sugm.OpenMapQuestId) :
            return(validate_mapquest_geocoder_parms(gqparms,opstat))
        
        elif(geocid == sugm.BaiduId) :
            return(validate_baidu_geocoder_parms(gqparms,opstat))
            
    elif(ptype == sugm.QUERY) :
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
        
        elif(geocid == sugm.BaiduId) :
            idList          =   baidu_query_idList 
            reqList         =   baidu_query_reqList 
        
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("Geocode not supportd")
            
    elif(ptype == sugm.REVERSE) :
        if(geocid == sugm.GoogleId) :
            idList          =   google_reverse_idList 
            reqList         =   google_reverse_reqList 
        
        elif(geocid == sugm.BingId) :
            idList          =   bing_reverse_idList 
            reqList         =   bing_reverse_reqList 

        elif(geocid == sugm.ArcGISId) :
            idList          =   arcgis_reverse_idList 
            reqList         =   arcgis_reverse_reqList 
        
        elif(geocid == sugm.OpenMapQuestId) :
            idList          =   mapquest_reverse_idList 
            reqList         =   mapquest_reverse_reqList 
                
        elif(geocid == sugm.NominatimId) :
            idList          =   nomin_reverse_idList 
            reqList         =   nomin_reverse_reqList 

        elif(geocid == sugm.BaiduId) :
            idList          =   baidu_reverse_idList 
            reqList         =   baidu_reverse_reqList 
            
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("Reverse not supported for current geocoder")
        
    if(not opstat.get_status()) :
        return(opstat)
        
    fparms = get_parms_for_input(gqparms,idList)
    #print("validate_cmd_parms",fparms)
    missingParm     =   False
        
    if(ptype == sugm.GEOCODER)      : cfg_key = get_form_id(geocid,sugm.GEOCODER) + "Parms"
    elif(ptype == sugm.QUERY)       : cfg_key = get_form_id(geocid,sugm.QUERY) + "Parms"
    elif(ptype == sugm.REVERSE)     : cfg_key = get_form_id(geocid,sugm.REVERSE) + "Parms"
    
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
        

def get_geocoder_form_parms_list(ptype,geocid) :
    """
    * ---------------------------------------------------------
    * function : get the input form parms id list for geocoding
    * 
    * parms :
    *  ptype   - geocode type INIT or QUERY or REVERSE
    *  geocid  - geocoder id
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(ptype == sugm.GEOCODER)      : plist = cfg.get_config_value(get_form_id(geocid,sugm.GEOCODER) + "Parms")    
    elif(ptype == sugm.QUERY)       : plist = cfg.get_config_value(get_form_id(geocid,sugm.QUERY) + "Parms")    
    elif(ptype == sugm.REVERSE)     : plist = cfg.get_config_value(get_form_id(geocid,sugm.REVERSE) + "Parms") 

    return(plist)
        
  
def get_geocoder_cmd_kwargs(ptype,geocid) :
    """
    * ---------------------------------------------------------
    * function : get the previously stored cfg kwargs for geocoding
    * 
    * parms :
    *  ptype   - geocode type INIT or QUERY or REVERSE
    *  geocid  - geocoder id
    *
    * returns : 
    *  geocoding kwargs from cfg
    * --------------------------------------------------------
    """
    
    if(ptype == sugm.GEOCODER)     : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.GEOCODER) + "Parms")
    elif(ptype == sugm.QUERY)      : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.QUERY) + "Parms")
    elif(ptype == sugm.REVERSE)    : geoparms = cfg.get_config_value(get_form_id(geocid,sugm.REVERSE) + "Parms")
    
    if(ptype == sugm.GEOCODER) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_geocoder_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_geocoder_labelList 
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_geocoder_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_geocoder_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_geocoder_labelList 
        elif(geocid == sugm.BaiduId)             : labelList       =   baidu_geocoder_labelList 

    elif(ptype == sugm.QUERY) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_query_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_query_labelList 
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_query_labelList 
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_query_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_query_labelList 
        elif(geocid == sugm.BaiduId)             : labelList       =   baidu_query_labelList 
        
    elif(ptype == sugm.REVERSE) :
        if(geocid == sugm.GoogleId)              : labelList       =   google_reverse_labelList 
        elif(geocid == sugm.BingId)              : labelList       =   bing_reverse_labelList
        elif(geocid == sugm.OpenMapQuestId)      : labelList       =   mapquest_reverse_labelList
        elif(geocid == sugm.NominatimId)         : labelList       =   nomin_reverse_labelList 
        elif(geocid == sugm.ArcGISId)            : labelList       =   arcgis_reverse_labelList 
        elif(geocid == sugm.BaiduId)             : labelList       =   baidu_reverse_labelList 
 
    #print("get_geocoder_cmd_kwargs\n",geoparms,"\n",labelList)

    geokwargs = {}

    if(geoparms != None) :
        for i in range(len(geoparms)) : 
            if(len(geoparms[i]) > 0) :
                if(geoparms[i] == 'False') :
                    geokwargs.update({labelList[i]:False}) 
                elif(geoparms[i] == 'True') :
                    geokwargs.update({labelList[i]:True}) 
                else :    
                    geokwargs.update({labelList[i]:geoparms[i]})

    #print("get_geocoder_cmd_kwargs : geokwargs\n",geokwargs)
    if(len(geokwargs) == 0) :
        return(None)
    else :
        
        if( (ptype == sugm.QUERY) or (ptype == sugm.REVERSE) ):
            return(customize_query_kwargs(geocid,geokwargs)) 
        else :
            return(geokwargs)

"""
#--------------------------------------------------------------------------
#  override kwargs stored in config
#--------------------------------------------------------------------------
"""
def customize_query_kwargs(geocid,geokwargs) :
    """
    * ---------------------------------------------------------
    * function : customize stored cfg kwargs for geocoding
    * 
    * parms :
    *  geocid     - geocoder id
    *  geokwargs  - geocoder kwargs
    *
    * returns : 
    *  geocoding kwargs from cfg
    * --------------------------------------------------------
    """

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
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoder display methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 




def display_geocode_inputs(geocid,gtype,showfull=False,statusHtml=None) :
    """
    * ---------------------------------------------------------
    * function : display geocode input form
    * 
    * parms :
    *  parms            - form parms
    *  ptype            - geocode op type
    *  showfull         - show all parms flag
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
 
    #print("display_geocode_inputs",geocid,gtype)
    
    if(geocid == None) :
        geocid = sugm.GoogleId
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid,True)
        
    opstat  =   validate_geocode_connect_parms(geocid)
    
    if(not (opstat.get_status()) ) :
        display_geocoders(geocid)
        display_exception(opstat)
        return()        
    
    geo_parms_html = get_geocoder_parms_table(geocid)

    
    if(gtype == sugm.QUERY) :
        if(geocid == sugm.ArcGISId)              : form    =   arcgis_query_form
        elif(geocid == sugm.BingId)              : form    =   bing_query_form
        elif(geocid == sugm.GoogleId)            : form    =   google_query_form
        elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_query_form
        elif(geocid == sugm.NominatimId)         : form    =   nomin_query_form
        elif(geocid == sugm.BaiduId)             : form    =   baidu_query_form
        
    else :
        if(geocid == sugm.ArcGISId)              : form    =   arcgis_reverse_form
        elif(geocid == sugm.BingId)              : form    =   bing_reverse_form
        elif(geocid == sugm.GoogleId)            : form    =   google_reverse_form
        elif(geocid == sugm.OpenMapQuestId)      : form    =   mapquest_reverse_form
        elif(geocid == sugm.NominatimId)         : form    =   nomin_reverse_form
        elif(geocid == sugm.BaiduId)             : form    =   baidu_reverse_form
    
    from dfcleanser.common.html_widgets import InputForm
    geofunc_input_form = InputForm(form[0],
                                   form[1],
                                   form[2],
                                   form[3],
                                   form[4],
                                   form[5],
                                   form[6])
    
    #geofunc_input_form.dump()
    
    if(gtype == sugm.QUERY) :
        
        selectDicts     =   [] 
        
        if(geocid == sugm.BingId) :
            
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            
            country_codes   =   get_Dict("Country_Codes")
            cc_keys         =   list(country_codes.keys())
            cc_keys.sort()
            ccsel           =   {"default":"United States","list":cc_keys}
            selectDicts.append(ccsel)

            bingsel           =   {"default":"False","list":["True","False"]}
            selectDicts.append(bingsel)
            bingsel1           =   {"default":"False","list":["True","False"]}
            selectDicts.append(bingsel1)
            
        elif(geocid == sugm.GoogleId)              : 
            
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            
            cctlds          =   get_Dict("ccTLDs")
            cctlds_keys     =   ["None"]
            ccs             =   list(cctlds.keys())
            ccs.sort()
            for i in range(len(ccs)) :
                cctlds_keys.append(ccs[i])    
            #cctlds_keys.sort()
            cctldssel       =   {"default":cctlds_keys[0],"list":cctlds_keys}
            selectDicts.append(cctldssel)
            
            langs           =   get_Dict("Google_Language_Codes")
            langs_keys      =   []
            lngs            =   list(langs.keys())
            lngs.sort()
            for i in range(len(lngs)) :
                langs_keys.append(lngs[i])    
            #langs_keys.sort()
            cctldssel       =   {"default":"English","list":langs_keys}
            selectDicts.append(cctldssel)
            
            googsel           =   {"default":"False","list":["True","False"]}
            selectDicts.append(googsel)
            
        elif(geocid == sugm.NominatimId)              :
            
            nonimsel          =   {"default":"False","list":["True","False"]}
            selectDicts.append(nonimsel)

        get_select_defaults(geofunc_input_form,
                            form[0],form[1],form[3],
                            selectDicts)

    elif(gtype == sugm.REVERSE) :
        
        selectDicts     =   []
        
        if(geocid == sugm.GoogleId)              : 
            
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            
            langs           =   get_Dict("Google_Language_Codes")
            langs_keys      =   []
            lngs            =   list(langs.keys())
            lngs.sort()
            for i in range(len(lngs)) :
                langs_keys.append(lngs[i])    
            #langs_keys.sort()
            cctldssel       =   {"default":"English","list":langs_keys}
            selectDicts.append(cctldssel)
            
            googsel           =   {"default":"False","list":["True","False"]}
            selectDicts.append(googsel)
            
            get_select_defaults(geofunc_input_form,
                                form[0],form[1],form[3],
                                selectDicts)

        elif(geocid == sugm.BingId) :
            
            from dfcleanser.sw_utilities.sw_utility_model import get_Dict
            
            country_codes   =   get_Dict("Country_Codes")
            cc_keys         =   list(country_codes.keys())
            cc_keys.sort()
            ccsel           =   {"default":"United States","list":cc_keys}
            selectDicts.append(ccsel)
            
            bingsel           =   {"default":"False","list":["True","False"]}
            selectDicts.append(bingsel) 
            
            get_select_defaults(geofunc_input_form,
                                form[0],form[1],form[3],
                                selectDicts)
            
        elif(geocid == sugm.OpenMapQuestId) :

            mapquestsel       =   {"default":"False","list":["True","False"]}
            get_select_defaults(geofunc_input_form,
                                form[0],form[1],form[3],
                                [mapquestsel])
            
            
    geofunc_input_form.set_gridwidth(620)
    geofunc_input_form.set_custombwidth(99) 
    
    if(showfull) :
        geofunc_input_form.set_fullparms(True)    
    
    geofunc_input_html = ""
    geofunc_input_html = geofunc_input_form.get_html()
    
    if (gtype == sugm.QUERY) :
        geofunc_heading_html =   "<div>Interactive Geocoding Parameters</div>"
    else :
        geofunc_heading_html =   "<div>Interactive Reverse Geocoding Parameters</div>"
        
    if(statusHtml is None) :
 
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [geofunc_heading_html,geo_parms_html,geofunc_input_html]
    
        display_generic_grid("geocode-connector-wrapper",gridclasses,gridhtmls)
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-bottom"]
        gridhtmls       =   [geofunc_heading_html,geo_parms_html,geofunc_input_html,statusHtml]
    
        display_generic_grid("geocode-connector-wrapper-with-notes",gridclasses,gridhtmls)
        
 
def get_geocoder_table(for_bulk_geocoding=False) :
    """
    * ---------------------------------------------------------
    * function : get html geocoders table
    * 
    * parms :
    *
    * returns : 
    *  html for geocoders table
    * --------------------------------------------------------
    """
      
    geocslistHeader     =   [""]
    geocslistRows       =   []
    geocslistWidths     =   [100]
    geocslistAligns     =   ["left"]
    geocslistHrefs      =   []

    geocstexts          =   []
    geocshrefs          =   []
    
    if(for_bulk_geocoding) :
        for i in range(len(sugm.supported_Bulk_Geocoders)) :
            geocstexts.append("&nbsp;&nbsp;" + sugm.get_geocoder_title(sugm.supported_Bulk_Geocoders[i]))
            geocshrefs.append("select_bulk_geocoder")
        
    else :
        
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


def display_geocoders(geocodeid,showfull=False,showNotes=True,with_status=None) :
    """
    * ---------------------------------------------------------
    * function : display geocoder init screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *   showfull   -   show all parms flag
    *   showNotes  -   show notes flag
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    listHtml = get_geocoder_table()
    
    if(geocodeid == None) :
        geocodeid       =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocodeid == None) : 
            geocodeid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocodeid,True)

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
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BingId,True)
        geocoder_input_form   =   [bing_geocoder_id,
                                   bing_geocoder_idList,
                                   bing_geocoder_labelList,
                                   bing_geocoder_typeList,
                                   bing_geocoder_placeholderList,
                                   bing_geocoder_jsList,
                                   bing_geocoder_reqList]

    elif(geocodeid == sugm.OpenMapQuestId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.OpenMapQuestId,True)
        geocoder_input_form   =   [mapquest_geocoder_id,
                                   mapquest_geocoder_idList,
                                   mapquest_geocoder_labelList,
                                   mapquest_geocoder_typeList,
                                   mapquest_geocoder_placeholderList,
                                   mapquest_geocoder_jsList,
                                   mapquest_geocoder_reqList]

    elif(geocodeid == sugm.NominatimId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.NominatimId,True)
        geocoder_input_form   =   [nomin_geocoder_id,
                                   nomin_geocoder_idList,
                                   nomin_geocoder_labelList,
                                   nomin_geocoder_typeList,
                                   nomin_geocoder_placeholderList,
                                   nomin_geocoder_jsList,
                                   nomin_geocoder_reqList]

    elif(geocodeid == sugm.ArcGISId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.ArcGISId,True)
        geocoder_input_form   =   [arcgis_geocoder_id,
                                   arcgis_geocoder_idList,
                                   arcgis_geocoder_labelList,
                                   arcgis_geocoder_typeList,
                                   arcgis_geocoder_placeholderList,
                                   arcgis_geocoder_jsList,
                                   arcgis_geocoder_reqList]
    
    elif(geocodeid == sugm.BaiduId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BaiduId,True)
        geocoder_input_form   =   [baidu_geocoder_id,
                                   baidu_geocoder_idList,
                                   baidu_geocoder_labelList,
                                   baidu_geocoder_typeList,
                                   baidu_geocoder_placeholderList,
                                   baidu_geocoder_jsList,
                                   baidu_geocoder_reqList]
    
    from dfcleanser.common.html_widgets import InputForm
    geocode_input_form = InputForm(geocoder_input_form[0],
                                   geocoder_input_form[1],
                                   geocoder_input_form[2],
                                   geocoder_input_form[3],
                                   geocoder_input_form[4],
                                   geocoder_input_form[5],
                                   geocoder_input_form[6])
    
    geocode_input_form.set_gridwidth(720)
    geocode_input_form.set_custombwidth(90)
    
    if(showfull) :
        geocode_input_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = geocode_input_form.get_html() 
        
    geocode_heading_html =   "<br><div>Geocoder Parms - " + sugm.get_geocoder_title(geocodeid) + "</div>"
 
    if(with_status is None) :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [geocode_heading_html,listHtml,geocode_input_html]
    
        display_generic_grid("geocode-connector-wrapper",gridclasses,gridhtmls)
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-bottom"]
        gridhtmls       =   [geocode_heading_html,listHtml,geocode_input_html,with_status]
    
        display_generic_grid("geocode-connector-wrapper-with-status",gridclasses,gridhtmls)
        
    
    if(showNotes) :
        notes = [] 
    
        if(geocodeid == sugm.ArcGISId) :
            return()
        elif(geocodeid == sugm.GoogleId) :
            return()
        elif(geocodeid == sugm.BingId) : 
            return()
            notes.append("Bing geoocoding requires an api_key for all Bing geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.OpenMapQuestId) :
            return()
            notes.append("OpenMapQuest geoocoding requires an api_key for all OpenMapQuest geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.NominatimId) : 
            return()
            notes.append("Nominatim geoocoding requires a user-agent for all Nominatim geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")
        elif(geocodeid == sugm.BaiduId) :        
            notes.append("Baidu geoocoding requires an api_key for all Baidu geocoding including bulk geocoding.")
            notes.append("The rest of the parameters are used as default values for any subsequent geocoding calls of this connector.")

        from dfcleanser.common.common_utils import display_msgs
        display_msgs(notes,None)






