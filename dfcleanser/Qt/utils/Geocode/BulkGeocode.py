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

DEBUG_GEOCODE_BULK  =   False


import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp

import dfcleanser.Qt.utils.Geocode.BulkGeocodeModel as BGM

from dfcleanser.common.html_widgets import (maketextarea, InputForm)
from dfcleanser.common.common_utils import (get_parms_for_input, display_generic_grid, opStatus, get_select_defaults, display_blank_line)

from dfcleanser.Qt.utils.Geocode.GeocodeModel import (BingId, GoogleId, BaiduId, BULK, QUERY, REVERSE, BULK_TUNING, ArcGISId)  

from dfcleanser.common.common_utils import log_debug_dfc

from dfcleanser.sw_utilities.DFCDataStores import get_Dict

import googlemaps

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google geocoder parms
#--------------------------------------------------------------------------
"""

google_bulk_geocoder_title               =   "Google V3 Bulk Geocoder Connector"
google_bulk_geocoder_id                  =   "googlebulkgeocoder"

google_bulk_geocoder_idList              =    ["ggbapikey",
                                               "ggbclient",
                                               "ggbclientsecret",
                                               "ggbtimeout",
                                               "ggbconnecttimeout",
                                               "ggbreadtimeout",
                                               "ggbretrytimeout",
                                               "ggbqueriespersecond",
                                               "ggbretryoverquerylimit",
                                               "ggbchannel",
                                               "ggbrequestskwargs",
                                               None,None,None,None,None,None]

google_bulk_geocoder_labelList           =   ["api_key",
                                              "client_id",
                                              "client_secret",
                                              "timeout",
                                              "connect_timeout",
                                              "read_timeout",
                                              "retry_timeout",
                                              "queries_per_second",
                                              "retry_over_query_limit",
                                              "channel",
                                              "requests_kwargs",
                                              "Test</br>Bulk</br>Geocoder</br>Connection",
                                              "Bulk</br>Geocoding",
                                              "Bulk</br>Reverse</br>Geocoding",
                                              "Bulk</br>Geocoding</br>Tuning",
                                              "Return","Help"]


google_bulk_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","select","text","text",
                                              "button","button","button","button","button","button"]

google_bulk_geocoder_placeholderList     =   ["enter account api key.",
                                              "enter account client id. (default - None) required for premier",
                                              "enter account client secret. (default - None) required for premier",
                                              "Combined overall timeout for HTTP requests, in seconds. (default - None)",
                                              "Connection timeout in seconds. (default - None)",
                                              "Read(HTTP) timeout in seconds. (default - None)",
                                              "Retry(HTTP) timeout in seconds. (default - None)",
                                              "Number of queries per second permitted (default 25 - Max 50)",
                                              "retry over query limit flag (default - False)",
                                              "channel parameter (default - None)",
                                              "Keyword args -http://docs.python-requests.org/en/latest/api/#main-interface ",
                                              None,None,None,None,None,None]

google_bulk_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(GoogleId) + "," + str(BULK) + ")",
                                              "display_geocoding_query_callback(" + str(GoogleId) + ")",
                                              "display_geocoding_reverse_callback(" + str(GoogleId)  +  ")",
                                              "display_bulk_tuning(" + str(GoogleId) + "," + str(BULK_TUNING) + ")",
                                              "geocode_return()",
                                              "display_help_url('"+str(dfchelp.GoogleInitHelp)+"')"]

google_bulk_geocoder_reqList             =   [0,1,2,3]


google_API_Key    =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"


"""
#--------------------------------------------------------------------------
#    google geocode bulk query form 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqdataframe",
                                               "bgqstartrow",
                                               "bgqaddress",
                                               "bgqcolumnname",
                                               "bgqsaveaddress",
                                               "bgqregion",
                                               "bgqlanguage",
                                               "bgqbulknumberlimit",
                                               "bgqbulkfailurelimit",
                                               "bgqbulkcheckpoint",
                                               None,None,None,None]

bulk_google_query_input_labelList         =   ["dataframe_to_geocode_from",
                                               "starting_row_id",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "region",
                                               "language",
                                               "max_addresses_to_geocode",
                                               "failure_limit_percent",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Display</br>Bulk</br>Reverse</br>Geocoding",
                                               "Return","Help"]

