"""
# dfc_common_html_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg 

from dfcleanser.common.common_utils import (displayHTML,opStatus,display_exception,single_quote)

"""
#--------------------------------------------------------------------------
#   Common html helper components
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   Common consts
#--------------------------------------------------------------------------
"""
new_line =   """
"""

DEFAULT_PAGE_WIDTH          =   980

MAX_BUTTON_WIDTH            =   160
SINGLE_BUTTON_WIDTH         =   (DEFAULT_PAGE_WIDTH/4)

CHECKBOX_HEIGHT             =   30
CENTERED_BUTTON_HEIGHT      =   40
MULTI_LINE_BUTTON_HEIGHT    =   25
BUTTON_HEIGHT               =   40
CHECKBOX_SIZE               =   20

debugForms                  =   False
debugFlag                   =   False

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  common html element helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_html_spaces(count) :
    
    spaces = ""
    
    for i in range(count) :
        spaces += "&nbsp;"
        
    return(spaces)

def tabs(count) :
    
    tabs    =   "    "
    tabsout =   ""
    
    for i in range(count-1) :
        tabsout += tabs
        
    return(tabsout)

def addblankline(count) :
    
    bline = ""
    for i in range(count) :
        bline = (bline + new_line + "  <br></br>")   
    return(bline)

def addformblankline(tabstart) :
    
    blank_line = ""
    blank_line = (blank_line + tabs(tabstart) + """<div style="height:10px;">""" + new_line + 
                  tabs((tabstart+1)) + """<br></br>""" + new_line + 
                  tabs(tabstart) + """</div>""")
    
    return(blank_line)

def addformtitle(title,inputtitle=False) :
    
    if(inputtitle) :
        title_html = ""
        title_html = (title_html + "  <div>" + new_line)
        title_html = (title_html + "    <p style='font-size:13px; font-weight:bold; text-indent:10%;'>")
        title_html = (title_html + title + "</p>" + new_line + "  </div>")
        return(title_html)
    else :
        return("  <h4 class='dc-doc-title'>" + title + "</h4>")

def addheading(title,level) :
    heading = ""
    heading = (heading + "<div  class='dchdr' >" + new_line)
    heading = (heading + "  <h" + str(level) + ">")
    if(level == 4) :
        heading = (heading + "&nbsp;&nbsp;") 
    heading = (heading + title + "</h" + str(level) + ">")
    heading = (heading + new_line + "</div>" + new_line)
    
    return(heading)

def addstylesheet(url) :
    
    stylesheet = ""
    stylesheet = (new_line + stylesheet + '  <link href="' + url + '" rel="stylesheet" ')
    stylesheet = (stylesheet + url + "'>")
    return(stylesheet)

def addattribute(name,value) :
    
    #print("addattribute",name,value)
    attribute = ""
    attribute = attribute + " " + name + "=" + '"' + str(value) + '"'
    return(attribute)

def addstyleattribute(name,value) :
    
    styleattribute = ""
    styleattribute = styleattribute + " " + name + ": " + value + "; "
    return(styleattribute)

def addjscript(url) :
    
    jsscript  =     ""
    
    jsscript     =   (jsscript + new_line + "  <script type='text/javascript'")
    jsscript     =   (jsscript + addattribute("src",url))
    jsscript     =   (jsscript + "></script>")
    
    return(jsscript)

def addstyle(styleUrl) :
    
    style_element = ""
    style_element = (style_element + new_line + "  <link")
    style_element = (style_element + addattribute("rel","stylesheet"))
    style_element = (style_element + addattribute("href",styleUrl))
    style_element = (style_element + "></link>")
    
    return(style_element)

def addcdn(cdnUrl) :
    
    cdn_element = ""
    cdn_element = (cdn_element + new_line + "  <script")
    cdn_element = (cdn_element + addattribute("src",cdnUrl))
    cdn_element = (cdn_element + "></script>")
    
    return(cdn_element)
      
def containscheckbox(forms) :
    for i in range(len(forms)) :
        if(forms[i][FORM_TYPE] == CHECKBOX_FORM_TYPE) : 
            return(True)
        
    return(False)

"""
#--------------------------------------------------------------------------
#  common html form functions
#--------------------------------------------------------------------------
"""
def maketextarea(rows) :
    return(["textarea",str(rows)])

def isenlargedtextarea(taObject) :
    if(type(taObject) == list) :
        return(True)
    else:
        return(False)

def gettextarearows(taObject) :
    if(isenlargedtextarea(taObject)) : 
        return(taObject[1])
    else:
        return(3)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   composite forms doc - docs with multiple unique forms - can be one
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""

#   composite form field ids
"""
FORM_TYPE                   =   0
FORM_TITLE                  =   1
FORM_DATA                   =   2

"""
#   common form form types 
"""
BUTTON_FORM_TYPE            =   0
INPUT_FORM_TYPE             =   1
CHECKBOX_FORM_TYPE          =   2
BLANK_LINE_TYPE             =   3
HEADER_LINE_TYPE            =   4
RADIO_FORM_TYPE             =   8

"""
#   HEADER_LINE_TYPE data FORM_DATA indices 
"""
HEADER_LINE_TITLE           =   0
HEADER_LINE_LEVEL           =   1
   
"""
* -----------------------------------------------------------------------*
*   Common helper methods to refactor forms for composite docs
* -----------------------------------------------------------------------*
"""
def get_button_tb_form(buttonparms) :
    
    button_tb      =   []
    button_tb.append(BUTTON_FORM_TYPE)
    button_tb.append(None)
    button_tb.append(buttonparms)
    
    return(button_tb)

def get_header_form(text) :

    header_form  =   []
    header_form.append(HEADER_LINE_TYPE)
    header_form.append(None)
    header  =   [text]
    header.append(3)
    header_form.append(header)

    return(header_form)


def get_input_form(inputparms,title=None) :
 
    input_form =   []
    input_form.append(INPUT_FORM_TYPE)
    input_form.append(title)
    input_form.append(inputparms)
 
    return(input_form)

def get_blank_line_form() :

    blank_line  =   []
    blank_line.append(BLANK_LINE_TYPE)
    blank_line.append(None)
    
    return(blank_line)
    
def get_radio_button_form(inputparms) :

    radio_form         =   []
    radio_form.append(RADIO_FORM_TYPE)
    radio_form.append(None)
    radio_form.append(inputparms)
    
    return(radio_form)

def get_checkbox_form(title,checkboxform) :

    checkbox_form  =   []
    checkbox_form.append(CHECKBOX_FORM_TYPE)
    checkbox_form.append(title)
    checkbox_form.append(checkboxform)
    
    return(checkbox_form)

def dump_form_list(formlist,offset,numperline) :

    listtext = ""
    #for i in range(offset) : listtext = (listtext+" ")
    listtext = (listtext + "[")
    for i in range(len(formlist)) :
        if(not(formlist[i] == None)) :
            if(type(formlist[i]) == list) :
                listtext = (listtext + "[") 
                for k in range(len(formlist[i])) :
                    listtext = (listtext + formlist[i][k])
                    if(not (k==(len(formlist[i])-1))) :
                        listtext = (listtext + "], ") 
            else :
                listtext = (listtext + formlist[i])
        else :
            listtext = (listtext + "None")
            
        if(not (i==(len(formlist)-1))) :
            listtext = (listtext + ", ")
        if(((i%numperline) == 0) and (not(i==0)) and (i<(len(formlist)-1)) and (not((i+1) == len(formlist))) ) :
            listtext = (listtext + "\n ")
            for j in range(offset) : listtext = (listtext+" ")
            
    listtext = (listtext + "]\n")
        
    return(listtext)

    
