"""
# Userfns
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
from PyQt5 import uic

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont


import dfcleanser.common.cfg as cfg 

import logging
logger = logging.getLogger(__name__)

DEBUG_USERFNS     =   False


def classify_age(age) :

    if(age < 10) : return("Child")
    elif(age < 19) : return("Teen")
    elif(age > 65): return("Senior")
    else : return("Adult")


def map_ages(df,colname,newcolname,naaction=None) :

    if(naaction is None) :
        df[newcolname]  =   df[colname].map(classify_age, na_action=None)  
    else :
        df[newcolname]  =   df[colname].map(classify_age, na_action='ignore')


def classify_heritage(race_code) :

    if( (race_code == "A") or (race_code == "H") ) : return("White")
    elif(race_code == "W") : return("African American")
    elif(race_code == "C") : return("Hispanic")
    elif(race_code == "X") : return("Native")
    else                    : return("Other")


def apply_heritage(df,colname,descent) :

    df[colname].apply(classify_heritage)


def get_sex_crimes_criteria(df,colname) :

    criteria    =   ( (df[colname] == "BATTERY_WITH_SEXUAL_CONTACT") | 
                      (df[colname] == "BESTIALITY, CRIME AGAINST NATURE SEXUAL ASSAULT WITH AMIM0065") |
                      (df[colname] == "INDECENT EXPOSURE") |                   
                      (df[colname] == "LETTERS LEWD") | 
                      (df[colname] == "LEWD CONDUCT") | 
                      (df[colname] == "ORAL COPULATION") | 
                      (df[colname] == "PEEPING TOM") | 
                      (df[colname] == "RAPE, FORCIBLE") | 
                      (df[colname] == "PIMPING") | 
                      (df[colname] == "RAPE, ATTEMPTED") | 
                      (df[colname] == "SEXUAL PENETRATION WITH A FOREIGN OBJECT") | 
                      (df[colname] == "SEX UNLAWFUL") ) 
    
    return(criteria)




from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


"""
from datetime import datetime

d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

