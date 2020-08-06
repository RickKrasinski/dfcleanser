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

import sys
this = sys.modules[__name__]

import pandas as pd
#import json
import numpy as np


state_ids_list          =   ["AL","AS","AK","AR","AZ","CA","CO","CT","DC",
                             "DE","FL","FM","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA",
                             "MA","MD","ME","MH","MI","MN","MO","MP","MS","MT",
                             "NC","ND","NE","NH","NJ","NM","NV","NY",
                             "OH","OK","OR","PA","PR","PW","RI","SC","SD",
                             "TN","TX","UT","VA","VI","VT","WA","WI","WV","WY",
                             "AE","AA","AP"]

state_names_list        =   ["Alabama","American_Samoa","Alaska","Arkansas","Arizona","California","Colorado","Connecticut","District_Of_Columbia",
                             "Delaware","Florida","Federated_States_Of_Micronesia","Georgia","Guam","Hawaii","Iowa","Idaho","Illinois","Indiana","Kansas","Kentucky","Louisiana",
                             "Massachusetts","Maryland","Maine","Marshall_Islands","Michigan","Minnesota","Missouri","Northern_Mariana_Islands","Mississippi","Montana",
                             "North_Carolina","North_Dakota","Nebraska","New_Hampshire","New_Jersey","New_Mexico","Nevada","New_York",
                             "Ohio","Oklahoma","Oregon","Pennsylvania","Puerto_Rico","Palau","Rhode_Island","South_Carolina","South_Dakota",
                             "Tennessee","Texas","Utah","Virginia","Virgin_Islands","Vermont","Washington","Wisconsin","West_Virginia","Wyoming",
                             "Armed_Forces_Foreign","Armed_Forces_America","Armed_Forces_Pacific"]

def get_state_name(stateid) :
    
    for i in range(len(state_ids_list)) :
        if(state_ids_list[i] == stateid) :
            return(state_names_list[i])

    return(None)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Bulk Geocoder runtime settings
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DISPLAY_MAIN                =   0
DISPLAY_ZIP_ATTRS           =   1
DISPLAY_ZIP_LOC_DATA        =   2

DISPLAY_GET_CITY_ZIPS       =   3
DISPLAY_GET_STATE_COUNTIES  =   4
DISPLAY_GET_COUNTY_CITIES   =   5
DISPLAY_GET_STATE_CITIES    =   6

PROCESS_ZIP_ATTRS           =   7
PROCESS_GET_CITY_ZIPS       =   8
PROCESS_GET_STATE_COUNTIES  =   9
PROCESS_GET_COUNTY_CITIES   =   10
PROCESS_GET_STATE_CITIES    =   11


zipcodes_file_name          =   "C:/Tech/Projects/Jupyter/Python/dfcleansergit/dfcleanser_census/working/uszips.csv"

uszips_columns              =   ["Zipcode","State","City","County","Latitude","Longitude","AreaCodes","ZipcodeType","LocationType","ActiveStatus"]

uszips_dtypes               =   {"Zipcode" : str,
                                 "State" : str,
                                 "City" : str,
                                 "County" : str,
                                 "Latitude" : np.float64,
                                 "Longitude" : np.float64,
                                 "AreaCodes" : str,
                                 "ZipcodeType" : str,
                                 "LocationType" : str,
                                 "ActiveStatus" : str}

import sys
import traceback


PRIMARY_CITY_TYPE           =   "PRIMARY"
ACCEPTABLE_CITY_TYPE        =   "ACCEPTABLE"
NOT_ACCEPTABLE_CITY_TYPE    =   "NOT ACCEPTABLE"
ANY_CITY_TYPE               =   "ANY"

ACTIVE_STATUS_TYPE          =   "ACTIVE"
DECOMMISIONED_STATUS_TYPE   =   "DECOMMISIONED"
EITHER_STATUS_TYPE          =   "EITHER"

