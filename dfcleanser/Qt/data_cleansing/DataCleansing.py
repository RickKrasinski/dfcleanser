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

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataCleansing_ID



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
# -                Data Cleansing subfunctions                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


DFS_SELECT                                  =   "DataCleansing dfsSelect"

DISPLAY_CLEANSE_COLUMNS                     =   "DataCleansing cleanse columns"

DISPLAY_CLEANSE_SINGLE_COLUMN               =   "DataCleansing cleanse single columns"
DISPLAY_CLEANSE_NON_NUMERIC_SINGLE_COLUMN   =   "DataCleansing cleanse non numeric single columns"
DISPLAY_CLEANSE_CATEGORY_SINGLE_COLUMN      =   "DataCleansing cleanse category single columns"

DISPLAY_CLEANSE_FLOAT_NANS_COLUMN           =   "DataCleansing cleanse float nans columns"
DISPLAY_CLEANSE_FLOAT_NONANS_COLUMN         =   "DataCleansing cleanse float no nans columns"

DISPLAY_CLEANSE_INT_NANS_COLUMN             =   "DataCleansing cleanse int nans columns"
DISPLAY_CLEANSE_INT_NONANS_COLUMN           =   "DataCleansing cleanse int no nans columns"

DISPLAY_CLEANSE_STRING_NANS_COLUMN          =   "DataCleansing cleanse string nans columns"
DISPLAY_CLEANSE_STRING_NONANS_COLUMN        =   "DataCleansing cleanse string no nans columns"

DISPLAY_CLEANSE_CATEGORY_COLUMN             =   "DataCleansing cleanse category columns"



DISPLAY_ROUND_COLUMN                        =   "DataCleansing round columns"
DISPLAY_WHITESPACE_COLUMN                   =   "DataCleansing whitespace columns"
DISPLAY_FILLNA_COLUMN                       =   "DataCleansing fillna columns"
DISPLAY_NN_FILLNA_COLUMN                    =   "DataCleansing non numeic fillna columns"

DISPLAY_REMOVE_CATEGORY                     =   "DataCleansing remove category"
DISPLAY_ADD_NEW_CATEGORY                    =   "DataCleansing add new category"
DISPLAY_REORDER_CATEGORY                    =   "DataCleansing reorder category"

DISPLAY_CLEANSE_ROWS                        =   "DataCleansing cleanse rows"
DISPLAY_CLEANSE_ROWS_DF_FILTER              =   "DataCleansing cleanse rows df filter"
DISPLAY_CLEANSE_ROWS_DF_CRITERIA            =   "DataCleansing cleanse rows df filter criteria"
DISPLAY_CLEANSE_ROWS_DF_SAVE                =   "DataCleansing cleanse rows df filter save"

