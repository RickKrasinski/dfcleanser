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

from dfcleanser.common.html_widgets import (get_button_tb_form, maketextarea, display_composite_form, ButtonGroupForm, 
                                            displayHeading, get_input_form, get_checkbox_form, CheckboxGroupForm, InputForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR)

from dfcleanser.common.common_utils import (display_notes, RunningClock)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    System html form elements
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

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

system_environment_keyTitleList         =   ["Select</br>Chapters",
                                             "Reset</br>Chapters",
                                             "Clear</br>Data",
                                             "System","dfcleanser</br>files","About",
                                             "EULA","Clear","Help"]

system_environment_jsList               =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.RESET_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.CLEAR_DATA)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_SYSTEM)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DFC_FILES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_ABOUT)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_EULA)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                             "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + ")"]


system_environment_abbr_doc_title       =   "System Options"
system_environment_abbr_doc_id          =   "systemoptions"
system_environment_abbr_title           =   None

system_environment_abbr_keyTitleList    =   ["dfcleanser</br>Chapters","EULA","README","System","Exit Setup","Clear"]

system_environment_abbr_jsList         =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_EULA)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_README)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_SYSTEM)+")",
                                            "process_system_tb_callback("+str(sysm.EXIT_SETUP)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_ABBR_MAIN)+")"]

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

dfc_utils_modules_checkbox_idList     =   ["dfcutildatastruct","dfcutilgenfunc","dfcutilgeocode","dfcutildfsubset","dfcutildfconcat"]
dfc_utils_modules_checkbox_labelList  =   ["Data Structures","Generic Function","Geocoding","Dataframe Subset","Dataframe Concat"]

dfc_utils_modules_checkbox_jsList     =   [None,None,None,None,None]

dfc_script_modules_checkbox_title      =   "dfcleanser Utilities"
dfc_script_modules_checkbox_id         =   "dfc_script_cb"

dfc_script_modules_checkbox_idList     =   ["dfcscripting"]
dfc_script_modules_checkbox_labelList  =   ["Scripting"]

dfc_script_modules_checkbox_jsList     =   [None]

system_chapters_tb_doc_title           =   "Chapters"
system_chapters_tb_doc_id              =   "chaptersoptions"
system_chapters_tb_title               =   None

system_chapters_tb_keyTitleList        =   ["Select Chapters</br>To Load","Return"]

system_chapters_tb_jsList              =   ["process_system_tb_callback("+str(sysm.PROCESS_CHAPTERS)+")",
                                            "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")"]

system_chapters_tb_centered            =   True

"""
#--------------------------------------------------------------------------
#    notebook save inputs
#--------------------------------------------------------------------------
"""
dfc_files_input_title               =   "dfcleanser files Parameters"
dfc_files_input_id                  =   "dfcfiles"
dfc_files_input_idList              =   ["nbname","newnbname",
                                         None,None,None,None,None]

dfc_files_input_labelList           =   ["notebook_name",
                                         "new_notebook_name",
                                         "Copy</br>Notebook</br>dfcleanser files",
                                         "Rename</br>Notebook</br>dfcleanser files",
                                         "Delete</br>Notebook</br>dfcleanser files",
                                         "Return","Help"]

dfc_files_input_typeList            =   ["text","text",
                                         "button","button","button","button","button"]

dfc_files_input_placeholderList     =   ["notebook name","new notebook name",
                                         None,None,None,None,None]

dfc_files_input_jsList              =    [None,None,
                                          "process_notebook_files_callback(0)",
                                          "process_notebook_files_callback(1)",
                                          "process_notebook_files_callback(2)",
                                          "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                          "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_COPY_ID) + ")"]

dfc_files_input_reqList             =   [0,1]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    System display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_system_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(system_environment_doc_id,
                                                               system_environment_keyTitleList,
                                                               system_environment_jsList,
                                                               False))])
    
    cfg.set_config_value(cfg.LAST_TASK_BAR_ID_KEY,sysm.DISPLAY_MAIN)

def display_system_main_abbr_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(system_environment_abbr_doc_id,
                                                               system_environment_abbr_keyTitleList,
                                                               system_environment_abbr_jsList,
                                                               False))])
    
    cfg.set_config_value(cfg.LAST_TASK_BAR_ID_KEY,sysm.DISPLAY_ABBR_MAIN)

def get_dcf_files_parms(parms) :
    from dfcleanser.common.common_utils import get_parms_for_input
    return(get_parms_for_input(parms,dfc_files_input_idList))

def get_current_checkboxes(cbtype) :

    if(cbtype == sysm.CORE) :
        if(cfg.get_config_value(cfg.CORE_CBS_KEY) == None) :
            return([1,1,1,1,1])
        else :
            return(cfg.get_config_value(cfg.CORE_CBS_KEY))
            
    elif(cbtype == sysm.UTILITIES) :
        if(cfg.get_config_value(cfg.UTILITIES_CBS_KEY) == None) :
            return([0,0,0,0,0])
        else :
            return(cfg.get_config_value(cfg.UTILITIES_CBS_KEY))
    
    else :
        if(cfg.get_config_value(cfg.SCRIPTING_CBS_KEY) == None) :
            return([0])
        else :
            return(cfg.get_config_value(cfg.SCRIPTING_CBS_KEY))
        
    return(None)

