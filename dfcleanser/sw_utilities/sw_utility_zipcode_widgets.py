"""
# sw_utility_zipcode_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.sw_utilities.sw_utility_zipcode_model as suzm

from dfcleanser.common.html_widgets import (ButtonGroupForm, InputForm)

from dfcleanser.common.common_utils import (get_parms_for_input, display_generic_grid, get_select_defaults)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Geocoders forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    zipcodes main task bar
#--------------------------------------------------------------------------
"""
zipcode_main_tb_doc_title               =   "Zipcodes"
zipcode_main_tb_title                   =   "Zipcodes"
zipcode_main_tb_id                      =   "zipcodemaintb"

zipcode_main_tb_keyTitleList            =   ["Get</br>Zipcode</br>Attributes",
                                             "Get</br>Zipcodes By</br>Location",
                                             "Clear","Reset","Help"]

zipcode_main_tb_jsList                  =   ["display_zipcode(" + str(suzm.DISPLAY_ZIP_ATTRS) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_ZIP_LOC_DATA) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.GEOCODING_MAIN_TASKBAR_ID) + "')"]

zipcode_main_tb_centered                =   False


"""
#--------------------------------------------------------------------------
#    zipcodes locations task bar
#--------------------------------------------------------------------------
"""
zipcode_locations_tb_doc_title          =   "Zipcode Locations"
zipcode_locations_tb_title              =   "Zipcode Locations"
zipcode_locations_tb_id                 =   "zipcodelocationstb"

zipcode_locations_tb_keyTitleList       =   ["Get</br>Zipcodes</br>For City",
                                             "Get</br>Counties</br>For State",
                                             "Get</br>Cities</br>For County",
                                             "Get</br>Cities</br>For State",
                                             "Clear","Reset","Help"]

zipcode_locations_tb_jsList             =   ["display_zipcode(" + str(suzm.DISPLAY_GET_CITY_ZIPS) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_GET_STATE_COUNTIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_GET_COUNTY_CITIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_GET_STATE_CITIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.GEOCODING_MAIN_TASKBAR_ID) + "')"]

