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


LAMBDA              =   True
FULL_FUNCTION       =   False
EITHER              =   2

def is_lambda_function(ftitle) :
    
    if(ftitle == "to_int_df_column")                            :   return(FULL_FUNCTION)
    elif(ftitle == "to_float_df_column")                        :   return(FULL_FUNCTION)
    elif(ftitle == "to_string_df_column")                       :   return(FULL_FUNCTION)
    elif(ftitle == "upperCase_df_column")                       :   return(FULL_FUNCTION)
    elif(ftitle == "normalize_df_column")                       :   return(FULL_FUNCTION)
    elif(ftitle == "normalize_list")                            :   return(LAMBDA)
    elif(ftitle == "get_trig_values_for_column")                :   return(FULL_FUNCTION)
    elif(ftitle == "get_trigonometric_values")                  :   return(LAMBDA)
    elif(ftitle == "convert_df_column_to_degrees_or_radians")   :   return(FULL_FUNCTION)
    elif(ftitle == "convert_to_degrees_or_radians")             :   return(LAMBDA)
    elif(ftitle == "absolute_df_column")                        :   return(FULL_FUNCTION)
    elif(ftitle == "absolute_values")                           :   return(LAMBDA)
    elif(ftitle == "round_df_col_float")                        :   return(FULL_FUNCTION)
    elif(ftitle == "get_df_geocode_center")                     :   return(FULL_FUNCTION)
    elif(ftitle == "get_geocode_center")                        :   return(FULL_FUNCTION)


def get_function_parms(ftitle) :
    
    if(ftitle == "to_int_df_column")                            :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "to_float_df_column")                        :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "to_string_df_column")                       :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "upperCase_df_column")                       :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "normalize_df_column")                       :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "normalize_list")                            :   fparms  =   "invalue"
    elif(ftitle == "get_trig_values_for_column")                :   fparms  =   "dftitle,dfcolname,trigfunc,newcolname"
    elif(ftitle == "get_trigonometric_values")                  :   fparms  =   "invalue,trigfunc"
    elif(ftitle == "convert_df_column_to_degrees_or_radians")   :   fparms  =   "dftitle,dfcolname,degrees,newcolname"
    elif(ftitle == "convert_to_degrees_or_radians")             :   fparms  =   "invalue,degrees"
    elif(ftitle == "absolute_df_column")                        :   fparms  =   "dftitle,dfcolname,newcolname"
    elif(ftitle == "absolute_values")                           :   fparms  =   "invalue"
    elif(ftitle == "round_df_col_float")                        :   fparms  =   "dftitle,dfcolname,decimals,newcolname"
    elif(ftitle == "get_df_geocode_center")                     :   fparms  =   "dfname,dfcolname"
    elif(ftitle == "get_geocode_center")                        :   fparms  =   "geocoords"
    
    fparms  =   fparms.split(",")
    
    return(fparms)


def get_function_call(ftitle,fparms_dict) :
 
    print("get_function_call",ftitle,fparms_dict)
    lambda_flag     =   is_lambda_function(ftitle)
    funcparms       =   get_function_parms(ftitle)
    
    if(not (lambda_flag)) :
        
        func_call       =   (ftitle + "(")

        for i in range(len(funcparms)) :
            
            if(funcparms[i] == "dftitle") :
                if(not (fparms_dict.get("dftitle",None) is None)) :
                    func_call       =   (func_call + "'" + fparms_dict.get("dftitle",None) + "'")
                else :
                    func_call       =   (func_call + "****")
            elif(funcparms[i] == "dfcolname") :
                if(not (fparms_dict.get("dfcolname",None) is None)) :
                    func_call       =   (func_call + ",  '" + fparms_dict.get("dfcolname",None) + "'")
                else :
                    func_call       =   (func_call + ",  ****")
            elif(funcparms[i] == "newcolname") :
                newcol  =  fparms_dict.get("newcolname",None)
                if( (not (newcol is None)) and (not (newcol == "None")) ) :
                    func_call       =   (func_call + ",  '" + newcol + "'")
                #else :
                    #if(not(newcol is None)) :
                        #func_call       =   (func_call + " ,****")
            elif(funcparms[i] == "opstat") :
                func_call       =   (func_call + ",  opstat ")
            else :
                func_call       =   (func_call + ",  " + "****") 

        func_call       =   (func_call + ")") 
        
    else :
        
        func_call   =   "lambda x: " + ftitle + "(x" 
        for i in range(len(funcparms)) :
            if(not(funcparms[i] == "invalue")) :
                func_call       =   (func_call + "," + "  ****")    
        func_call   =   func_call + ")"  
    return(func_call)


   
