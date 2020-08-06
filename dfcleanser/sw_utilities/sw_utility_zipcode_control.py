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

import numpy

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_zipcode_widgets as suzw
import dfcleanser.sw_utilities.sw_utility_zipcode_model as suzm

from dfcleanser.common.common_utils import (get_parms_for_input, display_exception, display_status, 
                                            display_notes, opStatus, RunningClock, log_debug_dfc,
                                            does_dir_exist, does_file_exist, delete_a_file,
                                            display_generic_grid)


 

def display_zipcode_utility(optionId,parms=None) :
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
    
    from IPython.display import clear_output
    clear_output()
    
    if(optionId == suzm.DISPLAY_MAIN) :
        suzw.display_zipcode_main_taskbar()        
        clear_sw_utility_zipcodedata()
        
    elif(optionId == suzm.DISPLAY_ZIP_ATTRS) :
        suzw.display_get_zipcode_attributes(parms)        

    elif(optionId == suzm.DISPLAY_ZIP_LOC_DATA) :
        suzw.display_zipcode_locations_taskbar()        
        
    elif(optionId == suzm.DISPLAY_GET_CITY_ZIPS) :
        suzw.display_get_zips_for_city(parms)        

    elif(optionId == suzm.DISPLAY_GET_STATE_COUNTIES) :
        suzw.display_get_counties_for_state(parms)        
        
    elif(optionId == suzm.DISPLAY_GET_COUNTY_CITIES) :
        suzw.display_get_cities_for_county(parms)        

    elif(optionId == suzm.DISPLAY_GET_STATE_CITIES) :
        suzw.display_get_cities_for_state(parms)        

    elif(optionId == suzm.PROCESS_ZIP_ATTRS) :
        process_zipcode_attributes(parms)        

    elif(optionId == suzm.PROCESS_GET_CITY_ZIPS) :
        process_zipcode_cities(parms)        

    elif(optionId == suzm.PROCESS_GET_STATE_COUNTIES) :
        process_state_counties(parms)        

    elif(optionId == suzm.PROCESS_GET_COUNTY_CITIES) :
        process_county_cities(parms)        

    elif(optionId == suzm.PROCESS_GET_STATE_CITIES) :
        process_state_cities(parms)        




