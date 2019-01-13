"""
# sw_utility_bulk_geocode_console
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_widgets as subgw

import dfcleanser.common.cfg as cfg

from dfcleanser.common.table_widgets import  (dcTable, ROW_MAJOR, get_row_major_table, SCROLL_NEXT)   
from dfcleanser.common.html_widgets import   get_html_spaces

from dfcleanser.common.common_utils import  display_generic_grid

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    geocoding console task bar
#--------------------------------------------------------------------------
"""
geocode_console_tb_doc_title               =   "Dataframe Concat"
geocode_console_tb_title                   =   "Dataframe Concat"
geocode_console_tb_id                      =   "dfconcat"

geocode_console_tb_keyTitleList            =   ["Run","Stop","Pause",
                                                "Resume","Error</br>Log"]

geocode_console_tb_jsList                  =   ["controlbulkrun(22)",
                                                "controlbulkrun(23)",
                                                "controlbulkrun(24)",
                                                "controlbulkrun(25)",
                                                "controlbulkrun(25)"]

geocode_console_tb_centered                =   False

"""
#--------------------------------------------------------------------------
#   bulk geocoding console html
#--------------------------------------------------------------------------
"""

bulk_start = """<div class="dfc-console-container" width='100%' style='overflow-x: hidden; overflow-y: hidden;'>"""
bulk_console_title = """<div class="dfc-console-title">
    <p class="dfc-console-title" style='text-align: center; font-size: 20px; font-family: Arial; font-weight: bold; margin: auto; overflow-x: hidden; overflow-y: hidden;'>Bulk Geocoding Run Console</p>
</div>
<br>
<br>
<br>
<br>
"""
    
bulk_console_container = """<div class="dfc-console-container" style=' text-align: center; margin: auto; border: 0px solid #428bca; overflow-x: hidden; overflow-y: hidden;'>
    <div style="text-align: center; margin:auto; margin-top:20px;">
        <table class="tableRowHoverOff" id="geocodeStatusBars" style="margin:auto;">
            <tbody>
"""
                
bulk_console_progress_row = """                    <tr class='dfc-progress-row' style='height: 30px;'>
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;'>"""

bulk_console_progress_col = """                        <td class='dfc-progress-col' style='width: 55%;'>
                            <div class='progress md-progress dfc-progress-div' style='height: 20px; '>
                                <div """

bulk_console_progress_col1 = """ class='progress-bar dfc-progress-bar' role='progressbar' style='height: 20px;'"""

bulk_console_progress_row_end = """                            </div>
                        </td>
                    </tr>
"""
                    
bulk_console_container_end = """            </tbody>
        </table>
    </div>
    </br>
"""

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:100%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_START_GEOCODER) + """)">Start</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_STOP_GEOCODER) + """)">Stop</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_PAUSE_GEOCODER) + """)">Pause</button>
            </div>
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_RESUME_GEOCODER) + """)">Resume</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_VIEW_ERRORS) + """)">View Errors</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_CHECKPT_GEOCODER) + """)">Checkpoint</button>
            </div>
        </div>
"""

bulk_console_status_start = """
        <br>
        <div>
            <img id='geocodeconsolestateId' src='https://rickkrasinski.github.io/dfcleanser/graphics/"""
bulk_console_status_middle = """'  style='display: block; margin-left: auto; margin-right: auto;' width='200' height='55'></img> """
bulk_console_status_end = """
        </div>
        <br>
"""

bulk_console_end = """</div>
"""
bulk_end = """</div>"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding console methods
#--------------------------------------------------------------------------
"""

def set_progress_bar_value(geocid,barid,barvalue) :
    """
    * -------------------------------------------------------------------------- 
    * function : update status bars
    * 
    * parms :
    *  geocid   - geocoder id
    *  barid    - progress bar id
    *  barvalue - bar value
    *
    * returns : 
    *  progress bar updated
    * --------------------------------------------------------
    """
    
    if(geocid == sugm.ArcGISId) :
        
        if(barid == 0)  :   bid = "arcgistotaladdrs"
        else            :   bid = "arcgiserrorrate"
        
    elif(geocid == sugm.GoogleId) :

        if(barid == 0)  :   bid = "googletotaladdrs"
        else            :   bid = "googleerrorrate"

    set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
    
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(set_progress_bar_js,
                "fail to set progress bar : ",
                 str(bid))


