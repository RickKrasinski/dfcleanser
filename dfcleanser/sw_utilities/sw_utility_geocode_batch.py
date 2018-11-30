"""
# sw_utility_geocode_batch 
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
from dfcleanser.common.common_utils import (display_grid, opStatus, get_parms_for_input, display_exception, display_status)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

import time
import googlemaps
import arcgis
import json


"""
#--------------------------------------------------------------------------
#    arcgis bulk parameters 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqclientid",
                                               "bgqclientsecret",
                                               "bgqaddress",
                                               "bgqcolumnname",
                                               "bgqlanguage",
                                               "bgqregion",
                                               "bgqbulknumberlimit",
                                               "bgqbulkcheclpointsize",
                                               "bgqbulkfailurelimit",
                                               "bgqdropaddress",
                                               "bgqsaveaddress",
                                               None,None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["google_maps_client_id",
                                               "google_maps_client_secret",
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

bulk_google_query_input_typeList          =   ["text","text",maketextarea(4),"text","text",
                                               "text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["google_maps client id (premium) - google api key (standard)",
                                              "google_maps client secret (premium)",
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

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.GoogleId)+")"]

bulk_google_query_input_reqList           =   [0,1,2,3,4,5]

bulk_google_query_input_form              =   [bulk_google_query_input_id,
                                               bulk_google_query_input_idList,
                                               bulk_google_query_input_labelList,
                                               bulk_google_query_input_typeList,
                                               bulk_google_query_input_placeholderList,
                                               bulk_google_query_input_jsList,
                                               bulk_google_query_input_reqList]  


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
                                          "baqaddress",
                                          "baqcolumnname",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqbatchsize",
                                          "baqbulknumberlimit",
                                          "baqbulkcheckpointsize",
                                          "baqdropaddress",
                                          "baqsaveaddress",
                                          "baqbulkfailurelimit",
                                          "baqsearchextent",
                                          None,None,None,None,None,None,None]

