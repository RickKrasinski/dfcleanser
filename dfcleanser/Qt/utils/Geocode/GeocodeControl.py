"""
# GeocoderControl 
"""

# -*- coding: utf-8 -*-

"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from signal import default_int_handler
from dfcleanser.common.common_utils import (opStatus, RunningClock, get_parms_for_input, is_column_in_df)

import dfcleanser.common.cfg as cfg
from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import SWGeocodeUtility_ID


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  Geocoding Validation methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 


def validate_arcgis_geocoder_parms(gparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate arcgis geocoder parms
    * 
    * parms :
    *  gparms  - arcgis geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_arcgis_geocoder_parms] gparms : \n  ",gparms))

    
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (arcgis_geocoder_id, arcgis_geocoder_idList)
    
    if(gparms is None) :

        gparms  =   cfg.get_config_value(arcgis_geocoder_id + "Parms")
        fparms  =   get_parms_for_input(gparms,arcgis_geocoder_idList)

    else :

        fparms  =   gparms

    if(len(fparms) > 0) :
        # if autheticated user,pw and agent must be defined
        # else all need to be blank
        if( (len(fparms[0]) > 0) or (len(fparms[1]) > 0) or (len(fparms[2]) > 0) ) :
            
            if(len(fparms[0]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Missing username parameter")
            elif(len(fparms[1]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("Missing password parameter")
            else :
                if(len(fparms[2]) == 0) :
                    fparms[2] = "my-application"
                
    else :

        opstat.set_status(False)
        opstat.set_errorMsg("no arcgis connect parameters")


def validate_bing_geocoder_parms(gparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate bing geocoder parms
    * 
    * parms :
    *  gparms  - bing geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
       add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_bing_geocoder_parms] gparms : \n  ",gparms))
   
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (bing_geocoder_id, bing_geocoder_idList)

    if(gparms is None) :

        gparms  =   cfg.get_config_value(bing_geocoder_id + "Parms")
        fparms  =   get_parms_for_input(gparms,bing_geocoder_idList)

    else :

        fparms  =   gparms
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_bing_geocoder_parms] fparms : \n  ",fparms))
    
    if(len(fparms) > 0) :
            
        if( len(fparms[0]) == 0 ) :

            opstat.set_status(False)
            opstat.set_errorMsg("Missing bing api_key parameter")
            
    else :

        opstat.set_status(False)
        opstat.set_errorMsg("Missing bing api_key parameter")



def validate_google_geocoder_parms(gparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate google geocoder parms
    * 
    * parms :
    *  gparms  - google geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
   
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_google_geocoder_parms] gparms : \n  ",gparms))
    
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (google_geocoder_id, google_geocoder_idList)
    
    if(gparms is None) :

        gparms  =   cfg.get_config_value(google_geocoder_id + "Parms")
        fparms  =   get_parms_for_input(gparms,google_geocoder_idList)

    else :

        fparms  =   gparms
     
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_google_geocoder_parms] fparms : \n  ",fparms))
   
    if(len(fparms) > 0) :
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No google api key defined")
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No google api key defined")


def validate_mapquest_geocoder_parms(gparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate mapquest geocoder parms
    * 
    * parms :
    *  gparms  - bing geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_mapquest_geocoder_parms] gparms : \n  ",gparms))
    
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (mapquest_geocoder_id,mapquest_geocoder_idList)
    
    if(gparms is None) :

        gparms  =   cfg.get_config_value(mapquest_geocoder_id + "Parms")
        fparms  =   get_parms_for_input(gparms,mapquest_geocoder_idList)

    else :

        fparms  =   gparms
     
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_mapquest_geocoder_parms] fparms : \n  ",fparms))
    
    if(len(fparms) > 0) :
            
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("Missing mapquest api_key parameter")
            
            cfg.set_config_value(mapquest_geocoder_id + "Parms",fparms)
            
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("Missing mapquest api_key parameter")


def validate_nominatim_geocoder_parms(gparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate nominatim geocoder parms
    * 
    * parms :
    *  gparms  - nominatim geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_nominatim_geocoder_parms] gparms : \n  ",gparms))
    
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (nomin_geocoder_id, nomin_geocoder_idList)

    if(gparms is None) :

        gparms  =   cfg.get_config_value(nomin_geocoder_id + "Parms")
        fparms  =   get_parms_for_input(gparms,nomin_geocoder_idList)

    else :

        fparms  =   gparms
     
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_nominatim_geocoder_parms] fparms : \n  ",fparms))
    
    if(len(fparms) > 0) :
    
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No Nominatum user_agent defined")
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("No Nominatum user_agent defined")


def validate_geocode_connect_parms(geocid,gcparms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_geocode_connect_parms] : ",geocid,"\n  ",gcparms))


    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import  (arcgis_geocoder_id, bing_geocoder_id, google_geocoder_id, mapquest_geocoder_id, nomin_geocoder_id, baidu_geocoder_id)
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import  (ArcGISId, BingId, GoogleId, OpenMapQuestId, NominatimId, BaiduId)

    if(geocid == ArcGISId)              :   form    =   arcgis_geocoder_id
    elif(geocid == BingId)              :   form    =   bing_geocoder_id
    elif(geocid == GoogleId)            :   form    =   google_geocoder_id
    elif(geocid == OpenMapQuestId)      :   form    =   mapquest_geocoder_id
    elif(geocid == NominatimId)         :   form    =   nomin_geocoder_id
        
    opstat  =   opStatus()
    
    if(not(gcparms is None)) :
        
        if(geocid == ArcGISId)         :   validate_arcgis_geocoder_parms(gcparms,opstat)
        elif(geocid == BingId)         :   validate_bing_geocoder_parms(gcparms,opstat)
        elif(geocid == GoogleId)       :   validate_google_geocoder_parms(gcparms,opstat)
        elif(geocid == OpenMapQuestId) :   validate_mapquest_geocoder_parms(gcparms,opstat)
        elif(geocid == NominatimId)    :   validate_nominatim_geocoder_parms(gcparms,opstat)
            
    else :
        
        if(not(geocid == ArcGISId)) :
            opstat.set_status(False)
            opstat.set_errorMsg("No geocoder connect parms defined")

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[test_geocoder][validate_geocode_connect_parms][end] : geocid : optat ",geocid,opstat.get_status()))
        
    return(opstat)


