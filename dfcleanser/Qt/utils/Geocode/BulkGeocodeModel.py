"""
# BulkGeocodeModel
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import json
import sys
import googlemaps


"""
#--------------------------------------------------------------------------
#   geocode debug flags
#--------------------------------------------------------------------------
"""

GEOCODE_TRACE_GET_GEOCODE           =   False

GEOCODE_TRACE_GET_GEOCODE_LOAD      =   False
GEOCODE_TRACE_ADD_RESULT            =   False
GEOCODE_TRACE_DISPLAY_FORM          =   False

DEBUG_GEOCODE_BULK_UTILS            =   False
GEOCODE_THREAD_DEBUG                =   False


GEOCODE_TRACE_GET_GEOCODE_VALUES    =   False

GEOCODE_TRACE_GET_GEOCODE_DETAILS   =   False
GEOCODE_TRACE_GET_RUN_TASK          =   False


GEOCODE_TRACE_PROCESS_RESULTS       =   False
GEOCODE_TRACE_FLUSH_RESULTS         =   False
GEOCODE_TRACE_PROCESS_ERRORS        =   False


import dfcleanser.common.cfg as cfg

import dfcleanser.Qt.utils.Geocode.GeocodeModel as GM

#import dfcleanser.Qt.utils.Geocode.BulkGeocodeConsole as BGCC
import dfcleanser.Qt.utils.Geocode.BulkGeocodeControl as BGC



#import dfcleanser.Qt.utils.Geocode.GeocodeControl as GC

from dfcleanser.common.common_utils import (opStatus,
                                            delete_a_file, rename_a_file, does_file_exist,
                                            does_dir_exist, make_dir)


from math import floor

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
GoogleId                    =   7
OpenMapQuestId              =   9
NominatimId                 =   11

supported_Geocoders         =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]
supported_Reverses          =   [ArcGISId,BingId,GoogleId,OpenMapQuestId,NominatimId]

supported_Bulk_Geocoders    =   [BingId,GoogleId]
supported_Bulk_Reverses     =   [BingId,GoogleId]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Bulk Geocoder runtime settings
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
GOOGLE_DELAY                =   0.5#05
BING_DELAY                  =   0.5
BAIDU_DELAY                 =   1

GOOGLE_TIMEOUT              =   5
BING_TIMEOUT                =   5
BAIDU_TIMEOUT               =   5
ARCGIS_TIMEOUT              =   45

GOOGLE_RETRY_LIMIT          =   3
BING_RETRY_LIMIT            =   3
BAIDU_RETRY_LIMIT           =   3

GOOGLE_THREAD_LIMIT         =   10
BING_THREAD_LIMIT           =   15
BAIDU_THREAD_LIMIT          =   10


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Geocoder Function Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_MAIN_GEOCODING          =   0

BULK_LOAD_GEOCODER              =   19
BULK_START_GEOCODER             =   20
BULK_STOP_GEOCODER              =   21
BULK_PAUSE_GEOCODER             =   22
BULK_RESUME_GEOCODER            =   23
BULK_VIEW_ERRORS                =   24
BULK_EXIT_GEOCODER              =   25
BULK_RESULTS_GEOCODER           =   26

PROCESS_BULK_RESULTS            =   30
REPORT_GEOCODE_RUN_ERROR        =   31

"""
#--------------------------------------------------------------------------
#   bulk results commands
#--------------------------------------------------------------------------
"""

DISPLAY_BULK_RESULTS_BASE                       =   0
DISPLAY_BULK_RESULTS_APPEND                     =   1
DISPLAY_BULK_RESULTS_EXPORT_CSV                 =   2

DISPLAY_BULK_RESULTS                            =   19 

DISPLAY_BULK_SOURCE_DF                          =   20 
DISPLAY_BULK_RESULTS_DF                         =   21 
DISPLAY_BULK_ERRORS_DF                          =   22 
DISPLAY_BULK_RESULTS_RETURN                     =   23
 

DISPLAY_BULK_ERRORS_CSV_PROCESSED               =   31


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

#INTERACTIVE                 =   0
BULK                        =   1
BULK_TUNING                 =   2

GEOCODE_ADDRESS             =   0
GEOCODE_COORDS              =   1


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
#   bulk geocoder current state
#--------------------------------------------------------------------------
"""
RUNNING                     =   0
STOPPED                     =   1
PAUSED                      =   2
STARTING                    =   3
STOPPING                    =   4
PAUSING                     =   5
FINISHED                    =   6
ERROR_LIMIT                 =   7

CHECKPOINT_STARTED          =   8
CHECKPOINT_COMPLETE         =   9


LOAD                        =   10
START                       =   11
STOP                        =   12
PAUSE                       =   13
RESUME                      =   14


GEOCODE_BAR                 =   0
ERROR_BAR                   =   1

"""
#--------------------------------------------------------------------------
#   bulk geocoder current load run parms
#--------------------------------------------------------------------------
"""

BULK_GEOCODE_CURRENT_GEOCODER       =   "currentBulkGeocodingGeocoder"
BULK_GEOCODE_CURRENT_GEOTYPE        =   "currentBulkGeocodingGeotype"
BULK_GEOCODE_CURRENT_RUNPARMS       =   "currentBulkGeocodingRunParms"
BULK_GEOCODE_CURRENT_ADDRPARMS      =   "currentBulkGeocodingAddressParms"


bulk_geocodes_sent_out          =   []

bulk_geocodes_tasks_active     =   {}



"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Task Class
#----------------------------------------------------------------------------
#   geocoding task class for retrieving gecoding results
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""

class GeocodeThread :
    
    geocoderId          =   -1
    geocodeType         =   GM.QUERY
    rowId               =   -1
    inputparms          =   None
    runParms            =   None
    
    geocode_results     =   None
    task_running        =   False
    
    thread_start_time   =   None
    
    opstat              =   None
        
    def __init__(self, geocoderId,geocodeType,rowid,inputparms,runparms):
        
        self.geocoderId         =   geocoderId
        self.geocoder_type      =   geocodeType
        self.rowId              =   rowid
        self.inputParms         =   inputparms
        self.runParms           =   runparms
        self.geocode_results    =   None
        self.task_running       =   False
        
        self.opstat             =   opStatus()
        
        if(geocoderId == GM.ArcGISId) :
            import datetime;
            self.thread_start_time = datetime.datetime.now().timestamp()

        bulk_geocodes_tasks_active.update({self.rowId : self.thread_start_time})

        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS ) :
            cfg.add_debug_to_log("GeocodeThread","[init]  " + str(inputparms))

    def run_geocoder_thread(self) :
        
        try :
            self.task_running       =   True
            self.run_geocode_method(self.opstat)  
        except :
            import sys
            BGC.process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,
                                              "[run_geocoder_thread] Task Exception : " + str(sys.exc_info()[0].__name__),
                                              "[run_geocoder_thread][" + self.opstat.get_errorMsg() + "]")
            
        self.task_running       =   False

        import time
        time.sleep(0.02)
        
            
    def run_geocode_method(self,opstat) :
        
        retry_count     =   0
        #import geopy
        
        if(GEOCODE_TRACE_GET_RUN_TASK)  :  
            if(retry_count > 0) :
                cfg.add_debug_to_log("run_geocode_method"," retry_count : limit ] " + str(retry_count) + " : " + str(GOOGLE_RETRY_LIMIT))        

        if(self.geocoderId == GM.GoogleId) :
            
            while(retry_count < GOOGLE_RETRY_LIMIT) :
                
                try :
                    if(self.geocoder_type == GM.QUERY) :
                        self.geocode_results    =   BGC.get_google_query_results(self.rowId,self.inputParms,self.runParms,opstat)
                    elif(self.geocoder_type == GM.REVERSE) :
                        self.geocode_results    =   BGC.get_google_reverse_results(self.rowId,self.inputParms,self.runParms,opstat) 
                except :
                    if(GEOCODE_TRACE_GET_RUN_TASK)  :   
                        cfg.add_debug_to_log("run_geocode_method","  excepton from get : " + str(self.inputParms) + " : " + + str(sys.exc_info()[0].__name__))        

                if(not (self.geocode_results is None) ) :
                    
                    # no error occurred
                    if(opstat.get_status()) :
                        if(self.geocoder_type == GM.QUERY) :
                            BGC.process_google_query_results(self.rowId,self.inputParms,self.runParms,self.geocode_results,opstat)
                        else :
                            BGC.process_google_reverse_results(self.rowId,self.inputParms,self.runParms,self.geocode_results,opstat)
                            
                        retry_count     =   GOOGLE_RETRY_LIMIT
            
                    else :

                        if( (opstat.get_errormsg() == GM.OverQueryLimitErrorMessage) or 
                            (opstat.get_errormsg() == GM.GoogleGeocoderConnectionErrorMessage) ): 
                        
                            stop_geocode_runner(opstat.get_errormsg())
                            retry_count     =   GOOGLE_RETRY_LIMIT
                        
                        elif(opstat.get_errormsg() == GM.TimeoutErrorMessage) :     
                            retry_count     =   retry_count + 1
                        
                        elif(opstat.get_errormsg() == GM.RetriableRequestErrorMessage) :     
                            retry_count     =   retry_count + 1
                            
                        if(retry_count == GOOGLE_RETRY_LIMIT) :   
                            BGC.process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,
                                                              opstat.get_errorMsg(),"[run_geocode_method] RETRY_LIMIT")
                    
                else :

                    BGC.process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,
                                                      "No results returned","[run_geocode_method] results none") 

                    retry_count     =   GOOGLE_RETRY_LIMIT
                    
        elif( (self.geocoderId == GM.BingId) ):
            
            retry_limit    =   BING_RETRY_LIMIT

            while(retry_count < retry_limit) :

                if(GEOCODE_TRACE_GET_GEOCODE) :
                    cfg.add_debug_to_log("run_geocode_method[get_geopy_geocode_results]"," address : " + str(self.inputParms))

                self.geocode_results    =   BGC.get_geopy_geocode_results(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,self.runParms,self.opstat)
                
                if(GEOCODE_TRACE_GET_GEOCODE) :
                    if(self.geocode_results is None) :
                        cfg.add_debug_to_log("run_geocode_method][get_geopy_geocode_results"," results : None")

                if(opstat.get_status()) :
                
                    if(self.geocode_results is None) :
                        BGC.process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,
                                                          opstat.get_errormsg(),"[run_geocode_method] results none")
                    else :
                        BGC.process_geopy_geocode_results(self.rowId,self.geocoderId,self.geocoder_type,self.inputParms,self.runParms,self.geocode_results,opstat)
                        
                    retry_count     =   retry_limit
            
                else :
                
                    if( (opstat.get_errorMsg() == GM.GeopyGeocoderConnectionErrorMessage) or
                        (opstat.get_errorMsg() == GM.GeopyGeocoderQuotaExceededMessage) or 
                        (opstat.get_errorMsg() == GM.GeopyErrorMessage) or 
                        (opstat.get_errorMsg() == GM.GeopyConfigurationError) or 
                        (opstat.get_errorMsg() == GM.GeopyGeocoderServiceErrorMessage) ) : 
    
                        stop_geocode_runner(opstat.get_errormsg())
                        retry_count     =   retry_limit
                    
                    elif(opstat.get_errorMsg() == GM.GeopyGeocoderGeocoderTimedOutMessage) :
                        retry_count     =   retry_count + 1  
                        
                    else :
                        stop_geocode_runner(opstat.get_errorMsg())
                        retry_count     =   retry_limit
                
                    if(retry_count == retry_limit) :
                        BGC.process_bulk_geocoding_errors(self.geocoderId,self.geocoder_type,self.rowId,self.inputParms,
                                                          opstat.get_errorMsg(),"[run_geocode_method] retry_limt")
                        BGC.process_geopy_geocode_results(self.rowId,self.geocoderId,self.geocoder_type,self.inputParms,self.runParms,self.geocode_results,opstat,self.rowId)
        
        if(GEOCODE_TRACE_GET_RUN_TASK) :            
            cfg.add_debug_to_log("run_geocode_method][complete]"," address : " + str(self.inputParms) + " stored " + str(opstat.get_status()))



        #bulk_geocodes_tasks_active.pop(self.rowid, None)
        try :
            from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
            dfc_Geocode_Runner.drop_thread(self.rowId)
        except Exception as e:
            cfg.add_debug_to_log("gmaps.geocode]","  error : "+ str(sys.exc_info()[0].__name__) + " : " + str(sys.exc_info()[1])) 
               
    def get_thread_run_state(self) :
        return(self.task_running)    
    
    def get_thread_row_id(self) :
        return(self.rowId)    

    def get_thread_start_time(self) :
        return(self.thread_start_time)    


"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Thread Monitor Class
#----------------------------------------------------------------------------
#   geocoding thread monitoring class for controlling geocode threads
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""        
import threading
        
class GeocodeThreadsMonitor:
    
    threaddict      =   {}
    maxthreads      =   0
        
    def __init__(self, maxthreadsparm):
        self.threaddict      =   {}
        self.maxthreads      =   maxthreadsparm
    
    def addthread(self, geocodetask, rowindex):
        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
            cfg.add_debug_to_log("addthread","["+ str(rowindex)+"]")

        self.threaddict.update({rowindex:geocodetask})
        threading.Thread(target=geocodetask.run_geocoder_thread).start()
        
    def dropthread(self, rowindex):

        if(not(self.threaddict.get(rowindex,None) is None)) :
            self.threaddict.pop(rowindex,None)
            if(GEOCODE_THREAD_DEBUG)  :    
                cfg.add_debug_to_log("dropthread","[" + str(rowindex) + "] : num active threads [" + str(len(self.threaddict))+"]" + str(list(self.threaddict.keys())))
        else :
            if(GEOCODE_THREAD_DEBUG)  :   
                cfg.add_debug_to_log("dropthread"," : thread not found")

    def more_threads_available(self):

        if(len(self.threaddict) < self.maxthreads) :
            return(True)
        else :
            return(False)

    def clear_completed_threads(self) :
        task_keys   =   list(self.threaddict.keys())

        if(0):#GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("clear_completed_threads"," : " + str(task_keys))
        
        for i in range(len(task_keys)) :
            ctask   =   self.threaddict.get(task_keys[i])

            if( not(ctask.get_thread_run_state()) ) :
                self.dropthread(ctask.get_thread_row_id())

    def all_threads_completed(self) :
        if(len(self.threaddict) == 0) :
            return(True)
        else :
            return(False)

    def threads_running(self) :
        return(len(self.threaddict))

