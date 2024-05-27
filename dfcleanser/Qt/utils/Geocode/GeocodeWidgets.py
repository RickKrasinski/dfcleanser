"""
# ZipCodeWidgets
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

from distutils import ccompiler
import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

import dfcleanser.common.cfg as cfg 
from dfcleanser.sw_utilities.dfc_qt_model import maketextarea

from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import SWGeocodeUtility_ID


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             general Data Import Housekeeping                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20

"""
#--------------------------------------------------------------------------
#   geocoder connect forms
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
                                         "Query</br>Geocoding",
                                         "Reverse</br>Geocoding",
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


arcgis_geocoder_reqList             =   [0,1,2]

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
                                         "Query</br>Geocoding",
                                         "Reverse</br>Geocoding",
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

google_geocoder_reqList             =   [0,1]

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
                                         "Query</br>Geocoding",
                                         "Reverse</br>Geocoding",
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

bing_geocoder_reqList               =   [0]

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
                                             "Query</br>Geocoding",
                                             "Reverse</br>Geocoding",
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

mapquest_geocoder_reqList               =   [0]

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
                                         "Query</br>Geocoding",
                                         "Reverse</br>Geocoding",
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

nomin_geocoder_reqList              =   [0]

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
                                         "Query</br>Geocoding",
                                         "Reverse</br>Geocoding",
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
#   Query Forms
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

arcgis_query_idList                 =    ["aqquery1",
                                          "aqquery2",
                                          "aqquery3",
                                          "aqquery4",
                                          "aqquery5",
                                          "aqcount",
                                          "aqtimeout",
                                          None,None,None,None]

arcgis_query_labelList              =   ["address(1)",
                                         "address(2)",
                                         "address(3)",
                                         "address(4)",
                                         "address(5)",
                                         "number_of_results",
                                         "timeout",
                                         "Get</br>Coord(s)",
                                         "Clear","Return","Help"]


arcgis_query_typeList               =   ["text","text","text","text","text","text","text",
                                         "button","button","button","button"]

arcgis_query_placeholderList        =   ["address 1",
                                         "address 2",
                                         "address 3",
                                         "address 4",
                                         "address 5",
                                         "max number of results per address (default - 1) ",
                                         "enter timeout in seconds (default - 10 seconds)",
                                         None,None,None,None]

arcgis_query_reqList                =   [0]


"""
#--------------------------------------------------------------------------
#   google get coords forms
#--------------------------------------------------------------------------
"""
google_query_title                  =   "Google V3 Geocoder Get Coordinates"
google_query_id                     =   "googlequery"

google_query_idList                 =    ["gqquery1",
                                          "gqquery2",
                                          "gqquery3",
                                          "gqquery4",
                                          "gqquery5",
                                          "gqcount",
                                          "gqtimeout",
                                          "gqbounds",
                                          "gqregion",
                                          "gqcomps",
                                          "gqlang",
                                          "gqsensor",
                                          None,None,None,None]

google_query_labelList              =   ["address(1)",
                                         "address(2)",
                                         "address(3)",
                                         "address(4)",
                                         "address(5)",
                                         "number_of_results",
                                         "timeout",
                                         "bounds",
                                         "region",
                                         "components",
                                         "language",
                                         "sensor",
                                         "Get</br>Coord(s)",
                                         "Clear","Return","Help"]


google_query_typeList               =   ["text","text","text","text","text","text","text",maketextarea(1),"select",maketextarea(1),"select","select",
                                         "button","button","button","button"]

google_query_placeholderList        =   ["address 1",
                                         "address 2",
                                         "address 3",
                                         "address 4",
                                         "address 5",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter bounding box of the viewport (default - None)",
                                         "enter the ccTLD region code (default - None)",
                                         "enter components dict) (default - None)",
                                         "enter the language (default - None)",
                                         "enter sensor flag (default - False)",
                                         None,None,None,None]

google_query_reqList                =   [0]


"""
#--------------------------------------------------------------------------
#   bing get coords form
#--------------------------------------------------------------------------
"""
bing_query_title                    =   "Bing Geocoder Get Coordinates"
bing_query_id                       =   "bingquery"

bing_query_idList                   =    ["bqquery1",
                                          "bqquery2",
                                          "bqquery3",
                                          "bqquery4",
                                          "bqquery5",
                                          "bqcount",
                                          "bqtimeout",
                                          "bqloc",
                                          "bqculture",
                                          "bqnbc",
                                          "bqcc",
                                          None,None,None,None]

bing_query_labelList                =   ["address(1)",
                                         "address(2)",
                                         "address(3)",
                                         "address(4)",
                                         "address(5)",
                                         "number_of_results",
                                         "timeout",
                                         "user_location",
                                         "culture",
                                         "include_neighborhood",
                                         "include_country_code",
                                         "Get</br>Coord(s)",
                                         "Clear","Return","Help"]


bing_query_typeList                 =   ["text","text","text","text","text","text","text","text","select","select","select",
                                         "button","button","button","button"]

bing_query_placeholderList          =   ["address 1",
                                         "address 2",
                                         "address 3",
                                         "address 4",
                                         "address 5",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         "enter coords to prioritize nearest to (default - None)",
                                         "enter two-letter country code (default - None) ",
                                         "return neighborhood field (default - False)",
                                         "return 2 digit country code (default - False)",
                                         None,None,None,None]

bing_query_reqList                  =   [0]


"""
#--------------------------------------------------------------------------
#   OpenMapQuest get coords form
#--------------------------------------------------------------------------
"""
mapquest_query_title                     =   "OpenMapQuest Get Coordinates"
mapquest_query_id                        =   "mapquestquery"

mapquest_query_idList                    =  ["mqquery1",
                                             "mqquery2",
                                             "mqquery3",
                                             "mqquery4",
                                             "mqquery5",
                                             "mqcount",
                                             "mqtimeout",
                                             None,None,None,None]

mapquest_query_labelList                 =  ["address(1)",
                                             "address(2)",
                                             "address(3)",
                                             "address(4)",
                                             "address(5)",
                                             "number_of_results",
                                             "timeout",
                                             "Get</br>Coord(s)",
                                             "Clear","Return","Help"]


mapquest_query_typeList                  =   ["text","text","text","text","text","text","text",
                                              "button","button","button","button"]

mapquest_query_placeholderList           =   ["address 1",
                                              "address 2",
                                              "address 3",
                                              "address 4",
                                              "address 5",
                                              "max number of results displayed per address (default - 1 : max 5) ",
                                              "enter timeout in seconds (default - 20)",
                                              None,None,None,None]

mapquest_query_reqList                   =   [0]


"""
#--------------------------------------------------------------------------
#   Nominatim get coords form
#--------------------------------------------------------------------------
"""
nomin_query_title                        =   "Nominatim Get Coordinates"
nomin_query_id                           =   "nominquery"

nomin_query_idList                       =  ["nqquery1",
                                             "nqquery2",
                                             "nqquery3",
                                             "nqquery4",
                                             "nqquery5",
                                             "nqcount",
                                             "nqtimeout",
                                             "nqaddr",
                                             "nqlang",
                                             "nqgeom",
                                             None,None,None,None]

nomin_query_labelList                    =  ["address(1)",
                                             "address(2)",
                                             "address(3)",
                                             "address(4)",
                                             "address(5)",
                                             "number_of_results",
                                             "timeout",
                                             "addressdetails",
                                             "language",
                                             "geometry",
                                             "Get</br>Coord(s)",
                                             "Clear","Return","Help"]


nomin_query_typeList                     =   ["text","text","text","text","text","text","text","select","text","text",
                                              "button","button","button","button"]

nomin_query_placeholderList              =   ["address 1",
                                              "address 2",
                                              "address 3",
                                              "address 4",
                                              "address 5",
                                              "max number of results displayed per address (default - 1 : max 5) ",
                                              "enter timeout in seconds (default - 20)",
                                              "Location.raw to include address details  (default - False)",
                                              "language in which to return results  (default - English)",
                                              "return the result’s geometry in wkt, svg, kml, or geojson formats (default - None)",
                                              None,None,None,None]

nomin_query_reqList                      =   [0]


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
                                          None,None,None,None]

baidu_query_labelList               =   ["address(s)",
                                         "number_of_results",
                                         "timeout",
                                         "Get</br>Coord(s)",
                                         "Clear","Return","Help"]


baidu_query_typeList                =   [maketextarea(6),"text","text",
                                         "button","button","button","button"]

baidu_query_placeholderList         =   ["single address string or [] list of address strings",
                                         "max number of results displayed per address (default - 1 : max 5) ",
                                         "enter timeout in seconds (default - 20)",
                                         None,None,None,None]

