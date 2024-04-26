"""
# DisplayUtils 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

from dfcleanser.common.common_utils import  (display_generic_grid, new_line)
import dfcleanser.common.cfg as cfg

import sys


this = sys.modules[__name__]

DEBUG_DROPDOWN = False


"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   Common Display Utility functions
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
status_template_html = """
    <div MID style="width:XXXWIDTH; margin-left:XXXMARGINpx; border: 0px solid #67a1f3;">
        <div style="width:XXXWIDTH; background-color:#67a1f3">
            <div style="width:XXXWIDTH; background-color:#67a1f3; color:#ffffff;">
                <b>Status:</b>
            </div>
        </div>
        <div style="width:XXXWIDTH; background-color:#ffffff">
            <div style="width:XXXWIDTH; margin-left:10px; background-color:#ffffff;">
                <div style="padding:6px; background-color:#ffffff;">
                    XXXMSG
                </div>
            </div>        
        </div>
    </div>
"""


def get_status_msg_html(msg, width=None, left=None, msgid=None, display=False):
    """
    #------------------------------------------------------------------
    #   display simple help note
    #
    #   msg         -   help msg
    #   width       -   custom width
    #   left        -   custom left margin
    #   msgid       -   message id
    #   display     -   display or return html
    #
    #------------------------------------------------------------------
    """

    status_html = status_template_html
    status_html = status_html.replace("XXXMSG", msg)

    if(msgid is None):
        status_html = status_html.replace("MID", "")
    else:
        status_html = status_html.replace("MID", " id ='" + msgid + "'")

    if(width is None):
        status_html = status_html.replace("XXXWIDTH", str(100)+"%")
    else:
        status_html = status_html.replace("XXXWIDTH", str(width)+"px")

    if(left is None):
        status_html = status_html.replace("XXXMARGIN", str(0))
    else:
        status_html = status_html.replace("XXXMARGIN", str(left))

    if(display):

        gridclasses = ["dfc-main"]
        gridhtmls = [status_html]

        display_generic_grid(
            "dfc-display-help-note-wrapper", gridclasses, gridhtmls)

        # print(status_html)

    else:

        return(status_html)

def get_exception_details_text(opstat):

    try:

        exception_text = ""

        if(not (opstat.get_systemRC0()) == None):
            exception_text = exception_text + "   " + str(opstat.get_systemRC0().__name__) + '\n'
 
        if(not (opstat.get_systemRC1()) == None):
            exception_text = exception_text + "   " + str(opstat.get_systemRC1()) + "\n"

    except:

        exception_text = "  "

    return(exception_text)


"""
#--------------------------------------------------------------------------
#    common display text utility
#--------------------------------------------------------------------------
"""

common_text_html = """
<div style='margin-left:XXXMARGINpx; width:XXXWIDTHpx;'>
        <span style='font-size:XXXFSIZEpx; font-family:"XXXFAMILY";'>
            XXXMSGTEXT
        </span>
    </div>
"""


def get_common_text_html(msg, width, leftmargin, fontsize=14, fontfamily="Courier"):
    """
    #------------------------------------------------------------------
    #   display a dfc exception
    #
    #   opstat   -   status object holding exception
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """

    common_msg_html = common_text_html
    common_msg_html = common_msg_html.replace("XXXWIDTH", str(width))
    common_msg_html = common_msg_html.replace("XXXMARGIN", str(leftmargin))
    common_msg_html = common_msg_html.replace("XXXFSIZE", str(fontsize))
    common_msg_html = common_msg_html.replace("XXXFAMILY", fontfamily)

    msg_text = ""
    for i in range(len(msg)):
        msg_text = msg_text + msg[i]
        if(i < (len(msg) - 1)):
            msg_text = msg_text + "<br>"

    common_msg_html = common_msg_html.replace("XXXMSGTEXT", msg_text)

    return(common_msg_html)






# """
# --------------------------------------------------------------------------
#   column names table 
# --------------------------------------------------------------------------
# """

