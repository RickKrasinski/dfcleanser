"""
# system_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.system.system_model as sysm

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, 
                                            get_html_spaces, CheckboxGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, SIMPLE)

from dfcleanser.common.common_utils import (display_notes, RunningClock, alert_user, displayHTML,  
                                            display_generic_grid, get_select_defaults)

from dfcleanser.common.display_utils import (displayParms)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    System html form elements
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    dataframe manager inputs
#--------------------------------------------------------------------------
"""
dfmgr_input_title                 =   "Dataframes Manager"
dfmgr_input_id                    =   "dfmgrform"
dfmgr_input_idList                =   ["dfmgrtitle",
                                       "dfnumrows",
                                       "dfnumcols",
                                       "dfnotes",
                                       None,None,None,None,None]

dfmgr_input_labelList             =   ["df_title",
                                       "df_num_rows",
                                       "df_num_cols",
                                       "df_notes",
                                       "Add df</br>to</br>dfc mgr",
                                       "Drop df</br>from</br>dfc mgr",
                                       "Update df</br>Notes in</br>dfc mgr",
                                       "Return",
                                       "Help"]

dfmgr_input_typeList              =   ["select","text","text",maketextarea(5),
                                       "button","button","button","button","button"]

dfmgr_input_placeholderList       =   ["dataframe title",
                                       "number of rows",
                                       "number of columns",
                                       "dataframe notes",
                                       None,None,None,None,None]

dfmgr_input_jsList                =   [None,None,None,None,
                                       "dfmgr_callback("+str(sysm.DISPLAY_ADD_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.DROP_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.UPDATE_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.RETURN_DATAFRAME)+")",
                                       "displayhelp('" + str(dfchelp.SYS_ENVIRONMENT_DFMGR_TASKBAR_ID) + "')"]

dfmgr_input_reqList               =   [0]

dfmgr_input_form                  =   [dfmgr_input_id,
                                       dfmgr_input_idList,
                                       dfmgr_input_labelList,
                                       dfmgr_input_typeList,
                                       dfmgr_input_placeholderList,
                                       dfmgr_input_jsList,
                                       dfmgr_input_reqList] 

 
dfmgr_add_input_title             =   "Dataframes Manager"
dfmgr_add_input_id                =   "dfmgraddform"
dfmgr_add_input_idList            =   ["dftitleadd",
                                       "dfaddcode",
                                       "dfnotesadd",
                                       None,None,None]

dfmgr_add_input_labelList         =   ["df_title",
                                       "df_name",
                                       "df_notes",
                                       "Add</br>df",
                                       "Return",
                                       "Help"]

dfmgr_add_input_typeList          =   ["text","text",maketextarea(5),
                                       "button","button","button"]

dfmgr_add_input_placeholderList   =   ["dfc mgr dataframe title",
                                       "datraframe object",
                                       "dfc mgr dataframe notes",
                                       None,None,None]

dfmgr_add_input_jsList            =   [None,None,None,
                                       "dfmgr_callback("+str(sysm.PROCESS_ADD_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.RETURN_DATAFRAME)+")",
                                       "displayhelp('" + str(dfchelp.SYS_ENVIRONMENT_DFMGR_ADD_ID) + "')"]

dfmgr_add_input_reqList           =   [0,1]

dfmgr_add_input_form              =   [dfmgr_add_input_id,
                                       dfmgr_add_input_idList,
                                       dfmgr_add_input_labelList,
                                       dfmgr_add_input_typeList,
                                       dfmgr_add_input_placeholderList,
                                       dfmgr_add_input_jsList,
                                       dfmgr_add_input_reqList]  


"""
#--------------------------------------------------------------------------
#    notebook README inputs
#--------------------------------------------------------------------------
"""
readme_input_title                =   "NoteBook README"
readme_input_id                   =   "dcreadmeform"
readme_input_idList               =   ["nbname",None]

readme_input_labelList            =   ["README","Return"]

readme_input_typeList             =   [maketextarea(50),"button"]

readme_input_placeholderList      =   [sysm.READMEText,None]

readme_input_jsList               =   [None,"process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")"]

readme_input_reqList              =   [0]

readme_input_form                 =   [readme_input_id,
                                       readme_input_idList,
                                       readme_input_labelList,
                                       readme_input_typeList,
                                       readme_input_placeholderList,
                                       readme_input_jsList,
                                       readme_input_reqList]  