bulk_google_query_input_typeList          =   ["select","text",maketextarea(2),"select","text",
                                               "select","select","text","text","text",
                                               "button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["dataframe to geocode",
                                              "row id to start geocoding from",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "[Latitude,Longitude] - stored as 2 columns  - [LatitudeLongitude] stored as one col",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "region (default - None)",
                                              "language (default - english)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                              "check point interval (default - every 10,000 rows)",
                                               None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_query_callback(" + str(GoogleId) + ")",
                                               "display_geocoding_reverse_callback(" + str(GoogleId) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_query_input_reqList           =   [0,1,2,3,4]




"""
#--------------------------------------------------------------------------
#    google geocode adjust bulk query parms 
#--------------------------------------------------------------------------
"""
bulk_google_query_adjust_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_adjust_input_id                =   "googleadjustbulkquery"
bulk_google_query_adjust_input_idList            =   ["bgqadjcolumnname",
                                                      "bgqadjerrors",
                                                      "bgqadjempty",
                                                      "bgqadjfulladdr",
                                                       None,None]

bulk_google_query_adjust_input_labelList         =   ["new_dataframe_lat_long_column_name(s)",
                                                      "lat_long_column_value_for_errors",
                                                      "lat_long_column_value_for_empty_values",
                                                      "retrieved_full_address_column_name",
                                                      "Merge With user df",
                                                      "Return"]

bulk_google_query_adjust_input_typeList          =   ["text","text","text","text","button","button"]

bulk_google_query_adjust_input_placeholderList   =  ["[Latitude,Longitude] - stored as 2 columns  - [LatitudeLongitude] stored as one col",
                                                     "[Latitude,Longitude] error value",
                                                     "default '",
                                                     "Rtrieved full_address olumn name", 
                                                     None,None]

bulk_google_query_adjust_input_jsList            =   [None,None,None,None,
                                                    "merge_query_geocoding_results(" + str(GoogleId) + ")",
                                                    "controlbulkrun(26)"]

bulk_google_query_adjust_input_reqList           =   [0,1,2,3]



"""
#--------------------------------------------------------------------------
#    google reverse bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_reverse_input_title           =   "Google Bulk Reverse Parameters"
bulk_google_reverse_input_id              =   "googlebulkreverse"
bulk_google_reverse_input_idList          =   ["bgrdataframe",
                                               "bgrstartrow",
                                               "bgrcolumnname",
                                               "bgrcolumnnames",
                                               "bgraddresscomponents",
                                               "bgraddresslength",
                                               "bgqloctypes",
                                               "bgrlanguage",
                                               "bgrbulknumberlimit",
                                               "bgrbulkfailurelimit",
                                               "bgrbulkcheckpoint",
                                               None,None,None,None]

bulk_google_reverse_input_labelList       =   ["dataframe_to_geocode_from",
                                               "starting_row_id",
                                               "dataframe_lat_long_column_name(s)",
                                               "full_address_column_name",
                                               "address_components_list",
                                               "address_components_length_flag",
                                               "valid_location_type(s)",
                                               "language",
                                               "max_lat_longs",
                                               "failure_limit_percent",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Addresses",
                                               "Display</br>Bulk</br>Coords",
                                               "Return","Help"]

bulk_google_reverse_input_typeList        =   ["select","text","text","text",maketextarea(2),"select","text",
                                               "select","text","text","text",
                                               "button","button","button","button"]

bulk_google_reverse_input_placeholderList =  ["datframe to geocode from",
                                              "starting row id to geocode from",
                                              "lat long colname(s) - latitudfe, longitude - 2 cols [latcolname,longcolname] 1 col",
                                              "single address column name to store full address",
                                              "address components list (default = None - store full address in address_column_name(s))",
                                              "address components short length (default = True) False = Long)",
                                              "A filter of one or more location types to accept as valid (default - ALL)",
                                              "language (default - english)",
                                              "number of lat_lngs to get addresses for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None]

bulk_google_reverse_input_jsList          =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_reverse_callback(" + str(GoogleId) + ")",
                                               "display_geocoding_query_callback(" + str(GoogleId) + ")",
                                               "geocode_return()",
                                               "display_help_url('"+str(dfchelp.GoogleQueryHelp)+"')"]

bulk_google_reverse_input_reqList         =   [0,1,2,3,4,5,6]



"""
#--------------------------------------------------------------------------
#    google geocode adjust bulk query parms 
#--------------------------------------------------------------------------
"""
bulk_google_reverse_adjust_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_reverse_adjust_input_id                =   "googlebulkreverseadjust"
bulk_google_reverse_adjust_input_idList            =   ["bgradjfullname",
                                                        "bgradjaddrerror",
                                                        "bgradjaddrempty",
                                                        "bgradjaddrcomps",
                                                        None,None]

bulk_google_reverse_adjust_input_labelList         =   ["retrieved_full_address_column_name",
                                                        "full_address_column_value_for_errors",
                                                        "full_address_column_value_for_empty_values",
                                                        "retrieved_address_components_column_names",
                                                        "Merge With user df",
                                                        "Return"]

bulk_google_reverse_adjust_input_typeList          =   ["text","text","text",maketextarea(3),"button","button"]

bulk_google_reverse_adjust_input_placeholderList   =  ["full address column name ",
                                                       "full address error column value ",
                                                       "full address emoty column value ",
                                                       "address comps column names",
                                                        None,None]

bulk_google_reverse_adjust_input_jsList            =   [None,None,None,None,
                                                        "merge_reverse_geocoding_results(" + str(GoogleId) + ")",
                                                        "controlbulkrun(26)",]

bulk_google_reverse_adjust_input_reqList           =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   bing geocoder parms
#--------------------------------------------------------------------------
"""
bing_bulk_geocoder_title                 =   "Bing Bulk Geocoder Connector"
bing_bulk_geocoder_id                    =   "bingbulkgeocoder"

bing_bulk_geocoder_idList                =    ["bingapikey",
                                               "bingagent",
                                               "bingtimeout",
                                               "bingfstring",
                                               "bingscheme",
                                               "bingproxies",
                                               None,None,None,None,None,None]

bing_bulk_geocoder_labelList             =   ["api_key",
                                               "user_agent",
                                               "timeout",
                                               "format_string",
                                               "scheme",
                                               "proxies",
                                               "Test</br>Geocoder</br>Connection",
                                               "Bulk</br>Query</br>Geocoding",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Display</br>Bulk</br>Geocoding</br>Tuning",
                                               "Return","Help"]


bing_bulk_geocoder_typeList              =   ["text","text","text","text","text","text",
                                              "button","button","button","button","button","button"]

bing_bulk_geocoder_placeholderList       =   ["enter Bing api key",
                                              "user agent (default - my-application)",
                                              "enter timeout in seconds (default 20)",
                                              "enter format string (default %s)",
                                              "enter scheme (default https)",
                                              "proxies dict (default None)",
                                              None,None,None,None,None,None]

bing_bulk_geocoder_jsList                 =   [None,None,None,None,None,None,
                                              "test_geocoder(" + str(BingId) + "," + str(BULK) + ")",
                                              "display_geocoding_query_callback(" + str(BingId) + ")",
                                              "display_geocoding_reverse_callback(" + str(BingId) + ")",
                                              "display_bulk_tuning(" + str(BingId) + "," + str(BULK_TUNING) + ")",
                                              "geocode_return()",
                                              "display_help_url('"+str(dfchelp.BingInitHelp )+"')"]
 
bing_bulk_geocoder_reqList               =   [0,1]

bing_bulk_API_Key    =   "AhwVfAKfw8CF4K2cwNgfj61-jYzQll4N92sjC6d3Hz-9O4HdCB34MwGObvhoJwB4"


"""
#--------------------------------------------------------------------------
#    bing bulk query form
#--------------------------------------------------------------------------
"""
bulk_bing_query_input_title               =   "Bing Bulk Geoocoding Parameters"
bulk_bing_query_input_id                  =   "bingbulkquery"
bulk_bing_query_input_idList              =   ["bbgdataframe",
                                               "bbgrowid",
                                               "bbqaddress",
                                               "bbqcolumnname",
                                               "bbqsaveaddress",
                                               "bbquserloc",
                                               "bbqculture",
                                               "bbqneighborhood",
                                               "bbqcountrycode",
                                               "bbqbulknumberlimit",
                                               "bbqbulkfailurelimit",
                                               "bbqbulkcheckpoint",
                                               None,None,None,None]

bulk_bing_query_input_labelList           =   ["dataframe_to_geocode",
                                               "starting_row_id",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "user_location",
                                               "culture",
                                               "include_neighborhood",
                                               "include_country_code",
                                               "max_addresses_to_geocode",
                                               "failure_limit_percent",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Display</br>Bulk</br>Reverse</br>Geocoding",
                                               "Return","Help"]

bulk_bing_query_input_typeList            =   ["select","text",maketextarea(2),"select","text","text",
                                               "select","select","select","text","text","text",
                                               "button","button","button","button"]

bulk_bing_query_input_placeholderList     =  ["dataframe to geocode",
                                              "row id to start geocoding from",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "[Latitude,Longitude] - stored as 2 columns  - [LatitudeLongitude] stored as one col",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "prioritize result closest to user_location [lat,lng] (default - None)",
                                              "culture (default - en)",
                                              "include neighborhood in response (default - False)",
                                              "include country code in response (default - False)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None]

bulk_bing_query_input_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_query_callback(" + str(BingId) + ")",
                                               "display_geocoding_reverse_callback(" + str(BingId) + ")",
                                               "geocode_return()",
                                               "display_help_url('"+str(dfchelp.GoogleQueryHelp )+"')"]

bulk_bing_query_input_reqList             =   [0,1,2,3]



"""
#--------------------------------------------------------------------------
#    bing bulk adjust query form
#--------------------------------------------------------------------------
"""
bulk_bing_query_adjust_input_title               =   "Bing Bulk Geoocoding Parameters"
bulk_bing_query_adjust_input_id                  =   "bingbulkadjustquery"
bulk_bing_query_adjust_input_idList              =   ["bbqcolumnname",
                                                      "bbqerrors",
                                                      "bbqempty",
                                                      "bbqfulladdr",
                                                      None,None]

bulk_bing_query_adjust_input_labelList           =   ["new_dataframe_lat_long_column_name(s)",
                                                      "lat_long_column_value_for_errors",
                                                      "lat_long_column_value_for_empty_values",
                                                      "retrieved_full_address_column_name",
                                                      "Merge With user df",
                                                      "Return"]

bulk_bing_query_adjust_input_typeList            =   ["text","text","text","text","button","button"]

bulk_bing_query_adjust_input_placeholderList     =  ["[Latitude,Longitude] - stored as 2 columns  - [LatitudeLongitude] stored as one col",
                                                     "[Latitude,Longitude] error value",
                                                     "[Latitude,Longitude] empty value",
                                                     "Retrieved Full address",
                                                     None,None]


bulk_bing_query_adjust_input_jsList              =   [None,None,None,None,
                                                      "merge_query_geocoding_results(" + str(BingId) + ")",
                                                      "controlbulkrun(26)"]

bulk_bing_query_adjust_input_reqList             =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#    bing bulk reverse form
#--------------------------------------------------------------------------
"""
bulk_bing_reverse_input_title             =   "Bing Bulk Geoocoding Parameters"
bulk_bing_reverse_input_id                =   "bingbulkreverse"
bulk_bing_reverse_input_idList            =   ["bbrdataframe",
                                               "bbrstartrow",
                                               "bbrcolumnname",
                                               "bbraddrcol",
                                               "bbraddrcomps",
                                               "bbrculture",
                                               "bbrcountrycode",
                                               "bbrbulknumberlimit",
                                               "bbrbulkfailurelimit",
                                               "bbrbulkcheckpoint",
                                               None,None,None,None]

bulk_bing_reverse_input_labelList         =   ["dataframe_to_geocode",
                                               "starting_row_id",
                                               "dataframe_lat_long_column_name(s)",
                                               "dataframe_column_name_for_geocode_address",
                                               "address_components_to_retrieve",
                                               "culture",
                                               "include_country_code",
                                               "max_lat_longs",
                                               "failure_limit_percent",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Addresses",
                                               "Display</br>Bulk</br>Query</br>Geocoding",
                                               "Return","Help"]

bulk_bing_reverse_input_typeList          =   ["select","text",maketextarea(1),"text","select",
                                               "select","select","text","text","text",
                                               "button","button","button","button"]

bulk_bing_reverse_input_placeholderList   =  ["dataframe to geocode",
                                              "row id to start geocoding from",
                                              "lat long colname(s) - latitudfe, longitude - 2 cols [latcolname,longcolname] - 1 col",
                                              "dataframe column name to store address",
                                              "select address components",
                                              "culture (default - en)",
                                              "include country code in response (default - False)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None]

bulk_bing_reverse_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_reverse_callback(" + str(BingId) + ")",
                                               "display_geocoding_query_callback(" + str(BingId) + ")",
                                               "geocode_return()",
                                               "display_help_url('"+str(dfchelp.GoogleQueryHelp )+"')"]

bulk_bing_reverse_input_reqList           =   [0,1,2,3]

SWUtility_bulk_geocode_inputs             =   [google_bulk_geocoder_id, bulk_google_query_input_id, bulk_google_reverse_input_id,
                                               bing_bulk_geocoder_id, bulk_bing_query_input_id, bulk_bing_reverse_input_id]


"""
#--------------------------------------------------------------------------
#    bing geocode adjust bulk reverse parms 
#--------------------------------------------------------------------------
"""
bulk_bing_reverse_adjust_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_bing_reverse_adjust_input_id                =   "bingbulkreverseadjust"
bulk_bing_reverse_adjust_input_idList            =   ["bgradjcolumnname",
                                                      "bgradjerrors",
                                                      "bgradjaddrempty",
                                                      "bgradjaddrcomps",
                                                      None,None]

bulk_bing_reverse_adjust_input_labelList         =   ["retrieved_full_address_column_name",
                                                      "full_address_column_value_for_errors",
                                                      "full_address_column_value_for_empty_values",
                                                      "retrieved_address_components_column_names",
                                                      "Merge With user df",
                                                      "Return"]

bulk_bing_reverse_adjust_input_typeList          =   ["text","text","text",maketextarea(3),"button","button"]

bulk_bing_reverse_adjust_input_placeholderList   =  ["full address column name ",
                                                     "full address error column value ",
                                                     "full address emoty column value ",
                                                     "address comps column names",
                                                      None,None]

bulk_bing_reverse_adjust_input_jsList            =   [None,None,None,None,
                                                        "merge_reverse_geocoding_results(" + str(BingId) + ")",
                                                        "controlbulkrun(26)"]

bulk_bing_reverse_adjust_input_reqList           =   [0,1,2,3]




"""
#--------------------------------------------------
#--------------------------------------------------
#    bulk tuning objects
#--------------------------------------------------
#--------------------------------------------------
"""


"""
#------------------------------------------------
#    bulk tune input form
#------------------------------------------------
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
                                                      "process_bulk_tuning()",
                                                      "display_bulk_tuning()",
                                                      "geocode_return()",
                                                      "displayhelp('" + str(dfchelp.GEOCODING_UTILITIES_TASKBAR_ID) + "')"]

