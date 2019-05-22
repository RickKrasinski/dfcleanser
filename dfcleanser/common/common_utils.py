""
# dfc_common_utils 

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.common.cfg import (DataTransform_ID, get_dfc_dataframe)

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


def run_javaScript(script) :
    
    #from IPython.core.display import Javascript
    
    #display_jupyter_HTML(Javascript(script))
    try : 

        from IPython.display import display, Javascript
        display(Javascript(script))

    except :
        alert_user("javascript failure" + script)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  javascript from python
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def run_jscript(jscript, errmsg=None) :
    """
    * ---------------------------------------------------------
    * function : run a javascript script
    * 
    * parms :
    *  jscript    - javascript script
    *  errmsg     - detailed error message
    *  errtitle   - error title
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

    def get_elapsed_time(self) :
        return(get_formatted_time(self.stoptime - self.starttime))
 
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Generic data functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def is_numeric(data) :
    import numpy as np  
    return(np.issubdtype(data, np.number)) 


def is_numeric_col(df,colname) :
    import numpy as np
    
    found = -1
    ftype = None
    
    df_cols     = df.columns.tolist()
    df_dtypes   = df.dtypes.tolist()
    

    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            found = i

    if(found != -1) :
        ftype = df_dtypes[found]

    if( (ftype == np.int8)      or (ftype == np.int16)  or 
        (ftype == np.uint8)     or (ftype == np.uint16) or 
        (ftype == np.uint32)    or (ftype == np.uint64) or 
        (ftype == int)          or (ftype == np.int32)  or 
        (ftype == np.int64)     or 
        (ftype == np.float16)   or (ftype == np.float32)  or
        (ftype == float)        or (ftype == np.float64) ) :
        return(True)
    else :
        return(False)


def is_numeric_col_int(df,colname) :

    import numpy as np

    found = -1
    ftype = None
    
    df_cols     = df.columns.tolist()
    df_dtypes   = df.dtypes.tolist()

    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            found = i

    if(found != -1) :
        ftype = df_dtypes[found]

    if( (ftype == np.int8)      or (ftype == np.int16) or 
        (ftype == int)          or (ftype == np.int64) ) :
        return(True)
    else :
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
    if(val== True) : return("True")
    if(val == False) : return("False")
    return(" ")


def is_datatype_numeric(datatype) :
 
    import datetime
    if( (datatype == object) or (datatype == str) or (datatype == 'datetime64[ns]') or
        (datatype == datetime.datetime) or (datatype == datetime.timedelta) ) :
        return(False) 
    else :
        return(True)

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
    
    #print("get_parms_for_input : inparms  ",inparms) 
    
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

    #print("\nget_select_defaults",formid,parmids,parmtypes,len(selectDicts))
    
    numselects  =   0
    
    for i in range(len(parmids)) :
        
        if(parmtypes[i] == "select") :
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
        return()
        
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
    #else :
    #    fontsize = 4
    #    width = ((maxllabels + maxlvalues) + 6) * fontsize
    #    from dfcleanser.common.html_widgets import DEFAULT_PAGE_WIDTH
    #    width = int(math.ceil((width / DEFAULT_PAGE_WIDTH) * 100)) + 20
    #    print("width",width)

    #    parms_table.set_smallwidth(width+6)

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
    #   extracty parm values from a dict
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
#--------------------------------------------------------------------------
#   dfcleanser table scrolling methods
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
    
    print("get_scroll_table_html",tableid,direction,tblw.get_table_value(tableid).get_tabletype())
    
    
    if(tblw.get_table_value(tableid).get_tabletype() == tblw. MULTIPLE) : 
       table_html = tblw.get_mult_table(tblw.get_table_value(tableid),direction,False)
    
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) : 
       table_html = tblw.get_col_major_table(tblw.get_table_value(tableid),direction,displayTable=False)
        
    else :
        table_html = tblw.get_row_major_table(tblw.get_table_value(tableid),direction,False)

    if(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) :
        
        print("COLUMN_MAJOR")
        tablehtmlloc    = table_html.find("<thead")
        tableendhtmlloc = table_html.find("</tbody>")
        table_html = table_html[tablehtmlloc:tableendhtmlloc+len("</tbody>")]
        
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw. MULTIPLE) :
        
        thead = table_html.find("<thead>")
        tend  = table_html.find("</table>")
    
        table_html = table_html[thead:(tend-1)]
    
    else :
        # check for no header tables
        if(table_html.find("<thead") == -1) :
            tablehtmlloc    = table_html.find("<tbody>")
            tableendhtmlloc = table_html.find("</tbody>")
        
            table_html = table_html[tablehtmlloc:tableendhtmlloc+len("</tbody>")]
            #print("get_scroll_table_html\n",table_html)
        
    new_table_html = patch_html(table_html)
    
    return(new_table_html)


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
    
    new_table_html  = get_scroll_table_html(tableid,direction)

    print("scroll_table",new_table_html)
    change_table_js = "$("
    if( (new_table_html.find("<thead") == -1) or (tableid == "dfschemaTable") ) :
        change_table_js = change_table_js + "'#" + tableid + "').html('"
        
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw. MULTIPLE) :
        change_table_js = change_table_js + "'#" + tableid + "').html('"    
        
    else :
        change_table_js = change_table_js + "'#" + tableid + "container').html('"
        
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_table parms : "+tableid+" "+str(direction))
 
    refresh_bg_js = "$('#" + tableid + "_thr').css({'background-color':'#6FA6DA'});"
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))
    refresh_bg_js = "$('#" + tableid + "_thr').css({'color':'white'});"
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))
    refresh_bg_js = "$('#" + tableid + "buttons').css({'margin-right':'1%'});"
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))

    buttons     =   ["downarrow","uparrow","leftarrow","rightarrow"]
    
    import datetime 
    tstamp = datetime.datetime.now().time()
    
    for i in range(len(buttons)) :
    
        button_id       =   tableid + buttons[i]+"img"
        change_html     =   ("'#" + button_id + "').attr('src'," + 
                             "'https://rickkrasinski.github.io/dfcleanser/graphics/" + buttons[i] + ".png?timestamp=" + str(tstamp) + "'")
        change_cols_js = ("$(" + change_html + ");")

        run_jscript(change_cols_js,"fail to refresh sroll table : ")
    

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
    
    from dfcleanser.common.html_widgets import InputForm
    input_html = InputForm(inputid,inputlist[0],inputlist[1],
                           inputlist[2],inputlist[3],inputlist[4],
                           inputlist[5],inputlist[6],inputlist[7],
                           True).get_html()


    startnewhtml    =   input_html.find("<div class='container dc-container dc-default-input-inner-div'>")
    endnewhtml      =   input_html.find("<form")
    newhtml         =   input_html[startnewhtml:(endnewhtml - (3 + len("</div>")))]
    
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
        
        change_input_js = "$('#" + formid + "').html('"
        change_input_js = change_input_js + new_input_html + "');"
    
        run_jscript(change_input_js,"fail to get full parms for : " + formid)
 
         
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
    
    print("scroll_sample_rows",tableid,direction)
    
    from dfcleanser.common.display_utils import display_more_sample_rows
    df_delim    =   tableid.find("_search_")
    if(df_delim > -1) :
        df_title  =   tableid[:df_delim]
    else :
        df_title  =   None
    
    print("df_title",df_title)
    
    
    table_html = display_more_sample_rows(get_dfc_dataframe(df_title),tableid,direction)
    
    thead = table_html.find("<thead>")
    tend  = table_html.find("</table>")
    
    table_html = table_html[thead:(tend-1)]
    
    new_table_html = patch_html(table_html)

    change_table_js = "$("
    change_table_js = change_table_js + "'#" + tableid + "').html('"
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))

    refresh_bg_js = "$('#" + tableid + "_thr').css({'background-color':'#6FA6DA'});"
    print("refresh_bg_js",refresh_bg_js)
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))
    
    refresh_bg_js = "$('#" + tableid + "_thr').css({'color':'white'});"
    print("refresh_bg_js",refresh_bg_js)
    run_jscript(refresh_bg_js,"fail scroll_sample_rows : "+tableid+" "+str(direction))


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
    new_rows_html = display_more_sample_rows(get_dfc_dataframe(),
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
    table_html = display_more_single_row(get_dfc_dataframe(),tableid,direction)
    
    thead = table_html.find("<tbody>")
    tend  = table_html.find("</tbody>")
    
    table_html = table_html[thead:(tend-1)]
    
    new_table_html = patch_html(table_html)

    change_table_js = "$("
    change_table_js = change_table_js + "'#" + tableid + "').html('"
    change_table_js = change_table_js + new_table_html + "');"
    
    run_jscript(change_table_js,"fail scroll_single_row : " + tableid + str(direction))

    
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
        
    df  =   cfg.get_dfc_dataframe(dftitle)

    from dfcleanser.sw_utilities.sw_utility_dfsubset_widgets import get_dfsubset_table
    cols_html = get_dfsubset_table(df,filters,colname)

    startinner  =   cols_html.find('<div class="input-group">')
    endinner    =   cols_html.find('<table class="table dc-table"')

    title_html  =   cols_html[startinner:endinner]
    endinner    =   title_html.rfind("</div>")
    title_html  =   "\t\t" + title_html[:endinner]
    
    
    startinner  =   cols_html.find('<tbody>')
    endinner    =   cols_html.find('</tbody>') + len('</tbody>')
    table_html  =   cols_html[startinner:endinner]
    
    return([title_html,table_html])


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

    fetched_html    =   get_dfsubset_vals_html(filters,colname) 
    panel_html      =   fetched_html[0]
    cols_html       =   fetched_html[1]
    
    panel_html   =   panel_html.replace("&","&amp;")
    new_panel_html = patch_html(panel_html)
    
    change_table_js = "$('#dcsubsetcolnamesTablePanelHeading').html('"
    change_table_js = change_table_js + new_panel_html + "');"
            
    run_jscript(change_table_js,"fail to get unique vals for : ")
    
    cols_html   =   cols_html.replace("&","&amp;")
    new_cols_html = patch_html(cols_html)
    
    change_table_js = "$('#dcsubsetcolnamesTable').html('"
    change_table_js = change_table_js + new_cols_html + "');"
            
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
 


def get_select_concat_df_vals(parms) :
    print("get_select_concat_df_vals",parms)

    dfsel   =   parms[0]
    df1     =   parms[1]
    df2     =   parms[2]
    
    import dfcleanser.common.cfg as cfg
    
    tdf         =   cfg.get_dfc_dataframe(df1)
    if(tdf is None) :
        df1rcount   =   ""
        df1ccount   =   ""
    else :
        df1rcount   =   str(len(tdf))
        df1cols     =   cfg.get_dfc_dataframe(df1).columns.tolist()
        df1ccount   =   str(len(df1cols))
    
    tdf         =   cfg.get_dfc_dataframe(df2)
    if(tdf is None) :
        df2rcount   =   ""
        df2ccount   =   ""
    else :
        df2rcount   =   str(len(tdf))
        df2cols     =   cfg.get_dfc_dataframe(df2).columns.tolist()
        df2ccount   =   str(len(df2cols))
    
    
    if(dfsel == df1) :
        
        if(not (df1rcount == "")) :
        
            update_row_js = "$('#df1numrows').val(" + df1rcount + ");"
            run_jscript(update_row_js,"update_row_count_js","update_row_count_js")
            update_row_js = "$('#df1numcols').val(" + df1ccount + ");"
            run_jscript(update_row_js,"update_row_js","update_row_js")

            update_row_js = "$('#df1numrows').attr('readonly', true);"
            run_jscript(update_row_js,"update_row_js","update_row_js")
            update_row_js = "$('#df1numcols').attr('readonly', true);"
            run_jscript(update_row_js,"update_row_js","update_row_js")
        
    if(dfsel == df2) :
        
        if(not (df2rcount == "")) :
        
            update_row_js = "$('#df2numrows').val(" + df2rcount + ");"
            run_jscript(update_row_js,"update_row_count_js","update_row_count_js")
            update_row_js = "$('#df2numcols').val(" + df2ccount + ");"
            run_jscript(update_row_js,"update_row_js","update_row_js")

            update_row_js = "$('#df2numrows').attr('readonly', true);"
            run_jscript(update_row_js,"update_row_js","update_row_js")
            update_row_js = "$('#df2numcols').attr('readonly', true);"
            run_jscript(update_row_js,"update_row_js","update_row_js")
 
    import json
    
    if(not (df1rcount == "")) :   
        df1cols     =   cfg.get_dfc_dataframe(df1).columns.tolist()
    else :
        df1cols     =   None
    if(not (df2rcount == "")) :   
        df2cols     =   cfg.get_dfc_dataframe(df2).columns.tolist()
    else :
        df2cols     =   None
    
    print("df1rcount",df1rcount,"df2rcount",df2rcount)
    
    if( (not (df1rcount == "")) and 
        (not (df2rcount == "")) ) :  
        
        print("df1cols",df1cols)
        print("df2cols",df2cols)
        # change diff columns fileds
        df1diffs    =   []
        for i in range(len(df1cols)) :
            if(not(df1cols[i] in df2cols)) :
                df1diffs.append(df1cols[i])
        df1dstr     =   json.dumps(df1diffs)
    
        df2diffs    =   []
        for i in range(len(df2cols)) :
            if(not(df2cols[i] in df1cols)) :
                df2diffs.append(df2cols[i])
        df2dstr     =   json.dumps(df2diffs)
    
    else :
        df1dstr     =   ""
        df2dstr     =   "" 
    
    print("df1dstr",df1dstr,"df2dstr",df2dstr)       
    update_row_js = "$('#df1diffcols').val(" + df1dstr + ");"
    run_jscript(update_row_js,"update_row_count_js","update_row_count_js")
    update_row_js = "$('#df2diffcols').val(" + df2dstr + ");"
    run_jscript(update_row_js,"update_row_count_js","update_row_count_js")
            
    update_row_js = "$('#df1diffcols').attr('readonly', true);"
    run_jscript(update_row_js,"update_row_js","update_row_js")
    update_row_js = "$('#df2diffcols').attr('readonly', true);"
    run_jscript(update_row_js,"update_row_js","update_row_js")
    

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
    if (isinstance(get_dfc_dataframe()[colname][0], str)) :
        
        uniques =   get_dfc_dataframe()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        if(is_numeric_col(get_dfc_dataframe(),colname)) :           
            uniques =   get_dfc_dataframe()[colname].unique().tolist()
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

    tablehtml = tblw.get_row_major_table(columnsamples_table,tblw.SCROLL_NEXT,False)


    
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
    
    from dfcleanser.common.cfg import get_dfc_dataframe_object
    dfcdf   =   get_dfc_dataframe_object(title)
    
    newdf       =   dfcdf.get_df()
    numrows     =   len(newdf)
    numcols     =   len(newdf.columns)
    notes       =   dfcdf.get_notes()
    
    change_input_js = "$('#dfnumrows').val(" + str(numrows) + ");"
    run_jscript(change_input_js,"fail to set df parms : " + formid)

    change_input_js = "$('#dfnumcols').val(" + str(numcols) + ");"
    run_jscript(change_input_js,"fail to set df parms : " + formid)

    change_input_js = "$('#dfnotes').val('" + notes + "');"
    run_jscript(change_input_js,"fail to set df parms : " + formid)



"""
#--------------------------------------------------------------------------
#   get full input html
#
#       inputid     - input form id
##
#   return new input html
#
#--------------------------------------------------------------------------
""" 
"""
def get_datetime_formats_html() :
    print("get_datetime_formats_html")    
    formatslist = []
    
    from dfcleanser.sw_utilities.sw_utility_control import get_Dict
    formats = get_Dict("strftime")

    keys = list(formats.keys())
    keys.sort()
    
    for i in range(len(keys)) :
        formatslist.append(keys[i])
        formatslist.append(formats.get(keys[i]))

    formatslistHeader    =   [""]
    formatslistRows      =   []
    formatslistWidths    =   [100]
    formatslistAligns    =   ["left"]
    formatslistHrefs     =   []
    
    for i in range(len(formatslist)) :
        if((i%2) == 0) :
            formatslistRows.append([formatslist[i]])
            formatslistHrefs.append([None])
        else :
            formatslistRows.append([formatslist[i]])
            formatslistHrefs.append(["select_datetime_format"])
        
    formats_table = None
                
    formats_table = tblw.dcTable("Formats","dtdatetimeformatsTable",DataTransform_ID,
                            formatslistHeader,formatslistRows,
                            formatslistWidths,formatslistAligns)
            
    formats_table.set_refList(formatslistHrefs)
    
    formats_table.set_small(True)
    formats_table.set_smallwidth(98)
    formats_table.set_smallmargin(2)

    formats_table.set_border(True)
        
    formats_table.set_checkLength(False)
            
    formats_table.set_textLength(20)
    formats_table.set_html_only(True) 
    
    formats_table.set_tabletype(tblw.ROW_MAJOR)
    formats_table.set_rowspertable(14)

    formats_html = tblw.get_row_major_table(formats_table,tblw.SCROLL_NEXT,False)
    
    return(formats_html)