start_parms_table = """
<table class='geocode-table'; style='margin-left: XXXLEFTMARGINpx'; width=XXXTABLEWIDTHpx;>
<tr>
    <th style='text-align:center;' class='geocode-header' width=XXXTABLEWIDTHpx;>XXXTABLETITLE</th>
</tr>
</table>
<table class='geocode-table'; style='margin-left: XXXLEFTMARGINpx'; width=XXXTABLEWIDTHpx;>
"""

end_parms_table = """
</table>
"""

parms_table_row = """
<tr width=XXXWIDTHpx;>
    <td class='geocode-column'; width=COLUMNWIDTHpx; style='text-align:center;'>XXXPARMNAME</td>
    <td class='geocode-column'; width=COLUMNWIDTHpx; style='text-align:center;'>XXXPARMVALUE</td>
</tr>
"""


def displayParms(title, labels, values, tblid, width=None, leftMargin=0): 


    table_html  =   start_parms_table.replace("XXXTABLEWIDTH",str(2*width))
    table_html  =   table_html.replace("XXXTABLETITLE",str(title))
    table_html  =   table_html.replace("XXXLEFTMARGIN",str(leftMargin))

    for i in range(len(labels)) :
        next_row_html   =   parms_table_row
        next_row_html   =   next_row_html.replace("XXXWIDTH",str(2*width))
        next_row_html   =   next_row_html.replace("COLUMNWIDTH",str(width))
        next_row_html   =   next_row_html.replace("XXXPARMNAME",str(labels[i]))
        next_row_html   =   next_row_html.replace("XXXPARMVALUE",str(values[i]))

        table_html  =   table_html + next_row_html
    
    table_html  =   table_html + end_parms_table

    return(table_html)



def display_status(msg, display=True, width=None, margin=None):
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """

    if(display):

        status_html = display_msgs(
            [msg], "Status :", width, margin, False, False, 11)

        from dfcleanser.common.common_utils import DUMP_HTML
        if(DUMP_HTML):
            print(status_html)

        gridclasses = ["dfc-top-"]
        gridhtmls = [status_html]

        display_generic_grid("dfc-notes-wrapper", gridclasses, gridhtmls)

    else:

        #status_html     =   display_msgs([msg],"Status :",width,margin,False,False,11)
        return(display_msgs([msg], "Status :", width, margin, False, False, 11))


def display_status_note(msg, full=True):
    """
    #------------------------------------------------------------------
    #   display statys msg
    #
    #   notes    -   msg
    #   full     -   full width
    #
    #------------------------------------------------------------------
    """

    notes_html = "<div style='text-align:center; border: 0px solid #67a1f3; font-size: 13px; font-color:#67a1f3; background-color:#F8F5E1;'><span style='color:#67a1f3;'>" + msg + "</span></div>"

    from dfcleanser.common.common_utils import DUMP_HTML
    if(DUMP_HTML):
        print(notes_html)

    gridclasses = ["dfc-top-"]
    gridhtmls = [notes_html]

    if(not (full)):
        display_generic_grid("dfc-notes-short-wrapper", gridclasses, gridhtmls)
    else:
        display_generic_grid("dfc-notes-wrapper", gridclasses, gridhtmls)



def display_dfcleanser_taskbar(tbform, shortform=False):

    tb_html = tbform.get_html()

    gridclasses = ["dfcleanser-common-grid-header"]
    gridhtmls = [tb_html]

    if(shortform):
        display_generic_grid("dfc-taskbar-wrapper-short",
                             gridclasses, gridhtmls)
    else:
        display_generic_grid("dfc-taskbar-wrapper", gridclasses, gridhtmls)


exception_error_template_html = """
    <div style="width:XXXWIDTH%; margin-left:XXXMARGINpx; border: 1px solid #67a1f3;">
        <div style="background-color:#67a1f3">
            <div style="margin-left:10px; background-color:#67a1f3; color:#ffffff;">
                <b>Error:</b>
            </div>
        </div>
        <div style="background-color:#ffffcc">
            <div style="margin-left:20px; background-color:#ffffcc;">
                <div style="padding:6px; background-color:#ffffcc;">
                    XXXMSG
                </div>
            </div>        
        </div>
    </div>
