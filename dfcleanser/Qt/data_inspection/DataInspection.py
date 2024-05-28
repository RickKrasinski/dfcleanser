"""
# DataInspection
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
from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataInspection_ID

from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsIndexTable



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
# -                 Data Inspection subfunctions                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


DFS_SELECT              =   "DataInspection dfsSelect"
DATA_TYPES_FUNCTION     =   "DataInspection DataTypes"
NANS_FUNCTION           =   "DataInspection Nans"
ROWS_FUNCTION           =   "DataInspection Rows"
COLUMNS_FUNCTION        =   "DataInspection Columns"
CATEGORIES_FUNCTION     =   "DataInspection Categories"

DFS_SELECT_ID           =   0
DATA_TYPES_ID           =   1
NANS_ID                 =   2
ROWS_ID                 =   3
COLUMNS_ID              =   4
CATEGORIES_ID           =   5

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection Main Screen                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DATA_INSPECTION_MAIN_GEOMETRY                       =   [0,0,1080,320]

DATA_INSPECTION_MAIN_DATA_TYPES_BUTTON_GEOMETRY     =   [60,10,140,50]
DATA_INSPECTION_MAIN_NANS_BUTTON_GEOMETRY           =   [200,10,140,50]
DATA_INSPECTION_MAIN_ROWS_BUTTON_GEOMETRY           =   [340,10,140,50]
DATA_INSPECTION_MAIN_COLUMNS_BUTTON_GEOMETRY        =   [480,10,140,50]
DATA_INSPECTION_MAIN_CATEGORIES_BUTTON_GEOMETRY     =   [620,10,140,50]
DATA_INSPECTION_MAIN_RESET_BUTTON_GEOMETRY          =   [760,10,140,50]
DATA_INSPECTION_MAIN_HELP_BUTTON_GEOMETRY           =   [900,10,140,50]



DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataInspectionGui(QtWidgets.QMainWindow):

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

        self.dftitle            =   None#"CrimeScenes"
        self.df                 =   None

        self.form               =   None
        self.stackedLayout      =   None

        self.df_select          =   None

        self.data_inspection_widgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

 
        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.dfcDataInspectionMainLayout.addLayout(self.stackedLayout)
        self.form.dfcDataInspectionMainLayout.addStretch()

        self.resize(DATA_INSPECTION_MAIN_GEOMETRY[2],DATA_INSPECTION_MAIN_GEOMETRY[3])

        from dfcleanser.common.cfg import DataInspection_add_df_signal
        DataInspection_add_df_signal.connectSignal(self.add_new_df)



    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_inspection\DataInspectionUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Data Inspection")
        
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
        icon_name   =   dfcdir +"\DataInspectionChapterIcon.png"
        self.app.setWindowIcon(QtGui.QIcon(icon_name))

        # Hide the question mark on dialogs
        self.app.setAttribute(Qt.AA_DisableWindowContextHelpButton) 
        
        # set overall app style
        self.app.setStyle('Fusion')      

        # -----------------------------------------------------#
        #            common window widgets             #
        # -----------------------------------------------------#

        # Status bar
        #self.setStatusBar(QtWidgets.QStatusBar())
        #self.statusBar().setStyleSheet("background-color: #ccffff; font-size: 12px; font-weight: normal; font-family: Arial; margin-left: 0px;")
        #self.statusbar  =   self.statusBar()

        # init the gui form
        self.init_data_inspect_form()

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_inspect_buttons(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("init_data_inspect_buttons]  "))

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.DataTypesbutton, self.form.Nansbutton, self.form.Rowsbutton, self.form.Columnsbutton, 
                         self.form.Categoriesbutton, self.form.InspectResetbutton, self.form.InspectHelpbutton]
        
        # init buttons for usage
        Inspect_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,Inspect_Button_Style)

        # set button styles
        #set_dfc_buttons_style(buttons,Inspect_Button_Style)
        
        # adding action to a button
        self.form.DataTypesbutton.clicked.connect(self.InspectDataTypes)
        self.form.Nansbutton.clicked.connect(self.InspectNans)  
        self.form.Rowsbutton.clicked.connect(self.InspectRows)  
        self.form.Columnsbutton.clicked.connect(self.InspectColumns)
        self.form.Categoriesbutton.clicked.connect(self.InspectCategories)  
        self.form.InspectResetbutton.clicked.connect(self.ResetDataInspect)  
        self.form.InspectHelpbutton.clicked.connect(self.HelpDataInspect)  

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_inspect_splash_screen(self):

        from dfcleanser.common.cfg import DataInspection_ID
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[init_data_inspect_splash_screen]  "))

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import DataInspection_ID
        build_chapter_splash_screen(DataInspection_ID, self.form.DataInspectsplash)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[end init_data_inspect_splash_screen]  "))

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionGui][add_new_df]  df_title",df_title))

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionGui] self.df_select",type(self.df_select),self.df_select.count()))

        self.init_stacked_index()

    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_dfs_to_inspect(self):#, DataInspectionLayout):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[init_dfs_to_inspect]  "))

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_inspect")

        self.dfc_dfs_combo_box  =   dfc_dfs_objects[0]
        dfc_dfs_layout          =   dfc_dfs_objects[1]

        self.df_select          =   self.dfc_dfs_combo_box
        self.dfc_dfs_layout     =   dfc_dfs_layout
 
        from PyQt5.QtWidgets import QWidget
        self.dfc_dfs     =   QWidget()
        self.dfc_dfs.setLayout(self.dfc_dfs_layout)

    def init_stacked_index(self) :   

        dfs_index  =   self.data_inspection_widgets_stack_dict.get(DFS_SELECT)

        if(dfs_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({DFS_SELECT: current_index})
            self.stackedLayout.addWidget(self.dfc_dfs)
        else :
            current_index   =   dfs_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,300)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[init_dfs_to_inspect] end",self.data_inspection_widgets_stack_dict))


    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_inspect_form(self):
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("\n[init_data_inspect_form]  "))

        self.init_data_inspect_buttons()
        self.init_data_inspect_splash_screen()
        self.init_dfs_to_inspect()
        
        self.init_stacked_index()

    def inspect_dfc_dataframe(self,dfc_name) :

        index = self.df_select.findText(dfc_name)
        self.df_select.setCurrentIndex(index) 

        self.InspectRows()       
        
    def get_current_inspect_df_title(self) :

        return(self.df_select.currentText())       
       
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              Data Inspection action methods                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   Inspect df DataTypes                        -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def InspectDataTypes(self):

        #self.form.DataTypesbutton.toggle()
        #self.statusBar().clearMessage()
        
        dftitle     =   self.get_current_inspect_df_title()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECTION")) :
            add_debug_to_log("DataInspection",print_to_string("dftitle",dftitle))

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(dftitle)

        if(df is None) :
                                    
            title       =   "dfcleanser error"       
            status_msg  =   "Invalid dfc dataframe defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectDataTypes]"))
        
        from PyQt5.QtWidgets import QLabel
        dtypes_title_label   =   QLabel()
        dtypes_title_label.setText("\nData Types Data for df '" + dftitle + "'\n")
        dtypes_title_label.setAlignment(Qt.AlignCenter)
        dtypes_title_label.resize(960,50)
        dtypes_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from dfcleanser.Qt.data_inspection.DataInspectionDataTypesTableViews import DataTypesTable
        self.DataTypesStats         =   DataTypesTable([dftitle])
        self.DataTypesStats.doubleClicked.connect(self.select_datatype)

        new_height  =   45 + (self.DataTypesStats.num_rows * DEFAULT_ROW_HEIGHT)

        self.DataTypesStats.setMinimumHeight(new_height)
        self.DataTypesStats.setMaximumHeight(new_height)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_DTYPES")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectDataTypes] DataTypesStats built"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.datatypes     =   QWidget()

        self.datatypesLayout     =   QVBoxLayout()
        self.datatypesLayout.addWidget(dtypes_title_label)
        self.datatypesLayout.addWidget(self.DataTypesStats)
        self.datatypesLayout.addStretch()

        self.datatypes.setLayout(self.datatypesLayout)
 
        data_types_index  =   self.data_inspection_widgets_stack_dict.get(DATA_TYPES_FUNCTION)
        if(data_types_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({DATA_TYPES_FUNCTION : current_index})
            self.stackedLayout.addWidget(self.datatypes)
        else :
            current_index   =   data_types_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_DTYPES")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectDataTypes] end",self.data_inspection_widgets_stack_dict))

        self.resize(1070,450)

    # -----------------------------------------------------------------#
    # -              Data Inspect DataTypes methods                   -#
    # -----------------------------------------------------------------#

    def select_datatype(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_DTYPES")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectDataTypes] select_datatype"))

        for idx in self.DataTypesStats.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_DTYPES")) :
            add_debug_to_log("DataInspection",print_to_string("[handleHistorydoubleclick] : double clicked : row ",row_number))
            add_debug_to_log("DataInspection",print_to_string("[handleHistorydoubleclick] : double clicked : column ",column_number))


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 end Inspect df DataTypes                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                    Inspect df Nans                            -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def InspectNans(self):
        """            
        #------------------------------------------------------------------
        #   Inspect Nans
        #
        #   Parms       -   NA
        #
        #   return      :   NA
        #
        #------------------------------------------------------------------
        """

        self.form.Nansbutton.toggle()
        self.statusBar().clearMessage()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectNans]"))

        self.dftitle = self.df_select.currentText()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("self.df_select.currentText()",self.df_select.currentText()))

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)

        if(df is None) :
                                    
            title       =   "dfcleanser error"       
            status_msg  =   "Invalid dfc dataframe defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)

        # build the overall nan layout
        from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
        from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

        NansLayout      =   QVBoxLayout()

        # build row and column nan stats
        NanStatsLayout  =   QHBoxLayout()

        nans_title_label    =   QLabel()
        nans_title_label.setText("\nNans Data for df '" + self.dftitle + "'\n")
        nans_title_label.setAlignment(Qt.AlignCenter)
        nans_title_label.resize(960,50)
        nans_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
 
        from dfcleanser.Qt.data_inspection.DataInspectionNansTableViews import RowNansTable, ColumnNansTable
        NanRowStats         =   RowNansTable([self.dftitle])
        NanColumnStats      =   ColumnNansTable([self.dftitle])

        new_height  =   30 + (4 * DEFAULT_ROW_HEIGHT)

        NanRowStats.setMinimumHeight(new_height)
        NanRowStats.setMaximumHeight(new_height)
        NanColumnStats.setMinimumHeight(new_height)
        NanColumnStats.setMaximumHeight(new_height)
        
        NanStatsLayout.addWidget(NanRowStats)
        NanStatsLayout.addWidget(NanColumnStats)

        NansLayout.addWidget(nans_title_label)
        NansLayout.addLayout(NanStatsLayout)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("NanRowStats",NanRowStats))
            add_debug_to_log("DataInspection",print_to_string("NanColumnStats",NanColumnStats))

        DropNanStatsLayout  =   QHBoxLayout()

        from dfcleanser.Qt.data_inspection.DataInspectionNansTableViews import DataInspectionDropRowNansTable, DataInspectionDropColsNansTable
        self.DropRowStats         =   DataInspectionDropRowNansTable([self.dftitle])
        self.DropColumnStats      =   DataInspectionDropColsNansTable([self.dftitle])

        DropNanStatsLayout.addWidget( self.DropRowStats )
        DropNanStatsLayout.addWidget(self.DropColumnStats)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("DropRowStats",self.DropRowStats))
            add_debug_to_log("DataInspection",print_to_string("DropColumnStats",self.DropColumnStats))

        NansLayout.addLayout(DropNanStatsLayout)

        # -----------------------------------
        #    Row Nans Drop form 
        # ------------------------------------
        row_nans_input_label    =   QLabel()
        row_nans_input_label.setText(" *Nans Threshold")
        row_nans_input_label.setAlignment(Qt.AlignLeft)
        row_nans_input_label.resize(420,30)
        row_nans_input_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Tahoma; ")

        row_nans_input_text     =   QLineEdit()
        row_nans_input_text.setAlignment(Qt.AlignLeft)
        row_nans_input_text.resize(420,30)
        row_nans_input_text.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Tahoma; ")

        self.row_nans_threshold     =   row_nans_input_text

        RowNansFormLayout  =   QVBoxLayout()
        RowNansFormLayout.addWidget(row_nans_input_label)
        RowNansFormLayout.addWidget(row_nans_input_text)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("RowNansFormLayout",RowNansFormLayout))

        # buttons for row nans
        row_nans_button         =   QPushButton()     
        row_nans_button.setText("Drop Rows with \npct of Cols > \nThreshold")
        row_nans_button.resize(140,90)
        row_nans_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        row_nans_button.clicked.connect(self.drop_pct_of_cols) 
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("row_nans_button",row_nans_button))

        row_nans_button1        =   QPushButton()     
        row_nans_button1.setText("Drop Rows\nwith Nan Count\n> Threshold")
        row_nans_button1.resize(140,90)
        row_nans_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        row_nans_button1.clicked.connect(self.drop_count_of_cols) 
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("row_nans_button1",row_nans_button1))

        row_nans_button2        =   QPushButton()     
        row_nans_button2.setText("\nHelp\n")
        row_nans_button2.resize(140,90)
        row_nans_button2.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        row_nans_button2.clicked.connect(self.drop_row_nans_help) 

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("row_nans_button2",row_nans_button2))

        RowNansbutonsLayout  =   QHBoxLayout()
        RowNansbutonsLayout.addWidget(row_nans_button)
        RowNansbutonsLayout.addWidget(row_nans_button1)
        RowNansbutonsLayout.addWidget(row_nans_button2)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("RowNansbutonsLayout",RowNansbutonsLayout))
        
        RowNansLayout  =   QVBoxLayout()
        RowNansLayout.addLayout(RowNansFormLayout)
        RowNansLayout.addLayout(RowNansbutonsLayout)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("RowNansLayout",RowNansLayout))

        # -----------------------------------
        #    Col Nans Drop form 
        # ------------------------------------
        col_nans_input_label    =   QLabel()
        col_nans_input_label.setText(" *Nans Threshold")
        col_nans_input_label.setAlignment(Qt.AlignLeft)
        col_nans_input_label.resize(420,30)
        col_nans_input_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("col_nans_input_label",col_nans_input_label))

        col_nans_input_text     =   QLineEdit()
        col_nans_input_text.setAlignment(Qt.AlignLeft)
        col_nans_input_text.resize(420,30)
        col_nans_input_text.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Tahoma; ")

        # save for easy access
        self.col_nans_threshold     =   col_nans_input_text

        ColsNansFormLayout  =   QVBoxLayout()
        ColsNansFormLayout.addWidget(col_nans_input_label)
        ColsNansFormLayout.addWidget(col_nans_input_text)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("ColsNansFormLayout",ColsNansFormLayout))

        # buttons for col nans
        col_nans_button         =   QPushButton()     
        col_nans_button.setText("Drop Rows with \npct of Cols > \nThreshold")
        col_nans_button.resize(140,90)
        col_nans_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        col_nans_button.clicked.connect(self.drop_pct_of_rows) 

        col_nans_button1        =   QPushButton()     
        col_nans_button1.setText("Drop Rows\nwith Nan Count\n> Threshold")
        col_nans_button1.resize(140,90)
        col_nans_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        col_nans_button1.clicked.connect(self.drop_count_of_rows) 

        col_nans_button2        =   QPushButton()     
        col_nans_button2.setText("\nHelp\n")
        col_nans_button2.resize(140,90)
        col_nans_button2.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        col_nans_button2.clicked.connect(self.drop_col_nans_help) 

        ColsNansbutonsLayout  =   QHBoxLayout()
        ColsNansbutonsLayout.addWidget(col_nans_button)
        ColsNansbutonsLayout.addWidget(col_nans_button1)
        ColsNansbutonsLayout.addWidget(col_nans_button2)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("ColsNansbutonsLayout",ColsNansbutonsLayout))
        
        ColsNansLayout  =   QVBoxLayout()
        ColsNansLayout.addLayout(ColsNansFormLayout)
        ColsNansLayout.addLayout(ColsNansbutonsLayout)

        DropNansLayout  =   QHBoxLayout()
        DropNansLayout.addLayout(RowNansLayout)
        DropNansLayout.addLayout(ColsNansLayout)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("DropNansLayout",DropNansLayout))

        # build the overall nans layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.nans    =   QWidget()

        self.nansLayout     =   QVBoxLayout()
        self.nansLayout.addLayout(NansLayout)
        self.nansLayout.addLayout(DropNansLayout)
        self.nansLayout.addStretch()

        self.nansLayout.setSpacing(10)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("self.nansLayout",self.nansLayout))

        self.nans.setLayout(self.nansLayout)

        nans_index  =   self.data_inspection_widgets_stack_dict.get(NANS_FUNCTION)
        if(nans_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({NANS_FUNCTION : current_index})
            self.stackedLayout.addWidget(self.nans)
        else :
            current_index   =   nans_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectNans] end",self.data_inspection_widgets_stack_dict))

        self.resize(1070,760)


    # -----------------------------------------------------------------#
    # -               Data Inspect Nans methods                       -#
    # -----------------------------------------------------------------#

    def drop_nan_cols(self,ttype) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        threshold   =   self.row_nans_threshold.text()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_pct_of_cols : threshold ",type(threshold),threshold))

        from dfcleanser.common.common_utils import  opStatus
        opstat = opStatus()

        try :
            threshold   =   float(threshold)
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Drop Nan Rows Threshold value '" + self.row_nans_input_text.text() + "' is invalid")

        if(opstat.get_status()) :

            from dfcleanser.Qt.data_inspection.DataInspectionModel  import  drop_df_nan_rows
            results     =   drop_df_nan_rows(self.df,threshold,ttype,opstat)
            dropcount   =   results[0]
            dflength    =   results[1]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_pct_of_cols : dropcount ",dropcount,dflength,opstat.get_status()))

        if(opstat.get_status()) :
            self.statusBar().showMessage(str(dropcount) + " Nan Rows dropped from df")
        else :
            self.statusBar().showMessage(opstat.get_errorMsg())

    def drop_pct_of_cols(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_pct_of_cols"))

        from dfcleanser.Qt.data_inspection.DataInspectionModel  import  BY_PERCENT
        self.drop_nan_cols(BY_PERCENT)

        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.issue_notice(self.dftitle)

        self.DropRowStats.reload_data()
        self.DropColumnStats.reload_data()

    def drop_count_of_cols(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_count_of_cols"))

        from dfcleanser.Qt.data_inspection.DataInspectionModel  import  BY_COUNT
        self.drop_nan_cols(BY_COUNT)

        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.issue_notice(self.dftitle)

        self.DropRowStats.reload_data()
        self.DropColumnStats.reload_data()


    def drop_row_nans_help(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_row_nans_help"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import INSPECT_ROW_NANS_ID
        display_url(INSPECT_ROW_NANS_ID)

    def drop_rows(self,ttype) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        from dfcleanser.common.common_utils import  opStatus
        opstat = opStatus()

        try :
            threshold   =   float(self.col_nans_threshold.text())
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Drop Nan Cols Threshold value '" + self.col_nans_threshold.text() + "' is invalid")
        
        if(opstat.get_status()) :
            from dfcleanser.Qt.data_inspection.DataInspectionModel  import  drop_df_nan_cols, BY_PERCENT, BY_COUNT 
            dropcount     =   drop_df_nan_cols(self.df,threshold,ttype,opstat)

        if(opstat.get_status()) :
            self.statusBar().showMessage(str(dropcount) + " Nan Columns dropped from df")
        else :
            self.statusBar().showMessage(opstat.get_errorMsg())


    def drop_pct_of_rows(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_pct_of_rows"))
        
        from dfcleanser.Qt.data_inspection.DataInspectionModel  import  BY_PERCENT, BY_COUNT 
        self.drop_rows(BY_PERCENT)

        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.issue_notice(self.dftitle)

        self.DropRowStats.reload_data()
        self.DropColumnStats.reload_data()


    def drop_count_of_rows(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_count_of_rows"))
        
        from dfcleanser.Qt.data_inspection.DataInspectionModel  import  BY_COUNT 
        self.drop_rows(BY_COUNT)
        
        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.issue_notice(self.dftitle)

        self.DropRowStats.reload_data()
        self.DropColumnStats.reload_data()


    def drop_col_nans_help(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspection",print_to_string("drop_cols_nans_help"))
                
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import INSPECT_COL_NANS_ID
        display_url(INSPECT_COL_NANS_ID)
        
    
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  end Inspect df Nans                          -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   inspect df rows                             -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def InspectRows(self):
        
        self.form.Rowsbutton.toggle()
        self.statusBar().clearMessage()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectRows]"))

        self.dftitle = self.df_select.currentText() 

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)

        if(df is None) :
                                    
            title       =   "dfcleanser error"       
            status_msg  =   "Invalid dfc dataframe defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)


        from PyQt5.QtWidgets import QLabel
        rows_title_label   =   QLabel()
        rows_title_label.setText("\nRows Data for df '" + self.dftitle + "'\n")
        rows_title_label.setAlignment(Qt.AlignCenter)
        rows_title_label.resize(400,50)
        rows_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")


        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        rows_button         =   QPushButton()     
        rows_button.setText("Inspect dataframe in dataframe browser")
        rows_button.setFixedSize(400,60)
        rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        rows_button.clicked.connect(self.inspect_in_df_browser) 
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("RowsbutonsLayout",rows_button))
        
        rows_button1        =   QPushButton()     
        rows_button1.setText("Inspect dataframe in Excel")
        rows_button1.setFixedSize(400,60)
        rows_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        rows_button1.clicked.connect(self.inspect_in_excel) 

        from PyQt5.QtWidgets import QVBoxLayout
        RowsbutonsLayout  =   QVBoxLayout()
        RowsbutonsLayout.addWidget(rows_title_label)
        RowsbutonsLayout.setAlignment(rows_title_label,Qt.AlignHCenter)
        RowsbutonsLayout.addWidget(rows_button)
        RowsbutonsLayout.setAlignment(rows_button,Qt.AlignHCenter)
        RowsbutonsLayout.addWidget(rows_button1)
        RowsbutonsLayout.setAlignment(rows_button1,Qt.AlignHCenter)
        RowsbutonsLayout.setAlignment(Qt.AlignVCenter)
        RowsbutonsLayout.addStretch()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("RowsbutonsLayout",RowsbutonsLayout))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QWidget
        self.rows     =   QWidget()

        self.rows.setLayout(RowsbutonsLayout)

        rows_index  =   self.data_inspection_widgets_stack_dict.get(ROWS_FUNCTION)
        if(rows_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({ROWS_FUNCTION : current_index})
            self.stackedLayout.addWidget(self.rows)
            self.stackedLayout.setAlignment(self.rows,Qt.AlignHCenter)       
        else :
            current_index   =   rows_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectRows] end",self.data_inspection_widgets_stack_dict))

        self.resize(1070,440)

    def inspect_in_df_browser(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("inspect_in_df_browser"))

        from dfcleanser.common.common_utils import run_jscript
        script  =   "browse_df_in_df_browser('" + str(self.dftitle) + "');"
        
        run_jscript(script)

    def inspect_in_excel(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_ROWS")) :
            add_debug_to_log("DataInspection",print_to_string("inspect_in_excel"))

        from dfcleanser.common.cfg import get_dfc_dataframe_df, get_dfcleanser_location 
        from dfcleanser.common.common_utils import open_as_excel, alert_user 
   
        df          =   get_dfc_dataframe_df(self.dftitle)

        import os

        tmp_csv_name    =   os.path.join(get_dfcleanser_location(),"files")
        tmp_csv_name    =   os.path.join(tmp_csv_name,"dfc_inspection_working.csv")

        try :
            
            index_columns       =   df.index.names
            
            if(len(index_columns) == 0) :
                df.to_csv(tmp_csv_name, index=False)
            else :
                df.to_csv(tmp_csv_name)
            
            os.startfile(tmp_csv_name)    
    
        except :
            
            alert_user("Unable to open df in excel")


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 end inspect df rows                           -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                    Inspect df Columns                         -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def InspectColumns(self):

        self.form.Columnsbutton.toggle()
        self.statusBar().clearMessage()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_COLUMNS")) :
            add_debug_to_log("DataInspection",print_to_string("\n[InspectColumns] : start"))

        self.dftitle = self.df_select.currentText()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_COLUMNS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectColumns] : dftitle : ",self.dftitle))

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)

        if(df is None) :
                                    
            title       =   "dfcleanser error"       
            status_msg  =   "Invalid dfc dataframe defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)

        from PyQt5.QtWidgets import QLabel
        colsindex_title_label   =   QLabel()
        colsindex_title_label.setText("\nColumn Index for df '" + self.dftitle + "'\n")
        colsindex_title_label.setAlignment(Qt.AlignCenter)
        colsindex_title_label.resize(960,50)
        colsindex_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        
        IndexStats         =   DataInspectionColumnsIndexTable([self.dftitle])
        
        new_height  =   30 + (IndexStats.num_rows * DEFAULT_ROW_HEIGHT)

        IndexStats.setMinimumHeight(new_height)
        IndexStats.setMaximumHeight(new_height)
                
        from PyQt5.QtWidgets import QLabel
        cols_title_label   =   QLabel()
        cols_title_label.setText("\nColumn Stats for df '" + self.dftitle + "'\n")
        cols_title_label.setAlignment(Qt.AlignCenter)
        cols_title_label.resize(960,50)
        cols_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        
        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,15,None]
        self.colsStats      =   DataInspectionColumnsStatsTable(parms)

        from PyQt5.QtWidgets import QLabel
        cols_sel_note   =   QLabel()
        cols_sel_note.setText("* Double Click on column name before displaying graphs\n")
        cols_sel_note.setAlignment(Qt.AlignLeft)
        cols_sel_note.resize(960,50)
        cols_sel_note.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspection_Column_Graphs_Widget
        parms               =   [self,self.dftitle,self.colsStats]
        self.colsGraphs     =   DataInspection_Column_Graphs_Widget(parms)

        # build the overall columns layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.columns     =   QWidget()

        self.columnsLayout     =   QVBoxLayout()
        self.columnsLayout.addWidget(colsindex_title_label)
        self.columnsLayout.addWidget(IndexStats)
        self.columnsLayout.addWidget(cols_title_label)
        self.columnsLayout.addWidget(self.colsStats)
        self.columnsLayout.addWidget(cols_sel_note)
        self.columnsLayout.addWidget(self.colsGraphs)
        self.columnsLayout.addStretch()

        self.columns.setLayout(self.columnsLayout)

        columns_index  =   self.data_inspection_widgets_stack_dict.get(COLUMNS_FUNCTION)

        if(columns_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({COLUMNS_FUNCTION : current_index})
            self.stackedLayout.addWidget(self.columns)
        else :
            current_index   =   columns_index

        self.stackedLayout.setCurrentIndex(current_index)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_COLUMNS")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectColumns] end\n",self.data_inspection_widgets_stack_dict))
        
        self.resize(1070,900)
        

    # -----------------------------------------------------------------#
    # -              Transfoprm Columns Widget methods                -#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 end Inspect df DataTypes                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Inspect df Categories                        -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def InspectCategories(self):
        
        self.form.Categoriesbutton.toggle()
        self.statusBar().clearMessage()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectCategories]"))

        self.dftitle = self.df_select.currentText() 

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)

        if(df is None) :
                                    
            title       =   "dfcleanser error"       
            status_msg  =   "Invalid dfc dataframe defined"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
    
            
        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)
        self.df     =   df

        # build categories columns table
        cols_list   =   self.df.columns.tolist()
        
        cat_col_found   =   False

        from dfcleanser.common.common_utils import is_categorical_col
        for i in range(len(cols_list)) :
            if(is_categorical_col(self.df,cols_list[i])) :
                cat_col_found   =   True
                break
        
        if(cat_col_found) :

            from PyQt5.QtWidgets import QLabel
            catcols_title_label   =   QLabel()
            catcols_title_label.setText("\nCategorical Columns for df '" + self.dftitle + "'\n")
            catcols_title_label.setAlignment(Qt.AlignCenter)
            catcols_title_label.resize(960,50)
            catcols_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

            from dfcleanser.Qt.data_inspection.DataInspectionCategoriesTableViews import DataInspectionCategoriesTable
            CatColumns        =   DataInspectionCategoriesTable([self.dftitle])

            if(CatColumns.num_rows < 25) :
                new_height  =   45 + (CatColumns.num_rows * DEFAULT_ROW_HEIGHT)
            else :
                new_height  =   45 + (25 * DEFAULT_ROW_HEIGHT)

            CatColumns.setMinimumHeight(new_height)
            CatColumns.setMaximumHeight(new_height)
        
            if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
                add_debug_to_log("DataInspection",print_to_string("[InspectCategories] : CatColumns height ",new_height))


        # build cat candidates table:
        from PyQt5.QtWidgets import QLabel
        catcandcols_title_label   =   QLabel()
        catcandcols_title_label.setText("\nCategorical Candidate Columns for df '" + self.dftitle + "'\n")
        catcandcols_title_label.setAlignment(Qt.AlignCenter)
        catcandcols_title_label.resize(960,50)
        catcandcols_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from dfcleanser.Qt.data_inspection.DataInspectionCategoriesTableViews import DataInspectionCategoryCandidatesTable
        CatCandidateColumns        =   DataInspectionCategoryCandidatesTable([self.dftitle])

        if(CatCandidateColumns.num_rows < 25) :
            new_height  =   45 + (CatCandidateColumns.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (25 * DEFAULT_ROW_HEIGHT)

        CatCandidateColumns.setMinimumHeight(new_height)
        CatCandidateColumns.setMaximumHeight(new_height)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectCategories] : CatCandidateColumns height ",new_height))

        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.categories         =   QWidget()
        self.categoriesLayout   =   QVBoxLayout()

        if(cat_col_found) :

            self.categoriesLayout.addWidget(catcols_title_label)
            self.categoriesLayout.addWidget(CatColumns)

        self.categoriesLayout.addWidget(catcandcols_title_label)
        self.categoriesLayout.addWidget(CatCandidateColumns)
        self.categoriesLayout.addStretch()

        self.categories.setLayout(self.categoriesLayout)

        categories_index  =   self.data_inspection_widgets_stack_dict.get(CATEGORIES_FUNCTION)
        if(categories_index is None) :
            current_index   =  len(self.data_inspection_widgets_stack_dict)
            self.data_inspection_widgets_stack_dict.update({CATEGORIES_FUNCTION: current_index})
            self.stackedLayout.addWidget(self.categories)
        else :
            current_index   =   categories_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT")) :
            add_debug_to_log("DataInspection",print_to_string("[InspectCategories] end",self.data_inspection_widgets_stack_dict))

        self.resize(1048,800)
    
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 Inspect df Categories end                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                 Reset Data Inspection                         -#
    # -----------------------------------------------------------------#
    def ResetDataInspect(self):
        
        self.form.InspectResetbutton.toggle()
        self.statusBar().clearMessage() 

        self.init_stacked_index()

    # -----------------------------------------------------------------#
    # -                 Data Inspection Help                          -#
    # -----------------------------------------------------------------#
    def HelpDataInspect(self):

        self.form.InspectHelpbutton.toggle()
        add_debug_to_log("DataInspection",print_to_string("HelpDataInspect"))
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import INSPECT_MAIN_TASKBAR_ID
        display_url(INSPECT_MAIN_TASKBAR_ID)

        #from dfcleanser.common.common_utils import display_url
        #display_url("https://rickkrasinski.github.io/dfcleanser-help/dfcleanser-data-inspection.html")



      
# -----------------------------------------------------------------#
# -                Global access to display uniques               -#
# -----------------------------------------------------------------#
def clearDataInspection()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, INSPECTION_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(INSPECTION_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(INSPECTION_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_inspect_form()

    clear_screen()

def closeDataInspectionInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, INSPECTION_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(INSPECTION_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(INSPECTION_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    logger.info(" Data Inspection Instances closed")


def showDataInspection()  :

    from dfcleanser.common.common_utils import clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, INSPECTION_QT_CHAPTER_ID, DATA_INSPECTION_TITLE
    
    clear_screen()

    data_inspection_gui = DataInspectionGui()
    data_inspection_gui.show()

    dfc_qt_chapters.add_qt_chapter(INSPECTION_QT_CHAPTER_ID,data_inspection_gui,"showDataInspection")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(INSPECTION_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Inspection Instances Loaded")



def closeDataInspectionChapter()  :

    closeDataInspectionInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDataInspection')","unable to delete data Inspection : ")    

         
 
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column uniques qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def browseDataframe(df_name)  :


    from dfcleanser.common.cfg import get_dfc_dataframe_df
    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
    
    df  =  get_dfc_dataframe_df(df_name) 
    
    if(df is None) :

        title   =   "dfcleanser browse dataframe"
        msg     =   "dataframe " + df_name + " is not defined"
        display_error_msg(title,msg)
        return()

    else :

        if(len(df) == 0) :

            title   =   "dfcleanser browse dataframe"
            msg     =   "dataframe " +  df_name + " has no data"
            display_error_msg(title,msg)
            return()

    from dfcleanser.common.common_utils import clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, INSPECTION_QT_CHAPTER_ID, DATA_INSPECTION_TITLE
    
    clear_screen()

    data_inspection_gui = DataInspectionGui()
    data_inspection_gui.show()

    data_inspection_gui.inspect_dfc_dataframe(df_name)

    dfc_qt_chapters.add_qt_chapter(INSPECTION_QT_CHAPTER_ID,data_inspection_gui,"showDataInspection")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(INSPECTION_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Inspection Instances Loaded")








