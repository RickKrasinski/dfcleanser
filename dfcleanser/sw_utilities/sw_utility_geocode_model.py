"""
# sw_utility_geocode_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

from dfcleanser.common.common_utils import (opStatus, get_dfc_dataframe)
import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_bulk_geocode_control as subgc
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw
import dfcleanser.sw_utilities.sw_utility_geocode_control as sugc

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
ArcGISId                    =   0
BaiduId                     =   1
BingId                      =   2
DataBCId                    =   3
GeocoderDotUSId             =   4
GeocodeFarmId               =   5
GeoNamesId                  =   6
GoogleId                    =   7
OpenCageId                  =   8
OpenMapQuestId              =   9
PickPointId                 =   10
NominatimId                 =   11
YahooPlaceFinderId          =   12

supported_Geocoders         =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BingId,GoogleId,NominatimId]

supported_Bulk_Geocoders    =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Bulk_Reverses     =   [GoogleId]

MAX_GOOGLE_TASKS            =   10

GOOGLE_DELAY                =   0.05
BING_DELAY                  =   0.5
OPENMAPQUEST_DELAY          =   1
NOMINATIM_DELAY             =   1


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Function Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_MAIN_GEOCODING          =   0

PROCESS_GEOCODER                =   1

CLEAR_GEOCODE_FORM              =   2
DISPLAY_GEOCODER                =   3
TEST_GEOCODER                   =   4
DISPLAY_GEOCODING               =   5
GET_TABLE                       =   6
PROCESS_GEOCODING               =   7



DISPLAY_DISTANCE                =   8
PROCESS_DISTANCE                =   9
DISPLAY_DF_DISTANCE             =   10
PROCESS_DF_DISTANCE             =   11

DISPLAY_FULL_GEOCODING          =   12

CHANGE_BULK_GEOCODER            =   13

DISPLAY_BULK_GEOCODER           =   14
PROCESS_BULK_GEOCODER           =   15

BULK_LOAD_GEOCODER              =   19
BULK_START_GEOCODER             =   20
BULK_STOP_GEOCODER              =   21
BULK_PAUSE_GEOCODER             =   22
BULK_RESUME_GEOCODER            =   23
BULK_VIEW_ERRORS                =   24
BULK_CHECKPT_GEOCODER           =   25





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding constants
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

GEOCODER                    =    0
QUERY                       =    1
REVERSE                     =    2

DISTANCE_HELP               =   8
DISTANCE_DF_HELP            =   8

INTERACTIVE                 =   0
BULK                        =   1



"""
#--------------------------------------------------------------------------
#   bulk geocoding input form table ids - tables loaded in grid
#--------------------------------------------------------------------------
"""
GEOCODERS_TABLE             =   -1
COLNAMES_TABLE              =   0
LANGUAGE_TABLE              =   1
REGION_TABLE                =   2
CATEGORIES_TABLE            =   3
ADDRESS_COMPONENTS_TABLE    =   4
RESULT_TYPES_TABLE          =   5
LOCATION_TYPES_TABLE        =   6


"""
#--------------------------------------------------------------------------
#   bulk geocoder running commands 
#--------------------------------------------------------------------------
"""

BATCH_TEST_CONNECTOR        =   14
BATCH_CLEAR                 =   15
BATCH_RETURN                =   16
BATCH_HELP                  =   17

BULK_GET_ADDRESS_COMPONENTS =   18
BULK_GET_RESULT_TYPES       =   19
BULK_GET_LOCATION_TYPES     =   20


"""
#--------------------------------------------------------------------------
#   bulk geocoder currebt state
#--------------------------------------------------------------------------
"""
RUNNING                     =   0
STOPPED                     =   1
PAUSED                      =   2
STARTING                    =   3
STOPPING                    =   4
PAUSING                     =   5
FINISHED                    =   6

LOAD                        =   10
START                       =   11
STOP                        =   12
PAUSE                       =   13
RESUME                      =   14


def get_geocoder_title(geoid) :
    
    if(geoid == ArcGISId) :
        return("ArcGIS")
    elif(geoid == BingId) :
        return("Bing")
    elif(geoid == DataBCId) :
        return("DataBC")
    elif(geoid == GoogleId) :
        return("GoogleV3")
    elif(geoid == OpenMapQuestId) :
        return("OpenMapQuest")
    elif(geoid == NominatimId) :
        return("Nominatim")




"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  BULK GEOCODING
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""




"""
#----------------------------------------------------------------------------
#-  Google maps geocode exceptions
#----------------------------------------------------------------------------
"""
ApiErrorMessage                         =   "API ERROR"
HTTPErrorMessage                        =   "HTTP ERROR"
TimeoutErrorMessage                     =   "TIMEOUT ERROR"
TransportErrorMessage                   =   "TRANSPORT ERROR"
RetriableRequestErrorMessage            =   "RETRIABLE REQUEST ERROR"
OverQueryLimitErrorMessage              =   "OVER QUERY LIMIT"


"""
#----------------------------------------------------------------------------
#-  Google geocode status codes
#----------------------------------------------------------------------------
"""
OK_STATUS                               =   "OK"
ZERO_RESULTS_STATUS                     =   "ZERO_RESULTS"
OVER_DAILY_LIMIT_STATUS                 =   "OVER_DAILY_LIMIT"
OVER_QUERY_LIMIT_STATUS                 =   "OVER_QUERY_LIMIT"
REQUEST_DENIED_STATUS                   =   "REQUEST_DENIED"
INVALID_REQUEST_STATUS                  =   "INVALID_REQUEST"
UNKNOWN_ERROR_STATUS                    =   "UNKNOWN_ERROR"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding classes and helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google geocode results class
#----------------------------------------------------------------------------
#   google geocode results received from google geocode call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class google_geocode_results:
    
    rowId           =   -1
    status          =   None
    results         =   None
    opstat          =   None
    
    def __init__(self,rowid,status,geocode_results,opstat) :
        self.rowId      =   rowid
        self.status     =   status
        self.results    =   geocode_results
        self.opstat     =   opstat

    def get_lat(self) :
        return(self.results.get("geometry").get("location").get("lat"))
    def get_lng(self) :
        return(self.results.get("geometry").get("location").get("lng"))
    def get_formatted_address(self) :
        return(self.results.get("formatted_address"))
    def get_location_type(self) :
        return(self.results.get("geometry").get("location_type"))
    def get_place_id(self) :
        return(self.results.get("place_id"))
    def get_types(self) :
        return(self.results.get("types"))

    def get_results(self) :
        return(self.results)
    
    def get_address_components(self) :
        return(self.results.get("address_components"))
    
    def get_row_Id(self) :
        return(self.rowId)
    def get_status(self) :
        return(self.opstat.get_status())
    def get_error_message(self) :
        return(self.opstat.get_errorMsg())


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google reverse results class
#----------------------------------------------------------------------------
#   google reverse results received from google reverse call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
class google_reverse_results:
    
    rowId           =   -1
    status          =   None
    results         =   None
    opstat          =   None
    
    def __init__(self,rowid,status,reverse_results,opstat) :
        self.rowId      =   rowid
        self.status     =   status
        self.results = reverse_results[0]
        self.opstat  = opstat

    def get_lat(self) :
        return(self.results.get("geometry").get("location").get("lat"))
    def get_lng(self) :
        return(self.results.get("geometry").get("location").get("lng"))
    def get_formatted_address(self) :
        return(self.results.get("formatted_address"))
    def get_location_type(self) :
        return(self.results.get("geometry").get("location_type"))
    def get_place_id(self) :
        return(self.results.get("place_id"))
    def get_types(self) :
        return(self.results.get("types"))

    def get_results(self) :
        return(self.results)
    
    def get_row_Id(self) :
        return(self.rowId)
    def get_status(self) :
        return(self.opstat.get_status())
    def get_error_message(self) :
        return(self.opstat.get_errorMsg())


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Google address components class
#----------------------------------------------------------------------------
#   google geocode results address received from google geocode/reverse call
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------
#-  Google geocode address component types
#----------------------------------------------------------------------------
"""
GOOGLE_GEOCODER_STREET_NUMBER_ID        =   'street_number'
GOOGLE_GEOCODER_ROUTE_ID                =   'route'
GOOGLE_GEOCODER_NEIGHBORHOOD_ID         =   'neighborhood'
GOOGLE_GEOCODER_LOCALITY_ID             =   'locality'
GOOGLE_GEOCODER_SUBLOCALITY_ID          =   'sublocality'
GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID        =   'administrative_area_level_1'
GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID        =   'administrative_area_level_2'
GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID        =   'administrative_area_level_3'
GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID        =   'administrative_area_level_4'
GOOGLE_GEOCODER_COUNTRY_ID              =   'country'
GOOGLE_GEOCODER_POSTAL_CODE_ID          =   'postal_code'