"""

exception_trace_template_html = """
    <div style="width:XXXWIDTH%; margin-left:XXXMARGINpx; border: 1px solid #67a1f3;">
        <div style="background-color:#67a1f3">
            <div style="margin-left:10px; background-color:#67a1f3; color:#ffffff;">
                <b>Exception Trace:</b>
            </div>
        </div>
        <div style="background-color:#ffffcc">
            <div style="margin-left:20px; background-color:#ffffcc;">
                <div style="padding:6px; background-color:#ffffcc;">
                    XXXTRACEMSG
                </div>
            </div>        
        </div>
    </div>
"""


def get_exception_html(opstat, width=None, left=None, display=False):
    """
    #------------------------------------------------------------------
    #   display a dfc exception
    #
    #   opstat   -   status object holding exception
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """

    msg = opstat.get_errorMsg()

    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
    add_error_to_log(msg, SEVERE_ERROR)

    if(not (opstat.get_exception() is None)):
        details_msg = get_exception_details(opstat)
        msg = (msg + "<br>" + details_msg)

    exception_html = exception_error_template_html
    exception_html = exception_html.replace("XXXMSG", msg)

    if(width is None):
        exception_html = exception_html.replace("XXXWIDTH", str(100))
    else:
        exception_html = exception_html.replace("XXXWIDTH", str(width))

    if(left is None):
        exception_html = exception_html.replace("XXXMARGIN", str(240))
    else:
        exception_html = exception_html.replace("XXXMARGIN", str(left))

    if(display):

        gridclasses = ["dfc-main"]
        gridhtmls = [exception_html]

        display_generic_grid(
            "dfc-display-help-note-wrapper", gridclasses, gridhtmls)

    else:

        return(exception_html)





def display_df_sizing_info(df):
    """            
    #------------------------------------------------------------------
    #   get the base sizing info of a dataframe
    #
    #   df              -   dataframe
    #
    #   return : basic sizing info
    #
    #------------------------------------------------------------------
    """

    # print("display_df_sizing_info")
    print("        [NUMBER OF ROWS] :", len(df))
    print("        [NUMBER OF COLS] :", len(df.columns))




"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#   display numeric df column data objects
#------------------------------------------------------------------
#------------------------------------------------------------------
"""





"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   Dataframe rows display methods
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""







"""            
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
# ------------------------------- common display  ---------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"""



