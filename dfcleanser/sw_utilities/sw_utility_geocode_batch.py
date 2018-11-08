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
import dfcleanser.common.help_utils as dfchelp

from dfcleanser.common.html_widgets import (maketextarea) 
from dfcleanser.common.common_utils import (display_grid)
from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)

"""
#--------------------------------------------------------------------------
#    arcgis bulk parameters 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "geocoderconnectorbulk"
bulk_google_query_input_idList            =   ["bgqapikey",
                                               "bgqaddress",
                                               "bgqcolumnname",
                                               "bgqdropaddress",
                                               "bgqsaveaddress",
                                               "bgqbulknumberlimit",
                                               "bgqbulkrunrate",
                                               "bgqbulkcheclpointsize",
                                               "bgqbulkfailurelimit",
                                               "bgqlanguage",
                                               "bgqregion",
                                               None,None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["google_api_key",
                                               "dataframe_composite_address",
                                               "new_column_name",
                                               "drop_Address_column_flag",
                                               "save_Address_column_name",
                                               "max_geocode_runs",
                                               "max_geocode_rate",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "language",
                                               "region",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Address</br>Columns",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_google_query_input_typeList          =   ["text",maketextarea(4),"text","text","text","text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["google api key",
                                              "select from 'Column Names' for constant value use 'val' ie.. 'Buffalo'",
                                              "single name : [lat,long] - two cols enter list [latname,longname]",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "max geocode get rate in geoocodes per second (default - 1/second)",
                                              "number of geocode results before checkpoint taken (default - 500) ",
                                              "failure rate in percent (default - 5%)",
                                              "language (default - english)",
                                              "region (default - None)",
                                              None,None,None,None,None,None,None]

bulk_google_query_input_jsList            =    [None,None,None,None,None,None,None,None,None,None,None,
                                                "process_bulk_query(0,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(1,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(2,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(3,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(4,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(5,"+str(sugm.GoogleId)+")",
                                                "process_bulk_query(6,"+str(sugm.GoogleId)+")"]

bulk_google_query_input_reqList           =   [0,1]

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
batch_arcgis_query_title            =   "arcGIS Geocoder Get Batch Coordinates"
batch_arcgis_query_id               =   "arcgisbatchquery"

batch_arcgis_query_idList           =    ["baqusername",
                                          "baqpw",
                                          "baqaddress",
                                          "baqcolumnname",
                                          "baqdropaddress",
                                          "baqsaveaddress",
                                          "baqbatchsize",
                                          "baqbulknumberlimit",
                                          "baqbulkcheclpointsize",
                                          "baqbulkfailurelimit",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqoutsr",
                                          None,None,None,None,None,None,None]

batch_arcgis_query_labelList        =   ["arcgis_username",
                                         "arcgis_pw",
                                         "dataframe_composite_address",
                                         "new_column_name",
                                         "drop_Address_column_flag",
                                         "save_Address_column_name",
                                         "batch_size",
                                         "max_geocode_runs",
                                         "checkpoint_size",
                                         "failure_limit",
                                         "source_country",
                                         "category",
                                         "out_sr",
                                         "Get</br> Bulk </br>Coords",
                                         "Get</br> Column </br>Names",
                                         "Get</br> Countries",
                                         "Get</br> Categories",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   ["text","text",maketextarea(4),"text","text","text","text",
                                         "text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["arcgis username",
                                         "arcgis password",
                                         "select from 'Column Names' for constant value use 'val' ie.. 'Buffalo'",
                                         "single name : [lat,long] - two cols enter list [latname,longname]",
                                         "drop address fields used in composite address (default = False)",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "batch size (default - geocoder recommended value",
                                         "max number of dataframe rows (default - len(datframe) )",
                                         "checkpoint size (default - batch size)",
                                         "failure limit (default - 5%)",
                                         "source country (defailt - US)",
                                         "category (defailt - None)",
                                         "out_sr (defailt - None)",
                                         None,None,None,None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,
                                         None,None,None,None,None,None,
                                         "process_bulk_query(0,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(1,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(2,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(3,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(4,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(5,"+str(sugm.ArcGISId)+")",
                                         "process_bulk_query(6,"+str(sugm.ArcGISId)+")"]


batch_arcgis_query_reqList          =   [0,1,2]

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



import googlemaps

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


def test_arcgis_connection(user,pw) :
    
    from arcgis.gis import GIS
    from arcgis.geocoding import get_geocoders

    gis = GIS("http://www.arcgis.com", user, pw)

    # use the first of GIS's configured geocoders
    geocoder = get_geocoders(gis)[0]

    arcgis_MaxBatchSize         =   geocoder.properties.locatorProperties.MaxBatchSize
    arcgis_SuggestedBatchSize   =   geocoder.properties.locatorProperties.SuggestedBatchSize
    
    cfg.set_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,arcgis_MaxBatchSize)
    cfg.set_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,arcgis_SuggestedBatchSize)
    


def run_arcgis_geocode(geocoder,addresslist) :

    from arcgis.geocoding import batch_geocode
    
    results = batch_geocode(addresslist)

    coord_fields = results[0].keys()

    #dict_keys(['score', 'attributes', 'address', 'location'])

    category = "Address"
    
    
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
#   geocoding factory class to monitor and control threads
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
class BulkGeocodingFactory :
    
    # stsic class variables
    total_geocode_runs      =   0
    total_elapsed_run_time  =   0
    halt_all_geocoding      =   False
    
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
 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoding task class for multiple geocoding tasks
#--------------------------------------------------------------------------
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
#   geocoding bulk display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#  get languages table
#--------------------------------------------------------------------------
"""
def get_languages_table(tableid,owner,callback) :

    languagesHeader      =   [""]
    languagesRows        =   []
    languagesWidths      =   [100]
    languagesAligns      =   ["left"]
    languagesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts       =   get_Dictlog()
    langdict    =   dicts.get("Language_Codes",None)
    languages   =   langdict.keys()
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
    languages_table.set_rowspertable(14)

    listHtml = get_row_major_table(languages_table,SCROLL_NEXT,False)
        
    return(listHtml)

