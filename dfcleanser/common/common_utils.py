""
# dfc_common_utils 

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.common.cfg import (get_dfc_dataframe_df)

import pandas as pd
import pandas.api.types as pat 
import datetime
import numpy as np


       
new_line =   """
"""


YEARS           =   0
DAYS            =   1
HOURS           =   2
MINUTES         =   3
SECONDS         =   4
MICROSECONDS    =   5
TIMEDELTA       =   6


def get_units_id(unit) :

    if(unit == "Years")                 :   return(YEARS) 
    elif(unit == "Days")                :   return(DAYS)
    elif(unit == "Hours")               :   return(HOURS)
    elif(unit == "Minutes")             :   return(MINUTES)
    elif(unit == "Seconds")             :   return(SECONDS)
    elif(unit == "MicroSeconds")        :   return(MICROSECONDS)
    elif(unit == "datetime.timedelta")  :   return(TIMEDELTA)
    
    return(None)

whitecolor      =   "#FFFFFF"
yellowcolor     =   "#FAF6BE"
redcolor        =   "#F1C4B7"
greencolor      =   "#ADECC4"
    

DUMP_HTML       =   False

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Generic display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def displayHTML(html) :
    from IPython.core.display import HTML 
    display_jupyter_HTML(HTML(html))

def display_jupyter_HTML(html) :
    from IPython.core.display import display 
    display(html)#, metadata=dict(isolated=True))
   
def clear_screen() :
    from IPython.display import clear_output
    clear_output()

def display_url(url) :
    import webbrowser
    webbrowser.open(url)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  javascript from python
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def run_javaScript(script) :
    
    #from IPython.core.display import Javascript
    
    #display_jupyter_HTML(Javascript(script))
    try : 

        from IPython.display import display, Javascript
        display(Javascript(script))

    except :
        alert_user("javascript failure" + script)


def run_jscript(jscript, errmsg=None) :
    """
    * ---------------------------------------------------------
    * function : run a javascript script
    * 
    * parms :
    *  jscript    - javascript script
    *  errmsg     - detailed error message
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    try :            
        from IPython.core.magics.display import Javascript
        display_jupyter_HTML(Javascript(jscript))

    except :
        if(not (errmsg is None)) :
            alert_user(errmsg)


"""
#--------------------------------------------------------------------------
#   display a windows message box
#
#       msg    - text in box
#       title  - msg box title
#
#--------------------------------------------------------------------------
"""          
def display_windows_MessageBox(msg,title) :
    """
    * ---------------------------------------------------------
    * function : display a message box
    * 
    * parms :
    *  msg     - message
    *  title   - box title
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    try :
        import win32api
        win32api.MessageBox(None,msg,title,1)
        
    except :
        print(msg,title)    
    
    