batch_arcgis_query_labelList        =   ["arcgis_username",
                                         "arcgis_pw",
                                         "dataframe_address_columns",
                                         "new_dataframe_lat_long_column_name(s)",
                                         "source_country",
                                         "category",
                                         "batch_size",
                                         "max_addresses_to_geocode",
                                         "checkpoint_size",
                                         "failure_limit",
                                         "drop_df_address_columns_flag",
                                         "save_geocoder_address_column_name",
                                         "search_extent",
                                         "Get</br> Bulk </br>Coords",
                                         "Get</br> Column </br>Names",
                                         "Get</br> Countries",
                                         "Get</br> Categories",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   ["text","text",maketextarea(4),"text","text","text",
                                         "text","text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["arcgis username",
                                         "arcgis password",
                                         "select from 'Column Names' for aggregate address : constant value use '+ Buffalo'",
                                         "'colname' stored as [lat,long] - ['latcolname','longcolname'] stored as two cols",
                                         "source country (default - US)",
                                         "category (defailt - None)",
                                         "batch size (default - geocoder recommended value)",
                                         "max number of dataframe rows (default - all dataframe rows)",
                                         "checkpoint size (default - batch size)",
                                         "failure limit (default - 5%)",
                                         "drop address fields used in composite address (default = False)",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "A set of bounding box coords that limit the search area (default - None)",
                                         None,None,None,None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,None,None,None,None,None,None,
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


addresses = ["380 New York St, Redlands, CA",
         "1 World Way, Los Angeles, CA",
         "1200 Getty Center Drive, Los Angeles, CA",
         "5905 Wilshire Boulevard, Los Angeles, CA",
         "100 Universal City Plaza, Universal City, CA 91608",
         "4800 Oak Grove Dr, Pasadena, CA 91109"]

addresses1= [{
            "Address": "380 New York St.",
            "City": "Redlands",
            "Region": "CA",
            "Postal": "92373"
        },{
            "Address": "1 World Way",
            "City": "Los Angeles",
            "Region": "CA",
            "Postal": "90045"
        }]
    


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   google bulk coding
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_bulk_input_parms(geocid,inputs) :
    
    from dfcleanser.common.common_utils import get_parms_for_input
    if(geocid == sugm.GoogleId) :
        return(get_parms_for_input(inputs,bulk_google_query_input_idList))
    else :
        return(get_parms_for_input(inputs,batch_arcgis_query_idList))


"""
#--------------------------------------------------------------------------
#   google query and reverse status codes
#--------------------------------------------------------------------------
"""
OK_STATUS                   =   "OK"
ZERO_RESULTS_STATUS         =   "ZERO_RESULTS"
OVER_DAILY_LIMIT_STATUS     =   "OVER_DAILY_LIMIT"
OVER_QUERY_LIMIT_STATUS     =   "OVER_QUERY_LIMIT"
REQUEST_DENIED_STATUS       =   "REQUEST_DENIED"
INVALID_REQUEST_STATUS      =   "INVALID_REQUEST"
UNKNOWN_ERROR_STATUS        =   "UNKNOWN_ERROR"


"""
#--------------------------------------------------------------------------
#   google geocode method codes
#--------------------------------------------------------------------------
"""
GEOCODE_QUERY               =   0
GEOCODE_REVERSE             =   1

"""
#--------------------------------------------------------------------------
#   bulk geocoder codes
#--------------------------------------------------------------------------
"""
GOOGLE_BULK_GEOCODER        =   0
ARCGIS_BULK_GEOCODER        =   1





def run_google_geocode(address) :

    client_id       =   ""
    client_secret   =   ""
    gmaps = googlemaps.Client(client_id=client_id, client_secret=client_secret)

    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    return(geocode_result)

def run_google_reverse(lat_long) :

    client_id       =   ""
    client_secret   =   ""
    gmaps = googlemaps.Client(client_id=client_id, client_secret=client_secret)
    
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((lat_long[0], lat_long[1]))
    return(reverse_geocode_result)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   arcgis batch geocoding base methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_arcgis_batch_geocode_connection(user,pw,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get an arcgis batch connection and return the batch parms
    * 
    * parms :
    *  user   - arcgis user id
    *  pw     - arcgis passowrd
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    from arcgis.gis import GIS
    from arcgis.geocoding import get_geocoders
    
    gis = GIS("http://www.arcgis.com", user, pw)

    geoocoder_not_found       =   True
    
    while (geoocoder_not_found) :
        for i in range(5) :
            if(geoocoder_not_found) :
                try :
                    geocoder                =   get_geocoders(gis)[0]
                    geoocoder_not_found     =   False

                except Exception as e:
                    opstat.store_exception("Unable to connect to arcgis ",e)

    if(opstat.get_status()) :
        
        arcgis_MaxBatchSize         =   geocoder.properties.locatorProperties.MaxBatchSize
        arcgis_SuggestedBatchSize   =   geocoder.properties.locatorProperties.SuggestedBatchSize
        
        return([geocoder,[arcgis_MaxBatchSize,arcgis_SuggestedBatchSize]])
    
    else :
        
        return(None)
        


def test_arcgis_batch_connection(user,pw,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : test the arcgis batch connection and retrieve the batch parms
    * 
    * parms :
    *  user   - arcgis user id
    *  pw     - arcgis passowrd
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    cparms  =   get_arcgis_batch_geocode_connection(user,pw,opstat)
    
    if(opstat.get_status()) :
        cfg.set_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,cparms[1][0])
        cfg.set_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,cparms[1][1])
        

def run_arcgis_geocode(geocoder,addresslist) :

    from arcgis.geocoding import batch_geocode
    results = batch_geocode(addresslist)

    coord_fields = results[0].keys()

    #dict_keys(['score', 'attributes', 'address', 'location'])

    category = "Address"
    
    
    
    
    
"""
batch_geocode(addresses, source_country=None, category=None, out_sr=None, geocoder=None) 

categories
https://developers.arcgis.com/rest/geocode/api-reference/geocoding-category-filtering.htm#ESRI_SECTION1_502B3FE2028145D7B189C25B1A00E17B   
"""
    
def run_arcgis_reverse(lat_long) :

    client_id       =   ""
    client_pw   =   ""


"""
#--------------------------------------------------------------------------
#   google geocoding class for getting coords
#--------------------------------------------------------------------------
"""
class google_geocode_results:
    
    results         =   None
    status          =   None
    
    def init_(self,geocode_response) :
        self.results = geocode_response.get("results",None)
        self.status  = geocode_response.get("status",None)

    def get_status(self) :
        return(self.status)
    
    def get_error_message(self) :
        return(self.results.get("error_message",None))

    def get_lat_long(self) :
        
        lat_long    =   None
        
        geom        =   self.results.get("geometry",None)
        if(not(geom==None)) :
            loc         =   geom.get("location",None)
            if(not(loc==None)) :
                lat_long    =   [loc.get("lat"),loc.get("long",None)]
        
        # check values and return None if error
        return(lat_long)
        
    def get_address(self) :
        addr    = self.results.get("formatted_address",None)
        
        #check error codes
        return(addr)
        
"""
#--------------------------------------------------------------------------
#   google reverse class for getting addresses
#--------------------------------------------------------------------------
"""
class google_reverse_results:
    
    results         =   None
    status          =   None
    
    def init_(self,reverse_response) :
        self.results = reverse_response.get("results",None)
        self.status  = reverse_response.get("status",None)

    def get_status(self) :
        return(self.status)

    def get_long_lat(self) :
        
        lat_long    =   None
        
        geom        =   self.results.get("geometry",None)
        if(not(geom==None)) :
            loc         =   geom.get("location",None)
            if(not(loc==None)) :
                lat_long    =   [loc.get("lat"),loc.get("long",None)]
        
        # check values and return None if error
        return(lat_long)
        
    def get_address(self) :
        addr    = self.results.get("formatted_address",None)
        
        #check error codes
        return(addr)
        
    def get_address_fields(self) :
        addr        =   self.results.get("address_components",None)
        addrcomps   =   google_address_components(addr)
        return(addrcomps) 
        
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  google address components objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#   address field identifiers
"""
ADDRESS             =   0
NEIGHBORHOOD        =   1
CITY                =   2
COUNTY              =   3
STATE               =   4
COUNTRY             =   5
ZIPCODE             =   6

"""
#   google address field keys
"""
ADDRESS_1_KEY       =   "street_number"
ADDRESS_2_KEY       =   "route"
NEIGHBORHOOD_KEY    =   "neighborhood"
CITY_KEY            =   "sublocality"
COUNTY_KEY          =   "administrative_area_level_2"
STATE_KEY           =   "administrative_area_level_1"
COUNTRY_KEY         =   "country"
ZIPCODE_KEY         =   "postal_code"


"""
#--------------------------------------------------------------------------
#  google address components class for getting individual address fields
#--------------------------------------------------------------------------
"""
class google_address_components:
    
    full_address_components  =   None
    long_address_components  =   None

    def init_(self,addr_comps) :
        self.address_components = addr_comps
        
        self.long_address_components = {}
        
        for i in len(self.full_address_components) :
            self.long_address_components.update({self.full_address_components(i).get("types")[0] : self.full_address_components(i).get("long_name")})

    def get_street_addr(self) :
        
        street_number   =   ""
        street          =   ""
        
        if(not(self.long_address_components.get(ADDRESS_1_KEY) == None)) :
            street_number = self.long_address_components.get(ADDRESS_1_KEY)
        if(not(self.long_address_components.get(ADDRESS_2_KEY) == None)) :
            street = self.long_address_components.get(ADDRESS_2_KEY)
        
        if( (len(street_number)>0) or (len(street)>0) ) :
            return(street_number + " " + street) 
        else :
            return(None)
        
    def get_neighborhood(self) :
        return(self.long_address_components.get(NEIGHBORHOOD_KEY,None))

    def get_city(self) :
        return(self.long_address_components.get(CITY_KEY,None))
        
    def get_county(self) :
        return(self.long_address_components.get(COUNTY_KEY,None))
        
    def get_state(self) :
        return(self.long_address_components.get(STATE_KEY,None))

    def get_country(self) :
        return(self.long_address_components.get(COUNTRY_KEY,None))
        
    def get_zip_code(self) :
        return(self.long_address_components.get(ZIPCODE_KEY,None))
        




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoding bulk display methods
#--------------------------------------------------------------------------
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



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  bulk geocode tables 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
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


"""
#------------------------------------------------------------------
#   display input froms for query and reverse
#------------------------------------------------------------------
"""
def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.GEOCODERS_TABLE,showfull=False) :

    print("display_bulk_geocode_inputs",geocid,geotype,tabletype,showfull)
    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
    
    if (geotype == sugm.ADDRESS_CONVERSION) :
        if(tabletype==sugm.GEOCODERS_TABLE) :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_table
            geo_parms_html = get_geocoder_table()    
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

    else :
        from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_parms_table
        geo_parms_html = get_geocoder_parms_table(geocid)
        if(geocid == sugm.GoogleId) :
            form    =   bulk_google_query_input_form
        elif(geocid == sugm.ArcGISId) :
            form    =   batch_arcgis_query_form
    
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
    
    if (geotype == sugm.ADDRESS_CONVERSION) :
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
    
    geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        
    if(not (cfg.is_dc_dataframe_loaded())) :
            
        sugw.display_geocode_main_taskbar() 
        opstat.set_status(False)
        opstat.set_errorMsg("No dataframe is imported which is required for bulk geoocoding  ")
        display_exception(opstat)
            
    else :
            
        cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,True)

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
                
                    from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
                    if(optionId == sugm.DISPLAY_BULK_GET_COORDS) :
                        display_bulk_geocode_inputs(geocid,sugm.ADDRESS_CONVERSION) 
                    else :
                        display_bulk_geocode_inputs(geocid,sugm.COORDS_CONVERSION)                
                
        elif(geocid == sugm.NominatimId) :
                
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
            if(optionId == sugm.DISPLAY_BULK_GET_COORDS) :
                display_bulk_geocode_inputs(geocid,sugm.ADDRESS_CONVERSION) 
            else :
                display_bulk_geocode_inputs(geocid,sugm.COORDS_CONVERSION)                
                
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
                        print("getting arcGIS bulk geocoder connect values")
                            
                        test_arcgis_batch_connection(fparms[0],fparms[1],opstat)
                        clock.stop()
                            
                        if(opstat.get_status()) :
                            fparms      =   cfg.get_config_value(batch_arcgis_query_id + "Parms")
                            fparms[6]   =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))   
                            cfg.set_config_value(batch_arcgis_query_id + "Parms",fparms)
                        
                        from IPython.display import clear_output
                        clear_output()

                    from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
                    if(optionId == sugm.DISPLAY_BULK_GET_COORDS) :
                        display_bulk_geocode_inputs(geocid,sugm.ADDRESS_CONVERSION) 
                    else :
                        display_bulk_geocode_inputs(geocid,sugm.COORDS_CONVERSION) 
                                
                    if(not(opstat.get_status())) :
                        print("\n")
                        display_exception(opstat)
                     
        else :
            sugw.display_geocode_main_taskbar() 
            display_status("Bulk Geocoding not supported for Current Geocoder : "+ sugm.get_geocoder_title(geocid))




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process bulk geocodinig components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#------------------------------------------------------------------
#   test arcgis batch connector
#------------------------------------------------------------------
"""
def test_arcgis_connector(parms) :

    #geotype     =   parms[1]
    fparms      =   get_parms_for_input(parms[2],sugw.arcgis_geocoder_idList)  

    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()
    
    from dfcleanser.common.common_utils import RunningClock
    clock = RunningClock()
    clock.start()
    
    try :
    
        if(len(fparms) == 2) :
            test_arcgis_batch_connection(fparms[0],fparms[1],opstat)
            if(opstat.get_status()) :
                cfg.set_config_value(sugw.batch_arcgis_geocoder_id + "Parms",fparms)
                bulk_parms      =   cfg.get_config_value(batch_arcgis_query_id + "Parms")
                if(bulk_parms == None) :
                    bulk_parms  =   []
                    for i in range((len(batch_arcgis_query_idList)-7)) :
                        bulk_parms.append("")
                    
                bulk_parms[0]   =   fparms[0] 
                bulk_parms[1]   =   fparms[1]
                bulk_parms[6]   =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
                cfg.set_config_value(batch_arcgis_query_id + "Parms",bulk_parms)
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("arcGIS connect parms incomplete")
    
    except Exception as e:
        opstat.store_exception("Unable to connect to arcgis ",e)
    
    clock.stop()
    
    sugw.display_geocoders(sugm.ArcGISId,showfull=False,showNotes=False)
    
    if(opstat.get_status()) :
        from dfcleanser.common.common_utils import display_status, displayParms
        displayParms("arcGIS Batch Size Settings",
                     ["MaxBatchSize","SuggestedBatchSize"],
                     [str(cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)),
                      str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))],
                     cfg.SWUtilities_ID)
        display_status("arcGIS batch geocoder connected to successfully")
    else :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat) 



