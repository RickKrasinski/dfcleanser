"""
# DataExport
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

DEBUG_DATA_EXPORT               =   False
DEBUG_DATA_EXPORT_HISTORIES     =   False
DEBUG_DATA_EXPORT_FILE_TYPE     =   False
DEBUG_DATA_EXPORT_DETAILS       =   False
DEBUG_DATA_EXPORT_FORMS         =   False
DEBUG_DATA_EXPORT_CONNECTORS    =   False

DEBUG_DATA_EXPORT_CSV           =   False
DEBUG_DATA_EXPORT_EXCEL         =   False
DEBUG_DATA_EXPORT_JSON          =   False
DEBUG_DATA_EXPORT_XML           =   False
DEBUG_DATA_EXPORT_HTML          =   False
DEBUG_DATA_EXPORT_SQLTABLE      =   False
DEBUG_DATA_EXPORT_CUSTOM        =   False




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


EXPORT_TYPE_HISTORIES                   =   "DataExport dfsExported"
EXPORT_FILE_TYPE_HISTORIES              =   "DataExport filetypes Exported"
EXPORT_WITH_PARMS                       =   "DataExport export parms"
EXPORT_STATUS                           =   "DataExport status"

EXPORT_CVS_FILE_TYPE_HISTORIES          =   "DataExport cvs filetypes Exported"
EXPORT_EXCEL_FILE_TYPE_HISTORIES        =   "DataExport excel filetypes Exported"
EXPORT_JSON_FILE_TYPE_HISTORIES         =   "DataExport json filetypes Exported"
EXPORT_XML_FILE_TYPE_HISTORIES          =   "DataExport xml filetypes Exported"
EXPORT_HTML_FILE_TYPE_HISTORIES         =   "DataExport html filetypes Exported"
EXPORT_SQLTABLE_FILE_TYPE_HISTORIES     =   "DataExport sqltable filetypes Exported"
EXPORT_CUSTOM_FILE_TYPE_HISTORIES       =   "DataExport custom filetypes Exported"

EXPORT_CSV_FORM                         =   "DataExport CSVFile"
EXPORT_EXCEL_FORM                       =   "DataExport ExcelFile"
EXPORT_JSON_FORM                        =   "DataExport JSONFile"
EXPORT_XML_FORM                         =   "DataExport XMLFile"
EXPORT_HTML_FORM                        =   "DataExport HTMLFile"
EXPORT_SQLTABLE_FORM                    =   "DataExport SQLTable"
EXPORT_CUSTOM_FORM                      =   "DataExport Custom"

EXPORT_DBCONNECTORS_TABLE               =   "dbconnectors table"
EXPORT_DBCONNECTORS_CREATE_FORM         =   "dbconnector create"
EXPORT_DBCONNECTORS_EDIT_FORM           =   "dbconnector edit"

"""
IMPORT_FILE_FORM                        =   "DataImport import file form"



IMPORT_DBCONNECTORS_TABLE             =   "DataImport DBConnectors Table"
IMPORT_DBCONNECTORS_CREATE_FORM       =   "DataImport DBConnectors Create Form"
IMPORT_DBCONNECTORS_EDIT_FORM         =   "DataImport DBConnectors Edit Form"