DISPLAY_DROP_DUPLICATE_ROWS                 =   "DataCleansing drop duplicate rows"

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
class DataCleansingGui(QtWidgets.QMainWindow):

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

        self.working_df         =   None

        self.DataCleansingWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.DataCleansingLayout.addLayout(self.stackedLayout)
        self.form.DataCleansingLayout.addStretch()

        from dfcleanser.common.cfg import DataCleansing_add_df_signal
        DataCleansing_add_df_signal.connectSignal(self.add_new_df)


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_cleansing\DataCleansingUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Data Cleansing")
        
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
        icon_name   =   dfcdir +"\DataCleasnsingChapterIcon.png"
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
        self.init_data_cleansing_form()

           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_cleansing_buttons(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING_DETAILS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[init_data_cleansing_buttons]  "))

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.CleanseColumnsbutton  =   QPushButton()   
        self.CleanseRowsbutton     =   QPushButton()    
        self.Helpbutton            =   QPushButton()     

        button_bar_button_list     =   [self.CleanseColumnsbutton, self.CleanseRowsbutton, self.Helpbutton]
        button_bar_text_list       =   ["Cleanse Columns","Cleanse Rows","Help"]
        button_bar_size_list       =   [330,70]
        button_bar_tool_tip_list   =   ["Cleanse Columns","Cleanse Rows","Cleanse Help"]
        button_bar_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar_connect_list    =   [self.data_cleanse_columns, self.data_cleanse_rows, self.data_cleanse_help]

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        self.cleanse_button_bar           =   QHBoxLayout()
        build_button_bar(self.cleanse_button_bar,button_bar_button_list,button_bar_text_list,button_bar_size_list,button_bar_tool_tip_list,button_bar_stylesheet,button_bar_connect_list)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.cleanse_button_bar)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.form.DataCleansingCmdbarLayout)
        self.form.DataCleansingCmdbarLayout.addLayout(cmdbarLayout)

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_cleansing_splash_screen(self):

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import DataCleansing_ID
        build_chapter_splash_screen(DataCleansing_ID, self.form.DataCleansingsplash)

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[add_new_df]  df_title",df_title))

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[add_new_df]",cfg.get_dfc_dataframes_titles_list()))
            add_debug_to_log("DataCleansingGui",print_to_string(" self.df_select",type(self.df_select),self.df_select.count()))

        self.init_stacked_index()
    
    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_dfs_to_cleanse(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING_DETAILS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[init_dfs_to_cleanse]  "))

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_cleanse")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

 
        from PyQt5.QtWidgets import QWidget
        self.dfc_dfs     =   QWidget()
        self.dfc_dfs.setLayout(self.dfc_dfs_layout)
    
    # -----------------------------------------------------------------#
    # -                Initialize the stacked index                   -#
    # -----------------------------------------------------------------#
    def init_stacked_index(self) : 

        dfs_index  =   self.DataCleansingWidgets_stack_dict.get(DFS_SELECT)

        if(dfs_index is None) :
            current_index   =  len(self.DataCleansingWidgets_stack_dict)
            self.DataCleansingWidgets_stack_dict.update({DFS_SELECT: current_index})
            self.stackedLayout.addWidget(self.dfc_dfs)
        else :
            self.init_data_cleansing_buttons()
            current_index   =   dfs_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,300)

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_cleansing_form(self):
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[init_data_cleansing_form]  "))

        buttons     =   [self.form.CleanseColumnsbutton, self.form.CleanseRowsbutton, self.form.Helpbutton] 
        callbacks   =   [self.data_cleanse_columns, self.data_cleanse_rows, self.data_cleanse_help]

        self.init_data_cleansing_buttons()
        self.init_data_cleansing_splash_screen()
        self.init_dfs_to_cleanse()
        self.init_stacked_index()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[init_data_cleansing_form] end\n  ",self.DataCleansingWidgets_stack_dict))

        #self.resize(1070,300)

    # -----------------------------------------------------------------#
    # -               Main Gui Data Import Methods                    -#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                      cleanse columns                          -#
    # -----------------------------------------------------------------#
    def data_cleanse_columns(self) :

        self.form.CleanseColumnsbutton.toggle()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[data_cleanse_columns]"))

        self.display_cleanse_columns()

    # -----------------------------------------------------------------#
    # -                       cleanse rows                            -#
    # -----------------------------------------------------------------#
    def data_cleanse_rows(self) :

        self.form.CleanseRowsbutton.toggle()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[data_cleanse_rows]"))

        self.display_cleanse_rows()

    # -----------------------------------------------------------------#
    # -                       cleanse rows                            -#
    # -----------------------------------------------------------------#
    def data_cleanse_help(self) :

        self.form.Helpbutton.toggle()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[data_cleanse_help]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_MAIN_TASKBAR_ID
        display_url(CLEANSE_MAIN_TASKBAR_ID)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display cleanse columns                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_cleanse_columns(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_columns]  "))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle = self.df_select.currentText()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_cleanse_columns] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_columns]  : dftitle : ",dftitle))

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_COLUMNS)
        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_select_column_to_cleanse_Widget
                parms               =   [self,dftitle]
                self.cleanse_col    =   DataCleansing_select_column_to_cleanse_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[Cleanse Columns] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_COLUMNS : current_index})
                self.stackedLayout.addWidget(self.cleanse_col)

        else :

            self.cleanse_col.reload_data(self,dftitle)
            current_index   =   data_cleanse_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_columns] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -            display cleanse single column                      -#
    # -----------------------------------------------------------------#

    def display_cleanse_single_column(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df         =   get_dfc_dataframe_df(self.dftitle)
        total_nans      =   self.df[self.colname].isnull().sum()

        from dfcleanser.common.common_utils import is_float_col
        if(is_float_col(self.df,self.colname)) :
            float_col   =   True
        else :
            float_col   =   False

        from dfcleanser.sw_utilities.dfc_qt_model import (NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN)

        from dfcleanser.common.common_utils import (is_categorical_col, is_numeric_col)  
        if(is_categorical_col(self.df,self.colname))  :
            formtype       =   CATEGORICAL_COLUMN 
        elif(is_numeric_col(self.df,self.colname)) :
            formtype       =   NUMERIC_COLUMN
        else :
            formtype       =   NON_NUMERIC_COLUMN   

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_single_column]  : dftitle : colname : formtype : ",self.dftitle,self.colname,formtype))

        if(formtype == NUMERIC_COLUMN) :

            if(float_col) :
                if(total_nans > 0) :
                    data_cleanse_nans_float_index   =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_FLOAT_NANS_COLUMN)
                    current_index                   =   data_cleanse_nans_float_index                         
                else :
                    data_cleanse_nonans_float_index =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_FLOAT_NANS_COLUMN)
                    current_index                   =   data_cleanse_nonans_float_index                                        
            else :
                if(total_nans > 0) :
                    data_cleanse_nans_int_index     =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_INT_NANS_COLUMN)
                    current_index                   =   data_cleanse_nans_int_index                                        
                else :
                    data_cleanse_nonans_int_index   =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_INT_NONANS_COLUMN)                    
                    current_index                   =   data_cleanse_nonans_int_index                                        

        elif(formtype == NON_NUMERIC_COLUMN) :

            if(total_nans > 0) :
                data_cleanse_nans_string_index      =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_STRING_NANS_COLUMN)
                current_index                       =   data_cleanse_nans_string_index                                        
            else :
                data_cleanse_nonans_string_index    =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_STRING_NONANS_COLUMN)                    
                current_index                       =   data_cleanse_nonans_string_index                                        
        
        else:

            data_cleanse_category_index     =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_CATEGORY_COLUMN)                    
            current_index                   =   data_cleanse_category_index                                        

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_single_column]  : formtype : current_index : ",formtype,current_index))
        
        if(current_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_cleanse_single_column_Widget, DataCleansing_cleanse_non_numeric_single_column_Widget, DataCleansing_cleanse_category_single_column_Widget
                parms               =   [self,self.dftitle,self.colname]

                if(formtype == NUMERIC_COLUMN) :

                    if(float_col) :
                        if(total_nans > 0) :
                            self.cleanse_nans_float_widget      =   DataCleansing_cleanse_single_column_Widget(parms)
                        else :
                            self.cleanse_nonans_float_widget    =   DataCleansing_cleanse_single_column_Widget(parms)                                       
                    else :
                        if(total_nans > 0) :
                            self.cleanse_nans_int_widget        =   DataCleansing_cleanse_single_column_Widget(parms)
                        else :
                            self.cleanse_nonans_int_widget      =   DataCleansing_cleanse_single_column_Widget(parms)

                elif(formtype == NON_NUMERIC_COLUMN) :

                    if(total_nans > 0) :
                        self.cleanse_nans_string_widget         =   DataCleansing_cleanse_non_numeric_single_column_Widget(parms)
                    else :
                        self.cleanse_nonans_string_widget       =   DataCleansing_cleanse_non_numeric_single_column_Widget(parms)

                else:

                    self.cleanse_category_widget                =   DataCleansing_cleanse_category_single_column_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_single_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)

                if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING_DETAILS")) :
                    add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_single_column]  : current_index : ",current_index))
                
                if(formtype == NUMERIC_COLUMN) :

                    if(float_col) :
                        if(total_nans > 0) :
                            self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_FLOAT_NANS_COLUMN : current_index})
                            self.stackedLayout.addWidget(self.cleanse_nans_float_widget)
                        else :
                            self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_FLOAT_NONANS_COLUMN : current_index})
                            self.stackedLayout.addWidget(self.cleanse_nonans_float_widget)
                    else :
                        if(total_nans > 0) :
                            self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_INT_NANS_COLUMN : current_index})
                            self.stackedLayout.addWidget(self.cleanse_nans_int_widget)
                        else :
                            self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_INT_NONANS_COLUMN : current_index})
                            self.stackedLayout.addWidget(self.cleanse_nonans_int_widget)

                elif(formtype == NON_NUMERIC_COLUMN) :

                    if(total_nans > 0) :
                        self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_STRING_NANS_COLUMN : current_index})
                        self.stackedLayout.addWidget(self.cleanse_nans_string_widget)
                    else :
                        self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_STRING_NONANS_COLUMN : current_index})
                        self.stackedLayout.addWidget(self.cleanse_nonans_string_widget)

                else:

                    self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_CATEGORY_COLUMN : current_index})
                    self.stackedLayout.addWidget(self.cleanse_category_widget)

        else :

            if(formtype == NUMERIC_COLUMN) :

                if(float_col) :
                    if(total_nans > 0) :
                        self.cleanse_nans_float_widget.reload_data(self,self.dftitle,self.colname)
                        current_index   =   data_cleanse_nans_float_index
                    else :
                        self.cleanse_nonans_float_widget.reload_data(self,self.dftitle,self.colname)
                        current_index   =   data_cleanse_nonans_float_index
                else :
                    if(total_nans > 0) :
                        self.cleanse_nans_int_widget.reload_data(self,self.dftitle,self.colname)
                        current_index   =   data_cleanse_nans_int_index
                    else :
                        self.cleanse_nonans_int_widget.reload_data(self,self.dftitle,self.colname)
                        current_index   =   data_cleanse_nonans_int_index

            elif(formtype == NON_NUMERIC_COLUMN) :

                if(total_nans > 0) :
                    self.cleanse_nans_string_widget.reload_data(self,self.dftitle,self.colname)
                    current_index   =   data_cleanse_nans_string_index
                else :
                    self.cleanse_nonans_string_widget.reload_data(self,self.dftitle,self.colname)
                    current_index   =   data_cleanse_nonans_string_index

            else:

                self.cleanse_category_widget.reload_data(self,self.dftitle,self.colname)
                current_index   =   data_cleanse_category_index


        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_single_column] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,800)
    
    # -----------------------------------------------------------------#
    # -                   display round column                        -#
    # -----------------------------------------------------------------#
    def display_round_column(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_round_column]  : selected dftitle : ",self.dftitle,self.colname))

        data_round_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_ROUND_COLUMN)
        
        if(data_round_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Round_Column_Form_Widget
                parms               =   [self,self.dftitle,self.colname]
                self.round_col      =   DataCleansing_Round_Column_Form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_round_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_ROUND_COLUMN : current_index})
                self.stackedLayout.addWidget(self.round_col)

        else :

            self.round_col.reload_data(self,self.dftitle,self.colname)
            current_index   =   data_round_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_round_column] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,500)

    # -----------------------------------------------------------------#
    # -                 display whitespace column                     -#
    # -----------------------------------------------------------------#

    def display_whitespace_column(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_whitespace_column]  : selected dftitle : ",self.dftitle,self.colname))

        data_whitespace_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_WHITESPACE_COLUMN)
        
        if(data_whitespace_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Remove_Whitespace_Form_Widget
                parms                   =   [self,self.dftitle,self.colname]
                self.whitespace_col     =   DataCleansing_Remove_Whitespace_Form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_whitespace_column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_WHITESPACE_COLUMN : current_index})
                self.stackedLayout.addWidget(self.whitespace_col)

        else :

            self.whitespace_col.reload_data(self,dftitle,colname)
            current_index   =   data_whitespace_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_whitespace_column] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -                 display fillna column                     -#
    # -----------------------------------------------------------------#

    def display_fillna_column(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_fillna_column]  : selected dftitle : ",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)

        from dfcleanser.common.common_utils import is_numeric_col
        if(is_numeric_col(df,colname)) :
            data_fillna_index       =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_FILLNA_COLUMN)
        else :
            data_nn_fillna_index    =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_NN_FILLNA_COLUMN)
        
        if(is_numeric_col(df,colname)) :

            if(data_fillna_index is None) :

                try :

                    from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Fillna_Form_Widget
                    parms                   =   [self,self.dftitle,self.colname]
                    self.fillna_col         =   DataCleansing_Fillna_Form_Widget(parms)

                except Exception as e:

                    opstat.set_status(False)
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[display_fillna_column] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                if(opstat.get_status()) :

                    current_index   =  len(self.DataCleansingWidgets_stack_dict)
                    self.DataCleansingWidgets_stack_dict.update({DISPLAY_FILLNA_COLUMN : current_index})
                    self.stackedLayout.addWidget(self.fillna_col)

            else :

                self.fillna_col.reload_data(self,dftitle,colname)
                current_index   =   data_fillna_index

        else :

            if(data_nn_fillna_index is None) :

                try :

                    from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Non_Numeic_Fillna_Form_Widget
                    parms                   =   [self,self.dftitle,self.colname]
                    self.nn_fillna_col      =   DataCleansing_Non_Numeic_Fillna_Form_Widget(parms)

                except Exception as e:

                    opstat.set_status(False)
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[display_fillna_column] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                if(opstat.get_status()) :

                    current_index   =  len(self.DataCleansingWidgets_stack_dict)
                    self.DataCleansingWidgets_stack_dict.update({DISPLAY_FILLNA_COLUMN : current_index})
                    self.stackedLayout.addWidget(self.nn_fillna_col)

            else :

                self.nn_fillna_col.reload_data(self,dftitle,colname)
                current_index   =   data_nn_fillna_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_fillna_column] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display cleanse columns end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
 

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display cleanse category column                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                 display add new category(s)                   -#
    # -----------------------------------------------------------------#

    def display_add_new_category(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_add_new_category]  : dftitle : colname : ",self.dftitle,self.colname))

        add_new_cat_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_ADD_NEW_CATEGORY)
        
        if(add_new_cat_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Add_Category_Form_Widget
                parms                   =   [self,self.dftitle,self.colname]
                self.add_new_category   =   DataCleansing_Add_Category_Form_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_add_new_category] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_ADD_NEW_CATEGORY : current_index})
                self.stackedLayout.addWidget(self.add_new_category)

        else :

            self.add_new_category.reload_data(self,dftitle,colname)
            current_index   =   add_new_cat_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_remove_category] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -                 display remove category(s)                    -#
    # -----------------------------------------------------------------#

    def display_remove_category(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_remove_category]  : dftitle : colname : ",self.dftitle,self.colname))

        remove_cat_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_REMOVE_CATEGORY)
        
        if(remove_cat_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Remove_Categories_Widget
                parms                   =   [self,self.dftitle,self.colname]
                self.remove_category    =   DataCleansing_Remove_Categories_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_remove_category] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_REMOVE_CATEGORY : current_index})
                self.stackedLayout.addWidget(self.remove_category)

        else :

            self.remove_category(self,dftitle,colname)
            current_index   =   remove_cat_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_remove_category] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -                 display reorder category(s)                   -#
    # -----------------------------------------------------------------#

    def display_reorder_category(self,dftitle,colname):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle    =   dftitle
        self.colname    =   colname

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_reorder_category]  : dftitle : colname : ",self.dftitle,self.colname))

        self.reorder_cat_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_REORDER_CATEGORY)
        
        if(self.reorder_cat_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_Reorder_Categories_Widget
                parms                   =   [self,self.dftitle,self.colname]
                self.reorder_category   =   DataCleansing_Reorder_Categories_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_reorder_category] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_REORDER_CATEGORY : current_index})
                self.stackedLayout.addWidget(self.reorder_category)

        else :

            self.reorder_category.reload_data(self,dftitle,colname)
            current_index   =   self.reorder_cat_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_reorder_category] end : stack \n  ",self.DataCleansingWidgets_stack_dict))

        self.resize(1070,700)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             display cleanse category column end               -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                    display cleanse rows                       -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    
    def display_cleanse_rows(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows]  "))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        dftitle         =   self.df_select.currentText()
        self.working_df =   None

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        active_dfs      =   get_dfc_dataframes_titles_list()

        if( (active_dfs is None) or (not (dftitle in active_dfs))) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_cleanse_rows] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows]  : dftitle : ",dftitle))

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_ROWS)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows]  : data_cleanse_index : ",data_cleanse_index))

        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_cleanse_rows_Widget
                parms               =   [self,dftitle]
                self.cleanse_rows   =   DataCleansing_cleanse_rows_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[Cleanse Rows] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_ROWS : current_index})
                self.stackedLayout.addWidget(self.cleanse_rows)

        else :

            self.cleanse_rows.reload_data(self,dftitle)
            current_index   =   data_cleanse_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,250)


    def display_cleanse_rows_filter_df(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  "))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        if(self.working_df is None) :

            dftitle = self.df_select.currentText()

            from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
            active_dfs      =   get_dfc_dataframes_titles_list()

            if( (active_dfs is None) or (not (dftitle in active_dfs))) :

                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_filter_df] invalid df '" + dftitle + "' selected "
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return()
                
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df                  =   get_dfc_dataframe_df(dftitle)
            self.working_df     =   df.copy(deep=True)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  : dftitle : ",dftitle))

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_ROWS_DF_FILTER )
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  : data_cleanse_index : ",data_cleanse_index))
        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingFilterdfWidgets import DataCleansingdfFiltersColumnWidget
                parms                           =   [self,dftitle]
                self.cleanse_rows_df_filter     =   DataCleansingdfFiltersColumnWidget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_filter_df] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_ROWS_DF_FILTER  : current_index})
                self.stackedLayout.addWidget(self.cleanse_rows_df_filter)

        else :

            self.cleanse_rows_df_filter.reload_data(self,self.working_df)
            current_index   =   data_cleanse_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,750)


    def display_cleanse_rows_criteria(self,working_df_title):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_criteria] working_df_title  : ",working_df_title))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.working_df_title     =   working_df_title

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_ROWS_DF_CRITERIA )
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_criteria]  : data_cleanse_index ",data_cleanse_index))
        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingFilterdfWidgets import DataCleansingdfFiltersCriteriaWidget
                parms                           =   [self,self.working_df_title]
                self.cleanse_rows_df_criteria   =   DataCleansingdfFiltersCriteriaWidget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_criteria] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                current_index   =   None

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_ROWS_DF_CRITERIA  : current_index})
                self.stackedLayout.addWidget(self.cleanse_rows_df_criteria)

        else :

            self.cleanse_rows_df_criteria.reload_data(self,self.working_df_title)
            current_index   =   data_cleanse_index

        if(not (current_index is None)) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_criteria] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,900)



    def display_cleanse_rows_filter_df(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  "))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        if(self.working_df is None) :

            dftitle = self.df_select.currentText()

            from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
            active_dfs      =   get_dfc_dataframes_titles_list()

            if( (active_dfs is None) or (not (dftitle in active_dfs))) :

                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_filter_df] invalid df '" + dftitle + "' selected "
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return()
                
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df                  =   get_dfc_dataframe_df(dftitle)
            self.working_df     =   df.copy(deep=True)

            if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
                add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  : dftitlle : ",dftitle))

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_ROWS_DF_FILTER )
            
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df]  : data_cleanse_index : ",data_cleanse_index))
        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingFilterdfWidgets import DataCleansingdfFiltersColumnWidget
                parms                           =   [self,dftitle]
                self.cleanse_rows_df_filter     =   DataCleansingdfFiltersColumnWidget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_filter_df] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_ROWS_DF_FILTER  : current_index})
                self.stackedLayout.addWidget(self.cleanse_rows_df_filter)

        else :

            self.cleanse_rows_df_filter.reload_data(self,self.working_df)
            current_index   =   data_cleanse_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_filter_df] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,850)


    def display_cleanse_rows_save_df(self,working_df_title):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_save_df]  working_df_title : ",working_df_title))

        self.working_df_title   =   working_df_title

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        data_cleanse_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_CLEANSE_ROWS_DF_SAVE)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_save_df]  : data_cleanse_index ",data_cleanse_index))
        
        if(data_cleanse_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingFilterdfWidgets import DataCleansingdfFiltersProcessdfWidget
                parms                       =   [self,self.working_df_title]
                self.cleanse_rows_df_save   =   DataCleansingdfFiltersProcessdfWidget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_cleanse_rows_save_df] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_CLEANSE_ROWS_DF_SAVE : current_index})
                self.stackedLayout.addWidget(self.cleanse_rows_df_save)

        else :

            self.cleanse_rows_df_save.reload_data(self,self.working_df_title)
            current_index   =   data_cleanse_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows_save_df] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,900)


    def display_drop_duplicates(self,dftitle):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_drop_duplicates]  "))

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        self.dftitle         =   dftitle

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_cleanse_rows]  : dftitlle : ",dftitle))

        drop_duplicates_index  =   self.DataCleansingWidgets_stack_dict.get(DISPLAY_DROP_DUPLICATE_ROWS)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_drop_duplicates]  : data_cleanse_index : ",drop_duplicates_index))

        
        if(drop_duplicates_index is None) :

            try :

                from dfcleanser.Qt.data_cleansing.DataCleansingWidgets import DataCleansing_drop_duplicate_rows_Widget
                parms                       =   [self,dftitle]
                self.drop_duplicate_rows    =   DataCleansing_drop_duplicate_rows_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[Cleanse Rows][display_drop_duplicates] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.DataCleansingWidgets_stack_dict)
                self.DataCleansingWidgets_stack_dict.update({DISPLAY_DROP_DUPLICATE_ROWS : current_index})
                self.stackedLayout.addWidget(self.drop_duplicate_rows)

        else :

            self.drop_duplicate_rows.reload_data(self,dftitle)
            current_index   =   drop_duplicates_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingGui",print_to_string("[display_drop_duplicates] end : stack \n  ",self.DataCleansingWidgets_stack_dict,"\n"))

        self.resize(1070,850)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display cleanse rows end                    -#
    # -----------------------------------------------------------------#
        

 

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to System Chapter                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def clearDataCleansing()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, CLEANSE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(CLEANSE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(CLEANSE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_cleansing_form()

    clear_screen()


def closeDataCleansingInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, CLEANSE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(CLEANSE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(CLEANSE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import DATA_CLEANSING_TITLE
    
    clear_screen()
    logger.info(" Data Cleansing Instances closed")

def showDataCleansing()  :

    from dfcleanser.common.common_utils import clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, CLEANSE_QT_CHAPTER_ID
    
    clear_screen()

    data_cleansing_gui = DataCleansingGui()
    data_cleansing_gui.show()

    dfc_qt_chapters.add_qt_chapter(CLEANSE_QT_CHAPTER_ID,data_cleansing_gui,"showDataCleansing")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(CLEANSE_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Cleansing Instances Loaded")


def closeDataCleansingChapter()  :

    closeDataCleansingInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDataCleansing')","unable to delete data import : ")    