def test_geocoder(geocid, gcparms, gmode=None):
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
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
        add_debug_to_log("DataExport",print_to_string("[GeocodeControl][test_geocoder] geocid gcparms : ",geocid, gcparms))
    
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import INTERACTIVE
    if(gmode is None) :
        gmode   =  INTERACTIVE 

    opstat = opStatus()

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId, BingId, BaiduId,  GoogleId, OpenMapQuestId, NominatimId)
    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (arcgis_geocoder_id, bing_geocoder_id, baidu_geocoder_id, google_geocoder_id, 
                                                            mapquest_geocoder_id, nomin_geocoder_id)


    if(geocid == ArcGISId)          :   form = arcgis_geocoder_id

    elif(geocid == BingId)          :   
        if(gmode   == INTERACTIVE) :
            form    =   bing_geocoder_id
        else :
            from dfcleanser.Qt.utils.Geocode.BulkGeocode import bing_bulk_geocoder_id
            form    =  bing_bulk_geocoder_id

    elif(geocid == BaiduId)         :   form = baidu_geocoder_id
    elif(geocid == GoogleId)        :   form = google_geocoder_id
    elif(geocid == OpenMapQuestId)  :   form = mapquest_geocoder_id
    elif(geocid == NominatimId)     :   form = nomin_geocoder_id

    opstat = validate_geocode_connect_parms(geocid,gcparms)

    if(not (opstat.get_status())):

        title       =   "dfcleanser exception"       
        status_msg  =   "[invalid geocoder connect parms]"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(opstat)

    else:
    
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            add_debug_to_log("DataExport",print_to_string("[GeocodeControl][test_geocoder] get geolocator : "))

        try:
            geolocator = get_geocoder_engine(geocid, opstat)
        except Exception as e:

            opstat.set_status(False)
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[unable to connect to geocoder] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                query = "11111 Euclid Ave, Cleveland OH "

                try:
                    address, (latitude, longitude) = geolocator.geocode(query)
                except Exception as e:

                    opstat.set_status(False)
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[unable to get geocoder info] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

    if(opstat.get_status())  :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            add_debug_to_log("DataExport",print_to_string("[GeocodeControl] got good geolocator : "))


        from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import (arcgis_geocoder_idList, bing_geocoder_idList, baidu_geocoder_idList, google_geocoder_idList,
                                                                mapquest_geocoder_idList, nomin_geocoder_idList)

        if(geocid == ArcGISId)          :   idlist = arcgis_geocoder_idList

        elif(geocid == BingId)          :   
            if(gmode   == INTERACTIVE) :
                idlist    =   bing_geocoder_idList
            else :
                from dfcleanser.Qt.utils.Geocode.BulkGeocode import bing_bulk_geocoder_idList
                idlist    =  bing_bulk_geocoder_idList

        elif(geocid == BaiduId)         :   idlist = baidu_geocoder_idList
        elif(geocid == GoogleId)        :   idlist = google_geocoder_idList
        elif(geocid == OpenMapQuestId)  :   idlist = mapquest_geocoder_idList
        elif(geocid == NominatimId)     :   idlist = nomin_geocoder_idList

        connect_parms   =   get_parms_for_input(gcparms,idlist)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            add_debug_to_log("DataExport",print_to_string("[GeocodeControl] connect_parms : ",gcparms))

        from dfcleanser.common.cfg import set_config_value

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            add_debug_to_log("DataExport",print_to_string("[GeocodeControl] set_config_value : ",form+"Parms",gcparms))


        set_config_value(form+"Parms",gcparms)

    return(opstat)
    


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common geocoder helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_geocoder_cmd_kwargs(ptype,geocid,geoparms=None) :
    """
    * ---------------------------------------------------------
    * function : get the previously stored cfg kwargs for geocoding
    * 
    * parms :
    *  ptype   - geocode type INIT or QUERY or REVERSE
    *  geocid  - geocoder id
    *
    * returns : 
    *  geocoding kwargs from cfg
    * --------------------------------------------------------
    """

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        add_debug_to_log("DataExport",print_to_string("[get_geocoder_cmd_kwargs] ptype : geocid : ",ptype,geocid,"\n  ",geoparms))


    import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm
    import dfcleanser.Qt.utils.Geocode.GeocodeWidgets as gcw
    
    if(geoparms is None) :

        if(ptype == gcm.GEOCODER)     : geoparms = cfg.get_config_value(gcm.get_form_id(geocid,gcm.GEOCODER) + "Parms")
        elif(ptype == gcm.QUERY)      : geoparms = cfg.get_config_value(gcm.get_form_id(geocid,gcm.QUERY) + "Parms")
        elif(ptype == gcm.REVERSE)    : geoparms = cfg.get_config_value(gcm.get_form_id(geocid,gcm.REVERSE) + "Parms")
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        add_debug_to_log("DataExport",print_to_string("[get_geocoder_cmd_kwargs] ptype : geocid : ",geoparms))
    
    if(ptype == gcm.GEOCODER) :

        if(geocid == gcm.GoogleId)              : labelList       =   gcw.google_geocoder_labelList 
        elif(geocid == gcm.BingId)              : labelList       =   gcw.bing_geocoder_labelList 
        elif(geocid == gcm.OpenMapQuestId)      : labelList       =   gcw.mapquest_geocoder_labelList 
        elif(geocid == gcm.NominatimId)         : labelList       =   gcw.nomin_geocoder_labelList 
        elif(geocid == gcm.ArcGISId)            : labelList       =   gcw.arcgis_geocoder_labelList 
        elif(geocid == gcm.BaiduId)             : labelList       =   gcw.baidu_geocoder_labelList 

    elif(ptype == gcm.QUERY) :

        if(geocid == gcm.GoogleId)              : labelList       =   gcw.google_query_labelList 
        elif(geocid == gcm.BingId)              : labelList       =   gcw.bing_query_labelList 
        elif(geocid == gcm.OpenMapQuestId)      : labelList       =   gcw.mapquest_query_labelList 
        elif(geocid == gcm.NominatimId)         : labelList       =   gcw.nomin_query_labelList 
        elif(geocid == gcm.ArcGISId)            : labelList       =   gcw.arcgis_query_labelList 
        elif(geocid == gcm.BaiduId)             : labelList       =   gcw.baidu_query_labelList 
        
    elif(ptype == gcm.REVERSE) :

        if(geocid == gcm.GoogleId)              : labelList       =   gcw.google_reverse_labelList 
        elif(geocid == gcm.BingId)              : labelList       =   gcw.bing_reverse_labelList
        elif(geocid == gcm.OpenMapQuestId)      : labelList       =   gcw.mapquest_reverse_labelList
        elif(geocid == gcm.NominatimId)         : labelList       =   gcw.nomin_reverse_labelList 
        elif(geocid == gcm.ArcGISId)            : labelList       =   gcw.arcgis_reverse_labelList 
        elif(geocid == gcm.BaiduId)             : labelList       =   gcw.baidu_reverse_labelList 
 
    geokwargs = {}

    if(geoparms != None) :
        for i in range(len(geoparms)) : 
            if(len(geoparms[i]) > 0) :
                if(geoparms[i] == 'False') :
                    geokwargs.update({labelList[i]:False}) 
                elif(geoparms[i] == 'True') :
                    geokwargs.update({labelList[i]:True}) 
                else :    
                    geokwargs.update({labelList[i]:geoparms[i]})

    if(len(geokwargs) == 0) :
        return(None)
    else :
        return(geokwargs)




"""
#--------------------------------------------------------------------------
#  get geocoder engine
#--------------------------------------------------------------------------
"""

def get_geocoder_engine(geocid, opstat):
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

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
        add_debug_to_log("DataExport",print_to_string("[get_geocoder_engine] ",str(geocid)))

    geolocator = None

    import geopy

    try:

        import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm

        geocinitparms = get_geocoder_cmd_kwargs(gcm.GEOCODER, geocid)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
            add_debug_to_log("DataExport",print_to_string("[get_geocoder_engine][get_geocoder_cmd_kwargs] ",geocinitparms))   

        if(geocid == gcm.GoogleId):
            from geopy.geocoders import GoogleV3
            if(geocinitparms == None):
                geolocator = GoogleV3()
            else:
                geolocator = GoogleV3(**geocinitparms)

        elif(geocid == gcm.BingId):
            from geopy.geocoders import Bing
            if(geocinitparms == None):
                geolocator = Bing()
            else:
                geolocator = Bing(**geocinitparms)

        elif(geocid == gcm.BaiduId):
            from geopy.geocoders import Baidu
            if(geocinitparms == None):
                geolocator = Baidu()
            else:
                geolocator = Baidu(**geocinitparms)

        elif(geocid == gcm.OpenMapQuestId):
            from geopy.geocoders import OpenMapQuest
            if(geocinitparms == None):
                geolocator = OpenMapQuest()
            else:
                geolocator = OpenMapQuest(**geocinitparms)

        elif(geocid == gcm.NominatimId):
            from geopy.geocoders import Nominatim
            if(geocinitparms == None):
                geolocator = Nominatim()
            else:
                geolocator = Nominatim(**geocinitparms)

        elif(geocid == gcm.ArcGISId):
            from geopy.geocoders import ArcGIS
            if(geocinitparms == None):
                geolocator = ArcGIS()
            else:
                geolocator = ArcGIS(**geocinitparms)

    except Exception as e:
                
        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[failure to get geocoder engine] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(geolocator)