EXPORT_DBCONNECTORS_TABLE             =   "DataExport DBConnectors Table"
"""

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  DataImport Main Screen                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

#DATA_IMPORT_MAIN_GEOMETRY                           =   [0,0,1080,1000]


DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Data Import main GUI                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataExportGui(QtWidgets.QMainWindow):

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

        self.DataExportWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.dfcDataExportMainLayout.addLayout(self.stackedLayout)
        self.form.dfcDataExportMainLayout.addStretch()

        from dfcleanser.common.cfg import DataExport_add_df_signal
        DataExport_add_df_signal.connectSignal(self.add_new_df)


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_export\DataExportUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Data Export")
        
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
        icon_name   =   dfcdir +"\DataExportChapterIcon.png"
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
        self.init_data_export_form()

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_export_buttons(self):

        if(DEBUG_DATA_EXPORT) :
            print("[init_data_export_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.CSVbutton, self.form.Excelbutton, self.form.JSONbutton, self.form.XMLbutton,
                         self.form.HTMLbutton, self.form.SQLTablebutton, self.form.Custombutton, 
                         self.form.ExportResetbutton, self.form.ExportHelpbutton]
        
        callbacks   =   [self.ExportCSVFile, self.ExportExcelFile, self.ExportJSONFile, self.ExportXMLFile,
                         self.ExportHTMLFile, self.ExportSQLTable, self.ExportCustom, 
                         self.ResetDataExport, self.HelpDataExport]
    
        # init buttons for usage
        Export_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,Export_Button_Style)

        # adding action to a button
        for i in range(len(buttons)) :
            buttons[i].clicked.connect(callbacks[i])


    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_export_splash_screen(self):

        if(DEBUG_DATA_EXPORT) :
            print("[init_data_export_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import DataExport_ID
        build_chapter_splash_screen(DataExport_ID, self.form.DataExportsplash)

        if(DEBUG_DATA_EXPORT) :
            print("[end init_data_export_splash_screen]  ")

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(DEBUG_DATA_EXPORT) :
            print("[DataExportGui][add_new_df]  df_title",df_title)

        self.df_select.addItem(df_title)
        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(DEBUG_DATA_EXPORT) :
            print("[DataExportGui] self.df_select",type(self.df_select),self.df_select.count())

        self.init_stacked_index()



    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_export_form(self):
        
        if(DEBUG_DATA_EXPORT) :
            print("[init_data_export_form]  ")

        self.init_data_export_buttons()
        self.init_data_export_splash_screen()
        self.display_export_histories()

        #self.resize(1070,600)

    # -----------------------------------------------------------------#
    # -                 remotely load data export                     -#
    # -----------------------------------------------------------------#

    def export_dfc_dataframe(self,dfc_name) :

        #index = self.df_select.findText(dfc_name)
        #self.df_select.setCurrentIndex(index) 

        self.init_data_export_form()       
            

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               Main Gui Data Import Methods                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                      Export CSV File                          -#
    # -----------------------------------------------------------------#
    def ExportCSVFile(self) :

        self.form.CSVbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportCSVFile]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.CSV_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.pandas_export_csv_id + "Parms")
        
        if(DEBUG_DATA_EXPORT) :
            print("[ExportCSVFile] cfg_parms : ",cfg_parms)

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)


    # -----------------------------------------------------------------#
    # -                     Export Excel File                         -#
    # -----------------------------------------------------------------#
    def ExportExcelFile(self) :

        self.form.Excelbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportExcelFile]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.EXCEL_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.pandas_export_excel_id + "Parms")

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)

    # -----------------------------------------------------------------#
    # -                      Export JSON File                         -#
    # -----------------------------------------------------------------#
    def ExportJSONFile(self) :

        self.form.JSONbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportJSONFile]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.JSON_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.pandas_export_json_id + "Parms")

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)

    # -----------------------------------------------------------------#
    # -                       Export XML File                         -#
    # -----------------------------------------------------------------#
    def ExportXMLFile(self) :

        self.form.XMLbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportXMLFile]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.XML_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.pandas_export_xml_id + "Parms")

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)


    # -----------------------------------------------------------------#
    # -                      Export HTML File                         -#
    # -----------------------------------------------------------------#
    def ExportHTMLFile(self) :

        self.form.HTMLbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportHTMLFile]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.HTML_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.pandas_export_html_id + "Parms")

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)

    # -----------------------------------------------------------------#
    # -                    Export via SQLTable                       -#
    # -----------------------------------------------------------------#
    def ExportSQLTable(self) :

        self.form.SQLTablebutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportSQLTable]")

        from dfcleanser.common.cfg import get_dfc_dataframes_select_list, DataExport_ID
        dataframes      =   get_dfc_dataframes_select_list(DataExport_ID)

        if(dataframes == None) :

            title       =   "dfcleanser error : [ExportSQLTable]"        
            status_msg  =   "no dfc dfs defined to export"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)
            opstat.set_status(False)

            return()

        from dfcleanser.sw_utilities.db_utils import EXPORT_FLAG
        dbconparms      =   [EXPORT_FLAG,self.export_with_db_connector]

        self.display_export_dbconnector_table(dbconparms)


    # -----------------------------------------------------------------#
    # -                     Export Custom                             -#
    # -----------------------------------------------------------------#
    def ExportCustom(self) :

        self.form.Custombutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("[ExportCustom]")

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        file_type   =   DEM.CUSTOM_EXPORT 
        dftitle     =   self.export_dftitle

        from dfcleanser.common.cfg import get_config_value
        cfg_parms   =   cfg.get_config_value(DEM.custom_export_id + "Parms")

        export_parms    =   [file_type,dftitle,cfg_parms]

        self.display_export_form(export_parms)

    
    # -----------------------------------------------------------------#
    # -                   Reset Data Export                           -#
    # -----------------------------------------------------------------#
    def ResetDataExport(self):
        
        self.form.ExportResetbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("ResetDataImport")

        self.display_export_histories()
        

    # -----------------------------------------------------------------#
    # -                 Data Inspection Help                          -#
    # -----------------------------------------------------------------#
    def HelpDataExport(self):

        self.form.ExportHelpbutton.toggle()

        if(DEBUG_DATA_EXPORT) :
            print("HelpDataExport")

        from dfcleanser.common.common_utils import display_url
        display_url("https://rickkrasinski.github.io/dfcleanser-help/dfcleanser-data-export.html")




    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 Data Export display methods                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display data export histories                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_histories(self):

        if(DEBUG_DATA_EXPORT_HISTORIES) :
            print("\n[display_export_histories]  ")

        export_history_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_TYPE_HISTORIES)
        
        if(export_history_index is None) :

            from dfcleanser.Qt.data_export.DataExportWidgets import DataExport_Export_Widget
            self.export_main   =   DataExport_Export_Widget([self])

            self.export_dftitle     =   self.export_main.df_select.currentText()

            current_index   =  len(self.DataExportWidgets_stack_dict)
            self.DataExportWidgets_stack_dict.update({EXPORT_TYPE_HISTORIES : current_index})
            self.stackedLayout.addWidget(self.export_main)

        else :

            self.export_main.reload_data()
            current_index   =   export_history_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_EXPORT_HISTORIES) :
            print("[display_export_histories] end : stack \n  ",self.DataExportWidgets_stack_dict,"\n")

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dataframes     =   get_dfc_dataframes_titles_list()

        if(dataframes is None) :
            height  =    650    
        else :
            height  =   (len(dataframes) * DEFAULT_ROW_HEIGHT) + 600

        self.resize(1070,height)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -           display data export file type histories             -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_file_type_histories(self, filetype):

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("\n[display_export_file_type_histories] : filetype", filetype)

        self.export_file_type   =   int(filetype)

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        if(self.export_file_type == DEM.CSV_EXPORT) :
            layout_index    =   EXPORT_CVS_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.EXCEL_EXPORT) :
            layout_index    =   EXPORT_EXCEL_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.JSON_EXPORT) :
            layout_index    =   EXPORT_JSON_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.XML_EXPORT) :
            layout_index    =   EXPORT_XML_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.HTML_EXPORT) :
            layout_index    =   EXPORT_HTML_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.SQLTABLE_EXPORT) :
            layout_index    =   EXPORT_SQLTABLE_FILE_TYPE_HISTORIES
        elif(self.export_file_type == DEM.CUSTOM_EXPORT) :
            layout_index    =   EXPORT_CUSTOM_FILE_TYPE_HISTORIES

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[display_export_file_type_histories] : layout_index ",layout_index)

        file_types_index  =   self.DataExportWidgets_stack_dict.get(layout_index)

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[display_export_file_type_histories] : file_types_index",file_types_index)

        if(file_types_index is None) :

            filetypehistoriesParms  =   [self,self.export_file_type,self.select_export_df_title,self.delete_export_histories,self.return_from_export_file_types] 
            from dfcleanser.Qt.data_export.DataExportWidgets import Data_Export_File_Type_Histories_Widget

            if(self.export_file_type == DEM.CSV_EXPORT) :
                self.data_export_csv_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_csv_file_type_history
            elif(self.export_file_type == DEM.EXCEL_EXPORT) :
                self.data_export_excel_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_excel_file_type_history
            elif(self.export_file_type == DEM.JSON_EXPORT) :
                self.data_export_json_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_json_file_type_history
            elif(self.export_file_type == DEM.XML_EXPORT) :
                self.data_export_xml_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_xml_file_type_history
            elif(self.export_file_type == DEM.HTML_EXPORT) :
                self.data_export_html_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_html_file_type_history
            elif(self.export_file_type == DEM.SQLTABLE_EXPORT) :
                self.data_export_sqltable_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_sqltable_file_type_history
            elif(self.export_file_type == DEM.CUSTOM_EXPORT) :
                self.data_export_custom_file_type_history  =   Data_Export_File_Type_Histories_Widget(filetypehistoriesParms)
                self.data_export_file_type_history      =   self.data_export_custom_file_type_history

            if(DEBUG_DATA_EXPORT_FILE_TYPE) :
                print("[display_export_file_type_histories] : current_index",len(self.DataExportWidgets_stack_dict))

            current_index   =  len(self.DataExportWidgets_stack_dict)
            self.DataExportWidgets_stack_dict.update({layout_index : current_index})
            self.stackedLayout.addWidget(self.data_export_file_type_history)
            
        else :

            if(self.export_file_type == DEM.CSV_EXPORT) :
                self.data_export_csv_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_csv_file_type_history
            elif(self.export_file_type == DEM.EXCEL_EXPORT) :
                self.data_export_excel_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_excel_file_type_history
            elif(self.export_file_type == DEM.JSON_EXPORT) :
                self.data_export_json_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_json_file_type_history
            elif(self.export_file_type == DEM.XML_EXPORT) :
                self.data_export_xml_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_xml_file_type_history
            elif(self.export_file_type == DEM.HTML_EXPORT) :
                self.data_export_html_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_html_file_type_history
            elif(self.export_file_type == DEM.SQLTABLE_EXPORT) :
                self.data_export_sqltable_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_sqltable_file_type_history
            elif(self.export_file_type == DEM.CUSTOM_EXPORT) :
                self.data_export_custom_file_type_history.reload_data()
                self.data_export_file_type_history      =   self.data_export_custom_file_type_history

            current_index   =   file_types_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[display_export_file_type_histories] end : stack :\n  ",self.DataExportWidgets_stack_dict)

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
        
        if(DEBUG_DATA_EXPORT_FILE_TYPE) :    
            print("[ExportFileTypeHistory][select_export_df_title]")

        for idx in self.data_export_file_type_history.exportfiletypehistory.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory][select_iexport_df_title] : row col : ",row_number,column_number)

        model   =   self.data_export_file_type_history.exportfiletypehistory.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :    
            print("[ExportFileTypeHistory][select_export_df_title] : cell value [",cell,"]")

        if(column_number == 0) :
            if(cell == " ") :
                tdata[row_number][column_number] = "X" 
            else :
                tdata[row_number][column_number] = " "      

            model.reload_data(tdata)

        elif(column_number == 1):

            filename    =   tdata[row_number][2]
            dftitle     =   tdata[row_number][1]

            if(DEBUG_DATA_EXPORT_FILE_TYPE) :    
                print("[ExportFileTypeHistory][select_export_df_title] : dftitle : filename ",dftitle,filename)

            self.display_export_with_parms(self.export_file_type,dftitle,filename)

    def return_from_export_file_types(self) :
        """            
        #------------------------------------------------------------------
        #   return to import histories ;ayout
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory] return_from_export_file_types")

        self.display_export_histories()

    def delete_export_histories(self) :
        """            
        #------------------------------------------------------------------
        #   delete the selected export histories
        #------------------------------------------------------------------
        """

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[ExportFileTypeHistory] delete_export_histories")

        model   =   self.data_export_file_type_history.exportfiletypehistory.model
        tdata   =   model.get_data()

        delete_list     =   []

        for i in range(len(tdata)) :
            check_value     =   tdata[i][0]
            if(not (check_value == " ")) :
                delete_list.append(tdata[i][1])

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
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
    # -                display_export_with_parms                      -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_with_parms(self,filetype,dftitle,filename):

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("\n[display_export_with_parms] ",filetype,dftitle,filename)

        self.export_with_filetype       =   filetype
        self.export_with_filename       =   filename
        export_parms                    =   [self,self.export_with_filetype,self.export_with_filename]          
        reload_parms                    =   [self.export_with_filetype,self.export_with_filename] 

        parms_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_WITH_PARMS)

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[display_export_with_parms] : parms_index : ",parms_index)

        if(parms_index is None) :

            from dfcleanser.Qt.data_export.DataExportWidgets import Export_With_Parms_Widget  
            self.exportwithParms_Widget  =   Export_With_Parms_Widget(export_parms)

            current_index   =  len(self.DataExportWidgets_stack_dict)
            self.DataExportWidgets_stack_dict.update({EXPORT_WITH_PARMS : current_index})
            self.stackedLayout.addWidget(self.exportwithParms_Widget)

        else :

            self.exportwithParms_Widget.reload_table_data(reload_parms)
            current_index   =   parms_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_EXPORT_FILE_TYPE) :
            print("[display_export_with_parms] end : stack \n  ",self.DataExportWidgets_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display_export_with_parms end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display_export_form                         -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_form(self, exportParms):


        self.export_file_form_file_type     =   int(exportParms[0])
        self.export_file_form_dftitle       =   exportParms[1]
        self.export_file_form_cfg_parms     =   exportParms[2]

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        if(DEBUG_DATA_EXPORT) :
            print("\n[display_export_form] filetype : dftitle  : ",self.export_file_form_file_type,self.export_file_form_dftitle,"\n cfgparms : \n  ",self.export_file_form_cfg_parms)

        import dfcleanser.Qt.data_export.DataExportModel as DEM
        if(self.export_file_form_file_type == DEM.CSV_EXPORT) :
            layout_index    =   EXPORT_CSV_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.EXCEL_EXPORT) :
            layout_index    =   EXPORT_EXCEL_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.JSON_EXPORT) :
            layout_index    =   EXPORT_JSON_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.XML_EXPORT) :
            layout_index    =   EXPORT_XML_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.HTML_EXPORT) :
            layout_index    =   EXPORT_HTML_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.SQLTABLE_EXPORT) :
            layout_index    =   EXPORT_SQLTABLE_FORM
            height          =   900
        elif(self.export_file_form_file_type == DEM.CUSTOM_EXPORT) :
            layout_index    =   EXPORT_CUSTOM_FORM
            height          =   700
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[display_export_form] layout_index : ",layout_index)

        file_form_types_index  =   self.DataExportWidgets_stack_dict.get(layout_index)

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[display_export_form] file_form_types_index : ",file_form_types_index)

        if(file_form_types_index is None) :

            self.filetypeformParms   =   [self.export_file_form_file_type,self.export_file_form_dftitle,self.export_file_form_cfg_parms] 

            if(DEBUG_DATA_EXPORT_FORMS) :
                print("[display_export_form] filetypeformParms : \n  ",self.filetypeformParms)

            if(self.export_file_form_file_type == DEM.CSV_EXPORT) :
                self.data_export_csv_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.EXCEL_EXPORT) :
                self.data_export_excel_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.JSON_EXPORT) :
                self.data_export_json_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.XML_EXPORT) :
                self.data_export_xml_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.HTML_EXPORT) :
                self.data_export_html_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.SQLTABLE_EXPORT) :
                self.data_export_sqltable_form  =   self.build_export_form(self.filetypeformParms,opstat)
            elif(self.export_file_form_file_type == DEM.CUSTOM_EXPORT) :
                self.data_export_custom_form  =   self.build_export_form(self.filetypeformParms,opstat)
            
            if(opstat.get_status()) :

                current_index   =  len(self.DataExportWidgets_stack_dict)
                self.DataExportWidgets_stack_dict.update({layout_index : current_index})

                if(DEBUG_DATA_EXPORT_FORMS) :
                    print("[display_export_form] file_form_types_index : ",file_form_types_index)

                if(self.export_file_form_file_type == DEM.CSV_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_csv_form)
                elif(self.export_file_form_file_type == DEM.EXCEL_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_excel_form)
                elif(self.export_file_form_file_type == DEM.JSON_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_json_form)
                elif(self.export_file_form_file_type == DEM.XML_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_xml_form)
                elif(self.export_file_form_file_type == DEM.HTML_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_html_form)
                elif(self.export_file_form_file_type == DEM.SQLTABLE_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_sqltable_form)
                elif(self.export_file_form_file_type == DEM.CUSTOM_EXPORT) :
                    self.stackedLayout.addWidget(self.data_export_custom_form)

            else :

                height  -   650

        else :
            
            self.filetypeformParms   =   [self.export_file_form_file_type,self.export_file_form_dftitle,self.export_file_form_cfg_parms] 

            if(DEBUG_DATA_EXPORT) :
                print("[display_export_form] file_form_types_index : ",file_form_types_index)
                print("[display_export_form] self.filetypeformParms",self.export_file_form_cfg_parms)

            if(self.export_file_form_file_type == DEM.CSV_EXPORT) :
                self.reload_form_values(self.data_export_csv_form,self.export_file_form_cfg_parms) 
            elif(self.export_file_form_file_type == DEM.EXCEL_EXPORT) :
                self.reload_form_values(self.data_export_excel_form,self.export_file_form_cfg_parms)
            elif(self.export_file_form_file_type == DEM.JSON_EXPORT) :
                self.reload_form_values(self.data_export_json_form,self.export_file_form_cfg_parms)
            elif(self.export_file_form_file_type == DEM.XML_EXPORT) :
                self.reload_form_values(self.data_export_xml_form,self.export_file_form_cfg_parms)
            elif(self.export_file_form_file_type == DEM.HTML_EXPORT) :
                self.reload_form_values(self.data_export_html_form,self.export_file_form_cfg_parms)
            elif(self.export_file_form_file_type == DEM.SQLTABLE_EXPORT) :
                self.reload_form_values(self.data_export_sqltable_form.sqlformWidget.export_form,self.export_file_form_cfg_parms)
            elif(self.export_file_form_file_type == DEM.CUSTOM_EXPORT) :
                self.reload_form_values(self.data_export_custom_form,self.export_file_form_cfg_parms)

            current_index   =   file_form_types_index

        if(opstat.get_status()) :
            self.stackedLayout.setCurrentIndex(current_index)

            if(DEBUG_DATA_EXPORT) :
                print("[display_export_form][end] : current_index ",current_index,"\n  ",self.DataExportWidgets_stack_dict,"\n")

        else :
            height  =   650

        self.resize(1070,height)


    # -----------------------------------------------------------------#
    # -          display Export form parms  local methods             -#
    # -----------------------------------------------------------------#

    def reload_form_values(self, exportform, values) :

        if(DEBUG_DATA_EXPORT) :
            print("\n[reload_form_values] exportform : values  : ",exportform,values)


        form_count  =   exportform.get_form_fields_count()
        for i in range(form_count) :
            exportform.set_form_input_value_by_index(i, "")

        if(not (values is None)) :
            if(len(values)==form_count) :
                for i in range(len(values)) :
                    exportform.set_form_input_value_by_index(i, values[i])

    def build_export_form(self, buildparms, opstat) :
        """
        * ----------------------------------------------------
        * function : build the import form
        * 
        * parms :
        *
        * returns : import form
        * ---------------------------------------------------
        """


        import dfcleanser.Qt.data_export.DataExportModel as DEM
        import dfcleanser.Qt.data_import.DataImportModel as DIM

        self.build_filetype     =   buildparms[0]
        self.build_dftitle      =   buildparms[1]
        self.build_parms        =   buildparms[2]

        if(DEBUG_DATA_EXPORT) :
            print("  [build_export_form] self.build_filetype :  self.build_dftitle : ",self.build_filetype,self.build_dftitle)
            print("  [build_export_form] build parms \n     : ",self.build_parms)
        
        if(DEBUG_DATA_EXPORT) :
            if(not (self.build_parms is None)) :
                print("  [build_export_form] self.build_parms :  ")

                for i in range(len(self.build_parms)) :
                    print("    [build_parms][",i,"] : ",self.build_parms[i])

            else :
                print("  [build_export_form] self.build_parms :  None ")    

        export_form             =   None

        try :

            export_df_titles    =   DIM.get_dftitles_list(DIM.EXPORT_HISTORY,self.build_filetype)
        
            if(self.build_dftitle is None) :
                last_df_title       =   DIM.get_last_dftitle(self.build_filetype,export_df_titles)
            else :
                last_df_title       =   self.build_dftitle
                
            if(DEBUG_DATA_EXPORT_FORMS) :
                print("  [build_export_form] last_df_title : ",last_df_title)

            if(self.build_filetype==DEM.SQLTABLE_EXPORT) :

                from dfcleanser.sw_utilities.DBUtilsWidgets import DBUtils_SQLExportInputFormWidget  
 
                formparms       =   [self,self.build_filetype,self.build_parms]               
                export_form     =   DBUtils_SQLExportInputFormWidget(formparms)
 
            else :

                from dfcleanser.common.cfg import get_dfc_dataframes_select_list, DataExport_ID
                dataframes      =   get_dfc_dataframes_select_list(DataExport_ID)

                if(dataframes == None) :

                    title       =   "dfcleanser exception : [build_export_from]"        
                    status_msg  =   "no dfc dfs defined to export"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)
                    opstat.set_status(False)

                    return()
                
                selectDicts     =   []
                
                if((not (export_df_titles is None))) :
                    df_titles    =   {"default":last_df_title,"list":export_df_titles}
                else :
                    df_titles    =   {"default":"","list":[""]}

                if(self.build_filetype == DEM.CSV_EXPORT) :

                    form_parms      =   [DEM.pandas_export_csv_id,DEM.pandas_export_csv_idList,DEM.pandas_export_csv_labelList,DEM.pandas_export_csv_typeList,DEM.pandas_export_csv_placeholderList,DEM.pandas_export_csv_reqList]
                    comboMethods    =   [self.update_export_csv_df,self.update_export_csv_history,None,None]
                    file_methods    =   [self.update_export_csv_file]
                    button_methods  =   [self.export_csv_file,self.clear_export_csv_file,self.return_from_export_csv_file,self.help_export_csv_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport CSV File\n"
                    form_width      =   900

                    selectDicts.append(dataframes)
                    selectDicts.append(df_titles)

                    boolFlag        =   {"default":"True","list":["True","False"]}
                    selectDicts.append(boolFlag)
                    selectDicts.append(boolFlag)

                elif(self.build_filetype == DEM.EXCEL_EXPORT) :

                    form_parms      =   [DEM.pandas_export_excel_id,DEM.pandas_export_excel_idList,DEM.pandas_export_excel_labelList,DEM.pandas_export_excel_typeList,DEM.pandas_export_excel_placeholderList,DEM.pandas_export_excel_reqList]
                    comboMethods    =   [self.update_export_excel_df,self.update_export_excel_history,None,None]
                    file_methods    =   [self.update_export_excel_file]
                    button_methods  =   [self.export_excel_file,self.clear_export_excel_file,self.return_from_export_excel_file,self.help_export_excel_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport Excel File\n"
                    form_width      =   900

                    selectDicts.append(dataframes)
                    selectDicts.append(df_titles)

                    boolFlag        =   {"default":"True","list":["True","False"]}
                    selectDicts.append(boolFlag)
                    selectDicts.append(boolFlag)
            
                elif(self.build_filetype == DEM.JSON_EXPORT) :

                    form_parms      =   [DEM.pandas_export_json_id,DEM.pandas_export_json_idList,DEM.pandas_export_json_labelList,DEM.pandas_export_json_typeList,DEM.pandas_export_json_placeholderList,DEM.pandas_export_json_reqList]
                    comboMethods    =   [self.update_export_json_df,self.update_export_json_history,None]
                    file_methods    =   [self.update_export_json_file]
                    button_methods  =   [self.export_json_file,self.clear_export_json_file,self.return_from_export_json_file,self.help_export_json_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport JSON File\n"
                    form_width      =   900
                    
                    selectDicts.append(dataframes)
                    selectDicts.append(df_titles)

                    orient_types   =   ["columns","index","split","records","table","values"]
                    orient         =   {"default":orient_types[0],"list":orient_types}
                    selectDicts.append(orient)


                elif(self.build_filetype == DEM.XML_EXPORT) :

                    form_parms      =   [DEM.pandas_export_xml_id,DEM.pandas_export_xml_idList,DEM.pandas_export_xml_labelList,DEM.pandas_export_xml_typeList,DEM.pandas_export_xml_placeholderList,DEM.pandas_export_xml_reqList]
                    comboMethods    =   [self.update_export_xml_df,self.update_export_xml_history,None]
                    file_methods    =   [self.update_export_xml_file]
                    button_methods  =   [self.export_xml_file,self.clear_export_xml_file,self.return_from_export_xml_file,self.help_export_xml_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport JSON File\n"
                    form_width      =   900
                    
                    selectDicts.append(dataframes)
                    selectDicts.append(df_titles)

                    indexsel       =   {"default":"True","list":["True","False"]}
                    selectDicts.append(indexsel)

                elif(self.build_filetype == DEM.HTML_EXPORT) :

                    form_parms      =   [DEM.pandas_export_html_id,DEM.pandas_export_html_idList,DEM.pandas_export_html_labelList,DEM.pandas_export_html_typeList,DEM.pandas_export_html_placeholderList,DEM.pandas_export_html_reqList]
                    comboMethods    =   [self.update_export_html_df,self.update_export_html_history,None,None]
                    file_methods    =   [self.update_export_html_file]
                    button_methods  =   [self.export_html_file,self.clear_export_html_file,self.return_from_export_html_file,self.help_export_html_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport HTML File\n"
                    form_width      =   1000

                    selectDicts.append(dataframes)
                    selectDicts.append(df_titles)

                    boolFlag        =   {"default":"True","list":["True","False"]}
                    selectDicts.append(boolFlag)
                    selectDicts.append(boolFlag)
            
                elif(self.build_filetype == DEM.CUSTOM_EXPORT) :

                    form_parms      =   [DEM.custom_export_id,DEM.custom_export_idList,DEM.custom_export_labelList,DEM.custom_export_typeList,DEM.custom_export_placeholderList,DEM.custom_export_reqList]
                    comboMethods    =   [self.update_export_custom_df]
                    file_methods    =   None
                    button_methods  =   [self.export_custom_file,self.clear_export_custom_file,self.return_from_export_custom_file,self.help_export_custom_file]
                    cfg_parms       =   self.build_parms
                    form_title      =   "\n\nExport Custom File\n"
                    form_width      =   900

                    selectDicts.append(dataframes)

                
                if(DEBUG_DATA_EXPORT_FORMS) :
                    print("  [build_export_form] : selectDicts",)
                    for i in range(len(selectDicts)) :
                        print("     [",str(i),"] : ",selectDicts[i])

                exportcomboList     =   selectDicts
                form_parms.append(exportcomboList)
                form_parms.append(comboMethods)            
                form_parms.append(file_methods)
                form_parms.append(button_methods)            
                form_parms.append(cfg_parms)            
                form_parms.append(form_title)
                form_parms.append(form_width)  

                if(DEBUG_DATA_EXPORT) :
                    print("  [build_export_form] form_parms :  ")

                from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
                export_form     =   dfcleanser_input_form_Widget(form_parms)

                if(self.build_filetype == DEM.CUSTOM_EXPORT) :  
                    code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df\n"
                    code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + last_df_title + "')\n"
                    export_form.set_form_input_value_by_index(1,code_preamble)
                
                if(DEBUG_DATA_EXPORT) :
                    print("  [build_export_form] after form_built : ")

            if(DEBUG_DATA_EXPORT) :
                print("  [build_export_form] : export_form saved")
       
        except Exception as e:

            title       =   "dfcleanser exception"        
            status_msg  =   "[build_export_form] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
            opstat.set_status(False)

        return(export_form)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             build_export_form callback methods                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    # -----------------------------------------------------------------#
    # -                 CSV_EXPORT callback methods                   -#
    # -----------------------------------------------------------------#

    def update_export_csv_df(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_csv_df]")

        dftitle =  self.data_export_csv_form.get_form_input_value_by_index(0) 
        self.data_export_csv_form.set_form_input_value_by_index(0,dftitle)

    def update_export_csv_file(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_csv_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"csv files (*.csv)")
        self.data_export_csv_form.set_form_input_value_by_index(1,fname[0])        
    
    def update_export_csv_history(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_csv_history]")

        csvfile =  self.data_export_csv_form.get_form_input_value_by_index(2) 
        self.data_export_csv_form.set_form_input_value_by_index(1,csvfile)

    def export_csv_file(self) :

        num_form_values     =   self.data_export_csv_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][export_csv_file]",num_form_values)

        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_csv_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][export_csv_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import CSV_EXPORT
        process_export_form(CSV_EXPORT, form_parms, self)

    def clear_export_csv_file(self) :
        
        form_field_count    =   self.data_export_csv_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_export_csv_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.data_export_csv_form.set_form_input_value_by_index(i,"")   

    def return_from_export_csv_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_csv_file]")

        self.display_export_histories()

    def help_export_csv_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_csv_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CSV_EXPORT_URL
        display_url(CSV_EXPORT_URL)

    # -----------------------------------------------------------------#
    # -                 EXCEL_EXPORT callback methods                 -#
    # -----------------------------------------------------------------#

    def update_export_excel_df(self) :
    
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_excel_df]")

        dftitle =  self.data_export_excel_form.get_form_input_value_by_index(0) 
        self.data_export_excel_form.set_form_input_value_by_index(0,dftitle)

    def update_export_excel_file(self) :
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_excel_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"excel files (*.xls)")
        self.data_export_excel_form.set_form_input_value_by_index(1,fname[0])        
    
    def update_export_excel_history(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_excel_history]")

        excelfile =  self.data_export_excel_form.get_form_input_value_by_index(2) 
        self.data_export_excel_form.set_form_input_value_by_index(1,excelfile)

    def export_excel_file(self) :
                
        num_form_values     =   self.data_export_excel_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_excel_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][export_excel_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import EXCEL_EXPORT
        process_export_form(EXCEL_EXPORT, form_parms, self)

    def clear_export_excel_file(self) :

        form_field_count    =   self.data_export_excel_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_export_excel_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.data_export_excel_form.set_form_input_value_by_index(i,"")   

    def return_from_export_excel_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_excel_file]")

        self.display_export_histories()

    def help_export_excel_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_excel_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import EXCEL_EXPORT_URL
        display_url(EXCEL_EXPORT_URL)


    # -----------------------------------------------------------------#
    # -                 JSON_EXPORT callback methods                  -#
    # -----------------------------------------------------------------#
    def update_export_json_df(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_jsonl_df]")

        dftitle =  self.data_export_json_form.get_form_input_value_by_index(0) 
        self.data_export_json_form.set_form_input_value_by_index(0,dftitle)

    def update_export_json_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_json_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.data_export_json_form.set_form_input_value_by_index(1,fname[0])        
    
    def update_export_json_history(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_json_history]")

        jsonfile =  self.data_export_json_form.get_form_input_value_by_index(2) 
        self.data_export_json_form.set_form_input_value_by_index(1,jsonfile)

    def export_json_file(self) :
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][export_json_file]")

        num_form_values     =   self.data_export_json_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_json_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][import_json_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import JSON_EXPORT
        process_export_form(JSON_EXPORT, form_parms, self)

    def clear_export_json_file(self) :

        form_field_count    =   self.data_export_json_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_json_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.data_export_json_form.set_form_input_value_by_index(i,"")   

    def return_from_export_json_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_json_file]")

        self.display_export_histories()

    def help_export_json_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_json_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import JSON_EXPORT_URL
        display_url(JSON_EXPORT_URL)


    # -----------------------------------------------------------------#
    # -                 XML_EXPORT callback methods                  -#
    # -----------------------------------------------------------------#
    def update_export_xml_df(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_xml_df]")

        dftitle =  self.data_export_xml_form.get_form_input_value_by_index(0) 
        self.data_export_xml_form.set_form_input_value_by_index(0,dftitle)

    def update_export_xml_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_xml_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"xml files (*.xml)")
        self.data_export_xml_form.set_form_input_value_by_index(1,fname[0])        
    
    def update_export_xml_history(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_xml_history]")

        xmlfile =  self.data_export_xml_form.get_form_input_value_by_index(2) 
        self.data_export_xml_form.set_form_input_value_by_index(1,xmlfile)

    def export_xml_file(self) :
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][export_xml_file]")

        num_form_values     =   self.data_export_xml_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_xml_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][import_xml_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import XML_EXPORT
        process_export_form(XML_EXPORT, form_parms, self)

    def clear_export_xml_file(self) :

        form_field_count    =   self.data_export_xml_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_xml_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.data_export_xml_form.set_form_input_value_by_index(i,"")   

    def return_from_export_xml_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_xml_file]")

        self.display_export_histories()

    def help_export_xml_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_xml_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import JSON_EXPORT_URL
        display_url(JSON_EXPORT_URL)



    # -----------------------------------------------------------------#
    # -                 HTML_EXPORT callback methods                  -#
    # -----------------------------------------------------------------#
    def update_export_html_df(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_html_df]")

        dftitle =  self.data_export_html_form.get_form_input_value_by_index(0) 
        self.data_export_html_form.set_form_input_value_by_index(0,dftitle)

    def update_export_html_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_html_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.data_export_html_form.set_form_input_value_by_index(1,fname[0])        
    
    def update_export_html_history(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[build_export_form][update_export_html_history]")

        htmlfile =  self.data_export_html_form.get_form_input_value_by_index(2) 
        self.data_export_html_form.set_form_input_value_by_index(1,htmlfile)

    def export_html_file(self) :
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][export_jhtml_file]")

        num_form_values     =   self.data_export_html_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_html_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][import_json_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import HTML_EXPORT
        process_export_form(HTML_EXPORT, form_parms, self)

    def clear_export_html_file(self) :

        form_field_count    =   self.data_export_html_form.get_form_fields_count()
        
        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_html_file] : form_field_count ",form_field_count,type(form_field_count))
        
        for i in range(form_field_count) :
            if(not (i==1)):
                self.data_export_html_form.set_form_input_value_by_index(i,"")   

    def return_from_export_html_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_html_file]")

        self.display_export_histories()

    def help_export_html_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_html_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import HTML_EXPORT_URL
        display_url(HTML_EXPORT_URL)



    # -----------------------------------------------------------------#
    # -                 CUSTOM_EXPORT callback methods                -#
    # -----------------------------------------------------------------#
    def update_export_custom_df(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][update_export_custom_df]")

        dftitle =  self.data_export_custom_form.get_form_input_value_by_index(0)
        code    =  self.data_export_custom_form.get_form_input_value_by_index(1)

        start_of_df_title   =   code.find("get_dfc_dataframe_df(")
        start_of_df_title   =   start_of_df_title + len("get_dfc_dataframe_df(")

        end_of_df_title     =   code.find(")",start_of_df_title)

        current_df_title    =   code[start_of_df_title : end_of_df_title]

        code.replace(current_df_title,dftitle)

        self.data_export_custom_form.set_form_input_value_by_index(1,code)

    def export_custom_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][export_custom_file]")
        
        num_form_values     =   self.data_export_custom_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.data_export_custom_form.get_form_input_value_by_index(i))

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_import_form][exmport_jcustom_file] form_parms : \n  ",form_parms)
 
        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import CUSTOM_EXPORT
        process_export_form(CUSTOM_EXPORT, form_parms, self)

    def clear_export_custom_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][clear_export_custom_file]")

        dftitle =  self.data_export_custom_form.get_form_input_value_by_index(0)
        code    =  self.data_export_custom_form.get_form_input_value_by_index(1)

        start_of_df_title   =   code.find("get_dfc_dataframe_df(")
        start_of_df_title   =   start_of_df_title + len("get_dfc_dataframe_df(")

        end_of_df_title     =   code.find(")",start_of_df_title)

        current_df_title    =   code[start_of_df_title : end_of_df_title]

        code.replace(current_df_title,dftitle)

        self.data_export_custom_form.set_form_input_value_by_index(1,code)

    def return_from_export_custom_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][return_from_export_custom_file]")

        self.display_export_histories()

    def help_export_custom_file(self) :

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[build_export_form][help_export_custom_file]")
       
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import EXPORT_CUSTOM_ID
        display_url(EXPORT_CUSTOM_ID)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display_export_form  end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             display_export_dbconnector_table                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_dbconnector_table(self, dbtparms) :

        self.dbconnector_export_type    =   dbtparms[0]  
        self.export_action              =   dbtparms[1] 


        #self.export_action              =   self.export_with_db_connector 
        
        if(DEBUG_DATA_EXPORT) :
            print("\n[display_export_dbconnector_table]  ",self.dbconnector_export_type,type(self.dbconnector_export_type),self.export_action,type(self.export_action))

        try :

            dbconnectors_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_DBCONNECTORS_TABLE)                

            if(DEBUG_DATA_EXPORT_CONNECTORS) :
                print("[display_export_dbconnector_table] dbconnectors_index : ",dbconnectors_index)

            if(dbconnectors_index is None) :

                from dfcleanser.sw_utilities.db_utils import EXPORT_FLAG
            
                dbconnecttblparms       =  [self,EXPORT_FLAG,self.export_action] 
                import dfcleanser.sw_utilities.DBUtilsWidgets as qt_dbu
                self.dbconnectorsTable  =  qt_dbu.DBUtilsDBConnectorsTableWidget(dbconnecttblparms) 
                self.stackedLayout.addWidget(self.dbconnectorsTable)
 
                current_index   =  len(self.DataExportWidgets_stack_dict)
                self.DataExportWidgets_stack_dict.update({EXPORT_DBCONNECTORS_TABLE : current_index})    

                if(DEBUG_DATA_EXPORT_CONNECTORS) :
                    print("[display_export_dbconnector_tanle] current_index : ",current_index)

            else :

                self.dbconnectorsTable.reload_data()
                current_index   =   dbconnectors_index

            self.stackedLayout.setCurrentIndex(current_index)

        except Exception as e:

            title       =   "dfcleanser exception"      
            status_msg  =   "[display_export_dbconnector_table] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(DEBUG_DATA_EXPORT_CONNECTORS) :
            print("[display_export_dbconnector_table] end\n  ",self.DataExportWidgets_stack_dict)

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display dvconnectors table end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                  Import with a DBConnector                    -#
    # -----------------------------------------------------------------#
    def export_with_db_connector(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[display_export_with_parms][export_with_db_connector] ")
        
        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, EXPORT_FLAG
        current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(EXPORT_FLAG)

        if(DEBUG_DATA_EXPORT) :
            print("[display_export_with_parms][export_with_db_connector] current_selected_connector : \n  ",current_selected_connector)

        self.statusBar().clearMessage() 
                        
                        
        from dfcleanser.Qt.data_export.DataExportModel import SQLTABLE_EXPORT
        self.export_with_filetype   =   SQLTABLE_EXPORT
        self.export_dftitle         =   self.export_main.df_select.currentText()

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox()
        dlg.setTextFormat(Qt.RichText)
        dlg.setWindowTitle("Db Connector Status")
        text_msg    =   ""
        dlg.setStyleSheet("QLabel{min-width: 350px;}")

        if(current_selected_connector is None) :

            dlg.setText("No dbconnector selected to export with")
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

                    if(DEBUG_DATA_EXPORT_DETAILS) :
                        print("  [display_export_with_parms][export_with_db_connector] self.import_with_filetype : ",self.export_with_filetype)

                    from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
                    Export_Details  =   ExportHistory.get_df_title_entry(self.export_with_filetype,self.export_dftitle)
                
                    if(DEBUG_DATA_EXPORT_DETAILS) :
                        print("  [display_export_with_parms][export_with_db_connector] Import Details : \n  ",self.export_dftitle)
    
                    if(not (Export_Details is None)) :
                    
                        full_parms      =   Export_Details.get_full_parms().copy()
                    
                        from dfcleanser.Qt.data_export.DataExportModel import SQLTABLE_EXPORT
                        if(self.import_with_filetype == SQLTABLE_EXPORT) :
                            full_parms.pop(0)
                            full_parms.pop(0)
                    else :
                        full_parms      =   []

                    if(DEBUG_DATA_EXPORT_DETAILS) :
                        print("  [display_export_with_parms][export_with_db_connector] full_parms : \n  ",full_parms)

                    cfg_parms   =   [self.export_dftitle,self.export_dftitle]

                    for i in range(len(full_parms)) :

                        if(not (full_parms[i] is None) ) :
                            cfg_parms.append(full_parms[i])
                        else :
                            cfg_parms.append("")

                    if(DEBUG_DATA_EXPORT_DETAILS) :
                        print("  [display_export_with_parms][export_with_db_connector] cfg_parms : \n: ",cfg_parms)
 
                    exportParms     =   [self.export_with_filetype,self.export_dftitle,cfg_parms]
                    self.display_export_form(exportParms)

                except Exception as e:

                    from dfcleanser.common.common_utils import opStatus
                    opstat      =   opStatus()
                    opstat.store_exception("Unable to save import parms to history",e)
            
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[display_export_with_parms][export_with_db_connector] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display Export Status                        -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_export_status(self, filetype, filename, dftitle):

        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("  [display_export_status] : filetype : dftitle : ",filetype, filename, dftitle)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        try :

            self.export_with_filetype       =   filetype
            self.export_with_filename       =   filename
            self.dftitle                    =   dftitle
                 
        
            parms_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_STATUS)
         
            if(DEBUG_DATA_EXPORT_DETAILS) :
                print("[display_export_status] : parms_index : ",parms_index)
       
            if(parms_index is None) :

                from dfcleanser.Qt.data_export.DataExportWidgets import Export_Status_Widget 
                export_parms              =   [self,self.export_with_filetype,self.export_with_filename,self.dftitle] 
                self.exportstatus_Widget  =   Export_Status_Widget(export_parms)

                current_index   =  len(self.DataExportWidgets_stack_dict)
                self.DataExportWidgets_stack_dict.update({EXPORT_STATUS : current_index})
                self.stackedLayout.addWidget(self.exportstatus_Widget)

            else :
            
                reload_parms   =   [self.export_with_filetype,self.export_with_filename,self.dftitle] 

                if(DEBUG_DATA_EXPORT_DETAILS) :
                    print("[display_export_status] : reload option : ",reload_parms)

                self.exportstatus_Widget.reload_table_data(reload_parms)
                current_index   =   parms_index

            if(DEBUG_DATA_EXPORT_DETAILS) :
                print("[display_export_status] : current_index : ",current_index)

            self.stackedLayout.setCurrentIndex(current_index)


        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_export_status] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

        if(opstat.get_status()) :

            if(DEBUG_DATA_EXPORT_DETAILS) :
                print("  [display_export_status] end\n    ",self.DataExportWidgets_stack_dict)

            self.resize(1070,800)

        else :

            self.display_export_histories()       















































    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              display Import with parms end                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



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
    # -             display Import form with parms end                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#














    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display dvconnectors form                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    def display_dbconnector_form(self,dbcon_form_parms):

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("\n[display_dbconnector_form] ")

        self.forCreate      =   dbcon_form_parms[0] 
        self.import_type    =   dbcon_form_parms[1] 
        self.dbconparms     =   dbcon_form_parms[2]
        self.dbcontable     =   dbcon_form_parms[3]

        self.statusBar().clearMessage()

        if(DEBUG_DATA_EXPORT_FORMS) :
            print("[display_dbconnector_form] self.forCreate  self.import_type :  ",self.forCreate,self.import_type)
            print("[display_dbconnector_form] self.dbconparms :  \n  ",self.dbconparms)

        if(self.forCreate) :
            dbconnectors_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_DBCONNECTORS_CREATE_FORM)
        else :
            dbconnectors_index  =   self.DataExportWidgets_stack_dict.get(EXPORT_DBCONNECTORS_EDIT_FORM)

        if(dbconnectors_index is None) :

            dbconform_parms     =   [self,self.import_type,self.dbconparms,self.forCreate,self.dbcontable]

            from dfcleanser.sw_utilities.DBUtilsWidgets import DBUtils_DBConnectorFormWidget
            
            if(self.forCreate) :
                self.dbconnectorCreateForm  =  DBUtils_DBConnectorFormWidget(dbconform_parms) 
                self.stackedLayout.addWidget(self.dbconnectorCreateForm)
            else :
                self.dbconnectorEditForm  =  DBUtils_DBConnectorFormWidget(dbconform_parms) 
                self.stackedLayout.addWidget(self.dbconnectorEditForm)
 
            current_index   =  len(self.DataExportWidgets_stack_dict)

            if(self.forCreate) :
                self.DataExportWidgets_stack_dict.update({EXPORT_DBCONNECTORS_CREATE_FORM : current_index})
            else :
                self.DataExportWidgets_stack_dict.update({EXPORT_DBCONNECTORS_EDIT_FORM : current_index})

            if(DEBUG_DATA_EXPORT_FORMS) :
                print("[display_dbconnector_form] current_index : ",current_index)

        else :
            
            if(DEBUG_DATA_EXPORT_FORMS) :
                print("[display_dbconnector_form][reload_form] : load_form_values ",dbconnectors_index,"\n  ",self.dbconparms)

            if(self.forCreate) :
                self.dbconnectorCreateForm.load_form_values(self.dbconparms)
            else :
                self.dbconnectorEditForm.load_form_values(self.dbconparms)
 
            current_index   =   dbconnectors_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("[display_dbconnector_form] end\n  ",self.DataExportWidgets_stack_dict)

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display dbconnectors table end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



      
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Global access to Data Export Chapter              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearDataExport()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, EXPORT_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(EXPORT_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(EXPORT_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_data_export_form()

    clear_screen()


def closeDataExportInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, EXPORT_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(EXPORT_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(EXPORT_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import DATA_EXPORT_TITLE
    
    clear_screen()
    displayHTML(DATA_EXPORT_TITLE)


def showDataExport()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, EXPORT_QT_CHAPTER_ID
    
    clear_screen()

    data_export_gui = DataExportGui()
    data_export_gui.show()

    dfc_qt_chapters.add_qt_chapter(EXPORT_QT_CHAPTER_ID,data_export_gui,"showDataExport")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(EXPORT_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Export Instances Loaded")



def closeDataExportChapter()  :

    closeDataExportInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDataExport')","unable to delete data export : ")    



def exportDataframe(df_name)  :

    from dfcleanser.common.common_utils import clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, EXPORT_QT_CHAPTER_ID
    
    clear_screen()

    data_export_gui = DataExportGui()
    data_export_gui.show()

    data_export_gui.export_dfc_dataframe(df_name)

    dfc_qt_chapters.add_qt_chapter(EXPORT_QT_CHAPTER_ID,data_export_gui,"showDataExport")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(EXPORT_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Data Export Instances Loaded")