"""
#--------------------------------------------------------------------------
#   get the composite forms doc  
#--------------------------------------------------------------------------
"""
def get_composite_form_doc(forms) : 
    
    #load_DC_objects() 
    composite_form_doc_html = ""

    # add each of the forms
    for i in range(len(forms)) : 
        # add the form title
        if(forms[i][FORM_TITLE] != None) :
            if(forms[i][FORM_TYPE] == INPUT_FORM_TYPE) :
                composite_form_doc_html = (composite_form_doc_html + new_line + tabs(1) + 
                                           addformtitle(str(forms[i][FORM_TITLE]),True))
            else :
                composite_form_doc_html = (composite_form_doc_html + new_line + tabs(1) + 
                                           addformtitle(str(forms[i][FORM_TITLE])))
            if( (forms[i][FORM_TYPE] != INPUT_FORM_TYPE) and (forms[i][FORM_TYPE] != CHECKBOX_FORM_TYPE) ) :
                composite_form_doc_html = (composite_form_doc_html + new_line + tabs(1) + 
                                           addblankline(1))
        # add the forms
        if(forms[i][FORM_TYPE] == BUTTON_FORM_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + forms[i][FORM_DATA].get_html())
                
        elif (forms[i][FORM_TYPE] == INPUT_FORM_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + forms[i][FORM_DATA].get_html())
            
        elif (forms[i][FORM_TYPE] == CHECKBOX_FORM_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + forms[i][FORM_DATA].get_html())
            
        elif (forms[i][FORM_TYPE] == BLANK_LINE_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + addblankline(1))
            
        elif (forms[i][FORM_TYPE] == HEADER_LINE_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + new_line + 
                                       "<h" + str(forms[i][FORM_DATA][HEADER_LINE_LEVEL]) +
                                       ">" + forms[i][FORM_DATA][HEADER_LINE_TITLE] +
                                       "</h" + str(forms[i][FORM_DATA][HEADER_LINE_LEVEL]) + ">")
            
        elif (forms[i][FORM_TYPE] == RADIO_FORM_TYPE) :
            composite_form_doc_html = (composite_form_doc_html + forms[i][FORM_DATA].get_html())
    
    return(composite_form_doc_html)


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Button Group Form 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Common Button Group Form html
* -----------------------------------------------------------------------*
"""
button_group_form_start = """
  <div style="margin-top:10px;" """
button_group_form_end = """  </div>"""

button_group_form_div_start = """
    <div class="container dc-container dc-default-input-button-container btn-grp-center">"""
button_group_form_left_div_start = """
    <div class="container dc-container dc-default-input-button-left-container">"""
    
button_group_form_div_end      =   """    </div>
"""

button_group_div_start         =   """      <div class="btn-group btn-center"  """
button_group_div_end           =   """      </div>
"""

regular_button_button_start     =   """        <button type="button" class="btn btn-primary" style = '"""
regular_button_button_end       =   """</button>
"""
    
button_group_form_style = """<style>
    overflow-x: hidden
</style>"""


"""
* -----------------------------------------------------------------------*
* Common Button Group helper functions
* -----------------------------------------------------------------------*
"""
def getbuttonsizing(buttonGroup) :
    
    # calculate the height of the button bar
    maxnewlines     =   0
    height          =   0
    width           =   0
    width_type      =   "px"

    # calculate the height the buttons
    for i in range(len(buttonGroup.get_keyList())) :
        newlines = 0
        
        for j in range(len(buttonGroup.get_keyList()[i])) :
            if(j<(len(buttonGroup.get_keyList()[i]) - 4)) :
                if(buttonGroup.get_keyList()[i][j:(j+5)] == "</br>") :
                    newlines += 1
        if(newlines > maxnewlines) :
            maxnewlines = newlines
    
    if(maxnewlines == 0) :
        if(buttonGroup.get_centered()) : 
            height = CENTERED_BUTTON_HEIGHT
        else : 
            height = BUTTON_HEIGHT
    else :
        height = (maxnewlines+1)*MULTI_LINE_BUTTON_HEIGHT

    # calculate the average width of the buttons
    import math
    if(buttonGroup.get_gridwidth() == 0) :
        width       =   math.floor(100 / len(buttonGroup.get_keyList()))
        width_type  =   "%"
    else :
        if(buttonGroup.get_custombwidth() == 0) :
            width   =   math.floor(buttonGroup.get_gridwidth() / len(buttonGroup.get_keyList()))
            width_type  =   "px"
        else :
            width = buttonGroup.get_custombwidth()
    
    # calculate the left margin of the buttons
    margin = 0
    
    if(buttonGroup.get_centered()) :
        if(buttonGroup.get_gridwidth() > 0) :
            
            gridwithadjust  =   math.floor(buttonGroup.get_gridwidth()*0.02)
            import math
            margin  =   math.floor(((buttonGroup.get_gridwidth()-gridwithadjust) - (len(buttonGroup.get_keyList()) * width)) / 2)
            if(margin < 0) :
                margin = 0
        else :
            margin  =   math.floor((100 - (width*len(buttonGroup.get_keyList()))) / 2)
        
    return(height, (str(width) + width_type), margin)
    
def get_button_style(index, height, width, margin, buttonGroup) :

    html    = ""
    
    if((index==0)) :
        if(buttonGroup.get_customstyle() == None) :
            if(buttonGroup.get_gridwidth() == 0) :
                html = (html + addstyleattribute("margin-left",str(margin) + "%"))
            else :
                html = (html + addstyleattribute("margin-left",str(margin) + "px"))
                
        else :
            html = (html + addstyleattribute("margin-left",str(margin) + "px"))
            
    html = (html + addstyleattribute("height",str(height)+"px"))
    html = (html + addstyleattribute("width",width) + "'")
    
    return(html)

def get_button_div_style(margin) :
    
    html = ""
    html = (html + "style='" + addstyleattribute("margin",
                                                 "0% 0% 0% "+str(margin)+"%") + "'>" + new_line)
    return(html)


def get_regular_button(buttonGroup,index) :
    
    regular_html = ""

    if(buttonGroup.get_customstyle() is None) :
        height, width, margin = getbuttonsizing(buttonGroup)
        #print("get_regular_button",height, width, margin)
        
    else :
        height = buttonGroup.get_customstyle().get("height")
        width  = str(buttonGroup.get_customstyle().get("width")) + "px"

        if(buttonGroup.get_customstyle().get("left-margin") == 0) :
            import math
            margin  =   math.floor(((buttonGroup.get_gridwidth()) - (len(buttonGroup.get_keyList()) * buttonGroup.get_customstyle().get("width"))) / 2) 
        else :
            margin = buttonGroup.get_customstyle().get("left-margin")
        
    regular_html = (regular_html + regular_button_button_start)
    
    if(not (buttonGroup.get_customstyle() is None)) :
        fontsize    =   buttonGroup.get_customstyle().get("font-size",None)
        if(not(fontsize is None)) :
            regular_html = (regular_html + addstyleattribute("font-size",str(fontsize)+"px"))
    
    regular_html = (regular_html + get_button_style(index,height,width,margin,buttonGroup))
        
    regular_html = (regular_html + addattribute("onclick",buttonGroup.get_jsList()[index]))
    regular_html = (regular_html + ">" + buttonGroup.get_keyList()[index])
    regular_html = (regular_html + regular_button_button_end)

    return(regular_html)