""" 
    
"""
#--------------------------------------------------------------------------
#   get full parms for an input
#
#       parms    - input id
# 
#   update the input form
#
#--------------------------------------------------------------------------
""" 
"""          
def get_datetime_formats(parms) :
    
    print("get_datetime_formats",parms)

    formats_html    =   get_datetime_formats_html()
    formid          =   "datetimecolnamesTableContainer"
   
    new_table_html = patch_html(formats_html)
    
    change_input_js = "$('#" + formid + "').html('"
    change_input_js = change_input_js + new_table_html + "');"
    
    run_jscript(change_input_js,"fail to get datatime format strings : ")

    buttons     =   ["downarrow","uparrow"]
    for i in range(len(buttons)) :
    
        import datetime 
        tstamp = datetime.datetime.now().time()

        change_cols_js = ("$('#" + buttons[i]+"Id" + "').attr('src'," +
                                 "'https://rickkrasinski.github.io/dfcleanser/graphics/" + buttons[i]+".png?timestamp=" + str(tstamp) +"');")
        
        #print("refresh_images",change_help_js)
        run_jscript(change_cols_js,"fail to refresh sroll table : ")
"""

"""
#--------------------------------------------------------------------------
#   get full input html
#
#       inputid     - input form id
##
#   return new input html
#
#--------------------------------------------------------------------------
""" 
"""
def get_cand_cols_html() :
    
    from dfcleanser.data_transform.data_transform_widgets import get_possible_datetime_cols
    import dfcleanser.common.cfg as cfg
    cands_html  =   get_possible_datetime_cols("datetimecolnamesTable",cfg.DataTransform_ID,"get_datetime_col",None)
    
    return(cands_html)
