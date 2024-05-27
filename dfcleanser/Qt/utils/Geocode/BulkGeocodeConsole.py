"""
# sw_utility_bulk_geocode_console
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""


import dfcleanser.common.help_utils as dfchelp
import dfcleanser.common.cfg as cfg

from dfcleanser.common.common_utils import  (display_generic_grid, run_jscript, display_blank_line,  get_image_url)

import dfcleanser.Qt.utils.Geocode.BulkGeocodeModel as BGM
import dfcleanser.Qt.utils.Geocode.GeocodeModel as GM

from dfcleanser.Qt.utils.Geocode.BulkGeocode import (bulk_google_query_input_id, bulk_bing_query_input_id, 
                                                     bulk_google_reverse_input_id, bulk_bing_reverse_input_id)

from dfcleanser.common.html_widgets import   (addattribute, addstyleattribute, new_line, InputForm, ButtonGroupForm)

from dfcleanser.sw_utilities.DisplayUtils import (display_status_note, displayParms)

from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import SWGeocodeUtility_ID

"""
#--------------------------------------------------------------------------
#   bulk results commands
#--------------------------------------------------------------------------
"""

PROCESS_BULK_RESULTS_APPEND_PROCESS             =   7
PROCESS_BULK_RESULTS_APPEND_CLEAR               =   8
PROCESS_BULK_RESULTS_APPEND_RETURN              =   9



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding display main taskbar
#--------------------------------------------------------------------------
"""
bulk_geocode_display_tb_doc_title            =   "Display Bulk Geocode"
bulk_geocode_display_tb_title                =   "Display Bulk Geocode"
bulk_geocode_display_tb_id                   =   "displaybulkgeocode"

bulk_geocode_display_tb_keyTitleList         =   ["Add</br>Geocode Data</br>to dataframe",
                                                  "Show</br>Source</br>Dataframe",
                                                  "Show</br>Results</br>Dataframe",
                                                  "Show</br>Errors</br>Dataframe"]

bulk_geocode_display_tb_jsList               =   ["display_bulk_geocoding_results(" + str(BGM.DISPLAY_BULK_RESULTS_APPEND) + ")",
                                                  "browse_bulk_geocoding_df(XXXDISPLAY_BULK_SOURCE_DF)",
                                                  "browse_bulk_geocoding_df(XXXDISPLAY_BULK_RESULTS_DF)",
                                                  "browse_bulk_geocoding_df(XXXDISPLAY_BULK_ERRORS_DF)"]

bulk_geocode_display_tb_centered             =   False


"""
#--------------------------------------------------------------------------
#   bulk geocoding main taskbar
#--------------------------------------------------------------------------
"""
bulk_geocode_process_tb_doc_title            =   "Process Bulk Geocode"
bulk_geocode_process_tb_title                =   "Process Bulk Geocode"
bulk_geocode_process_tb_id                   =   "procbulkgeocode"

bulk_geocode_process_tb_keyTitleList         =   ["Export</br>Results to</br>CSV File",
                                                  "Export</br>Results to</br>SQL Table",
                                                  "Export</br>Errors to</br>CSV File",
                                                  "Exit</br>Current</br>Bulk Run"]

from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import GEOCODING_ERROR_LOG_DF_TITLE, GEOCODING_RESULTS_DF_TITLE 

bulk_geocode_process_tb_jsList               =   ["export_bulk_geocoding_df('" + str(GEOCODING_RESULTS_DF_TITLE) + "')",
                                                  "export_bulk_geocoding_df('" + str(GEOCODING_RESULTS_DF_TITLE) + "')",
                                                  "export_bulk_geocoding_df('" + str(GEOCODING_ERROR_LOG_DF_TITLE) + "')",
                                                  "exit_bulk_geocoding()"]

bulk_geocode_process_tb_centered             =   False



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console html
#--------------------------------------------------------------------------
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
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;' """

bulk_console_progress1_row = """                    <tr>
"""


bulk_console_progress_col = """                        <td class='dfc-progress-col' style='width: 55%;'>
                            <div class='progress md-progress dfc-progress-div' style='height: 20px; '>
                                <div """

bulk_console_progress_col1 = """ class='progress-bar dfc-progress-bar' role='progressbar' style='height: 20px;'"""