UNIQUE_ZIPCODE_TYPE         =   "UNIQUE"
STANDARD_ZIPCODE_TYPE       =   "STANDARD"
PO_BOX_ZIPCODE_TYPE         =   "PO BOX"
MILITARY_TYPE               =   "MILITARY"
DIPLOMATIC_TYPE             =   "DIPLOMATIC"
APO_ZIPCODE_TYPE            =   "APO"
FPO_ZIPCODE_TYPE            =   "FPO"
DPO_ZIPCODE_TYPE            =   "DPO"
ANY_ZIPCODE_TYPE            =   "ANY"

UNIQUE_text                 =   "Unique Govt Post Office"
STANDARD_text               =   "Standard Post Office"
PO_BOX_text                 =   "PO Box Post Office"
APO_text                    =   "Air Army Post Office"
FPO_text                    =   "Fleet Post Office"
DPO_text                    =   "Diplomatic Post Office"




def get_cities_for_zipcode(zipcode,city_type=PRIMARY_CITY_TYPE,active_status=ACTIVE_STATUS_TYPE) :
    return(us_zipcodes.get_zip_cities(zipcode,city_type,active_status))

def get_county_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_county(zipcode))

def get_state_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_state(zipcode))

def get_latitude_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_latitude(zipcode))    

def get_longitude_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_longitude(zipcode))    

def get_areacodes_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_area_codes(zipcode))
    
def get_type_for_zipcode(zipcode) :
    
    zctype  =   us_zipcodes.get_zipcode_type(zipcode)
    
    if(zctype == DIPLOMATIC_TYPE) :
        return(DPO_ZIPCODE_TYPE)
    
    elif(zctype == MILITARY_TYPE) :
        
        city    =   get_cities_for_zipcode(zipcode,city_type=PRIMARY_CITY_TYPE)
        
        if(city == APO_ZIPCODE_TYPE) :
            return(APO_ZIPCODE_TYPE)
        elif(city == FPO_ZIPCODE_TYPE) :
            return(FPO_ZIPCODE_TYPE)
        elif(city == DPO_ZIPCODE_TYPE) :
            return(DPO_ZIPCODE_TYPE)
        else :
            return("MILITARY")
        
    else :
        return(zctype)  
    
def is_zipcode_active(zipcode) :
    
    status  =   us_zipcodes.get_zip_active_status(zipcode)
    if(status == ACTIVE_STATUS_TYPE) :
        return(True)
    else :
        return(False)

    
def get_zipcodes_for_city(state, city, zipcode_type=ANY_ZIPCODE_TYPE, active_status=ACTIVE_STATUS_TYPE) :
    return(us_zipcodes.get_city_zips_list(state, city, zipcode_type, active_status))    
    
def get_counties_for_state(state) :
    return(us_zipcodes.get_state_counties_list(state))

def get_cities_for_county(state,county,city_type) :
    return(us_zipcodes.get_cities_for_county(state,county,city_type))

def get_cities_for_state(state,city_type) :
    return(us_zipcodes.get_cities_for_state(state,city_type))


