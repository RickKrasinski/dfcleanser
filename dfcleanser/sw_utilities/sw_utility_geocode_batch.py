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
                                               "bgqdropaddress",
                                               "bgqsaveaddress",
                                               "bgqbulknumberlimit",
                                               "bgqbulkrunrate",
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
                                               "drop_df_address_column(s)_flag",
                                               "save_geocoder_address_column_name",
                                               "max_addresses_to_geocode",
                                               "max_geocode_rate",
                                               "checkpoint_size",
                                               "failure_limit",
                                               "drop_df_address_columns_flag",
                                               "save_geocoder_address_column_name",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column </br>Names",
                                               "Get</br> Languages",
                                               "Get</br> Regions",
                                               "Clear","Return","Help"]

bulk_google_query_input_typeList          =   ["text","text",maketextarea(4),"text","text","text","text",
                                               "text","text","text","text","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["google_maps client id (premium) - google api key (standard)",
                                              "google_maps client secret (premium)",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "language (default - english)",
                                              "region (default - None)",
                                              "drop address columns used in aggregate address (default - False)",
                                              "retrieve aggregate address and store in column name (default - None - don't retrieve and save)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "geocode rate in geoocodes per second (default - 5/second - max 5/sec)",
                                              "number of geocode results before checkpoint taken (default - 2000) ",
                                              "failure limit (default - 5%)",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                               None,None,None,None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,None,None,None,None,
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


batch_arcgis_query_typeList         =   ["text","text",maketextarea(4),"text","text","text","text",
                                         "text","text","text","text","text","text",
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
    from arcgis.gis import GIS
    from arcgis.geocoding import get_geocoders
    
    gis = GIS("http://www.arcgis.com", user, pw)

    try :
        # use the first of GIS's configured geocoders
        geocoder = get_geocoders(gis)[0]

        arcgis_MaxBatchSize         =   geocoder.properties.locatorProperties.MaxBatchSize
        arcgis_SuggestedBatchSize   =   geocoder.properties.locatorProperties.SuggestedBatchSize
    
        cfg.set_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,arcgis_MaxBatchSize)
        cfg.set_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,arcgis_SuggestedBatchSize)
        
    except Exception as e:
        opstat.store_exception("Unable to connect to arcgis ",e)
        

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
#   geocoding factory class to monitor and control threads
#--------------------------------------------------------------------------
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
#  get regions table
#--------------------------------------------------------------------------
"""
def get_regions_table(tableid,owner,callback,countriesFlag=False) :

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



"""
def process_address_conversion(formid,parms) :
    
    print("process_address_conversion",formid,parms)
    
    opstat = opStatus()
    
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    
    if(formid == ADDRESS_CONVERSION) :
        

        if(len(parms[7]) > 0) :
            if(parms[7].find("[") > -1) :
                
                inlist = parms[7].lstrip("[")
                inlist = inlist.rstrip("]")
                new_column_names =  inlist.split(",")
            else :
                new_column_names =  [parms[7]]
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("No GPS Coords column name(s) defined")

        if(len(parms[8]) > 0) :
            delete_flag = True
        else :
            delete_flag = False
        
        if(opstat.get_status()) :
            
            try :
                for i in range(len(new_column_names)) :
                    set_dc_dataframe(get_dc_dataframe().assign(newcolname = new_column_names[i]))
            except Exception as e:
                opstat.store_exception("Add New GPS Coords Column(s) Error",e)
                
            if(opstat.get_status()) :
                
                for i in range(len(get_dc_dataframe())) :
                    address     =   ""
                    for j in range(len(parms) - 2) :
                        if(len(parms[j]) > 0) :
                            address =   (address + get_dc_dataframe().iloc[i:parms[j]] + " ")
            
                    if(len(address) > 0) :
                        location = geolocator.geocode(address)
                    else :
                        location = None
                        
                    if(len(new_column_names) == 1) :
                        get_dc_dataframe().iloc[i:new_column_names[0]] = [location.latitude, location.longitude]
                    else :
                        get_dc_dataframe().iloc[i:new_column_names[0]] = location.latitude
                        get_dc_dataframe().iloc[i:new_column_names[1]] = location.longitude
                        
                if(delete_flag) :
                    for i in range(len(parms) - 2) :
                        if(len(parms[i]) > 0) :
                            try :
                                set_dc_dataframe(get_dc_dataframe().drop([parms[i]],axis=1))
                            except Exception as e:
                                opstat.store_exception("Drop Column(s) Error" + parms[i],e)
                                display_exception(opstat)
                        
        else :
            display_exception(opstat)
            
    else : 
        
        if(len(parms[2]) > 0) :
            addr_column_name =  [parms[7]]
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("No Address column name defined")

        if(len(parms[3]) > 0) :
            delete_flag = True
        else :
            delete_flag = False
        
        if(opstat.get_status()) :
            
            try :
                set_dc_dataframe(get_dc_dataframe().assign(newcolname = addr_column_name))
            except Exception as e:
                opstat.store_exception("Add New GPS Coords Column(s) Error",e)
                
            if(opstat.get_status()) :
                
                for i in range(len(get_dc_dataframe())) :
                    address = geolocator.reverse(parms[0] + ", " + parms[1])
                    get_dc_dataframe().iloc[i:addr_column_name] = address
                        
                if(delete_flag) :
                    for i in range(2) :
                        if(len(parms[i]) > 0) :
                            try :
                                set_dc_dataframe(get_dc_dataframe().drop([parms[i]],axis=1))
                            except Exception as e:
                                opstat.store_exception("Drop Column(s) Error" + parms[i],e)
                                display_exception(opstat)
                        
        else :
            display_exception(opstat)
