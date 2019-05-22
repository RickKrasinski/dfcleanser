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

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR)

from dfcleanser.common.common_utils import (display_notes, RunningClock, alert_user, displayHTML, opStatus, 
                                            display_exception, display_generic_grid, get_select_defaults)


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
dfmgr_input_idList                =   ["dftitle",
                                       "dfnumrows",
                                       "dfnumcols",
                                       "dfnotes",
                                       None,None,None,None,None,None]

dfmgr_input_labelList             =   ["df_title",
                                       "df_num_rows",
                                       "df_num_cols",
                                       "df_notes",
                                       "Add</br>df</br>to dfc",
                                       "Drop</br>df</br>from dfc",
                                       "Update</br>df</br>in dfc",
                                       "Set As</br>Current</br>dfc df",
                                       "Return",
                                       "Help"]

dfmgr_input_typeList              =   ["select","text","text",maketextarea(5),
                                       "button","button","button","button","button","button"]

dfmgr_input_placeholderList       =   ["dataframe title",
                                       "number of rows",
                                       "number of columns",
                                       "dataframe notes",
                                       None,None,None,None,None,None]

dfmgr_input_jsList                =   [None,None,None,None,
                                       "dfmgr_callback("+str(sysm.DISPLAY_ADD_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.DROP_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.UPDATE_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.SET_DATAFRAME)+")",
                                       "dfmgr_callback("+str(sysm.RETURN_DATAFRAME)+")",
                                       "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + ")"]

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
                                       "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + ")"]

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

system_environment_keyTitleList         =   ["Select</br>Utilities",
                                             "dataframe</br>Manager",
                                             "dfcleanser</br>Files",
                                             "System",
                                             "About",
                                             "EULA","Clear","Reset","Help"]

system_environment_jsList               =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DATAFRAMES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DFC_FILES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_SYSTEM)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_ABOUT)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_EULA)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_MAIN)+")",
                                             "process_pop_up_cmd(6)",
                                             "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + ")"]

system_environment_centered             =   True

system_environmentA_doc_title           =   "System Options"
system_environmentA_doc_id              =   "systemoptionsA"
system_environmentA_title               =   None

system_environmentA_keyTitleList        =   ["Select</br>Utilities",
                                             "dataframe</br>Manager",
                                             "dfcleanser</br>Files",
                                             "System"]

system_environmentA_jsList              =   ["process_system_tb_callback("+str(sysm.DISPLAY_CHAPTERS)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DATAFRAMES)+")",
                                             "process_system_tb_callback("+str(sysm.DISPLAY_DFC_FILES)+")",
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
                                             "displayhelp(" + str(dfchelp.SYS_ENVIRONMENT_MAIN_TASKBAR_ID) + ")"]

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

dfc_utils_modules_checkbox_idList     =   ["dfcutildatastruct","dfcutilgenfunc","dfcutilgeocode","dfcutildfsubset"]
dfc_utils_modules_checkbox_labelList  =   ["Data Structures","Generic Function","Geocoding","Dataframe Subset"]

dfc_utils_modules_checkbox_jsList     =   [None,None,None,None,None]

dfc_script_modules_checkbox_title      =   "dfcleanser Scripting"
dfc_script_modules_checkbox_id         =   "dfc_script_cb"

dfc_script_modules_checkbox_idList     =   ["dfcscripting"]
dfc_script_modules_checkbox_labelList  =   ["Scripting"]

dfc_script_modules_checkbox_jsList     =   [None]

system_chapters_tb_doc_title           =   "Chapters"
system_chapters_tb_doc_id              =   "chaptersoptions"
system_chapters_tb_title               =   None

system_chapters_tb_keyTitleList        =   ["Load Utilities</br>Selected","Return"]

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
                                         "Copy</br>Notebook</br>dfcleanser</br>files",
                                         "Rename</br>Notebook</br>dfcleanser</br>files",
                                         "Delete</br>Notebook</br>dfcleanser</br>files",
                                         "Return","Help"]

