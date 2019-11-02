""
# dfc_common_utils 

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.common.cfg import (DataTransform_ID, get_dfc_dataframe_df)

import dfcleanser.common.table_widgets as tblw         
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
        while 1: 
            #for cursor in '|/-\\': yield cursor
            clockfaces =    ["https://rickkrasinski.github.io/dfcleanser/graphics/hour1.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour2.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour3.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour4.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour5.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour6.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour7.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour8.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour9.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour10.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour11.png",
                             "https://rickkrasinski.github.io/dfcleanser/graphics/hour12.png"]
            
            for clockface in clockfaces : yield clockface

    def __init__(self, delay=None):
        self.clock_generator = self.spinning_clock()
        
        self.image_html = (self.image_html + '<div class="container" id="clockcontainer" style=" width:60px; height:60px; margin-left:20px; ">')
        self.image_html = (self.image_html + '    <img id="clockrunner" src="https://rickkrasinski.github.io/dfcleanser/graphics/hour12.png" height="60" width="60"></img>' + "</div>")
        
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
import pandas.api.types as pat

def get_column_datatype(df,colname) :
    
    try :
        return(df[colname].dtype)
    except :
        return(None)

def is_numeric_col(df,colname) :

    datatype   =   get_column_datatype(df,colname)

    if(not (datatype is None)) :
        return(pat.is_numeric_dtype(datatype)) 
    else :
        return(False)

def is_int_col(df,colname) :

    datatype   =   get_column_datatype(df,colname)

    if(not (datatype is None)) :
        return(pat.is_integer_dtype(datatype)) 
    else :
        return(False)

def is_float_col(df,colname) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_float_dtype(datatype)) 
    else :
        return(False)

def is_string_col(df,colname) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_string_dtype(datatype))
    else :
        return(False)

def is_object_col(df,colname) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_object_dtype(datatype))
    else :
        return(False)

def is_bool_col(df,colname) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_bool_dtype(datatype))
    else :
        return(False)

def is_categorical_col(df,colname) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_categorical_dtype(datatype))
    else :
        return(False)

def is_datetime64_col(df,colname,anydatetime64=False) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        
        if(anydatetime64) :
            return(pat.is_datetime64_any_dtype(datatype)) 
        else :
            return(pat.is_datetime64_dtype(datatype))
    else :
        return(False)

def is_timedelta64_col(df,colname,anydatetime64=False) :
    
    datatype   =   get_column_datatype(df,colname)
    
    if(not (datatype is None)) :
        return(pat.is_timedelta64_dtype(datatype)) 
    else :
        return(False)

def is_timestamp_col(df,colname) :
    
    import pandas as pd
    if(get_column_datatype(df,colname) == pd.Timestamp) :
        return(True)
    else :
        return(False)

def is_datetime_col(df,colname) :
    
    import datetime
    if(get_column_datatype(df,colname) == datetime.datetime) :
        return(True)
    else :
        return(False)

def is_date_col(df,colname) :
    
    import datetime
    if(get_column_datatype(df,colname) == datetime.date) :
        return(True)
    else :
        return(False)

def is_time_col(df,colname) :
    
    import datetime
    if(get_column_datatype(df,colname) == datetime.time) :
        return(True)
    else :
        return(False)
    
def is_timedelta_col(df,colname) :
    
    import datetime
    if(get_column_datatype(df,colname) == datetime.timedelta) :
        return(True)
    else :
        return(False)
    
