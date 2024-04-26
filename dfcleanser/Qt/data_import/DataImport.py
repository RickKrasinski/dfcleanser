"""
# DataImport
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

DEBUG_DATA_IMPORT               =   True
DEBUG_DATA_IMPORT_HISTORIES     =   False
DEBUG_DATA_IMPORT_FILE_TYPE     =   False
DEBUG_DATA_IMPORT_DETAILS       =   False
DEBUG_DATA_IMPORT_FORMS         =   False
DEBUG_DATA_IMPORT_COMMECTORS    =   False

DEBUG_DATA_IMPORT_CSV           =   False
DEBUG_DATA_IMPORT_FWF           =   False
DEBUG_DATA_IMPORT_EXCEL         =   False
DEBUG_DATA_IMPORT_JSON          =   False
DEBUG_DATA_IMPORT_XML           =   False
DEBUG_DATA_IMPORT_PDF           =   False
DEBUG_DATA_IMPORT_HTML          =   False
DEBUG_DATA_IMPORT_SQLTABLE      =   False
DEBUG_DATA_IMPORT_SQLQUERY      =   False
DEBUG_DATA_IMPORT_CUSTOM        =   False


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


IMPORT_TYPE_HISTORIES                   =   "DataImport dfsImported"

IMPORT_CVS_FILE_TYPE_HISTORIES          =   "DataImport cvs filetypes Imported"
IMPORT_FWF_FILE_TYPE_HISTORIES          =   "DataImport fwf filetypes Imported"
IMPORT_EXCEL_FILE_TYPE_HISTORIES        =   "DataImport excel filetypes Imported"
IMPORT_JSON_FILE_TYPE_HISTORIES         =   "DataImport json filetypes Imported"
IMPORT_XML_FILE_TYPE_HISTORIES          =   "DataImport xml filetypes Imported"
IMPORT_PDF_FILE_TYPE_HISTORIES          =   "DataImport pdf filetypes Imported"
IMPORT_HTML_FILE_TYPE_HISTORIES         =   "DataImport html filetypes Imported"
IMPORT_SQLTABLE_FILE_TYPE_HISTORIES     =   "DataImport sqltable filetypes Imported"
IMPORT_SQLQUERY_FILE_TYPE_HISTORIES     =   "DataImport sqlquery filetypes Imported"
IMPORT_CUSTOM_FILE_TYPE_HISTORIES       =   "DataImport custom filetypes Imported"

EXPORT_CVS_FILE_TYPE_HISTORIES          =   "DataExport cvs filetypes Exported"
EXPORT_EXCEL_FILE_TYPE_HISTORIES        =   "DataExport excel filetypes Exported"
EXPORT_JSON_FILE_TYPE_HISTORIES         =   "DataExport json filetypes Exported"
EXPORT_XML_FILE_TYPE_HISTORIES          =   "DataExport xml filetypes Exported"
EXPORT_PDF_FILE_TYPE_HISTORIES          =   "DataExport pdf filetypes Exported"
EXPORT_HTML_FILE_TYPE_HISTORIES         =   "DataExport html filetypes Exported"
EXPORT_SQLTABLE_FILE_TYPE_HISTORIES     =   "DataExport sqltable filetypes Exported"
EXPORT_CUSTOM_FILE_TYPE_HISTORIES       =   "DataExport custom filetypes Exported"


EXPORT_FILE_TYPE_HISTORIES              =   "DataImport filetypes Exported"
IMPORT_WITH_PARMS                       =   "DataImport with parms"
IMPORT_STATUS                           =   "DataImport status"

EXPORT_WITH_PARMS                       =   "DataImport export parms"
IMPORT_FILE_FORM                        =   "DataImport import file form"


IMPORT_CSV_FORM                       =   "DataImport CSVFile"
IMPORT_FWF_FORM                       =   "DataImport FWFFile"
IMPORT_EXCEL_FORM                     =   "DataImport ExcelFile"
IMPORT_JSON_FORM                      =   "DataImport JSONFile"
IMPORT_XML_FORM                       =   "DataImport XMLFile"
IMPORT_PDF_FORM                       =   "DataImport PDFFile"
IMPORT_HTML_FORM                      =   "DataImport HTMLFile"
IMPORT_HTML_DFS_FORM                  =   "DataImport HTMLFile dfs"
IMPORT_HTML_DF_SAVE_FORM              =   "DataImport HTMLFile save df"
IMPORT_SQLTABLE_FORM                  =   "DataImport SQLTable"
IMPORT_SQLQUERY_FORM                  =   "DataImport SLQQuery"
IMPORT_CUSTOM_FORM                    =   "DataImport Custom"

IMPORT_DBCONNECTORS_TABLE             =   "DataImport DBConnectors Table"
IMPORT_DBCONNECTORS_CREATE_FORM       =   "DataImport DBConnectors Create Form"
IMPORT_DBCONNECTORS_EDIT_FORM         =   "DataImport DBConnectors Edit Form"

EXPORT_DBCONNECTORS_TABLE             =   "DataExport DBConnectors Table"


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  DataImport Main Screen                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DATA_IMPORT_MAIN_GEOMETRY                           =   [0,0,1080,1000]


DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Data Import main GUI                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataImportGui(QtWidgets.QMainWindow):

    #def __init__(self):
    def __init__(self, **kwargs):  

        # Enables PyQt event loop in IPython
        #fix_ipython()  

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

        self.DataImportWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)
        

        self.init_gui()

        self.form.dfcDataImportMainLayout.addLayout(self.stackedLayout)
        self.form.dfcDataImportMainLayout.addStretch()

        #self.form.ClockLabel     =   self.Import_Clock.get_clockface_widget()
        #self.form.ClockLabel.show()


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_import\DataImportUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Data Import")
        
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
        icon_name   =   dfcdir +"\DataImportChapterIcon.png"
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
        self.statusbar  =   self.statusBar()
        
        # init the gui form
        self.init_data_import_form()

           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_import_buttons(self):

        if(DEBUG_DATA_IMPORT) :
            print("[init_data_inspect_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.CSVbutton, self.form.FWFbutton, self.form.Excelbutton, self.form.JSONbutton, self.form.XMLbutton,
                         self.form.HTMLbutton, self.form.SQLTablebutton, self.form.SQLQuerybutton, self.form.Custombutton, 
                         self.form.ImportResetbutton, self.form.ImportHelpbutton]
        
        callbacks   =   [self.ImportCSVFile, self.ImportFWFFile, self.ImportExcelFile, self.ImportJSONFile, self.ImportXMLFile,
                         self.ImportHTMLFile, self.ImportSQLTable, self.ImportSQLQuery, self.ImportCustom, 
                         self.ResetDataImport, self.HelpDataImport]
    
        # init buttons for usage
        Import_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,Import_Button_Style)

        # set button styles
        
        #set_dfc_buttons_style(buttons,Import_Button_Style)
        
        # adding action to a button
        for i in range(len(buttons)) :
            buttons[i].clicked.connect(callbacks[i])


    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_import_splash_screen(self):

        if(DEBUG_DATA_IMPORT) :
            print("[init_data_inspect_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import DataImport_ID
        build_chapter_splash_screen(DataImport_ID, self.form.DataImportsplash)

        if(DEBUG_DATA_IMPORT) :
            print("[end init_data_import_splash_screen]  ")

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_import_clock(self):

        if(DEBUG_DATA_IMPORT) :
            print("[init_data_import_clock]  ")

        from dfcleanser.common.common_utils import RunningClock
        self.Import_Clock        =   RunningClock(self.form.ClockLabel)

        from PyQt5.QtGui import QImage, QPixmap
        from dfcleanser.common.common_utils import get_clock_image_file_name
        image   =   QImage(get_clock_image_file_name(0))
        pixmap  =   QPixmap.fromImage(image)
        
        self.form.ClockLabel.setPixmap(pixmap)
        self.Import_Clock.get_clockface_widget().show()

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_import_form(self):
        
        if(DEBUG_DATA_IMPORT) :
            print("[init_data_import_form]  ")

        self.init_data_import_buttons()
        self.init_data_import_splash_screen()
        self.init_data_import_clock()
        self.display_import_histories()

        self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               Main Gui Data Import Methods                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                      Import CSV File                          -#
    # -----------------------------------------------------------------#
    def ImportCSVFile(self) :

        self.form.CSVbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportCSVFile]")

        from dfcleanser.Qt.data_import.DataImportModel import CSV_IMPORT, pandas_import_csv_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   CSV_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_csv_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)


    # -----------------------------------------------------------------#
    # -                      Import FWF File                          -#
    # -----------------------------------------------------------------#
    def ImportFWFFile(self) :

        self.form.FWFbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportFWFFile]")

        from dfcleanser.Qt.data_import.DataImportModel import FWF_IMPORT, pandas_import_fwf_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   FWF_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_fwf_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)
       

    # -----------------------------------------------------------------#
    # -                     Import Excel File                         -#
    # -----------------------------------------------------------------#
    def ImportExcelFile(self) :

        self.form.Excelbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportExcelFile]")

        from dfcleanser.Qt.data_import.DataImportModel import EXCEL_IMPORT, pandas_import_excel_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   EXCEL_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_excel_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)


    # -----------------------------------------------------------------#
    # -                      Import JSON File                         -#
    # -----------------------------------------------------------------#
    def ImportJSONFile(self) :

        self.form.JSONbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportFWFFile]")

        from dfcleanser.Qt.data_import.DataImportModel import JSON_IMPORT, pandas_import_json_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   JSON_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_json_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)
        

    # -----------------------------------------------------------------#
    # -                      Import XML File                          -#
    # -----------------------------------------------------------------#
    def ImportXMLFile(self) :

        self.form.XMLbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportXMLFile]")

        from dfcleanser.Qt.data_import.DataImportModel import XML_IMPORT, pandas_import_xml_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   XML_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_xml_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)

    # -----------------------------------------------------------------#
    # -                      Import HTML File                         -#
    # -----------------------------------------------------------------#
    def ImportHTMLFile(self) :

        self.form.HTMLbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportExcelFile]")

        from dfcleanser.Qt.data_import.DataImportModel import HTML_IMPORT, pandas_import_html_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   HTML_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(pandas_import_html_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)


    # -----------------------------------------------------------------#
    # -                    Import via SQLTable                       -#
    # -----------------------------------------------------------------#
    def ImportSQLTable(self) :

        self.form.SQLTablebutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportSQLTable]")
       
        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT, pandas_import_sqltable_common_id
        self.import_with_filetype       =   SQLTABLE_IMPORT

        from dfcleanser.common.cfg import get_config_value
        import_file_form_cfg_parms     =   get_config_value(pandas_import_sqltable_common_id+"Parms")
        
        if(DEBUG_DATA_IMPORT) :
            print("[ImportSQLTable] cfg parms : ",import_file_form_cfg_parms)

        if(import_file_form_cfg_parms is None) :

            from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
            dftitles_list   =   ImportHistory.get_df_titles_for_file_type(SQLTABLE_IMPORT) 
            if(len(dftitles_list) > 0) :    
                self.import_with_dftitle        =   dftitles_list[0]
            else :
                self.import_with_dftitle        =   "No dfs Imported"                

        else :

            self.import_with_dftitle        =   import_file_form_cfg_parms[0]            

        dconntblparms   =   [0,self.import_with_db_connector]
        self.display_dbconnector_table(dconntblparms)


    # -----------------------------------------------------------------#
    # -                    Import via SQLQuery                        -#
    # -----------------------------------------------------------------#
    def ImportSQLQuery(self) :

        self.form.SQLQuerybutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportSQLQuery]")


        from dfcleanser.Qt.data_import.DataImportModel import SQLQUERY_IMPORT, pandas_import_sqlquery_id
        self.import_with_filetype       =   SQLQUERY_IMPORT

        from dfcleanser.common.cfg import get_config_value
        import_file_form_cfg_parms     =   get_config_value(pandas_import_sqlquery_id+"Parms")
        
        if(DEBUG_DATA_IMPORT) :
            print("[ImportSQLQuery] cfg parms : ",import_file_form_cfg_parms)

        if(import_file_form_cfg_parms is None) :

            from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
            dftitles_list   =   ImportHistory.get_df_titles_for_file_type(SQLQUERY_IMPORT) 
            if(len(dftitles_list) > 0) :
                self.import_with_dftitle        =   dftitles_list[0]
            else :
                self.import_with_dftitle        =   "No dfs Imported"

        else :

            self.import_with_dftitle        =   import_file_form_cfg_parms[0]            

        dconntblparms   =   [0,self.import_with_db_connector]
        self.display_dbconnector_table(dconntblparms)

    # -----------------------------------------------------------------#
    # -                     Import Custom                             -#
    # -----------------------------------------------------------------#
    def ImportCustom(self) :

        self.form.Custombutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("[ImportCustom]")

        from dfcleanser.Qt.data_import.DataImportModel import CUSTOM_IMPORT, custom_import_id
        from dfcleanser.common.cfg import get_config_value

        import_file_form_file_type     =   CUSTOM_IMPORT
        import_file_form_dftitle       =   None
        import_file_form_cfg_parms     =   get_config_value(custom_import_id+"Parms")

        importParms    =   [import_file_form_file_type,import_file_form_dftitle,import_file_form_cfg_parms]
        
        self.display_import_form(importParms)

    
    # -----------------------------------------------------------------#
    # -                   Reset Data Import                           -#
    # -----------------------------------------------------------------#
    def ResetDataImport(self):
        
        self.form.ImportResetbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("ResetDataImport")

        self.display_import_histories()
        

    # -----------------------------------------------------------------#
    # -                 Data Inspection Help                          -#
    # -----------------------------------------------------------------#
    def HelpDataImport(self):

        self.form.ImportHelpbutton.toggle()

        if(DEBUG_DATA_IMPORT) :
            print("HelpDataImport")

        from dfcleanser.common.common_utils import display_url
        display_url("https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-data-import.html")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Data Import main GUI end                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#





    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 Data Import display methods                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display data import histories                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_histories(self):

        if(DEBUG_DATA_IMPORT_HISTORIES) :
            print("\n[display_import_histories]  ")

        import_history_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_TYPE_HISTORIES)
        
        if(import_history_index is None) :

            from dfcleanser.Qt.data_import.DataImportWidgets import Data_Import_Histories_Widget
            self.import_histories   =   Data_Import_Histories_Widget([self.select_import_type_history,self.select_export_type_history])

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({IMPORT_TYPE_HISTORIES : current_index})
            self.stackedLayout.addWidget(self.import_histories)

        else :

            self.import_histories.reload_data()
            current_index   =   import_history_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT_HISTORIES) :
            print("[display_import_histories] end : stack \n  ",self.DataImportWidgets_stack_dict_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -            display data import histories methods              -#
    # -----------------------------------------------------------------#
    def select_import_type_history(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        for idx in self.import_histories.importHistory.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()

        if(DEBUG_DATA_IMPORT_HISTORIES) :
            print("[display_import_histories][select_import_type_history]",row_number,column_number)

        model   =   self.import_histories.importHistory.model
        tdata   =   model.get_data()

        if(column_number == 0) :
            if(not (tdata[row_number][1] == 0) ) :
                self.display_import_file_type_histories(row_number)            


    def select_export_type_history(self) :
        """            
        #------------------------------------------------------------------
        #   drop nans in columns
        #
        #   Parms       -   ttype type of drop
        #
        #------------------------------------------------------------------
        """

        for idx in self.import_histories.exportHistory.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()

        if(DEBUG_DATA_IMPORT_HISTORIES) :
            print("[display_import_histories] select_export_type_history",row_number,column_number)

        model   =   self.import_histories.exportHistory.model
        tdata   =   model.get_data()

        if(column_number == 0) :
            if(not (tdata[row_number][1] == 0) ) :
                self.display_export_file_type_histories(row_number)            


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             display data import histories end                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -           display data import file type histories             -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_file_type_histories(self, filetype):

        if(DEBUG_DATA_IMPORT) :
            print("\n[display_import_file_type_histories]", filetype)

        self.import_file_type   =   filetype

        import dfcleanser.Qt.data_import.DataImportModel as DIM
        if(self.import_file_type == DIM.CSV_IMPORT) :
            layout_index    =   IMPORT_CVS_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.FWF_IMPORT) :
            layout_index    =   IMPORT_FWF_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.EXCEL_IMPORT) :
            layout_index    =   IMPORT_EXCEL_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.JSON_IMPORT) :
            layout_index    =   IMPORT_JSON_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.XML_IMPORT) :
            layout_index    =   IMPORT_XML_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.PDF_IMPORT) :
            layout_index    =   IMPORT_PDF_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.HTML_IMPORT) :
            layout_index    =   IMPORT_HTML_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.SQLTABLE_IMPORT) :
            layout_index    =   IMPORT_SQLTABLE_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.SQLQUERY_IMPORT) :
            layout_index    =   IMPORT_SQLQUERY_FILE_TYPE_HISTORIES
        elif(self.import_file_type == DIM.CUSTOM_IMPORT) :
            layout_index    =   IMPORT_CUSTOM_FILE_TYPE_HISTORIES

        file_types_index  =   self.DataImportWidgets_stack_dict.get(layout_index)

        if(file_types_index is None) :

            filetypehistoriesParms  =   [self.import_file_type,self.select_import_df_title,self.delete_import_histories,self.return_from_file_types] 
            from dfcleanser.Qt.data_import.DataImportWidgets import Data_Import_File_Type_Histories_Widget

            if(self.import_file_type == DIM.CSV_IMPORT) :
                self.data_import_csv_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_csv_file_type_history
            elif(self.import_file_type == DIM.FWF_IMPORT) :
                self.data_import_fwf_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_fwf_file_type_history
            elif(self.import_file_type == DIM.EXCEL_IMPORT) :
                self.data_import_excel_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_excel_file_type_history
            elif(self.import_file_type == DIM.JSON_IMPORT) :
                self.data_import_json_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_json_file_type_history
            elif(self.import_file_type == DIM.XML_IMPORT) :
                self.data_import_xml_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_xml_file_type_history
            elif(self.import_file_type == DIM.PDF_IMPORT) :
                self.data_import_pdf_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_pdf_file_type_history
            elif(self.import_file_type == DIM.HTML_IMPORT) :
                self.data_import_html_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_html_file_type_history
            elif(self.import_file_type == DIM.SQLTABLE_IMPORT) :
                self.data_import_sqltable_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_sqltable_file_type_history
            elif(self.import_file_type == DIM.SQLQUERY_IMPORT) :
                self.data_import_sqlquery_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_sqlquery_file_type_history
            elif(self.import_file_type == DIM.CUSTOM_IMPORT) :
                self.data_import_custom_file_type_history  =   Data_Import_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_import_file_type_history      =   self.data_import_custom_file_type_history

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({layout_index : current_index})

            if(self.import_file_type == DIM.CSV_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_csv_file_type_history)
            elif(self.import_file_type == DIM.FWF_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_fwf_file_type_history)
            elif(self.import_file_type == DIM.EXCEL_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_excel_file_type_history)
            elif(self.import_file_type == DIM.JSON_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_json_file_type_history)
            elif(self.import_file_type == DIM.XML_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_xml_file_type_history)
            elif(self.import_file_type == DIM.PDF_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_pdf_file_type_history)
            elif(self.import_file_type == DIM.HTML_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_html_file_type_history)
            elif(self.import_file_type == DIM.SQLTABLE_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_sqltable_file_type_history)
            elif(self.import_file_type == DIM.SQLQUERY_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_sqlquery_file_type_history)
            elif(self.import_file_type == DIM.CUSTOM_IMPORT) :
                self.stackedLayout.addWidget(self.data_import_custom_file_type_history)

        else :

            if(self.import_file_type == DIM.CSV_IMPORT) :
                self.data_import_csv_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_csv_file_type_history
            elif(self.import_file_type == DIM.FWF_IMPORT) :
                self.data_import_fwf_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_fwf_file_type_history
            elif(self.import_file_type == DIM.EXCEL_IMPORT) :
                self.data_import_excel_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_excel_file_type_history
            elif(self.import_file_type == DIM.JSON_IMPORT) :
                self.data_import_json_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_json_file_type_history
            elif(self.import_file_type == DIM.XML_IMPORT) :
                self.data_import_xml_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_xml_file_type_history
            elif(self.import_file_type == DIM.PDF_IMPORT) :
                self.data_import_pdf_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_pdf_file_type_history
            elif(self.import_file_type == DIM.HTML_IMPORT) :
                self.data_import_html_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_html_file_type_history
            elif(self.import_file_type == DIM.SQLTABLE_IMPORT) :
                self.data_import_sqltable_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_sqltable_file_type_history
            elif(self.import_file_type == DIM.SQLQUERY_IMPORT) :
                self.data_import_sqlquery_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_sqlquery_file_type_history
            elif(self.import_file_type == DIM.CUSTOM_IMPORT) :
                self.data_import_custom_file_type_history.reload_data()
                self.data_import_file_type_history      =   self.data_import_custom_file_type_history

            current_index   =   file_types_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ImportFileTypeHistory] end",self.DataImportWidgets_stack_dict)

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -       display data import file type histories methods         -#
    # -----------------------------------------------------------------#
    def select_import_df_title(self) :
        """            
        #------------------------------------------------------------------
        #   select a df to delete or import with
        #------------------------------------------------------------------
        """

        for idx in self.data_import_file_type_history.importfiletypehistory.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ImportFileTypeHistory] select_import_df_title",row_number,column_number)

        model   =   self.data_import_file_type_history.importfiletypehistory.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :    
            print("[ImportFileTypeHistory] select_import_df_title : cell value [",cell,"]")

        if(column_number == 0) :
            if(cell == " ") :
                tdata[row_number][column_number] = "X" 
            else :
                tdata[row_number][column_number] = " "      

            model.reload_data(tdata)

        elif(column_number == 1):

            if(not (tdata[row_number][2] == 0)) :
                self.display_import_with_parms(self.import_file_type,cell)
        

    def return_from_file_types(self) :
        """            
        #------------------------------------------------------------------
        #   return from data import file type history
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ImportFileTypeHistory] return_from_file_types")

        self.display_import_histories()


    def delete_import_histories(self) :
        """            
        #------------------------------------------------------------------
        #   delete selected import histories
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ImportFileTypeHistory] delete_import_histories")

        model   =   self.data_import_file_type_history.importfiletypehistory.model
        tdata   =   model.get_data()

        delete_list     =   []

        for i in range(len(tdata)) :
            check_value     =   tdata[i][0]
            if(not (check_value == " ")) :
                delete_list.append(tdata[i][1])

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ImportFileTypeHistory] delete_list",delete_list)
        
        if(len(delete_list) > 0) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Verify import File history Delete")
            dlg.setText("Do you want to delete historie(s)")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlg.exec()

            if(button == QMessageBox.Yes) :

                from dfcleanser.Qt.data_import.DataImportModel import ImportHistory

                for i in range(len(delete_list)) :
                    ImportHistory.delete_from_history(self.import_file_type,delete_list[i])

                from PyQt5.QtWidgets import QMessageBox
                dlga = QMessageBox(self)
                dlga.setWindowTitle("Delete Import File history Status")
                dlga.setText("Selected Import Histories Deleted")
                dlga.setStandardButtons(QMessageBox.Ok)
                dlga.setStyleSheet("QLabel{min-width: 300px;}");
                button = dlga.exec()

        else :

            from PyQt5.QtWidgets import QMessageBox
            dlgc = QMessageBox(self)
            dlgc.setWindowTitle("Delete Import File history Status")
            dlgc.setText("No historie(s) selected to delete.")
            dlgc.setStandardButtons(QMessageBox.Ok)
            dlgc.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlgc.exec()



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -        display data import file type histories end            -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -           display data export file type histories             -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_file_type_histories(self, filetype):

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("\n[display_export_file_type_histories] : filetype", filetype)

        self.export_file_type   =   filetype

        import dfcleanser.Qt.data_export.DataExportModel as dem
        if(self.export_file_type == dem.CSV_EXPORT) :
            layout_index    =   EXPORT_CVS_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.EXCEL_EXPORT) :
            layout_index    =   EXPORT_EXCEL_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.JSON_EXPORT) :
            layout_index    =   EXPORT_JSON_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.HTML_EXPORT) :
            layout_index    =   EXPORT_HTML_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.SQLTABLE_EXPORT) :
            layout_index    =   EXPORT_SQLTABLE_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.CUSTOM_EXPORT) :
            layout_index    =   EXPORT_CUSTOM_FILE_TYPE_HISTORIES
        elif(self.export_file_type == dem.XML_EXPORT) :
            layout_index    =   EXPORT_XML_FILE_TYPE_HISTORIES

        file_types_index  =   self.DataImportWidgets_stack_dict.get(layout_index)

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[display_export_file_type_histories] : layout_index : file_types_index",layout_index,file_types_index)

        if(file_types_index is None) :

            filetypehistoriesParms  =   [self.export_file_type,self.select_export_df_title,self.delete_export_histories,self.return_from_export_file_types] 
            from dfcleanser.Qt.data_import.DataImportWidgets import Data_Export_File_Type_Histories_Widget

            if(self.export_file_type == dem.CSV_EXPORT) :
                self.data_export_csv_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_csv_file_type_history
            elif(self.export_file_type == dem.EXCEL_EXPORT) :
                self.data_export_excel_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_excel_file_type_history
            elif(self.export_file_type == dem.JSON_EXPORT) :
                self.data_export_json_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_json_file_type_history
            elif(self.export_file_type == dem.HTML_EXPORT) :
                self.data_export_html_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_html_file_type_history
            elif(self.export_file_type == dem.SQLTABLE_EXPORT) :
                self.data_export_sqltable_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_sqltable_file_type_history
            elif(self.export_file_type == dem.CUSTOM_EXPORT) :
                self.data_export_custom_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_custom_file_type_history
            elif(self.export_file_type == dem.XML_EXPORT) :
                self.data_export_xml_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_xml_file_type_history

            if(DEBUG_DATA_IMPORT_FILE_TYPE) :
                print("[display_export_file_type_histories] : current_index",len(self.DataImportWidgets_stack_dict))

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({layout_index : current_index})
            self.stackedLayout.addWidget(self.data_export_file_type_history)
            
        else :

            if(self.export_file_type == dem.CSV_EXPORT) :
                self.data_export_csv_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_csv_file_type_history
            elif(self.export_file_type == dem.EXCEL_EXPORT) :
                self.data_export_excel_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_excel_file_type_history
            elif(self.export_file_type == dem.JSON_EXPORT) :
                self.data_export_json_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_json_file_type_history
            elif(self.export_file_type == dem.HTML_EXPORT) :
                self.data_export_html_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_html_file_type_history
            elif(self.export_file_type == dem.SQLTABLE_EXPORT) :
                self.data_export_sqltable_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_sqltable_file_type_history
            elif(self.export_file_type == dem.CUSTOM_EXPORT) :
                self.data_export_custom_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_custom_file_type_history
            elif(self.export_file_type == dem.XML_EXPORT) :
                self.data_export_xml_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_xml_file_type_history

            current_index   =   file_types_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[display_export_file_type_histories] end : stack :\n  ",self.DataImportWidgets_stack_dict)

        self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -     display data export file type histories  methods          -#
    # -----------------------------------------------------------------#
    
    def select_export_df_title(self) :
        """            
        #------------------------------------------------------------------
        #   select a df to delete or import with
        #------------------------------------------------------------------
        """
        
        if(DEBUG_DATA_IMPORT) :    
            print("[ExportFileTypeHistory][select_export_df_title]")

        for idx in self.data_export_file_type_history.exportfiletypehistory.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DATA_IMPORT) :
            print("[ExportFileTypeHistory][select_iexport_df_title] : row col : ",row_number,column_number)

        model   =   self.data_export_file_type_history.exportfiletypehistory.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DATA_IMPORT) :    
            print("[ExportFileTypeHistory][select_export_df_title] : cell value [",cell,"]")

        if(column_number == 0) :
            if(cell == " ") :
                tdata[row_number][column_number] = "X" 
            else :
                tdata[row_number][column_number] = " "      

            model.reload_data(tdata)

        elif(column_number == 1):

            if(not (tdata[row_number][2] == 0)) :
                self.display_import_with_export_parms(self.export_file_type,tdata[row_number][1],tdata[row_number][2])

    def return_from_export_file_types(self) :
        """            
        #------------------------------------------------------------------
        #   return to import histories ;ayout
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory] return_from_export_file_types")

        self.display_import_histories()

    def delete_export_histories(self) :
        """            
        #------------------------------------------------------------------
        #   delete the selected export histories
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory] delete_export_histories")

        model   =   self.data_export_file_type_history.exportfiletypehistory.model
        tdata   =   model.get_data()

        delete_list     =   []

        for i in range(len(tdata)) :
            check_value     =   tdata[i][0]
            if(not (check_value == " ")) :
                delete_list.append(tdata[i][1])

        if(DEBUG_DATA_IMPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory] delete_list",delete_list)
        
        if(len(delete_list) > 0) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Verify export File history Delete")
            dlg.setText("Do you want to delete historie(s)")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlg.exec()

            if(button == QMessageBox.Yes) :

                from dfcleanser.Qt.data_import.DataImportModel import ExportHistory

                for i in range(len(delete_list)) :
                    ExportHistory.delete_from_history(self.import_file_type,delete_list[i])

                from PyQt5.QtWidgets import QMessageBox
                dlga = QMessageBox(self)
                dlga.setWindowTitle("Delete Export File history Status")
                dlga.setText("Selected Export Histories Deleted")
                dlga.setStandardButtons(QMessageBox.Ok)
                dlga.setStyleSheet("QLabel{min-width: 300px;}");
                button = dlga.exec()

        else :

            from PyQt5.QtWidgets import QMessageBox
            dlgc = QMessageBox(self)
            dlgc.setWindowTitle("Delete Export File history Status")
            dlgc.setText("No historie(s) selected to delete.")
            dlgc.setStandardButtons(QMessageBox.Ok)
            dlgc.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlgc.exec()


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -        display data export file type histories end            -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display Import with parms                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_with_parms(self, filetype, dftitle):

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[display_import_with_parms] : filetype : dftitle : ",filetype, dftitle)

        try :

            self.import_with_filetype       =   filetype
            self.import_with_dftitle        =   dftitle
                 
            parms_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_WITH_PARMS)
         
            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("[display_import_with_parms] : parms_index : ",parms_index)
       
            if(parms_index is None) :

                from dfcleanser.Qt.data_import.DataImportWidgets import Import_With_Parms_Widget 
                import_parms                 =   [self.import_with_filetype,self.import_with_dftitle,self.import_with_parms,self.return_from_parms] 
                self.importwithParms_Widget  =   Import_With_Parms_Widget(import_parms)

                current_index   =  len(self.DataImportWidgets_stack_dict)
                self.DataImportWidgets_stack_dict.update({IMPORT_WITH_PARMS : current_index})
                self.stackedLayout.addWidget(self.importwithParms_Widget)

            else :
            
                reload_parms    =   [self.import_with_filetype,self.import_with_dftitle,None] 
                
                if(DEBUG_DATA_IMPORT) :
                    print("[display_import_with_parms] : reload option : ",reload_parms)

                self.importwithParms_Widget.reload_table_data(reload_parms)
                current_index   =   parms_index

            self.stackedLayout.setCurrentIndex(current_index)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_import_with_parms] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[display_import_with_parms] end\n  stack : ",self.DataImportWidgets_stack_dict)

        self.resize(1070,700)


    # -----------------------------------------------------------------#
    # -             display Import with parms methods                 -#
    # -----------------------------------------------------------------#
    def import_with_parms(self) :

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("\n[display_import_with_parms][import_with_parms] :  filetype : dftitle : ",self.import_with_filetype,self.import_with_dftitle)
        
        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT, SQLQUERY_IMPORT, FWF_IMPORT

        IMPORT_FLAG     =   0
 
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("\n[display_import_with_parms][import_with_parms] :  IMPORT_FLAG : ",IMPORT_FLAG)

        if((self.import_with_filetype == SQLTABLE_IMPORT) or (self.import_with_filetype == SQLQUERY_IMPORT)) :

            dconntblparms   =   [IMPORT_FLAG,self.import_with_db_connector]
            self.display_dbconnector_table(dconntblparms)
            
        else :

            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("\n[display_import_with_parms][import_with_parms] getting Import_Details : ")

            from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
            Import_Details  =   ImportHistory.get_df_title_entry(self.import_with_filetype,self.import_with_dftitle)

            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("[display_import_with_parms][import_with_parms] Import Details Dump : ")
                Import_Details.dump()
    
            full_parms      =   Import_Details.get_full_parms()
            addl_parms      =   Import_Details.get_addl_parms()

            if(self.import_with_filetype == FWF_IMPORT) :
                addl_parms  =   None

            if(DEBUG_DATA_IMPORT) :
                print("[display_import_with_parms][import_with_parms] full_parms : \n  ",full_parms)
                print("[display_import_with_parms][import_with_parms] addl_parms : \n  ",addl_parms)

            cfg_parms   =   [self.import_with_dftitle,self.import_with_dftitle]

            for i in range(len(full_parms)) :

                if(not (full_parms[i] is None) ) :
                    cfg_parms.append(full_parms[i])
                else :
                    cfg_parms.append("")
        
            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("\n[display_import_with_parms][import_with_parms] cfg_parms - after full \n: ",cfg_parms)

            if(not (addl_parms is None)) :

                addl_parms_keys     =   list(addl_parms.keys())
                addl_parms_str  =   "{"

                for i in range(len(addl_parms_keys)) :
                    addl_parms_str  =   addl_parms_str + '\"' + addl_parms_keys[i] + '\" : \"' + str(addl_parms.get(addl_parms_keys[i]))
                    if(i < (len(addl_parms_keys) -1)) :
                        addl_parms_str  =   addl_parms_str + '\",\n' 
                    else :
                        addl_parms_str  =   addl_parms_str + '\"'

                addl_parms_str  =   addl_parms_str + "}"
                cfg_parms.append(addl_parms_str)

            self.cfg_parms  =   cfg_parms

            if(DEBUG_DATA_IMPORT) :
                print("\n[display_import_with_parms][import_with_parms] \n  cfg_parms : ",self.cfg_parms)

            #from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type
            #file_text   =   get_text_for_import_type(self.import_with_filetype)
            #self.statusbar.showMessage("Importing " + file_text + " : ----")

            importParms     =   [self.import_with_filetype,self.import_with_dftitle,self.cfg_parms]
            self.display_import_form(importParms)


    def return_from_parms(self) :

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[display_import_with_parms][return_from_parms]")

        self.display_import_histories()


    # -----------------------------------------------------------------#
    # -                  Import with a DBConnector                    -#
    # -----------------------------------------------------------------#
    def import_with_db_connector(self) :

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_with_parms][import_with_db_connector] ")
        
        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, IMPORT_FLAG
        current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(IMPORT_FLAG)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_with_parms][import_with_db_connector] current_selected_connector : \n  ",current_selected_connector)

        self.statusBar().clearMessage() 

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox()
        dlg.setTextFormat(Qt.RichText)
        dlg.setWindowTitle("Db Connector Status")
        text_msg    =   ""
        dlg.setStyleSheet("QLabel{min-width: 350px;}")

        if(current_selected_connector is None) :

            dlg.setText("No dbconnector selected to import with")
            dlg.setStandardButtons(QMessageBox.Ok)
            button = dlg.exec()

        else :
            
            from dfcleanser.sw_utilities.db_utils import get_db_id_title

            SQL_Server_Type             =   current_selected_connector.get_db_id()
            SQL_Server_Type_Text        =   get_db_id_title(int(SQL_Server_Type))
            db_library                  =   current_selected_connector.get_db_library()
            Server_Name                 =   current_selected_connector.get_server()
            Database                    =   current_selected_connector.get_database()

            text_msg        =   "Importing Table with : <br>"
            text_msg        =   text_msg + "    SQL_Server_Type : " + SQL_Server_Type_Text + "<br>"
            text_msg        =   text_msg + "    db_library : " + db_library + "<br>"
            text_msg        =   text_msg + "    Server_Name : " + Server_Name + "<br>"
            text_msg        =   text_msg + "    Database : " + Database + "<br>"
            text_msg        =   text_msg + "<br> Continue with Import? <br>"
        
            dlg.setText(text_msg)
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button = dlg.exec()

            if(button == QMessageBox.Yes) :

                try :

                    if(DEBUG_DATA_IMPORT) :
                        print("  [display_import_with_parms][import_with_db_connector] self.import_with_filetype : ",self.import_with_filetype)

                    from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
                    Import_Details  =   ImportHistory.get_df_title_entry(self.import_with_filetype,self.import_with_dftitle)
                
                    if(DEBUG_DATA_IMPORT) :
                        print("  [display_import_with_parms][import_with_db_connector] Import Details : \n  ",self.import_with_dftitle)
    
                    if(not (Import_Details is None)) :
                    
                        full_parms      =   Import_Details.get_full_parms().copy()

                        if(DEBUG_DATA_IMPORT) :
                            print("  [display_import_with_parms][import_with_db_connector] full_parms : \n  ",full_parms)

                    
                        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT, SQLQUERY_IMPORT
                        if(self.import_with_filetype == SQLTABLE_IMPORT) :
                            full_parms.pop(0)
                            full_parms.pop(0)
                        #else :
                        #    full_parms.pop(0)
                        #    full_parms.pop(0)

                    else :
                        full_parms      =   []

                    if(DEBUG_DATA_IMPORT) :
                        print("  [display_import_with_parms][import_with_db_connector] full_parms : \n  ",full_parms)

                    if(not (self.import_with_filetype == SQLQUERY_IMPORT)) :
                        cfg_parms   =   [self.import_with_dftitle,self.import_with_dftitle]
                    else :
                        cfg_parms   =   []

                    for i in range(len(full_parms)) :

                        if(not (full_parms[i] is None) ) :
                            cfg_parms.append(full_parms[i])
                        else :
                            cfg_parms.append("")

                    if(DEBUG_DATA_IMPORT) :
                        print("  [display_import_with_parms][import_with_db_connector] cfg_parms : \n: ",cfg_parms)
 
                    importParms     =   [self.import_with_filetype,self.import_with_dftitle,cfg_parms]
                    self.display_import_form(importParms)

                except Exception as e:

                    from dfcleanser.common.common_utils import opStatus
                    opstat      =   opStatus()
                    opstat.store_exception("Unable to save import parms to history",e)
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[display_import_with_parms][import_with_db_connector] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display Import with parms end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display Import Status                        -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_status(self, filetype, dftitle):

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [display_import_status] : filetype : dftitle : ",filetype, dftitle)

        try :

            self.import_with_filetype       =   filetype
            self.import_with_dftitle        =   dftitle
                 
        
            parms_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_STATUS)
         
            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("  [display_import_status] : parms_index : ",parms_index)
       
            if(parms_index is None) :

                from dfcleanser.Qt.data_import.DataImportWidgets import Import_Status_Widget 
                import_parms              =   [self.import_with_filetype,self.import_with_dftitle,self.return_from_status] 
                self.importstatus_Widget  =   Import_Status_Widget(import_parms)

                current_index   =  len(self.DataImportWidgets_stack_dict)
                self.DataImportWidgets_stack_dict.update({IMPORT_STATUS : current_index})
                self.stackedLayout.addWidget(self.importstatus_Widget)

            else :
            
                reload_parms                    =   [self.import_with_filetype,self.import_with_dftitle] 

                if(DEBUG_DATA_IMPORT_DETAILS) :
                    print("  [display_import_status] : reload option : ",reload_parms)

                self.importstatus_Widget.reload_table_data(reload_parms)
                current_index   =   parms_index

            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("  [display_import_status] : current_index : ",current_index)


            self.stackedLayout.setCurrentIndex(current_index)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_import_status] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [display_import_status] end\n    ",self.DataImportWidgets_stack_dict)

        self.resize(1070,800)


    # -----------------------------------------------------------------#
    # -                display Import status methods                  -#
    # -----------------------------------------------------------------#


    def return_from_status(self) :

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[display_import_status][return_from_status]")

        self.display_import_histories()


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display Import Status end                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display Export with parms                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_with_export_parms(self,filetype,dftitle,filename):

        if(DEBUG_DATA_IMPORT) :
            print("\n[display_import_with_export_parms] ",filetype,dftitle,filename)

        self.export_with_filetype       =   filetype
        self.export_with_dftitle        =   dftitle
        self.export_with_filename       =   filename
        export_parms                    =   [self.export_with_filetype,self.export_with_dftitle,self.export_with_filename,self.export_with_parms,self.return_from_parms]          
        reload_parms                    =   [self.export_with_filetype,self.export_with_dftitle,self.export_with_filename] 

        parms_index  =   self.DataImportWidgets_stack_dict.get(EXPORT_WITH_PARMS)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_with_export_parms] : parms_index : ",parms_index)

        if(parms_index is None) :

            from dfcleanser.Qt.data_import.DataImportWidgets import Import_With_Export_Parms_Widget  
            self.exportwithParms_Widget  =   Import_With_Export_Parms_Widget(export_parms)

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({EXPORT_WITH_PARMS : current_index})
            self.stackedLayout.addWidget(self.exportwithParms_Widget)

        else :

            self.exportwithParms_Widget.reload_table_data(reload_parms)
            current_index   =   parms_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_with_export_parms] end : stack \n  ",self.DataImportWidgets_stack_dict)

        self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -             display Export with parms methods                 -#
    # -----------------------------------------------------------------#
    def export_with_parms(self) :

        if(DEBUG_DATA_IMPORT) :
            print("\n  [display_import_with_export_parms][export_with_parms]",self.export_with_filetype,self.export_with_filename)

        dftitleParms    =   [self.export_with_filetype,self.export_with_filename]

        from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
        exportValues    =  get_export_details_values(dftitleParms) 
        ptitles         =   exportValues[0]
        pvals           =   exportValues[1]
       
        if(DEBUG_DATA_IMPORT) :
            print("  [display_import_with_export_parms][export_with_parms][ptitles] : \n    ",ptitles)
            print("  [display_import_with_export_parms][export_with_parms][pvalues] : \n    ",pvals)

        import_with_export_parms    =   self.exportwithParms_Widget.import_with_export_values
        export_with_titles          =   import_with_export_parms[0]
        export_with_values          =   import_with_export_parms[1]

        if(DEBUG_DATA_IMPORT) :
            print("  [display_import_with_export_parms][export_with_parms][export_with_titles] : \n    ",export_with_titles)
            print("  [display_import_with_export_parms][export_with_parms][export_with_values] : \n    ",export_with_values)

        import dfcleanser.Qt.data_export.DataExportModel as dem
        import dfcleanser.Qt.data_import.DataImportModel as DIM

        if(self.export_with_filetype== dem.CSV_EXPORT) :
            import_labels   =   DIM.pandas_import_csv_labelList[:8]
            out_file_type   =   DIM.CSV_IMPORT
        elif(self.export_with_filetype == dem.EXCEL_EXPORT) :
            import_labels   =   DIM.pandas_import_excel_labelList[:9]
            out_file_type   =   DIM.EXCEL_IMPORT
        elif(self.export_with_filetype == dem.JSON_EXPORT) :
            import_labels   =   DIM.pandas_import_json_labelList[:7]
            out_file_type   =   DIM.JSON_IMPORT
        elif(self.export_with_filetype == dem.HTML_EXPORT) :
            import_labels   =   DIM.pandas_import_html_labelList[:6]
            out_file_type   =   DIM.HTML_IMPORT
        elif(self.export_with_filetype == dem.SQLTABLE_EXPORT) :
            import_labels   =   DIM.pandas_import_sqltable_common_labelList[:9]
            out_file_type   =   DIM.SQLTABLE_IMPORT
        elif(self.export_with_filetype == dem.CUSTOM_EXPORT) :
            import_labels   =   DIM.custom_import_labelList[:3]
            out_file_type   =   DIM.CUSTOM_IMPORT

        if(DEBUG_DATA_IMPORT) :
            print("  [display_import_with_export_parms][export_with_parms][import_labels] : \n    ",import_labels)

        import_cfg_parms            =   []

        for i in range(len(import_labels)) :
                
            parm_to_match    =   import_labels[i]
            if(parm_to_match in export_with_titles) :

                match_index     =   export_with_titles.index(parm_to_match)
                print("match_index",match_index)
                if(match_index > -1) :
                    import_cfg_parms.append(export_with_values[match_index])

            else :

                if(parm_to_match.find("_history") > -1) :
                    import_cfg_parms.append(import_cfg_parms[0])
                else :
                    import_cfg_parms.append("")

        if(DEBUG_DATA_IMPORT) :
            print("  [export_with_parms]  cfg_parms :\n    ",import_cfg_parms)

        importParms             =   [out_file_type , import_cfg_parms[0], import_cfg_parms]
        self.display_import_form(importParms)

    def return_from_export_parms(self) :

        if(DEBUG_DATA_IMPORT) :
            print("[return_from_export_parms]")

        self.display_import_histories()

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display Export with parms end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display Import form parms                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_import_form(self, importParms):


        self.import_file_form_file_type     =   int(importParms[0])
        self.import_file_form_dftitle       =   importParms[1]
        self.import_file_form_cfg_parms     =   importParms[2]

        if(DEBUG_DATA_IMPORT) :
            print("\n[display_import_form] filetype : dftitle  : ",self.import_file_form_file_type,self.import_file_form_dftitle,"\n cfgparms : \n  ",self.import_file_form_cfg_parms)


        import dfcleanser.Qt.data_import.DataImportModel as DIM
        if(self.import_file_form_file_type == DIM.CSV_IMPORT) :
            layout_index    =   IMPORT_CSV_FORM
            height          =   850
        elif(self.import_file_form_file_type == DIM.FWF_IMPORT) :
            layout_index    =   IMPORT_FWF_FORM
            height          =   800
        elif(self.import_file_form_file_type == DIM.EXCEL_IMPORT) :
            layout_index    =   IMPORT_EXCEL_FORM
            height          =   850
        elif(self.import_file_form_file_type == DIM.JSON_IMPORT) :
            layout_index    =   IMPORT_JSON_FORM
            height          =   850
        elif(self.import_file_form_file_type == DIM.XML_IMPORT) :
            layout_index    =   IMPORT_XML_FORM
            height          =   1000
        elif(self.import_file_form_file_type == DIM.PDF_IMPORT) :
            layout_index    =   IMPORT_PDF_FORM
            height          =   700
        elif(self.import_file_form_file_type == DIM.HTML_IMPORT) :
            layout_index    =   IMPORT_HTML_FORM
            height          =   800
        elif(self.import_file_form_file_type == DIM.SQLTABLE_IMPORT) :
            layout_index    =   IMPORT_SQLTABLE_FORM
            height          =   1000
        elif(self.import_file_form_file_type == DIM.SQLQUERY_IMPORT) :
            layout_index    =   IMPORT_SQLQUERY_FORM
            height          =   1000
        elif(self.import_file_form_file_type == DIM.CUSTOM_IMPORT) :
            layout_index    =   IMPORT_CUSTOM_FORM
            height          =   700
        
        if(DEBUG_DATA_IMPORT) :
            print("[display_import_form] layout_index : ",layout_index)

        file_form_types_index  =   self.DataImportWidgets_stack_dict.get(layout_index)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_form] file_form_types_index : ",file_form_types_index)

        if(file_form_types_index is None) :

            filetypeformParms   =   [self.import_file_form_file_type,self.import_file_form_dftitle,self.import_file_form_cfg_parms] 

            if(DEBUG_DATA_IMPORT) :
                print("[display_import_form] filetypeformParms : \n  ",filetypeformParms)

            if(self.import_file_form_file_type == DIM.CSV_IMPORT) :
                self.data_import_csv_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.FWF_IMPORT) :
                self.data_import_fwf_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.EXCEL_IMPORT) :
                self.data_import_excel_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.JSON_IMPORT) :
                self.data_import_json_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.XML_IMPORT) :
                self.data_import_xml_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.PDF_IMPORT) :
                self.data_import_pdf_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.HTML_IMPORT) :
                self.data_import_html_form  =   self.build_import_form(filetypeformParms)
            
            elif(self.import_file_form_file_type == DIM.SQLTABLE_IMPORT) :
                self.data_import_sqltable_form  =   self.build_import_form(filetypeformParms)
            elif(self.import_file_form_file_type == DIM.SQLQUERY_IMPORT) :
                self.data_import_sqlquery_form  =   self.build_import_form(filetypeformParms)
            
            elif(self.import_file_form_file_type == DIM.CUSTOM_IMPORT) :
                self.data_import_custom_form  =   self.build_import_form(filetypeformParms)
        
            good_form   =   True

            if(self.import_file_form_file_type == DIM.CSV_IMPORT) :
                if(self.data_import_csv_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.FWF_IMPORT) :
                if(self.data_import_fwf_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.EXCEL_IMPORT) :
                if(self.data_import_excel_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.JSON_IMPORT) :
                if(self.data_import_json_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.XML_IMPORT) :
                if(self.data_import_xml_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.PDF_IMPORT) :
                if(self.data_import_pdf_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.HTML_IMPORT) :
                if(self.data_import_html_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.SQLTABLE_IMPORT) :
                if(self.data_import_sqltable_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.SQLQUERY_IMPORT) :
                if(self.data_import_sqlquery_form is None) : good_form = False
            elif(self.import_file_form_file_type == DIM.CUSTOM_IMPORT) :
                if(self.data_import_custom_form is None) : good_form = False
 
            if(good_form) :

                current_index   =  len(self.DataImportWidgets_stack_dict)
                self.DataImportWidgets_stack_dict.update({layout_index : current_index})

                if(DEBUG_DATA_IMPORT) :
                    print("[display_import_form] file_form_types_index : ",file_form_types_index)

                if(self.import_file_form_file_type == DIM.CSV_IMPORT) :

                    from PyQt5.QtWidgets import QScrollArea
                    self.csv_scroll     =   QScrollArea()

                    self.csv_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    self.csv_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    self.csv_scroll.setWidgetResizable(True)

                    self.data_import_csv_form.setFixedWidth(980)

                    self.csv_scroll.setWidget(self.data_import_csv_form)
                    self.csv_scroll.setFixedHeight(600)

                    self.stackedLayout.addWidget(self.csv_scroll)#self.data_import_csv_form)

                elif(self.import_file_form_file_type == DIM.FWF_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_fwf_form)

                elif(self.import_file_form_file_type == DIM.EXCEL_IMPORT) :

                    from PyQt5.QtWidgets import QScrollArea
                    self.excel_scroll     =   QScrollArea()

                    self.excel_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    self.excel_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    self.excel_scroll.setWidgetResizable(True)

                    self.data_import_excel_form.setFixedWidth(980)

                    self.excel_scroll.setWidget(self.data_import_excel_form)
                    self.excel_scroll.setFixedHeight(600)

                    self.stackedLayout.addWidget(self.excel_scroll)#self.data_import_excel_form)

                elif(self.import_file_form_file_type == DIM.JSON_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_json_form)
                elif(self.import_file_form_file_type == DIM.XML_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_xml_form)
                elif(self.import_file_form_file_type == DIM.PDF_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_pdf_form)
                elif(self.import_file_form_file_type == DIM.HTML_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_html_form)
                elif(self.import_file_form_file_type == DIM.SQLTABLE_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_sqltable_form)
                elif(self.import_file_form_file_type == DIM.SQLQUERY_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_sqlquery_form)
                elif(self.import_file_form_file_type == DIM.CUSTOM_IMPORT) :
                    self.stackedLayout.addWidget(self.data_import_custom_form)

        else :

            if(DEBUG_DATA_IMPORT_FORMS) :
                print("[display_import_form] file_form_types_index : ",file_form_types_index)

            if(self.import_file_form_file_type == DIM.CSV_IMPORT) :
                self.data_import_csv_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.FWF_IMPORT) :
                self.data_import_fwf_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.EXCEL_IMPORT) :
                self.data_import_excel_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.JSON_IMPORT) :
                self.data_import_json_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.XML_IMPORT) :
                self.data_import_xml_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.PDF_IMPORT) :
                self.data_import_pdf_form.load_form_values(self.import_file_form_cfg_parms)
            elif(self.import_file_form_file_type == DIM.HTML_IMPORT) :
                self.data_import_html_form.load_form_values(self.import_file_form_cfg_parms)
            
            elif(self.import_file_form_file_type == DIM.SQLTABLE_IMPORT) :

                load_vals   =   [self,self.import_file_form_file_type,self.import_file_form_cfg_parms]
                self.data_import_sqltable_form.reload_sql_import_form_values(load_vals)

            elif(self.import_file_form_file_type == DIM.SQLQUERY_IMPORT) :

                load_vals   =   [self,self.import_file_form_file_type]
                self.data_import_sqlquery_form.load_form_values(load_vals)

            elif(self.import_file_type == DIM.CUSTOM_IMPORT) :
                self.data_import_custom_form.load_form_values(self.import_file_form_cfg_parms)

            current_index   =   file_form_types_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_form][end] : current_index ",current_index,"\n  ",self.DataImportWidgets_stack_dict,"\n")

        self.resize(1070,height)


    def build_import_form(self, buildparms) :
        """
        * ----------------------------------------------------
        * function : build the import form
        * 
        * parms :
        *
        * returns : import form
        * ---------------------------------------------------
        """

        if(DEBUG_DATA_IMPORT) :
            print("\n  [build_import_form] buildparms : ",buildparms)

        import dfcleanser.Qt.data_import.DataImportModel as DIM

        self.build_filetype     =   buildparms[0]
        self.build_dftitle      =   buildparms[1]
        self.build_parms        =   buildparms[2]

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        try :

            if( (self.build_filetype==DIM.SQLTABLE_IMPORT)  or (self.build_filetype==DIM.SQLQUERY_IMPORT) ):

                from dfcleanser.sw_utilities.DBUtilsWidgets import DBUtils_SQLImportInputFormWidget  
 
                formparms       =   [self,self.build_filetype,self.build_parms]               
                import_form     =   DBUtils_SQLImportInputFormWidget(formparms)
 
            else :

                import_df_titles    =   DIM.get_dftitles_list(DIM.IMPORT_HISTORY,self.build_filetype)

                if(self.build_dftitle is None) :
                    if(not(import_df_titles is None)) :
                        last_df_title   =   DIM.get_last_dftitle(self.build_filetype,import_df_titles)
                    else :
                        last_df_title   =   ""
                else :
                    last_df_title       =   self.build_dftitle
                
                selectDicts     =   []
                
                if((not (import_df_titles is None))) :
                    df_titles    =   {"default":last_df_title,"list":import_df_titles}
                else :
                    df_titles    =   {"default":"","list":[""]}
                
                if(DEBUG_DATA_IMPORT) :
                    print("  [build_import_form] df_titles : ",df_titles)

                selectDicts.append(df_titles)

                if(DEBUG_DATA_IMPORT) :
                    print("  [build_import_form] : selectDicts",selectDicts)

                if(self.build_filetype == DIM.CSV_IMPORT) :

                    form_parms      =   [DIM.pandas_import_csv_id,DIM.pandas_import_csv_idList,DIM.pandas_import_csv_labelList,DIM.pandas_import_csv_typeList,DIM.pandas_import_csv_placeholderList,DIM.pandas_import_csv_reqList]
                    comboMethods    =   [self.update_csv_df]
                    file_methods    =   [self.update_csv_file]
                    button_methods  =   [self.import_csv_file,self.clear_csv_file,self.return_from_csv_file,self.help_csv_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport CSV File\n"
                    form_width      =   900

                elif(self.build_filetype == DIM.FWF_IMPORT) :

                    form_parms     =   [DIM.pandas_import_fwf_id,DIM.pandas_import_fwf_idList,DIM.pandas_import_fwf_labelList,DIM.pandas_import_fwf_typeList,DIM.pandas_import_fwf_placeholderList,DIM.pandas_import_fwf_reqList]
                    comboMethods    =   [self.update_fwf_df]
                    file_methods    =   [self.update_fwf_file]
                    button_methods  =   [self.import_fwf_file,self.clear_fwf_file,self.return_from_fwf_file,self.help_fwf_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport FWF File\n"
                    form_width      =   900
             
                elif(self.build_filetype == DIM.EXCEL_IMPORT) :

                    form_parms     =    [DIM.pandas_import_excel_id,DIM.pandas_import_excel_idList,DIM.pandas_import_excel_labelList,DIM.pandas_import_excel_typeList,DIM.pandas_import_excel_placeholderList,DIM.pandas_import_excel_reqList]
                    comboMethods    =   [self.update_excel_df]
                    file_methods    =   [self.update_excel_file]
                    button_methods  =   [self.import_excel_file,self.clear_excel_file,self.return_from_excel_file,self.help_excel_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport Excel File\n"
                    form_width      =   900
            
                elif(self.build_filetype == DIM.JSON_IMPORT) :

                    form_parms     =   [DIM.pandas_import_json_id,DIM.pandas_import_json_idList,DIM.pandas_import_json_labelList,DIM.pandas_import_json_typeList,DIM.pandas_import_json_placeholderList,DIM.pandas_import_json_reqList]
                    comboMethods    =   [self.update_json_df,None,None]
                    file_methods    =   [self.update_json_file]
                    button_methods  =   [self.import_json_file,self.clear_json_file,self.return_from_json_file,self.help_json_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport JSON File\n"
                    form_width      =   900
                    
                    orient_sel      =   {"default":"columns","list":["columns","split","records","index","values"]}
                    selectDicts.append(orient_sel)

                    typ_sel         =   {"default":"frame","list":["frame","series"]}
                    selectDicts.append(typ_sel)

                elif(self.build_filetype == DIM.XML_IMPORT) :

                    form_parms     =   [DIM.pandas_import_xml_id,DIM.pandas_import_xml_idList,DIM.pandas_import_xml_labelList,DIM.pandas_import_xml_typeList,DIM.pandas_import_xml_placeholderList,DIM.pandas_import_xml_reqList]
                    comboMethods    =   [self.update_xml_df,None,None]
                    file_methods    =   [self.update_xml_file]
                    button_methods  =   [self.import_xml_file,self.clear_xml_file,self.return_from_xml_file,self.help_xml_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport XML File\n"
                    form_width      =   900
                    
                    elems_sel      =   {"default":"False","list":["True","False"]}
                    selectDicts.append(elems_sel)

                    attrs_sel      =   {"default":"False","list":["True","False"]}
                    selectDicts.append(attrs_sel)
                
                elif(self.build_filetype == DIM.PDF_IMPORT) :

                    form_parms     =   [DIM.pandas_import_pdf_id,DIM.pandas_import_pdf_idList,DIM.pandas_import_pdf_labelList,DIM.pandas_import_pdf_typeList,DIM.pandas_import_pdf_placeholderList,DIM.pandas_import_pdf_reqList]
                    comboMethods    =   [self.update_pdf_df,None,None]
                    file_methods    =   [self.update_pdf_file]
                    button_methods  =   [self.import_pdf_file,self.clear_pdf_file,self.return_from_pdf_file,self.help_pdf_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport PDF File\n"
                    form_width      =   900
                    
                elif(self.build_filetype == DIM.HTML_IMPORT) :

                    form_parms      =   [DIM.pandas_import_html_id,DIM.pandas_import_html_idList,DIM.pandas_import_html_labelList,DIM.pandas_import_html_typeList,DIM.pandas_import_html_placeholderList,DIM.pandas_import_html_df_reqList]
                    comboMethods    =   [self.update_html_df]
                    file_methods    =   [self.update_html_file]
                    button_methods  =   [self.import_html_file,self.clear_html_file,self.return_from_html_file,self.help_html_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport HTML File\n"
                    form_width      =   1000
            
                elif(self.build_filetype == DIM.CUSTOM_IMPORT) :

                    form_parms      =   [DIM.custom_import_id,DIM.custom_import_idList,DIM.custom_import_labelList,DIM.custom_import_typeList,DIM.custom_import_placeholderList,DIM.custom_import_reqList]
                    comboMethods    =   [self.update_custom_df]
                    file_methods    =   None
                    button_methods  =   [self.import_custom_file,self.clear_custom_file,self.return_from_custom_file,self.help_custom_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nImport Custom File\n"
                    form_width      =   900

                importcomboList     =   selectDicts
                form_parms.append(importcomboList)
                form_parms.append(comboMethods)            
                form_parms.append(file_methods)
                form_parms.append(button_methods)            
                form_parms.append(cfg_parms)            
                form_parms.append(form_title)
                form_parms.append(form_width)            

                from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget, SMALL
                if( (self.build_filetype == DIM.CSV_IMPORT) or (self.build_filetype == DIM.EXCEL_IMPORT) ) :
                    import_form     =   dfcleanser_input_form_Widget(form_parms)#,size=SMALL)
                else:
                    import_form     =   dfcleanser_input_form_Widget(form_parms)


            if(self.build_filetype == DIM.CSV_IMPORT)           :   self.csv_import_form        =   import_form
            elif(self.build_filetype == DIM.FWF_IMPORT)         :   self.fwf_import_form        =   import_form
            elif(self.build_filetype == DIM.EXCEL_IMPORT)       :   self.excel_import_form      =   import_form
            elif(self.build_filetype == DIM.JSON_IMPORT)        :   self.json_import_form       =   import_form
            elif(self.build_filetype == DIM.XML_IMPORT)         :   self.xml_import_form        =   import_form
            elif(self.build_filetype == DIM.PDF_IMPORT)         :   self.pdf_import_form        =   import_form
            elif(self.build_filetype == DIM.HTML_IMPORT)        :   self.html_import_form       =   import_form
            elif(self.build_filetype == DIM.SQLTABLE_IMPORT)    :   self.html_import_form       =   import_form
            elif(self.build_filetype == DIM.SQLQUERY_IMPORT)    :   self.html_import_form       =   import_form
            elif(self.build_filetype == DIM.CUSTOM_IMPORT)      :   self.custom_import_form     =   import_form
        
        except Exception as e:

            title       =   "dfcleanser exception"        
            status_msg  =   "[build_import_form] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
            opstat.set_status(False)

        if(opstat.get_status()) :
            return(import_form)
        else :
            return(None)
    

    """
    * -------------------------------------------------------------------------- 
    *                   CSV Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_csv_df(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_csv_df]")

        dftitle =  self.csv_import_form.get_form_input_value_by_index(1) 
        self.csv_import_form.set_form_input_value_by_index(0,dftitle)

    def update_csv_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_csv_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"csv files (*.csv)")
        self.csv_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_csv_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_csv_file]")

        num_form_values     =   self.csv_import_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_csv_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_csv_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import CSV_IMPORT

        process_import_form(CSV_IMPORT, form_parms, self)

    def clear_csv_file(self) :
        
        form_field_count    =   self.csv_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_csv_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.csv_import_form.set_form_input_value_by_index(i,"")   

    def return_from_csv_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_csv_file]")

        self.display_import_histories()

    def help_csv_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_csv_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CSV_IMPORT_URL
        display_url(CSV_IMPORT_URL)

    """
    * -------------------------------------------------------------------------- 
    *                   FWF Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_fwf_df(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_fwf_df]")

        dftitle =  self.fwf_import_form.get_form_input_value_by_index(1) 
        self.fwf_import_form.set_form_input_value_by_index(0,dftitle)

    def update_fwf_file(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_fwf_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"fwf files (*.fwf)")
        self.fwf_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_fwf_file(self) :

        num_form_values     =   7
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_fwf_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_fwf_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import FWF_IMPORT

        self.Import_Clock.start()

        process_import_form(FWF_IMPORT, form_parms, self)

        self.Import_Clock.stop()

    def clear_fwf_file(self) :
        
        form_field_count    =   self.fwf_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_fwf_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.fwf_import_form.set_form_input_value_by_index(i,"")   

    def return_from_fwf_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_fwf_file]")

        self.display_import_histories()

    def help_fwf_file(self) :
                
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_fwf_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import FWF_IMPORT_URL
        display_url(FWF_IMPORT_URL)


    """
    * -------------------------------------------------------------------------- 
    *                  Excel Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_excel_df(self) :
    
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_excel_df]")

        dftitle =  self.excel_import_form.get_form_input_value_by_index(1) 
        self.excel_import_form.set_form_input_value_by_index(0,dftitle)

    def update_excel_file(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_excel_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"excel files (*.xls)")
        self.excel_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_excel_file(self) :
                
        num_form_values     =   9
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_excel_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_excel_file] form_parms : \n  ",form_parms)
 
        self.Import_Clock.start()

        import time
        time.sleep(3)

        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import EXCEL_IMPORT
        process_import_form(EXCEL_IMPORT, form_parms, self)

        self.Import_Clock.stop()


    def clear_excel_file(self) :

        form_field_count    =   self.excel_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_excel_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.excel_import_form.set_form_input_value_by_index(i,"")   

    def return_from_excel_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_excel_file]")

        self.display_import_histories()

    def help_excel_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_excel_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import EXCEL_IMPORT_URL
        display_url(EXCEL_IMPORT_URL)


    """
    * -------------------------------------------------------------------------- 
    *                  JSON Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_json_df(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_jsonl_df]")

        dftitle =  self.json_import_form.get_form_input_value_by_index(1) 
        self.json_import_form.set_form_input_value_by_index(0,dftitle)

    def update_json_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_json_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.json_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_json_file(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_json_file]")

        num_form_values     =   7
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_json_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_json_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import JSON_IMPORT
        process_import_form(JSON_IMPORT, form_parms, self)

    def clear_json_file(self) :

        form_field_count    =   self.json_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_json_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.json_import_form.set_form_input_value_by_index(i,"")   

    def return_from_json_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_json_file]")

        self.display_import_histories()

    def help_json_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_json_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import JSON_IMPORT_URL
        display_url(JSON_IMPORT_URL)

    """
    * -------------------------------------------------------------------------- 
    *                  XML Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_xml_df(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_xml_df]")

        dftitle =  self.xml_import_form.get_form_input_value_by_index(1) 
        self.xml_import_form.set_form_input_value_by_index(0,dftitle)

    def update_xml_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_xml_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"xml files (*.xml)")
        self.xml_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_xml_file(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_xml_file]")

        num_form_values     =   self.xml_import_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_xml_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][impoxmlrt_json_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import XML_IMPORT
        process_import_form(XML_IMPORT, form_parms, self)

    def clear_xml_file(self) :

        form_field_count    =   self.xml_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_xml_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.xml_import_form.set_form_input_value_by_index(i,"")   

    def return_from_xml_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_xml_file]")

        self.display_import_histories()

    def help_xml_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_xml_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import JSON_IMPORT_URL
        display_url(JSON_IMPORT_URL)



    """
    * -------------------------------------------------------------------------- 
    *                  PDF Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_pdf_df(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_pdf_df]")

        dftitle =  self.pdf_import_form.get_form_input_value_by_index(1) 
        self.pdf_import_form.set_form_input_value_by_index(0,dftitle)

    def update_pdf_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][update_pdf_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"pdf files (*.pdf)")
        self.pdf_import_form.set_form_input_value_by_index(2,fname[0])        

    def import_pdf_file(self) :
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_pdf_file]")

        num_form_values     =   self.pdf_import_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_pdf_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][impoxmlrt_pdf_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import PDF_IMPORT
        process_import_form(PDF_IMPORT, form_parms, self)

    def clear_pdf_file(self) :

        form_field_count    =   self.pdf_import_form.get_form_fields_count()
        
        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][clear_pdf_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.pdf_import_form.set_form_input_value_by_index(i,"")   

    def return_from_pdf_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_pdf_file]")

        self.display_import_histories()

    def help_pdf_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_xml_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import JSON_IMPORT_URL
        display_url(JSON_IMPORT_URL)


    """
    * -------------------------------------------------------------------------- 
    *                  HTML Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_html_df(self) :
        print("[update_html_df]")

    def update_html_file(self) :
        print("[update_html_file]")

    def import_html_file(self) :

        num_form_values     =   6
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_import_html_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][import_html_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import HTML_IMPORT
        process_import_form(HTML_IMPORT, form_parms, self)


    def clear_html_file(self) :
        print("[clear_html_file]")

    def return_from_html_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_html_file]")
        self.display_import_histories()

    def help_html_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_jhtml_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import HTML_IMPORT_URL
        display_url(HTML_IMPORT_URL)

    """
    * -------------------------------------------------------------------------- 
    *               SQLTable Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_sqltable_df(self) :
        print("[update_sqltable_df]")

    def update_sqltable_file(self) :
        print("[update_sqltable_file]")

    def import_sqltable_file(self) :
        print("[import_sqltable_file]")

    def clear_sqltable_file(self) :
        print("[clear_sqltable_file]")

    def return_from_sqltable_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_sqltable_file]")
        self.display_import_histories()

    def help_sqltable_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_sqltable_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SQLTABLE_IMPORT_URL
        display_url(SQLTABLE_IMPORT_URL)

    """
    * -------------------------------------------------------------------------- 
    *               SQLQuery Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_sqlquery_df(self) :
        print("[update_sqlquery_df]")

    def update_sqlquery_file(self) :
        print("[update_sqlquery_file]")

    def import_sqlquery_file(self) :
        print("[import_sqlquery_file]")

    def clear_ssqlquery_file(self) :
        print("[clear_sqlquery_file]")

    def return_from_sqlquery_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_sqlquery_file]")
        self.display_import_histories()

    def help_sqlquery_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_sqlquery_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SQLQUERY_IMPORT_URL
        display_url(SQLQUERY_IMPORT_URL)


    """
    * -------------------------------------------------------------------------- 
    *                  Custom Import local methods
    * -------------------------------------------------------------------------- 
    """
    def update_custom_df(self) :
        print("[update_custom_df]")

    def update_custom_file(self) :
        print("[update_custom_file]")

    def import_custom_file(self) :
        print("[import_custom_file]")

    def clear_custom_file(self) :
        print("[clear_custom_file]")

    def return_from_custom_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][return_from_custom_file]")
        self.display_import_histories()

    def help_custom_file(self) :

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[build_import_form][help_jhtml_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import IMPORT_CUSTOM_ID
        display_url(IMPORT_CUSTOM_ID)

    
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             display Import form with parms end                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dvconnectors table                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dbconnector_table(self, dbtparms) : #, import_type, df_title):

        self.dbconnector_import_type    =   dbtparms[0]  
        self.import_action              =   dbtparms[1] 
        
        if(DEBUG_DATA_IMPORT) :
            print("\n[display_dbconnector_table] : import_type ",self.dbconnector_import_type,type(self.dbconnector_import_type),self.import_action,type(self.import_action))

        try :

            from dfcleanser.sw_utilities.db_utils import IMPORT_FLAG
            if(self.dbconnector_import_type == IMPORT_FLAG) :
                dbconnectors_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_DBCONNECTORS_TABLE)
            else :
                dbconnectors_index  =   self.DataImportWidgets_stack_dict.get(EXPORT_DBCONNECTORS_TABLE)                

            if(DEBUG_DATA_IMPORT_COMMECTORS) :
                print("[display_dbconnector_table] dbconnectors_index : ",dbconnectors_index)

            if(dbconnectors_index is None) :
            
                dbconnecttblparms       =  [self,self.dbconnector_import_type,self.import_action] 
                import dfcleanser.sw_utilities.DBUtilsWidgets as qt_dbu
                self.dbconnectorsTable  =  qt_dbu.DBUtilsDBConnectorsTableWidget(dbconnecttblparms) 
                self.stackedLayout.addWidget(self.dbconnectorsTable)
 
                current_index   =  len(self.DataImportWidgets_stack_dict)
                if(self.dbconnector_import_type == IMPORT_FLAG) :
                    self.DataImportWidgets_stack_dict.update({IMPORT_DBCONNECTORS_TABLE : current_index})
                else :
                    self.DataImportWidgets_stack_dict.update({EXPORT_DBCONNECTORS_TABLE : current_index})    

                if(DEBUG_DATA_IMPORT_COMMECTORS) :
                    print("[display_dbconnector_tanle] current_index : ",current_index)

            else :

                self.dbconnectorsTable.reload_data()
                current_index   =   dbconnectors_index

            self.stackedLayout.setCurrentIndex(current_index)

        except Exception as e:

            title       =   "dfcleanser exception"      
            status_msg  =   "[display_dbconnector_table] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(DEBUG_DATA_IMPORT_COMMECTORS) :
            print("[display_dbconnector_table] end\n  ",self.DataImportWidgets_stack_dict)

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display dvconnectors table end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dvconnectors form                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dbconnector_form(self,dbcon_form_parms):

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("\n[display_dbconnector_form] ")

        self.forCreate      =   dbcon_form_parms[0] 
        self.import_type    =   dbcon_form_parms[1] 
        self.dbconparms     =   dbcon_form_parms[2]
        self.dbcontable     =   dbcon_form_parms[3]

        self.statusBar().clearMessage()

        if(DEBUG_DATA_IMPORT_FORMS) :
            print("[display_dbconnector_form] self.forCreate  self.import_type :  ",self.forCreate,self.import_type)
            print("[display_dbconnector_form] self.dbconparms :  \n  ",self.dbconparms)

        if(self.forCreate) :
            dbconnectors_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_DBCONNECTORS_CREATE_FORM)
        else :
            dbconnectors_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_DBCONNECTORS_EDIT_FORM)

        if(dbconnectors_index is None) :

            dbconform_parms     =   [self,self.import_type,self.dbconparms,self.forCreate,self.dbcontable]

            from dfcleanser.sw_utilities.DBUtilsWidgets import DBUtils_DBConnectorFormWidget
            
            if(self.forCreate) :
                self.dbconnectorCreateForm  =  DBUtils_DBConnectorFormWidget(dbconform_parms) 
                self.stackedLayout.addWidget(self.dbconnectorCreateForm)
            else :
                self.dbconnectorEditForm  =  DBUtils_DBConnectorFormWidget(dbconform_parms) 
                self.stackedLayout.addWidget(self.dbconnectorEditForm)
 
            current_index   =  len(self.DataImportWidgets_stack_dict)

            if(self.forCreate) :
                self.DataImportWidgets_stack_dict.update({IMPORT_DBCONNECTORS_CREATE_FORM : current_index})
            else :
                self.DataImportWidgets_stack_dict.update({IMPORT_DBCONNECTORS_EDIT_FORM : current_index})

            if(DEBUG_DATA_IMPORT_FORMS) :
                print("[display_dbconnector_form] current_index : ",current_index)

        else :
            
            if(DEBUG_DATA_IMPORT_FORMS) :
                print("[display_dbconnector_form][reload_form] : load_form_values ",dbconnectors_index,"\n  ",self.dbconparms)

            if(self.forCreate) :
                self.dbconnectorCreateForm.load_form_values(self.dbconparms)
            else :
                self.dbconnectorEditForm.load_form_values(self.dbconparms)
 
            current_index   =   dbconnectors_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[display_dbconnector_form] end\n  ",self.DataImportWidgets_stack_dict)

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display dbconnectors table end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display data import json objects                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    
    # -----------------------------------------------------------------#
    # -                 display data import json dfs                  -#
    # -----------------------------------------------------------------#

    def display_import_json_dfs(self, dfs):

        if(DEBUG_DATA_IMPORT) :
            print("\n[display_import_json_dfs]")

        self.dfslist   =   dfs
 
        dfs_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_HTML_DFS_FORM)

        if(dfs_index is None) :

            importjsondfsParms  =   [self.dfslist,self.select_table_id,self.return_from_json_dfs,self.help_for_json_dfs] 
            from dfcleanser.Qt.data_import.DataImportWidgets import DataImportHTMLdfsWidget

            self.import_json_dfs  =   DataImportHTMLdfsWidget(importjsondfsParms)

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({IMPORT_HTML_DFS_FORM : current_index})

            self.stackedLayout.addWidget(self.import_json_dfs)

        else :

            #self.import_json_dfs.reload_table_data(self.dfslist)
            current_index   =   self.DataImportWidgets_stack_dict.get(IMPORT_HTML_DFS_FORM)

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_json_dfs] end",self.DataImportWidgets_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -       display data import file type histories methods         -#
    # -----------------------------------------------------------------#
    def select_table_id(self) :


        for idx in self.import_json_dfs.importhtmldfsTable.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DATA_IMPORT) :
            print("[display_import_json_dfs][select_itable_id]",row_number,column_number)

        model   =   self.import_json_dfs.importhtmldfsTable.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DATA_IMPORT) :    
            print("[display_import_json_dfs][select_itable_id] : cell value [",cell,"]")

        if(column_number == 0) :
            self.display_save_import_json_df(self.dfslist[row_number])

    def return_from_json_dfs(self) :

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_json_dfs][return_from_json_dfs]")

        self.display_import_histories()


    def help_for_json_dfs(self) :

        if(DEBUG_DATA_IMPORT) :
            print("[display_import_json_dfs][help_for_json_dfs]")
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import HTML_IMPORT_URL
        display_url(HTML_IMPORT_URL)

    
    # -----------------------------------------------------------------#
    # -                  save data import json dfs                    -#
    # -----------------------------------------------------------------#

    def display_save_import_json_df(self, df):

        if(DEBUG_DATA_IMPORT) :
            print("\n[display_save_import_json_df]")

        self.df  =   df
 
        dfs_index  =   self.DataImportWidgets_stack_dict.get(IMPORT_HTML_DF_SAVE_FORM)

        if(dfs_index is None) :

            importjsonsavedfParms  =   [self.df,self.return_from_save_json,self.help_for_save_json] 
            from dfcleanser.Qt.data_import.DataImportWidgets import DataImportHTMLdfSaveWidget

            self.import_json_save_df  =   DataImportHTMLdfSaveWidget(importjsonsavedfParms)

            current_index   =  len(self.DataImportWidgets_stack_dict)
            self.DataImportWidgets_stack_dict.update({IMPORT_HTML_DF_SAVE_FORM : current_index})

            self.stackedLayout.addWidget(self.import_json_save_df)

        else :

            self.import_json_save_df.reset_form_df([self.df])
            current_index   =   IMPORT_HTML_DF_SAVE_FORM

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_IMPORT) :
            print("[display_save_import_json_df] end \n  ",self.DataImportWidgets_stack_dict)

        self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -                    Return from save json                      -#
    # -----------------------------------------------------------------#
    def return_from_save_json(self) :

        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][return_from_save_json]")

        self.display_import_histories()

    # -----------------------------------------------------------------#
    # -                     Select a SQLServerType                    -#
    # -----------------------------------------------------------------#
    def help_for_save_json(self) :

        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][help_for_save_json]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import HTML_IMPORT_URL
        display_url(HTML_IMPORT_URL)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display data import json objects end             -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


     
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Global access to Data Import Chapter              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearDataImport()  :

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import DATA_IMPORT_TITLE
    
    clear_screen()
    #displayHTML(DATA_IMPORT_TITLE)

    from dfcleanser.common.cfg import dfc_qt_chapters, IMPORT_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(IMPORT_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(IMPORT_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_import_form()

    clear_screen()

def closeDataImportInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, IMPORT_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(IMPORT_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(IMPORT_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import DATA_IMPORT_TITLE
    
    clear_screen()
    #displayHTML(DATA_IMPORT_TITLE)
    logger.info(" Data Import Instances closed")

def showDataImport()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, IMPORT_QT_CHAPTER_ID, DATA_IMPORT_TITLE
    
    clear_screen()
    #displayHTML(DATA_IMPORT_TITLE)

    #logger.info("Loading Data Import Instance")

    data_import_gui = DataImportGui()
    data_import_gui.show()

    dfc_qt_chapters.add_qt_chapter(IMPORT_QT_CHAPTER_ID,data_import_gui,"showDataImport")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(IMPORT_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Import Instances Loaded")

    #dfc_qt_chapters.dump_dfc_qt_chapters()

def closeDataImportChapter()  :

    closeDataImportInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDataImport')","unable to delete data import : ")    



