"""
# DataCleansingControl
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

from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic


#import dfcleanser.common.cfg as cfg 
from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataCleansing_ID


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
from dfcleanser.sw_utilities.dfc_qt_model import fix_ipython
fix_ipython()




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    Data Cleansing methods                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


import dfcleanser.Qt.data_import.DataImportModel as DIM
from dfcleanser.common.common_utils import opStatus, get_parms_for_input


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing display info functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_uniques_for_cleanse_column(dftitle,colname) :
    """
    * -------------------------------------------------------
    * function : display unique values for a column
    * 
    * parms :
    *   parms[0]           -   col name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[display_uniques_for_cleanse_column]",dftitle,colname))

    from dfcleanser.common.common_utils import run_jscript
    script  =   "display_Column_Uniques('" + dftitle + "','" + colname + "');"

    run_jscript(script)

    return


def display_outliers_for_cleanse_column(dftitle,colname) :
    """
    * --------------------------------------------------------
    * function : display outliers for a column
    * 
    * parms :
    *   parms[0]           -   col name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[display_outliers_for_cleanse_column]",colname))

    from dfcleanser.common.common_utils import run_jscript
    script  =   "display_Column_Outliers('" + dftitle + "','" + colname + "');"

    run_jscript(script)

    return


def change_column_values(changeparms) :
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[change_column_values]",changeparms))

    dftitle     =   changeparms[0]  
    colname     =   changeparms[1]
    oldvalue    =   changeparms[2]
    newvalue    =   changeparms[3]

    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    from dfcleanser.common.common_utils import is_numeric_col, is_int_col, is_bool_col, is_float_col

    if(is_numeric_col(df,colname)) :

        if(is_int_col(df,colname)) :

            try :
                foldvalue   =   int(oldvalue)
            except :

                title       =   "dfcleanser exception : [change_column_values]"       
                status_msg  =   "Current Value is not a valid int "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                return()
            
            try :
                fnewvalue   =   int(newvalue)
            except :

                title       =   "dfcleanser exception : [change_column_values]"       
                status_msg  =   "New Value is not a valid int "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                return()
            
            if(foldvalue == fnewvalue) :

                title       =   "dfcleanser exception : [change_column_values]"        
                status_msg  =   "old value and new value are the same"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

           
        elif(is_float_col(df,colname)) :

            try :
                foldvalue   =   float(oldvalue)
            except :

                title       =   "dfcleanser exception : [change_column_values]"       
                status_msg  =   "Current Value is not a valid float "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                return()
            
            try :
                fnewvalue   =   float(newvalue)
            except :

                title       =   "dfcleanser exception : [change_column_values]"       
                status_msg  =   "New Value is not a valid float "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                return()
            
            if(foldvalue == fnewvalue) :

                title       =   "dfcleanser exception : [change_column_values]"        
                status_msg  =   "old value and new value are the same"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return()

    else :

        foldvalue   =   oldvalue
        fnewvalue   =   newvalue

        if(foldvalue == fnewvalue) :

            title       =   "dfcleanser exception : [change_column_values]"        
            status_msg  =   "old value and new value are the same"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
    
    try :
            
        criteria                    =   (df[colname] == foldvalue)
        df.loc[criteria,colname]    =   fnewvalue

        from dfcleanser.common.cfg import set_dfc_dataframe_df
        set_dfc_dataframe_df(dftitle,df)
        
        title       =   "dfcleanser status : [change_column_values]"       
        status_msg  =   "value changed successfully "
        from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
        display_status_msg(title,status_msg)

        
    except Exception as e:
                
        title       =   "dfcleanser exception : [change_column_values]"       
        status_msg  =   "change value error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)
    
    return()


def drop_column(dftitle,colname) :
    """
    * --------------------------------------------------------
    * function : drop a specific col
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[drop_column] : ",dftitle,colname))
     
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    droplist    =   []
    droplist.append(colname)
    
    opstat = opStatus()
    
    try :
        
        df.drop(droplist,axis=1,inplace=True)
        from dfcleanser.common.common_utils import reindex_df
        reindex_df(df) 
        
        set_dfc_dataframe_df(dftitle,df)
        
    except Exception as e:

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[drop_column] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)
        
    return(opstat)