"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-  Geocoding Runner Class
#----------------------------------------------------------------------------
#   class for running the current geocoding instance from dfcleanser.
#   controls threads and updates display
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
def stop_geocode_runner(error_msg=None) :
    dfc_Geocode_Runner.stop_run(error_msg) 
def pause_geocode_runner() :
    dfc_Geocode_Runner.pause_run() 
def resume_geocode_runner() :
    dfc_Geocode_Runner.resume_run() 
def checkpoint_geocode_runner() :
    dfc_Geocode_Runner.checkpoint_run() 

def get_geocode_runner_results_log() :
    return(dfc_Geocode_Runner.get_results_log())
def get_geocode_runner_results_count() :
    return(dfc_Geocode_Runner.get_results_log_count())
def get_geocode_runner_error_log() :
    return(dfc_Geocode_Runner.get_error_log())

def get_geocode_runner_state() :
    return(dfc_Geocode_Runner.get_run_state())
def set_geocode_runner_state(state) :
    dfc_Geocode_Runner.set_run_state(state)
    
def get_geocode_runner_halt_flag() :
    return(dfc_Geocode_Runner.get_halt_flag())
def set_geocode_runner_halt_flag(state) :
    dfc_Geocode_Runner.set_halt_flag(state)

def get_geocode_runner_id() :
    return(dfc_Geocode_Runner.get_geocode_id())
def get_geocode_runner_type() :
    return(dfc_Geocode_Runner.get_geocode_type())
def get_geocode_runParms() :
    return(dfc_Geocode_Runner.get_runParms())
def get_geocode_connector() :
    return(dfc_Geocode_Runner.get_geocode_connector())
def set_geocode_connector(connector) :
    return(dfc_Geocode_Runner.set_geocode_connector(connector))
def get_geocode_maxrows() :
    return(dfc_Geocode_Runner.get_geocode_maxrows())
def get_geocode_checkpoint_interval() :
    return(dfc_Geocode_Runner.get_geocode_checkpoint_interval())

def get_geocode_run_total_time() :
    return(dfc_Geocode_Runner.get_total_run_time())

def get_geocode_lat_long_map() :
    return(dfc_Geocode_Runner.get_geocode_lat_long_map())

"""
#----------------------------------------------------------------------------
#-  Bulk Geocoding Runner Class
#----------------------------------------------------------------------------
"""

import datetime

