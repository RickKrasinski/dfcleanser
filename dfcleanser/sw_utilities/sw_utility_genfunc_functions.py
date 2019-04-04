"""
# sw_utility_genfunc_functions 
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 03:09:39 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
   
def to_numeric_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert a string column to float
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to apply float to
    *  newcolname  - dataframe column to add and store result in 
    *                 : if None modify dfcolname in place
    *
    * returns : 
    *     dataframe column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("a_to_long_column")
    
    
def to_string_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert numeric column to string
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  newcolname  - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    df column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("to_string_column")
    
    
def upperCase_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert string column to upper case
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  newcolname  - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    df column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("upperCase_column")
    

def normalize_df_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : normalize a dataframe column
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  newcolname  - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    adds new normalized column to a dataframe
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler() 
    scaled_values = scaler.fit_transform(df[dfcolname])

    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    if(newcolname == None) :
        df[dfcolname] = scaled_values
    else :
        from dfcleanser.data_transform.data_transform_columns_control import add_column
        add_column(newcolname, scaled_values, opstat)

    if(not opstat.get_status()) :
        from dfcleanser.common.common_utils import display_exception
        display_exception(opstat)   


def normalize_list(valuesList) :
    """
    * ------------------------------------------------------------------------
    * function : normalize a list of values
    * 
    * parms :
    *  valuesList    - dataframe title
    *
    * returns : 
    *    normalized values
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler() 
    scaled_values = scaler.fit_transform(valuesList)

    valuesList = scaled_values


def get_trigonometric_column_values(dftitle, dfcolname, trigfunc) :
    """
    * ------------------------------------------------------------------------
    * function : get normalized column values
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  trigfunc      - trig function to apply 
    *                    ('sin','cos','tan','arcsin','arccos','arctan')
    *
    * returns : 
    *    updated df column
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np

    trigcol = np.array()

    if(trigfunc == 'sin') :
        trigcol = np.sin(df[dfcolname])
    elif(trigfunc == 'cos') :
        trigcol = np.cos(df[dfcolname])
    elif(trigfunc == 'tan') :
        trigcol = np.tan(df[dfcolname])
    elif(trigfunc == 'arcsin') :
        trigcol = np.arcsin(df[dfcolname])
    elif(trigfunc == 'arccos') :
        trigcol = np.arccos(df[dfcolname])
    else :
        trigcol = np.arctan(df[dfcolname])

    return(trigcol )
    

def convert_df_to_degrees_or_radians(dfname, dfcolname, degrees) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees
    * 
    * parms :
    *  dfname        - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  degrees       - True  - convert to degrees
    *                  False - conveet to radians
    *
    * returns : 
    *    df column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dfname)

    import numpy as np
    if(degrees) :
        df[dfcolname] = np.degrees(df[dfcolname])
    else :
        df[dfcolname] = np.radians(df[dfcolname])


def convert_to_degrees_or_radians(invalues, degrees) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees
    * 
    * parms :
    *  invalues      - values to convert
    *  degrees       - True  - convert to degrees
    *                  False - conveet to radians
    *
    * returns : 
    *    invalues converted and returned
    *    if type(invalues) == list return list
    *    else  return singleton
    *
    * Notes : 
    *    dfcleanser generic function
    *    lamda compatible
    * -------------------------------------------------------------------------
    """

    import numpy as np
    if(degrees) :
        return(np.degrees(invalues))
    else :
        return(np.radians(invalues))


def absolute_df_column(dfname, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to absolute value
    * 
    * parms :
    *  dfname        - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *
    * returns : 
    *    dfname[dfcolname] changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dfname)

    import numpy as np
    df[dfcolname] = np.absolute(df[dfcolname])


def absolute_values(invalue) :
    """
    * ------------------------------------------------------------------------
    * function : convert single or list to absolute value(s)
    * 
    * parms :
    *  invalue       - values(s) to take abs of
    *
    * returns : 
    *    if type(invalue) == list return a list 
    *    else return a singleton
    *
    * Notes : 
    *    dfcleanser generic function
    *    lamda compatible
    * -------------------------------------------------------------------------
    """

    import numpy as np
    return(np.absolute(invalue))
    