"""
#----------------------------------------------------------------------------
#   google address components common us field defs
#----------------------------------------------------------------------------
"""
google_address_components_comments  =   {GOOGLE_GEOCODER_STREET_NUMBER_ID: "STREET NUMBER",
                                         GOOGLE_GEOCODER_ROUTE_ID: "STREET",
                                         GOOGLE_GEOCODER_NEIGHBORHOOD_ID: "NEIGHBORHOOD",
                                         GOOGLE_GEOCODER_LOCALITY_ID: "LOCALITY",
                                         GOOGLE_GEOCODER_SUBLOCALITY_ID: "CITY",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID: "STATE",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID: "COUNTY",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID: "AREA 3",
                                         GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID: "AREA 4",
                                         GOOGLE_GEOCODER_COUNTRY_ID: "COUNTRY",
                                         GOOGLE_GEOCODER_POSTAL_CODE_ID: "ZIPCODE"}

"""
#----------------------------------------------------------------------------
#   default address for googl;e address components
#----------------------------------------------------------------------------
"""
default_address_format                  =  [GOOGLE_GEOCODER_STREET_NUMBER_ID,
                                            GOOGLE_GEOCODER_ROUTE_ID,
                                            GOOGLE_GEOCODER_NEIGHBORHOOD_ID,
                                            GOOGLE_GEOCODER_LOCALITY_ID,
                                            GOOGLE_GEOCODER_SUBLOCALITY_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_1_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_2_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_3_ID,
                                            GOOGLE_GEOCODER_ADMIN_LEVEL_4_ID,
                                            GOOGLE_GEOCODER_COUNTRY_ID,
                                            GOOGLE_GEOCODER_POSTAL_CODE_ID]


