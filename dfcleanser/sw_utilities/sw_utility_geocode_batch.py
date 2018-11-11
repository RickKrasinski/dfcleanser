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
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqapikey",
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
                                               None,None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["google_api_key",
                                               "dataframe_composite_address",
                                               "new_lat_long_column_name(s)",
                                               "language",
                                               "region",
                                               "drop_address_column(s)_flag",
                                               "returned_single_address_column_name",
                                               "max_geocode_runs",
                                               "max_geocode_rate",
                                               "checkpoint_size",
                                               "failure_limit",
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
                                              "language (default - english)",
                                              "region (default - None)",
                                              "drop address fields used in composite address (default = False)",
                                              "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "max geocode get rate in geoocodes per second (default - 1/second)",
                                              "number of geocode results before checkpoint taken (default - 500) ",
                                              "failure rate in percent (default - 5%)",
                                              
                                               None,None,None,None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_LANGUAGES)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_GET_REGIONS)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.GoogleId)+")",
                                               "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.GoogleId)+")"]

bulk_google_query_input_reqList           =   [0,1,2,3,4]

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
"""
#--------------------------------------------------------------------------
#   arcGIS batch geocoder form
#--------------------------------------------------------------------------
"""
batch_arcgis_geocoder_title            =   "arcGIS Batch Geocoder Parms"
batch_arcgis_geocoder_id               =   "arcgisbatchgeocoder"

batch_arcgis_geocoder_idList           =    ["bagusername",
                                             "bagpw",
                                             None,None,None,None,None]

batch_arcgis_geocoder_labelList        =   ["arcgis_username",
                                            "arcgis_pw",
                                            "Test</br>Geocoder",
                                            "Get</br> Bulk </br>Coords",
                                            "Clear","Return","Help"]


batch_arcgis_geocoder_typeList         =   ["text","text",
                                            "button","button","button","button","button"]

batch_arcgis_geocoder_placeholderList  =   ["arcgis username",
                                            "arcgis password",
                                            None,None,None,None,None]

batch_arcgis_geocoder_jsList           =   [None,None,
                                            "process_batch_geocoder(" + str(sugm.BATCH_TEST_CONNECTOR) + ")",
                                            "process_batch_geocoder(" + str(sugm.BULK_GET_COORDS) + ")",
                                            "process_batch_geocoder(" + str(sugm.BATCH_CLEAR) + ")",
                                            "process_batch_geocoder(" + str(sugm.BATCH_RETURN) + ")",
                                            "process_batch_geocoder(" + str(sugm.BATCH_HELP) + ")"]


batch_arcgis_geocoder_reqList          =   [0,1]

batch_arcgis_geocoder_form             =   [batch_arcgis_geocoder_id,
                                            batch_arcgis_geocoder_idList,
                                            batch_arcgis_geocoder_labelList,
                                            batch_arcgis_geocoder_typeList,
                                            batch_arcgis_geocoder_placeholderList,
                                            batch_arcgis_geocoder_jsList,
                                            batch_arcgis_geocoder_reqList]



batch_arcgis_address_geocoder_labelList        =   ["arcgis_username",
                                                    "arcgis_pw",
                                                    "Test</br>Geocoder",
                                                    "Get</br> Bulk </br>Addresses",
                                                    "Clear","Return","Help"]

batch_arcgis_address_geocoder_jsList           =   [None,None,
                                                    "process_batch_geocoder(" + str(sugm.BATCH_TEST_CONNECTOR) + ")",
                                                    "process_batch_geocoder(" + str(sugm.BULK_GET_ADDRESS) + ")",
                                                    "process_batch_geocoder(" + str(sugm.BATCH_CLEAR) + ")",
                                                    "process_batch_geocoder(" + str(sugm.BATCH_RETURN) + ")",
                                                    "process_batch_geocoder(" + str(sugm.BATCH_HELP) + ")"]





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

batch_arcgis_query_idList           =    ["baqaddress",
                                          "baqcolumnname",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqoutsr",
                                          "baqdropaddress",
                                          "baqsaveaddress",
                                          "baqbatchsize",
                                          "baqbulknumberlimit",
                                          "baqbulkcheclpointsize",
                                          "baqbulkfailurelimit",
                                          None,None,None,None,None,None,None]