def display_system_chapters_taskbar() :

    dfc_core_modules_checkbox   =  CheckboxGroupForm(dfc_core_modules_checkbox_id,
                                                     dfc_core_modules_checkbox_idList,
                                                     dfc_core_modules_checkbox_labelList,
                                                     dfc_core_modules_checkbox_jsList,
                                                     get_current_checkboxes(sysm.CORE),
                                                     [1,1,1,1,1])
    
    dfc_core_modules_checkboxForm = get_checkbox_form("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dfcleanser Core Modules",
                                                      dfc_core_modules_checkbox)

    dfc_utils_modules_checkbox =  CheckboxGroupForm(dfc_utils_modules_checkbox_id,
                                                    dfc_utils_modules_checkbox_idList,
                                                    dfc_utils_modules_checkbox_labelList,
                                                    dfc_utils_modules_checkbox_jsList,
                                                    get_current_checkboxes(sysm.UTILITIES),
                                                    [0,0,0,0,0])
    
    dfc_utils_modules_checkboxForm = get_checkbox_form("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dfcleanser Utilities",
                                                       dfc_utils_modules_checkbox)

    dfc_script_modules_checkbox     =  CheckboxGroupForm(dfc_script_modules_checkbox_id,
                                                         dfc_script_modules_checkbox_idList,
                                                         dfc_script_modules_checkbox_labelList,
                                                         dfc_script_modules_checkbox_jsList,
                                                         get_current_checkboxes(sysm.SCRIPTING),
                                                         [0])
    
    dfc_script_modules_checkboxForm = get_checkbox_form("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dfcleanser Utilities",
                                                        dfc_script_modules_checkbox)

    display_composite_form([dfc_core_modules_checkboxForm,
                            dfc_utils_modules_checkboxForm,
                            dfc_script_modules_checkboxForm])
    
    display_composite_form([get_button_tb_form(ButtonGroupForm(system_chapters_tb_doc_id,
                                                               system_chapters_tb_keyTitleList,
                                                               system_chapters_tb_jsList,
                                                               system_chapters_tb_centered))])
    print("\n")
    
def display_dfc_files_form() :
    
    dfc_files_input_form =  InputForm(dfc_files_input_id,
                                      dfc_files_input_idList,
                                      dfc_files_input_labelList,
                                      dfc_files_input_typeList,
                                      dfc_files_input_placeholderList,
                                      dfc_files_input_jsList,
                                      dfc_files_input_reqList)
    
    nbname = cfg.get_notebook_name()
    cfg.set_config_value(dfc_files_input_id + "Parms",[nbname,""])

    display_composite_form([get_input_form(dfc_files_input_form,
                            dfc_files_input_title)])
    

""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   display the EULA
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
def display_EULA():
    
    from dfcleanser.system.system_control import isEULA_read
    
    if(isEULA_read()) : 
        eula_file_name  =   cfg.get_dfcleanser_location()+"\html\EULARead.html" 
    else :
        eula_file_name  =   cfg.get_dfcleanser_location()+"\html\EULA.html"

    from dfcleanser.common.common_utils import   displayHTML,display_windows_MessageBox      
    try :    
        eula_file = open(eula_file_name, 'r', encoding="utf-8")
        eula_html = (eula_file.read())
        eula_file.close()

        displayHTML(eula_html) 
            
    except :
        display_windows_MessageBox("Unable to open EULA file" + eula_file_name,"EULA Read Error")

def display_README():
    
    readme_file_name  =   cfg.get_notebook_path()+"\dfcleanser\html\README.md"
    
    from dfcleanser.common.common_utils import display_windows_MessageBox      
        
    try :    
        readme_file = open(readme_file_name, 'r', encoding="utf-8")# as eula_file :
        readme_md   = (readme_file.read()) #json.load(eula_file)
        readme_file.close()
        
        from IPython.display import Markdown, display
        display(Markdown(readme_md))
            
    except :
        display_windows_MessageBox("Unable to open README file" + readme_file,"README Read Error")

""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   show info functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""
def show_sys_info():
    
    import sys
    sysver = sys.version
    
    cindex = sysver.index("|")
    vermaj = sysver[0:(cindex-1)]
    vermaj.strip()
    print("\n")
    displayHeading("Installed Python Info",4)
    
    print("\n    Version  : ",vermaj)
    print("    API      : ",sys.api_version)    
    print("    Info     : ",sys.version_info,"\n",flush=True)

    show_setup_notes()
    
    show_libs_info()    


def show_about_info():
    
    print("\nAuthor : Rick Krasinski")
    print("Dataframe Cleanser Version : 1.0.0")