def get_geocode_address_string(address_vector,rowIndex) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get address string from address cols input parms
    * 
    * parms :
    *  address_vector   - address vector of names and name types
    *  rowIndex         - dataframe row index
    *
    * returns : 
    *  address string to feed geocoder
    * --------------------------------------------------------
    """
    
    geocode_address     =   ""
    
    from dfcleanser.common.common_utils import get_dc_dataframe
    df  =   get_dc_dataframe()
    
    for i in range(len(address_vector[0])) :
        if(address_vector[1][i]) :
            geocode_address.append(df.loc[rowIndex,[address_vector[0][i]]] + " ")            
        else :
            geocode_address.append(address_vector[0][i] + " ")   
    
    return(geocode_address)


def get_address_map(address_cols) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get address object from address cols input parms
    * 
    * parms :
    *  address_cols       - address column names input parm
    *
    * returns : 
    *  address vector of names and name types
    * --------------------------------------------------------
    """
    
    address_vector      =   [[],[]]
    
    address_cols        =   address_cols.replace(",","")
    address_components  =   address_cols.split("+")
    
    colnames            =   cfg.get_dc_dataframe().columns.values.tolist() 
   
    for i in range(len(address_components)) :
        address_vector[0].append(address_components[i])
        if(not(address_components[i] in colnames)) :
            address_vector[1].append(False)
        else :
            address_vector[1].append(True)
            
    return(address_vector)


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
    from dfcleanser.common.common_utils import get_parms_for_input,get_dc_dataframe
    
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
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(len(get_dc_dataframe()))})
            else :
                if(int(fparms[6]) > len(get_dc_dataframe())) :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(len(get_dc_dataframe()))})
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
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : str(len(get_dc_dataframe()))})
            else :
                if(int(fparms[7]) > len(get_dc_dataframe())) :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : str(len(get_dc_dataframe()))})
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : fparms[7]})
            
            if(len(fparms[8]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : fparms[6]})

            if(len(fparms[9]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : "5"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : fparms[9]}) 

            if(len(fparms[10]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : "False"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : "True"}) 

            if(len(fparms[11]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[11] : fparms[11]})
                
            if(len(fparms[12]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[12] : fparms[12]}) 
                
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