def drop_value_rows(dftitle,colname,value) :
    """
    * --------------------------------------------------------
    * function : drop rows for column value
    * 
    * parms :
    *   value           -   column value to match
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
   
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[drop_value_rows] : ",dftitle,colname,value))

    opstat      =   opStatus()
    
    import pandas as pd
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)
    
    if(value == "nan") :

        df.dropna(subset=[colname],inplace=True)
        from dfcleanser.common.common_utils import reindex_df
        reindex_df(df) 
        
    else :
        
        droplist    =   []
        
        dfcoldata   =   df[colname].tolist()
 
        from dfcleanser.common.common_utils import (is_datetime64_col, is_numeric_col, is_timedelta64_col ) 

        if(is_numeric_col(df,colname)) :
            dropvalue   =   pd.to_numeric(value)
        elif(is_datetime64_col(df,colname,anydatetime64=True)) :
            dropvalue   =   pd.to_datetime(value)
        elif(is_timedelta64_col(df,colname,anydatetime64=True)) :
            dropvalue   =   pd.to_timedelta(value)
        else :
            dropvalue   =   value
    
        for i in range(len(dfcoldata)) :
            
            if(dfcoldata[i] == dropvalue) :
                droplist.append(df.index.get_loc(df.index[i]))

        if(len(droplist) > 0) :
        
            try :
                
                df.drop(droplist,axis=0,inplace=True)
                
                from dfcleanser.common.common_utils import reindex_df
                reindex_df(df) 

                set_dfc_dataframe_df(dftitle,df)
        
            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[drop_value_rows] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
                

    return(opstat)


def round_column_data(dftitle,colname,numdigits) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[round_column_data] : ",dftitle,colname,numdigits))
    
    opstat      =   opStatus()
    
    import pandas as pd
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    try :     

        accuracy    =   int(numdigits)
        rounds      =   {colname: accuracy}

        df = df.round(rounds)
        set_dfc_dataframe_df(dftitle,df)  

    except Exception as e:

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[drop_value_rows] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)


def drop_nan_rows(dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[drop_nan_rows] : ",dftitle,colname))

    opstat      =   opStatus()
    
    import pandas as pd
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    try :
            
        df = df[df[colname].notna()]
        set_dfc_dataframe_df(dftitle,df)

    except Exception as e:

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[Drop Nan Rows] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)


def fill_nan_values(dftitle,colname,fillvalue,fillnamethod) :
        
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[fill_nan_values] : ",dftitle,colname,fillvalue,fillnamethod))

    opstat      =   opStatus()
    
    import pandas as pd
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    try :
                

        if(not (fillnamethod is None)) :

            if(len(fillnamethod) == 0) :
                fillnavalue   =   fillvalue
            elif(fillnamethod == "None - use fillna_value") :
                fillnavalue   =   fillvalue    
            elif(fillnamethod == "mean") :
                fillnavalue     =   df[colname].mean()    
            elif(fillnamethod == "median") :
                fillnavalue     =   df[colname].median()    
            elif(fillnamethod == "min") :
                fillnavalue     =   df[colname].min()    
            elif(fillnamethod == "max") :
                fillnavalue     =   df[colname].max()
            else :    
                fillnavalue     =   fillvalue
       
        if(not(fillnavalue is None)) :

            if(len(fillnavalue) > 0) :      
                    
                from dfcleanser.common.common_utils import is_numeric_col, get_numeric_from_string
                if(is_numeric_col(df,colname)) :
                    nan_value   =   get_numeric_from_string(fillnavalue)
                else :
                    nan_value   =   fillnavalue

                if(not (nan_value == None)) :

                    try :

                        df[colname].fillna(value=nan_value,inplace=True)
                        set_dfc_dataframe_df(dftitle,df)

                    except Exception as e:

                        opstat.set_status(False)
            
                        title       =   "dfcleanser exception"       
                        status_msg  =   "[Drop Nan Rows] error "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)
                    
                else :

                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid Nan value")

            else :

                opstat.set_status(False)
                opstat.set_errorMsg("Invalid Nan value")

        else :

            opstat.set_status(False)
            opstat.set_errorMsg("Invalid Nan value")

    except Exception as e:

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[Drop Nan Rows] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)



whitespace_chars                =   ["\\t","\\n","\\f","\\r","\\b","\\v"]
whitespace_chars_text           =   ["&nbsp;Horizontal Tab","&nbsp;Linefeed","&nbsp;Formfeed","&nbsp;Cariage Return","&nbsp;Backspace","&nbsp;Vertical Tab"]
whitespace_chars_ids            =   ["HTab","Lfeed","Ffeed","CReturn","Bspace","VTab"]


def remove_whitespace(dftitle,colname,wschars,leadflag) :
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[remove_whitespace] : ",dftitle,colname,wschars,leadflag))
    
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    whitespacechars =   wschars.split(",")
    
    whitespaceopts  =   []
    
    if("All" in whitespacechars) :
        whitespaceopts  =   whitespace_chars  
    else :
        
        for i in range(len(whitespace_chars_text)) :
            if(whitespace_chars_text[i] in whitespacechars) :
                whitespaceopts.append(whitespace_chars[i])
    
    import pandas as pd
    uniquesIndices  =    pd.DataFrame([[k,v.values]
                                       for k,v in df.groupby(colname).groups.items()], 
                                      columns=[colname,'indices'])
    
    try :
    
        for i in range(len(uniquesIndices)) :
            
            unique_val          =   uniquesIndices.iloc[i,uniquesIndices.columns.get_loc(colname)]
                    
            uniques_indices     =   uniquesIndices.iloc[i,uniquesIndices.columns.get_loc("indices")]
            
            for j in range(len(whitespaceopts)) :
                
                if(unique_val.find(whitespaceopts[j]) > -1) :
                    
                    if(leadflag == "All") :
                        df.iloc[uniques_indices,df.columns.get_loc(colname)]    =   unique_val.replace(whitespaceopts[i],"")
                    elif(leadflag == "Leading and Trailing") :
                        new_unique_val                                          =   unique_val.lstrip(whitespaceopts[i])
                        new_unique_val                                          =   new_unique_val.rstrip(whitespaceopts[i])
                        df.iloc[uniques_indices,df.columns.get_loc(colname)]    =   new_unique_val
                    elif(leadflag == "Leading Only") :
                        df.iloc[uniques_indices,df.columns.get_loc(colname)]    =   unique_val.lstrip(whitespaceopts[i])
                    else :
                        df.iloc[uniques_indices,df.columns.get_loc(colname)]    =   unique_val.rstrip(whitespaceopts[i])

        set_dfc_dataframe_df(dftitle,df)
                        
    except Exception as e :
        opstat.store_exception("Unable to parse whitespace chars for column '" + str(colname) + "'" + " at row " + str(i),e)
        
                
    return(opstat)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Data Cleansing Categorical methods                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def get_category_type_parms(df,colname,parms) :
    """
    * --------------------------------------------------------
    * function : get and convert cat parms
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    goodParms   =   True

    import pandas as pd
    CI                  =   pd.CategoricalIndex(df[colname])
    cats                =   CI.categories.tolist()
    sample_category     =   cats[0]

    get_category_type_parms =    []

    for i in range(len(parms)) :

        if(type(sample_category) is int) :
            get_category_type_parms.append(int(parms[i]))
        elif(type(sample_category) is float) :
            get_category_type_parms.append(float(parms[i]))
        elif(type(sample_category) is str) :
            get_category_type_parms.append(str(parms[i]))

        else :
            get_category_type_parms.append(parms[i])

    if(goodParms) :
        return(get_category_type_parms)
    else :
        return(None)