def validate_cmd_parms(ptype,geocid,gqparms,opstat) :
    """
    * ---------------------------------------------------------
    * function : validate command parms
    * 
    * parms :
    *  ptype   - geocode type QUERY or REVERSE
    *  geocid  - geocoder id
    *  gqparms - geocoder parms
    *  opstat  - processing status 
    *
    * returns : 
    *  valid status of parms
    * --------------------------------------------------------
    """

    import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm
    import dfcleanser.Qt.utils.Geocode.GeocodeWidgets as gcw

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")) :
        add_debug_to_log("DataExport",print_to_string("[validate_cmd_parms] gqparms : \n  ",gqparms))
   
    if(ptype == gcm.GEOCODER) :
    
        if(geocid == gcm.ArcGISId) :
            return(validate_arcgis_geocoder_parms(gqparms,opstat))
        
        elif(geocid == gcm.GoogleId) :
            return(validate_google_geocoder_parms(gqparms,opstat))
        
        elif(geocid == gcm.NominatimId) :
            return(validate_nominatim_geocoder_parms(gqparms,opstat))
        
        elif(geocid == gcm.BingId) :
            return(validate_bing_geocoder_parms(gqparms,opstat))
            
        elif(geocid == gcm.OpenMapQuestId) :
            return(validate_mapquest_geocoder_parms(gqparms,opstat))
        
        elif(geocid == gcm.BaiduId) :
            return(validate_baidu_geocoder_parms(gqparms,opstat))
            
    elif(ptype == gcm.QUERY) :

        if(geocid == gcm.GoogleId)              :   reqList         =   gcw.google_query_reqList 
        elif(geocid == gcm.BingId)              :   reqList         =   gcw.bing_query_reqList 
        elif(geocid == gcm.OpenMawQuestId)      :   reqList         =   gcw.mapquest_query_reqList 
        elif(geocid == gcm.NominatimId)         :   reqList         =   gcw.nomin_query_reqList 
        elif(geocid == gcm.ArcGISId)            :   reqList         =   gcw.arcgis_query_reqList 
        elif(geocid == gcm.BaiduId)             :   reqList         =   gcw.baidu_query_reqList 
        else :

            opstat.set_status(False)
            title       =   "dfcleanser exception"       
            status_msg  =   "[Geocode not supportd]"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

    elif(ptype == gcm.REVERSE) :

        if(geocid == gcm.GoogleId)              :   reqList         =   gcw.google_reverse_reqList 
        elif(geocid == gcm.BingId)              :   reqList         =   gcw.bing_reverse_reqList 
        elif(geocid == gcm.ArcGISId)            :   reqList         =   gcw.arcgis_reverse_reqList 
        elif(geocid == gcm.OpenMapQuestId)      :   reqList         =   gcw.mapquest_reverse_reqList 
        elif(geocid == gcm.NominatimId)         :   reqList         =   gcw.nomin_reverse_reqList 
        elif(geocid == gcm.BaiduId)             :   reqList         =   gcw.baidu_reverse_reqList 
        else :

            opstat.set_status(False)
            title       =   "dfcleanser exception"       
            status_msg  =   "[Geocode not supportd]"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
       
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
        add_debug_to_log("DataExport",print_to_string("[validate_cmd_parms(] : reqList ", reqList))
       
    missingParm     =   False
        
    cfg_key = gcm.get_form_id(geocid,ptype) + "Parms"
    
    if(len(gqparms) > 0) :
    
        for i in range(len(reqList)) :
            if(not missingParm) :
                if(len(gqparms[i]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Required parm " + str(i) + " not defined")
                    missingParm = True
                    break

    else :

        opstat.set_status(False)
        title       =   "dfcleanser exception"       
        status_msg  =   "[no parms defined]"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)



def run_geocoder_query(geocid, parms):
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

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[run_geocoder_query]", geocid,"\n  ", parms))

    opstat          = opStatus()
    coords          = []
    latest_results  = []

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY

    validate_cmd_parms(QUERY, geocid, parms, opstat)

    if(not opstat.get_status()):

        title       =   "dfcleanser error"       
        status_msg  =   "[" + opstat.get_errorMsg() + "]"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

    else:

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
            add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] parms ok : \n  ",parms))

        queryparms = None
        numresults = 0
        geolocator = get_geocoder_engine(geocid, opstat)

        import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm

        if(opstat.get_status()):

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                add_debug_to_log("DataExport",print_to_string("[run_geocoder_query][got geocoder engine]"))

            try:

                queryparms = get_geocoder_cmd_kwargs(QUERY, geocid, parms)
            
                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] queryparms : \n          ",queryparms))

                timeout     =   queryparms.get("timeout")
                if(len(timeout) > 0 ) :
                     queryparms.update({"timeout" : int(timeout)}) 
                else :  
                    queryparms.update({"timeout" : 1})   

                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] : queryparms\n  ", queryparms))

                addresses_to_geocode = []
                addr_parm = "address(x)"

                for i in range(5):

                    addr_key    =   addr_parm.replace("x", str(i+1))
                    address     =   queryparms.get(addr_key)

                    if(len(address) > 0):

                        addresses_to_geocode.append(address)
                        queryparms.pop(addr_key,None)

                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_query][addresses_to_geocode] \n    ",addresses_to_geocode))

                if(geocid == gcm.BingId):

                    user_culture    =   queryparms.get("culture")
                    csep            =   user_culture.find(":")
                    culture         =   user_culture[:csep+1]
                    queryparms.update({"culture": culture})


                    user_loc        =   queryparms.get("user_location")
                    if(not (user_loc is None) ):

                        from dfcleaser.Qt.DFFCDataStores import get_valid_geopoint
                        geopoint        =   get_valid_geopoint(user_loc)

                        if(geopoint is None) :
                         
                            # display status message
                            title       =   "dfcleanser error"       
                            status_msg  =   "[Bing Query] user location not valid geopoint "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                            display_error_msg(title,status_msg)
                        
                            queryparms.update({"user_location": None})

                        else :
                            queryparms.update({"user_location": geopoint})

                    else :
                        queryparms.update({"user_location": None})    
                    
                    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                        add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] : end bingid \n  ", queryparms))

                elif(geocid == gcm.GoogleId):

                    bounds        =   queryparms.get("bounds")
                    if(not (bounds is None) ):

                        # bounds must be 2 geopoints
                        from ast import literal_eval
                        bounds_list     =   literal_eval(bounds)

                        if(not (len(bounds_list) == 2)) :

                            # display status message
                            title       =   "dfcleanser error"       
                            status_msg  =   "[Google Query] bounds needs two geopints "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                            display_error_msg(title,status_msg)
                        
                            queryparms.update({"bounds": None})

                        else :
                            
                            bounds_ok   =   True
                            from dfcleaser.Qt.DFFCDataStores import get_valid_geopoint
                            for k in range(len(bounds_list)) :

                                geopoint        =   get_valid_geopoint(bounds_list[k])   

                                if(geopoint is None) :
                         
                                    # display status message
                                    title       =   "dfcleanser error"       
                                    status_msg  =   "[Google Query] bounds " + str(k) + " is not valid geopoint "
                                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                                    display_error_msg(title,status_msg)
                        
                                    queryparms.update({"bounds": None})
                                    bounds_ok   =   False
                                    break

                            if(bounds_ok) :
                                queryparms.update({"bounds": bounds})

                            else :
                                queryparms.update({"bounds": None})    

                    if(queryparms.get("region") == "None"):
                        queryparms.pop("region")

                    else:

                        user_region     =   queryparms.get("region")
                        csep            =   user_culture.find(":")
                        region          =   user_culture[:csep+1]
                        queryparms.update({"region": region})
 
                    if(queryparms.get("language") == "English"):
                        queryparms.pop("language")

                    else:

                        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
                        lang_codes = get_Dict("Language_Codes")
                        lang = lang_codes.get(queryparms.get("language"))
                        queryparms.update({"language": lang})

                numresults  =   queryparms.get("number_of_results")

                if(numresults is None) :
                    queryparms.update({"exactly_one": True}) 
                else :  
                    numresults  =   int(numresults) 
                    if(numresults > 1):
                        queryparms.update({"exactly_one": False})
                    else:
                        queryparms.update({"exactly_one": True})

                queryparms.pop("number_of_results",None)
                            
                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] : queryparms \n         ", queryparms))

                # -----------------------------#
                # for each address geocode it  #
                # -----------------------------#
                for i in range(len(addresses_to_geocode)):

                    if(len(queryparms) > 0):
                        location = geolocator.geocode(addresses_to_geocode[i], **queryparms)
                    else:
                        location = geolocator.geocode(addresses_to_geocode[i])

                    if(location is None):
                        latest_results.append(None)
                    else:

                        if(type(location) == list):
                            for k in range(len(location)):

                                latest_result = [addresses_to_geocode[i],location[k].address,location[k].latitude,location[k].longitude]
                                
                                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] latest_result \n        ", latest_result))
                                
                                latest_results.append(latest_result)

                        else:

                            latest_results.append([addresses_to_geocode[i],location.address,location.latitude,location.longitude])

            except Exception as e:

                opstat.set_status(False)

                user_loc        =   queryparms.get("user_location")
                from dfcleaser.Qt.DFFCDataStores import get_valid_geopoint
                geopoint        =   get_valid_geopoint(user_loc)

                if(geopoint is None) :
                        
                    queryparms.update({"user_location": None})
                    # display status message
        
                    title       =   "dfcleanser error"       
                    status_msg  =   "[Bing Query] user location not valid geopoint "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)

                else :
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[Error getting geocoder coords]"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)


        # -------------------------------------- #
        # ----- process and format results ----- #
        # -------------------------------------- #
        if(opstat.get_status()):

            last_user_addr  =   ""
            drop_user_addr  =   False

            for i in range(len(latest_results)) :

                if(latest_results[i][0] == last_user_addr) :
                    drop_user_addr  =   True

                last_user_addr  =  latest_results[i][0] 
                if(drop_user_addr) :    
                    latest_results[i][0] = ""
                drop_user_addr  =   False
            
            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_DETAILS")):
                add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] : latest_results \n         ", latest_results))

            return(latest_results)
        
        else :
            
            return(None)



