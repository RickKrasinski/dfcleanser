"""
# sw_utility_bulk_geocode_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw

import dfcleanser.common.help_utils as dfchelp

from dfcleanser.common.html_widgets import (maketextarea) 
from dfcleanser.common.common_utils import (display_grid, opStatus, get_parms_for_input, 
                                            display_exception, get_dfc_dataframe)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, 
                                             SCROLL_NEXT, ROW_MAJOR)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    google bulk forms 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google geocoder connect parms
#--------------------------------------------------------------------------
"""
google_bulk_geocoder_title               =   "Google V3 Bulk Geocoder"
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
                                               None,None,None,None,None,None,None]

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
                                              "Interactive</br>Geocoding",
                                              "Clear","Return","Help"]


google_bulk_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","select","text","text",
                                              "button","button","button","button","button","button","button"]

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
                                              None,None,None,None,None,None,None]

google_bulk_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.GoogleId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.GoogleId)  + "," + str(sugm.QUERY) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.GoogleId)  + "," + str(sugm.REVERSE) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.INTERACTIVE) + ")",
                                              "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                              "display_help_url('" + str(dfchelp.GoogleInitHelp) + "')"]

google_bulk_geocoder_reqList             =   [0,1,2]

google_bulk_geocoder_form                =   [google_bulk_geocoder_id,
                                              google_bulk_geocoder_idList,
                                              google_bulk_geocoder_labelList,
                                              google_bulk_geocoder_typeList,
                                              google_bulk_geocoder_placeholderList,
                                              google_bulk_geocoder_jsList,
                                              google_bulk_geocoder_reqList]

google_API_Key    =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"


"""
#--------------------------------------------------------------------------
#    google geocode bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqdataframe",
                                               "bgqaddress",
                                               "bgqdropaddress",
                                               "bgqcolumnname",
                                               "bgqsaveaddress",
                                               "bgqregion",
                                               "bgqlanguage",
                                               "bgqloctypes",
                                               "bgqbulknumberlimit",
                                               "bgqbulkfailurelimit",
                                               None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "drop_df_address_columns_flag",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "region",
                                               "language",
                                               "acceptable_location_types",
                                               "max_addresses_to_geocode",
                                               "failure_limit_percent",
                                               "Get</br> Location </br>Types",
                                               "Get</br> Bulk </br>Coords",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_google_query_ltypes_input_labelList  =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "drop_df_address_columns_flag",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "region",
                                               "language",
                                               "location_types",
                                               "max_addresses_to_geocode",
                                               "failure_limit",
                                               "Get</br> Column</br>Names",
                                               "Get</br> Bulk </br>Coords",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_google_query_input_typeList          =   ["select",maketextarea(4),"select","text",
                                               "text","select","select","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "drop address columns defined in dataframe_address_columns (default = False)",
                                              "colname lat,lng is stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "region (default - None)",
                                              "language (default - english)",
                                              "valid location types default - ALL",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                               None,None,None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,
                                               "get_geocoding_table(" + str(sugm.LOCATION_TYPES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_query_ltypes_input_jsList     =   [None,None,None,None,None,None,None,None,None,None,
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]





bulk_google_query_input_reqList           =   [0,1,2,3,4]

bulk_google_query_input_form              =   [bulk_google_query_input_id,
                                               bulk_google_query_input_idList,
                                               bulk_google_query_input_labelList,
                                               bulk_google_query_input_typeList,
                                               bulk_google_query_input_placeholderList,
                                               bulk_google_query_input_jsList,
                                               bulk_google_query_input_reqList]  

result_typeParm     =   None
location_typeParm   =   None
languageParm        =   None

"""
#--------------------------------------------------------------------------
#    google reverse bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_reverse_input_title           =   "Google Bulk Reverse Parameters"
bulk_google_reverse_input_id              =   "googlebulkreverse"
bulk_google_reverse_input_idList          =   ["bgrdataframe",
                                               "bgrcolumnname",
                                               "bgraddresscomponents",
                                               "bgraddresslength",
                                               "bgrformattedaddress",
                                               "bgrlocationtype",
                                               "bgrlanguage",
                                               "bgrbulknumberlimit",
                                               "bgrbulkfailurelimit",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_labelList       =   ["dataframe_to_geocode_from",
                                               "dataframe_lat_long_column_name(s)",
                                               "address_components_dict",
                                               "address_components_length_flag",
                                               "address_column_name(s)",
                                               "location_type(s)",
                                               "language",
                                               "max lat_longs",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Addresses",
                                               "Get</br>Address</br>Comps",
                                               "Get</br>Location</br>Types",
                                               "Bulk </br>Geocoding",
                                               "Clear","Return","Help"]

bulk_google_reverse_input_typeList        =   ["select","text",maketextarea(6),"select","text","text",
                                               "select","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_reverse_input_placeholderList =  ["datframe to geocode from",
                                              "lat long colname(s) - [latcolname,longcolname] read from two cols",
                                              "address components dict (default = None - store full address in address_column_name)",
                                              "address components short length (default = True) False = Long)",
                                              "address column name to store full address or list to store components",
                                              "A filter of one or more location types to accept as valid (default - ALL)",
                                              "language (default - english)",
                                              "number of lat_lngs to get addresses for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_jsList          =   [None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.ADDRESS_COMPONENTS_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.LOCATION_TYPES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_reverse_input_reqList         =   [0,1,2,3,4,5,6]

bulk_google_reverse_input_form            =   [bulk_google_reverse_input_id,
                                               bulk_google_reverse_input_idList,
                                               bulk_google_reverse_input_labelList,
                                               bulk_google_reverse_input_typeList,
                                               bulk_google_reverse_input_placeholderList,
                                               bulk_google_reverse_input_jsList,
                                               bulk_google_reverse_input_reqList]  


"""
#--------------------------------------------------------------------------
#   arcGIS get batch coords forms
#--------------------------------------------------------------------------
"""

create_user_url = "https://www.arcgis.com/home/createaccount.html#"
user = "RickKrasinski"
pw = "Password2018"


"""
#--------------------------------------------------------------------------
#   arcgis batch geocoder connect parms
#--------------------------------------------------------------------------
"""
arcgis_connect_help                       =   "https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#gis"


batch_arcgis_geocoder_title               =   "ArcGis Batch Geocoder"
batch_arcgis_geocoder_id                  =   "arcgisbatchgeocoder"

batch_arcgis_geocoder_idList              =    ["agburl",
                                                "agbusername",
                                                "agbpassword",
                                                "agbkeyfile",
                                                "agbcertfile",
                                                "agbverifycert",
                                                "agbsetactive",
                                                "agbclientid",
                                                "agbprofile",
                                                "agbkwargs",
                                                None,None,None,None,None,None]

batch_arcgis_geocoder_labelList           =   ["url",
                                              "username",
                                              "password",
                                              "key_file",
                                              "cert_file",
                                              "verify_cert",
                                              "set_active",
                                              "client_id",
                                              "profile",
                                              "kwargs",
                                              "Test</br>Bulk</br>Geocoder</br>Connection",
                                              "Bulk</br>Geocoding",
                                              "Interactive</br>Geocoding",
                                              "Clear","Return","Help"]


batch_arcgis_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","text",maketextarea(4),
                                              "button","button","button","button","button","button"]

batch_arcgis_geocoder_placeholderList     =   ["a web address to either a local Portal or to ArcGIS Online (default - None)",
                                              "login user name (case-sensitive)",
                                              "password (case-sensitive)",
                                              "The file path to a user’s key certificate for PKI authentication. (default - None)",
                                              "The file path to a user’s certificate file for PKI authentication. (default - None)",
                                              "ensure all SSL. (default - True)",
                                              "The GIS object will be used as the default GIS object throughout. (default - True)",
                                              "Optional string for the client ID value. (default None)",
                                              "profile that the user wishes to use to authenticate. (default - None)",
                                              "option keyword args (default - None)",
                                              None,None,None,None,None,None]

batch_arcgis_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.ArcGISId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY)  + "," + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.INTERACTIVE) + ")",
                                              "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                              "display_help_url('" + arcgis_connect_help + "')"]