def rename_category(dftitle,colname,oldcat,newcat) :
    """
    * -------------------------------------------------------- 
    * function : rename a category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
     
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[remove_whitespace] : ",dftitle,colname,oldcat,newcat))
   
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    if( (len(oldcat)==0) or (len(newcat)==0) or (oldcat == newcat) ) :
                
        title       =   "dfcleanser error"       
        status_msg  =   "Category Inputs are invalid"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

    else :

        fromcategory        =   oldcat
        tocategory          =   newcat
    
        change_cat_dict     =   {fromcategory:tocategory}
    
        try :
            df[colname] = df[colname].cat.rename_categories(change_cat_dict)
        except Exception as e:

            opstat.set_status(False)
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[rename_category] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

    return(opstat)       

    
def add_category(dftitle,colname,newcat) :
    """
    * ---------------------------------------------------------
    * function : add a category
    * 
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[add_category] : ",dftitle,colname,newcat))
   
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    if( len(newcat) == 0) :
        
        title       =   "dfcleanser error"       
        status_msg  =   "Category Inputs are invalid"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

 
    else :

        newcategory        =   newcat
        new_cat_list        =   [newcategory]
        
        corderlist          =   df[colname].cat.categories.tolist() 
        
        for i in range(len(corderlist)) :
            
            if(newcategory == corderlist[i]) :

                title       =   "dfcleanser error"       
                status_msg  =   "Category Already defined"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)
               
                opstat.set_status(False)
                
        if(opstat.get_status()) :
     
            try :
        
                df[colname]     =   df[colname].cat.add_categories(new_cat_list)#,inplace=True)
        
            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[add_category] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

    return(opstat)