""" 
    
"""
#--------------------------------------------------------------------------
#   get full parms for an input
#
#       parms    - input id
# 
#   update the input form
#
#--------------------------------------------------------------------------
""" 
"""          
def get_cand_cols(parms) :
    
    print("get_cand_cols",parms)

    cols_html    =   get_cand_cols_html()
    formid       =   "datetimecolnamesTableContainer"
   
    new_table_html = patch_html(cols_html)
    
    change_input_js = "$('#" + formid + "').html('"
    change_input_js = change_input_js + new_table_html + "');"
    
    run_jscript(change_input_js,"fail to get datatime format strings : ")

    buttons     =   ["downarrow","uparrow"]
    for i in range(len(buttons)) :
    
        import datetime 
        tstamp = datetime.datetime.now().time()

        change_cols_js = ("$('#" + buttons[i]+"Id" + "').attr('src'," +
                                 "'https://rickkrasinski.github.io/dfcleanser/graphics/" + buttons[i]+".png?timestamp=" + str(tstamp) +"');")
        
        #print("refresh_images",change_help_js)
        run_jscript(change_cols_js,"fail to refresh sroll table : ")
"""


def get_gen_func_values(parms) :

    """
    * ---------------------------------------------------------
    * function : get generic function values for a form
    * 
    * Parms :
    *  formid    - form id
    *  ftitle    - genfunc title
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    formid      =   parms[0]
    ftitle      =   parms[1]
    
    import dfcleanser.common.cfg as cfg
    dftitle     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
    
    import dfcleanser.common.cfg as cfg
    
    if(formid == "addcolfuncs") :
        
        from dfcleanser.data_transform.data_transform_columns_widgets import add_column_code_gf_input_id
        addparms    =   cfg.get_config_value(add_column_code_gf_input_id+"Parms")
        if(not (addparms is None)) :
            newcolname  =   addparms[0]
        else :
            newcolname  =   "USER VALUE"
        
        dfcolname   =   "USER VALUE"
        
    else :

        from dfcleanser.data_transform.data_transform_columns_widgets import apply_column_gf_input_id
        addparms    =   cfg.get_config_value(apply_column_gf_input_id+"Parms")
        if(not (addparms is None)) :
            dfcolname  =   addparms[0]
        else :
            dfcolname  =   "USER VALUE"
        
        newcolname   =   "None"

    from dfcleanser.sw_utilities.sw_utility_genfunc_control import get_generic_function, get_generic_function_desc
    gt_func         =   get_generic_function(ftitle)
    
    if(gt_func is None) :
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule
        gfmodule    =   reservedfunctionsmodule
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctions
        if(ftitle == reservedfunctions[0])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[1])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[2])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[3])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[4])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[5])  :    kwvals  =   {"inlist":"USER VALUE"}
        if(ftitle == reservedfunctions[6])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"trigfunc":"","opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[7])  :    kwvals  =   {"invalue":"USER VALUE","trigfunc":"USER VALUE"}
        if(ftitle == reservedfunctions[8])  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"degrees":"","opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[9])  :    kwvals  =   {"invalue":"USER VALUE","degrees":"USER VALUE"}
        if(ftitle == reservedfunctions[10]) :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[11]) :    kwvals  =   {"invalue":"USER VALUE"}
        if(ftitle == reservedfunctions[12]) :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"decimals":"","opstat":"opstat","newcolname":newcolname}
        if(ftitle == reservedfunctions[13]) :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"opstat":"opstat"}
        if(ftitle == reservedfunctions[14]) :    kwvals  =   {"geocoords":"USER VALUE","opstat":"opstat"}
         
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_function_kwargs
        gfcode      =   get_function_kwargs(gfmodule,ftitle,kwvals)
        gfcode      =   gfcode.replace("\n","dfc_new_line")
        gfcode      =   gfcode.replace("'",'"')

        gfdesc      =   get_generic_function_desc(ftitle)
        gfdesc      =   gfdesc.replace("\n","dfc_new_line")
        gfdesc      =   gfdesc.replace("'",'"')
        
    else :
        gfmodule    =   gt_func.get_func_module()
        gfcode      =   gt_func.get_func_code()
        gfcode      =   gfcode.replace("\n","dfc_new_line")
        gfcode      =   gfcode.replace("'",'"')

        gfdesc      =   get_generic_function_desc(ftitle)        
        gfdesc      =   gfdesc.replace("\n","dfc_new_line")
        gfdesc      =   gfdesc.replace("'",'"')
    
    if(formid == "addcolfuncs") :
        
        change_val_js = "$('#addcolmodule').val('"
        change_val_js = change_val_js + gfmodule + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")

        change_val_js = "$('#addcolname').val('"
        change_val_js = change_val_js + ftitle + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")

        change_val_js = "set_textarea('addcolcodefcode', '"
        change_val_js = change_val_js + gfcode + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")
        
        change_val_js = "set_textarea('addcoldesc', '"
        change_val_js = change_val_js + gfdesc + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")

    if(formid == "fnselect") :
        
        change_val_js = "$('#fmodule').val('"
        change_val_js = change_val_js + gfmodule + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")

        change_val_js = "$('#fnname').val('"
        change_val_js = change_val_js + ftitle + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")

        change_val_js = "set_textarea('fntoapply', '"
        change_val_js = change_val_js + gfcode + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")
        
        change_val_js = "set_textarea('fndesc', '"
        change_val_js = change_val_js + gfdesc + "');"
        run_jscript(change_val_js,"fail to get sample values for : ")
        
        
        
        
        
        
        
        
        
        

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Generic scripting helper methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   display a script exception
#
#       e    - exception
#
##--------------------------------------------------------------------------
""" 
def display_script_exception(e) :

    from dfcleanser.scripting.data_scripting_widgets import exit_scripting_mode
    exit_scripting_mode()
    
    opstat = opStatus()
    opstat.store_exception("Scripting Exception",e)
    display_exception(opstat)
  
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Datatype helper methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   datatype helper methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""      
def get_dtype_from_value(df,colname) :
    
    import datetime
    
    val = df[colname][1]
    if( (isinstance(val,datetime.date) ) and 
        (type(val) is datetime.date )) : 
        return(12)
    elif(isinstance( df[colname][1],datetime.datetime)) :
        return(11)

    if(isinstance( df[colname][1],object)) : 
        return(14)
    elif(isinstance( df[colname][1],str)) :
        return(13)
    elif(isinstance( df[colname][1],datetime.timedelta)) :
        return(11)
    else :
        return(-1)


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


def is_datetime_value(val) :
    
    try :
        import datetime
        if( (type(val) == datetime.datetime) ) :#or 
        #(get_dfc_dataframe()[colname].dtype == 'datetime64[ns]') or 
        #(get_dfc_dataframe()[colname].dtype == '<M8[ns]') or 
        #(get_dfc_dataframe()[colname].dtype == '>M8[ns]') ):
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_date_value(val) :
    
    try :    
        import datetime
        if( (type(val) == datetime.date) ):
            return(True)
        else :
            return(False)
    except :
        return(False)
        
def is_time_value(val) :
    
    try :    
        import datetime
    
        if( (type(val) == datetime.time) ) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_timedelta_value(val) :
    
    try :
        import datetime
        if( (type(val) == datetime.timedelta) ) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_str_value(val) :
    
    try :    
        if(isinstance(str)) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_datetime_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)
    
    try :
        import datetime
        if( (type(val) == datetime.datetime) ) :#or 
        #(get_dfc_dataframe()[colname].dtype == 'datetime64[ns]') or 
        #(get_dfc_dataframe()[colname].dtype == '<M8[ns]') or 
        #(get_dfc_dataframe()[colname].dtype == '>M8[ns]') ):
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_date_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)

    try :    
        import datetime
        if( (type(val) == datetime.date) ):
            return(True)
        else :
            return(False)
    except :
        return(False)
        
def is_time_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)
    
    try :    
        import datetime
    
        if( (type(val) == datetime.time) ) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_timedelta_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)
    
    try :
        import datetime
        if( (type(val) == datetime.timedelta) ) :
            return(True)
        else :
            return(False)
    except :
        return(False)

def is_str_column(df,colname) :
    
    val = get_first_non_nan_value(df,colname)

    try :    

        if(isinstance(val,str)) :
            return(True)
        else :
            return(False)
    except :
        return(False)

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
    elif(dt == 'datetime64[ns]')                : return(11)
    elif(is_datetime_datatype(dt))              : return(12)
    elif(is_datetime_datatype(dt))              : return(13)
    elif(is_timedelta_datatype(dt))             : return(14)
    elif(dt == 'timedelta64[ns]')               : return(14)

    elif(dt == str)                             : return(15) 
    elif(dt == object)                          : return(16)
    elif(dt == 'O')                             : return(16) 

    elif(dt == int)                             : return(17) 
    elif(dt == float)                           : return(18) 
    elif(isinstance(dt,pandas.core.dtypes.dtypes.CategoricalDtype))  : return(19) 
    
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

    return(None)


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
    
    foundat = 0
    while(foundat > -1) :
        foundat = instr.find(",")
        if(foundat > -1) :
            instr = instr[0:foundat] + "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + instr[foundat+1:]
    
    return(instr)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   system message helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""     
def display_exception(opstat,display=True) :
    
    #print("\n")
    exception_html = ""
    exception_html = (exception_html + '<div class="container" style="border: 0px solid #428bca; width:82%; margin-left:20px;">' + new_line)
    exception_html = (exception_html + '    <div class="row">' + new_line)
    exception_html = (exception_html + '        <div class="panel panel-primary" style="border: 0px">' + new_line)
    exception_html = (exception_html + '            <div class="panel-heading dc-table-panel-heading" style="height:40px;">' + new_line)
    exception_html = (exception_html + '                <div class="input-group">' + new_line)
    exception_html = (exception_html + '                    <p class="dc-table-title" style="margin-bottom:5px;">Error : </p>' + new_line)
    exception_html = (exception_html + '                </div>' + new_line) 
    exception_html = (exception_html + '            </div>' + new_line)
    exception_html = (exception_html + '            <div></br></div>' + new_line)
    exception_html = (exception_html + '            <div class="exception-status">' + new_line)
    exception_html = (exception_html + '                <p>' + "&nbsp;" + str(opstat.get_errorMsg()) + '</p>' + new_line)
    exception_html = (exception_html + '            </div>' + new_line)

    if(not (opstat.get_systemRC0()) == None) :
        exception_html = (exception_html + '            <div class="exception-status-detail" style="height:30px;">' + new_line)
        exception_html = (exception_html + '                <p>' + "&nbsp;&nbsp;&nbsp;" + str(opstat.get_systemRC0().__name__) + '</p>' + new_line)
        exception_html = (exception_html + '            </div>' + new_line)
    
    if(not (opstat.get_systemRC1()) == None) :
        
        rcstring = str(opstat.get_systemRC1())
        rcstring = rcstring.replace(";","<br>&nbsp;&nbsp;&nbsp;")
        exception_html = (exception_html + '            <div class="exception-status-detail" style="height:30px;">' + new_line)
        exception_html = (exception_html + '                <p>' + "&nbsp;&nbsp;&nbsp;" + rcstring + '</p>' + new_line)
        exception_html = (exception_html + '            </div>' + new_line)
        
    #exception_html = (exception_html + '        <div><br></div>' + new_line) 
        
    exception_html = (exception_html + '        </div>' + new_line) 
    exception_html = (exception_html + '    </div>' + new_line) 
    exception_html = (exception_html + "</div>")
    
    #print(exception_html)
    from IPython.display import HTML
    from IPython.display import display
    
    if(display) :
        display_jupyter_HTML(HTML(exception_html))
    else :
        return(exception_html)

def display_status(msg, skipLines = 0, display=True) :
    
    status_html = ""
    
    if(skipLines > 0) :
        for i in range(skipLines) :
            status_html = (status_html + new_line) 
    
    if(display) :        
        status_html = (status_html + '<div class="container" style="width:80%; margin-left:30px; margin-bottom:5px;">' + new_line)
    else :
        status_html = (status_html + '<div class="container" style="width:480px; margin-bottom:5px;">' + new_line)
        
    status_html = (status_html + '    <div class="row" style="margin-bottom:0px;">' + new_line)
    status_html = (status_html + '        <div class="panel panel-primary" style="border:0px; margin-bottom:0px;">' + new_line)
    status_html = (status_html + '            <div class="panel-heading dc-table-panel-heading" style="height:40px; margin-bottom:0px;">' + new_line)
    status_html = (status_html + '                <div class="input-group">' + new_line)
    status_html = (status_html + '                    <p class="dc-table-title">Status : </p>' + new_line)
    status_html = (status_html + '                </div>' + new_line) 
    status_html = (status_html + '            </div>' + new_line)
    status_html = (status_html + "            <div class='note-line'>" + new_line)
    status_html = (status_html + "                <p></p>" + new_line)
    status_html = (status_html + "            </div>" + new_line)
    
    if(type(msg) == str) :
    
        status_html = (status_html + "            <div class='status-line'>" + new_line)
        status_html = (status_html + "                <p><span class='status-line'>" + str(msg) + "</span></p>" + new_line)
        status_html = (status_html + "            </div>" + new_line)
        
    else :
        
        for i in range(len(msg)) :
            status_html = (status_html + "        <div class='note-line'>" + new_line)
            status_html = (status_html + "            <p><span class='note-line'>" + msg[i] + "</span></p>" + new_line)
            status_html = (status_html + "        </div>" + new_line)

    status_html = (status_html + '        </div>' + new_line) 
    status_html = (status_html + '    </div>' + new_line) 
    status_html = (status_html + '</div>')
    
    #print(status_html)
    if(display) :
        displayHTML(status_html)
    else :
        return(status_html)


def display_msgs(notes,text,color=False,margin=30,helpmsg=False,display=True) :
    
    notes_html = ""
    if(display) :
        notes_html = (notes_html + '<div class="container" style="width:80%; margin-left:' + str(margin) + 'px; border:1px;">' + new_line)
    else :
        notes_html = (notes_html + '<div class="container" style="width:480px; border:1px;">' + new_line)
        
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
    
    if(display) :
        
        import dfcleanser.common.cfg as cfg
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            display_msgs(notes,"Notes :")
            
        else :
            
            notes_html      =   display_msgs(notes,"Notes :",color=False,margin=30,helpmsg=False,display=False) 
            gridclasses     =   ["dfc-top-"]
            gridhtmls       =   [notes_html]
    
            display_generic_grid("dfc-notes-pop-up-wrapper",gridclasses,gridhtmls)
            
    else :
        return(display_msgs(notes,"Notes :",color=False,margin=30,helpmsg=False,display=False))
        

    
def display_inline_help(helptext,margin=80) :
    display_msgs(helptext,"Help :",False,margin,True)    


#LAST_EXCEPTION_STACK_TRACE  =   "LastStackTrace"
    
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
#    grid components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
wrapper_start   = """<div class='"""
wrapper_start1  = """'>
"""