batch_arcgis_geocoder_reqList             =   [0,1,2]

batch_arcgis_geocoder_form                =   [batch_arcgis_geocoder_id,
                                               batch_arcgis_geocoder_idList,
                                               batch_arcgis_geocoder_labelList,
                                               batch_arcgis_geocoder_typeList,
                                               batch_arcgis_geocoder_placeholderList,
                                               batch_arcgis_geocoder_jsList,
                                               batch_arcgis_geocoder_reqList]


"""
#--------------------------------------------------------------------------
#   arcGIS get batch coords forms
#--------------------------------------------------------------------------
"""
arcgis_geocode_help                 =   "https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.geocoding.html#batch-geocode"

batch_arcgis_query_title            =   "arcGIS Geocoder Get Batch Coordinates"
batch_arcgis_query_id               =   "arcgisbatchquery"

batch_arcgis_query_idList           =    ["bagdataframe",
                                          "bagaddrcomps",
                                          "baqcolumnname",
                                          "baqsaveaddress",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqoutsr",
                                          "baqbatchsize",
                                          "baqscore",
                                          "baqdropaddress",
                                          "baqbulknumberlimit",
                                          "baqbulkfailurelimit",
                                          None,None,None,None,None]

batch_arcgis_query_labelList        =   ["dataframe_to_geocode",
                                         "dataframe_address_columns",
                                         "new_dataframe_lat_long_column_name(s)",
                                         "save_geocoder_full_address_column_name",
                                         "source_country",
                                         "category",
                                         "out_sr",
                                         "batch_size",
                                         "score",
                                         "drop_df_address_columns_flag",
                                         "max_addresses_to_geocode",
                                         "failure_limit",
                                         "Get</br> Bulk </br>Coords",
                                         "Get</br> Column </br>Names",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   ["select",maketextarea(4),"text", "text","select",
                                         "select","text","text","text","select","text","text",
                                         "button","button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["dataframe to geocode",
                                         "select from 'Column Names' for aggregate address : constant value use '+ Buffalo'",
                                         "'colname' stored as [lat,long] - ['latcolname','longcolname'] stored as two cols",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "source country (default - US)",
                                         "category (defailt - None)",
                                         "The (WKID) spatial reference of the x/y coordinates returned by a geocode request (default - None)",
                                         "batch size (default - geocoder recommended value)",
                                         "address match score threshold (0-100)  (default - 85%)",
                                         "drop address fields used in composite address (default = False)",
                                         "max number of dataframe rows (default - all dataframe rows)",
                                         "failure limit (default - 5%)",
                                         None,None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,None,None,None,None,None,
                                         "process_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                         "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                         "geocode_return()",
                                         "display_help_url('" + arcgis_geocode_help + "')"]

batch_arcgis_query_reqList          =   [0,1,2,3,4,5,6,7,8]

batch_arcgis_query_form             =   [batch_arcgis_query_id,
                                         batch_arcgis_query_idList,
                                         batch_arcgis_query_labelList,
                                         batch_arcgis_query_typeList,
                                         batch_arcgis_query_placeholderList,
                                         batch_arcgis_query_jsList,
                                         batch_arcgis_query_reqList]


"""
#--------------------------------------------------------------------------
#    bing bulk forms 
#--------------------------------------------------------------------------
"""
bing_bulk_geocoder_title                 =   "Bing Bulk Geocoder"
bing_bulk_geocoder_id                    =   "bingbulkgeocoder"

bing_bulk_geocoder_idList                =    ["bingapikey",
                                               "bingagent",
                                               "bingtimeout",
                                               "bingfstring",
                                               "bingscheme",
                                               "bingproxies",
                                               None,None,None,None,None,None,None]

bing_bulk_geocoder_labelList             =   ["api_key",
                                               "user_agent",
                                               "timeout",
                                               "format_string",
                                               "scheme",
                                               "proxies",
                                               "Test</br>Geocoder</br>Connection",
                                               "Bulk</br>Geocoding",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Interactive</br>Geocoding",
                                               "Clear","Return","Help"]


bing_bulk_geocoder_typeList              =   ["text","text","text","text","text","text",
                                              "button","button","button","button","button","button","button"]

bing_bulk_geocoder_placeholderList       =   ["enter Bing api key",
                                              "user agent (default - my-application)",
                                              "enter timeout in seconds (default 20)",
                                              "enter format string (default %s)",
                                              "enter scheme (default https)",
                                              "proxies dict (default None)",
                                              None,None,None,None,None,None,None]

bing_bulk_geocoder_jsList                 =   [None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.BingId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + ","+ ","  + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + ","+ ","  + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.INTERACTIVE) + ")",
                                              "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                               "display_help_url('" + str(dfchelp.BingInitHelp) + "')"]

bing_bulk_geocoder_reqList               =   [0]

bing_bulk_geocoder_form                  =   [bing_bulk_geocoder_id,
                                              bing_bulk_geocoder_idList,
                                              bing_bulk_geocoder_labelList,
                                              bing_bulk_geocoder_typeList,
                                              bing_bulk_geocoder_placeholderList,
                                              bing_bulk_geocoder_jsList,
                                              bing_bulk_geocoder_reqList]


bulk_bing_query_input_title               =   "Bing Bulk Geoocoding Parameters"
bulk_bing_query_input_id                  =   "bingbulkquery"
bulk_bing_query_input_idList              =   ["dataframe to geocode",
                                               "bbqaddress",
                                               "bbqcolumnname",
                                               "bbqdropaddress",
                                               "bbqsaveaddress",
                                               "bbqlanguage",
                                               "bbqregion",
                                               "bbqbulknumberlimit",
                                               "bbqbulkcheclpointsize",
                                               "bbqbulkfailurelimit",
                                               None,None,None,None,None,None]

bulk_bing_query_input_labelList           =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Bulk </br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_bing_query_input_typeList            =   ["select",maketextarea(4),"text","select",
                                               "text","select","select","text","text","text",
                                               "button","button","button","button","button","button"]

bulk_bing_query_input_placeholderList     =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                               None,None,None,None,None,None]