def get_formatted_time(seconds) :
    """
    * ---------------------------------------------------------
    * function : get a formatted representation of delta time
    * 
    * Parms :
    *  seconds    - number of seonds
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return( "%d:%02d:%02d" % (h, m, s)  )  



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Running Clock class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
    
import time
import threading

class RunningClock:
    
    busy        =   False
    delay       =   0.3
    starttime   =   0
    stoptime    =   0
    image_html  =   ""

    @staticmethod
    def spinning_clock():
        
        clockfaces =    [get_image_url(HOUR_1_IMAGE),get_image_url(HOUR_2_IMAGE),get_image_url(HOUR_3_IMAGE),get_image_url(HOUR_4_IMAGE),
                         get_image_url(HOUR_5_IMAGE),get_image_url(HOUR_6_IMAGE),get_image_url(HOUR_7_IMAGE),get_image_url(HOUR_8_IMAGE),
                         get_image_url(HOUR_9_IMAGE),get_image_url(HOUR_10_IMAGE),get_image_url(HOUR_11_IMAGE),get_image_url(HOUR_12_IMAGE)]
        
        while 1: 

            for clockface in clockfaces : yield clockface
            

    def __init__(self, delay=None):
        self.clock_generator = self.spinning_clock()
        
        self.image_html = (self.image_html + '<div class="container" id="clockcontainer" style=" width:60px; height:60px; margin-left:20px; ">')
        self.image_html = (self.image_html + '    <img id="clockrunner" src="./PandasDataframeCleanser_files/graphics/hour12.png" height="60" width="60"></img>' + "</div>")
        
        displayHTML(self.image_html)
        
        if delay and float(delay): self.delay = delay

    def clock_task(self):
        while self.busy:
            change_face_js = "$('#clockrunner').attr('src','" + next(self.clock_generator) + "');"
            run_javaScript(change_face_js)
            time.sleep(self.delay)

    def start(self):
        self.busy = True
        threading.Thread(target=self.clock_task).start()
        self.starttime = time.time()

    def stop(self):
        self.busy = False
        delete_clock = "$('#clockcontainer').remove();"
        time.sleep(self.delay)
        self.stoptime = time.time()
        run_javaScript(delete_clock)
        return(str(get_formatted_time(self.stoptime-self.starttime)) + " seconds")

    def get_elapsed_time(self) :
        return(get_formatted_time(self.stoptime - self.starttime))
 
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Generic data type methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def get_column_datatype(df,colname) :
    
    try :
        return(df[colname].dtype)
    except :
        return(None)

def is_numeric_col(df,colname) :

    try :
        return(pat.is_numeric_dtype(get_column_datatype(df,colname))) 
    except :
        return(False)
        
def is_numeric_datatype(dtype) :
    
    try :
        return(pat.is_numeric_dtype(dtype)) 
    except :
        return(False)
    

def is_int_col(df,colname) :

    try :
        return(pat.is_integer_dtype(get_column_datatype(df,colname))) 
    except :
        return(False)

def is_float_col(df,colname) :
    
    try :
        return(pat.is_float_dtype(get_column_datatype(df,colname))) 
    except :
        return(False)

def is_string_col(df,colname) :
    
    try :
        return(pat.is_string_dtype(get_column_datatype(df,colname)))
    except :
        return(False)

def is_object_col(df,colname) :
    
    try :
        return(pat.is_object_dtype(get_column_datatype(df,colname)))
    except :
        return(False)

def is_bool_col(df,colname) :
    
    try :
        return(pat.is_bool_dtype(get_column_datatype(df,colname)))
    except :
        return(False)

def is_categorical_col(df,colname) :
    
    try :
        return(pat.is_categorical_dtype(get_column_datatype(df,colname)))
    except :
        return(False)

def is_datetime64_col(df,colname,anydatetime64=False) :
    
    try :
        if(anydatetime64) :
            return(pat.is_datetime64_any_dtype(get_column_datatype(df,colname))) 
        else :
            return(pat.is_datetime64_dtype(get_column_datatype(df,colname)))
    except :
        return(False)

def is_timedelta64_col(df,colname,anydatetime64=False) :
    
    try :
        return(pat.is_timedelta64_dtype(get_column_datatype(df,colname))) 
    except :
        return(False)



def is_timestamp_col(df,colname) :
    try : 
        if(df[colname].dtype == pd.Timestamp) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_datetime_col(df,colname) :
    try :
        if(isinstance(df[colname][0],datetime.datetime)) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_date_col(df,colname) :
    try : 
        if(isinstance(df[colname][0],datetime.date)) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_time_col(df,colname) :
    try :  
        if(isinstance(df[colname][0],datetime.time)) :
            return(True)
        else :
            return(False)
    except :
        return(False)
    
def is_timedelta_col(df,colname) :
    try :  
        if(isinstance(df[colname][0],datetime.timedelta)) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_Timestamp_col(df,colname) :
    try :   
        if(isinstance(df[colname][0],pd.Timestamp)) :
            return(True)
        else :
            return(False)
    except :
        return(False)
    
def is_Timedelta_col(df,colname) :
    try :
        if(isinstance(df[colname][0],pd.Timedelta)) :
            return(True)
        else :
            return(False)
    except :
        return(False)
    
def is_datetime_type_col(df,colname) :
    
    if( (is_datetime_col(df,colname)) or (is_date_col(df,colname)) or
        (is_time_col(df,colname)) or (is_timedelta_col(df,colname)) or 
        (is_datetime64_col(df,colname)) or (is_timedelta64_col(df,colname)) or 
        (is_Timestamp_col(df,colname)) or (is_Timedelta_col(df,colname))) :
        return(True)
    else :
        return(False)
  

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser datatype mapping from datatypes to display strings
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 
def get_converted_value(dtype_str,value,opstat) :
    
    cvalue  =   None
    
    try :
    
        if( (dtype_str == "uint8")  or (dtype_str == "numpy.uint8") )                       :   cvalue  =   np.uint8(value)
        elif( (dtype_str == "uint16") or (dtype_str == "numpy.uint16") )                    :   cvalue  =   np.uint16(value)
        elif( (dtype_str == "uint32") or (dtype_str == "numpy.uint32") )                    :   cvalue  =   np.uint32(value)
        elif( (dtype_str == "uint164") or (dtype_str == "numpy.uint64") )                   :   cvalue  =   np.uint64(value)
        elif( (dtype_str == "int8") or (dtype_str == "numpy.int8") )                        :   cvalue  =   np.int8(value)
        elif( (dtype_str == "int16") or (dtype_str == "numpy.int16") )                      :   cvalue  =   np.int16(value)
        elif( (dtype_str == "int32") or (dtype_str == "numpy.int32") )                      :   cvalue  =   np.int32(value)
        elif( (dtype_str == "int64") or (dtype_str == "numpy.int64") )                      :   cvalue  =   np.int64(value)
        elif( (dtype_str == "float16") or (dtype_str == "numpy.float16") )                  :   cvalue  =   np.float16(value)
        elif( (dtype_str == "float32") or (dtype_str == "numpy.float32") )                  :   cvalue  =   np.float32(value)
        elif( (dtype_str == "float64") or (dtype_str == "numpy.float64") )                  :   cvalue  =   np.float64(value)
        elif(dtype_str == "datetime.datetime")                                              :   cvalue  =   datetime.datetime(value)
        elif(dtype_str == "datetime.date")                                                  :   cvalue  =   datetime.date(value)
        elif(dtype_str == "datetime.time")                                                  :   cvalue  =   datetime.time(value)
        elif(dtype_str == "datetime.timedelta")                                             :   cvalue  =   datetime.timedelta(value)
        elif(dtype_str == "int")                                                            :   cvalue  =   int(value)
        elif(dtype_str == "float")                                                          :   cvalue  =   float(value)
        elif(dtype_str == "str")                                                            :   cvalue  =   str(value)
        elif(dtype_str == "object")                                                         :   cvalue  =   object(value)
        elif( (dtype_str == "category") or (dtype_str == "pandas.category") )               :   cvalue  =   pd.Categorical(value)
        elif( (dtype_str == "datetime64") or (dtype_str == "numpy.datetime64") )            :   cvalue  =   np.datetime64(value)
        elif( (dtype_str == "timedelta64") or (dtype_str == "numpy.timedelta64") )          :   cvalue  =   np.timedelta64(value)
        elif( (dtype_str == "Timestamp") or (dtype_str == "pandas.Timestamp") )             :   cvalue  =   pd.Timestamp(value)
        elif( (dtype_str == "Timedelta") or (dtype_str == "pandas.Timedelta") )             :   cvalue  =   pd.Timedelta(value)
        
    except Exception as e:
        opstat.store_exception("Unable to convert value to " + dtype_str,e)
    
    return(cvalue)
    
        
def get_dtype_str_for_datatype(coldtype,fullname=True) :

    if(coldtype == np.uint8)    :   
        if(fullname)    :   return("uint8")  
        else            :   return("numpy.uint8")
    elif(coldtype == np.uint16)                   :   
        if(fullname)    :   return("uint16")
        else            :   return("numpy.uint16")
    elif(coldtype == np.uint32)                   :   
        if(fullname)    :   return("numpy.uint32")
        else            :   return("uint32")
    elif(coldtype == np.uint64)                   :   
        if(fullname)    :   return("numpy.uint64")
        else            :   return("uint64")
    elif(coldtype == np.int8)                   :   
        if(fullname)    :   return("numpy.int8")
        else            :   return("int8")
    elif(coldtype == np.int16)                   :   
        if(fullname)    :   return("numpy.int16")
        else            :   return("int16")
    elif(coldtype == np.int32)                   :   
        if(fullname)    :   return("numpy.int32")
        else            :   return("int32")
    elif(coldtype == np.int64)                   :   
        if(fullname)    :   return("numpy.int64")
        else            :   return("int64")
    elif(coldtype == np.float16)                   :   
        if(fullname)    :   return("numpy.float16")
        else            :   return("float16")
    elif(coldtype == np.float32)                   :   
        if(fullname)    :   return("numpy.float32")
        else            :   return("float32")
    elif(coldtype == np.float64)                   :   
        if(fullname)    :   return("numpy.float64")
        else            :   return("float64")
    
    elif(coldtype == int)                         :   return("int")
    elif(coldtype == float)                       :   return("float")
    elif(coldtype == str)                         :   return("str")
    elif(coldtype == object)                      :   return("object")
    
    elif(coldtype == pd.Categorical)       :   
        if(fullname)    :   return("pandas.Categorical")
        else            :   return("Categorical")
    elif(coldtype == np.datetime64)               :   
        if(fullname)    :   return("numpy.datetime64")
        else            :   return("datetime64")
    elif(coldtype == np.timedelta64)               :   
        if(fullname)    :   return("numpy.timedelta64")
        else            :   return("timedelta64")
    elif(coldtype == pd.Timestamp)                 :   
        if(fullname)    :   return("pandas.Timestamp")
        else            :   return("Timestamp")
    elif(coldtype == pd.Timedelta)                 :   
        if(fullname)    :   return("pandas.Timedelta")
        else            :   return("Timedelta")
        
    elif(coldtype == datetime.datetime)           :   
        if(fullname)    :   return("datetime.datetime")
        else            :   return("datetime")
    elif(coldtype == datetime.date)               :   
        if(fullname)    :   return("datetime.date")
        else            :   return("date")
    elif(coldtype == datetime.time)               :   
        if(fullname)    :   return("datetime.time")
        else            :   return("time")
    elif(coldtype == datetime.timedelta)          :   
        if(fullname)    :   return("datetime.timedelta")
        else            :   return("timedelta")
    
    return(None)

def get_str_of_datatypes() :
    
    datatypes   =   ["uint8","uint16","uint32","uint64","int8","int16","int32","int64",
                     "float16","float32","float64","int","float","str","object",
                     "datetime64","timedelta64","Timestamp","Timedelta",
                     "datetime","date","time","timedelta"]
    
    return(datatypes)


def get_datatype_from_dtype_str(dtype_str) :
    
    
    if( (dtype_str == "uint8")  or (dtype_str == "numpy.uint8") )                       :   return(np.uint8)
    elif( (dtype_str == "uint16") or (dtype_str == "numpy.uint16") )                    :   return(np.uint16)
    elif( (dtype_str == "uint32") or (dtype_str == "numpy.uint32") )                    :   return(np.uint32)
    elif( (dtype_str == "uint164") or (dtype_str == "numpy.uint64") )                   :   return(np.uint64)
    elif( (dtype_str == "int8") or (dtype_str == "numpy.int8") )                        :   return(np.int8)
    elif( (dtype_str == "int16") or (dtype_str == "numpy.int16") )                      :   return(np.int16)
    elif( (dtype_str == "int32") or (dtype_str == "numpy.int32") )                      :   return(np.int32)
    elif( (dtype_str == "int64") or (dtype_str == "numpy.int64") )                      :   return(np.int64)
    elif( (dtype_str == "float16") or (dtype_str == "numpy.float16") )                  :   return(np.float16)
    elif( (dtype_str == "float32") or (dtype_str == "numpy.float32") )                  :   return(np.float32)
    elif( (dtype_str == "float64") or (dtype_str == "numpy.float64") )                  :   return(np.float64)
    elif( (dtype_str == "datetime") or (dtype_str == "datetime.datetime") )             :   return(datetime.datetime)
    elif( (dtype_str == "date") or (dtype_str == "datetime.date") )                     :   return(datetime.date)
    elif( (dtype_str == "time") or (dtype_str == "datetime.time") )                     :   return(datetime.time)
    elif( (dtype_str == "timedelta") or (dtype_str == "datetime.timedelta") )           :   return(datetime.timedelta)
    elif(dtype_str == "int")                                                            :   return(int)
    elif(dtype_str == "float")                                                          :   return(float)
    elif(dtype_str == "str")                                                            :   return(str)
    elif(dtype_str == "object")                                                         :   return(object)
    elif( (dtype_str == "Categorical") or (dtype_str == "pandas.Categorical") )         :   return(pd.Categorical)
    elif( (dtype_str == "datetime64") or (dtype_str == "numpy.datetime64") )            :   return(np.datetime64)
    elif( (dtype_str == "timedelta64") or (dtype_str == "numpy.timedelta64") )          :   return(np.timedelta64)
    elif( (dtype_str == "Timestamp") or (dtype_str == "pandas.Timestamp") )             :   return(pd.Timestamp)
    elif( (dtype_str == "Timedelta") or (dtype_str == "pandas.Timedelta") )             :   return(pd.Timedelta)

    return(None)
    


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser datatype helper methods for listing and displays
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 
def get_datatype(dtypeid) :
    
    import pandas
    import numpy
    
    typeparm = None
    
    if(dtypeid == 0)      : typeparm = numpy.uint8
    elif(dtypeid == 1)    : typeparm = numpy.uint16
    elif(dtypeid == 2)    : typeparm = numpy.uint32
    elif(dtypeid == 3)    : typeparm = numpy.uint64
    elif(dtypeid == 4)    : typeparm = numpy.int8
    elif(dtypeid == 5)    : typeparm = numpy.int16
    elif(dtypeid == 6)    : typeparm = numpy.int32
    elif(dtypeid == 7)    : typeparm = numpy.int64
    elif(dtypeid == 8)    : typeparm = numpy.float16
    elif(dtypeid == 9)    : typeparm = numpy.float32
    elif(dtypeid == 10)   : typeparm = numpy.float64
    elif(dtypeid == 11)   : typeparm = datetime.datetime
    elif(dtypeid == 12)   : typeparm = datetime.date
    elif(dtypeid == 13)   : typeparm = datetime.time
    elif(dtypeid == 14)   : typeparm = datetime.timedelta
    elif(dtypeid == 15)   : typeparm = str
    elif(dtypeid == 16)   : typeparm = object
    elif(dtypeid == 17)   : typeparm = int
    elif(dtypeid == 18)   : typeparm = float
    elif(dtypeid == 19)   : typeparm = pandas.core.dtypes.dtypes.CategoricalDtype
    elif(dtypeid == 20)   : typeparm = numpy.datetime64
    elif(dtypeid == 21)   : typeparm = numpy.timedelta64
    
    return(typeparm)
    
def is_datetime_datatype(datatype) :
    
    if( (datatype == 'datetime64[ns]') or
        (datatype == '<M8[ns]') or
        (datatype == '>M8[ns]') ) :
        return(True)
    else :
        return(False)

def is_timedelta_datatype(datatype) :
    
    if( datatype == 'timedelta64[ns]') :
        return(True)
    else :
        return(False)

def get_datatype_id(dt) :
    
    import numpy
    #import datetime
    import pandas

    #print("get_datatype_id",dt)
    if(dt ==  numpy.uint8)                      : return(0)
    elif(dt == numpy.uint16)                    : return(1) 
    elif(dt == numpy.uint32)                    : return(2) 
    elif(dt == numpy.uint64)                    : return(3) 
    elif(dt == numpy.int8)                      : return(4) 
    elif(dt == numpy.int16)                     : return(5) 
    elif(dt == numpy.int32)                     : return(6)
    elif(dt == numpy.int64)                     : return(7) 
    elif(dt == numpy.float16)                   : return(8) 
    elif(dt == numpy.float32)                   : return(9)
    elif(dt == numpy.float64)                   : return(10) 
    elif(is_datetime_datatype(dt))              : return(11)
    elif(is_datetime_datatype(dt))              : return(12)
    elif(is_datetime_datatype(dt))              : return(13)
    elif(is_timedelta_datatype(dt))             : return(14)
    elif(dt == str)                             : return(15) 
    elif(dt == object)                          : return(16)
    elif(dt == 'O')                             : return(16) 
    elif(dt == int)                             : return(17) 
    elif(dt == float)                           : return(18) 
    elif(isinstance(dt,pandas.core.dtypes.dtypes.CategoricalDtype))  : return(19) 
    elif(dt == 'datetime64[ns]')                : return(20)
    elif(dt == 'timedelta64[ns]')               : return(21)

    return(-1)


def get_datatypes_list(full=True) :
    """
    #--------------------------------------------------------------------------
    #   get a list of supported datatypes
    #
    #       full   - full name flag 
    #
    #   return :
    #       list of datatypes
    #
    #--------------------------------------------------------------------------
    """
    
    if(full) :
        
        dtlist  =   ["numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64",
                     "numpy.int8","numpy.int16","numpy.int32","numpy.int64",
                     "numpy.float16","numpy.float32","numpy.float64","str",
                     "object","int","float","pandas.Categorical"]
        
    else :
        
        dtlist  =   ["uint8","uint16","uint32","uint64",
                     "int8","int16","int32","int64",
                     "float16","float32","float64","str",
                     "object","int","float","Categorical"]
        
    
    return(dtlist)


"""
#--------------------------------------------------------------------------
#   Datatype helper methods
#--------------------------------------------------------------------------
"""


def is_simple_type(value) :
    if type(value) in (int, float, bool, str) :
        return(True)
    else :
        return(False)

def get_first_non_nan_value(df,colname) :

    import pandas as pd
    
    found   =   -1
    
    for i in range(len(df)) :
        if(is_simple_type(df.iloc[i][colname])) :
        
            if(not (pd.isnull(df.iloc[i][colname])) ) :    
                found = i
                break;
        else :
            
            if(not (df.iloc[i][colname] is None)) :
                found = i
                break;
    
    if(found == -1) :
        return(None)
    else :
        return(df.iloc[found][colname])


def is_str_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)

    try :    

        if(isinstance(val,str)) :
            return(True)
        else :
            return(False)
    except :
        return(False)


def does_col_contain_nan(df,colname) :

    totnans =  df[colname].isnull().sum() 
    if(totnans > 0) :
        return(True)
    else :
        return(False)
        

def is_string_a_float(string) : 
    try :
        float(string)
        return(True)
    except : 
        return(False)


def is_string_an_int(string) : 
    try :
        int(string)
        return(True)
    except : 
        return(False)

 
def get_numeric_from_string(string) :
    
    if(is_string_a_float(string)) :
        return(float(string))
    elif(is_string_an_int(string)) :
        return(int(string))
    else :
        return(None)


def does_string_contain_single_quote(string) : 
    
    for i in range(len(string)) :
        if(string[i] == "'") :
            return(True)
            
    return(False)


def get_string_value(val) :
    
    if(type(val) == str) : return(val)
    if(val == None) : return("None")
    if(val == True) : return("True")
    if(val == False) : return("False")
    return(" ")


def is_column_in_df(df,colname) :
    
    df_cols     =   df.columns
    df_cols     =   df_cols.tolist()

    if(colname in df_cols)  :
        return(True) 
    else :
        return(False)

         
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Input Form parms parsing methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_num_input_ids(idList) :
    
    count = 0
    for i in range(len(idList)) :
        if(idList[i] != None) :
            count = count + 1
            
    return(count)

def getmaxlength(list) : 
    maxlen = 0;
    for i in range(len(list)) :
        if(len(list[i]) > maxlen) :
            maxlen = len(list[i])
            
    return(maxlen)

def addspaces(count) :
    spaces = "";
    for i in range(count) :
        spaces = spaces + " ";
        
    return(spaces)


def valid_parms_list(labels, parms) :
    """
    #--------------------------------------------------------------------------
    #   get the parameter list for a returned form
    #
    #       parms  - input form parms 
    #       ids    - list of ids to match parms
    #
    #   return list of parms
    #
    #--------------------------------------------------------------------------
    """
    
    goodList = True 
    
    if( (labels != None) and (parms != None) and
        (len(labels) == len(parms)) ) :
        for i in range(len(labels)) :
            if( (len(labels[i]) == 0) or (len(parms[i]) == 0) ) :
                goodList = False
                    
    return(goodList)

     
def get_parms_for_input(parms,ids) :
    """
    #--------------------------------------------------------------------------
    #   get the parameter list for a returned form
    #
    #       parms  - input form parms 
    #       ids    - list of ids to match parms
    #
    #   return list of parms
    #
    #--------------------------------------------------------------------------
    """
    outparms = []
    
    #print("\nget_parms_for_input",type(parms),parms)
    #print("\nget_parms_for_input",type(ids),ids)
    
    try :
        
        if( (parms == None) or (ids == None) or 
           ((len(parms) == 0) or (len(ids) == 0)) ) :
            return(outparms)
    
        #print("\nget_parms_for_input : parms",len(parms),type(parms),parms) 
        #print("\nget_parms_for_input : ids  ",len(ids),ids) 
        
        if(type(parms) == str) :
            import json
            inparms = json.loads(parms)
        else :
            inparms = parms
            
    except :
        print("get_parms_for_input invalid input parms")
    
    #print("\n\nget_parms_for_input : inparms  ",inparms) 
    
    try :
        
        if(len(inparms[0]) == 0) :
            return(outparms)
        
        for i in range(len(ids)) :
            if(not (ids[i] is None)) :
                found = -1
                for j in range(len(inparms[0])) :
                    if(inparms[0][j] == ids[i]) :
                        found = j
                if(found > -1) :
                    outparms.append(inparms[1][found])
                else :
                    outparms.append("")
            else :
                if(ids[i] != None) :
                    outparms.append("")  
                    
    except :
        print("get_parms_for_input invalid idlist")    

    return(outparms)

     
def get_select_defaults(form,formid,parmids,parmtypes,selectDicts) :
    """
    #--------------------------------------------------------------------------
    #   get all select dicts for a form
    #
    #       formid         - form id 
    #       parmids        - parms list id 
    #       parmtypes      - parm types
    #       selectDicts    - list of select dicts
    #
    #   return select default value
    #
    #--------------------------------------------------------------------------
    """

    numselects  =   0
    
    for i in range(len(parmids)) :
        
        if( (parmtypes[i] == "select") or (parmtypes[i] == "selectmultiple") ):
            
            form.add_select_dict(formid,
                                 parmids,
                                 parmids[i],
                                 selectDicts[numselects])
            
            numselects  =   numselects + 1

 

def get_parms_list_from_dict(labels,parmsdict) :
    """
    #-----------------------------------------------------------
    #   extract parm values from a dict
    #
    #       labels    - parm labels
    #       parmsdict - parm dict
    #
    #   return list of parms values
    #
    #----------------------------------------------------------
    """
    parmsValues     =   []
    
    for i in range(len(labels)) :
        parmsValues.append(parmsdict.get(labels[i],""))

    return(parmsValues)
 

STRING_PARM             =   0
INT_PARM                =   1
FLOAT_PARM              =   2
BOOLEAN_PARM            =   3
DICT_PARM               =   4


def get_function_parms(pkeys,pvals,ptypes) :
    """
    * ---------------------------------------------------------
    * function : get kwargs from form cfg parms
    * 
    * parms :
    *  pkeys    - parm key values
    *  pvals    - parm values
    *  ptypes   - parm types
    *
    * returns : 
    *  geocoder engine 
    * --------------------------------------------------------
    """

    kwargs      =   {}

    if(type(pvals) == str) :
        p1vals = pvals.strip("[")
        p1vals = p1vals.strip("]")
        p1vals = p1vals.strip('"')

        print("p1vals",type(p1vals),len(p1vals),p1vals)
        if("," in p1vals) :
        
            import json
            plist = json.loads(p1vals)
        else :
            plist = [p1vals]
            
    else :
        plist = pvals    
    
    for i in range(len(pkeys)) :
        if(len(plist[i]) > 0) :
            if(ptypes[i] == FLOAT_PARM) :
                pval = float(plist[i])
            elif(ptypes[i] == INT_PARM) :
                pval = int(plist[i])
            elif(ptypes[i] == BOOLEAN_PARM) :
                if(plist[i] == "True") :
                    pval = True
                else :
                    pval = False
            elif(ptypes[i] == DICT_PARM) :
                pval    =   json.loads(plist[i])            
            else :
                pval = plist[i]
   
            kwargs.update({pkeys[i] : pval})
     
    return(kwargs)    


"""
#--------------------------------------------------------------------------
#   dfcleanser get full parms methods
#--------------------------------------------------------------------------
"""
def get_full_parms_html(inputid) :
    """
    * ---------------------------------------------------------
    * function : get full input html
    * 
    * Parms :
    *  inputid     - input form id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import get_Input
    inputlist = get_Input(inputid)
    
    #print("get_full_parms_html",)
    
    from dfcleanser.common.html_widgets import InputForm
    input_form   =   InputForm(inputid,inputlist[0],inputlist[1],
                               inputlist[2],inputlist[3],inputlist[4],
                               inputlist[5])
    
    input_form.set_form_select_dict(inputlist[6])
    input_form.set_form_custom_dict(inputlist[7])
    input_form.set_label_note_dict(inputlist[8])
    
    input_form.set_fullparms(True)
    input_html = input_form.get_html()
    
    #print("input_html",input_html)
    
    startnewhtml    =   input_html.find(inputid + "input") + len(inputid + "input") + 3
    endnewhtml      =   input_html.find(inputid + "tb")
    newhtml         =   input_html[startnewhtml:endnewhtml]
    endnewhtml      =   newhtml.rfind("<div") -1
    newhtml         =   newhtml[0:endnewhtml]
    endnewhtml      =   newhtml.rfind("</div>") -1
    
    newhtml         =   newhtml[0:endnewhtml]
    
    #print("newhtml",newhtml)
    
    return(newhtml)
    

