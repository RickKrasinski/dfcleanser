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

def add_normalized_column(dftitle, dfcolname, newcolname=None) :
    """
    * ------------------------------------------------------------------------
    * function : add a normalized column to a dataframe
    * 
    * parms :
    *  dftitle     - dataframe title
    *  dfcolname   - dataframe column to normalize
    *  newcolname  - dataframe column to add
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


def get_normalized_column_values(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : get normalized column values
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to normalize
    *
    * returns : 
    *    normalized columns list
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

    return(scaled_values)


def normalize_column(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : normalize a column in place
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to normalize
    *
    * returns : 
    *    N/A
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

    df[dfcolname] = scaled_values


def get_trigonometric_column_values(dftitle, dfcolname, trigfunc) :
    """
    * ------------------------------------------------------------------------
    * function : get normalized column values
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *   trigfunc         - trig function to apply ('sin','cos','tan','arcsin','arccos','arctan')
    *
    * returns : 
    *    trig columns list
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
    

def convert_to_degrees(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to degrees
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *
    * returns : 
    *    N/A column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    df[dfcolname] = np.degrees(df[dfcolname])


def convert_to_radians(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to radians
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *
    * returns : 
    *    N/A column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    df[dfcolname] = np.radians(df[dfcolname])


def absolute_column(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : convert dataframe column to absolute value
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to apply trig function to
    *
    * returns : 
    *    N/A column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    df[dfcolname] = np.absolute(df[dfcolname])


def round_to_int(dftitle, dfcolname) :
    """
    * ------------------------------------------------------------------------
    * function : round float column to decials range
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to round
    *
    * returns : 
    *    N/A column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    df[dfcolname] = np.rint(df[dfcolname])


def round_float(dftitle, dfcolname, decimals) :
    """
    * ------------------------------------------------------------------------
    * function : round float column to decials range
    * 
    * parms :
    *  dftitle             - dataframe title
    *  dfcolname     - dataframe column to round
    *  decimals        - round precision
    *
    * returns : 
    *    N/A column changed in place
    *
    * Notes : 
    *    dfcleanser generic function
    * -------------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import get_dfc_dataframe
    df = get_dfc_dataframe(dftitle)

    import numpy as np
    df[dfcolname] = np.round_(df[dfcolname,decimals])

