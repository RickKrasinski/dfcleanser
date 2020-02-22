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
import dfcleanser.sw_utilities.sw_utility_bulk_geocode_control as subgc

import dfcleanser.common.help_utils as dfchelp

import dfcleanser.common.cfg as cfg

from dfcleanser.common.table_widgets import  (dcTable, ROW_MAJOR, get_row_major_table, SCROLL_DOWN, 
                                              get_df_describe_table, get_stats_table)   
from dfcleanser.common.html_widgets import   (addattribute, addstyleattribute, new_line, 
                                              InputForm, ButtonGroupForm)

from dfcleanser.common.common_utils import  (display_generic_grid, get_select_defaults,  displayParms,
                                             run_jscript, display_status)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   bulk geocoding console components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding main taskbar
#--------------------------------------------------------------------------
"""
bulk_geocode_process_tb_doc_title            =   "Process Bulk Geocode"
bulk_geocode_process_tb_title                =   "Process Bulk Geocode"
bulk_geocode_process_tb_id                   =   "procbulkgeocode"

bulk_geocode_process_tb_keyTitleList         =   ["Concat</br>Results to</br>Dataframe",
                                                  "Export</br>Results to</br>CSV File",
                                                  "Export</br>Results to</br>SQL Table",
                                                  "Show</br>Source</br>Dataframe",
                                                  "Show</br>Results</br>Dataframe",
                                                  "Show</br>Errors</br>Dataframe",
                                                  "End</br>Geocoding"]

bulk_geocode_process_tb_jsList               =   ["display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_RESULTS_CONCAT) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_RESULTS_EXPORT_CSV) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_RESULTS_EXPORT_SQL) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_SOURCE_DF) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_RESULTS_DF) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_ERRORS_DF) + ")",
                                                  "display_bulk_geocoding_results(" + str(sugm.DISPLAY_BULK_RESULTS_RETURN) + ")"]

bulk_geocode_process_tb_centered             =   False



bulk_geocode_process_tb_centered             =   False

bulk_geocode_process_tb_form                 =   [bulk_geocode_process_tb_id,
                                                  bulk_geocode_process_tb_keyTitleList,
                                                  bulk_geocode_process_tb_jsList,
                                                  bulk_geocode_process_tb_centered] 

"""
#--------------------------------------------------------------------------
#   bulk geocoding process concat input
#--------------------------------------------------------------------------
"""
bulk_geocode_proc_input_title             =   "Google Bulk Geoocoding Processing"
bulk_geocode_proc_input_id                =   "geocodebulkproc"
bulk_geocode_proc_input_idList            =   ["gbpaxis",
                                               "gbpjoin",
                                               "gbpdropaddrcols",
                                               None,None,None,None]

bulk_geocode_proc_input_labelList         =   ["axis_to_concatenate_over",
                                               "join_value",
                                               "drop_address_cols_flag",
                                               "Concat Results</br> To dataframe",
                                               "Clear","Return","Help"]


bulk_geocode_proc_input_typeList          =   ["select","select","select","button","button","button","button"]

bulk_geocode_proc_input_placeholderList   =   ["axis to concatenate ( 0-rows : 1-columns default eows )",
                                               "('inner' or 'outer' default : 'outer')",
                                               "drop address columns from source df (default : False)",
                                               None,None,None,None]

bulk_geocode_proc_input_jsList            =   [None,None,None,
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CONCAT_PROCESS) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CONCAT_CLEAR) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CONCAT_RETURN) + ")",
                                               "displayhelp('" + str(dfchelp.PROCESS_BULK_RESULTS_CONCAT_HELP) + "')"]

bulk_geocode_proc_input_reqList           =   [0,1,2]

bulk_geocode_proc_input_form              =   [bulk_geocode_proc_input_id,
                                               bulk_geocode_proc_input_idList,
                                               bulk_geocode_proc_input_labelList,
                                               bulk_geocode_proc_input_typeList,
                                               bulk_geocode_proc_input_placeholderList,
                                               bulk_geocode_proc_input_jsList,
                                               bulk_geocode_proc_input_reqList]  


"""
#--------------------------------------------------------------------------
#   bulk reverse process concat input
#--------------------------------------------------------------------------
"""
bulk_geocode_procr_input_title            =   "Google Bulk Geoocoding Processing"
bulk_geocode_procr_input_id               =   "reversebulkproc"
bulk_geocode_procr_input_idList           =   ["gbpaxis",
                                               "gbpjoin",
                                               None,None,None,None]

bulk_geocode_procr_input_labelList        =   ["axis_to_concatenate_over",
                                               "join_value",
                                               "Process</br> Reverse </br>Results",
                                               "Clear","Return","Help"]


bulk_geocode_procr_input_typeList         =   ["select","select","button","button","button","button"]

bulk_geocode_procr_input_placeholderList  =   ["axis to concatenate ( 0-rows : 1-columns default eows )",
                                               "('inner' or 'outer' default : 'outer')",
                                               "csv file name ",
                                              None,None,None,None]

bulk_geocode_procr_input_jsList           =   [None,None,None,
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_REVERSE_RESULTS_CONCAT_PROCESS) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_REVERSE_RESULTS_CONCAT_CLEAR) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_REVERSE_RESULTS_CONCAT_RETURN) + ")",
                                               "displayhelp('" + str(dfchelp.PROCESS_BULK_REVERSE_RESULTS_CONCAT_HELP) + "')"]

bulk_geocode_procr_input_reqList          =   [0,1]

bulk_geocode_procr_input_form             =   [bulk_geocode_procr_input_id,
                                               bulk_geocode_procr_input_idList,
                                               bulk_geocode_procr_input_labelList,
                                               bulk_geocode_procr_input_typeList,
                                               bulk_geocode_procr_input_placeholderList,
                                               bulk_geocode_procr_input_jsList,
                                               bulk_geocode_procr_input_reqList]  


"""
#--------------------------------------------------------------------------
#   bulk geocoding process export csv input
#--------------------------------------------------------------------------
"""
bulk_geocode_export_input_title            =   "Google Bulk Geoocoding Processing"
bulk_geocode_export_input_id               =   "bulkcsvexport"
bulk_geocode_export_input_idList           =   ["gbpcsvfilename",
                                                None,None,None,None]

bulk_geocode_export_input_labelList        =   ["csv_file_name",
                                                "Export Results</br> To csv file",
                                                "Clear","Return","Help"]


bulk_geocode_export_input_typeList         =   ["text","button","button","button","button"]

bulk_geocode_export_input_placeholderList  =   ["csv file name ",
                                                None,None,None,None]

bulk_geocode_export_input_jsList           =   [None,
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CSV_PROCESS) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CSV_CLEAR) + ")",
                                               "process_bulk_geocoding_results(" + str(sugm.PROCESS_BULK_RESULTS_CSV_RETURN) + ")",
                                               "displayhelp('" + str(dfchelp.PROCESS_BULK_RESULTS_CSV_HELP) + "')"]

bulk_geocode_export_input_reqList          =   [0]

bulk_geocode_export_input_form             =   [bulk_geocode_export_input_id,
                                                bulk_geocode_export_input_idList,
                                                bulk_geocode_export_input_labelList,
                                                bulk_geocode_export_input_typeList,
                                                bulk_geocode_export_input_placeholderList,
                                                bulk_geocode_export_input_jsList,
                                                bulk_geocode_export_input_reqList]  


SWUtility_bulk_geocode_console_inputs      =   [bulk_geocode_proc_input_id,bulk_geocode_procr_input_id,bulk_geocode_export_input_id]

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

bulk_console_commands = """        <div style="margin-top:10px; margin-bottom:20px; width:100%;">
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_START_GEOCODER) + """)">Start</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_STOP_GEOCODER) + """)">Stop</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_PAUSE_GEOCODER) + """)">Pause</button>
            </div>
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  margin-left:0px; width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_RESUME_GEOCODER) + """)">Resume</button>
                <button type="button" class="btn btn-primary" style="  width:100px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_CHECKPT_GEOCODER) + """)">Checkpoint</button>
            </div>
            <br>
            <div class="container" style="margin-top:20px; width:95%; overflow-x: hidden !important;">
                <button type="button" class="btn btn-primary" style="  width:300px;  height:40px;" onclick="controlbulkrun(""" + str(sugm.BULK_RESULTS_GEOCODER) + """)">Process Results</button>
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

bulk_console_error_start = """
                    <tr class='dfc-progress-row' style='height: 30px;'>
                        <td class='dfc-progress-title' style='width: 45%; font-size: 14px; font-family: Arial; text-align: left; padding-right: 20px;  padding-bottom: 20px;'  id="geocodeerrors">"""

bulk_console_error_end = """</td>
                    </tr>
