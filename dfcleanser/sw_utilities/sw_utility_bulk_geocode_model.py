"""
# sw_utility_bulk_geocode_model
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_control as subgc


from dfcleanser.common.common_utils import (opStatus, get_dfc_dataframe)

import time


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
    
    for i in range(len(address_map.colsIndices)) :
        
        if(address_map.colsIndices[i] > -1) :
            geocode_address.append(df.iloc[rowIndex,address_map.colIndices[i]] + " ")
        else :
            geocode_address.append(address_map.colValues[i] + " ")
        
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
    
    address_cols        =   address_cols.replace(",","")
    address_components  =   address_cols.split("+")
    
    colnames            =   cfg.get_dfc_dataframe().columns.values.tolist() 
   
    for i in range(len(address_components)) :

        if(address_components[i] in colnames) :
            colIndices.append(colnames.get_loc())
            colValues.append(None)
            
        else :
            colIndices.append(-1)
            colValues.append(address_components[i])
    
    addressMap  =    AddressMap(colIndices,colValues)       
            
    return(addressMap)


        
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
    geocodeType         =   sugm.QUERY
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
        
        threading.Thread(target=self.geocoder_task).start()

    def geocoder_task(self):
        self.task_running       =   True
        self.run_geocode_method()            
        self.task_running       =   False

    def get_task_run_results(self) :
        return([self.rowId,self.geocode_results,self.opstat])
 
    def run_geocode_method(self) :
        
        if(self.geocoderId == sugm.GoogleId) :
            if(self.geocoder_type == sugm.QUERY) :
                self.geocode_results    =   subgc.get_google_geocode_results(self.inputParms,self.runParms)
            elif(self.geocoder_type == sugm.REVERSE) :
                self.geocode_results    =   subgc.get_google_reverse_results(self.inputParms,self.runParms) 

            # no error occurred
            if(self.geocode_results.get_status()) :
                if(self.geocoder_type == sugm.QUERY) :
                    subgc.process_google_geocode_results(self.inputParms,self.runParms,self.geocode_results)
                else :
                    subgc.process_google_reverse_results(self.inputParms,self.runParms,self.geocode_results)
            
            # error occurred        
            else :
                if(self.geocode_results.get_error_message() == OverQueryLimitErrorMessage) : 
                    stop_geocode_runner()
                
                subgc.process_google_geocoding_errors(self.geocoder_type,self.inputParms,self.runParms,self.geocode_results)
                
        else :
            self.geocode_results    =   None            

    def get_task_run_state(self) :
        return(self.task_running)    
        
        
class GeocodeTaskListMonitor:
    
    taskdict        =   {}
    maxtasks        =   0
        
    def __init__(self, maxtasksparm):
        self.taskdict        =   {}
        self.maxtasks        =   maxtasksparm
    
    def addtask(self, geocodetask, rowindex):
        self.taskdict.update({rowindex:geocodetask})
        
    def droptask(self, rowindex):
        self.taskdict.pop(rowindex)

    def more_tasks_available(self):
        if(len(self.taskdict) < self.maxtasks) :
            return(True)
        else :
            return(False)

    def clear_completed_tasks(self) :
        tasks   =   self.taskdict.keys().sort() 
        
        for i in range(len(tasks)) :
            if(not (self.taskdict.get(tasks[i]).get_task_run_state()) ) : 
                self.droptask(tasks[i])
        

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
    geotype             =   None
    runParms            =   None
    addressParms        =   None
    
    rowindex            =   0
    maxrows             =   0

    state               =   sugm.STOPPED
    halt_all_geocoding  =   True
 
    geocodeTaskMonitor  =   None
    geocodingResults    =   None
    geocodingErrorLog   =   None
       
    def __init__(self):
        self.geocoder           =   None
        self.geotype            =   None
        self.runParms           =   None
        self.addressParms       =   None
        self.rowindex           =   0
        self.maxrows            =   0
        self.state              =   sugm.STOPPED
        self.halt_all_geocoding =   True
        
        self.geocodeTaskMonitor =   None
        self.geocodingResults   =   None
        self.geocodingErrorLog  =   None
        
    def load_run(self,geocoderId,geoType,runParms,addressParms,maxrowsparm):
        self.geocoder           =   geocoderId
        self.geotype            =   geoType
        self.runParms           =   runParms
        self.addressParms       =   addressParms
        self.maxrows            =   maxrowsparm
        
        if(geocoderId == sugm.GoogleId) :
            self.geocodeTaskListMonitor  =   GeocodeTaskListMonitor(sugm.MAX_GOOGLE_TASKS)
        
        from dfcleanser.sw_utilities.sw_utility_bulk_geocode_control import init_geocoding_data_structures
        bulkstructures          =   init_geocoding_data_structures(self.geocoder,self.geotype,self.runParms)
        self.geocodingResults   =   bulkstructures[0]
        self.geocodingErrorLog  =   bulkstructures[1]
        
    def start_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.rowindex           =   0
        self.start_bulk_geocode_runner(0)        

    def stop_run(self):
        self.state              =   sugm.STOPPING
        BulkGeocodeRunner.halt_all_geocoding = True
            
    def pause_run(self):
        self.state              =   sugm.PAUSING
        BulkGeocodeRunner.halt_all_geocoding = True
    
    def resume_run(self):
        self.state              =   sugm.RUNNING
        BulkGeocodeRunner.halt_all_geocoding = False
        self.start_bulk_geocode_runner(self.rowindex)        
        
    def get_run_state(self):
        return(self.state)
    
    def start_bulk_geocode_runner(self,rowIndex) :
        self.rowindex   =   rowIndex
        threading.Thread(target=self.bulk_geocode_runner_task).start()
        
    def bulk_geocode_runner_task(self):
        while (not(BulkGeocodeRunner.halt_all_geocoding)) :
            
            if(self.geocoder == sugm.ArcGISId) :
                
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

                
            elif(self.geocoder == sugm.GoogleId) :
                
                opstat      =   opStatus()
                
                if(self.geocodeTaskListMonitor.more_tasks_available()) :
                    next_addr       =   get_geocode_address_string(self.addressParms,self.rowindex)
                    geocodetask     =   GeocodeTask(sugm.GoogleId,sugm.QUERY,self.runParms,next_addr)  
                    self.geocodeTaskListMonitor.addtask(geocodetask,self.rowindex)
                    
                    self.rowindex   =   self.rowindex + 1
                    time.sleep(sugm.GOOGLE_DELAY)
                    
                else :
                    
                    self.geocodeTaskMonitor.clear_completed_tasks()
                    
                    time.sleep(sugm.GOOGLE_DELAY)
                    
                if(self.rowindex > self.maxrows) :
                    BulkGeocodeRunner.halt_all_geocoding = True    
                    
            else :
                BulkGeocodeRunner.halt_all_geocoding = True    
            
            
    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        
        
