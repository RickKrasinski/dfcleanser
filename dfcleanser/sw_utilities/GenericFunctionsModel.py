"""
# sw_utility_genfunc_widgets
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.help_utils as dfchelp
import dfcleanser.common.cfg as cfg
from dfcleanser.common.common_utils import get_parms_for_input

"""
#--------------------------------------------------------------------------
#    apply dfc fn parms functions
#--------------------------------------------------------------------------
"""  

PROCESS_ROUND_FLOAT_FN                  =   500
PROCESS_TRIG_FN                         =   501 
PROCESS_RANDOM_INT_FN                   =   502 
PROCESS_RANDOM_FLOAT_FN                 =   503 
PROCESS_RANDOM_DATETIME_FN              =   504 
PROCESS_GEOCODE_DIST_CENTER_FN          =   505 
PROCESS_GEOCODE_DIST_POINT_FN           =   506 
PROCESS_STRIP_CHAR_FN                   =   507 
PROCESS_LSTRIP_CHAR_FN                  =   508 
PROCESS_RSTRIP_CHAR_FN                  =   509 
PROCESS_CENTER_STR_FN                   =   510 
PROCESS_LJUST_STR_FN                    =   511 
PROCESS_RJUST_STR_FN                    =   512 
PROCESS_REPLACE_STR_FN                  =   513 
PROCESS_SLICE_STR_FN                    =   514 

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    generic functions components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


genfns                              =   ["absolute()",
                                         "square()",
                                         "square_root()",
                                         "ceiling()",
                                         "floor()",
                                         "round_to_int()",
                                         "reciprocal()",
                                         "positive()",
                                         "negative()",
                                         "normalize_mean()",
                                         "normalize_min_max()",
                                         "uppercase_str()",
                                         "lowercase_str()",
                                         "todegrees()",
                                         "toradians()"
                                        ]

genfns_with_parms                   =   ["round_float(ndigits)",
                                         "strip(stripchar)",
                                         "lstrip(stripchar)",
                                         "rstrip(stripchar)",
                                         "center(width,fillchar)",
                                         "left_justify(width,fillchar)",
                                         "right_justify(width,fillchar)",
                                         "replace(oldchar,newchar)",
                                         "slice(startind,stopind)",
                                         "get_trig_value(trigfn)",
                                         "get_dist_from_center_pt(units)",
                                         "get_dist_from_point(units,pt)",
                                         "random_int_range(minint,maxint)",
                                         "random_float_range(minfloat,maxfloat)",
                                         "random_datetime_range(mindatetime,maxdatetime)"
                                         ]


reservedfunctionsmodule             =    "dfcleanser.sw_utilities.GenericFunctionsFunctions"

    



"""
#--------------------------------------------------------------------------
#    apply generic functions without parms to column
#--------------------------------------------------------------------------
"""

def get_column_from_dfc_apply_fn(callerid,df,dftitle,fntoapply,coltoapply,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process add column from a dfc function
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    import numpy as np
    
    if( (fntoapply == "uppercase_str()") or (fntoapply == "lowercase_str()") ) :
            
        from dfcleanser.common.common_utils import is_string_col
        if(not(is_string_col(df,coltoapply))) :
            opstat.set_status(False)
            opstat.set_errorMsg("Column " + coltoapply + " is not a string required for " + fntoapply)
            return(None)
               
    else :
            
        from dfcleanser.common.common_utils import is_numeric_col
        if(not(is_numeric_col(df,coltoapply))) :
            opstat.set_status(False)
            opstat.set_errorMsg("Column " + coltoapply + " is not a numeric required for " + fntoapply)
            return(None)
        
    np_array    =   df[coltoapply].to_numpy()
        
    try :
            
        if(fntoapply == "absolute()")           :    new_col_array   =   np.absolute(np_array)
        elif(fntoapply == "square()")           :    new_col_array   =   np.square(np_array)
        elif(fntoapply == "square_root()")      :    new_col_array   =   np.sqrt(np_array)
        elif(fntoapply == "ceiling()")          :    new_col_array   =   np.ceil(np_array)
        elif(fntoapply == "floor()")            :    new_col_array   =   np.floor(np_array)
        elif(fntoapply == "round_to_int()")     :    new_col_array   =   np.rint(np_array)
        elif(fntoapply == "reciprocal()")       :    new_col_array   =   np.reciprocal(np_array)
        elif(fntoapply == "positive()")         :    new_col_array   =   np.positive(np_array)
        elif(fntoapply == "negative()")         :    new_col_array   =   np.negative(np_array)
            
        elif(fntoapply == "normalize_mean()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import normalize_df_column
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   normalize_df_column(dftitle, coltoapply, 0, opstat)
        
        elif(fntoapply == "normalize_min_max()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import normalize_df_column
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   normalize_df_column(dftitle, coltoapply, 1, opstat)
            
        elif(fntoapply == "uppercase_str()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import upper_lower_case_df_column, UPPER_CASE
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   upper_lower_case_df_column(dftitle, coltoapply, UPPER_CASE, opstat)
                
        elif(fntoapply == "lowercase_str()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import upper_lower_case_df_column, LOWER_CASE
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   upper_lower_case_df_column(dftitle, coltoapply, LOWER_CASE, opstat)
            
        elif(fntoapply == "todegrees()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import convert_df_column_to_degrees_or_radians
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   convert_df_column_to_degrees_or_radians(dftitle, coltoapply, True, opstat)
            
        elif(fntoapply == "toradians()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import convert_df_column_to_degrees_or_radians
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            new_col_array   =   convert_df_column_to_degrees_or_radians(dftitle, coltoapply, False, opstat)
            
        clock.stop()
            
    except Exception as e:
        opstat.store_exception("Apply fn to Column Error : " + coltoapply + " " + fntoapply,e)

    if(opstat.get_status()) :
        return(new_col_array)
    else :
        return(None)
            
    return(None)


"""
#--------------------------------------------------------------------------
#    apply generic functions with parms to column
#--------------------------------------------------------------------------
"""

def get_column_from_dfc_with_parms_apply_fn(df,fnid,fntoapply,coltoapply,idlist,parms,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process add column from a dfc function
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
   
    fparms  =   get_parms_for_input(parms[2],idlist)
        
           
    if(fnid == dtm.PROCESS_ROUND_FLOAT_FN) :
        
        ndigits     =   fparms[1]
        
        if(len(ndigits) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No number_of_digits parm defined")
            
        else :
            try :
                ndigits         =   int(ndigits)
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("number_of_digits parm is not numeric")
         
        if(opstat.get_status()) :
            
            try :
                new_col_array   =   df[coltoapply].apply(lambda x: x.round(ndigits))
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)
                clock.stop()

            
    elif( (fnid == PROCESS_STRIP_CHAR_FN) or 
          (fnid == PROCESS_LSTRIP_CHAR_FN) or 
          (fnid == PROCESS_RSTRIP_CHAR_FN) ):
        
        stripchar     =   fparms[1]
        
        if(len(stripchar) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No character_to_strip parm defined")
        else :
            
            try :
                if(fnid == PROCESS_STRIP_CHAR_FN) :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).strip(stripchar))
                elif(fnid == PROCESS_LSTRIP_CHAR_FN) :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).lstrip(stripchar))
                else :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).rstrip(stripchar))
                    
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)
                clock.stop()

    
    elif( (fnid == PROCESS_CENTER_STR_FN) or 
          (fnid == PROCESS_LJUST_STR_FN) or 
          (fnid == PROCESS_RJUST_STR_FN) ) :
        
        width     =   fparms[1]
                
        if(len(width) == 0) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("No string_width parm defined")
        
        else :
            
            try :
                width         =   int(width)
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("string_width parm is not numeric")
        
            if(opstat.get_status()) :
            
                fillchar  =   fparms[2]
                if(len(fillchar) == 0) :
                    
                    opstat.set_status(False)
                    opstat.set_errorMsg("No fill_char parm defined")
                
                else :
                    
                    try :
                        if(fnid == PROCESS_CENTER_STR_FN) :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).center(width,fillchar))
                        elif(fnid == PROCESS_LJUST_STR_FN) :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).ljust(width,fillchar))
                        else :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).rjust(width,fillchar))    
                    except Exception as e:
                        opstat.store_exception("Exception running : " + str(fntoapply),e)
                        clock.stop()

    elif(fnid == PROCESS_REPLACE_STR_FN) :
        
        oldchar     =   fparms[1]
        newchar     =   fparms[2]
        
        if(len(oldchar) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No current_substring parm defined")
            
        else :
            try :
                new_col_array   =   df[coltoapply].map(lambda x: str(x).replace(oldchar,newchar))
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)
                clock.stop()

    elif(fnid == PROCESS_SLICE_STR_FN) :
        
        startind    =   fparms[1]
        stopind     =   fparms[2]
        
        if(len(startind) == 0) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("No slice_start_index parm defined")
            
        else :
            
            try :
                startind         =   int(startind)
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("slice_start_index parm is not numeric")
                
            if(opstat.get_status()) :
                
                if(len(stopind) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No slice_end_index parm defined")
                    
                else :
                    
                    try :
                        stopind         =   int(stopind)
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("slice_end_index parm is not numeric")
        
            if(opstat.get_status()) :
                try :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x)[startind:stopind])
                except Exception as e:
                    opstat.store_exception("Exception running : " + str(fntoapply),e)

            elif(fnid == PROCESS_TRIG_FN) :
        
                trigfunc    =   fparms[1]
        
                if(len(trigfunc) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No trigonometric_function parm defined")
        
                else :
            
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import get_trig_values_for_column
                    dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
                    new_col_array   =   get_trig_values_for_column(dftitle, coltoapply, trigfunc, opstat)
            
    elif( (fnid == PROCESS_RANDOM_INT_FN) or 
          (fnid == PROCESS_RANDOM_FLOAT_FN) or 
          (fnid == PROCESS_RANDOM_DATETIME_FN) ) :
        
        minvalue    =   fparms[1]
        maxvalue    =   fparms[2]
        
        if(len(minvalue) == 0) :
            opstat.set_status(False)
            if(fnid == PROCESS_RANDOM_INT_FN) :
                opstat.set_errorMsg("No minimum_integer_value parm defined")
            elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                opstat.set_errorMsg("No minimum_float_value parm defined")
            else :
                opstat.set_errorMsg("No minimum_datetime_value parm defined")
        
        else :
            
            try :
                if(fnid == PROCESS_RANDOM_INT_FN) :
                    minvalue    =   int(minvalue)    
                elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                    minvalue    =   float(minvalue)    
            except :
                opstat.set_status(False)
                if(fnid == PROCESS_RANDOM_INT_FN) :
                    opstat.set_errorMsg("minimum_integer_value parm is not numeric")
                elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                    opstat.set_errorMsg("minimum_float_value parm is not numeric")
                    
            if(opstat.get_status()) :
                
                if(len(maxvalue) == 0) :
                    opstat.set_status(False)
                    if(fnid == PROCESS_RANDOM_INT_FN) :
                        opstat.set_errorMsg("No maximum_integer_value parm defined")
                    elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                        opstat.set_errorMsg("No maximum_float_value parm defined")
                    else :
                        opstat.set_errorMsg("No maximum_datetime_value parm defined")
                        
                else :
                    try :
                        if(fnid == PROCESS_RANDOM_INT_FN) :
                            maxvalue    =   int(maxvalue)    
                        elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                            maxvalue    =   float(maxvalue)    
                    except :
                        opstat.set_status(False)
                        if(fnid == PROCESS_RANDOM_INT_FN) :
                            opstat.set_errorMsg("maximum_integer_value parm is not numeric")
                        elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                            opstat.set_errorMsg("maximum_float_value parm is not numeric")
            
            if(opstat.get_status()) :
            
                dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            
                if(fnid == PROCESS_RANDOM_INT_FN) :
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import random_int_range
                    new_col_array   =   random_int_range(dftitle, minvalue, maxvalue, opstat)
                elif(fnid == PROCESS_RANDOM_FLOAT_FN) :
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import random_float_range
                    new_col_array   =   random_float_range(dftitle, minvalue, maxvalue, opstat)
                else :
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import random_datetime_range
                    new_col_array   =   random_datetime_range(dftitle, minvalue, maxvalue, opstat)


    elif( (fnid == PROCESS_GEOCODE_DIST_CENTER_FN) or 
          (fnid == PROCESS_GEOCODE_DIST_POINT_FN) ):
        
        if(fnid == PROCESS_GEOCODE_DIST_CENTER_FN) :
            units    =   fparms[1]
        else :
            units    =   fparms[2]
        
        if(len(units) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No distance_units parm defined")
        else :
            if(fnid == PROCESS_GEOCODE_DIST_POINT_FN) :
                point    =   fparms[1]
                if(len(point) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No point parm defined")
                    
        if(opstat.get_status()) :
            
            dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            
            if(fnid == PROCESS_GEOCODE_DIST_CENTER_FN) :    
                from dfcleanser.sw_utilities.GenericFunctionsFunctions import get_dist_from_center_df_column
                new_col_array   =   get_dist_from_center_df_column(dftitle, coltoapply, units, opstat)
            else :    
                from dfcleanser.sw_utilities.GenericFunctionsFunctions import get_dist_from_point_df_column
                new_col_array   =   get_dist_from_point_df_column(dftitle, coltoapply, point, units, opstat)
    
    
    if(opstat.get_status()) :
        return(new_col_array)
    else :    
        return(None)




Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#F5F7A5"


def get_genfunc_list() :
    """
    * ------------------------------------------------------------------------
    * function : get the list of dfc reserved functions
    * 
    * parms :
    *
    * returns : 
    *    function call
    *
    * -------------------------------------------------------------------------
    """
    
    gtfuncs = genfns
    
    for i in range(len(genfns_with_parms)) :
        gtfuncs.append(genfns_with_parms[i])
        
    gtfuncs.sort()
    
    return(gtfuncs)


def add_column_to_df(df,colname,colList,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : add column with column list
    * 
    * parms :
    *   df      -   dataframe title
    *   colname -   column name
    *   collist -   column values
    *   opstat  -   op status var
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import is_existing_column
    if(is_existing_column(df,colname)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Column to Add : '" + colname + "' already exists")
        return()
    
    try :
        namesdict = {}
        namesdict.update({"newcolname" : colname})
        
        df   =   df.assign(newcolname=colList)
        df.rename(columns=namesdict,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Add New Column Error",e)
    
    return(df)