"""
#--------------------------------------------------------------------------
#  get regions table
#--------------------------------------------------------------------------
"""
def get_regions_table(tableid,owner,callback) :

    regionsHeader      =   [""]
    regionsRows        =   []
    regionsWidths      =   [100]
    regionsAligns      =   ["left"]
    regionsHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts           =   get_Dictlog()
    regionsdict     =   dicts.get("Language_Codes",None)
    regions         =   regionsdict.keys()
    regions.sort()
    
    for i in range(len(regions)) :
        
        regionsrow = [regions[i]]
        regionsRows.append(regionsrow)
        regionsHrefs.append([callback])
        
    regions_table = None
                
    regions_table = dcTable("Regions",tableid,owner,
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
    regions_table.set_rowspertable(14)

    listHtml = get_row_major_table(regions_table,SCROLL_NEXT,False)
        
    return(listHtml)

"""
#--------------------------------------------------------------------------
#  get regions table
#--------------------------------------------------------------------------
"""
def get_categories_table(tableid,owner,callback) :

    categoriesHeader      =   [""]
    categoriesRows        =   []
    categoriesWidths      =   [100]
    categoriesAligns      =   ["left"]
    categoriesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_control import get_Dictlog
    dicts           =   get_Dictlog()
    regionsdict     =   dicts.get("Language_Codes",None)
    categories         =   regionsdict.keys()
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
    categories_table.set_rowspertable(14)

    listHtml = get_row_major_table(categories_table,SCROLL_NEXT,False)
        
    return(listHtml)


"""
#------------------------------------------------------------------
#   display input froms for query and reverse
#------------------------------------------------------------------
"""
def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.COLNAMES_TABLE,showfull=False) :

    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
    
    if (geotype == sugm.ADDRESS_CONVERSION) :
        from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
        if(tabletype==sugm.COLNAMES_TABLE) :
            geo_parms_html = get_df_col_names_table("gedfcolnamesTable",cfg.SWGeocodeUtility_ID,"add_df_column")
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"select_language")
        elif(tabletype==sugm.REGION_TABLE) :
            geo_parms_html = get_regions_table("gedfregionsTable",cfg.SWGeocodeUtility_ID,"select_region")
        elif(tabletype==sugm.CATEGORIES_TABLE) :
            geo_parms_html = get_categories_table("gedfregionsTable",cfg.SWGeocodeUtility_ID,"select_category")
            
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
























   
        
        
        
        
        
        
        
        
        