def get_fullparms(parms) :
    """
    * ---------------------------------------------------------
    * function : get full parms for an input
    * 
    * Parms :
    *  parms    - input id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    formid     =   parms[0]
    
    input_html = get_full_parms_html(formid)
    new_input_html = patch_html(input_html)
    
    import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm  
    from dfcleanser.sw_utilities.sw_utility_geocode_widgets import display_geocoders  
    
    if(formid == "arcgisgeocoder")      :   display_geocoders(sugm.ArcGISId,True)
    elif(formid == "googlegeocoder")    :   display_geocoders(sugm.GoogleId,True)
    elif(formid == "binggeocoder")      :   display_geocoders(sugm.BingId,True)
    elif(formid == "mapquestgeocoder")  :   display_geocoders(sugm.OpenMapQuestId,True)
    elif(formid == "nomingeocoder")     :   display_geocoders(sugm.NominatimId,True)
        
    else :
        
        change_input_js = "$('#" + formid + "input').html('"
        change_input_js = change_input_js + new_input_html + "');"
        run_jscript(change_input_js,"fail to get full parms for : " + formid)
        
        change_input_js = "$('#" + formid + "').css('background-color','#F8F5E1');";
        run_jscript(change_input_js,"fail to get full parms for : " + formid)
        
        #change_input_js = "$('#" + formid + "tb button').button();";
        #run_jscript(change_input_js,"fail to get full parms for : " + formid)
        


def set_chapter_df(parms) :
    """
    * ---------------------------------------------------------
    * function : set the default df for a chapter
    * 
    * Parms :
    *  parms    - input id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    chapterid   =   parms[0]
    df_name     =   parms[1]
    
    from dfcleanser.common.cfg import set_config_value, CURRENT_CLEANSE_DF, CURRENT_TRANSFORM_DF, CURRENT_EXPORT_DF, CURRENT_GEOCODE_DF, CURRENT_SUBSET_DF, CURRENT_INSPECTION_DF
    
    if(chapterid == "dcdfdataframe") :
        set_config_value(CURRENT_CLEANSE_DF,df_name)

    elif(chapterid == "dtdfdataframe") :
        set_config_value(CURRENT_TRANSFORM_DF,df_name)
        
    elif(chapterid == "dedfdataframe") :
        set_config_value(CURRENT_EXPORT_DF,df_name)
    
    elif(chapterid == "dgdfdataframe") :
        set_config_value(CURRENT_GEOCODE_DF,df_name)
    
    elif(chapterid == "dsdfdataframe") :
        set_config_value(CURRENT_SUBSET_DF,df_name)
        
    else :
        set_config_value(CURRENT_INSPECTION_DF,df_name)
        


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser html common utilities
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def patch_html(htmlin,replaceNewline=True) :
    
    # strip out javascript bad chars
    if(replaceNewline) :
        new_table_html = htmlin.replace('\n','')
    else :
        new_table_html = htmlin
        
    newsinglequote = '\&apos;'
    
    #TODO fix hack
    for i in range(len(new_table_html)+2000) :
        if(i < len(new_table_html)) :
            if(new_table_html[i] == "'") :
                new_str = new_table_html[:i] + newsinglequote + new_table_html[i+1:] 
                new_table_html = new_str
    
    return(new_table_html)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser table scrolling methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def refresh_scroll_buttons(tableid) :
    
    buttonids     =   ["downarrow", "uparrow", "leftarrow", "rightarrow"]
    buttons       =   [DOWN_ARROW_IMAGE, UP_ARROW_IMAGE, LEFT_ARROW_IMAGE, RIGHT_ARROW_IMAGE]

    
    for i in range(len(buttons)) :
        
        button_id       =   tableid + buttonids[i] + "Id"
        
        change_html     =   ("'#" + button_id + "').attr('src'," + "'" + get_image_url(buttons[i]) + "'")
        change_cols_js = ("$(" + change_html + ");")

        run_jscript(change_cols_js,"fail to refresh sroll table : ")
    


def scroll_table(parms) :
    """
    * ---------------------------------------------------------
    * function : scroll a dc table
    * 
    * Parms :
    *  tableid    - table id
    *  direction  - scroll direction
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    tableid     =   parms[0]
    direction   =   int(parms[1])
    
    #print("scroll_table",tableid,direction)
    from dfcleanser.common.display_utils import get_scroll_table_html
    new_table_html  = get_scroll_table_html(tableid,direction)
    
    if(new_table_html is None) :
        return()

    #print("scroll_table",new_table_html)
    change_table_js = "$("
    if( (new_table_html.find("<thead") == -1) or (tableid == "dfschemaTable") or (tableid == "dfchknumTable") ) :
        change_table_js = change_table_js + "'#" + tableid + "').html('"
        
    else :
        change_table_js = change_table_js + "'#" + tableid + "container').html('"
        
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_table parms : "+tableid+" "+str(direction))
 
    refresh_bg_js = "$('#" + tableid + "_thr').css({'background-color':'#6FA6DA'});"
    run_jscript(refresh_bg_js,"fail scroll_table : "+tableid+" "+str(direction))
    refresh_bg_js = "$('#" + tableid + "_thr').css({'color':'white'});"
    run_jscript(refresh_bg_js,"fail scroll_table : "+tableid+" "+str(direction))
    refresh_bg_js = "$('#" + tableid + "buttons').css({'margin-right':'1%'});"
    run_jscript(refresh_bg_js,"fail scroll_table : "+tableid+" "+str(direction))

    refresh_scroll_buttons(tableid)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser df subset utility dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_dfsubset_vals_html(filters,colname) :
    """
    * ---------------------------------------------------------
    * function : get full parms for an input
    * 
    * Parms :
    *  parms    - input id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    from dfcleanser.sw_utilities.sw_utility_dfsubset_widgets import get_subset_input_id, get_subset_input_labelList
    import dfcleanser.common.cfg as cfg
    
    # get the drop flag and col name list
    dfsparms = cfg.get_config_value(get_subset_input_id+"Parms")
        
    if( (not(dfsparms == None)) and (len(dfsparms) > 0) ):
        dftitle = cfg.get_cfg_parm_from_input_list(get_subset_input_id,
                                                   "input_dataframe",
                                                    get_subset_input_labelList)
        
    df  =   get_dfc_dataframe_df(dftitle)

    from dfcleanser.sw_utilities.sw_utility_dfsubset_widgets import get_dfsubset_table
    cols_html = get_dfsubset_table(df,filters,colname)

    startinner  =   cols_html.find('">')
    startinner  =   startinner + len('">') + 1
    endinner    =   cols_html.rfind("</div>")
    endinner    =   endinner - 1

    table_html  =   cols_html[startinner:endinner]
    
    return(table_html)