baidu_query_reqList                 =   [0]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoder reverse address forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google get address forms
#--------------------------------------------------------------------------
"""
google_reverse_title                   =   "Google V3 Geocoder Get Address"
google_reverse_id                      =   "googlereverse"

google_reverse_idList                  =    ["grquery1",
                                             "grquery2",
                                             "grquery3",
                                             "grquery4",
                                             "grquery5",
                                             "grcount",
                                             "grtimeout",
                                             "grlang",
                                             "grsensor",
                                             None,None,None,None]

google_reverse_labelList               =   ["latitude_longitude(1)",
                                            "latitude_longitude(2)",
                                            "latitude_longitude(3)",
                                            "latitude_longitude(4)",
                                            "latitude_longitude(5)",
                                            "number_of_results",
                                            "timeout",
                                            "language",
                                            "sensor",
                                            "Get</br>Address(s)",
                                            "Clear","Return","Help"]


google_reverse_typeList                =   ["text","text","text","text","text","text","text","select","select",
                                            "button","button","button","button"]

google_reverse_placeholderList         =   ["[latitude, longitude](1)",
                                            "[latitude, longitude](2)",
                                            "[latitude, longitude](3)",
                                            "[latitude, longitude](4)",
                                            "[latitude, longitude](5)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "enter the language (default - English)",
                                            "enter sensor flag (default - False)",
                                            None,None,None,None]

google_reverse_reqList                 =   [0]


"""
#--------------------------------------------------------------------------
#   ArcGIS get address forms
#--------------------------------------------------------------------------
"""
arcgis_reverse_title                   =   "ArcGIS Geocoder Get Address"
arcgis_reverse_id                      =   "arcgisreverse"

arcgis_reverse_idList                  =    ["arquery1",
                                             "arquery2",
                                             "arquery3",
                                             "arquery4",
                                             "arquery5",
                                             "arcount",
                                             "artimeout",
                                             "ardistance",
                                             "arwkid",
                                             None,None,None,None]

arcgis_reverse_labelList               =   ["latitude_longitude(1)",
                                            "latitude_longitude(2)",
                                            "latitude_longitude(3)",
                                            "latitude_longitude(4)",
                                            "latitude_longitude(5)",
                                            "number_of_results",
                                            "timeout",
                                            "distance",
                                            "wkid",
                                            "Get</br>Address(s)",
                                            "Clear","Return","Help"]


arcgis_reverse_typeList                =   ["text","text","text","text","text","text","text","text","text",
                                            "button","button","button","button"]

arcgis_reverse_placeholderList         =   ["[latitude, longitude](1)",
                                            "[latitude, longitude](2)",
                                            "[latitude, longitude](3)",
                                            "[latitude, longitude](4)",
                                            "[latitude, longitude](5)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "Distance from the query location (default - None)",
                                            "WKID to use for both input and output coordinates (default - 4236)",
                                            None,None,None,None]

arcgis_reverse_reqList                 =   [0]


"""
#--------------------------------------------------------------------------
#   Bing get address forms
#--------------------------------------------------------------------------
"""
bing_reverse_title                     =   "Bing Geocoder Get Address"
bing_reverse_id                        =   "bingreverse"

bing_reverse_idList                    =    ["brquery1",
                                             "brquery2",
                                             "brquery3",
                                             "brquery4",
                                             "brquery5",
                                             "brcount",
                                             "brtimeout",
                                             "brculture",
                                             "brincludecc",
                                             None,None,None,None]

bing_reverse_labelList                 =   ["latitude_longitude(1)",
                                            "latitude_longitude(2)",
                                            "latitude_longitude(3)",
                                            "latitude_longitude(4)",
                                            "latitude_longitude(5)",
                                            "number_of_results",
                                            "timeout",
                                            "culture",
                                            "include_country_code",
                                            "Get</br>Address(s)",
                                            "Clear","Return","Help"]


bing_reverse_typeList                  =   ["text","text","text","text","text","text","text","select","select",
                                            "button","button","button","button"]

bing_reverse_placeholderList           =   ["[latitude, longitude](1)",
                                            "[latitude, longitude](2)",
                                            "[latitude, longitude](3)",
                                            "[latitude, longitude](4)",
                                            "[latitude, longitude](5)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            "enter culture code",
                                            "include country code",
                                            None,None,None,None]

bing_reverse_reqList                   =   [0]


"""
#--------------------------------------------------------------------------
#   OpenMapQuest get address forms
#--------------------------------------------------------------------------
"""
mapquest_reverse_title                     =   "OpenMapQuest Geocoder Get Address"
mapquest_reverse_id                        =   "mapquestreverse"

mapquest_reverse_idList                    =    ["mrquery1",
                                                 "mrquery2",
                                                 "mrquery3",
                                                 "mrquery4",
                                                 "mrquery5",
                                                 "mrcount",
                                                 "mrtimeout",
                                                 "mrlanguage",
                                                 "mradetails",
                                                 None,None,None,None]

mapquest_reverse_labelList                 =   ["latitude_longitude(1)",
                                                "latitude_longitude(2)",
                                                "latitude_longitude(3)",
                                                "latitude_longitude(4)",
                                                "latitude_longitude(5)",
                                                "number_of_results",
                                                "timeout",
                                                "language",
                                                "addressdetails",
                                                "Get</br>Address(s)",
                                                "Clear","Return","Help"]


mapquest_reverse_typeList                  =   ["text","text","text","text","text","text","text","text","select",
                                                "button","button","button","button"]

mapquest_reverse_placeholderList           =   ["[latitude, longitude](1)",
                                                "[latitude, longitude](2)",
                                                "[latitude, longitude](3)",
                                                "[latitude, longitude](4)",
                                                "[latitude, longitude](5)",
                                                "max number of results displayed per address (default - 1 : max 5) ",
                                                "enter timeout in seconds (default - 20)",
                                                "Preferred language in which to return results (default - English)",
                                                "include address details such as city, county ... (default - True)",
                                                None,None,None,None]

mapquest_reverse_reqList                   =   [0]


"""
#--------------------------------------------------------------------------
#   Nominatim get address forms
#--------------------------------------------------------------------------
"""
nomin_reverse_title                        =   "Nominatim Geocoder Get Address"
nomin_reverse_id                           =   "nominreverse"

nomin_reverse_idList                       =    ["nrquery1",
                                                 "nrquery2",
                                                 "nrquery3",
                                                 "nrquery4",
                                                 "nrquery5",
                                                 "nrcount",
                                                 "nrtimeout",
                                                 "nrlanguage",
                                                 "nraddressdetails",
                                                 None,None,None,None]

nomin_reverse_labelList                    =   ["latitude_longitude(1)",
                                                "latitude_longitude(2)",
                                                "latitude_longitude(3)",
                                                "latitude_longitude(4)",
                                                "latitude_longitude(5)",
                                                "number_of_results",
                                                "timeout",
                                                "language",
                                                "address_details",
                                                "Get</br>Address(s)",
                                                "Clear","Return","Help"]


nomin_reverse_typeList                     =   ["text","text","text","text","text","text","text","text","select",
                                                "button","button","button","button"]

nomin_reverse_placeholderList              =   ["[latitude, longitude](1)",
                                                "[latitude, longitude](2)",
                                                "[latitude, longitude](3)",
                                                "[latitude, longitude](4)",
                                                "[latitude, longitude](5)",
                                                "max number of results displayed per address (default - 1 : max 5) ",
                                                "enter timeout in seconds (default - 20)",
                                                "Preferred language in which to return results (default - English)",
                                                "address details included",
                                                None,None,None,None]

nomin_reverse_reqList                      =   [0]


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
                                             None,None,None,None]

baidu_reverse_labelList                =   ["latitude_longitude(s)",
                                            "number_of_results",
                                            "timeout",
                                            "Get</br>Address(s)",
                                            "Clear","Return","Help"]


baidu_reverse_typeList                 =   [maketextarea(6),"text","text",
                                            "button","button","button"]

baidu_reverse_placeholderList          =   ["list or tuple of (latitude, longitude)",
                                            "max number of results displayed per address (default - 1 : max 5) ",
                                            "enter timeout in seconds (default - 20)",
                                            None,None,None,None]

baidu_reverse_reqList                  =   [0]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoding Distance Forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

from_address_distance_title                =   "Geocoding From Addresses"
from_address_distance_id                   =   "fromaddrdistid"

from_address_distance_idList               =    ["fromaddrdist1",
                                                 "fromaddrdist2",
                                                 "fromaddrdist3",
                                                 "fromaddrdist4",
                                                 "fromaddrdist5"]

from_address_distance_labelList             =   ["from_address(1)",
                                                "from_address(2)",
                                                "from_address(3)",
                                                "from_address(4)",
                                                "from_address(5)"]


from_address_distance_typeList              =   ["text","text","text","text","text"]

from_address_distance_placeholderList       =   ["from address 1",
                                                "from address 2",
                                                "from address 3",
                                                "from address 4",
                                                "from address 5"]

from_address_distance_reqList               =   [0]


to_address_distance_title                =   "Geocoding To Addresses"
to_address_distance_id                   =   "toaddrdistid"

to_address_distance_idList               =      ["toaddrdist1",
                                                 "toaddrdist2",
                                                 "toaddrdist3",
                                                 "toaddrdist4",
                                                 "toaddrdist5"]

to_address_distance_labelList             =     ["to_address(1)",
                                                "to_address(2)",
                                                "to_address(3)",
                                                "to_address(4)",
                                                "to_address(5)"]


to_address_distance_typeList              =     ["text","text","text","text","text"]

to_address_distance_placeholderList       =     ["to address 1",
                                                "to address 2",
                                                "to address 3",
                                                "to address 4",
                                                "to address 5"]

to_address_distance_reqList             =   [0]



from_latlng_distance_title                =   "Geocoding From laylnges"
from_latlng_distance_id                   =   "fromaddrdistid"

from_latlng_distance_idList               =    ["fromaddrdist1",
                                                 "fromaddrdist2",
                                                 "fromaddrdist3",
                                                 "fromaddrdist4",
                                                 "fromaddrdist5"]

from_latlng_distance_labelList             =   ["from_Latitude_Longitude(1)",
                                                "from_Latitude_Longitude(2)",
                                                "from_Latitude_Longitude(3)",
                                                "from_Latitude_Longitude(4)",
                                                "from_Latitude_Longitude(5)"]


from_latlng_distance_typeList              =   ["text","text","text","text","text"]

from_latlng_distance_placeholderList       =   ["from Latitude_Longitude 1",
                                                "from Latitude_Longitude 2",
                                                "from Latitude_Longitude 3",
                                                "from latlng 4",
                                                "from latlng 5"]

from_latlng_distance_reqList               =   [0]


to_latlng_distance_title                =   "Geocoding To latlnges"
to_latlng_distance_id                   =   "toaddrdistid"

to_latlng_distance_idList               =      ["toaddrdist1",
                                                 "toaddrdist2",
                                                 "toaddrdist3",
                                                 "toaddrdist4",
                                                 "toaddrdist5"]

to_latlng_distance_labelList             =     ["to_Latitude_Longitude(1)",
                                                "to_Latitude_Longitude(2)",
                                                "to_Latitude_Longitude(3)",
                                                "to_Latitude_Longitude(4)",
                                                "to_Latitude_Longitude(5)"]


to_latlng_distance_typeList              =     ["text","text","text","text","text"]

to_latlng_distance_placeholderList       =     ["to latlng 1",
                                                "to latlng 2",
                                                "to latlng 3",
                                                "to latlng 4",
                                                "to latlng 5"]

to_latlng_distance_reqList             =   [0]



addr_dist_utility_input_title             =   "Address Distance Columns"
addr_dist_utility_input_id                =   "addrdist"

addr_dist_utility_input_idList            =   ["disunits",
                                               "distalg",
                                               "elipsoid",
                                               None,None,None,None,None]

addr_dist_utility_input_labelList         =   ["distance_units",
                                               "distance_algorithm",
                                               "elipsoid",
                                               "Calculate</br>Address</br>Distance",
                                               "Get</br>LatLng</br>Distance",
                                               "Get</br>Dataframe</br>Distance",
                                               "Clear","Return","Help"]


addr_dist_utility_input_typeList          =   ["select","select","select",
                                               "button","button","button","button","button","button"]

addr_dist_utility_input_placeholderList   =  ["result in km - True : km, False : miles (default - True) ",
                                              "geocode algorithm (default - geodesic) ",
                                              "select elipsoid (default - 'WGS-84') ",
                                              None,None,None,None,None]

addr_dist_utility_input_reqList           =   [0,1]




latlng_dist_utility_input_title             =   "Address Distance Columns"
latlng_dist_utility_input_id                =   "addrdist"

latlng_dist_utility_input_idList            =   ["disunits",
                                               "distalg",
                                               "elipsoid",
                                               None,None,None,None,None]

latlng_dist_utility_input_labelList         =   ["distance_units",
                                               "distance_algorithm",
                                               "elipsoid",
                                               "Calculate</br>LatLng</br>Distance",
                                               "Get</br>Address</br>Distance",
                                               "Get</br>Dataframe</br>Distance",
                                               "Clear","Return","Help"]


latlng_dist_utility_input_typeList          =   ["select","select","select",
                                               "button","button","button","button","button","button"]

latlng_dist_utility_input_placeholderList   =  ["result in km - True : km, False : miles (default - True) ",
                                              "geocode algorithm (default - geodesic) ",
                                              "select elipsoid (default - 'WGS-84') ",
                                              None,None,None,None,None]



latlng_dist_utility_input_reqList           =   [0,1]


"""
#--------------------------------------------------------------------------
#    address dataframe distance input forms
#--------------------------------------------------------------------------
"""
addr_df_dist_utility_input_title             =   "Address Distance Columns"
addr_df_dist_utility_input_id                =   "addrdfdist"
addr_df_dist_utility_input_idList            =   ["addrdffromdistdf",
                                                  "fromlatlngcolumns",
                                                  "fromcolnames",
                                                  "tolatlngcolumns",
                                                  "tocolnames",
                                                  "newcol",
                                                  "dfdisunits",
                                                  "dfdistalg",
                                                  "dfelipsoid",
                                                  None,None,None,None]

addr_df_dist_utility_input_labelList         =   ["dataframe",
                                                  "dataframe_location_from_columns",
                                                  "dataframe_column_from_name(s)",
                                                  "dataframe_location_to_columns",
                                                  "to_dataframe_column_to_name(s)",
                                                  "new_distance_column_name",
                                                  "distance_units",
                                                  "distance_algorithm",
                                                  "elipsoid",
                                                  "Calculate</br>Dataframe</br>Distance",
                                                  "Clear","Return","Help"]

addr_df_dist_utility_input_typeList          =   ["select","text","select",
                                                  "text","select",
                                                  "text","select","select","select",
                                                  "button","button","button","button"]

addr_df_dist_utility_input_placeholderList   =  ["enter from dataframe",
                                                 "from df {lat,lng] column names - select from from_dataframe_column_name(s)",
                                                 "from dataframe column names",
                                                 "to {lat,lng] column names - select from to_dataframe_column_name(s)",
                                                 "to column names",
                                                 "enter column name to store distance(s) in",
                                                 "result in km - True : km, False : miles (default = True) ",
                                                 "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                 "select elipsoid (default = 'WGS-84') ",
                                                 None,None,None,None]

addr_df_dist_utility_input_reqList           =   [0,1,2,3,4,5,6,7,8]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoding Distance Forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

center_pt_input_title                   =   "Geocoding To latlnges"
center_pt_input_id                      =   "centerptform1id"
center_pt_1_input_id                      =   "centerpt1form1id"
center_pt_2_input_id                      =   "centerpt2form1id"

center_pt_input_idList                  =      ["centerpt1",
                                                 "centerpt2",
                                                 "centerpt3",
                                                 "centerpt4",
                                                 "centerpt5"]

center_pt_input_labelList             =     ["Latitude_Longitude",
                                                "Latitude_Longitude",
                                                "Latitude_Longitude",
                                                "Latitude_Longitude",
                                                "Latitude_Longitude"]


center_pt_input_typeList              =     ["text","text","text","text","text"]

center_pt_input_placeholderList       =     ["to latlng 1",
                                                "to latlng 2",
                                                "to latlng 3",
                                                "to latlng 4",
                                                "to latlng 5"]

center_pt_input_reqList             =   [0]


"""
#--------------------------------------------------------------------------
#    address center from df input form
#--------------------------------------------------------------------------
"""
addr_center_df_utility_input_title          =   "Address Center Point"
addr_center_df_utility_input_id             =   "addrdfcenter"
addr_center_df_utility_input_idList         =   ["centerdf",
                                                 "centerdflatlng",
                                                 "centerdfcols",
                                                 None,None,None,None]

addr_center_df_utility_input_labelList      =   ["dataframe_title",
                                                 "dataframe_column_to_get_center_point_for",
                                                 "dataframe_column_name(s)",
                                                 "Calculate</br>df Column</br>Center Point",
                                                 "Get</br>Locations</br>for Center Point",
                                                 "Return","Help"]

addr_center_df_utility_input_typeList       =   ["select","text","select",
                                                 "button","button","button","button"]

addr_center_df_utility_input_placeholderList =   ["select df to get lat,lng columns from",
                                                 "df [lat,lng] columns names - select from dataframe_column_name(s)",
                                                 "column names",
                                                 None,None,None,None]

addr_center_df_utility_input_reqList        =   [0,1,2]





"""
#--------------------------------------------------------------------------
#    dataframe distance from common location input form
#--------------------------------------------------------------------------
"""
df_dist_from_loc_utility_input_title                =   "Address Distance To Location"
df_dist_from_loc_utility_input_id                   =   "distancelocation"
df_dist_from_loc_utility_input_idList               =   ["commonlocation",
                                                         "todistancedf",
                                                         "todistlatlngs",
                                                         "todistcollist",
                                                         "newdistcolname",
                                                         "dfdisunits",
                                                         "dfdistalg",
                                                         "dfelipsoid",
                                                         None,None,None,None,None]

df_dist_from_loc_utility_input_labelList             =   ["common_user_location_for_calculating_distance_from",
                                                         "dataframe_for_calculating_distance(s)_to",
                                                         "distance_to_dataframe_column_name(s)",
                                                         "distance_to_dataframe_column_names_list",
                                                         "new_distance_column_name",
                                                         "distance_units",
                                                         "distance_algorithm",
                                                         "elipsoid",
                                                         "Calculate Distance</br>From</br>Location",
                                                         "Get Distance</br>From</br>Center Point",
                                                         "Get Distance</br>From Center</br>Point List",
                                                         "Return","Help"]

df_dist_from_loc_utility_input_typeList             =   ["text","select","text","select","text",
                                                         "select","select","select",
                                                         "button","button","button","button","button"]

df_dist_from_loc_utility_input_placeholderList      =   ["set common from location (address or coords)",
                                                         "df for to locations",
                                                         "lat, lng column names",
                                                         "column names list",
                                                         "new distance column name",
                                                         "result in km - True : km, False : miles (default = True) ",
                                                         "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                         "select elipsoid (default = 'WGS-84') ",
                                                          None,None,None,None,None]

df_dist_from_loc_utility_input_reqList           =      [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#    address dataframe center distance input form
#--------------------------------------------------------------------------
"""
df_dist_from_center_utility_input_title             =   "Address Distance To Center"
df_dist_from_center_utility_input_id                =   "distancecenter"
df_dist_from_center_utility_input_idList            =   ["todistancedf",
                                                         "todistlatlngs",
                                                         "todistcollist",
                                                         "centerpointdf",
                                                         "centerpointcol",
                                                         "cebterptcollist",
                                                         "newdistcolname",
                                                         "dfdisunits",
                                                         "dfdistalg",
                                                         "dfelipsoid",
                                                         None,None,None,None,None]

df_dist_from_center_utility_input_labelList         =   ["dataframe_for_calculating_distance(s)_to",
                                                         "column_name(s)_for_calculating_distance(s)_to",
                                                         "dataframe_for_calculating_distance(s)_to_column_names_list",
                                                         "dataframe_for_calculating_center_point",
                                                         "column_name_to_calculate_center_point",
                                                         "dataframe_for_calculating_center_points_from_column_names_list",
                                                         "new_distance_column_name",
                                                         "distance_units",
                                                         "distance_algorithm",
                                                         "elipsoid",
                                                         "Calculate Distance</br>From</br>Center Point",
                                                         "Define Distance</br>From</br>Location",
                                                         "Define Distance</br>From Closest</br>Location",
                                                         "Return","Help"]

df_dist_from_center_utility_input_typeList          =   ["select","text","select","select","text","select","text",
                                                         "select","select","select",
                                                         "button","button","button","button","button"]

df_dist_from_center_utility_input_placeholderList   =   ["df for to locations",
                                                         "lat, lng column names",
                                                         "column names list",
                                                         "df for center point",
                                                         "col for center point",
                                                         "column names list",
                                                         "new distance column name",
                                                         "result in km - True : km, False : miles (default = True) ",
                                                         "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                         "select elipsoid (default = 'WGS-84') ",
                                                          None,None,None,None,None]

df_dist_from_center_utility_input_reqList           =    [0,1,2,3]


"""
#--------------------------------------------------------------------------
#    address dataframe closest distance input form
#--------------------------------------------------------------------------
"""
df_dist_from_closest_utility_input_title             =   "Address Distance To Center"
df_dist_from_closest_utility_input_id                =   "distancecenter"
df_dist_from_closest_utility_input_idList            =   ["todistancedf",
                                                         "todistlatlngs",
                                                         "todistcollist",

                                                         "listpoints",
                                                         "listnames",

                                                         "listpointcolname",
                                                         "listdistvalue",
                                                         "listtitlecolname",

                                                         "dfdisunits",
                                                         "dfdistalg",
                                                         "dfelipsoid",

                                                         None,None,None,None,None]

df_dist_from_closest_utility_input_labelList         =   ["dataframe_for_calculating_distance(s)_to",
                                                         "column_name(s)_for_calculating_distance(s)_to",
                                                         "column_names_for_calculating_distance(s)_to_list",

                                                         "distance_list_points",
                                                         "distance_list_names",

                                                         "distance_values_column_name",
                                                         "distance_point_column_name",
                                                         "distance_title_column_name",

                                                         "distance_type",
                                                         "distance_units",
                                                         "distance_algorithm",
                                                         "elipsoid",

                                                         "Calculate Distance</br>From</br>Closest",
                                                         "Define Distance</br>From</br>Location",
                                                         "Define Distance</br>From</br>Center Point",
                                                         "Return","Help"]

df_dist_from_closest_utility_input_typeList          =   ["select","text","select", 
                                                          maketextarea(5),maketextarea(5),
                                                          "text","text","text",
                                                         "select","select","select","select",
                                                         "button","button","button","button","button"]

df_dist_from_closest_utility_input_placeholderList   =   ["df for to locations",
                                                         "lat, lng column names",
                                                         "column names list",

                                                         "geopoint list values"
                                                         "geopoint list title"

                                                         "distance value column name",
                                                         "distance geopoint value",
                                                         "distance geopoint title",

                                                         "distance type",
                                                         "result in km - True : km, False : miles (default = True) ",
                                                         "select algorithm - geodesic : great_circle (default = geodesic) ",
                                                         "select elipsoid (default = 'WGS-84') ",
                                                          None,None,None,None,None]

df_dist_from_closest_utility_input_reqList           =    [0,1,2,3]



"""
#--------------------------------------------------------------------------
#    location split input forms
#--------------------------------------------------------------------------
"""
dfc_split_column_utility_input_title         =   "Split Location Column"
dfc_split_column_utility_input_id            =   "splitloc"
dfc_split_column_utility_input_idList        =   ["splitlocdf",
                                                  "splitloccol",
                                                  "splitloccollist",
                                                  "splitloclatcol",
                                                  "splitloclngcol",
                                                  None,None,None]

dfc_split_column_utility_input_labelList     =   ["dataframe",
                                                  "split_column_name",
                                                  "column_names_list",
                                                  "new_split_Lat_column_name",
                                                  "new_split_Lng_column_name",
                                                  "Split</br>Lat_Lng</br>Column",
                                                  "Return","Help"]

dfc_split_column_utility_input_typeList      =   ["select","text","select","text","text",
                                                  "button","button","button"]

dfc_split_column_utility_input_placeholderList   =  ["enter from dataframe",
                                                 "lat_lng column name",
                                                 "dataframe column names",
                                                 "split lat column name",
                                                 "split lng column name",
                                                 None,None,None]