def get_address_from_components(addr_comps,addr_map,short=True) :
    """
    * --------------------------------------------------------------------
    * function : get a complete address from google address components 
    * 
    * parms :
    *  addr_comps  - address components
    *  addr_map    - address parms map
    *  short       - get short values boolean
    *
    * returns : 
    *  full adddress defined by map from address components
    * -------------------------------------------------------------------
    """
    
    out_address     =   ""
    
    if(addr_comps != None) :
        if(len(addr_comps) > 0) :
            for i in range(len(addr_map)) :
                for j in range(len(addr_comps)) :
                    ctypes  =   addr_comps[j].get("types",None)
                    if(ctypes != None) :
                        if(addr_map[i] in ctypes) :
                            if(short) :
                                out_address     =   out_address + addr_comps[j].get("short_name"," ") + " "
                            else :
                                out_address     =   out_address + addr_comps[j].get("long_name"," ") + " "    
                            break
    
    return(out_address)                    
                        

"""
#--------------------------------------------------------------------------
#  google address components class for getting individual address fields
#--------------------------------------------------------------------------
"""
class google_address_components:
    
    address_components  =   None

    def __init__(self,addr_comps) :
        self.address_components = addr_comps
        

    def get_address_component(self,address_component_id,shortName=True) :
        
        if(self.address_components != None) :
            if(len(self.address_components) > 0) :
                for i in range(len(self.address_components)) :
                    ctypes  =   self.address_components[i].get("types",None)
                    if(ctypes != None) :
                        if(address_component_id in ctypes) :
                            if(shortName) :
                                return(self.address_components[i].get("short_name"," "))
                            else :
                                return(self.address_components[i].get("long_name"," "))
                                
                return("")
                
            else :
                return("") 
                
        else :
            return("")
        
    def get_full_address_from_components(self,addr_format,shortName=True) :
        
        out_address     =   ""
        
        if(addr_format != None) :
            if(len(addr_format) > 0) :
                for i in range(len(addr_format)) :
                    out_address     =   out_address + self.get_address_component(addr_format[i],shortName)
                    
        

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding results log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_RESULTS_DF_TITLE          =   "Current_Geocoding_Results_df"
GEOCODING_RESULTS_DF_NOTES          =   "Bulk Geocoding Results df"