"""
#--------------------------------------------------------------------------
#   run google bulk geocoding
#--------------------------------------------------------------------------
"""
def run_google_bulk_geocode(runParms,opstat,state) :
    
    print("run_google_bulk_geocode",runParms) 
    

"""
#--------------------------------------------------------------------------
#   run google bulk geocoding
#--------------------------------------------------------------------------
"""
def run_arcgis_bulk_geocode(runParms,opstat,state) :
    """
    * -------------------------------------------------------------------------- 
    * function : run the arcgis bulk geocoder
    * 
    * parms :
    *  runParms     - arcgis run parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    #print("\nrun_arcgis_bulk_geocode :",state,"\n",runParms) 

    if(state == sugm.LOAD) :
        #print("\nrun_arcgis_bulk_geocode : LOAD\n",runParms) 
        address_map     =   get_address_map(runParms.get(batch_arcgis_query_labelList[2]))
    
        if(opstat.get_status()) :
            display_geocoder_console(sugm.ArcGISId,runParms,opstat)
            load_geocode_runner(sugm.ArcGISId,runParms,address_map)
    
    elif(state == sugm.BULK_START_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : START\n",runParms)
        display_geocoder_console(sugm.ArcGISId,runParms,opstat,sugm.RUNNING)
    
    elif(state == sugm.BULK_STOP_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : STOP\n",runParms)
        display_geocoder_console(sugm.ArcGISId,runParms,opstat,sugm.STOPPED)

    elif(state == sugm.BULK_PAUSE_GEOCODER) :
        #print("\nrun_arcgis_bulk_geocode : PAUSE\n",runParms)
        display_geocoder_console(sugm.ArcGISId,runParms,opstat,sugm.PAUSED)
    
def get_bulk_coords(geocid,inputs,state=sugm.LOAD) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the bulk coords - validate parms and load job runner
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    #print("get_bulk_coords",geocid,state,"\n",inputs)
    
    opstat      =   opStatus()
    if(not (inputs == None)) :
        runParms    =   validate_bulk_parms(geocid,inputs,opstat) 
    else :
        if(geocid == sugm.ArcGISId) :
            parms   =   cfg.get_config_value(batch_arcgis_query_id+"Parms")
        elif(geocid == sugm.GoogleId) :
            parms   =   cfg.get_config_value(bulk_google_query_input_id+"Parms")
        
        runParms    =   validate_bulk_parms(geocid,parms,opstat) 
            
    #print("\nget_bulk_coords \n",runParms)
    
    if(opstat.get_status()) :
        
        if(geocid == sugm.GoogleId) :
            run_google_bulk_geocode(runParms,opstat,state)
        else :
            run_arcgis_bulk_geocode(runParms,opstat,state)
        
    else :
        display_bulk_geocoding(sugm.DISPLAY_BULK_GET_COORDS)
        display_exception(opstat)
       
    

def process_bulk_geocoding(optionId,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : process the bulk geocoding commands
    * 
    * parms :
    *  optionId     - geocoder identifier
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    #print("\nprocess_bulk_geocoding",optionId,parms)
    
    from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
    sugw.display_geocode_main_taskbar() 
        
    fid     =   int(parms[0])
    geocid  =   int(parms[1])
    geotype =   int(parms[2])
    inputs  =   parms[3]
    
    if(not (inputs == None)) :
        inputs  =   json.loads(inputs)
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import get_bulk_input_parms
        inputs  =   get_bulk_input_parms(geocid,inputs)
    else :
        inputs  =   cfg.get_config_value("arcgisbatchquery"+"Parms")
            
    if(geocid == sugm.GoogleId) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import bulk_google_query_input_id
        cfg.set_config_value(bulk_google_query_input_id+"Parms",inputs)
    else :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import batch_arcgis_query_id
        cfg.set_config_value(batch_arcgis_query_id+"Parms",inputs)
           
    #print("process_bulk_geocoding",fid,geocid,inputs) 
        
    if(fid == sugm.BULK_GET_COORDS) :
        get_bulk_coords(geocid,inputs)           
    elif(fid == sugm.BULK_GET_ADDRESS_COLS) :
        display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)
    elif(fid == sugm.BULK_GET_LANGUAGES) :
        display_bulk_geocode_inputs(geocid,geotype,sugm.LANGUAGE_TABLE)
    elif(fid == sugm.BULK_GET_REGIONS) :
        display_bulk_geocode_inputs(geocid,geotype,sugm.REGION_TABLE)
    elif(fid == sugm.BULK_GET_COUNTRIES) :
        display_bulk_geocode_inputs(geocid,geotype,sugm.REGION_TABLE)
    elif(fid == sugm.BULK_GET_CATEGORIES) :
        display_bulk_geocode_inputs(geocid,geotype,sugm.CATEGORIES_TABLE)
        
    elif(fid == sugm.BULK_CLEAR) :
        if(geocid == sugm.GoogleId) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import bulk_google_query_input_id
            bparms = cfg.get_config_value(bulk_google_query_input_id+"Parms")
            for i in range(len(bparms)) :
                if(i>0) : bparms[i] = ""
            cfg.set_config_value(bulk_google_query_input_id+"Parms",bparms)
        else :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import batch_arcgis_query_id
            bparms = cfg.get_config_value(batch_arcgis_query_id+"Parms")
            for i in range(len(bparms)) :
                if(i>0) : bparms[i] = ""
            cfg.set_config_value(batch_arcgis_query_id+"Parms",bparms)

        display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)
        
    elif(fid == sugm.BULK_RETURN) :
        from dfcleanser.sw_utilities.sw_utility_geocode_control import display_geocode_utility
        display_geocode_utility(sugm.DISPLAY_GEOCODING)
                
    elif(fid == sugm.BULK_HELP) :
        if(geocid == sugm.GoogleId) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import bulk_google_query_input_id
            bparms = cfg.get_config_value(bulk_google_query_input_id+"Parms")
        else :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import batch_arcgis_query_id
            bparms = cfg.get_config_value(batch_arcgis_query_id+"Parms")
            
        print("BULK_HELP",bparms)
        display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)

    elif(fid == sugm.BULK_START_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)

    elif(fid == sugm.BULK_PAUSE_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)
        
    elif(fid == sugm.BULK_STOP_GEOCODER) :
        get_bulk_coords(geocid,inputs,fid)



def process_test_bulk_connector(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : process commands from test the bulk geocoder
    * 
    * parms :
    *  parms        - input parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fid     =   int(parms[0]) 
        
    if(fid == sugm.BATCH_TEST_CONNECTOR) :
        test_arcgis_connector(parms)
            
    if(fid == sugm.BULK_GET_COORDS) :
        geocid  = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        geotype = int(parms[1])
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs            
        display_bulk_geocode_inputs(geocid,geotype)            
            
    if(fid == sugm.BATCH_CLEAR)     :
        cfg.drop_config_value("arcgisbatchgeocoder"+"Parms")
        cfg.drop_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)
        cfg.drop_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)            
            
        geotype = int(parms[1])
        sugw.display_geocoders(sugm.ArcGISId,showfull=False,showNotes=False)
            
    if(fid == sugm.BATCH_RETURN)    :
        geotype = int(parms[1])
        if(geotype == sugm.DISPLAY_GET_COORDS) :
            sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)
        else :
            sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,parms,sugm.REVERSEPARMS)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

bulk_console_title = """<div class="dfc-console-title">
    <p class="dfc-console-title" style='text-align: center; font-size: 20px; font-family: Arial; font-weight: bold; margin: auto;'>Bulk Geocoding Run Console</p>