def to_int_df_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert a string column to int
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to apply float to
    *  newcolname  - dataframe column to add and store result in 
    *                 : if None modify dfcolname in place
    *
    * returns : 
    *     opstat object for status
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
            df[dfcolname] = df[dfcolname].astype('int',copy=False)
        else :
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,newcolname)) :
                df[newcolname] = df[dfcolname].astype('int')
            else :
                new_col_values  =   df[dfcolname].astype('int')
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, new_col_values, opstat)
                
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Convert to int Error : " + str(sys.exc_info()[0].__name__)) 
        
    return(opstat)

    
def to_float_df_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : convert a string column to int
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to apply float to
    opstat  =   opStatus()
    *  newcolname  - dataframe column to add and store result in 
    *                 : if None modify dfcolname in place
    *
    * returns : 
    *     opstat object for status
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
            df[dfcolname] = df[dfcolname].astype('float',copy=False)
        else :
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,newcolname)) :
                df[newcolname] = df[dfcolname].astype('float')
            else :
                new_col_values  =   df[dfcolname].astype('float')
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, new_col_values, opstat)
                
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Convert to float Error : " + str(sys.exc_info()[0].__name__))        

    return(opstat)
    
    
def to_string_df_column(dftitle, dfcolname, newcolname=None) :
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
            df[dfcolname] = df[dfcolname].astype('str',copy=False)
        else :
            from dfcleanser.common.common_utils import is_column_in_df
            if(is_column_in_df(df,newcolname)) :
                df[newcolname] = df[dfcolname].astype('str')
            else :
                new_col_values  =   df[dfcolname].astype('str')
                from dfcleanser.data_transform.data_transform_columns_control import add_column
                add_column(dftitle, newcolname, new_col_values, opstat)
                
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Covert to string : " + str(sys.exc_info()[0].__name__))        

    return(opstat) 
       
    
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
    
    
def normalize_list(inlist) :
    """
    * ------------------------------------------------------------------------
    * function : normalize a list of values
    * 
    * parms :
    *  inlist    - list of values
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
    scaled_values = scaler.fit_transform(inlist)

    return(scaled_values)


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


def get_trigonometric_values(invalue, trigfunc) :
    """
    * ------------------------------------------------------------------------
    * function : get normalized column values
    * 
    * parms :
    *  invalue       - input value
    *  trigfunc      - trig function to apply 
    *                    ('sin','cos','tan','arcsin','arccos','arctan')
    *
    * returns : 
    *    trig value
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    import numpy as np
    
    if(trigfunc == 'sin')           :   return(np.sin(invalue))
    elif(trigfunc == 'cos')         :   return(np.cos(invalue))
    elif(trigfunc == 'tan')         :   return(np.tan(invalue))
    elif(trigfunc == 'arcsin')      :   return(np.arcsin(invalue))
    elif(trigfunc == 'arccos')      :   return(np.arccos(invalue))
    elif(trigfunc == 'arctan')      :   return(np.arctan(invalue))
    else                            :   return(None)


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