def get_dfsubset_vals(parms) :
    """
    * ---------------------------------------------------------
    * function : get dfsubset vals
    * 
    * Parms :
    *  parms    - input id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    filters     =   parms[0]
    colname     =   parms[1]
    
    if( (colname == -1) or (len(colname) == 0) ):
        colname = None

    table_html      =   get_dfsubset_vals_html(filters,colname) 
    
    table_html      =   table_html.replace("&","&amp;")
    new_table_html  =   patch_html(table_html)
    
    change_table_js = "$('#dcsubsetcolnamesTablecontainer').html('"
    change_table_js = change_table_js + new_table_html + "');"
            
    run_jscript(change_table_js,"fail to get unique vals for : ")
    
    buttons     =   ["downarrow","uparrow"]
    
    for i in range(len(buttons)) :
    
        tstamp = datetime.datetime.now().time()

        change_cols_js = ("$('#" + buttons[i]+"Id" + "').attr('src'," +
                                 "'https://rickkrasinski.github.io/dfcleanser/graphics/" + buttons[i] + ".png?timestamp=" + str(tstamp) +"');")
        
        run_jscript(change_cols_js,"fail to refresh sroll table : ")
    
    if(filters == -1) : 
        change_title_js = "$('#dcsubsetcolnamesTableTitle').text('Column Values')"
        run_jscript(change_title_js,"fail to get unique vals for : ")
    else :
        change_title_js = "$('#dcsubsetcolnamesTableTitle').text('Column Names')"
        run_jscript(change_title_js,"fail to get unique vals for : ")


col_names_table_start   =   """
                    <div class="container" style="padding:5px; margin:auto; width:100%; border:0px" id="subdatacolnamescontainer">
                        <div class="container" style="padding:5px; margin:auto; width:100%"  id="subdatacolnamesselectdiv">
                            <div class="container dc-container dc-default-input-inner-div">
                                <div class="form-group-sm">
                                    <label  for="subdatacolnames" style="text-align:left; font-size: 13px">* XXXXDSSUBID</label>
                                    <select id="subdatacolnames" multiple="multiple" size="30" style="margin-left:1px; font-size: 11px" class="form-control">
"""


col_names_table_end1   =   """
                                    </select>
                                </div>
                                <div style="margin-top: 10px"  id="censusdfinsertcols">

"""

col_names_table_end2   =   """
                                </div>
                            </div>
                        </div>
                    </div>
"""

col_names_buttons   =   """
                                    <div class="container dc-container dc-default-input-button-container btn-grp-center">
                                        <div class="btn-group btn-center"   style="width: 100%">
                                            <button type="button" class="btn btn-primary" style = ' font-size: 13px;  margin-left: 50px;  height: 75px;  width: 110px ' onclick="get_census_callback(33)">Insert</br>Columns</br>Into df(s)</button>
                                            <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 110px ' onclick="get_census_callback(0)">Return</button>
                                            <button type="button" class="btn btn-primary" style = ' font-size: 13px;  height: 75px;  width: 110px ' onclick="displayhelp(https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-swutilities.html#dfc_swutilities_subset)">Help</button>
                                        </div>
                                    </div>
"""

col_names_table_end     =   col_names_table_end1 + col_names_buttons + col_names_table_end2
 
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser df census utility dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data inspection dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
def get_df_browser_search(numeric) :
    ""
    * ---------------------------------------------------------
    * function : get column samples
    * 
    * Parms :
    *  numeric    - search for numeric values
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    ""
    #print("get_df_browser_search",numeric,type(numeric))
    
    if(numeric == 1) :
        num_flag    =   False
    else :
        num_flag    =   True
    
    import dfcleanser.common.cfg as cfg
    from dfcleanser.data_inspection.data_inspection_widgets import get_colsearch_form
    new_html    =   get_colsearch_form(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                       num_flag).get_html()
    
    start_html  =   new_html.find("<div class='container' style='padding:5px; margin:auto; width:100%'  id="+'"datainspectcolsearchinput">')
    end_html    =   len(new_html) - 6
    
    new_html    =   new_html[start_html:end_html-7]
    new_html    =   new_html.replace("'",'"')
    new_html    =   new_html.replace('("colsearchnames"',"('colsearchnames'")
    
    final_html  =   patch_html(new_html)

    change_table_js = "$('#datainspectcolsearch').html('"
    change_table_js = change_table_js + final_html + "');"
            
    run_jscript(change_table_js,"fail to get search df html : ")
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data transform dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def change_col_stats(parms)  :
    
    selectid    =   parms[0]
    colid       =   parms[1]
    
    import dfcleanser.common.cfg as cfg
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    colnames    =   list(df.columns)
    if(not (colid in colnames)) :
        return()
    
    cfg.set_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY,colid)

    from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
    colstats_html   =   display_transform_col_data(df,colid,False)
    
    start_html  =   colstats_html.find('<div class="panel panel-primary"')
    end_html    =   len(colstats_html) - 14
    
    new_html    =   colstats_html[start_html:end_html]
    final_html  =   patch_html(new_html)
    
    change_table_js = "$('#colstatsTablecontainer').html('"
    change_table_js = change_table_js + final_html + "');"
            
    run_jscript(change_table_js,"fail to change col stats html : ")
    
    if(selectid == "mapcolumnname") :
        
        counts  =   df[colid].value_counts().to_dict()
        uniques =   list(counts.keys())

        if(is_numeric_col(df,colid)) :
            uniques.sort()

        keyslist = ""
            
        for i in range(len(uniques)) :
            keyslist = (keyslist + str(uniques[i])) 
            if(not((i+1) == len(uniques))) :
                keyslist = (keyslist + str(","))
        
        if(len(uniques) > 300) :
            keyslist = "mapping keys too large to define by hand"
            parmsProtect = True
        else :
            parmsProtect = False
            
        change_map_vals_js = "$('#mapkeys').val('" + keyslist + "');"
        change_map_vals_prop_js = "$('#mapkeys').prop('disabled', true);"
            
        run_jscript(change_map_vals_js,"fail to change map vals html : ")
        run_jscript(change_map_vals_prop_js,"fail to change map vals html : ")
        
        if(parmsProtect) :
            change_map_protect_js = "$('#mapvals').prop('disabled', true);"
        else :
            change_map_protect_js = "$('#mapvals').prop('disabled', false);"
            
        run_jscript(change_map_protect_js,"fail to change map vals html : ")
        



def get_column_samples(parms) :
    """
    * ---------------------------------------------------------
    * function : get sample values for a colummn
    * 
    * Parms :
    *  parms    - input id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    colname     =   parms

    from dfcleanser.common.display_utils import get_column_samples_html
    cols_html   =   get_column_samples_html(colname) 

    new_cols_html = patch_html(cols_html)
    
    change_table_js = "$('#datetimecolnamesTableContainer').html('"
    change_table_js = change_table_js + new_cols_html + "');"
            
    run_jscript(change_table_js,"fail to get sample values for : ")


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser system dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def select_df(parms) :
    """
    * ---------------------------------------------------------
    * function : select a df
    * 
    * Parms :
    *  parms    - formid, title
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    formid     =   parms[0]
    title      =   parms[1]
    
    from dfcleanser.common.cfg import get_dfc_dataframe
    dfcdf   =   get_dfc_dataframe(title)
    
    newdf       =   dfcdf.get_df()
    numrows     =   len(newdf)
    numcols     =   len(newdf.columns)
    notes       =   dfcdf.get_notes()
    
    change_input_js = "$('#dfnumrows').val(" + str(numrows) + ");"
    run_jscript(change_input_js,"fail to set df parms : " + formid)

    change_input_js = "$('#dfnumcols').val(" + str(numcols) + ");"
    run_jscript(change_input_js,"fail to set df parms : " + formid)

    notes      =   notes.replace("\n","dfc_new_line")
    notes      =   notes.replace("'",'"')
    
    change_input_js = "set_textarea('dfnotes', '"
    change_input_js = change_input_js + notes + "');"
    run_jscript(change_input_js,"fail to get sample values for : ")


def open_as_excel(dfid) :
    """
    * ---------------------------------------------------------
    * function : open a df in excel
    * 
    * Parms :
    *  dfid    - dataframe id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
        
    import os
    import dfcleanser.common.cfg as cfg

    if(dfid == 0) :
        df          =   cfg.get_current_chapter_df(cfg.DataInspection_ID)
        
        dfc_temp_path       =   os.path.join(cfg.get_dfcleanser_location(),"files","temp")
        dfc_temp_path       =   (dfc_temp_path + "\\exceldfs\\")
        
        try :
            
            tmp_name    =   dfc_temp_path + cfg.get_config_value(cfg.CURRENT_INSPECTION_DF) + "_temp.csv"
            
            index_columns       =   df.index.names
            
            if(len(index_columns) == 0) :
                df.to_csv(tmp_name, index=False)
            else :
                df.to_csv(tmp_name)
            
            os.startfile(tmp_name)    
    
        except :
            
            alert_user("Unable to open df in excel")
            
    elif(dfid == 1) :
        
        try :
            
            tmp_name    =   cfg.get_config_value(cfg.BULK_GEOCODE_EXPORTED_CSV_ID)
            os.startfile(tmp_name)    
    
        except :
            
            alert_user("Unable to open " + str(tmp_name) + " in excel")
        
    elif(dfid == 2) :
        
        try :
            
            tmp_name    =   cfg.get_config_value(cfg.BULK_GEOCODE_APPENDED_CSV_ID)
            os.startfile(tmp_name)    
    
        except :
            
            alert_user("Unable to open df in excel")

    elif(dfid == 3) :
        
        try :
            
            tmp_name    =   cfg.get_config_value(cfg.BULK_ERRORS_EXPORTED_CSV_ID)
            os.startfile(tmp_name)    
    
        except :
            
            alert_user("Unable to open df in excel")

    elif(dfid == 4) :
        
        try :
            
            import os
            
            tmp_csv_name    =   os.path.join(cfg.get_dfcleanser_location(),"files")
            tmp_csv_name    =   os.path.join(tmp_csv_name,"dfc_subset_working.csv")
            
            from dfcleanser.sw_utilities.sw_utility_dfsubset_model import get_current_subset_df
            df  =   get_current_subset_df()
            
            index_columns       =   df.index.names
            
            if(len(index_columns) == 0) :
                df.to_csv(tmp_csv_name, index=False)
            else :
                df.to_csv(tmp_csv_name)
            
            os.startfile(tmp_csv_name)    
    
        except :
            
            alert_user("Unable to open df in excel")


def change_df_select(visible_df_forms) :
    """
    * ---------------------------------------------------------
    * function : change the df list in select forms
    * 
    * Parms :
    *  visible_df_forms - dfs to make visible
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    #print("change_df_select",visible_df_forms) 
    
    import dfcleanser.common.cfg as cfg
    
    for i in range(len(visible_df_forms)) :
        cfg.update_chapter_df_select(visible_df_forms[i])

 
def get_apply_fn(funcparms) :
    """
    * ---------------------------------------------------------
    * function : change apply fn code box
    * 
    * Parms :
    *  funcparms - column name, function id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    cname   =   funcparms[0]
    fnid    =   funcparms[1]
    
    change_fncode_js  =   "get_apply_fn_parms('" + cname + "','" + fnid + "')"
    print("change_fncode_js",change_fncode_js)

    run_jscript(change_fncode_js,"fail to set df parms : " + change_fncode_js)



def get_add_df_col_change_html(dftitle) :
    """
    * ---------------------------------------------------------
    * function : get colnmes list for a df
    * 
    * Parms :
    *  dftitle - dfc df title
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
     
    #from dfcleanser.common.cfg import get_dfc_dataframe_df
    current_df      =   get_dfc_dataframe_df(dftitle)
    colnames        =   current_df.columns.tolist()

    selhtml         =   ""

    for i in range(len(colnames)) :
        selhtml     =   (selhtml + "                    <option style='text-align:left; font-size:11px;'")
            
        if(i == 0) :
            selhtml     =   (selhtml + " selected")
                
        selhtml     =   (selhtml + ">" + colnames[i] + "</option>")
        if(i < len(colnames)) :
            selhtml     =   (selhtml + new_line)    
        
    return(selhtml)


def get_add_df_col_change(adddfparms) :
    """
    * ---------------------------------------------------------
    * function : change add col from df df titles
    * 
    * Parms :
    *  adddfparms - column name, function id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    selectid        =   adddfparms[0]
    dfname          =   adddfparms[1]
    
    change_select_html  =   get_add_df_col_change_html(dfname)
    
    new_select_html = patch_html(change_select_html)
    
    if(selectid == "addcoloutdftitle") :
    
        change_select_js = "$('#addcolddfoindex').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
        
    else :
        
        change_select_js = "$('#addcolddfcname').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
        
        change_select_js = "$('#addcolddfsindex').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
        
   