def show_libs_info():
    
    displayHeading("dfcleanser Dependencies",4)
    print("\n")
    print("           * The following table shows the python modules used by dfcleanser.")
    print("           * Green indicates installed version matches tested with version.")
    print("           * Yellow indicates installed version newer than tested with version and potential problem.")
    print("           * Red indicates installed version older than tested with version and potential problem requiring update.")
    
    
    clock = RunningClock()
    clock.start()
    
    
    libsHeader    =   ["Lib Name","Tested</br>With Version","Installed Version"]
    libsRows      =   []
    libsWidths    =   [40,30,30]
    libsAligns    =   ["left","center","center"]


    testedModules               =   ["Python","pandas","IPython","sklearn","matplotlib","numpy",
                                     "json","SQLAlchemy","pymysql","mysql-connector-python",
                                     "pyodbc","pymssql","SQLite3","psycopg2","cx-oracle","geopy"]
    testedmoduleVersions        =   ["3.5.5","0.22.0", "6.2.1","0.19.1", "2.1.2","1.14.2",
                                     "2.0.9","1.2.5","0.8.0","2.0.4",
                                     "4.0.22","2.1.3","3.8.6","2.7.3.1","6.1","1.12.0"]
    installedmoduleVersions     =   []

    installedmoduleVersions.append(str(get_python_version()))
    import pandas
    installedmoduleVersions.append(str(pandas.__version__))
    import IPython
    installedmoduleVersions.append(str(IPython.__version__))
    import sklearn
    installedmoduleVersions.append(str(sklearn.__version__))
    import matplotlib
    installedmoduleVersions.append(str(matplotlib.__version__))
    import numpy
    installedmoduleVersions.append(str(numpy.__version__))
    import json
    installedmoduleVersions.append(str(json.__version__))
    import sqlalchemy
    installedmoduleVersions.append(str(sqlalchemy.__version__))
    import pymysql
    installedmoduleVersions.append(str(pymysql.__version__))
    import mysql.connector    
    installedmoduleVersions.append(str(mysql.connector.__version__))
    #import pyodbc    
    installedmoduleVersions.append(str("unknown"))
    import pymssql    
    installedmoduleVersions.append(str(pymssql.__version__))
    #import sqlite3    
    installedmoduleVersions.append(str("unknown"))
    import psycopg2
    
    pgversion =  str(psycopg2.__version__)
    found = pgversion.find("(")
    if(found > 0)  :
        installedmoduleVersions.append(pgversion[0:found-1])
    else :
        installedmoduleVersions.append(pgversion)
    
    import cx_Oracle    
    installedmoduleVersions.append(str(cx_Oracle.__version__))
    import geopy    
    installedmoduleVersions.append(str(geopy.__version__))
    
    for i in range(len(testedModules)) :
        libsrow = []
        libsrow.append(str(testedModules[i]))
        libsrow.append(str(testedmoduleVersions[i]))
        libsrow.append(str(installedmoduleVersions[i]))
        
        libsRows.append(libsrow)
    
    colorList = []    
    for i in range(len(testedModules)) :
        colorRow = []
        if(installedmoduleVersions[i] == "unknown") :
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

    libs_table.set_tabletype(ROW_MAJOR)
    libs_table.set_rowspertable(len(testedModules))
    libs_table.set_color(True)
    libs_table.set_colorList(colorList)
    libs_table.set_small(True)
    libs_table.set_smallwidth(80)
    libs_table.set_smallmargin(80)
    libs_table.set_smallfsize(12)
    libs_table.set_checkLength(False)
    libs_table.set_border(False)

    #libs_table.set_border(False)
    
    libs_table.display_table()

    clock.stop()  
    
def show_setup_notes():
    
    displayHeading("dfcleanser Notes",4)
    print("\n")
    
    setupNotes = []
    from dfcleanser.common.html_widgets import get_html_spaces
    nbname = cfg.get_notebook_name()
    if(not (nbname == None)) :
        setupNotes.append("Notebook Name" + get_html_spaces(22) + ":&nbsp;&nbsp;" + str(nbname))
    nbpath = cfg.get_notebook_path()    
    if(not (nbpath == None)) :
        setupNotes.append("Notebook Path" + get_html_spaces(23) + ":&nbsp;&nbsp;" + str(nbpath))
    import jupyter_core
    setupNotes.append("Custom JS File Location" + get_html_spaces(9) + ":&nbsp;&nbsp;" + str(jupyter_core.paths.jupyter_config_dir() + '\custom\custom.js'))
    setupNotes.append("Custom CSS File Location" + get_html_spaces(7) + ":&nbsp;&nbsp;" + str(jupyter_core.paths.jupyter_config_dir() + '\custom\custom.css'))
    setupNotes.append("Please read the README file for dfcleanser install, load and setup")

    display_notes(setupNotes)
 
"""
#--------------------------------------------------------------------------
#   get formatted representation of python version
#
#--------------------------------------------------------------------------
"""    
def get_python_version() :
    
    import sys
    sysver = sys.version
    
    cindex = sysver.index("|")
    vermaj = sysver[0:(cindex-1)]
    vermaj.strip()
    
    return(vermaj)