bulk_console_progress_row_end = """                    </tr>
"""

bulk_console_progress1_row_end = """                            </div>
                        </td>
                    </tr>
"""
                    
bulk_console_container_end = """            </tbody>
        </table>
    </div>
    </br>
"""

bulk_console_commands = """        <br><div style="margin-top: 10px; margin-bottom:20px; width:100%">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" id="dfc_start" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(BGM.BULK_START_GEOCODER) + """)">Start</button>
                <button type="button" id="dfc_stop" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(BGM.BULK_STOP_GEOCODER) + """)">Stop</button>
                <button type="button" id="dfc_pause" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(BGM.BULK_PAUSE_GEOCODER) + """)">Pause</button>
                <button type="button" id="dfc_resume" class="btn btn-primary" style="  margin-left:0px; width:100px;  height:40px;" onclick="controlbulkrun(""" + str(BGM.BULK_RESUME_GEOCODER) + """)">Resume</button>
                <button type="button" id="dfc_exit" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="exit_bulk_geocoding()">Exit Run</button>
            </div>
            <br>
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" id="dfc_process" class="btn btn-primary" style="  width:300px;  height:40px;" onclick="controlbulkrun(""" + str(BGM.BULK_RESULTS_GEOCODER) + """)">Process Results</button>
            </div>
        </div>
"""

bulk_console_status_start = """
        <br>
        <div>
            <img id='geocodeconsolestateId' src='"""
            
bulk_console_status_middle = """'  style='display: block; margin-left: auto; margin-right: auto;' width='200' height='55'></img> """

bulk_console_status_end = """
        </div>
        <br>
"""

bulk_console_error_start = """
                    <tr class='dfc-progress-row' style='height: 30px;'>
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;'  id="geocodeerrors">"""

bulk_console_error_end = """</td>
                    </tr>
"""

bulk_console_end = """</div>
"""
bulk_end = """</div>"""



def display_base_taskbar() :
    
    from dfcleanser.sw_utilities.DisplayUtils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(bulk_geocode_process_tb_id,
                                            bulk_geocode_process_tb_keyTitleList,
                                            bulk_geocode_process_tb_jsList,
                                            bulk_geocode_process_tb_centered))
    

def get_progress_bar_html(barParms) :
    """
    * ---------------------------------------------------------
    * function : get the html for a progress bar
    * 
    * parms :
    *  barParms   - [bartitle,barid,barmin,barmax,currentvalue]
    *
    * returns : 
    *  progress bar html
    * --------------------------------------------------------
    """
    
    bar_html = ""
    bar_html = (bar_html + bulk_console_progress_row)
    bar_html = (bar_html + addattribute("id",barParms[1]) + ">")
    bar_html = (bar_html + barParms[0] + "</td>" + new_line)
    bar_html = (bar_html + bulk_console_progress_row_end)
    
    bar_html = (bar_html + bulk_console_progress1_row)
    bar_html = (bar_html + bulk_console_progress_col)
    bar_html = (bar_html + addattribute("id",barParms[2]))
    bar_html = (bar_html + bulk_console_progress_col1)    
    bar_html = (bar_html + addattribute("style",addstyleattribute("width",str(barParms[4])+"%")))
    bar_html = (bar_html + addattribute("aria-valuenow",str(barParms[5])))
    bar_html = (bar_html + addattribute("aria-valuemin",str(barParms[3])))
    bar_html = (bar_html + addattribute("aria-valuemax",str(barParms[4])))
    bar_html = (bar_html + ">" + str(barParms[4]) + "%" + "</div>" + new_line)
    bar_html = (bar_html + bulk_console_progress1_row_end)
    
    return(bar_html)