def display_msgs(notes, heading, width=None, margin=30, display=True, color=False, fontsize=None):
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   text     -   heading text
    #   color    -   display in color
    #   margin   -   left margin
    #   fontsize -   font size
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """

    notes_html = ""

    if(not (width is None)):
        width_tag = " width:" + str(width) + "px;"
    else:
        width_tag = ""

    if(not (margin is None)):
        margin_tag = " margin-left:" + str(margin) + "px;"
    else:
        margin_tag = ""

    if(not (fontsize is None)):
        fontsize_tag = " font-size:" + str(fontsize) + "px;"
    else:
        fontsize_tag = ""

    notes_html = (notes_html + '<div class="container" style="' +
                  width_tag + margin_tag + fontsize_tag + ' border:1px;">' + new_line)

    notes_html = (notes_html + '    <div class="row">' + new_line)

    if(color):
        notes_html = (
            notes_html + '        <div class="panel panel-primary" style="border:1px; background-color:#ffffcc">' + new_line)
    else:
        notes_html = (
            notes_html + '        <div class="panel panel-primary" style="border:0px;  ">' + new_line)

    if(not (heading == None)):
        notes_html = (
            notes_html + '            <div class="panel-heading dc-note-panel-heading" style="height:40px;">' + new_line)
        notes_html = (
            notes_html + '                <div class="input-group">' + new_line)
        notes_html = (
            notes_html + '                    <p class="dc-table-title" style="margin-bottom:5px; padding-bottom:5px; ">' + heading + '</p>' + new_line)
        notes_html = (notes_html + '                </div>' + new_line)
        notes_html = (notes_html + '            </div>' + new_line)

    notes_html = (notes_html + "        <div class='note-line'>" + new_line)
    notes_html = (
        notes_html + "            <p><span class='note-line' style='word-wrap:break-word;'></span></p>" + new_line)
    notes_html = (notes_html + "        </div>" + new_line)

    for i in range(len(notes)):
        notes_html = (
            notes_html + "        <div class='note-line'>" + new_line)
        notes_html = (notes_html + "            <p><span class='note-line' style='word-wrap:break-word;'>" +
                      notes[i] + "</span></p>" + new_line)
        notes_html = (notes_html + "        </div>" + new_line)

    notes_html = (notes_html + '        </div>' + new_line)
    notes_html = (notes_html + '    </div>' + new_line)
    notes_html = (notes_html + "</div>")

    from dfcleanser.common.common_utils import DUMP_HTML,  displayHTML
    if(DUMP_HTML):
        print(notes_html)

    if(display):
        displayHTML(notes_html)
    else:
        return(notes_html)


def display_notes(notes, display=True, width=None, margin=None):
    """
    #------------------------------------------------------------------
    #   display generic list of msgs
    #
    #   notes    -   list of msgs
    #   display  -   display or return html
    #
    #------------------------------------------------------------------
    """

    if(display):

        notes_html = display_msgs(
            notes, "Notes :", width, margin, False, False, 11)
        gridclasses = ["dfc-top"]
        gridhtmls = [notes_html]

        display_generic_grid("dfc-notes-wrapper", gridclasses, gridhtmls)

    else:
        return(display_msgs(notes, "Notes :", width, margin, False, False, 11))


def get_exception_details(opstat):
    """
    #------------------------------------------------------------------
    #   get exception details
    #
    #   opstat   -   status object holding exception
    #
    #------------------------------------------------------------------
    """

    try:

        exception_html = ""
        exception_html = (
            exception_html + '<div class="container exception-status">' + new_line)
        exception_html = (exception_html + '    <div class="row">' + new_line)
        exception_html = (
            exception_html + '        <div class="panel panel-primary" style="border: 0px">' + new_line)

        if(not (opstat.get_systemRC0()) == None):
            exception_html = (
                exception_html + '            <div class="exception-status-detail">' + new_line)
            exception_html = (exception_html + '                <p>' + "&nbsp;&nbsp;&nbsp;" +
                              str(opstat.get_systemRC0().__name__) + '</p>' + new_line)
            exception_html = (exception_html + '            </div>' + new_line)

        if(not (opstat.get_systemRC1()) == None):

            rcstring = str(opstat.get_systemRC1())
            rcstring = rcstring.replace(";", "<br>&nbsp;&nbsp;&nbsp;")
            exception_html = (
                exception_html + '            <div class="exception-status-detail">' + new_line)
            exception_html = (exception_html + '                <p>' +
                              "&nbsp;&nbsp;&nbsp;" + rcstring + '</p>' + new_line)
            exception_html = (exception_html + '            </div>' + new_line)

        exception_html = (exception_html + '        </div>' + new_line)
        exception_html = (exception_html + '    </div>' + new_line)
        exception_html = (exception_html + "</div>")

    except:

        exception_html = "  "

    return(exception_html)



"""            
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
# ----------------------------- dfc console objects -------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"""


"""            
#----------------------------------------------------------------------------------------
# ----------------------------- dfc console html ----------------------------------------
#----------------------------------------------------------------------------------------
"""


key_list_start = """<div class="btn-group">
"""
key_list_end = """</div>
"""

button_start = """    <div class="btn-group" style="height: XXXBUTTONHEIGHTpx">
"""
button_middle = """        <button class='btn btn-primary' style='height: XXXHEIGHTpx ;  width: XXXWIDTHpx ; margin-left:XXXMARGINpx' onclick='XXXCALLBACK'>XXXTEXT</button>
"""
button_end = """    </div>
"""

console_sidebar_start = """            <div>
"""
console_sidebar_end = """            </div>
"""