class BulkGeocodeRunner:
    
    geocid                  =   None
    geotype                 =   None
    runParms                =   None
    addressParms            =   None
    
    rowindex                =   0
    maxrows                 =   0

    state                   =   STOPPED
    halt_all_geocoding      =   True
    geocoding_in_error      =   False
    
    geocoder                =   None
    
    geocodeThreadsMonitor   =   None
    geocodingResults        =   None
    geocodingErrorLog       =   None
    
    ResultsLength           =   0
    ErrorsLength            =   0
    
    start_time              =   0
    stop_time               =   0
    
    stop_error_msg          =   None
    
    checkpoint_on           =   False
    checkpoint_interval     =   10000
    last_checkpoint_rowid   =   0
    
    lat_long_map            =   []
       
    def __init__(self):
        
        self.geocid                 =   None
        self.geotype                =   None
        self.runParms               =   None
        self.addressParms           =   None

        self.rowindex               =   0
        self.startindex             =   0
        self.maxrows                =   0

        self.state                  =   STOPPED
        self.halt_all_geocoding     =   True
        self.geocoding_in_error     =   False
        
        self.geocoder               =   None
        
        self.geocodeThreadsMonitor  =   None
        self.geocodingResults       =   None
        self.geocodingErrorLog      =   None
        
        self.ResultsLength          =   0
        self.ErrorsLength           =   0
        
        self.start_time             =   0
        self.stop_time              =   0
        self.stop_error_msg         =   None
        
        self.checkpoint_on          =   False
        self.checkpoint_interval    =   10000 
        self.last_checkpoint_rowid  =   0

        self.lat_long_map           =   []

        self.api_parms              =   {}
        
        
    def load_run(self,geocoderId,geoType,runParms,addressParms):
        
        if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
            cfg.add_debug_to_log("load_run","  : geocid : " + str(geocoderId) + " geotype : " + str(geoType)) 
            cfg.add_debug_to_log("load_run","  : runParms : " + str(runParms))

           
        self.geocid             =   geocoderId
        self.geotype            =   geoType
        self.runParms           =   runParms
        self.addressParms       =   addressParms

        cfg.set_config_value(BULK_GEOCODE_CURRENT_GEOCODER,self.geocid)
        cfg.set_config_value(BULK_GEOCODE_CURRENT_GEOTYPE,self.geotype)
        cfg.set_config_value(BULK_GEOCODE_CURRENT_RUNPARMS,self.runParms)
        #cfg.set_config_value(BULK_GEOCODE_CURRENT_ADDRPARMS,self.addressParms)
        
        if(self.geotype == GM.REVERSE) :
            self.lat_long_map   =   get_lat_longs_map(self.geocid,self.runParms)
        
        if(self.geocid == GM.GoogleId) :
            
            if(self.geotype == GM.QUERY) :
                
                self.maxrows                =   int(runParms.get("max_addresses_to_geocode"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
                
            else :
                
                self.maxrows                =   int(runParms.get("max_lat_longs"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
                
        elif(self.geocid == GM.BingId) :
            
            if(self.geotype == GM.QUERY) :
                
                self.maxrows                =   int(runParms.get("max_addresses_to_geocode"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))

            else :
                
                self.maxrows                =   int(runParms.get("max_lat_longs"))
                self.checkpoint_interval    =   int(runParms.get("checkpoint_interval"))
        
        if(self.geocid == GM.GoogleId):
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(GOOGLE_THREAD_LIMIT)
        elif(self.geocid == GM.BingId):
            self.geocodeThreadsMonitor  =   GeocodeThreadsMonitor(BING_THREAD_LIMIT)
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import init_geocoding_data_structures
        bulkstructures          =   init_geocoding_data_structures(self.geocid,self.geotype,self.runParms)
        self.geocodingResults   =   bulkstructures[0]
        self.geocodingErrorLog  =   bulkstructures[1]

        self.api_parms  =   BulkGeocodeRunParms(self.geocid,self.geotype,runParms)
        if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
            cfg.add_debug_to_log("load_run","  : self.api_parms : " + str(self.api_parms.get_api_parms())) 

        control_bulk_keys([ENABLE,DISABLE,DISABLE,DISABLE,DISABLE,DISABLE,DISABLE],"G")
        
        
    def start_run(self):
        opstat          =   opStatus()

        if(GEOCODE_THREAD_DEBUG) :
            cfg.add_debug_to_log("start_run","") 

        set_status_bar(STARTING)
        self.set_run_state(STARTING)

        self.set_halt_flag(False)
        
        if((self.geocid == GM.BingId) or (self.geocid == GM.GoogleId)) :
            
            runparms            =   self.get_runParms()

            try:
                start_row           =   int(runparms.get("starting_row_id"))
                self.rowindex       =   start_row
                self.startindex     =   start_row
            except:
                self.rowindex   =   0    

        else :
            self.rowindex           =   0
        
        self.start_time         =   datetime.datetime.now()
        self.stop_time          =   datetime.datetime.now()
        
        return(self.start_bulk_geocode_runner(self.rowindex))
        
    def stop_run(self,error_msg=None) :

        if(self.get_run_state() == PAUSED) :

            set_status_bar(STOPPED)
            self.set_run_state(STOPPED)
           
        else : 

            set_status_bar(STOPPING)
            self.set_run_state(STOPPING)
            
        self.set_halt_flag(True)
        import datetime
        self.stop_time          =   datetime.datetime.now()
        
        if(GEOCODE_THREAD_DEBUG)  :   
            if(self.stop_error_msg == None) :
                cfg.add_debug_to_log("stop_run","")
            else :
                cfg.add_debug_to_log("stop_run"," : " + self.stop_error_msg)
        
    def pause_run(self) :
        set_status_bar(PAUSING)
        self.set_run_state(PAUSING)
        self.set_halt_flag(True)
        if(GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("pause_run"," : halt PAUSE")

    def resume_run(self):
        set_status_bar(RUNNING)
        self.set_run_state(RUNNING)
        self.set_halt_flag(False)
        self.rowindex           =   self.geocodingResults.get_results_count()
        self.start_bulk_geocode_runner(self.rowindex)        
        
    def checkpoint_run(self) :
        self.checkpoint_on  =   True
        self.pause_run()
        
    def get_run_state(self):
        return(self.state)
    
    def set_run_state(self,runstate):
        
        if(GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("set_run_state"," : current state : new state :" + str(self.state) + "  " + str(runstate))
        
        self.state  =   runstate
    
    def start_bulk_geocode_runner(self,rowIndex) :

        if(GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("start_bulk_geocode_runner"," : " + "geocid : " + str(self.geocid) + " geotype " + str(self.geotype) + " maxrows " + str(self.maxrows) + " rowindex " + str(rowIndex))

        self.rowindex   =   rowIndex
        opstat          =   opStatus()

        from dfcleanser.Qt.utils.Geocode.BulkGeocode import(get_bulk_google_geocoder_connection,google_bulk_geocoder_id)        
        try :
            if(self.geocid == GM.GoogleId) :   
                geocoderparms   =   cfg.get_config_value(google_bulk_geocoder_id+"Parms")
                self.geocoder   =   get_bulk_google_geocoder_connection(geocoderparms[0],geocoderparms[1],geocoderparms[2],opstat)
            else :  
                from dfcleanser.Qt.utils.Geocode.GeocodeControl import get_geocoder_engine
                self.geocoder   =   get_geocoder_engine(self.geocid,opstat)
                
        except Exception as e:
            opstat.store_exception("Unable to establish " + GM.get_geocoder_title(self.geocid) + " geocoder connection ",e)
        
        if(opstat.get_status()) :
        
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                cfg.add_debug_to_log("start_bulk_geocode_runner"," got connection")
            
            self.set_halt_flag(False)
            threading.Thread(target=self.bulk_geocode_runner_task).start()
            set_status_bar(RUNNING)
            
            control_bulk_keys([DISABLE,ENABLE,ENABLE,DISABLE,ENABLE,DISABLE,DISABLE],"H")
            
            return(opstat)
            
        else :
            return(opstat)
        
    def bulk_geocode_runner_task(self) :
        
        opstat                  =   opStatus()
        arcgis_geocodethread    =   None   
        
        while ( (not (self.is_geocode_run_complete()))  ) :

            self.geocodeThreadsMonitor.clear_completed_threads()

            if(self.geocid == GM.GoogleId) :
                delay   =   GOOGLE_DELAY
            elif(self.geocid == GM.BingId) :
                delay   =   BING_DELAY
                        
            import time
            time.sleep(delay)


            if(self.is_checkpoint_needed())  :
                
                if(self.geocid == GM.GoogleId) :
                    delay   =   GOOGLE_DELAY
                elif(self.geocid == GM.BingId) :
                    delay   =   BING_DELAY
                        
                import time
                time.sleep(delay)
                
                if(self.geocodeThreadsMonitor.all_threads_completed()) :
                    self.checkpoint_results(opstat)
                    
                    if(opstat.get_status()) :
                        set_status_bar(RUNNING)
                        control_bulk_keys([DISABLE,ENABLE,ENABLE,DISABLE,ENABLE,ENABLE,DISABLE],"I")
                    else :
                        self.geocodingErrorLog.log_error(self.last_checkpoint_rowid,"NA",opstat.get_errorMsg(),"",opstat)
                        self.pause_run()                        
                
            else :
            
                if( not (self.get_halt_flag()) ) :
                
                    if( (self.geocid == GM.GoogleId) or (self.geocid == GM.BingId) ):
                    
                        if(self.geocodeThreadsMonitor.more_threads_available()) :
                        
                            if(self.rowindex < (self.maxrows + self.startindex)) :
                            
                                if(self.geotype == GM.QUERY) :

                                    try :

                                        next_addr       =   get_geocode_address_string(self.geocid,self.runParms,self.addressParms,self.rowindex)
                                
                                        if(GEOCODE_THREAD_DEBUG)  :
                                            cfg.add_debug_to_log("bulk_geocode_runner_task"," new thread " + str(next_addr) )
                                    
                                        geocodethread   =   GeocodeThread(self.geocid,self.geotype,self.rowindex,next_addr,self.runParms)  
                                        self.geocodeThreadsMonitor.addthread(geocodethread,self.rowindex)

                                    except  :
                                        import sys
                                        if(GEOCODE_TRACE_GET_GEOCODE)  : 
                                            cfg.add_debug_to_log("add query"," thread exception " + str(sys.exc_info()[0].__name__))
                                    
                                else :
                                    
                                    try :

                                        next_lat_lng    =   get_geocode_reverse_lat_lng_string(self.geocid,self.runParms,self.rowindex)
                                
                                        if(GEOCODE_THREAD_DEBUG)  :
                                            cfg.add_debug_to_log("bulk_geocode_runner_task"," next_lat_lng " + str(next_lat_lng) )

                                        geocodethread   =   GeocodeThread(self.geocid,self.geotype,self.rowindex,next_lat_lng,self.runParms)  
                                        self.geocodeThreadsMonitor.addthread(geocodethread,self.rowindex)

                                    except  :
                                        import sys
                                        if(GEOCODE_TRACE_GET_GEOCODE)  : 
                                            cfg.add_debug_to_log("add reverse"," thread exception " + str(sys.exc_info()[0].__name__))
                                                                                
                                self.rowindex   =   self.rowindex + 1
                    
                            else :
                                if(GEOCODE_TRACE_GET_GEOCODE)  : 
                                    cfg.add_debug_to_log("bulk_geocode_runner_task"," halt no threads available")
                                self.set_halt_flag(True)
                            
                        else :
                    
                            if(self.geocid == GM.GoogleId) :
                                delay   =   GOOGLE_DELAY
                            elif(self.geocid == GM.BingId) :
                                delay   =   BING_DELAY
                        
                            import time
                            time.sleep(delay)
                        
                        self.update_status_bar(self.rowindex)
                    
                        if( self.rowindex >= (self.maxrows + self.startindex) ) :
                            self.set_halt_flag(True)
                            if(GEOCODE_THREAD_DEBUG)  :   
                                cfg.add_debug_to_log("bulk_geocode_runner_task"," halt max rows : halt - google " + str(self.rowindex) + " " + str(self.maxrows))

     
                    else :
                        set_geocode_runner_halt_flag(True)    
                        self.geocoding_in_error     =   True

                    self.update_status_bar(self.rowindex) 
                    self.update_state()

                else :
                
                    self.update_status_bar(self.rowindex) 
                    self.update_state()
                
                    import time
                    time.sleep(0.2)


        if(self.is_geocode_run_complete()) :
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                cfg.add_debug_to_log("bulk_geocode_runner_task"," is complete : " + str(self.is_geocode_run_complete()))
        
        if(self.is_geocode_run_complete()) :
            
            if(GEOCODE_THREAD_DEBUG)  :   
                cfg.add_debug_to_log("geocode run is complete"," : self.geocoding_in_error " + str(self.geocoding_in_error)) 
                
            self.update_status_bar(self.rowindex) 
            self.update_state()            
            
            self.geocodingResults.finish_results_log(opstat)
            self.geocodingErrorLog.finish_error_log(opstat)

            import datetime
            self.stop_time         =   datetime.datetime.now()
            
            if(self.geocoding_in_error) :
                set_status_bar(STOPPED) 
            else :   
                set_status_bar(FINISHED)
                set_geocode_runner_state(FINISHED)

                current_count       =   self.geocodingResults.get_results_count()
                current_percent     =   int( ( current_count / self.maxrows ) * 100 )
                set_progress_bar_value(self.geocid,self.geotype,GEOCODE_BAR,current_count,current_percent)

                total_errors        =   get_geocode_runner_error_log().get_error_count()
                current_error_rate  =   (total_errors / get_geocode_maxrows()) 
                set_progress_bar_value(self.geocid,self.geotype,ERROR_BAR,total_errors,int(current_error_rate))
                
                control_bulk_keys([DISABLE,DISABLE,DISABLE,DISABLE,DISABLE,DISABLE,ENABLE],"J")

        
    def is_geocode_run_complete(self) :
        
        
        if(self.geocodeThreadsMonitor.all_threads_completed()) :
            if((self.geocodingErrorLog.get_error_count() + self.geocodingResults.get_results_count()) >= self.maxrows) :

                if(GEOCODE_THREAD_DEBUG)  :   
                    cfg.add_debug_to_log("is_geocode_run_complete"," : state "+ str(self.state) + " threads completed :  " + str(self.geocodeThreadsMonitor.all_threads_completed()) + " results : " + str(self.geocodingResults.get_results_count()) + " errors : " + str(self.geocodingErrorLog.get_error_count()))

                return(True)
                
        return(False)

    def update_status_bar(self,id) :
        
        if(not (self.ResultsLength == self.geocodingResults.get_results_count())) :

            current_count       =   self.geocodingResults.get_results_count()
            current_percent     =   int( ( current_count / self.maxrows ) * 100 )
            
            set_progress_bar_value(self.geocid,self.geotype,GEOCODE_BAR,current_count,current_percent)
            
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                cfg.add_debug_to_log("update_status_bar"," current_count : current_percent " + str(current_count) + " : " + str(current_percent)) 
            
            self.ResultsLength  =   self.geocodingResults.get_results_count()

    def update_state(self) :
        
        opstat  =   opStatus()
        
        more_threads        =   self.geocodeThreadsMonitor.more_threads_available()
        all_threads         =   self.geocodeThreadsMonitor.all_threads_completed()
        threads_running     =   self.geocodeThreadsMonitor.threads_running()
        
        run_state   =   self.get_run_state()
            
        if(self.get_run_state()   ==  STARTING) : 
            if( (not (more_threads) )  or 
                (self.geocodingResults.get_results_count() > 0) ) : 
                set_status_bar(RUNNING)
                self.set_run_state(RUNNING)
                
        elif(self.get_run_state()   ==  STOPPING) :

            print("STOPPING")
            if(all_threads) :
                set_status_bar(STOPPED)
                self.set_run_state(STOPPED)

                opstat   =   opStatus()
                self.geocodingResults.finish_results_log(opstat)
                self.geocodingErrorLog.finish_error_log(opstat)

                import datetime
                self.stop_time         =   datetime.datetime.now()

                control_bulk_keys([DISABLE,DISABLE,DISABLE,DISABLE,DISABLE,DISABLE,ENABLE],"M")
            
        elif(self.get_run_state()   ==  PAUSING) :
            if(all_threads) : 
                set_status_bar(PAUSED)
                self.set_run_state(PAUSED)
                get_geocode_runner_results_log().flush_results_to_dataframe(opstat)
                
                control_bulk_keys([DISABLE,DISABLE,DISABLE,ENABLE,ENABLE,DISABLE,ENABLE],"K")
                
                if(self.checkpoint_on) :
                    if(GEOCODE_THREAD_DEBUG)  :   
                        cfg.add_debug_to_log("checkpoint_on",str(self.state))        

                    self.checkpoint_results()
                    set_status_bar(CHECKPOINT_COMPLETE)

        if(GEOCODE_TRACE_GET_GEOCODE) :
            if(not (run_state == self.get_run_state())) :
                cfg.add_debug_to_log("update_state"," : previous state : " + str(run_state) + " new run state : " +  str(self.get_run_state()) + " threads : " + str(threads_running) )


    def is_checkpoint_needed(self) :
        
        if((self.rowindex - self.last_checkpoint_rowid) >= self.checkpoint_interval) :
            
            if(GEOCODE_THREAD_DEBUG)  :   
                cfg.add_debug_to_log("is_checkpoint_needed"," : True  : rowindex : " + str(self.rowindex) + " interval : " + str(self.checkpoint_interval) + " last_checkpoint_rowid :  " + str(self.last_checkpoint_rowid))
            return(True)
            
        else :
            return(False)
            
    def checkpoint_results(self,opstat) :
        
        self.update_status_bar(-1)
        set_status_bar(CHECKPOINT_STARTED)
        control_bulk_keys([DISABLE,DISABLE,DISABLE,DISABLE,ENABLE,DISABLE,DISABLE],"L")

        
        if(GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("checkpoint_results"," : flush_results_to_dataframe")
        
        self.geocodingResults.flush_results_to_dataframe(opstat)
        
        if(self.geotype == GM.QUERY) :
        
            if(self.geocid == GM.GoogleId) :
                df_source   =   self.runParms.get("dataframe_to_geocode_from") 
            elif(self.geocid == GM.BingId) :
                df_source   =   self.runParms.get("dataframe_to_geocode") 
                
        else :
            
            if(self.geocid == GM.GoogleId) :
                df_source   =   self.runParms.get("dataframe_to_geocode_from") 
            elif(self.geocid == GM.BingId) :
                df_source   =   self.runParms.get("dataframe_to_geocode") 
        
        file_name       =   cfg.get_notebookName() + "_" + df_source + "_checkpoint"
        
        import os

        chckpt_file_path_name  =   os.path.join(cfg.get_notebookPath(),"PandasDataframeCleanser_files")
        chckpt_file_path_name  =   os.path.join(chckpt_file_path_name,"geocode_checkpoints")
        
        if(not (does_dir_exist(chckpt_file_path_name)) ) :   
            
            if( not(make_dir(chckpt_file_path_name)) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("Checkpoint dir " + chckpt_file_path_name + " not created successfully ")
                
        if(opstat.get_status()) :
            
            if(self.last_checkpoint_rowid == 0) :
                start_row_id    =   0
                file_number     =   0
            else :
                start_row_id    =   self.last_checkpoint_rowid
                file_number     =   floor(start_row_id / self.checkpoint_interval)
            
            chckpt_file_name    =   file_name + str(file_number) + ".csv"
            chckpt_file_name    =   os.path.join(chckpt_file_path_name,chckpt_file_name)
            
            if(GEOCODE_THREAD_DEBUG)  :   
                cfg.add_debug_to_log("checkpoint_results"," : chckpt_file_name " + str(chckpt_file_name)) 
        
            if(does_file_exist(chckpt_file_name)) :
                backup_checkpoint_file_name     =   chckpt_file_name.replace(".csv","_backup.csv")
                delete_a_file(backup_checkpoint_file_name,opstat)
                rename_a_file(chckpt_file_name,backup_checkpoint_file_name,opstat)
        
            if(opstat.get_status()) :
        
                if(GEOCODE_THREAD_DEBUG)  :   
                    cfg.add_debug_to_log("checkpoint_results"," : write to csv : " + str( self.last_checkpoint_rowid))
                
                try :
                
                    df = self.geocodingResults.get_geocoding_results_df() 
                    checkpoint_df   =   df.iloc[start_row_id:(len(df))] 
                    checkpoint_df   =   checkpoint_df.sort_values('source_df_rowid')
                    checkpoint_df.to_csv(chckpt_file_name,index=False)
                    self.last_checkpoint_rowid  =   len(df)
            
                except Exception as e: 
                    opstat.store_exception("Unable to export to csv file " + chckpt_file_name,e)
                    if(GEOCODE_THREAD_DEBUG)  :
                        cfg.add_debug_to_log("Unable to export to csv file",str(sys.exc_info()[0].__name__))
                    
                    self.last_checkpoint_rowid  =   len(df)                        
                        
            else :
                if(GEOCODE_THREAD_DEBUG)  :   
                    cfg.add_debug_to_log("checkpoint_results"," : incomplete] : " + str(opstat.get_errorMsg()))
                
                df = self.geocodingResults.get_geocoding_results_df()
                self.last_checkpoint_rowid  =   len(df)
                    
        if(GEOCODE_THREAD_DEBUG)  :   
            cfg.add_debug_to_log("checkpoint_results : complete",str( self.last_checkpoint_rowid))
    
        set_status_bar(CHECKPOINT_COMPLETE)

        
    def get_results_log(self):
        return(self.geocodingResults)
    def get_results_log_count(self):
        if(not(self.geocodingResults is None)) :
            return(self.geocodingResults.get_results_count())
        else :
            return(0)
    def get_error_log(self):
        if(not(self.geocodingErrorLog is None)) :
            return(self.geocodingErrorLog)
        else :
            return(None)
    def get_halt_flag(self):
        return(self.halt_all_geocoding)
    def set_halt_flag(self,fstate):
        if(GEOCODE_TRACE_GET_GEOCODE)  :   
            cfg.add_debug_to_log("set_halt_flag"," : " + str(fstate) + " " + " " + str(self.maxrows)  )
        self.halt_all_geocoding     =   fstate
    def get_geocode_id(self):
        return(self.geocid)
    def get_geocode_type(self):
        return(self.geotype)
    def get_runParms(self):
        return(self.runParms)
        
    def get_geocode_connector(self):
        return(self.geocoder)
    def set_geocode_connector(self,connector):
        self.geocoder = connector
    def get_geocode_maxrows(self):
        return(self.maxrows)
    def get_geocode_checkpoint_interval(self):
        return(self.checkpoint_interval)

    def get_total_run_time(self) :
        if(self.stop_time == 0) :
            self.stop_time =  datetime.datetime.now()
        timedelta   =   self.stop_time  -   self.start_time
        return(timedelta.days * 24 * 3600 + timedelta.seconds)
        
    def get_geocode_lat_long_map(self):
        return(self.lat_long_map )
    
    def get_api_parms(self) :
        return(self.api_parms)
     
    def drop_thread(self,rowid) :
        self.geocodeThreadsMonitor.dropthread(rowid)

"""
#--------------------------------------------------------------------------
#   static geocode runner object
#--------------------------------------------------------------------------
"""    
dfc_Geocode_Runner  =   BulkGeocodeRunner()        






"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Bulk Geocoder display tables methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

ADDRESS_COMPONENTS_TABLE    =   0
LOCATION_TYPES_TABLE        =   1

def display_bulk_splash() :

    bulk_splash_html = """
            <div style="margin-left: 0px">
                <img src="https://rickkrasinski.github.io/dfcleanser/graphics/BulkGeocodeSplash.png" style="width: 820px; height: 100px; ">
            </div>
    """

    from dfcleanser.common.common_utils import displayHTML
    displayHTML(bulk_splash_html)



# """
# --------------------------------------------------------------------------
#   geocoder names table 
# --------------------------------------------------------------------------
# """

start_geocoder_table = """
<table class='geocode-table geocoder-column' width=150px;><th style='text-align:center;' class='geocode-header'>Bulk Geocoders</th>
"""

end_geocoder_table = """
</table>
"""

geocoder_table_row = """
<tr><td class='geocoder-column' onclick="select_bulk_geocoder(XXXGEOID);" style='text-align:left;'>XXXTABCOL</td></tr>
"""

def get_geocoders_table() :

    table_html  =   ""
    table_html  =   table_html + start_geocoder_table

    geocoders   =   ["Bing","Google"]
    geocodeids  =   [2,7]

    for i in range(len(geocoders)) :

        next_row    =   geocoder_table_row.replace("XXXGEOID",str(geocodeids[i])) 
        next_row    =   next_row.replace("XXXTABCOL",str(geocoders[i]))
        table_html  =   table_html + next_row

    table_html  =   table_html + end_geocoder_table

    return(table_html)


# """
# --------------------------------------------------------------------------
#   column names table 
# --------------------------------------------------------------------------
# """

start_table = """
<div class='column_header'>
<table class='geocode-table' width=240px;><th style='text-align:center;' class='geocode-header'>Column Names</th></table>
</div>
<div>
<table class='column-body'>
"""

start_reverse_table = """
<div class='column_header'>
<table class='geocode-table' width=240px;><th style='text-align:center;' class='geocode-header'>Column Names</th></table>
</div>
<div class='column-body-reverse'>
<table class='column-body'>
"""

end_table = """
</table>
</div>
"""

table_row = """
<tr width=240px;><td class='geocode-column'; width=240px; onclick="select_addr_col(XXXGEOID,'XXXTABCOL');" style='text-align:left;'>XXXTABCOL</td></tr>
"""

reverse_table_row = """
<tr width=240px;><td class='geocode-column'; width=240px; onclick="select_lat_lng_col(XXXGEOID,'XXXTABCOL');" style='text-align:left;'>XXXTABCOL</td></tr>
"""

def get_column_names_table(geocodeid,geotype,df) :

    cols    =   df.columns.tolist()

    table_html  =   ""

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
    if(geotype == QUERY) :
        table_html  =   table_html + start_table
    else :
        table_html  =   table_html + start_reverse_table

    for i in range(len(cols)) :

        if(geocodeid == BingId) :
            if(geotype == QUERY) :
                next_row    =   table_row.replace("XXXGEOID","2") 
            else :
                next_row    =   reverse_table_row.replace("XXXGEOID","2") 
        else :
            if(geotype == QUERY) :
                next_row    =   table_row.replace("XXXGEOID","7") 
            else :
                next_row    =   reverse_table_row.replace("XXXGEOID","7")

        next_row    =   next_row.replace("XXXTABCOL",cols[i])
        table_html  =   table_html + next_row

    table_html  =   table_html + end_table

    return(table_html)

# """
# --------------------------------------------------------------------------
#   address components table 
# --------------------------------------------------------------------------
# """

comp_start_table = """
<div class='column_header'>
<table class='geocode-table' width=240px;><th style='text-align:center;' class='geocode-header'>Address Components</th></table>
</div>
<div>
<table class='column-body-addr-comps'>
"""

comp_end_table = """
</table>
</div>
"""

comp_table_row = """
<tr width=240px;><td class='geocode-column'; width=240px; onclick="add_addr_comp('XXXXGEOCODEID','XXXTABCOL');" style='text-align:left;'>XXXTABCOL</td></tr>
"""

def get_address_components_table(geocodeid) :
    """
    * ---------------------------------------------------------
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
    
    acomplist       =   ["street_number", "route", "neighborhood", "locality", "administrative_area_level_1", "administrative_area_level_2", "country", "postal_code"]

    acomplist       =   ["street_number", "route", "neighborhood", "locality", "state", "county", "country", "postal_code"]
    addrcomplist    =   []

    for i in range(len(acomplist)) :
        addrcomplist.append(acomplist[i])

    table_html  =   ""
    table_html  =   table_html + comp_start_table

    for i in range(len(addrcomplist)) :

        next_row    =   comp_table_row.replace("XXXTABCOL",addrcomplist[i])
        next_row    =   next_row.replace("XXXXGEOCODEID",str(geocodeid))
        table_html  =   table_html + next_row

    table_html  =   table_html + comp_end_table

    return(table_html)

# """
# --------------------------------------------------------------------------
#   location types table 
# --------------------------------------------------------------------------
# """

location_start_table = """
<div class='column_header'>
<table class='geocode-table' width=240px;><th style='text-align:center;' class='geocode-header'>Location Types</th></table>
</div>
<div>
<table  class='column-body-loc-types'>
"""

location_end_table = """
</table>
</div>
"""

location_table_row = """
<tr width=240px;><td class='geocode-column'; width=240px; onclick="add_location_type('XXXXGEOCODEID','XXXTABCOL');" style='text-align:left;'>XXXTABCOL</td></tr>
"""


def get_location_types_table(geocodeid) :
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

    loctypeslist    =   ["APPROXIMATE", "GEOMETRIC_CENTER", "RANGE_INTERPOLATED", "ROOFTOP"]

    table_html  =   ""
    table_html  =   table_html + location_start_table

    for i in range(len(loctypeslist)) :

        next_row    =   location_table_row.replace("XXXTABCOL",loctypeslist[i])
        next_row    =   next_row.replace("XXXXGEOCODEID",str(geocodeid))
        table_html  =   table_html + next_row

    table_html  =   table_html + location_end_table

    return(table_html)

from dfcleanser.sw_utilities.DisplayUtils import get_status_note_msg_html

msg                     =   "Click on a column in the 'Column Names' table to choose the dataframe_lat_long_column_names field."
geocode_note_html       =   get_status_note_msg_html(msg, width=540, left=20, fontsize=12, display=False)
msg1                    =   "Click on a value in the 'Adress Components' table to build the address_components_list field."
geocode_note1_html      =   get_status_note_msg_html(msg1, width=540, left=20, fontsize=12, display=False)
msg2                    =   "Click on a value in the 'Location Types' table to build the location_types_list field."
geocode_note2_html      =   get_status_note_msg_html(msg2, width=540, left=20, fontsize=12, display=False)

geocode_google_reverse_notes_html      =   geocode_note_html + geocode_note1_html + geocode_note2_html


# """
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#   bulk run oarameters
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# """

bulk_parms_start_table = """
<div class='column_header' style='margin-left:65px;'>
<table class='geocode-table' width=600px;><th style='text-align:center;' class='geocode-header'>Bulk Geocode XXXOPTYPE Run Parameters</th></table>
</div>
<div class='column-body-loc-types' style='margin-left:65px;'>
<table>
"""

bulk_parms_end_table = """
</table>
</div>
"""

bulk_parms_table_row = """
<tr width=600px;>
  <td class='geocode-column'; width=300px; style='text-align:left;'>XXXPARMNAME</td>
  <td class='geocode-column'; width=300px; style='text-align:left;'>XXXPARMVALUE</td>
</tr>
"""

bulk_parms_error_table_row = """
<tr width=600px;>
  <td class='geocode-column'; width=300px; style='text-align:left;'>XXXPARMNAME</td>
  <td class='geocode-error-column'; width=300px; style='text-align:left;'>XXXPARMVALUE</td>
</tr>
"""

def get_bulk_parms_table(geocodeid,geotype,runparms,opstat) :
    """
    * --------------------------------------------------------
    * function : get table of bulk geocoding parms
    * 
    * parms :
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY

    if(DEBUG_GEOCODE_BULK_UTILS)  :
        cfg.add_debug_to_log("get_bulk_parms_table",str(geocodeid) + str(geotype) + "\n  " + str(runparms))

    table_html  =   ""
    table_html  =   table_html + bulk_parms_start_table
    if(geotype == QUERY) :
        table_html  =   table_html.replace("XXXOPTYPE","Query") 
    else :
        table_html  =   table_html.replace("XXXOPTYPE","Reverse")   
    
    from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_bing_query_input_labelList, bulk_bing_reverse_input_labelList, 
                                                         bulk_google_query_input_labelList, bulk_google_reverse_input_labelList)
    from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_bing_query_input_idList, bulk_bing_reverse_input_idList, 
                                                         bulk_google_query_input_idList, bulk_google_reverse_input_idList)

    if(geocodeid == BingId) :

        if(geotype == QUERY) :
            labellist   =   bulk_bing_query_input_labelList[:len(bulk_bing_query_defaults)]
            idlist      =   bulk_bing_query_input_idList[:len(bulk_bing_query_defaults)]
            required    =   bulk_bing_query_required
        else :
            labellist   =   bulk_bing_reverse_input_labelList[:len(bulk_bing_reverse_defaults)]
            idlist      =   bulk_bing_reverse_input_idList[:len(bulk_bing_reverse_defaults)]
            required    =   bulk_bing_reverse_required
    else :

        if(geotype == QUERY) :
            labellist   =   bulk_google_query_input_labelList[:len(bulk_google_query_defaults)]
            idlist      =   bulk_google_query_input_idList[:len(bulk_google_query_defaults)]
            required    =   bulk_google_query_required
        else :
            labellist   =   bulk_google_reverse_input_labelList[:len(bulk_google_reverse_defaults)]
            idlist      =   bulk_google_reverse_input_idList[:len(bulk_google_reverse_defaults)]
            required    =   bulk_google_reverse_required
    
    parmids     =   []
    parmvals    =   []

    for i in range(len(labellist)) :
        parmids.append(labellist[i])
        parmvals.append(runparms.get(labellist[i]))

    good_labels     =   []
    final_vals      =   []

    for i in range(len(parmids)) :

        good_labels.append(parmids[i])
        if( (parmids[i] is None) or (len(parmids[i]) == 0) ) : 
            if(i in required) :
                final_vals.append("Error : Parm is Required")
            else :
                final_vals.appen(get_bulk_default_parm(geocodeid,geotype,i))
        
        else :

            final_vals.append(parmvals[i])

    for i in range(len(good_labels)) :
        
        if(final_vals[i] == "Error : Parm is Required") :
            next_row    =   bulk_parms_error_table_row.replace("XXXPARMNAME",good_labels[i])
            next_row    =   next_row.replace("XXXPARMVALUE",str(final_vals[i]))
        else :
            next_row    =   bulk_parms_table_row.replace("XXXPARMNAME",good_labels[i])
            next_row    =   next_row.replace("XXXPARMVALUE",str(final_vals[i]))
        
        table_html  =   table_html + next_row
 

    table_html  =   table_html + bulk_parms_end_table

    return(table_html)



bulk_google_query_defaults      =   [None,None,None,None,None,"english","ALL",False,"len(df)",2,10000]
bulk_google_query_required      =   [0,1,2]

bulk_google_reverse_defaults    =   [None,None,None,True,None,"ALL","english","len(df)",2,10000]
bulk_google_reverse_required    =   [0,1,2,4]

bulk_bing_query_defaults        =   [None,None,None,None,None,"US",False,False,"len(df)",2,10000]
bulk_bing_query_required        =   [0,1,2]

bulk_bing_reverse_defaults      =   [None,None,None,"US",False,"len(df)",2,10000]
bulk_bing_reverse_required      =   [0,1]


def get_bulk_default_parm(geocodeid,geotype,parm_offset) :
    """
    * -------------------------------------------------------- 
    * function : get default values of parms not entered
    * 
    * parms :
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY

    if(DEBUG_GEOCODE_BULK_UTILS)  :
        cfg.add_debug_to_log("get_bulk_default_parm",str(geocodeid) + str(geotype) + str(parm_offset))

    if(geocodeid == BingId) :

        if(geotype == QUERY) :

            defaults    =   bulk_bing_query_defaults
            required    =   bulk_bing_query_required 

        else :

            defaults    =   bulk_bing_reverse_defaults
            required    =   bulk_bing_reverse_required 

    else :

        if(geotype == QUERY) :

            defaults    =   bulk_google_query_defaults
            required    =   bulk_google_query_required 

        else :

            defaults    =   bulk_google_reverse_defaults
            required    =   bulk_google_reverse_required 
    
    if(DEBUG_GEOCODE_BULK_UTILS)  :
        cfg.add_debug_to_log("get_bulk_default_parm"," defaults : " + str(defaults))

    default_value   =   defaults[parm_offset]

    if(default_value is None) :
        if(parm_offset in required) :
            default_value   =   "Error : parm must be entered"

    return(default_value)




"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Dataframe Describe Table components 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

new_line =   """
"""

def addstyleattribute(name,value) :
    """
    * -------------------------------------------------------------------------- 
    * function : add style attribute
    * 
    * parms :
    *   namw        -   style attribute name
    *   value       -   style attribute value 
    *
    * returns : 
    *  html style attribute
    * --------------------------------------------------------
    """
    
    styleattribute = ""
    styleattribute = styleattribute + " " + name + ":" + value + "; "
    return(styleattribute)




"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table html 
* -----------------------------------------------------------------------*
"""

table_head_end = """
                </thead>"""

mini_table_start = """
                            <div container dc-tbl-container" style='border:0px; """
mini_table_end = """                            </div>
"""

mini_panel_start = """                                <div class="panels panel-primary" style="border:0px;">"""
mini_panel_end   = """                                </div>
"""

mini_panel_heading_start = """
                                    <div class="panel-heading clearfix dc-describe-table-panel-heading" style="background-color: rgb(61, 126, 216);">
                                        <div class="input-group-btn">"""
mini_panel_heading_end = """                                        </div>
                                    </div>"""

mini_panel_title_start = """
                                            <p class="panel-title dc-describe-table-panel-title pull-left">"""

mini_data_table_start = """
                                    <div>
                                        <table class="table">"""
mini_data_table_end = """
                                        </table>
                                    </div>
"""

mini_table_head_start = """
                                            <thead>
                                                <tr class="dc-describe-table-head">
"""
describe_df_table_head_start = """
                                            <thead>
                                                <tr class="dc-describe-table-head">
"""
mini_table_head_end = """                                                </tr>
                                            </thead>"""
                                            
mini_table_head_col_start = """                                                    <th class=" dccolhead dc-describe-table-head-col">"""
describe_df_table_head_col_start = """                                                    <th class=" dccolhead dc-describe-table-head-col">"""

mini_data_table_body_start = """
                                            <tbody>"""
mini_data_table_body_end = """
                                            </tbody>"""

mini_data_table_body_row_start = """
                                                <tr class='dc-describe-table-body-row'>"""
describe_df_table_body_row_start = """
                                                <tr class='dc-describe-table-body-row'>"""
mini_data_table_body_row_end = """
                                                </tr>"""

describe_df_table_body_first_col = """
                                                    <td class="dctablecol dccolwrap dc-describe-table-body-first-col">"""
describe_df_table_body_col = """
                                                    <td class="dctablecol dccolwrap">"""
mini_data_table_body_col = """
                                                    <td class="dctablecol dccolwrap">"""

"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table methods 
* -----------------------------------------------------------------------*
"""
def get_stats_table(title,colnames,colvalues,width=0) : 
    
    stats_HTML  =   ""
    
    if(width==0) :
        stats_HTML  =   (stats_HTML + mini_table_start + "'>" + new_line)
    else :
        stats_HTML  =   (stats_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "'>" + new_line)

    stats_HTML  =   (stats_HTML + mini_panel_start)

    stats_HTML  =   (stats_HTML + mini_panel_heading_start)
    stats_HTML  =   (stats_HTML + mini_panel_title_start)
    stats_HTML  =   (stats_HTML + title + "</p>" + new_line)
    stats_HTML  =   (stats_HTML + mini_panel_heading_end)

    stats_HTML  =   (stats_HTML + mini_data_table_start)

    # table head
    stats_HTML  =   (stats_HTML + mini_table_head_start)
    for i in range(len(colnames)) :
        stats_HTML  =   (stats_HTML + mini_table_head_col_start + str(colnames[i]) + "</th>" + new_line)
    stats_HTML  =   (stats_HTML + mini_table_head_end)

    # table body
    stats_HTML  =   (stats_HTML + mini_data_table_body_start)
    stats_HTML  =   (stats_HTML + mini_data_table_body_row_start)   
    for i in range(len(colvalues)) :
        stats_HTML  =   (stats_HTML + mini_data_table_body_col + str(colvalues[i]) + "</td>")   
    stats_HTML  =   (stats_HTML + mini_data_table_body_row_end)

    stats_HTML  =   (stats_HTML + mini_data_table_body_end)
    
    stats_HTML  =   (stats_HTML + mini_data_table_end)
    
    stats_HTML  =   (stats_HTML + mini_panel_end)
    stats_HTML  =   (stats_HTML + mini_table_end)

    return(stats_HTML)
    
"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table methods 
* -----------------------------------------------------------------------*
"""
def get_df_describe_table(df_title,df,rowids,colids,width=0,centered=False) : 

    df_describe_HTML  =   ""
    
    if(width==0) :
        if(centered) :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + "' align='center' >" + new_line)
        else :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + "'>" + new_line)
    else :
        if(centered) :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "' align='center' >" + new_line)
        else :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "'>" + new_line)
        
    df_describe_HTML  =   (df_describe_HTML + mini_panel_start)

    df_describe_HTML  =   (df_describe_HTML + mini_panel_heading_start)
    df_describe_HTML  =   (df_describe_HTML + mini_panel_title_start)
    df_describe_HTML  =   (df_describe_HTML + df_title + " dataframe : " +  str(len(df)) + " Rows x " + str(len(df.columns)) + " Columns" + "</p>" + new_line)
    df_describe_HTML  =   (df_describe_HTML + mini_panel_heading_end)

    df_describe_HTML  =   (df_describe_HTML + mini_data_table_start)
    
    # table head
    df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_start)
    
    colnames          =   list(df.columns)
    
    for i in range(len(colids)) :
        if(colids[i] == None) :
            df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + "........" + "</th>" + new_line) 
        else :
            if(colids[i] == -1) :
                df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + "row index" + "</th>" + new_line)
            else :
                df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + str(colnames[colids[i]]) + "</th>" + new_line)
                               
    df_describe_HTML  =   (df_describe_HTML + table_head_end)

    # table body
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_start)
    
    for i in range(len(rowids)) :
        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_row_start)   
        
        for j in range(len(colids)) :
        
            if(j == 0) :
                
                if(rowids[i] == None) :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_first_col + "........" + "</td>") 
                else :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_first_col + str(rowids[i]) + "</td>")    
            
            else :
                if(rowids[i] == None) :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + "........" + "</td>")
                else :
                
                    if(colids[j] == None) :
                        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + "........" + "</td>") 
                    else :
                        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + str(df.iloc[rowids[i],colids[j]]) + "</td>")   
            
        df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_row_end)
        
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_end)

    
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_end)

    df_describe_HTML  =   (df_describe_HTML + mini_panel_end)
    df_describe_HTML  =   (df_describe_HTML + mini_table_end)

    return(df_describe_HTML)



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
 
    from dfcleanser.Qt.Geocode.BulkGeocode import (google_bulk_geocoder_id, bing_bulk_geocoder_id, bulk_google_query_input_id,
                                                   bulk_bing_query_input_id, bulk_google_reverse_input_id, bulk_bing_reverse_input_id)
    if(gtype == GEOCODER)  :
        if(geocid == GoogleId)           : return(google_bulk_geocoder_id)
        elif(geocid == BingId)           : return(bing_bulk_geocoder_id)
         
    elif(gtype == QUERY)  :
        if(geocid == GoogleId)           : return(bulk_google_query_input_id)
        elif(geocid == BingId)           : return(bulk_bing_query_input_id)
         
    elif(gtype == REVERSE)  :
         if(geocid == GoogleId)            : return(bulk_google_reverse_input_id)
         if(geocid == BingId)              : return(bulk_bing_reverse_input_id)



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
    
    def __init__(self, colnames,colvalues,df):
        
        self.colNames       =   colnames
        self.colValues      =   colvalues
        self.colIndices     =   [] 
        
        df_colnames         =   df.columns.values.tolist() 
        
        for i in range(len(self.colNames)) :

            if(self.colNames[i] == -1) :
                self.colIndices.append(-1)    
            else :
                for j in range(len(df_colnames)) :
                    if(self.colNames[i] == df_colnames[j]) :
                        self.colIndices.append(j)
        
    def get_colindices(self): 
        return(self.colIndices)
    
    def get_colValues(self): 
        return(self.colValues)