"""        


"""
#--------------------------------------------------------------------------
#   display bulk geocodinig forms
#--------------------------------------------------------------------------
"""
def display_bulk_geocoding(optionId) :
    
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        
        if(not (cfg.is_dc_dataframe_loaded())) :
            
            sugw.display_geocode_main_taskbar() 
            opstat = opStatus()
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
                    notes.append("You must enter a client_id and secret_key for the google bulk geocoder")
                    from dfcleanser.common.common_utils import display_msgs
                    display_msgs(notes,None)
                    
                else :
                    
                    if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :
                        
                        sugw.display_geocoders(geocid,False,False) 
                        notes.append("You must enter a client_id and secret_key for the google bulk geocoder")
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
                
                notes   =   []
                fparms  =   cfg.get_config_value("arcgisbatchgeocoderParms")
                if(fparms == None) :
                
                    sugw.display_geocoders(geocid,False,False) 
                    notes.append("You must enter a username and password for the arcGIS bulk geocoder")
                    from dfcleanser.common.common_utils import display_msgs
                    display_msgs(notes,None)
                    
                else :
                    
                    if( (len(fparms[0]) == 0) or (len(fparms[1]) == 0) ) :
                    
                        sugw.display_geocoders(geocid,False,False) 
                        notes.append("You must enter a username and password for the arcGIS geocoder")
                        from dfcleanser.common.common_utils import display_msgs
                        display_msgs(notes,None)
                        
                    else :
                        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
                        if(optionId == sugm.DISPLAY_BULK_GET_COORDS) :
                            display_bulk_geocode_inputs(geocid,sugm.ADDRESS_CONVERSION) 
                        else :
                            display_bulk_geocode_inputs(geocid,sugm.COORDS_CONVERSION)                
                     
            else :
                sugw.display_geocode_main_taskbar() 
                display_status("Bulk Geocoding not supported for Current Geocoder : "+ sugm.get_geocoder_title(geocid))


"""
#--------------------------------------------------------------------------
#   run google bulk geocoding
#--------------------------------------------------------------------------
"""
def run_google_bulk_geocode(runParms,opstat) :
    
    print("run_google_bulk_geocode",runParms) 
    
"""
#--------------------------------------------------------------------------
#   run google bulk geocoding
#--------------------------------------------------------------------------
"""
def run_arcgis_bulk_geocode(runParms,opstat) :

    print("run_arcgis_bulk_geocode",runParms) 

"""
#--------------------------------------------------------------------------
#   validate bulk geocodinig parms
#--------------------------------------------------------------------------
"""
def validate_bulk_parms(geocid,inputs,opstat) :

    bulk_geocode_kwargs     =   {}
    
    if(geocid == sugm.GoogleId) :
        from dfcleanser.common.common_utils import get_parms_for_input
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
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No address columns defined")
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[2] : fparms[2]})     



        
        
        
        
        
        
    else :
        from dfcleanser.common.common_utils import get_parms_for_input,get_dc_dataframe
        fparms = get_parms_for_input(inputs,batch_arcgis_query_idList)

        # check the required parms 
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No arcGIS username defined")
        else :
            bulk_geocode_kwargs.update({batch_arcgis_query_labelList[0] : fparms[0]})    
            if(len(fparms[1]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No arcGIS password defined")
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[1] : fparms[1]})     
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No address columns defined")
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[2] : fparms[2]})     
                    if(len(fparms[3]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No lat long columns defined")
                    else :
                        bulk_geocode_kwargs.update({batch_arcgis_query_labelList[3] : fparms[3]})    

        if(opstat.get_status()) :
            
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})
                
            if(len(fparms[5]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[5] : fparms[5]})  
                
            if(len(fparms[6]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)})
            else :
                batch_size  =   int(fparms[6])
                if(batch_size > cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("batch size exceeds arcGIS suggested max batch size of "+ str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)))
                    
            if(len(fparms[7]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : len(get_dc_dataframe())})
            else :
                if(int(fparms[7]) > len(get_dc_dataframe())) :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : len(get_dc_dataframe())})
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : int(fparms[7])})
            
            if(len(fparms[8]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : int(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : int(fparms[8])})

            if(len(fparms[9]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : 5})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : int(fparms[9])}) 

            if(len(fparms[10]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : False})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : True}) 

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
#   process bulk geocodinig 
#--------------------------------------------------------------------------
"""
def get_bulk_coords(geocid,inputs) :
    
    opstat      =   opStatus()
    runParms    =   validate_bulk_parms(geocid,inputs,opstat) 
    
    if(opstat.get_status()) :
        
        if(geocid == sugm.GoogleId) :
            run_google_bulk_geocode(runParms,opstat)
        else :
            run_arcgis_bulk_geocode(runParms,opstat)
        
        
    
    