"""
* -----------------------------------------------------------------------*
* Common Button Group Form class
* -----------------------------------------------------------------------*
*
*   ATTRIBUTES
*
*   formid          -   html id for form
*   keyList         -   key text list
*   jsList          -   list of javascript callbacks
*   centered        -   flag to determine if form is centered
*   short           -   flag if button bar is short (not full page width)
*   inform          -   if button group within another form
*   custom          -   custom form parms (dict 'keywidth' and 'leftmargin')
*  
* -----------------------------------------------------------------------*
"""
class ButtonGroupForm :
   
    # full constructor
    def __init__(self,    
                 formid         =   "",
                 keyList        =   [],
                 jsList         =   [],
                 centered       =   False,
                 gridwidth      =   0,
                 custombwidth   =   0,
                 customstyle    =   None) :
        
        # instance variables

        # minimum init attributes
        self.formid         =   formid
        self.keyList        =   keyList
        self.jsList         =   jsList
        self.centered       =   centered
        
        # minimum form data attributes
        self.gridwidth      =   gridwidth
        self.custombwidth   =   custombwidth
        self.customstyle    =   customstyle
        
    def get_formid(self) :
        return(self.formid)
    def set_formid(self,setParm) :
        self.formid = setParm
    def get_keyList(self) :
        return(self.keyList)
    def set_keyList(self,setParm) :
        self.keyList = setParm
    def get_jsList(self) :
        return(self.jsList)
    def set_jsList(self,setParm) :
        self.jsList = setParm
    def get_centered(self) :
        return(self.centered)
    def set_centered(self,setParm) :
        self.centered = setParm
    def get_gridwidth(self) :
        return(self.gridwidth)
    def set_gridwidth(self,setParm) :
        self.gridwidth = setParm
    def get_custombwidth(self) :
        return(self.custombwidth)
    def set_custombwidth(self,setParm) :
        self.custombwidth = setParm
    def get_customstyle(self) :
        return(self.customstyle)
    def set_customstyle(self,setParm) :
        self.customstyle = setParm

    def get_html(self) :
        
        #self.dump()
        button_group_form_html = ""

        button_group_form_html = (button_group_form_html + button_group_form_start + addattribute("id",self.get_formid()) + ">")
            
        if((len(self.get_keyList()) == 1) and (not(self.get_centered()))) :
            button_group_form_html = (button_group_form_html + button_group_form_left_div_start + new_line)
        else :    
            button_group_form_html = (button_group_form_html + button_group_form_div_start + new_line)
        
        if(self.get_gridwidth() == 0) :
            button_group_form_html = (button_group_form_html + button_group_div_start + addattribute("style",addstyleattribute("width","100%")) + ">" + new_line)
        else :
            button_group_form_html = (button_group_form_html + button_group_div_start + addattribute("style",addstyleattribute("width",str(self.get_gridwidth()) + "px")) + ">" + new_line)
    
        # for each button in the list
        for i in range(len(self.get_keyList())) :
        
            button_group_form_html = (button_group_form_html + get_regular_button(self,i))
        
        button_group_form_html = (button_group_form_html + button_group_div_end)
        button_group_form_html = (button_group_form_html + button_group_form_div_end)
        button_group_form_html = (button_group_form_html + button_group_form_end)
    
        if((self.get_formid() == "#coluniquesnormaloptionstb") or (self.get_formid() == "#inspectionoptionstb") ):
            self.dump()
            print(button_group_form_html)

        return(button_group_form_html)


    def dump(self) :

        print("\nformid          [0] : ",self.get_formid())
        print("keyList         [1] : ["+ str(len(self.get_keyList())) + "] "+ "] " + dump_form_list(self.get_keyList(),27,4))
        print("jsList          [2] : ["+ str(len(self.get_jsList())) + "] "+ "] " + dump_form_list(self.get_jsList(),27,2))
        print("centered        [3] : ",self.get_centered())
        print("gridwidth       [7] : ",self.get_gridwidth())
        print("custombwidth    [8] : ",self.get_custombwidth())
        print("customstyle     [9] : ",self.get_customstyle())


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Input Group Form elements
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Common Input Group Form html
* -----------------------------------------------------------------------*
"""
input_group_form_start          = ("""<div class='dc-default-input-div'>""")
input_group_short_form_start    = ("""<div class='dc-default-short-input-div'>""")
input_group_grid_form_start     = ("""<div """)

input_group_form_end = ("""
</div>""")
input_group_grid_form_end     = """
</div>"""

input_group_form_top = ("""<div class='container' style=' padding:5px; margin:auto; width:99%; """)
input_group_form_pop_up_top = ("""<div class='container' style=' padding:5px; margin:auto; width:99%; background-color:#F8F5E1; """)
                        
input_group_short_form_top = ("""  <div class='container' style=' padding:5px; margin:auto; width:99%; """)
input_group_short_form_pop_up_top = ("""  <div class='container' style=' padding:5px; margin:auto; width:99%; background-color:#F8F5E1; """)

input_group_custom_form_top =   """  <div class="container dc-container" style='width: """ 
input_group_custom_form_pop_up_top =   """  <div class='container dc-container' """ + addstyleattribute("background-color","#F8F5E1") + """style='width: """ 
 
input_group_custom_form_top1 =  """ padding:5px; border: 1px solid #428bca;'"""
                        
input_group_form_bottom = """  </div>"""

input_group_div_top = "    <div class='container dc-container dc-default-input-inner-div'>"# dc-container dc-default-input-inner-div'>"# style=' margin-bottom:10px; overflow-y:hidden;'>"


input_group_form_div_start = (new_line + tabs(2) + "  <div class='form-group-sm'>")
input_group_form_div_textarea_start = (new_line + tabs(2) + """<div class="form-group-sm" style="height:120px" >""")

input_group_form_div_end = (new_line + tabs(2) + """  </div>""")

input_group_form_label_start = (new_line + tabs(3) + """<label """)
input_group_form_small_label_start = (new_line + tabs(3) + """  <label """)

input_group_form_label_end = """</label>"""
input_group_form_small_label_end = """</label>"""
#input_group_form_small_label_end = ("""</label>"""  + new_line + 
#                                    tabs(3) + """</div>""")
   
input_group_form_input_start = (new_line + tabs(3) + """  <input """)
input_group_form_input_end = "></input>"

input_group_form_textarea_start = (new_line + tabs(3) + """  <textarea """)
input_group_form_textarea_end = "></textarea>"
input_group_form_textarea1_end = "</textarea>"

input_group_form_button_start = (new_line + """    <button type='button' class='btn btn-primary' onclick='""")
input_group_form_button_end = """</button>"""

input_group_fullparms_start = """
        <div class="panel-heading dc-table-panel-heading">
"""
input_group_fullparms_middle = """            <button class="btn-group dc-show-full" """ 
input_group_fullparms_custom_middle = """            <button class="btn-group dc-show-full" """ 

