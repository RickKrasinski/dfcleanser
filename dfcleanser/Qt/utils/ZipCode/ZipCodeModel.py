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


DEBUG_ZIPS      =   False



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
#   Zip Code common 
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

from dfcleanser.common.cfg import get_common_files_path

zipcodes_file_name          =   get_common_files_path() + "uszips.csv"

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

"""
#--------------------------------------------------------------------------
#   Zip Code City List types 
#--------------------------------------------------------------------------
"""
CITY_ZIPS_PRIMARY_LIST          =   "CITY_ZIPS_PRIMARY_LIST"
CITY_ZIPS_SECONDARY_LIST        =   "CITY_ZIPS_SECONDARY_LIST"
CITY_ZIPS_POBOX_LIST            =   "CITY_ZIPS_POBOX_LIST"
CITY_ZIPS_UNIQUES_LIST          =   "CITY_ZIPS_UNIQUES_LIST"
CITY_ZIPS_UNACCEPTABLE_LIST     =   "CITY_ZIPS_UNACCEPTABLE_LIST"
CITY_ZIPS_DECOMMISSIONED_LIST   =   "CITY_ZIPS_DECOMMISSIONED_LIST"


"""
#--------------------------------------------------------------------------
#   Zip Code location types 
#--------------------------------------------------------------------------
"""
PRIMARY_LOCATION_TYPE                   =   "PRIMARY"
ACCEPTABLE_LOCATION_TYPE                =   "ACCEPTABLE"
PRIMARY_OR_ACCEPTABLE_LOCATION_TYPE     =   "PRIMARY_OR_ACCEPTABLE"
NOT_ACCEPTABLE_LOCATION_TYPE            =   "NOT ACCEPTABLE"
ANY_LOCATION_TYPE                       =   "ANY"

"""
#--------------------------------------------------------------------------
#   Zip Code status types 
#--------------------------------------------------------------------------
"""
ACTIVE_STATUS_TYPE          =   "ACTIVE"
DECOMMISIONED_STATUS_TYPE   =   "DECOMMISIONED"
EITHER_STATUS_TYPE          =   "EITHER"

"""
#--------------------------------------------------------------------------
#   Zip Code types 
#--------------------------------------------------------------------------
"""
UNIQUE_ZIPCODE_TYPE         =   "UNIQUE"
STANDARD_ZIPCODE_TYPE       =   "STANDARD"
PO_BOX_ZIPCODE_TYPE         =   "PO BOX"
MILITARY_TYPE               =   "MILITARY"
DIPLOMATIC_TYPE             =   "DIPLOMATIC"
APO_ZIPCODE_TYPE            =   "APO"
FPO_ZIPCODE_TYPE            =   "FPO"
DPO_ZIPCODE_TYPE            =   "DPO"
ANY_ZIPCODE_TYPE            =   "ANY"

UNIQUE_text                 =   "Single Address Post Office"
STANDARD_text               =   "Standard Post Office"
PO_BOX_text                 =   "PO Box Post Office"
APO_text                    =   "Air Army Post Office"
FPO_text                    =   "Fleet Post Office"
DPO_text                    =   "Diplomatic Post Office"


"""
#--------------------------------------------------------------------------
#   Zip Code df column offsets 
#--------------------------------------------------------------------------
"""

ZIPCODE_OFFSET              =   0
STATE_OFFSET                =   1
CITY_OFFSET                 =   2
NAME_OFFSET                 =   3
COUNTY_OFFSET               =   4
LATITUDE_OFFSET             =   5
LONGITUDE_OFFSET            =   6
AREA_CODES_OFFSET           =   7
ZIPCODE_TYPE_OFFSET         =   8
LOCATION_TYPE_OFFSET        =   9
ACTIVE_STATUS_OFFSET        =   10


"""
#--------------------------------------------------------------------------
#   Zip Code table types 
#--------------------------------------------------------------------------
"""

CITY_ZIPCODES_TABLE         =   0
STATE_COUNTIES_TABLE        =   1
COUNTY_CITIES_TABLE         =   2
STATE_CITIES_TABLE          =   3



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    Basic Zipcode Attributes                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_cities_for_zipcode(zipcode,location_type=PRIMARY_LOCATION_TYPE,active_status=ACTIVE_STATUS_TYPE) :
    return(us_zipcodes.get_zip_cities(zipcode,location_type,active_status))

def get_business_name_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_business_name(zipcode))

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
        
        city    =   get_cities_for_zipcode(zipcode,city_type=PRIMARY_LOCATION_TYPE)
        
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