"""
#--------------------------------------------------------------------------
#    system environment task bar
#--------------------------------------------------------------------------
"""
system_environment_doc_title            =   "System Options"
system_environment_doc_id               =   "systemoptions"
system_environment_title                =   None

system_environment_keyTitleList         =   ["Utilities</br>Manager",
                                             "dataframe</br>Manager",
                                             "System",
                                             "About",
                                             "EULA",
                                             "Clear","Reset","Help"]

system_environment_jsList               =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DATAFRAMES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_SYSTEM)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_ABOUT)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_EULA)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + "')"]

system_environment_centered             =   True

system_environmentA_doc_title           =   "System Options"
system_environmentA_doc_id              =   "systemoptionsA"
system_environmentA_title               =   None

system_environmentA_keyTitleList        =   ["Select</br>Utilities",
                                             "dataframe</br>Manager",
                                             "System"]

system_environmentA_jsList              =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DATAFRAMES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_SYSTEM)+")"]

system_environmentA_centered            =   True

system_environmentB_doc_title           =   "System Options"
system_environmentB_doc_id              =   "systemoptionsB"
system_environmentB_title               =   None

system_environmentB_keyTitleList        =   ["About","EULA","Clear","Reset","Help"]

system_environmentB_jsList              =   ["process_system_tb_callback("+str(sysm.DISPLAY_ABOUT)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_EULA)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp('" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + "')"]

system_environmentB_centered            =   True




"""
#--------------------------------------------------------------------------
#    chapters checkboxes
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfcleanser core modules checkboxes
#--------------------------------------------------------------------------
"""
dfc_core_modules_checkbox_title      =   "dfcleanser Core Modules"
dfc_core_modules_checkbox_id         =   "dfc_core_cb"

dfc_core_modules_checkbox_idList     =   ["dfcimport","dfcinspect","dfccleansing","dfctransform","dfcexport"]
dfc_core_modules_checkbox_labelList  =   ["Data Import","Data Inspection","Data Cleansing","Data Transform","Data Export"]

dfc_core_modules_checkbox_jsList     =   [None,None,None,None,None]

dfc_utils_modules_checkbox_title      =   "dfcleanser Utilities"
dfc_utils_modules_checkbox_id         =   "dfc_utils_cb"

dfc_utils_modules_checkbox_idList     =   ["dfcutildatastruct","dfcutilgeocode","dfcutilzipcode","dfcutildfsubset","dfcutildfcensus","dfcscripting"]
dfc_utils_modules_checkbox_labelList  =   ["Common","Geocoding","Zipcodes","df Subset","Census","Scripting"]

dfc_utils_modules_checkbox_jsList     =   [None,None,None,None,None,None]

system_chapters_tb_doc_title           =   "Chapters"
system_chapters_tb_doc_id              =   "chaptersoptions"
system_chapters_tb_title               =   None

system_chapters_tb_keyTitleList        =   ["Load Utilities</br>Selected","Return","Help"]

system_chapters_tb_jsList              =   ["process_system_tb_callback("+str(sysm.PROCESS_CHAPTERS)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                            "displayhelp('" + str(dfchelp.SYS_ENVIRONMENT_UTILS_TASKBAR_ID) + "')"]

system_chapters_tb_centered            =   True

system_inputs                          =   [dfmgr_input_id,dfmgr_add_input_id,readme_input_id]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    System display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_system_main_taskbar() :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        from dfcleanser.common.display_utils import display_dfcleanser_taskbar
        display_dfcleanser_taskbar(ButtonGroupForm(system_environment_doc_id,
                                                   system_environment_keyTitleList,
                                                   system_environment_jsList,
                                                   system_environment_centered))
    else :
        
        system_tb_A     =   ButtonGroupForm(system_environmentA_doc_id,
                                            system_environmentA_keyTitleList,
                                            system_environmentA_jsList,
                                            system_environmentA_centered)
        
        system_tb_A.set_gridwidth(480)
        system_tb_A_html    =   system_tb_A.get_html()
        
        system_tb_B     =   ButtonGroupForm(system_environmentB_doc_id,
                                            system_environmentB_keyTitleList,
                                            system_environmentB_jsList,
                                            system_environmentB_centered)
        
        system_tb_B.set_gridwidth(480)
        system_tb_B_html    =   system_tb_B.get_html()
        
        gridclasses     =   ["dfc-top-","dfc-footer"]
        gridhtmls       =   [system_tb_A_html,system_tb_B_html]
    
        display_generic_grid("dfcleanser-system-tb-pop-up-wrapper",gridclasses,gridhtmls)
 
      
