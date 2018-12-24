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


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
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
"""
    
bulk_console_container = """<div class="dfc-console-container" style=' width: 60%; text-align: center; margin: auto; border: 1px solid #428bca; overflow-x: hidden; overflow-y: hidden;'>
    <div style="text-align: center; margin:auto; margin-top:20px;">
        <table class="tableRowHoverOff" id="geocodeStatusBars" style="margin:auto; width: 90%;">
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
"""

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:100%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(22)">Run</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(23)">Pause</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:54px;  height:40px;" onclick="controlbulkrun(24)">Stop</button>
            </div>
        </div>
"""

bulk_console_status = """        <div style=' width: 30%; text-align: center; height: 30px; margin: auto;'>
            <p id='bulkstatus' style='height: 30px; padding-top: 5px; text-align: center; font-size: 14px; font-family: Arial; color: #474747; font-weight: bold; """
bulk_console_status1 = """ : margin: auto;'>"""
bulk_console_status2 = """</p>
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

"""
def set_status_bar(status) :
    
    btext   =   ""
    
    from dfcleanser.system.system_model import Green,Red,Yellow
    if(status == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(status == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(status == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"

    if(len(btext) > 0) :
        set_status_bar_js = "set_bulk_progress_status('" + str(btext) + "', '" + str(bcolor) + "');"
    
        print("set_status_bar_js",set_status_bar_js)
        from dfcleanser.common.common_utils import run_jscript
        run_jscript(set_status_bar_js,
                    "fail to set progress status color : ",
                    str(btext))
"""


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
    console_html = (console_html + bulk_console_title)
    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))    
    
    console_html = (console_html + bulk_console_container_end)  
    console_html = (console_html + bulk_console_commands)
    
    from dfcleanser.system.system_model import Green,Red,Yellow    
    if(state == sugm.RUNNING) : 
        bcolor  =   Green
        btext   =   "Running"
    elif(state == sugm.STOPPED) :
        bcolor  =   Red
        btext   =   "Stopped"
    elif(state == sugm.STOPPING) :
        bcolor  =   Red
        btext   =   "Stopping"
    elif(state == sugm.PAUSED) :
        bcolor  =   Yellow
        btext   =   "Paused"
    elif(state == sugm.PAUSING) :
        bcolor  =   Yellow
        btext   =   "Pausing"
    
    console_html = (console_html + bulk_console_status)
    from dfcleanser.common.html_widgets import addstyleattribute
    console_html = (console_html + addstyleattribute("background-color",str(bcolor)))
    console_html = (console_html + bulk_console_status1 + btext)
    console_html = (console_html + bulk_console_status2)
    
    console_html = (console_html + bulk_console_end)  
    console_html = (console_html + bulk_end)
        
    return(console_html)     
        
        
def display_geocoder_console(geocid,runParms,opstat,state=sugm.STOPPED) :
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

    if(geocid == sugm.ArcGISId) :
        
        if(not(runParms == None)) :
            from dfcleanser.common.common_utils import displayParms, get_parms_list_from_dict 
            parms   =   get_parms_list_from_dict(subgw.batch_arcgis_query_labelList,runParms) 
            displayParms("arcGIS Bulk Geocoding Parms",subgw.batch_arcgis_query_labelList,parms,"arcgisbulkparms")

        bar0 = ["Total Addresses Geocoded","arcgistotaladdrs",0,100,0]
        bar1 = ["Geocode Error Rate","arcgiserrorrate",0,100,0]
        
        progressBars    =   [bar0,bar1]
        
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
        from dfcleanser.common.common_utils import displayHTML
        
        displayHTML(console_html)
        
        print("\n")
        
    elif(geocid == sugm.GoogleId) :
        print("google console")



