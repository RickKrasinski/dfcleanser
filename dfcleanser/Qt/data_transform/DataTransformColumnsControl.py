"""
# DataTransformColumnsControl
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

DEBUG_TRABSFORM_COLUMN           =   True


DEBUG_DATA_IMPORT_HISTORIES     =   False
DEBUG_DATA_IMPORT_FILE_TYPE     =   False
DEBUG_DATA_IMPORT_DETAILS       =   False
DEBUG_DATA_IMPORT_FORMS         =   True

DEBUG_DATA_IMPORT_CSV           =   False
DEBUG_DATA_IMPORT_FWF           =   False
DEBUG_DATA_IMPORT_EXCEL         =   True
DEBUG_DATA_IMPORT_JSON          =   True
DEBUG_DATA_IMPORT_HTML          =   True
DEBUG_DATA_IMPORT_SQLTABLE      =   True
DEBUG_DATA_IMPORT_SQLQUERY      =   True
DEBUG_DATA_IMPORT_CUSTOM        =   True


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            general Data Transform Housekeeping                -#
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


import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM
from dfcleanser.common.common_utils import opStatus


def process_rename_column(dftitle,oldcolname,newcolname) :
    """
    * -------------------------------------------------------
    * function : rename column transform option
    * 
    * parms :
    *   dftitle   -   dftitle
    *   colname   -   col name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_rename_column]",dftitle,oldcolname,newcolname)
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [process_rename_column]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

                    
        from dfcleanser.common.common_utils import  is_column_in_df           
        if(not (is_column_in_df(df,oldcolname))) :

            title       =   "dfcleanser error : [process_rename_column]"        
            status_msg  =   "invalid current column name"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

        else :

            namesdict = {}
            namesdict.update({oldcolname:newcolname})
    
            try :
        
                df.rename(columns=namesdict,inplace=True)

                title       =   "dfcleanser status : [process_rename_column]"        
                status_msg  =   "column renamed successfully"
                from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                display_status_msg(title,status_msg)

                from dfcleanser.common.cfg import set_dfc_dataframe_df
                set_dfc_dataframe_df(dftitle,df)

       
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[process_rename_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)
    
    return(opstat)  


def process_drop_column(dftitle,colname) :
    """
    * --------------------------------------------------------
    * function : drop column transform option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_drop_column]",dftitle,colname)
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [process_drop_column]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        from dfcleanser.common.common_utils import  is_column_in_df           
        if(not (is_column_in_df(df,colname))) :

            title       =   "dfcleanser error : [process_drop_column]"        
            status_msg  =   "invalid column name"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

        else :
    
            try :

                from PyQt5.QtWidgets import QMessageBox
                dlg = QMessageBox()
                dlg.setTextFormat(Qt.RichText)
                dlg.setWindowTitle("Drop Column")
                dlg.setText("Drop Column " + colname)
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                button = dlg.exec()

                if(button == QMessageBox.Yes) :
                
                    df.drop([colname],inplace=True,axis=1)
                    df.reset_index(drop=True,inplace=True)

                    from dfcleanser.common.cfg import set_dfc_dataframe_df
                    set_dfc_dataframe_df(dftitle,df)
                    
                    title       =   "dfcleanser status : [process_drop_column]"        
                    status_msg  =   "column " + colname + " dropped successfully"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                    display_status_msg(title,status_msg)
            
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[process_drop_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

    return(opstat)


def process_reorder_columns(dftitle,newcolorder) :
    """
    * --------------------------------------------------------
    * function : reorder column transform option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =    opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_reorder_columns]",dftitle,"\n",newcolorder)
     
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [process_reorder_columns]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        try : 
            
            df  =   df[newcolorder]  

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)

            title       =   "dfcleanser status : [process_reorder_columns]"        
            status_msg  =   "columns reodered successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)
            
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_reorder_columns] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)