"""
#--------------------------------------------------------------------------
#   process bulk geocodinig 
#--------------------------------------------------------------------------
"""
def process_bulk_geocoding(optionId,parms) :
    
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
        sugw.display_geocode_main_taskbar() 
        
        fid     =   int(parms[0])
        geocid  =   int(parms[1])
        geotype =   int(parms[2])
        inputs  =   parms[3]
        inputs  =   json.loads(inputs)
        
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import get_bulk_input_parms
        inputs = get_bulk_input_parms(geocid,inputs) 
            
        if(geocid == sugm.GoogleId) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import bulk_google_query_input_id
            cfg.set_config_value(bulk_google_query_input_id+"Parms",inputs)
        else :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import batch_arcgis_query_id
            cfg.set_config_value(batch_arcgis_query_id+"Parms",inputs)
           
        print("PROCESS_BULK_GET_COORDS",fid,geocid,inputs) 
        
        if(fid == sugm.BULK_GET_COORDS) :
            print("BULK_GET_COORDS")           
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




"""
#--------------------------------------------------------------------------
#   process batch geocoder test
#--------------------------------------------------------------------------
"""
def process_test_bulk_connector(optionId,parms) :

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
#   bulk geocoding components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

bulk_console_title = """<div class="dfc-console-title">
    <p>Bulk Geocoding Run Console</p>
</div>"""
    
bulk_console_container = """<div class="dfc-console-container">
    <div style="text-align: center; margin:auto; margin-top:20px;">
        <table class="dcprogresstable" id="geocodeStatusBars" style="margin:auto;">
            <tbody>
"""
                
bulk_console_progress_row = """                    <tr class='dfc-progress-row'>
                        <td class='dfc-progress-title'>"""

bulk_console_progress_col = """                        <td class='dfc-progress-col'>
                            <div class='progress md-progress dfc-progress-div'>
                                <div """

bulk_console_progress_col1 = """ class='progress-bar dfc-progress-bar' role='progressbar' """

bulk_console_progress_row_end = """                            </div>
                        </td>
                    </tr>
"""
                    
bulk_console_container_end = """            </tbody>
        </table>
    </div>
"""

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:95%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(0)">Run</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(1)">Pause</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(2)">Stop</button>
            </div>
        </div>
"""

bulk_console_end = """</div>
"""


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

def get_bulk_geocode_console_html(progressbarList) :
    
    console_html = ""
    console_html = (console_html + bulk_console_title)
    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))    
    
    console_html = (console_html + bulk_console_container_end)  
    console_html = (console_html + bulk_console_commands)  
    console_html = (console_html + bulk_console_end)  
        
    return(console_html)     
        
        
        
        
        
        
        
