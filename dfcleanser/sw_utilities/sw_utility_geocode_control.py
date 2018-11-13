"""
# sw_utility_geocode_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

import json

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw
import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm

from dfcleanser.common.table_widgets import drop_owner_tables

from dfcleanser.common.common_utils import (get_parms_for_input, display_exception, display_status, 
                                            display_notes, opStatus, RunningClock)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

            
def get_num_input_ids(idList) :
    
    count = 0
    for i in range(len(idList)) :
        if(idList[i] != None) :
            count = count + 1
            
    return(count)

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar control function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_geocode_utility(optionId,parms=None) :

    from IPython.display import clear_output
    clear_output()

    if(not cfg.check_if_dc_init()) :
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
        #display_status("DataframeCleanser not fully initialized yet - please wait and try again")
        return

    if(optionId == sugm.DISPLAY_GEOCODING) :
        sugw.display_geocode_main_taskbar()        
        
        clear_sw_utility_geocodedata()
        
    elif(optionId == sugm.DISPLAY_GET_COORDS) :
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)

    elif(optionId == sugm.DISPLAY_GET_ADDRESS) :
        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,parms,sugm.REVERSEPARMS)
            
    elif(optionId == sugm.PROCESS_GET_COORDS) :
        sugw.display_geocode_main_taskbar()        
        
        fid = parms[0]
        
        if(fid == 0) :
            get_geocoder_coords(parms)
        else :
            if(cfg.is_dc_dataframe_loaded()) :
                get_geocoder_df_coords(parms)
            else :
                sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)
                display_status("No Dataframe Loaded to get dataframe coords")
    
    elif(optionId == sugm.DISPLAY_DF_GET_COORDS) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if( (geocid == sugm.GoogleId) or (geocid == sugm.NominatimId) ) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
            display_bulk_geocode_inputs(geocid,sugm.ADDRESS_CONVERSION)
        elif(geocid == sugm.ArcGISId) : 
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_arcgis_connector_inputs
            display_arcgis_connector_inputs(sugm.ADDRESS_CONVERSION)
        else :
            sugw.display_geocode_main_taskbar() 
            display_status("Bulk Geocoding not supported for Current Geocoder : "+ sugm.get_geocoder_title(geocid))
    
    elif(optionId == sugm.DISPLAY_DF_GET_ADDRESS) : 
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if( (geocid == sugm.GoogleId) or (geocid == sugm.ArcGISId) or (geocid == sugm.NominatimId) ) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
            display_bulk_geocode_inputs(geocid,sugm.COORDS_CONVERSION)
        else :
            sugw.display_geocode_main_taskbar() 
            display_status("Bulk Geocoding not supported for Current Geocoder : "+ sugm.get_geocoder_title(geocid))
    
    elif(optionId ==  sugm.PROCESS_DF_GET_COORDS) :
        
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
           
        print("PROCESS_DF_GET_COORDS",fid,geocid,inputs) 
        
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
            sugw.display_geocode_inputs(geotype,None,sugm.QUERYPARMS)
            print("BULK_RETURN")
                
        elif(fid == sugm.BULK_HELP) :
            if(geocid == sugm.GoogleId) :
                from dfcleanser.sw_utilities.sw_utility_geocode_batch import bulk_google_query_input_id
                bparms = cfg.get_config_value(bulk_google_query_input_id+"Parms")
            else :
                from dfcleanser.sw_utilities.sw_utility_geocode_batch import batch_arcgis_query_id
                bparms = cfg.get_config_value(batch_arcgis_query_id+"Parms")
            
            print("BULK_HELP",bparms)
            display_bulk_geocode_inputs(geocid,geotype,sugm.COLNAMES_TABLE)
            
    elif(optionId == sugm.PROCESS_GET_ADDRESS) :
        
        sugw.display_geocode_main_taskbar()        
        
        fid = parms[0]
        
        if(fid == 0) :
            get_geocoder_address(parms)
        else :
            if(cfg.is_dc_dataframe_loaded()) :
                get_df_geocoder_address(parms)
            else :
                sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,parms,sugm.REVERSEPARMS)
                display_status("No Dataframe Loaded to get dataframe coords")
    
    elif(optionId == sugm.PROCESS_DF_GET_ADDRESS) :
        print("PROCESS_DF_GET_ADDRESS",parms)
        
    elif(optionId ==  sugm.DISPLAY_DISTANCE) :
        clear_output() 
        sugw.display_calc_distance_input_form()
    
    elif(optionId ==  sugm.PROCESS_DISTANCE) :
        sugw.display_geocode_main_taskbar() 
        print("PROCESS_DISTANCE",parms)        
    
    elif(optionId ==  sugm.DISPLAY_DF_DISTANCE) :
        clear_output()        
        sugw.display_calc_df_distance_input_form()

    elif(optionId ==  sugm.PROCESS_DF_DISTANCE) :
        sugw.display_geocode_main_taskbar() 
        print("PROCESS_DF_DISTANCE",parms)        

    elif(optionId == sugm.DISPLAY_GEOCODER) :
        
        geocid = None
        
        if(parms != None) :
            for i in range(len(sugm.supported_Geocoders)) :
                if(sugm.get_geocoder_title(sugm.supported_Geocoders[i]) == parms) :
                    geocid = sugm.supported_Geocoders[i]
        
        sugw.display_geocoders(geocid) 
    
    elif(optionId == sugm.PROCESS_GEOCODER) :
 
        print("PROCESS_GEOCODER",parms)
        geocid  =   None
        fid     =   -1
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            if(fid < 3) :
                inputs  =   parms[2]
            
        if(fid == 0) :
            test_geocoder(geocid,inputs)
            
        elif(fid == 1) :
            sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)

        elif(fid == 2) :
            sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,parms,sugm.REVERSEPARMS)

        elif(fid == 3) :
            sugw.display_geocoders(geocid) 

    elif(optionId == sugm.DISPLAY_FULL_GEOCODING) :
        sugw.display_geocoders(None,True)
        
    elif(optionId == sugm.DISPLAY_FULL_QUERY) :
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,None,sugm.QUERYPARMS,False,True)

    elif(optionId == sugm.DISPLAY_FULL_REVERSE) :
        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,None,sugm.REVERSEPARMS,False,True)

    elif(optionId == sugm.DISPLAY_FULL_BULK_GOOGLE_QUERY) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
        display_bulk_geocode_inputs(sugm.GoogleId,sugm.ADDRESS_CONVERSION,sugm.COLNAMES_TABLE,True)
    
    elif(optionId == sugm.DISPLAY_FULL_BATCH_ARCGIS_QUERY) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
        display_bulk_geocode_inputs(sugm.ArcGISId,sugm.ADDRESS_CONVERSION,sugm.COLNAMES_TABLE,True)

    elif(optionId == sugm.PROCESS_BATCH_TEST_CONNECTOR) :
        fid     =   int(parms[0]) 
        
        if(fid == sugm.BATCH_TEST_CONNECTOR) :
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import test_arcgis_connector
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
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_arcgis_connector_inputs
            display_arcgis_connector_inputs(geotype)
            
        if(fid == sugm.BATCH_RETURN)    :
            geotype = int(parms[1])
            if(geotype == sugm.DISPLAY_GET_COORDS) :
                sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)
            else :
                sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,parms,sugm.REVERSEPARMS)
           
            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoder helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#  get geocoder engine
#--------------------------------------------------------------------------
"""
def get_geocoder_engine(geocid,opstat) :
    
    geolocator  =   None
    
    try :
            
        geocinitparms = get_geocoder_cmd_parms(sugm.INITPARMS,geocid)
        
        #print("get_geocoder_engine",geocinitparms)
        if(geocid == sugm.GoogleId) :
            from geopy.geocoders import GoogleV3
            if(geocinitparms == None) :
                geolocator = GoogleV3() 
            else :
                geolocator = GoogleV3(**geocinitparms)
            
        elif(geocid == sugm.BingId) :
            from geopy.geocoders import Bing
            if(geocinitparms == None) :
                geolocator = Bing() 
            else :
                geolocator = Bing(**geocinitparms)
            
        elif(geocid == sugm.DataBCId) :
            from geopy.geocoders import DataBC
            if(geocinitparms == None) :
                geolocator = DataBC() 
            else :
                geolocator = DataBC(**geocinitparms)
            
        elif(geocid == sugm.GeocoderDotUSId) :
            from geopy.geocoders import GeocoderDotUS
            if(geocinitparms == None) :
                geolocator = GeocoderDotUS() 
            else :
                geolocator = GeocoderDotUS(**geocinitparms)
                    
        elif(geocid == sugm.OpenMapQuestId) :
            from geopy.geocoders import OpenMapQuest
            if(geocinitparms == None) :
                geolocator = OpenMapQuest() 
            else :
                geolocator = OpenMapQuest(**geocinitparms)
                    
        elif(geocid == sugm.NominatimId) :
            from geopy.geocoders import Nominatim
            if(geocinitparms == None) :
                geolocator = Nominatim() 
            else :
                geolocator = Nominatim(**geocinitparms)
                    
        elif(geocid == sugm.YahooPlaceFinderId) :
            from geopy.geocoders import YahooPlaceFinder
            if(geocinitparms == None) :
                geolocator = YahooPlaceFinder() 
            else :
                geolocator = YahooPlaceFinder(**geocinitparms)
                    
        elif(geocid == sugm.ArcGISId) :
            from geopy.geocoders import ArcGIS
            if(geocinitparms == None) :
                geolocator = ArcGIS() 
            else :
                geolocator = ArcGIS(**geocinitparms)
                    
    except Exception as e:
        opstat.store_exception("Error initializing geocoder service",e)
    
    return(geolocator)    
  