def process_zipcode_attributes(parms) :
    
    DEBUG_PROC_ZC_ATTRS     =   False
    
    opstat  =   opStatus()
    
    fparms      =   get_parms_for_input(parms,suzw.zipcode_atributes_input_idList)
    zipcode     =   fparms[0]
    
    cfg.set_config_value(suzw.zipcode_atributes_input_id + "Parms",fparms)
    
    suzw.display_get_zipcode_attributes(parms) 
    
    print("\n")
    
    zipattrsHeader        =   [""]
    zipattrsRows          =   []
    zipattrsWidths        =   [30,70]
    zipattrsAligns        =   ["left","left"]
    
    primary_cities          =   suzm.get_cities_for_zipcode(zipcode,city_type=suzm.PRIMARY_CITY_TYPE)
    acceptable_cities       =   suzm.get_cities_for_zipcode(zipcode,city_type=suzm.ACCEPTABLE_CITY_TYPE)
    not_acceptable_cities   =   suzm.get_cities_for_zipcode(zipcode,city_type=suzm.NOT_ACCEPTABLE_CITY_TYPE)
    
    zipcode_county          =   suzm.get_county_for_zipcode(zipcode) 
    zipcode_state           =   suzm.get_state_for_zipcode(zipcode)
    
    zipcode_latitude        =   suzm.get_latitude_for_zipcode(zipcode) 
    zipcode_longitude       =   suzm.get_longitude_for_zipcode(zipcode)
    
    zipcode_areacodes       =   suzm.get_areacodes_for_zipcode(zipcode)
    
    zipcode_active_status   =   suzm.is_zipcode_active(zipcode)
    
    zipcode_type            =   suzm.get_type_for_zipcode(zipcode)
    
    """
    501 603 604 8720 8732 8753 9001 9203 9204 9213 11708
    """
    if(DEBUG_PROC_ZC_ATTRS) :
        
        print("primary_cities",primary_cities)
        if(not (acceptable_cities is None)) :
            print("acceptable_cities",len(acceptable_cities),acceptable_cities)
        else :
            print("acceptable_cities",acceptable_cities)
        
        if(not (not_acceptable_cities is None)) :
            print("not_acceptable_cities",len(not_acceptable_cities),not_acceptable_cities)
        else :
            print("not_acceptable_cities",not_acceptable_cities)
    
        print("zipcode_county",zipcode_county)
        print("zipcode_state",zipcode_state)
        print("zipcode_latitude",type(zipcode_latitude),zipcode_latitude)
        print("zipcode_longitude",type(zipcode_longitude),zipcode_longitude)
    
        print("zipcode_areacodes",type(zipcode_areacodes),zipcode_areacodes)
        print("zipcode_active_status",zipcode_active_status)
        print("zipcode_type",zipcode_type)
    
    
    if( (not (zipcode_active_status)) and 
        (primary_cities is None) ) :
        
        zipattrsRows.append(["Current Status","Zipcode is Invalid"])
        
    else :
    
        if(zipcode_active_status) :
            zipattrsRows.append(["Current Status","Active"])
        else :
            zipattrsRows.append(["Current Status","Decommissioined"])
    
        if(primary_cities is None) :
        
            zipattrsRows.append(["Primary City","None"])
        
        else :
        
            if( (primary_cities == suzm.APO_ZIPCODE_TYPE) or 
                (primary_cities == suzm.FPO_ZIPCODE_TYPE) or 
                (primary_cities == suzm.DPO_ZIPCODE_TYPE) ) :
            
                zipattrsRows.append(["Primary City","Washington DC"])
            
            else :
                zipattrsRows.append(["Primary City",str(primary_cities)])
    
        if(zipcode_county is None) :
            zipattrsRows.append(["County","None"])
        else :
            zipattrsRows.append(["County",str(zipcode_county)])
    
        if(zipcode_state is None) :
            zipattrsRows.append(["State","None"])
        else :
            zipattrsRows.append(["State",str(zipcode_state)])
    
        if( (zipcode_latitude is None) or (zipcode_longitude is None) or 
            (numpy.isnan(zipcode_latitude)) or (numpy.isnan(zipcode_longitude)) ) :
            zipattrsRows.append(["[Latitude,Longitude]","Unknown"])
        else :
            zipattrsRows.append(["[Latitude,Longitude]","[" + str(round(zipcode_latitude,7)) + " , " + str(round(zipcode_longitude,7)) + "]"])
    
        if(zipcode_type is None) :
            zipattrsRows.append(["Zipcode Type","None"])
        else :
        
            if(zipcode_type == suzm.UNIQUE_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.UNIQUE_text)])
            elif(zipcode_type == suzm.STANDARD_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.STANDARD_text)])
            elif(zipcode_type == suzm.PO_BOX_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.PO_BOX_text)])
            elif(zipcode_type == suzm.APO_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.APO_text)])
            elif(zipcode_type == suzm.FPO_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.FPO_text)])
            elif(zipcode_type == suzm.DPO_ZIPCODE_TYPE) :
                zipattrsRows.append(["Zipcode Type",str(suzm.DPO_text)])
            else :
                zipattrsRows.append(["Zipcode Type","Unknown"])
    
        if(not (zipcode_areacodes is None)) :
        
            if(type(zipcode_areacodes) == list) :
                for i in range(len(zipcode_areacodes)) :
                    zipcode_areacodes[i]       =   zipcode_areacodes[i].replace("'","")
                    
            zipattrsRows.append(["Area Codes",str(zipcode_areacodes)])
        
        if( not (acceptable_cities is None)) :
            if(len(acceptable_cities) > 0)  :
                zipattrsRows.append(["Acceptable Cities",str(acceptable_cities)])
        
        if( not (not_acceptable_cities is None)) :
            if(len(not_acceptable_cities) > 0) :
                zipattrsRows.append(["Not Acceptable Cities",str(not_acceptable_cities)])
 
    zipattrs_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    zipattrs_table        =   dcTable("Zipcode " + str(zipcode) + " Properties",'zipcodeattrsid',
                                    cfg.SWZipcodeUtility_ID,
                                    zipattrsHeader,zipattrsRows,
                                    zipattrsWidths,zipattrsAligns)
            
    zipattrs_table.set_small(True)
    zipattrs_table.set_checkLength(False)

    zipattrs_table.set_border(True)
    zipattrs_table.set_tabletype(ROW_MAJOR)
    zipattrs_table.set_rowspertable(50)
    zipattrsHtml = get_row_major_table(zipattrs_table,SCROLL_DOWN,False)
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [zipattrsHtml]
    
    display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)
 