dfc_split_column_utility_input_reqList       =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#    location join input forms
#--------------------------------------------------------------------------
"""
dfc_join_column_utility_input_title         =   "Join Location Column"
dfc_join_column_utility_input_id            =   "splitloc"
dfc_join_column_utility_input_idList        =   ["joinlocdf",
                                                  "joinloccol",
                                                  "joinloccollist",
                                                  "splitloclatcol",
                                                  "splitloclngcol",
                                                  None,None,None]

dfc_join_column_utility_input_labelList     =   ["dataframe",
                                                  "join_lat_column_name",
                                                  "join_lat_column_names_list",
                                                  "join_lng_column_name",
                                                  "join_lng_column_names_list",
                                                  "new_join_Lng_column_name",
                                                  "Join</br>Lat Lng</br>Columns",
                                                  "Return","Help"]

dfc_join_column_utility_input_typeList      =   ["select","text","select","text","select","text",
                                                  "button","button","button"]

dfc_join_column_utility_input_placeholderList   =  ["enter from dataframe",
                                                 "lat column name",
                                                 "lat column names",
                                                 "lng column name",
                                                 "lng column names",
                                                 "join column name",
                                                 None,None,None]

dfc_join_column_utility_input_reqList       =   [0,1,2,3,4]




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Geocode Geocoders Table                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class GeocodersModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(GeocodersModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            #print("data model Qt.DisplayRole",row,column)
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)

class Geocoders_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   tblparms[0]
        self.bulk_flag          =   tblparms[1]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocoders_Table] : init",self.bulk_flag)

        self.init_tableview()

        self.doubleClicked.connect(self.select_geocoder) 


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table][reload_data] zipcode : ")

        tbldata    =   self.load_geocoder_data()
        self.model.reload_data(tbldata)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocoders_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        geocoders_data     =   self.load_geocoder_data()
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
           print("  [Geocoders_Table][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = GeocodersModel(geocoders_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
           print("  [Geocoders_Table][init_tableview] : model loaded")

        self.num_rows   =   len(geocoders_data)
        
        if(self.num_rows < 8) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (8 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(geocoders_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_geocoder_data(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocoders_Table][load_geocoders_data]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_list
        geocoders_list  =  get_geocoder_list(self.bulk_flag) 

        data    =   []

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocoders_Table][load_geocoders_data] geocoders_list : \n    ",geocoders_list)

        for i in range(len(geocoders_list)) :
                
            data_row    =   []
            data_row.append(geocoders_list[i])
            data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocoders_Table][dump] : data")
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

        self.column_headers     =   ["Geocoder"]
        self.column_widths      =   [200]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table][end load]")

        return(data)
    
    def select_geocoder(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table][select_geocoder]")

        row_number      =   None
        column_number   =   None

        for idx in self.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table][select_geocoder] ",row_number,column_number)

        model   =   self.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocoders_Table][select_geocoder] ",cell)

        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_id, set_current_geocoder_id

        geocoder_id  =  get_geocoder_id(cell) 
        set_current_geocoder_id(geocoder_id)
        
        self.parent.display_select_geocoder(self.bulk_flag,geocoder_id)

def get_geocoder_connector_form(geocoder_id,button_methods) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        print("    [get_geocoder_connector_form]",geocoder_id)
   
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId,BingId,GoogleId,OpenMapQuestId, NominatimId, get_geocoder_title)
    
    if(geocoder_id == ArcGISId) :
        form_parms      =   [arcgis_geocoder_id,arcgis_geocoder_idList,arcgis_geocoder_labelList,arcgis_geocoder_typeList,arcgis_geocoder_placeholderList,arcgis_geocoder_reqList]
    elif(geocoder_id == BingId) :
        form_parms      =   [bing_geocoder_id,bing_geocoder_idList,bing_geocoder_labelList,bing_geocoder_typeList,bing_geocoder_placeholderList,bing_geocoder_reqList]
    elif(geocoder_id == GoogleId) :
        form_parms      =   [google_geocoder_id,google_geocoder_idList,google_geocoder_labelList,google_geocoder_typeList,google_geocoder_placeholderList,google_geocoder_reqList]
    elif(geocoder_id == NominatimId) :
        form_parms      =   [nomin_geocoder_id,nomin_geocoder_idList,nomin_geocoder_labelList,nomin_geocoder_typeList,nomin_geocoder_placeholderList,nomin_geocoder_reqList]
    elif(geocoder_id == OpenMapQuestId) :
        form_parms      =   [mapquest_geocoder_id,mapquest_geocoder_idList,mapquest_geocoder_labelList,mapquest_geocoder_typeList,mapquest_geocoder_placeholderList,mapquest_geocoder_reqList]
    else :

        geocoder_id = BingId
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id, get_geocoder_parms, set_current_geocoder_id, BingId
        
        set_current_geocoder_id(geocoder_id)
        form_parms      =   [bing_geocoder_id,bing_geocoder_idList,bing_geocoder_labelList,bing_geocoder_typeList,bing_geocoder_placeholderList,bing_geocoder_reqList]

    geocoder_title  =   get_geocoder_title(geocoder_id)  

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        print("    [get_geocoder_connector_form][geocoder_title]",geocoder_title)

    comboMethods    =   None
    comboList       =   None
    file_methods    =   None
    button_methods  =   [button_methods[0],button_methods[1],button_methods[2],button_methods[3],button_methods[4],button_methods[5],button_methods[6]]
    cfg_parms       =   None
    form_title      =   "\n" + geocoder_title + " Geocoder Connector Parms\n"
    form_width      =   800

    form_parms.append(comboList)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)        

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    geocode_connector_form    =   dfcleanser_input_form_Widget(form_parms)

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        print("    [get_geocoder_connector_form] form built",geocoder_id)

    return(geocode_connector_form)

class Geocode_connector_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget]")

        super().__init__()

        self.parent         =   dfparms[0]
        self.bulk_flag      =   dfparms[1]
        self.geocoder_id    =   dfparms[2]
        self.callbacks      =   dfparms[3]

        self.geocoder_connector_form    =   None

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget] end")

    def reload_data(self,parent,bulkflag,geocid) :
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget][reload_data] ")

        self.parent         =   parent
        self.bulk_flag      =   bulkflag
        self.geocoder_id    =   geocid

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget][reload_data][end] ",self.bulk_flag,self.geocoder_id)
        

    def build_connector_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_connector_form_Widget][build_connector_form] ",self.bulk_flag,self.geocoder_id)

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        new_geocoder_connector_form    =   get_geocoder_connector_form(self.geocoder_id,self.callbacks)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id, get_geocoder_parms, set_current_geocoder_id, BingId
        geocoderid  =   get_current_geocoder_id()
        
        if(geocoderid is None) :
            set_current_geocoder_id(BingId)
            geocoderid  =   BingId

        geocoder_parms  =   get_geocoder_parms(geocoderid)
        parm_count      =   new_geocoder_connector_form.get_form_fields_count()

        for i in range(parm_count) :
            new_geocoder_connector_form.set_form_input_value_by_index(i,geocoder_parms[i])

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_connector_form_Widget][build_connector_form] geocoder_parms : \n    ",geocoder_parms)

        return(new_geocoder_connector_form)

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_connector_form_Widget][init_form] ",self.bulk_flag,self.geocoder_id)

        self.geocoder_connector_form    =   self.build_connector_form()


        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.geocodeconnectorLayout     =   QVBoxLayout()
        self.geocodeconnectorLayout.addWidget(self.geocoder_connector_form)
        self.geocodeconnectorLayout.addStretch()

        self.setLayout(self.geocodeconnectorLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_connector_form_Widget][init_form] end")

class Geoocoder_Connector_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget]")

        super().__init__()

        self.parent         =   dfparms[0]
        self.bulk_flag      =   dfparms[1]
        self.geocoder_id    =   dfparms[2]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget] end")

    def reload_data(self,parent,bulkflag,geocoderid) :

        self.parent         =   parent
        self.bulk_flag      =   bulkflag
        self.geocoder_id    =   geocoderid
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget][reload_data] ",self.bulk_flag,self.geocoder_id)

        self.geocoder_connector_callbacks   =   [self.test_geocoder_connector,self.interactive_geocoding,self.interactive_reverse_geocoding,self.bulk_geoocooding,self.clear_form,self.geocode_connector_return,self.geocoder_connector_help]
        parms   =   [self.parent,self.bulk_flag,self.geocoder_id,self.geocoder_connector_callbacks]
        self.geocode_connect_parms_form     =   Geocode_connector_form_Widget(parms)

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geoocoder_Connector_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

        self.geocoder_connector_callbacks   =   [self.test_geocoder_connector,self.interactive_geocoding,self.interactive_reverse_geocoding,self.bulk_geoocooding,self.clear_form,self.geocode_connector_return,self.geocoder_connector_help]
        parms   =   [self.parent,self.bulk_flag,self.geocoder_id,self.geocoder_connector_callbacks]
        self.geocode_connect_parms_form     =   Geocode_connector_form_Widget(parms)
        self.geocode_connect_parms_form.setFixedWidth(800)

        tblparms   =   [self.parent,self.bulk_flag]       
        self.geocoders_table   =    Geocoders_Table(tblparms)

        if(self.geocoders_table.num_rows < 6) :
            new_height  =   35 + (self.geocoders_table.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (6 * DEFAULT_ROW_HEIGHT)
        
        self.geocoders_table.setMinimumHeight(new_height)
        self.geocoders_table.setMaximumHeight(new_height)
        self.geocoders_table.setFixedWidth(200)

        self.geocoders_tableLayout  =   QVBoxLayout()
        
        from PyQt5.QtWidgets import QLabel
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        note_label   =   QLabel()
        note_label.setText("\nDouble Click on Geocoder to select.")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")


        self.geocoders_tableLayout.addWidget(spacer_label)
        self.geocoders_tableLayout.addWidget(self.geocoders_table)
        self.geocoders_tableLayout.addWidget(note_label)
        self.geocoders_tableLayout.addStretch()
        self.geocoders_tableLayout.setAlignment(Qt.AlignTop)

        self.geocoders_form_layout  =   QVBoxLayout()
        self.geocoders_form_layout.addWidget(self.geocode_connect_parms_form)
        self.geocoders_form_layout.setAlignment(Qt.AlignTop)
         
        self.geocoderLayout     =   QHBoxLayout()
        self.geocoderLayout.addLayout(self.geocoders_tableLayout) 
        self.geocoderLayout.addLayout(self.geocoders_form_layout)       
        self.geocoderLayout.setAlignment(Qt.AlignTop)

        self.setLayout(self.geocoderLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_connector_form_Widget][init_form] end")
    
    def test_geocoder_connector(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("[Geoocoder_Connector_Widget][test_geocoder_connector] \n  ",type(self.geocode_connect_parms_form.geocoder_connector_form))

        total_parms             =   self.geocode_connect_parms_form.geocoder_connector_form.get_form_fields_count()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("[Geoocoder_Connector_Widget][test_geocoder_connector] total_parms  ",total_parms)

        geocode_connect_parms   =   []

        for i in range(total_parms) :
            geocode_connect_parms.append(self.geocode_connect_parms_form.geocoder_connector_form.get_form_input_value_by_index(i))

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget][test_geocoder_connector] gcparms : \n  ",geocode_connect_parms)

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import test_geocoder
        opstat  =   test_geocoder(self.geocoder_id, geocode_connect_parms)

        if(opstat.get_status()) :

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId, BingId, BaiduId,  GoogleId, OpenMapQuestId, NominatimId, set_current_geocoder_id)
            from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (arcgis_geocoder_id, bing_geocoder_id, baidu_geocoder_id, google_geocoder_id, mapquest_geocoder_id, nomin_geocoder_id)


            if(self.geocoder_id == ArcGISId)          :   form = arcgis_geocoder_id
            elif(self.geocoder_id == BingId)          :   form = bing_geocoder_id
            elif(self.geocoder_id == BaiduId)         :   form = baidu_geocoder_id
            elif(self.geocoder_id == GoogleId)        :   form = google_geocoder_id
            elif(self.geocoder_id == OpenMapQuestId)  :   form = mapquest_geocoder_id
            elif(self.geocoder_id == NominatimId)     :   form = nomin_geocoder_id

            cfg.set_config_value(form+"Parms",geocode_connect_parms)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[test_geocoder_connector] geocoder connector connected"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            set_current_geocoder_id(self.geocoder_id)

    def interactive_geocoding(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget][interactive_geocoding]")
       
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        self.parent.display_interactive_geocoding(QUERY)

    def interactive_reverse_geocoding(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_connector_form_Widget][interactive_reverse_geocoding]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import REVERSE
        self.parent.display_interactive_geocoding(REVERSE)

    def bulk_geoocooding(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget][bulk_geoocooding]")
    
    def clear_form(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_connector_form_Widget]clear_form]")

    def geocode_connector_return(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Connector_Widget][geocode_connector_return]")

        self.parent.init_geocode()

    def geocoder_connector_help(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_connector_form_Widget][geocoder_connector_help]")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Geocode Geocoders Table end                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Geocoder Connector Table                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class GeocodeGeocodingModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(GeocodeGeocodingModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            #print("data model Qt.DisplayRole",row,column)
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)

class Geocode_Geocoding_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   tblparms[0]
        self.geocoder_id        =   tblparms[1]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Geocoding_Table : init",self.geocoder_id)

        self.init_tableview()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Connector_Table][reload_data] : ")

        tbldata    =   self.load_geocode_geocoding_data()
        self.model.reload_data(tbldata)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        geocode_geocoding_data     =   self.load_geocode_geocoding_data()
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
           print("  [Geocode_Geocoding_Table][init_tableview] : headers",self.column_headers)

        if(self.model is None) :
            self.model = GeocodeGeocodingModel(geocode_geocoding_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
           print("  [Geocode_Geocoding_Table][init_tableview] : model loaded")

        self.num_rows   =   len(geocode_geocoding_data)
        
        if(self.num_rows < 8) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (8 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(geocode_geocoding_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_geocode_geocoding_data(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Table][load_geocode_geocoding_data]")

        import dfcleanser.Qt.utils.Geocode.GeocodeWidgets as gcw  
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import  (ArcGISId, BingId, GoogleId, OpenMapQuestId, NominatimId, BaiduId)

        if(self.geocoder_id == ArcGISId)              :   
            form        =   arcgis_geocoder_id
            labellist   =   arcgis_geocoder_labelList 
        elif(self.geocoder_id == BingId)              :   
            form        =   bing_geocoder_id
            labellist   =   bing_geocoder_labelList
        elif(self.geocoder_id == GoogleId)            :   
            form        =   google_geocoder_id
            labellist   =   google_geocoder_labelList
        elif(self.geocoder_id == OpenMapQuestId)      :   
            form        =   mapquest_geocoder_id
            labellist   =   mapquest_geocoder_labelList
        elif(self.geocoder_id == NominatimId)         :   
            form        =   nomin_geocoder_id
            labellist   =   nomin_geocoder_labelList
        elif(self.geocoder_id == BaiduId)             :   
            form        =   baidu_geocoder_id
            labellist   =   nomin_geocoder_labelList

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_parms
        connect_parms   =   get_geocoder_parms(self.geocoder_id)
        connect_labels  =   labellist
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_Table][load_geocode_geocoding_data] : ",self.geocoder_id," \n  ",connect_parms,"\n  ",connect_labels)

        data    =   []

        data_row    =   []
        data_row.append("Geocoder")
        data.append(data_row)

        data_row    =   []
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_title
        gtitle  =   get_geocoder_title(self.geocoder_id)
        data_row.append("  " + gtitle)
        data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_Table][lload_geocode_geocoding_data] connect_parms : \n    ",connect_parms)

        for i in range(len(connect_parms)) :
                
            data_row    =   []

            if(len(connect_parms[i]) > 0) :
                data_row.append(connect_labels[i])
                data.append(data_row)
                data_row    =   []
                data_row.append("  " + connect_parms[i])
                data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_Table][dump] : data")
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

        self.column_headers     =   ["Geocode Connector Parms"]
        self.column_widths      =   [180]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("[Geocode_Geocoding_Table][end load]")

        return(data)


def get_geocoding_query_form(geocoder_id,button_methods) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        print("    [get_geocoder_query_form]",geocoder_id)
   
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId,BingId,GoogleId,OpenMapQuestId, NominatimId, get_geocoder_title)
    
    selectDicts     =   []

    if(geocoder_id == ArcGISId) :
        
        form_parms      =   [arcgis_query_id,arcgis_query_idList,arcgis_query_labelList,arcgis_query_typeList,arcgis_query_placeholderList,arcgis_query_reqList]
        comboList       =   None
        comboMethods    =   None

    elif(geocoder_id == BingId) :
        
        form_parms      =   [bing_query_id,bing_query_idList,bing_query_labelList,bing_query_typeList,bing_query_placeholderList,bing_query_reqList]

        from dfcleanser.sw_utilities.DFCDataStores import get_formatted_country_codes
        countries       =   get_formatted_country_codes()
        ccsel           =   {"default":countries[0],"list":countries}
        selectDicts.append(ccsel)

        bingsel         =   {"default":"False","list":["True","False"]}
        selectDicts.append(bingsel)
        bingsel1        =   {"default":"False","list":["True","False"]}
        selectDicts.append(bingsel1)
    
        comboList       =   selectDicts
        comboMethods    =   [None,None,None]

    elif(geocoder_id == GoogleId) :

        form_parms      =   [google_query_id,google_query_idList,google_query_labelList,google_query_typeList,google_query_placeholderList,google_query_reqList]
    

        from dfcleanser.sw_utilities.DFCDataStores import get_formatted_country_codes
        countries       =   get_formatted_country_codes()
        ccsel           =   {"default":countries[0],"list":countries}
        selectDicts.append(ccsel)

            
        # get google languages
        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
        langs           =   get_Dict("Language_Codes")
        langs_keys      =   []

        if(not (langs is None)) :

            lngs            =   list(langs.keys())
            lngs.sort()
            for i in range(len(lngs)) :
                langs_keys.append(lngs[i])  

        else :
            langs_keys.append("English") 

        langssel       =   {"default":"English","list":langs_keys}
        selectDicts.append(langssel)
            
        # set google sensor
        googsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(googsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None,None,None] 

    elif(geocoder_id == NominatimId) :

        form_parms      =   [nomin_query_id,nomin_query_idList,nomin_query_labelList,nomin_query_typeList,nomin_query_placeholderList,nomin_query_reqList]
           
        nonimsel          =   {"default":"False","list":["True","False"]}
        selectDicts.append(nonimsel)
        comboList   =   selectDicts
        comboMethods    =   [None]
    
    elif(geocoder_id == OpenMapQuestId) :
        
        form_parms      =   [mapquest_query_id,mapquest_query_idList,mapquest_query_labelList,mapquest_query_typeList,mapquest_query_placeholderList,mapquest_query_reqList]
        comboList       =   None
        comboMethods    =   None

    else :

        geocoder_id = BingId
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id, get_geocoder_parms, set_current_geocoder_id, BingId
        
        set_current_geocoder_id(geocoder_id)
        form_parms      =   [bing_query_id,bing_query_idList,bing_query_labelList,bing_query_typeList,bing_query_placeholderList,bing_query_reqList]

    geocoder_title  =   get_geocoder_title(geocoder_id)  

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        print("    [get_geocoder_query_form][geocoder_title]",geocoder_title)

    file_methods    =   None
    button_methods  =   [button_methods[0],button_methods[1],button_methods[2],button_methods[3]]
    cfg_parms       =   None
    form_title      =   "\n" + geocoder_title + " Geocode Query Parms\n"
    form_width      =   570

    form_parms.append(comboList)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)  

    #print("cfg_parms",cfg_parms)      

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget, SMALL
    if(geocoder_id == GoogleId) :
        geocode_query_form    =   dfcleanser_input_form_Widget(form_parms,SMALL)
    else :
        geocode_query_form    =   dfcleanser_input_form_Widget(form_parms)

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        print("    [get_geocoder_query_form] form built",geocoder_id)

    return(geocode_query_form)


def get_geocoding_reverse_form(geocoder_id,button_methods) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        print("    [get_geocoder_reverse_form]",geocoder_id)
   
    selectDicts     =   []

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId,BingId,GoogleId,OpenMapQuestId, NominatimId, get_geocoder_title)
    
    if(geocoder_id == ArcGISId) :
        form_parms      =   [arcgis_reverse_id,arcgis_reverse_idList,arcgis_reverse_labelList,arcgis_reverse_typeList,arcgis_reverse_placeholderList,arcgis_reverse_reqList]

        comboList       =   None
        comboMethods    =   None

    elif(geocoder_id == BingId) :
        form_parms      =   [bing_reverse_id,bing_reverse_idList,bing_reverse_labelList,bing_reverse_typeList,bing_reverse_placeholderList,bing_reverse_reqList]
        
        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
        country_codes   =   get_Dict("Country_Codes")
        cc_keys         =   list(country_codes.keys())
        cc_keys.sort()
        ccsel           =   {"default":"'United States'","list":cc_keys}
        selectDicts.append(ccsel)

        bingsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(bingsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None,None]

    elif(geocoder_id == GoogleId) :
        form_parms      =   [google_reverse_id,google_reverse_idList,google_reverse_labelList,google_reverse_typeList,google_reverse_placeholderList,google_reverse_reqList]
           
        from dfcleanser.sw_utilities.DFCDataStores import get_Dict

        # get google languages
        langs           =   get_Dict("Language_Codes")
        langs_keys      =   []

        if(not (langs is None)) :

            lngs            =   list(langs.keys())
            lngs.sort()
            for i in range(len(lngs)) :
                langs_keys.append(lngs[i])  

        else :
            langs_keys.append("English") 

        langssel       =   {"default":"English","list":langs_keys}
        selectDicts.append(langssel)
            
        # set google sensor
        googsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(googsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None,None] 
    
    elif(geocoder_id == NominatimId) :
        form_parms      =   [nomin_reverse_id,nomin_reverse_idList,nomin_reverse_labelList,nomin_reverse_typeList,nomin_reverse_placeholderList,nomin_reverse_reqList]
    
        # addr details
        addrsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(addrsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None] 
     
    elif(geocoder_id == OpenMapQuestId) :
        form_parms      =   [mapquest_reverse_id,mapquest_reverse_idList,mapquest_reverse_labelList,mapquest_reverse_typeList,mapquest_reverse_placeholderList,mapquest_reverse_reqList]
        
        # addr details
        addrsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(addrsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None] 
     
    else :

        geocoder_id = BingId
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id, get_geocoder_parms, set_current_geocoder_id, BingId
        
        set_current_geocoder_id(geocoder_id)
        form_parms      =   [bing_reverse_id,bing_reverse_idList,bing_reverse_labelList,bing_reverse_typeList,bing_reverse_placeholderList,bing_reverse_reqList]

        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
        country_codes   =   get_Dict("Country_Codes")
        cc_keys         =   list(country_codes.keys())
        cc_keys.sort()
        ccsel           =   {"default":"'United States'","list":cc_keys}
        selectDicts.append(ccsel)

        bingsel           =   {"default":"False","list":["True","False"]}
        selectDicts.append(bingsel)
    
        comboList       =   selectDicts
        comboMethods    =   [None,None]


    geocoder_title  =   get_geocoder_title(geocoder_id)  

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        print("    [get_geocoder_reverse_form][geocoder_title]",geocoder_title)

    file_methods    =   None
    button_methods  =   [button_methods[0],button_methods[1],button_methods[2],button_methods[3]]
    cfg_parms       =   None
    form_title      =   "\n" + geocoder_title + " Geocode Reverse Parms\n"
    form_width      =   800

    form_parms.append(comboList)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)        

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    geocode_reverse_form    =   dfcleanser_input_form_Widget(form_parms)

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        print("    [get_geocoder_reverse_form] form built",geocoder_id)

    return(geocode_reverse_form)


class Geocode_Geocoding_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_form_Widget]")

        super().__init__()

        self.parent         =   dfparms[0]
        self.geocode_mode   =   dfparms[1]
        self.geocoder_id    =   dfparms[2]
        self.callbacks      =   dfparms[3]

        self.geocoder_connector_form    =   None

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget] end")

    def reload_data(self,parent,geocode_mode,geocid) :
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_connector_form_Widget][reload_data] ")

        self.parent         =   parent
        self.geocode_mode   =   geocode_mode
        self.geocoder_id    =   geocid

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_geocoding_form_Widget][reload_data][end] ",self.geocode_mode,self.geocoder_id)
        

    def build_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_form_Widget][build_form] ",self.geocode_mode,self.geocoder_id)

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        if(self.geocode_mode == QUERY) :
            new_geocoder_query_form     =   get_geocoding_query_form(self.geocoder_id,self.callbacks)
            new_geocoder_query_form.resize(570,800)
            #new_geocoder_query_form.setFixedHeight(800)

            print("type new_geocoder_query_form",type(new_geocoder_query_form))
        else :
            new_geocoder_reverse_form   =   get_geocoding_reverse_form(self.geocoder_id,self.callbacks)            

        if(self.geocode_mode == QUERY) :

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_query_parms
            stored_parms    =   get_geocoder_query_parms(self.geocoder_id)
            parm_count      =   new_geocoder_query_form.get_form_fields_count()
            
            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
                print("  [Geocode_Geocoding_form_Widget][parm_count] ",parm_count)

        else :

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_reverse_parms
            stored_parms    =   get_geocoder_reverse_parms(self.geocoder_id)
            parm_count      =   new_geocoder_reverse_form.get_form_fields_count()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_form_Widget][stored_parms] ",stored_parms)

        if(not (stored_parms is None)) :
            for i in range(parm_count) :
                if(self.geocode_mode == QUERY) :
                    new_geocoder_query_form.set_form_input_value_by_index(i,stored_parms[i])
                else :
                    new_geocoder_reverse_form.set_form_input_value_by_index(i,stored_parms[i])

        else :

            if(self.geocode_mode == QUERY) :

                new_geocoder_query_form.set_form_input_value_by_index(5,str(1))
                new_geocoder_query_form.set_form_input_value_by_index(6,str(20))
                
            else :
 
                new_geocoder_reverse_form.set_form_input_value_by_index(5,str(1))
                new_geocoder_reverse_form.set_form_input_value_by_index(6,str(20))

                import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm
                if(self.geocoder_id  == gcm.BingId) :
                    new_geocoder_reverse_form.set_form_input_value_by_index(7,"United States")    


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_geocoding_form_Widget][build_form] geocoder_parms : \n    ",stored_parms)

        if(self.geocode_mode == QUERY) :
            return(new_geocoder_query_form)
        else :
            return(new_geocoder_reverse_form)
        

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_form_Widget][init_form] ",self.geocode_mode,self.geocoder_id)

        from PyQt5.QtWidgets import QScrollArea
        self.scroll     =   QScrollArea()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.geocoder_geocoding_form    =   self.build_form()
        self.geocoder_geocoding_form.setFixedWidth(770)


        self.scroll.setWidget(self.geocoder_geocoding_form)
        self.scroll.setFixedHeight(600)

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.geocodeconnectorLayout     =   QVBoxLayout()
        self.geocodeconnectorLayout.addWidget(self.scroll)
        self.geocodeconnectorLayout.addStretch()

        self.setLayout(self.geocodeconnectorLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_form_Widget][init_form] end")


class Geoocoder_Geocoding_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget]")

        super().__init__()

        self.parent         =   dfparms[0]
        self.geocode_mode   =   dfparms[1]
        self.geocoder_id    =   dfparms[2]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget] end")

    def reload_data(self,parent,mode,geocoderid) :

        self.parent         =   parent
        self.geocode_mode   =   mode
        self.geocoder_id    =   geocoderid
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reload_data] ",self.geocode_mode,self.geocoder_id)

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Geocoding_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        if(self.geocode_mode == QUERY) :
            
            self.geocoder_query_callbacks   =   [self.query_request,self.clear_query_form,self.query_return,self.query_help]
            parms   =   [self.parent,self.geocode_mode,self.geocoder_id,self.geocoder_query_callbacks]
            self.geocode_geocoding_parms_form     =   Geocode_Geocoding_form_Widget(parms)
            self.geocode_geocoding_parms_form.setFixedWidth(800)
        
        else :

            self.geocoder_reverse_callbacks   =   [self.reverse_request,self.clear_reverse_form,self.reverse_return,self.reverse_help]
            parms   =   [self.parent,self.geocode_mode,self.geocoder_id,self.geocoder_reverse_callbacks]
            self.geocode_geocoding_parms_form     =   Geocode_Geocoding_form_Widget(parms)
            self.geocode_geocoding_parms_form.setFixedWidth(800)

        tblparms   =   [self.parent,self.geocoder_id]       
        self.geocode_connector_table   =    Geocode_Geocoding_Table(tblparms)

        if(self.geocode_connector_table.num_rows < 15) :
            new_height  =   35 + (self.geocode_connector_table.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (15 * DEFAULT_ROW_HEIGHT)
        
        self.geocode_connector_table.setMinimumHeight(new_height)
        self.geocode_connector_table.setMaximumHeight(new_height)
        self.geocode_connector_table.setFixedWidth(180)
        
        from PyQt5.QtWidgets import QLabel
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        note_label   =   QLabel()
        note_label.setText("\nDouble Click on Geocoder to select.")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        self.geocoders_tableLayout  =   QVBoxLayout()
        self.geocoders_tableLayout.addWidget(spacer_label)
        self.geocoders_tableLayout.addWidget(self.geocode_connector_table)
        self.geocoders_tableLayout.addStretch()
        self.geocoders_tableLayout.setAlignment(Qt.AlignTop)

        self.geocoders_form_layout  =   QVBoxLayout()
        self.geocoders_form_layout.addWidget(self.geocode_geocoding_parms_form)
        self.geocoders_form_layout.setAlignment(Qt.AlignTop)
         
        self.geocoderLayout     =   QHBoxLayout()
        self.geocoderLayout.addLayout(self.geocoders_tableLayout) 
        self.geocoderLayout.addLayout(self.geocoders_form_layout)       
        self.geocoderLayout.setAlignment(Qt.AlignTop)

        self.setLayout(self.geocoderLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Geocoding_Widget][init_form] end")

    def query_request(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geoocoder_Geocoding_Widget][query_request] \n  ")

        query_parms_count   =   self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_fields_count()
        query_parms         =  []

        for i in range(query_parms_count) :
            query_parms.append(self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_input_value_by_index(i))

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import run_geocoder_query
        query_results   =   run_geocoder_query(self.geocoder_id, query_parms)

        if(not(query_results is None)) :

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_form_id, QUERY
            cfg_key = get_form_id(self.geocoder_id,QUERY) + "Parms"

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
                print(cfg_key,query_parms)

            from dfcleanser.common.cfg import set_config_value
            set_config_value(cfg_key,query_parms)

            self.parent.display_geocoding_data(self.geocode_mode,query_results)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][query_request] \n  ",query_results)

    def clear_query_form(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][clear_query_form] \n  ")

        query_parms_count   =   self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_fields_count()
        for i in range(query_parms_count) :
            self.geocode_geocoding_parms_form.geocoder_geocoding_form.set_form_input_value_by_index(i,"")

    def query_return(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][query_return] \n  ")

        self.parent.init_geocode()

    def query_help(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][query_help] \n  ")

    def reverse_request(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reverse_request] \n  ")

        reverse_parms_count   =   self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_fields_count()
        reverse_parms         =  []

        for i in range(reverse_parms_count) :
            reverse_parms.append(self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_input_value_by_index(i))
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reverse_request]  reverse_parms ",reverse_parms)

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import run_geocoder_reverse
        reverse_results   =   run_geocoder_reverse(self.geocoder_id, reverse_parms)

        if(not(reverse_results is None)) :

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
                print("[Geoocoder_Geocoding_Widget][reverse_request] \n  ",reverse_results)

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_form_id, REVERSE
            cfg_key = get_form_id(self.geocoder_id,REVERSE) + "Parms"

            from dfcleanser.common.cfg import set_config_value
            set_config_value(cfg_key,reverse_parms)

            self.parent.display_geocoding_data(self.geocode_mode,reverse_results)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reverse_request] \n  ",reverse_results)

    def clear_reverse_form(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][clear_reverse_form] \n  ")

        query_parms_count   =   self.geocode_geocoding_parms_form.geocoder_geocoding_form.get_form_fields_count()
        for i in range(query_parms_count) :
            self.geocode_geocoding_parms_form.geocoder_geocoding_form.set_form_input_value_by_index(i,"")

    def reverse_return(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reverse_return] \n  ")

        self.parent.init_geocode()#self.parent.display_select_geocoder(False,geocoderid=self.geocoder_id)

    def reverse_help(self) :
 
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Widget][reverse_help] \n  ")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           Geocoder Geocoding Results Table                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class GeocodeGeocodingResultsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(GeocodeGeocodingResultsModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            #print("data model Qt.DisplayRole",row,column)
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignCenter)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)

class Geocode_Geocoding_Results_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   tblparms[0]
        self.geocoder_type      =   tblparms[1]
        self.geocoding_results  =   tblparms[2]


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Geocoding_Results_Table : init",self.geocoder_type)
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Geocoding_Results_Table : results\n  ",self.geocoding_results)


        self.init_tableview()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,parent,geocode_type,results):
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][reload_data] : ")
        
        self.parent             =   parent
        self.geocoder_type      =   geocode_type
        self.geocoding_results  =   results

        tbldata    =   self.load_geocode_results_data()
        self.model.reload_data(tbldata)

        self.num_rows   =   len(tbldata)
        
        if(self.num_rows <15) :
            new_height  =   25 + ((self.num_rows) * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        geocode_geocoding_results_data     =   self.load_geocode_results_data()
        
        if(self.model is None) :
            self.model = GeocodeGeocodingModel(geocode_geocoding_results_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
           print("  [Geocode_Geocoding_Results_Table][init_tableview] : model loaded")

        self.num_rows   =   len(geocode_geocoding_results_data)
        
        if(self.num_rows <15) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(geocode_geocoding_results_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)



    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_query_data(self,geocoding_results,data):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][load_query_data]")
            print("  [Geocode_Geocoding_Results_Table][load_query_data] results : \n    ",geocoding_results)

        for i in range(len(geocoding_results)) :

            data_row    =   []
        
            data_row.append(geocoding_results[i][0])
            data_row.append(geocoding_results[i][1])
            data_row.append(geocoding_results[i][2])
            data_row.append(geocoding_results[i][3])
 
            data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Geocoding_Results_Table][dump] : data")
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

        column_headers     =   ["User Coords","Geocoder Address","Latitude","Longitude"]
        column_widths      =   [250,410,90,90]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Geocoding_Results_Table][end load]")

        return([column_headers,column_widths])

    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_reverse_data(self,geocoding_results,data):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][load_reverse_data]")
            print("  [Geocode_Geocoding_Results_Table][load_reverse_data] results : \n    ",geocoding_results)

        for i in range(len(geocoding_results)) :
                
            data_row    =   []
        
            data_row.append(geocoding_results[i][0])
            data_row.append(geocoding_results[i][1])
            data_row.append(geocoding_results[i][2])
            data_row.append(geocoding_results[i][3])
 
            data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][dump] : data")
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

        column_headers     =   ["User Coords","Geocoder Address","Latitude","Longitude"]
        column_widths      =   [195,385,100,100]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Geocoding_Results_Table][end load]")

        return([column_headers,column_widths])



    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_geocode_results_data(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Geocoding_Results_Table][load_geocode_results_data]")
            print("  [Geocode_Geocoding_Results_Table][load_geocode_results_data]         \n",self.geocoding_results)

        data    =   []

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        if(self.geocoder_type == QUERY) :
            
            table_sizing            =   self.load_query_data(self.geocoding_results,data)
            self.column_headers     =   table_sizing[0]
            self.column_widths      =   table_sizing[1]

        else :

            table_sizing            =   self.load_reverse_data(self.geocoding_results,data)
            self.column_headers     =   table_sizing[0]
            self.column_widths      =   table_sizing[1]


        return(data)


class Geoocoder_Geocoding_Results_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Results_Widget]")

        super().__init__()

        self.parent             =   dfparms[0]
        self.geocode_mode       =   dfparms[1]
        self.geocoding_results  =   dfparms[2]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Results_Widget] end")

    def reload_data(self,parent,mode,results) :

        self.parent             =   parent
        self.geocode_mode       =   mode
        self.geocoding_results  =   results
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Results_Widget][reload_data] ",self.geocode_mode)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        if(self.geocode_mode == QUERY) :
            self.geocode_geocoding_query_results.reload_data(self.parent,self.geocode_mode,self.geocoding_results)  
        else :
            self.geocode_geocoding_reverse_results.reload_data(self.parent,self.geocode_mode,self.geocoding_results)   

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Geocoding_Results_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        if(self.geocode_mode == QUERY) :
            
            parms   =   [self.parent,self.geocode_mode,self.geocoding_results]
            self.geocode_geocoding_query_results     =   Geocode_Geocoding_Results_Table(parms)
            self.geocode_geocoding_query_results.setFixedWidth(850)
        
        else :

            parms   =   [self.parent,self.geocode_mode,self.geocoding_results]
            self.geocode_geocoding_reverse_results     =   Geocode_Geocoding_Results_Table(parms)
            self.geocode_geocoding_reverse_results.setFixedWidth(800)

        self.geocoding_results_tableLayout  =   QVBoxLayout()
        
        if(self.geocode_mode == QUERY) :
            title_msg   =   "Geocoding Query Results"
        else :
            title_msg   =   "Geocoding Reverse Results"

        from PyQt5.QtWidgets import QLabel
        title_label   =   QLabel()
        title_label.setText("\n\n" + title_msg + "\n")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.geocoding_results_tableLayout.addWidget(title_label)

        if(self.geocode_mode == QUERY) :
            self.geocoding_results_tableLayout.addWidget(self.geocode_geocoding_query_results)
        else :
            self.geocoding_results_tableLayout.addWidget(self.geocode_geocoding_reverse_results) 

        spacer_label   =   QLabel()
        spacer_label.setText("\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.geocoding_results_tableLayout.addWidget(spacer_label)


        from PyQt5.QtWidgets import QPushButton
        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_results) 

        self.geocoding_results_tableLayout.addWidget(return_button,alignment=Qt.AlignHCenter)

        self.geocoding_results_tableLayout.addStretch()
        self.geocoding_results_tableLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.geocoding_results_tableLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Geocoding_Results_Widget][init_form] end")

    def return_from_results(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Geocoding_Results_Widget][return_from_results]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY, REVERSE
        if(self.geocode_mode == QUERY) :
            self.parent.display_interactive_geocoding(QUERY)
        else :
            self.parent.display_interactive_geocoding(REVERSE)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Geocoder Distance Results Table                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class GeocodeDistanceResultsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(GeocodeDistanceResultsModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            #print("data model Qt.DisplayRole",row,column)
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignCenter)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)
    

class Geocode_Distance_Results_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   tblparms[0]
        self.distance_type      =   tblparms[1]
        self.distance_units     =   tblparms[2]
        self.distance_results   =   tblparms[3]


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Distance_Results_Table : init",self.distance_type,self.distance_units)
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Distance_Results_Table : results\n  ",self.distance_results)


        self.init_tableview()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_Results_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,parent,distance_type,units,results):
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_Results_Table][reload_data] : ")
        
        self.parent             =   parent
        self.distance_type      =   distance_type
        self.distance_units     =   units
        self.distance_results   =   results

        tbldata    =   self.load_distance_data(self.distance_type,self.distance_results)
        self.model.reload_data(tbldata)

        self.num_rows   =   len(tbldata)
        
        if(self.num_rows <15) :
            new_height  =   40 + ((self.num_rows) * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_Results_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        geocode_distance_results_data     =   self.load_distance_data(self.distance_type,self.distance_results)
        
        if(self.model is None) :
            self.model = GeocodeGeocodingModel(geocode_distance_results_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
           print("  [Geocode_Distance_Results_Table][init_tableview] : model loaded")

        self.num_rows   =   len(geocode_distance_results_data)
        
        if(self.num_rows <15) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(geocode_distance_results_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)

    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_distance_data(self,distance_type,distance_results):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_Results_Table][load_distance_data]")
            print("  [Geocode_Distance_Results_Table][load_distance_data] results : \n    ",distance_results)

        from_list   =   distance_results[0]
        to_list     =   distance_results[1]
        distances   =   distance_results[2]

        data    =   []

        for i in range(len(distances)) :

            data_row    =   []
        
            data_row.append(distances[i])
            data_row.append(from_list[i])
            data_row.append(to_list[i])
 
            data.append(data_row)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
            print("  [Geocode_Distance_Results_Table][dump] : data")
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        if(distance_type == ADDRESS) :

            if(self.distance_units == "miles") :
                self.column_headers     =   ["Distance(Miles)","From Address","To Address"]
            else :
                self.column_headers     =   ["Distance(Kilometers)","From Address","To Address"]

            self.column_widths      =   [250,300,300]

        else :

            if(self.distance_units == "Miles") :
                self.column_headers     =   ["Distance(Miles)","From Geopoint","To Geopoint"]
            else :
                self.column_headers     =   ["Distance(Kilometers)","From Geopoint","To Geopoint"]

            self.column_widths      =   [250,300,300]


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Geocoding_Results_Table][end load]")

        return(data)

class Geoocoder_Distance_Results_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Distance_Results_Widget]")
            for i in range(len(dfparms)) :
                print("[Geoocoder_Distance_Results_Widget] dfparm ",dfparms[i])    

        super().__init__()

        self.parent             =   dfparms[0]
        self.distance_type      =   dfparms[1]
        self.distance_units     =   dfparms[2]
        self.distance_results   =   dfparms[3]


        self.from_list          =   dfparms[3][0]
        self.to_list            =   dfparms[3][1]
        self.distances          =   dfparms[3][2]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Distance_Results_Widget] end")

    def reload_data(self,parent,mode,units,results) :

        self.parent             =   parent
        self.distance_type      =   mode
        self.distance_units     =   units
        self.distance_results   =   results
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Distance_Results_Widget][reload_data] ",self.distance_type)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        if(self.distance_type == ADDRESS) :
            self.geocode_address_distance_results.reload_data(self.parent,self.distance_type,self.distance_units,self.distance_results)  
        else :
            self.geocode_latlng_distance_results.reload_data(self.parent,self.distance_type,self.distance_units,self.distance_results)   

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Distance_Results_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        if(self.distance_type == ADDRESS) :
            
            parms   =   [self.parent,self.distance_type,self.distance_units,self.distance_results]
            self.geocode_address_distance_results     =   Geocode_Distance_Results_Table(parms)
            self.geocode_address_distance_results.setFixedWidth(850)
        
        else :

            parms   =   [self.parent,self.distance_type,self.distance_units,self.distance_results]
            self.geocode_latlng_distance_results     =   Geocode_Distance_Results_Table(parms)
            self.geocode_latlng_distance_results.setFixedWidth(800)

        self.geocoding_results_tableLayout  =   QVBoxLayout()
        
        if(self.distance_type == ADDRESS) :
            title_msg   =   "Geocoding Address Distance Results"
        else :
            title_msg   =   "Geocoding LatLng Distance Results"

        from PyQt5.QtWidgets import QLabel
        title_label   =   QLabel()
        title_label.setText("\n\n" + title_msg + "\n")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.geocoding_results_tableLayout.addWidget(title_label)

        if(self.distance_type == ADDRESS) :
            self.geocoding_results_tableLayout.addWidget(self.geocode_address_distance_results)
        else :
            self.geocoding_results_tableLayout.addWidget(self.geocode_latlng_distance_results) 

        spacer_label   =   QLabel()
        spacer_label.setText("\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.geocoding_results_tableLayout.addWidget(spacer_label)


        from PyQt5.QtWidgets import QPushButton
        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_results) 

        self.geocoding_results_tableLayout.addWidget(return_button,alignment=Qt.AlignHCenter)

        self.geocoding_results_tableLayout.addStretch()
        self.geocoding_results_tableLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.geocoding_results_tableLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Distance_Results_Widget][init_form] end")

    def return_from_results(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Distance_Results_Widget][return_from_results]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        self.parent.display_geocoding_distance_utility(ADDRESS)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Geocode Utilities Widget                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_Utilities_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Utilities_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Utilities_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][init_form]")

        self.init_command_bar()

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_geocode")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addLayout(self.dfc_dfs_layout)
        self.transform_col_Layout.addStretch()

        self.setLayout(self.transform_col_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][init_form] end")


    def init_command_bar(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][init_command_bar]")

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.distance_button        =   QPushButton()   
        self.center_button          =   QPushButton()   
        self.center_loc_button      =   QPushButton()    
        self.split_loc_button       =   QPushButton()
        self.join_loc_button        =   QPushButton()        
        self.return_button          =   QPushButton()   
        self.help_button            =   QPushButton()  

        button_bar1_button_list     =   [self.distance_button ,self.center_button,self.center_loc_button,
                                         self.split_loc_button,self.join_loc_button,self.return_button,self.help_button]
        
        button_bar1_text_list       =   ["Calculate\nDistance","Calculate\nCenter","Calculate\nDistance\nFrom\nLocation",
                                         "Split\nLat_Lng\nColumn","Join\nLat_Lng\nColumns","Return","Help"]
        button_bar1_size_list       =   [144,110]
        button_bar1_tool_tip_list   =   ["Calculate Distance","Calculate Center","Calculation distance from Location",
                                         "Split column into Lat Lng columns","Join Lat,Lng Columns into column","Return","Help"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.calculate_distance,self.calculate_center,self.calculate_distance_from_loc,
                                         self.split_column,self.join_columns,self.return_from_geocode_utils,self.help_for_geocode_utils]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.GeocodeCmdbarLayout)
        self.parent.form.GeocodeCmdbarLayout.addLayout(cmdbarLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][init_command_bar] end")


    # -----------------------------------------------------------------#
    # -              Transfoprm Columns Widget methods                -#
    # -----------------------------------------------------------------#

    def calculate_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        self.parent.display_geocoding_distance_utility(ADDRESS)

   
    def calculate_df_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_df_distance]")
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DATAFRAME
        self.parent.display_geocoding_distance_utility(DATAFRAME)
     
    def calculate_center(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_center]")
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_center_point(USER_LOCATION)

    def calculate_distance_from_loc(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_distance_from_loc]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(USER_LOCATION)

    def split_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][split_column]")

        self.parent.display_geocoding_split()

    def join_columns(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][join_columns]")

        self.parent.display_geocoding_join()
    
 
    def return_from_geocode_utils(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Utilities_Widget][return_from_geocode_utils]\n")
        
        self.parent.init_geocode_form()      

    def help_for_geocode_utils(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][help_for_geocode_utils]")
        


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Geocode Address Distance Widget                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_Address_Distance_Utility_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Address_Distance_Utility_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Address_Distance_Utility_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Address_Distance_Utility_Widget] end")

    def reload_banner(self) :
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Address_Distance_Utility_Widget][reload_data] ")

        self.init_command_bar()

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Address_Distance_Utility_Widget][init_form]")

        form_parms      =   [from_address_distance_id,from_address_distance_idList,from_address_distance_labelList,from_address_distance_typeList,
                             from_address_distance_placeholderList,from_address_distance_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\nFrom Addresses\n"
        form_width      =   400
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.distance_addr_from_form    =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Address_Distance_Utility_Widget] distance_addr_from_form built")

        form_parms      =   [to_address_distance_id,to_address_distance_idList,to_address_distance_labelList,to_address_distance_typeList,
                             to_address_distance_placeholderList,to_address_distance_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\nTo Addresses\n"
        form_width      =   400
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.distance_addr_to_form    =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Address_Distance_Utility_Widget] distance_addr_to_form built")

        from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
 
        self.addr_dist_Layout     =   QHBoxLayout()
        self.addr_dist_Layout.addWidget(self.distance_addr_from_form ) 
        self.addr_dist_Layout.addWidget(self.distance_addr_to_form )       
        self.addr_dist_Layout.setAlignment(Qt.AlignTop)

        form_parms      =   [addr_dist_utility_input_id,addr_dist_utility_input_idList,addr_dist_utility_input_labelList,addr_dist_utility_input_typeList,
                             addr_dist_utility_input_placeholderList,addr_dist_utility_input_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   [self.calculate_address_distance,self.get_latlng_distance,self.get_df_distance,self.clear_distance,self.return_distance]
        cfg_parms       =   None
        form_title      =   ""
        form_width      =   800

        selectDicts     =   []

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)
        
        form_parms.append(selectDicts)
        form_parms.append([None,None,None])            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.distance_addr_cmd_form    =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Address_Distance_Utility_Widget] distance_addr_cmd_form built")
        
        self.distance_form_layout    =  QVBoxLayout() 
        self.distance_form_layout.addWidget(self.distance_addr_cmd_form) 
        self.distance_form_layout.addStretch() 

        self.addr_Layout     =   QVBoxLayout()
        self.addr_Layout.addLayout(self.addr_dist_Layout)
        self.addr_Layout.addLayout(self.distance_form_layout)
        self.addr_Layout.addStretch()
        
        self.setLayout(self.addr_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Address_Distance_Utility_Widget][init_form] end")

    def calculate_address_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_address_distanc]")

        from_addresses  =   []
        for i in range(5) :
            from_addresses.append(self.distance_addr_from_form.get_form_input_value_by_index(i))

        from dfcleanser.common.cfg import set_config_value, get_config_value
        set_config_value(from_address_distance_id+"Parms",from_addresses)

        to_addresses  =   []
        for i in range(5) :
            to_addresses.append(self.distance_addr_to_form.get_form_input_value_by_index(i))

        set_config_value(to_address_distance_id+"Parms",to_addresses)

        distance_parms  =   []
        distance_parms.append(self.distance_addr_cmd_form.get_form_input_value_by_index(0))
        distance_parms.append(self.distance_addr_cmd_form.get_form_input_value_by_index(1))
        distance_parms.append(self.distance_addr_cmd_form.get_form_input_value_by_index(2))

        set_config_value(addr_dist_utility_input_id+"Parms",distance_parms)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_distances
        parms       =   [from_addresses,to_addresses,distance_parms]
        distances   =   process_calculate_distances(ADDRESS,parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[calculate_address_distance] : distances ",distances)

        results     =   []
        results.append(from_addresses)
        results.append(to_addresses)
        results.append(distances) 

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        self.parent.display_geocoding_distance_data(ADDRESS,distance_parms[0],results)


    def get_latlng_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_latlng_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import LAT_LNG
        self.parent.display_geocoding_distance_utility(LAT_LNG)
     
    def get_df_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_df_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DATAFRAME
        self.parent.display_geocoding_distance_utility(DATAFRAME)

    def clear_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][clear_distance]")
        
        for i in range(5) :
            self.distance_addr_from_form.set_form_input_value_by_index(i,"")
            self.distance_addr_to_form.set_form_input_value_by_index(i,"")
  
    def return_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_distance]")
        
        self.parent.display_geocoding_utilities()        

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Geocode Address Distance Widget                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_LatLng_Distance_Utility_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_LatLng_Distance_Utility_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_LatLng_Distance_Utility_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_LatLng_Distance_Utility_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_LatLng_Distance_Utility_Widget][init_form]")

        form_parms      =   [from_latlng_distance_id,from_latlng_distance_idList,from_latlng_distance_labelList,from_latlng_distance_typeList,
                             from_latlng_distance_placeholderList,from_latlng_distance_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\n Geocode LatLng From Addresses\n"
        form_width      =   400
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.latlng_addr_from_form    =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_LatLng_Distance_Utility_Widget] dlatlng_addr_from_form built")

        form_parms      =   [to_latlng_distance_id,to_latlng_distance_idList,to_latlng_distance_labelList,to_latlng_distance_typeList,
                             to_latlng_distance_placeholderList,to_latlng_distance_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\n Geocode Distance To LatLng\n"
        form_width      =   400
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.latlng_addr_to_form    =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_LatLng_Distance_Utility_Widget] latlng_addr_to_form built")

        from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
 
        self.latlng_dist_Layout     =   QHBoxLayout()
        self.latlng_dist_Layout.addWidget(self.latlng_addr_from_form ) 
        self.latlng_dist_Layout.addWidget(self.latlng_addr_to_form )       
        self.latlng_dist_Layout.setAlignment(Qt.AlignTop)

        form_parms      =   [latlng_dist_utility_input_id,latlng_dist_utility_input_idList,latlng_dist_utility_input_labelList,latlng_dist_utility_input_typeList,
                             latlng_dist_utility_input_placeholderList,latlng_dist_utility_input_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   [self.calculate_latlng_distance,self.get_address_distance,self.get_latlng_df_distance,self.clear_latlng_distance,self.return_latlng_distance]
        cfg_parms       =   None
        form_title      =   ""
        form_width      =   800

        selectDicts     =   []

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)
        
        form_parms.append(selectDicts)
        form_parms.append([None,None,None])            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.distance_latlng_cmd_form    =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_LatLng_Distance_Utility_Widget] distance_latlng_cmd_form built")
        
        self.distance_form_layout    =  QVBoxLayout() 
        self.distance_form_layout.addWidget(self.distance_latlng_cmd_form) 
        self.distance_form_layout.addStretch() 

        self.latlng_Layout     =   QVBoxLayout()
        self.latlng_Layout.addLayout(self.latlng_dist_Layout)
        self.latlng_Layout.addLayout(self.distance_form_layout)
        self.latlng_Layout.addStretch()
        
        self.setLayout(self.latlng_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_LatLng_Distance_Utility_Widget][init_form] end")


    def calculate_latlng_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_latlng_distanc]")

        from_addresses  =   []
        for i in range(5) :
            from_addresses.append(self.latlng_addr_from_form.get_form_input_value_by_index(i))

        from dfcleanser.common.cfg import set_config_value
        set_config_value(from_latlng_distance_id+"Parms",from_addresses)         

        to_addresses  =   []
        for i in range(5) :
            to_addresses.append(self.latlng_addr_to_form .get_form_input_value_by_index(i))
        set_config_value(to_latlng_distance_id+"Parms",from_addresses)         

        distance_parms  =   []
        distance_parms.append(self.distance_latlng_cmd_form.get_form_input_value_by_index(0))
        distance_parms.append(self.distance_latlng_cmd_form.get_form_input_value_by_index(1))
        distance_parms.append(self.distance_latlng_cmd_form.get_form_input_value_by_index(2))
        set_config_value(latlng_dist_utility_input_id + "Parms",distance_parms)  

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import LAT_LNG
        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_distances
        parms   =   [from_addresses,to_addresses,distance_parms]
        distances   =   process_calculate_distances(LAT_LNG,parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[calculate_address_distance] : distances ",distances)

        results     =   []
        results.append(from_addresses)
        results.append(to_addresses)
        results.append(distances) 

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        self.parent.display_geocoding_distance_data(ADDRESS,distance_parms[0],results)
   
    def get_address_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_address_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
        self.parent.display_geocoding_distance_utility(ADDRESS)
     
    def get_latlng_df_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_df_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DATAFRAME
        self.parent.display_geocoding_distance_utility(DATAFRAME)

    def clear_latlng_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][clear_latlng_distance]")

        for i in range(5) :
            self.latlng_addr_from_form.set_form_input_value_by_index(i,"")
            self.latlng_addr_to_form.set_form_input_value_by_index(i,"")
  
    def return_latlng_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_latlng_distance]")
        
        self.parent.display_geocoding_utilities()        


# -----------------------------------------------------------------#
# -               Geocode Address Distance Widget                 -#
# -----------------------------------------------------------------#

class Geocode_df_Distance_Utility_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_df_Distance_Utility_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_df_Distance_Utility_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 14px; font-weight:bold; font-family: Arial;")

        text1       =   "If GeoLocation is defined by \na single column\nselect a single column"
        text_delim  =   "\n---------------------------------------\n" 
        text2       =   "If GeoLocation is defined by \n a Latitude column and \n a Longitude column\ndefine the columns\nas [LatColumn,LngColumn]"
        label_text  =   text1 + text_delim + text2

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        title_label   =   QLabel()
        title_label.setText(label_text)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; font-weight:normal; font-family:  Arial; background-color:#ffffcc; border: 1px solid black;")

        form_parms      =   [addr_df_dist_utility_input_id,addr_df_dist_utility_input_idList,addr_df_dist_utility_input_labelList,
                             addr_df_dist_utility_input_typeList,addr_df_dist_utility_input_placeholderList,addr_df_dist_utility_input_reqList]

        selectDicts     =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dataframes      =   get_dfc_dataframes_titles_list()
        dfsel           =   {"default":dataframes[0],"list": dataframes}
        selectDicts.append(dfsel)

        df              =   get_dfc_dataframe_df(dataframes[0])
        df_cols         =   df.columns.tolist() 
        colssel         =   {"default":df_cols[0],"list": df_cols} 
        selectDicts.append(colssel)
        selectDicts.append(colssel)

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_df,self.select_from_column,self.select_to_column,None,None,None]
        file_methods    =   None
        button_methods  =   [self.calculate_dataframe_distance,self.clear_dataframe_distance,self.return_dataframe_distance,self.help_dataframe_distance]
        cfg_parms       =   None
        form_title      =   "\n\nGet Distance Between df columns"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.distance_df_form    =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_df_Distance_Utility_Widget] distance_df_form built")
        
        self.distance_notesLayout  =   QVBoxLayout()
        self.distance_notesLayout.addWidget(spacer_label)
        self.distance_notesLayout.addWidget(title_label)
        self.distance_notesLayout.addStretch()
        self.distance_notesLayout.setAlignment(Qt.AlignTop)

        self.distance_form_layout  =   QVBoxLayout()
        self.distance_form_layout.addWidget(self.distance_df_form)
        self.distance_form_layout.setAlignment(Qt.AlignTop)
         
        self.distanceLayout     =   QHBoxLayout()
        self.distanceLayout.addLayout(self.distance_notesLayout) 
        self.distanceLayout.addLayout(self.distance_form_layout)       
        self.distanceLayout.setAlignment(Qt.AlignTop)

        self.df_Layout     =   QVBoxLayout()
        self.df_Layout.addLayout(self.distanceLayout)
        self.df_Layout.addStretch()
        
        self.setLayout(self.df_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget][init_form] end")

    def select_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget][select_dfc]")

        new_df  =   self.distance_df_form.get_form_input_value_by_index(0)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df              =   get_dfc_dataframe_df(new_df)
        df_cols         =   df.columns.tolist() 

        self.distance_df_form.set_form_input_value_by_index(1,df_cols[0])
        self.distance_df_form.reset_form_combobox_by_index(2,df_cols)

        self.distance_df_form.set_form_input_value_by_index(3,df_cols[0])
        self.distance_df_form.reset_form_combobox_by_index(4,df_cols)

    def select_from_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget][select_from_column]")

        new_from_col  =   self.distance_df_form.get_form_input_value_by_index(2)
        self.distance_df_form.set_form_input_value_by_index(1,new_from_col)

    def select_to_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Distance_Utility_Widget][select_to_column]")

        new_to_col  =   self.distance_df_form.get_form_input_value_by_index(4)
        self.distance_df_form.set_form_input_value_by_index(3,new_to_col)

    def calculate_dataframe_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][calculate_dataframe_distance]")

        parms   =   []
        parms.append(self.distance_df_form.get_form_input_value_by_index(0))
        parms.append(self.distance_df_form.get_form_input_value_by_index(1))
        parms.append(self.distance_df_form.get_form_input_value_by_index(3))
        parms.append(self.distance_df_form.get_form_input_value_by_index(5)) 
        parms.append(self.distance_df_form.get_form_input_value_by_index(6)) 
        parms.append(self.distance_df_form.get_form_input_value_by_index(7)) 
        parms.append(self.distance_df_form.get_form_input_value_by_index(8)) 

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_df_distances
        df_col_distances    =   process_calculate_df_distances(parms) 

        if(not (df_col_distances is None)) :

            try :

                dftitle         =   self.distance_df_form.get_form_input_value_by_index(0)
                dist_col_name   =   self.distance_df_form.get_form_input_value_by_index(5)

                from dfcleanser.common.cfg import get_dfc_dataframe_df
                df  =   get_dfc_dataframe_df(dftitle)

                df[dist_col_name]   =   df_col_distances

                from dfcleanser.common.cfg import set_dfc_dataframe_df
                set_dfc_dataframe_df(dftitle,df)

                title       =   "dfcleanser status"       
                status_msg  =   dist_col_name + " added to " + dftitle
                from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                display_status_msg(title,status_msg)

            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[unable to save df dist column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)


    def clear_dataframe_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][clear_dataframe_distance]")
        
        self.distance_df_form.set_form_input_value_by_index(1,"")
        self.distance_df_form.set_form_input_value_by_index(3,"")
        self.distance_df_form.set_form_input_value_by_index(5,"")
  
    def return_dataframe_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_dataframe_distance]")

        self.parent.display_geocoding_utilities()        

    def help_dataframe_distance(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][help_dataframe_distance]")

        self.parent.display_geocoding_utilities()        


# -----------------------------------------------------------------#
# -                 Geocode Center Point Widget                   -#
# -----------------------------------------------------------------#

class Geocode_Center_Point_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Center_Point_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Center_Point_Widget] end")

    def reload_banner(self) :
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Widget][reload_data] ")

        self.init_command_bar()

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Widget][init_form]")

        form_parms      =   [center_pt_input_id,center_pt_input_idList,center_pt_input_labelList,center_pt_input_typeList,
                             center_pt_input_placeholderList,center_pt_input_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\n\nLocations\n"
        form_width      =   250
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.center_point_location   =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Center_Point_Widget]center_point_location  built")

        form_parms      =   [center_pt_1_input_id,center_pt_input_idList,center_pt_input_labelList,center_pt_input_typeList,
                             center_pt_input_placeholderList,center_pt_input_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\n\nLocations\n"
        form_width      =   250
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.center_point1_location   =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Center_Point_Widget]center_point1_location  built")

        form_parms      =   [center_pt_2_input_id,center_pt_input_idList,center_pt_input_labelList,center_pt_input_typeList,
                             center_pt_input_placeholderList,center_pt_input_reqList]
        
        comboList       =   None
        comboMethods    =   None
        file_methods    =   None
        button_methods  =   None
        cfg_parms       =   None
        form_title      =   "\n\nLocations\n"
        form_width      =   250
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.center_point2_location   =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Center_Point_Widget]center_point2_location  built")


        from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
 
        self.center_pts_Layout     =   QHBoxLayout()
        self.center_pts_Layout.addWidget(self.center_point_location ) 
        self.center_pts_Layout.addWidget(self.center_point1_location ) 
        self.center_pts_Layout.addWidget(self.center_point2_location )       
        self.center_pts_Layout.setAlignment(Qt.AlignTop)


        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.calc_center_pt         =   QPushButton()   
        self.get_df_center_pt       =   QPushButton()    
        self.return_button          =   QPushButton()   
        self.help_button            =   QPushButton()    

        button_bar1_button_list     =   [self.calc_center_pt ,self.get_df_center_pt,self.return_button,self.help_button]
        
        button_bar1_text_list       =   ["Calculate\nCenter Point\n for Locations","Get\nCenter Pt\nFor df","Return","Help"]
        button_bar1_size_list       =   [220,110]
        button_bar1_tool_tip_list   =   ["Calculate Center","Get df column pt center","Return","Help"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.calculate_center_point,self.get_center_pt_for_df,self.return_from_center_pt,self.help_for_center_pt]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nEnter locations as [Latitude,Longitude] pairs.")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")


        self.addr_Layout     =   QVBoxLayout()
        self.addr_Layout.addLayout(self.center_pts_Layout)
        self.addr_Layout.addLayout(cmdbarLayout)
        self.addr_Layout.addWidget(note_label)
        self.addr_Layout.addStretch()
        
        self.setLayout(self.addr_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Widget][init_form] end")


    def calculate_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Center_Point_Widget][calculate_center_point]")

        parms       =   []
        locparms    =   []
        for i in range(5) :
            locparms.append(self.center_point_location.get_form_input_value_by_index(i))
        parms.append(locparms)
        from dfcleanser.common.cfg import set_config_value
        set_config_value(center_pt_input_id+"Parms",locparms)

        locparms1    =   []
        for i in range(5) :
            locparms1.append(self.center_point1_location.get_form_input_value_by_index(i))
        parms.append(locparms1)
        set_config_value(center_pt_1_input_id+"Parms",locparms1)

        locparms2   =   []
        for i in range(5) :
            locparms2.append(self.center_point2_location.get_form_input_value_by_index(i))
        parms.append(locparms)
        set_config_value(center_pt_2_input_id+"Parms",locparms2)
       
        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_center_pt
        center_point    =   process_calculate_center_pt(parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Center_Point_Widget][calculate_center_point] center point : ",center_point)

        geocode_points  =   []
        for i in range(len(locparms)) :
            if(len(str(locparms[i])) > 0) :
                geocode_points.append(locparms[i])
        for i in range(len(locparms1)) :
            if(len(str(locparms1[i])) > 0) :
                geocode_points.append(locparms1[i])
        for i in range(len(locparms2)) :
            if(len(str(locparms2[i])) > 0) :
                geocode_points.append(locparms2[i])

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_center_point_data(USER_LOCATION,geocode_points,center_point)
        

    def get_center_pt_for_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_latlng_distance]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DF_CENTER_POINT_LOCATION
        self.parent.display_geocoding_center_point(DF_CENTER_POINT_LOCATION)
    
    def return_from_center_pt(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_from_center_pt]")
        
        self.parent.display_geocoding_utilities()        

    def help_for_center_pt(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_from_center_pt]")
        
        self.parent.display_geocoding_utilities()        


# -----------------------------------------------------------------#
# -             Geocode Center Point Results Widget               -#
# -----------------------------------------------------------------#


class GeocodeCenterPointResultsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(GeocodeCenterPointResultsModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            #print("data model Qt.DisplayRole",row,column)
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if((column == 0) and (row == 1)):
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignCenter)

        if role==Qt.BackgroundColorRole:
            if((column == 0) and (row==1)):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)
    

class Geocode_Center_Point_Results_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   tblparms[0]
        self.center_point_type  =   tblparms[1]
        self.center_point_data  =   tblparms[2]

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(self.center_point_type == USER_LOCATION) : 

            self.geopoints  =   self.center_point_data
            self.dftitle    =   None
            self.colname    =   None 

        else :

            self.geopoints  =   None
            self.dftitle    =   self.center_point_data[0]
            self.colname    =   self.center_point_data[1] 
        
        self.center_point   =   tblparms[3]


        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Center_Point_Results_Table] : init",self.center_point_type,self.geopoints,self.dftitle,self.colname,self.center_point)

        self.init_tableview()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Results_Table] : end\n")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,parent,center_point_type,geopoints,center_point):
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Results_Table][reload_data] : ")
        
        self.parent             =   parent
        self.center_point_type  =   center_point_type
        self.center_point_data  =   geopoints

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(self.center_point_type == USER_LOCATION) : 

            self.geopoints  =   geopoints
            self.dftitle    =   None
            self.colname    =   None 

        else :

            self.geopoints  =   None
            self.dftitle    =   geopoints[0]
            self.colname    =   geopoints[1] 
        
        self.center_point   =   center_point

        tbldata    =   self.load_center_point_data(self.center_point_type,self.center_point_data,self.center_point)
        self.model.reload_data(tbldata)

        self.num_rows   =   len(tbldata)
        
        if(self.num_rows <15) :
            new_height  =   45 + ((self.num_rows) * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Results_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        geocode_center_point_results_data     =   self.load_center_point_data(self.center_point_type,self.center_point_data,self.center_point)
        
        if(self.model is None) :
            self.model = GeocodeCenterPointResultsModel(geocode_center_point_results_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
           print("  [Geocode_Center_Point_Results_Table][init_tableview] : model loaded")

        self.num_rows   =   len(geocode_center_point_results_data)
        
        if(self.num_rows <15) :
            new_height  =   45 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignLeft)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(geocode_center_point_results_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)

    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_center_point_data(self,center_point_type,center_point_data,center_point):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_Results_Table][load_distance_data]",center_point_type,center_point)
            print("  [Geocode_Distance_Results_Table][load_distance_data] results : \n    ",center_point_data)

        data    =   []

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(geocoderid is None) :

            title       =   "dfcleanser mesage"       
            status_msg  =   "select a geocoder to get address for center point"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

        else :

            from dfcleanser.common.common_utils import opStatus
            opstat      =   opStatus()

            from dfcleanser.Qt.utils.Geocode.GeocodeControl import get_geocoder_engine
            geolocator          =   get_geocoder_engine(geocoderid, opstat)
            location            =   geolocator.reverse(center_point)
            reverse_address     =   location.address

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
                print("  [Geocode_Center_Point_Widget][calculate_df_center_point] reverse_address : ",reverse_address)

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import split_geocode_address
            split_geo_addr  =   split_geocode_address(reverse_address)

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
                print("  [Geocode_Center_Point_Widget][calculate_df_center_point] split_geo_addr : ",split_geo_addr,type(split_geo_addr))

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(center_point_type == USER_LOCATION) : 

            data_row    =   [str(center_point),split_geo_addr[0],split_geo_addr[1]]
            data.append(data_row) 
            
            data_row    =   ["User Locations","",""]
            data.append(data_row) 

            num_data_rows   =   int(len(center_point_data)/3)
            num_part_row    =   len(center_point_data) % 3

            for i in range((num_data_rows)) :

                data_row    =   []
                from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
                
                current_point   =   get_geopoint_from_string(center_point_data[(i*3)+0])
                current_point   =   str(current_point)
                data_row.append(current_point)
                
                current_point   =   get_geopoint_from_string(center_point_data[(i*3)+1])
                current_point   =   str(current_point)
                data_row.append(current_point)

                current_point   =   get_geopoint_from_string(center_point_data[(i*3)+2])
                current_point   =   str(current_point)
                data_row.append(current_point)

                data.append(data_row)

            if(num_part_row > 0) :
                data_row    =   ["","",""]
                
                from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string                
                for j in range(num_part_row) :

                    current_point   =   get_geopoint_from_string(center_point_data[(num_data_rows * 3) + j])
                    current_point   =   str(current_point)
                    data_row[j]     =   current_point

                data.append(data_row)

            self.column_headers     =   ["Center Point","",""]

        else :

            data_row    =   [str(center_point),split_geo_addr[0],split_geo_addr[1]]#str(center_point_data[0]),str(center_point_data[1])]
            data.append(data_row) 

            self.column_headers     =   ["Center Point","Address",""]

        self.column_widths      =   [250,300,300]

        return(data)


class Geoocoder_Center_Point_Results_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Center_Point_Results_Widget]")
            for i in range(len(dfparms)) :
                print("[Geoocoder_Center_Point_Results_Widget] dfparm ",dfparms[i])    

        super().__init__()

        self.parent             =   dfparms[0]
        self.center_point_type  =   dfparms[1]
        self.geodata            =   dfparms[2]
        self.center_point       =   dfparms[3]

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(self.center_point_type == USER_LOCATION) : 

            self.geopoints  =   self.geodata
            self.dftitle    =   None
            self.colname    =   None 

        else :

            self.geopoints  =   None
            self.dftitle    =   self.geodata[0]
            self.colname    =   self.geodata[1] 
        
        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Center_Point_Results_Widget] end")

    def reload_data(self,parent,center_point_type,geodata,center_point) :

        self.parent             =   parent
        self.center_point_type  =   center_point_type
        self.geodata            =   geodata
        self.center_point       =   center_point

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(self.center_point_type == USER_LOCATION) : 

            self.geopoints  =   self.geodata
            self.dftitle    =   None
            self.colname    =   None 

        else :

            self.geopoints  =   None
            self.dftitle    =   self.geodata[0]
            self.colname    =   self.geodata[1] 

        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Center_Point_Results_Widget][reload_data] ",self.center_point_type,self.geodata,self.center_point)

        if(self.center_point_type == USER_LOCATION) :
            self.geocode_center_point_results.reload_data(self.parent,self.center_point_type,self.geodata,self.center_point)  
        else :
            self.geocode_df_center_point_results.reload_data(self.parent,self.center_point_type,self.geodata,self.center_point)   

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geoocoder_Distance_Results_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(self.center_point_type == USER_LOCATION) :
            
            parms   =   [self.parent,self.center_point_type,self.geodata,self.center_point]
            self.geocode_center_point_results     =   Geocode_Center_Point_Results_Table(parms)
            self.geocode_center_point_results.setFixedWidth(850)
        
        else :

            parms   =   [self.parent,self.center_point_type,self.geodata,self.center_point]
            self.geocode_df_center_point_results     =   Geocode_Center_Point_Results_Table(parms)
            self.geocode_df_center_point_results.setFixedWidth(800)

        self.geocoding_results_tableLayout  =   QVBoxLayout()
        
        if(self.center_point_type == USER_LOCATION) :
            title_msg   =   "Geocoding Center Point For User Locations"
        else :
            title_msg   =   "Geocoding Center Point For df '" + self.dftitle + "' : '" + self.colname + "' Column"

        from PyQt5.QtWidgets import QLabel
        title_label   =   QLabel()
        title_label.setText("\n\n" + title_msg + "\n")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.geocoding_results_tableLayout.addWidget(title_label)

        if(self.center_point_type == USER_LOCATION) :
            self.geocoding_results_tableLayout.addWidget(self.geocode_center_point_results)
        else :
            self.geocoding_results_tableLayout.addWidget(self.geocode_df_center_point_results) 

        spacer_label   =   QLabel()
        spacer_label.setText("\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        #self.geocoding_results_tableLayout.addWidget(spacer_label)


        from PyQt5.QtWidgets import QPushButton
        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_results) 

        self.geocoding_results_tableLayout.addWidget(return_button,alignment=Qt.AlignHCenter)

        self.geocoding_results_tableLayout.addStretch()
        self.geocoding_results_tableLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.geocoding_results_tableLayout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Distance_Results_Widget][init_form] end")

    def return_from_results(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geoocoder_Distance_Results_Widget][return_from_results] ",self.center_point_type)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DF_CENTER_POINT_LOCATION, USER_LOCATION
        if(self.center_point_type == USER_LOCATION) :
            self.parent.display_geocoding_center_point(USER_LOCATION)
        else :
            self.parent.display_geocoding_center_point(DF_CENTER_POINT_LOCATION)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Geocode df Center Point Widget                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_df_Center_Point_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_df_Center_Point_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_df_Center_Point_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 14px; font-weight:bold; font-family: Arial;")

        text1       =   "If GeoLocation is defined by \na single column\nselect a single column"
        text_delim  =   "\n---------------------------------------\n" 
        text2       =   "If GeoLocation is defined by \n a Latitude column and \n a Longitude column\ndefine the columns\nas [LatColumn,LngColumn]"
        label_text  =   text1 + text_delim + text2

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        title_label   =   QLabel()
        title_label.setText(label_text)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 12px; font-weight:normal; background-color:#ffffcc; font-family: Atial; border: 1px solid black;")

        form_parms      =   [addr_center_df_utility_input_id,addr_center_df_utility_input_idList,addr_center_df_utility_input_labelList,
                             addr_center_df_utility_input_typeList, addr_center_df_utility_input_placeholderList,addr_center_df_utility_input_reqList]
        
        selectDicts     =   []
    
        dfs             =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dfs         =   get_dfc_dataframes_titles_list()
        df_sel      =   {"default":dfs[0],"list":dfs}
        selectDicts.append(df_sel)
        
        df          =   get_dfc_dataframe_df(dfs[0])
        dfcols      =   df.columns.tolist()
        cols_sel    =   {"default":dfcols[0],"list":dfcols}
        selectDicts.append(cols_sel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_Center_Point_df,self.select_Center_Point_col,None]
        file_methods    =   None
        button_methods  =   [self.calculate_df_center_point,self.get_list_center_point,self.return_from_df_center,self.help_for_df_center]
        cfg_parms       =   None
        form_title      =   "\n\nGet Center Point For df Column\n"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_center_point_location   =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_df_Center_Point_Widget]center_point_location  built")

        self.centerpt_notesLayout  =   QVBoxLayout()
        self.centerpt_notesLayout.addWidget(spacer_label)
        self.centerpt_notesLayout.addWidget(title_label)
        self.centerpt_notesLayout.addStretch()
        self.centerpt_notesLayout.setAlignment(Qt.AlignTop)

        self.centerpt_form_layout  =   QVBoxLayout()
        self.centerpt_form_layout.addWidget(self.df_center_point_location )
        self.centerpt_form_layout.setAlignment(Qt.AlignTop)
         
        self.centerptLayout     =   QHBoxLayout()
        self.centerptLayout.addLayout(self.centerpt_notesLayout) 
        self.centerptLayout.addLayout(self.centerpt_form_layout)       
        self.centerptLayout.setAlignment(Qt.AlignTop)

        from PyQt5.QtWidgets import  QVBoxLayout
        self.df_center_Layout     =   QVBoxLayout()
        self.df_center_Layout.addLayout(self.centerptLayout)
        self.df_center_Layout.addStretch()
        
        self.setLayout(self.df_center_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][init_form] end")

    def select_Center_Point_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][select_Center_Point_df]")
        
        dftitle     =   self.df_center_point_location.get_form_input_value_by_index(0)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df          =   get_dfc_dataframe_df(dftitle)
        dfcols      =   df.columns.tolist()

        self.df_center_point_location.reset_form_combobox_by_index(2, dfcols)    
        self.df_center_point_location.reset_form_combobox_by_index(5, dfcols)

    def select_Center_Point_col(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][select_Center_Point_col]")

        dfcol           =   self.df_center_point_location.get_form_input_value_by_index(2)
        current_col     =   self.df_center_point_location.get_form_input_value_by_index(1)

        if(len(current_col) > 0) :
            
            if(current_col.find("[") < 0) :

                new_col =   "["
                new_col =   new_col + current_col
                new_col =   new_col + ", "
                new_col =   new_col + dfcol
                new_col =   new_col + "]"
                self.df_center_point_location.set_form_input_value_by_index(1,new_col) 
            
            else :
                self.df_center_point_location.set_form_input_value_by_index(1,dfcol)           
        else :
            self.df_center_point_location.set_form_input_value_by_index(1,dfcol)

    def calculate_df_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Widget][calculate_df_center_point]")

        parms       =   []

        parms.append(self.df_center_point_location.get_form_input_value_by_index(0))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(1))

        if(len(parms[0]) > 0) :
            if(len(parms[1]) >0) :
       
                from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_df_center_pt
                center_point    =   process_calculate_df_center_pt(parms)

                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
                    print("  [Geocode_Center_Point_Widget][calculate_df_center_point] center_point : ",center_point)

                from dfcleanser.Qt.utils.Geocode.GeocodeModel import DF_CENTER_POINT_LOCATION
                self.parent.display_geocoding_center_point_data(DF_CENTER_POINT_LOCATION,parms,center_point)

            else :

                title       =   "dfcleanser error"       
                status_msg  =   "No dfc col name defined"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

        else :

            title       =   "dfcleanser error"       
            status_msg  =   "No df title defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)


   
    def get_list_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_list_center_point]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_center_point(USER_LOCATION)
    
    def return_from_df_center(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_from_df_center]")
        
        self.parent.display_geocoding_utilities()        


    def help_for_df_center(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][elp_for_df_center]")
        
        self.parent.display_geocoding_utilities()        




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           Geocode Distance from User Location                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_Distance_From_User_Loaction_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n  [Geocode_Distance_From_User_Loaction_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_User_Loaction_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_User_Loaction_Widget][init_form]")
        
        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 14px; font-weight:bold; font-family: Arial;")

        text1       =   "If GeoLocation is defined by \na single column\nselect a single column"
        text_delim  =   "\n---------------------------------------\n" 
        text2       =   "If GeoLocation is defined by \n a Latitude column and \n a Longitude column\ndefine the columns\nas [LatColumn,LngColumn]"
        label_text  =   text1 + text_delim + text2

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        title_label   =   QLabel()
        title_label.setText(label_text)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 12px; font-weight:normal; background-color:#ffffcc; font-family: Arial; border: 1px solid black;")

        form_parms      =   [df_dist_from_loc_utility_input_id,df_dist_from_loc_utility_input_idList,df_dist_from_loc_utility_input_labelList,
                             df_dist_from_loc_utility_input_typeList, df_dist_from_loc_utility_input_placeholderList,df_dist_from_loc_utility_input_reqList]
        
        selectDicts     =   []
    
        dfs             =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dfs         =   get_dfc_dataframes_titles_list()
        df_sel      =   {"default":dfs[0],"list":dfs}
        selectDicts.append(df_sel)
        
        df          =   get_dfc_dataframe_df(dfs[0])
        dfcols      =   df.columns.tolist()
        cols_sel    =   {"default":dfcols[0],"list":dfcols}
        selectDicts.append(cols_sel)

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_User_Loaction_df,self.select_User_Loaction_col,None,None,None]
        file_methods    =   None
        button_methods  =   [self.calculate_dist_from_point,self.get_center_point_input,self.get_closest_center_point_input,self.return_from_df_dist_point,self.help_for_df_dist_point]
        cfg_parms       =   None
        form_title      =   "\n\nGet Distance(s) From User Location to df Column Values\n"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_user_location   =   dfcleanser_input_form_Widget(form_parms)
        self.df_user_location.set_form_input_value_by_index(0,"(Latitude,Longitude)")
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_User_Loaction_Widget] form built")

        self.user_distance_notesLayout  =   QVBoxLayout()
        self.user_distance_notesLayout.addWidget(spacer_label)
        self.user_distance_notesLayout.addWidget(title_label)
        self.user_distance_notesLayout.addStretch()
        self.user_distance_notesLayout.setAlignment(Qt.AlignTop)

        self.user_distance_form_layout  =   QVBoxLayout()
        self.user_distance_form_layout.addWidget(self.df_user_location)
        self.user_distance_form_layout.setAlignment(Qt.AlignTop)
         
        self.user_distanceLayout     =   QHBoxLayout()
        self.user_distanceLayout.addLayout(self.user_distance_notesLayout) 
        self.user_distanceLayout.addLayout(self.user_distance_form_layout)       
        self.user_distanceLayout.setAlignment(Qt.AlignTop)

        from PyQt5.QtWidgets import  QVBoxLayout
        self.df_center_Layout     =   QVBoxLayout()
        self.df_center_Layout.addLayout(self.user_distanceLayout)
        self.df_center_Layout.addStretch()
        
        self.setLayout(self.df_center_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_User_Loaction_Widget][init_form] end")


    def select_User_Loaction_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][select_User_Loaction_df]")
        
        dftitle     =   self.df_user_location.get_form_input_value_by_index(0)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df          =   get_dfc_dataframe_df(dftitle)
        dfcols      =   df.columns.tolist()

        self.df_user_location.reset_form_combobox_by_index(2, dfcols)    

    def select_User_Loaction_col(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_df_Center_Point_Widget][select_User_Loaction_col]")

        dfcol     =   self.df_user_location.get_form_input_value_by_index(3)
        self.df_user_location.set_form_input_value_by_index(2,dfcol)
        
    def calculate_dist_from_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Center_Point_Widget][calculate_dist_from_point]")

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_df_distances_from_fixed_location
        parms   =   []
        parms.append(self.df_user_location.get_form_input_value_by_index(0))
        parms.append(self.df_user_location.get_form_input_value_by_index(1))
        parms.append(self.df_user_location.get_form_input_value_by_index(2))
        parms.append(self.df_user_location.get_form_input_value_by_index(4))
        parms.append(self.df_user_location.get_form_input_value_by_index(5)) 
        parms.append(self.df_user_location.get_form_input_value_by_index(6))
        parms.append(self.df_user_location.get_form_input_value_by_index(7)) 

        distances   =   process_calculate_df_distances_from_fixed_location(parms)  

        if(not (distances is None)) :

            cfg_parms   =   []
            cfg_parms.append(parms[0])
            cfg_parms.append(parms[1])
            cfg_parms.append(parms[2])
            cfg_parms.append(self.df_user_location.get_form_input_value_by_index(3))
            cfg_parms.append(parms[3])
            cfg_parms.append(parms[4])
            cfg_parms.append(parms[5])
            cfg_parms.append(parms[6])

            from dfcleanser.common.cfg import set_config_value
            set_config_value(df_dist_from_loc_utility_input_id+"Parsm",cfg_parms)

            from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
            df              =   get_dfc_dataframe_df(parms[1])
            df[parms[3]]    =   distances

            set_dfc_dataframe_df(parms[1],df)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[calculate_dist_from_point] new distance column added"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

   
    def get_center_point_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_center_point_input]")
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DF_CENTER_POINT_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(DF_CENTER_POINT_LOCATION)
    
    def get_closest_center_point_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][get_closest_center_point_input]")
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import CENTER_POINT_LIST_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(CENTER_POINT_LIST_LOCATION)
   
    def return_from_df_dist_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][return_from_df_dist_point]")
        
        self.parent.display_geocoding_utilities()        


    def help_for_df_dist_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Utilities_Widget][help_for_df_dist_point]")
        
        self.parent.display_geocoding_utilities()        



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -        Geocode Distance from Center Point Location            -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_Distance_From_Center_Point_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Distance_From_Center_Point_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Distance_From_Center_Point_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        spacer_label   =   QLabel()
        spacer_label.setText("\n\n\n\n\n\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 12px; font-weight:bold; font-family: Arial;")

        text1       =   "If GeoLocation is defined by \na single column\nselect a single column"
        text_delim  =   "\n---------------------------------------\n" 
        text2       =   "If GeoLocation is defined by \n a Latitude column and \n a Longitude column\ndefine the columns\nas [LatColumn,LngColumn]"
        label_text  =   text1 + text_delim + text2

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        title_label   =   QLabel()
        title_label.setText(label_text)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; font-weight:normal; background-color:#ffffcc; font-family: Arial; border: 1px solid black;")

        form_parms      =   [df_dist_from_center_utility_input_id,df_dist_from_center_utility_input_idList,df_dist_from_center_utility_input_labelList,
                             df_dist_from_center_utility_input_typeList, df_dist_from_center_utility_input_placeholderList,df_dist_from_center_utility_input_reqList]
        
        selectDicts     =   []
    
        dfs             =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dfs         =   get_dfc_dataframes_titles_list()
        df_sel      =   {"default":dfs[0],"list":dfs}
        selectDicts.append(df_sel)
        
        df          =   get_dfc_dataframe_df(dfs[0])
        dfcols      =   df.columns.tolist()
        cols_sel    =   {"default":dfcols[0],"list":dfcols}
        selectDicts.append(cols_sel)

        selectDicts.append(df_sel)
        selectDicts.append(cols_sel)

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_Distance_From_Center_Point_df,self.select_Distance_From_Center_Point_col,self.select_center_pt_df,self.select_ctpt_col,None,None,None]
        file_methods    =   None
        button_methods  =   [self.calculate_dist_from_center_point,self.get_point_input,self.get_closest_input,self.return_from_df_dist_center_point,self.help_for_df_dist_center_point]
        cfg_parms       =   None
        form_title      =   "\n\nGet Distance From Center Point to df Column Values\n"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_center_point_location   =   dfcleanser_input_form_Widget(form_parms)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Distance_From_Center_Point_Widget]center_point_location  built")

        self.centerpt_distance_notesLayout  =   QVBoxLayout()
        self.centerpt_distance_notesLayout.addWidget(spacer_label)
        self.centerpt_distance_notesLayout.addWidget(title_label)
        self.centerpt_distance_notesLayout.addStretch()
        self.centerpt_distance_notesLayout.setAlignment(Qt.AlignTop)

        self.centerpt_distance_form_layout  =   QVBoxLayout()
        self.centerpt_distance_form_layout.addWidget(self.df_center_point_location)
        self.centerpt_distance_form_layout.setAlignment(Qt.AlignTop)
         
        self.centerpt_distanceLayout     =   QHBoxLayout()
        self.centerpt_distanceLayout.addLayout(self.centerpt_distance_notesLayout) 
        self.centerpt_distanceLayout.addLayout(self.centerpt_distance_form_layout)       
        self.centerpt_distanceLayout.setAlignment(Qt.AlignTop)

        from PyQt5.QtWidgets import  QVBoxLayout
        self.df_center_Layout     =   QVBoxLayout()
        self.df_center_Layout.addLayout(self.centerpt_distanceLayout)
        self.df_center_Layout.addStretch()
        
        self.setLayout(self.df_center_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][init_form] end")


    def select_Distance_From_Center_Point_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  Geocode_Distance_From_Center_Point_Widget][select_Distance_From_Center_Point_df]")
        
        dftitle     =   self.df_center_point_location.get_form_input_value_by_index(0)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df          =   get_dfc_dataframe_df(dftitle)
        dfcols      =   df.columns.tolist()

        self.df_center_point_location.reset_form_combobox_by_index(2, dfcols)    

    def select_Distance_From_Center_Point_col(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][select_Distance_From_Center_Point_col]")

        dfcol     =   self.df_center_point_location.get_form_input_value_by_index(2)
        self.df_center_point_location.set_form_input_value_by_index(1,dfcol)


    def select_center_pt_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  Geocode_Distance_From_Center_Point_Widget][select_center_pt_df]")
        
        dftitle     =   self.df_center_point_location.get_form_input_value_by_index(3)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df          =   get_dfc_dataframe_df(dftitle)
        dfcols      =   df.columns.tolist()

        self.df_center_point_location.reset_form_combobox_by_index(4, dfcols)    

    def select_ctpt_col(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][select_ctpt_col]")

        dfctptcol     =   self.df_center_point_location.get_form_input_value_by_index(5)
        self.df_center_point_location.set_form_input_value_by_index(4,dfctptcol)

    def calculate_dist_from_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][calculate_dist_from_center_point]")

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_df_distances_from_center_point
        parms   =   []
        parms.append(self.df_center_point_location.get_form_input_value_by_index(0))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(1))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(3)) 
        parms.append(self.df_center_point_location.get_form_input_value_by_index(4))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(6)) 
        parms.append(self.df_center_point_location.get_form_input_value_by_index(7))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(8))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(9)) 

        center_pt_distances     =   process_calculate_df_distances_from_center_point(parms)        
        
        if(not (center_pt_distances is None)) :

            cfg_parms   =   []
            cfg_parms.append(parms[0])
            cfg_parms.append(parms[1])
            cfg_parms.append(self.df_center_point_location.get_form_input_value_by_index(2))
            cfg_parms.append(parms[2])
            cfg_parms.append(parms[3])
            cfg_parms.append(self.df_center_point_location.get_form_input_value_by_index(5))
            cfg_parms.append(parms[4])            
            cfg_parms.append(parms[5])
            cfg_parms.append(parms[6])
            cfg_parms.append(parms[7])

            from dfcleanser.common.cfg import set_config_value
            set_config_value(df_dist_from_center_utility_input_id+"Parms",cfg_parms)

            from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
            df              =   get_dfc_dataframe_df(parms[0])
            df[parms[4]]    =   center_pt_distances

            set_dfc_dataframe_df(parms[0],df)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[calculate_dist_from_center_point] new distance column added"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)
   
   
    def get_point_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][get_point_input]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(USER_LOCATION)

    def get_closest_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][get_closest_input]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import CENTER_POINT_LIST_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(CENTER_POINT_LIST_LOCATION)
    
    def return_from_df_dist_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][return_from_df_dist_center_point]")
        
        self.parent.display_geocoding_utilities()        


    def help_for_df_dist_center_point(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][help_for_df_dist_center_point]")
        
        self.parent.display_geocoding_utilities()    


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -        Geocode Distance from Closest Point Location           -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Geocode_Distance_From_Closest_Point_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Distance_From_Closest_Point_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Distance_From_Closest_Point_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Closest_Point_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        spacer_label   =   QLabel()
        spacer_label.setText("\n")
        spacer_label.setAlignment(Qt.AlignCenter)
        spacer_label.setStyleSheet("font-size: 12px; font-weight:bold; font-family: Arial;")

        text1       =   "If GeoLocation is defined by \na single column\nselect a single column"
        text_delim  =   "\n---------------------------------------\n" 
        text2       =   "If GeoLocation is defined by \n a Latitude column and \n a Longitude column\ndefine the columns\nas [LatColumn,LngColumn]"
        label_text  =   text1 + text_delim + text2

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout
        title_label   =   QLabel()
        title_label.setText(label_text)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; font-weight:normal; background-color:#ffffcc; font-family: Arial; border: 1px solid black;")

        form_parms      =   [df_dist_from_closest_utility_input_id,df_dist_from_closest_utility_input_idList,df_dist_from_closest_utility_input_labelList,
                             df_dist_from_closest_utility_input_typeList, df_dist_from_closest_utility_input_placeholderList,df_dist_from_closest_utility_input_reqList]
        
        selectDicts     =   []
    
        dfs             =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dfs         =   get_dfc_dataframes_titles_list()
        df_sel      =   {"default":dfs[0],"list":dfs}
        selectDicts.append(df_sel)
        
        df          =   get_dfc_dataframe_df(dfs[0])
        dfcols      =   df.columns.tolist()
        cols_sel    =   {"default":dfcols[0],"list":dfcols}
        selectDicts.append(cols_sel)

        distsel           =   {"default":"Closest","list": ["Closest","Farthest"]}
        selectDicts.append(distsel)

        unitssel           =   {"default":"km","list": ["km","miles"]}
        selectDicts.append(unitssel)
        algssel           =   {"default":"geodesic","list": ["geodesic","great_circle"]}
        selectDicts.append(algssel)
        aelipsoidsel           =   {"default":"WGS-84","list": ["WGS-84","GRS-80","Airy (1830)","intl 1924","Clarke (1880)","GRS-67"]}
        selectDicts.append(aelipsoidsel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_Closest_Point_df,self.select_Closest_Point_col,None,None,None,None]
        file_methods    =   None
        button_methods  =   [self.calculate_dist_from_points_list,self.get_point_input,self.get_center_input,self.return_from_points_list,self.help_for_points_list]
        cfg_parms       =   None
        form_title      =   "\n\nGet Distance From Center Point to df Column Values\n"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_center_point_location   =   dfcleanser_input_form_Widget(form_parms)


        print("self.df_center_point_location",self.df_center_point_location)

        from PyQt5.QtWidgets import QScrollArea
        self.list_scroll     =   QScrollArea()

        self.list_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.list_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_scroll.setWidgetResizable(True)

        self.df_center_point_location.setFixedWidth(760)

        self.list_scroll.setWidget(self.df_center_point_location)
        self.list_scroll.setFixedHeight(660)
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Distance_From_Center_Point_Widget] list_location built")

        self.centerpt_distance_notesLayout  =   QVBoxLayout()
        self.centerpt_distance_notesLayout.addWidget(spacer_label)
        self.centerpt_distance_notesLayout.addWidget(title_label)
        self.centerpt_distance_notesLayout.addStretch()
        self.centerpt_distance_notesLayout.setAlignment(Qt.AlignTop)

        self.centerpt_distance_form_layout  =   QVBoxLayout()
        self.centerpt_distance_form_layout.addWidget(spacer_label)
        #self.centerpt_distance_form_layout.addWidget(self.df_center_point_location)
        self.centerpt_distance_form_layout.addWidget(self.list_scroll)
        self.centerpt_distance_form_layout.setAlignment(Qt.AlignTop)
         
        self.centerpt_distanceLayout     =   QHBoxLayout()
        self.centerpt_distanceLayout.addLayout(self.centerpt_distance_notesLayout) 
        self.centerpt_distanceLayout.addLayout(self.centerpt_distance_form_layout)       
        self.centerpt_distanceLayout.setAlignment(Qt.AlignTop)

        from PyQt5.QtWidgets import  QVBoxLayout
        self.df_center_Layout     =   QVBoxLayout()
        self.df_center_Layout.addLayout(self.centerpt_distanceLayout)
        self.df_center_Layout.addStretch()
        
        self.setLayout(self.df_center_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][init_form] end")


    def select_Closest_Point_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  Geocode_Distance_From_Center_Point_Widget][select_Closest_Point_df]")
        
        dftitle     =   self.df_center_point_location.get_form_input_value_by_index(0)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df          =   get_dfc_dataframe_df(dftitle)
        dfcols      =   df.columns.tolist()

        self.df_center_point_location.reset_form_combobox_by_index(2, dfcols)    

    def select_Closest_Point_col(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][select_Closest_Point_col]")

        dfcol     =   self.df_center_point_location.get_form_input_value_by_index(2)
        self.df_center_point_location.set_form_input_value_by_index(1,dfcol)

    def calculate_dist_from_points_list(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Closest_Point_Widget][calculate_dist_from_points_list]")

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import process_calculate_df_distances_from_list_points
        parms   =   []
        parms.append(self.df_center_point_location.get_form_input_value_by_index(0))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(1))
        parms_locations     =  self.df_center_point_location.get_form_input_value_by_index(3).replace("\\n","") 
        parms.append(parms_locations) 
        parms_names         =  self.df_center_point_location.get_form_input_value_by_index(4).replace("\\n","") 
        parms.append(parms_names)
        parms.append(self.df_center_point_location.get_form_input_value_by_index(5))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(6)) 
        parms.append(self.df_center_point_location.get_form_input_value_by_index(7))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(8))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(9)) 
        parms.append(self.df_center_point_location.get_form_input_value_by_index(10))
        parms.append(self.df_center_point_location.get_form_input_value_by_index(11)) 

        list_pt_distances_data     =   process_calculate_df_distances_from_list_points(parms)        
        
        if(not (list_pt_distances_data is None)) :

            list_points_distance_values     =   list_pt_distances_data[0]
            list_points_locations           =   list_pt_distances_data[1]
            list_points_names               =   list_pt_distances_data[2]

            cfg_parms   =   []
            cfg_parms.append(parms[0])
            cfg_parms.append(parms[1])
            cfg_parms.append(self.df_center_point_location.get_form_input_value_by_index(2))
            cfg_parms.append(parms[2])
            cfg_parms.append(parms[3])
            cfg_parms.append(parms[4])            
            cfg_parms.append(parms[5])
            cfg_parms.append(parms[6])
            cfg_parms.append(parms[7])
            cfg_parms.append(parms[8])            
            cfg_parms.append(parms[9])
            cfg_parms.append(parms[10])

            from dfcleanser.common.cfg import set_config_value
            set_config_value(df_dist_from_closest_utility_input_id+"Parms",cfg_parms)

            #return()

            from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
            df              =   get_dfc_dataframe_df(parms[0])
            df[parms[4]]    =   list_points_distance_values
            df[parms[5]]    =   list_points_locations
            df[parms[6]]    =   list_points_names

            set_dfc_dataframe_df(parms[0],df)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[calculate_dist_from_points_list] new columns added"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)
   
   
    def get_point_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][get_point_input]")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(USER_LOCATION)

    def get_center_input(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][get_center_input]")
        
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DF_CENTER_POINT_LOCATION
        self.parent.display_geocoding_distance_from_fixed_location(DF_CENTER_POINT_LOCATION)
    
    def return_from_points_list(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][return_from_points_list]")
        
        self.parent.display_geocoding_utilities()        


    def help_for_points_list(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Distance_From_Center_Point_Widget][help_for_points_list]")
        
        self.parent.display_geocoding_utilities()    


# -----------------------------------------------------------------#
# -                Geocode Split Location Widget                  -#
# -----------------------------------------------------------------#
class Geocode_Split_Column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Split_Column_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Split_Column_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout

        form_parms      =   [dfc_split_column_utility_input_id,dfc_split_column_utility_input_idList,dfc_split_column_utility_input_labelList,
                             dfc_split_column_utility_input_typeList,dfc_split_column_utility_input_placeholderList,dfc_split_column_utility_input_reqList]

        selectDicts     =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dataframes      =   get_dfc_dataframes_titles_list()
        dfsel           =   {"default":dataframes[0],"list": dataframes}
        selectDicts.append(dfsel)

        df              =   get_dfc_dataframe_df(dataframes[0])
        df_cols         =   df.columns.tolist() 
        colssel         =   {"default":df_cols[0],"list": df_cols} 
        selectDicts.append(colssel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_df,self.select_split_column]
        file_methods    =   None
        button_methods  =   [self.split_location,self.return_split_location,self.help_split_location]
        cfg_parms       =   None
        form_title      =   "\n\nSplit Lat_Lng Column"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.split_column_form    =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Split_Column_Widget] split_column_form built")
        
        self.split_Layout     =   QVBoxLayout()
        self.split_Layout.addWidget(self.split_column_form)
        self.split_Layout.addStretch()
        
        self.setLayout(self.split_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][init_form] end")

    def select_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][select_dfc]")

        new_df  =   self.split_column_form.get_form_input_value_by_index(0)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df              =   get_dfc_dataframe_df(new_df)
        df_cols         =   df.columns.tolist() 

        self.split_column_form.set_form_input_value_by_index(1,df_cols[0])
        self.split_column_form.reset_form_combobox_by_index(2,df_cols)

    def select_split_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][select_from_column]")

        new_from_col  =   self.split_column_form.get_form_input_value_by_index(2)
        self.split_column_form.set_form_input_value_by_index(1,new_from_col)

    def split_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][split_location]")

    def return_split_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][return_split_location]")

        self.parent.display_geocoding_utilities()        

    def help_split_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Split_Column_Widget][help_split_location]")

        self.parent.display_geocoding_utilities()        



# -----------------------------------------------------------------#
# -                Geocode Join Location Widget                  -#
# -----------------------------------------------------------------#
class Geocode_Join_Columns_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("\n[Geocode_Join_Columns_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget] dftitle ; ")

        self.init_form()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Join_Columns_Widget] end")

    def init_form(self):  

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout

        form_parms      =   [dfc_join_column_utility_input_id,dfc_join_column_utility_input_idList,dfc_join_column_utility_input_labelList,
                             dfc_join_column_utility_input_typeList,dfc_join_column_utility_input_placeholderList,dfc_join_column_utility_input_reqList]

        selectDicts     =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
        dataframes      =   get_dfc_dataframes_titles_list()
        dfsel           =   {"default":dataframes[0],"list": dataframes}
        selectDicts.append(dfsel)

        df              =   get_dfc_dataframe_df(dataframes[0])
        df_cols         =   df.columns.tolist() 
        colssel         =   {"default":df_cols[0],"list": df_cols} 
        selectDicts.append(colssel)
        selectDicts.append(colssel)

        comboList       =   selectDicts
        comboMethods    =   [self.select_df,self.select_join_lat_column,self.select_join_lng_column]
        file_methods    =   None
        button_methods  =   [self.join_location,self.return_join_location,self.help_join_location]
        cfg_parms       =   None
        form_title      =   "\n\nJoin Lat Lng Columns"
        form_width      =   800
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.join_column_form    =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("[Geocode_Join_Columns_Widget] split_column_form built")
        
        self.join_Layout     =   QVBoxLayout()
        self.join_Layout.addWidget(self.join_column_form)
        self.join_Layout.addStretch()
        
        self.setLayout(self.join_Layout)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][init_form] end")

    def select_df(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][select_dfc]")

        new_df  =   self.join_column_form.get_form_input_value_by_index(0)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df              =   get_dfc_dataframe_df(new_df)
        df_cols         =   df.columns.tolist() 

        self.join_column_form.set_form_input_value_by_index(1,df_cols[0])
        self.join_column_form.reset_form_combobox_by_index(2,df_cols)

        self.join_column_form.set_form_input_value_by_index(3,df_cols[0])
        self.join_column_form.reset_form_combobox_by_index(4,df_cols)
       

    def select_join_lat_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][select_join_lat_column]")

        new_from_col  =   self.join_column_form.get_form_input_value_by_index(2)
        self.join_column_form.set_form_input_value_by_index(1,new_from_col)

    def select_join_lng_column(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][select_join_lng_column]")

        new_from_col  =   self.join_column_form.get_form_input_value_by_index(4)
        self.join_column_form.set_form_input_value_by_index(3,new_from_col)


    def join_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][join_location]")

    def return_join_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][return_join_location]")

        self.parent.display_geocoding_utilities()        

    def help_join_location(self) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            print("  [Geocode_Join_Columns_Widget][help_join_location]")

        self.parent.display_geocoding_utilities()        