def is_datetime_type_col(df,colname) :
    
    if( (is_datetime_col(df,colname)) or (is_date_col(df,colname)) or
        (is_time_col(df,colname)) or (is_timedelta_col(df,colname)) ) :
        return(True)
    else :
        return(False)
  

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser datatype helper methods for listing and displays
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
""" 
def get_datatype(dtypeid) :
    
    import numpy
    import datetime
    import pandas
    
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
    

def is_numeric_datatype_id(dtypeId) :
    
    if((dtypeId == 0) or (dtypeId == 1) or (dtypeId == 2) or (dtypeId == 3) or 
       (dtypeId == 4) or (dtypeId == 5) or (dtypeId == 6) or (dtypeId == 7) or 
       (dtypeId == 8) or (dtypeId == 9) or (dtypeId == 10) or (dtypeId == 17) or 
       (dtypeId == 18))  : 
        return(True)
    else :
        return(False)        

def is_integer_datatype_id(dtypeId) :
    
    if((dtypeId == 0) or (dtypeId == 1) or (dtypeId == 2) or (dtypeId == 3) or 
       (dtypeId == 4) or (dtypeId == 5) or (dtypeId == 6) or (dtypeId == 7) or 
       (dtypeId == 17) )  : 
        return(True)
    else :
        return(False)        

def is_datetime_datatype_id(dtypeId) :
    
    if((dtypeId == 11) or (dtypeId == 12) or (dtypeId == 13) or (dtypeId == 14) )  : 
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

def get_datatype_str(dt_id) :

    if(dt_id == 0)      : return("numpy.uint8")
    elif(dt_id == 1)    : return("numpy.uint16")
    elif(dt_id == 2)    : return("numpy.uint32")
    elif(dt_id == 3)    : return("numpy.uint64")
    elif(dt_id == 4)    : return("numpy.int8")
    elif(dt_id == 5)    : return("numpy.int16")
    elif(dt_id == 6)    : return("numpy.int32")
    elif(dt_id == 7)    : return("numpy.int64")
    elif(dt_id == 8)    : return("numpy.float16")
    elif(dt_id == 9)    : return("numpy.float32")
    elif(dt_id == 10)   : return("numpy.float64")
    elif(dt_id == 11)   : return("datetime.datetime")
    elif(dt_id == 12)   : return("datetime.date")
    elif(dt_id == 13)   : return("datetime.time")
    elif(dt_id == 14)   : return("datetime.timedelta")
    elif(dt_id == 15)   : return("str")
    elif(dt_id == 16)   : return("object")
    elif(dt_id == 17)   : return("int")
    elif(dt_id == 18)   : return("float")
    elif(dt_id == 19)   : return("category")
    elif(dt_id == 20)   : return("numpy.datetime64")
    elif(dt_id == 21)   : return("numpy.timedelta64")
    
    return("unknown")


def get_datatype_id_from_str(dt_str) :

    if(dt_str == "numpy.uint8")             :   return(0)
    elif(dt_str == "numpy.uint16")          :   return(1)
    elif(dt_str == "numpy.uint32")          :   return(2)
    elif(dt_str == "numpy.uint64")          :   return(3)
    elif(dt_str == "numpy.int8")            :   return(4)
    elif(dt_str == "numpy.int16")           :   return(5)
    elif(dt_str == "numpy.int32")           :   return(6)
    elif(dt_str == "numpy.int64")           :   return(7)
    elif(dt_str == "numpy.float16")         :   return(8)
    elif(dt_str == "numpy.float32")         :   return(9)
    elif(dt_str == "numpy.float64")         :   return(10)
    elif(dt_str == "datetime.datetime")     :   return(11)
    elif(dt_str == "datetime.date")         :   return(12)
    elif(dt_str == "datetime.time")         :   return(13)
    elif(dt_str == "datetime.timedelta")    :   return(14)
    elif(dt_str == "str")                   :   return(15)
    elif(dt_str == "object")                :   return(16)
    elif(dt_str == "int")                   :   return(17)
    elif(dt_str == "float")                 :   return(18)
    elif(dt_str == "category")              :   return(19)
    elif(dt_str == "numpy.datetime64")      :   return(20)
    elif(dt_str == "numpy.timedelta64")     :   return(21)

    return(None)


def get_datatypes_list(full=True) :
    
    if(full) :
        
        dtlist  =   ["numpy.uint8","numpy.uint16","numpy.uint32","numpy.uint64",
                     "numpy.int8","numpy.int16","numpy.int32","numpy.int64",
                     "numpy.float16","numpy.float32","numpy.float64","datetime.datetime",
                     "datetime.date","datetime.time","datetime.timedelta","str",
                     "object","int","float","category","numpy.datetime64","numpy.timedelta64"]
        
    else :
        
        dtlist  =   ["uint8","uint16","uint32","uint64",
                     "int8","int16","int32","int64",
                     "float16","float32","float64","datetime.datetime",
                     "datetime.date","datetime.time","datetime.timedelta","str",
                     "object","int","float","category","datetime64","timedelta64"]
        
    
    return(dtlist)


"""
#--------------------------------------------------------------------------
#   Datatype helper methods
#--------------------------------------------------------------------------
"""

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

    
    try :
        
        if( (parms == None) or (ids == None) or 
           ((len(parms) == 0) or (len(ids) == 0)) ) :
            return(outparms)
    
        #print("get_parms_for_input : parms",len(parms),parms) 
        #print("get_parms_for_input : ids  ",len(ids),ids) 
        
        if(type(parms) == str) :
            import json
            inparms = json.loads(parms)
        else :
            inparms = parms
            
    except :
        print("get_parms_for_input invalid input parms")
    
    #print("get_parms_for_input : inparms  ",inparms) 
    
    try :
        
        if(len(inparms[0]) == 0) :
            return(outparms)
        
        for i in range(len(ids)) :
            if(ids[i] != None):
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

    #print("\nget_select_defaults\n",selectDicts)
    
    numselects  =   0
    
    for i in range(len(parmids)) :
        
        if( (parmtypes[i] == "select") or (parmtypes[i] == "selectmultiple") ):
            form.add_select_dict(formid,
                                 parmids,
                                 parmids[i],
                                 selectDicts[numselects])
            
            numselects  =   numselects + 1

 
def displayParms(title,labels,values,tblid,width=None,leftMargin=0,display=True,font=None) :
    """
    #--------------------------------------------------------------------------
    #   display a list of parms as a table
    #
    #       title  - parms title 
    #       labels - parm labels
    #       values - parm values
    #       id     - table id
    #       width  - fixed table width in pixels
    #
    #   return table of parms
    #
    #--------------------------------------------------------------------------
    """ 

    maxllabels      =   0
    maxlvalues      =   0

    if( not ( (len(labels)>0) and (len(labels) == len(values)) ) ) :
        return("<p>Invalid Parameter List</p>")
        
    for i in range(len(labels)) :
        if(len(labels[i])>maxllabels) :
            maxllabels = len(labels[i])
            
    for i in range(len(values)) :
        if(len(values[i])>maxlvalues) :
            
            # check for line breaks
            if("<br/>" in values[i]) :
                #print("line break in parm")
                nextlinebreak   =   0
                lastlinebreak   =   0
                totcount = 0
                while ( (nextlinebreak != -1) and (totcount < 10)) :
                    
                    totcount = totcount + 1
                    nextlinebreak = values[i][lastlinebreak:].find("<br/>")  
                    if(nextlinebreak != -1) :
                         if( (nextlinebreak + len("<br/>") > maxlvalues) ) :
                            maxlvalues = (nextlinebreak + len("<br/>"))
                         lastlinebreak = lastlinebreak + nextlinebreak + len("<br/>")
    
            else :
                maxlvalues = len(values[i])
                
    #print("displayParms",maxllabels,maxlvalues)
    
    if(display) :      
        print("\n")        
    
    import math
    labelwidth = int(math.ceil((maxllabels / (maxllabels + maxlvalues)) * 100)) 
    if(labelwidth < 20) :
        labelwidth  =   20
    
    valuewidth = (100 - 4) - labelwidth
    
    if( (len(labels) == 1) and (len(labels[0]) == 1) ) :
        parmsWidths    =   [1,labelwidth,1,valuewidth+4]
    else :
        parmsWidths    =   [1,labelwidth,3,valuewidth]
    parmsAligns    =   ["center","left","center","left"]
    
    colorList = []    
    
    parmsRows      =   []
    
    for i in range(len(labels)) : 
        if( (len(labels[i]) > 0) and (len(values[i]) > 0) ) :
            if( (len(labels) == 1) and (len(labels[0]) == 1) ) :
                parmsRows.append([" ",labels[i]," ",values[i]]) 
            else :
                parmsRows.append([" ",labels[i],"<b>:</b>",values[i]])
            colorList.append([whitecolor,whitecolor,whitecolor,whitecolor])
    
    parmsHeader    =   ["","","",""]
    parms_table = tblw.dcTable(title,"parmsTable",tblid,
                               parmsHeader,parmsRows,parmsWidths,parmsAligns)

    parms_table.set_rowspertable(len(labels))
    parms_table.set_small(True)
    
    if(not (width is None)) :
        parms_table.set_smallwidth(width)

    parms_table.set_smallmargin(leftMargin)
    parms_table.set_border(False)
    parms_table.set_checkLength(False)
    if(not(font is None)) :
        parms_table.set_table_column_parms({"font":font})

    if(display) :
        parms_table.display_table()
    else :
        return(parms_table.get_html())
        

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
def get_scroll_table_html(tableid,direction) :
    """
    * ---------------------------------------------------------
    * function : get a scrolled dc table html
    * 
    * Parms :
    *  tableid    - table id
    *  direction  - scroll direction
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    #print("get_scroll_table_html",tableid,direction,tblw.get_table_value(tableid).get_tabletype())
    
    if(tblw.get_table_value(tableid).get_tabletype() == tblw.ROW_MAJOR) : 
         table_html = tblw.get_row_major_table(tblw.get_table_value(tableid),direction,False)
    
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) : 
        tblw.scroll_col_major_table(tblw.get_table_value(tableid),direction)
        return(None)
    
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw.ROW_COL_MAJOR) : 
        #print("ROW_COL_MAJOR",tblw.get_table_value(tableid),direction)
         #table_html = tblw.get_row_major_table(tblw.get_table_value(tableid),direction,False)
        return(None)
        
    else :
        return(None)

    if(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) :
        
        print("COLUMN_MAJOR")
        tablehtmlloc    = table_html.find("<thead")
        tableendhtmlloc = table_html.find("</tbody>")
        table_html = table_html[tablehtmlloc:tableendhtmlloc+len("</tbody>")]
        
    else :
        # check for no header tables
        if(table_html.find("<thead") == -1) :
            tablehtmlloc    = table_html.find("<tbody")
            table_html      = table_html[tablehtmlloc + len("<tbody"):]
            
            tablehtmlloc    = table_html.find("<tbody>")
            table_html      = table_html[tablehtmlloc:]
            
            tableendhtmlloc = table_html.find("</tbody>")
        
            table_html = table_html[tablehtmlloc:tableendhtmlloc+len("</tbody>")]
        
    new_table_html = patch_html(table_html)
    
    return(new_table_html)