"""
#Total Geocode Errors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;0</td>

bulk_console_end = """</div>
"""
bulk_end = """</div>"""

"""
#--------------------------------------------------------------------------
#   bulk geocoding console methods
#--------------------------------------------------------------------------
"""

geocode_results_bar_text     =   "Total Addresses Geocoded &nbsp;&nbsp;&nbsp;: &nbsp;"
reverse_results_bar_text     =   "Total Locations Geocoded &nbsp;&nbsp;&nbsp;: &nbsp;"
errors_bar_text              =   "Total Geocode Errors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;"

def display_base_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(bulk_geocode_process_tb_id,
                                               bulk_geocode_process_tb_keyTitleList,
                                               bulk_geocode_process_tb_jsList,
                                               bulk_geocode_process_tb_centered),False)


def set_progress_bar_value(geocid,geotype,barid,countvalue,barvalue) :
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
        
        if(barid == sugm.GEOCODE_BAR)   :   
            bid         =   "arcgistotaladdrs"
            countid     =   "geocodeaddresses"
            bhtml       =   geocode_results_bar_text + str(countvalue)
        else                            :   
            bid         =   "arcgiserrorrate"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)

            
    elif(geocid == sugm.GoogleId) :

        if(barid == sugm.GEOCODE_BAR)   :   
            bid         =   "bgqbulknumberlimit"
            countid     =   "geocodeaddresses"
            if(geotype == sugm.QUERY) :
                bhtml       =   geocode_results_bar_text + str(countvalue)
            else :
                bhtml       =   reverse_results_bar_text + str(countvalue)
        else                            :   
            bid         =   "bgqbulkfailurelimit"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)
            
    elif(geocid == sugm.BingId) :

        if(barid == sugm.GEOCODE_BAR)   :   
            bid         =   "bbqbulknumberlimit"
            countid     =   "geocodeaddresses"
            if(geotype == sugm.QUERY) :
                bhtml       =   geocode_results_bar_text + str(countvalue)
            else :
                bhtml       =   reverse_results_bar_text + str(countvalue)
        else                            :   
            bid         =   "bbrbulknumberlimit"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)
            
    elif(geocid == sugm.BaiduId) :

        if(barid == sugm.GEOCODE_BAR)   :   
            bid         =   "baiduqbulknumberlimit"
            countid     =   "geocodeaddresses"
            if(geotype == sugm.QUERY) :
                bhtml       =   geocode_results_bar_text + str(countvalue)
            else :
                bhtml       =   reverse_results_bar_text + str(countvalue)
        else                            :   
            bid         =   "baidurbulknumberlimit"
            countid     =   "geocodeerrors"
            bhtml       =   errors_bar_text + str(countvalue)
            

    if(barid == sugm.GEOCODE_BAR) :
        
        set_progress_bar_js = "set_bulk_progress_bar('" + bid + "', " + str(barvalue) + ");"
    
        run_jscript(set_progress_bar_js,"fail to set progress bar : ")

    set_progress_count_js = "$('#" + countid + "').html('" + bhtml +"');"

    run_jscript(set_progress_count_js,"fail to set count value : ")


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
    
    if(subgc.get_geocode_runner_state() == state) : return()
    
    if(sugm.GEOCODE_DEBUG)  :   sugm.log_dfc(-1,"set_status_bar " + str(state) + " " + str(subgc.get_geocode_runner_state()))
    
    if(state == sugm.STARTING) : 
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Starting_State.png"
    elif(state == sugm.RUNNING) : 
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Running_State.png"
    elif(state == sugm.STOPPED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopped_State.png"
    elif(state == sugm.FINISHED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Finished_State.png"
    elif(state == sugm.PAUSED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Paused_State.png"
    elif(state == sugm.STOPPING) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Stopping_State.png"
    elif(state == sugm.PAUSING) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Pausing_State.png"
    elif(state == sugm.ERROR_LIMIT) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Error_Limit_Exceeded_State.png"
    elif(state == sugm.CHECKPOINT_STARTED) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Checkpoint_Started_State.png"
    elif(state == sugm.CHECKPOINT_COMPLETE) :
        image   =   "https://rickkrasinski.github.io/dfcleanser/graphics/Checkpoint_Completed_State.png"

    import datetime 
    tstamp = datetime.datetime.now().time()

    change_state_js = ("$('#geocodeconsolestateId').attr('src'," + "'" + image + "?timestamp=" + str(tstamp) + "'" + ");")

    run_jscript(change_state_js,"fail to change console state : ")



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
        
    console_html = (console_html + bulk_console_error_start)
    console_html = (console_html + "Total Geocode Errors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;0")
    console_html = (console_html + bulk_console_error_end)
    
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

    print("get_bulk_parms_table_html",geocid,geotype,"\n",runParms)

    parmsHeader      =   [""]
    parmsRows        =   []
    parmsWidths      =   [100]
    parmsAligns      =   ["left"]

    parmskeys   =   list(runParms.keys())
    
    for i in range(len(parmskeys)) :
        
        parmsrow = [parmskeys[i] + "&nbsp;:"]
        parmsRows.append(parmsrow)
        parmsrow = ["&nbsp;&nbsp;&nbsp;" + str(runParms.get(parmskeys[i]))]
        parmsRows.append(parmsrow)
        
    parms_table = None
    
    if(geotype == sugm.QUERY) :           
        parms_table = dcTable("Query Parms","geocodeParms",
                              cfg.SWGeocodeUtility_ID,
                              parmsHeader,parmsRows,
                              parmsWidths,parmsAligns)
    else :
        parms_table = dcTable("Reverse Parms","geocodeParms",
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

    listHtml = get_row_major_table(parms_table,SCROLL_DOWN,False)

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
    #print("display_geocoder_console",runParms)

    geocoding_heading_html  =   "<div>Bulk Geocoding Console</div><nr></br>"
    parms_html  =   get_bulk_parms_table_html(geocid,geotype,runParms) 
    
    if(cmd == sugm.LOAD) :    state  =   sugm.STOPPED
    else : state  =   sugm.STOPPED
    
    if(geocid == sugm.ArcGISId) :
        
        bar0 = ["Total Addresses Geocoded","geocodeaddresses","arcgistotaladdrs",0,100,0]
        
        progressBars    =   [bar0]
        
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
        print("\n")
        
    elif(geocid == sugm.GoogleId) :
        
        if(geotype == sugm.QUERY) :
            bar0 = [geocode_results_bar_text+"0","geocodeaddresses","bgqbulknumberlimit",0,100,0]
        else :
            bar0 = [reverse_results_bar_text+"0","geocodeaddresses","bgrbulknumberlimit",0,100,0]

        progressBars    =   [bar0]
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
    
    elif(geocid == sugm.BingId) :
        
        if(geotype == sugm.QUERY) :
            bar0 = [geocode_results_bar_text+"0","geocodeaddresses","bbqbulknumberlimit",0,100,0]
        else :
            bar0 = [reverse_results_bar_text+"0","geocodeaddresses","bbrbulknumberlimit",0,100,0]

        progressBars    =   [bar0]
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
    
    elif(geocid == sugm.BingId) :
        
        if(geotype == sugm.QUERY) :
            bar0 = [geocode_results_bar_text+"0","geocodeaddresses","baiduqbulknumberlimit",0,100,0]
        else :
            bar0 = [reverse_results_bar_text+"0","geocodeaddresses","baidurbulknumberlimit",0,100,0]

        progressBars    =   [bar0]
        console_html    =   get_bulk_geocode_console_html(progressBars,state)
        
    print(console_html)
    
    gridclasses     =   ["dfcleanser-common-grid-header-large","dfc-left","dfc-right"]
    gridhtmls       =   [geocoding_heading_html,parms_html,
                         console_html]
    
    display_generic_grid("geocode-console-wrapper",gridclasses,gridhtmls)


def get_results_df_html(opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the results for the source mini table
    * 
    * parms :
    *  opstat - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    # build geocode results table   
    results_df_title    =   sugm.GEOCODING_RESULTS_DF_TITLE
    results_df          =   subgc.get_geocode_runner_results_log().get_geocoding_results_df()
    
    rowids              =   [0,1,None,(len(results_df)-2),(len(results_df)-1)]
    colids              =   [-1]
    
    for i in range(len(list(results_df.columns))) :
        colids.append(i)
    
    results_df_html     =   get_df_describe_table(results_df_title,results_df,rowids,colids,680,True)   

    return(results_df_html)


def display_geocoder_process_results(optionid,opstat,showFull=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the process bu;k geocoding results
    * 
    * parms :
    *  geotype      - geocoder cmd type
    *  opstat       - opStatus object to return status and error message
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(not ((optionid == sugm.DISPLAY_BULK_RESULTS_CONCAT_PROCESSED) or 
            (optionid == sugm.DISPLAY_BULK_RESULTS_CSV_PROCESSED))) :
        
        geocoding_heading_html      =   "<div>Process Bulk Geocoding Results</div>"

        labels      =   ["Total Geocode Results","Total Geocode Errors","Total Run Time - Seconds","Geocodes/Second"]
        values      =   [str(subgc.get_geocode_runner_results_log().get_results_count()),
                         str(subgc.get_geocode_runner_error_log().get_error_count()),
                         str(subgc.get_geocode_run_total_time()),
                         str(round(subgc.get_geocode_runner_results_log().get_results_count()/subgc.get_geocode_run_total_time(),2))]
        
        stats_html  =   displayParms("Bulk Geocoding Run Stats",labels,values,"gstat",200,0,False)

        geocid              =   subgc.get_geocode_runner_id()
        geotype             =   subgc.get_geocode_runner_type() 

        # ----------------------------------
        # get intermediate input forms
        # ----------------------------------
        proc_command_input_html     =   ""
    
        if(optionid == sugm.DISPLAY_BULK_RESULTS_BASE) :
        
            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)
        
        if(optionid == sugm.DISPLAY_BULK_RESULTS) :
        
            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)


        elif(optionid == sugm.DISPLAY_BULK_RESULTS_CONCAT) :
        
            if(geocid == sugm.GoogleId) :
        
                proc_command_input_form   =   InputForm(bulk_geocode_proc_input_form[0],bulk_geocode_proc_input_form[1],
                                                        bulk_geocode_proc_input_form[2],bulk_geocode_proc_input_form[3],
                                                        bulk_geocode_proc_input_form[4],bulk_geocode_proc_input_form[5],
                                                        bulk_geocode_proc_input_form[6])
            
                selectDicts     =   []
            
                geocsel         =   {"default":"1","list":["0","1"]}
                selectDicts.append(geocsel)
                geocsel         =   {"default":"outer","list":["outer","inner"]}
                selectDicts.append(geocsel)
                geocsel         =   {"default":"False","list":["True","False"]}
                selectDicts.append(geocsel)

                get_select_defaults(proc_command_input_form,
                                    bulk_geocode_proc_input_id,
                                    bulk_geocode_proc_input_idList,
                                    bulk_geocode_proc_input_typeList,
                                    selectDicts)

                proc_command_input_form.set_gridwidth(620)
                proc_command_input_form.set_custombwidth(170)
            
            elif(geocid == sugm.ArcGISId) :
        
                proc_command_input_form   =   InputForm(bulk_geocode_proc_input_form[0],bulk_geocode_proc_input_form[1],
                                                        bulk_geocode_proc_input_form[2],bulk_geocode_proc_input_form[3],
                                                        bulk_geocode_proc_input_form[4],bulk_geocode_proc_input_form[5],
                                                        bulk_geocode_proc_input_form[6])
        
                proc_command_input_form.set_gridwidth(620)
                proc_command_input_form.set_custombwidth(170)

        elif(optionid == sugm.DISPLAY_BULK_REVERSE_RESULTS_CONCAT) :
        
            if(geocid == sugm.GoogleId) :
            
                proc_command_input_form   =   InputForm(bulk_geocode_procr_input_form[0],bulk_geocode_procr_input_form[1],
                                                        bulk_geocode_procr_input_form[2],bulk_geocode_procr_input_form[3],
                                                        bulk_geocode_procr_input_form[4],bulk_geocode_procr_input_form[5],
                                                        bulk_geocode_procr_input_form[6])
        
                selectDicts     =   []
            
                geocsel         =   {"default":"1","list":["0","1"]}
                selectDicts.append(geocsel)
                geocsel         =   {"default":"outer","list":["outer","inner"]}
                selectDicts.append(geocsel)
                geocsel         =   {"default":"False","list":["True","False"]}
                selectDicts.append(geocsel)

                get_select_defaults(proc_command_input_form,
                                    bulk_geocode_procr_input_id,
                                    bulk_geocode_procr_input_idList,
                                    bulk_geocode_procr_input_typeList,
                                    selectDicts)

                proc_command_input_form.set_gridwidth(860)
                proc_command_input_form.set_custombwidth(110)


        elif(optionid == sugm.DISPLAY_BULK_RESULTS_EXPORT_CSV) :

            proc_command_input_form   =   InputForm(bulk_geocode_export_input_form[0],bulk_geocode_export_input_form[1],
                                                    bulk_geocode_export_input_form[2],bulk_geocode_export_input_form[3],
                                                    bulk_geocode_export_input_form[4],bulk_geocode_export_input_form[5],
                                                    bulk_geocode_export_input_form[6])
            
            if(geotype == sugm.QUERY) :
                
                gparms          =   cfg.get_config_value(subgw.bulk_google_query_input_id + "Parms")
                csv_file_name   =   gparms[0] + "_Geocoding_Results.csv"
                cfg.set_config_value(bulk_geocode_export_input_id + "Parms",[csv_file_name])
            
            else :
                
                gparms          =   cfg.get_config_value(subgw.bulk_google_reverse_input_id + "Parms")
                csv_file_name   =   gparms[0] + "_Reverse_Results.csv"
                cfg.set_config_value(bulk_geocode_export_input_id + "Parms",[csv_file_name])
        
            proc_command_input_form.set_gridwidth(860)
            proc_command_input_form.set_custombwidth(140)


        elif(optionid == sugm.DISPLAY_BULK_RESULTS_EXPORT_SQL) :

            proc_command_input_form   =   InputForm(bulk_geocode_export_input_form[0],bulk_geocode_export_input_form[1],
                                                    bulk_geocode_export_input_form[2],bulk_geocode_export_input_form[3],
                                                    bulk_geocode_export_input_form[4],bulk_geocode_export_input_form[5],
                                                    bulk_geocode_export_input_form[6])
        
            proc_command_input_form.set_gridwidth(860)
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)

            proc_command_input_form.set_custombwidth(90)


        elif(optionid == sugm.DISPLAY_BULK_SOURCE_DF) :
            
            geocid      =   subgc.get_geocode_runner_id()
            geotype     =   subgc.get_geocode_runner_type() 
            
            if(geotype == sugm.QUERY) :
                if(geocid == sugm.GoogleId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
                elif(geocid == sugm.ArcGISId) :
                    geoparms        =   cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
                elif(geocid == sugm.BingId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_bing_query_input_id+"Parms")
                elif(geocid == sugm.BaiduId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_baidu_query_input_id+"Parms")
            
            else :
                if(geocid == sugm.GoogleId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_google_reverse_input_id+"Parms")
                elif(geocid == sugm.BingId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_bing_reverse_input_id+"Parms")
                elif(geocid == sugm.BingId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_baidu_reverse_input_id+"Parms")
                    

            df_title     =   geoparms[0]
            print("\n")
            display_dataframe(df_title,cfg.SWGeocodeUtility_ID,opstat)
            
            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)

        
        elif(optionid == sugm.DISPLAY_BULK_RESULTS_DF) :
            
            print("\n")
            display_dataframe(sugm.GEOCODING_RESULTS_DF_TITLE,cfg.SWGeocodeUtility_ID,opstat)

            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)

        
        elif(optionid == sugm.DISPLAY_BULK_ERRORS_DF) :
            
            print("\n")
            display_dataframe(sugm.GEOCODING_ERROR_LOG_DF_TITLE,cfg.SWGeocodeUtility_ID,opstat)
            
            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)

        elif(optionid == sugm.DISPLAY_BULK_RESULTS_RETURN) :
            proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                          bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
            custom_keys     =   {"width":110,"left-margin":100}
            proc_command_input_form.set_buttonstyle(custom_keys)

        #proc_command_input_form.dump()
        proc_command_input_html     =   proc_command_input_form.get_html()

        gridclasses     =   ["dfcleanser-common-grid-header",
                             "dfc-top",
                             "dfc-footer"]
    
        gridhtmls       =   [geocoding_heading_html,
                             stats_html,
                             proc_command_input_html]
    
        display_generic_grid("geocode-final-wrapper",gridclasses,gridhtmls)
        

    # ----------------------------------
    # display final processed results 
    # ----------------------------------
    
    else :
        
        proc_command_input_html     =   ""
    
        proc_command_input_form   =   ButtonGroupForm(bulk_geocode_process_tb_form[0],bulk_geocode_process_tb_form[1],
                                                      bulk_geocode_process_tb_form[2],bulk_geocode_process_tb_form[3])
    
        custom_keys     =   {"width":110,"left-margin":100}
        proc_command_input_form.set_buttonstyle(custom_keys)
        
        proc_command_input_html     =   proc_command_input_form.get_html()  
        
        if(optionid == sugm.DISPLAY_BULK_RESULTS_CONCAT_PROCESSED) :     
            
            geocid      =   subgc.get_geocode_runner_id()
            geotype     =   subgc.get_geocode_runner_type() 
            #runParms    =   subgc.get_geocode_runParms()

            geocoding_heading_html      =   "<div>Bulk Geocoding Concatenate Final Results</div>"
           
            # build geocode source df table   
            if(geotype == sugm.QUERY) :
                if(geocid == sugm.GoogleId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_google_query_input_id+"Parms")
                elif(geocid == sugm.ArcGISId) :
                    geoparms        =   cfg.get_config_value(subgw.batch_arcgis_query_id+"Parms")
                elif(geocid == sugm.BingId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_bing_query_input_id+"Parms")
                elif(geocid == sugm.BaiduId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_baidu_query_input_id+"Parms")
            
            else :
                if(geocid == sugm.GoogleId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_google_reverse_input_id+"Parms")
                elif(geocid == sugm.BingId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_bing_reverse_input_id+"Parms")
                elif(geocid == sugm.BaiduId) :
                    geoparms        =   cfg.get_config_value(subgw.bulk_baidu_reverse_input_id+"Parms")

            source_df_title     =   geoparms[0]
            source_df           =   cfg.get_dfc_dataframe_df(source_df_title)
            
            stats_title                 =   source_df_title + " dataframe"
            stats_colnames              =   ["Total Rows","Total Columns"]
    
            stats_values                =   [len(source_df),len(source_df.columns)]
                                     
            stats_html                  =   get_stats_table(stats_title,stats_colnames,stats_values)

        if(optionid == sugm.DISPLAY_BULK_RESULTS_CSV_PROCESSED) :     

            geocoding_heading_html      =   "<div>Bulk Geocoding Export CSV Final Results</div>"
           
            results_df_title    =   sugm.GEOCODING_RESULTS_DF_TITLE
            results_df          =   subgc.get_geocode_runner_results_log().get_geocoding_results_df()
            
            stats_title         =   results_df_title + " dataframe"
            stats_colnames      =   ["Total Rows","Total Columns"]
    
            stats_values        =   [len(results_df),len(results_df.columns)]
                                     
            stats_html          =   get_stats_table(stats_title,stats_colnames,stats_values)


        gridclasses     =   ["dfcleanser-common-grid-header",
                             "dfc-header",
                             "dfc-footer"]
    
        gridhtmls       =   [geocoding_heading_html,
                             stats_html,
                             proc_command_input_html]
    
        display_generic_grid("geocode-final-wrapper",gridclasses,gridhtmls)



def display_dataframe(df_title,owner,opstat) :
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

    df  =   cfg.get_dfc_dataframe_df(df_title)
    
    if(len(df) == 0) :
        display_status("dataframe " + df_title + " has no rows")
        return()
        
    else :

        try :  
              
            df_heading_html      =   "<div>" + df_title + "&nbsp;dataframe</div>"
                    
            rows_table      =   dcTable(df_title,df_title + "_search_" + str(owner),owner)
        
            from dfcleanser.common.display_utils import display_sample_rows
            sample_row_html =   display_sample_rows(df,rows_table,0,0,opstat,False)
                    
            gridclasses     =   ["dfcleanser-common-grid-header","df-display-wrapper-content"]
            gridhtmls       =   [df_heading_html,sample_row_html]
                    
            display_generic_grid("df-display-wrapper",gridclasses,gridhtmls)
                    
             
        except Exception as e:
            opstat.store_exception("Error displaying dataframe " + df_title,e)
            display_status("Error displaying dataframe " + df_title)




