"""

date_reported   =   "Date Reported"
date_occurred   =   "Date Occurred"
date_response   =   "Date of Police Response"
date_arrest     =   "Date of Arrest"
date_closed     =   "Date of Closure"


def get_addl_dates(column_name,df,colnum) :

    if(column_name == date_response) :
        response_dates  =   []
        for i in range(len(df)) :
            start_date  =   df.iloc[i,colnum]
            end_date    =   start_date + timedelta(days=2)
            response_dates.append(random_date(start_date,end_date))
        return(response_dates)
    
    elif(column_name == date_arrest) :
        arrest_dates  =   []
        for i in range(len(df)) :
            start_date  =   df.iloc[i,colnum]
            end_date    =   start_date + timedelta(days=10)
            arrest_dates.append(random_date(start_date,end_date))
        return(arrest_dates)    

    elif(column_name == date_closed) :
        closed_dates  =   []
        for i in range(len(df)) :
            start_date  =   df.iloc[i,colnum]
            end_date    =   start_date + timedelta(days=365)
            closed_dates.append(random_date(start_date,end_date))
        return(closed_dates)



TIME_HOUR       =   0
TIME_MINUTE     =   1
TIME_SECOND     =   2

def build_time_component(x,time_incr,time_unit) :

    hours       =   0
    minutes     =   0
    seconds     =   0


    if(time_unit == TIME_HOUR) :

        hours   =   x * time_incr
    
    elif(time_unit == TIME_MINUTE) :

        total_minutes   =   x * time_incr
        hours           =   int(total_minutes / 60)
        minutes         =   int(total_minutes - (hours * 60))
        seconds         =   0

    else:

        total_seconds   =   x * time_incr
        hours           =   int(total_seconds / 3600)
        seconds         =   total_seconds - (hours * 3600)
        minutes         =   int(seconds / 60)
        seconds         =   int(seconds - (minutes * 60))
        

    from datetime import time
    date_time_time = time(hours,minutes,seconds)

    return(date_time_time)



Topanga_Area_Station    =   ["21501 Schoenborn St. Canoga Pk. 91304",[34.2214,-118.6]]

West_Valley_Station     =   ["19020 Vanowen St. Reseda 91335",[34.1933,-118.547]]

Devonshire_Station      =   ["10250 Etiwanda Ave. Northridge 91325",[34.2569,-118.531]]

Mission_Station         =   ["11121 N. Sepulveda Bl. Mission Hills 91345",[34.273,-118.468]]

Foothill_Station        =   ["12760 Osborne St. Pacoima 91331",[34.2531,-118.41]]

Valley_Bureau           =   ["870 Nollan Pl. Panorama City 91402",[34.2139,-118.445]]

Van_Nuys_Station        =   ["6240 Sylmar Ave. Van Nuys 91401",[34.1832,-118.445]]

N_Hollywood_Station     =   ["11640 Burbank Bl. N. Hwd 91601",[34.1716,-118.386]]

Northeast_Station       =   ["3353 San Fernando Rd. L.A. 90065",[34.1192,-118.249]]

Central_Bureau          =   ["251 E. 6th St. L.A. 90014" ,[34.0439,-118.247]]

Rampart_Station         =   ["1401 W. 6th St. L.A. 90017",[34.0566,-118.267]]

Newton_Station          =   ["3400 S. Central Ave. L.A. 90011",[34.0122,-118.256]]

Harbor_Station          =   ["2175 John S. Gibson Bl. San Pedro 90731",[33.7577,-118.289]]

Southeast_Station       =   ["145 W. 108th St. L.A. 90061",[33.9387,-118.275]]

South_Bureau            =   ["7600 S. Broadway L.A. 90003",[33.9701,-118.278]]

Southwest_Station       =   ["1546 W. Martin Luther King Jr. Bl. L.A. 90062",[34.0105,-118.305]]

South_Traffic_Division  =   ["4125 Crenshaw Bl. L.A. 90008",[34.0093,-118.336]]

Pacific_Station         =   ["12312 Culver Bl. L.A. 90066",[33.9916,-118.42]]

West_LA_Station         =   ["1663 Butler Ave. L.A. 90025",[34.0438,-118.451]]

Willshire_Station       =   ["4861 Venice Bl. L.A. 90019",[34.0469,-118.343]]

West_Bureau             =   ["4849 Venice Bl. L.A. 90019",[34.047,-118.343]]

Olympic_Station         =   ["1130 S. Vermont Ave. L.A. 90006",[34.0502,-118.291]]

Hollywood_Station       =   ["1358 N. Wilcox Ave. L.A. 90028",[34.0958,-118.331]]


police_stations         =   [Topanga_Area_Station,West_Valley_Station,Devonshire_Station,Mission_Station,Foothill_Station,Valley_Bureau,Van_Nuys_Station,N_Hollywood_Station,Northeast_Station,
                             Central_Bureau,Rampart_Station,Newton_Station,Harbor_Station,Southeast_Station,South_Bureau,Southwest_Station,South_Traffic_Division,Pacific_Station,West_LA_Station,
                             Willshire_Station,West_Bureau,Olympic_Station,Hollywood_Station]



Northwest_Boundary      =   ["6100 Sepulveda Blvd, Van Nuys, CA 91411",[34.1813,-118.464]]

Northeast_Boundary      =   ["4550 Oak Grove Dr, Pasadena, CA 91103",[34.1955,-118.174]]

Southwest_Boundary      =   ["736 Bart Earle Wy, Rolling Hills Estates, CA 90274",[33.771,-118.369]]

Souteast_Boundary      =   ["13225 Beach Blvd, Westminster, CA 92683",[33.7686,-117.993]]


precint_names           =   ["Topanga_Area_Station","West_Valley_Station","Devonshire_Station","Mission_Station","Foothill_Station","Valley_Bureau",
                            "Van_Nuys_Station","N_Hollywood_Station","Northeast_Station","Central_Bureau","Rampart_Station","Newton_Station",
                            "Harbor_Station","Southeast_Station","South_Bureau","Southwest_Station","South_Traffic_Division","Pacific_Station",
                            "West_LA_Station","Willshire_Station","West_Bureau","Olympic_Station","Hollywood_Station"]

precint_locations       =   [[34.2214,-118.6],[34.1933,-118.547],[34.2569,-118.531],[34.273,-118.468],[34.273,-118.468],[34.2139,-118.445],
                             [34.1832,-118.445],[34.1716,-118.386],[34.1192,-118.249],[34.0439,-118.247],[34.0566,-118.267],[34.0122,-118.256],
                             [33.7577,-118.289],[33.9387,-118.275],[33.9701,-118.278],[34.0105,-118.305],[34.0093,-118.336],[33.9916,-118.42],
                             [34.0438,-118.451],[34.0469,-118.343],[34.047,-118.343],[34.0502,-118.291],[34.0958,-118.331]]


def get_random_geocode(topWest,bottomEast,round) :

    max_lat = topWest[0]
    max_lng = topWest[1]
    
    min_lat = bottomEast[0]
    min_lng = bottomEast[1]

    import random
    random_lat  =   random.uniform(max_lat, min_lat)   
    random_lat  =   round(random_lat,4) 

    random_lng  =   random.uniform(max_lng, min_lng)   
    random_lng  =   round(random_lng,4) 

    return((random_lat,random_lng))


def get_suspect_locs(dftitle) :

    from dfcleanser.common.cfg import get_dfc_dataframe_df

    df = get_dfc_dataframe_df(dftitle) 

    suspect_locs    =   []

    for i in range(len(df)) :

        suspect_locs.append(str(get_random_geocode([34.1813,-118.464],[33.7686,-117.993],round)))


    return(suspect_locs)



#df.iloc[0, df.columns.get_loc("a")]#



