bulk_bing_query_input_jsList              =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_bing_query_input_reqList             =   [0,1,2,3,4,5,6]

bulk_bing_query_input_form                =   [bulk_bing_query_input_id,
                                               bulk_bing_query_input_idList,
                                               bulk_bing_query_input_labelList,
                                               bulk_bing_query_input_typeList,
                                               bulk_bing_query_input_placeholderList,
                                               bulk_bing_query_input_jsList,
                                               bulk_bing_query_input_reqList]  


"""
#--------------------------------------------------------------------------
#    mapquest bulk forms 
#--------------------------------------------------------------------------
"""
mapquest_bulk_geocoder_title                 =   "OpenMapQuest Bulk Geocoder"
mapquest_bulk_geocoder_id                    =   "mapquestbulkgeocoder"

mapquest_bulk_geocoder_idList                =    ["mapquestbapikey",
                                                   "mapquestbagent",
                                                   "mapquestbtimeout",
                                                   "mapquestbfstring",
                                                   "mapquestbscheme",
                                                   "mapquestbproxies",
                                                   "mapquestbcountry",
                                                   "mapquestbdomain",
                                                   None,None,None,None,None,None,None]

mapquest_bulk_geocoder_labelList             =   ["api_key",
                                                  "user_agent",
                                                  "timeout",
                                                  "format_string",
                                                  "scheme ",
                                                  "proxies",
                                                  "country_bias",
                                                  "domain",
                                                  "Test</br>Geocoder</br>Connection",
                                                  "Bulk</br>Geocoding",
                                                  "Bulk</br>Reverse</br>Geocoding",
                                                  "Interactive</br>Geocoding",
                                                  "Clear","Return","Help"]

mapquest_bulk_geocoder_typeList              =   ["text","text","text","text","text","text","text","text",
                                                  "button","button","button","button","button","button","button"]

mapquest_bulk_geocoder_placeholderList       =   ["enter MapQuest API Key",
                                                  "enter user agent (default 'my-application'",
                                                  "enter timeout in seconds (default 20)",
                                                  "enter format string (default '%s'",
                                                  "enter scheme (default 'https')",
                                                  "enter proxies dict (default None)",
                                                  "country to bias results to (default None)",
                                                  "Domain where the target service is hosted. (default open.mapquestapi.com')",
                                                  None,None,None,None,None,None,None]

mapquest_bulk_geocoder_jsList                =   [None,None,None,None,None,None,None,None,
                                                  "test_geocoder(" + str(sugm.OpenMapQuestId) + "," + str(sugm.BULK) + ")",
                                                  "display_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                                  "display_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                                  "display_geocoders(" + str(sugm.OpenMapQuestId) + "," + str(sugm.INTERACTIVE) + ")",
                                                  "clear_geocode_form(" + str(sugm.OpenMapQuestId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                                  "geocode_return()",
                                                  "display_help_url('" + str(dfchelp.OpenMapQuestInitHelp) + "')"]

mapquest_bulk_geocoder_reqList               =   [0,1]

mapquest_bulk_geocoder_form                  =   [mapquest_bulk_geocoder_id,
                                                  mapquest_bulk_geocoder_idList,
                                                  mapquest_bulk_geocoder_labelList,
                                                  mapquest_bulk_geocoder_typeList,
                                                  mapquest_bulk_geocoder_placeholderList,
                                                  mapquest_bulk_geocoder_jsList,
                                                  mapquest_bulk_geocoder_reqList]



bulk_mapquest_query_input_title           =   "OpenMapQuest Bulk Geoocoding Parameters"
bulk_mapquest_query_input_id              =   "mapquestbulkquery"
bulk_mapquest_query_input_idList          =   ["bmqdataframe",
                                               "bmqcolumnlist",
                                               "bmqcolumnname",
                                               "bmqdropaddress",
                                               "bmqsaveaddress",
                                               "bmqlanguage",
                                               "bmqregion",
                                               "bmqbulknumberlimit",
                                               "bmqbulkcheclpointsize",
                                               "bmqbulkfailurelimit",
                                               None,None,None,None,None,None]

bulk_mapquest_query_input_labelList       =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_mapquest_query_input_typeList        =   ["select",maketextarea(4),"text","select",
                                               "text","select","select","text","text","text",
                                               "button","button","button","button","button","button"]

bulk_mapquest_query_input_placeholderList =  ["dataframe_to_geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                               None,None,None,None,None,None]

bulk_mapquest_query_input_jsList          =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.OpenMapQuestId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.OpenMapQuestId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.OpenMapQuestInitHelp) + "')"]

bulk_mapquest_query_input_reqList         =   [0,1,2,3,4]

bulk_mapquest_query_input_form            =   [bulk_mapquest_query_input_id,
                                               bulk_mapquest_query_input_idList,
                                               bulk_mapquest_query_input_labelList,
                                               bulk_mapquest_query_input_typeList,
                                               bulk_mapquest_query_input_placeholderList,
                                               bulk_mapquest_query_input_jsList,
                                               bulk_mapquest_query_input_reqList]  