def refresh_scroll_buttons(tableid) :
    
    buttons     =   ["downarrow","uparrow","leftarrow","rightarrow"]
    
    import datetime 
    tstamp = datetime.datetime.now().time()
    
    for i in range(len(buttons)) :
        
        button_id       =   tableid + buttons[i] + "Id"
        
        change_html     =   ("'#" + button_id + "').attr('src'," + 
                             "'https://rickkrasinski.github.io/dfcleanser/graphics/" + buttons[i] + ".png?timestamp=" + str(tstamp) + "'")
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

         
def scroll_sample_rows(parms) :
    """
    * ---------------------------------------------------------
    * function : scroll the sample table
    * 
    * Parms :
    *  parms[0]    - table id
    *  parms[1]    - scroll direction
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    tableid     =   parms[0]
    direction   =   int(parms[1])
    
    #print("scroll_sample_rows",tableid,direction)
    
    from dfcleanser.common.display_utils import display_more_sample_rows
    df_delim    =   tableid.find("_search_")
    if(df_delim > -1) :
        df_title  =   tableid[:df_delim]
    else :
        from dfcleanser.common.cfg import get_config_value,CURRENT_INSPECTION_DF
        if(tableid == "DIsamplerows") :
            df_title    =   get_config_value(CURRENT_INSPECTION_DF)
        else :
            df_title  =   None
    
    #print("df_title",df_title)
    
    table_html = display_more_sample_rows(get_dfc_dataframe_df(df_title),tableid,direction)
    
    #print("table_html",table_html)    
    
    thead = table_html.find("<thead>")
    table_html = table_html[thead:]
    tend  = table_html.find("</table>")
    table_html = table_html[0:(tend-1)]
    
    new_table_html = patch_html(table_html)

    change_table_js = "$("
    change_table_js = change_table_js + "'#" + tableid + "').html('"
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))

    refresh_bg_js = "$('#" + tableid + "_thr').css({'background-color':'#6FA6DA'});"
    #print("refresh_bg_js",refresh_bg_js)
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))
    
    refresh_bg_js = "$('#" + tableid + "_thr').css({'color':'white'});"
    #print("refresh_bg_js",refresh_bg_js)
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))
    
    return


def get_sample_row(parms) :
    """
    * ---------------------------------------------------------
    * function : get a sample row for df browser
    * 
    * Parms :
    *  parms[0]    - table id
    *  parms[1]    - row id
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    tableId     =   parms[0][0]
    newrowId    =   int(parms[0][1])
        
    from dfcleanser.common.display_utils import display_more_sample_rows
    new_rows_html = display_more_sample_rows(get_dfc_dataframe_df(),
                                             tableId,1,newrowId,opstat)

    table_html = patch_html(new_rows_html)
    
    thead = table_html.find("<thead>")
    tend  = table_html.find("</table>")
    
    table_html = table_html[thead:(tend-1)]
    
    new_table_html = patch_html(table_html)

    change_table_js = "$("
    change_table_js = change_table_js + "'#" + tableId + "').html('"
    change_table_js = change_table_js + new_table_html + "');"

    run_jscript(change_table_js,"fail get_sample_row parms : "+tableId)
    