def run_geocoder_reverse(geocid, parms):
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

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] geocoderid : parms ", geocid, "\n          ", parms))

    opstat          = opStatus()
    addresses       = []
    latest_results  = []

    import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm

    validate_cmd_parms(gcm.REVERSE, geocid, parms, opstat)

    if(not opstat.get_status()):
        
        title       =   "dfcleanser error"       
        status_msg  =   "[invalid geocode reverse parms]"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

    else:

        geolocator = get_geocoder_engine(geocid, opstat)

        if(opstat.get_status()):

            try:

                reverseparms = get_geocoder_cmd_kwargs(gcm.REVERSE, geocid, parms)

                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : reverseparms \n            ",reverseparms))

                timeout     =   reverseparms.get("timeout")
                if(len(timeout) > 0 ) :
                    reverseparms.update({"timeout" : int(timeout)}) 
                else :  
                    reverseparms.update({"timeout" : 1})   

                num_results     =   reverseparms.get("number_of_results")
                if(num_results is None) :
                    num_results     =   1
                else :
                    num_results     =   int(num_results)

                if(num_results > 1):
                    reverseparms.update({"exactly_one": False})
                else:
                    reverseparms.update({"exactly_one": True})

                reverseparms.pop("number_of_results",None)
 
                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : final reverseparms \n          ",reverseparms))

                coords_to_geocode = []
                coord_parm = "latitude_longitude(x)"

                for i in range(5):

                    coord_key = coord_parm.replace("x", str(i+1))
                    coord = reverseparms.get(coord_key)

                    if(not (coord is None)):

                        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
                        new_geopoint    =   get_geopoint_from_string(coord)

                        if(not (new_geopoint is None)) :

                            coords_to_geocode.append(new_geopoint)
                            reverseparms.pop(coord_key)

                        else :

                            opstat.set_status(False)
                            title       =   "dfcleanser exception"       
                            status_msg  =   "Latitude_Longitude(" + str(i) + " invalid\n" + "format is : [Latitude,Longitude]"
                            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                            display_error_msg(title,status_msg)

                            return(None)
                 
                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : coords_to_geocode ",coords_to_geocode))

                # get other oarms per encoder
                if(geocid == gcm.GoogleId):

                    if(reverseparms.get("language") == "English"):
                        reverseparms.pop("language")

                    else:

                        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
                        lang_codes = get_Dict("Google_Language_Codes")
                        lang = lang_codes.get(reverseparms.get("language"))
                        reverseparms.update({"language": lang})

                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : num_results : ",num_results, "\n", reverseparms))

                reverse_results = []

                # -------------------------------------- #
                # --- for each coordinate geocode it --- #
                # -------------------------------------- #
                for i in range(len(coords_to_geocode)):

                    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                        add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : coords_to_geocode[", str(i), "]", coords_to_geocode[i]))

                    try :

                        if(len(reverseparms) > 0):
                            location = geolocator.reverse(coords_to_geocode[i], **reverseparms)
                        else:
                            location = geolocator.reverse(coords_to_geocode[i])

                    except Exception as e :

                        opstat.set_status(False)
                        title       =   "dfcleanser exception"       
                        status_msg  =   "[unable to connect to google geocoder] error "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)

                    if(location is None):

                        title       =   "dfcleanser exception"       
                        status_msg  =   "[invalid lat_lng(" + str(i) + ") coords]"
                        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                        display_error_msg(title,status_msg)

                    else:

                        if(type(location) == list):

                            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                                add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] : coords_to_geocode[", i, "] len :  ", type(location), len(location)))

                            for k in range(len(location)):
                                
                                latest_result = [coords_to_geocode[i], location[k].address, location[k].latitude,location[k].longitude]
                                latest_results.append(latest_result)

                            addresses.append(location)

                        else:

                            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                                add_debug_to_log("DataExport",print_to_string("[run_geocoder_query] : location ", type(location), len(location), location))

                            new_results     =   [coords_to_geocode[i],location.address,location.latitude,location.longitude]
                            latest_results.append(new_results)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[Error getting geocoder addresses]"
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[run_geocoder_reverse] latest_results ", len(latest_results)))
            for p in range(len(latest_results)):
                add_debug_to_log("DataExport",print_to_string("  latest_results[", p, "] : ", latest_results[p]))

        # -------------------------------------- #
        # ----- process and format results ----- #
        # -------------------------------------- #
        if(opstat.get_status()):

            last_coords = ""
            final_results = []
            total_coords = 0

            for i in range(len(latest_results)):

                if(not (latest_results[i][0] == last_coords)):

                    last_coords = latest_results[i][0]
                    total_coords = total_coords + 1
                    current_address_total = 1

                    new_result = ["(" + str(total_coords) + ") : " + str(latest_results[i][0]), latest_results[i][1],latest_results[i][2], str(latest_results[i][3])]
                    final_results.append(new_result)

                else:

                    current_address_total = current_address_total + 1

                    if(1):#current_address_total <= numresults):
                        new_result = ["",latest_results[i][1],latest_results[i][2], str(latest_results[i][3])]
                        final_results.append(new_result)

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                add_debug_to_log("DataExport",print_to_string("final_results ", len(final_results)))
                for p in range(len(final_results)):
                    add_debug_to_log("DataExport",print_to_string("final_results[", p, "] : ", final_results[p]))

            return(final_results)
        
        else :

            return(None)



# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
#                       Geocoding Center Point Methods                      #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

def get_geocode_center(geocoords,opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get the center point of a list of [lat,lng] locations
    * 
    * parms :
    *  geocoords     - geecode locations list
    *
    * returns : 
    *    center point if no exception
    *    opStatus object if exception
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    import math
    
    try :
        
        if(len(geocoords) > 0) :
            
            x = float(0)
            y = float(0)
            z = float(0)
            
            for i in range(len(geocoords)) :
                
                latitude    =   geocoords[i][0] * math.pi / 180
                longitude   =   geocoords[i][1] * math.pi / 180

                try :

                    x   =   x + math.cos(latitude) * math.cos(longitude)
                    y   =   y + math.cos(latitude) * math.sin(longitude)
                    z   =   z + math.sin(latitude)
                
                except :
                
                    opstat.set_status(False)
                    opstat.set_errorMsg("Calculate Geocode Center x,y,z Exception : " + str(sys.exc_info()[0].__name__))
                    return(None)
                    
            x   =   x / len(geocoords)
            y   =   y / len(geocoords)
            z   =   z / len(geocoords)
            
            centralLongitude    =   math.atan2(y,x)
            centralSquareRoot   =   math.sqrt(x * x + y * y)
            centralLatitude     =   math.atan2(z, centralSquareRoot)
            
            centralLatitude     =   round((centralLatitude * 180 / math.pi),5)
            centralLongitude    =   round((centralLongitude * 180 / math.pi),5)
            
            return((centralLatitude,centralLongitude))
            
        else :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Calculate Geocode Center Error : geocoords list is empty")
            return(None)
            
    except :
        
        opstat.set_status(False)
        opstat.set_errorMsg("Calculate Geocode Center Exception : " + str(sys.exc_info()[0].__name__))
        return(None)


# ------------------------------------------------------------------------- #
#                     Geocode Center Point for user list                    #
# ------------------------------------------------------------------------- #

def process_calculate_center_pt(parms):

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_center_pt] : locations 1 \n ",parms[0]))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_center_pt] : locations 2 \n ",parms[1]))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_center_pt] : locations 3 \n ",parms[2]))

    #import json
    points  =   []

    for i in range(len(parms[0])) :
        if(len(parms[0][i]) > 0) :
            try :
                from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
                new_point       =   parms[0][i].replace("\\n","")
                current_point   =   get_geopoint_from_string(new_point)
                points.append(current_point)
            except :
                
                from PyQt5 import Qt, QtCore
                from PyQt5.QtWidgets import QMessageBox
                dlg = QMessageBox()
                dlg.setTextFormat(Qt.RichText)
                dlg.setWindowTitle("Get Center Point")
                dlg.setText("Location_1 LatLng : "+str(i) + " is invalid \n Continue Processing")
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                button = dlg.exec()

                if(button == QMessageBox.No) :
                    return(None)

    for i in range(len(parms[1])) :
        if(len(parms[1][i]) > 0) :
            try :
                new_point       =   parms[1][i].replace("\\n","")
                current_point   =   get_geopoint_from_string(new_point)
                points.append(current_point)
            except :

                from PyQt5.QtWidgets import QMessageBox
                dlg = QMessageBox()
                dlg.setTextFormat(Qt.RichText)
                dlg.setWindowTitle("Get Center Point")
                dlg.setText("Location_2 LatLng : "+str(i) + " is invalid \n Continue Processing")
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                button = dlg.exec()

                if(button == QMessageBox.No) :
                    return(None)

    for i in range(len(parms[2])) :
        if(len(parms[2][i]) > 0) :
            try :
                new_point       =   parms[2][i].replace("\\n","")
                current_point   =   get_geopoint_from_string(new_point)
                points.append(current_point)
            except :

                from PyQt5.QtWidgets import QMessageBox
                dlg = QMessageBox()
                dlg.setTextFormat(Qt.RichText)
                dlg.setWindowTitle("Get Center Point")
                dlg.setText("Location_3 LatLng : "+str(i) + " is invalid \n Continue Processing")
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                button = dlg.exec()

                if(button == QMessageBox.No) :
                    return(None)
                
    if(len(points)<1) :

        title       =   "dfcleanser error"       
        status_msg  =   "No valid latlng locations defined"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
    
    else :

        from dfcleanser.common.common_utils import opStatus
        opstat          =   opStatus()
        center_point    =   get_geocode_center(points,opstat)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("center_point",center_point))

    if(opstat.get_status()) :
        return(center_point)
    else :
        return(None)