console_sidebar_button_start = """                <div class='btn-group'style='width: XXXWIDTHpx; margin-left:XXXMARGINpx'>
"""
console_sidebar_button_middle = """                    <button type='button' class='btn btn-primary' style='height: XXXHEIGHTpx ;  width: XXXWIDTHpx' onclick='XXXCALLBACK'>XXXTEXT</button>
"""
console_sidebar_button_end = """                </div><br>
"""

console_image_start = """            <div style="margin-left: 0px">
                <img src="XXXURL" style="width: XXXWIDTHpx ; height: XXXHEIGHTpx ">
            </div>
"""

"""            
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
# ----------------------------- dfc console classes -------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"""


def get_chapter_console_html(chapterid):

    if(chapterid == cfg.DC_CENSUS_ID):
        return(dfc_census_console.get_console_html())
    else:

        console_htmls = dfc_splash_console.get_console_html()
        return(console_htmls)


class dfcConsole:

    chapter_id = None
    upper_keys = None
    side_keys = None
    image = None

    # full constructor
    def __init__(self, chapterid, upperkeys, sidekeys, splashimage):

        self.chapter_id = chapterid
        self.upper_keys = upperkeys
        self.side_keys = sidekeys
        self.image = splashimage

    def get_console_html(self):

        console_html = ""

        keys_list = self.upper_keys.get_keys_list()

        console_html = (console_html + key_list_start)

        for i in range(len(keys_list)):

            if(type(keys_list[i]) == str):

                console_html = (console_html + keys_list[i])

            else:

                console_html = (console_html + button_start)
                console_html = console_html.replace(
                    'XXXBUTTONHEIGHT', str(keys_list[i].get_height()))

                console_html = (console_html + button_middle)
                console_html = console_html.replace(
                    'XXXHEIGHT', str(keys_list[i].get_height()))
                console_html = console_html.replace(
                    'XXXWIDTH', str(keys_list[i].get_width()))
                console_html = console_html.replace(
                    'XXXMARGIN', str(keys_list[i].get_lmargin()))
                console_html = console_html.replace(
                    'XXXCALLBACK', str(keys_list[i].get_callback()))
                console_html = console_html.replace(
                    'XXXTEXT', str(keys_list[i].get_text()))

                console_html = (console_html + button_end)

        console_html = (console_html + key_list_end)

        upper_keys_html = console_html
        console_html = ""

        # add sidebar
        console_html = (console_html + console_sidebar_start)

        console_html = console_html.replace(
            'XXXMARGIN', str(self.side_keys.get_lmargin()))

        current_sidebar_keys_list = self.side_keys.get_keys_list()

        for i in range(len(current_sidebar_keys_list)):

            console_html = (console_html + console_sidebar_button_start)
            console_html = console_html.replace('XXXBUTTONHEIGHT', str(
                current_sidebar_keys_list[i].get_height()))

            console_html = (console_html + console_sidebar_button_middle)
            console_html = console_html.replace('XXXHEIGHT', str(
                current_sidebar_keys_list[i].get_height()))
            console_html = console_html.replace(
                'XXXWIDTH', str(current_sidebar_keys_list[i].get_width()))
            console_html = console_html.replace('XXXMARGIN', str(
                current_sidebar_keys_list[i].get_lmargin()))
            console_html = console_html.replace('XXXCALLBACK', str(
                current_sidebar_keys_list[i].get_callback()))
            console_html = console_html.replace(
                'XXXTEXT', str(current_sidebar_keys_list[i].get_text()))

            console_html = (console_html + console_sidebar_button_end)

        console_html = (console_html + console_sidebar_end)

        sidebar_html = console_html
        console_html = ""

        # add image
        console_html = (console_html + console_image_start)
        console_html = console_html.replace(
            'XXXHEIGHT', str(self.image.get_height()))
        console_html = console_html.replace(
            'XXXWIDTH', str(self.image.get_width()))
        console_html = console_html.replace(
            'XXXURL', str(self.image.get_url()))

        return([upper_keys_html, sidebar_html, console_html])

    def dump_dfcConsole(self):

        print("\n------------- upper keys --------------------")

        keys_list = self.upper_keys.get_keys_list()

        for i in range(len(keys_list)):

            if(type(keys_list[i]) == str):

                print("Key : ["+str(i)+"] : type ", keys_list[i])

            else:

                print("Key : ["+str(i)+"] : type ", type(keys_list[i]))
                print("height      : ", keys_list[i].get_height())
                print("width       : ", keys_list[i].get_width())
                print("lmargin     : ", keys_list[i].get_lmargin())
                print("callback    : ", keys_list[i].get_callback())
                print("text        : ", keys_list[i].get_text())

        print("------------- upper keys --------------------\n")

        print("\n------------- side keys --------------------")
        print("side keys : ", type(self.side_keys))
        print("lmargin : ", self.side_keys.get_lmargin())
        keys_list = self.side_keys.get_keys_list()
        print("keys_list type", type(keys_list))
        print("keys_list type", len(keys_list))
        for i in range(len(keys_list)):
            if(type(keys_list[i]) == list):
                print("keys_list type["+str(i)+"]", type(keys_list[i]))

            else:
                print("Key : ["+str(i)+"]")
                print("height      : ", keys_list[i].get_height())
                print("width       : ", keys_list[i].get_width())
                print("lmargin     : ", keys_list[i].get_lmargin())
                print("callback    : ", keys_list[i].get_callback())
                print("text        : ", keys_list[i].get_text())

        print("------------- side keys --------------------\n")

        print("\n------------- image --------------------")
        print("image : type ", type(self.image))
        print("height        : ", self.image.get_height())
        print("width         : ", self.image.get_width())
        print("url           : ", self.image.get_url())
        print("------------- image --------------------\n")