</div>
<br>
"""
    
bulk_console_container = """<div class="dfc-console-container" style=' width: 60%; text-align: center; margin: auto; border: 1px solid #428bca;'>
    <div style="text-align: center; margin:auto; margin-top:20px;">
        <table class="tableRowHoverOff" id="geocodeStatusBars" style="margin:auto; width: 90%;">
            <tbody>
"""
                
bulk_console_progress_row = """                    <tr class='dfc-progress-row' style='height: 30px;'>
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;'>"""

bulk_console_progress_col = """                        <td class='dfc-progress-col' style='width: 55%;'>
                            <div class='progress md-progress dfc-progress-div' style='height: 20px; '>
                                <div """

bulk_console_progress_col1 = """ class='progress-bar dfc-progress-bar' role='progressbar' style='height: 20px;'"""

bulk_console_progress_row_end = """                            </div>
                        </td>
                    </tr>
"""
                    
bulk_console_container_end = """            </tbody>
        </table>
    </div>
"""

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:100%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(22)">Run</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(23)">Pause</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(24)">Stop</button>
            </div>
        </div>
"""

bulk_console_status = """        <div style=' width: 30%; text-align: center; height: 30px; margin: auto;'>
            <p id='bulkstatus' style='height: 30px; padding-top: 5px; text-align: center; font-size: 14px; font-family: Arial; color: #474747; font-weight: bold; """