batch_arcgis_query_labelList        =   ["dataframe_composite_address",
                                         "new_lat_long_column_name(s)",
                                         "source_country",
                                         "category",
                                         "out_sr",
                                         "drop_Address_column_flag",
                                         "save_Address_column_name",
                                         "batch_size",
                                         "max_geocode_runs",
                                         "checkpoint_size",
                                         "failure_limit",
                                         "Get</br> Bulk </br>Coords",
                                         "Get</br> Column </br>Names",
                                         "Get</br> Countries",
                                         "Get</br> Categories",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   [maketextarea(4),"text","text","text","text",
                                         "text","text","text","text","text","text",
                                         "button","button","button","button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["select from 'Column Names' for constant value use 'val' ie.. 'Buffalo'",
                                         "single name : [lat,long] - two cols enter list [latname,longname]",
                                         "source country (defailt - US)",
                                         "category (defailt - None)",
                                         "out_sr (defailt - None)",
                                         "drop address fields used in composite address (default = False)",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "batch size (default - geocoder recommended value",
                                         "max number of dataframe rows (default - len(datframe) )",
                                         "checkpoint size (default - batch size)",
                                         "failure limit (default - 5%)",
                                         None,None,None,None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,None,None,None,None,
                                         "process_bulk_query("+str(sugm.BULK_GET_COORDS)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_ADDRESS_COLS)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_COUNTRIES)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_GET_CATEGORIES)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_CLEAR)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_RETURN)+","+str(sugm.ArcGISId)+")",
                                         "process_bulk_query("+str(sugm.BULK_HELP)+","+str(sugm.ArcGISId)+")"]


batch_arcgis_query_reqList          =   [0,1,2,3]

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
    
    from dfcleanser.common.common_utils import opStatus, display_exception

    opstat  =   opStatus()

    gis = GIS("http://www.arcgis.com", user, pw)

    try :
        # use the first of GIS's configured geocoders
        geocoder = get_geocoders(gis)[0]

        arcgis_MaxBatchSize         =   geocoder.properties.locatorProperties.MaxBatchSize
        arcgis_SuggestedBatchSize   =   geocoder.properties.locatorProperties.SuggestedBatchSize
    
        cfg.set_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,arcgis_MaxBatchSize)
        cfg.set_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY,arcgis_SuggestedBatchSize)
        
    except Exception as e:
        opstat.store_exception("Unable to connect to arcgis ",e)

    if(opstat.get_status() ) :
        return(True) 
    else :
        display_exception(opstat)
    


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
def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.COLNAMES_TABLE,showfull=False) :

    print("display_bulk_geocode_inputs",geocid,geotype,tabletype,showfull)
    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
    
    if (geotype == sugm.ADDRESS_CONVERSION) :
        from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
        if(tabletype==sugm.COLNAMES_TABLE) :
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
#   display arcgis batch connector
#------------------------------------------------------------------
"""
def display_arcgis_connector_inputs(geotype) :

    print("display_arcgis_connector_inputs",geotype)
    
    from dfcleanser.common.html_widgets import display_composite_form,get_input_form,InputForm
    if (geotype == sugm.ADDRESS_CONVERSION) :
        display_composite_form([get_input_form(InputForm(batch_arcgis_geocoder_id,
                                                         batch_arcgis_geocoder_idList,
                                                         batch_arcgis_geocoder_labelList,
                                                         batch_arcgis_geocoder_typeList,
                                                         batch_arcgis_geocoder_placeholderList,
                                                         batch_arcgis_geocoder_jsList,
                                                         batch_arcgis_geocoder_reqList))])

    else :
        display_composite_form([get_input_form(InputForm(batch_arcgis_geocoder_id,
                                                         batch_arcgis_geocoder_idList,
                                                         batch_arcgis_address_geocoder_labelList,
                                                         batch_arcgis_geocoder_typeList,
                                                         batch_arcgis_geocoder_placeholderList,
                                                         batch_arcgis_address_geocoder_jsList,
                                                         batch_arcgis_geocoder_reqList))])
    

"""
#------------------------------------------------------------------
#   test arcgis batch connector
#------------------------------------------------------------------
"""
def test_arcgis_connector(parms) :

    print("test_arcgis_connector",parms)
    
    from dfcleanser.common.common_utils import get_parms_for_input
    geotype     =   parms[1]
    fparms      =   get_parms_for_input(parms,batch_arcgis_geocoder_idList)   
    
    from dfcleanser.common.html_widgets import display_composite_form,get_input_form,InputForm
    if (geotype == sugm.ADDRESS_CONVERSION) :
        display_composite_form([get_input_form(InputForm(batch_arcgis_geocoder_id,
                                                         batch_arcgis_geocoder_idList,
                                                         batch_arcgis_geocoder_labelList,
                                                         batch_arcgis_geocoder_typeList,
                                                         batch_arcgis_geocoder_placeholderList,
                                                         batch_arcgis_geocoder_jsList,
                                                         batch_arcgis_geocoder_reqList))])

    else :
        display_composite_form([get_input_form(InputForm(batch_arcgis_geocoder_id,
                                                         batch_arcgis_geocoder_idList,
                                                         batch_arcgis_address_geocoder_labelList,
                                                         batch_arcgis_geocoder_typeList,
                                                         batch_arcgis_geocoder_placeholderList,
                                                         batch_arcgis_address_geocoder_jsList,
                                                         batch_arcgis_geocoder_reqList))])
    

    test_arcgis_connection(fparms[0],fparms[1])



















   
        
        
        
        
        
        
        
        
        