MAX_RESULTS_DISPLAYED               =   200
DISPLAY_RESULTS_SIZE                =   20


class BulkGeocodeResults:
    
    geocode_results_df      =   None
    column_headers_list     =   []
    
    def __init__(self,column_headers,dftitle=None):
        self.column_headers = column_headers
        
        if(dftitle == None) :
            self.column_headers_list    =   column_headers
            import pandas as pd
            self.geocode_results_df = pd.DataFrame(columns=self.column_headers_list)
            dfc_geocode_results_df  = cfg.dfc_dataframe(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df,GEOCODING_RESULTS_DF_NOTES)
            cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)
            cfg.add_dfc_dataframe(dfc_geocode_results_df)
        
        else :
            self.geocode_results_df  = cfg.get_dfc_dataframe(dftitle)

    def add_result(self,rowResults) :
        
        print("    add_result",rowResults[0],len(self.geocode_results_df),"\n     ",rowResults,flush=True)
        
        #self.geocode_results_df     =   self.geocode_results_df.append([rowResults], ignore_index=True)
        import pandas as pd
        self.geocode_results_df     =   self.geocode_results_df.append(pd.Series(rowResults,index=self.column_headers_list),ignore_index=True)
        #rowid   =   int(rowResults[0])
        print("    add_result",rowResults[0],len(self.geocode_results_df),flush=True)
        
        #import pandas as pd
#        self.geocode_results_df.loc[rowid]   =   rowResults
        
        #import pandas as pd
        #new_results_df   =   pd.DataFrame([rowResults],columns=self.column_headers)
        cfg.get_dfc_df(GEOCODING_RESULTS_DF_TITLE).set_df(self.geocode_results_df)
        
    def show_results(self, startrowindex) :
        print("show_results",startrowindex)

        resultsHeader      =   self.column_headers_map[0]
        resultsRows        =   []
        resultsWidths      =   self.column_headers_map[1]
        resultsAligns      =   ["center"]
        for i in range((len(self.column_headers_map[0])-1)) :
            resultsAligns.append("left")    

        for i in range(MAX_RESULTS_DISPLAYED) :
            df      =   cfg.get_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
            result  =   df.loc[df[self.column_headers_map[0]] == startrowindex+i] 
            result  =   result.tolist()
        
            resultrow   =   []
            for i in range(len(self.column_headers_map[0])) :
                resultrow.append(result[i])
            resultsRows.append(resultrow)
        
        results_table = None
                
        results_table = dcTable("Geocode Results","geoocoderreslstable",
                                cfg.SWGeocodeUtility_ID,
                                resultsHeader,resultsRows,
                                resultsWidths,resultsAligns)
            
        results_table.set_tabletype(ROW_MAJOR)
        results_table.set_rowspertable(ERRORS_TABLE_SIZE)

        listHtml = get_row_major_table(results_table,SCROLL_NEXT,False)

        #print(listHtml)        
        return(listHtml)

    def get_results_count(self) :    
        return(len(self.geocode_results_df))

    def clear_results(self) :    
        self.geocode_results_df = None
        cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)

    def get_geocoding_df(self) :    
        return(self.geocode_results_df)


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding error log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_ERROR_LOG_DF_TITLE            =   "Current_Geocoding_Error_Log_df"
GEOCODING_ERROR_LOG_DF_NOTES            =   "Geocoding Error Logging Dataframe"

GEOCODING_ERROR_LOG_COULUMN_NAME_LIST   =   ['rowid','geocode_input_value','error_message']

MAX_ERRORS_DISPLAYED                    =   200
ERRORS_TABLE_SIZE                       =   20