# ------------------------------------------------------------------------- #
#             Change a df column into a list of geocode points              #
# ------------------------------------------------------------------------- #

def get_geocode_points_from_df(df_title,col_name) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[get_geocode_points_from_df] df_title : col_name : ",df_title,col_name))

 
    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(df_title)

    if(df is None) :

        title       =   "dfcleanser error"       
        status_msg  =   "dataframe selected is invalid"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)

    separate_lat_lng_columns    =   False

    try :

        if(col_name.find("[") < 0) :

            df_lat_lng_col_name             =   col_name
            df_latitude_col_name            =   None
            df_longitude_col_name           =   None

            separate_lat_lng_columns        =   False

        else :

            colname     =  col_name.replace("[","") 
            colname     =  colname.replace("]","")  
            colname     =   colname.split(",")

            df_lat_lng_col_name         =   None
            df_latitude_col_name        =   colname[0]
            df_longitude_col_name       =   colname[1]
            
            separate_lat_lng_columns    =   True

    except :

        title       =   "dfcleanser error"       
        status_msg  =   "column_name" + col_name + " to get geocode points for is invalid"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("df_lat_lng_col_name",df_lat_lng_col_name))
        add_debug_to_log("DataExport",print_to_string("df_latitude_col_name",df_latitude_col_name))
        add_debug_to_log("DataExport",print_to_string("df_longitude_col_name",df_longitude_col_name))
        add_debug_to_log("DataExport",print_to_string("separate_lat_lng_columns",df_longitude_col_name))

    geocode_pts             =   []
    total_error_points      =   0

    if(not(separate_lat_lng_columns)) :

        df_points   =   df[df_lat_lng_col_name].tolist()

        for i in range(len(df_points)) :

            current_point   =   df_points[i]

            geopoint     =  current_point.replace("[","") 
            geopoint     =  geopoint.replace("]","")  
            geopoint     =  geopoint.replace("(","") 
            geopoint     =  geopoint.replace(")","")           
            geopoint     =  geopoint.split(",")

            try :

                new_lat     =   float(geopoint[0])
                new_lng     =   float(geopoint[1])

                geocode_pts.append((new_lat,new_lng))  

            except :
                total_error_points  =   total_error_points + 1

    else :

        df_lats     =   df[df_latitude_col_name].tolist()
        df_lngs     =   df[df_longitude_col_name].tolist()

        for i in range(len(df)) :

            try :
                geocode_pts.append((float(df_lats[i],float(df_lngs[i]))))    
            except :
                total_error_points  =   total_error_points + 1

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("len(geocode_pts),total_error_points))
        if(len(geocode_pts) > 0) :
            for i in range(5) :
                add_debug_to_log("DataExport",print_to_string(geocode_pts[i]))

    return([geocode_pts,total_error_points])



# ------------------------------------------------------------------------- #
#                   Geocode Center Point for a df columnt                   #
# ------------------------------------------------------------------------- #

def process_calculate_df_center_pt(parms):

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_center_pt] : parms \n ",parms))

    dataframe_title         =   parms[0]
    df_col_names            =   parms[1]

    geocode_points_data     =   get_geocode_points_from_df(dataframe_title,df_col_names)

    if(not (geocode_points_data is None)) :

        geocode_points  =   geocode_points_data[0]
        total_errors    =   geocode_points_data[1]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_center_pt] : len geocode_points : ",len(geocode_points)," errors : ",total_errors))

        if( (len(geocode_points) > 0) and (total_errors < 200) ) :

            from dfcleanser.common.common_utils import opStatus
            opstat          =   opStatus()
            center_point    =   get_geocode_center(geocode_points,opstat)

            if(opstat.get_status()) :
                
                if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                    add_debug_to_log("DataExport",print_to_string("[process_calculate_df_center_pt] center_point : ",center_point,type(center_point)))
                    
                return(center_point)
            
            else :

                title       =   "dfcleanser error"       
                status_msg  =   "calculating center point error"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)

        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_calculate_df_center_pt] errors"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
        
    else :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_calculate_df_center_pt] no geopoints"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)



# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
#                         Geocoding Distance Methods                        #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #




# ------------------------------------------------------------------------- #
#           calculate distance method between singleton coords              #
# ------------------------------------------------------------------------- #

def get_distance(from_loc, to_loc, distance_units, algorithm, elipsoid, opstat):
    """
    * ---------------------------------------------------------
    * function : calculate the dist betweern coords - singleton
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    from geopy import distance

    calc_distance = 0

    try :

        if(algorithm == "geodesic"):

            if(distance_units == "km"):
                if(not(elipsoid == "WGS-84")):
                    calc_distance = distance.geodesic(from_loc, to_loc, elipsoid=elipsoid).km
                else:
                    calc_distance = distance.geodesic(from_loc, to_loc).km
            else:
                if(not(elipsoid == "WGS-84")):
                    calc_distance = distance.geodesic(from_loc, to_loc, elipsoid=elipsoid).miles
                else:
                    calc_distance = distance.geodesic(from_loc, to_loc).miles

        elif(algorithm == "great_circle"):

            if(distance_units == "km"):
                calc_distance = distance.great_circle(from_loc, to_loc).km
            else:
                calc_distance = distance.great_circle(from_loc, to_loc).miles

        else:

            opstat.set_status(False)
            opstat.set_errorMsg("Invalid geocoding algorithm : " + str(algorithm))

    except Exception as e:

        opstat.set_status(False)

        add_debug_to_log("DataExport",print_to_string("from loc",from_loc,to_loc))
            
        title       =   "dfcleanser exception"       
        status_msg  =   "Error calculating distances "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)



    return(calc_distance)



# ------------------------------------------------------------------------- #
#      calculate distance method between lists of from and to coords        #
# ------------------------------------------------------------------------- #

def calculate_geocode_distances(from_locs_list, to_locs_list, distance_units, algorithm, elipsoid, opstat):
    """
    * ---------------------------------------------------------
    * function : calculate the dist betweern coords - list of 
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[calculate_geocode_distances] : parms  ",len(from_locs_list),len(to_locs_list),distance_units, algorithm, elipsoid))

    distances = []

    try:

        if(1):#type(from_locs_list[0]) == list):

            for i in range(len(from_locs_list)):
                calc_distance = get_distance(from_locs_list[i], to_locs_list[i], distance_units, algorithm, elipsoid, opstat)
                calc_distance = round(calc_distance,3)
                distances.append(calc_distance)

        else:

            calc_distance = get_distance(from_locs_list, to_locs_list, distance_units, algorithm, elipsoid, opstat)
            calc_distance = round(calc_distance,3)
            distances.append(calc_distance)

    except Exception as e:
        #opstat.set_status(False)

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "Error calculating distances "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

        #opstat.store_exception("Error calculating distances", e)

    return(distances)