def convert_to_degrees_or_radians(invalue, degrees) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees
    * 
    * parms :
    *  invalue       - values to convert
    *  degrees       - True  - convert to degrees
    *                  False - conveet to radians
    *
    * returns : 
    *    invalues converted and returned
    *    if type(invalue) == list return list
    *    else  return singleton
    *
    * Notes : 
    *    dfcleanser generic function
    *    lamda compatible
    * -------------------------------------------------------------------------
    """

    import numpy as np
    if(degrees) :
        return(np.degrees(invalue))
    else :
        return(np.radians(invalue))


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
    

def round_df_col_float(dftitle, dfcolname, decimals, newcolname=None) :
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
        
        kwargs_text     =   "from " + module + " import " + fname + new_line
        kwargs_text     =   kwargs_text + fname + "("
        
        for i in range(len(kwargs)) :
            
            if(i == (len(kwargs)-1)) :
                endchar     =   ""
            else :
                endchar     =   ", "
            
            if(i>0) :
                kwargs_text     =   kwargs_text  + kwargs[i] + "="  
            
            if(not(kwvals is None)) :
                
                kwval   =   kwvals.get(kwargs[i],None)
                if(kwval is None) :
                    kwargs_text     =   kwargs_text  + " 'USER VALUE' " + endchar  
                else :
                    kwargs_text     =   kwargs_text  + str(kwval) + endchar  
            else :    
                kwargs_text     =   kwargs_text  + " 'user value' " + endchar
                
        kwargs_text     =   kwargs_text + ") "        
                
        return(kwargs_text)
        
    else :
        
        return(None)


def get_df_function_source(ftitle,sourceOnly=True) :

    import inspect
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctions

    if(ftitle == reservedfunctions[0])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_int_df_column
        gfcode      =   inspect.getsource(to_int_df_column)        
    elif(ftitle == reservedfunctions[1])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_float_df_column
        gfcode      =   inspect.getsource(to_float_df_column) 
    elif(ftitle == reservedfunctions[2])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_string_df_column
        gfcode      =   inspect.getsource(to_string_df_column) 
    elif(ftitle == reservedfunctions[3])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import upperCase_df_column
        gfcode      =   inspect.getsource(upperCase_df_column) 
    elif(ftitle == reservedfunctions[4])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import normalize_df_column
        gfcode      =   inspect.getsource(normalize_df_column) 
    elif(ftitle == reservedfunctions[5])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import normalize_list
        gfcode      =   inspect.getsource(normalize_list) 
    elif(ftitle == reservedfunctions[6])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_trig_values_for_column
        gfcode      =   inspect.getsource(get_trig_values_for_column) 
    elif(ftitle == reservedfunctions[7])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_int_df_column
        gfcode      =   inspect.getsource(to_int_df_column) 
    elif(ftitle == reservedfunctions[8])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_float_df_column
        gfcode      =   inspect.getsource(to_float_df_column) 
    elif(ftitle == reservedfunctions[9])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import to_string_df_column
        gfcode      =   inspect.getsource(to_string_df_column) 
    elif(ftitle == reservedfunctions[10])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import upperCase_df_column
        gfcode      =   inspect.getsource(upperCase_df_column) 
    elif(ftitle == reservedfunctions[11])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_trigonometric_values
        gfcode      =   inspect.getsource(get_trigonometric_values) 
    elif(ftitle == reservedfunctions[12])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import convert_df_column_to_degrees_or_radians
        gfcode      =   inspect.getsource(convert_df_column_to_degrees_or_radians) 
    elif(ftitle == reservedfunctions[13])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import convert_to_degrees_or_radians
        gfcode      =   inspect.getsource(convert_to_degrees_or_radians) 
    elif(ftitle == reservedfunctions[14])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import absolute_df_column
        gfcode      =   inspect.getsource(absolute_df_column) 
    elif(ftitle == reservedfunctions[15])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import absolute_values
        gfcode      =   inspect.getsource(absolute_values) 
    elif(ftitle == reservedfunctions[16])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import round_df_col_float
        gfcode      =   inspect.getsource(round_df_col_float) 
    elif(ftitle == reservedfunctions[17])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_df_geocode_center
        gfcode      =   inspect.getsource(get_df_geocode_center) 
    elif(ftitle == reservedfunctions[18])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_geocode_center
        gfcode      =   inspect.getsource(get_geocode_center) 
        
    if(sourceOnly) :
        firstcomment    =   gfcode.find('"""')
        secondcomment   =   gfcode.find('"""',firstcomment + 3)
        
        newgfcode       =   gfcode[secondcomment+3:]
        newgfcode       =   newgfcode.lstrip("\n")
        newgfcode       =   newgfcode.lstrip("\n")

        return(str(newgfcode))
        
    else :
        return(gfcode)
        
        
        
        
        
        







        
