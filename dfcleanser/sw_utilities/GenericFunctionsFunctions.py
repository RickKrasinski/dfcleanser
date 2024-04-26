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
* -------------------------------------------------------------
*                    System Generic Functions data
* -------------------------------------------------------------
* -------------------------------------------------------------
"""


def get_generic_function_code(ftitle) :
    
    import inspect
    
    if(ftitle.find("upper_lower_case_df_column") > -1)                  :   return(inspect.getsource(upper_lower_case_df_column))
    elif(ftitle.find("normalize_df_column")  > -1)                      :   return(inspect.getsource(normalize_df_column))
    elif(ftitle.find("get_trig_values_for_column") > -1)                :   return(inspect.getsource(get_trig_values_for_column))
    elif(ftitle.find("convert_df_column_to_degrees_or_radians") > -1)   :   return(inspect.getsource(convert_df_column_to_degrees_or_radians))
    elif(ftitle.find("absolute_df_column") > -1)                        :   return(inspect.getsource(absolute_df_column))
    elif(ftitle.find("round_df_column") > -1)                           :   return(inspect.getsource(round_df_column))
    elif(ftitle.find("get_dist_from_center_pt") > -1)                   :   return(inspect.getsource(get_dist_from_center_df_column))
    elif(ftitle.find("get_dist_from_point") > -1)                       :   return(inspect.getsource(get_dist_from_point_df_column))
    elif(ftitle.find("random_int_range") > -1)                          :   return(inspect.getsource(random_int_range))
    elif(ftitle.find("random_float_range") > -1)                        :   return(inspect.getsource(random_float_range))
    elif(ftitle.find("random_datetime_range") > -1)                     :   return(inspect.getsource(random_datetime_range))
    elif(ftitle.find("get_trig_value") > -1)                            :   return(inspect.getsource(get_trig_values_for_column))
    else                                                                :   return("No code found")              


"""
* -------------------------------------------------------------
* -------------------------------------------------------------
*                    System Generic Functions
* -------------------------------------------------------------
* -------------------------------------------------------------
"""

UPPER_CASE  =   0
LOWER_CASE  =   1


def upper_lower_case_df_column(dftitle, dfcolname, caseopt, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : convert string column to upper case
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  caseopt     - upper lower case select
    *  opstat      - opstatus
    *
    * returns : 
    *    Successful : upper cased columns list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    df                  =   cfg.get_dfc_dataframe_df(dftitle)
    new_col_values      =   []

    try :
        
        if(caseopt == UPPER_CASE) :
            new_col_values  =   df[dfcolname].map(lambda x: str(x).upper())
        else :
            new_col_values  =   df[dfcolname].map(lambda x: str(x).lower())
        
        return(new_col_values)
        
    except Exception as e:
        opstat.store_exception("'upper_lower_case_df_column' error : " + str(caseopt) + " : " + dftitle + " " + dfcolname,e)
        return(None)
        
    

def normalize_df_column(dftitle, dfcolname, normtype, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : normalize a dataframe column
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  opstat      - opstatus
    *
    * returns : 
    *    Successful : normalized column list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    df      =   cfg.get_dfc_dataframe_df(dftitle)
 
    try :
        
        if(normtype == 0) :
        
            col_mean    =   df[dfcolname].mean()
            col_std     =   df[dfcolname].std()
        
            normalized_col  =   (df[dfcolname]-col_mean)/col_std
        
        else :
        
            col_min     =   df[dfcolname].min()
            col_max     =   df[dfcolname].max()
        
            normalized_col  =   (df[dfcolname]-col_min)/(col_max-col_min)
        
    except Exception as e:
        opstat.store_exception("'normalize_df_column' error : " + dftitle + " " + dfcolname,e)
        return(None)
    
    return(normalized_col)
        
    

def get_trig_values_for_column(dftitle, dfcolname, trigfunc, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get trig column values
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  trigfunc      - trig function to apply 
    *                    ('sin','cos','tan','arcsin','arccos','arctan')
    *
    * returns : 
    *    Successful : col list of trig values  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    df  =   cfg.get_dfc_dataframe_df(dftitle)

    try :
        
        import numpy as np
        trigcol = np.array()
    
        if(trigfunc == 'sin')       :   trigcol = np.sin(df[dfcolname])
        elif(trigfunc == 'cos')     :   trigcol = np.cos(df[dfcolname])
        elif(trigfunc == 'tan')     :   trigcol = np.tan(df[dfcolname])
        elif(trigfunc == 'arcsin')  :   trigcol = np.arcsin(df[dfcolname])
        elif(trigfunc == 'arccos')  :   trigcol = np.arccos(df[dfcolname])
        elif(trigfunc == 'arctan')  :   trigcol = np.arctan(df[dfcolname])
        else                        :   
            trigcol     =   None
            
        return(trigcol)
                
    except Exception as e:
        opstat.store_exception("'get_trig_values_for_column' error : " + dftitle + " " + dfcolname + " " + trigfunc,e)
        return(None)
        

def convert_df_column_to_degrees_or_radians(dftitle, dfcolname, degrees, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees or radians
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *  degrees       - True  - convert to degrees
    *                  False - conveet to radians
    *
    * returns : 
    *    Successful : converted column values list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    df = cfg.get_dfc_dataframe_df(dftitle)

    import numpy as np
    colvalues = np.array()

    try :
        
        if(degrees) :
            colvalues   =   np.degrees(df[dfcolname])
        else :
            colvalues   =   np.radians(df[dfcolname])
            
        return(colvalues)
    
    except Exception as e:
        opstat.store_exception("'convert_df_column_to_degrees_or_radians' error : " + dftitle + " " + dfcolname + " " + str(degrees),e)
        return(None)
        

def random_int_range(dftitle, randomIntLower, randomIntUpper,opstat) :
    """
    * -------------------------------------------------------
    * function : generate column of random ints in a range
    * 
    * parms :
    *  dftitle          - dataframe title
    *  randomIntLower   - random integer lower range value
    *  randomIntUpper   - random integer upper range value
    *
    * returns : 
    *    Successful : column values list of random ints  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * --------------------------------------------------------
    """

    #opstat              =   opStatus()
    df = cfg.get_dfc_dataframe_df(dftitle)
    
    #import numpy as np
    import random
    
    colrandints = []
    
    try :
        
        for i in range(len(df)) :
            colrandints.append(random.randrange(int(randomIntLower),int(randomIntUpper))) 
            
        return(colrandints)
        
    except Exception as e:
        opstat.store_exception("'random_int_range' error : " + dftitle + " " + str(randomIntLower) + " " + str(randomIntUpper),e)
        return(None)


def random_float_range(dftitle, randomFloatLower, randomFloatUpper, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : generate column of random floats in a range
    * 
    * parms :
    *  dftitle            - dataframe title
    *  randomFloatLower   - random integer lower range value
    *  randomFloatUpper   - random integer upper range value
    *
    * returns : 
    *    Successful : cols list of random floats  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    #opstat              =   opStatus()
    df = cfg.get_dfc_dataframe_df(dftitle)
    
    import numpy as np
    import random
    
    colrandfloats  =   np.array()
    
    try :
        
        for i in range(len(df)) :
            colrandfloats.append(random.randrange(float(randomFloatLower),float(randomFloatUpper)))  
        
        return(colrandfloats)
        
    except Exception as e:
        opstat.store_exception("'random_float_range' error : " + dftitle + " " + str(randomFloatLower) + " " + str(randomFloatUpper),e)
        return(None)


def random_datetime_range(dftitle, randomdatetimeLower, randomdatetimeUpper,opstat) :
    """
    * ------------------------------------------------------------------------
    * function : generate column of random floats in a range
    * 
    * parms :
    *  dftitle              - dataframe title
    *  randomdatetimeLower  - random datetime lower range value
    *  randomdatetimeUpper  - random datetime upper range value
    *
    * returns : 
    *    Successful : cols list of random datetimes  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    #opstat              =   opStatus()
    df = cfg.get_dfc_dataframe_df(dftitle)
    
    import numpy as np
    import random
    
    colranddatetimes  =   np.array()
    
    try :
        
        lower_datetime  =   0
        upper_datetime  =   0
        
        for i in range(len(df)) :
            colranddatetimes.append(random.randrange(int(lower_datetime),int(upper_datetime)))  
        
        return(colranddatetimes)
        
    except Exception as e:
        opstat.store_exception("'random_float_range' error : " + dftitle + " " + str(randomdatetimeLower) + " " + str(randomdatetimeUpper),e)
        return(None)