class dfcConsoleKeyList:

    lmargin = 0
    keys_list = None

    def __init__(self, blmargin, bkeys):

        self.lmargin = blmargin
        self.keys_list = bkeys

    def get_lmargin(self):
        return(self.lmargin)

    def get_keys_list(self):
        return(self.keys_list)


class dfcConsoleButton:

    height = 0
    width = 0
    lmargin = 0
    callback = None
    text = None

    def __init__(self, bheight, bwidth, blmargin, bcallback, btext):

        self.height = bheight
        self.width = bwidth
        self.lmargin = blmargin
        self.callback = bcallback
        self.text = btext

    def get_height(self):
        return(self.height)

    def get_width(self):
        return(self.width)

    def get_lmargin(self):
        return(self.lmargin)

    def get_callback(self):
        return(self.callback)

    def get_text(self):
        return(self.text)


class dfcConsoleImage:

    height = 0
    width = 0
    url = None

    def __init__(self, bheight, bwidth, burl):

        self.height = bheight
        self.width = bwidth
        self.url = burl

    def get_height(self):
        return(self.height)

    def get_width(self):
        return(self.width)

    def get_url(self):
        return(self.url)


"""            
#----------------------------------------------------------------------------------------
# ----------------------------- dfc console html values----------------------------------
#----------------------------------------------------------------------------------------
"""

"""            
# ----------------------------- dfc console values----------------------------------
"""

dfc_splash_banner_1 = dfcConsoleButton(
    30, 140, 0, "control_qt_chapter(5)", "System")
dfc_splash_banner_2 = dfcConsoleButton(
    30, 120, 0, "control_qt_chapter(4)", "Data Import")
dfc_splash_banner_3 = dfcConsoleButton(
    30, 122, 0, "control_qt_chapter(0)", "Data Inspection")
dfc_splash_banner_4 = dfcConsoleButton(
    30, 122, 0, "control_qt_chapter(1)", "Data Cleansing")
dfc_splash_banner_5 = dfcConsoleButton(
    30, 120, 0, "control_qt_chapter(2)", "Data Transform")
dfc_splash_banner_6 = dfcConsoleButton(
    30, 120, 0, "control_qt_chapter(3)", "Data Export")

dfc_splash_banner_list = [dfc_splash_banner_1, dfc_splash_banner_2,
                          dfc_splash_banner_3, dfc_splash_banner_4, dfc_splash_banner_5, dfc_splash_banner_6]
dfc_splash_banner_keys = dfcConsoleKeyList(20, dfc_splash_banner_list)