class BulkGeocodeErrorLog:
    
    error_log_df    =   None
        
    def __init__(self):
        import pandas as pd
        self.error_log_df = pd.DataFrame(columns=GEOCODING_ERROR_LOG_COULUMN_NAME_LIST)
        dfc_geocode_error_log = cfg.dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df,GEOCODING_ERROR_LOG_DF_NOTES)
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
        cfg.add_dfc_dataframe(dfc_geocode_error_log)

    def log_error(self,rowindex,inputValue,errorMsg):
        import pandas as pd
        new_error_df   =   pd.Dataframe([rowindex,inputValue,errorMsg],columns=GEOCODING_ERROR_LOG_COULUMN_NAME_LIST)
        self.error_log_df.append(new_error_df)
        
    def show_errors(self, startrowindex) :
        
        print("get_geocode_error_log_table",startrowindex)

        errorsHeader      =   ["rowid","input value","error message"]
        errorsRows        =   []
        errorsWidths      =   [10,35,55]
        errorsAligns      =   ["center","left","left"]

        for i in range(MAX_ERRORS_DISPLAYED) :
            df      =   cfg.get_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
            cerror  =   df.loc[df[GEOCODING_ERROR_LOG_COULUMN_NAME_LIST[0]] == startrowindex+i] 
            cerror  =   cerror.tolist()
        
            cerrorrow = [cerror[0],cerror[1],cerror[2]]
            errorsRows.append(cerrorrow)
        
        errors_table = None
                
        errors_table = dcTable("Geocode Errors","geoocodererrortable",
                               cfg.SWGeocodeUtility_ID,
                               errorsHeader,errorsRows,
                               errorsWidths,errorsAligns)
            
        errors_table.set_tabletype(ROW_MAJOR)
        errors_table.set_rowspertable(ERRORS_TABLE_SIZE)

        listHtml = get_row_major_table(errors_table,SCROLL_NEXT,False)

        #print(listHtml)        
        return(listHtml)
 
    def get_error_count(self) :    
        return(len(self.error_log_df))

    def clear_error_log(self) :    
        self.error_log_df = None
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)





























"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Address Maps
#----------------------------------------------------------------------------
#   geocode address map for creating address string from dataframe columns
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

class AddressMap:
    
    def __init__(self, colindices,colvalues):
        self.colIndices     =   colindices
        self.colValues      =   colvalues
        
    def get_colindices(self): 
        return(self.colIndices)
    
    def get_colValues(self): 
        return(self.colValues)

def get_geocode_address_string(address_map,rowIndex) : 
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
    
    df  =   get_dfc_dataframe()
    
    for i in range(len(address_map.get_colindices())) :
        
        if(not (address_map.get_colindices()[i] == -1) ) :
            geocode_address     =   geocode_address + df.loc[rowIndex,address_map.get_colindices()[i]] + " "
        else :
            geocode_address     =   geocode_address + address_map.get_colValues()[i] + " "
        
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

    colIndices  =   []
    colValues   =   []
    
    address_cols        =   address_cols.replace(","," ")
    address_components  =   address_cols.split("+")
    
    for i in range(len(address_components)) :
        address_components[i]   =   address_components[i].lstrip(" ")
        address_components[i]   =   address_components[i].rstrip(" ")
        
    colnames            =   cfg.get_dfc_dataframe().columns.values.tolist() 
    
    for i in range(len(address_components)) :

        if(address_components[i] in colnames) :
            colIndices.append(address_components[i])
            colValues.append(None)
            
        else :
            colIndices.append(-1)
            colValues.append(address_components[i])
    
    addressMap  =    AddressMap(colIndices,colValues)       
    
    return(addressMap)



"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Task Class
#----------------------------------------------------------------------------
#   geocoding task class for retrieving gecoding results
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
import threading