def display_add_df_input() :
    """
    * -------------------------------------------------------------------------- 
    * function : add a dataframe to the dfc list 
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import InputForm
    dfmanager_input_form = InputForm(dfmgr_add_input_id,
                                     dfmgr_add_input_idList,
                                     dfmgr_add_input_labelList,
                                     dfmgr_add_input_typeList,
                                     dfmgr_add_input_placeholderList,
                                     dfmgr_add_input_jsList,
                                     dfmgr_add_input_reqList)
                    
    dfmanager_input_form.set_shortForm(True)
    dfmanager_input_form.set_gridwidth(480)
    dfmanager_input_form.set_custombwidth(70)
    dfmanager_input_form.set_fullparms(True)
        
    dfmgr_input_html = dfmanager_input_form.get_html()
    
    dfmgr_heading_html       =   "<div>Add df to dfc dataframe Manager</div>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dfmgr_heading_html,dfmgr_input_html]
    
    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer            
    display_pop_up_buffer()    
    
    
def get_current_checkboxes(cbtype) :
    """
    * -------------------------------------------------------------------------- 
    * function : get currently displayed module checkboxes
    * 
    * parms :
    *  cbtype       - checkbox type
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(cbtype == sysm.CORE) :
        return([1,1,1,1,1])
    else :
        return(cfg.get_util_chapters_loaded())


def display_system_chapters_taskbar() :
    """
    * -------------------------------------------------------------------------- 
    * function : display system taskbar
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    print("\n")
    dfc_utils_modules_checkbox =  CheckboxGroupForm(dfc_utils_modules_checkbox_id,
                                                    dfc_utils_modules_checkbox_idList,
                                                    dfc_utils_modules_checkbox_labelList,
                                                    dfc_utils_modules_checkbox_jsList,
                                                    get_current_checkboxes(sysm.UTILITIES))
    
    if(not (cfg.get_dfc_mode() == cfg.INLINE_MODE)) :
        dfc_utils_modules_checkbox.set_rows_count([2,2,1])
    
    dfc_utils_modules_heading_html       =   "<div>dfcleanser Utilities</div><br>"
    dfc_utils_modules_checkbox_html      =   dfc_utils_modules_checkbox.get_html()
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dfc_utils_modules_heading_html,dfc_utils_modules_checkbox_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfcleanser-chapters-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    dfc_script_modules_tb           =   ButtonGroupForm(system_chapters_tb_doc_id,
                                                        system_chapters_tb_keyTitleList,
                                                        system_chapters_tb_jsList,
                                                        system_chapters_tb_centered)
    
    dfc_script_modules_tb.set_gridwidth(480)
    dfc_script_modules_tb.set_custombwidth(160)
    
    dfc_script_modules_tb_html      =   dfc_script_modules_tb.get_html()

    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [dfc_script_modules_tb_html]
    
    display_generic_grid("dfcleanser-chapters-tb-wrapper",gridclasses,gridhtmls)

    print("\n")


def get_df_list_html(title) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the html for list of dfc dataframes
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    fparms  =   []

    if(title is None) :

        if(cfg.is_a_dfc_dataframe_loaded()) :
            df_titles   =   cfg.get_dfc_dataframes_titles_list()
            fparms      =   [df_titles[0],str(len(cfg.get_dfc_dataframe_df(df_titles[0]))),
                             str(len(cfg.get_dfc_dataframe_df(df_titles[0]).columns)),
                             cfg.get_dfc_dataframe_notes(df_titles[0])]
        else :
            fparms  =   ["","","",""]
    
    else :
    
        if(cfg.is_a_dfc_dataframe_loaded()) :
            dfc_df  =   cfg.get_dfc_dataframe(title)
        
            if(dfc_df is None) :
                fparms  =   ["","","",""] 
            else :
                fparms  =   [title,str(len(cfg.get_dfc_dataframe_df(title))),
                             str(len(cfg.get_dfc_dataframe_df(title).columns)),
                             cfg.get_dfc_dataframe_notes(title)]
        else :
            fparms  =   ["","","",""]    
        
    parmsProtect = [False,True,True,False]
        
    cfg.set_config_value(dfmgr_input_id+"Parms",fparms)
    cfg.set_config_value(dfmgr_input_id+"ParmsProtect",parmsProtect)
            
    dfmanager_input_form = InputForm(dfmgr_input_id,
                                     dfmgr_input_idList,
                                     dfmgr_input_labelList,
                                     dfmgr_input_typeList,
                                     dfmgr_input_placeholderList,
                                     dfmgr_input_jsList,
                                     dfmgr_input_reqList)
                    
    selectDicts =   []
    df_titles   =   cfg.get_dfc_dataframes_titles_list()
     
    #if(df_titles is None) :
    if(not (cfg.is_a_dfc_dataframe_loaded())) :    
        dfs     =   {"default":" ","list":[" "]}
    else :   
        dfs     =   {"default":str(fparms[0]),"list":df_titles,"callback":"select_new_df"}
    selectDicts.append(dfs)
        
    get_select_defaults(dfmanager_input_form,
                        dfmgr_input_id,
                        dfmgr_input_idList,
                        dfmgr_input_typeList,
                        selectDicts)

    dfmanager_input_form.set_shortForm(True)
    dfmanager_input_form.set_gridwidth(480)
    dfmanager_input_form.set_custombwidth(90)
    dfmanager_input_form.set_fullparms(True)
        
    dfmgr_input_html = dfmanager_input_form.get_html()
    
    return(dfmgr_input_html)


def display_df_dataframes(title) :  
    """
    * -------------------------------------------------------------------------- 
    * function : display dataframe manager form
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
 
    dfmgr_input_html    =  get_df_list_html(title)
    dfmgr_heading_html  =   "<div>Current dfCleanser dataframes </div>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dfmgr_heading_html,dfmgr_input_html]

    print("\n")
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer            
    display_pop_up_buffer()    