def get_bulk_geocode_console_html(geocodeid,geotype,runparms,progressbarList,state) :
    """
    * -------------------------------------------------------
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
    
    btext   =   BGM.get_status_bar_image(state)
    
    console_html = (console_html + bulk_console_status_start + btext)
    console_html = (console_html + bulk_console_status_middle)
    console_html = (console_html + bulk_console_status_end)

    console_html = (console_html + bulk_console_container)
    
    for i in range(len(progressbarList))  :
        console_html = (console_html + get_progress_bar_html(progressbarList[i]))
    
    error_log   =   BGM.get_geocode_runner_error_log()
    
    if(not(error_log is None)) :
        errorcount  =   error_log.get_error_count()
    else :
        errorcount  =   0
    
    console_html = (console_html + bulk_console_error_start)
    console_html = (console_html + "Total Geocode Errors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;" + str(errorcount))
    console_html = (console_html + bulk_console_error_end)
    
    console_html = (console_html + bulk_console_container_end)  

    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()


    from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import display_bulk_geocode_run_parms

    #from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_bulk_parms_table
    bulk_parms_html =   display_bulk_geocode_run_parms(geocodeid,geotype,runparms,280,90)


    console_html = (console_html + bulk_parms_html)
    console_html = (console_html + bulk_console_commands)
    
    from dfcleanser.Qt.utils.Geocode.GeocodeModel import BingId, GoogleId, QUERY

    if(geocodeid == BingId) :

        if(geotype == QUERY) :
            return_html     =   query_return_button_html.replace("XXXGEOCODEID",str(BingId))
        else :
            return_html     =   reverse_return_button_html.replace("XXXGEOCODEID",str(BingId))

    else :

        if(geotype == QUERY) :
            return_html     =   query_return_button_html.replace("XXXGEOCODEID",str(GoogleId))
        else :
            return_html     =   reverse_return_button_html.replace("XXXGEOCODEID",str(GoogleId))

    console_html = (console_html + return_html)
    
    console_html = (console_html + bulk_console_end)  
    console_html = (console_html + bulk_end)

    return(console_html)     
 


query_return_button_html  =   """
<div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
    <button type="button" id="dfc_run_parms" class="btn btn-primary" style="  width:400px;  height:40px;" onclick="display_geocoding_query_callback(XXXGEOCODEID)">ReEnter Geocodeing Query Parameters</button>
</div>
"""

reverse_return_button_html  =   """
<div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
    <button type="button" id="dfc_run_parms" class="btn btn-primary" style="  width:400px;  height:40px;" onclick="display_geocoding_reverse_callback(XXXGEOCODEID)">ReEnter Geocodeing Reverse Parameters</button>
</div>
"""



def display_geocoder_console(geocid,geotype,runParms,opstat,refresh=False,cmd=BGM.STOP) :
    """
    * -------------------------------------------------------
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

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY, BingId, GoogleId

    geocoding_heading_html  =   "<div class='dfcleanser-common-grid-header-large' width='400' >Bulk Geocoding Console</div><nr></br>"

    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()

    #from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_bulk_parms_table
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import display_bulk_geocode_run_parms
    bulk_parms_html =   display_bulk_geocode_run_parms(geocid,geotype,runParms,width=260,left=90)

    if(not (opstat.get_status())) :

        from dfcleanser.common.common_utils import displayHTML
        displayHTML(geocoding_heading_html)
        displayHTML(bulk_parms_html)

        if(geocid == BingId) :

            if(geotype == QUERY) :
                return_html     =   query_return_button_html.replace("XXXGEOCODEID",str(BingId))
            else :
                return_html     =   reverse_return_button_html.replace("XXXGEOCODEID",str(BingId))

        else :

            if(geotype == QUERY) :
                return_html     =   query_return_button_html.replace("XXXGEOCODEID",str(GoogleId))
            else :
                return_html     =   reverse_return_button_html.replace("XXXGEOCODEID",str(GoogleId))

        displayHTML(return_html)

    else :

        if(refresh) :
        
            state           =   BGM.get_geocode_runner_state()
            results_count   =   BGM.get_geocode_runner_results_count()
        
        else :
        
            results_count   =   0 
        
            if(cmd == BGM.LOAD) :    
                state  =   BGM.STOPPED
            else : 
                state  =   BGM.STOPPED
    
        if(geocid == GoogleId) :
        
            if(geotype == QUERY) :
                bar0 = [BGM.geocode_results_bar_text+str(results_count),"geocodeaddresses","bgqbulknumberlimit",0,100,results_count]
            else :
                bar0 = [BGM.reverse_results_bar_text+str(results_count),"geocodeaddresses","bgrbulknumberlimit",0,100,results_count]

            progressBars    =   [bar0]
            console_html    =   get_bulk_geocode_console_html(geocid,geotype,runParms,progressBars,state)
    
        elif(geocid == BingId) :
        
            if(geotype == QUERY) :
                bar0 = [BGM.geocode_results_bar_text+str(results_count),"geocodeaddresses","bbqbulknumberlimit",0,100,results_count]
            else :
                bar0 = [BGM.reverse_results_bar_text+str(results_count),"geocodeaddresses","bbrbulknumberlimit",0,100,results_count]

            progressBars    =   [bar0]
            console_html    =   get_bulk_geocode_console_html(geocid,geotype,runParms,progressBars,state)
        

        gridclasses     =   ["dfcleanser-common-grid-header-large","dfc-main"]
        gridhtmls       =   [geocoding_heading_html,console_html]
    
        display_generic_grid("geocode-console-wrapper",gridclasses,gridhtmls)
    
        if(refresh) :
        
            if(state    ==   BGM.STOPPED)       :   BGM.control_bulk_keys([BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.ENABLE,BGM.ENABLE,BGM.ENABLE],"A")
            elif(state  ==   BGM.PAUSED)        :   BGM.control_bulk_keys([BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.ENABLE,BGM.DISABLE,BGM.ENABLE],"B")
            elif(state  ==   BGM.FINISHED)      :   BGM.control_bulk_keys([BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.DISABLE,BGM.ENABLE],"C")
            elif(state  ==   BGM.ERROR_LIMIT)   :   BGM.control_bulk_keys([BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.ENABLE,BGM.ENABLE],"D")
    
        else :
        
            BGM.control_bulk_keys([BGM.ENABLE,BGM.DISABLE,BGM.DISABLE,BGM.DISABLE,BGM.ENABLE,BGM.ENABLE,BGM.DISABLE],"E")


