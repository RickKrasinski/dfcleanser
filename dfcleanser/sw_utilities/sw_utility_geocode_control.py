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
    
    # get simple coordinates for an address        
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
    
    # get address for simple coords       
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
    
    # display bulk geocoding op;tions
    elif( (optionId == sugm.DISPLAY_BULK_GET_COORDS) or (optionId == sugm.DISPLAY_BULK_GET_ADDRESS) ) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocoding
        display_bulk_geocoding(optionId) 
        
    # process bulk geocoding op;tions
    elif( (optionId ==  sugm.PROCESS_BULK_GET_COORDS)  or (optionId ==  sugm.PROCESS_BULK_GET_ADDRESS) ):
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import process_bulk_geocoding
        process_bulk_geocoding(optionId,parms)            
    
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
                    
        if(cfg.get_config_value(cfg.BULK_GEOCODE_MODE_KEY) == None) :
            sugw.display_geocoders(geocid)
        else :
            sugw.display_geocoders(geocid,False,False)
    
    elif(optionId == sugm.PROCESS_GEOCODER) :
 
        print("PROCESS_GEOCODER",parms)
        geocid  =   None
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            
            print("PROCESS_GEOCODER",fid,geocid)
            if(fid < 3) :

                if(geocid == sugm.ArcGISId) : 
                    ids =   sugw.arcgis_geocoder_idList
                elif(geocid == sugm.GoogleId) :
                    ids =   sugw.google_geocoder_idList
                    
                inputs  =   get_parms_for_input(parms[2],ids)
                if(len(inputs) > 0) :
                    cfg.set_config_value(sugw.get_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    
            
        if(fid == 0)    :   test_geocoder(geocid,inputs)
        elif(fid == 1)  :   
            sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,parms,sugm.QUERYPARMS)
        elif(fid == 2)  : 
            print("fid",fid)
            from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocoding
            display_bulk_geocoding(sugm.DISPLAY_BULK_GET_COORDS) 
        elif(fid == 3)  :
            cfg.drop_config_value(sugw.get_form_id(geocid,sugm.GEOCODER) + "Parms")
            if(cfg.get_config_value(cfg.BULK_GEOCODE_MODE_KEY) == None) :
                sugw.display_geocoders(geocid)
            else :
                sugw.display_geocoders(geocid,False,False)

    
    # show full parameters for geocoding parms in a grid
    elif(optionId == sugm.DISPLAY_FULL_GEOCODING) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(cfg.get_config_value(cfg.BULK_GEOCODE_MODE_KEY) == None) :
            sugw.display_geocoders(geocid,True)
        else :
            sugw.display_geocoders(geocid,True,False)
        
    elif(optionId == sugm.DISPLAY_FULL_QUERY) :
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,None,sugm.QUERYPARMS,True)

    elif(optionId == sugm.DISPLAY_FULL_REVERSE) :
        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,None,sugm.REVERSEPARMS,True)

    elif(optionId == sugm.DISPLAY_FULL_BULK_GOOGLE_QUERY) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
        display_bulk_geocode_inputs(sugm.GoogleId,sugm.ADDRESS_CONVERSION,sugm.COLNAMES_TABLE,True)
    
    elif(optionId == sugm.DISPLAY_FULL_BULK_ARCGIS_QUERY) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import display_bulk_geocode_inputs
        display_bulk_geocode_inputs(sugm.ArcGISId,sugm.ADDRESS_CONVERSION,sugm.COLNAMES_TABLE,True)

    # process testing of the bulk geocode connector
    elif(optionId == sugm.PROCESS_TEST_BULK_CONNECTOR) :
        from dfcleanser.sw_utilities.sw_utility_geocode_batch import process_test_bulk_connector
        process_test_bulk_connector(parms)           
    
    elif(optionId == sugm.CLEAR_GEOCODE_PARMS) :
        
        gtype   =   int(parms[0])
        geocid  =   int(parms[1])
        
        print("CLEAR_GEOCODE_PARMS",gtype,geocid)
        
        if(gtype == sugm.ADDRESS_CONVERSION) :
            cfg.drop_config_value(sugw.get_form_id(geocid,gtype) + "Parms")
            sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,None,sugm.QUERYPARMS)

        else :
            cfg.drop_config_value(sugw.get_form_id(geocid,gtype) + "Parms")
            sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,None,sugm.REVERSEPARMS)
        
    elif(optionId == sugm.BULK_GEOCODE_RUN) :
        print("BULK_GEOCODE_RUN")
        
    elif(optionId == sugm.BULK_GEOCODE_PAUSE) :
        print("BULK_GEOCODE_PAUSE")
        
    elif(optionId == sugm.BULK_GEOCODE_STOP) :
        print("BULK_GEOCODE_STOP")
            
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
            
        geocinitparms = sugw.get_geocoder_cmd_kwargs(sugm.GEOCODERPARMS,geocid)
        
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
#--------------------------------------------------------------------------
#   taskbar process Utility functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#  test the geocoder connection and get sample
#--------------------------------------------------------------------------
"""
def test_geocoder(geocid,gcparms) :

    opstat      =   opStatus()
    
    sugw.validate_cmd_parms(sugm.GEOCODERPARMS,geocid,gcparms,opstat) 
    
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
    
    addresses   =   []
    coords      =   []
    
    sugw.validate_cmd_parms(sugm.QUERYPARMS,geocid,parms,opstat)
    
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
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.QUERYPARMS,geocid)
                query = queryparms.get("address(s)")
                queryparms.pop("address(s)")
                
                if(len(query) > 2) :
                    
                    query = query.replace("\n","")
                    
                    # only 1 coord pair
                    if(query.find("],") == -1) :
                        addresses.append(query)
                        
                    # multiple addresses
                    else :
                
                        # find out how lat longs in query
                        nextaddr      =   0
                        startaddr     =   0
                
                        while nextaddr < len(query) :
                            nextaddr = query[startaddr:].find("],")
                            if(nextaddr == -1) :
                                addresses.append(query[startaddr:len(query)])
                                nextaddr = len(query)
                            else :
                                addresses.append(query[startaddr:(nextaddr+1)])
                                startaddr     =   nextaddr + 2
                        
                        for i in range(len(addresses)) :
                            addresses[i]    =  addresses[i].replace("[","") 
                            addresses[i]    =  addresses[i].replace("]","")

                else :
                    opstat.get_status(False)
                    opstat.set_errorMsg("address(s) parm is invalid")    
                
                if(queryparms.get("number_of_results") != None) :
                    numresults = int(queryparms.get("number_of_results"))
                    queryparms.pop("number_of_results")
                    if(geocid == sugw.DataBCId) :
                        queryparms.update({"max_results":numresults}) 
                    else :
                        queryparms.update({"exactly_one":False})
                
                for i in range(len(addresses)) :
                
                    if(len(queryparms) > 0) :
                        location = geolocator.geocode(addresses[i], **queryparms) 
                    else :
                        location = geolocator.geocode(addresses[i]) 
                    
                    coords.append(location)
                    
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()
        
        sugw.display_geocode_inputs(sugm.ADDRESS_CONVERSION,inparms,sugm.QUERYPARMS) 
        
        if(opstat.get_status()) :
            
            print("\n")
            display_status("coordinates retrieved successfully")
            
            notes = []
            
            for j in range(len(coords)) : 
                
                if(len(addresses) > 1) :
                    notes.append("Starting Address " + str(j) + " : " + addresses[j])
                else :
                    notes.append("Starting Address : " + addresses[j])
                    
                notes.append("  ")
                notes.append("&nbsp;&nbsp;Returned Coords   : ")
                if(type(coords[j]) == list) :
                    for i in range(len(location)) :
                        if(i<numresults) :
                            notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Address&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;" + coords[j][i].address) 
                            notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Latitude&nbsp;&nbsp;:&nbsp;&nbsp;" + str(coords[j][i].latitude))
                            notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Longitude&nbsp;&nbsp; :&nbsp;&nbsp;" + str(coords[j][i].longitude))
                else :
                    notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Address   : " + coords[j].address) 
                    notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Latitude  : " + str(coords[j].latitude))
                    notes.append("&nbsp;&nbsp;&nbsp;&nbsp;Longitude : " + str(coords[j].longitude))

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
                
                qparms  =   sugw.get_geocoder_cmd_kwargs(sugm.QUERYDFPARMS,geocid)
                
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
    
    coords      =   []
    locations   =   []

    sugw.validate_cmd_parms(sugm.REVERSEPARMS,geocid,parms,opstat)
    
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
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.REVERSEPARMS,geocid)
                #print("queryparms",queryparms)
                query = queryparms.get("latitude_longitude(s)")
                queryparms.pop("latitude_longitude(s)")
                
                if(len(query) > 2) :
                    
                    query = query.replace(" ","")
                    query = query.replace("\n","")
                    
                    # only 1 coord pair
                    if(query.find("],") == -1) :
                        coords.append(query)
                        
                    # multiple coord pairs
                    else :
                
                        # find out how lat longs in query
                        nextcoords      =   0
                        startcoords     =   0
                
                        while nextcoords < len(query) :
                            nextcoords = query[startcoords:].find("],")
                            if(nextcoords == -1) :
                                coords.append(query[startcoords:len(query)])
                                nextcoords = len(query)
                            else :
                                coords.append(query[startcoords:(nextcoords+1)])
                                startcoords     =   nextcoords + 2
                                
                else :
                    opstat.get_status(False)
                    opstat.set_errorMsg("latitude_longitudes(s) parm is invalid")    
                
                if(queryparms.get("number_of_results") != None) :
                    numresults = int(queryparms.get("number_of_results"))
                    queryparms.pop("number_of_results")
                    queryparms.update({"exactly_one":False})

                print("get_geocoder_address",queryparms)
                
                for i in range(len(coords)) :
                    if(len(queryparms) > 0) :
                        location = geolocator.reverse(coords[i], exactly_one=False)#**queryparms) 
                    else :
                        location = geolocator.reverse(coords[i]) 
                    
                    locations.append(location)
                print("get_geocoder_address",locations)        
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()

        sugw.display_geocode_inputs(sugm.COORDS_CONVERSION,inparms,sugm.REVERSEPARMS) 
        
        if(opstat.get_status()) :
            
            print("get_geocoder_address",numresults)
            
            if(location == None) :
                display_status("no address retrieved check coordinates")
            else :
                print("\n")
                if(len(locations) > 1) :
                    display_status("addresses retrieved successfully")
                else :
                    display_status("address retrieved successfully")
                
                notes = []
                for i in range(len(locations)) :
                    if(len(locations) > 1) :
                        notes.append("Address " + str(i) + " : ")   
                    notes.append("&nbsp;&nbsp;Address Coordinates   : " + coords[i])
                    notes.append("  ")
                    notes.append("&nbsp;&nbsp;Returned Address : ")
                    if(type(locations[i]) == list) :
                        for j in range(len(locations[i])) :
                            if(i<numresults) :
                                notes.append("&nbsp;&nbsp;&nbsp;&nbsp;" + locations[i][j].address)    
                    else :
                        notes.append("&nbsp;&nbsp;&nbsp;&nbsp;" + locations[i].address)
                
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
 
    cfg.drop_config_value(cfg.BULK_GEOCODE_MODE_KEY)
    return