def add_col_from_df_change_df(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the col name list fro add col from df
    * 
    * Parms :
    *  parms - selectid, ftitle
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    selectid    =   parms[0]
    ftitle      =   parms[1]
    
    print("add_col_from_df_change_df",parms,selectid,ftitle)
    
    change_select_html  =   get_add_df_col_change_html(ftitle)
    
    new_select_html = patch_html(change_select_html)
    
    if(selectid == "addcolsourcedftitle") :
    
        change_select_js = "$('#addcolsourcecolname').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
        
        change_select_js = "$('#addcolsourceindex').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
    
    elif(selectid == "addcoloutputdftitle") :
    
        change_select_js = "$('#addcoloutputindex').html('"
        change_select_js = change_select_js + new_select_html + "');"
            
        run_jscript(change_select_js,"fail to get sample values for : ")
        
    else :
        
        return()
    
    reset_source_index_list_js  =   "$('#addcoldfsourceindexlist').val('[]');"
    run_jscript(reset_source_index_list_js,"fail to change col stats html : ")

    reset_output_index_list_js  =   "$('#addcoldfoutputindexlist').val('[]');"
    run_jscript(reset_output_index_list_js,"fail to change col stats html : ")


def clear_add_col_df(parms)  :
    """
    * ---------------------------------------------------------
    * function : clear the add col from df inputs
    * 
    * Parms :
    *  parms - optionid
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    optionid    =   parms[0]
    
    import dfcleanser.common.cfg as cfg
    
    dftitle     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
    
    import dfcleanser.data_transform.data_transform_model as dtm
    if(optionid == dtm.CLEAR_SOURCE_PARMS) :
        
        add_col_from_df_change_df(["addcolsourcedftitle",dftitle])
        
    else :
        
        add_col_from_df_change_df(["addcoloutputdftitle",dftitle])


def change_add_col_df_source_col(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the datatype for new col in ass cold from df
    * 
    * Parms :
    *  parms - optionid
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    selectid    =   parms[0]
    ftitle      =   parms[1]
    colname     =   parms[2]
    
    current_df  =   get_dfc_dataframe_df(ftitle)
    
    source_col_dtype    =   current_df[colname].dtype
    
    print("source_col_dtype",source_col_dtype)
    
    dtype_str           =   get_dtype_str_for_datatype(source_col_dtype)
    print("dtype_str",dtype_str,type(dtype_str))
    
    reset_source_index_list_js  =   "$('#addcoloutputdftype').val('" + dtype_str + "');"
    run_jscript(reset_source_index_list_js,"fail to change col stats html : ")


def change_current_row_value(column)  :
    """
    * ---------------------------------------------------------
    * function : change the column value 
    * 
    * Parms :
    *  parms - optionid
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    from dfcleanser.common import cfg as cfg
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)    
    row_id      =   cfg.get_config_value(cfg.CLEANSING_ROW_KEY)
    
    
    index_columns   =   df.index.names
    
    index_names     =   []
    index_offset    =   0
                    
    if(len(index_columns) > 0) :
        for i in range(len(index_columns)) :
            if( not (index_columns[i] is None) ) :
                index_names.append(index_columns[i])
            else :
                index_offset    =   1

    col_index   =   None
    
    if(len(index_names) > 0)  :
        for i in range(len(index_names)) :
            if(index_names[i] == column) :
                col_index   =   (i + 1) * -1
                break
            
    if(col_index is None) :
        df_columns  =   list(df.columns)
        for i in range(len(df_columns)) :
            if(df_columns[i] == column) :
                col_index   =   i 
                break
                
    if(not (col_index is None)) :
        
        cfg.set_config_value(cfg.CLEANSING_COL_KEY,col_index)
        
        if(col_index < 0) :
            
            col_index       =   (col_index + 1) * -1
            index_array     =   df.index.values
            current_value   =   index_array[row_id][col_index + index_offset]
            
        else :
        
            current_value   =   df.iloc[row_id,col_index]
        
        set_current_value_js  =   "$('#changercval').val('" + str(current_value) + "');"
        run_jscript(set_current_value_js,"fail to change col stats html : ")