bulk_tune_utility_input_reqList                 =   [0,1]


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

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geocoder_title

    geocoders.append(get_geocoder_title(ArcGISId))  
    geocoders.append(get_geocoder_title(BaiduId))  
    geocoders.append(get_geocoder_title(BingId))  
    geocoders.append(get_geocoder_title(GoogleId))  

    geocid  =   cfg.get_config_value("currentGeocoder")
    if(geocid == None) :
        geocdefault     =   get_geocoder_title(GoogleId)
    else :
        geocdefault     =   get_geocoder_title(geocid)
    
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

    display_blank_line()
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Bulk Geocoder display methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def display_bulk_geocoders(geocodeid,showfull=True,with_status=None) :
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

    from dfcleanser.common.cfg import is_a_dfc_dataframe_loaded
    if(not (is_a_dfc_dataframe_loaded())) :
        
        title       =   "dfcleanser error"       
        status_msg  =   "[display_bulk_geocoders] no dfs are imported "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import display_bulk_splash
        display_bulk_splash()

        return

    if( not ((geocodeid == BingId) or (geocodeid == GoogleId)) ) :
        geocodeid    =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocodeid is None) :
            geocodeid   =   BingId   
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,BingId)  

    geocoder_input_form = None
    
    if(geocodeid == GoogleId) :

        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,GoogleId)

        geocoder_input_form   =   InputForm(google_bulk_geocoder_id,
                                            google_bulk_geocoder_idList,
                                            google_bulk_geocoder_labelList,
                                            google_bulk_geocoder_typeList,
                                            google_bulk_geocoder_placeholderList,
                                            google_bulk_geocoder_jsList,
                                            google_bulk_geocoder_reqList)
        
        selectDicts     =   []   
            
        retry_flag     =   {"default" : "False",
                            "list" : ["True","False"]}
        selectDicts.append(retry_flag)

        get_select_defaults(geocoder_input_form,
                            google_bulk_geocoder_id,
                            google_bulk_geocoder_idList,
                            google_bulk_geocoder_typeList,
                            selectDicts)
        
    else :

        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,BingId)

        geocoder_input_form   =   InputForm(bing_bulk_geocoder_id,
                                            bing_bulk_geocoder_idList,
                                            bing_bulk_geocoder_labelList,
                                            bing_bulk_geocoder_typeList,
                                            bing_bulk_geocoder_placeholderList,
                                            bing_bulk_geocoder_jsList,
                                            bing_bulk_geocoder_reqList)
    
 
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import display_bulk_splash
    display_bulk_splash()

    if(geocodeid == GoogleId) :
        geocode_heading_html =   "<br><div width=90%; class='dfcleanser-common-grid-header';>Google Bulk Geocoder Parameters </div><br>" 
    else :      
        geocode_heading_html =   "<br><div width=90%; class='dfcleanser-common-grid-header';>Bing Bulk Geocoder Parameters </div><br>"

    from dfcleanser.common.common_utils import displayHTML
    displayHTML(geocode_heading_html)
 
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_geocoders_table 
    geocoders_table   =   get_geocoders_table()
    
    geocoder_input_form.set_gridwidth(580)
    geocoder_input_form.set_custombwidth(90)

    geocoder_input_form.set_fullparms(True)

    geocode_input_html = ""
    geocode_input_html = geocoder_input_form.get_html()

    from dfcleanser.common.common_utils import display_generic_grid
    gridclasses     =   ["dfc-left","dfc-right"]
    gridhtmls       =   [geocoders_table,geocode_input_html]
                    
    display_generic_grid("df-geocode-geocoder-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.cfg import run_javascript
    run_javascript("window.scroll_to(11)","do scroll ")  

    # clear the debug log
    from dfcleanser.common.common_utils import (clear_dfc_debug_log)
    clear_dfc_debug_log()


# """
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#   bulk query objects
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# """



# """
# --------------------------------------------------------------------------
#   display bulk query
# --------------------------------------------------------------------------
# """

def display_bulk_query_geocoding(geocodeid) :
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

    if(BGM.GEOCODE_TRACE_DISPLAY_FORM) :

        log_debug_dfc(-1,"[display_bulk_reverse_geocoding] geocodeid " + str(geocodeid))
        log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_bing_query_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_bing_query_input_id+"Parms")))        
        log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_google_query_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_google_query_input_id+"Parms")))        

    from dfcleanser.common.common_utils import displayHTML
    
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import display_bulk_splash
    display_bulk_splash()

    if(geocodeid == GoogleId) :
        title = "Google"
    else :
        title = "Bing"
    geocode_heading_html =   "<br><div class='dfcleanser-common-grid-header'; width=820px;>" + title + " Query Bulk Geocoding Parameters</div><br>"

    displayHTML(geocode_heading_html)

    df_list     =   cfg.get_dfc_dataframes_titles_list()
    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
    if(default_df is None) :
        default_df  =   df_list[0]

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df          =   get_dfc_dataframe_df(default_df)

    if(geocodeid == GoogleId) :
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_column_names_table
        column_name_table   =   get_column_names_table(GoogleId,QUERY,df) 
        
        if(BGM.GEOCODE_TRACE_DISPLAY_FORM) :
            log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_google_query_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_google_query_input_id+"Parms")))        

        # build the input form
        from dfcleanser.common.html_widgets import InputForm
        geocoding_input_form   =   InputForm(bulk_google_query_input_id,
                                            bulk_google_query_input_idList,
                                            bulk_google_query_input_labelList,
                                            bulk_google_query_input_typeList,
                                            bulk_google_query_input_placeholderList,
                                            bulk_google_query_input_jsList,
                                            bulk_google_query_input_reqList)
        
        selectDicts     =   []   
            
        df_list     =   cfg.get_dfc_dataframes_titles_list()
        default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
        dataframes  =   {"default" : default_df,
                        "list" : df_list,
                        "callback" : "change_bulk_df"}
        selectDicts.append(dataframes)
            
        savecoords      =   {"default" : "[Latitude,Longitude]",
                            "list" : ["[Latitude,Longitude]","Latitude_Longitude"]}
        selectDicts.append(savecoords)

        from dfcleanser.sw_utilities.DFCDataStores import get_formatted_country_codes
        countries       =   get_formatted_country_codes()
        ccsel           =   {"default":countries[0],"list":countries}
        selectDicts.append(ccsel)
        
        languages       =   {}
        languages.update({"default": "English"})
            
        langdict        =   get_Dict("Language_Codes")
        languageslist   =   list(langdict.keys())
        languageslist.sort()
        languages.update({"list":languageslist})
        selectDicts.append(languages)
            
        get_select_defaults(geocoding_input_form,
                            bulk_google_query_input_id,
                            bulk_google_query_input_idList,
                            bulk_google_query_input_typeList,
                            selectDicts)

        geocoding_input_form.set_gridwidth(580)
        geocoding_input_form.set_custombwidth(120)
    
        geocoding_input_form.set_fullparms(True)

        geocoding_input_html = ""
        geocoding_input_html = geocoding_input_form.get_html() 

    else :

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_column_names_table
        column_name_table   =   get_column_names_table(BingId,QUERY,df) 

        if(BGM.GEOCODE_TRACE_DISPLAY_FORM) :
            log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_bing_query_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_bing_query_input_id+"Parms")))        


        # build the input form
        from dfcleanser.common.html_widgets import InputForm
        geocoding_input_form   =   InputForm(bulk_bing_query_input_id,
                                            bulk_bing_query_input_idList,
                                            bulk_bing_query_input_labelList,
                                            bulk_bing_query_input_typeList,
                                            bulk_bing_query_input_placeholderList,
                                            bulk_bing_query_input_jsList,
                                            bulk_bing_query_input_reqList)
        
        selectDicts     =   []   

        df_list     =   cfg.get_dfc_dataframes_titles_list()
        default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
        
        if(default_df is None) :
            default_df  =   df_list[0]
            
        dataframes  =   {"default" : default_df,
                        "list" : df_list,
                        "callback" : "change_bulk_df"}
        selectDicts.append(dataframes)
            
        savecoords      =   {"default" : "[Latitude,Longitude] ",
                            "list" : ["[Latitude,Longitude]","Latitude_Longitude"]}
        selectDicts.append(savecoords)

        from dfcleanser.sw_utilities.DFCDataStores import get_formatted_language_codes
        languages       =   get_formatted_language_codes()
        ccsel           =   {"default":languages[0],"list":languages}
        selectDicts.append(ccsel)

        includecomp     =   {"default" : "False",
                            "list" : ["True","False"]}
        selectDicts.append(includecomp)
        selectDicts.append(includecomp)
           
        get_select_defaults(geocoding_input_form,
                            bulk_bing_query_input_id,
                            bulk_bing_query_input_idList,
                            bulk_bing_query_input_typeList,
                            selectDicts)

        geocoding_input_form.set_gridwidth(580)
        geocoding_input_form.set_custombwidth(120)
    
        geocoding_input_form.set_fullparms(True)

        geocoding_input_html = ""
        geocoding_input_html = geocoding_input_form.get_html() 


    from dfcleanser.common.common_utils import display_generic_grid
    gridclasses     =   ["dfc-left","dfc-right"]
    gridhtmls       =   [column_name_table,geocoding_input_html]
                    
    display_generic_grid("df-geocode-bing-bulk-reverse-wrapper",gridclasses,gridhtmls)
    
    display_blank_line()
    from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html

    if(geocodeid == GoogleId) :
        
        msg     =   "You can add constants(single quotes) to 'dataframe_address_columns' field to refine the address. eg : Address + 'Los Angeles' + 'CA' "
        get_status_note_msg_html(msg, width=700, left=0, fontsize=12, display=True)

    else :
    
        msg     =   "You can add constants to 'dataframe_address_columns' field to refine the address. eg : Address + 'Los Angeles' + 'CA' "
        get_status_note_msg_html(msg, width=700, left=0,  fontsize=12, display=True)

        msg1     =   "You can define a geopoint [lat,lng] for the 'user_location' field to define the a geopoint that the adddress is closest to."
        get_status_note_msg_html(msg1, width=700, left=0,  fontsize=12, display=True)