dfc_splash_sidebar_1 = dfcConsoleButton(
    30, 140, 0, "control_qt_chapter(6)", "Geocoding")
dfc_splash_sidebar_2 = dfcConsoleButton(
    30, 140, 0, "add_dfcleanser_chapter(" + str(cfg.DC_CENSUS_ID) + ")", "Census Data")
dfc_splash_sidebar_3 = dfcConsoleButton(
    30, 140, 0, "control_qt_chapter(7)", "Zip Codes")
dfc_splash_sidebar_5 = dfcConsoleButton(
    30, 140, 0, "reset_dfc_chapters()", "Reset All Chapters")
dfc_splash_sidebar_6 = dfcConsoleButton(
    30, 140, 0, "close_dfc_chapters()", "Close All Chapters")
dfc_splash_sidebar_7 = dfcConsoleButton(
    30, 140, 0, "unload_dfcleanser()", "Unload dfcleanser")
dfc_splash_sidebar_8 = dfcConsoleButton(
    30, 140, 0, "display_help_url(" + '"https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-index.html"' + ")", "Help")

dfc_splash_sidebar_list = [dfc_splash_sidebar_1, dfc_splash_sidebar_2, dfc_splash_sidebar_3, dfc_splash_sidebar_5,
                           dfc_splash_sidebar_6, dfc_splash_sidebar_7, dfc_splash_sidebar_8]
dfc_splash_sidebar_keys = dfcConsoleKeyList(20, dfc_splash_sidebar_list)

dfc_splash_image = dfcConsoleImage(
    210, 600, "https://rickkrasinski.github.io/dfcleanser/graphics/dfcleanserConsoleSplash.png")

dfc_splash_console = dfcConsole(
    cfg.DC_CONSOLE_ID, dfc_splash_banner_keys, dfc_splash_sidebar_keys, dfc_splash_image)



"""            
# ----------------------------- dfc Census values ----------------------------------
"""

"""
dfc_census_banner_1 = dfcConsoleButton(50, 226, 0, "get_census_callback("+str(
    DISPLAY_DOWNLOAD_CENSUS_DATA)+")", "Download Census Datasets")
dfc_census_banner_2 = dfcConsoleButton(
    50, 230, 0, "get_census_callback("+str(DISPLAY_CONFIGURE_CENSUS_DATA)+")", "Setup Census Datasets")
dfc_census_banner_3 = dfcConsoleButton(50, 226, 0, "get_census_callback("+str(
    DISPLAY_LOAD_CENSUS_TO_DFC_DFS)+")", "Load Census Datasets <br>To Memory")
dfc_census_banner_4 = "<br>"
dfc_census_banner_5 = dfcConsoleButton(50, 226, 0, "get_census_callback("+str(
    DISPLAY_CENSUS_DATASETS_FOR_INSERT)+")", "Join Census Columns <br>To User dfs")
dfc_census_banner_6 = dfcConsoleButton(
    50, 230, 0, "get_census_callback("+str(DISPLAY_EXPORT_CENSUS_DFS)+")", "Export Census Datasets")
dfc_census_banner_7 = dfcConsoleButton(50, 226, 0, "get_census_callback("+str(
    DISPLAY_LOAD_CENSUS_DATA_TO_DB)+")", "Load Census Datasets <br>To db(s)")

dfc_census_banner_list = [dfc_census_banner_1, dfc_census_banner_2, dfc_census_banner_3,
                          dfc_census_banner_4, dfc_census_banner_5, dfc_census_banner_6, dfc_census_banner_7]

dfc_census_banner_keys = dfcConsoleKeyList(20, dfc_census_banner_list)

dfc_census_sidebar_1 = dfcConsoleButton(
    30, 140, 0, "load_dfcleanser_chapter(" + str(cfg.DC_CENSUS_ID) + ")", "Reset Chapter")
dfc_census_sidebar_2 = dfcConsoleButton(
    30, 140, 0, "close_dfcleanser_chapter(" + str(cfg.DC_CENSUS_ID) + ")", "Close Chapter")
dfc_census_sidebar_3 = dfcConsoleButton(
    30, 140, 0, "display_help_url(" + '"https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-census-utility.html"' + ")", "Help")

dfc_census_sidebar_list = [dfc_census_sidebar_1,
                           dfc_census_sidebar_2, dfc_census_sidebar_3]
dfc_census_sidebar_keys = dfcConsoleKeyList(20, dfc_census_sidebar_list)

dfc_census_image = dfcConsoleImage(
    90, 542, "https://rickkrasinski.github.io/dfcleanser/graphics/CensusSplash.png")

dfc_census_console = dfcConsole(
    cfg.DC_CENSUS_ID, dfc_census_banner_keys, dfc_census_sidebar_keys, dfc_census_image)

"""