def process_zipcode_cities(parms) :
    
    opstat  =   opStatus()
    
    fparms      =   get_parms_for_input(parms,suzw.zipcode_cities_input_idList)
    city        =   fparms[0]
    state       =   fparms[1][:2]
    
    cfg.set_config_value(suzw.zipcode_cities_input_id + "Parms",fparms)
    
    suzw.display_get_zips_for_city(parms) 
    
    print("\n")
    
    
    cityzipsHeader        =   [""]
    cityzipsRows          =   []
    cityzipsWidths        =   [30,70]
    cityzipsAligns        =   ["left","left"]
    
    cityzips            =   suzm.get_zipcodes_for_city(state, city, zipcode_type=suzm.STANDARD_ZIPCODE_TYPE, active_status=suzm.ACTIVE_STATUS_TYPE)
    citypobzips         =   suzm.get_zipcodes_for_city(state, city, zipcode_type=suzm.PO_BOX_ZIPCODE_TYPE, active_status=suzm.ACTIVE_STATUS_TYPE)
    cityuniquezips      =   suzm.get_zipcodes_for_city(state, city, zipcode_type=suzm.UNIQUE_ZIPCODE_TYPE, active_status=suzm.ACTIVE_STATUS_TYPE)
    
    citydecomzips       =   suzm.get_zipcodes_for_city(state, city, zipcode_type=suzm.ANY_ZIPCODE_TYPE, active_status=suzm.DECOMMISIONED_STATUS_TYPE)

    if(not (cityzips is None)) :
        cityzipsRows.append([suzm.STANDARD_text + " Zipcodes",str(cityzips)])

    if(not (citypobzips is None)) :
        cityzipsRows.append([suzm.PO_BOX_text + " Zipcodes",str(citypobzips)])
    
    if(not (cityuniquezips is None)) :
        cityzipsRows.append([suzm.UNIQUE_text + " Zipcodes",str(cityuniquezips)])
        
    if(not (citydecomzips is None)) :
        cityzipsRows.append(["Decommissioned" + " Zipcodes",str(citydecomzips)])
    
    
    cityzips_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    cityzips_table        =   dcTable("Zipcodes For " + str(city.upper()) + ", " + str(state),'cityzipcodesid',
                                    cfg.SWZipcodeUtility_ID,
                                    cityzipsHeader,cityzipsRows,
                                    cityzipsWidths,cityzipsAligns)
            
    cityzips_table.set_small(True)
    cityzips_table.set_checkLength(False)

    cityzips_table.set_border(True)
    cityzips_table.set_tabletype(ROW_MAJOR)
    cityzips_table.set_rowspertable(50)
    cityzipsHtml = get_row_major_table(cityzips_table,SCROLL_DOWN,False)
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [cityzipsHtml]
    
    display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)
   
 