# """
# --------------------------------------------------------------------------
#   display bulk reverse
# --------------------------------------------------------------------------
# """

def display_bulk_reverse_geocoding(geocodeid,tableid=None) :
    """
    * ---------------------------------------------------------
    * function : display geocoder reverse screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import displayHTML
    
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import display_bulk_splash
    display_bulk_splash()
    
    if(geocodeid == GoogleId) :
        title = "Google"
    else :
        title = "Bing"

    geocode_heading_html =   "<br><div class='dfcleanser-common-grid-header'; width=820px;>" + title + " Reverse Bulk Geocoding Parameters</div><br>"
    displayHTML(geocode_heading_html)

    df_list     =   cfg.get_dfc_dataframes_titles_list()
    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
    if(default_df is None) :
        default_df  =   df_list[0]
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df          =   get_dfc_dataframe_df(default_df)

    if(geocodeid == GoogleId) :

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_column_names_table
        column_name_table   =   get_column_names_table(GoogleId,REVERSE,df) 
        
        if(BGM.GEOCODE_TRACE_DISPLAY_FORM) :
            log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_google_reverse_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_google_reverse_input_id+"Parms")))        

        # build the input form
        from dfcleanser.common.html_widgets import InputForm
        geocoding_input_form   =   InputForm(bulk_google_reverse_input_id,
                                            bulk_google_reverse_input_idList,
                                            bulk_google_reverse_input_labelList,
                                            bulk_google_reverse_input_typeList,
                                            bulk_google_reverse_input_placeholderList,
                                            bulk_google_reverse_input_jsList,
                                            bulk_google_reverse_input_reqList)
        
        selectDicts  =   []

        df_list     =   cfg.get_dfc_dataframes_titles_list()
        default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)

        if(default_df is None) :
            default_df  =   df_list[0]

        dataframes  =   {"default" : default_df,
                        "list" : df_list,
                        "callback" : "change_bulk_query_df"}
        selectDicts.append(dataframes)

        lengthFlag      =   {"default":"short","list":["short","long"]}
        selectDicts.append(lengthFlag)
            
        languages       =   {}
        languages.update({"default": "English"})

        langdict        =   get_Dict("Language_Codes")
        languageslist   =   list(langdict.keys())
        languageslist.sort()
        languages.update({"list":languageslist})
        selectDicts.append(languages)
            
        get_select_defaults(geocoding_input_form,
                            bulk_google_reverse_input_id,
                            bulk_google_reverse_input_idList,
                            bulk_google_reverse_input_typeList,
                            selectDicts)
           
        geocoding_input_form.set_gridwidth(580)
        geocoding_input_form.set_custombwidth(110)
    
        geocoding_input_form.set_fullparms(True)

        geocoding_input_html = ""
        geocoding_input_html = geocoding_input_form.get_html() 


        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_address_components_table, get_location_types_table
        addr_comps_table    =   get_address_components_table(geocodeid)
        loc_types_table     =   get_location_types_table(geocodeid)

        from dfcleanser.common.common_utils import display_generic_grid
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import geocode_google_reverse_notes_html
        gridclasses     =   ["dfc-top","dfc-middle","dfc-bottom","dfc-right","dfc-footer"]
        gridhtmls       =   [column_name_table,addr_comps_table,loc_types_table,geocoding_input_html,geocode_google_reverse_notes_html]
                    
        display_generic_grid("df-geocode-google-bulk-reverse-wrapper",gridclasses,gridhtmls)

    else :

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_column_names_table
        column_name_table   =   get_column_names_table(BingId,REVERSE,df) 

        if(BGM.GEOCODE_TRACE_DISPLAY_FORM) :
            log_debug_dfc(-1,"[display_bulk_reverse_geocoding] " + bulk_bing_reverse_input_id+"Parms" + " cfg_parms : \n        " + str(cfg.get_config_value(bulk_bing_reverse_input_id+"Parms")))        

        # build the input form
        from dfcleanser.common.html_widgets import InputForm
        geocoding_input_form   =   InputForm(bulk_bing_reverse_input_id,
                                            bulk_bing_reverse_input_idList,
                                            bulk_bing_reverse_input_labelList,
                                            bulk_bing_reverse_input_typeList,
                                            bulk_bing_reverse_input_placeholderList,
                                            bulk_bing_reverse_input_jsList,
                                            bulk_bing_reverse_input_reqList)
        
        selectDicts     =   []

        df_list     =   cfg.get_dfc_dataframes_titles_list()
        default_df  =   df_list[0]

        dataframes  =   {"default" : default_df,
                        "list" : df_list,
                        "callback" : "change_bulk_reverse_df"}
        selectDicts.append(dataframes)

        addrcomps     =   {"default" : "Full Address Only",
                           "list" : ["Full Address Only","Full Address And Components"]}
        selectDicts.append(addrcomps)
            
        countries       =   {}
        countries.update({"default": "United States"})
            
        countrydict     =   get_Dict("Country_Codes")
        countrylist     =   list(countrydict.keys())
        countrylist.sort()
        countries.update({"list":countrylist})
        selectDicts.append(countries)
 
        includecomp     =   {"default" : "False",
                            "list" : ["True","False"]}
        selectDicts.append(includecomp)
           
        get_select_defaults(geocoding_input_form,
                            bulk_bing_reverse_input_id,
                            bulk_bing_reverse_input_idList,
                            bulk_bing_reverse_input_typeList,
                            selectDicts)

        geocoding_input_form.set_gridwidth(580)
        geocoding_input_form.set_custombwidth(120)
    
        geocoding_input_form.set_fullparms(True)

        geocoding_input_html = ""
        geocoding_input_html = geocoding_input_form.get_html() 

        from dfcleanser.common.common_utils import display_generic_grid
        gridclasses     =   ["dfc-left","dfc-right"]
        gridhtmls       =   [column_name_table,geocoding_input_html]
                    
        display_generic_grid("df-geocode-bing-bulk-reverse-wrapper",gridclasses,gridhtmls)



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Bulk Geocoder process methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def process_bulk_query_geocoding(geocodeid,runparms) :
    """
    * ---------------------------------------------------------
    * function : display geocoder reverse screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()

    from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import get_bulk_coords
    get_bulk_coords(geocodeid,runparms,refresh=False) 