def get_address_map(dftitle,address_cols) : 
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
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
        cfg.add_debug_to_log("get_address_map"," dftitle : address_cols "  + str(dftitle) + " : " + str(address_cols) )

    am_colNames     =   []
    am_colValues    =   []
    
    address_cols        =   address_cols.replace(","," ")
    address_components  =   address_cols.split("+")

    if(GEOCODE_TRACE_GET_GEOCODE_LOAD) :
        cfg.add_debug_to_log("get_address_map"," : address_components " + str(address_components))
    
    for i in range(len(address_components)) :
        address_components[i]   =   address_components[i].lstrip(" ")
        address_components[i]   =   address_components[i].rstrip(" ")

    df          =   cfg.get_dfc_dataframe_df(dftitle)    
    colnames    =   df.columns.values.tolist() 

    for i in range(len(address_components)) :

        address_components[i]    =   address_components[i].replace("'","")

        if(address_components[i] in colnames) :
            am_colNames.append(address_components[i])
            am_colValues.append(None)
        else :
            am_colNames.append(-1)
            am_colValues.append(address_components[i])

        if(GEOCODE_TRACE_GET_GEOCODE_LOAD) :
            cfg.add_debug_to_log("get_address_map"," : colNames " + str(am_colNames))
            cfg.add_debug_to_log("get_address_map"," : colValues " + str(am_colValues))

    addressMap  =    AddressMap(am_colNames,am_colValues,df)       

    return(addressMap)