def change_selected_dfc_census_col(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the dfc census column selected 
    * 
    * Parms :
    *  parms - attributes
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    colname     =   parms[0]
    colid       =   parms[1]
    #dtype       =   parms[2]
    #nanvalue    =   parms[3]
        
    if(1) :
        print("change_selected_dfc_census_col : ",colname,colid)
        
    from dfcleanser.sw_utilities.sw_utility_census_model import current_dataset_inserting_from
    #datasetid               =   current_dataset_inserting_from.get_datasetid()
    
    from dfcleanser.common.cfg import get_config_value,  CENSUS_SELECTED_SUBSET_ID   
    subdataid               =   get_config_value(CENSUS_SELECTED_SUBSET_ID)
    if(subdataid is None) :
        subdataid   =   0
            
    subdata_col_attributes  =   current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
    cols_list               =   subdata_col_attributes.get_columns_list() 
    
    for i in range(len(cols_list)) :
        if(cols_list[i] == int(colid)) :
            col_index   =   i

    col_dtype       =   current_dataset_inserting_from.get_col_dtype(col_index,subdataid)
    
    if(col_dtype is None) :
        
        from dfcleanser.sw_utilities.sw_utility_census_model import current_dataset_inserting_from
        datasetid   =   current_dataset_inserting_from.get_datasetid()
        
        from dfcleanser.sw_utilities.sw_utility_census_widgets import get_census_dfs_for_dataset
        from dfcleanser.sw_utilities.sw_utility_census_model import get_dfs_for_dataset
        dataset_dfs =   get_census_dfs_for_dataset(datasetid)
        df_ds       =   get_dfs_for_dataset(current_dataset_inserting_from.get_datasetid())
        
        ds_df_offset    =   0
        
        for i in range(len(dataset_dfs)) : 
            for j in range(len(df_ds)) :
                if(dataset_dfs[i] == df_ds[j]) :
                    ds_df_offset    =   i
        
        if(len(dataset_dfs) > 0) :
            
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            
            df          =   get_dfc_dataframe_df(dataset_dfs[ds_df_offset])
            dfdtypes    =   df.dtypes.tolist()
            col_dtype   =   str(dfdtypes[int(colid)])
            
        else :    
            col_dtype   =   str("TBD")

    if(is_numeric_col(df,colname)) :        
        minval      =   str(df[colname].min())    
        maxval      =   str(df[colname].max())
    else :
        minval      =   "NA"    
        maxval      =   "NA"

    nanvalue    =   current_dataset_inserting_from.get_col_nanvalue(col_index,subdataid)
    if(nanvalue is None) :
        nanvalue = "nan"
        
    set_current_value_js  =   "$('#coltoinsertminval').val('" + minval + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")
    
    set_current_value_js  =   "$('#coltoinsertmaxval').val('" + maxval + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")

    set_current_value_js  =   "$('#coltoinsertdtype').val('" + str(col_dtype) + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")

    set_current_value_js  =   "$('#newcoldtype').val('" + "uint8" + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")

    set_current_value_js  =   "$('#currentcolnanval').val('" + str(nanvalue) + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")
    
    set_current_value_js  =   "$('#newcolnanval').val('" + "" + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")
     
    #set_current_value_js  =   "$('#colstoinsert option:selected.text('" + str(colname) + "');"
    set_current_value_js  =   "$('#colstoinsert option[value=" + '"' + colname + '"]' + "').attr('selected', true);"
    print(set_current_value_js)
    run_jscript(set_current_value_js,"fail to change col stats html : ")


def change_dfc_census_col_attrs(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the dfc census column attributes 
    * 
    * Parms :
    *  parms - attributes
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    colname     =   parms[0]
    colid       =   int(parms[1])
    dtype       =   parms[2]
    nanvalue    =   parms[3]
        
    if(1) :
        print("change_dfc_census_col_attrs : ",colname,colid,dtype,nanvalue)
        
    from dfcleanser.sw_utilities.sw_utility_census_model import current_dataset_inserting_from
    #datasetid               =   current_dataset_inserting_from.get_datasetid()
    
    subdataid               =   current_dataset_inserting_from.get_subdatasetid()
    
    if(subdataid is None) :
        subdataid   =   0
            
    subdata_col_attributes  =   current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
    cols_list               =   subdata_col_attributes.get_columns_list() 
    
    print("subdataid",subdataid)
    print("cols_list",cols_list)  
    
    #for i in range(len(cols_list)) :
    #    if(cols_list[i] == int(colid)) :
    #        col_index   =   i
    #        break


    current_dataset_inserting_from.set_col_dtype(colid, dtype, subdataid)
    current_dataset_inserting_from.set_col_nanvalue(colid, nanvalue, subdataid)
    
    current_dataset_inserting_from.dump()    

    set_current_value_js  =   "$('#coltoinsertdtype').val('" + str(dtype) + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")

    set_current_value_js  =   "$('#currentcolnanval').val('" + str(nanvalue) + "');"
    run_jscript(set_current_value_js,"fail to change col stats html : ")
    
    #set_current_value_js  =   "$('#colstoinsert option:selected.text('" + str(colname) + "');"
    set_current_value_js  =   "$('#colstoinsert option[value=" + '"' + colname + '"]' + "').attr('selected', true);"
    print(set_current_value_js)
    run_jscript(set_current_value_js,"fail to change col stats html : ")


def change_census_df_to_insert_from(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the census df text  
    * 
    * Parms :
    *  parms - attributes
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    print("change_census_df_to_insert_from",parms)
    
    
    df_list         =   parms[0]
    df_selected     =   parms[1]
    #df_keys         =   parms[2]
    
    new_df_keys     =   []

    from dfcleanser.sw_utilities.sw_utility_census_model import get_index_keys_for_census_df
    selected_df_keys    =   get_index_keys_for_census_df(df_selected)
    
    if(not (df_selected == " ")) :
    
        df_list     =   df_selected
        new_df_keys =   selected_df_keys        
            
        set_current_value_js  =   "$('#censusdfstoload').val('" + str(df_list) + "');"
        run_jscript(set_current_value_js,"fail to change col stats html : ")

        set_current_value_js  =   "$('#userdfsindexkeys').val('" + str(new_df_keys) + "');"
        run_jscript(set_current_value_js,"fail to change col stats html : ")


def change_user_df_to_insert_into(parms)  :
    """
    * ---------------------------------------------------------
    * function : change the user df text 
    * 
    * Parms :
    *  parms - attributes
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    user_df_title   =   parms[0]
    user_df         =   cfg.get_dfc_dataframe_df(user_df_title)

    print("change_user_df_to_insert_into",parms)
  
  
def dfc_document_loaded(idtag) :
    
    from dfcleanser.system.system_model import set_document_loaded
    set_document_loaded()
    print("dfc_document_loaded")


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   end dfcleanser system dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
        
"""
#--------------------------------------------------------------------------
#    display apply fn working idlist
#--------------------------------------------------------------------------
""" 
add_cols_list_holder                 =   []

def get_add_col_list() :
    return(add_cols_list_holder)
def set_add_col_list(colslist) :
    global add_cols_list_holder
    add_cols_list_holder = colslist

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser scripting utility dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_script_exception(e) :
    """
    #--------------------------------------------------------------------------
    #   display a script exception
    #
    #       e    - exception
    #
    #--------------------------------------------------------------------------
    """ 
    from dfcleanser.scripting.data_scripting_widgets import exit_scripting_mode
    exit_scripting_mode()
    
    opstat = opStatus()
    opstat.store_exception("Scripting Exception",e)
    display_exception(opstat)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   html string helper methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""      

def replace_lt_gt(instr,ltchar="&lt;",gtchar="&gt;") :
    
    foundat = 0
    while(foundat > -1) :
        foundat = instr.find("<")
        if(foundat > -1) :
            instr = instr[0:foundat] + ltchar + instr[foundat+1:]

    foundat = 0
    while(foundat > -1) :
        foundat = instr.find(">")
        if(foundat > -1) :
            instr = instr[0:foundat] + gtchar + instr[foundat+1:]
    
    return(instr)


def replace_comma(instr) :
    """
    #------------------------------------------------------------------
    #   replace comma in string with new line
    #
    #   instr    -   input string
    #
    #------------------------------------------------------------------
    """      
    
    foundat = 0
    while(foundat > -1) :
        foundat = instr.find(",")
        if(foundat > -1) :
            instr = instr[0:foundat] + "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + instr[foundat+1:]
    
    return(instr)


def is_existing_column(df,colname) : 
    """
    #------------------------------------------------------------------
    #   check if colname is in df
    #
    #   df       -   dataframe
    #   colname  -   column name
    #
    #------------------------------------------------------------------
    """      
    
    df_cols = df.columns.tolist()
    
    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            return(True)

    return(False)


def single_quote(parm) :
    """
    #------------------------------------------------------------------
    #   enclose string in single quotes
    #
    #   parm  -   strng to enclose
    #
    #------------------------------------------------------------------
    """      

    return("'"+parm+"'")


def any_char_in_cols(df, schar, getvals):
    """
    #------------------------------------------------------------------
    #   chek if any char in cols
    #
    #   opstat   -   status object holding exception
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """      
    
    schar_in_cols = [[]]

    for k in range(len(df.columns)) :
        schar_in_cols.append([0,[]])
      
        for l in range(len(df)) : 
           
          if(schar in str(df.iloc[l,k])) :
              schar_in_cols[k][0] = schar_in_cols[k][0] + 1
              
              if(getvals) :
                  schar_in_cols[k][1].append(k)
                  
    return(schar_in_cols) 


def get_help_note_html(msg,width=None,left=None,msgid=None) :
    
    if(msgid is None) :
        mid = ""
    else :
        mid = msgid
    
    if(width is None) :
        notes_html   =   "<br><div id ='" + mid + "' style='text-align:center; border: 1px solid #67a1f3; font-color:#67a1f3; background-color:#F8F5E1;'><span style='color:#67a1f3;'>" + msg + "</span></div><br>"
    else :
        notes_html   =   "<br><div id ='" + mid + "' style='width:" + str(width) + "%; margin-left:" + str(left) + "px; text-align:center; border: 1px solid #67a1f3; font-color:#67a1f3; background-color:#F8F5E1;'><span style='color:#67a1f3;'>" + msg + "</span></div><br>"
    
    if(DUMP_HTML)  :
        print(notes_html)
    
    return(notes_html)

def get_help_note_warning_html(msg) :

    notes_html   =   "<br><div style='text-align:center;  width:90%; border: 1px solid #67a1f3; font-color:#67a1f3; background-color:#F8F5E1;'><span style='color:#ff0000;'>" + msg + "</span></div><br>"
    return(notes_html)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   system message helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""     
def display_exception(opstat,display=True) :
    """
    #------------------------------------------------------------------
    #   display a dfc exception
    #
    #   opstat   -   status object holding exception
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """      

    if(display) :
        
        import dfcleanser.common.cfg as cfg
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            #display_msgs(notes,"Notes :")
            error_html      =   display_msgs([opstat.get_errorMsg()],"Error :",color=False,margin=5,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [error_html]
    
            display_generic_grid("dfc-notes-wrapper",gridclasses,gridhtmls)
            
        else :
            
            error_html      =   display_msgs([opstat.get_errorMsg()],"Error :",color=False,margin=30,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [error_html]
    
            display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)
        
        if(not (opstat.get_exception() is None) ) :

            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
                #display_msgs(notes,"Notes :")
                error_html      =   get_exception_details(opstat)
                gridclasses     =   ["dfc-top-"]
                gridhtmls       =   [error_html]
    
                display_generic_grid("dfc-notes-wrapper",gridclasses,gridhtmls)
            
            else :
            
                error_html      =   get_exception_details(opstat) 
                gridclasses     =   ["dfc-top-"]
                gridhtmls       =   [error_html]
    
                display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)
    
    else :
        return(display_msgs([opstat.get_errorMsg(),get_exception_details(opstat)],"Error :",color=False,margin=30,helpmsg=False,display=False))



def get_exception_details(opstat) :
    """
    #------------------------------------------------------------------
    #   get exception details
    #
    #   opstat   -   status object holding exception
    #
    #------------------------------------------------------------------
    """      
    
    try :

        exception_html = ""
        exception_html = (exception_html + '<div class="container exception-status">' + new_line)
        exception_html = (exception_html + '    <div class="row">' + new_line)
        exception_html = (exception_html + '        <div class="panel panel-primary" style="border: 0px">' + new_line)

        if(not (opstat.get_systemRC0()) == None) :
            exception_html = (exception_html + '            <div class="exception-status-detail">' + new_line)
            exception_html = (exception_html + '                <p>' + "&nbsp;&nbsp;&nbsp;" + str(opstat.get_systemRC0().__name__) + '</p>' + new_line)
            exception_html = (exception_html + '            </div>' + new_line)
    
        if(not (opstat.get_systemRC1()) == None) :
        
            rcstring = str(opstat.get_systemRC1())
            rcstring = rcstring.replace(";","<br>&nbsp;&nbsp;&nbsp;")
            exception_html = (exception_html + '            <div class="exception-status-detail">' + new_line)
            exception_html = (exception_html + '                <p>' + "&nbsp;&nbsp;&nbsp;" + rcstring + '</p>' + new_line)
            exception_html = (exception_html + '            </div>' + new_line)
        
        exception_html = (exception_html + '        </div>' + new_line) 
        exception_html = (exception_html + '    </div>' + new_line) 
        exception_html = (exception_html + "</div>")
        
    except :
        
        exception_html  =   "  "
    
    return(exception_html)
    


def display_grid_status(msg) :
    """
    #------------------------------------------------------------------
    #   display status msgs in a grid
    #
    #   msg      -   msg
    #
    #------------------------------------------------------------------
    """      
    
    status_html     =   display_status(msg,False,False)    
    
    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [status_html]
    
    import dfcleanser.common.cfg as cfg
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)
        

def display_msgs(notes,text,color=False,margin=30,helpmsg=False,display=True) :
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   text     -   heading text
    #   color    -   display in color
    #   margin   -   left margin
    #   helpmsg  -   help msg flag
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """      
    
    notes_html = ""
    if(display) :
        notes_html = (notes_html + '<div class="container" style="width:80%; margin-left:' + str(margin) + 'px; border:1px;">' + new_line)
    else :
        notes_html = (notes_html + '<div class="container" style="width:80%; border:1px;">' + new_line)
        
    notes_html = (notes_html + '    <div class="row">' + new_line)
    if(color) :
        if(helpmsg) :
            notes_html = (notes_html + '        <div class="panel panel-primary" style="border:1px; background-color:#95C0FB;">' + new_line)
        else :
            notes_html = (notes_html + '        <div class="panel panel-primary" style="border:1px; background-color:#FAFB95;">' + new_line)
    else :
        notes_html = (notes_html + '        <div class="panel panel-primary" style="border:0px;  ">' + new_line)
    
    if(not (text == None)) :   
        notes_html = (notes_html + '            <div class="panel-heading dc-note-panel-heading" style="height:40px;">' + new_line)
        notes_html = (notes_html + '                <div class="input-group">' + new_line)
        notes_html = (notes_html + '                    <p class="dc-table-title" style="margin-bottom:5px; padding-bottom:5px; ">' + text +'</p>' + new_line)
        notes_html = (notes_html + '                </div>' + new_line) 
        notes_html = (notes_html + '            </div>' + new_line)
    
    
    notes_html = (notes_html + "        <div class='note-line'>" + new_line)
    notes_html = (notes_html + "            <p><span class='note-line' style='word-wrap:break-word;'></span></p>" + new_line)
    notes_html = (notes_html + "        </div>" + new_line)

    for i in range(len(notes)) :
        notes_html = (notes_html + "        <div class='note-line'>" + new_line)
        notes_html = (notes_html + "            <p><span class='note-line' style='word-wrap:break-word;'>" + notes[i] + "</span></p>" + new_line)
        notes_html = (notes_html + "        </div>" + new_line)
    
    notes_html = (notes_html + '        </div>' + new_line) 
    notes_html = (notes_html + '    </div>' + new_line) 
    notes_html = (notes_html + "</div>")
    
    from dfcleanser.common.common_utils import DUMP_HTML
    if(DUMP_HTML) :
        print(notes_html)
            
    if(display) :
        displayHTML(notes_html)
    else :
        return(notes_html)


def display_notes(notes,display=True) :
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """      
    
    if(display) :
        
        import dfcleanser.common.cfg as cfg
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            #display_msgs(notes,"Notes :")
            notes_html      =   display_msgs(notes,"Notes :",color=False,margin=5,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [notes_html]
    
            display_generic_grid("dfc-notes-wrapper",gridclasses,gridhtmls)
            
        else :
            
            notes_html      =   display_msgs(notes,"Notes :",color=False,margin=30,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [notes_html]
    
            display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)
            
    else :
        return(display_msgs(notes,"Notes :",color=False,margin=30,helpmsg=False,display=False))


def display_status_note(msg,full=True) :
    """
    #------------------------------------------------------------------
    #   display statys msg
    #
    #   notes    -   msg
    #   full     -   full width
    #
    #------------------------------------------------------------------
    """      
    
    notes_html   =   "<br><div style='text-align:center; border: 1px solid #67a1f3; font-color:#67a1f3; background-color:#F8F5E1;'><span style='color:#67a1f3;'>" + msg + "</span></div><br>"

    if(DUMP_HTML) :
        print(notes_html)
        
    gridclasses     =   ["dfc-top-"]
    gridhtmls       =   [notes_html]
    
    import dfcleanser.common.cfg as cfg
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :

        if( not (full)) :
            display_generic_grid("dfc-notes-short-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-notes-wrapper",gridclasses,gridhtmls)
            
    else :
            
        gridclasses     =   ["dfc-top-"]
        gridhtmls       =   [notes_html]
    
        display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)


def display_status(msg,short=False,display=True) :
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """      

    if(display) :
        
        import dfcleanser.common.cfg as cfg
        
        if( (cfg.get_dfc_mode() == cfg.INLINE_MODE) and (not(short)) ):
            
            #display_msgs(notes,"Notes :")
            status_html     =   display_msgs([msg],"Status :",color=False,margin=5,helpmsg=False,display=False) 
            
            if(DUMP_HTML) :
                print(status_html)
                
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [status_html]
    
            display_generic_grid("dfc-notes-wrapper",gridclasses,gridhtmls)
            
        else :
            
            status_html     =   display_msgs([msg],"Status :",color=False,margin=30,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [status_html]
    
            display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)
            
    else :
        return(display_msgs([msg],"Status :",color=False,margin=30,helpmsg=False,display=False))


def print_page_separator(title,divid) :
    
    style_name      =   "dfc-divider_" + str(divid)
    
    divider_cont    =   ("<div style='margin-left: 0px; width:95%;'>" + new_line) 
    divider1_html   =   ("        <style>" + new_line + "            hr." + style_name + " { " + new_line + "                overflow: visible; padding: 0; width: 90%; border: none; box-shadow: 0 0 10px 1px #296093; text-align: center;" + new_line + "            } " + new_line)
    divider2_html   =   ('            hr.' + style_name + ':after { ' + new_line + '                content: "' + title + '"; ')
    divider3_html   =   (" display: inline-block; position: relative; top: -0.7em; font-size: 24px; font-weight: bold;" + new_line + "                font-family: Arial; color: #236BAF; padding: 0 0.25em; background: white;" + new_line + "            }" + new_line + "        </style>" + new_line) 
    
    
    divider_start_html  =   ("    <hr class='" + style_name + "'>" + new_line + "    <div>" + new_line)
    divider_end_html    =   ("    </div>" + new_line + "</div>" + new_line + "<br>" + new_line)
    
    divider_html     =   (divider_cont + divider_start_html + divider1_html + divider2_html + divider3_html + divider_end_html) 
    
    from dfcleanser.common.common_utils import (displayHTML)
    displayHTML(divider_html)

    
def display_inline_help(helptext,margin=80) :
    display_msgs(helptext,"Help :",False,margin,True)    

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   operation status class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
class opStatus :

    # full constructor
    def __init__(self,    
                 status          =   True,
                 errorMsg        =   "",
                 systemRC0       =   None,
                 systemRC1       =   None,
                 trace           =   None,
                 exception       =   None) :
        
        # instance variables

        # minimum init attributes
        self.status          =   status
        self.errorMsg        =   errorMsg
        self.systemRC0       =   systemRC0
        self.systemRC1       =   systemRC1
        self.trace           =   trace
        self.exception       =   exception
      
    # class setters
    def set_status(self,statusParm) :
        self.status = statusParm
    def set_errorMsg(self,errorMsgParm) :
        self.errorMsg = errorMsgParm
    def set_systemRC0(self,systemRCParm) :
        self.systemRC0 = systemRCParm
    def set_systemRC1(self,systemRCParm) :
        self.systemRC1 = systemRCParm
    def set_trace(self,traceParm) :
        self.trace = traceParm
    def set_exception(self,exceptionParm) :
        self.exception = exceptionParm

    # class getters
    def get_status(self) :
        return(self.status)
    def get_errorMsg(self) :
        return(self.errorMsg)
    def get_systemRC0(self) :
        return(self.systemRC0)
    def get_systemRC1(self) :
        return(self.systemRC1)
    def get_trace(self) :
        return(self.trace)
    def get_exception(self) :
        return(self.exception)

    def store_exception(self,emsg,e) :
        self.status = False;
        self.errorMsg   = emsg
        import sys
        self.systemRC0  = sys.exc_info()[0]
        self.systemRC1  = sys.exc_info()[1]
        self.trace      = sys.exc_info()[2]
        self.exception  = sys.exc_info()



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    display grid helper components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

common_wrappers     =   ["data-import-stats-wrapper","data-import-wrapper","df-inspection-nan-wrapper",
                         "df-index-common-wrapper","col-change-datatype-transform-wrapper",
                         "dfc-common-480px-single-wrapper","dfc-common-480px-2-vert-wrapper",
                         "dfc-common-480px-3-vert-wrapper","dfc-transform-480px-3-vert-wrapper",
                         "display-df-apply-fn-wrapper"]

"""
<div class='dfcleanser-common-grid-header'>

  <div style="margin-top: 10px"  id="systemoptions">
    <div class="container dc-container dc-default-input-button-container btn-grp-center">
      <div class="btn-group btn-center"   style="width: 100%">
        <button type="button" class="btn btn-primary" style = 'margin-left: 2% ;  height: 50px ;  width: 12% ' onclick="process_system_tb_callback(1)">Utilities</br>Manager</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_system_tb_callback(3)">dataframe</br>Manager</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_system_tb_callback(4)">System</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_system_tb_callback(6)">About</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_system_tb_callback(12)">EULA</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_system_tb_callback(0)">Clear</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="process_pop_up_cmd(6)">Reset</button>
        <button type="button" class="btn btn-primary" style = 'height: 50px ;  width: 12% ' onclick="displayhelp(101)">Help</button>
      </div>
    </div>
  </div>
</div>
</div>
"""


wrapper_start   = """<div class='"""
wrapper_start1  = """'>
"""
wrapper_start1_pop_up  = """' style='background-color: #F8F5E1;'>
"""
wrapper_end     = """</div>"""


GRID_HEADER     =   0
GRID_LEFT       =   1
GRID_MAIN       =   2
GRID_RIGHT      =   3
GRID_FOOTER     =   4


def display_generic_grid(gridname,gridclasses,gridhtmls,pop_up=False) :
    
    gridHTML = ""
    from dfcleanser.common.html_widgets import new_line
    
    if(pop_up) :
        if(gridname in common_wrappers) :
            gridHTML = (gridHTML + wrapper_start + gridname + wrapper_start1_pop_up + new_line)
        else :
            gridHTML = (gridHTML + wrapper_start + gridname + wrapper_start1 + new_line)
    else :
        gridHTML = (gridHTML + wrapper_start + gridname + wrapper_start1 + new_line)
    
    for i in range(len(gridclasses)) :
        
        gridHTML = (gridHTML + "<div class='" + gridclasses[i] + "'>" + new_line)
        gridHTML = (gridHTML + gridhtmls[i] + new_line)
        gridHTML = (gridHTML + "</div>" + new_line)

    gridHTML = (gridHTML + wrapper_end + new_line)

    if(gridname == "#dfsubset-wrapper") :
        print(gridHTML)

    displayHTML(gridHTML)
    

"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Column uniques functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
    

"""            
#------------------------------------------------------------------
#   get a simple list of unique values for a column
#
#   return : list of unique vals
#
#   df              -   dataframe
#   columnName      -   column name 
#
#------------------------------------------------------------------
"""
def get_col_uniques(df, columnName)  :  
    try :
        return(df[columnName].unique())
    except :
        return(df[columnName])

"""            
#------------------------------------------------------------------
#   get a count of unique values in a column
#
#   return : number of unique vals
#
#   df              -   dataframe
#   columnName      -   column name 
#
#------------------------------------------------------------------
"""
def get_num_uniques(df, columnName)  :   

    return(len(df.columnName.unique()))
    
"""            
#------------------------------------------------------------------
#   get a count of unique values in a column
#
#   return : number of unique vals
#
#   df              -   dataframe
#   columnID        -   column name 
#
#------------------------------------------------------------------
"""
def get_col_num_uniques(df, columnName)  :   

    try :
        return(len(df[columnName].unique()))
    except :
        return(len(df))

        
"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Convert datatypes helper functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""    
  
           
def convert_df_cols_datatype(df,colnames,convdatatype,nafillValue=None) :
    """
    #------------------------------------------------------------------
    #   convert a list of dataframe columns to a speicific data type
    #
    #   df              -   dataframe
    #   colnames        -   list of colnames
    #
    #   convdatatype    -   datatype to convert columns to
    #                           int 
    #                           float
    #                           str
    #
    #   nafillvalue     -   fill value to be used for nas found
    #                       'mean' - indicates mean colulm value to fill nas
    #                       numeric value matching type of convdatatype
    #                       None - do not fill nas(default)
    #
    #------------------------------------------------------------------
    """      
    opstat = opStatus()
    
    for x in range(0,len(colnames)) :
        
        if(nafillValue != None) : 
            
            if(nafillValue == 'mean') : 
                cnafillValue = get_converted_value(df[colnames[x]].mean(),convdatatype,opstat)
            else :
                cnafillValue = get_converted_value(nafillValue,convdatatype,opstat)

            if(opstat.get_status()) :
                try :
                    df[colnames[x]] = df[colnames[x]].fillna(cnafillValue)
                    
                    df[colnames[x]] = df[colnames[x]].astype(get_datatype(convdatatype))
                except Exception as e: 
                    opstat.store_exception("Convert Data Type Error for column " + colnames[x],e)
                    
        else :
            try :
                df[colnames[x]] = df[colnames[x]].astype(get_datatype(convdatatype))
            except Exception as e: 
                opstat.store_exception("Convert Data Type Error for column " + colnames[x],e)
            
    return(opstat)



    
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   dfc cell files helpers
#------------------------------------------------------------------
#------------------------------------------------------------------
"""     
def get_common_dfcleanser_loc()  :

    import os
    import dfcleanser
    ppath = os.path.abspath(dfcleanser.__file__)
    #print("dfc path",dcfpath)   

    initpyloc = ppath.find("__init__.py")
    if(initpyloc > 0) :
        ppath = ppath[:initpyloc]

    return(ppath)
    
def get_dfc_cell_file(filename,opstat)  :

    dfcell_file_path = os.path.join(get_common_dfcleanser_loc() + "files\\cells",filename + ".txt") 

    try :
        cell_code = read_text_file(dfcell_file_path,opstat)
        if(cell_code == None) :
            display_exception(opstat)    
        return(cell_code)
        
    except Exception as e:
        opstat.store_exception("[get_cell_file][" + filename +"]",e)
        display_exception(opstat)
        
    return("no dfc cell for " + filename)
    
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   common file methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

import os
import json

def remove_files_from_dir(path,opstat) :

    os.chdir(path)
    
    for file_name in os.listdir(path) :
        try :
            os.remove(file_name)
        except FileNotFoundError as e:
            opstat.store_exception("File Not Found : " + "filename " + path + " " + file_name,e)
        except Exception as e:
            opstat.store_exception("remove filename " + path + " " + file_name,e)
    
    from dfcleanser.common.cfg import get_notebookPath
    os.chdir(get_notebookPath())

def delete_a_file(path,opstat) :

    try :
        os.remove(path)
    except FileNotFoundError as e:
        opstat.store_exception("File Not Found : " + "filename " + path,e)
    except Exception as e:
        opstat.store_exception("remove filename " + path,e)

def rename_a_file(oldname,newname,opstat) :

    try :
        os.rename(oldname,newname)
    except FileNotFoundError as e:
        opstat.store_exception("File Not Found : " + "filename " + oldname,e)
    except Exception as e:
        opstat.store_exception("rename filename " + oldname,e)
                        
def read_json_file(path,opstat) :
    
    json_data = {}
    
    if(os.path.isfile(path)) :
        try :
            with open(path,'r') as json_file :
                json_data = json.load(json_file)
                json_file.close()
                return(json_data)
        except Exception as e:
            opstat.store_exception("[error opening file][" + path +"]",e)
            
    return(None)
    
def write_json_file(path,json_data,opstat) :
    
    try :
        with open(path,'w') as json_file :
            json.dump(json_data,json_file)
            json_file.close()
    except Exception as e:
        opstat.store_exception("[error opening file][" + path +"]",e)

def read_text_file(path,opstat) :
    
    text_data = ""
    
    if(os.path.isfile(path)) :
        try :
            with open(path,'r') as text_file :
                text_data = text_file.read()
                text_file.close()
                return(text_data)
        except Exception as e:
            opstat.store_exception("[error opening file][" + path +"]",e)
            
    return(None)
    
def write_text_file(path,text_data,opstat) :
    
    try :
        with open(path,'w') as text_file :
            json.dump(text_data,text_file)
            text_file.close()
    except Exception as e:
        opstat.store_exception("[error opening file][" + path +"]",e)
 
def does_file_exist(path) :
    
    if(os.path.exists(path)) :
        if(os.path.isfile(path)) :   
            return(True)
        else :
            return(False)
    else :
        return(False)
    
def does_dir_exist(path) :
    
    if(os.path.exists(path)) :
        if(os.path.isdir(path)) :   
            return(True)
        else :
            return(False)
    else :
        return(False)
    
def make_dir(path) :
    
    try :
        os.mkdir(path)
        return(True)
    
    except FileExistsError:
        return(True)
    except :
        return(False)
        
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   common user notify methods
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def alert_user(text) :
    run_jscript('window.alert(' + '"' + text + '"' + ');',"fail to get datatime format strings : ")
    

NO_CFG_FILE_ID              =   1000
CORRUPTED_CFG_FILE_ID       =   1001
   
    
def confirm_user(text,confirmID) :
    run_jscript('displayconfirm(' + '"' + text + '",' + str(confirmID) + ');',"fail display confirm : ")
    
    
    
def handle_confirm(parms) :
    
    print("handle_confirm",parms)
    
    confirmID   =   int(parms[0])
    response    =   int(parms[1])
    
    if(confirmID == NO_CFG_FILE_ID) :
        if(response == 1) :
            alert_user("Blank default config file is loaded.")
        else :
            alert_user("Reset the Kernel and after completion Reset the dfcleanser notebook.")
    
    elif(confirmID == CORRUPTED_CFG_FILE_ID) :
        if(response == 1) :
            alert_user("The corrupted cfg file is renammed and a Blank default is loaded.")
        else :
            alert_user("Reset the Kernel and after completion Reset the dfcleanser notebook.")
    
    


"""
#--------------------------------------------------------------------------
#   static dfcleanser debug log
#--------------------------------------------------------------------------
"""


def log_debug_dfc(rowid,text) :
    dfc_debug_log.append([rowid,text])  
    
def clear_dfc_debug_log() :
    if(len(dfc_debug_log) > 0) :
        for i in range(len(dfc_debug_log)) :
            dfc_debug_log.pop()    
    
def dump_dfc_debug_log(index=None,text=None) :
    for i in range(len(dfc_debug_log)) :
        if(index == None) :
            if(text == None) :
                print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])
            else :
                if(dfc_debug_log[i][1].find(text) > -1) :
                    print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
                
        else :
            if(dfc_debug_log[i][0] == index) :
                if(text == None) :
                    print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])
                else :
                    if(dfc_debug_log[i][1].find(text) > -1) :
                        print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
            else :
                if(not (text == None) ) :
                    if(dfc_debug_log[i][1].find(text) > -1) :
                        print("rowid : ",dfc_debug_log[i][0],"  ",dfc_debug_log[i][1])    
                
    
    
dfc_debug_log  =   []



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfc image functionality
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

dfc_image_files     =   ["pandas.png","dataCleansing.png","dataImport.png","dataInspection.png","dataCleansing1.jpg","dataTransform.jpg","dataTransform.jpg","dataExport.png",
                         "Script.png","SWUtilities.png","ListBuild.png","dataframeSubset.png","GetLongLat.png","census.png","systemEnvironment.png","Restricted.jpg",
                         "leftarrow.png","rightarrow.png","uparrow.png","downarrow.png",
                         "Starting_State.png","Running_State.png","Stopped_State.png","Finished_State.png","Paused_State.png","Stopping_State.png",
                         "Pausing_State.png","Error_Limit_Exceeded_State.png","Checkpoint_Started_State.png","Checkpoint_Completed_State.png"]


def get_local_image_path(imagename) :
    
    #print("./PandasDataframeCleanser_files/graphics/" + imagename)
    return("./PandasDataframeCleanser_files/graphics/" + imagename)
    


"""
#--------------------------------------------------------------------------
#   dfc section titles
#--------------------------------------------------------------------------
"""

PANDAS_TITLE_IMAGE                  =   100
PANDAS_TITLE1_IMAGE                 =   101
IMPORT_TITLE_IMAGE                  =   102
INSPECT_TITLE_IMAGE                 =   103
CLEANSING_TITLE_IMAGE               =   104
TRANSFORM_TITLE_IMAGE               =   105
EXPORT_TITLE_IMAGE                  =   106
SCRIPTING_TITLE_IMAGE               =   107
SW_UTILS_TITLE_IMAGE                =   108
SW_UTILS_DS_TITLE_IMAGE             =   109
SW_UTILS_SUB_TITLE_IMAGE            =   110
SW_UTILS_GEOCODE_TITLE_IMAGE        =   111
SW_UTILS_ZIPCODE_TITLE_IMAGE        =   112
SW_UTILS_CENSUS_TITLE_IMAGE         =   113
SYSTEM_TITLE_IMAGE                  =   114
WORKING_TITLE_IMAGE                 =   115


PANDAS_TITLE_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/pandas.png"
PANDAS_TITLE1_SRC_URL               =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing.png"
IMPORT_TITLE_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataImport.png"
INSPECT_TITLE_SRC_URL               =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataInspection.png"
CLEANSING_TITLE_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataCleansing1.jpg" 
TRANSFORM_TITLE_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataTransform.jpg"
EXPORT_TITLE_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataExport.png"
SCRIPTING_TITLE_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/Script.png"
SW_UTILS_TITLE_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/SWUtilities.png"
SW_UTILS_DS_TITLE_SRC_URL           =   "https://rickkrasinski.github.io/dfcleanser/graphics/ListBuild.png"
SW_UTILS_SUB_TITLE_SRC_URL          =   "https://rickkrasinski.github.io/dfcleanser/graphics/dataframeSubset.png"
SW_UTILS_GEOCODE_TITLE_SRC_URL      =   "https://rickkrasinski.github.io/dfcleanser/graphics/GetLongLat.png"
SW_UTILS_ZIPCODE_TITLE_SRC_URL      =   "https://rickkrasinski.github.io/dfcleanser/graphics/zipcode.png"
SW_UTILS_CENSUS_TITLE_SRC_URL       =   "https://rickkrasinski.github.io/dfcleanser/graphics/census.png"
SYSTEM_TITLE_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/systemEnvironment.png"
WORKING_TITLE_SRC_URL               =   "https://rickkrasinski.github.io/dfcleanser/graphics/Restricted.jpg"

"""
#--------------------------------------------------------------------------
#   scrolling images
#--------------------------------------------------------------------------
"""

LEFT_ARROW_IMAGE            =   200
RIGHT_ARROW_IMAGE           =   201
UP_ARROW_IMAGE              =   202
DOWN_ARROW_IMAGE            =   203


LEFT_ARROW_SRC_URL          =   "https://rickkrasinski.github.io/dfcleanser/graphics/leftarrow.png"
RIGHT_ARROW_SRC_URL         =   "https://rickkrasinski.github.io/dfcleanser/graphics/rightarrow.png"
UP_ARROW_SRC_URL            =   "https://rickkrasinski.github.io/dfcleanser/graphics/uparrow.png"
DOWN_ARROW_SRC_URL          =   "https://rickkrasinski.github.io/dfcleanser/graphics/downarrow.png"


"""
#--------------------------------------------------------------------------
#   CLOCK images
#--------------------------------------------------------------------------
"""

HOUR_1_IMAGE                =   300
HOUR_2_IMAGE                =   301
HOUR_3_IMAGE                =   302
HOUR_4_IMAGE                =   303
HOUR_5_IMAGE                =   304
HOUR_6_IMAGE                =   305
HOUR_7_IMAGE                =   306
HOUR_8_IMAGE                =   307
HOUR_9_IMAGE                =   308
HOUR_10_IMAGE               =   309
HOUR_11_IMAGE               =   310
HOUR_12_IMAGE               =   311


HOUR_1_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour1.png"
HOUR_2_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour2.png"
HOUR_3_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour3.png"
HOUR_4_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour4.png"
HOUR_5_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour5.png"
HOUR_6_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour6.png"
HOUR_7_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour7.png"
HOUR_8_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour8.png"
HOUR_9_SRC_URL              =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour9.png"
HOUR_10_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour10.png"
HOUR_11_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour11.png"
HOUR_12_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/hour12.png"


"""
#--------------------------------------------------------------------------
#   geocoding images
#--------------------------------------------------------------------------
"""

GEOCODE_STARTING_IMAGE                 =   1000
GEOCODE_RUNNING_IMAGE                  =   1001
GEOCODE_STOPPED_IMAGE                  =   1002
GEOCODE_FINISHED_IMAGE                 =   1003
GEOCODE_PAUSED_IMAGE                   =   1004
GEOCODE_STOPPING_IMAGE                 =   1005
GEOCODE_PAUSING_IMAGE                  =   1006
GEOCODE_ERROR_LIMIT_IMAGE              =   1007
GEOCODE_CHECKPOINT_STARTED_IMAGE       =   1008
GEOCODE_CHECKPOINT_COMPLETE_IMAGE      =   1009

GEOCODE_STARTING_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/Starting_State.png"
GEOCODE_RUNNING_SRC_URL                 =   "https://rickkrasinski.github.io/dfcleanser/graphics/Running_State.png"
GEOCODE_STOPPED_SRC_URL                 =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopped_State.png"
GEOCODE_FINISHED_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/Finished_State.png"
GEOCODE_PAUSED_SRC_URL                  =   "https://rickkrasinski.github.io/dfcleanser/graphics/Paused_State.png"
GEOCODE_STOPPING_SRC_URL                =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopping_State.png"
GEOCODE_PAUSING_SRC_URL                 =   "https://rickkrasinski.github.io/dfcleanser/graphics/Pausing_State.png"
GEOCODE_ERROR_LIMIT_SRC_URL             =   "https://rickkrasinski.github.io/dfcleanser/graphics/Error_Limit_Exceeded_State.png"
GEOCODE_CHECKPOINT_STARTED_SRC_URL      =   "https://rickkrasinski.github.io/dfcleanser/graphics/Checkpoint_Started_State.png"
GEOCODE_CHECKPOINT_COMPLETE_SRC_URL     =   "https://rickkrasinski.github.io/dfcleanser/graphics/Checkpoint_Completed_State.png"


def copy_dfc_images_to_local() :
    
    import os
    #from shutil import copyfile
    
    from dfcleanser.common.cfg import get_notebookPath, get_notebookName
        
    notebook_path       =   get_notebookPath()
    notebook_name       =   get_notebookName()
        
    local_images_path   =   os.path.join(notebook_path + notebook_name + "_files","graphics")
        
    if(not (does_dir_exist(local_images_path))) : 
        make_dir(local_images_path)
    
    from sys import platform
    
    if (platform == "win32") :
        os.system('copy 1.txt.py 2.txt.py')
    else :
        os.system('cp 1.txt.py 2.txt.py')
    
    from dfcleanser.common.cfg import get_dfcleanser_location
        
    dfcleanser_path     =   get_dfcleanser_location()
    
    for i in range(len(dfc_image_files)) :

        dfc_file        =   os.path.join(dfcleanser_path,dfc_image_files[i])
        local_file      =   os.path.join(local_images_path,dfc_image_files[i])
        
        if (platform == "win32") :
            os.system('copy ' + dfc_file + " " + local_file)
        else :
            os.system('cp '  + dfc_file + " " + local_file)

def is_web_connected() :
    
    import urllib.request
    
    host='https://rickkrasinski.github.io/dfcleanser/graphics/pandas.png'
    
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        #print("web not connected")
        return False


def get_image_url(imageid) :
    
    url     =   ""
    
    if(imageid == PANDAS_TITLE_IMAGE)                   : url     =   PANDAS_TITLE_SRC_URL
    if(imageid == PANDAS_TITLE1_IMAGE)                  : url     =   PANDAS_TITLE1_SRC_URL
    elif(imageid == IMPORT_TITLE_IMAGE)                 : url     =   IMPORT_TITLE_SRC_URL
    elif(imageid == INSPECT_TITLE_IMAGE)                : url     =   INSPECT_TITLE_SRC_URL
    elif(imageid == CLEANSING_TITLE_IMAGE)              : url     =   CLEANSING_TITLE_SRC_URL
    elif(imageid == TRANSFORM_TITLE_IMAGE)              : url     =   TRANSFORM_TITLE_SRC_URL
    elif(imageid == EXPORT_TITLE_IMAGE)                 : url     =   EXPORT_TITLE_SRC_URL
    elif(imageid == SCRIPTING_TITLE_IMAGE)              : url     =   SCRIPTING_TITLE_SRC_URL
    elif(imageid == SW_UTILS_TITLE_IMAGE)               : url     =   SW_UTILS_TITLE_SRC_URL
    elif(imageid == SW_UTILS_DS_TITLE_IMAGE)            : url     =   SW_UTILS_DS_TITLE_SRC_URL
    elif(imageid == SW_UTILS_SUB_TITLE_IMAGE)           : url     =   SW_UTILS_SUB_TITLE_SRC_URL
    elif(imageid == SW_UTILS_GEOCODE_TITLE_IMAGE)       : url     =   SW_UTILS_GEOCODE_TITLE_SRC_URL
    elif(imageid == SW_UTILS_ZIPCODE_TITLE_IMAGE)       : url     =   SW_UTILS_ZIPCODE_TITLE_SRC_URL
    elif(imageid == SW_UTILS_CENSUS_TITLE_IMAGE)        : url     =   SW_UTILS_CENSUS_TITLE_SRC_URL
    elif(imageid == SYSTEM_TITLE_IMAGE)                 : url     =   SYSTEM_TITLE_SRC_URL
    elif(imageid == WORKING_TITLE_IMAGE)                : url     =   WORKING_TITLE_SRC_URL
    elif(imageid == LEFT_ARROW_IMAGE)                   : url     =   LEFT_ARROW_SRC_URL
    elif(imageid == RIGHT_ARROW_IMAGE)                  : url     =   RIGHT_ARROW_SRC_URL
    elif(imageid == UP_ARROW_IMAGE)                     : url     =   UP_ARROW_SRC_URL
    elif(imageid == DOWN_ARROW_IMAGE)                   : url     =   DOWN_ARROW_SRC_URL
    elif(imageid == GEOCODE_STARTING_IMAGE)             : url     =   GEOCODE_STARTING_SRC_URL
    elif(imageid == GEOCODE_RUNNING_IMAGE)              : url     =   GEOCODE_RUNNING_SRC_URL
    elif(imageid == GEOCODE_STOPPED_IMAGE)              : url     =   GEOCODE_STOPPED_SRC_URL
    elif(imageid == GEOCODE_FINISHED_IMAGE)             : url     =   GEOCODE_FINISHED_SRC_URL
    elif(imageid == GEOCODE_PAUSED_IMAGE)               : url     =   GEOCODE_PAUSED_SRC_URL
    elif(imageid == GEOCODE_STOPPING_IMAGE)             : url     =   GEOCODE_STOPPING_SRC_URL
    elif(imageid == GEOCODE_PAUSING_IMAGE)              : url     =   GEOCODE_PAUSING_SRC_URL
    elif(imageid == GEOCODE_ERROR_LIMIT_IMAGE)          : url     =   GEOCODE_ERROR_LIMIT_SRC_URL
    elif(imageid == GEOCODE_CHECKPOINT_STARTED_IMAGE)   : url     =   GEOCODE_CHECKPOINT_STARTED_SRC_URL
    elif(imageid == GEOCODE_CHECKPOINT_COMPLETE_IMAGE)  : url     =   GEOCODE_CHECKPOINT_COMPLETE_SRC_URL
    elif(imageid == HOUR_1_IMAGE)                       : url     =   HOUR_1_SRC_URL
    elif(imageid == HOUR_2_IMAGE)                       : url     =   HOUR_2_SRC_URL
    elif(imageid == HOUR_3_IMAGE)                       : url     =   HOUR_3_SRC_URL
    elif(imageid == HOUR_4_IMAGE)                       : url     =   HOUR_4_SRC_URL
    elif(imageid == HOUR_5_IMAGE)                       : url     =   HOUR_5_SRC_URL
    elif(imageid == HOUR_6_IMAGE)                       : url     =   HOUR_6_SRC_URL
    elif(imageid == HOUR_7_IMAGE)                       : url     =   HOUR_7_SRC_URL
    elif(imageid == HOUR_8_IMAGE)                       : url     =   HOUR_8_SRC_URL
    elif(imageid == HOUR_9_IMAGE)                       : url     =   HOUR_9_SRC_URL
    elif(imageid == HOUR_10_IMAGE)                      : url     =   HOUR_10_SRC_URL
    elif(imageid == HOUR_11_IMAGE)                      : url     =   HOUR_11_SRC_URL
    elif(imageid == HOUR_12_IMAGE)                      : url     =   HOUR_12_SRC_URL
 
    import datetime 
    tstamp = datetime.datetime.now().time()
    
    image   =   url + "?timestamp=" + str(tstamp)
    
    return(image)















 