input_group_fullparms_middle1 = """ OnClick="getfullparms("""
input_group_fullparms_end = """)">Show All Parameters</button>
        </div>
"""

input_group_select_start = (new_line + tabs(2) + """        <select """)
input_group_select_multiple_start = (new_line + tabs(2) + """        <select multiple """)
input_group_select_middle = """  style="margin-left:1px; font-size: 11px;" class="form-control"> 
"""
input_group_select_end = (tabs(2) + """        </select>""")





"""
* -----------------------------------------------------------------------*
* Common Input Group Form helper functions
* -----------------------------------------------------------------------*
"""
def get_num_inputs(idList) :

    pcount = 0;
    for i in range(len(idList)) :
        if(idList[i] != None) : pcount = pcount + 1
    
    return(pcount)

NOT_DISPLAYED   =   0
REQUIRED        =   1
DISPLAYED       =   2


def should_display(idList,reqList,i,parmsList) :

    for j in range(len(reqList)) :
        if(reqList[j] == i) :
            return(REQUIRED)
    
    if(not (parmsList is None)) :
        if(i < len(parmsList)) :
            if( not (parmsList[i] == "")) :
                return(DISPLAYED)
            else :
                return(NOT_DISPLAYED)
    else :
        return(NOT_DISPLAYED)    


def get_form_parms(formid,idList) :
    
    formParms = cfg.get_config_value(formid + "Parms")

    if(formParms == None) :
        return(None)
    else :
        
        for i in range(len(formParms)) :
            if( not(isinstance(formParms[i], str))) :
                cfg.drop_config_value(formid + "Parms")
                print("drop non string parm",formid)
                return(None)
        
        totalids = 0
        
        # strip Nones 
        for i in range(len(idList)) :
            if(not(idList[i] == None)) : totalids = totalids + 1
            
        if(len(formParms) == totalids) :
            return(formParms)
        else :
            print("drop len err parm",formid,len(formParms),totalids)
            cfg.drop_config_value(formid + "Parms")
            return(None)
    
def display_full_parms(formid,idList,reqList) :

    formParms = get_form_parms(formid,idList)

    # if no previous parms defined display all parms
    if(formParms == None) :
        return(True)
    else :
        
        pcount = get_num_inputs(idList);
        
        if(pcount == len(reqList)) :
            return(True)
            
        fcount = 0;
        
        for i in range(len(formParms)) :
            if(len(formParms[i]) > 0) : fcount = fcount + 1
    
        # if full set of previous parms  
        if(pcount == fcount)    : return(True)
        
        # if no previous parms  
        if(fcount == 0)         : return(True)
    
    return(False)

