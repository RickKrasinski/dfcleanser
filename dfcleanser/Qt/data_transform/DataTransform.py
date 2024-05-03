"""
# data cleansing
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

DEBUG_TRANSFORM                 =   False
DEBUG_TRANSFORM_DATAFRAMES      =   False
DEBUG_TRANSFORM_DATETIME        =   False

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Transform Housekeeping                 -#
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
# -                Data Cleansing subfunctions                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


DFS_SELECT                                  =   "DataTransform dfsSelect"

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Column Transform Layouts                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DISPLAY_TRANSFORM_COLUMN                    =   "DataTransform transform column"

DISPLAY_RENAME_COLUMN                       =   "DataTransform rename column"
DISPLAY_RENAME_COLUMN_FORM                  =   "DataTransform rename column form"
DISPLAY_UNIVERSAL_RENAME_COLUMN_FORM        =   "DataTransform universal rename column form"

DISPLAY_DROP_COLUMN                         =   "DataTransform drop column"
DISPLAY_REORDER_COLUMN                      =   "DataTransform reorder column"

DISPLAY_ADD_COLUMN                          =   "DataTransform add column"
DISPLAY_ADD_COLUMN_FROM_FNS                 =   "DataTransform add column from fns"
DISPLAY_ADD_COLUMN_FROM_USER_CODE           =   "DataTransform add column from user code"
DISPLAY_ADD_COLUMN_FROM_MERGE               =   "DataTransform add column from merge"
DISPLAY_ADD_COLUMN_FROM_JOIN                =   "DataTransform add column from join"

DISPLAY_DUMMIES_COLUMN                      =   "DataTransform dummies column"
DISPLAY_MAP_COLUMN                          =   "DataTransform map column"
DISPLAY_SAVE_COLUMN                         =   "DataTransform save column"
DISPLAY_COPY_COLUMN                         =   "DataTransform copy column"
DISPLAY_CAT_COLUMN                          =   "DataTransform categorical column"

DISPLAY_APPLY_FN_SELECT_COLUMN              =   "DataTransform apply fn select column"
DISPLAY_APPLY_DFC_FN_COLUMN                 =   "DataTransform apply dcf fn column"
DISPLAY_APPLY_USER_FN_COLUMN                =   "DataTransform apply user fn column"

DISPLAY_CHANGE_DATATYPE_NO_NANS             =   "DataTransform change datatype no nans"
DISPLAY_CHANGE_DATATYPE_NANS                =   "DataTransform change datatype nans"
DISPLAY_CHANGE_DATATYPE_SELECT_COLUMN       =   "DataTransform change datatype select column"

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -        Dataframe Column Names Row Transform Layouts           -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DISPLAY_TRANSFORM_DATAFRAME                 =   "DataTransform transform dataframe"
DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES_ROW   =   "DataTransform transform dataframe col names row"
DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES       =   "DataTransform transform dataframe col names"
DISPLAY_TRANSFORM_DATAFRAME_SAVE_ROW        =   "DataTransform transform dataframe save col names row"
DISPLAY_TRANSFORM_DATAFRAME_ADD_ROW         =   "DataTransform transform dataframe add col names row"

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              Dataframe Index Transform Layouts                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DISPLAY_TRANSFORM_DATAFRAME_INDEX           =   "DataTransform transform dataframe index"
DISPLAY_TRANSFORM_DATAFRAME_INDEX_DATA      =   "DataTransform transform dataframe index data"
DISPLAY_TRANSFORM_DATAFRAME_SET_INDEX       =   "DataTransform transform dataframe set index"
DISPLAY_TRANSFORM_DATAFRAME_RESET_INDEX     =   "DataTransform transform dataframe reset index"
DISPLAY_TRANSFORM_DATAFRAME_REINDEX_INDEX   =   "DataTransform transform dataframe reindex index"
DISPLAY_TRANSFORM_DATAFRAME_APPEND_INDEX    =   "DataTransform transform dataframe append index"
DISPLAY_TRANSFORM_DATAFRAME_SORT_INDEX      =   "DataTransform transform dataframe sort index"

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Dataframe Sort Transform Layouts                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DISPLAY_TRANSFORM_DATAFRAME_SORT_DF         =   "DataTransform transform dataframe sort df"


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Datetime Transform Layouts                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

DISPLAY_TRANSFORM_DATETIME                  =   "DataTransform transform datetime"
DISPLAY_TRANSFORM_DATETIME_CONVERT          =   "DataTransform transform datetime convert"
DISPLAY_TRANSFORM_DATETIME_TIME_CONVERT     =   "DataTransform transform datetime time convert"
DISPLAY_TRANSFORM_DATETIME_TIMEDELTA        =   "DataTransform transform datetime timedelta"
DISPLAY_TRANSFORM_CALCULATE_TIMEDELTA       =   "DataTransform transform calculate timedelta"
DISPLAY_TRANSFORM_MERGE                     =   "DataTransform transform merge"
DISPLAY_TRANSFORM_COMPONENTS                =   "DataTransform transform components"



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              Data Cleansing Style Constants                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       System main GUI                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataTransformGui(QtWidgets.QMainWindow):

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

        self.DataTransformWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.DataTransformLayout.addLayout(self.stackedLayout)
        self.form.DataTransformLayout.addStretch()

        from dfcleanser.common.cfg import DataTransform_add_df_signal
        DataTransform_add_df_signal.connectSignal(self.add_new_df)

        #set the window size for dfcleanser
        #geometry = QtWidgets.QApplication.desktop().availableGeometry()

        #print("geometry",geometry)
        
        #titleBarHeight = self.style().pixelMetric(
        #    CustomizeWindowHint flag needs to be set first before the WindowCloseButtonHintQtGui.QStyle.PM_TitleBarHeight,
        #    QtGui.QStyleOptionTitleBar(),
        #    self
        #)
        #geometry.setHeight(geometry.height() - (titleBarHeight*2))
        #geometry.setWidth(1109)
        #self.setGeometry(geometry)



    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_transform\DataTransformUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Data Transform")
        
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
        icon_name   =   dfcdir +"\DataTransformChapterIcon.png"
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
        self.init_data_transform_form()

           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_transform_buttons(self):

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][init_data_transform_buttons]  ")

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.dataframe_button               =   QPushButton()   
        #self.rows_button                    =   QPushButton()    
        self.columns_button                 =   QPushButton()   
        self.datetime_button                =   QPushButton()
        self.help_button                    =   QPushButton()     

        button_bar_button_list     =   [self.dataframe_button, self.columns_button, self.datetime_button, self.help_button]
        button_bar_text_list       =   ["dataframes","Columns","datetime","Help"]
        button_bar_size_list       =   [250,70]
        button_bar_tool_tip_list   =   ["Transform dataframes","Transform Columns","Transform datetime","Transform Help"]
        button_bar_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar_connect_list    =   [self.data_transform_dataframes, self.data_transform_columns, 
                                        self.data_transform_datetime, self.data_transform_help]

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        self.transform_button_bar           =   QHBoxLayout()
        build_button_bar(self.transform_button_bar,button_bar_button_list,button_bar_text_list,button_bar_size_list,button_bar_tool_tip_list,button_bar_stylesheet,button_bar_connect_list)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.transform_button_bar)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.form.DataTransformCmdbarLayout)
        self.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_transform_splash_screen(self):

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][init_data_transform_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import DataTransform_ID
        build_chapter_splash_screen(DataTransform_ID, self.form.DataTransformsplash)

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][add_new_df]  df_title",df_title)

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(DEBUG_TRANSFORM) :
            print("self.df_select",type(self.df_select),self.df_select.count())

        self.init_stacked_index()

    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_dfs_to_transform(self):

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][init_dfs_to_transform]  ")
        
        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_transform")

        self.df_select          =   dfc_dfs_objects[0]
        self.dfc_dfs_layout     =   dfc_dfs_objects[1]

        from PyQt5.QtWidgets import QWidget
        self.dfc_dfs     =   QWidget()
        self.dfc_dfs.setLayout(self.dfc_dfs_layout)
        
    # -----------------------------------------------------------------#
    # -               Initialize the widgets stack                    -#
    # -----------------------------------------------------------------#
    def init_stacked_index(self) :

        dfs_index  =   self.DataTransformWidgets_stack_dict.get(DFS_SELECT)

        if(dfs_index is None) :
            current_index   =  len(self.DataTransformWidgets_stack_dict)
            self.DataTransformWidgets_stack_dict.update({DFS_SELECT: current_index})
            self.stackedLayout.addWidget(self.dfc_dfs)
        else :
            self.init_data_transform_buttons()
            current_index   =   dfs_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,400)

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_transform_form(self):
        
        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][init_data_transform_form]  ")

        self.init_data_transform_buttons()
        self.init_data_transform_splash_screen()
        self.init_dfs_to_transform()
        self.init_stacked_index()

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][init_data_transform_form] end \n",self.DataTransformWidgets_stack_dict,"\n")

    # -----------------------------------------------------------------#
    # -              Main Gui Data Transform Methods                  -#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                    transform dataframes                       -#
    # -----------------------------------------------------------------#
    def data_transform_dataframes(self) :

        self.form.TransformdataframeButton.toggle()

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][data_transform_dataframes]")

        self.display_transform_dataframes()

    # -----------------------------------------------------------------#
    # -                       transform rows                          -#
    # -----------------------------------------------------------------#
    def data_transform_rows(self) :

        self.form.TransformrowsButton.toggle()

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][data_transform_rows]")

    # -----------------------------------------------------------------#
    # -                       transform cols                          -#
    # -----------------------------------------------------------------#
    def data_transform_columns(self) :

        self.form.TransformcolumnsButton.toggle()

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][data_transform_columns]")

        self.display_transform_columns()

    # -----------------------------------------------------------------#
    # -                     transform datetime                        -#
    # -----------------------------------------------------------------#
    def data_transform_datetime(self) :

        self.form.TransformdatetimeButton.toggle()

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][data_transform_datetime]")

        self.display_transform_datetime(DTDM.DATETIME_MAIN)

    # -----------------------------------------------------------------#
    # -                     transform help                        -#
    # -----------------------------------------------------------------#
    def data_transform_help(self) :

        #self.form.TransformhelpButton.toggle()

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][data_transform_help]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_MAIN_TASKBAR_ID
        display_url(TRANSFORM_MAIN_TASKBAR_ID)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display transform columns methods                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_transform_columns(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_transform_columns]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_columns] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM) :
            print("[DataCleansingGui][display_transform_columns]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_transform_columns_Widget
                parms               =   [self,self.dftitle]
                self.transform_col  =   DataTransform_transform_columns_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_columns] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_COLUMN : current_index})
                self.stackedLayout.addWidget(self.transform_col)

        else :

            self.transform_col.reload_banner()
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_transform_columns] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,400)


    # -----------------------------------------------------------------#
    # -                        rename column                          -#
    # -----------------------------------------------------------------#
    def display_rename_column_form(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_rename_column_form]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()
        
        self.dftitle     =   self.df_select.currentText()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_RENAME_COLUMN_FORM)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_rename_column_form_Widget
                parms                   =   [self,self.dftitle]
                self.rename_col_form    =   DataTransform_rename_column_form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_rename_column_form] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_RENAME_COLUMN_FORM : current_index})
                self.stackedLayout.addWidget(self.rename_col_form)

        else :

            self.rename_col_form.reload_data(self,self.dftitle)

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_rename_column_form] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,900)
    
    # -----------------------------------------------------------------#
    # -                   universal rename column                     -#
    # -----------------------------------------------------------------#
    def display_universal_rename_column_form(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_universal_rename_column_form]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()
        
        self.dftitle     =   self.df_select.currentText()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_UNIVERSAL_RENAME_COLUMN_FORM)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_universal_column_form_Widget
                parms                           =   [self,self.dftitle]
                self.universal_rename_col_form  =   DataTransform_universal_column_form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_universal_rename_column_form] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_UNIVERSAL_RENAME_COLUMN_FORM : current_index})
                self.stackedLayout.addWidget(self.universal_rename_col_form)

        else :

            self.universal_rename_col_form.reload_data(self,self.dftitle)
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_universal_rename_column_form] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,900)
    

    # -----------------------------------------------------------------#
    # -                         drop column                           -#
    # -----------------------------------------------------------------#
    def display_drop_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_drop_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle     =   self.df_select.currentText()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_DROP_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_drop_column_Widget
                parms               =   [self,self.dftitle]
                self.drop_col       =   DataTransform_drop_column_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_drop_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_DROP_COLUMN : current_index})
                self.stackedLayout.addWidget(self.drop_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_drop_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,700)

    
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display add column                          -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                         add column                            -#
    # -----------------------------------------------------------------#
    def display_add_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_add_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle     =   self.df_select.currentText()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_ADD_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_add_column_form_Widget
                parms               =   [self,self.dftitle]
                self.add_col        =   DataTransform_add_column_form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_ADD_COLUMN : current_index})
                self.stackedLayout.addWidget(self.add_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_add_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,900)

    def display_add_colum_from_fns(self, new_colname):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_add_colum_from_fns]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle             =   self.df_select.currentText()
        self.new_colname    =   new_colname

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_add_colum_from_fns invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_ADD_COLUMN_FROM_FNS )
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_add_column_from_fns_form_Widget
                parms                   =   [self,self.dftitle,self.new_colname]
                self.add_col_from_fns   =   DataTransform_add_column_from_fns_form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_column_from_fns] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_ADD_COLUMN_FROM_FNS  : current_index})
                self.stackedLayout.addWidget(self.add_col_from_fns)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_add_colum_from_fns] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,650)

    def display_add_colum_from_user_code(self,newcolname):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_add_colum_from_user_code]  ",newcolname)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_add_colum_from_fns invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle    =   dftitle
        self.colname    =   newcolname

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_ADD_COLUMN_FROM_USER_CODE)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_add_column_from_user_code_form_Widget
                parms                           =   [self,self.dftitle,self.colname]
                self.add_col_from_user_code     =   DataTransform_add_column_from_user_code_form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_column_from_user_code] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_ADD_COLUMN_FROM_USER_CODE : current_index})
                self.stackedLayout.addWidget(self.add_col_from_user_code)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_add_colum_from_user_code] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,800)

    def display_add_colum_from_merge(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_add_colum_from_merge]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_add_colum_from_merge] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_ADD_COLUMN_FROM_MERGE)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_add_column_from_merge_form_Widget
                parms                       =   [self,self.dftitle]
                add_col_from_merge          =   DataTransform_add_column_from_merge_form_Widget(parms)

                if(not(add_col_from_merge is None)) :               
                    self.add_col_from_merge     =   add_col_from_merge
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_column_from_merge] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_ADD_COLUMN_FROM_MERGE : current_index})
                self.stackedLayout.addWidget(self.add_col_from_merge)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,800)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_add_colum_from_merge] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    def display_add_colum_from_join(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_add_colum_from_join]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_add_colum_from_join] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_ADD_COLUMN_FROM_JOIN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_add_column_from_join_form_Widget
                parms                   =   [self,self.dftitle]
                add_col_from_join       =   DataTransform_add_column_from_join_form_Widget(parms)
                
                if(not(add_col_from_join is None)) :               
                    self.add_col_from_join     =   add_col_from_join
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_column_from_join] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_ADD_COLUMN_FROM_JOIN : current_index})
                self.stackedLayout.addWidget(self.add_col_from_join)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,1000)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_add_colum_from_join] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display add column end                       -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                  display reorder column                       -#
    # -----------------------------------------------------------------#

    def display_reorder_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_reorder_colum]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_reorder_colum] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_REORDER_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_reorder_column_Widget
                parms           =   [self,self.dftitle]
                reorder_col     =   DataTransform_reorder_column_Widget(parms)
                
                if(not(reorder_col is None)) :               
                    self.reorder_col     =   reorder_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_reorder_column_from_join] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_REORDER_COLUMN : current_index})
                self.stackedLayout.addWidget(self.reorder_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,700)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_reorder_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

    # -----------------------------------------------------------------#
    # -                  display dummies column                       -#
    # -----------------------------------------------------------------#
    def display_dummies_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_dummies_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_dummies_column] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_DUMMIES_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_dummies_column_form_Widget
                parms           =   [self,self.dftitle]
                dummies_col     =   DataTransform_dummies_column_form_Widget(parms)
                
                if(not(dummies_col is None)) :               
                    self.dummies_col     =   dummies_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_dummies_column_from_join] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_DUMMIES_COLUMN : current_index})
                self.stackedLayout.addWidget(self.dummies_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,800)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_dummies_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    

    # -----------------------------------------------------------------#
    # -                    display save columns                       -#
    # -----------------------------------------------------------------#
    def display_save_columns(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_save_columns]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_save_columns] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_SAVE_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_save_column_form_Widget
                parms       =   [self,self.dftitle]
                save_col    =   DataTransform_save_column_form_Widget(parms)
                
                if(not(save_col is None)) :               
                    self.save_col     =   save_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_save_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_SAVE_COLUMN : current_index})
                self.stackedLayout.addWidget(self.save_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,950)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_save_columns] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    # -----------------------------------------------------------------#
    # -                    display copy columns                       -#
    # -----------------------------------------------------------------#
    def display_copy_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_copy_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_copy_column] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_COPY_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_copy_column_form_Widget
                parms       =   [self,self.dftitle]
                copy_col    =   DataTransform_copy_column_form_Widget(parms)
                
                if(not(copy_col is None)) :               
                    self.copy_col     =   copy_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_copy_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_COPY_COLUMN : current_index})
                self.stackedLayout.addWidget(self.copy_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,800)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_copy_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display apply fn columns variants                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                  display apply fn columns                     -#
    # -----------------------------------------------------------------#
    def display_apply_fn_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_apply_fn_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle     =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_apply_fn_column] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_APPLY_FN_SELECT_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_apply_fn_select_Widget
                parms       =   [self,self.dftitle]
                apply_fn_col     =   DataTransform_apply_fn_select_Widget(parms)
                
                if(not(apply_fn_col is None)) :               
                    self.apply_fn_col     =   apply_fn_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_apply_fn_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_APPLY_FN_SELECT_COLUMN : current_index})
                self.stackedLayout.addWidget(self.apply_fn_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,900)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_apply_fn_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    # -----------------------------------------------------------------#
    # -                  display apply df fn columns                  -#
    # -----------------------------------------------------------------#
    def display_apply_dfc_fn_column(self,colname):

        self.colname    =   colname

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_apply_fn_column]  ",self.colname)

        dftitle     =   self.df_select.currentText()
        self.dftitle     =   dftitle
        
        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_APPLY_DFC_FN_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_apply_dfc_fn_form_Widget
                parms               =   [self,self.dftitle,self.colname]
                apply_dfc_fn_col    =   DataTransform_apply_dfc_fn_form_Widget(parms)
                
                if(not(apply_dfc_fn_col is None)) :               
                    self.apply_dfc_fn_col     =   apply_dfc_fn_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_apply_dfc_fn_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_APPLY_DFC_FN_COLUMN : current_index})
                self.stackedLayout.addWidget(self.apply_dfc_fn_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,600)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_apply_dfc_fn_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

    # -----------------------------------------------------------------#
    # -                 display apply user fn columns                 -#
    # -----------------------------------------------------------------#
    def display_apply_user_fn_column(self,colname):

        self.colname    =   colname

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_apply_user_fn_column]  ",self.colname)

        dftitle     =   self.df_select.currentText()
        self.dftitle     =   dftitle
        
        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_APPLY_USER_FN_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_apply_user_fn_form_Widget
                parms                =   [self,self.dftitle,self.colname]
                apply_user_fn_col    =   DataTransform_apply_user_fn_form_Widget(parms)
                
                if(not(apply_user_fn_col is None)) :               
                    self.apply_user_fn_col     =   apply_user_fn_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_apply_user_fn_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_APPLY_USER_FN_COLUMN : current_index})
                self.stackedLayout.addWidget(self.apply_user_fn_col)

        else :

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,900)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_apply_user_fn_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")



    # -----------------------------------------------------------------#
    # -                      display select a column                  -#
    # -----------------------------------------------------------------#
    """
    def display_select_column(self,select_column_for):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_select_column] select_column_for ",select_column_for)

        dftitle             =   self.df_select.currentText()
        self.dftitle        =   dftitle
        self.select_for     =   select_column_for
        
        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_CHANGE_DATATYPE_SELECT_COLUMN)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_select_column] data_transform_index ",data_transform_index)

        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_select_column_form_Widget
                parms               =   [self,self.dftitle,self.select_for]
                self.select_form    =   DataTransform_select_column_form_Widget(parms)
                
            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_select_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_CHANGE_DATATYPE_SELECT_COLUMN : current_index})
                self.stackedLayout.addWidget(self.select_form)

        else :

            self.select_form.reload_data(self,self.dftitle,self.select_for)
            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,900)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_select_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")
    """

# -----------------------------------------------------------------#
    # -                    display map column                         -#
    # -----------------------------------------------------------------#
    def display_map_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_map_column]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle         =   self.df_select.currentText()
        #self.colname    =   colname

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_dummies_column] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_MAP_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_map_column_form_Widget
                parms           =   [self,self.dftitle]
                map_col    =   DataTransform_map_column_form_Widget(parms)
                
                if(not(map_col is None)) :               
                    self.map_col     =   map_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_map_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_MAP_COLUMN : current_index})
                self.stackedLayout.addWidget(self.map_col)

        else :

            current_index   =   data_transform_index
            self.map_col.reload_data(self,self.dftitle)

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,950)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_map_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")



    # -----------------------------------------------------------------#
    # -                    display category columns                   -#
    # -----------------------------------------------------------------#
    def display_category_column(self):

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_category_column] ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle         =   self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_category_column] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        self.dftitle     =   dftitle

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_CAT_COLUMN)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_category_column_form_Widget
                parms       =   [self,self.dftitle]
                cat_col     =   DataTransform_category_column_form_Widget(parms)
                
                if(not(cat_col is None)) :               
                    self.cat_col     =   cat_col
                else :
                    opstat.set_status(False)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_category_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_CAT_COLUMN : current_index})
                self.stackedLayout.addWidget(self.cat_col)

        else :

            current_index   =   data_transform_index
            self.cat_col.reload_data(self,self.dftitle)

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,950)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_category_column] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")



    # -----------------------------------------------------------------#
    # -                 display change column datatype                -#
    # -----------------------------------------------------------------#
    def display_change_column_datatype(self,colname):

        self.colname    =   colname

        if(DEBUG_TRANSFORM) :
            print("\n[DataTransformGui][display_change_column_datatype]  ",self.colname)

        dftitle         =   self.df_select.currentText()
        self.dftitle    =   dftitle
        
        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df              =   get_dfc_dataframe_df(self.dftitle)
        if(self.colname is None) :
            total_nans  =   0
        else :
            total_nans  =   df[self.colname].isnull().sum()

        if(total_nans == 0) :
            data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_CHANGE_DATATYPE_NO_NANS)
        else :
            data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_CHANGE_DATATYPE_NANS)            
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformColumnsWidgets import DataTransform_change_datatype_form_Widget
                parms                   =   [self,self.dftitle,self.colname]
                change_datatype_form    =   DataTransform_change_datatype_form_Widget(parms)
                
            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_change_column_datatype] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                
                if(total_nans == 0) :

                    self.DataTransformWidgets_stack_dict.update({DISPLAY_CHANGE_DATATYPE_NO_NANS : current_index})
                    self.change_datatype_no_nans_form   =  change_datatype_form 
                    self.stackedLayout.addWidget(self.change_datatype_no_nans_form)

                else :

                    self.DataTransformWidgets_stack_dict.update({DISPLAY_CHANGE_DATATYPE_NANS : current_index})
                    self.change_datatype_nans_form   =  change_datatype_form 
                    self.stackedLayout.addWidget(self.change_datatype_nans_form)

        else :

            if(total_nans == 0) :
                self.change_datatype_no_nans_form.reload_data(self,self.dftitle,self.colname)
            else :
                self.change_datatype_nans_form.reload_data(self,self.dftitle,self.colname)    

            current_index   =   data_transform_index

        if(opstat.get_status()) :

            self.stackedLayout.setCurrentIndex(current_index)
            if(total_nans == 0) :
                self.resize(1070,850)
            else :
                self.resize(1070,950)

        if(DEBUG_TRANSFORM) :
            print("[DataTransformGui][display_change_column_datatype] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -            display transform columns Layouts end              -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display transform dataframe                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_transform_dataframes(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_columns]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_dataframe] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_dataframe]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_Widget
                parms               =   [self,self.dftitle]
                self.transform_df   =   DataTransform_transform_dataframe_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_dataframe] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME : current_index})
                self.stackedLayout.addWidget(self.transform_df)

        else :

            self.transform_df.reload_banner()
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_dataframe] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,400)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -      display transform dataframe column names Layouts         -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_transform_dataframe_column_names(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_dataframe_column_names]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_dataframe_column_names] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_dataframe_column_names]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES_ROW)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_col_names_row_Widget
                parms                           =   [self,self.dftitle]
                self.transform_df_col_names     =   DataTransform_transform_dataframe_col_names_row_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_dataframe_column_names] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES_ROW : current_index})
                self.stackedLayout.addWidget(self.transform_df_col_names)
                self.stackedLayout.setAlignment(Qt.AlignHCenter)

        else :

            self.transform_df_col_names.reload_data(self,self.dftitle)
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_dataframe_column_names] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,400)

    def display_transform_col_names_row(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_col_names_row]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_col_names_row] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_col_names_row]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_column_names_Widget
                parms              =   [self,self.dftitle]
                self.col_names     =   DataTransform_transform_column_names_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_col_names_row] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME_COL_NAMES : current_index})
                self.stackedLayout.addWidget(self.col_names)

        else :

            self.col_names.reload_data()
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_col_names_row] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        #self.stackedLayout

        self.resize(1070,700)

    def display_transform_save_col_names_row(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_save_col_names_row]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_save_col_names_row] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_save_col_names_row]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME_SAVE_ROW)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_save_col_names_row_Widget
                parms                   =   [self,self.dftitle]
                self.save_col_names     =   DataTransform_transform_dataframe_save_col_names_row_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_save_col_names_row] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME_SAVE_ROW : current_index})
                self.stackedLayout.addWidget(self.save_col_names)

        else :

            #self.col_names.reload_data()
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_save_col_names_row] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        #self.stackedLayout

        self.resize(1070,600)

    def display_transform_add_col_names_row(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_add_col_names_row]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_add_col_names_row] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_add_col_names_row]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME_ADD_ROW)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_add_col_names_row_Widget
                parms                   =   [self,self.dftitle]
                self.add_col_names     =   DataTransform_transform_dataframe_add_col_names_row_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_add_col_names_row] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME_ADD_ROW : current_index})
                self.stackedLayout.addWidget(self.add_col_names)

        else :

            #self.col_names.reload_data()
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_add_col_names_row] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,800)
  
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display transform index Layouts                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_transform_dataframe_index(self,index_option):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_dataframe_index]  option : ",index_option)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_dataframe_index] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_dataframe_index]  : dftitlle : ",dftitle)

        if(index_option == DTDM.DF_INDEX_MAIN) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_INDEX
            form_height     =   400
        elif(index_option == DTDM.DF_SHOW_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_INDEX_DATA
            form_height     =   400        
        elif(index_option == DTDM.DF_SET_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_SET_INDEX
            form_height     =   800        
        elif(index_option == DTDM.DF_RESET_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_RESET_INDEX
            form_height     =   800
        elif(index_option == DTDM.DF_REINDEX_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_REINDEX_INDEX
            form_height     =   900
        elif(index_option == DTDM.DF_APPEND_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_APPEND_INDEX
            form_height     =   800
        elif(index_option == DTDM.DF_SORT_INDEX) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATAFRAME_SORT_INDEX
            form_height     =   500

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(data_transform_index_id)
        
        if(data_transform_index is None) :

            try :

                if(index_option == DTDM.DF_INDEX_MAIN) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_index_Widget
                    parms                       =   [self,self.dftitle]
                    self.transform_df_index     =   DataTransform_transform_dataframe_index_Widget(parms)
                
                elif(index_option == DTDM.DF_SHOW_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_df_index_Widget
                    parms               =   [self,self.dftitle]
                    self.show_index     =   DataTransform_transform_df_index_Widget(parms)

                elif(index_option == DTDM.DF_SET_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_set_index_Widget
                    parms               =   [self,self.dftitle]
                    self.set_index      =   DataTransform_transform_dataframe_set_index_Widget(parms)

                elif(index_option == DTDM.DF_RESET_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_reset_index_Widget
                    parms               =   [self,self.dftitle]
                    self.reset_index      =   DataTransform_transform_dataframe_reset_index_Widget(parms)

                elif(index_option == DTDM.DF_REINDEX_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_reset_index_Widget
                    parms                   =   [self,self.dftitle]
                    self.reindex_index      =   DataTransform_transform_dataframe_reset_index_Widget(parms)

                elif(index_option == DTDM.DF_APPEND_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_append_index_Widget
                    parms               =   [self,self.dftitle]
                    self.append_index   =   DataTransform_transform_dataframe_append_index_Widget(parms)

                elif(index_option == DTDM.DF_SORT_INDEX) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_sort_index_Widget
                    parms               =   [self,self.dftitle]
                    self.sort_index     =   DataTransform_transform_dataframe_sort_index_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_dataframe_index] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({data_transform_index_id : current_index})

                if(index_option == DTDM.DF_INDEX_MAIN) :
                    self.stackedLayout.addWidget(self.transform_df_index)
                elif(index_option == DTDM.DF_SHOW_INDEX) :
                    self.stackedLayout.addWidget(self.show_index)
                elif(index_option == DTDM.DF_SET_INDEX) :
                    self.stackedLayout.addWidget(self.set_index)
                elif(index_option == DTDM.DF_RESET_INDEX) :
                    self.stackedLayout.addWidget(self.reset_index)
                elif(index_option == DTDM.DF_REINDEX_INDEX) :
                    self.stackedLayout.addWidget(self.reindex_index)
                elif(index_option == DTDM.DF_APPEND_INDEX) :
                    self.stackedLayout.addWidget(self.append_index)
                elif(index_option == DTDM.DF_SORT_INDEX) :
                    self.stackedLayout.addWidget(self.sort_index)

        else :

            if(index_option == DTDM.DF_INDEX_MAIN) :
                self.transform_df_index.reload_data()
                form_height     =   400
            elif(index_option == DTDM.DF_SHOW_INDEX) :
                self.show_index.reload_data()
                form_height     =   400
            elif(index_option == DTDM.DF_SET_INDEX) :
                self.set_index.reload_data(self,self.dftitle)
                form_height     =   800
            elif(index_option == DTDM.DF_RESET_INDEX) :
                self.reset_index.reload_data(self,self.dftitle)
                form_height     =   800
            elif(index_option == DTDM.DF_REINDEX_INDEX) :
                self.reindex_index.reload_data(self,self.dftitle)
                form_height     =   900
            elif(index_option == DTDM.DF_APPEND_INDEX) :
                self.append_index.reload_data(self,self.dftitle)
                form_height     =   800 
            elif(index_option == DTDM.DF_SORT_INDEX) :
                self.sort_index.reload_data(self,self.dftitle)
                form_height     =   500

            current_index   =    data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,form_height)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_dataframe_index] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display transform sort df Layout                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_transform_sort_df(self):

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("\n[DataTransformGui][display_transform_sort_df]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_sort_df] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataCleansingGui][display_transform_sort_df]  : dftitlle : ",dftitle)

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(DISPLAY_TRANSFORM_DATAFRAME_SORT_DF)
        
        if(data_transform_index is None) :

            try :

                from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_dataframe_sort_df_Widget
                parms               =   [self,self.dftitle]
                self.sort_df        =   DataTransform_transform_dataframe_sort_df_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_sort_df] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({DISPLAY_TRANSFORM_DATAFRAME_SORT_DF : current_index})
                self.stackedLayout.addWidget(self.sort_df)

        else :

            self.sort_df.reload_data(self,self.dftitle)
            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_TRANSFORM_DATAFRAMES) :
            print("[DataTransformGui][display_transform_sort_df] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display transform datatime Layouts               -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_transform_datetime(self,datetime_option,colname=None):

        if(DEBUG_TRANSFORM_DATETIME) :
            print("\n[DataTransformGui][display_transform_datetime]  option : ",datetime_option,colname)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_datetime] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        self.dftitle     =   dftitle

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataCleansingGui][display_transform_datetime]  dftitle : ",dftitle)

        if(datetime_option == DTDM.DATETIME_MAIN) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATETIME
            form_height     =   400
        elif(datetime_option == DTDM.DATETIME_CONVERT) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATETIME_CONVERT
            form_height     =   850        
        elif(datetime_option == DTDM.DATETIME_TIME_CONVERT) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATETIME_TIME_CONVERT
            form_height     =   850        
        elif(datetime_option == DTDM.DATETIME_CONVERT_TIMEDELTA) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_DATETIME_TIMEDELTA
            form_height     =   800
        elif(datetime_option == DTDM.DATETIME_CALCULATE_TIMEDELTA) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_CALCULATE_TIMEDELTA
            form_height     =   850
        elif(datetime_option == DTDM.DATETIME_MERGE) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_MERGE
            form_height     =   900
        elif(datetime_option == DTDM.DATETIME_COMPONENTS) :
            data_transform_index_id  =   DISPLAY_TRANSFORM_COMPONENTS
            form_height     =   750

        data_transform_index  =   self.DataTransformWidgets_stack_dict.get(data_transform_index_id)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataCleansingGui][display_transform_datetime]  data_transform_index : ",data_transform_index)

        
        if(data_transform_index is None) :

            try :

                if(datetime_option == DTDM.DATETIME_MAIN) :
                            
                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_datetime_Widget
                    parms                   =   [self,self.dftitle]
                    self.transform_widget   =   DataTransform_transform_datetime_Widget(parms)
                
                elif(datetime_option == DTDM.DATETIME_CONVERT) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_datatime_convert_Widget
                    parms                   =   [self,self.dftitle]
                    self.convert_widget     =   DataTransform_transform_datatime_convert_Widget(parms)
                
                elif(datetime_option == DTDM.DATETIME_TIME_CONVERT) :
                            
                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_datatime_time_convert_Widget
                    parms                       =   [self,self.dftitle,colname]
                    self.convert_time_widget    =   DataTransform_transform_datatime_time_convert_Widget(parms)

                elif(datetime_option == DTDM.DATETIME_CONVERT_TIMEDELTA) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_timedelta_convert_Widget
                    parms                   =   [self,self.dftitle]
                    self.timedelta_widget   =   DataTransform_transform_timedelta_convert_Widget(parms)

                elif(datetime_option == DTDM.DATETIME_CALCULATE_TIMEDELTA) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_calculate_timedelta_Widget
                    parms                               =   [self,self.dftitle]
                    self.calculate_timedelta_widget     =   DataTransform_transform_calculate_timedelta_Widget(parms)

                elif(datetime_option == DTDM.DATETIME_MERGE) :

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_merge_datetime_Widget
                    parms                 =   [self,self.dftitle]
                    self.merge_widget     =   DataTransform_transform_merge_datetime_Widget(parms)

                else :    

                    from dfcleanser.Qt.data_transform.DataTransformDataframeWidgets import DataTransform_transform_datetime_components_Widget
                    parms                       =   [self,self.dftitle]
                    self.components_widget      =   DataTransform_transform_datetime_components_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_transform_datetime] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataTransformWidgets_stack_dict)
                self.DataTransformWidgets_stack_dict.update({data_transform_index_id : current_index})

                if(datetime_option == DTDM.DATETIME_MAIN) :
                    self.stackedLayout.addWidget(self.transform_widget)
                elif(datetime_option == DTDM.DATETIME_CONVERT) :
                    self.stackedLayout.addWidget(self.convert_widget)
                elif(datetime_option == DTDM.DATETIME_TIME_CONVERT) :
                    self.stackedLayout.addWidget(self.convert_time_widget)
                elif(datetime_option == DTDM.DATETIME_CONVERT_TIMEDELTA) :
                    self.stackedLayout.addWidget(self.timedelta_widget)
                elif(datetime_option == DTDM.DATETIME_CALCULATE_TIMEDELTA) :
                    self.stackedLayout.addWidget(self.calculate_timedelta_widget)
                elif(datetime_option == DTDM.DATETIME_MERGE) :
                    self.stackedLayout.addWidget(self.merge_widget)
                else :    
                    self.stackedLayout.addWidget(self.components_widget)

        else :

            if(datetime_option == DTDM.DATETIME_MAIN) :
                self.transform_widget.reload_banner()
            elif(datetime_option == DTDM.DATETIME_CONVERT) :
                self.convert_widget.reload_data(self,self.dftitle)
            elif(datetime_option == DTDM.DATETIME_TIME_CONVERT) :
                self.convert_time_widget.reload_data(self,self.dftitle)
            elif(datetime_option == DTDM.DATETIME_CONVERT_TIMEDELTA) :
                self.timedelta_widget.reload_data(self,self.dftitle)
            elif(datetime_option == DTDM.DATETIME_CALCULATE_TIMEDELTA) :
                self.calculate_timedelta_widget.reload_data(self,self.dftitle)
            elif(datetime_option == DTDM.DATETIME_MERGE) :
                self.merge_widget.reload_data(self,self.dftitle)
            else :    
                self.components_widget.reload_data(self,self.dftitle)

            current_index   =   data_transform_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)
            self.resize(1070,form_height)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransformGui][display_transform_datetime] end : stack \n  ",self.DataTransformWidgets_stack_dict,"\n")

        

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display transform dataframe end                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to System Chapter                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearDataTransform()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, TRANSFORM_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(TRANSFORM_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(TRANSFORM_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_transform_form()

    clear_screen()


def closeDataTransformInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, TRANSFORM_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(TRANSFORM_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(TRANSFORM_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import DATA_TRANSFORM_TITLE
    
    clear_screen()
    #displayHTML(DATA_TRANSFORM_TITLE)
    logger.info(" Data Transform Instances closed")

def showDataTransform()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, TRANSFORM_QT_CHAPTER_ID, DATA_TRANSFORM_TITLE
    
    clear_screen()
    #displayHTML(DATA_TRANSFORM_TITLE)

    #logger.info("Opening showDataTransform GUI")

    data_transform_gui = DataTransformGui()
    data_transform_gui.show()

    dfc_qt_chapters.add_qt_chapter(TRANSFORM_QT_CHAPTER_ID,data_transform_gui,"showDataTransform")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(TRANSFORM_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Ytansform Instances Loaded")

    #return data_transform_gui  

def closeDataTransformChapter()  :

    closeDataTransformInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDataTransform')","unable to delete data Transform : ")    