def absolute_df_column(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to absolute value
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *
    * returns : 
    *    Successful : col list of abs values  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    opstat              =   opStatus()
    df = cfg.get_dfc_dataframe_df(dftitle)

    import numpy as np
    colabsolutes = np.array()

    try :
        
        colabsolutes   =   np.absolute(df[dfcolname])
        return(colabsolutes)
        
    except Exception as e:
        opstat.store_exception("'absolute_df_column' error : " + dftitle + " " + dfcolname,e)
        return(opstat)


def round_df_column(dftitle, dfcolname, decimals) :
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
    *    Successful : roundex col vals list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """
    
    opstat              =   opStatus()
    df = cfg.get_dfc_dataframe_df(dftitle)

    import numpy as np
    dfrounds = np.array()

    try :
        
        if(decimals == 0) :
            dfrounds    =   np.rint(df[dfcolname])
        else :
            dfrounds    =   np.round_(df[dfcolname,decimals])
            
        return(dfrounds)
                
    except Exception as e:
        opstat.store_exception("'round_df_column' error : " + dftitle + " " + dfcolname + " " + str(decimals),e)
        return(opstat)
        

def get_dist_from_center_df_column(df,dfcolname,units,opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get the distance from geocode center 
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  units         - distance units
    *
    * returns : 
    *    Successful : distance col vals list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("get_dist_from_center_df_column")


def get_dist_from_point_df_column(df,dfcolname,point,units,opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get the distance from geocode pt 
    * 
    * parms :
    *  dftitle       - dataframe title
    *  dfcolname     - dataframe column to round
    *  units         - distance units
    *  decimals      - rounding precision
    *                   0 - round to int
    *
    * returns : 
    *    Successful : distance col vals list  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    print("get_dist_from_point_df_column")



def get_df_geocode_center(dftitle,dfcolname,opstat) :
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
    
    #opstat  =   opStatus()
    
    import json
    
    geocoords   =   []
    
    df  =   cfg.get_dfc_dataframe_df(dftitle) 
    
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
        return(None)
                
                
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
        




        
        
       
        







        