wrapper_end     = """</div>"""

#header_start    = """<div class="box header" style="color:black;">
#  """
#sidebar_start   = """<div class="box sidebar">"""
#sidebar1_start  = """<div class="box sidebar1">"""


#content_start   = """<div class="box content" style="color:black">"""
#footer_start    = """<div class="box footer">"""

#section_end     = """</div>
#""" 


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

    #print(gridHTML)
    displayHTML(gridHTML)



def is_existing_column(df,colname) : 
    
    df_cols = df.columns.tolist()
    
    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            return(True)

    return(False)

def single_quote(parm) :
    return("'"+parm+"'")

def any_char_in_cols(df, schar, getvals):
    
  schar_in_cols = [[]]

  for k in range(len(df.columns)) :
      schar_in_cols.append([0,[]])
      
      for l in range(len(df)) : 
           
          if(schar in str(df.iloc[l,k])) :
              schar_in_cols[k][0] = schar_in_cols[k][0] + 1
              
              if(getvals) :
                  schar_in_cols[k][1].append(k)
                  
  return(schar_in_cols) 


"""            
#------------------------------------------------------------------
#
#   Column uniques functions
#
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
    return(df[columnName].unique())

"""            
#------------------------------------------------------------------
#   get a simple list of unique values for a column
#
#   return : list of unique vals
#
#   df              -   dataframe
#   columnId        -   column name 
#
#------------------------------------------------------------------
"""
def get_col_uniques_by_id(df, columnId)  :  
    try :
        return(df[columnId].unique())
    except :
        return(df[columnId])

    #return(df[columnId].unique())

   
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
def get_num_uniques_by_id(df, columnId)  :   

    #return(len(df.ix[:,columnId].unique()))
    #return(len(df.loc[columnId].unique()))
    try :
        return(len(df[columnId].unique()))
    except :
        return(len(df))
        
    
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
def convert_nafill_value(nafillValue,dtype,opstat):
    
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
def convert_df_cols(df,colnames,convdatatype,nafillValue=None) :
    
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
#
#   dfc cell files helpers
#
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
    
    
    
    
    
    
    
    