class GeocodeTask:
    
    geocoderId          =   -1
    geocodeType         =   QUERY
    rowId               =   -1
    inputparms          =   None
    runParms            =   None
    
    geocode_results     =   None
    task_running        =   False
        
    def __init__(self, geocoderId,geocodeType,rowid,inputparms,runparms):
        self.geocoderId         =   geocoderId
        self.geocoder_type      =   geocodeType
        self.rowId              =   rowid
        self.inputParms         =   inputparms
        self.runParms           =   runparms
        self.geocode_results    =   None
        
    def run_geocoder_task(self):
        print("run_geocoder_task",self.rowId,flush=True)
        self.task_running       =   True
        self.run_geocode_method()            
        self.task_running       =   False

    def run_geocode_method(self) :
        
        if(self.geocoderId == GoogleId) :
            if(self.geocoder_type == QUERY) :
                self.geocode_results    =   subgc.get_google_geocode_results(self.rowId,self.inputParms,self.runParms)
            elif(self.geocoder_type == REVERSE) :
                self.geocode_results    =   subgc.get_google_reverse_results(self.rowId,self.inputParms,self.runParms) 

            if(not (self.geocode_results == None) ) :
                # no error occurred
                if(self.geocode_results.get_status()) :
                    if(self.geocoder_type == QUERY) :
                        subgc.process_google_geocode_results(self.inputParms,self.runParms,self.geocode_results)
                    else :
                        subgc.process_google_reverse_results(self.inputParms,self.runParms,self.geocode_results)
            
                # error occurred        
                else :
                    if(self.geocode_results.get_error_message() == OverQueryLimitErrorMessage) : 
                        stop_geocode_runner()
                
                    subgc.process_google_geocoding_errors(self.geocoder_type,self.inputParms,self.runParms,self.geocode_results)
                    
            else :
                subgc.process_google_geocoding_errors(self.geocoder_type,self.inputParms,self.runParms,self.geocode_results)    
                
        else :
            self.geocode_results    =   None            

    def get_task_run_state(self) :
        return(self.task_running)    
    
    def get_task_row_id(self) :
        return(self.rowId)    
        
        