def get_lat_longs_map(geocid,runParms) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get lat_long indices object from lat long cols input parms
    * 
    * parms :
    *  address_cols       - address column names input parm
    *
    * returns : 
    *  address vector of names and name types
    * --------------------------------------------------------
    """
            
    #from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_google_reverse_input_labelList, bulk_bing_reverse_input_labelList)
        
    if(geocid   ==  GoogleId) :
            
        df_name         =   runParms.get("dataframe_to_geocode_from") 
        lat_lng_cols    =   runParms.get("dataframe_lat_long_column_name(s)")
            
    elif(geocid   ==  BingId) :
            
        df_name         =   runParms.get("dataframe_to_geocode")
        lat_lng_cols    =   runParms.get("dataframe_lat_long_column_name(s)")
        
    df_title    =   df_name
    df          =   cfg.get_dfc_dataframe_df(df_title)    
    colnames    =   df.columns.values.tolist() 
            
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
        cfg.add_debug_to_log("get_lat_longs_map","  : df_name : " + str(df_name) + " lat_lng_cols : " + str(lat_lng_cols) + " : " + str(len(lat_lng_cols))) 
                
    if(lat_lng_cols.find("+") > -1) :
        lat_lng_cols_list   =  lat_lng_cols.split(" + ")
    else :
        lat_lng_cols_list   =  lat_lng_cols

    colnames    =   list(df.columns)
    
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
        cfg.add_debug_to_log("get_lat_longs_map","  : lat_lng_cols_list : " + str(lat_lng_cols_list) + " : " + str(type(lat_lng_cols_list))) 
            
    lat_long_col_indices    =   []

    if(type(lat_lng_cols_list) == list) :

        for i in range(len(lat_lng_cols_list)) :
            for j in range(len(colnames)) :
    
                if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
                    cfg.add_debug_to_log("get_lat_longs_map","  : colnames : " + str(colnames[j])  + str(len(colnames[j]))) 

                if(lat_lng_cols_list[i] == colnames[j]) :
                    lat_long_col_indices.append(j)

    else :

        for j in range(len(colnames)) :   
            if(lat_lng_cols_list == colnames[j]) :
                    lat_long_col_indices.append(j)
                    break
                
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :  
        cfg.add_debug_to_log("get_lat_longs_map","  :  lat_long_col_indices : " + str(lat_long_col_indices)) 
                
    return(lat_long_col_indices)


def get_geocode_address_string(geocid,runparms,address_map,rowIndex) : 
    """
    * ------------------------------------------------------------
    * 
    * parms :
    *  address_vector   - address vector of names and name types
    *  rowIndex         - dataframe row index
    *
    * returns : 
    *  address string to feed geocoder
    * ------------------------------------------------------------
    """

    import pandas as pd    
    geocode_address     =   ""

    if(geocid   ==  GoogleId) :
        df_name     =   runparms.get("dataframe_to_geocode_from") 
        
    elif(geocid   ==  BingId) :
        df_name     =   runparms.get("dataframe_to_geocode") 
        
    df  =   cfg.get_dfc_dataframe_df(df_name)
    
    map_col_inidices    =  address_map.get_colindices() 
    
    for i in range(len(map_col_inidices)) :
        
        if(not (map_col_inidices[i] == -1) ) :
            addr_comp   =   df.iloc[rowIndex,map_col_inidices[i]]
                        
            if(not ( (pd.isna(addr_comp)) or 
                     (addr_comp is None) ) ) :           
                geocode_address     =   geocode_address + str(addr_comp) + " "
        else :
            geocode_address     =   geocode_address + address_map.get_colValues()[i] + " "
     
    if(GEOCODE_TRACE_GET_GEOCODE_DETAILS) :
        cfg.add_debug_to_log("get_geocode_address_string"," address : " + str(geocode_address))
           
    return(geocode_address)


def get_geocode_reverse_lat_lng_string(geocid,runparms,rowIndex) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get lat,lng string from address cols input parms
    * 
    * parms :
    *  runparms   - reverse run parms
    *  rowIndex   - dataframe row index
    *
    * returns : 
    *  address string to feed geocoder
    * --------------------------------------------------------
    """
    
    if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
        cfg.add_debug_to_log("get_geocode_reverse_lat_lng_string"," : geocid " + str(geocid) + " rowid " + str(rowIndex))  
        cfg.add_debug_to_log("get_geocode_reverse_lat_lng_string"," : runparms " + str(runparms))
        
    try : 
        
        if(geocid   ==  GoogleId) :
            df_name         =   runparms.get("dataframe_to_geocode_from") 
            
        elif(geocid   ==  BingId) :
            df_name         =   runparms.get("dataframe_to_geocode")
        
        df  =   cfg.get_dfc_dataframe_df(df_name)

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_geocode_lat_long_map
        lat_lng_cols_list   =   get_geocode_lat_long_map() 
        
        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
            cfg.add_debug_to_log("get_geocode_reverse_lat_lng_string"," : lat_lng_cols_list " + str(lat_lng_cols_list) + " len : " + str(len(lat_lng_cols_list)))  
        
        if(len(lat_lng_cols_list) == 1) :
        
            df_lat_lng          =   df.iloc[rowIndex,lat_lng_cols_list[0]]
            
            df_lat_lng          =   df_lat_lng.replace("[","")
            df_lat_lng          =   df_lat_lng.replace("[","")
            df_lat_lng          =   df_lat_lng.replace("(","")
            df_lat_lng          =   df_lat_lng.replace(")","")
            df_lat_lng_list     =   df_lat_lng.split(",")
            df_lat              =   df_lat_lng_list[0]
            df_lng              =   df_lat_lng_list[1]
        
        else :
            
            df_lat              =   df.iloc[rowIndex,lat_lng_cols_list[0]]
            df_lng              =   df.iloc[rowIndex,lat_lng_cols_list[1]]
            
    except :
        if(GEOCODE_TRACE_GET_GEOCODE)  :   
            cfg.add_debug_to_log("get_geocode_reverse_lat_lng_string exception"," : "  + str(sys.exc_info()[0].__name__))
        return(None)         
    
    lat_lng     =   "[" + str(df_lat) + "," + str(df_lng) + "]" 

    return(lat_lng)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console widgets methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding console key bar