def process_state_counties(parms) :
    
    opstat  =   opStatus()
    
    fparms      =   get_parms_for_input(parms,suzw.state_counties_input_idList)
    state       =   fparms[0][:2]
    
    cfg.set_config_value(suzw.state_counties_input_id + "Parms",fparms)
    
    suzw.display_get_counties_for_state(parms) 
    
    print("\n")
    
    countiesHeader        =   [""]
    countiesRows          =   []
    countiesWidths        =   [15,85]
    countiesAligns        =   ["left","left"]
    
    counties            =   suzm.get_counties_for_state(state)

    if(not (counties is None)) :
        countiesRows.append(["Counties",str(counties)])
    
    counties_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    counties_table        =   dcTable("Counties For " + str(suzm.get_state_name(state).upper()),'countiescodesid',
                                    cfg.SWZipcodeUtility_ID,
                                    countiesHeader,countiesRows,
                                    countiesWidths,countiesAligns)
            
    counties_table.set_small(True)
    counties_table.set_checkLength(False)

    counties_table.set_border(True)
    counties_table.set_tabletype(ROW_MAJOR)
    counties_table.set_rowspertable(50)
    countiesHtml = get_row_major_table(counties_table,SCROLL_DOWN,False)
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [countiesHtml]
    
    display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)


def process_county_cities(parms) :
    
    opstat  =   opStatus()
    
    fparms      =   get_parms_for_input(parms,suzw.county_cities_input_idList)
    state       =   fparms[0][:2]
    county      =   fparms[1] 
    
    cfg.set_config_value(suzw.county_cities_input_id + "Parms",fparms)
    
    suzw.display_get_cities_for_county(parms) 
    
    print("\n")
    
    citiesHeader        =   [""]
    citiesRows          =   []
    citiesWidths        =   [20,80]
    citiesAligns        =   ["left","left"]

    primary_cities          =   suzm.get_cities_for_county(state,county,city_type=suzm.ANY_CITY_TYPE)

    if(not (primary_cities is None)) :
        citiesRows.append(["US Zipcode Cities",str(primary_cities)])
    
    cities_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    cities_table        =   dcTable("Cities For " + str(county) + " - " + str(suzm.get_state_name(state).upper()),'citiescodesid',
                                    cfg.SWZipcodeUtility_ID,
                                    citiesHeader,citiesRows,
                                    citiesWidths,citiesAligns)
            
    cities_table.set_small(True)
    cities_table.set_checkLength(False)

    cities_table.set_border(True)
    cities_table.set_tabletype(ROW_MAJOR)
    cities_table.set_rowspertable(50)
    citiesHtml = get_row_major_table(cities_table,SCROLL_DOWN,False)
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [citiesHtml]
    
    display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)


def process_state_cities(parms) :
    
    opstat  =   opStatus()
    
    fparms      =   get_parms_for_input(parms,suzw.state_cities_input_idList)
    state       =   fparms[0][:2]
    
    cfg.set_config_value(suzw.state_cities_input_id + "Parms",fparms)
    
    suzw.display_get_cities_for_state(parms) 
    
    print("\n")
    
    citiesHeader        =   [""]
    citiesRows          =   []
    citiesWidths        =   [20,80]
    citiesAligns        =   ["left","left"]

    primary_cities          =   suzm.get_cities_for_state(state,city_type=suzm.ANY_CITY_TYPE)

    if(not (primary_cities is None)) :
        citiesRows.append(["US Zipcode Cities",str(primary_cities)])
    
    cities_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    cities_table        =   dcTable("Cities For " + str(suzm.get_state_name(state).upper()),'citiescodesid',
                                    cfg.SWZipcodeUtility_ID,
                                    citiesHeader,citiesRows,
                                    citiesWidths,citiesAligns)
            
    cities_table.set_small(True)
    cities_table.set_checkLength(False)

    cities_table.set_border(True)
    cities_table.set_tabletype(ROW_MAJOR)
    cities_table.set_rowspertable(50)
    citiesHtml = get_row_major_table(cities_table,SCROLL_DOWN,False)
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [citiesHtml]
    
    display_generic_grid("display-geocode-coords-wrapper",gridclasses,gridhtmls)

          
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common zipcode helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def clear_sw_utility_zipcodedata() :
    
    a = 12