# ------------------------------------------------------------------------- #
#                   process calculate distance inputs                       #
# ------------------------------------------------------------------------- #

def process_calculate_distances(point_type,parms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : point_tyep ",point_type))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : from locations \n ",parms[0]))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : to locations \n ",parms[1]))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : alg parms \n ",parms[2]))

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS
    if(point_type == ADDRESS) :

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()
        if(geocoderid is None) :

            title       =   "dfcleanser error"       
            status_msg  =   "No geocoder defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
        
        else :

            query_run_parms     =   []
            import dfcleanser.Qt.utils.Geocode.GeocodeModel as gcm
            if(geocoderid == gcm.ArcGISId) :
                
                query_run_parms.append("1")                 # only one result
                query_run_parms.append("20")                # timeout
            
            elif(geocoderid == gcm.GoogleId) :
                
                query_run_parms.append("1")                 # only one result
                query_run_parms.append("20")                # timeout
                query_run_parms.append("")                  # bounds
                query_run_parms.append("United States")     # region
                query_run_parms.append("")                  # components
                query_run_parms.append("English")           # language
                query_run_parms.append("False")             # sensor                
            
            elif(geocoderid == gcm.BingId) :
                
                query_run_parms.append("1")                 # only one result
                query_run_parms.append("20")                # timeout
                query_run_parms.append("")                  # user location
                query_run_parms.append("United States")     # culture
                query_run_parms.append("False")             # neighborhood
                query_run_parms.append("False")             # country code
            
            elif(geocoderid == gcm.OpenMapQuestId) :
                
                query_run_parms.append("1")                 # only one result
                query_run_parms.append("20")                # timeout
            
            elif(geocoderid == gcm.NominatimId) :
                
                query_run_parms.append("1")                 # only one result
                query_run_parms.append("20")                # timeout
                query_run_parms.append("False")             # details
                query_run_parms.append("")                  # language
                query_run_parms.append("")                  # geometry
            
            else :

                title       =   "dfcleanser error"       
                status_msg  =   "Invalid geocoder defined"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)

            # build parms list to change addresses to lat long values
            query_parms     =   []
            for i in range(len(parms[0])) :
                query_parms.append(parms[0][i])

            for i in range(len(query_run_parms)) :
                query_parms.append(query_run_parms[i]) 

            query_results   =   run_geocoder_query(geocoderid, query_parms)

            from_lat_lngs   =   []
            for i in range(len(query_results)) :
                geopoint    =   (query_results[i][2],query_results[i][3])
                from_lat_lngs.append(geopoint)

            # build parms list to change addresses to lat long values
            query_parms     =   []
            for i in range(len(parms[1])) :
                query_parms.append(parms[1][i])

            for i in range(len(query_run_parms)) :
                query_parms.append(query_run_parms[i]) 

            query_results     =   run_geocoder_query(geocoderid, query_parms) 

            to_lat_lngs   =   []
            for i in range(len(query_results)) :
                geopoint    =   (query_results[i][2],query_results[i][3])
                to_lat_lngs.append(geopoint)

    else :

        from_lat_lngs   =   []
        to_lat_lngs     =   []

        for i in range(len(parms[0])) :

            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
            new_geopoint    =   get_geopoint_from_string(parms[0][i])

            if(not (new_geopoint is None)) :

                from_lat_lngs.append(new_geopoint)
            
            else :
                
                title       =   "dfcleanser error"       
                status_msg  =   "Invalid from : lat lng value " + str(i)
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)

        for i in range(len(parms[1])) :
            
            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
            new_geopoint    =   get_geopoint_from_string(parms[1][i])

            if(not (new_geopoint is None)) :

                to_lat_lngs.append(new_geopoint)
            
            else :
                
                title       =   "dfcleanser error"       
                status_msg  =   "Invalid to : lat lng value " + str(i)
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)
            
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : from_lat_lngs ",from_lat_lngs))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : to_lat_lngs ",to_lat_lngs))

    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()
        
    distance_list   =   calculate_geocode_distances(from_lat_lngs, to_lat_lngs, parms[2][0], parms[2][1], parms[2][2], opstat)    

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_distances] : distance list",distance_list,"\n"))

    return(distance_list)



# ------------------------------------------------------------------------- #
#                   process calculate df distance inputs                    #
# ------------------------------------------------------------------------- #

def process_calculate_df_distances(parms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances] : parms \n  ",parms))

    df_title                    =   parms[0]
    from_df_col_name            =   parms[1]
    to_df_col_name              =   parms[2]
    new_col_name                =   parms[3]
    distance_units              =   parms[4]
    distance_alg                =   parms[5]
    elipsoid                    =   parms[6]

    from_geocode_points_data    =   get_geocode_points_from_df(df_title,from_df_col_name)

    if(not (from_geocode_points_data is None)) :

        from_geocode_points  =      from_geocode_points_data[0]
        from_total_errors    =      from_geocode_points_data[1]
        from_error_rate      =      from_total_errors / len(from_geocode_points)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances] :from_geocode_points  ",len(from_geocode_points)," error_rate : ",from_error_rate))

        if( (len(from_geocode_points) > 0) and (from_error_rate < 0.10) ) :
             
            to_geocode_points_data  =   get_geocode_points_from_df(df_title,to_df_col_name)
            to_geocode_points       =   to_geocode_points_data[0]
            to_total_errors         =   to_geocode_points_data[1]
            to_error_rate           =   to_total_errors / len(to_geocode_points)

            if( (len(to_geocode_points) > 0) and (to_error_rate < 0.10) ) :

                from dfcleanser.common.common_utils import opStatus
                opstat              =   opStatus()
                df_col_distances    =   calculate_geocode_distances(from_geocode_points, to_geocode_points, distance_units, distance_alg, elipsoid, opstat)

                if(opstat.get_status()) :

                    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                        add_debug_to_log("DataExport",print_to_string("df_col_distances",len(df_col_distances)))

                    return(df_col_distances)
            
                else :

                    title       =   "dfcleanser error"       
                    status_msg  =   "calculating df distance error"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)

                    return(None)
                
            else :

                title       =   "dfcleanser error"       
                status_msg  =   "[process_calculate_df_distances] error rate : " + str(to_error_rate)
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)

        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_calculate_df_distances]  error rate : " + str(from_error_rate)
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
        
    else :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_calculate_df_distances] failed"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)



# ------------------------------------------------------------------------- #
#                   process calculate df distance inputs                    #
# ------------------------------------------------------------------------- #

def process_calculate_df_distances_from_fixed_location(parms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_fixed_location] : parms \n  ",parms))

    fixed_point         =   parms[0]
    df_title            =   parms[1]
    df_col_name         =   parms[2]
    new_col_name        =   parms[3]
    distance_units      =   parms[4]
    distance_alg        =   parms[5]
    elipsoid            =   parms[6]

    #import json
    try :

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string

        fixed_geocode_point     =   get_geopoint_from_string(fixed_point)

    except :
            
        title       =   "dfcleanser error"       
        status_msg  =   "fixed point for distance is invalid : "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
    
    to_geocode_points_data    =   get_geocode_points_from_df(df_title,df_col_name )

    if(not (to_geocode_points_data is None)) :

        to_geocode_points  =      to_geocode_points_data[0]
        to_total_errors    =      to_geocode_points_data[1]
        to_error_rate      =      to_total_errors / len(to_geocode_points)

        if( (len(to_geocode_points) > 0) and (to_error_rate < 0.10) ) :

            geocode_distances   =   []
            from dfcleanser.common.common_utils import opStatus
            opstat              =   opStatus()

            for i in range(len(to_geocode_points)) :

                current_distance    =   get_distance(fixed_geocode_point, to_geocode_points[i], distance_units, distance_alg, elipsoid, opstat)
                if(not (current_distance is None)) :
                    geocode_distances.append(current_distance) 

            return(geocode_distances)

        else :
         
            title       =   "dfcleanser error"       
            status_msg  =   "to distances are bad : "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
        
    else :

        title       =   "dfcleanser error"       
        status_msg  =   "excessive error rate : " + str(to_error_rate)
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
    
    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):   
        add_debug_to_log("DataExport",print_to_string("geocode_distances",geocode_distances))


# ------------------------------------------------------------------------- #
#                   process calculate df distance inputs                    #
# ------------------------------------------------------------------------- #