def process_bulk_reverse_geocoding(geocodeid,runparms) :
    """
    * ---------------------------------------------------------
    * function : display geocoder reverse screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()

    from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import get_bulk_addresses
    get_bulk_addresses(geocodeid,runparms,refresh=False) 


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Bulk Geocoder test geocoder connection methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def test_bulk_geocoder_connection(geocodeid, parms) :

    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[BulkGeocode][test_bulk_geocoder_connection] : geocodeid : parms :" + str(geocodeid) + "\n   " + str(parms)) 

    if(geocodeid == BingId):
        ids = bing_bulk_geocoder_idList
    elif(geocodeid == GoogleId):
        ids = google_bulk_geocoder_idList

    inputs = get_parms_for_input(parms, ids)

    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[BulkGeocode][test_bulk_geocoder_connection] : inputs "  + str(inputs)) 

    opstat = opStatus()

    if(geocodeid == GoogleId) :
        opstat  =   test_google_bulk_connector(inputs)  
    elif(geocodeid == BingId) :

        if(DEBUG_GEOCODE_BULK) :
            log_debug_dfc(-1,"[BulkGeocode][test_bulk_geocoder_connection] : calling test_geocoder :") 

        from dfcleanser.Qt.utils.Geocode.GeocodeControl import test_geocoder
        opstat  =   test_geocoder(BingId,inputs,BULK)

    if(opstat.get_status()):

        from dfcleanser.common.cfg import run_javascript
        run_javascript("alert('connected with geocoder successfully')","connect ok ")    

    else :
        
        from dfcleanser.common.cfg import run_javascript
        run_javascript("alert('unable to connect with geocoder successfully')","connect ok ")    

    display_bulk_geocoders(geocodeid)


def validate_bulk_google_geocoder_parms(connectParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the google connect parms
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    if( len(connectParms[0]) == 0 ) :
        if( (len(connectParms[1]) == 0) or (len(connectParms[2]) == 0) ) :        
            opstat.set_status(False)
            opstat.set_errorMsg("google connect parms incomplete")

def get_bulk_google_geocoder_connection(apikey,cid,csecret,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a google bulk geocode connection
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[get_bulk_google_geocoder_connection] apikey : cid : csecret  " + str(apikey) + str(cid) + str(csecret) )

    api_key     =   None
    gmaps       =   None
    
    if(len(apikey) == 0) : 
        client_ID       =  cid   
        client_Secret   =  csecret
    else :
        api_key     =   apikey
        
    try :
        if(api_key == None) :
            gmaps           =   googlemaps.Client(client_id=client_ID,client_secret=client_Secret)
        else :
            gmaps           =   googlemaps.Client(key=api_key)
        
    except ValueError :
        opstat.set_status(False)
        opstat.set_errorMsg("CLIENT CREDENTIALS INVALID")
    except NotImplementedError :
        opstat.set_status(False)
        opstat.set_errorMsg("NotImplementedError")

    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[get_bulk_google_geocoder_connection] opstat  " + str(opstat.get_status()) )
        
    return(gmaps)

def test_google_bulk_connector(connectParms) :
    """
    * --------------------------------------------------------
    * function : control the arcgis bulk geocoder
    * 
    * parms :
    *  connectParms - google connect parms
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[test_google_bulk_connector] connectParms : \n    " + str(connectParms)) 
   
    test_address    =   "1111 Euclid Ave, Cleveland OH "

    opstat      =   opStatus()
    validate_bulk_google_geocoder_parms(connectParms,opstat) 

    if(DEBUG_GEOCODE_BULK) :
        log_debug_dfc(-1,"[test_google_bulk_connector] validate parms : " + opstat.get_status()) 
    
    if(opstat.get_status()) :
    
        try :
            get_bulk_google_geocoder_connection(connectParms[0],connectParms[1],connectParms[2],opstat)
            
            if(opstat.get_status()) :
                cfg.set_config_value(google_bulk_geocoder_id + "Parms",connectParms)
            
                from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import get_google_query_results
                test_results    =   get_google_query_results(0,test_address,None,opstat) 
    
        except Exception as e :

            opstat.set_status(False)
            title       =   "dfcleanser exception"       
            status_msg  =   "[unable to connect to google geocoder] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
    
    if(opstat.get_status()) :
        
        from dfcleanser.common.cfg import run_javascript
        run_javascript("alert('connected with geocoder successfully')","connect ok ")    
    
    else :
        
        from dfcleanser.common.cfg import run_javascript
        run_javascript("alert('failed to connect with geocoder successfully')","connect ok ")    

    return(opstat)