"""
#--------------------------------------------------------------------------
#    Nominatim bulk forms 
#--------------------------------------------------------------------------
"""
nomin_bulk_geocoder_title                =   "Nominatim Bulk Geocoder"
nomin_bulk_geocoder_id                   =   "nominbulkgeocoder"

nomin_bulk_geocoder_idList               =    ["bnominagent",
                                               "bnomintimeout",
                                               "bnominformat",
                                               "bnominbias",
                                               "bnominproxies",
                                               "bnomindomain",
                                               "bnominscheme",
                                               None,None,None,None,None,None,None]

nomin_bulk_geocoder_labelList             =   ["user_agent",
                                               "timeout",
                                               "format_string",
                                               "country_bias",
                                               "proxies",
                                               "domain",
                                               "scheme",
                                               "Test</br>Geocoder</br>Connection",
                                               "Bulk</br>Geocoding",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Interactive</br>Geocoding",
                                               "Clear","Return","Help"]


nomin_bulk_geocoder_typeList             =   ["text","text","text","text","text","text","text",
                                              "button","button","button","button","button","button","button"]

nomin_bulk_geocoder_placeholderList      =   ["enter custom User-Agent (required)",
                                              "enter timeout in secs (default 20)",
                                              "enter format string (default %s)",
                                              "enter country to bias results (default - None)",
                                              "enter proxies dict)",
                                             "enter domain (default nominatim.openstreetmap.org)",
                                             "enter scheme (default https)",
                                             None,None,None,None,None,None,None]

nomin_bulk_geocoder_jsList                =   [None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.NominatimId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.NominatimId) + "," + str(sugm.INTERACTIVE) + ")",
                                              "clear_geocode_form(" + str(sugm.NominatimId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                              "display_help_url('" + str(dfchelp.NominatimInitHelp) + "')"]


nomin_bulk_geocoder_reqList              =   [0]

nomin_bulk_geocoder_form                 =   [nomin_bulk_geocoder_id,
                                              nomin_bulk_geocoder_idList,
                                              nomin_bulk_geocoder_labelList,
                                              nomin_bulk_geocoder_typeList,
                                              nomin_bulk_geocoder_placeholderList,
                                              nomin_bulk_geocoder_jsList,
                                              nomin_bulk_geocoder_reqList]


bulk_nominatim_query_input_title          =   "Nominatim Bulk Geoocoding Parameters"
bulk_nominatim_query_input_id             =   "nominatimbulkquery"
bulk_nominatim_query_input_idList         =   ["bnqdataframe",
                                               "bnqaddress",
                                               "bnqcolumnname",
                                               "bnqdropaddress",
                                               "bnqsaveaddress",
                                               "bnqlanguage",
                                               "bnqregion",
                                               "bnqbulknumberlimit",
                                               "bnqbulkcheclpointsize",
                                               "bnqbulkfailurelimit",
                                               None,None,None,None,None,None]

bulk_nominatim_query_input_labelList      =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_nominatim_query_input_typeList       =   ["select",maketextarea(4),"text","select",
                                               "text","select","select","text","text","text",
                                               "button","button","button","button","button","button"]

bulk_nominatim_query_input_placeholderList =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                               None,None,None,None,None,None]

bulk_nominatim_query_input_jsList         =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.NominatimId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.NominatimId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.OpenMapQuestInitHelp) + "')"]

bulk_nominatim_query_input_reqList        =   [0,1,2,3,4]