"""
#--------------------------------------------------------------------------
#  get command kwargs stored in config
#--------------------------------------------------------------------------
"""
def get_geocoder_cmd_parms(ptype,geocid) :

        
    if(ptype == sugm.INITPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_geocoderkwargs",cfg.GLOBAL)
    elif(ptype == sugm.QUERYPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_querykwargs")
    elif(ptype == sugm.QUERYDFPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_df_querykwargs")
    elif(ptype == sugm.REVERSEPARMS) :
        geokwargs = cfg.get_config_value(sugm.get_geocoder_title(geocid) + "_reversekwargs")
 
    #print("get_geocoder_cmd_parms",geokwargs)
    geocparms = {}

    if(geokwargs != None) :
        for i in range(len(geokwargs)) : 
            geoparm = geokwargs[i]
        
            if( (geoparm.get("value") != None) and (geoparm.get("value") != "" )) :
                geocparms.update({geoparm.get("key"):geoparm.get("value")})

    if(len(geocparms) == 0) :
        return(None)
    else :
        return(geocparms)
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   taskbar process Utility functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
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
#  test the geocoder connection and get sample
#--------------------------------------------------------------------------
"""
def test_geocoder(geocid,gcparms) :

    opstat      =   opStatus()
    
    opstat = sugw.validate_cmd_parms(sugm.INITPARMS,geocid,gcparms) 
    
    if( not (opstat.get_status()) ) :
    
        sugw.display_geocoders(geocid) 
        display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()
 
        try :
            geolocator = get_geocoder_engine(geocid,opstat)
            
        except Exception as e:
            opstat.store_exception("Error initializing geocoder service",e)

        if(opstat.get_status()) :
            
            query = "11111 Euclid Ave, Cleveland OH " 
            
            try :
                address, (latitude, longitude) = geolocator.geocode(query) 
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()
        
        sugw.display_geocoders(geocid) 
        
        if(opstat.get_status()) :
            
            print("\n")
            display_status("geocoder ran successfully")
            
            notes = []
            notes.append("Starting Address   : " + query)
            notes.append("  ")
            notes.append("Returned Address   : " + address)
            notes.append("Returned Latitude  : " + str(latitude))
            notes.append("Returned Longitude : " + str(longitude))
            
            display_notes(notes)
            
        else :
            display_exception(opstat)



"""
#--------------------------------------------------------------------------
#  get geocoder address
#--------------------------------------------------------------------------
"""
def get_geocoder_coords(inparms) :
    
    geocid  =   inparms[1]
    parms   =   inparms[2]
    opstat  =   opStatus()
    
    opstat = sugw.validate_cmd_parms(sugm.QUERYPARMS,geocid,parms)
    
    if(not opstat.get_status()) :
        
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,None,sugm.QUERYPARMS)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)
        
        queryparms  = None
        query       = None

        numresults   =  0
        
        if(opstat.get_status()) :
            
            try :
                
                queryparms = get_geocoder_cmd_parms(sugm.QUERYPARMS,geocid)
                query = queryparms.get("query")
                queryparms.pop("query")
                
                if(queryparms.get("number_of_results") != None) :
                    numresults = int(queryparms.get("number_of_results"))
                    queryparms.pop("number_of_results")
                    if(geocid == sugw.DataBCId) :
                        queryparms.update({"max_results":numresults}) 
                    else :
                        queryparms.update({"exactly_one":False})
                
                if(len(queryparms) > 0) :
                    location = geolocator.geocode(query, **queryparms) 
                else :
                    location = geolocator.geocode(query) 
                    
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()
        
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,inparms,sugm.QUERYPARMS) 
        
        if(opstat.get_status()) :
            
            print("\n")
            display_status("coordinates retrieved successfully")
            
            notes = []
            notes.append("Starting Address   : " + query)
            notes.append("  ")
            notes.append("Returned Coords(s)   : ")
            if(type(location) == list) :
                for i in range(len(location)) :
                    if(i<numresults) :
                        notes.append("&nbsp;&nbsp;Address&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;" + location[i].address) 
                        notes.append("&nbsp;&nbsp;Latitude&nbsp;&nbsp;:&nbsp;&nbsp;" + str(location[i].latitude))
                        notes.append("&nbsp;&nbsp;Longitude&nbsp;&nbsp; :&nbsp;&nbsp;" + str(location[i].longitude))
            else :
                notes.append("&nbsp;&nbsp;Address   : " + location.address) 
                notes.append("&nbsp;&nbsp;Latitude  : " + str(location.latitude))
                notes.append("&nbsp;&nbsp;Longitude : " + str(location.longitude))

            display_notes(notes)
            
        else :
            display_exception(opstat)

"""
#--------------------------------------------------------------------------
#  get df coords parms
#--------------------------------------------------------------------------
"""
def get_df_coords_parms(geocid,parms) :
        
    dfform  =   sugw.get_comp_addr_conv_form(geocid) 
    fparms  =   get_parms_for_input(parms,dfform[1])
    
    dfcolsList = fparms[0].split("+")
    for i in range(len(dfcolsList)) :
        dfcolsList[i] = dfcolsList[i].strip()
            
    coltypes = []
    
    for i in range(len(dfcolsList)) :
        if(dfcolsList[i].find("'") != -1) :
            coltypes.append(False)
            staticname = dfcolsList[i].replace("'","")
            #staticname = staticname[i].lstrip("'")
            dfcolsList[i] = staticname
        else :
            coltypes.append(True)
    
    fparms[0] = [dfcolsList,coltypes]
    
    return(fparms)

"""
#--------------------------------------------------------------------------
#  get geocoder address for dataframe 
#--------------------------------------------------------------------------
"""
def get_geocoder_df_coords(inparms) :
    
    return()
    
    geocid  =   inparms[1]
    parms   =   inparms[2]
    opstat  =   opStatus()
    
    opstat = sugw.validate_cmd_parms(sugm.QUERYDFPARMS,geocid,parms)
    
    if(not opstat.get_status()) :
        
        sugw.display_comp_addr_geocode_inputs(inparms)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)

        if(opstat.get_status()) :
            
            try :
                
                queryparms = get_df_coords_parms(geocid,parms)
                
                #print("get_geocoder_df_addresses",queryparms)
                
                cols        =   queryparms[0]
                
                colnames    =   []
                
                if(queryparms[1].find(",") > 1) :
                    cnames = queryparms[1].split(",")
                    for i in range(len(cnames)) :
                        colnames.append(cnames[i])
                else :
                    colnames.append(queryparms[1])

                if(len(queryparms[2]) > 0) :
                    deloldcols  =   True
                else :
                    deloldcols  =   False
                
                qparms  =   get_geocoder_cmd_parms(sugm.QUERYDFPARMS,geocid)
                
                if(len(qparms) > 3) :
                    qparms  =   qparms[3:]
                
                invalidaddr     =   []
                timeoutaddr     =   []
                parseerror      =   []
                
                stopRun         =   False
                
                totalTimeouts   =   0
                MAX_TIMEOUTS    =   100
                
                totalParseErrors   =   0
                MAX_PARSEERRORS    =   200
                
                addresses       =   []
                latitudes       =   []
                longitudes      =   []
                latlongs        =   []
                
                # for each row in the dataframe
                for i in range(len(cfg.get_dc_dataframe())) :
                    
                    if(stopRun) :  
                        i = len(cfg.get_dc_dataframe()) + 1
                    else :
                        
                        query = ""
                        for j in range(len(cols[0])) :
                            if(cols[1][j]) :
                                val = cfg.get_dc_dataframe().iloc[i][cols[0][j]]
                                import pandas as pd
                                if(not pd.isnull(val)) :
                                    query = query + " " + str(val) 
                            else :
                                query = query + " " + str(cols[0][j])
                
                        if(len(query > 0)) :
                        
                            import geopy as gp
                        
                            try :    
                                if(len(qparms) > 0) :
                                    address, (latitude, longitude) = geolocator.geocode(query, **qparms) 
                                else :
                                    address, (latitude, longitude) = geolocator.geocode(query)
                                
                                    if(len(colnames) == 1) :
                                        latlongs.append((latitude, longitude)) 
                                    else :
                                        latitudes.append(latitude)
                                        longitudes.append(longitude)
                                        if(len(colnames) == 3) :
                                            addresses.append(address)
                                        
                                addresses.append(address)
                                latitudes.append(latitude)
                                longitudes.append(longitude)
                                
                            except gp.exc.ConfigurationError as e:
                                opstat.store_exception("ConfigurationError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderServiceError as e:
                                opstat.store_exception("GeocoderServiceError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderQueryError as e:
                                opstat.store_exception("GeocoderQueryError Error",e)
                                stopRun = True
                            except gp.exc.GeocoderQuotaExceeded as e:
                                opstat.store_exception("GeocoderQuotaExceeded Error",e)
                                stopRun = True
                            except gp.exc.GeocoderAuthenticationFailure as e:
                                opstat.store_exception("GeocoderAuthenticationFailure",e)
                                stopRun = True
                            except gp.exc.GeocoderInsufficientPrivileges as e:
                                opstat.store_exception("GeocoderInsufficientPrivileges Error",e)
                                stopRun = True
                            except gp.exc.GeocoderTimedOut as e:
                                
                                totalTimeouts = totalTimeouts + 1
                                
                                if(totalTimeouts > MAX_TIMEOUTS) :
                                    stopRun = True
                                    opstat.store_exception("GeocoderTimedOut Error",e)
                                else :
                                    addresses.append(None)
                                    latitudes.append(None)
                                    longitudes.append(None)
                                    timeoutaddr.append(i)
    
                            except gp.exc.GeocoderUnavailable as e:
                                opstat.store_exception("GeocoderUnavailable Error",e)
                                stopRun = True
                            except gp.exc.GeocoderParseError as e:
                                
                                totalParseErrors = totalParseErrors + 1
                                
                                if(totalParseErrors > MAX_PARSEERRORS) :
                                    stopRun = True
                                    opstat.store_exception("GeocoderParseError Error",e)
                                else :
                                    addresses.append(None)
                                    latitudes.append(None)
                                    longitudes.append(None)
                                    parseerror.append(i)
                                    
                            except gp.exc.GeocoderNotFound as e:
                                opstat.store_exception("GeocoderNotFound Error",e)
                                stopRun = True
    
                        else :
                            invalidaddr.append(i)
                            
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()

        if(opstat.get_status()) :
            
            try :
                
                # create new lat long cols
                from dfcleanser.data_transform.data_transform_columns_widgets import add_column
                
                if(len(colnames) == 1) :
                    add_column(colnames[0],latlongs,opstat) 
                else :
                    add_column(colnames[0],latitudes,opstat)
                    add_column(colnames[1],longitudes,opstat)
                    if(len(colnames) == 3) :
                        add_column(colnames[2],addresses,opstat)
                
                # delete old cols
                if(deloldcols) :
                    for i in range(len(queryparms[1])) :
                        if(queryparms[1][i]) :
                            cfg.set_dc_dataframe(cfg.get_dc_dataframe().drop([queryparms[0][i]],axis=1))
                
            except Exception as e:
                opstat.store_exception("Unable to save coors columns",e)

            print("\n")
            display_status("dataframe coordinates loaded successfully")
            
            notes = []
            notes.append("Total Coords Loaded   : " + str(len(cfg.get_dc_dataframe())))
            notes.append("  ")
            notes.append("Total Timeouts        : " + str(len(timeoutaddr)))
            notes.append("Total Parse Errors    : " + str(len(parseerror)))
            
            display_notes(notes)
            
        else :
            display_exception(opstat)


"""
#--------------------------------------------------------------------------
#  get geocoder address
#--------------------------------------------------------------------------
"""
def get_geocoder_address(inparms) :

    geocid  =   inparms[1]
    parms   =   inparms[2]
    opstat  =   opStatus()
    
    opstat = sugw.validate_cmd_parms(sugm.REVERSEPARMS,geocid,parms)
    
    if(not opstat.get_status()) :
        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,None,sugm.REVERSEPARMS)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)
        numresults   =  0
        
        if(opstat.get_status()) :
            
            try :
                
                queryparms = get_geocoder_cmd_parms(sugm.REVERSEPARMS,geocid)
                #print("queryparms",queryparms)
                query = queryparms.get("query")
                queryparms.pop("query")
                
                if(queryparms.get("number_of_results") != None) :
                    numresults = int(queryparms.get("number_of_results"))
                    queryparms.pop("number_of_results")
                    queryparms.update({"exactly_one":False})
                
                if(len(queryparms) > 0) :
                    location = geolocator.reverse(query, **queryparms) 
                else :
                    location = geolocator.reverse(query) 
                    
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()

        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,inparms,sugm.REVERSEPARMS) 
        
        if(opstat.get_status()) :
            
            print("\n")
            display_status("address retrieved successfully")
            
            notes = []
            notes.append("Address Coordinates   : " + query)
            notes.append("  ")
            notes.append("Returned Address(s)   : ")
            if(type(location) == list) :
                for i in range(len(location)) :
                    if(i<numresults) :
                        notes.append("&nbsp;&nbsp;" + location[i].address)    
            else :
                notes.append("&nbsp;&nbsp;" + location.address)
                
            display_notes(notes)
        else :
            display_exception(opstat)

"""
#--------------------------------------------------------------------------
#  get geocoder address
#--------------------------------------------------------------------------
"""
def get_df_geocoder_address(inparms) :

    print("get_df_geocoder_address",inparms)
    return() 



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoders utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_sw_utility_geocodedata() :
    
    drop_owner_tables(cfg.SWGeocodeUtility_ID)
    clear_sw_utility_geocode_cfg_values()


def clear_sw_utility_geocode_cfg_values() :
 
    #drop_config_value(ADDR_CONV_COL_LIST_PARM)
    return