zipcode_locations_tb_centered             =   False




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    geocoding utilities input form
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    zipcode attributes input form
#--------------------------------------------------------------------------
"""
zipcode_atributes_input_title             =   "Zipcode Attributes"
zipcode_atributes_input_id                =   "zipcodeattrs"
zipcode_atributes_input_idList            =   ["zipcodeid",
                                               None,None,None,None]

zipcode_atributes_input_labelList         =   ["zip_code",
                                               "Get</br>Zipcode</br>Attributes",
                                               "Clear","Return","Help"]

zipcode_atributes_input_typeList          =   ["text","button","button","button","button"]

zipcode_atributes_input_placeholderList   =   ["Enter 5 didgit zipcode",
                                              None,None,None,None]

zipcode_atributes_input_jsList            =    [None,
                                                "process_zipcode(" + str(suzm.PROCESS_ZIP_ATTRS) + ")",
                                                "display_zipcode(" + str(suzm.DISPLAY_ZIP_ATTRS) + ")",
                                                "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                                "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

zipcode_atributes_input_reqList           =   [0]


"""
#--------------------------------------------------------------------------
#    zipcode cities input form
#--------------------------------------------------------------------------
"""
zipcode_cities_input_title             =   "Zipcode Cities"
zipcode_cities_input_id                =   "zipcodecities"
zipcode_cities_input_idList            =   ["cityname",
                                            "stateid",
                                             None,None,None,None]

zipcode_cities_input_labelList         =   ["city",
                                            "state",
                                            "Get</br>Zipcodes</br>For City",
                                            "Clear","Return","Help"]

zipcode_cities_input_typeList          =   ["text","select","button","button","button","button"]

zipcode_cities_input_placeholderList   =   ["Enter city",
                                            "select state",
                                            None,None,None,None]

zipcode_cities_input_jsList            =    [None,None,
                                             "process_zipcode(" + str(suzm.PROCESS_GET_CITY_ZIPS) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_ZIP_LOC_DATA) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

zipcode_cities_input_reqList           =   [0,1]


"""
#--------------------------------------------------------------------------
#    state counties input form
#--------------------------------------------------------------------------
"""
state_counties_input_title             =   "State Counties"
state_counties_input_id                =   "statecounties"
state_counties_input_idList            =   ["stateid",
                                             None,None,None,None]

state_counties_input_labelList         =   ["state",
                                            "Get</br>State</br>Counties",
                                            "Clear","Return","Help"]

state_counties_input_typeList          =   ["select","button","button","button","button"]

state_counties_input_placeholderList   =   ["select state",
                                            None,None,None,None]

state_counties_input_jsList            =    [None,
                                             "process_zipcode(" + str(suzm.PROCESS_GET_STATE_COUNTIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_ZIP_LOC_DATA) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

state_counties_input_reqList           =   [0]


"""
#--------------------------------------------------------------------------
#    county cities input form
#--------------------------------------------------------------------------
"""
county_cities_input_title             =   "County Cities"
county_cities_input_id                =   "countycities"
county_cities_input_idList            =   ["stateid",
                                           "countyid",
                                           None,None,None,None]

county_cities_input_labelList         =   ["state",
                                           "county",
                                           "Get</br>County</br>Cities",
                                           "Clear","Return","Help"]

county_cities_input_typeList          =   ["select","select","button","button","button","button"]

county_cities_input_placeholderList   =   ["select state",
                                           "select county",
                                           None,None,None,None]

county_cities_input_jsList            =    [None,None,
                                             "process_zipcode(" + str(suzm.PROCESS_GET_COUNTY_CITIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_ZIP_LOC_DATA) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

county_cities_input_reqList           =   [0,1]


"""
#--------------------------------------------------------------------------
#    state cities input form
#--------------------------------------------------------------------------
"""
state_cities_input_title             =   "State Counties"
state_cities_input_id                =   "statecities"
state_cities_input_idList            =   ["stateid",
                                          None,None,None,None]

state_cities_input_labelList         =   ["state",
                                          "Get</br>State</br>Cities",
                                          "Clear","Return","Help"]

state_cities_input_typeList          =   ["select","button","button","button","button"]

state_cities_input_placeholderList   =   ["select state",None,None,None,None]

state_cities_input_jsList            =    [None,
                                             "process_zipcode(" + str(suzm.PROCESS_GET_STATE_CITIES) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_ZIP_LOC_DATA) + ")",
                                             "display_zipcode(" + str(suzm.DISPLAY_MAIN) + ")",
                                             "displayhelp('" + str(dfchelp.GEOCODING_CALC_DISTANCE_ID) + "')"]

state_cities_input_reqList           =   [0]


 
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar display and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_zipcode_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(zipcode_main_tb_id,
                                               zipcode_main_tb_keyTitleList,
                                               zipcode_main_tb_jsList,
                                               zipcode_main_tb_centered),False)


def display_zipcode_locations_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(zipcode_locations_tb_id,
                                               zipcode_locations_tb_keyTitleList,
                                               zipcode_locations_tb_jsList,
                                               zipcode_locations_tb_centered),False)


def display_get_zipcode_attributes(parms) :
    """
    * ---------------------------------------------------------
    * function : display the calculate distance form 
    * 
    * parms :
    *  pytype  - address or coords
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    zip_attr_form  =   InputForm(zipcode_atributes_input_id,
                                 zipcode_atributes_input_idList,
                                 zipcode_atributes_input_labelList,
                                 zipcode_atributes_input_typeList,
                                 zipcode_atributes_input_placeholderList,
                                 zipcode_atributes_input_jsList,
                                 zipcode_atributes_input_reqList)   
        
    zip_attr_form.set_gridwidth(720)
    zip_attr_form.set_custombwidth(100)
    
    zip_attr_form.set_fullparms(True)
   
    zip_attr_input_html = ""
    zip_attr_input_html = zip_attr_form.get_html() 
    
    zip_attr_heading_html =   "<div>Get Zipcode Attributes</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [zip_attr_heading_html,zip_attr_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)