def get_active_status_for_zipcode(zipcode) :
    return(us_zipcodes.get_zip_active_status(zipcode))
    

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Basic Location Data Methods                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_zipcodes_for_city(state, city, zipcode_list_type) : 
    return(us_zipcodes.get_city_zips_list(state, city, zipcode_list_type))  
    
def get_counties_for_state(state) :
    return(us_zipcodes.get_state_counties_list(state))

def get_cities_for_county(state,county,city_type) :
    return(us_zipcodes.get_cities_for_county(state,county,city_type))

def get_cities_for_state(state,city_type) :
    return(us_zipcodes.get_cities_for_state(state,city_type))



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     US ZipCodes data store                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


class US_Zipcodes :
    
    zipcodes        =   None
    cities          =   None
    
    # full constructor
    def __init__(self) :

        print("zipcodes_file_name",zipcodes_file_name)

        self.zipcodes  =   pd.read_csv(zipcodes_file_name,dtype=uszips_dtypes)
        
        #print("zipcodes",len(self.zipcodes))
        
        self.zipcodes["State"]                  =   self.zipcodes["State"].astype(str)
        self.zipcodes["City"]                   =   self.zipcodes["City"].astype(str)
        self.zipcodes["BusinessName"]           =   self.zipcodes["BusinessName"].astype(str)
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
        
            
    def get_zip_cities(self,zipcode,location_type,active_status) : 
        
        try :
            
            if(active_status == ACTIVE_STATUS_TYPE) :
            
                if(location_type == PRIMARY_OR_ACCEPTABLE_LOCATION_TYPE) :
                
                    criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                      ( (self.zipcodes["LocationType"] == PRIMARY_LOCATION_TYPE) | 
                                                        (self.zipcodes["LocationType"] == ACCEPTABLE_LOCATION_TYPE) ) )
                
                elif(location_type == ANY_LOCATION_TYPE) :
                
                    criteria                    =   (self.zipcodes["Zipcode"] == zipcode) 
                        
                elif(location_type == PRIMARY_LOCATION_TYPE) :
                
                    criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                      (self.zipcodes["LocationType"] == PRIMARY_LOCATION_TYPE) & 
                                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE))
                
                elif(location_type == ACCEPTABLE_LOCATION_TYPE) :
                
                    criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                      (self.zipcodes["LocationType"] == ACCEPTABLE_LOCATION_TYPE) & 
                                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE))

                elif(location_type == NOT_ACCEPTABLE_LOCATION_TYPE) :
                
                    criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                      (self.zipcodes["LocationType"] == NOT_ACCEPTABLE_LOCATION_TYPE))

                else :
                
                    criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                      (self.zipcodes["LocationType"] == location_type) )
                    
            elif(active_status == DECOMMISIONED_STATUS_TYPE) :
                
                criteria                    =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                                  (self.zipcodes["ActiveStatus"] == DECOMMISIONED_STATUS_TYPE))
                
            zipcode_cities_df         =   self.zipcodes[criteria]
            
            zipcode_city    =   []
            
            for i in range(len(zipcode_cities_df)) :
                zipcode_city.append(zipcode_cities_df.iloc[i,CITY_OFFSET])
            
            if(active_status == ACTIVE_STATUS_TYPE) :
                if( (location_type == PRIMARY_LOCATION_TYPE) or 
                    (location_type == ACCEPTABLE_LOCATION_TYPE) or 
                    (location_type == NOT_ACCEPTABLE_LOCATION_TYPE) ):
                    return(zipcode_city)
            else :
                return(zipcode_city)
            
            return(None)
                
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
            
            if(len(county_df) > 0) :
                return(county_df.iloc[0,COUNTY_OFFSET]) 
            else :
                return(None)
            
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    def get_zip_business_name(self, zipcode) :  
        
        try :
            
            criteria                =   ( (self.zipcodes["Zipcode"] == zipcode) )
            zip_business_name_df    =   self.zipcodes[criteria]
            
            if(len(zip_business_name_df) > 0) :
                
                for i in range(len(zip_business_name_df)) :
                    if(zip_business_name_df[i,LOCATION_TYPE_OFFSET] == PRIMARY_LOCATION_TYPE) :
                        business_name   =   zip_business_name_df[i,NAME_OFFSET]
                        
                for i in range(len(zip_business_name_df)) :
                    if(not (zip_business_name_df[i,NAME_OFFSET] == business_name) ) :
                        return(zip_business_name_df[i,NAME_OFFSET])
                
                return(None) 
            else :
                return(None)
            
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_business_name Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    def get_zip_state(self, zipcode) :  
        
        try :
            criteria      =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                (self.zipcodes["LocationType"] == "PRIMARY") )
            state_df      =   self.zipcodes[criteria]
            
            if(len(state_df) > 0) :
                return(state_df.iloc[0,STATE_OFFSET])
            else :
                return(None)
            
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
            
            if(len(latitude_df) > 0) :
                return(latitude_df.iloc[0,LATITUDE_OFFSET]) 
            else :
                return(None)
            
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
            
            if(len(longitude_df)) :
                return(longitude_df.iloc[0,LONGITUDE_OFFSET]) 
            else :
                return(None)
            
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
            
            if(len(area_codes_df) > 0) :
                area_codes  =   area_codes_df.iloc[0,AREA_CODES_OFFSET]
            else :
                area_codes  =   None
            
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
            criteria            =   ( (self.zipcodes["Zipcode"] == zipcode) )
            zipcode_type_df     =   self.zipcodes[criteria]
            
            if(len(zipcode_type_df) > 0) :
                
                for i in range(len(zipcode_type_df)) :
                    if(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == UNIQUE_ZIPCODE_TYPE) :
                        return(UNIQUE_ZIPCODE_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == PO_BOX_ZIPCODE_TYPE) :
                        return(PO_BOX_ZIPCODE_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == MILITARY_TYPE) :
                        return(MILITARY_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == DIPLOMATIC_TYPE) :
                        return(DIPLOMATIC_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == APO_ZIPCODE_TYPE) :
                        return(APO_ZIPCODE_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == FPO_ZIPCODE_TYPE) :
                        return(FPO_ZIPCODE_TYPE)
                    elif(zipcode_type_df.iloc[i,ZIPCODE_TYPE_OFFSET] == DPO_ZIPCODE_TYPE) :
                        return(DPO_ZIPCODE_TYPE)
                    else :
                        return(STANDARD_ZIPCODE_TYPE)

            else :
                return(None)
            
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zipcode_type Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    def get_zip_location_type(self, zipcode) :  
        
        try :
            criteria                =   ( (self.zipcodes["Zipcode"] == zipcode) )
            zip_location_type_df    =   self.zipcodes[criteria]
            
            if(len(zip_location_type_df) > 0) :
                
                
                
                return(zip_location_type_df.iloc[0,ACTIVE_STATUS_OFFSET]) 
            else :
                return(None)
            
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

    def get_zip_active_status(self, zipcode) :  
        
        try :
            criteria                =   ( (self.zipcodes["Zipcode"] == zipcode) & 
                                          (self.zipcodes["LocationType"] == "PRIMARY") )
            zip_active_status_df    =   self.zipcodes[criteria]
            
            if(len(zip_active_status_df) > 0) :
                return(zip_active_status_df.iloc[0,ACTIVE_STATUS_OFFSET]) 
            else :
                return(None)
            
        except KeyError :
            return(None)
        except IndexError :
            return(None)
        except Exception :
            print("get_zip_state Exception : ",sys.exc_info()[0],sys.exc_info()[1])
            traceback.print_tb(sys.exc_info()[2])

            
    def get_city_zips_list(self, state, city, zipcode_list_type) :

        if(DEBUG_ZIPS) :        
            print("get_city_zips_list",state, city, zipcode_list_type)
            print(self.zipcodes["State"])

        state   =   state.upper()
        city    =   city.upper()
        
        try :
            
            if(zipcode_list_type == CITY_ZIPS_PRIMARY_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ZipcodeType"] == STANDARD_ZIPCODE_TYPE) & 
                                      (self.zipcodes["LocationType"] == PRIMARY_LOCATION_TYPE) &
                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE) )
                
            elif(zipcode_list_type == CITY_ZIPS_SECONDARY_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ZipcodeType"] == STANDARD_ZIPCODE_TYPE) & 
                                      (self.zipcodes["LocationType"] == ACCEPTABLE_LOCATION_TYPE) &
                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE) )
                
            elif(zipcode_list_type == CITY_ZIPS_POBOX_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ZipcodeType"] == PO_BOX_ZIPCODE_TYPE) & 
                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE) )
                
            elif(zipcode_list_type == CITY_ZIPS_UNIQUES_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ZipcodeType"] == UNIQUE_ZIPCODE_TYPE) & 
                                      #(self.zipcodes["LocationType"] != NOT_ACCEPTABLE_CITY_TYPE) &
                                      (self.zipcodes["ActiveStatus"] == ACTIVE_STATUS_TYPE) )
                
            elif(zipcode_list_type == CITY_ZIPS_UNACCEPTABLE_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ZipcodeType"] != UNIQUE_ZIPCODE_TYPE) & 
                                      (self.zipcodes["LocationType"] == NOT_ACCEPTABLE_LOCATION_TYPE) )
                
            elif(zipcode_list_type == CITY_ZIPS_DECOMMISSIONED_LIST) :
                
                zips_criteria   =   ( (self.zipcodes["State"] == state) & 
                                      (self.zipcodes["City"] == city) & 
                                      (self.zipcodes["ActiveStatus"] == DECOMMISIONED_STATUS_TYPE) )
                
            else :
                
                return(None)
                
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
            
            if(city_type == ANY_LOCATION_TYPE) :
                
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
            
            if(city_type == ANY_LOCATION_TYPE) :
                
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


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    US ZipCodes data store end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Zip Code attributes 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_zipcode_attributes(zipcode) :
    
    
    zip_attrs_dict          =   {}
    
    
    primary_cities          =   get_cities_for_zipcode(zipcode,location_type=PRIMARY_LOCATION_TYPE)
    acceptable_cities       =   get_cities_for_zipcode(zipcode,location_type=ACCEPTABLE_LOCATION_TYPE)
    not_acceptable_cities   =   get_cities_for_zipcode(zipcode,location_type=NOT_ACCEPTABLE_LOCATION_TYPE)
    
    zipcode_business_name   =   get_business_name_for_zipcode(zipcode)
    
    zipcode_county          =   get_county_for_zipcode(zipcode) 
    zipcode_state           =   get_state_for_zipcode(zipcode)
    
    zipcode_latitude        =   get_latitude_for_zipcode(zipcode) 
    zipcode_longitude       =   get_longitude_for_zipcode(zipcode)
    
    zipcode_areacodes       =   get_areacodes_for_zipcode(zipcode)
    
    zipcode_active_status   =   get_active_status_for_zipcode(zipcode)
    
    zipcode_type            =   get_type_for_zipcode(zipcode)
    
    if(zipcode_type == UNIQUE_ZIPCODE_TYPE) :
        zipcode_type_text   =   UNIQUE_text
    elif(zipcode_type == STANDARD_ZIPCODE_TYPE) :
        zipcode_type_text   =   STANDARD_text
    elif(zipcode_type == PO_BOX_ZIPCODE_TYPE) :
        zipcode_type_text   =   PO_BOX_text
    elif(zipcode_type == APO_ZIPCODE_TYPE) :
        zipcode_type_text   =   STANDARD_text
    elif(zipcode_type == FPO_ZIPCODE_TYPE) :
        zipcode_type_text   =   FPO_text
    elif(zipcode_type == DPO_ZIPCODE_TYPE) :
        zipcode_type_text   =   DPO_text
    else :
        zipcode_type_text   =   "Unkniwn"
        
    if( (not (primary_cities is None)) ) :
        zip_attrs_dict.update({"Primary City(s)":primary_cities})
    else :
        zip_attrs_dict.update({"Primary City(s)":"Zipcode is Invalid : No Primary City"})
        
    if( (not (acceptable_cities is None)) ) :
        zip_attrs_dict.update({"Acceptable City(s)": acceptable_cities})
    else :
        zip_attrs_dict.update({"Acceptable City(s)": None})

    if( (not (not_acceptable_cities is None)) ) :
        zip_attrs_dict.update({"Not Acceptable City(s)": not_acceptable_cities})
    else :
        zip_attrs_dict.update({"Not Acceptable City(s)": None})

    zip_attrs_dict.update({"Business/Neighborhood Name" : zipcode_business_name})
    zip_attrs_dict.update({"County" : zipcode_county})
    zip_attrs_dict.update({"State" : zipcode_state})
    
    import numpy
    if( (zipcode_latitude is None) or (zipcode_longitude is None) or 
       (numpy.isnan(zipcode_latitude)) or (numpy.isnan(zipcode_longitude)) ) :
        ziplatlong    =   "Unknown"
    else :
        ziplatlong    =   "[" + str(round(zipcode_latitude,7)) + " , " + str(round(zipcode_longitude,7)) + "]"
        
    zip_attrs_dict.update({"[Latitude, Longitude]" : ziplatlong})
    
    if(not (zipcode_areacodes is None)) :
        
        if(type(zipcode_areacodes) == list) :
            for i in range(len(zipcode_areacodes)) :
                zipcode_areacodes[i]       =   zipcode_areacodes[i].replace("'","")
                    
        zipareacodes    =   str(zipcode_areacodes)
    else :
        zipareacodes    =   "Unknown"

    zip_attrs_dict.update({"Area Codes" : zipareacodes})
    
    zip_attrs_dict.update({"Current Status" : zipcode_active_status})
    zip_attrs_dict.update({"Zipcode Type" : zipcode_type_text})
    
    return(zip_attrs_dict)
    