def process_calculate_df_distances_from_center_point(parms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_center_point] : parms \n  ",parms))

    df_title                    =   parms[0]
    df_col_name                 =   parms[1]
    center_pt_df_title          =   parms[2]
    center_pt_df_col_name       =   parms[3]
    new_col_name                =   parms[4]
    distance_units              =   parms[5]
    distance_alg                =   parms[6]
    elipsoid                    =   parms[7]

    from dfcleanser.common.common_utils import opStatus
    opstat          =   opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
    df      =   get_dfc_dataframe_df(center_pt_df_title)
    points  =   df[center_pt_df_col_name].tolist()

    geopoints   =   []
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string

    for i in range(len(points)) :
        geopoints.append(get_geopoint_from_string(points[i]))


    center_point    =   get_geocode_center(geopoints,opstat)

    if(opstat.get_status()) :

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")) :
            add_debug_to_log("DataExport",print_to_string("center_point",center_point))

        ptsdf       =   get_dfc_dataframe_df(df_title)
        ptspoints   =   ptsdf[df_col_name].tolist()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string
        geopoints   =   []
        for i in range(len(ptspoints)) :
            geopoints.append(get_geopoint_from_string(ptspoints[i]))

        center_pt_distances     =   []

        for i in range(len(geopoints)):
            calc_distance = get_distance(geopoints[i], center_point, distance_units, distance_alg, elipsoid, opstat)

            if(opstat.get_status()) :

                calc_distance = round(calc_distance,3)
                center_pt_distances.append(calc_distance)

            else :

                center_pt_distances.append(0)  

        return(center_pt_distances)     

    else :
        
        title       =   "dfcleanser error"       
        status_msg  =   "Unable to calculate center point"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
    
    if(opstat.get_status()) :

        ptsdf[new_col_name]  = center_pt_distances
        set_dfc_dataframe_df(center_pt_df_title,ptsdf) 

        title       =   "dfcleanser mesage"       
        status_msg  =   "[process_calculate_df_distances_from_center_point] column added"
        from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
        display_status_msg(title,status_msg)

        return(center_pt_distances)     

# ------------------------------------------------------------------------- #
#           process calculate df distance point list inputs                 #
# ------------------------------------------------------------------------- #

def process_calculate_df_distances_from_list_points(parms) :

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : parms "))

    df_title                    =   parms[0]
    df_col_name                 =   parms[1]

    distance_list_pts           =   parms[2]
    distance_names_list         =   parms[3] 

    distance_values_col_name    =   parms[4]
    distance_points_col_name    =   parms[5]
    distance_names_col_name     =   parms[6]

    distance_type               =   parms[7]

    distance_units              =   parms[8]
    distance_alg                =   parms[9]
    elipsoid                    =   parms[10]

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : df_title ",df_title))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : df_col_name ",df_col_name))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_list_points\n    ",distance_list_pts))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_list_names\n    ",distance_names_list))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_values_col_name ",distance_values_col_name))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_points_col_name ",distance_points_col_name))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_names_col_name ",distance_names_col_name))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_type ",distance_type))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_units ",distance_units))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_alg ",distance_alg))
        add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : elipsoid ",elipsoid))


    from dfcleanser.common.common_utils import opStatus
    opstat          =   opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
    df      =   get_dfc_dataframe_df(df_title)
    points  =   df[df_col_name].tolist()

    geopoints   =   []
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_geopoint_from_string

    for i in range(len(points)) :
        geopoints.append(get_geopoint_from_string(points[i]))

    try :

        exec(distance_list_pts)
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import GeocodePointsList
        list_distance_points    =   GeocodePointsList.get_locations()
        
        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : list_distance_points \n    ",list_distance_points))
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : list_distance_points ",type(list_distance_points),type(list_distance_points[0]),type(list_distance_points[0][0]),type(list_distance_points[0][1])))
        
        distance_points     =   []
        if(type(list_distance_points[0]) == list) :
            for i in range(len(list_distance_points)) :
                current_pt  =   (list_distance_points[i][0],list_distance_points[i][1])
                distance_points.append(current_pt)

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_points \n    ",distance_points,type(distance_points[0])))

    except Exception as e:

        title       =   "dfcleanser exception"       
        status_msg  =   "[unable to get distance list] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

        return(None)

    try :

        exec(distance_names_list)
        list_distance_names    =   GeocodePointsList.get_names()

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : list_distance_names \n    ",list_distance_names))


    except Exception as e:

        title       =   "dfcleanser exception"       
        status_msg  =   "[unable to get distance names list] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

        return(None)


    distance_range              =   []
    distance_range_location     =   []
    distance_range_name         =   []

    # for each column point get didtance from compare list
    for i in range(len(geopoints)) :

        if(distance_type == "Closest") :
            current_distance    =   40000
        else :
            current_distance    =   0

        current_point_index  =   0

        for j in range(len(distance_points)) :

            new_distance = round(get_distance(geopoints[i], distance_points[j], distance_units, distance_alg, elipsoid, opstat),5)
        
            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                if(i == 0) :
                    add_debug_to_log("DataExport",print_to_string("[process_calculate_][",j,"] : geopoints[",i,"] : distance_points[",j,"] ",geopoints[i], distance_points[j]))
                    add_debug_to_log("DataExport",print_to_string("[process_calculate_][",j,"] : new_distance : current_distance : current_point_index ",new_distance,current_distance,current_point_index))

            if(distance_type == "Closest") :
                if(new_distance < current_distance) :
                    current_distance    =   new_distance
                    current_point_index =   j
            else :
                if(new_distance > current_distance) :
                    current_distance    =   new_distance
                    current_point_index =   j

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
                if(i == 0) :
                    add_debug_to_log("DataExport",print_to_string("[process_calculate_][",j,"] : new_distance : current_distance : current_point_index ",new_distance,current_distance,current_point_index))
            

        distance_range.append(round(current_distance,4))
        distance_range_location.append(distance_points[current_point_index])
        distance_range_name.append(list_distance_names[current_point_index])

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            if(i == 0) :
                add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_range ",distance_range))
                add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_range_location ",distance_range_location))
                add_debug_to_log("DataExport",print_to_string("[process_calculate_df_distances_from_list_points] : distance_range_name ",distance_range_name))

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE")):
            if((len(distance_range) % 3000) == 0) :
                add_debug_to_log("DataExport",print_to_string("[process_calculate_] : len(distance_range) ",len(distance_range)))


    return([distance_range,distance_range_location,distance_range_name])