def scroll_single_row(parms) :
    """
    * ---------------------------------------------------------
    * function : get a simgle row for df browser
    * 
    * Parms :
    *  parms[0]    - table id
    *  parms[1]    - scroll direction
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    tableid     =   parms[0]
    direction   =   int(parms[1])
    
    from dfcleanser.common.display_utils import display_more_single_row
    table_html = display_more_single_row(get_dfc_dataframe_df(),tableid,direction)
    
    thead = table_html.find("<tbody>")
    tend  = table_html.find("</tbody>")
    
    table_html = table_html[thead:(tend-1)]
    
    new_table_html = patch_html(table_html)

    change_table_js = "$("
    change_table_js = change_table_js + "'#" + tableid + "').html('"
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_single_row : " + tableid + str(direction))


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
    
        import datetime 
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
 

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data inspection dynamic html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_df_browser_search_html(colname) :
    """
    * ---------------------------------------------------------
    * function : get column samples
    * 
    * Parms :
    *  colname    - column name
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    print("get_df_browser_search_html")

def get_df_browser_search(numeric) :
    """
    * ---------------------------------------------------------
    * function : get column samples
    * 
    * Parms :
    *  numeric    - search for numeric values
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    #print("get_df_browser_search",numeric,type(numeric))
    
    if(numeric == 1) :
        num_flag    =   False
    else :
        num_flag    =   True
    
    import dfcleanser.common.cfg as cfg
    from dfcleanser.data_inspection.data_inspection_widgets import get_colsearch_form
    new_html    =   get_colsearch_form(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                       num_flag).get_html()
    
    start_html  =   new_html.find("<div class='container' style='padding:5px; margin:auto; width:100%;'  id="+'"datainspectcolsearchinput">')
    
    #end_html    =   new_html.find('<div style="margin-top:10px;"  id="datainspectcolsearchtb">')
    end_html    =   len(new_html) - 6
    
    #print("\n\nget_df_browser_search",len(new_html),start_html,end_html,"\n",new_html)
    
    new_html    =   new_html[start_html:end_html-7]
    new_html    =   new_html.replace("'",'"')
    new_html    =   new_html.replace('("colsearchnames"',"('colsearchnames'")
    
    final_html  =   patch_html(new_html)

    change_table_js = "$('#datainspectcolsearch').html('"
    change_table_js = change_table_js + final_html + "');"
            
    run_jscript(change_table_js,"fail to get search df html : ")


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data transform html methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def change_col_stats(parms)  :
    
    selectid    =   parms[0]
    colid       =   parms[1]
    
    print("change_col_stats",parms,selectid,colid)
    
    import dfcleanser.common.cfg as cfg
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
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
        
        if(len(keyslist) > 300) :
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


def get_column_samples_html(colname) :
    """
    * ---------------------------------------------------------
    * function : get column samples
    * 
    * Parms :
    *  colname    - column name
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    columnsamplesHeader      =   [""]

    columnsamplesRows        =   []
    columnsamplesWidths      =   [100]
    columnsamplesAligns      =   ["left"]
    columnsamplesHrefs       =   []
    
    uniques =   [] 
        
    #check if the object is string
    if (isinstance(get_dfc_dataframe_df()[colname][0], str)) :
        
        uniques =   get_dfc_dataframe_df()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        if(is_numeric_col(get_dfc_dataframe_df(),colname)) :           
            uniques =   get_dfc_dataframe_df()[colname].unique().tolist()
            uniques.sort()

    if(len(uniques) > 0) :

        if(len(uniques) > 3) :
            count = 3
        else :
            count = len(uniques)
            
        for i in range(count) :
            columnsamplesRows.append([str(uniques[i])])
            columnsamplesHrefs.append([None])

    else : 
        columnsamplesRows.append([str(colname)])
        columnsamplesHrefs.append([None])
        columnsamplesRows.append([" Unique Values not listable: "])
        columnsamplesHrefs.append([None])
        
    columnsamples_table = None

    columnsamples_table = tblw.dcTable("Column Samples",
                                       "datetimecolnamesTable",DataTransform_ID,
                                       columnsamplesHeader,columnsamplesRows,
                                       columnsamplesWidths,columnsamplesAligns)
    
    columnsamples_table.set_refList(columnsamplesHrefs)

    columnsamples_table.set_small(True)
    columnsamples_table.set_smallwidth(98)
    columnsamples_table.set_smallmargin(10)

    columnsamples_table.set_border(True)
        
    columnsamples_table.set_checkLength(True)
            
    columnsamples_table.set_textLength(30)
    columnsamples_table.set_html_only(True) 
    
    columnsamples_table.set_tabletype(tblw.ROW_MAJOR)
    columnsamples_table.set_rowspertable(14)

    tablehtml = tblw.get_row_major_table(columnsamples_table,tblw.SCROLL_DOWN,False)


    
    startinner = tablehtml.find('<div class="row">')
    endinner    =   len(tablehtml) - 7
    
    return(tablehtml[startinner:endinner])


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
    print("get_column_samples",parms,colname)
    cols_html   =   get_column_samples_html(colname) 
    #print("cols_html",cols_html)
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
        df          =   cfg.get_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_INSPECTION_DF))
        
    dfc_temp_path       =   os.path.join(cfg.get_dfcleanser_location(),"files","temp")
    dfc_temp_path       =   (dfc_temp_path + "\\exceldfs\\")
        
    try :
            
        tmp_name    =   dfc_temp_path + cfg.get_config_value(cfg.CURRENT_INSPECTION_DF) + "_temp.csv"
        df.to_csv(tmp_name, index=False)
        os.startfile(tmp_name)    
    
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
     
    from dfcleanser.common.cfg import get_dfc_dataframe_df
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
def get_datatype_title(dt_id) :
    return("&#60;" + get_datatype_str(dt_id) + "&#62;")


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
    
    #print(exception_html)
    #from IPython.display import HTML
    #from IPython.display import display
    
    #if(display) :
    #    display_jupyter_HTML(HTML(exception_html))
    #else :
    #    return(exception_html)