def remove_category(dftitle,colname,delcat) :
    """
    * --------------------------------------------------------
    * function : remove a category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[remove_category] : ",dftitle,colname,delcat))
    
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    if( len(delcat) == 0) :
        
        title       =   "dfcleanser error"       
        status_msg  =   "Category Inputs are invalid"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :
    
        removecategories        =   delcat  

        rem_cat_list    =   [] 
        corderlist      =   df[colname].cat.categories.tolist() 
        
        for i in range(len(removecategories)) :
    
            remcategory =   removecategories[i]
            
            if(not (remcategory in corderlist)) :

                title       =   "dfcleanser error"       
                status_msg  =   "Category not Removed : Category : '" + str(remcategory) + "' not in categories"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                opstat.set_status(False)
                
            else :

                rem_cat_list.append(remcategory)
    
        if(opstat.get_status()) :
            
            try :
        
                df[colname]     =   df[colname].cat.remove_categories(rem_cat_list)#,inplace=True)
        
            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[remove_category] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

    return(opstat)

    
def remove_unused_categories(dftitle,colname) :
    """
    * --------------------------------------------------------
    * function : remove unused categories
    * 
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[remove_unused_categories] : ",dftitle,colname))

    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    try :
        
        df[colname]     =   df[colname].cat.remove_unused_categories()#inplace=True)
        
    except Exception as e:

        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[remove_unused_categories] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)
 

def reorder_category(dftitle,colname,catsorder) :
    """
    * --------------------------------------------------------
    * function : reorder category
    * 
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[reorder_category] : ",dftitle,colname,catsorder))


    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)
    
    orderlist   =   catsorder
    corderlist  =   df[colname].cat.categories.tolist() 

    catparms    =   get_category_type_parms(df,colname,orderlist) 

    if(catparms is None) :

        opstat.set_status(False)
        opstat.set_errorMsg("Categories not Reordered : Invalid categories " + str(orderlist))
        
    else :

        orderflag   =   True
    
        try :
            df[colname]     =   df[colname].cat.reorder_categories(catparms,ordered=orderflag)#,inplace=True)
        except Exception as e:
        
            opstat.set_status(False)
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[reorder_category] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

    return(opstat)


def toggle_category_order(dftitle,colname,ctaorder) :
    """
    * ---------------------------------------------------------
    * function : toggle category order attribute
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
     
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[toggle_category_order] : ",dftitle,colname,ctaorder))
   
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    orderlist   =   ctaorder

    if(orderlist is None) :
        orderlist  =   df[colname].cat.categories.tolist() 

    import pandas as pd
        
    CI          =   pd.CategoricalIndex(df[colname])
    orderflag   =   CI.ordered

    try :
        df[colname]     =   df[colname].cat.reorder_categories(orderlist,ordered=orderflag)#,inplace=True)
    except Exception as e:
        
        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[toggle_category_order] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)

def sort_categories(dftitle,colname) :
    """
    * --------------------------------------------------------
    * function : sort category order attribute
    * 
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[sort_categories] : ",dftitle,colname))
   
    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)
    
    try :
        df.sort_values(colname,inplace=True)
        
    except Exception as e:
        
        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[sort_categories] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)

def drop_duplicate_rows(parms,display=True):
    """
    * ---------------------------------------------------
    * function : drop df duplicate rows
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * ---------------------------------------------------
    """
    
    opstat = opStatus()
    
    colnames    =   parms[0]
    
    fparms      =   get_parms_for_input(parms[1],dtrw.df_drop_dups_transform_input_idList)
    
    if(len(colnames) == 0) :
        colnames    =   None
        
    if(fparms[0] == "Drop") :
        drop = True
    else :
        drop = False
    
    keep        =   fparms[1]
    if(keep == "False") :
        keep    =   False
        
    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
            
    if(not (colnames is None)) :
        if(not drop) :
            fcolnames   =   []  
            colslist    =   df.columns.tolist()
            
            for i in range(len(colslist)) :
                if(not (colslist[i] in colnames)) :
                    fcolnames.append(colslist[i]) 
                    
            colnames    =   fcolnames
                
    if(opstat.get_status()) :
        
        try : 
            
            df.drop_duplicates(colnames,keep=keep,inplace=True)
                
        except Exception as e: 
            opstat.store_exception("Unable to drop duplicate rows : " + colnames,e)

    return(opstat)
 
def apply_criteria_to_df(df,criteria,opstat) :
    """
    * --------------------------------------------------------
    * function : sort category order attribute
    * 
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingControl",print_to_string("[apply_criteria_to_df] : \n",criteria))
   
    try :

        exec(criteria)
        
    except Exception as e:
        
        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[apply_criteria_to_df] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return()

































