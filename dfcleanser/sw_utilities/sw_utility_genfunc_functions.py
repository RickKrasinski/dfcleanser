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
from dfcleanser.common.common_utils import opStatus


"""
* -------------------------------------------------------------
*                    System Generic Functions
* -------------------------------------------------------------
"""

def upperCase_df_column(dftitle, dfcolname, newcolname=None) :
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
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    try :
        
        if(newcolname is None) :
            df[dfcolname].apply(lambda x: x.upper(), inplace=True)
        else :
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,newcolname)) :
                df[newcolname] = map(lambda x: x.upper(), df[dfcolname])
            else :
                new_col_values  =   map(lambda x: x.upper(), df[dfcolname])
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, new_col_values, opstat)
        
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Covert to uppercase Error : " + str(sys.exc_info()[0].__name__))        
    
    return(opstat) 


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
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    from sklearn.preprocessing import MinMaxScaler

    try :
        
        scaler = MinMaxScaler() 
        scaled_values = scaler.fit_transform(df[dfcolname])

        if(newcolname == None) :
            df[dfcolname] = scaled_values
        else :
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,newcolname)) :
                df[newcolname] = scaled_values
            else :
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, scaled_values, opstat)
                
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Covert to uppercase Error : " + str(sys.exc_info()[0].__name__))        
        
    return(opstat)
    

def get_trig_values_for_column(dftitle, dfcolname, trigfunc, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : get trig column values
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  trigfunc      - trig function to apply 
    *                    ('sin','cos','tan','arcsin','arccos','arctan')
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    df  =   cfg.get_dfc_dataframe(dftitle)

    try :
        
        import numpy as np
        trigcol = np.array()
    
        if(not (df is None)) :
            
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,dfcolname)) :

                if(trigfunc == 'sin')       :   trigcol = np.sin(df[dfcolname])
                elif(trigfunc == 'cos')     :   trigcol = np.cos(df[dfcolname])
                elif(trigfunc == 'tan')     :   trigcol = np.tan(df[dfcolname])
                elif(trigfunc == 'arcsin')  :   trigcol = np.arcsin(df[dfcolname])
                elif(trigfunc == 'arccos')  :   trigcol = np.arccos(df[dfcolname])
                elif(trigfunc == 'arctan')  :   trigcol = np.arctan(df[dfcolname])
                else                        :   
                    opstat.set_status(False)
                    opstat.set_errorMsg("trig Func " + trigfunc + " is not supported")
                
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("df column name " + dfcolname + " is not found")
            
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("dataframe " + dftitle + " is not defined")
   
        if(opstat.get_status()) :
            if(not (newcolname is None)) :
                df[dfcolname]     =   trigcol
            else :
            
                from dfcleanser.common.common_utils import is_column_in_df
                if(not (is_column_in_df(df,newcolname))) :
                
                    from dfcleanser.data_transform.data_transform_columns_control import add_column
                    add_column(dftitle, newcolname, trigcol, opstat)
                
                else :
                    df[newcolname]  =   trigcol
        
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Covert to uppercase Error : " + str(sys.exc_info()[0].__name__))        
        
    return(opstat)

def convert_df_column_to_degrees_or_radians(dftitle, dfcolname, degrees, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees or radians
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  degrees       - True  - convert to degrees
    *                  False - conveet to radians
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    opstat  =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    colvalues = np.array()

    try :
        
        if(degrees) :
            colvalues   =   np.degrees(df[dfcolname])
        #df[dfcolname] = np.degrees(df[dfcolname])
        else :
            colvalues   =   np.radians(df[dfcolname])
    
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Covert to degrees/radians : " + str(sys.exc_info()[0].__name__))        
        
    if(opstat.get_status()) :
        
        try :
            
            if(not (newcolname is None)) :
                df[dfcolname]  =   colvalues
            else :
            
                from dfcleanser.common.common_utils import is_column_in_df
                if(not (is_column_in_df(df,newcolname))) :
                
                    from dfcleanser.data_transform.data_transform_columns_control import add_column
                    add_column(dftitle, newcolname, colvalues, opstat)
                
                else :
                    df[newcolname]  =   colvalues
                    
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Covert to degrees/radians : " + str(sys.exc_info()[0].__name__))        
                    
    return(opstat)


def absolute_df_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to absolute value
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    opstat  =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    colabsolutes = np.array()

    try :
        
        from dfcleanser.common.common_utils import is_column_in_df
        if(is_column_in_df(df,dfcolname)) :
            colabsolutes   =   np.absolute(df[dfcolname])
        
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("col name : " + dfcolname + " not found")        
            
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Convert to absolutes : " + str(sys.exc_info()[0].__name__))        

    if(opstat.get_status()) :
        if(newcolname is None) :
            df[dfcolname] = colabsolutes
        else :
            
            from dfcleanser.common.common_utils import is_column_in_df
            if(not (is_column_in_df(df,newcolname))) :
                
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, colabsolutes, opstat)
           
            else :
                df[newcolname] = colabsolutes        
                
    return(opstat)


def round_df_column(dftitle, dfcolname, decimals, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : round float column to decials range
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  decimals      - rounding precision
    *                   0 - round to int
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    opstat  =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    dfrounds = np.array()

    try :
        
        from dfcleanser.common.common_utils import is_column_in_df
        if(is_column_in_df(df,dfcolname)) :

            if(decimals == 0) :
                dfrounds    =   np.rint(df[dfcolname])
            else :
                dfrounds    =   np.round_(df[dfcolname,decimals])
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("col name : " + dfcolname + " not found")        
                
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Round Values : " + str(sys.exc_info()[0].__name__))        

    if(opstat.get_status()) :
        if(newcolname is None) :
            df[dfcolname] = dfrounds
        else :
            
            from dfcleanser.common.common_utils import is_column_in_df
            if(not (is_column_in_df(df,newcolname))) :
                
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, dfrounds, opstat)
                
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("col name : " + newcolname + " not found")        

    return(opstat)

def get_dist_from_center_df_column(dftitle,dfcolname,units,newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : get the distance from geocode center 
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  units         - distance units
    *  decimals      - rounding precision
    *                   0 - round to int
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("get_dist_from_center_df_column")

def get_dist_from_point_df_column(dftitle,dfcolname,point,units,newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : get the distance from geocode center 
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  units         - distance units
    *  decimals      - rounding precision
    *                   0 - round to int
    *  newcolname    - dataframe column to add - if None modify dfcolname in place
    *
    * returns : 
    *    opstat object for status
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("get_dist_from_point_df_column")



def get_df_geocode_center(dftitle,dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : get the center point of a dataframe locations column
    * 
    * parms :
    *  dftitle       - dataframe name
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
    
    opstat  =   opStatus()
    
    import json
    
    geocoords   =   []
    
    df  =   cfg.get_dfc_dataframe(dftitle) 
    
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

    if(opstat.get_status()) :
        return(get_geocode_center(geocoords,opstat)) 
    else :
        return(opstat)
                
                
def get_geocode_center(geocoords) :
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
    
    opstat  =   opStatus()
    
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
            return(opstat)
            
    except :
        
        opstat.set_status(False)
        opstat.set_errorMsg("Calculate Geocode Center Exception : " + str(sys.exc_info()[0].__name__))
        return(opstat)
        




        
        
       
        







        