def display_get_zips_for_city(parms) :
    
    zip_cities_form  =   InputForm(zipcode_cities_input_id,
                                   zipcode_cities_input_idList,
                                   zipcode_cities_input_labelList,
                                   zipcode_cities_input_typeList,
                                   zipcode_cities_input_placeholderList,
                                   zipcode_cities_input_jsList,
                                   zipcode_cities_input_reqList)  
    
    
    selectDicts     =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)
    
    get_select_defaults(zip_cities_form,
                        zipcode_cities_input_id,
                        zipcode_cities_input_idList,
                        zipcode_cities_input_typeList,
                        selectDicts)

        
    zip_cities_form.set_gridwidth(720)
    zip_cities_form.set_custombwidth(100)
    
    zip_cities_form.set_fullparms(True)
   
    zip_cities_input_html = ""
    zip_cities_input_html = zip_cities_form.get_html() 
    
    zip_cities_heading_html =   "<div>Get Zipcodes For City</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [zip_cities_heading_html,zip_cities_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)

    
    
def display_get_counties_for_state(parms) :
    
    state_counties_form  =   InputForm(state_counties_input_id,
                                     state_counties_input_idList,
                                     state_counties_input_labelList,
                                     state_counties_input_typeList,
                                     state_counties_input_placeholderList,
                                     state_counties_input_jsList,
                                     state_counties_input_reqList)  
    
    selectDicts     =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)
    
    get_select_defaults(state_counties_form,
                        state_counties_input_id,
                        state_counties_input_idList,
                        state_counties_input_typeList,
                        selectDicts)

        
    state_counties_form.set_gridwidth(720)
    state_counties_form.set_custombwidth(100)
    
    state_counties_form.set_fullparms(True)
   
    state_counties_input_html = ""
    state_counties_input_html = state_counties_form.get_html() 
    
    state_counties_heading_html =   "<div>Get State Counties</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [state_counties_heading_html,state_counties_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)

    
def display_get_cities_for_county(parms) :

    if(parms is None) :
        
        fparms      =  cfg.get_config_value(county_cities_input_id+"Parms") 
        if(not (fparms is None)) :
            stateid     =  fparms[0] 
        else :
            stateid     =   None
        
    else :
    
        fparms      =   get_parms_for_input(parms,county_cities_input_idList)
        stateid     =   fparms[0]
        cfg.set_config_value(county_cities_input_id+"Parms",fparms)
    
    county_cities_form  =   InputForm(county_cities_input_id,
                                     county_cities_input_idList,
                                     county_cities_input_labelList,
                                     county_cities_input_typeList,
                                     county_cities_input_placeholderList,
                                     county_cities_input_jsList,
                                     county_cities_input_reqList)  
    
    selectDicts     =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))
    
    if(stateid is None) :
        state_def   =   states_list[0] 
    else :
        state_def   =   stateid
        
    state_sel    =   {"default":state_def,"list":states_list,"callback" : "change_state_for_counties"}
    selectDicts.append(state_sel)
    
    state_id   =   state_def[:2] 
        
    counties_list   =   suzm.get_counties_for_state(state_id)
    county_sel      =   {"default":counties_list[0],"list":counties_list}
    selectDicts.append(county_sel)
    
    get_select_defaults(county_cities_form,
                        county_cities_input_id,
                        county_cities_input_idList,
                        county_cities_input_typeList,
                        selectDicts)

        
    county_cities_form.set_gridwidth(720)
    county_cities_form.set_custombwidth(100)
    
    county_cities_form.set_fullparms(True)
   
    county_cities_input_html = ""
    county_cities_input_html = county_cities_form.get_html() 
    
    county_cities_heading_html =   "<div>Get County Cities</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [county_cities_heading_html,county_cities_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)
    
    
def display_get_cities_for_state(parms) :
    
    state_cities_form  =   InputForm(state_cities_input_id,
                                     state_cities_input_idList,
                                     state_cities_input_labelList,
                                     state_cities_input_typeList,
                                     state_cities_input_placeholderList,
                                     state_cities_input_jsList,
                                     state_cities_input_reqList)  
    
    selectDicts     =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)
    
    get_select_defaults(state_cities_form,
                        state_cities_input_id,
                        state_cities_input_idList,
                        state_cities_input_typeList,
                        selectDicts)

        
    state_cities_form.set_gridwidth(720)
    state_cities_form.set_custombwidth(100)
    
    state_cities_form.set_fullparms(True)
   
    state_cities_input_html = ""
    state_cities_input_html = state_cities_form.get_html() 
    
    state_cities_heading_html =   "<div>Get State Cities</div>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [state_cities_heading_html,state_cities_input_html]
    
    print("\n")
    display_generic_grid("geocode-utility-wrapper",gridclasses,gridhtmls)
    