dfc_files_input_typeList            =   ["select","text",
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
    
    #from dfcleanser.common.html_widgets import new_line
    #df_addcode  =   "from dfcleanser.common.cfg import dfc_dataframe, add_dfc_dataframe" + new_line
    #df_addcode  =   (df_addcode + "new_dfc_df = dfc_dataframe(*df_title, USER DF, *df_notes)" + new_line)
    #df_addcode  =   (df_addcode + "add_dfc_dataframe(new_dfc_df)")
    
    #fparms  =   ["",df_addcode,""]
    #cfg.set_config_value(dfmgr_add_input_id+"Parms",fparms)
    #cfg.drop_config_value(dfmgr_add_input_id+"ParmsProtect")
            
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
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-top"]
    gridhtmls       =   [dfmgr_heading_html,dfmgr_input_html]
    
    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfcleanser-dfmgr-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfcleanser-dfmgr-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer            
    display_pop_up_buffer()    
    
    
def get_dcf_files_parms(parms) :
    from dfcleanser.common.common_utils import get_parms_for_input
    return(get_parms_for_input(parms,dfc_files_input_idList))


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
        if(1):#cfg.get_config_value(cfg.CORE_CBS_KEY) == None) :
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
                                                    get_current_checkboxes(sysm.UTILITIES),
                                                    [0,0,0,0,0])
    
    if(not (cfg.get_dfc_mode() == cfg.INLINE_MODE)) :
        dfc_utils_modules_checkbox.set_rows_count([2,2])
    
    dfc_utils_modules_heading_html       =   "<div>dfcleanser Utilities</div>"
    dfc_utils_modules_checkbox_html      =   dfc_utils_modules_checkbox.get_html()
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [dfc_utils_modules_heading_html,dfc_utils_modules_checkbox_html]

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfcleanser-chapters-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfcleanser-chapters-pop-up-wrapper",gridclasses,gridhtmls)
    
    dfc_script_modules_checkbox     =  CheckboxGroupForm(dfc_script_modules_checkbox_id,
                                                         dfc_script_modules_checkbox_idList,
                                                         dfc_script_modules_checkbox_labelList,
                                                         dfc_script_modules_checkbox_jsList,
                                                         get_current_checkboxes(sysm.SCRIPTING),
                                                         [0])
    
    print("\n")
    dfc_script_modules_heading_html       =   "<div>dfcleanser Scripting</div>"
    
    dfc_script_modules_checkbox_html      =   dfc_script_modules_checkbox.get_html()

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
    gridhtmls       =   [dfc_script_modules_heading_html,dfc_script_modules_checkbox_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfcleanser-chapters-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfcleanser-chapters-pop-up-wrapper",gridclasses,gridhtmls)

    dfc_script_modules_tb           =   ButtonGroupForm(system_chapters_tb_doc_id,
                                                        system_chapters_tb_keyTitleList,
                                                        system_chapters_tb_jsList,
                                                        system_chapters_tb_centered)
    
    dfc_script_modules_tb.set_gridwidth(480)
    
    dfc_script_modules_tb_html      =   dfc_script_modules_tb.get_html()

    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [dfc_script_modules_tb_html]
    
    display_generic_grid("dfcleanser-chapters-tb-wrapper",gridclasses,gridhtmls)

    print("\n")


def display_df_dataframes(title=None) :  
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
 
    fparms  =   []

    if(title == None) :
        current_df  =   cfg.get_current_dfc_dataframe_title()
    else :
        current_df  =   title

    cfg.set_config_value(cfg.CURRENT_DF_DISPLAYED_KEY,current_df)
    
    if(not(current_df == None)) :
        cdf     =   cfg.get_dfc_dataframe(current_df)
        cdfn    =   cfg.get_dfc_dataframe_notes(current_df)
        
        fparms.append(current_df)
        
        if(not(cdf is None)) :
            fparms.append(str(len(cdf)))
            fparms.append(str(len(cdf.columns)))
        else :
            fparms.append("")
            fparms.append("")
            
        if(not(cdfn == None)) :
            fparms.append(cdfn)
        else :
            fparms.append("")
    else :
        fparms  =   ["","","",""]
        
    parmsProtect = [False,True,True,False]
        
    cfg.set_config_value(dfmgr_input_id+"Parms",fparms)
    cfg.set_config_value(dfmgr_input_id+"ParmsProtect",parmsProtect)
            
    from dfcleanser.common.html_widgets import InputForm
    dfmanager_input_form = InputForm(dfmgr_input_id,
                                     dfmgr_input_idList,
                                     dfmgr_input_labelList,
                                     dfmgr_input_typeList,
                                     dfmgr_input_placeholderList,
                                     dfmgr_input_jsList,
                                     dfmgr_input_reqList)
                    
    selectDicts =   []
    df_titles   =   cfg.get_dfc_dataframe_titles_list()
     
    if(df_titles is None) :
        dfs     =   {"default":" ","list":[" "]}
    else :   
        dfs     =   {"default":str(df_titles[0]),"list":df_titles,"callback":"select_new_df"}
    selectDicts.append(dfs)
        
    get_select_defaults(dfmanager_input_form,
                        dfmgr_input_id,
                        dfmgr_input_idList,
                        dfmgr_input_typeList,
                        selectDicts)

    dfmanager_input_form.set_shortForm(True)
    dfmanager_input_form.set_gridwidth(480)
    dfmanager_input_form.set_custombwidth(70)
    dfmanager_input_form.set_fullparms(True)
        
    dfmgr_input_html = dfmanager_input_form.get_html()
    
    dfmgr_heading_html       =   "<div>Current dfCleanser dataframes </div>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-top"]
    gridhtmls       =   [dfmgr_heading_html,dfmgr_input_html]
    
    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfcleanser-dfmgr-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfcleanser-dfmgr-pop-up-wrapper",gridclasses,gridhtmls)

    from dfcleanser.common.display_utils import display_pop_up_buffer            
    display_pop_up_buffer()    