"""
#------------------------------------------------------------------
#   Google Bulk Geocoder test geocoder methods end
#------------------------------------------------------------------
""" 



"""
#------------------------------------------------------------------
#   Bulk Geocoder display process results
#------------------------------------------------------------------
""" 

def display_geocode_utility(optionId, parms=None):
    """
    * ---------------------------------------------------------
    * function : main geocode process function
    * 
    * parms :
    *  optionId  - geocoder option to process
    *  parms     - option parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if(1):
        from IPython.display import clear_output
        clear_output()

    if(not (cfg.is_a_dfc_dataframe_loaded())):
        cfg.drop_config_value(cfg.CURRENT_GEOCODE_DF)

    if(not cfg.check_if_dc_init()):
        
        sugw.display_geocoding_console()
        clear_sw_utility_geocodedata()
    
    else:

        from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
        if(not (are_owner_inputs_defined(cfg.SWGeocodeUtility_ID))):

            swu_geoocode_inputs = []

            for i in range(len(SWUtility_bulk_geocode_inputs)):
                swu_geoocode_inputs.append(SWUtility_bulk_geocode_inputs[i])

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import SWUtility_bulk_geocode_console_inputs
            for i in range(len(SWUtility_bulk_geocode_console_inputs)):
                swu_geoocode_inputs.append(SWUtility_bulk_geocode_console_inputs[i])

            #from dfcleanser.Qt.utils.Geocode.BukkGeocode import 
            #for i in range(len(sugw.SWUtility_geocode_inputs)):
            #    swu_geoocode_inputs.append(sugw.SWUtility_geocode_inputs[i])

            define_inputs(cfg.SWGeocodeUtility_ID, swu_geoocode_inputs)


    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import (DISPLAY_MAIN_GEOCODING,TEST_GEOCODER,BULK_EXIT_GEOCODER)

    if(optionId == DISPLAY_MAIN_GEOCODING):
        sugw.display_geocoding_console()
        clear_sw_utility_geocodedata()

    #SAVE
    # geoocode exit bulk
    elif(optionId == BULK_EXIT_GEOCODER):

        opstat = opStatus()

        drop_current_geocode_data = parms

        if(drop_current_geocode_data == "1"):

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import (GEOCODING_RESULTS_DF_TITLE,GEOCODING_ERROR_LOG_DF_TITLE)
            cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)
            cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)

            # delete checkpoint files
            import os

            chckpt_file_path_name = os.path.join(cfg.get_notebookPath(), "PandasDataframeCleanser_files")
            chckpt_file_path_name = os.path.join(chckpt_file_path_name, "geocode_checkpoints")

            df_source = cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)

            file_name = cfg.get_notebookName() + "_" + df_source + "_checkpoint"

            if(cfg.does_dir_exist(chckpt_file_path_name)):

                for i in range(100):

                    chckpt_file_name = file_name + str(i) + ".csv"
                    chckpt_file_name = os.path.join(chckpt_file_path_name, chckpt_file_name)

                    if(cfg.does_file_exist(chckpt_file_name)):

                        cfg.delete_a_file(chckpt_file_name, opstat)
                        chckpt_file_name = chckpt_file_name.replace(".csv", "_backup.csv")
                        cfg.delete_a_file(chckpt_file_name, opstat)

                    else:
                        break

        display_bulk_geocoders(BingId)
        #clear_sw_utility_geocodedata()

        from dfcleanser.sw_utilities.DisplayUtils import display_status_note
        if(drop_current_geocode_data == "1"):
            display_status_note( "Bulk Geocode Results, Error and Checkpoint files removed")
        else:
            display_status_note("Bulk Geocode Results, Error and Checkpoint files retained")


    elif(optionId == BGM.PROCESS_BULK_RESULTS):

        opstat = opStatus()

        cmd = parms[0]

        if(cmd == BGM.DISPLAY_BULK_RESULTS_RETURN):

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import refresh_bulk_geocode_console
            refresh_bulk_geocode_console()

        elif((cmd == BGM.DISPLAY_BULK_RESULTS_APPEND) or
             (cmd == BGM.DISPLAY_BULK_RESULTS_EXPORT_CSV)):

            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(cmd, opstat)

        elif(cmd == BGM.DISPLAY_BULK_RESULTS):
            
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(cmd, opstat, True)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_APPEND_CLEAR):

            cfg.drop_config_value(subgcs.bulk_geocode_append_input_id + "Parms")
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(cmd, opstat)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_APPEND_RETURN):
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_RESULTS_BASE, opstat)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_CSV_CLEAR):

            cfg.drop_config_value(subgcs.bulk_geocode_export_input_id + "Parms")
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(cmd, opstat)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_CSV_RETURN):
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_RESULTS_BASE, opstat)

        elif(cmd == BGM.DISPLAY_BULK_SOURCE_DF):
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_SOURCE_DF, opstat)

        elif(cmd == BGM.DISPLAY_BULK_RESULTS_DF):
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_RESULTS_DF, opstat)

        elif(cmd == BGM.DISPLAY_BULK_ERRORS_DF):
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(BGM.DISPLAY_BULK_ERRORS_DF, opstat)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_APPEND_PROCESS):
            from dfcleanser.Qy.utils.Geocode.BulkGeocodeControl import process_geocode_final_results
            process_geocode_final_results(cmd, parms)

        elif(cmd == BGM.PROCESS_BULK_RESULTS_CSV_PROCESS):
            from dfcleanser.Qy.utils.Geocode.BulkGeocodeControl import process_geocode_final_results
            process_geocode_final_results(cmd, parms)

        else:
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole import display_geocoder_process_results
            display_geocoder_process_results(cmd, opstat, True)










def display_bulk_tuning(geoparms) :

    from IPython.display import clear_output

    clear_output()
    display_bulk_tune_input_form()
    
    

def test_pan() :

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df          =   get_dfc_dataframe_df("Crime_Scenes")

    cols    =   df.columns.tolist()

    import pandas as pd
    cols_df = pd.DataFrame(cols, columns=['Column Name'])

    import panel as pn
    pn.extension('tabulator')
    col_names_table  =   pn.widgets.Tabulator(cols_df,show_index=False,selectable=True,theme='site')

    def click(event):
        print('Clicked cell in column, row with value ')

    col_names_table.on_click(click) 


    col_names_table

    return(col_names_table)



# """
# --------------------------------------------------------------------------
#   column names table utility
# --------------------------------------------------------------------------
# """