bulk_console_status1 = """ : margin: auto;'>"""
bulk_console_status2 = """</p>
        </div>
        <br>
"""

bulk_console_end = """</div>
"""

def set_progress_bar_value(geocid,barid,barvalue) :
    
    if(geocid == sugm.ArcGISId) :
        
        if(barid == 0)  :   bid = "arcgistotaladdrs"
        else            :   bid = "arcgiserrorrate"
        
    elif(geocid == sugm.GoogleId) :

        if(barid == 0)  :   bid = "googletotaladdrs"
        else            :   bid = "googleerrorrate"

    set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(set_progress_bar_js,
                "fail to set progress bar : ",
                 str(bid))

def set_status_bar(status) :
    
    btext   =   ""
    
    from dfcleanser.system.system_model import Green,Red,Yellow
    if(status == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(status == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(status == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"

    if(len(btext) > 0) :
        set_status_bar_js = "set_bulk_progress_status('" + str(btext) + "', '" + str(bcolor) + "');"
    
        print("set_status_bar_js",set_status_bar_js)
        from dfcleanser.common.common_utils import run_jscript
        run_jscript(set_status_bar_js,
                    "fail to set progress status color : ",
                    str(btext))



def get_progress_bar_html(barParms) :
    
    # bartitle,barid,barmin,barmax,progress
    from dfcleanser.common.html_widgets import addattribute, addstyleattribute, new_line
    
    bar_html = ""
    bar_html = (bar_html + bulk_console_progress_row)
    bar_html = (bar_html + barParms[0] + "</td>" + new_line)
    bar_html = (bar_html + bulk_console_progress_col)
    bar_html = (bar_html + addattribute("id",barParms[1]))
    bar_html = (bar_html + bulk_console_progress_col1)    
    bar_html = (bar_html + addattribute("style",addstyleattribute("width",str(barParms[4])+"%")))
    bar_html = (bar_html + addattribute("aria-valuenow",str(barParms[4])))
    bar_html = (bar_html + addattribute("aria-valuemin",str(barParms[2])))
    bar_html = (bar_html + addattribute("aria-valuemax",str(barParms[3])))
    bar_html = (bar_html + ">" + str(barParms[4]) + "%" + "</div>" + new_line)
    bar_html = (bar_html + bulk_console_progress_row_end)
    
    return(bar_html)

def get_bulk_geocode_console_html(progressbarList,state) :
    
    console_html = ""
    console_html = (console_html + bulk_console_title)
    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))    
    
    console_html = (console_html + bulk_console_container_end)  
    console_html = (console_html + bulk_console_commands)
    
    from dfcleanser.system.system_model import Green,Red,Yellow    
    if(state == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(state == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(state == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"
    
    console_html = (console_html + bulk_console_status)
    from dfcleanser.common.html_widgets import addstyleattribute
    console_html = (console_html + addstyleattribute("background-color",str(bcolor)))
    console_html = (console_html + bulk_console_status1 + btext)
    console_html = (console_html + bulk_console_status2)
    
    console_html = (console_html + bulk_console_end)  
        
    return(console_html)     
        
        
def display_geocoder_console(geocid,runParms,opstat,state=sugm.STOPPED) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the bulk geocoding console
    * 
    * parms :
    *  geocid       - geocoder identifier
    *  runParms     - run parameters
    *  address_set  - address col names
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    #print("display_geocoder_console",geocid,"\n",runParms)
    
    #sugw.display_geocode_main_taskbar()
    
    if(geocid == sugm.ArcGISId) :
        
        if(not(runParms == None)) :
            from dfcleanser.common.common_utils import displayParms, get_parms_list_from_dict 
            parms   =   get_parms_list_from_dict(batch_arcgis_query_labelList,runParms) 
            displayParms("arcGIS Bulk Geocoding Parms",batch_arcgis_query_labelList,parms,"arcgisbulkparms")

        bar0 = ["Total Addresses Geocoded","arcgistotaladdrs",0,100,0]
        bar1 = ["Geocode Error Rate","arcgiserrorrate",0,100,0]
        
        progressBars    =   [bar0,bar1]
        
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
        from dfcleanser.common.common_utils import displayHTML
        
        #print(console_html)
        displayHTML(console_html)
        
    elif(geocid == sugm.GoogleId) :
        print("google console")













"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding tasking components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""




        
"""
#--------------------------------------------------------------------------
#   geocoding factory class to monitor and control threads
#--------------------------------------------------------------------------
"""
class BulkGeocodingFactory :
    
    # stsic class variables
    total_geocode_runs      =   0
    total_elapsed_run_time  =   0
    halt_all_geocoding      =   False
    bulkgeocodeparms        =   []
    starttime               =   0
    
    # stsic class methods
    @staticmethod
    def init_() :
        BulkGeocodingFactory.total_geocode_runs      =   0
        BulkGeocodingFactory.total_elapsed_run_time  =   0
        BulkGeocodingFactory.halt_all_geocoding      =   False 
    
    @staticmethod
    def increment_goecode_runs() :
        BulkGeocodingFactory.total_geocode_runs  =   BulkGeocodingFactory.total_geocode_runs + 1
        
    @staticmethod
    def increment_run_times(elapsed_time) :
        BulkGeocodingFactory.total_elapsed_run_time  =   BulkGeocodingFactory.total_elapsed_run_time + elapsed_time
        
    @staticmethod
    def get_total_geocode_runs() :
        return(BulkGeocodingFactory.total_geocode_runs)
        
    @staticmethod
    def get_geocode_runs_rate() :
        return(BulkGeocodingFactory.total_geocode_runs / BulkGeocodingFactory.total_elapsed_run_time)
        
    @staticmethod
    def process_error_code(geocoderid,results) :
        
        # check if stoppable error
        if(0) :
            return(True)    
        else :
            return(False)
        
    @staticmethod
    def set_halt_flag(halt_state) :
        BulkGeocodingFactory.halt_all_geocoding  =   halt_state       
 
    def __init__(self):
        BulkGeocodingFactory.total_geocode_runs      =   0
        BulkGeocodingFactory.total_elapsed_run_time  =   0
        BulkGeocodingFactory.halt_all_geocoding      =   False
        BulkGeocodingFactory.bulkgeocodeparms        =   []
        BulkGeocodingFactory.starttime               =   0
    
    def bulk_geocoder_controller_task(self):
        while (not(BulkGeocodingFactory.halt_all_geocoding)) :
            
            # check geocoder task stats 
            # and update control as needed
            # and display the run statistics
            
            # clean up any tasks and start new ones
            
            # delay 1/10 second
            time.sleep(0.1)
            
            
    def start_bulk_geocoder_controller(self,bulkgeocodeparms) :
        self.bulkgeocodeparms   =   bulkgeocodeparms
        threading.Thread(target=self.bulk_geocoder_controller_task).start()
        self.starttime = time.time()

    def stop_bulk_geocoder_controller(self):
        self.runGeocoder = False





"""
#--------------------------------------------------------------------------
#   geocoding task class for multiple geocoding tasks
#--------------------------------------------------------------------------
"""

import threading

class GeocodeTask:
    
    runGeocoder     =   False
    delay           =   0.3
    starttime       =   0
    stoptime        =   0
    geocoderId      =   -1
    geoparms        =   None
    geocode_method  =   None
    geocode_results =   None  
 
        
    def __init__(self, geocoderId):
        self.geocoderId     =   geocoderId
        self.runGeocoder    =   False

    def geocoder_task(self):
        while (self.runGeocoder) and (not(GeocodeTask.halt_all_geocoding)) :
            self.run_geocode_method()
            # check error code
            GeocodeTask.set_halt_flag(GeocodeTask.process_error_code(self.geocoderid,self.results))
            
            # delay 2/10 second
            time.sleep(0.2)

    def run_geocoder(self,geocode_method,geoparms):
        self.geocode_method     =   geocode_method
        self.geoparms           =   geoparms
        self.runGeocoder        =   True
        threading.Thread(target=self.geocoder_task).start()
        import time
        self.starttime = time.time()

    def stop_geocoder(self):
        self.runGeocoder = False

    def get_run_results(self) :
        return(self.geocode_results)
 
    def run_geocode_method(self) :
        
        if(self.geocoderId == GOOGLE_BULK_GEOCODER) :
            if(self.geocode_method == GEOCODE_QUERY) :
                self.geocode_results = run_google_geocode(self.geoparms)
            elif(self.geocode_method == GEOCODE_REVERSE) :
                self.geocode_results = run_google_reverse(self.geoparms)
                
        elif(self.geocoderId == ARCGIS_BULK_GEOCODER) :
            if(self.geocode_method == GEOCODE_QUERY) :
                self.geocode_results = run_arcgis_geocode(self.geoparms)
            elif(self.geocode_method == GEOCODE_REVERSE) :
                self.geocode_results = run_arcgis_reverse(self.geoparms)
        

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   current geocoder running task
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""




"""
#--------------------------------------------------------------------------
#   common helper methopds
#--------------------------------------------------------------------------
"""
def load_geocode_runner(geocoderId,runParms,address_set) :
    dfc_Geocode_Runner.load_run(geocoderId,runParms,address_set)    

def start_geocode_runner() :
    dfc_Geocode_Runner.start_run() 
    
def stop_geocode_runner() :
    dfc_Geocode_Runner.stop_run() 
    
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
    
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 

def arcgis_run_next_batch(runParms) :
    print("arcgis_run_next_batch")

def google_run_next_geocode(runParms) :
    print("google_run_next_geocode")


       
class BulkGeocodeRunner:
    
    geocoder            =   None
    runParms            =   None
    addressParms        =   None
    rowindex            =   0
    errors              =   0
    state               =   sugm.STOPPED
    checkpoint_file     =   None
    halt_all_geocoding  =   True
 
        
    def __init__(self):
        self.geocoder           =   None
        self.runParms           =   None
        self.addressParms       =   None
        self.rowindex           =   0
        self.errors             =   0
        self.state              =   sugm.STOPPED
        self.checkpoint_file    =   None
        self.halt_all_geocoding =   True
        
    def load_run(self,geocoderId,runParms,addressParms):
        self.geocoder           =   geocoderId
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        
    def start_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.rowindex           =   0

    def stop_run(self):
        self.state              =   sugm.STOPPED
        BulkGeocodeRunner.halt_all_geocoding = True
            
    def pause_run(self):
        self.state              =   sugm.PAUSED
        BulkGeocodeRunner.halt_all_geocoding = True
    
    def resume_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        
    def get_run_state(self):
        return(self.state)
        
    def bulk_geocode_runner_task(self):
        while (not(BulkGeocodeRunner.halt_all_geocoding)) :
            
            if(self.geocoder == sugm.ArcGISId) :
                arcgis_run_next_batch(self.runParms)
            elif(self.geocoder == sugm.GoogleId) :
                google_run_next_geocode(self.runParms)
            else :
                BulkGeocodeRunner.halt_all_geocoding = True    
            # check geocoder task stats 
            # and update control as needed
            # and display the run statistics
            
            # clean up any tasks and start new ones
            
            # delay 1/10 second
            time.sleep(0.1)
            
            
    def start_bulk_geocode_runner(self,bulkgeocodeparms) :
        threading.Thread(target=self.bulk_geocode_runner_task).start()
    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        
