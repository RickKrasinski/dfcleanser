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

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw
import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_control as subgc
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw

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

            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar control function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_geocode_utility(optionId,parms=None) :
    """
    * ---------------------------------------------------------
    * function : main geocode process function
    * 
    * parms :
    *  optionId  - geocoder option to process
    *  parms     - option parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    print("display_geocode_utility",optionId,parms)
    from IPython.display import clear_output
    clear_output()

    if(not cfg.check_if_dc_init()) :
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
        #display_status("DataframeCleanser not fully initialized yet - please wait and try again")
        return

    if(optionId == sugm.DISPLAY_MAIN_GEOCODING) :
        sugw.display_geocode_main_taskbar()        
        clear_sw_utility_geocodedata()
        
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



    elif(optionId == sugm.PROCESS_GEOCODER) :
 
        print("PROCESS_GEOCODER",parms)
        geocid  =   None
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            
        elif(fid == 1)  :   
            sugw.display_geocode_inputs(parms,sugm.QUERY)
            
    
    # show full parameters for geocoding parms in a grid
    elif(optionId == sugm.DISPLAY_FULL_GEOCODING) :

        formid  =    parms[0]        
        
        if( (formid == "arcgisgeocoder") or 
            (formid == "googlegeocoder") or
            (formid == "binggeocoder") or
            (formid == "mapquestgeocoder") or
            (formid == "nomingeocoder") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.GEOCODER
            
        elif( (formid == "arcgisquery") or 
              (formid == "googlequery") or
              (formid == "bingquery") or
              (formid == "mapquestquery") or
              (formid == "nominquery") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.QUERY

        elif( (formid == "arcgisreverse") or 
              (formid == "googlereverse") or
              (formid == "bingreverse") or
              (formid == "mapquestreverse") or
              (formid == "nominreverse") ) :
            
            gmode   =   sugm.INTERACTIVE
            gtype   =   sugm.REVERSE
            
        elif( (formid == "arcgisbatchgeocoder") or 
              (formid == "googlebulkgeocoder") or
              (formid == "bingbulkgeocoder") or
              (formid == "mapquestbulkgeocoder") or
              (formid == "nominbulkgeocoder") ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.GEOCODER

        elif( (formid == "arcgisbatchquery") or 
              (formid == "googlebulkquery") or
              (formid == "bingbulkquery") or
              (formid == "mapquestbulkquery") or
              (formid == "nominatimbulkquery") ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.QUERY
        
        elif( (formid == "googlebulkquery")  ) :
            
            gmode   =   sugm.BULK
            gtype   =   sugm.REVERSE
        
        if(gtype == sugm.GEOCODER) :
            if(gmode == sugm.INTERACTIVE) :
                sugw.display_geocoders(geocid,True,False)
            else :
                subgw.display_bulk_geocoders(geocid,True)
                
        else :
            if(gmode == sugm.INTERACTIVE) :
                sugw.display_geocode_inputs(geocid,gtype,True)
            else :
                subgw.display_bulk_geocoding(geocid,gtype,True)


    elif(optionId == sugm.PROCESS_GEOCODING) :
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        fparms  =   parms[3]

        sugw.display_geocode_main_taskbar()        
        
        if(gmode == sugm.INTERACTIVE) :
            if(gtype == sugm.QUERY) :
                run_geocoder_query(geocid,fparms)
            else :
                run_geocoder_reverse(geocid,fparms)                
        else :
            if(cfg.is_a_dfc_dataframe_loaded()) :
                if(gtype == sugm.QUERY) :
                    subgc.run_bulk_geocoder_query(geocid,fparms)
                else :
                    subgc.run_bulk_geocoder_reverse(geocid,fparms)
            else :
                display_status("No Dataframe Loaded to run bulk geocoding")

    elif(optionId == sugm.DISPLAY_GEOCODING) :
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        fparms  =   parms[3]
        
        if(gmode == sugm.INTERACTIVE) :
            sugw.display_geocode_inputs(geocid,gtype)
        else :
            subgw.display_bulk_geocoding(geocid,gtype)

    elif(optionId == sugm.TEST_GEOCODER) :
        
        geocid  =   int(parms[0])
        gmode   =   int(parms[1])
        
        if(gmode == sugm.INTERACTIVE) :
            
            if(geocid == sugm.ArcGISId)         :   ids =   sugw.arcgis_geocoder_idList
            elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
            elif(geocid == sugm.GoogleId)       :   ids =   sugw.google_geocoder_idList
            elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
            elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
            inputs  =   get_parms_for_input(parms[2],ids)
                
            print("TEST_GEOOCODER",inputs)
            if(len(inputs) > 0) :
                cfg.set_config_value(sugw.get_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

            test_geocoder(geocid,inputs)
            
        else :
            
            if(geocid == sugm.ArcGISId)         :   ids =   subgw.batch_arcgis_geocoder_idList
            elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
            elif(geocid == sugm.GoogleId)       :   ids =   subgw.google_bulk_geocoder_idList
            elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
            elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
            inputs  =   get_parms_for_input(parms[2],ids)
                
            print("TEST_GEOOCODER",inputs)
            if(len(inputs) > 0) :
                cfg.set_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

            subgc.test_bulk_geocoder(geocid,inputs)
   
    elif(optionId == sugm.CLEAR_GEOCODE_FORM) :
        
        geocid  =   int(parms[0])
        gtype   =   int(parms[1])
        gmode   =   int(parms[2])
        
        print("CLEAR_GEOCODE_FORM",geocid,gtype,gmode)
        
        if(gmode == sugm.INTERACTIVE) :
            cfg.drop_config_value(sugw.get_form_id(geocid,gtype) + "Parms")
            
            if(gtype == sugm.GEOCODER) :
                sugw.display_geocoders(geocid)
            else :
                sugw.display_geocode_inputs(geocid,gtype)
                
        else :
            cfg.drop_config_value(subgw.get_bulk_form_id(geocid,gtype) + "Parms")
            
            if(gtype == sugm.GEOCODER) :
                subgw.display_bulk_geocoders(geocid)
            else :
                subgw.display_bulk_geocode_inputs(geocid,gtype)
                
    elif(optionId == sugm.DISPLAY_GEOCODER) :
                
        geocid  =   int(parms[0])
        if(geocid == -1) :
            geocid  =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
            if(geocid == None) :
                geocid  =   sugm.GoogleId
        
        gmode   =   int(parms[1])
                
        if(gmode == sugm.INTERACTIVE) :
            sugw.display_geocoders(geocid)
        else :
            subgw.display_bulk_geocoders(geocid)
 
    elif(optionId == sugm.GET_TABLE) :
        tableid =   int(parms[0])
        geocid  =   int(parms[1])
        gtype   =   int(parms[2])
        gmode   =   int(parms[3])
        fparms  =   parms[4]
        
        if(gmode == sugm.INTERACTIVE) :
            sugw.display_geocode_inputs(geocid,gtype)

        else :
            subgw.display_bulk_geocode_inputs(geocid,gtype,tableid)



    #"""
    #--------------------------------------------------------------------------
    #   bulk geocoding run  functions
    #--------------------------------------------------------------------------
    #"""
       
    elif(optionId == sugm.BULK_GEOCODE_RUN) :
        print("BULK_GEOCODE_RUN")
        
        parms   =   []
        parms.append(sugm.BULK_START_GEOCODER)
        parms.append(cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY))
        parms.append(sugm.QUERY)
        parms.append(None)
        subgc.process_bulk_geocoding_run_cmd(optionId,parms)
        
    elif(optionId == sugm.BULK_GEOCODE_PAUSE) :
        print("BULK_GEOCODE_PAUSE")
        
        parms   =   []
        parms.append(sugm.BULK_PAUSE_GEOCODER)
        parms.append(cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY))
        parms.append(sugm.QUERY)
        parms.append(None)
        subgc.process_bulk_geocoding_run_cmd(optionId,parms)
        
    elif(optionId == sugm.BULK_GEOCODE_STOP) :
        print("BULK_GEOCODE_STOP")
        
        parms   =   []
        parms.append(sugm.BULK_STOP_GEOCODER)
        parms.append(cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY))
        parms.append(sugm.QUERY)
        parms.append(None)
        subgc.process_bulk_geocoding_run_cmd(optionId,parms)




    elif(optionId == sugm.CHANGE_BULK_GEOCODER) :
        
        geocid = None
        
        if(parms != None) :
            for i in range(len(sugm.supported_Geocoders)) :
                if(sugm.get_geocoder_title(sugm.supported_Geocoders[i]) == parms) :
                    geocid = sugm.supported_Geocoders[i]
                    
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid)
        
        optype = cfg.get_config_value(cfg.BULK_GEOCODE_MODE_KEY)
        if(optype == None) :
            optype = sugm.QUERY
        else :
            if(optype == sugm.QUERY) :
                optype = sugm.QUERY
            else :
                optype = sugm.REVERSE 
                
        subgw.display_bulk_geocoding(geocid,optype)
                   
    elif(optionId == sugm.DISPLAY_BULK_GEOCODER) :
        
        geocid = None
        
        if(parms != None) :
            for i in range(len(sugm.supported_Bulk_Geocoders)) :
                if(sugm.get_geocoder_title(sugm.supported_Bulk_Geocoders[i]) == parms) :
                    geocid = sugm.supported_Bulk_Geocoders[i]
                    
        subgw.display_bulk_geocoders(geocid,False)
    
    elif(optionId == sugm.PROCESS_BULK_GEOCODER) :
 
        print("PROCESS_BULK_GEOCODER",parms)
        geocid  =   None
        fid     =   None
        
        if(parms != None) :
            fid     =   parms[0]
            geocid  =   parms[1]
            
        if(fid == 5)    :  
            
            if(geocid == sugm.ArcGISId)         :   ids =   subgw.batch_arcgis_geocoder_idList
            elif(geocid == sugm.BingId)         :   ids =   sugw.bing_geocoder_idList
            elif(geocid == sugm.GoogleId)       :   ids =   subgw.google_bulk_geocoder_idList
            elif(geocid == sugm.OpenMapQuestId) :   ids =   sugw.mapquest_geocoder_idList
            elif(geocid == sugm.NominatimId)    :   ids =   sugw.nomin_geocoder_idList
                    
            inputs  =   get_parms_for_input(parms[2],ids)
                
            print("PROCESS_GEOCODER BULK TEST",inputs)
            if(len(inputs) > 0) :
                cfg.set_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms",inputs)    

            subgw.test_bulk_geocoder(geocid,inputs)
        
        elif(fid == 6)  :   
            subgw.display_bulk_geocode_inputs(geocid,sugm.QUERY)            
        
        elif(fid == 7)  : 
            sugw.display_geocoders(geocid) 
            
        elif(fid == 8)  :
            cfg.drop_config_value(subgw.get_bulk_form_id(geocid,sugm.GEOCODER) + "Parms")
            subgw.display_bulk_geocoders(geocid,False)
         
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
    """
    * ---------------------------------------------------------
    * function : get a geocoder engine
    * 
    * parms :
    *  geocid    - geocoder id
    *  opstat    - operation status object
    *
    * returns : 
    *  geocoder engine 
    * --------------------------------------------------------
    """

    geolocator  =   None
    
    try :
            
        geocinitparms = sugw.get_geocoder_cmd_kwargs(sugm.GEOCODER,geocid)
        
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