def test_html_table() :

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df          =   get_dfc_dataframe_df("Crime_Scenes")

    cols    =   df.columns.tolist()

    table_html  =   ""
    table_html  =   table_html + start_table

    for i in range(len(cols)) :
        next_row    =   table_row.replace("XXXTABCOL",cols[i])
        table_html  =   table_html + next_row

    table_html  =   table_html + end_table

    from dfcleanser.common.common_utils import displayHTML
    #displayHTML(table_html)


           # build the input form
    from dfcleanser.common.html_widgets import InputForm
    geocoding_input_form   =   InputForm(bulk_bing_query_input_id,
                                            bulk_bing_query_input_idList,
                                            bulk_bing_query_input_labelList,
                                            bulk_bing_query_input_typeList,
                                            bulk_bing_query_input_placeholderList,
                                            bulk_bing_query_input_jsList,
                                            bulk_bing_query_input_reqList)
        
    selectDicts     =   []   

    df_list     =   cfg.get_dfc_dataframes_titles_list()
    default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
        
    if(default_df is None) :
        default_df  =   df_list[0]
            
    dataframes  =   {"default" : default_df,
                        "list" : df_list,
                        "callback" : "change_bulk_df"}
    selectDicts.append(dataframes)
            
    savecoords      =   {"default" : "[Latitude,Longitude]",
                            "list" : ["[Latitude,Longitude]","[LatitudeLongitude]"]}
    selectDicts.append(savecoords)
            
    countries       =   {}
    countries.update({"default": "United States"})
            
    countrydict     =   get_Dict("Country_Codes")
    countrylist     =   list(countrydict.keys())
    countrylist.sort()
    countries.update({"list":countrylist})
    selectDicts.append(countries)
 
    includecomp     =   {"default" : "False",
                            "list" : ["True","False"]}
    selectDicts.append(includecomp)
    selectDicts.append(includecomp)
           
    get_select_defaults(geocoding_input_form,
                            bulk_bing_query_input_id,
                            bulk_bing_query_input_idList,
                            bulk_bing_query_input_typeList,
                            selectDicts)

    geocoding_input_form.set_gridwidth(580)
    geocoding_input_form.set_custombwidth(110)
    
    geocoding_input_form.set_fullparms(True)

    geocoding_input_html = ""
    geocoding_input_html = geocoding_input_form.get_html() 

    #displayHTML(geocoding_input_html)

    from dfcleanser.common.common_utils import display_generic_grid
    gridclasses     =   ["dfc-left","dfc-right"]
    gridhtmls       =   [table_html,geocoding_input_html]
                    
    display_generic_grid("df-geocode-bulk-reverse-wrapper",gridclasses,gridhtmls)