"""
* -----------------------------------------------------------------------*
* Common Input Group Form class
* -----------------------------------------------------------------------*
*
*   ATTRIBUTES
*
*   formid          -   html id for form
*   idList          -   html id for inputs
*   labelList       -   labels for inputs
*   typeList        -   data types id for inputs
*   placeholderList -   placeholders for inputs
*   jsList          -   list of javascript callbacks
*   reqList         -   list of flags to determine if parm is required
*   centered        -   flag to determine if form is centered
*   shortForm       -   flag if form is short (not full page width)
*   custom          -   custom form parms (dict 'width' and 'nokeys')
*   fullparms       -   flag to display all parms or just required
*   gridwidth       -   width of form in px
*
* -----------------------------------------------------------------------*
"""
class InputForm :

    # full constructor
    def __init__(self,    
                 formid             =   "",
                 idList             =   [],
                 labelList          =   [],
                 typeList           =   [],
                 placeholderList    =   [],
                 jsList             =   [],
                 reqList            =   [],
                 
                 shortForm          =   False,
                 fullparms          =   False,
                 gridwidth          =   0,
                 custombwidth       =   0,
                 buttonstyle        =   None) :
        
        # instance variables

        # minimum init attributes
        self.formid             =   formid
        self.idList             =   idList
        self.labelList          =   labelList
        self.typeList           =   typeList
        self.placeholderList    =   placeholderList
        self.jsList             =   jsList
        self.reqList            =   reqList
        
        # minimum form data attributes
        self.shortForm          =   shortForm
        self.fullparms          =   fullparms
        self.gridwidth          =   gridwidth
        self.custombwidth       =   custombwidth
        self.buttonstyle        =   buttonstyle
        self.borderwidth        =   0
        
        self.selectDict         =   {}

    def get_formid(self) :
        return(self.formid)
    def set_formid(self,setParm) :
        self.formid = setParm
    def get_idList(self) :
        return(self.idList)
    def set_idList(self,setParm) :
        self.idList = setParm
    def get_labelList(self) :
        return(self.labelList)
    def set_labelList(self,setParm) :
        self.labelList = setParm
    def get_typeList(self) :
        return(self.typeList)
    def set_typeList(self,setParm) :
        self.typeList = setParm
    def get_placeholderList(self) :
        return(self.placeholderList)
    def set_placeholderList(self,setParm) :
        self.placeholderList = setParm
    def get_jsList(self) :
        return(self.jsList)
    def set_jsList(self,setParm) :
        self.jsList = setParm
    def get_reqList(self) :
        return(self.reqList)
    def set_reqList(self,setParm) :
        self.reqList = setParm
    def get_shortForm(self) :
        return(self.shortForm)
    def set_shortForm(self,setParm) :
        self.shortForm = setParm
    def get_fullparms(self) :
        return(self.fullparms)
    def set_fullparms(self,setParm) :
        self.fullparms = setParm
    def get_gridwidth(self) :
        return(self.gridwidth)
    def set_gridwidth(self,setParm) :
        self.gridwidth = setParm
    def get_custombwidth(self) :
        return(self.custombwidth)
    def set_custombwidth(self,setParm) :
        self.custombwidth = setParm
    def get_buttonstyle(self) :
        return(self.buttonstyle)
    def set_buttonstyle(self,setParm) :
        self.buttonstyle = setParm
    def get_borderwidth(self) :
        return(self.borderwidth)
    def set_borderwidth(self,width) :
        self.borderwidth = width
        
    def get_select_default(self,idkey) :
        seldict     =   self.selectDict.get(idkey,None) 
        if(not (seldict == None)) :
            return(seldict.get("default",None))
        else :
            return(None)
    
    def get_select_current(self,idkey) :
        seldict     =   self.selectDict.get(idkey,None) 
        if(not (seldict == None)) :
            return(seldict.get("current",None))
        else :
            return(seldict.get("default",None))
    
    def get_select_callback(self,idkey) :
        seldict     =   self.selectDict.get(idkey,None) 
        if(not (seldict == None)) :
            return(seldict.get("callback",None))
        else :
            return(None)
            
    def get_select_list(self,idkey) :
        seldict     =   self.selectDict.get(idkey,None) 
        if(not (seldict == None)) :
            return(seldict.get("list",None))
        else :
            return(None)
       
    def add_select_dict(self,formid,parmidsList,parmid,seldict) :
        
        from dfcleanser.common.cfg import get_config_value
        parmslist   =   get_config_value(formid+"Parms")
    
        if(parmslist is None) :
            seldict.update({"current" : seldict.get("default")})
        else :
        
            found   =   False
            
            for i in range(len(parmidsList)) :
                if(parmidsList[i] == parmid) :
                    if(parmslist[i] is None ) :
                        seldict.update({"current" : seldict.get("default")}) 
                    else :
                        seldict.update({"current" : parmslist[i]})
                    found   =   True
                    break;
            
            if(not found) :
                seldict.update({"current" : seldict.get("default")})    
                    
        self.selectDict.update({parmid:seldict})
        
    def get_select_html(self,idkey,fparm) :

        selhtml     =   ""
        
        options =   self.get_select_list(idkey)

        for i in range(len(options)) :
            selhtml     =   (selhtml + tabs(3) + "        <option style='text-align:left; font-size:11px;'")
            
            if(fparm is None) :
                if(options[i] == self.get_select_current(idkey)) :
                    selhtml     =   (selhtml + " selected")
            else :
                if(options[i] == fparm) :
                    selhtml     =   (selhtml + " selected")
                
            selhtml     =   (selhtml + ">" + options[i] + "</option>")
            if(i < len(options)) :
                selhtml     =   (selhtml + new_line)    
        
        return(selhtml)
        
    def get_html(self) :
        
        if(debugFlag) : 
            self.dump()
        if(self.get_formid() == "#datainspectcolsearch") :
           self.dump()                  
        
        input_group_form_html = ""
        if(self.get_gridwidth() > 0) :
            input_group_form_html = (input_group_form_html + input_group_grid_form_start + "style='margin-left:auto; margin-right:auto; width:" + str(self.get_gridwidth()) + "px;'>")
        else :
            if(self.get_shortForm()) :
                input_group_form_html = (input_group_form_html + input_group_short_form_start)
            else :
                input_group_form_html = (input_group_form_html + input_group_form_start)

        bkeyList    =   []
        bjsList     =   []
        bcount      =   0

        # add to fullparms repositiry
        add_Input(self.get_formid(),self.get_idList(),self.get_labelList(),
                  self.get_typeList(),self.get_placeholderList(),
                  self.get_jsList(),self.get_reqList(),self.get_shortForm(),
                  self.get_buttonstyle())

        customWidth = 0
        noKeys      = False
    
        if(customWidth == 0) :
            if(self.get_shortForm()) :
                if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_short_form_top)
                    if(self.get_borderwidth() == 0) :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border","0px") + "'")
                    else :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border",str(self.get_borderwidth()) + "px solid #428bca;") + "'")
                else :
                    input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_short_form_pop_up_top ) 
                    if(self.get_borderwidth() == 0) :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border","0px") + "'")
                    else :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border",str(self.get_borderwidth()) + "px solid #428bca;") + "'")
            else :
                if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                    input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_form_top)
                    if(self.get_borderwidth() == 0) :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border","0px") + "'")
                    else :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border",str(self.get_borderwidth()) + "px solid #428bca;") + "'")
                else :
                    input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_form_pop_up_top)
                    if(self.get_borderwidth() == 0) :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border","0px") + "'")
                    else :
                        input_group_form_html = (input_group_form_html + addstyleattribute("border",str(self.get_borderwidth()) + "px solid #428bca;") + "'")
                    
        else :
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_custom_form_top + str(customWidth) + "%;")
            else :
                input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_custom_form_pop_up_top + str(customWidth) + "%;")
    
        input_group_form_html = (input_group_form_html + addattribute("id",self.get_formid()) +">")

        if(self.get_fullparms()) :
            display_all_flag = True
        else :
            display_all_flag = display_full_parms(self.get_formid(),self.get_idList(),self.get_reqList())

        if(not display_all_flag) :
            input_group_form_html = (input_group_form_html + input_group_fullparms_start)
            input_group_form_html = (input_group_form_html + input_group_fullparms_middle)
                
            input_group_form_html = (input_group_form_html + addattribute("id",self.get_formid()+"fullparms"))
            input_group_form_html = (input_group_form_html + input_group_fullparms_middle1)
            input_group_form_html = (input_group_form_html + single_quote(self.get_formid()))
            input_group_form_html = (input_group_form_html + input_group_fullparms_end)
    
        input_group_form_html = (input_group_form_html + new_line + tabs(1) + input_group_div_top)

        # check if input form has saved values
        formParms = get_form_parms(self.get_formid(),self.get_idList())
    
        if(formParms != None) : 
            if(len(formParms) == 0) : formParms = None
            
        formParmsProtect = None
        if(formParms != None) :
            formParmsProtect = cfg.get_config_value(self.get_formid() + "ParmsProtect")
    
        # for each input in form
        for i in range(len(self.get_idList())) : 
            
            if(self.get_idList()[i] is None)    :   
                display_flag    =   REQUIRED
            else :
                display_flag    =   should_display(self.get_idList(),self.get_reqList(),i,formParms)
            
            
            if( (display_all_flag) or (display_flag == REQUIRED) or (display_flag == DISPLAYED)) :
        
                if( (self.get_typeList()[i] == "text") or 
                    (self.get_typeList()[i] == "textarea") or 
                    (self.get_typeList()[i] == "file") or 
                    (isenlargedtextarea(self.get_typeList()[i]))) : 

                    # add the div for each input line>
                    input_group_form_html = (input_group_form_html + tabs(3) + 
                                             input_group_form_div_start)
    
                    # add the label for each input line
                    if( not self.get_shortForm()) :
                        input_group_form_html = (input_group_form_html + input_group_form_label_start)
                    else :
                        input_group_form_html = (input_group_form_html + input_group_form_small_label_start)
                    
                    inputelementId = self.get_idList()[i]
                    input_group_form_html = (input_group_form_html + 
                                             addattribute("for",inputelementId))
                    
                    # add the label for each input line
                    if( not self.get_shortForm()) :
                        input_group_form_html = (input_group_form_html + addattribute("style","text-align:left; font-size: 11px;"))
                    else :
                        input_group_form_html = (input_group_form_html + addattribute("style","text-align:left; font-size: 11px;"))
                    

                    input_group_form_html = (input_group_form_html + ">")

                    if(display_flag == REQUIRED) :
                        input_group_form_html = (input_group_form_html + "* " + self.get_labelList()[i])    
                    else :    
                        input_group_form_html = (input_group_form_html + self.get_labelList()[i])
                
                    if( not self.get_shortForm()) :
                        input_group_form_html = (input_group_form_html + input_group_form_label_end)
                    else :
                        input_group_form_html = (input_group_form_html + input_group_form_small_label_end)
 
                    # add the input for each input line
                    if((self.get_typeList()[i] == "text") or (self.get_typeList()[i] == "file")) :
                        input_group_form_html = (input_group_form_html + input_group_form_input_start)
                    else : 
                        input_group_form_html = (input_group_form_html + input_group_form_textarea_start)

                    if(self.get_typeList()[i] == "file") :
                        input_group_form_html = (input_group_form_html + addattribute("type","text"))
                        input_group_form_html = (input_group_form_html + addattribute("class","form-control"))
                        input_group_form_html = (input_group_form_html + addattribute("style","font-size: 11px;"))
                    else :
                        if( (self.get_typeList()[i] == "textarea") or (isenlargedtextarea(self.get_typeList()[i])) ) :
                            if(self.get_typeList()[i] != "textarea") :
                                input_group_form_html = (input_group_form_html + addattribute("rows",gettextarearows(self.get_typeList()[i])))
                            else :
                                input_group_form_html = (input_group_form_html + addattribute("rows",3))
                        else :         
                            input_group_form_html = (input_group_form_html + addattribute("type",self.get_typeList()[i])) 
                   
                        input_group_form_html = (input_group_form_html + addattribute("class","form-control"))
                        input_group_form_html = (input_group_form_html + addattribute("style","text-align:left; font-size: 11px;"))
                
                    input_group_form_html = (input_group_form_html + addattribute("id",self.get_idList()[i]))#"input" + formid + idList[i]))
                    input_group_form_html = (input_group_form_html + addattribute("placeholder",self.get_placeholderList()[i]))
            
                    # add the stored input values
                    if(formParms != None) :
                        if(type(formParms[i]) == list) :
                            iparm = str(formParms[i])
                            iparm = iparm.strip("]")
                            iparm = iparm.strip("[")
                    
                        elif(type(formParms) == str) :
                            iparm = formParms
                        else :
                            iparm = formParms[i]
                    
                        if( (self.get_typeList()[i] == "textarea") or (isenlargedtextarea(self.get_typeList()[i])) ) :
                            if(formParmsProtect != None) :
                                if(formParmsProtect[i] == True) :
                                    input_group_form_html = (input_group_form_html + " readonly>" + iparm)
                                else :
                                    input_group_form_html = (input_group_form_html + ">" + iparm)
                            else:
                                input_group_form_html = (input_group_form_html + ">" + iparm)
                                
                        else :
                            if(formParmsProtect == None) :
                                input_group_form_html = (input_group_form_html + addattribute("value",iparm))
                            else :
                                if(formParmsProtect[i] == True) :
                                    input_group_form_html = (input_group_form_html + addattribute("value",iparm) + " readonly")
                                else : 
                                    input_group_form_html = (input_group_form_html + addattribute("value",iparm))
                            
                    if( (self.get_typeList()[i] == "textarea") or (isenlargedtextarea(self.get_typeList()[i])) ) :
                        if(formParms != None) :
                            input_group_form_html = (input_group_form_html + input_group_form_textarea1_end)
                        else :    
                            input_group_form_html = (input_group_form_html + input_group_form_textarea_end) 
                    else : 
                        input_group_form_html = (input_group_form_html + input_group_form_input_end)
    
                    if(self.get_typeList()[i] == "file") :
                
                        input_group_form_html = (input_group_form_html + input_group_form_input_start)
                        input_group_form_html = (input_group_form_html + addattribute("type",self.get_typeList()[i]))
                
                        if(customWidth > 0) :
                            input_group_form_html = (input_group_form_html + addattribute("style","width:" + str("100%") + ";"))
                    
                        fileelementID = "file" + self.get_idList()[i]
                        input_group_form_html = (input_group_form_html + addattribute("id",fileelementID))

                        input_group_form_html = (input_group_form_html + 
                                                 addattribute("onchange","javascript:" + 
                                                              "onChangefileselect('" +
                                                              inputelementId + "','" + 
                                                              fileelementID + "')"))
                        input_group_form_html = (input_group_form_html + 
                                                 addattribute("class","btn btn-primary"))
                        input_group_form_html = (input_group_form_html + 
                                                 addattribute("style",(addstyleattribute("width","100%") +
                                                                       addstyleattribute("font-size","12px") +
                                                                       addstyleattribute("color","#cfdbee")) ))
                        input_group_form_html = (input_group_form_html + input_group_form_input_end)
                
                    # end the div for each input line
                    input_group_form_html = (input_group_form_html + input_group_form_div_end)
            
                elif( (self.get_typeList()[i] == "select") or (self.get_typeList()[i] == "selectmultiple") ):

                    # add the label for the select
                    input_group_form_html = (input_group_form_html + input_group_form_div_start)
                     
                    if( not self.get_shortForm()) :
                        input_group_form_html = (input_group_form_html + input_group_form_label_start)
                    else :
                        input_group_form_html = (input_group_form_html + input_group_form_small_label_start)
                    
                    input_group_form_html = (input_group_form_html + 
                                             addattribute("for",self.get_idList()[i]))
                    
                    input_group_form_html = (input_group_form_html + " style='text-align:left; font-size: 11px;'")    
                        
                    input_group_form_html = (input_group_form_html + ">")
                    
                    if(display_flag == REQUIRED) :
                        input_group_form_html = (input_group_form_html + "* " + self.get_labelList()[i])    
                    else :    
                        input_group_form_html = (input_group_form_html + self.get_labelList()[i])
                    
                    if( not self.get_shortForm()) :
                        input_group_form_html = (input_group_form_html + input_group_form_label_end)
                    else :
                        input_group_form_html = (input_group_form_html + input_group_form_small_label_end)

                    if(self.get_typeList()[i] == "select") :
                        input_group_form_html = (input_group_form_html + input_group_select_start)
                    else :
                        input_group_form_html = (input_group_form_html + input_group_select_multiple_start)

                    # add onchange event handler
                    if(not (self.get_select_callback(self.get_idList()[i])) == None) :
                        input_group_form_html = (input_group_form_html + "onChange=" + '"' +
                                                 self.get_select_callback(self.get_idList()[i]) +
                                                 "('" + self.get_idList()[i] + "')" + '"')
                    
                    input_group_form_html = (input_group_form_html + addattribute("id",self.get_idList()[i])) 
                    input_group_form_html = (input_group_form_html + input_group_select_middle)
                    
                    if(not (formParms is None)) :
                        fparm   =   formParms[i]
                    else :
                        fparm   =   None
                    
                    input_group_form_html = (input_group_form_html + self.get_select_html(self.get_idList()[i],fparm))

                    input_group_form_html = (input_group_form_html + input_group_select_end)
                    input_group_form_html = (input_group_form_html + input_group_form_div_end)
                    
                else :
            
                    if( (self.get_typeList()[i] == "button") and (not noKeys) ): 
                
                        bkeyList.append(self.get_labelList()[i])
                        bjsList.append(self.get_jsList()[i])
                        bcount  =   bcount + 1
                
        # end the form
        input_group_form_html = (input_group_form_html + new_line + tabs(1) + "   </div>")
        #input_group_form_html = (input_group_form_html + new_line + input_group_form_bottom)
                    
        # check if need to append buttons at bottom
        if(bcount > 0) :

            input_group_form_html = (input_group_form_html + ButtonGroupForm(self.get_formid() +"tb",
                                                                             bkeyList,
                                                                             bjsList,
                                                                             True,
                                                                             self.get_gridwidth(),
                                                                             self.get_custombwidth(),
                                                                             self.get_buttonstyle()).get_html())

        input_group_form_html = (input_group_form_html + new_line + input_group_form_bottom)
        
        input_group_form_html = (input_group_form_html + input_group_form_end)

        if((self.get_formid() == "#importPandasCSV") or (self.get_formid() == "#setnewcoltransform") or (self.get_formid() == "$$addcolcodeInput") ) :   
            print(input_group_form_html)
            self.dump()

        return(input_group_form_html)

    def dump(self) :

        print("\nformid          [0] : ",self.get_formid())
        print("idList          [1] : ["+ str(len(self.get_idList())) + "] " + dump_form_list(self.get_idList(),27,5))
        print("labelList       [2] : ["+ str(len(self.get_labelList())) + "] " + dump_form_list(self.get_labelList(),27,5))
        print("typeList        [3] : ["+ str(len(self.get_typeList())) + "] " + dump_form_list(self.get_typeList(),27,15))
        print("placeholderList [4] : ["+ str(len(self.get_placeholderList())) + "] " + dump_form_list(self.get_placeholderList(),27,1))
        print("jsList          [5] : ["+ str(len(self.get_jsList())) + "] " + dump_form_list(self.get_jsList(),27,1))
        print("reqList         [6] : ",self.get_reqList())
        print("shortform       [7] : ",self.get_shortForm())
        print("fullparms       [8] : ",self.get_fullparms())
        print("gridwidth       [9] : ",self.get_gridwidth())
        print("custombwidth    [10]: ",self.get_custombwidth())
        print("buttonstyle     [11]: ",self.get_buttonstyle())
        
        if(len(self.selectDict) > 0) :
            print("select lists    [12]: ",len(self.selectDict))
            ids     =   list(self.selectDict.keys())
            for i in range(len(ids)) :
                print("\n   Id : ",ids[i],"\n")
                print("     defaullt : ",self.get_select_default(ids[i]))
                print("     list     : ",self.get_select_list(ids[i]))


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Checkbox Group Form elements
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Common Checkbox Group html 
* -----------------------------------------------------------------------*
"""
checkbox_group_form_start   = new_line + ("""  <form class="container dc-container" style='""" + 
                                          addstyleattribute("width","100%") + """'""")