def display_offline() :
    """
    * -------------------------------------------------------------------------- 
    * function : display offline toggle mode
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    from dfcleanser.common.html_widgets import InputForm
    dfmanager_input_form = InputForm(dfmgr_offline_input_id,
                                     dfmgr_offline_input_idList,
                                     dfmgr_offline_input_labelList,
                                     dfmgr_offline_input_typeList,
                                     dfmgr_offline_input_placeholderList,
                                     dfmgr_offline_input_jsList,
                                     dfmgr_offline_input_reqList)
    
    selectDicts      =   []
    
    if(sysm.get_dfc_run_offline_status()) :
        stat    =   "True"
    else :
        stat    =   "False"
    offline_mode     =   {"default": stat,"list":["False","True"]}
    selectDicts.append(offline_mode)
        
    get_select_defaults(dfmanager_input_form,
                        dfmgr_offline_input_id,
                        dfmgr_offline_input_idList,
                        dfmgr_offline_input_typeList,
                        selectDicts)

                    
    dfmanager_input_form.set_shortForm(True)
    dfmanager_input_form.set_gridwidth(480)
    dfmanager_input_form.set_custombwidth(100)
    dfmanager_input_form.set_fullparms(True)
        
    dfmgr_input_html = dfmanager_input_form.get_html()
    
    dfmgr_heading_html       =   "<div>Run dfc Offline Manager</div>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dfmgr_heading_html,dfmgr_input_html]
    
    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    from dfcleanser.common.display_utils import display_pop_up_buffer            
    display_pop_up_buffer()    
    



def display_EULA():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser EULA
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.system.system_control import isEULA_read
    
    if(isEULA_read()) : 
        eula_file_name  =   cfg.get_common_files_path()+"\EULARead.html" 
    else :
        eula_file_name  =   cfg.get_common_files_path()+"\EULA.html"

    try :    
        eula_file = open(eula_file_name, 'r', encoding="utf-8")
        eula_html = (eula_file.read())
        eula_file.close()

        displayHTML(eula_html) 
            
    except :
        alert_user("Unable to open EULA file" + eula_file_name)

def display_README():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser README
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    readme_file_name  =   cfg.get_notebookPath()+"\dfcleanser\html\README.md"
    
    try :    
        readme_file = open(readme_file_name, 'r', encoding="utf-8")# as eula_file :
        readme_md   = (readme_file.read()) #json.load(eula_file)
        readme_file.close()
        
        from IPython.display import Markdown, display
        display(Markdown(readme_md))
            
    except :
        alert_user("Unable to open README file" + readme_file)


def show_sys_info():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser system info
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    title       =   "Installed Python Info"
    ptitles     =   ["Version","API","Info"]
    pvalues     =   [str(get_python_version()),str(sys.api_version),str(sys.version_info)]
    
    parms_html      =   displayParms(title,ptitles,pvalues,cfg.System_ID,None,0,False,11)
    notes_html      =   show_setup_notes()
    libs_html       =   show_libs_info()    
    libs_notes_html =   show_libs_notes()
    
    gridclasses     =   ["dfc-header","dfc-top","dfc-bottom","dfc-footer"]
    gridhtmls       =   [parms_html,notes_html,libs_html,libs_notes_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-sys-info-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-sys-info-pop-up-wrapper",gridclasses,gridhtmls)
    
    from dfcleanser.common.display_utils import display_pop_up_buffer
    display_pop_up_buffer()
    
    
def show_about_info():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser about info
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    print("\nAuthor : Rick Krasinski")
    print("Dataframe Cleanser Version : 1.0.0")


def show_libs_notes():
    
    libNotes = []
    libNotes.append("Green indicates installed version matches tested with version.")
    libNotes.append("Yellow indicates installed version newer than tested with version and potential problem.")
    libNotes.append("Red indicates installed version older than tested with version and potential problem requiring update.")
 
    lib_notes_html      =   display_notes(libNotes,False)

    return(lib_notes_html)

def show_libs_info():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser libs info
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    clock = RunningClock()
    clock.start()
    
    
    libsHeader    =   ["Lib Name","Tested</br>With</br>Version","Installed</br>Version"]
    libsRows      =   []
    libsWidths    =   [40,30,30]
    libsAligns    =   ["left","center","center"]


    testedModules               =   ["Python","IPython","ipywidgets","ipykernel","notebook",
                                     "pandas","sklearn","matplotlib","numpy","scipy",
                                     "json","SQLAlchemy","pymysql","mysql-connector-python",
                                     "pyodbc","pymssql","SQLite3","psycopg2","cx-oracle",
                                     "geopy","googlemaps","arcgis"]
    
    testedmoduleVersions        =   ["3.7.3","7.4.0","7.4.2","5.1.0","5.7.8",
                                     "0.24.2","0.20.3","3.0.3","1.16.2","1.2.1",
                                     "2.0.9","1.3.1","0.9.3","8.0.16",
                                     "4.0.26","2.1.4","3.8.6","2.8.2","7.1.3",
                                     "1.19.0","2.5.1","1.6.1"]

    installedmoduleVersions     =   []

    installedmoduleVersions.append(str(get_python_version()))
    import IPython
    installedmoduleVersions.append(str(IPython.__version__))
    
    try :
        import ipywidgets
        installedmoduleVersions.append(str(ipywidgets.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
        
    try :
        import ipykernel
        installedmoduleVersions.append(str(ipykernel.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import notebook
        installedmoduleVersions.append(str(notebook.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import pandas
        installedmoduleVersions.append(str(pandas.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import sklearn
        installedmoduleVersions.append(str(sklearn.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import matplotlib
        installedmoduleVersions.append(str(matplotlib.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import numpy
        installedmoduleVersions.append(str(numpy.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import scipy
        installedmoduleVersions.append(str(scipy.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import json
        installedmoduleVersions.append(str(json.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import sqlalchemy
        installedmoduleVersions.append(str(sqlalchemy.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import pymysql
        installedmoduleVersions.append(str(pymysql.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import mysql.connector    
        installedmoduleVersions.append(str(mysql.connector.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
        
    #import pyodbc    
    installedmoduleVersions.append(str("unknown"))
    
    try :
        import pymssql    
        installedmoduleVersions.append(str(pymssql.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
        
    #import sqlite3    
    installedmoduleVersions.append(str("unknown"))
    
    try :
        import psycopg2
    
        pgversion =  str(psycopg2.__version__)
        found = pgversion.find("(")
        if(found > 0)  :
            installedmoduleVersions.append(pgversion[0:found-1])
        else :
            installedmoduleVersions.append(pgversion)
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import cx_Oracle    
        installedmoduleVersions.append(str(cx_Oracle.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import geopy    
        installedmoduleVersions.append(str(geopy.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    try :
        import googlemaps    
        installedmoduleVersions.append(str(googlemaps.__version__))
    except :
        installedmoduleVersions.append(str("-1"))
    
    try :
        import arcgis    
        installedmoduleVersions.append(str(arcgis.__version__))
    except :
        installedmoduleVersions.append(str("-1"))

    
    for i in range(len(testedModules)) :
        libsrow = []
        libsrow.append(str(testedModules[i]))
        libsrow.append(str(testedmoduleVersions[i]))
        if(installedmoduleVersions[i] == "-1") :
            installedmoduleVersions[i] = "not installed"

        libsrow.append(str(installedmoduleVersions[i]))
        
        libsRows.append(libsrow)
    
    colorList = []    
    for i in range(len(testedModules)) :
        colorRow = []
        if(installedmoduleVersions[i] == "not installed") :
            colorRow = [sysm.Yellow,sysm.Yellow,sysm.Red]
        elif(installedmoduleVersions[i] == "unknown") :
            colorRow = [sysm.Green,sysm.Green,sysm.Yellow]
        elif(testedmoduleVersions[i] > installedmoduleVersions[i]) :
            colorRow = [sysm.Red,sysm.Red,sysm.Red]
        elif(testedmoduleVersions[i] < installedmoduleVersions[i]) :
            colorRow = [sysm.Yellow,sysm.Yellow,sysm.Yellow]
        else :
            colorRow = [sysm.Green,sysm.Green,sysm.Green]
        
        colorList.append(colorRow)

    libs_table = dcTable("Python Libraries","dcmodsTable",
                         cfg.System_ID,
                         libsHeader,libsRows,libsWidths,libsAligns)

    libs_table.set_tabletype(SIMPLE)
    libs_table.set_rowspertable(len(testedModules))
    libs_table.set_color(True)
    libs_table.set_colorList(colorList)
    libs_table.set_small(True)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        libs_table.set_smallwidth(99)
        libs_table.set_smallmargin(2)
    else :
        libs_table.set_smallwidth(98)
        libs_table.set_smallmargin(2)
        
    libs_table.set_checkLength(False)
    libs_table.set_border(False)

    clock.stop()  
    
    return(libs_table.get_html())


    
def show_setup_notes():
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser setup notes
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    title       =   "Setup Notes"
    ptitles     =   ["Notebook Name","Notebook Path","dfcleanser path"]
    pvalues     =   [cfg.get_notebookName(),cfg.get_notebookPath(),cfg.get_dfcleanser_location()]
    
    parms_html      =   displayParms(title,ptitles,pvalues,cfg.System_ID,None,0,False,11)
    
    return(parms_html)
   
    setupNotes = []
    nbname = cfg.get_notebookName()
    if(not (nbname == None)) :
        setupNotes.append("Notebook Name" + get_html_spaces(22) + ":&nbsp;&nbsp;" + str(nbname))
    nbpath = cfg.get_notebookPath()    
    if(not (nbpath == None)) :
        setupNotes.append("Notebook Path" + get_html_spaces(23) + ":&nbsp;&nbsp;" + str(nbpath))
    #import jupyter_core
    setupNotes.append("Notebook Path" + get_html_spaces(2) + ":&nbsp;&nbsp;</br>&nbsp;&nbsp;" + cfg.get_notebookPath())
    setupNotes.append("Notebook Name" + get_html_spaces(24) + ":&nbsp;&nbsp;" + cfg.get_notebookName())
    setupNotes.append("dfcleanser path" + get_html_spaces(12) + ":&nbsp;&nbsp;" + cfg.get_dfcleanser_location())
    
    setupNotes.append("Please read the README file for dfcleanser install, load and setup")

    setup_notes_html      =   display_notes(setupNotes,False)

    return(setup_notes_html)
 
"""
#--------------------------------------------------------------------------
#   get formatted representation of python version
#
#--------------------------------------------------------------------------
"""    
def get_python_version() :
    
    import sys
    sysver = sys.version
    
    try :
        cindex = sysver.index("(")
        vermaj = sysver[0:(cindex-1)]
    except :
        vermaj =  sysver
        
    vermaj.strip()
    
    return(vermaj)