"""<html> 
<head> 
    <title>Text alignment</title> 
    <style> 
        h1{text-align: left;} 
    </style> 
</head> 
<body> 
    <h1>GeeksforGeeks</h1> 
</body> 
</html>
"""
#onclick="moveValue(this);"


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoders utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""


def clear_sw_utility_geocodedata():

    drop_owner_tables(cfg.SWGeocodeUtility_ID)

    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWGeocodeUtility_ID)

    clear_sw_utility_geocode_cfg_values()


def clear_sw_utility_geocode_cfg_values():

    cfg.drop_config_value(cfg.BULK_GEOCODE_MODE_KEY)
    cfg.drop_config_value("geocodeprocresultsParms")
    cfg.drop_config_value("geocodeprocresultsParmsProtect")
    #cfg.drop_config_value(sugw.addr_center_df_utility_input_id + "Parms")
    #cfg.drop_config_value(sugw.addr_center_df_utility_input_id + "ParmsProtect")
    #cfg.drop_config_value(sugw.addr_center_utility_input_id + "Parms")
    #cfg.drop_config_value(sugw.addr_center_utility_input_id + "ParmsProtect")

    # cfg.drop_config_value(cfg.CURRENT_GEOCODE_DF)

    # cfg.drop_config_value(sugw.addr_df_dist_utility_input_id+"Parms")
    cfg.drop_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)
    cfg.drop_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)
    cfg.drop_config_value(cfg.BULK_GEOCODE_MODE_KEY)

    return