def process_df_distance(parms):
    """
    * ---------------------------------------------------------
    * function : calculate the dist betweern coords in a column
    * 
    * parms :
    *  parms  - input parms
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
        add_debug_to_log("DataExport",print_to_string("process_df_distance parms \n", parms))

    opstat = opStatus()

    fparms = get_parms_for_input(parms, sugw.addr_df_dist_utility_input_idList)

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
        add_debug_to_log("DataExport",print_to_string("process_df_distance fparms \n", fparms))

    # get the from geocode column info
    from_dftitle = fparms[0]
    from_df = cfg.get_dfc_dataframe_df(from_dftitle)
    from_lat_lng_cols = fparms[1]

    from_lat_column_name = None
    from_lng_column_name = None

    to_lat_column_name = None
    to_lng_column_name = None

    if(len(from_lat_lng_cols) > 0):

        try:

            from_cols_list = []

            from_cols_list = from_lat_lng_cols.lstrip("[")
            from_cols_list = from_cols_list.rstrip("]")
            from_cols_list = from_cols_list.split(",")

            if(len(from_cols_list) > 2):

                opstat.set_status(False)
                opstat.set_errorMsg("from_columns : too many column names " + str(from_cols_list))

            elif(len(from_cols_list) == 1):

                if(not (is_column_in_df(from_df, from_cols_list[0]))):
                    opstat.set_status(False)
                    opstat.set_errorMsg("from_columns column name is invalid " + str(from_cols_list[0]))

            else:

                from_lat_column_name = from_cols_list[0]
                from_lng_column_name = from_cols_list[1]

                if(not (is_column_in_df(from_df, from_lat_column_name))):
                    opstat.set_status(False)
                    opstat.set_errorMsg("from_columns lat column name is invalid " + str(from_lat_column_name))
                else:
                    if(not (is_column_in_df(from_df, from_lng_column_name))):
                        opstat.set_status(False)
                        opstat.set_errorMsg("from_columns lng column name is invalid " + str(from_lng_column_name))

        except Exception as e:
            opstat.store_exception("from_columns is invalid " + str(fparms[1]), e)

    else:
        opstat.set_status(False)
        opstat.set_errorMsg("from_columns are not defined ")

    if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
        add_debug_to_log("DataExport",print_to_string("process_df_distance : from_cols_list : ", from_cols_list))

    # get the to geocode column info
    if(opstat.get_status()):

        to_df = cfg.get_dfc_dataframe_df(from_dftitle)
        to_lat_lng_cols = fparms[3]

        to_lat_column_name = None
        to_lng_column_name = None

        if(len(to_lat_lng_cols) > 0):

            try:

                to_cols_list = []

                to_cols_list = to_lat_lng_cols.lstrip("[")
                to_cols_list = to_cols_list.rstrip("]")
                to_cols_list = to_cols_list.split(",")

                if(len(to_cols_list) > 2):

                    opstat.set_status(False)
                    opstat.set_errorMsg("to_columns : too many column names " + str(to_cols_list))

                elif(len(to_cols_list) == 1):

                    if(not (is_column_in_df(from_df, to_cols_list[0]))):
                        opstat.set_status(False)
                        opstat.set_errorMsg("to_columns column name is invalid " + str(to_cols_list[0]))

                else:

                    to_lat_column_name = to_cols_list[0]
                    to_lng_column_name = to_cols_list[1]

                    if(not (is_column_in_df(from_df, to_lat_column_name))):
                        opstat.set_status(False)
                        opstat.set_errorMsg(
                            "to_columns lat column name is invalid " + str(to_lat_column_name))
                    else:
                        if(not (is_column_in_df(from_df, to_lng_column_name))):
                            opstat.set_status(False)
                            opstat.set_errorMsg("to_columns lng column name is invalid " + str(to_lng_column_name))

            except Exception as e:
                opstat.store_exception("to_columns is invalid " + str(fparms[4]), e)

        else:
            opstat.set_status(False)
            opstat.set_errorMsg("to_columns are not defined ")

    # get and validsate the new distance column name
    if(opstat.get_status()):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
            add_debug_to_log("DataExport",print_to_string("process_df_distance to_cols_list : ", to_cols_list))

        new_col_name = fparms[5]

        if(len(new_col_name) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("distance column name is invalid " + str(new_col_name))

    # get and validsate the geocode run parms
    if(opstat.get_status()):

        distance_units = fparms[6]
        algorithm = fparms[7]
        elipsoid = fparms[8]

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
            add_debug_to_log("DataExport",print_to_string("process_df_distance new_col_name : ", new_col_name))
            add_debug_to_log("DataExport",print_to_string("process_df_distance distance_units : ", distance_units))
            add_debug_to_log("DataExport",print_to_string("process_df_distance algorithm  : ", algorithm))
            add_debug_to_log("DataExport",print_to_string("process_df_distance elipsoid  : ", elipsoid))

    # build the coord lists
    if(opstat.get_status()):

        total_coords = len(from_df)
        distances_list = []

        from_coords_list = []
        to_coords_list = []

        # single from lat_lng column
        if((from_lat_column_name is None)):

            current_from_lat_lng_coords = from_df[from_cols_list[0]]

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_from_lat_lng_coords  : \n",current_from_lat_lng_coords))

            for i in range(len(from_df)):

                current_lat_lng_coords = current_from_lat_lng_coords[i]

                current_lat_lng_coords = current_lat_lng_coords.lstrip("[")
                current_lat_lng_coords = current_lat_lng_coords.rstrip("]")
                current_lat_lng_coords = current_lat_lng_coords.lstrip("(")
                current_lat_lng_coords = current_lat_lng_coords.rstrip(")")
                current_lat_lng_coords = current_lat_lng_coords.split(",")

                try:
                    currennt_from_geocode_coord = [float(current_lat_lng_coords[0]), float(current_lat_lng_coords[0])]
                except:
                    currennt_from_geocode_coord = None

                from_coords_list.append(currennt_from_geocode_coord)

        # separate from lat_lng columns
        else:

            current_from_lat_coords = from_df[from_lat_column_name]
            current_from_lng_coords = from_df[from_lng_column_name]

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_from_lat_coords  : \n",current_from_lat_coords))
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_from_lng_coords  : \n",current_from_lng_coords))

            for i in range(len(from_df)):

                try:
                    currennt_from_geocode_coord = [float(current_from_lat_coords[i]), float(current_from_lng_coords[i])]
                except:
                    currennt_from_geocode_coord = None

                from_coords_list.append(currennt_from_geocode_coord)

        # single to lat_lng column
        if((to_lat_column_name is None)):

            current_to_lat_lng_coords = from_df[to_cols_list[0]]

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_to_lat_lng_coords  : \n",current_to_lat_lng_coords))

            for i in range(len(from_df)):

                current_lat_lng_coords = current_to_lat_lng_coords[i]

                current_lat_lng_coords = current_lat_lng_coords.lstrip("[")
                current_lat_lng_coords = current_lat_lng_coords.rstrip("]")
                current_lat_lng_coords = current_lat_lng_coords.lstrip("(")
                current_lat_lng_coords = current_lat_lng_coords.rstrip(")")
                current_lat_lng_coords = current_lat_lng_coords.split(",")

                try:
                    currennt_to_geocode_coord = [
                        float(current_lat_lng_coords[0]), float(current_lat_lng_coords[0])]
                except:
                    currennt_to_geocode_coord = None

                to_coords_list.append(currennt_to_geocode_coord)

        # separate from lat_lng columns
        else:

            current_to_lat_coords = from_df[to_lat_column_name]
            current_to_lng_coords = from_df[to_lng_column_name]

            if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_to_lat_coords  : \n",current_to_lat_coords))
                add_debug_to_log("DataExport",print_to_string("process_df_distance : current_to_lng_coords  : \n",current_to_lng_coords))

            for i in range(len(from_df)):

                try:
                    currennt_to_geocode_coord = [
                        float(current_to_lat_coords[i]), float(current_to_lng_coords[i])]
                except:
                    currennt_to_geocode_coord = None

                to_coords_list.append(currennt_to_geocode_coord)

    # build the coord lists
    if(opstat.get_status()):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
            add_debug_to_log("DataExport",print_to_string("process_df_distance : from_coords_list : \n", from_coords_list))
            add_debug_to_log("DataExport",print_to_string("process_df_distance : to_coords_list : \n", to_coords_list))

        distances = calculate_geocode_distances(from_coords_list, to_coords_list, distance_units, algorithm, elipsoid, opstat)

    # display the results
    if(opstat.get_status()):

        if(is_debug_on(SWGeocodeUtility_ID,"DEBUG_GEOCODE_UTILITY")):
            add_debug_to_log("DataExport",print_to_string("process_df_distance : distances : \n", distances))

        display_status_note("distances calculated successfully")

        from dfcleanser.sw_utilities.GenericFunctionsModel import add_column_to_df
        from_df = add_column_to_df(from_df, new_col_name, distances, opstat, False)
        from_df[new_col_name] = from_df[new_col_name].astype(float, copy=False)

        cfg.set_dfc_dataframe_df(from_dftitle, from_df)
        cfg.set_config_value(sugw.addr_df_dist_utility_input_id+"Parms",fparms)

    if(opstat.get_status()):

        notes = "New Column : '" +  str(new_col_name) + "' added to '" + str(from_dftitle) + "' dataframe"
        display_status_note(notes)


        temp_js_list    =   sugw.addr_df_dist_utility_tb_jsList.copy()
        temp_js_list[0]    =   temp_js_list[0].replace("XXXXDFTITLE","'" + from_dftitle + "'")
        temp_js_list[0]    =   temp_js_list[0].replace("XXXXCOLUMNNAME","'" + new_col_name + "'")

        inspect_tb = ButtonGroupForm(sugw.addr_df_dist_utility_tb_id,
                                     sugw.addr_df_dist_utility_tb_keyTitleList,
                                     temp_js_list,
                                     sugw.addr_df_dist_utility_tb_centered)

        inspect_tb.set_customstyle({"font-size": 13, "height": 50, "width": 150, "left-margin": 40})

        gridclasses = ["main"]
        gridhtmls = [inspect_tb.get_html()]

        display_generic_grid("df-common-colnames-wrapper",gridclasses, gridhtmls)

        notes = []
        notes.append("To view column changes click on Inspect Columns.")

        from dfcleanser.sw_utilities.DisplayUtils import get_common_text_html
        help_html = get_common_text_html(notes, 560, 150)

        gridclasses = ["dfc-main"]
        gridhtmls = [help_html]

        display_generic_grid(
            "dfc-common-720px-1-vert-wrapper", gridclasses, gridhtmls)

    else:
        get_exception_html(opstat, width=90, left=40, display=True)