def set_status_bar(state) :
    """
    * -------------------------------------------------------------------------- 
    * function : set the geocode console state
    * 
    * parms :
    *  state   - state to change to
    *
    * returns : 
    *  state html updated
    * --------------------------------------------------------
    """
 
    #print("    set_status_bar",state)
    if(state == sugm.STARTING) : 
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Starting_State.png"
    elif(state == sugm.RUNNING) : 
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Running_State.png"
    elif(state == sugm.STOPPED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopped_State.png"
    elif(state == sugm.FINISHED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Finished_State.png"
    elif(state == sugm.PAUSED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Paiused_State.png"
    elif(state == sugm.STOPPING) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopping_State.png"
    elif(state == sugm.PAUSING) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Pausing_State.png"

    import datetime 
    tstamp = datetime.datetime.now().time()

    change_state_js = ("$('#geocodeconsolestateId').attr('src'," + "'" + image + "?timestamp=" + str(tstamp) + "'" + ");")
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(change_state_js,
                "fail to change console state : ",
                str(state))



def get_progress_bar_html(barParms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for a progress bar
    * 
    * parms :
    *  barParms   - [bartitle,barid,barmin,barmax,currentvalue]
    *
    * returns : 
    *  progress bar html
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import addattribute, addstyleattribute, new_line
    
    bar_html = ""
    bar_html = (bar_html + bulk_console_progress_row)
    bar_html = (bar_html + barParms[0] + "</td>" + new_line)
    bar_html = (bar_html + bulk_console_progress_col)
    bar_html = (bar_html + addattribute("id",barParms[1]))
    bar_html = (bar_html + bulk_console_progress_col1)    
    bar_html = (bar_html + addattribute("style",addstyleattribute("width",str(barParms[4])+"%")))
    bar_html = (bar_html + addattribute("aria-valuenow",str(barParms[4])))
    bar_html = (bar_html + addattribute("aria-valuemin",str(barParms[2])))
    bar_html = (bar_html + addattribute("aria-valuemax",str(barParms[3])))
    bar_html = (bar_html + ">" + str(barParms[4]) + "%" + "</div>" + new_line)
    bar_html = (bar_html + bulk_console_progress_row_end)
    
    return(bar_html)

def get_bulk_geocode_console_html(progressbarList,state) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for the bulk geocoding console
    * 
    * parms :
    *  progressbarList   - list of progress bars
    *  state             - state of console
    *
    * returns : console html
    * --------------------------------------------------------
    """
    
    console_html = ""
    console_html = (console_html + bulk_start)
    
    if(state == sugm.RUNNING) : 
        btext   =   "Running_State.png"
    elif(state == sugm.STOPPED) :
        btext   =   "Stopped_State.png"
    elif(state == sugm.STOPPING) :
        btext   =   "Stopping_State.png"
    elif(state == sugm.PAUSED) :
        btext   =   "Paused_State"
    elif(state == sugm.PAUSING) :
        btext   =   "Pausing_State"
    
    console_html = (console_html + bulk_console_status_start + btext)
    console_html = (console_html + bulk_console_status_middle)
    console_html = (console_html + bulk_console_status_end)

    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))    
    
    console_html = (console_html + bulk_console_container_end)  
    
    console_html = (console_html + bulk_console_commands)
    
    console_html = (console_html + bulk_console_end)  
    console_html = (console_html + bulk_end)
    
    return(console_html)     

        
def get_bulk_parms_table_html(geocid,geotype,runParms) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for the parms table
    * 
    * parms :
    *  geocid       - geocoder identifier
    *  runParms     - run parameters
    *
    * returns : parms html
    * --------------------------------------------------------
    """
    
    parmsHeader      =   [""]
    parmsRows        =   []
    parmsWidths      =   [100]
    parmsAligns      =   ["left"]

    parmskeys   =   list(runParms.keys())
    
    for i in range(len(parmskeys)) :
        
        parmsrow = [parmskeys[i] + "&nbsp;:"]
        parmsRows.append(parmsrow)
        parmsrow = ["&nbsp;&nbsp;&nbsp;"+ runParms.get(parmskeys[i])]
        parmsRows.append(parmsrow)
        
    parms_table = None
                
    parms_table = dcTable("Query Parms","geocodeParms",
                          cfg.SWGeocodeUtility_ID,
                          parmsHeader,parmsRows,
                          parmsWidths,parmsAligns)
            
    parms_table.set_small(True)
    parms_table.set_smallwidth(240)
    parms_table.set_smallmargin(10)

    parms_table.set_border(False)
        
    parms_table.set_checkLength(False)
            
    parms_table.set_textLength(30)
    parms_table.set_html_only(True) 
    
    parms_table.set_tabletype(ROW_MAJOR)
    parms_table.set_rowspertable(28)

    listHtml = get_row_major_table(parms_table,SCROLL_NEXT,False)

    #print(listHtml)        
    return(listHtml)

        
def display_geocoder_console(geocid,geotype,runParms,opstat,cmd=sugm.STOP) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the bulk geocoding console
    * 
    * parms :
    *  geocid       - geocoder identifier
    *  runParms     - run parameters
    *  address_set  - address col names
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    #print("\n\ndisplay_geocoder_console",geocid,geotype,cmd,"\n",runParms)
        
    geocoding_heading_html  =   "<p>" + get_html_spaces(68) + "Bulk Geocoding Console</p>"
    parms_html  =   get_bulk_parms_table_html(geocid,geotype,runParms) 
    
    if(cmd == sugm.LOAD) :    state  =   sugm.STOPPED
    else : state  =   sugm.STOPPED
    
    if(geocid == sugm.ArcGISId) :
        
        if(not(runParms == None)) :
            from dfcleanser.common.common_utils import displayParms, get_parms_list_from_dict 
            parms   =   get_parms_list_from_dict(subgw.batch_arcgis_query_labelList,runParms) 
            displayParms("arcGIS Batch Geocoding Parms",subgw.batch_arcgis_query_labelList,parms,"arcgisbulkparms")

        bar0 = ["Total Addresses Geocoded","arcgistotaladdrs",0,100,0]
        bar1 = ["Geocode Error Rate","arcgiserrorrate",0,100,0]
        
        progressBars    =   [bar0,bar1]
        
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
        print("\n")
        
    elif(geocid == sugm.GoogleId) :
        
        bar0 = ["Total Addresses Geocoded","bgqbulknumberlimit",0,100,0]
        bar1 = ["Geocode Error Rate","bgqbulkfailurelimit",0,100,0]

        progressBars    =   [bar0,bar1]
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
    gridclasses     =   ["df-concat-header","dfc-left","dfc-right"]
    gridhtmls       =   [geocoding_heading_html,parms_html,
                         console_html]
    
    display_generic_grid("geocode-console-wrapper",gridclasses,gridhtmls)
