checkbox_group_form_pop_up_start   = new_line + ("""  <form class="container dc-container" style='""" + 
                                          addstyleattribute("background-color","#F8F5E1") + addstyleattribute("width","100%") + """'""")
checkbox_group_form_end     = new_line + """  </form>"""

checkbox_group_div_start    = new_line + """   <div class='container dc-container'>"""
checkbox_group_div_end      = new_line + """   </div>"""

checkbox_group_div1_start   = new_line + """     <div class='row text-left' style='margin: 0px auto; text-align:center;'>"""
checkbox_group_div1_end     = new_line + """     </div>"""

checkbox_group_label_start  = new_line + """       <label class='btn btn-primary' """
checkbox_group_label_end    = """><span class='badge'>&check;</span></label>"""

checkbox_group_input_start  = """ <input type='checkbox' class='badgebox' """


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Bootstrap Badgebox (checkbox) Group Form class
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
*
*   ATTRIBUTES
*
*   formid          -   html id for form
*   idList          -   html id for inputs
*   labelList       -   labels for inputs
*   jsList          -   list of javascript callbacks
*   chklist         -   list of flags to determine if checked
*   disabledlist    -   flag to determine if disabled
*
* -----------------------------------------------------------------------*
"""

class CheckboxGroupForm :
    
    # full constructor
    def __init__(self,    
                 formid         =   "",
                 idList         =   [],
                 labelList      =   [],
                 jsList         =   [],
                 chklist        =   [],
                 disabledlist   =   []) :

        
        # instance variables

        # minimum init attributes
        self.formid         =   formid
        self.idList         =   idList
        self.labelList      =   labelList
        self.jsList         =   jsList
        self.chklist        =   chklist
        
        # minimum form data attributes
        self.disabledlist   =   disabledlist
        self.rowscount      =   None

    def get_formid(self) :
        return(self.formid)
    def set_formid(self,setParm) :
        self.formid = setParm
    def get_idList(self) :
        return(self.idList)
    def set_idList(self,setParm) :
        self.idList = setParm
    def get_labelList(self) :
        return(self.labelList)
    def set_labelList(self,setParm) :
        self.labelList = setParm
    def get_jsList(self) :
        return(self.jsList)
    def set_jsList(self,setParm) :
        self.jsList = setParm
    def get_chklist(self) :
        return(self.chklist)
    def set_chklist(self,setParm) :
        self.chklist = setParm
    def get_disabledlist(self) :
        return(self.disabledlist)
    def set_disabledlist(self,setParm) :
        self.disabledlist = setParm
    def get_rows_count(self) :
        return(self.rowscount)
    def set_rows_count(self,setParm) :
        self.rowscount = setParm

    def get_html(self) :

        if(debugFlag) : 
            self.dump()

        checkbox_group_form_html = ""
        
        # begin the form  
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_form_start)
        else :
            checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_form_pop_up_start)
        
        checkbox_group_form_html = (checkbox_group_form_html + addattribute("id",self.formid)+">")
    
        checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_div_start)
        
        if(self.get_rows_count() is None) :
            numrows     =   1
        else :
            numrows     =   len(self.get_rows_count())
        
        current_cb  =   0
        
        for j in range(numrows) :
            
            checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_div1_start)    
            
            if(self.get_rows_count() is None) :
                numcbs     =   len(self.get_idList())
            else :
                numcbs     =   self.get_rows_count()[j]
            
            # add each of the checkboxws
            for i in range(numcbs) : 
        
                # add the checkbox label
                checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_label_start)
                checkbox_group_form_html = (checkbox_group_form_html + addattribute("for",self.get_idList()[current_cb]))
                checkbox_group_form_html = (checkbox_group_form_html + ">" + self.get_labelList()[current_cb] + " ")

                checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_input_start)
                checkbox_group_form_html = (checkbox_group_form_html + addattribute("id",self.get_idList()[current_cb]))
        
                if(len(self.get_chklist()) > 0) :
                    if(self.get_chklist()[current_cb]) :
                        checkbox_group_form_html = (checkbox_group_form_html + " checked")    
            
                if(len(self.get_disabledlist()) > 0) :
                    if(self.get_disabledlist()[current_cb]) :
                        checkbox_group_form_html = (checkbox_group_form_html + " disabled")    
        
                checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_label_end)
                
                current_cb  =   current_cb + 1

            # end the form
            checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_div1_end)
            
            if(not(self.get_rows_count() is None)) :
                if(not (j == (len(self.get_rows_count()) -1))) :
                    checkbox_group_form_html = (checkbox_group_form_html + "<br>")
            
            
        checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_div_end)
        checkbox_group_form_html = (checkbox_group_form_html + checkbox_group_form_end)

        if((self.get_formid() == "dceulaform") or (self.get_formid() == "dropcolsinput") or (self.get_formid() == "addcolcodeInput") ) :   
            print(checkbox_group_form_html)
        
        return(checkbox_group_form_html)


    def dump(self) :

        print("\nformid          [0] : ",self.get_formid())
        print("idList          [1] : ",self.get_idList())
        print("labelList       [2] : ",self.get_labelList())
        print("jsList          [3] : ",self.get_jsList())
        print("chklist         [4] : ",self.get_chklist())
        print("disabledlist    [5] : ",self.get_disabledlist())



    
"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Radio Form elements 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Common Radio Form html 
* -----------------------------------------------------------------------*
"""
radio_container_start = """<div class='container dc-container'>"""
radio_container_end   = """</div>"""