class US_Zipcodes :
    
    zipcodes        =   None
    cities          =   None
    
    # full constructor
    def __init__(self) :

        self.zipcodes  =   pd.read_csv(zipcodes_file_name,dtype=uszips_dtypes)
        
        self.zipcodes["State"]                  =   self.zipcodes["State"].astype(str)
        self.zipcodes["City"]                   =   self.zipcodes["City"].astype(str)
        self.zipcodes["County"]                 =   self.zipcodes["County"].astype(str)
        self.zipcodes["AreaCodes"]              =   self.zipcodes["AreaCodes"].astype(str)
        self.zipcodes["ZipcodeType"]            =   self.zipcodes["ZipcodeType"].astype(str)
        self.zipcodes["LocationType"]           =   self.zipcodes["LocationType"].astype(str)
        self.zipcodes["ActiveStatus"]           =   self.zipcodes["ActiveStatus"].astype(str)
                
        self.zipcodes["AreaCodes"]              =   self.zipcodes["AreaCodes"].astype(object)
        self.zipcodes["AreaCodes"]              =   self.zipcodes["AreaCodes"].apply(lambda x: None if x == "nan" else x)
        self.zipcodes["ZipcodeType"]            =   self.zipcodes["ZipcodeType"].astype(object)
        self.zipcodes["ZipcodeType"]            =   self.zipcodes["ZipcodeType"].apply(lambda x: None if x == "nan" else x)
        self.zipcodes["LocationType"]           =   self.zipcodes["LocationType"].astype(object)
        self.zipcodes["LocationType"]           =   self.zipcodes["LocationType"].apply(lambda x: None if x == "nan" else x)
        self.zipcodes["ActiveStatus"]           =   self.zipcodes["ActiveStatus"].astype(object)
        self.zipcodes["ActiveStatus"]           =   self.zipcodes["ActiveStatus"].apply(lambda x: None if x == "nan" else x)
        
        self.cities     =   self.zipcodes
        self.cities.set_index(keys=["State","City"],drop=False)
        
            
    def get_zip_cities(self, zipcode,city_type,active_status) :  
        
        
        
        acceptable_cities_list      =   []
        unacceptable_cities_list    =   []
        
        try :
            
            criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                              (self.zipcodes["LocationType"] == "PRIMARY") )
            primary_zipcode_city_df     =   self.zipcodes[criteria]
            
            zipcode_status              =   primary_zipcode_city_df.iloc[0,9] 
            zipcode_city                =   primary_zipcode_city_df.iloc[0,2]
            
            if( (active_status == DECOMMISIONED_STATUS_TYPE) and
                (not(zipcode_status == DECOMMISIONED_STATUS_TYPE)) ):
                    return(None)
            
            if( (active_status == ACTIVE_STATUS_TYPE) and
                (not(zipcode_status == ACTIVE_STATUS_TYPE)) ) :
                    return(None)
                    
            if(city_type == PRIMARY_CITY_TYPE) :
                return(zipcode_city)
                        
            elif( (city_type == NOT_ACCEPTABLE_CITY_TYPE) or (city_type == ANY_CITY_TYPE) ) :
                
                criteria        =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                      (self.zipcodes["LocationType"] == NOT_ACCEPTABLE_CITY_TYPE) )
                city_rows_df    =   self.zipcodes[criteria]
                
                if(len(city_rows_df) > 0) :
                    unacceptable_cities_list    =   list(city_rows_df["City"].unique())
                else :
                    unacceptable_cities_list    =   []
                    
                if(city_type == ANY_CITY_TYPE) :
                    
                    criteria        =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                          (self.zipcodes["LocationType"] == ACCEPTABLE_CITY_TYPE) )
                    city_rows_df    =  self.zipcodes[criteria]
                    
                    if(len(city_rows_df) > 0) :
                        acceptable_cities_list    =   list(city_rows_df["City"].unique())
                        acceptable_cities_list.append(zipcode_city)
                    else :
                        acceptable_cities_list    =   [zipcode_city]
                            
            else :
                        
                criteria        =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                      (self.zipcodes["LocationType"] == ACCEPTABLE_CITY_TYPE) )
                city_rows_df    =  self.zipcodes[criteria]
                
                if(len(city_rows_df) > 0) :
                    acceptable_cities_list    =   list(city_rows_df["City"].unique())
                else :
                    acceptable_cities_list    =   []
                    
            
            all_cities_list     =   [] 

            if(len(acceptable_cities_list) > 0) :
                for j in range(len(acceptable_cities_list)) :
                    all_cities_list.append(acceptable_cities_list[j])
                    
            if(len(unacceptable_cities_list) > 0) :
                for j in range(len(unacceptable_cities_list)) :
                    all_cities_list.append(unacceptable_cities_list[j])
                    
            return(all_cities_list)
                            
        except KeyError :
            return(None)
        except IndexError : 
            return(None)
        except Exception :
            print("get_zip_cities : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

            

    def get_zip_county(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            county_df     =   self.zipcodes[criteria]
            return(county_df.iloc[0,3])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])


    def get_zip_state(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            state_df      =   self.zipcodes[criteria]
            return(state_df.iloc[0,1])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])


    def get_zip_latitude(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            latitude_df   =   self.zipcodes[criteria]
            return(latitude_df.iloc[0,4])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])
            
    def get_zip_longitude(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            longitude_df  =   self.zipcodes[criteria]
            return(longitude_df.iloc[0,5])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    def get_zip_area_codes(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            area_codes_df =   self.zipcodes[criteria]
            area_codes    =   area_codes_df.iloc[0,6]    
            
            if(not (area_codes is None)) :
                area_codes  =   area_codes.replace(" ","")
                area_codes  =   area_codes.split(",")
                area_codes.sort()
                if(len(area_codes) > 0) :
                    return(area_codes)
                else :
                    return(None)
            else :
                return(None)
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    
    def get_zipcode_type(self, zipcode) :  
        
        try :
            criteria            =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                      (self.zipcodes["LocationType"] == "PRIMARY") )
            zipcode_type_df     =   self.zipcodes[criteria]
            return(zipcode_type_df.iloc[0,7])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zipcode_type Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])


    def get_zip_active_status(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            latitude_df   =   self.zipcodes[criteria]
            return(latitude_df.iloc[0,9])    
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

            
    def get_city_zips_list(self, state, city, zipcode_type, active_status) :

        state   =   state.upper()
        city    =   city.upper()
        
        try :
            
            if(zipcode_type == ANY_ZIPCODE_TYPE) :
                
                if(active_status == EITHER_STATUS_TYPE) :
                    
                    zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                          (self.zipcodes["City"] == city) )
                
                else :
                    
                    zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                          (self.zipcodes["City"] == city) & 
                                          (self.zipcodes["ActiveStatus"] == active_status) )
            
            else : 
                
                if(active_status == EITHER_STATUS_TYPE) :
                    
                    zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                          (self.zipcodes["City"] == city) &
                                          (self.zipcodes["ZipcodeType"] == zipcode_type) )
                
                else :
                    
                    zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                          (self.zipcodes["City"] == city) & 
                                          (self.zipcodes["ZipcodeType"] == zipcode_type) &
                                          (self.zipcodes["ActiveStatus"] == active_status) )
 
            zips_df         =   self.zipcodes[zips_criteria]
            
            if(len(zips_df) > 0) :
                
                zips_list   =   list(zips_df["Zipcode"].unique())
                zips_list.sort()
                return(zips_list)
                
            else :
                
                return(None)

        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])
            
            
    def get_state_counties_list(self, state) :
        
        try :
            
            state_criteria  =   ( (self.zipcodes["State"] == state) )
            counties_df     =   self.zipcodes[state_criteria]
            
            counties        =   list(counties_df["County"].unique())
            counties.sort()
            
            return(counties)
                
        except KeyError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

            
    def get_cities_for_county(self, state, county, city_type) :  
        
        try :
            
            state   =   state.upper()
            county  =   county.upper()
            
            if(city_type == ANY_CITY_TYPE) :
                
                city_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["County"] == county))
                
            else :
                
                city_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["County"] == county) & 
                                      (self.zipcodes["LocationType"] == city_type))
               
            cities_df       =   self.zipcodes[city_criteria]
            
            cities          =   list(cities_df["City"].unique())
            cities.sort()
            
            return(cities)
                
        except KeyError :
            return(None)
        except Exception :
            print("get_cities_for_county : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])


    def get_cities_for_state(self, state, city_type) :  
        
        try :
            
            state   =   state.upper()
            
            if(city_type == ANY_CITY_TYPE) :
                
                city_criteria   =   ( (self.zipcodes["State"] == state) )
                
            else :
                
                city_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["LocationType"] == city_type))
               
            cities_df       =   self.zipcodes[city_criteria]
            
            cities          =   list(cities_df["City"].unique())
            cities.sort()
            
            return(cities)
                
        except KeyError :
            return(None)
        except Exception :
            print("get_cities_for_county : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

        

us_zipcodes    =   US_Zipcodes()