def display_grid_status(msg) :
    """
    #------------------------------------------------------------------
    #   display status msgs in a grid
    #
    #   msg      -   msg
    #
    #------------------------------------------------------------------
    """      
    
    status_html     =   display_status(msg,False)    
    
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
        notes_html = (notes_html + '            <div class="panel-heading dc-table-panel-heading" style="height:40px;">' + new_line)
        notes_html = (notes_html + '                <div class="input-group">' + new_line)
        notes_html = (notes_html + '                    <p class="dc-table-title" style="margin-bottom:5px; padding-bottom:5px;">' + text +'</p>' + new_line)
        notes_html = (notes_html + '                </div>' + new_line) 
        notes_html = (notes_html + '            </div>' + new_line)
    
    
    notes_html = (notes_html + "        <div class='note-line'>" + new_line)
    notes_html = (notes_html + "            <p><span class='note-line'></span></p>" + new_line)
    notes_html = (notes_html + "        </div>" + new_line)

    for i in range(len(notes)) :
        notes_html = (notes_html + "        <div class='note-line'>" + new_line)
        notes_html = (notes_html + "            <p><span class='note-line'>" + notes[i] + "</span></p>" + new_line)
        notes_html = (notes_html + "        </div>" + new_line)
    
    notes_html = (notes_html + '        </div>' + new_line) 
    notes_html = (notes_html + '    </div>' + new_line) 
    notes_html = (notes_html + "</div>")
    
    #print(notes_html)
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