def round_float(dftitle, dfcolname, decimals) :
    """
    * ------------------------------------------------------------------------
    * function : round float column to decials range
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  decimals      - rounding precision
    *                   0 - round to int
    *
    * returns : 
    *    df column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    
    if(decimals == 0) :
        df[dfcolname] = np.rint(df[dfcolname])
    else :
        df[dfcolname] = np.round_(df[dfcolname,decimals])


def get_df_geocode_center(dfname,dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : get the center point of a dataframe locations column
    * 
    * parms :
    *  dfname        - dataframe name
    *  dfcolname     - dataframe column to use for locations
    *
    * returns : 
    *    center point if no exception
    *    opStatus object if exception
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()
    
    import json
    
    geocoords   =   []
    
    df  =   cfg.get_dfc_dataframe(dfname) 
    
    if(len(dfcolname == 1)) :
        geocoords   =   df[dfcolname[0]].tolist()
        
        if(type(geocoords[0]) == str) :
            geocoords   =   json.dumps(geocoords)   
            
    elif(len(dfcolname) == 2) :
            
        geolats     =   df[dfcolname[0]].tolist()
        if(type(geolats[0]) == str) :
            geolats   =   json.dumps(geolats)
                
        geolongs    =   df[dfcolname[1]].tolist()    
        if(type(geolongs[0]) == str) :
            geolongs   =   json.dumps(geolongs)
            
        for i in range(len(geolats)) :
            geocoords.append([geolats[i],geolongs[i]])
   
    else :
        
        opstat.set_status(False)
        opstat.set_errorMsg("get_df_geocode_center Error : column names list is invalid")
        return(opstat)

    if(opstat.get_status()) :
        return(get_geocode_center(geocoords,opstat))             
                
                
def get_geocode_center(geocoords,opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get the center point of a list of [lat,lng] locations
    * 
    * parms :
    *  geocoords     - geeoce locations list
    *
    * returns : 
    *    df column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    import math
    
    try :
        
        # verify geecoords 
        for i in range(len(geocoords)) :
            
            try :
                float(geocoords[i][0])
                float(geocoords[i][1])
            except :
                geocoords.pop(i)
    
        if(len(geocoords > 0)) :
            
            x = float(0)
            y = float(0)
            z = float(0)
            
            for i in range(len(geocoords)) :
                
                latitude    =   geocoords[i][0] * math.pi / 180
                longitude   =   geocoords[i][1] * math.pi / 180

                x   =   x + math.cos(latitude) * math.cos(longitude)
                y   =   y + math.cos(latitude) * math.sin(longitude)
                z   =   z + math.sin(latitude)
                
            x   =   x / len(geocoords)
            y   =   y / len(geocoords)
            z   =   z / len(geocoords)
            
            centralLongitude    =   math.atan2(y,x)
            centralSquareRoot   =   math.sqrt(x * x + y * y)
            centralLatitude     =   math.atan2(z, centralSquareRoot)
            
            centralLatitude     =   centralLatitude * 180 / math.pi
            centralLongitude    =   centralLongitude * 180 / math.pi
            
            return([centralLatitude,centralLongitude])
            
        else :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Calculate Geocode Center Error : geocoords list is empty")
            return(None)
            
    except :
        
        opstat.set_status(False)
        opstat.set_errorMsg("Calculate Geocode Center Exception : " + str(sys.exc_info()[0].__name__))
        return(None)
        

def get_function_help_doc(module,fname) :
    
    temp_file   =   "temp_help_file"
    
    import contextlib

    try :
        
        with open(temp_file, 'w') as f:
            with contextlib.redirect_stdout(f):
                help(module + "." + fname)
            
        f.close()
    
        with open(temp_file,'r') as h:
            textdata = h.read()

        h.close()
        
    except :
        textdata    =   ""
    
    if(len(textdata) > 0) :
        import os
        os.remove(temp_file)
    
        start_help  =   textdata.find(fname + "(")
    
        return(textdata[start_help:])
    else :
        return("")


def get_function_kwargs(module,fname,kwvals=None) :
    
    help_text   =   get_function_help_doc(module,fname)
    
    if(len(help_text) > 0) :
    
        start_kwargs    =   help_text.find("(")    
        end_kwargs      =   help_text.find(")")
        
        kwargs  =   help_text[start_kwargs+1:end_kwargs]
        kwargs  =   kwargs.split(",")
        
        for i in range(len(kwargs)) :
            kwargs[i]   =   kwargs[i].lstrip(" ")
            kwargs[i]   =   kwargs[i].rstrip(" ")
            
            defval      =   kwargs[i].find("=")
            if(defval > -1) :
                kwargs[i]   =   kwargs[i][:defval] 
        
        from dfcleanser.common.html_widgets import new_line
                
        kwargs_text     =   "{ " + new_line
        
        for i in range(len(kwargs)) :
            if(kwargs[i] == 'dftitle') :
                kwargs_text     =   kwargs_text  + kwargs[i] + " : '" + cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF) + "'," + new_line
                
            elif(kwargs[i] == 'dfcolname') :
                if(kwvals is None) :
                    kwargs_text     =   kwargs_text  + kwargs[i] + " : " + " 'user value' " + "," + new_line 
                else :
                    if(len(kwvals[1]) > 0) :
                        kwargs_text     =   kwargs_text  + kwargs[i] + " : " + str(kwvals[i]) + "," + new_line  
                    else :
                        kwargs_text     =   kwargs_text  + kwargs[i] + " : " + " 'user value' " + "," + new_line
            else :    
                kwargs_text     =   kwargs_text  + kwargs[i] + " : " + " 'user value' " + "," + new_line 
                
        kwargs_text     =   kwargs_text + "} "        
                
        return(kwargs_text)
        
    else :
        
        return(None)













        