def get_results_df_html(opstat) :
    """
    * --------------------------------------------------------
    * function : get the results for the source mini table
    * 
    * parms :
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    # build geocode results table   
    results_df_title    =   BGM.GEOCODING_RESULTS_DF_TITLE
    results_df          =   BGM.get_geocode_runner_results_log().get_geocoding_results_df()
    
    rowids              =   [0,1,None,(len(results_df)-2),(len(results_df)-1)]
    colids              =   [-1]
    
    for i in range(len(list(results_df.columns))) :
        colids.append(i)
    
    results_df_html     =   get_df_describe_table(results_df_title,results_df,rowids,colids,680,True)   

    return(results_df_html)


def get_bulk_display_tb() :
    
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
    df_title    =   cfg.get_config_value(BULK_GEOCODING_DF_TITLE)


    modified_jslist                =   bulk_geocode_display_tb_jsList
    modified_jslist[1]             =   modified_jslist[1].replace("XXXDISPLAY_BULK_SOURCE_DF","'" + str(df_title) + "'")
    modified_jslist[2]             =   modified_jslist[2].replace("XXXDISPLAY_BULK_RESULTS_DF","'" + BGM.GEOCODING_RESULTS_DF_TITLE + "'")
    modified_jslist[3]             =   modified_jslist[3].replace("XXXDISPLAY_BULK_ERRORS_DF","'" + BGM.GEOCODING_ERROR_LOG_DF_TITLE + "'")
    
     
    display_bulk_geocode_tb     =   ButtonGroupForm(bulk_geocode_display_tb_id,
                                                    bulk_geocode_display_tb_keyTitleList,
                                                    modified_jslist,
                                                    bulk_geocode_display_tb_centered)
    
    custom_keys     =   {"width":120,"height":75,"left-margin":185}
    display_bulk_geocode_tb.set_customstyle(custom_keys)
    
    display_bulk_geocode_tb_html    =   display_bulk_geocode_tb.get_html()
    
    return(display_bulk_geocode_tb_html)
    
    
def get_bulk_process_tb() :
    
    process_bulk_geocode_tb     =   ButtonGroupForm(bulk_geocode_process_tb_id,
                                                    bulk_geocode_process_tb_keyTitleList,
                                                    bulk_geocode_process_tb_jsList,
                                                    bulk_geocode_process_tb_centered)
    
    custom_keys     =   {"width":120,"height":75,"left-margin":185}
    process_bulk_geocode_tb.set_customstyle(custom_keys)
    
    process_bulk_geocode_tb_html    =   process_bulk_geocode_tb.get_html()
    
    return(process_bulk_geocode_tb_html)


#https://geopy.readthedocs.io/en/stable/#exceptions

def display_geocoder_process_results(optionid,opstat,showFull=False) :
    """
    * ---------------------------------------------------------
    * function : display the process bu;k geocoding results
    * 
    * parms :
    *  geotype      - geocoder cmd type
    *  opstat       - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY, BingId, GoogleId
    
    from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import dfc_Geocode_Runner
    dfc_Geocode_Runner.geocodingResults.finish_results_log(opstat)
    dfc_Geocode_Runner.geocodingErrorLog.finish_error_log(opstat)
    
    if(1) :
        
        geocoding_heading_html      =   "<div class='dfcleanser-common-grid-header'>Process Bulk Geocoding Results</div>"
        
        run_time    =   BGM.get_geocode_run_total_time()
        
        if(run_time > 0) :
            geocodes_per_sec    =   str(round(BGM.get_geocode_runner_results_log().get_results_count()/run_time,2))
        else :
            geocodes_per_sec    =   0

        labels      =   ["Total Geocode Results","Total Geocode Errors","Total Run Time - Seconds","Geocodes/Second"]
        values      =   [str(BGM.get_geocode_runner_results_log().get_results_count()),
                         str(BGM.get_geocode_runner_error_log().get_error_count()),
                         str(BGM.get_geocode_run_total_time()),
                         str(geocodes_per_sec)]
        
        stats_html  =   displayParms("Bulk Geocoding Run Stats",labels,values,"gstat",240,200)
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeControl import display_bulk_geocode_df_parms
        dfs_html    =   display_bulk_geocode_df_parms(240,200)

        geocid              =   BGM.get_geocode_runner_id()
        geotype             =   BGM.get_geocode_runner_type() 
        
        display_tb_html     =   None
        process_tb_html     =   None

        BGM.dfc_Geocode_Runner.geocodingResults.flush_results_to_dataframe(opstat)

        geocid      =   BGM.get_geocode_runner_id()
        geotype     =   BGM.get_geocode_runner_type() 
            
        if(geotype == QUERY) :
            if(geocid == GoogleId) :
                geoparms        =   cfg.get_config_value(bulk_google_query_input_id+"Parms")
            elif(geocid == BingId) :
                geoparms        =   cfg.get_config_value(bulk_bing_query_input_id+"Parms")
            
        else :
            if(geocid == GoogleId) :
                geoparms        =   cfg.get_config_value(bulk_google_reverse_input_id+"Parms")
            elif(geocid == BingId) :
                geoparms        =   cfg.get_config_value(bulk_bing_reverse_input_id+"Parms")

        df_title     =   geoparms[0]

        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import BULK_GEOCODING_DF_TITLE 
        cfg.set_config_value(BULK_GEOCODING_DF_TITLE,df_title)


        # ----------------------------------
        # get intermediate input forms
        # ----------------------------------
        proc_command_input_html     =   ""
        
        if(optionid == BGM.DISPLAY_BULK_RESULTS_BASE) :
        
            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()
        
        elif(optionid == BGM.DISPLAY_BULK_RESULTS) :
        
            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()
            
        elif(optionid == BGM.DISPLAY_BULK_SOURCE_DF) :
            
            geocid      =   BGM.get_geocode_runner_id()
            geotype     =   BGM.get_geocode_runner_type() 
            
            if(geotype == QUERY) :
                if(geocid == GoogleId) :
                    geoparms        =   cfg.get_config_value(bulk_google_query_input_id+"Parms")
                elif(geocid == BingId) :
                    geoparms        =   cfg.get_config_value(bulk_bing_query_input_id+"Parms")
            
            else :
                if(geocid == GoogleId) :
                    geoparms        =   cfg.get_config_value(bulk_google_reverse_input_id+"Parms")
                elif(geocid == BingId) :
                    geoparms        =   cfg.get_config_value(bulk_bing_reverse_input_id+"Parms")

            df_title     =   geoparms[0]

            display_blank_line()
            display_geocoding_dataframe(df_title,cfg.SWGeocodeUtility_ID,opstat)
            
            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()
        
        elif(optionid == BGM.DISPLAY_BULK_RESULTS_DF) :
            
            display_geocoding_dataframe(BGM.GEOCODING_RESULTS_DF_TITLE,cfg.SWGeocodeUtility_ID,opstat)

            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()
        
        elif(optionid == BGM.DISPLAY_BULK_ERRORS_DF) :
            
            display_geocoding_dataframe(BGM.GEOCODING_ERROR_LOG_DF_TITLE,cfg.SWGeocodeUtility_ID,opstat)
            
            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()

        elif(optionid == BGM.DISPLAY_BULK_RESULTS_RETURN) :
            
            display_tb_html     =   get_bulk_display_tb()
            process_tb_html     =   get_bulk_process_tb()

        if(display_tb_html is None) :
            
            display_tb_html         =   ""
            process_tb_html         =   ""
            
        gridclasses     =   ["dfcleanser-common-grid-header",
                             "dfc-top",
                             "dfc-main",
                             "dfc-bottom",
                             "dfc-footer"]

        gridhtmls       =   [geocoding_heading_html,
                             stats_html,
                             dfs_html,
                             display_tb_html,
                             process_tb_html]
    
        display_generic_grid("geocode-final-wrapper",gridclasses,gridhtmls)

        