def test_geocoder(geocid,gcparms) :
    """
    * ---------------------------------------------------------
    * function : test the geocoder connection and run sample
    * 
    * parms :
    *  geocid    - geocoder id
    *  gcparms   - geocoder parms
    *
    * returns : 
    *  N?A 
    * --------------------------------------------------------
    """

    print("test_geocoder",geocid,gcparms)
    
    opstat      =   opStatus()
    
    if(geocid == sugm.ArcGISId)              :  
        form    =   sugw.arcgis_geocoder_id
    elif(geocid == sugm.BingId)              :  
        form    =   sugw.bing_geocoder_id
    elif(geocid == sugm.GoogleId)            :  
        form    =   sugw.google_geocoder_id
    elif(geocid == sugm.OpenMapQuestId)      :  
        form    =   sugw.mapquest_geocoder_id
    elif(geocid == sugm.NominatimId)         :  
        form    =   sugw.nomin_geocoder_id
        
    cfg.set_config_value(form+"Parms",gcparms)

    opstat  =   sugw.validate_geocode_connect_parms(geocid) 
    
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



def run_geocoder_query(geocid, parms) :
    """
    * ---------------------------------------------------------
    * function : run a geocoder query operation
    * 
    * parms :
    *  inparms   - geocoder query parms
    *
    * returns : 
    *  N?A 
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    addresses   =   []
    coords      =   []
    
    sugw.validate_cmd_parms(sugm.QUERY,geocid,parms,opstat)
    
    if(not opstat.get_status()) :
        
        sugw.display_geocode_inputs(None,sugm.QUERY)
        
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
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.QUERY,geocid)
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
        
        sugw.display_geocode_inputs(geocid,sugm.QUERY) 
        
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


def get_bulk_query_parms(geocid,parms) :
    """
    * ---------------------------------------------------------
    * function : get the bulk query parms 
    * 
    * parms :
    *  geocid   - geocoder id
    *  parms    - geocoder input parms
    *
    * returns : 
    *  bulk query parms 
    * --------------------------------------------------------
    """
        
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



def run_geocoder_reverse(geocid,parms) :
    """
    * ---------------------------------------------------------
    * function : run a geocode reverse 
    * 
    * parms :
    *  inparms  - geocoder reverse input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    #geocid  =   inparms[1]
    #parms   =   inparms[2]
    opstat  =   opStatus()
    
    coords      =   []
    locations   =   []

    sugw.validate_cmd_parms(sugm.REVERSE,geocid,parms,opstat)
    
    if(not opstat.get_status()) :
        sugw.display_geocode_inputs(None,sugm.REVERSE)
        
        if(opstat.get_errorMsg() != "No Parms") :
            display_exception(opstat)
        
    else :
        
        clock = RunningClock()
        clock.start()

        geolocator = get_geocoder_engine(geocid,opstat)
        numresults   =  0
        
        if(opstat.get_status()) :
            
            try :
                
                queryparms = sugw.get_geocoder_cmd_kwargs(sugm.REVERSE,geocid)
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

                print("run_geocoder_reverse",queryparms)
                
                for i in range(len(coords)) :
                    if(len(queryparms) > 0) :
                        location = geolocator.reverse(coords[i], exactly_one=False)#**queryparms) 
                    else :
                        location = geolocator.reverse(coords[i]) 
                    
                    locations.append(location)
                print("run_geocoder_reverse",locations)        
            except Exception as e:
                opstat.store_exception("Error getting geocoder coords",e)
            
        clock.stop()

        sugw.display_geocode_inputs(geocid,sugm.REVERSE) 
        
        if(opstat.get_status()) :
            
            print("run_geocoder_reverse",numresults)
            
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