"""    
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   common error messages display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

error_template_html = """
    <div MID style="width:XXXWIDTH%; margin-left:XXXMARGINpx; border: 0px solid #67a1f3;">
        <div style="background-color:#67a1f3">
            <div style="margin-left:10px; background-color:#67a1f3; color:#ffffff;">
                <b>Error:</b>
            </div>
        </div>
        <div style="background-color:#ffffff">
            <div style="margin-left:20px; background-color:#ffffff;">
                <div style="padding:6px; background-color:#ffffff;">
                    XXXMSG
                </div>
            </div>        
        </div>
    </div>
"""


def get_error_msg_html(msg, width=None, left=None, msgid=None, display=False):
    """
    #------------------------------------------------------------------
    #   display simple help note
    #
    #   msg         -   help msg
    #   width       -   custom width
    #   left        -   custom left margin
    #   msgid       -   message id
    #   display     -   display or return html
    #
    #------------------------------------------------------------------
    """

    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
    add_error_to_log(msg, SEVERE_ERROR)

    error_html = error_template_html
    error_html = error_html.replace("XXXMSG", msg)

    if(msgid is None):
        error_html = error_html.replace("MID", "")
    else:
        error_html = error_html.replace("MID", " id ='" + msgid + "'")

    if(width is None):
        error_html = error_html.replace("XXXWIDTH", str(100))
    else:
        error_html = error_html.replace("XXXWIDTH", str(width))

    if(left is None):
        error_html = error_html.replace("XXXMARGIN", str(0))
    else:
        error_html = error_html.replace("XXXMARGIN", str(left))

    if(display):

        gridclasses = ["dfc-main"]
        gridhtmls = [error_html]

        display_generic_grid(
            "dfc-display-help-note-wrapper", gridclasses, gridhtmls)

    else:

        return(error_html)


status_note_template_html = """
        <div style="padding:6px; height:40px; width:XXXWIDTHpx; margin-left:XXXMARGINpx; background-color:#ffffcc">
            <div style="padding:6px; margin-left:20px; background-color:#ffffcc;">
                <div style="padding:6px; font-size:XXXFONTSIZEpx; background-color:#ffffcc;">
                    XXXMSG
                </div>
            </div>        
        </div>
"""


def get_status_note_msg_html(msg, width=None, left=None, fontsize=None, display=False):
    """
    #------------------------------------------------------------------
    #   display simple help note
    #
    #   msg         -   help msg
    #   width       -   custom width
    #   left        -   custom left margin
    #   display     -   display or return html
    #
    #------------------------------------------------------------------
    """

    status_note_html = status_note_template_html
    status_note_html = status_note_html.replace("XXXMSG", msg)

    if(width is None):
        status_note_html = status_note_html.replace("XXXWIDTH", str(100))
    else:
        status_note_html = status_note_html.replace("XXXWIDTH", str(width))

    if(left is None):
        status_note_html = status_note_html.replace("XXXMARGIN", str(240))
    else:
        status_note_html = status_note_html.replace("XXXMARGIN", str(left))
    
    if(fontsize is None):
        status_note_html = status_note_html.replace("XXXFONTSIZE", str(11))
    else:
        status_note_html = status_note_html.replace("XXXFONTSIZE", str(fontsize))

    if(display):

        gridclasses = ["dfc-main"]
        gridhtmls = [status_note_html]

        display_generic_grid("dfc-display-help-note-wrapper", gridclasses, gridhtmls)

    else:

        return(status_note_html)