radio_div_start = """  <div class="text-center">"""
radio_div_end   = """  </div>"""

radio_div1_start = """    <div class='btn-group' """
radio_div1_end   = """
    </div>"""

radio_label_start = """      <label class="btn btn-primary">"""
radio_label_end   = """      </label>
"""

radio_div_split_start = """    <div class='btn-group'>
"""
radio_div_split_end   = """    </div>"""

radio_div_split_space = """
    <br></br>
"""

radio_input_start = """        <input type='radio' name='options'"""
radio_input_middle   = """&nbsp;"""
radio_input_end   = """</input>"""

"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Radio Group Form class
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
*
*   ATTRIBUTES
*
*   radioid         -   html id for form
*   idList          -   html id for inputs
*   labelList       -   labels for inputs
*   checked         -   which radio is checked
*
* -----------------------------------------------------------------------*
"""
class RadioGroupForm :

    # full constructor
    def __init__(self,    
                 radioid    =   "",
                 idList     =   [],
                 labelList  =   [],
                 checked    =   -1) :
        
        # instance variables

        # minimum init attributes
        self.radioid    =   radioid
        self.idList     =   idList
        self.labelList  =   labelList
        
        # minimum form data attributes
        self.checked    =   checked
    def get_radioid(self) :
        return(self.radioid)
    def set_formid(self,setParm) :
        self.formid = setParm
    def get_idList(self) :
        return(self.idList)
    def set_idList(self,setParm) :
        self.idList = setParm
    def get_labelList(self) :
        return(self.labelList)
    def set_labelList(self,setParm) :
        self.labelList = setParm
    def get_checked(self) :
        return(self.checked)
    def set_checked(self,setParm) :
        self.checked = setParm

    def get_html(self) :

        if(debugFlag) : 
            self.dump()

        radioHTML = ""

        radioHTML = (radioHTML + radio_container_start + new_line )
        radioHTML = (radioHTML + radio_div_start + new_line )
        radioHTML = (radioHTML + radio_div1_start)
        radioHTML = (radioHTML + addattribute("id",self.get_radioid()) +">" + new_line)    
    
        rowlengths = []
    
        if(len(self.get_idList()) > 10) :
            import math
            numrows = int(math.ceil(len(self.get_idList()) / 10))
            numperrow = int(math.ceil(len(self.get_idList()) / numrows))
        
            for k in range(numrows) :
                if(k == (numrows - 1)) :
                    rowlengths.append(len(self.get_idList()) - ((k)*numperrow))
                else :
                    rowlengths.append(numperrow)
        
        else :
            rowlengths.append(len(self.get_idList()))
            numperrow = len(self.get_idList())
    
        for i in range(len(rowlengths)) :
            radioHTML = (radioHTML + radio_div_split_start)    
            index = ((i) * numperrow)
            for j in range(rowlengths[i]) :
                radioHTML = (radioHTML + radio_label_start + new_line)
                radioHTML = (radioHTML + radio_input_start)
                if(index+j == self.get_checked()) :
                    radioHTML = (radioHTML + addattribute("checked","checked")) 
#                if(len(self.get_jslist())>0) :
#                    radioHTML = (radioHTML + addattribute("onclick",self.get_jslist()[index+j]))     
#            
            
                radioHTML = (radioHTML + addattribute("id",self.get_idList()[index+j]) + ">")
                radioHTML = (radioHTML + radio_input_middle)
                radioHTML = (radioHTML + self.get_labelList()[index+j])
                radioHTML = (radioHTML + radio_input_end + new_line)
                radioHTML = (radioHTML + radio_label_end)
        
            radioHTML = (radioHTML + radio_div_split_end)
            if(not (i == (len(rowlengths)-1))) :
                radioHTML = (radioHTML + radio_div_split_space)    

        radioHTML = (radioHTML + radio_div1_end + new_line)
        radioHTML = (radioHTML + radio_div_end + new_line )
        radioHTML = (radioHTML + radio_container_end)

        if(self.get_radioid == "dtconvertdatatype") :   
            print(radioHTML)

        return(radioHTML)

    def dump(self) :

        print("\nradioid         [0] : ",self.get_radioid())
        print("idList          [1] : ",self.get_idList())
        print("labelList       [2] : ",self.get_labelList())
        print("jchecked        [3] : ",self.get_checked())




    
"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common helper methods to display forms 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""   
    
def displayHeading(text,level) :
    
    displayHTML(addheading(text,level))



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser Input form repository
# -------------------------------------------------------------------------
#   Repository is used to store input form parms to dynamically show minimum
#   parms or show full parms list
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser Input form repository static helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_Input(formid) :
    return(DataframeCleanserInputLog.get_InputForm(formid))
    
def add_Input(formid,idList,labelList,typeList,placeholderList,jsList,reqList,shortForm=False,custom=None) :
    if(formid != "dceulaform") :
        DataframeCleanserInputLog.add_InputForm(formid,idList,labelList,typeList,placeholderList,jsList,reqList,shortForm=False,buttonstyle=None)

def delete_Input(formid) :
    DataframeCleanserInputLog.delete_InputForm(formid) 

def delete_all(ownerid=None) :
    DataframeCleanserInputLog.delete_all(ownerid) 

def define_inputs(ownerid,formlist) :
    DataframeCleanserInputLog.define_owner_list(ownerid,formlist) 



class DCInputLog :

    # full constructor
    def __init__(self) :
        
        # instance variables
        self.inputlog   =   {}
        self.ownerDict  =   {}

    def get_InputForm(self,formid) :
        return(self.inputlog.get(formid))

    def add_InputForm(self,formid,idList,labelList,typeList,placeholderList,jsList,reqList,shortForm=False,buttonstyle=None) :

        inputformList = []
        inputformList.append(idList)
        inputformList.append(labelList)
        inputformList.append(typeList)
        inputformList.append(placeholderList)
        inputformList.append(jsList)
        inputformList.append(reqList)
        inputformList.append(shortForm)
        inputformList.append(buttonstyle)
        
        self.inputlog.update({formid:inputformList})
        
    def delete_InputForm(self,formid) :
        
        self.inputlog.pop(formid)
    
    def delete_all(self,ownerid) :
        
        if(ownerid == None) :
            self.inputlog         =   {}
        else :
            for i in range(len(self.ownerList)) :
                ownerlist = list(self.ownerDict.vals())
                if(ownerlist[i] == ownerid) :
                    ownerforms = self.ownerDict.get(ownerlist[i])
                    for j in range(len(ownerforms)) :
                        self.inputlog.pop(ownerforms[j])    
            
    def define_owner_list(self,ownerid,formlist) :
        
        self.ownerDict.update({ownerid:formlist})
        
    def get_inputlog_file_name(self) :
        nbname  =   cfg.get_notebook_name()
        if(not (nbname == None)) :
            return(cfg.get_files_path() + nbname + "_inputlog.json")
        else :
            return(None)

    def load_inputlog_file(self) :

        try :
            
            fname   =    self.get_inputlog_file_name() 
            if(not (fname == None)) :
                with open(fname, 'r') as log_file :
                    import json
                    self.dictlog = json.load(log_file)
                   
                log_file.close()
                
        except Exception as e:
            self.inputlog          =   {}

            opstat = opStatus()
            opstat.store_exception("Unable to load input form logs" + str(id),e)
            display_exception(opstat)
    
    def save_inputlog_file(self,id) :
        
        try :
            fname   =    self.get_inputlog_file_name() 
            if(not (fname == None)) :
                with open(fname, 'w') as log_file :
                    import json
                    json.dump(self.listlog,log_file)
                    
                log_file.close()
                
        except Exception as e:
            opstat = opStatus()
            opstat.store_exception("Unable to save input forms logs" + str(id),e)
            display_exception(opstat)


"""
* ----------------------------------------------------
# instantiation of the Input form repository
* ----------------------------------------------------
"""    
DataframeCleanserInputLog    =   DCInputLog()





    
    
    
    
                    



