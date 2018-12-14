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
from dfcleanser.common.common_utils import (display_grid, opStatus, get_parms_for_input, display_exception, 
                                            get_dfc_dataframe, display_status)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    google bulk forms 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    google geocode bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqapikey",
                                               "bgqclientid",
                                               "bgqclientsecret",
                                               "bgqaddress",
                                               "bgqdropaddress",
                                               "bgqcolumnname",
                                               "bgqsaveaddress",
                                               "bgqlanguage",
                                               "bgqregion",
                                               "bgqbulknumberlimit",
                                               "bgqbulkcheclpointsize",
                                               "bgqbulkfailurelimit",
                                               None,None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["google_api_key",
                                               "google_maps_client_id",
                                               "google_maps_client_secret",
                                               "dataframe_address_columns",
                                               "drop_df_address_columns_flag",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_google_query_input_typeList          =   ["text","text","text",maketextarea(4),"text","text",
                                               "text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["google_maps api key",
                                              "google_maps client id (premier)",
                                              "google_maps client secret (premier)",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "drop address columns defined in dataframe_address_columns (default = False)",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "retrieve full address from google and store in column name (default = None - don't retrieve and save)",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                               None,None,None,None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.GoogleId)+")"]

bulk_google_query_input_reqList           =   [0,1,2,3,4,5,6]

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
bulk_google_reverse_input_id              =   "googlebulkquery"
bulk_google_reverse_input_idList          =   ["bgrapikey",
                                               "bgrclientid",
                                               "bgrclientsecret",
                                               "bgrcolumnname",
                                               "bgrformattedaddress",
                                               "bgraddresscomponents",
                                               "bgraddresslength",
                                               "bgrresulttype",
                                               "bgrlocationtype",
                                               "bgrlanguage",
                                               "bgrbulknumberlimit",
                                               "bgrbulkcheckpointsize",
                                               "bgrbulkfailurelimit",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_labelList       =   ["google_api_key",
                                               "google_maps_client_id",
                                               "google_maps_client_secret",
                                               "dataframe_lat_long_column_name(s)",
                                               "get_formatted_address_flag",
                                               "get_address_components_list",
                                               "address_components_type_flag",
                                               "result_type",
                                               "location_type",
                                               "language",
                                               "max lat_longs",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_google_reverse_input_typeList        =   ["text","text","text","text","text",maketextarea(6),
                                               "text","text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_reverse_input_placeholderList =  ["google_maps api key",
                                              "google_maps client id (premier) ",
                                              "google_maps client secret (premier)",
                                              "lat long colname(s) - [latcolname,longcolname] read from two cols",
                                              "get the google formatted address column name (default = Full_Address)",
                                              "individual address components dict (default = None - don't retrieve any components)",
                                              "address components short length (default = True) False = Long)",
                                              "A filter of one or more address types",
                                              "A filter of one or more location types",
                                              "language (default - english)",
                                              "number of lat_lngs to get addresses for (default - len(dataframe))",
                                              "number of reverse results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_jsList          =   [None,None,None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.GoogleId)+")"]

bulk_google_reverse_input_reqList         =   [0,1,2,3,4,5]

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
#   arcGIS get batch coords forms
#--------------------------------------------------------------------------
"""
batch_arcgis_query_title            =   "arcGIS Geocoder Get Batch Coordinates"
batch_arcgis_query_id               =   "arcgisbatchquery"

batch_arcgis_query_idList           =    ["bagusername",
                                          "bagpw",
                                          "bagreferer",
                                          "baqaddress",
                                          "baqcolumnname",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqbatchsize",
                                          "baqbulknumberlimit",
                                          "baqbulkcheckpointsize",
                                          "baqscore",
                                          "baqbulkfailurelimit",
                                          "baqdropaddress",
                                          "baqsaveaddress",
                                          "baqsearchextent",
                                          None,None,None,None,None,None,None]

batch_arcgis_query_labelList        =   ["arcgis_username",
                                         "arcgis_pw",
                                         "referer",
                                         "dataframe_address_columns",
                                         "new_dataframe_lat_long_column_name(s)",
                                         "source_country",
                                         "category",
                                         "batch_size",
                                         "max_addresses_to_geocode",
                                         "checkpoint_size",
                                         "score",
                                         "failure_limit",
                                         "drop_df_address_columns_flag",
                                         "save_geocoder_address_column_name",
                                         "search_extent",
                                         "Get</br> Bulk </br>Coords",
                                         "Get</br> Column </br>Names",
                                         "Get</br> Countries",
                                         "Get</br> Categories",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   ["text","text","text",maketextarea(4),"text","text","text",
                                         "text","text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["arcgis username",
                                         "arcgis password",
                                         "ArcGIS referer (default : my-application)",
                                         "select from 'Column Names' for aggregate address : constant value use '+ Buffalo'",
                                         "'colname' stored as [lat,long] - ['latcolname','longcolname'] stored as two cols",
                                         "source country (default - US)",
                                         "category (defailt - None)",
                                         "batch size (default - geocoder recommended value)",
                                         "max number of dataframe rows (default - all dataframe rows)",
                                         "checkpoint size (default - batch size)",
                                         "address match score threshold (0-100)  (default - 85%)",
                                         "failure limit (default - 5%)",
                                         "drop address fields used in composite address (default = False)",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "A set of bounding box coords that limit the search area (default - None)",
                                         None,None,None,None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
                                         "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_COUNTRIES)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_CATEGORIES)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.ArcGISId)+")"]

batch_arcgis_query_reqList          =   [0,1,2,3,4,5,6,7,8,9]

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
bulk_bing_query_input_title               =   "Bing Bulk Geoocoding Parameters"
bulk_bing_query_input_id                  =   "bingbulkquery"
bulk_bing_query_input_idList              =   ["bbqclientid",
                                               "bbqclientsecret",
                                               "bbqaddress",
                                               "bbqcolumnname",
                                               "bbqlanguage",
                                               "bbqregion",
                                               "bbqbulknumberlimit",
                                               "bbqbulkcheclpointsize",
                                               "bbqbulkfailurelimit",
                                               "bbqdropaddress",
                                               "bbqsaveaddress",
                                               None,None,None,None,None,None,None]

bulk_bing_query_input_labelList           =   ["bing_client_id",
                                               "bing_client_secret",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_bing_query_input_typeList            =   ["text","text",maketextarea(4),"text","text",
                                               "text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_bing_query_input_placeholderList     =  ["bing client id (premium) - google api key (standard)",
                                              "bing client secret (premium)",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                               None,None,None,None,None,None,None]

bulk_bing_query_input_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.BingId)+")"]

bulk_bing_query_input_reqList             =   [0,1,2,3,4,5]

bulk_bing_query_input_form                =   [bulk_bing_query_input_id,
                                               bulk_bing_query_input_idList,
                                               bulk_bing_query_input_labelList,
                                               bulk_bing_query_input_typeList,
                                               bulk_bing_query_input_placeholderList,
                                               bulk_bing_query_input_jsList,
                                               bulk_bing_query_input_reqList]  


"""
#--------------------------------------------------------------------------
#    bing bulk forms 
#--------------------------------------------------------------------------
"""
bulk_mapquest_query_input_title           =   "OpenMapQuest Bulk Geoocoding Parameters"
bulk_mapquest_query_input_id              =   "mapquestbulkquery"
bulk_mapquest_query_input_idList          =   ["bmqclientid",
                                               "bmqclientsecret",
                                               "bmqaddress",
                                               "bmqcolumnname",
                                               "bmqlanguage",
                                               "bmqregion",
                                               "bmqbulknumberlimit",
                                               "bmqbulkcheclpointsize",
                                               "bmqbulkfailurelimit",
                                               "bmqdropaddress",
                                               "bmqsaveaddress",
                                               None,None,None,None,None,None,None]

bulk_mapquest_query_input_labelList       =   ["mapquest_client_id",
                                               "mapquest_client_secret",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_mapquest_query_input_typeList        =   ["text","text",maketextarea(4),"text","text",
                                               "text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_mapquest_query_input_placeholderList =  ["mapquest client id (premium) - google api key (standard)",
                                              "mapquest client secret (premium)",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                               None,None,None,None,None,None,None]

bulk_mapquest_query_input_jsList          =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.BingId)+")"]

bulk_mapquest_query_input_reqList         =   [0,1,2,3,4,5]

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
bulk_nominatim_query_input_title          =   "Nominatim Bulk Geoocoding Parameters"
bulk_nominatim_query_input_id             =   "nominatimbulkquery"
bulk_nominatim_query_input_idList         =   ["bnqclientid",
                                               "bnqclientsecret",
                                               "bnqaddress",
                                               "bnqcolumnname",
                                               "bnqlanguage",
                                               "bnqregion",
                                               "bnqbulknumberlimit",
                                               "bnqbulkcheclpointsize",
                                               "bnqbulkfailurelimit",
                                               "bnqdropaddress",
                                               "bnqsaveaddress",
                                               None,None,None,None,None,None,None]

bulk_nominatim_query_input_labelList      =   ["mapquest_client_id",
                                               "mapquest_client_secret",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "language",
                                               "region",
                                               "max_addresses_to_geocode",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_nominatim_query_input_typeList       =   ["text","text",maketextarea(4),"text","text",
                                               "text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_nominatim_query_input_placeholderList =  ["mapquest client id (premium) - google api key (standard)",
                                              "mapquest client secret (premium)",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                               None,None,None,None,None,None,None]

bulk_nominatim_query_input_jsList         =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.BingId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.BingId)+")"]

bulk_nominatim_query_input_reqList        =   [0,1,2,3,4,5]

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


def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.GEOCODERS_TABLE,showfull=False) :
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

    print("display_bulk_geocode_inputs",geocid,geotype,tabletype,showfull)
    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
    
    if (geotype == sugm.GEOCODE_QUERY) :
        if(tabletype==sugm.GEOCODERS_TABLE) :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_table
            geo_parms_html = get_geocoder_table(True) 
            
        if(tabletype==sugm.COLNAMES_TABLE) :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_df_col_names_table("gegdfcolnamesTable",cfg.SWGeocodeUtility_ID,"gb_google_add_df_column")
            else :
                geo_parms_html = get_df_col_names_table("geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"gb_arcgis_add_df_column")
                
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"gb_select_language")
            
        elif(tabletype==sugm.REGION_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_regions_table("gegdfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_region")
            else :
                geo_parms_html = get_regions_table("geadfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_country",True)
                
        elif(tabletype==sugm.CATEGORIES_TABLE) :
            geo_parms_html = get_categories_table("gedfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_category")
            
        if(geocid == sugm.GoogleId) :
            form    =   bulk_google_query_input_form
        elif(geocid == sugm.ArcGISId) :
            form    =   batch_arcgis_query_form
        elif(geocid == sugm.BingId) :
            form    =   bulk_bing_query_input_form
        elif(geocid == sugm.OpenMapQuestId) :
            form    =   bulk_mapquest_query_input_form
        elif(geocid == sugm.NominatimId) :
            form    =   bulk_nominatim_query_input_form

    else :
        from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_parms_table
        geo_parms_html = get_geocoder_parms_table(geocid)
        
        if(geocid == sugm.GoogleId) :
            form    =   bulk_google_reverse_input_form
#        elif(geocid == sugm.ArcGISId) :
#            form    =   batch_arcgis_query_form
#        elif(geocid == sugm.BingId) :
#            form    =   sugw.bing_query_form
#        elif(geocid == sugm.OpenMapQuestId) :
#            form    =   sugw.mapquest_query_form
#        elif(geocid == sugm.NominatimId) :
#            form    =   sugw.nomin_query_form
    
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
    
    if (geotype == sugm.GEOCODE_QUERY) :
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Dataframe Address(s) To Coordinates</h4>" 
    else :
        geofunc_heading_html = "<h4>&nbsp;&nbsp;&nbsp;Convert Dataframe Coordinates To Address</h4>"
        
    display_grid("acconv_wrapper",
                 geofunc_heading_html,
                 geo_parms_html,
                 geofunc_input_html,
                 None)



def display_bulk_geocoding(optionId) :
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
    
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
            
        if(optionId == sugm.DISPLAY_BULK_GEOCODE_QUERY) :
        
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.GEOCODE_QUERY)
            
            if( not( geocid in sugm.supported_Bulk_Geocoders) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                opstat.set_errorMsg("Bulk geoocoding is not supported for the currently selected geocoder")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.GEOCODE_QUERY)    
                
        else :
            
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.GEOCODE_REVERSE)            
            
            if( not( geocid in sugm.supported_Bulk_Reverses) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                opstat.set_errorMsg("Bulk reverse geoocoding is not supported for the currently selected geocoder")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.GEOCODE_REVERSE)    


def validate_bulk_geocoding_connector(geocId) :
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

    """
        if(geocid == sugm.GoogleId)  :
                
            notes   =   []
            fparms  =   cfg.get_config_value("googlegeocoderParms")
            if(fparms == None) :
                
                sugw.display_geocoders(geocid,False,False)
                notes.append("You must enter a required client_id and secret_key for the google bulk geocoder")
                from dfcleanser.common.common_utils import display_msgs
                display_msgs(notes,None)
                    
            else :
                    
                if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :
                        
                    sugw.display_geocoders(geocid,False,False) 
                    notes.append("You must enter a required client_id and secret_key for the google bulk geocoder")
                    from dfcleanser.common.common_utils import display_msgs
                    display_msgs(notes,None)
                        
                else :   
                
                    if(optionId == sugm.DISPLAY_BULK_GEOCODE_QUERY) :
                        display_bulk_geocode_inputs(geocid,sugm.GEOCODE_QUERY) 
                    else :
                        display_bulk_geocode_inputs(geocid,sugm.GEOCODE_REVERSE)                
                
        elif(geocid == sugm.NominatimId) :
                
            if(optionId == sugm.DISPLAY_BULK_GEOCODE_QUERY) :
                display_bulk_geocode_inputs(geocid,sugm.GEOCODE_QUERY) 
            else :
                display_bulk_geocode_inputs(geocid,sugm.GEOCODE_REVERSE)                
                
        elif(geocid == sugm.ArcGISId) : 
                
            fparms  =   []
            notes   =   []
                
            fparms = cfg.get_config_value(batch_arcgis_query_id + "Parms")
                
            if(fparms == None) :
                afparms  =   cfg.get_config_value(sugw.arcgis_geocoder_id + "Parms")
                if(not (afparms == None)) :
                    fparms  =   []
                    for i in range(3) :
                        fparms.append(afparms[i]) 
                    for i in range(3,len(batch_arcgis_query_idList)) :
                        fparms.append("")
                    cfg.set_config_value(batch_arcgis_query_id + "Parms",fparms)
                
            if(fparms == None) :
                
                sugw.display_geocoders(geocid,False,False) 
                notes.append("You must enter a required username and password for the arcGIS bulk geocoder")
                from dfcleanser.common.common_utils import display_msgs
                display_msgs(notes,None)
                    
            else :
                    
                if( (len(fparms[0]) == 0) or (len(fparms[1]) == 0)) :
                    
                    sugw.display_geocoders(geocid,False,False) 
                    notes.append("You must enter a required username, password and user agent for the arcGIS bulk geocoder")
                    from dfcleanser.common.common_utils import display_msgs
                    display_msgs(notes,None)
                        
                else :
                        
                    # check the geocoder parms and get the batch size
                    if(len(fparms[6]) == 0) :
                        from dfcleanser.common.common_utils import RunningClock
                        clock = RunningClock()
                        clock.start()
                        
                        from dfcleanser.common.common_utils import display_notes
                        notes = ["getting arcGIS bulk geocoder connect values"]
                        display_notes(notes)
                        
                        from dfcleanser.sw_utilities.sw_utility_bulk_geocode_control import test_arcgis_batch_connection
                        test_arcgis_batch_connection(fparms[0],fparms[1],opstat)
                        clock.stop()
                            
                        if(opstat.get_status()) :
                            fparms      =   cfg.get_config_value(batch_arcgis_query_id + "Parms")
                            fparms[6]   =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))   
                            cfg.set_config_value(batch_arcgis_query_id + "Parms",fparms)
                        
                        from IPython.display import clear_output
                        clear_output()

                    if(optionId == sugm.DISPLAY_BULK_GEOCODE_QUERY) :
                        display_bulk_geocode_inputs(geocid,sugm.GEOCODE_QUERY) 
                    else :
                        display_bulk_geocode_inputs(geocid,sugm.GEOCODE_REVERSE) 
                                
                    if(not(opstat.get_status())) :
                        print("\n")
                        display_exception(opstat)
                     
        else :
            sugw.display_geocode_main_taskbar() 
            display_status("Bulk Geocoding not supported for Current Geocoder : "+ sugm.get_geocoder_title(geocid))
    """

def get_bulk_input_parms(geocid,inputs) :
    
    if(geocid == sugm.GoogleId) :
        return(get_parms_for_input(inputs,bulk_google_query_input_idList))
    else :
        return(get_parms_for_input(inputs,batch_arcgis_query_idList))





def validate_bulk_parms(geocid,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geocid       - geocoder id
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}
    
    if(geocid == sugm.GoogleId) :

        fparms = get_parms_for_input(inputs,bulk_google_query_input_idList)

        # check the required parms 
        if(len(fparms[1]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No client_id defined")
        else :
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[1] : fparms[1]})    
            if(len(fparms[2]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No secret_key defined")
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[2] : fparms[2]})     
                if(len(fparms[3]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No address columns defined")
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[3] : fparms[3]})     

        if(opstat.get_status()) :
            
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})
                
            if(len(fparms[5]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})  

            if(len(fparms[6]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(len(get_dfc_dataframe()))})
            else :
                if(int(fparms[6]) > len(get_dfc_dataframe())) :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(len(get_dfc_dataframe()))})
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : fparms[6]})

            if(len(fparms[7]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : str(2000)})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : fparms[7]})

            if(len(fparms[8]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : "5"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : fparms[8]}) 

            if(len(fparms[9]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : "False"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : "True"}) 

            if(len(fparms[10]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : fparms[10]})
        
    else :
        
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