bulk_nominatim_query_input_form           =   [bulk_nominatim_query_input_id,
                                               bulk_nominatim_query_input_idList,
                                               bulk_nominatim_query_input_labelList,
                                               bulk_nominatim_query_input_typeList,
                                               bulk_nominatim_query_input_placeholderList,
                                               bulk_nominatim_query_input_jsList,
                                               bulk_nominatim_query_input_reqList]  





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoding bulk display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#  bulk geocode tables 
#--------------------------------------------------------------------------
"""
def get_languages_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of languages
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    languagesHeader      =   [""]
    languagesRows        =   []
    languagesWidths      =   [100]
    languagesAligns      =   ["left"]
    languagesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts       =   get_Dictlog()
    langdict    =   dicts.get("Language_Codes",None)
    languages   =   list(langdict.keys())
    languages.sort()
    
    for i in range(len(languages)) :
        
        languagesrow = [languages[i]]
        languagesRows.append(languagesrow)
        languagesHrefs.append([callback])
        
    languages_table = None
                
    languages_table = dcTable("Languages",tableid,owner,
                              languagesHeader,languagesRows,
                              languagesWidths,languagesAligns)
            
    languages_table.set_refList(languagesHrefs)
    
    languages_table.set_small(True)
    languages_table.set_smallwidth(98)
    languages_table.set_smallmargin(10)

    languages_table.set_border(True)
        
    languages_table.set_checkLength(True)
            
    languages_table.set_textLength(26)
    languages_table.set_html_only(True) 
    
    languages_table.set_tabletype(ROW_MAJOR)
    languages_table.set_rowspertable(20)

    listHtml = get_row_major_table(languages_table,SCROLL_NEXT,False)

    #print(listHtml)        
    return(listHtml)


def get_regions_table(tableid,owner,callback,countriesFlag=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of regions
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    regionsHeader      =   [""]
    regionsRows        =   []
    regionsWidths      =   [100]
    regionsAligns      =   ["left"]
    regionsHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts           =   get_Dictlog()
    regionsdict     =   dicts.get("Country_Codes",None)
    regions         =   list(regionsdict.keys())
    regions.sort()
    
    for i in range(len(regions)) :
        
        regionsrow = [regions[i]]
        regionsRows.append(regionsrow)
        regionsHrefs.append([callback])
        
    regions_table = None
    
    if(countriesFlag) :
        ttitle  =   "Countries" 
    else :
        ttitle  =   "Regions" 
          
    regions_table = dcTable(ttitle,tableid,owner,
                             regionsHeader,regionsRows,
                             regionsWidths,regionsAligns)
            
    regions_table.set_refList(regionsHrefs)
    
    regions_table.set_small(True)
    regions_table.set_smallwidth(98)
    regions_table.set_smallmargin(10)

    regions_table.set_border(True)
        
    regions_table.set_checkLength(True)
            
    regions_table.set_textLength(26)
    regions_table.set_html_only(True) 
    
    regions_table.set_tabletype(ROW_MAJOR)
    regions_table.set_rowspertable(20)

    listHtml = get_row_major_table(regions_table,SCROLL_NEXT,False)
    #print(listHtml)        
    return(listHtml)


def get_categories_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    categoriesHeader      =   [""]
    categoriesRows        =   []
    categoriesWidths      =   [100]
    categoriesAligns      =   ["left"]
    categoriesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts           =   get_Dictlog()
    regionsdict     =   dicts.get("Language_Codes",None)
    categories      =   list(regionsdict.keys())
    categories.sort()
    
    for i in range(len(categories)) :
        
        categoriesrow = [categories[i]]
        categoriesRows.append(categoriesrow)
        categoriesHrefs.append([callback])
        
    categories_table = None
                
    categories_table = dcTable("Categories",tableid,owner,
                               categoriesHeader,categoriesRows,
                               categoriesWidths,categoriesAligns)
            
    categories_table.set_refList(categoriesHrefs)
    
    categories_table.set_small(True)
    categories_table.set_smallwidth(98)
    categories_table.set_smallmargin(10)

    categories_table.set_border(True)
        
    categories_table.set_checkLength(True)
            
    categories_table.set_textLength(26)
    categories_table.set_html_only(True) 
    
    categories_table.set_tabletype(ROW_MAJOR)
    categories_table.set_rowspertable(20)

    listHtml = get_row_major_table(categories_table,SCROLL_NEXT,False)
        
    return(listHtml)


def get_address_components_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    addrcompsHeader       =   [""]
    addrcompsRows         =   []
    addrcompsWidths       =   [100]
    addrcompsAligns       =   ["left"]
    addrcompsHrefs        =   []

    from dfcleanser.sw_utilities.sw_utility_control import get_List
    addrcomplist    =   get_List("Address_Components")

    for i in range(len(addrcomplist)) :
        
        addrcompsrow = [addrcomplist[i]]
        addrcompsRows.append(addrcompsrow)
        addrcompsHrefs.append([callback])
        
    addrcomps_table = None
                
    addrcomps_table = dcTable("Address Components",tableid,owner,
                               addrcompsHeader,addrcompsRows,
                               addrcompsWidths,addrcompsAligns)
            
    addrcomps_table.set_refList(addrcompsHrefs)
    
    addrcomps_table.set_small(True)
    addrcomps_table.set_smallwidth(98)
    addrcomps_table.set_smallmargin(10)

    addrcomps_table.set_border(True)
        
    addrcomps_table.set_checkLength(True)
            
    addrcomps_table.set_textLength(32)
    addrcomps_table.set_html_only(True) 
    
    addrcomps_table.set_tabletype(ROW_MAJOR)
    addrcomps_table.set_rowspertable(20)

    listHtml = get_row_major_table(addrcomps_table,SCROLL_NEXT,False)
    #print(listHtml)    
    return(listHtml)


def get_result_types_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    restypesHeader        =   [""]
    restypesRows          =   []
    restypesWidths        =   [100]
    restypesAligns        =   ["left"]
    restypesHrefs         =   []


    for i in range(10) :
        
        restypesrow = [str(i)]
        restypesRows.append(restypesrow)
        restypesHrefs.append([callback])
        
    restypes_table = None
                
    restypes_table = dcTable("result types",tableid,owner,
                             restypesHeader,restypesRows,
                             restypesWidths,restypesAligns)
            
    restypes_table.set_refList(restypesHrefs)
    
    restypes_table.set_small(True)
    restypes_table.set_smallwidth(98)
    restypes_table.set_smallmargin(10)

    restypes_table.set_border(True)
        
    restypes_table.set_checkLength(True)
            
    restypes_table.set_textLength(22)
    restypes_table.set_html_only(True) 
    
    restypes_table.set_tabletype(ROW_MAJOR)
    restypes_table.set_rowspertable(20)

    listHtml = get_row_major_table(restypes_table,SCROLL_NEXT,False)
        
    return(listHtml)


def get_location_types_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    loctypesHeader        =   [""]
    loctypesRows          =   []
    loctypesWidths        =   [100]
    loctypesAligns        =   ["left"]
    loctypesHrefs         =   []

    from dfcleanser.sw_utilities.sw_utility_control import get_List
    loctypeslist    =   get_List("Location_Types")

    for i in range(len(loctypeslist)) :
        
        loctypesrow = [loctypeslist[i]]
        loctypesRows.append(loctypesrow)
        loctypesHrefs.append([callback])
        
    loctypes_table = None
                
    loctypes_table = dcTable("Location Types",tableid,owner,
                             loctypesHeader,loctypesRows,
                             loctypesWidths,loctypesAligns)
            
    loctypes_table.set_refList(loctypesHrefs)
    
    loctypes_table.set_small(True)
    loctypes_table.set_smallwidth(98)
    loctypes_table.set_smallmargin(10)

    loctypes_table.set_border(True)
        
    loctypes_table.set_checkLength(True)
            
    loctypes_table.set_textLength(22)
    loctypes_table.set_html_only(True) 
    
    loctypes_table.set_tabletype(ROW_MAJOR)
    loctypes_table.set_rowspertable(20)

    listHtml = get_row_major_table(loctypes_table,SCROLL_NEXT,False)
    #print(listHtml)        
    return(listHtml)




"""
#--------------------------------------------------------------------------
#  bulk geocode display methods
#--------------------------------------------------------------------------
"""
def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.COLNAMES_TABLE,showfull=False) :
    """
    * --------------------------------------------------------- 
    * function : display the input form for geoocoding
    * 
    * parms :
    *  geocid       - geocode identiifier
    *  geotype      - geocode command type   
    *  tabletype    - html table identifier
    *  showfull     - show full parm list flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    print("display_bulk_geocode_inputs",geocid,geotype,tabletype)

    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
    
    if (geotype == sugm.QUERY) :
        if(tabletype==sugm.GEOCODERS_TABLE) :
            geo_parms_html = sugw.get_geocoder_table(True) 
            
        elif(tabletype==sugm.COLNAMES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = sugw.get_df_col_names_table("gegdfcolnamesTable",cfg.SWGeocodeUtility_ID,"gb_google_add_df_column")
            else :
                geo_parms_html = sugw.get_df_col_names_table("geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"gb_arcgis_add_df_column")
                
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"gb_select_language")
            
        elif(tabletype==sugm.REGION_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_regions_table("gegdfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_region")
            else :
                geo_parms_html = get_regions_table("geadfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_country",True)
        
        elif(tabletype==sugm.LOCATION_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_location_types_table("gegdfltypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_location_type")
                
        else :
            geo_parms_html = get_categories_table("gedfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_category")
            
        if(geocid == sugm.GoogleId) :
            if(tabletype==sugm.COLNAMES_TABLE) :
                form    =   bulk_google_query_input_form
            else :
                form    =   [bulk_google_query_input_id,
                             bulk_google_query_input_idList,
                             bulk_google_query_ltypes_input_labelList,
                             bulk_google_query_input_typeList,
                             bulk_google_query_input_placeholderList,
                             bulk_google_query_ltypes_input_jsList,
                             bulk_google_query_input_reqList]  
                
        elif(geocid == sugm.ArcGISId) :
            form    =   batch_arcgis_query_form
            inparms     =   cfg.get_config_value(batch_arcgis_query_id+"Parms")
            inparms[8]  =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
            cfg.set_config_value(batch_arcgis_query_id+"Parms",inparms)
        elif(geocid == sugm.BingId) :
            form    =   bulk_bing_query_input_form
        elif(geocid == sugm.OpenMapQuestId) :
            form    =   bulk_mapquest_query_input_form
        elif(geocid == sugm.NominatimId) :
            form    =   bulk_nominatim_query_input_form

    else :
        
        if(tabletype==sugm.GEOCODERS_TABLE) :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_table
            geo_parms_html = get_geocoder_table(True) 
            
        elif(tabletype==sugm.ADDRESS_COMPONENTS_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_address_components_table("graddrcompsTable",cfg.SWGeocodeUtility_ID,"gbr_google_add_addrcomp")
        
        elif(tabletype==sugm.RESULT_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_result_types_table("grresulttypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_result_type")
                
        elif(tabletype==sugm.LOCATION_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_location_types_table("grlocationtypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_location_type")
            
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"gbr_select_language")

        else :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_parms_table
            geo_parms_html = get_geocoder_parms_table(geocid)
        
        if(geocid == sugm.GoogleId) :
            form    =   bulk_google_reverse_input_form

    
    from dfcleanser.common.html_widgets import InputForm
    geofunc_input_form = InputForm(form[0],
                                   form[1],
                                   form[2],
                                   form[3],
                                   form[4],
                                   form[5],
                                   form[6],
                                   shortForm=False)
    if (geotype == sugm.QUERY) :
        if(geocid == sugm.GoogleId) :
            geocsel           =   {"default":"False","list":["True","False"]}
            geofunc_input_form.add_select_dict("bgqdropaddress",geocsel)
            
        elif(geocid == sugm.ArcGISId) :
            geocsel           =   {"default":"False","list":["True","False"]}
            geofunc_input_form.add_select_dict("baqdropaddress",geocsel)

        elif(geocid == sugm.BingId) :
            geocsel           =   {"default":"False","list":["True","False"]}
            geofunc_input_form.add_select_dict("bbqdropaddress",geocsel)
            
        elif(geocid == sugm.OpenMapQuestId) :
            geocsel           =   {"default":"False","list":["True","False"]}
            geofunc_input_form.add_select_dict("bmqdropaddress",geocsel)
            
        elif(geocid == sugm.NominatimId) :
            geocsel           =   {"default":"False","list":["True","False"]}
            geofunc_input_form.add_select_dict("bnqdropaddress",geocsel)
        
    else :
        if(geocid == sugm.GoogleId) :
            geocsel           =   {"default":"True","list":["True","False"]}
            geofunc_input_form.add_select_dict("bgraddresslength",geocsel)
            
    
    if(geotype == sugm.QUERY) : 
        geofunc_input_form.set_gridwidth(620)
        
        # add select lists
        if(geocid == sugm.GoogleId) :
            geofunc_input_form.add_select_dict("bgqdataframe",cfg.get_dfc_dataframes_select_list())
            
            regions             =   {}
            regions.update({"default": "United States"})

            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            regionsdict     =   dicts.get("Country_Codes",None)
            regionslist     =   list(regionsdict.keys())
            regionslist.sort()
            regions.update({"list":regionslist})
            
            geofunc_input_form.add_select_dict("bgqregion",regions)

            languages       =   {}
            languages.update({"default": "English"})

            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            langdict        =   dicts.get("Language_Codes",None)
            languageslist   =   list(langdict.keys())
            languageslist.sort()
            languages.update({"list":languageslist})
            geofunc_input_form.add_select_dict("bgqlanguage",languages)

        elif(geocid == sugm.ArcGISId) :
            geofunc_input_form.add_select_dict("bagdataframe",cfg.get_dfc_dataframes_select_list())
            
            regions             =   {}
            regions.update({"default": "United States"})

            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            regionsdict     =   dicts.get("Country_Codes",None)
            regionslist     =   list(regionsdict.keys())
            regionslist.sort()
            regions.update({"list":regionslist})
            
            geofunc_input_form.add_select_dict("baqsourcecountry",regions)

            categories       =   {}
            categories.update({"default": "Address"})
            
            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            catdict         =   dicts.get("ArcGIS_Categories",None)
            catslist        =   list(catdict.keys())
            catslist.sort()
            categories.update({"list":catslist})
            geofunc_input_form.add_select_dict("baqcategory",categories)
            
    else :
        geofunc_input_form.set_gridwidth(680)
        geofunc_input_form.set_custombwidth(92)
        
                # add select lists
        if(geocid == sugm.GoogleId) :
            geofunc_input_form.add_select_dict("bgrdataframe",cfg.get_dfc_dataframes_select_list())
            
            languages       =   {}
            languages.update({"default": "English"})

            from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
            dicts           =   get_Dictlog()
            langdict        =   dicts.get("Language_Codes",None)
            languageslist   =   list(langdict.keys())
            languageslist.sort()
            languages.update({"list":languageslist})
            geofunc_input_form.add_select_dict("bgrlanguage",languages)
            
            locations       =   {}
            locations.update({"default": "ROOFTOP"})
            
            from dfcleanser.sw_utilities.sw_utility_control import get_Listlog
            lists           =   get_Listlog()
            loclist         =   lists.get("Location_Types",None)
            loclist.sort()
            locations.update({"list":loclist})
            geofunc_input_form.add_select_dict("bgrlocationtype",locations)
    
    if(showfull) :
        geofunc_input_form.set_fullparms(True)    
    
    geofunc_input_html = ""
    geofunc_input_html = geofunc_input_form.get_html()
    
    if (geotype == sugm.QUERY) :
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;" + sugm.get_geocoder_title(geocid) + "Bulk Geocoding</h4>" 
    else :
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;" + sugm.get_geocoder_title(geocid) + "Bulk Reverse Geocoding</h4>"
   
    if(geotype == sugm.QUERY) :   
        display_grid("geocode_query_wrapper",
                     geofunc_heading_html,
                     geo_parms_html,
                     geofunc_input_html,
                     None)
    else :
        display_grid("geocode_reverse_wrapper",
                     geofunc_heading_html,
                     geo_parms_html,
                     geofunc_input_html,
                     None)


def display_bulk_geocoding(geocid,geotype) :
    """
    * -------------------------------------------------------------------------- 
    * function : display bulk geocoding input forms
    * 
    * parms :
    *  optionId  - identify get coords or get address
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    if(not (cfg.is_a_dfc_dataframe_loaded())) :
            
        sugw.display_geocode_main_taskbar() 
        opstat.set_status(False)
        opstat.set_errorMsg("No dataframe is imported which is required for bulk geoocoding  ")
        display_exception(opstat)
            
    else :
    
        if(geotype == sugm.QUERY) :
        
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.QUERY)
            
            if( not( geocid in sugm.supported_Bulk_Geocoders) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                print("\n")
                opstat.set_errorMsg("Bulk geoocoding is not supported for the currently selected geocoder")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.QUERY)    
                
        else :
            
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.REVERSE)            
            
            if( not( geocid in sugm.supported_Bulk_Reverses) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                opstat.set_errorMsg("Bulk reverse geoocoding is not supported for the currently selected geocoder")
                print("\n")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.REVERSE)    


def display_bulk_geocoders(geocodeid,showfull=False) :
    """
    * ---------------------------------------------------------
    * function : display bulk geocoder parm screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *   showfull   -   show all parms flag
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    listHtml = sugw.get_geocoder_table(True)
    
    if(geocodeid == None) :
        geocodeid       =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocodeid == None) : 
            geocodeid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocodeid)

    geocoder_input_form = None
    
    if( (geocodeid == None) or (geocodeid == sugm.GoogleId) ) :

        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.GoogleId)
        geocoder_input_form   =   [google_bulk_geocoder_id,
                                   google_bulk_geocoder_idList,
                                   google_bulk_geocoder_labelList,
                                   google_bulk_geocoder_typeList,
                                   google_bulk_geocoder_placeholderList,
                                   google_bulk_geocoder_jsList,
                                   google_bulk_geocoder_reqList]

    elif(geocodeid == sugm.BingId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BingId)
        geocoder_input_form   =   [bing_bulk_geocoder_id,
                                   bing_bulk_geocoder_idList,
                                   bing_bulk_geocoder_labelList,
                                   bing_bulk_geocoder_typeList,
                                   bing_bulk_geocoder_placeholderList,
                                   bing_bulk_geocoder_jsList,
                                   bing_bulk_geocoder_reqList]
        
    elif(geocodeid == sugm.OpenMapQuestId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.OpenMapQuestId)
        geocoder_input_form   =   [mapquest_bulk_geocoder_id,
                                   mapquest_bulk_geocoder_idList,
                                   mapquest_bulk_geocoder_labelList,
                                   mapquest_bulk_geocoder_typeList,
                                   mapquest_bulk_geocoder_placeholderList,
                                   mapquest_bulk_geocoder_jsList,
                                   mapquest_bulk_geocoder_reqList]

    elif(geocodeid == sugm.NominatimId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.NominatimId)
        geocoder_input_form   =   [nomin_bulk_geocoder_id,
                                   nomin_bulk_geocoder_idList,
                                   nomin_bulk_geocoder_labelList,
                                   nomin_bulk_geocoder_typeList,
                                   nomin_bulk_geocoder_placeholderList,
                                   nomin_bulk_geocoder_jsList,
                                   nomin_bulk_geocoder_reqList]

    elif(geocodeid == sugm.ArcGISId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.ArcGISId)
        geocoder_input_form   =   [batch_arcgis_geocoder_id,
                                   batch_arcgis_geocoder_idList,
                                   batch_arcgis_geocoder_labelList,
                                   batch_arcgis_geocoder_typeList,
                                   batch_arcgis_geocoder_placeholderList,
                                   batch_arcgis_geocoder_jsList,
                                   batch_arcgis_geocoder_reqList]
    
    geocode_heading_html = "<h4>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bulk Geocoder Parms - " + sugm.get_geocoder_title(geocodeid) + "</h4>"

    from dfcleanser.common.html_widgets import InputForm
    geocode_input_form = InputForm(geocoder_input_form[0],
                                   geocoder_input_form[1],
                                   geocoder_input_form[2],
                                   geocoder_input_form[3],
                                   geocoder_input_form[4],
                                   geocoder_input_form[5],
                                   geocoder_input_form[6],
                                   shortForm=False)
    
    if(geocodeid == sugm.GoogleId) :

        geocsel           =   {"default":"False","list":["True","False"]}
        geocode_input_form.add_select_dict("ggbretryoverquerylimit",geocsel)
 
    elif(geocodeid == sugm.BingId) :
        
        geocsel           =   {"default":"True","list":["True","False"]}
        geocode_input_form.add_select_dict("verify_cert",geocsel)
        geocode_input_form.add_select_dict("set_active",geocsel)
    
    geocode_input_form.set_gridwidth(640)
    
    if(showfull) :
        geocode_input_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = geocode_input_form.get_html() 
    
    display_grid("sql_connector_wrapper",
                 geocode_heading_html,
                 listHtml,
                 geocode_input_html,None)
    



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  bulk geocode input validation methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_bulk_input_parms(geocid,geotype,inputs) :
    
    if(geotype == sugm.QUERY) :
        if(geocid == sugm.GoogleId) :
            return(get_parms_for_input(inputs,bulk_google_query_input_idList))
        else :
            return(get_parms_for_input(inputs,batch_arcgis_query_idList))

    else :
        if(geocid == sugm.GoogleId) :
            return(get_parms_for_input(inputs,bulk_google_reverse_input_idList))



def validate_google_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}

    if(geotype == sugm.QUERY) :

        fparms = get_parms_for_input(inputs,bulk_google_query_input_idList)

        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe selected defined")
        else :
                
            if(opstat.get_status()) :
                if(len(fparms[1]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe address column name(s) defined")
                
            if(opstat.get_status()) :
                if(len(fparms[3]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe lat lng column name(s) defined")

        if(opstat.get_status()) :
                
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[2] : fparms[2]})
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[3] : fparms[3]})
                
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[4] : fparms[4]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[4] : "None"})
                
            if(len(fparms[5]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : fparms[5]})    
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : "None"}) 
                
            if(len(fparms[6]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[6] : fparms[6]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : "en"})
                
            if(len(fparms[7]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : fparms[7]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : "ALL"})

            if(len(fparms[8]) > 0) :
                if(int(fparms[8]) > len(cfg.get_dfc_dataframe())) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : len(cfg.get_dfc_dataframe())}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : fparms[8]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : len(cfg.get_dfc_dataframe())}) 
                    
            if(len(fparms[9]) > 0) :
                if(int(fparms[9]) > 100) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : "2"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : fparms[9]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : "2"}) 
                    
    else :
                
        # check the required reverse parms
        fparms = get_parms_for_input(inputs,bulk_google_reverse_input_idList)

        if( (len(fparms[0]) == 0) and (len(fparms[1]) == 0) and (len(fparms[2]) == 0) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("No api key or client id and secret parm(s) defined")
        else :
                
            # check the required query parms 
            if(len(fparms[0]) == 0) :
                if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :   
                    opstat.set_status(False)
                    opstat.set_errorMsg("No client id and secret parm(s) defined")
                        
            if(opstat.get_status()) :
                if(len(fparms[3]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No lat lng column name defined")
                
            if(opstat.get_status()) :
                if(len(fparms[4]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No address column name defined")
        
        # validate non required parmsd            
        if(opstat.get_status()) :
                
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[2] : fparms[2]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[3] : fparms[3]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[4] : fparms[4]})
                
            if(len(fparms[5]) > 0) :
                try :
                    import json
                    addr_comps = json.loads(fparms[5])     
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("address components dict errort")
                        
                if(opstat.get_status()) :  
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : fparms[5]})
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[6] : "long"})
                    
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : ""})
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[6] : "short"})
                
            if(len(fparms[7]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : fparms[7]}) 
                
            if(len(fparms[8]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : fparms[8]}) 
                
            if(len(fparms[9]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : fparms[9]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : "en"})

            if(len(fparms[10]) > 0) :
                if(int(fparms[10]) > len(cfg.get_dfc_dataframe())) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : len(cfg.get_dfc_dataframe())}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : fparms[10]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : len(cfg.get_dfc_dataframe())}) 

            if(len(fparms[11]) > 0) :
                if(int(fparms[11]) > len(cfg.get_dfc_dataframe())) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[11] : len(cfg.get_dfc_dataframe())}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[11] : fparms[11]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[11] : len(cfg.get_dfc_dataframe())}) 

            if(len(fparms[12]) > 0) :
                if(int(fparms[12]) > 100) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[12] : 2}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[12] : fparms[12]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[12] : 2}) 

    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def validate_bulk_parms(geocid,geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geocid       - geocoder id
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}
    
    if(geocid == sugm.GoogleId) :
        bulk_geocode_kwargs     =   validate_google_bulk_parms(geotype,inputs,opstat)       
                
    elif(geocid == sugm.ArcGISId) :
        
        fparms = inputs#get_parms_for_input(inputs,batch_arcgis_query_idList)

        #print("\nvalidate_bulk_parms\n",fparms)
        # check the required parms 
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No " + bulk_google_query_input_labelList[0] + " defined")
        else :
            bulk_geocode_kwargs.update({batch_arcgis_query_labelList[0] : fparms[0]})    
            if(len(fparms[1]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No " + bulk_google_query_input_labelList[1] + " defined")
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[1] : fparms[1]})
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No " + bulk_google_query_input_labelList[2] + " defined")
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[2] : fparms[2]})     
                    if(len(fparms[3]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No " + bulk_google_query_input_labelList[3] + " defined")
                    else :
                        bulk_geocode_kwargs.update({batch_arcgis_query_labelList[3] : fparms[3]})    

        if(opstat.get_status()) :
            
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})
                
            if(len(fparms[5]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})  
                
            if(len(fparms[6]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))})
            else :
                batch_size  =   int(fparms[6])
                if(batch_size > cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("batch size exceeds arcGIS suggested max batch size of "+ str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)))
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : fparms[6]})    
                    
            if(len(fparms[7]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : str(len(get_dfc_dataframe()))})
            else :
                if(int(fparms[7]) > len(get_dfc_dataframe())) :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : str(len(get_dfc_dataframe()))})
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : fparms[7]})
            
            if(len(fparms[8]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : fparms[6]})
            
            if(len(fparms[9]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : "85"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : fparms[9]}) 

            if(len(fparms[10]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : "5"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : fparms[9]}) 

            if(len(fparms[11]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[11] : "False"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[11] : "True"}) 

            if(len(fparms[12]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[12] : fparms[12]})
                
            if(len(fparms[13]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[13] : fparms[13]}) 
                
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def get_bulk_form_id(geocid,gtype) :
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
         if(geocid == sugm.ArcGISId)            : return(batch_arcgis_geocoder_id)   
         elif(geocid == sugm.GoogleId)          : return(google_bulk_geocoder_id)
         elif(geocid == sugm.BingId)            : return(bing_bulk_geocoder_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(mapquest_bulk_geocoder_id)
         elif(geocid == sugm.NominatimId)       : return(nomin_bulk_geocoder_id)
    elif(gtype == sugm.QUERY)  :
         if(geocid == sugm.ArcGISId)            : return(batch_arcgis_query_id) 
         elif(geocid == sugm.GoogleId)          : return(bulk_google_query_input_id)
         elif(geocid == sugm.BingId)            : return(bulk_bing_query_input_id)
         elif(geocid == sugm.OpenMapQuestId)    : return(bulk_mapquest_query_input_id)
         elif(geocid == sugm.NominatimId)       : return(bulk_nominatim_query_input_id)
    elif(gtype == sugm.REVERSE)  :
         if(geocid == sugm.GoogleId)            : return(bulk_google_reverse_input_id)



def test_bulk_geocoder(geocid,inputs) :
    print("test_bulk_geocoder",geocid,inputs)