def display_geocoding_dataframe(df_title,owner,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the process bu;k geocoding results
    * 
    * parms :
    *  df_title     -   dataframe title
    *  owner        -   owner of display
    *  opstat       -   opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(df_title == BGM.GEOCODING_ERROR_LOG_DF_TITLE) :
        
        from dfcleanser.Qt.utils.Geocode.BulkFeocodeModel import get_geocode_runner_error_log
        geocode_df          =   BGM.get_geocode_runner_error_log().get_error_log_df()    
        geocode_df_title    =   BGM.GEOCODING_ERROR_LOG_DF_TITLE
        geocode_tableid     =   "currentgeoocodeerrors"
        
    elif(df_title == BGM.GEOCODING_RESULTS_DF_TITLE) :
        
        from dfcleanser.Qt.utils.Geocode.BulkGeocodeModel import get_geocode_runner_results_log
        geocode_df          =   get_geocode_runner_results_log().get_geocoding_results_df() 
        
        geocode_df_title    =   BGM.GEOCODING_RESULTS_DF_TITLE
        geocode_tableid     =   "currentgeoocoderesults"
        
    else :
        
        geocode_df          =   cfg.get_dfc_dataframe_df(df_title)    
        geocode_df_title    =   df_title
        geocode_tableid     =   "currentgeoocodeource"
    
    if(len(geocode_df) == 0) :
        display_status_note("dataframe " + df_title + " has no rows")
        return()
        
    else :

        try :  
            
            num_cols    =   len(geocode_df.columns)
            
            if(geocode_df_title == BGM.GEOCODING_RESULTS_DF_TITLE) :
                
                numRows     =   500
                
                df_cols     =   list(geocode_df.columns)
                num_cols    =   len(df_cols)
                
                # query
                if("source_df_address" in df_cols) :
                    
                    if(num_cols == 4) :
                        col_widths  =   [88,720,81,81]
                    elif(num_cols == 5) :
                        col_widths  =   [88,360,81,81,360]
                
                # reverse
                else :
                    
                    if(num_cols == 8) :
                        col_widths  =   [48,81,81,260,125,100,125,100]
                    elif(num_cols == 9) :
                        col_widths  =   [48,81,81,160,105,40,85,60,300]  
                    else :
                        col_widths  =   None
                        
                displayParms    =   [numRows,col_widths]
                    
            else :
                
                numRows     =   200
                col_widths  =   [88,180,522,150]
                
                displayParms    =   [numRows,col_widths]
              
            dfparms     =   [geocode_df,geocode_df_title,geocode_tableid]
            
            from dfcleanser.Qt.DataInspection.DataInspectionWidgets import display_inspect_rows
            display_inspect_rows(0,dfparms,displayParms)
             
        except Exception as e:
            opstat.store_exception("Error displaying dataframe " + df_title,e)
            display_status_note("Error displaying dataframe " + df_title)














