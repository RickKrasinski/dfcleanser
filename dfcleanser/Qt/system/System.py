"""
# system
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic


import dfcleanser.common.cfg as cfg 

DEBUG_SYSTEM                    =   False
DEBUG_SYSTEM_DFS                =   False
DEBUG_SYSTEM_INFO               =   False
DEBUG_SYSTEM_FILES              =   False

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
from dfcleanser.sw_utilities.dfc_qt_model import fix_ipython
fix_ipython()


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Data Import subfunctions                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


SYSTEM_DFC_DATAFRAMES                   =   "Syatem dfc datafranes"
SYSTEM_INFO                             =   "System info"
SYSTEM_ABOUT                            =   "System about"
SYSTEM_EULA                             =   "System eula"
SYSTEM_README                           =   "System readme"


DISPLAY_DFCS                            =   "System display dfs"
DISPLAY_DFC_HISTORIES                   =   "System display dfs histories"
DISPLAY_ADD_USER_DF                     =   "System display dfs add user df"

DISPLAY_INFO                            =   "System display info"
DISPLAY_ABOUT                           =   "System display about"
DISPLAY_SYSFILES                        =   "System display sys files"
DISPLAY_FILE                            =   "System display fils"

DISPLAY_EULA                            =   "System display eula"



EXPORT_EXCEL_FILE_TYPE_HISTORIES        =   "DataExport excel filetypes Exported"
EXPORT_JSON_FILE_TYPE_HISTORIES         =   "DataExport json filetypes Exported"
EXPORT_HTML_FILE_TYPE_HISTORIES         =   "DataExport html filetypes Exported"
EXPORT_SQLTABLE_FILE_TYPE_HISTORIES     =   "DataExport sqltable filetypes Exported"
EXPORT_CUSTOM_FILE_TYPE_HISTORIES       =   "DataExport custom filetypes Exported"


DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       System main GUI                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class SystemGui(QtWidgets.QMainWindow):

    #def __init__(self):
    def __init__(self, **kwargs):  

        # Enables PyQt event loop in IPython
        fix_ipython()  

        # create the app for uniques
        from PyQt5.QtCore import QCoreApplication

        self.app = QCoreApplication.instance()
        if(self.app is None) :
            self.app = QtWidgets.QApplication(sys.argv) 

        # release resources on close
        self.app.setQuitOnLastWindowClosed(True)  

        super().__init__()

        self.mainLayout         =   None
        self.selectdfsLayout    =   None

        self.dftitle            =   None
        self.df                 =   None

        self.form               =   None
        self.stackedLayout      =   None


        self.SystemWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.dfcSystemMainLayout.addLayout(self.stackedLayout)
        self.form.dfcSystemMainLayout.addStretch()


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\system\SystemUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - System")
        
        # Center window on screen
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                         int((screen.height() - size.height()) / 2), )
        
        # don't Accept drops
        self.setAcceptDrops(False)

        # don't allopw code viewing
        self.code_history_viewer = None 

        # -----------------------------------------------------#
        #       common app attribute settings         #
        # -----------------------------------------------------#
        # Set the app icon
        dfcdir      =   cfg.DataframeCleanserCfgData.get_dfc_cfg_dir_name()  
        icon_name   =   dfcdir +"\dfcicon.png"
        self.app.setWindowIcon(QtGui.QIcon(icon_name))

        # Hide the question mark on dialogs
        self.app.setAttribute(Qt.AA_DisableWindowContextHelpButton) 
        
        # set overall app style
        self.app.setStyle('Fusion')      

        # -----------------------------------------------------#
        #            common window widgets             #
        # -----------------------------------------------------#

        # Status bar
        self.setStatusBar(QtWidgets.QStatusBar())
        self.statusBar().setStyleSheet("background-color: #ccffff; font-size: 12px; font-weight: normal; font-family: Arial; margin-left: 0px;")
        
        # init the gui form
        self.init_data_import_form()

           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_system_buttons(self):

        if(DEBUG_SYSTEM) :
            print("[SystemGui][init_data_inspect_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.dfcdfsbutton, self.form.Infobutton, self.form.Aboutbutton, self.form.SysFilesbutton, 
                         self.form.EULAbutton, self.form.ReadMebutton, self.form.Helpbutton] 
        
        callbacks   =   [self.dfc_dataframes, self.system_info, self.dfc_about, self.dfc_SysFiles, self.dfc_Eula, self.dfc_readme, self.dfc_help]
    
        # init buttons for usage
        System_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,System_Button_Style)

        # adding action to a button
        for i in range(len(buttons)) :
            buttons[i].clicked.connect(callbacks[i])


    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_system_splash_screen(self):

        if(DEBUG_SYSTEM) :
            print("[SystemGui][init_data_inspect_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import System_ID
        build_chapter_splash_screen(System_ID, self.form.Systemsplash)

        if(DEBUG_SYSTEM) :
            print("[end init_data_import_splash_screen]  ")


    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_import_form(self):
        
        if(DEBUG_SYSTEM) :
            print("[SystemGui][init_data_import_form]  ")

        self.init_system_buttons()
        self.init_system_splash_screen()

        self.resize(1070,300)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               Main Gui Data Import Methods                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                      dfc dataframes                           -#
    # -----------------------------------------------------------------#
    def dfc_dataframes(self) :

        self.form.dfcdfsbutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_dataframes]")

        self.display_dfcleanser_dfs()

    # -----------------------------------------------------------------#
    # -                      dfc Syatem INfo                          -#
    # -----------------------------------------------------------------#
    def system_info(self) :

        self.form.Infobutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][system_info]")

        self.display_dfcleanser_info()

    # -----------------------------------------------------------------#
    # -                        dfc About                              -#
    # -----------------------------------------------------------------#
    def dfc_about(self) :

        self.form.Aboutbutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_about]")

        self.display_dfcleanser_about()

    # -----------------------------------------------------------------#
    # -                        Sys Files                              -#
    # -----------------------------------------------------------------#
    def dfc_SysFiles(self) :

        self.form.SysFilesbutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_sysfiles]")

        self.display_dfcleanser_sys_files()


    # -----------------------------------------------------------------#
    # -                          dfc EULLA                            -#
    # -----------------------------------------------------------------#
    def dfc_Eula(self) :

        self.form.EULAbutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_Eula]")

        self.display_dfcleanser_EULA()

    # -----------------------------------------------------------------#
    # -                          dfc ReadMe                           -#
    # -----------------------------------------------------------------#
    def dfc_readme(self) :

        self.form.ReadMebutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_readme]")

        self.display_dfcleanser_readme()

    # -----------------------------------------------------------------#
    # -                          dfc ReadMe                           -#
    # -----------------------------------------------------------------#
    def dfc_help(self) :

        self.form.Helpbutton.toggle()

        if(DEBUG_SYSTEM) :
            print("[SystemGui][dfc_help]")

        from dfcleanser.common.common_utils import display_url
        display_url("https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-system-environment.html")

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                    display dfcleanser dfs                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_dfcleanser_dfs(self):

        if(DEBUG_SYSTEM_DFS) :
            print("\n[SystemGui][display_dfcleanser_dfs]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        system_dfs_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_DFCS)
        
        if(system_dfs_index is None) :

            try :

                from dfcleanser.Qt.system.SystemWidgets import System_dfc_dfs_Widget
                self.dfc_dfs   =   System_dfc_dfs_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_dfcleanser_dfs] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.SystemWidgets_stack_dict)
                self.SystemWidgets_stack_dict.update({DISPLAY_DFCS : current_index})
                self.stackedLayout.addWidget(self.dfc_dfs)

        else :

            self.dfc_dfs.reload_data()
            current_index   =   system_dfs_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_DFS) :
            print("[SystemGui][display_dfcleanser_dfs] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,600)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display dfcleanser dfs end                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display dfcleanser dfs History                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_dfcleanser_dfs_histories(self):

        if(DEBUG_SYSTEM_DFS) :
            print("\n[SystemGui][display_dfcleanser_dfs_histories]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        system_dfs_histories_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_DFC_HISTORIES)
        
        if(system_dfs_histories_index is None) :

            try :

                from dfcleanser.Qt.system.SystemWidgets import System_dfc_dfs_histories_Widget
                callbacks   =   [self]
                self.dfc_dfs_histories   =   System_dfc_dfs_histories_Widget(callbacks)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_dfcleanser_dfs_histories] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                if(DEBUG_SYSTEM_DFS) :
                    print("\n[SystemGui][display_dfcleanser_dfs_histories]  add widget",type(self.dfc_dfs_histories))


                current_index   =  len(self.SystemWidgets_stack_dict)
                self.SystemWidgets_stack_dict.update({DISPLAY_DFC_HISTORIES : current_index})
                self.stackedLayout.addWidget(self.dfc_dfs_histories)

        else :

            #self.dfc_dfs.reload_data()
            current_index   =   system_dfs_histories_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_DFS) :
            print("[SystemGui][display_dfcleanser_dfs_histories] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             display dfcleanser dfs History end                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 display add user df to dfc                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_add_user_df_to_dfc(self):

        if(DEBUG_SYSTEM_DFS) :
            print("\n[SystemGui][display_add_user_df_to_dfc]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        system_add_user_df_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_ADD_USER_DF)
        
        if(system_add_user_df_index is None) :

            try :

                from dfcleanser.Qt.system.SystemWidgets import System_add_user_df_to_dfc_Widget
                callbacks   =   [self]
                self.dfc_dfs_add_user_df  =   System_add_user_df_to_dfc_Widget(callbacks)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_user_df_to_dfc] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.SystemWidgets_stack_dict)
                self.SystemWidgets_stack_dict.update({DISPLAY_ADD_USER_DF : current_index})
                self.stackedLayout.addWidget(self.dfc_dfs_add_user_df)

        else :

            current_index   =   system_add_user_df_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_DFS) :
            print("[SystemGui][SystemGui][display_add_user_df_to_dfc] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display add user df to dfc end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display dfcleanser info                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_dfcleanser_info(self):

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemGui][display_dfcleanser_info]  ")

        system_dfs_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_INFO)
        
        if(system_dfs_index is None) :
            current_index   =  len(self.SystemWidgets_stack_dict)
        else :
            current_index   =   system_dfs_index
        
        if(DEBUG_SYSTEM_INFO) :
            print("[display_dfcleanser_info] : current_index ",current_index)

        from dfcleanser.common.common_utils import RunningClock
        from IPython.display import clear_output
        clear_output()
        #clock = RunningClock()
        #clock.start()
 
        try :

            from dfcleanser.Qt.system.SystemWidgets import System_Info_Widget
            self.info   =   System_Info_Widget()

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_dfcleanser_info] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(DEBUG_SYSTEM_INFO) :
            print("[SystemGui][display_dfcleanser_info] : self.info ",self.info)


        if(system_dfs_index is None) :

            self.SystemWidgets_stack_dict.update({DISPLAY_INFO : current_index})
            self.stackedLayout.addWidget(self.info)

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemGui][display_dfcleanser_info] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,900)

        #if(not (clock is None)) :
        #    clock.stop()
        #    logger.info("Running dfcleanser System chapter")



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 display dfcleanser info end                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display dfcleanser about                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dfcleanser_about(self):

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemGui][display_dfcleanser_about]  ")

        about_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_ABOUT)
        
        if(about_index is None) :
            current_index   =  len(self.SystemWidgets_stack_dict)
        else :
            current_index   =   about_index
            
        from dfcleanser.Qt.system.SystemWidgets import System_About_Widget
        self.about   =   System_About_Widget()

        if(about_index is None) :

            self.SystemWidgets_stack_dict.update({DISPLAY_ABOUT : current_index})
            self.stackedLayout.addWidget(self.about)

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemGui][display_dfcleanser_about] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dfcleanser about end                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 display dfcleanser sys files                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_dfcleanser_sys_files(self):

        if(DEBUG_SYSTEM_FILES) :
            print("\n[SystemGui][display_dfcleanser_sys_files]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        system_sysfiles_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_SYSFILES)
        
        if(DEBUG_SYSTEM_FILES) :
            print("\n[SystemGui][display_dfcleanser_sys_files] system_sysfiles_index ",system_sysfiles_index)
        
        if(system_sysfiles_index is None) :

            try :

                from dfcleanser.Qt.system.SystemWidgets import cfg_files_Widget
                self.dfc_sysfiles   =   cfg_files_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_dfcleanser_sys_files] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.SystemWidgets_stack_dict)
                self.SystemWidgets_stack_dict.update({DISPLAY_SYSFILES : current_index})
                self.stackedLayout.addWidget(self.dfc_sysfiles)

        else :

            #self.dfc_dfs.reload_data()
            current_index   =   system_sysfiles_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_DFS) :
            print("[SystemGui][display_dfcleanser_sys_files] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,600)


    def display_dfcleanser_file(self,file_name):

        if(DEBUG_SYSTEM_FILES) :
            print("\n[SystemGui][display_dfcleanser_file]  file_name ",file_name)

        self.file_name  =   file_name

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        system_file_index  =   self.SystemWidgets_stack_dict.get(DISPLAY_FILE)
        
        if(DEBUG_SYSTEM_FILES) :
            print("\n[SystemGui][display_dfcleanser_file]  system_file_index ",system_file_index)
        
        if(system_file_index is None) :

            try :

                from dfcleanser.Qt.system.SystemWidgets import dfc_file_Widget
                self.dfc_file   =   dfc_file_Widget([self,self.file_name])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_dfcleanser_file] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.SystemWidgets_stack_dict)
                self.SystemWidgets_stack_dict.update({DISPLAY_FILE : current_index})
                self.stackedLayout.addWidget(self.dfc_file)

        else :

            self.dfc_file.reload_data(self.file_name)
            #from dfcleanser.Qt.system.SystemWidgets import dfc_file_Widget
            #self.dfc_file   =   dfc_file_Widget([self,self.file_name])
            current_index   =   system_file_index

            if(DEBUG_SYSTEM_FILES) :
                print("\n[SystemGui][display_dfcleanser_file]  ",current_index)


        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_SYSTEM_FILES) :
            print("[SystemGui][display_dfcleanser_file] end : stack \n  ",self.SystemWidgets_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display dfcleanser sys files end                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#





    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display dfcleanser EULA                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dfcleanser_EULA(self):

        if(DEBUG_SYSTEM) :
            print("\n[SystemGui][display_dfcleanser_eula]  ")

        DFCLEANSER_EULA    =   "https://rickkrasinski.github.io/dfcleanser/dfcleanser_EULA.html"    

        from dfcleanser.common.common_utils import display_url
        display_url(DFCLEANSER_EULA)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dfcleanser EULA end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display dfcleanser readme                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dfcleanser_readme(self):

        if(DEBUG_SYSTEM) :
            print("\n[display_dfcleanser_readme]  ")

        DFCLEANSER_README    =   "https://rickkrasinski.github.io/dfcleanser/README.md"    

        from dfcleanser.common.common_utils import display_url
        display_url(DFCLEANSER_README)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dfcleanser readme end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                      System main GUI end                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to System Chapter                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearSystem()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()
     
    from dfcleanser.common.cfg import dfc_qt_chapters, SYSTEM_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(SYSTEM_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(SYSTEM_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_import_form()

    clear_screen()

def closeSystemInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, SYSTEM_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(SYSTEM_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(SYSTEM_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import SYSTEM_TITLE
    
    clear_screen()
    #displayHTML(SYSTEM_TITLE)
    logger.info(" System Instances closed")


def showSystem()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, SYSTEM_QT_CHAPTER_ID, SYSTEM_TITLE
    
    clear_screen()
    #displayHTML(SYSTEM_TITLE)

    #logger.info("Opening showSystem GUI")

    system_gui = SystemGui()
    system_gui.show()

    dfc_qt_chapters.add_qt_chapter(SYSTEM_QT_CHAPTER_ID,system_gui,"showSystem")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(SYSTEM_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " System Instances Loaded")

    #return system_gui  

def closeSystemChapter()  :

    closeSystemInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCSystem')","unable to delete System : ")    