def process_save_column(dftitle,colnames,fname,ftype,withIndex=False) :
    """
    * ---------------------------------------------------------
    * function : save column transform option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_save_column]",dftitle,colnames,fname,ftype,withIndex)

    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [process_save_column]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        for i in range(len(colnames)) :

            from dfcleanser.common.common_utils import  is_column_in_df           
            if(not (is_column_in_df(df,colnames[i]))) :

                title       =   "dfcleanser error : [process_save_columns]"        
                status_msg  =   "invalid column name " + colnames[i] + " is not in df"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                opstat.set_status(False)
                break
            
        if(opstat.get_status()) :
            
            if(len(fname) == 0) :

                title       =   "dfcleanser error : [process_save_columns]"        
                status_msg  =   "No file name to save columns to is defined "
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                opstat.set_status(False)

    
    if(opstat.get_status())  :
    
        try :
            
            if(ftype == "json") :
                    
                cols            =   list(df.columns)
                cols_to_drop    =   []
                    
                for i in range(len(cols)) :
                    if(not (cols[i] in colnames) ) :
                        cols_to_drop.append(cols[i])
                            
                temp_df     =   df.drop(cols_to_drop,axis=1)
                temp_df.reset_index(drop=True,inplace=True)
                fname   =   fname + ".json"
                temp_df.to_json(fname)
                    
            elif(ftype == "excel") :
                    
                fname   =   fname + ".xls"
                df.to_excel(fname,columns=colnames,header=True,index=withIndex)
                    
            else :
                    
                df.to_csv(fname,columns=colnames,header=True,index=withIndex)
                        
        except Exception as e:
                
            title       =   "dfcleanser exception"       
            status_msg  =   "[process_save_columns] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
                
    return(opstat)


def process_copy_column(dftitle,copyfromcol,copytocol) :
    """
    * -------------------------------------------------------
    * function : copy column transform option
    * 
    *
    * returns : 
    *  N/A
    * -------------------------------------------------------
    """
 
    opstat  =   opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_copy_column]",dftitle,copyfromcol,copytocol)

    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [process_save_column]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :
    
        try : 
        
            df[copytocol] = df[copyfromcol]

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
        
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_copy_columns] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
        
    return(opstat)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Transform apply fn to column methods              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def process_apply_user_fn_to_column(user_code) :
    """
    * ---------------------------------------------------
    * function : apply fn to column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------
    """
    
    opstat  =   opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_apply_user_fn_to_column]process_apply_user_fn_to_column\n",user_code)
    
    fn_code         =   user_code
            
    if(len(user_code) > 0) :
                
        try :
                    
            exec(fn_code)

            
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_apply_user_fn_to_column] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    else :

        title       =   "dfcleanser exception"       
        status_msg  =   "[process_apply_user_fn_to_column] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        #from dfcleanser.common.cfg import set_dfc_dataframe_df
        #set_dfc_dataframe_df(dftitle,df)
        #TBD


        opstat.set_status(False)

    return(opstat)        


def process_apply_dfc_fn_to_column(dftitle,colname,dfc_fn,fnparms,add_column_name=None) :
    """
    * ------------------------------------
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * ------------------------------------
    """
    
    import pandas as pd
    
    opstat  =   opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_apply_dfc_fn_to_column]",dftitle,colname,dfc_fn,fnparms,add_column_name)

    if( (dftitle is None) or (len(dftitle) == 0) ) :

        opstat.set_status(False)
        opstat.set_errorMsg("No dftitle defined")

    else :

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(dftitle)
    
        if(len(colname) == 0) :

            opstat.set_status(False)
            opstat.set_errorMsg("No column to apply fn to defined")

        else :

            from dfcleanser.sw_utilities.GenericFunctionsModel import genfns, genfns_with_parms
            if( (not(dfc_fn in genfns)) and (not(dfc_fn in genfns_with_parms))) :

                opstat.set_status(False)
                opstat.set_errorMsg("invalid dfc fn defined")

            else :

                if( dfc_fn in genfns_with_parms)  :

                    if( (fnparms is None) or (len(fnparms) == 0) ) :

                        opstat.set_status(False)
                        opstat.set_errorMsg("invalid fn parms for dfc fn defined")

                    else :

                        try :

                            import json
                            parms_dict = json.loads(fnparms)
                        
                        except Exception as e:

                            title       =   "dfcleanser exception"       
                            status_msg  =   "[process_apply_dfc_fn_to_column] error "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                            display_exception(title,status_msg,e)

                            opstat.set_status(False)

                else :

                    parms_dict  =   None

    if(opstat.get_status()) :

        if(parms_dict is None) :
            new_col_values  =   get_column_from_dfc_apply_fn(df,dftitle,dfc_fn,colname,opstat)

        else :

            new_col_values  =   get_column_from_dfc_with_parms_apply_fn(df,dfc_fn,colname,parms_dict,opstat)

        if(opstat.get_status()) :

            try :

                if(add_column_name is None) :

                    df[colname]=pd.Series(new_col_values)

                else :

                    from dfcloeanser.sw_utilities.GenericFunctionsModel import add_column_to_df
                    df  =   add_column_to_df(df,add_column_name,new_col_values,opstat)

                if(opstat.get_status()):

                    from dfcleanser.common.cfg import set_dfc_dataframe_df
                    set_dfc_dataframe_df(dftitle,df)

            except Exception as e:
                opstat.store_exception("Apply fn to Column Error : " + coltoapply + "\n   ",e)

    if(not (opstat.get_status())) :

        if(opstat.get_exception()is None) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_apply_dfc_fn_to_column] error \n" + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error
            display_error(title,status_msg)

        else:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_apply_dfc_fn_to_column] error \n" + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,opstat.get_exception())
        
    return(df)


# -----------------------------------------------------------------#
# -           Transform get column values for apply fn            -#
# -----------------------------------------------------------------#

def get_column_from_dfc_apply_fn(df,dftitle,fntoapply,coltoapply,opstat) :
    """
    * -------------------------------------------------------
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

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[get_column_from_dfc_apply_fn]",dftitle,fntoapply,coltoapply)
    
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
            new_col_array   =   normalize_df_column(dftitle, coltoapply, 0, opstat)
        
        elif(fntoapply == "normalize_min_max()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import normalize_df_column
            new_col_array   =   normalize_df_column(dftitle, coltoapply, 1, opstat)
            
        elif(fntoapply == "uppercase_str()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import upper_lower_case_df_column, UPPER_CASE
            new_col_array   =   upper_lower_case_df_column(dftitle, coltoapply, UPPER_CASE, opstat)
                
        elif(fntoapply == "lowercase_str()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import upper_lower_case_df_column, LOWER_CASE
            new_col_array   =   upper_lower_case_df_column(dftitle, coltoapply, LOWER_CASE, opstat)
            
        elif(fntoapply == "todegrees()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import convert_df_column_to_degrees_or_radians
            new_col_array   =   convert_df_column_to_degrees_or_radians(dftitle, coltoapply, True, opstat)
            
        elif(fntoapply == "toradians()")    : 
                
            from dfcleanser.sw_utilities.GenericFunctionsFunctions import convert_df_column_to_degrees_or_radians
            new_col_array   =   convert_df_column_to_degrees_or_radians(dftitle, coltoapply, False, opstat)
            
    except Exception as e:
        opstat.store_exception("Apply fn to Column Error : " + coltoapply + " " + fntoapply,e)

    if(opstat.get_status()) :
        return(new_col_array)
    else :
        return(None)

def get_column_from_dfc_with_parms_apply_fn(df,fntoapply,coltoapply,parms_dict,opstat) :
    """
    * -----------------------------------------------------
    * function : process add column from a dfc function
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * -----------------------------------------------------
    """

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[get_column_from_dfc_with_parms_apply_fn]",fntoapply,coltoapply,parms_dict)
            
    if(fntoapply == "round_float(ndigits)") :
        
        ndigits     =   parms_dict.get("ndigits")
        
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

            
    elif( (fntoapply ==  "strip(stripchar)") or 
          (fntoapply ==  "lstrip(stripchar)") or 
          (fntoapply ==  "rstrip(stripchar)") ) :
        
        stripchar     =   parms_dict.get("stripchar")
        
        if(len(stripchar) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No character_to_strip parm defined")
        else :
            
            try :
                if(fntoapply ==  "strip(stripchar)") :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).strip(stripchar))
                elif(fntoapply ==  "lstrip(stripchar)") :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).lstrip(stripchar))
                else :
                    new_col_array   =   df[coltoapply].map(lambda x: str(x).rstrip(stripchar))
                    
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)

    
    elif( (fntoapply == "center(width,fillchar)") or 
          (fntoapply == "left_justify(width,fillchar)") or 
          (fntoapply == "right_justify(width,fillchar)") ) :
        
        width     =   parms_dict.get("width")
                
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
            
                fillchar  =   parms_dict.get("fillchar")
                if(len(fillchar) == 0) :
                    
                    opstat.set_status(False)
                    opstat.set_errorMsg("No fill_char parm defined")
                
                else :
                    
                    try :
                        if(fntoapply == "center(width,fillchar)") :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).center(width,fillchar))
                        elif(fntoapply == "left_justify(width,fillchar)") :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).ljust(width,fillchar))
                        else :
                            new_col_array   =   df[coltoapply].map(lambda x: str(x).rjust(width,fillchar))    
                    except Exception as e:
                        opstat.store_exception("Exception running : " + str(fntoapply),e)

    
    elif(fntoapply == "replace(oldchar,newchar)") :
        
        oldchar     =   parms_dict.get("oldchar")
        newchar     =   parms_dict.get("newchar")
        
        if( len(oldchar) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No old char parm defined")
            
        else :
            try :
                new_col_array   =   df[coltoapply].map(lambda x: str(x).replace(oldchar,newchar))
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)

    elif(fntoapply == "slice(startind,stopind)") :
        
        startind    =   parms_dict.get("startind")
        stopind     =   parms_dict.get("stopind")
        
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

    elif(fntoapply == "get_trig_value(trigfn)") :
        
        trigfunc    =   parms_dict.get("trigfunc")
        
        if(len(trigfunc) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No trigonometric_function parm defined")
        
        else :
            
            new_col_array   =   get_trig_values_for_column(df, coltoapply, trigfunc, opstat)
            
    elif( (fntoapply == "random_int_range(minint,maxint)") or 
          (fntoapply == "random_float_range(minfloat,maxfloat)") or 
          (fntoapply == "random_datetime_range(mindatetime,maxdatetime)") ) :
        
        if( (fntoapply == "random_int_range(minint,maxint)")) :
            
            minvalue    =   parms_dict.get("minint")
            maxvalue    =   parms_dict.get("maxint")

            try :
                minvalue    =   int(minvalue)
                maxvalue    =   int(maxvalue)
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)

        elif(fntoapply == "random_float_range(minfloat,maxfloat)") :
          
            minvalue    =   parms_dict.get("minfloat")
            maxvalue    =   parms_dict.get("maxfloat")

            try :
                minvalue    =   float(minvalue)
                maxvalue    =   random_float_range(maxvalue)
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)

        else :
          
            minvalue    =   parms_dict.get("mindatetime")
            maxvalue    =   parms_dict.get("maxdatetime")
       
            try :
                tminvalue    =   int(minvalue)
                tmaxvalue    =   int(maxvalue)
            except Exception as e:
                opstat.store_exception("Exception running : " + str(fntoapply),e)

            
            if(opstat.get_status()) :
            
                dftitle         =   cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID)
            
                if(fntoapply == "random_int_range(minint,maxint)") :
                    new_col_array   =   random_int_range(df, minvalue, maxvalue, opstat)
                elif("random_float_range(minfloat,maxfloat)") :
                    new_col_array   =   random_float_range(df, minvalue, maxvalue, opstat)
                else :
                    new_col_array   =   random_datetime_range(df, minvalue, maxvalue, opstat)


    elif( (fntoapply == "get_dist_from_center_pt(units)") or 
          (fntoapply == "get_dist_from_point(units,pt)") ):
        
            units    =   parms_dict.get("units")
        
            if(len(units) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No distance_units parm defined")
            else :
                if(fntoapply == "get_dist_from_point(units,pt)") :
                    point    =   parms_dict.get("pts")
                    if(len(point) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No point parm defined")
                    
            if(opstat.get_status()) :
            
                if(fntoapply == "get_dist_from_center_pt(units)") :    
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import get_dist_from_center_df_column
                    new_col_array   =   get_dist_from_center_df_column(df, coltoapply, units, opstat)
                else :    
                    from dfcleanser.sw_utilities.GenericFunctionsFunctions import get_dist_from_point_df_column
                    new_col_array   =   get_dist_from_point_df_column(df, coltoapply, point, units, opstat)
    
    if(opstat.get_status()) :
        return(new_col_array)
    else :    
        return(None)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            Transform apply fn to column methods end           -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#






# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -        Mapping, Dummies and Category control functions        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                  Transform Dummies column                     -#
# -----------------------------------------------------------------#

def make_col_categorical_from_dummies(dftitle, colname, removeCol)  : 
    """
    * -----------------------------------------------------------
    * function : make a column categorical in place using dummies
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   removeCol       -   remove the original column
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 

    opstat = opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[make_col_categorical_from_dummies]",dftitle, colname, removeCol)
 
    import pandas as pd

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [make_col_categorical]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :
   
        y = df[[colname]]
    
        try :
        
            dummies_df = pd.get_dummies(y)

            if(DEBUG_TRABSFORM_COLUMN) :
                print("[make_col_categorical_from_dummies] got caty : ")
                print("[make_col_categorical_from_dummies] dummies : ",len(dummies_df.columns))

        except Exception as e:
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[make_col_categorical_from_dummies] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

        if( opstat.get_status() ): 

            if( removeCol) :

                try :
            
                    df.drop(colname, axis = 1, inplace = True)
                    df.reset_index(drop=True,inplace=True) 
            
                except Exception as e: 

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[make_col_categorical_from_dummies remove col] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)
    
            if( opstat.get_status()): 

                try :

                    if(DEBUG_TRABSFORM_COLUMN) :
                        print("[make_col_categorical_from_dummies] dummies : ",len(df.columns))
                        print("[make_col_categorical_from_dummies] dummies : ",df.columns.tolist())

                    df = pd.concat([df, dummies_df], axis=1)

                    from dfcleanser.common.cfg import set_dfc_dataframe_df    
                    set_dfc_dataframe_df(dftitle,df)                             

                    if(DEBUG_TRABSFORM_COLUMN) :
                        print("[make_col_categorical_from_dummies] dummies : ",len(df.columns))
                        print("[make_col_categorical_from_dummies] dummies : ",df.columns.tolist())
            
                    title       =   "dfcleanser status : [process_dummies_column]"        
                    status_msg  =   "column dummies created successfully"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                    display_status_msg(title,status_msg)

                    from dfcleanser.common.cfg import df_Column_Changed_signal
                    df_Column_Changed_signal.issue_notice(dftitle)

                except Exception as e:

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[make_col_categorical_from_dummies concat] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)

    return(opstat)


# -----------------------------------------------------------------#
# -              Transform Map column from code                   -#
# -----------------------------------------------------------------#

def process_transform_column_map(mapcode)  :   
    """
    * ---------------------------------------------------------- 
    * function : make a column categorical in place using map
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
   
    opstat = opStatus()


    try :

        exec(mapcode)

        
    except Exception as e:
        
        opstat.set_status(False)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[apply_criteria_to_df] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    return(opstat)


# -----------------------------------------------------------------#
# -             Transform make column categorical                 -#
# -----------------------------------------------------------------#
def process_category_convert_transform(dftitle,colname,order_flag,unique_option,uniques_list) :
    """
    * -------------------------------------------------------------------------- 
    * function : categorical transform
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat          =   opStatus()

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_category_convert_transform]",dftitle,colname,order_flag,unique_option)
        print("[process_category_convert_transform] \n    ",uniques_list)

    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(df[colname].isnull().sum() > 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[To convert column to category all Nans must be removed "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)
        
        opstat.set_status(False)
        return(opstat)
    
    else :

        if(order_flag == "False") :
            ordercat    =   False
        else :
            ordercat    =   True

        if(not(unique_option == "use all uniques")) :

            try :

                import json
                uniques     =   json.loads(uniques_list)

            except Exception as e: 

                title       =   "dfcleanser exception"       
                status_msg  =   "[process_category_convert_transform] \n uniques_list is invalid "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

            if(opstat.get_status()) :

                if(not(unique_option == "define exclude list from 'unique_values' to subtract from all")) : 

                    uniques_to_convert     =   df[colname].unique().tolist()
                    uniques_to_convert.sort()

                    for i in range(len(uniques)) :
                        uniques_to_convert.remove(uniques[i])

                else :

                    uniques_to_convert  =   uniques
                             
            else :

                uniques_to_convert    =   df[colname].unique().tolist()

        else :

            uniques_to_convert    =   df[colname].unique().tolist()            

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_category_convert_transform] uniques_to_convert : \n    ",uniques_to_convert)
            
    if(opstat.get_status()) :
    
        try :

            import pandas as pd
            
            cattype     =   pd.CategoricalDtype(categories = uniques_to_convert,ordered=ordercat)
            df[colname] =   df[colname].astype(cattype)
        
            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)

            title       =   "dfcleanser status : [process_category_convert]"        
            status_msg  =   "column " + colname + " changed to category successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(dftitle)
                    
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_category_convert_transform] \n convert failure "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_category_convert_transform] opstat : \n    ",opstat.get_status())

    return(opstat)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -       Mapping, Dummies and Category control functions end     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Transform change column datatype                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def change_col_datatype(df,new_fillna_column,colname,datatype,opstat) :
    """
    * -----------------------------------------
    * function : change column datatype
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * -----------------------------------------
    """ 
        
    import numpy as np
    import pandas as pd
    import datetime
    
    from dfcleanser.common.common_utils import get_datatype_from_dtype_str  
    new_datatype    =   get_datatype_from_dtype_str(datatype)

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[change_col_datatype]",colname,datatype,new_datatype)
        
    try :
            
        if(datatype == "datetime.date") :

            df[colname]    =   df[colname] = new_fillna_column.astype(new_datatype,copy=True)
            df[colname]    =   df[colname].dt.date
            df[colname]    =   pd.to_datetime(df[colname])

        elif(datatype == "datetime.time") :
            print("time")
            df[colname]    =   df[colname] = new_fillna_column.astype("datetime.time",copy=True)
            print("time1")
            df[colname]    =   df[colname].dt.time
            print("time2")
            df[colname]    =   pd.to_datetime(df[colname])

        elif(new_datatype == type(np.timedelta64)) :
            df[colname]    =   pd.to_timedelta(new_fillna_column,errors='ignore')
        else :
            print("vanilla")
            df[colname]    =   df[colname] = new_fillna_column.astype(new_datatype,copy=True)
                
    except Exception as e:

        opstat.set_status(False)

        opstat.store_exception("Error changing datatype for column " + colname + " to " + datatype,e)
        title       =   "dfcleanser exception"       
        status_msg  =   "[change column datatype] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

        

def process_change_column_datatype(dftitle,colname,datatype,nafillvalue,nafillmethod,nafillthreshold)  :
    """
    * ----------------------------------------------------
    * function : change column datatype
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * ----------------------------------------------------
    """ 

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[process_change_column_datatype]",dftitle,colname,datatype,nafillvalue,nafillmethod,nafillthreshold)

    opstat      =   opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(df[colname].isnull().sum() > 0)  :

        if( (len(nafillvalue) == 0) or (nafillmethod == "None") ) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("You must define a NA fill value or a NA fill method.")
            
        if(opstat.get_status()) :
            
            if(len(nafillvalue) == 0):
                nafillvalue     =   None

            else :
                from dfcleanser.common.common_utils import get_converted_value
                nafillvalue    =   get_converted_value(datatype,nafillvalue,opstat) 

            if(nafillvalue is None) :  
              
                if(nafillmethod == "None"):
                    nafillmethod    =   None
                    
                    opstat.set_status(False)
                    opstat.set_errorMsg("You must define a NA fill value or a NA fill method.")

                else :
                
                    if(nafillmethod == "mean") :
                
                        from dfcleanser.common.common_utils import is_numeric_col
                        if(is_numeric_col(df,colname)) :
                            
                            nafillvalue     =   df[colname].mean()
                            nafillmethod    =   None

                        else :
                            
                            opstat.set_status(False)
                            opstat.set_errorMsg("can not define a mean nafill value for a non numeric column")
                            nafillvalue     =   None
                            
        if(opstat.get_status()) :
                    
            if(len(nafillthreshold) == 0) :
                nafillthreshold     =   None
            else :
                nafillthreshold     =   float(nafillthreshold)
                   
        if(opstat.get_status()) :  
            
            try :
                        
                if(nafillvalue is None) :
                    new_fillna_column   =   df[colname].fillna(method=nafillmethod,inplace=False,limit=nafillthreshold) 
                else :
                    new_fillna_column   =   df[colname].fillna(nafillvalue,inplace=False,limit=nafillthreshold) 
                            
                change_col_datatype(df,new_fillna_column,colname,datatype,opstat)    
                    
            except Exception as e:
                
                if(not (nafillmethod is None) ) :
                    opstat.store_exception("fillna failure for column " + colname + " : method = " + nafillmethod + " : value = " + str(nafillvalue),e)
                else :
                    opstat.store_exception("fillna failure for column " + colname + " : value = " + str(nafillvalue),e)
                            
                opstat.set_status(False)

    else :

        new_fillna_column   =   df[colname]
        change_col_datatype(df,new_fillna_column,colname,datatype,opstat)

    if(not (opstat.get_status()) ):

        if(opstat.get_exception() is None) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_change_column_datatype] \n " + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

        else :

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_change_column_datatype] error"
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,opstat.get_exception())

            opstat.set_status(False)

    return(opstat)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            Transform change column datatype end               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def make_col_categorical(dftitle, colname, reverse=None)  :   
    """
    * --------------------------------------------------------------
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   reverse         -   reverse the order of the values befor categorize
    *
    * returns : 
    *  N/A
    * ---------------------------------------------------------------
    """ 

    opstat = opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [make_col_categorical]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        from dfcleanser.common.common_utils import get_col_uniques
        ccats       =   get_col_uniques(df, colname)
    
        num_nans    =   df[colname].isnull().sum()

        if(num_nans == 0) :
        
            try :
                if (reverse == None) :
                    ccats.sort()
                else :
                    ccats.sort(reverse=True)
    
                df[colname] = df[colname].astype("category",categories=ccats).cat.codes
          
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[make_col_categorical] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

        else : 

            title       =   "dfcleanser error : [make_col_categorical]"        
            status_msg  =   colname + " has nans"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

    return(opstat)


def make_col_categorical_from_map(dftitle, colname, cmap, handleNA)  :   
    """
    * ---------------------------------------------------------- 
    * function : make a column categorical in place using map
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   cmpa            -   column value map
    *                       ( {'Man': 0, 'Woman': 1} )
    *
    *   handleNA        -   how to handle nas
    *                       'ignore' - ignore errors
    *                       None     - no handling at all 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
   
    opstat = opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser error : [make_col_categorical_from_map]"        
        status_msg  =   "invalid dftitle"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        collist = df[colname]

        if( (handleNA == None) or (handleNA == 'ignore') ) : 

            try :
                df[colname] = collist.map(cmap,handleNA)
            except Exception as e: 

                title       =   "dfcleanser exception"       
                status_msg  =   "[make_col_categorical_from_map] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)
            
        else:

            title       =   "dfcleanser error : [make_col_categorical_from_map]"        
            status_msg  =   "invalid handlena"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

    return(opstat)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           Mapping, Dummies and Category functions end         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Transform generic methods                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def get_trig_values_for_column(df, dfcolname, trigfunc, opstat) :
    """
    * ------------------------------------------------------------------------
    * function : get trig column values
    * 
    * parms :
    *  df            - dataframe
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

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[get_trig_values_for_column]",dfcolname, trigfunc)
    
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
        opstat.store_exception("'get_trig_values_for_column' error : " + dfcolname + " " + trigfunc,e)
        return(None)
        
def random_int_range(df, randomIntLower, randomIntUpper,opstat) :
    """
    * -------------------------------------------------------
    * function : generate column of random ints in a range
    * 
    * parms :
    *  df               - dataframe 
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

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[random_int_range]",randomIntLower, randomIntUpper)

    import random
    
    colrandints = []
    
    try :
        
        for i in range(len(df)) :
            colrandints.append(random.randrange(int(randomIntLower),int(randomIntUpper))) 
            
        return(colrandints)
        
    except Exception as e:
        opstat.store_exception("'random_int_range' error :  " + str(randomIntLower) + " " + str(randomIntUpper),e)
        return(None)


def random_float_range(df, randomFloatLower, randomFloatUpper, opstat) :
    """
    * ----------------------------------------------------------
    * function : generate column of random floats in a range
    * 
    * parms :
    *  df                 - dataframe
    *  randomFloatLower   - random integer lower range value
    *  randomFloatUpper   - random integer upper range value
    *
    * returns : 
    *    Successful : cols list of random floats  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * ------------------------------------------------------------
    """

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[random_float_range]",randomFloatLower, randomFloatUpper)
    
    import numpy as np
    import random
    
    colrandfloats  =   np.array()
    
    try :
        
        for i in range(len(df)) :
            colrandfloats.append(random.randrange(float(randomFloatLower),float(randomFloatUpper)))  
        
        return(colrandfloats)
        
    except Exception as e:
        opstat.store_exception("'random_float_range' error :  " + str(randomFloatLower) + " " + str(randomFloatUpper),e)
        return(None)


def random_datetime_range(df, randomdatetimeLower, randomdatetimeUpper,opstat) :
    """
    * --------------------------------------------------------
    * function : generate column of random floats in a range
    * 
    * parms :
    *  df                   - dataframe title
    *  randomdatetimeLower  - random datetime lower range value
    *  randomdatetimeUpper  - random datetime upper range value
    *
    * returns : 
    *    Successful : cols list of random datetimes  
    *    Error : opstat
    *
    * Notes : 
    *    dfcleanser generic function
    * --------------------------------------------------------
    """

    if(DEBUG_TRABSFORM_COLUMN) :
        print("[random_datetime_range]",randomdatetimeLower, randomdatetimeUpper)
    
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
        opstat.store_exception("'random_float_range' error :  " + str(randomdatetimeLower) + " " + str(randomdatetimeUpper),e)
        return(None)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Transform generic methods end                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#