def display_dfc_files_form() :
    """
    * -------------------------------------------------------------------------- 
    * function : display dfcleanser files form
    * 
    * parms :
    *  N/A
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()

    import os
    
    from dfcleanser.common.common_utils import get_common_dfcleanser_loc
    dfc_path        =   get_common_dfcleanser_loc()
    dfc_nbs_path    =   os.path.join(dfc_path, 'files', 'notebooks')
    os.chdir(dfc_nbs_path)
    
    dfc_nb_files    =   os.listdir(dfc_nbs_path)
    dfc_nbs         =   []

    for i in range(len(dfc_nb_files)) :
        if(os.path.isfile(dfc_nb_files[i]))  :
            found =  dfc_nb_files[i].find("_config.json") 
            if(found > -1) :
                dfc_nbs.append(dfc_nb_files[i][:found])
    
    # build the input form
    dfc_files_input_form =  InputForm(dfc_files_input_id,
                                      dfc_files_input_idList,
                                      dfc_files_input_labelList,
                                      dfc_files_input_typeList,
                                      dfc_files_input_placeholderList,
                                      dfc_files_input_jsList,
                                      dfc_files_input_reqList)
    
    nbname = cfg.get_current_notebook_name()
    cfg.set_config_value(dfc_files_input_id + "Parms",[nbname,""])
    
    selectDicts =   []
    nbs     =   {"default":str(nbname),"list":dfc_nbs}
    selectDicts.append(nbs)
        
    get_select_defaults(dfc_files_input_form,
                        dfc_files_input_id,
                        dfc_files_input_idList,
                        dfc_files_input_typeList,
                        selectDicts)
        
    dfc_files_input_form.set_shortForm(True)
    dfc_files_input_form.set_gridwidth(480)
    dfc_files_input_form.set_fullparms(True)
    dfc_files_input_form.set_custombwidth(86)
    
    try :    
    
        dfc_files_input_html = ""
        
        #print("dfc_files_input_html\n",dfc_files_input_html)
        
        dfc_files_heading_html  =   "<div>Notebook : '" + str(nbname) + "' Files  </div><br>"
        dfc_files_input_html    =   dfc_files_input_form.get_html()
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
        gridhtmls       =   [dfc_files_heading_html,dfc_files_input_html]
    
        print("\n")
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfcleanser-files-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfcleanser-files-pop-up-wrapper",gridclasses,gridhtmls)
        
    except Exception as e:
        opstat.store_exception("Unable to display dfc files form ",e)
    
    if( not (opstat.get_status())) :
        display_exception(opstat)


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
    
    readme_file_name  =   cfg.get_notebook_path()+"\dfcleanser\html\README.md"
    
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
    
    from dfcleanser.common.common_utils import displayParms
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
    
    testedmoduleVersions        =   ["3.7.0","7.2.0","7.4.2","5.1.0","5.7.2",
                                     "0.23.4","0.20.1","3.0.2","1.15.4","1.1.0",
                                     "2.0.9","1.2.14","0.9.2","8.0.12",
                                     "4.0.22","2.1.4","3.8.6","2.7.5","6.4.1",
                                     "1.17.0","2.5.1","1.5.1"]

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
        libsrow.append(str(installedmoduleVersions[i]))
        
        libsRows.append(libsrow)
    
    colorList = []    
    for i in range(len(testedModules)) :
        colorRow = []
        if(installedmoduleVersions[i] == "-1") :
            installedmoduleVersions[i] == "not installed"
            colorRow = [sysm.Yellow,sysm.Yellow,sysm.Yellow]
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

    libs_table.set_tabletype(ROW_MAJOR)
    libs_table.set_rowspertable(len(testedModules))
    libs_table.set_color(True)
    libs_table.set_colorList(colorList)
    libs_table.set_small(True)
    libs_table.set_smallwidth(99)
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
    
    #displayHeading("dfcleanser Notes",4)
    #print("\n")
    
    setupNotes = []
    nbname = cfg.get_notebook_name()
    if(not (nbname == None)) :
        setupNotes.append("Notebook Name" + get_html_spaces(22) + ":&nbsp;&nbsp;" + str(nbname))
    nbpath = cfg.get_notebook_path()    
    if(not (nbpath == None)) :
        setupNotes.append("Notebook Path" + get_html_spaces(23) + ":&nbsp;&nbsp;" + str(nbpath))
    import jupyter_core
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