def display_status(msg,display=True) :
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
            status_html     =   display_msgs([msg],"Status :",color=False,margin=5,helpmsg=False,display=False) 
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
wrapper_start   = """<div class='"""
wrapper_start1  = """'>
"""

wrapper_end     = """</div>"""


GRID_HEADER     =   0
GRID_LEFT       =   1
GRID_MAIN       =   2
GRID_RIGHT      =   3
GRID_FOOTER     =   4


def display_generic_grid(gridname,gridclasses,gridhtmls) :
    
    gridHTML = ""
    from dfcleanser.common.html_widgets import new_line
    gridHTML = (gridHTML + wrapper_start + gridname + wrapper_start1 + new_line)
    
    for i in range(len(gridclasses)) :
        
        gridHTML = (gridHTML + "<div class='" + gridclasses[i] + "'>" + new_line)
        gridHTML = (gridHTML + gridhtmls[i] + new_line)
        gridHTML = (gridHTML + "</div>" + new_line)

    gridHTML = (gridHTML + wrapper_end + new_line)

    if(gridname == "#dfsubset-wrapper") :
        print(gridHTML)
    #print(gridHTML)
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

def convert_nafill_value(nafillValue,dtype,opstat):
    """
    #------------------------------------------------------------------
    #   convert a nafill value to a speicific data type
    #
    #   nafillvalue     -   fill value to be used for nas found
    #
    #   dtype           -   datatype to convert value to
    #
    #   opstat          -   status parm
    #
    #------------------------------------------------------------------
    """      
    import numpy as np
    import datetime
    import pandas

    cnafillValue    = None

    try :
        
       if(dtype == 0)       : cnafillValue = np.uint8(nafillValue)
       elif(dtype == 1)     : cnafillValue = np.uint16(nafillValue)        
       elif(dtype == 2)     : cnafillValue = np.uint32(nafillValue)        
       elif(dtype == 3)     : cnafillValue = np.uint64(nafillValue)        
       elif(dtype == 4)     : cnafillValue = np.int8(nafillValue)        
       elif(dtype == 5)     : cnafillValue = np.int16(nafillValue)        
       elif(dtype == 6)     : cnafillValue = np.int32(nafillValue)        
       elif(dtype == 7)     : cnafillValue = np.int64(nafillValue)        
       elif(dtype == 8)     : cnafillValue = np.float16(nafillValue) 
       elif(dtype == 9)     : cnafillValue = np.float32(nafillValue)        
       elif(dtype == 10)    : cnafillValue = np.float64(nafillValue)
       elif(dtype == 11)    : return(isinstance(nafillValue,datetime.date))
       elif(dtype == 12)    : return(isinstance(nafillValue,datetime.timedelta))
       elif(dtype == 13)    : return(isinstance(nafillValue,str)) 
       elif(dtype == 14)    : return(isinstance(nafillValue,object)) 
       elif(dtype == 15)    : return(isinstance(nafillValue,pandas.core.dtypes.dtypes.CategoricalDtype))

    except Exception as e:
        opstat.set_status(False)
        opstat.store_exception("fillna value is invalid for datatype",e)
    
    return(cnafillValue)

  
           
def convert_df_cols(df,colnames,convdatatype,nafillValue=None) :
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
                cnafillValue = convert_nafill_value(df[colnames[x]].mean(),convdatatype,opstat)
            else :
                cnafillValue = convert_nafill_value(nafillValue,convdatatype,opstat)

            if(opstat.get_status()) :
                try :
                    #print("convert_df_cols",cnafillValue,type(cnafillValue))
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
    
    from dfcleanser.common.cfg import get_notebook_path
    os.chdir(get_notebook_path())

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
    
def does_dir_exist(path) :
    
    if(os.path.exists(path)) :
        if(os.path.isdir(path)) :   
            return(True)
        else :
            return(False)
    
def make_dir(path) :
    
    try :
        os.mkdir(path)
        return()
    
    except FileExistsError:
        return()
        
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
    
    
    
    
    
    
    
    