class GeocodeTaskListMonitor:
    
    taskdict        =   {}
    maxtasks        =   0
        
    def __init__(self, maxtasksparm):
        self.taskdict        =   {}
        self.maxtasks        =   maxtasksparm
    
    def addtask(self, geocodetask, rowindex):
        print("    addtask : ",rowindex,flush=True)
        self.taskdict.update({rowindex:geocodetask})
        threading.Thread(target=geocodetask.run_geocoder_task).start()

        
    def droptask(self, rowindex):
        

        if(not(self.taskdict.get(rowindex,None) is None)) :
            self.taskdict.pop(rowindex,None)
            print("    droptask : ",rowindex,"task popped",flush=True)
        else :
            print("    droptask : ",rowindex,"task not found",flush=True)

    def more_tasks_available(self):
        if(len(self.taskdict) < self.maxtasks) :
            return(True)
        else :
            return(False)

    def clear_completed_tasks(self) :
        task_keys   =   list(self.taskdict.keys())
        
        for i in range(len(task_keys)) :
            ctask   =   self.taskdict.get(task_keys[i])
            if( not(ctask.get_task_run_state()) ) :
                self.droptask(ctask.get_task_row_id())

    def all_tasks_completed(self) :
        if(len(self.taskdict) == 0) :
            return(True)
        else :
            return(False)
        

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Runner Class
#----------------------------------------------------------------------------
#   class for running the current geocoding instance from dfcleanser.
#   controls tasks and updates display
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#   common helper methopds
#--------------------------------------------------------------------------
"""
def load_geocode_runner(geocoderId,geotype,runParms,address_map) :
    dfc_Geocode_Runner.load_run(geocoderId,geotype,runParms,address_map)    

def start_geocode_runner() :
    return(dfc_Geocode_Runner.start_run()) 
    
def stop_geocode_runner() :
    dfc_Geocode_Runner.stop_run() 
    
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
    
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 

def get_geocode_runner_results_log() :
    return(dfc_Geocode_Runner.get_results_log())
def get_geocode_runner_error_log() :
    return(dfc_Geocode_Runner.get_error_log())

def get_geocode_runner_state() :
    return(dfc_Geocode_Runner.get_run_state())
def get_geocode_runner_halt_flag() :
    return(dfc_Geocode_Runner.get_halt_flag())
def set_geocode_runner_halt_flag(state) :
    dfc_Geocode_Runner.set_halt_flag(state)

def get_geocode_runner_id() :
    return(dfc_Geocode_Runner.get_geocode_id())
def get_geocode_runner_type() :
    return(dfc_Geocode_Runner.get_geocode_type())
def get_geocode_connector() :
    return(dfc_Geocode_Runner.get_geocode_connector())
def set_geocode_connector(connector) :
    return(dfc_Geocode_Runner.set_geocode_connector(connector))

def drop_geocode_task(rowindex) :
    return(dfc_Geocode_Runner.drop_geocoder_task(rowindex))

def add_row_nan_error(rowid,ltype) :
    print("add_row_nan_error",rowid.ltype)
    
    
"""
#----------------------------------------------------------------------------
#-  Bulk Geocoding Runner Class
#----------------------------------------------------------------------------
"""
       
class BulkGeocodeRunner:
    
    geocid              =   None
    geotype             =   None
    runParms            =   None
    addressParms        =   None
    
    rowindex            =   0
    maxrows             =   0

    state               =   STOPPED
    halt_all_geocoding  =   True
    
    geocoder            =   None
    
    geocodeTaskListMonitor  =   None
    geocodingResults        =   None
    geocodingErrorLog       =   None
       
    def __init__(self):
        self.geocid             =   None
        self.geotype            =   None
        self.runParms           =   None
        self.addressParms       =   None

        self.rowindex           =   0
        self.maxrows            =   0

        self.state              =   STOPPED
        self.halt_all_geocoding =   True
        
        self.geocoder           =   None
        
        self.geocodeTaskMonitor =   None
        self.geocodingResults   =   None
        self.geocodingErrorLog  =   None
        
    def load_run(self,geocoderId,geoType,runParms,addressParms):
        self.geocid             =   geocoderId
        self.geotype            =   geoType
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        if(self.geocid == GoogleId) :
            if(self.geotype == QUERY) :
                self.maxrows            =   int(runParms.get("max_addresses_to_geocode"))
        
        if(self.geocid == GoogleId) :
            self.geocodeTaskListMonitor  =   GeocodeTaskListMonitor(MAX_GOOGLE_TASKS)
        
        from dfcleanser.sw_utilities.sw_utility_bulk_geocode_control import init_geocoding_data_structures
        bulkstructures          =   init_geocoding_data_structures(self.geocid,self.geotype,self.runParms)
        self.geocodingResults   =   bulkstructures[0]
        self.geocodingErrorLog  =   bulkstructures[1]
        
    def start_run(self):
        self.state              =   RUNNING
        
        from dfcleanser.sw_utilities.sw_utility_bulk_geocode_console import set_status_bar
        set_status_bar(STARTING)

        BulkGeocodeRunner.halt_all_geocoding = False
        self.rowindex           =   0
        return(self.start_bulk_geocode_runner(0))
        
    def stop_run(self):
        self.state              =   STOPPING
        BulkGeocodeRunner.halt_all_geocoding = True
            
    def pause_run(self):
        self.state              =   PAUSING
        BulkGeocodeRunner.halt_all_geocoding = True
    
    def resume_run(self):
        self.state              =   RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.start_bulk_geocode_runner(self.rowindex)        
        
    def get_run_state(self):
        return(self.state)
    
    def start_bulk_geocode_runner(self,rowIndex) :
        
        print("start_bulk_geocode_runner",rowIndex)
        self.rowindex   =   rowIndex
        opstat          =   opStatus()
        
        try :
            if(self.geocid == ArcGISId) :
                geocoderparms   =   cfg.get_config_value(subgw.batch_arcgis_geocoder_id+"Parms")
                self.geocoder   =   subgc.get_arcgis_batch_geocode_connection(geocoderparms[1],geocoderparms[2],opstat)
            
            elif(self.geocid == GoogleId) :   
                geocoderparms   =   cfg.get_config_value(subgw.google_bulk_geocoder_id+"Parms")
                self.geocoder   =   subgc.get_bulk_google_geocoder_connection(geocoderparms[0],geocoderparms[1],
                                                                              geocoderparms[2],opstat)
            else :   
                self.geocoder   =   sugc.get_geocoder_engine(self.geocid,opstat)
                
        except Exception as e:
            opstat.store_exception("Unable to establish " + get_geocoder_title(self.geocid) + " geocoder connection ",e)
        
        if(opstat.get_status()) :
            self.halt_all_geocoding     =   False
            threading.Thread(target=self.bulk_geocode_runner_task).start()
            
            from dfcleanser.sw_utilities.sw_utility_bulk_geocode_console import set_status_bar
            set_status_bar(RUNNING)
            return(opstat)
        else :
            return(opstat)
        
    def bulk_geocode_runner_task(self):
        while ( not (get_geocode_runner_halt_flag()) ) :
            
            if(self.geocid == ArcGISId) :
                
                opstat              =   opStatus()
                next_batch_addrs    =   subgc.get_arcgis_batch_addresses(self.rowindex,self.runParms,self.addressParms)
                geocoder = None
                geocode_results     =   subgc.get_arcgis_geocode_batch(geocoder,next_batch_addrs,opstat)
                
                if(opstat.get_status()) :
                    
                    # batch retrieved ok
                    self.rowindex   =   subgc.process_arcgis_geocode_batch_results(geocode_results,self.runParms,opstat)
                    
                    if(self.rowindex >= self.maxrows) :
                        BulkGeocodeRunner.halt_all_geocoding    =   True    
                
                else :
                    
                    BulkGeocodeRunner.halt_all_geocoding    =   True    
                    subgc.process_arcgis_geocode_batch_error(geocode_results,self.runParms,opstat) 

                
            elif(self.geocid == GoogleId) :
                
                opstat      =   opStatus()
                if(self.geocodeTaskListMonitor.more_tasks_available()) :
                    
                    if(not (self.rowindex > self.maxrows) ) :
                        
                        next_addr       =   get_geocode_address_string(self.addressParms,self.rowindex)
                        geocodetask     =   GeocodeTask(self.geocid,self.geotype,self.rowindex,next_addr,self.runParms)  
                        self.geocodeTaskListMonitor.addtask(geocodetask,self.rowindex)

                        self.rowindex   =   self.rowindex + 1
                    
                        if(self.geocid == GoogleId) :
                            delay   =   GOOGLE_DELAY
                        elif(self.geocid == GoogleId) :
                            delay   =   BING_DELAY
                        elif(self.geocid == OpenMapQuestId) :
                            delay   =   OPENMAPQUEST_DELAY
                        else :
                            delay   =   NOMINATIM_DELAY
                            
                    else :
                        
                        self.geocodeTaskListMonitor.clear_completed_tasks()
                        
                        if(self.geocodeTaskListMonitor.all_tasks_completed()) :
                            from dfcleanser.sw_utilities.sw_utility_bulk_geocode_console import set_status_bar
                            set_status_bar(FINISHED)
                            set_geocode_runner_halt_flag(True)
                        
                    
                else :
                    
                    if(self.geocid == GoogleId) :
                        delay   =   GOOGLE_DELAY
                    elif(self.geocid == GoogleId) :
                        delay   =   BING_DELAY
                    elif(self.geocid == OpenMapQuestId) :
                        delay   =   OPENMAPQUEST_DELAY
                    else :
                        delay   =   NOMINATIM_DELAY
                    
                    import time
                    time.sleep(delay) 
                    
                    self.geocodeTaskListMonitor.clear_completed_tasks()
                    
                if( (self.rowindex > self.maxrows) and 
                    (self.geocodeTaskListMonitor.all_tasks_completed()) ) :
                    set_geocode_runner_halt_flag(True)
                    set_status_bar(FINISHED)
    
            else :
                set_geocode_runner_halt_flag(True)    
            
    def get_results_log(self):
        return(self.geocodingResults)
    def get_error_log(self):
        return(self.geocodingErrorLog)
    def get_halt_flag(self):
        return(self.halt_all_geocoding)
    def set_halt_flag(self,fstate):
        self.halt_all_geocoding     =   fstate
    def get_geocode_id(self):
        return(self.geocid)
    def get_geocode_type(self):
        return(self.geotype)
    def get_geocode_connector(self):
        return(self.geocoder)
    def set_geocode_connector(self,connector):
        self.geocoder = connector
    
    def drop_geocoder_task(self,rowid) :
        self.geocodeTaskListMonitor.droptask(rowid)


"""
#--------------------------------------------------------------------------
#   static geocode runner object
#--------------------------------------------------------------------------
"""    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        