#--------------------------------------------------------------------------
"""

START_KEY       =   0
STOP_KEY        =   1
PAUSE_KEY       =   2
RESUME_KEY      =   3
CHKPT_KEY       =   4
PARMS_KEY       =   5
RESULTS_KEY     =   6

ENABLE          =   0
DISABLE         =   1

ENABLE_COLOR    =   "#0275d8"
DISABLE_COLOR   =   "#ccddff"


def control_bulk_keys(action_list,trace=None) :
    
    if(GEOCODE_TRACE_GET_GEOCODE)  :  
        if(trace is None)  :
            cfg.add_debug_to_log("control_bulk_keys",str(action_list) )
        else :
            cfg.add_debug_to_log("control_bulk_keys","[" + str(trace) + "] " + str(action_list) )
    
    for i in range(len(action_list)) :
        if(not (action_list[i] is None) ) :
            if(i ==0 )      :   control_bulk_key(START_KEY,action_list[i]) 
            elif(i == 1)    :   control_bulk_key(STOP_KEY,action_list[i]) 
            elif(i == 2)    :   control_bulk_key(PAUSE_KEY,action_list[i]) 
            elif(i == 3)    :   control_bulk_key(RESUME_KEY,action_list[i]) 
            elif(i == 4)    :   control_bulk_key(CHKPT_KEY,action_list[i])
            elif(i == 5)    :   control_bulk_key(PARMS_KEY,action_list[i])
            else            :   control_bulk_key(RESULTS_KEY,action_list[i])

def control_bulk_key(keyid,action) :

    if(keyid == START_KEY) :        bid     =   "dfc_start"
    elif(keyid == STOP_KEY) :       bid     =   "dfc_stop"
    elif(keyid == PAUSE_KEY) :      bid     =   "dfc_pause"
    elif(keyid == RESUME_KEY) :     bid     =   "dfc_resume"
    elif(keyid == CHKPT_KEY) :      bid     =   "dfc_checkpoint"
    elif(keyid == PARMS_KEY) :      bid     =   "dfc_run_parms"
    elif(keyid == RESULTS_KEY) :    bid     =   "dfc_process"
    
    if(action == ENABLE) :
        key_state   =   "false"
        key_color   =   ENABLE_COLOR
    else :
        key_state   =   "true"
        key_color   =   DISABLE_COLOR
        
    change_color_js     =   "$('#" + bid + "').css('background-color','" + key_color + "');"
    disable_click_js    =   "$('#" + bid + "').prop('disabled'," + key_state + ");"
    
    from dfcleanser.common.common_utils import  run_jscript
    run_jscript(change_color_js,"fail to change button color")
    run_jscript(disable_click_js,"fail to disanle click")


def set_status_bar(state) :
    """
    * -------------------------------------------------------
    * function : set geocode status banner
    * 
    * parms :
    *  state   - geocoding state
    *
    * returns : 
    *  NA
    * --------------------------------------------------------
    """
    
    change_state_js = ("$('#geocodeconsolestateId').attr('src'," + "'" + get_status_bar_image(state) + "'" + ");")
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(change_state_js,"fail to change console state : ")


geocode_results_bar_text     =   "Total Addresses Geocoded &nbsp;&nbsp;&nbsp;: &nbsp;"
reverse_results_bar_text     =   "Total Locations Geocoded &nbsp;&nbsp;&nbsp;: &nbsp;"
errors_bar_text              =   "Total Geocode Errors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;"


def set_progress_bar_value(geocid,geotype,barid,countvalue,barvalue) :
    """
    * -------------------------------------------------------
    * function : update status bars
    * 
    * parms :
    *  geocid   - geocoder id
    *  barid    - progress bar id
    *  barvalue - bar value
    *
    * returns : 
    *  progress bar updated
    * --------------------------------------------------------
    """

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import (QUERY, BingId, GoogleId)
    
    if(geocid == GoogleId) :

        if(barid == GEOCODE_BAR)   :   
            bid         =   "bgqbulknumberlimit"
            countid     =   "geocodeaddresses"
            if(geotype == QUERY) :
                bhtml       =   geocode_results_bar_text + str(countvalue)
            else :
                bhtml       =   reverse_results_bar_text + str(countvalue)
        else                            :   
            bid         =   "bgqbulkfailurelimit"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)
            
    elif(geocid == BingId) :

        if(barid == GEOCODE_BAR)   :   
            
            countid     =   "geocodeaddresses"
            
            if(geotype == QUERY) :
                
                bhtml       =   geocode_results_bar_text + str(countvalue)
                bid         =   "bbqbulknumberlimit"
                
            else :
                
                bhtml       =   reverse_results_bar_text + str(countvalue)
                bid         =   "bbrbulknumberlimit"
                
        else                            :   
            bid         =   "bbrbulknumberlimit"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)
            

    if(barid == GEOCODE_BAR) :
        
        try :
            from dfcleanser.common.common_utils import run_jscript
            set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
            run_jscript(set_progress_bar_js,"fail to set progress bar : ")
        
        except :

            #TODOD
        
            cfg.add_debug_to_log("set_progress_bar_value exception ","") 
    
    from dfcleanser.common.common_utils import run_jscript
    set_progress_count_js = "$('#" + countid + "').html('" + bhtml +"');"
    run_jscript(set_progress_count_js,"fail to set count value : ")

def get_status_bar_image(state) :
    """
    * -------------------------------------------------------
    * function : set the geocode console state
    * 
    * parms :
    *  state   - state to change to
    *
    * returns : 
    *  state html updated
    * --------------------------------------------------------
    """
    from dfcleanser.common.common_utils import  (GEOCODE_STARTING_IMAGE, GEOCODE_RUNNING_IMAGE, GEOCODE_STOPPED_IMAGE, GEOCODE_FINISHED_IMAGE, GEOCODE_PAUSED_IMAGE,
                                                GEOCODE_STOPPING_IMAGE, GEOCODE_PAUSING_IMAGE, GEOCODE_ERROR_LIMIT_IMAGE, GEOCODE_CHECKPOINT_STARTED_IMAGE, 
                                                GEOCODE_CHECKPOINT_COMPLETE_IMAGE)
    
    from dfcleanser.common.common_utils import get_image_url
    if(state == STARTING) : 
        image   =   get_image_url(GEOCODE_STARTING_IMAGE)
    elif(state == RUNNING) : 
        image   =   get_image_url(GEOCODE_RUNNING_IMAGE)
    elif(state == STOPPED) :
        image   =   get_image_url(GEOCODE_STOPPED_IMAGE)
    elif(state == FINISHED) :
        image   =   get_image_url(GEOCODE_FINISHED_IMAGE)
    elif(state == PAUSED) :
        image   =   get_image_url(GEOCODE_PAUSED_IMAGE)
    elif(state == STOPPING) :
        image   =   get_image_url(GEOCODE_STOPPING_IMAGE)
    elif(state == PAUSING) :
        image   =   get_image_url(GEOCODE_PAUSING_IMAGE)
    elif(state == ERROR_LIMIT) :
        image   =   get_image_url(GEOCODE_ERROR_LIMIT_IMAGE)
    elif(state == CHECKPOINT_STARTED) :
        image   =   get_image_url(GEOCODE_CHECKPOINT_STARTED_IMAGE)
    elif(state == CHECKPOINT_COMPLETE) :
        image   =   get_image_url(GEOCODE_CHECKPOINT_COMPLETE_IMAGE)
        
    return(image)



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

MAX_RESULTS_CACHED                  =   1000

class BulkGeocodeResults:
    
    geocode_results_df      =   None
    geocode_results_list    =   []
    geocoderid              =   None
    geotype                 =   None
    max_geocodes            =   0
    column_headers_list     =   []
    last_percent            =   0
    bulk_results_finished   =   False

    rows_completed_list     =   []
    
    def __init__(self,geocid,geotype,maxgeocodes,column_headers,dftitle=None):
        
        if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
            cfg.add_debug_to_log("__init__ BulkGeocodeResults"," : " + str(geocid) + " " + str(geotype) + " " + str(maxgeocodes))
            cfg.add_debug_to_log("__init__ BulkGeocodeResults"," : column headers : " + str(column_headers))
        
        #self.column_headers         =   column_headers
        self.geocoderid             =   geocid 
        self.geotype                =   geotype 
        self.max_geocodes           =   maxgeocodes 
        self.geocode_results_list   =   []
        self.column_headers_list    =   column_headers
        self.bulk_results_finished  =   False
        
        
        for i in range(len(self.column_headers_list)) :
            self.column_headers_list[i]     =   self.column_headers_list[i].lstrip(" ") 
            self.column_headers_list[i]     =   self.column_headers_list[i].rstrip(" ")
            if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
                cfg.add_debug_to_log("column_headers_list[i] : ",str(i) + " : " + str(self.column_headers_list[i]))
        
        if(dftitle == None) :
            
            import pandas as pd
            self.geocode_results_df =   pd.DataFrame(columns=self.column_headers_list)
            
            if( (self.geocoderid == GoogleId) or (self.geocoderid == ArcGISId) ) :
                
                import numpy as np
                if(len(self.column_headers_list) == 4) :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : str,
                                                                                 self.column_headers_list[2] : str,
                                                                                 self.column_headers_list[3] : str})
                else :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : str,
                                                                                 self.column_headers_list[2] : np.float64,
                                                                                 self.column_headers_list[3] : np.float64,
                                                                                 self.column_headers_list[4] : str})
    
            elif(self.geocoderid == BingId) :
                
                import numpy as np
                if(len(self.column_headers_list) == 2) :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : str})
                else :
                    self.geocode_results_df  =   self.geocode_results_df.astype({self.column_headers_list[0] : np.int64,
                                                                                 self.column_headers_list[1] : np.float64,
                                                                                 self.column_headers_list[2] : np.float64})

            cfg.add_df_to_dfc(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df,"",GEOCODING_RESULTS_DF_NOTES)
            cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)

        else :
            self.geocode_results_df  = cfg.get_dfc_dataframe_df(dftitle)

    def add_result(self,rowid,georunParms,geocodeResults,opstat) :
        """
        * -------------------------------------------------------
        * function : add geocode results to the results df
        * 
        * parms :
        *  rowResults       - row results
        *  opstat           - opstatus
        *  split_lat_lng    - bar value
        *
        * returns : 
        *  progress bar updated
        * --------------------------------------------------------
        """
        
        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :
            cfg.add_debug_to_log("add_result","[start] len(df) : len(result_list) : " + str(len(self.geocode_results_df)) + " : " + str(len(self.geocode_results_list)))

        try :
            
            if(self.load_results()) :

                new_row_results     =   []

                if(georunParms[0] == GM.QUERY) :

                    if(georunParms[1] == GM.GoogleId) :

                        lat_lng_merged  =   georunParms[3]

                        if(not (lat_lng_merged)) :

                            new_row_results.append(geocodeResults.get_row_Id())
                            new_row_results.append(georunParms[2])
                            merged_lat_lng  =    [geocodeResults.get_lat(),geocodeResults.get_lng()]
                            new_row_results.append(str(merged_lat_lng))
                            new_row_results.append(geocodeResults.get_formatted_address())       
                            self.geocode_results_list.append(tuple(new_row_results))

                        else :

                            new_row_results.append(geocodeResults.get_row_Id())
                            new_row_results.append(georunParms[2])
                            new_row_results.append(str(geocodeResults.get_lat()))
                            new_row_results.append(str(geocodeResults.get_lng()))
                            new_row_results.append(geocodeResults.get_formatted_address())       
                            self.geocode_results_list.append(tuple(new_row_results))

                    elif(georunParms[1] == GM.BingId) :

                        lat_lng_merged  =   georunParms[3]

                        if( not (lat_lng_merged)) :

                            new_row_results.append(geocodeResults.get_row_Id())
                            new_row_results.append(georunParms[2])
                            merged_lat_lng  =    [geocodeResults.get_lat(),geocodeResults.get_lng()]
                            new_row_results.append(str(merged_lat_lng))
                            new_row_results.append(geocodeResults.get_full_address())       
                            self.geocode_results_list.append(tuple(new_row_results))

                        else :

                            new_row_results.append(geocodeResults.get_row_Id())
                            new_row_results.append(georunParms[2])
                            new_row_results.append(str(geocodeResults.get_lat()))
                            new_row_results.append(str(geocodeResults.get_lng()))
                            new_row_results.append(geocodeResults.get_full_address())       
                            self.geocode_results_list.append(tuple(new_row_results))
                        
                    if(GEOCODE_TRACE_ADD_RESULT)  :   
                        cfg.add_debug_to_log("add_result","[end] len(df) : len(result_list) : " + str(len(self.geocode_results_df)) + " : " + str(len(self.geocode_results_list)))
                        self.rows_completed_list.append(rowid)

                else : #REVERSE

                    if(georunParms[1] == GM.GoogleId) :

                        if(GEOCODE_TRACE_ADD_RESULT)  :   
                            cfg.add_debug_to_log("add_result"," type geocodeResults : " + str(type(geocodeResults)))
                            cfg.add_debug_to_log("add_result"," georunParms: \n            " + str(georunParms))

                        self.geocode_results_list.append(tuple(geocodeResults))

                        if(GEOCODE_TRACE_ADD_RESULT)  :   
                            cfg.add_debug_to_log("add_result"," geocode_results_list len() : " + str(len(self.geocode_results_list)))


                    elif(georunParms[1] == GM.BingId) :  

                        if(GEOCODE_TRACE_ADD_RESULT)  :   
                            cfg.add_debug_to_log("add_result"," type: " + str(type(geocodeResults)))
                            cfg.add_debug_to_log("add_result"," georunParms: " + str(georunParms))

                        if(georunParms[3] == "Full Address Only") :

                            new_row_results.append(str(geocodeResults.get_row_Id()))
                            new_row_results.append(str(geocodeResults.get_geopoint()))
                            new_row_results.append(str(geocodeResults.get_location())) 

                        else :

                            new_row_results.append(str(geocodeResults.get_row_Id()))
                            new_row_results.append(str(geocodeResults.get_geopoint()))

                            addr_comps  =   geocodeResults.get_location()
                            raw_data    =   addr_comps.raw
                            
                            new_row_results.append(str(raw_data.get("address").get("formattedAddress")))
                            new_row_results.append(str(raw_data.get("address").get("locality")))
                            new_row_results.append(str(raw_data.get("address").get("adminDistrict")))
                            new_row_results.append(str(raw_data.get("address").get("adminDistrict2")))
                            new_row_results.append(str(raw_data.get("address").get("postalCode")))

                            #new_row_results.append(str(geocodeResults.get_location())) 

                        if(GEOCODE_TRACE_ADD_RESULT)  :   
                            cfg.add_debug_to_log("add_result"," new_row_results : " + str(new_row_results))

                        self.geocode_results_list.append(tuple(new_row_results))


            if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :
                self.flush_results_to_dataframe(opstat)
        
            cfg.set_dfc_dataframe_df(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df)

            if(0):#GEOCODE_TRACE_ADD_RESULT)  :   
                cfg.add_debug_to_log("add_result"," done: " + str(len(self.geocode_results_list)) + "\n")
            
        except :

            opstat.set_status(False)
            import sys
            opstat.set_errormsg("[add_result] exception : "  + str(sys.exc_info()[0].__name__))
            if(GEOCODE_TRACE_ADD_RESULT)  :
                cfg.add_debug_to_log("add_result"," exception : " + str(sys.exc_info()[0].__name__))

        
    def flush_results_to_dataframe(self,opstat) :
        
        if(GEOCODE_TRACE_FLUSH_RESULTS)  :   
            cfg.add_debug_to_log("flush_results_to_dataframe"," - df len : " + str(len(self.geocode_results_df)) + " result list len : " + str(len(self.geocode_results_list)))
        
        if(len(self.geocode_results_list) > 0) :
           
            try :
                
                results_df  =   cfg.get_dfc_dataframe_df(GEOCODING_RESULTS_DF_TITLE)
                if(results_df is None) :
                    cfg.add_df_to_dfc(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df,df_source="GEOCODING UTILITY",df_notes="Geocoding Results Dataframe")
                
                import pandas as pd
                import numpy
                
                new_column_headers_list     =  self.column_headers_list

                if(GEOCODE_TRACE_FLUSH_RESULTS)  :   
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.column_headers_list \n         " + str(new_column_headers_list))
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_list len " + str(len(self.geocode_results_list)))
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_list \n        " + str(self.geocode_results_list))

                new_geocode_results     =   pd.DataFrame(self.geocode_results_list,columns=new_column_headers_list)

                if(GEOCODE_TRACE_FLUSH_RESULTS)  :   
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - new_geocode_results : " + " : " + str(len(new_geocode_results)))
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - new_geocode_results " + str(new_geocode_results.columns))
                
                if(GEOCODE_TRACE_FLUSH_RESULTS)  :   
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_df : " + str(type(self.geocode_results_df)) + " : " + str(len(self.geocode_results_df)))
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_df " + str(self.geocode_results_df.columns))

                self.geocode_results_df =   pd.concat([self.geocode_results_df,new_geocode_results],ignore_index=True)
                    
                if(GEOCODE_TRACE_FLUSH_RESULTS)  :   
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_df : type : " + str(type(self.geocode_results_df)) + " : " + str(len(self.geocode_results_df)))
                    cfg.add_debug_to_log("flush_results_to_dataframe"," - self.geocode_results_df : columns : " + str(self.geocode_results_df.columns))
            
                cfg.set_dfc_dataframe_df(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df)
                self.geocode_results_list   =   []
                
            except :
                opstat.set_status(False)
                import sys
                opstat.set_errorMsg("flush_results_to_dataframe Exception : "  + str(sys.exc_info()[0].__name__))
                if(GEOCODE_TRACE_FLUSH_RESULTS)  :
                    cfg.add_debug_to_log("flush_results_to_dataframe",opstat.get_errorMsg())
        
        
    def load_results(self) :
        
        retry_count     =   0
        
        if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :  
            while( (len(self.geocode_results_list) >= MAX_RESULTS_CACHED) and 
                   (retry_count < 20) ) :
                
                retry_count     =   retry_count + 1
                import time
                time.sleep(0.05)
                
        if(len(self.geocode_results_list) >= MAX_RESULTS_CACHED)  :  
            return(False)
        else :
            return(True)
        
        
    def get_results_count(self) :    
        return(len(self.geocode_results_df) + len(self.geocode_results_list))

    def clear_geocoding_results(self) :    
        self.geocode_results_df = None
        cfg.drop_dfc_dataframe(GEOCODING_RESULTS_DF_TITLE)

    def get_geocoding_results_df(self) :    
        return(self.geocode_results_df)

    def add_nan_result(self,rowid,inputparms,parmsDict,opstat) :
        
        if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
            cfg.add_debug_to_log("add_nan_result",str(inputparms))  

        try :
            
            row_result  =   []
            row_result.append(rowid)
            row_result.append(inputparms)
        
            import numpy as np
            for i in range(2,len(self.column_headers_list)) :
            
                if(not (parmsDict is None)) :
                    parmsValue  =   parmsDict.get(self.column_headers_list[i],None)
                else :
                    parmsValue  =   None
            
                if(GEOCODE_TRACE_GET_GEOCODE_DETAILS)  :   
                    cfg.add_debug_to_log("add_nan_result",str(parmsValue))
            
                if(not (parmsValue is None)) :
                    row_result.append(str(parmsValue))    
                else :
                    row_result.append(np.NaN)
            
            self.add_result(row_result)
            
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("add_nan_result Exception : "  + str(sys.exc_info()[0].__name__))
            
        
    def finish_results_log(self,opstat) : 

        if(self.bulk_results_finished):
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                cfg.add_debug_to_log("finish_results_log"," results flushed ")            
            return()
        
        self.bulk_results_finished  =   True
        
        import numpy
        
        if(GEOCODE_TRACE_GET_GEOCODE)  :   
            cfg.add_debug_to_log("finish_results_log",str(self.get_results_count()))
        
        try :
            
            self.flush_results_to_dataframe(opstat)
            df_type_dict                =   {'source_df_rowid':numpy.int64}
            self.geocode_results_df     =   self.geocode_results_df.astype(dtype=df_type_dict,copy=False)
            self.geocode_results_df.sort_values(by=['source_df_rowid'],inplace=True)
            
            self.geocode_results_df.set_index(["source_df_rowid"],drop=False,inplace=True)
            
            cfg.set_dfc_dataframe_df(GEOCODING_RESULTS_DF_TITLE,self.geocode_results_df)
            
        except :
            
            opstat.set_status(False)
            import sys
            opstat.set_errorMsg("[finish_results_log] : "  + str(sys.exc_info()[0].__name__))
            if(GEOCODE_TRACE_GET_GEOCODE)  :   
                cfg.add_debug_to_log("finish_results_log"," excpetion : " + str(sys.exc_info()[0].__name__))            
            

    def get_column_headers_list(self) :
        return(self.column_headers_list)



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding bulk error log class
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
GEOCODING_ERROR_LOG_DF_TITLE            =   "Current_Geocoding_Error_Log_df"
GEOCODING_ERROR_LOG_DF_NOTES            =   "Geocoding Error Logging Dataframe"

GEOCODING_ERROR_LOG_COLUMN_NAME_LIST    =   ['source_df_rowid','geocode_input_value','error_message','Note']

MAX_ERRORS_DISPLAYED                    =   200
ERRORS_TABLE_SIZE                       =   20

MAX_ERRORS_CACHED                       =   200

BULK_GEOCODING_DF_TITLE                 =   "Bulk_Geoooding_Current_df_title"

class BulkGeocodeErrorLog:
    
    error_log_df        =   None
    error_log_list      =   [] 
    error_limit         =   0.0 
    
    def __init__(self,error_limit):
        
        if(GEOCODE_TRACE_PROCESS_ERRORS)  :   
            cfg.add_debug_to_log("__init__  BulkGeocodeErrorLog",str(error_limit))
        
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
        
        import pandas as pd
        self.error_log_df = pd.DataFrame(columns=GEOCODING_ERROR_LOG_COLUMN_NAME_LIST)
        cfg.add_df_to_dfc(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df,"",GEOCODING_ERROR_LOG_DF_NOTES)

        
        self.error_log_list     =   []
        self.error_limit        =   error_limit
        
        if(GEOCODE_TRACE_PROCESS_ERRORS)  : 
            if(self.error_log_df is None) :
                cfg.add_debug_to_log("__init__  BulkGeocodeErrorLog : error_log_df "," : None" + " error_log_list : " + str(len(self.error_log_list)))
            else :
                cfg.add_debug_to_log("__init__  BulkGeocodeErrorLog : error_log_df ", " : " + str(len(self.error_log_df)) + " error_log_list : " + str(len(self.error_log_list)))
        

    def log_error(self,rowindex,inputValue,errorMsg,note,opstat):
               
        if(GEOCODE_TRACE_PROCESS_ERRORS) :
            cfg.add_debug_to_log("log_error"," self.load_errors() " +  str(self.load_errors()))

        if(self.load_errors()) :
            if(note is None) :
                self.error_log_list.append(tuple([rowindex,inputValue,errorMsg," "]))
            else :
                self.error_log_list.append(tuple([rowindex,inputValue,errorMsg,note]))

            
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :
            self.flush_errors_to_dataframe(opstat)


    def flush_errors_to_dataframe(self,opstat) :

        if(GEOCODE_TRACE_PROCESS_ERRORS)  : 
            cfg.add_debug_to_log("flush_errors_to_dataframe","[self.error_log_list] : " + str(type(self.error_log_list)) + " error_count : " + str(len(self.error_log_list)))
            cfg.add_debug_to_log("flush_errors_to_dataframe","[self.error_log_df] : " + str(type(self.error_log_df)) + " error_count : " + str(self.get_error_count()))
        
        try :
            
            if(len(self.error_log_list) > 0) :
                import pandas as pd
                #self.error_log_df = self.error_log_df.concat(pd.DataFrame(self.error_log_list, columns=GEOCODING_ERROR_LOG_COLUMN_NAME_LIST))

                if(GEOCODE_TRACE_PROCESS_ERRORS)  :   
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.column_headers_list " + str(GEOCODING_ERROR_LOG_COLUMN_NAME_LIST))
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.column_headers_list " + str(self.error_log_list))

                new_geocode_erors     =   pd.DataFrame(self.error_log_list,columns=GEOCODING_ERROR_LOG_COLUMN_NAME_LIST)

                if(GEOCODE_TRACE_PROCESS_ERRORS)  :   
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - new_geocode_erors : " + str(type(new_geocode_erors)) + " : " + str(len(new_geocode_erors)))
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - new_geocode_erors " + str(new_geocode_erors.columns))
                
                if(GEOCODE_TRACE_PROCESS_ERRORS)  :   
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.error_log_df : " + str(type(self.error_log_df)) + " : " + str(len(self.error_log_df)))
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.error_log_df " + str(self.error_log_df))

                self.error_log_df =   pd.concat([self.error_log_df,new_geocode_erors],ignore_index=True)
                    
                if(GEOCODE_TRACE_PROCESS_ERRORS)  :   
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.error_log_df : type : " + str(type(self.error_log_df)) + " : " + str(len(self.error_log_df)))
                    cfg.add_debug_to_log("flush_errors_to_dataframe"," - self.error_log_df : columns : " + str(self.error_log_df.columns))

                cfg.set_dfc_dataframe_df(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df)
                self.error_log_list   =   []
                
        except :
            opstat.set_status(False)
            import sys
            opstat.set_errormsg("flush_errors_to_dataframe Exception : "  + str(sys.exc_info()[0].__name__))
        
        
    def load_errors(self) :
        
        retry_count     =   0
        
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :  
            while( (len(self.error_log_list) >= MAX_ERRORS_CACHED) and 
                   (retry_count < 20) ) :
                
                retry_count     =   retry_count + 1
                import time
                time.sleep(0.05)
                
        if(len(self.error_log_list) >= MAX_ERRORS_CACHED)  :  
            return(False)
        else :
            return(True)

 
    def get_error_count(self) : 
        if(self.error_log_df is None) :
            error_log_count     =   0
        else :
            error_log_count     =   len(self.error_log_df)
            
        return(error_log_count + len(self.error_log_list))

    def clear_error_log(self) :    
        self.error_log_df = None
        cfg.drop_dfc_dataframe(GEOCODING_ERROR_LOG_DF_TITLE)
        self.error_log_list     =   []
   
    def get_error_limit(self) :
        return(self.error_limit)
        
    def finish_error_log(self,opstat) :    
        self.flush_errors_to_dataframe(opstat)
        self.error_log_df = self.error_log_df.sort_values("source_df_rowid")
        self.error_log_df.index = range(0,len(self.error_log_df.index))
        cfg.set_dfc_dataframe_df(GEOCODING_ERROR_LOG_DF_TITLE,self.error_log_df)
        
    def get_error_log_df(self) :
        return(self.error_log_df)
    
 
def get_final_lat_lng_col_names(geocid,runParms) :
    """
    * --------------------------------------------------------- 
    * function : get lat lng col names
    * 
    * parms :
    *  geocid     - geocoder identifier
    *  geotype    - geocoding op type
    *  runParms   - run parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    #from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_google_query_input_labelList,
    #                                                    bulk_bing_query_input_labelList)

    if(geocid == GoogleId) :
        lat_long_col_name   =   runParms.get("new_dataframe_lat_long_column_name(s)")
    else :
        lat_long_col_name   =   runParms.get("new_dataframe_lat_long_column_name(s)")

    if(GEOCODE_TRACE_PROCESS_ERRORS) :
        cfg.add_debug_to_log("get_lat_lng_col_name",str(lat_long_col_name))

    if( (lat_long_col_name.find("[") > -1) or (lat_long_col_name.find("]") > -1) ) :

        lat_lng_col_names   =   lat_long_col_name.replace("[","") 
        lat_lng_col_names   =   lat_lng_col_names.replace("]","")   
        lat_lng_col_names   =   lat_lng_col_names.split(",")

        return(lat_lng_col_names)

    else :

        return(lat_long_col_name)


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   geocoding data components 
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def init_geocoding_data_structures(geocid,geotype,runParms) :
    """
    * --------------------------------------------------------- 
        lat_long_col_name   =   runParms.get(bulk_bing_query_input_labelList[2])
    * function : init data structures to run geocoder
    * 
    * parms :
    *  geocid     - geocoder identifier
    *  geotype    - geocoding op type
    *  runParms   - run parameters
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
        cfg.add_debug_to_log("init_geocoding_data_structures"," : geocid " + str(geocid) + " geotype : " + str(geotype))
        cfg.add_debug_to_log("init_geocoding_data_structures"," : runParms " + str(runParms))

    if(geotype == QUERY) :
        columns     =   ["source_df_rowid", "source_df_address"]
    else :
        columns     =   ["source_df_rowid"]

    max_geocodes  =   0
    
    if(geocid == GoogleId) :
        
        if(geotype == QUERY) :  
            
            lat_long_col_names   =   get_final_lat_lng_col_names(geocid,runParms)
            
            if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :
                cfg.add_debug_to_log("init_geocoding_data_structures"," : lat_long_col_names" + str(lat_long_col_names))
            
            if(type(lat_long_col_names) == list) :
                columns.append(lat_long_col_names[0])
                columns.append(lat_long_col_names[1])
            else :
                columns.append(lat_long_col_names)
            
            f_address   =   runParms.get("save_geocoder_full_address_column_name")
            if(not (f_address is None)) :
                if(len(f_address) > 0) :
                    if(not (f_address == "None") ):
                        columns.append(f_address)
                    else :
                        columns.append("returned_full_address")
            
            max_geocodes   =   int(runParms.get("max_addresses_to_geocode"))
            
        else : # Reverse
            
            lat_long_col_name       =   runParms.get("dataframe_lat_long_column_name(s)")
            lat_long_col_name_list  =   lat_long_col_name.split(",")
            
            if(len(lat_long_col_name_list) == 1) :
                
                columns.append(lat_long_col_name_list[0])
                
            else :
                columns.append(lat_long_col_name_list[0])
                columns.append(lat_long_col_name_list[1])

            columns.append("Full_Address")

            addr_comps   =   GM.get_google_address_components(runParms.get("address_components_list"))

            if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
                cfg.add_debug_to_log("address_components_to_retrieve",runParms.get("address_components_list"))
                cfg.add_debug_to_log("addr_comps",str(type(addr_comps)) + str(addr_comps))

            if(not (len(addr_comps) == 0)) :
                for i in range(len(addr_comps)) :
                    columns.append(addr_comps[i])

            columns.append("location_type")

            max_geocodes   =   int(runParms.get("max_lat_longs"))

           
    elif(geocid == BingId) :
        
        if(geotype == QUERY) :  
            
            lat_long_col_names   =   get_final_lat_lng_col_names(geocid,runParms)
            
            if(GEOCODE_TRACE_GET_GEOCODE_LOAD) :
                cfg.add_debug_to_log("lat_long_col_names",str(lat_long_col_names))
             
            if(type(lat_long_col_names) == list) :
                columns.append(lat_long_col_names[0])
                columns.append(lat_long_col_names[1])
            else :
                columns.append(lat_long_col_names)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            f_address   =   runParms.get("save_geocoder_full_address_column_name")
            if(not (f_address is None)) :
                if(len(f_address) > 0) :
                    if(not (f_address == "None") ):
                        columns.append(f_address)
                    else :
                        columns.append("returned_full_address")
            
            max_geocodes   =   int(runParms.get("max_addresses_to_geocode"))
        
        
        else : # geocode reverse
            
            lat_long_col_name       =   runParms.get("dataframe_lat_long_column_name(s)")
            lat_long_col_name_list  =   lat_long_col_name.split(",")
            
            for i in range(len(lat_long_col_name_list)) :
                lat_long_col_name_list[i]   =  lat_long_col_name_list[i].replace("[","")     
                lat_long_col_name_list[i]   =  lat_long_col_name_list[i].replace("]","")
                
            if(len(lat_long_col_name_list) == 1) :
                
                columns.append(lat_long_col_name_list[0])
                
            else :
                
                columns.append(lat_long_col_name_list[0])
                columns.append(lat_long_col_name_list[1])
            
            addrcompsflag   =   runParms.get("address_components_to_retrieve")
            
            if(addrcompsflag is None) : 
                columns.append("full_address")
                
            else :
                
                if(addrcompsflag == "Full Address Only")  :
                    columns.append("full_address") 
                
                else :
                    
                    columns.append("full_address")
                    columns.append("locality")
                    columns.append("state")
                    columns.append("county")
                    columns.append("zipcode")

            max_geocodes   =   int(runParms.get("max_lat_longs"))
        
                
    else :
        if(GEOCODE_TRACE_GET_GEOCODE_LOAD) :
            cfg.add_debug_to_log("init geocoder data stores"," : bad geocoder")
    
    # init the bulk geocode results data stroe
    BulkGeocodeResultsdf    =   BulkGeocodeResults(geocid,geotype,max_geocodes,columns)  
    
    # init the bulk geocode errors data stroe
    error_limit             =   runParms.get("failure_limit_percent")
    if(error_limit is None) :
        error_limit     =   5
    else :
        error_limit     =   int(error_limit)
        
    BulkGeocodeErrors       =   BulkGeocodeErrorLog(error_limit)    

    return([BulkGeocodeResultsdf,BulkGeocodeErrors])


class BulkGeocodeRunParms:
    
    api_parms               =   None
    geocoderid              =   None
    geotype                 =   None
    
    def __init__(self,geocid,geotype,queryParms):
        
        if(GEOCODE_TRACE_GET_GEOCODE_LOAD)  :   
            cfg.add_debug_to_log("__init__ BulkGeocodeRunParms"," : " + str(geocid) + " " + str(geotype))
        
        self.geocoderid             =   geocid 
        self.geotype                =   geotype 
        self.api_parms              =   {}

        if(self.geocoderid  ==  BingId) :

            if(self.geotype == QUERY) :

                user_location_parm          =   queryParms.get("user_location")
                if(user_location_parm == "None") :
                    user_location_parm    =   None
                else :

                    geocode_pt  =   user_location_parm.replace("(","")
                    geocode_pt  =   geocode_pt.replace(")","")
                    geocode_pt  =   geocode_pt.replace("[","")
                    geocode_pt  =   geocode_pt.replace("]","")

                    geocode_coords  =   geocode_pt.split(",")
                
                    try :

                        lat     =   float(geocode_coords[0])
                        lng     =   float(geocode_coords[1])

                        if(GEOCODE_TRACE_GET_GEOCODE)  :   
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : query : " + str(lat) + str(lng))

                        import geopy
                        user_location_parm   =  geopy.point.Point(lat,lng) 
                                        
                    except  :
                            
                        title       =   "dfcleanser error"       
                        status_msg  =   "[get_geopy_geocoder_results] invalid user_location "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                        display_error_msg(title,status_msg)

                        return(None)

                self.api_parms.update({"user_location_parm" : user_location_parm})

                culture_parm                =   queryParms.get("culture")
                if(culture_parm == "None") :
                    culture_parm    =   None

                self.api_parms.update({"culture_parm" : culture_parm})

                timeout_parm                =   int(BING_TIMEOUT)
                self.api_parms.update({"timeout_parm" : timeout_parm})

            
                include_neighborhood_parm   =   queryParms.get("include_neighborhood")
                if(include_neighborhood_parm == "True") :
                    include_neighborhood_parm   =   True
                else :
                    include_neighborhood_parm   =   None
                self.api_parms.update({"include_neighborhood_parm" : include_neighborhood_parm})
            
                include_country_code_parm   =   queryParms.get("include_country_code")
                if(include_country_code_parm == "True") :
                    include_country_code_parm   =   True
                else :
                    include_country_code_parm   =   False
                self.api_parms.update({"include_country_code_parm" : include_country_code_parm})

            else : # Bing reverse

                culture_parm                =   queryParms.get("culture")
                self.api_parms.update({"culture_parm" : culture_parm})

                include_country_code_parm   =   queryParms.get("include_country_code")
                self.api_parms.update({"include_country_code_parm" : include_country_code_parm})
        
        else : # Google

            if(self.geotype == QUERY) :

                """
                bounds_parm          =   queryParms.get("bounds")

                if(GEOCODE_TRACE_GET_GEOCODE)  :   
                    cfg.add_debug_to_log("BulkGeocodeRunParms"," : bounds_parm : " + str(type(bounds_parm)) + " " + str(bounds_parm))

               
                if(bounds_parm == "None") :
                    bounds_parm    =   None
                
                else :

                    first_coord_end     =   bounds_parm.find(")")
                    first_coord         =   bounds_parm[0:first_coord_end]
                    second_coord        =   bounds_parm[(first_coord_end+2):]

                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        cfg.add_debug_to_log("BulkGeocodeRunParms"," : first_coord_pair : " + str(first_coord))
                        cfg.add_debug_to_log("BulkGeocodeRunParms"," : second_coord_pair : " + str(second_coord))


                    first_coord         =   first_coord.replace("[","")
                    first_coord         =   first_coord.replace("]","")
                    first_coord         =   first_coord.replace("(","")
                    first_coord         =   first_coord.replace(")","")
                    first_coord_pair    =   first_coord.split(",")

                    second_coord        =   second_coord.replace("[","")
                    second_coord        =   second_coord.replace("]","")
                    second_coord        =   second_coord.replace("(","")
                    second_coord        =   second_coord.replace(")","")
                    second_coord_pair   =   second_coord.split(",")

                    if(GEOCODE_TRACE_GET_GEOCODE)  :   
                        cfg.add_debug_to_log("BulkGeocodeRunParms"," : first_coord_pair : " + str(first_coord_pair))
                        cfg.add_debug_to_log("[BulkGeocodeRunParms"," : second_coord_pair : " + str(second_coord_pair))

                    try :

                        lat1     =   float(first_coord_pair[0])
                        lng1     =   float(first_coord_pair[1])

                        lat2     =   float(second_coord_pair[0])
                        lng2     =   float(second_coord_pair[1])

                        if(GEOCODE_TRACE_GET_GEOCODE)  :   
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : lat1 - lng1 : " + str(lat1) + " " + str(lng1))
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : lat2 - lng2 : " + str(lat2) + " " + str(lng2))

                        import geopy
                        bounds_pt1   =  (lat1,lng1)#geopy.point.Point(lat1,lng1) 
                        bounds_pt2   =  (lat2,lng2)#geopy.point.Point(lat2,lng2)
                        
                        if(GEOCODE_TRACE_GET_GEOCODE)  :   
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : bounds_pt1 : " + str(type(bounds_pt1)) + " " + str(bounds_pt1))
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : bounds_pt2 : " + str(type(bounds_pt2)) + " " +str(bounds_pt2))

                        bounds_parm     =   (bounds_pt1,bounds_pt2)

                        bounds_parm     =   str(bounds_parm)

                        if(GEOCODE_TRACE_GET_GEOCODE)  :   
                            cfg.add_debug_to_log("BulkGeocodeRunParms"," : bounds_parm : " + str(type(bounds_parm)) + " " + str(bounds_parm))

                                        
                    except Exception as e:

                        title       =   "dfcleanser error"       
                        status_msg  =   "[get_geopy_geocoder_results] invalid bounds value "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)
                            
                        return(None)
                    
                    self.api_parms.update({"bounds_parm" : bounds_parm})
                    
                """

                regionParm      =   queryParms.get("region")
                colon_char      =   regionParm.find(":")
                regionParm      =   regionParm[(colon_char + 1) :]
                self.api_parms.update({"regionParm" : regionParm})

                languageParm    =   queryParms.get("language")
                self.api_parms.update({"languageParm" : languageParm})


            else : #Reverse

                if(not (queryParms == None)) :

                    location_typeParm   =   queryParms.get("valid_location_type(s)",None)
                    if(len(location_typeParm) == 0) :
                        loc_type_parm   =   None
                    else :

                        loc_type_parm   =  location_typeParm.replace("[","") 
                        loc_type_parm   =  loc_type_parm.replace("]","")
                        loc_type_parm   =  loc_type_parm.split()

                    from dfcleanser.sw_utilities.DFCDataStores import get_Dict
                    languagedict    =   get_Dict("Language_Codes")
                    languageParm    =   languagedict.get(queryParms.get("language",None))
            
                else :

                    loc_type_parm       =   None
                    languageParm        =   None

                self.api_parms.update({"loc_type_parm" : loc_type_parm})
                self.api_parms.update({"languageParm" : languageParm})


    def get_api_parm(self,parmid) :
        return(self.api_parms.get(parmid))

    def get_api_parms(self) :
        return(self.api_parms)
