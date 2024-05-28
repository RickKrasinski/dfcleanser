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

from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

import dfcleanser.common.cfg as cfg 
from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataExport_ID

from dfcleanser.Qt.data_export.DataExportModel import (CSV_EXPORT, EXCEL_EXPORT, JSON_EXPORT, HTML_EXPORT, XML_EXPORT, CUSTOM_EXPORT, SQLTABLE_EXPORT)
from dfcleanser.Qt.data_export.DataExportModel import (pandas_export_csv_labelList, pandas_export_excel_labelList, pandas_export_json_labelList,
                                                       pandas_export_xml_labelList, pandas_export_html_labelList, custom_export_labelList)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             general Data Import Housekeeping                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     DataExport WIdgets                        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -              Export with Parms Display Widget                 -#
# -----------------------------------------------------------------#
class DataExport_Export_Widget(QtWidgets.QWidget):
    """            
    #------------------------------------------------------------------
    #   Import parms and commands
    #
    #   Parms       -   dftitle imported
    #
    #------------------------------------------------------------------
    """

    def __init__(self,  exportparms, **kwargs):  

        super().__init__()
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExport_Export_Widget] "))

        self.parent     =   exportparms[0]

        self.init_form()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExport_Export_Widget] : done"))

    def reload_data(self) :

        self.export_histories.reload_data()

    def init_form(self):  

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExport_Export_Widget]  init_form"))

        self.export_histories   =   Data_Export_Histories_Widget([self.select_export_type_history])

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects  =   build_select_dfs_layout("*dataframes_to_export")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout
 
        from PyQt5.QtWidgets import QWidget
        self.dfc_dfs     =   QWidget()
        self.dfc_dfs.setLayout(self.dfc_dfs_layout)

        from PyQt5.QtWidgets import QVBoxLayout
        self.export_layout   =   QVBoxLayout()
        self.export_layout.addWidget(self.export_histories)
        self.export_layout.addWidget(self.dfc_dfs)
        self.export_layout.addStretch()

        self.setLayout(self.export_layout)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExport_Export_Widget] init from end"))

    
    # -----------------------------------------------------------------#
    # -            display data export histories methods              -#
    # -----------------------------------------------------------------#

    def select_export_type_history(self) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[display_export_histories] select_export_type_history"))


        for idx in self.export_histories.exportHistory.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[display_export_histories] select_export_type_history",row_number,column_number))

        model   =   self.export_histories.exportHistory.model
        tdata   =   model.get_data()

        if(column_number == 0) :
            if(not (tdata[row_number][1] == 0) ) :
                self.parent.display_export_file_type_histories(row_number)            
 

# -----------------------------------------------------------------#
# -           Table view and Model for Export History             -#
# -----------------------------------------------------------------#

class DataExportsHistoryModel(QtCore.QAbstractTableModel):
    def __init__(self, exportHistorydata, col_headers):

        super(DataExportsHistoryModel, self).__init__()
        self._data = exportHistorydata
        self.col_headers = col_headers

    def reload_data(self,exportHistorydata) :
        self._data = exportHistorydata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list

            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            elif(column == 5) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.col_headers)) :
                return(self.col_headers[section])
            else :
                return("  ")
            
        return super().headerData(section, orientation, role)

# -----------------------------------------------------------------#
# -               Table view for Export History                   -#
# -----------------------------------------------------------------#
class DataExportsHistoryTable(QtWidgets.QTableView):

    def __init__(self, **kwargs):  

        super().__init__()
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] "))

        self.mainLayout         =   None
        self.model              =   None

        self.init_tableview()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : end"))


    def reload_data(self):
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : reload_data"))

        export_history_data     =   self.load_exportHistory_data()
        self.model.reload_data(export_history_data)
   
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : init_tableview"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        historydata     =   self.load_exportHistory_data()

        if(self.model is None) :
            self.model = DataExportsHistoryModel(historydata, self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
           add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : model loaded"))

        self.num_rows   =   len(historydata )

        if(self.num_rows < 15) :
            new_height  =   (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(historydata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                    load the table data                        -#
    # -----------------------------------------------------------------#
    def load_exportHistory_data(self):

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : load_exportHistory_data "))

        export_file_types    =   ["Pandas CSV Exports","Pandas EXCEL Exports","Pandas JSON Exports",
                                  "Pandas HTML Exports","Pandas SQL TABLE Exports","Custom Exports","XML Exports"]


        file_type_totals    =   []

        for i in range(len(export_file_types)) :

            from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
            df_titles   =   ExportHistory.get_df_titles_for_file_type(i)

            if(not (df_titles is None)) :
                file_type_totals.append(len(df_titles))
            else :
                file_type_totals.append(0)

        data    =   []

        for i in range(len(export_file_types)) :

            data_row    =   []
            data_row.append(str(export_file_types[i]))
            data_row.append(str(file_type_totals[i]))

            data.append(data_row)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportsHistoryTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("DataExportWidgets",print_to_string("  [",j,"]",data[j]))

        self.column_headers     =   ["Export Type","Export Count"]
        self.column_widths      =   [675,300]

        return(data)

# -----------------------------------------------------------------#
# -         Table view and Model for Export History end           -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                Data Export Histories Widget                   -#
# -----------------------------------------------------------------#
class Data_Export_Histories_Widget(QtWidgets.QWidget):

    def __init__(self,  histparms, **kwargs):  

        super().__init__()

        self.select_export_callback     =   histparms[0]

        self.exportHistory              =   None

        self.init_form()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_Histories_Widget] end"))

    def reload_data(self) :

        self.exportHistory.reload_data()

    def init_form(self):  

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_Histories_Widget]  init_form"))


        from PyQt5.QtWidgets import QLabel
        exports_title_label   =   QLabel()
        exports_title_label.setText("\nPandas Export History\n")
        exports_title_label.setAlignment(Qt.AlignCenter)
        exports_title_label.resize(480,50)
        exports_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        self.exportHistory         =   DataExportsHistoryTable()
        self.exportHistory.doubleClicked.connect(self.select_export_callback)

        new_height  =   45 + (self.exportHistory.num_rows * DEFAULT_ROW_HEIGHT)

        self.exportHistory.setMinimumHeight(new_height)
        self.exportHistory.setMaximumHeight(new_height)

        from PyQt5.QtWidgets import QLabel
        history_notes_label   =   QLabel()
        history_notes_label.setText("Double Click on the Export Type to get a list of previous exports to use as inputs for an export.")
        history_notes_label.setAlignment(Qt.AlignCenter)
        history_notes_label.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")
        
        from PyQt5.QtWidgets import QLabel
        history_notes_label1   =   QLabel()
        history_notes_label1.setText("\nTo Export a df not in the export histories. Select the df to export and click on the appropriate export file button on the command bar.")
        history_notes_label1.setAlignment(Qt.AlignCenter)
        history_notes_label1.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.finalhistoriesLayout     =   QVBoxLayout()
        self.finalhistoriesLayout.addWidget(exports_title_label)
        self.finalhistoriesLayout.addWidget(self.exportHistory)
        self.finalhistoriesLayout.addWidget(history_notes_label)
        self.finalhistoriesLayout.addWidget(history_notes_label1)
        self.finalhistoriesLayout.addStretch()

        self.setLayout(self.finalhistoriesLayout)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_HISTORY")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_Histories_Widget] init from end"))


# -----------------------------------------------------------------#
# -                Data Export Histories Widget end               -#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -        Table view and Model for ExportTypes History           -#
# -----------------------------------------------------------------#

class DataExportTypesHistorysModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(DataExportTypesHistorysModel, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignCenter)
            elif(column == 1) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:

            if(column == 1):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)

# -----------------------------------------------------------------#
# -             Table view for ExportTypes History                -#
# -----------------------------------------------------------------#
class DataExportTypesHistorysTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()
        
        self.mainLayout         =   None
        self.model              =   None

        self.file_type          =   dfparms[0]

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : init",self.file_type))

        self.init_tableview()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : done"))

    def reload_data(self):
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportHistoryExportsTable] : reload_data"))

        export_file_type_history_data     =   self.load_export_type_history_data()
        self.model.reload_data(export_file_type_history_data)
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : init_tableview",self.file_type))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportsHistorydata     =   self.load_export_type_history_data()

        if(self.model is None) :
            self.model = DataExportTypesHistorysModel(exportsHistorydata ,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
           add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : model loaded : headers : ",self.column_headers))

        self.num_rows   =   len(exportsHistorydata)
        
        if(self.num_rows < 15) :
            new_height  =   25 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   25 + (15 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(exportsHistorydata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 load the table data                     -#
    # -----------------------------------------------------------------#
    def load_export_type_history_data(self):

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : load_export_type_history_data "))

        from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
        df_titles   =   ExportHistory.get_df_titles_for_file_type(self.file_type)

        df_file_names   =   []

        for i in range(len(df_titles)) :
            
            from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
            history_entry   =   ExportHistory.get_df_title_entry(self.file_type,df_titles[i])

            df_file_names.append(str(history_entry.get_full_parms()[0])) 

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : load_export_type_history_data  : df_file_names  \n  ",df_file_names))

        data    =   []

        for i in range(len(df_titles)) :

            data_row    =   []
            data_row.append(" ")
            data_row.append(str(df_file_names[i]))
            data_row.append(str(df_titles[i]))

            data.append(data_row)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportTypesHistorysTable] : data",len(data)))
            for j in range(len(data)) :
                add_debug_to_log("DataExportWidgets",print_to_string("    [",j,"] : ",data[j]))

        self.column_headers     =   ["DEL","df Title","File Name"]
        self.column_widths      =   [20,300,645]

        return(data)

# -----------------------------------------------------------------#
# -       Table view and Model for ExportTypes History end        -#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -          Data Export file Type Histories Widget               -#
# -----------------------------------------------------------------#
class Data_Export_File_Type_Histories_Widget(QtWidgets.QWidget):

    def __init__(self,  histparms, **kwargs):  

        super().__init__()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_File_Type_Histories_Widget]",histparms))

        self.parent                     =   histparms[0]
        self.filetype                   =   histparms[1]
        self.select_export_callback     =   histparms[2]
        self.delete_export_callback     =   histparms[3]
        self.return_export_callback     =   histparms[4]

        self.init_form()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_ExIport_File_Type_Histories_Widget] : end"))
    
    def reload_data(self) :

        self.exportfiletypehistory.reload_data()

    def init_form(self):  

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_File_Type_Histories_Widget] : init_form"))

        if(self.filetype == CSV_EXPORT)         : filetitle  =   "CSV"
        elif(self.filetype == EXCEL_EXPORT)     : filetitle  =   "Excel"
        elif(self.filetype == JSON_EXPORT)      : filetitle  =   "JSON"
        elif(self.filetype == HTML_EXPORT)      : filetitle  =   "HTML"
        elif(self.filetype == SQLTABLE_EXPORT)  : filetitle  =   "SQLTable"
        else :                                        filetitle  =   "Custom"

        from PyQt5.QtWidgets import QLabel
        export_file_type_label   =   QLabel()
        export_file_type_label.setText("\nPandas " + str(filetitle) + " Export History\n")
        export_file_type_label.setAlignment(Qt.AlignCenter)
        export_file_type_label.resize(960,90)
        export_file_type_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        
        self.exportfiletypehistory        =   DataExportTypesHistorysTable([self.filetype])
        self.exportfiletypehistory.doubleClicked.connect(self.select_export_callback)
        
        new_height  =   45 + (self.exportfiletypehistory.num_rows * DEFAULT_ROW_HEIGHT)

        self.exportfiletypehistory.setMinimumHeight(new_height)
        self.exportfiletypehistory.setMaximumHeight(new_height)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_File_Type_Histories_Widget] : init_form : table built"))

        from PyQt5.QtWidgets import QLabel
        export_file_type_notes_label   =   QLabel()
        export_file_type_notes_label.setText("\nDouble Click on DEL column to select exports to delete from the history. Double Click on the df Title column to use the export for next parms.\n")
        export_file_type_notes_label.setAlignment(Qt.AlignCenter)
        export_file_type_notes_label.resize(960,50)
        export_file_type_notes_label.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")

        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        ftypes_button         =   QPushButton()     
        ftypes_button.setText("Delete\nSelected\nExport History(s)")
        ftypes_button.setFixedSize(300,90)
        ftypes_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        ftypes_button.clicked.connect(self.delete_export_callback) 
        
        ftypes_button1        =   QPushButton()     
        ftypes_button1.setText("Return")
        ftypes_button1.setFixedSize(300,90)
        ftypes_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        ftypes_button1.clicked.connect(self.return_export_callback) 
        
        from PyQt5.QtWidgets import QHBoxLayout
        ftypesbutonsLayout  =   QHBoxLayout()
        ftypesbutonsLayout.addWidget(ftypes_button)
        ftypesbutonsLayout.addWidget(ftypes_button1)
        ftypesbutonsLayout.setAlignment(Qt.AlignHCenter)

        from PyQt5.QtWidgets import QVBoxLayout
        self.exportfiletypesLayout     =   QVBoxLayout()
        self.exportfiletypesLayout.addWidget(export_file_type_label)
        self.exportfiletypesLayout.addWidget(self.exportfiletypehistory)
        self.exportfiletypesLayout.addWidget(export_file_type_notes_label)
        self.exportfiletypesLayout.addLayout(ftypesbutonsLayout)
        self.exportfiletypesLayout.addStretch()

        self.setLayout(self.exportfiletypesLayout)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_FILE_TYPES")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Data_Export_File_Type_Histories_Widget] : init_form : end"))


# -----------------------------------------------------------------#
# -         Data Export file Type Histories Widget end            -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -         Data Export file Type Histories objects end           -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Data Export with parms objects                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -          Table view and Model for Export Details              -#
# -----------------------------------------------------------------#

class DataExportDetailsModel(QtCore.QAbstractTableModel):
    def __init__(self, importdata, colheaders):

        super(DataExportDetailsModel, self).__init__()
        self._data          =   importdata
        self.column_names   =   colheaders

    def reload_data(self,importdata) :
        self._data = importdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)

    def data(self, index, role):
        
        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list

            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            elif(column == 1) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)


class DataExportDetailsTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : init",dfparms))


        self.mainLayout         =   None
        self.model              =   None

        self.filetype           =   dfparms[0]
        self.filename           =   dfparms[1]

        self.init_tableview()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : init_tableview end"))

    def reload_data(self,reloadparms) :
        
        self.filetype          =   reloadparms[0]
        self.filename          =   reloadparms[1]
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : reload_data : filetype : dftitle : ",self.filetype,self.filename))

        exportdetailsdata       =   self.load_export_details_data()
        self.num_rows           =   len(exportdetailsdata)
        self.model.reload_data(exportdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (25 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : reload_data : end : "))

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : init_tableview",self.filetype,self.filename))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportdetailsdata     =   self.load_export_details_data()
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
           add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : column headers : ",self.column_headers))

        if(1):#self.model is None) :
            self.model = DataExportDetailsModel(exportdetailsdata  ,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
           add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : model loaded "))

        self.num_rows   =   len(exportdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   35 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (25 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(exportdetailsdata)
        for row in range(self.num_rows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)

    # -----------------------------------------------------------------#
    # -                    load the table data                        -#
    # -----------------------------------------------------------------#
    def load_export_details_data(self):

        dftitleParms    =   [self.filetype,self.filename]
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : load_export_details_data ",self.filetype,self.filename))

        try :

            from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
            exportValues    =  get_export_details_values(dftitleParms) 

        except Exception as e:
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[load_export_details_data] corrupt : " + str(self.filename)
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            return()


        ptitles     =   exportValues[0]
        pvals       =   exportValues[1]

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : \n      ptitles : ",ptitles,"\n      pvals : ",pvals))

        if( (len(ptitles) > 0) and (len(pvals) > 0) and (len(ptitles) == len(pvals))) :

            data    =   []

            for i in range(len(ptitles)) :

                data_row    =   []
                data_row.append(str(ptitles[i]))
                data_row.append(str(pvals[i]))

                data.append(data_row)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[DataExportDetailsTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("DataExportWidgets",print_to_string("        [",j,"] : ",data[j]))

        self.column_headers     =   ["Parameter Name","Parameter Value"]
        self.column_widths      =   [300,675]

        return(data)
    
# -----------------------------------------------------------------#
# -          Tableview and Model for Export Details end           -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -              Export with Parms Display Widget                 -#
# -----------------------------------------------------------------#
class Export_With_Parms_Widget(QtWidgets.QWidget):
    """            
    #------------------------------------------------------------------
    #   Import parms and commands
    #
    #   Parms       -   dftitle imported
    #
    #------------------------------------------------------------------
    """

    def __init__(self,  importparms, **kwargs):  

        super().__init__()
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget] ",importparms[1],importparms[2]))

        self.parent             =   importparms[0]
        self.filetype           =   importparms[1]
        self.filename           =   importparms[2]

        self.init_form()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget] : done"))
    
    def reload_table_data(self,reloadparms) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][reload_table_data] : reloadparms : \n    ",reloadparms))

        self.filetype   =   reloadparms[0]
        self.filename   =   reloadparms[1]

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget] : filetype : filename : ",self.filetype,self.filename))

        parms   =   [self.filetype,self.filename]
        self.exportdetailsTable.reload_data(parms)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][reload_table_data] : end : "))


    def init_form(self):  

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout
        self.exportparmsLayout        =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        export_file_type_label   =   QLabel()
        export_file_type_label.setText("\n\nExport Details\n")
        export_file_type_label.setAlignment(Qt.AlignCenter)
        export_file_type_label.resize(960,90)
        export_file_type_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        exportparms                   =   [self.filetype,self.filename] 
        self.exportdetailsTable       =   DataExportDetailsTable(exportparms)

        # buttons for dissplay import parms
        from PyQt5.QtWidgets import QPushButton
        parms_button         =   QPushButton()     
        parms_button.setText("Export\nWith Parms\nAbove")
        parms_button.setFixedSize(300,90)
        parms_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button.clicked.connect(self.export_with_parms) 
        
        parms_button1        =   QPushButton()     
        parms_button1.setText("Return")
        parms_button1.setFixedSize(300,90)
        parms_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button1.clicked.connect(self.return_from_export_parms) 
        
        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.addWidget(parms_button1)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)

        self.exportparmsLayout.addWidget(export_file_type_label)
        self.exportparmsLayout.addWidget(self.exportdetailsTable)
        self.exportparmsLayout.addLayout(parmsbutonsLayout)
        self.exportparmsLayout.addStretch()

        self.setLayout(self.exportparmsLayout)


    # -----------------------------------------------------------------#
    # -             display Export with parms methods                 -#
    # -----------------------------------------------------------------#
    def export_with_parms(self) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][export_with_parms]",self.filetype,self.filename))

        dftitleParms    =   [self.filetype,self.filename]

        from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
        exportValues    =  get_export_details_values(dftitleParms) 
        ptitles         =   exportValues[0]
        pvals           =   exportValues[1]
       
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][export_with_parms]\n    [ptitles] : ",ptitles,"\n    [pvalues] : ",pvals))
    
        if(self.filetype == CSV_EXPORT) :
            export_labels   =   pandas_export_csv_labelList[:6]
        elif(self.filetype == EXCEL_EXPORT) :
            export_labels   =   pandas_export_excel_labelList[:7]
        elif(self.filetype == JSON_EXPORT) :
            export_labels   =   pandas_export_json_labelList[:5]
        elif(self.filetype == HTML_EXPORT) :
            export_labels   =   pandas_export_html_labelList[:6]
        elif(self.filetype == SQLTABLE_EXPORT) :
            export_labels   =   pandas_export_sqltable_labelList[:9]
        elif(self.filetype == CUSTOM_EXPORT) :
            export_labels   =   custom_export_labelList[:2]

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][export_with_parms] : export_labels : \n    ",export_labels))

        from dfcleanser.sw_utilities.dfc_qt_model import build_cfg_parms_from_history
        if(self.filetype == SQLTABLE_EXPORT) :
            export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=False) 
        else : 
            if(self.filetype == CUSTOM_EXPORT) :
                export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=False) 
            else :     
                export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=True)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[export_with_parms]  cfg_parms :\n    ",export_cfg_parms))

        exportParms             =   [self.filetype , export_cfg_parms[0], export_cfg_parms]
        self.parent.display_export_form(exportParms)

    def return_from_export_parms(self) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_PARMS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_With_Parms_Widget][return_from_export_parms]"))

        self.parent.display_export_histories()


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              Data Export with parms objects end               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                    Export Status Widget                       -#
# -----------------------------------------------------------------#
class Export_Status_Widget(QtWidgets.QWidget):

    def __init__(self,  exportparms, **kwargs):  

        super().__init__()
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] ",exportparms[1],exportparms[2],exportparms[3]))

        self.parent             =   exportparms[0]
        self.filetype           =   exportparms[1]
        self.filename           =   exportparms[2]
        self.dftitle            =   exportparms[3]

        self.init_form()

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : done"))
    
    def reload_table_data(self,reloadparms) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] reload_table_data : reloadparms : ",reloadparms))

        self.filetype   =   reloadparms[0]
        self.filename   =   reloadparms[1]
        self.dftitle    =   reloadparms[2]

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : filetype : dftitle : filename : ",self.filetype,self.dftitle,self.filename))

        if(self.filetype == 4) :
            reload_parms    =   [self.filetype,self.filename,None]
        else :
            reload_parms    =   [self.filetype,self.dftitle,None]

        self.exportparmsTable.reload_data(reload_parms)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.num_rows_label.setText("\n\n" + str(self.dftitle) + " : Num Rows : " + str(len(df)))
        self.num_cols_label.setText(str(self.dftitle) + " : Num Cols : " + str(len(df.columns)))


    def init_form(self):  

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : init_form"))

        from PyQt5.QtWidgets import QVBoxLayout
        self.exportstatusLayout      =   QVBoxLayout()

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_DETAILS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : df"))

        from PyQt5.QtWidgets import QLabel
        self.num_rows_label    =   QLabel()
        self.num_rows_label.setText("\n\n" + str(self.dftitle) + " : Num Rows : " + str(len(df)))
        self.num_rows_label.setAlignment(Qt.AlignCenter)
        self.num_rows_label.resize(960,50)
        self.num_rows_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        self.num_cols_label    =   QLabel()
        self.num_cols_label.setText(str(self.dftitle) + " : Num Cols : " + str(len(df.columns)))
        self.num_cols_label.setAlignment(Qt.AlignCenter)
        self.num_cols_label.resize(960,50)
        self.num_cols_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
       
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_DETAILS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : labels"))

        self.exportstatusLayout.addWidget(self.num_rows_label)
        self.exportstatusLayout.addWidget(self.num_cols_label)

        if(self.filetype == 4) :
             exportparms                     =   [self.filetype,self.filename]
        else :    
            exportparms                     =   [self.filetype,self.filename]
             
        self.exportparmsTable           =   DataExportDetailsTable(exportparms)
        self.exportstatusLayout.addWidget(self.exportparmsTable)

        # buttons for dissplay import status
        from PyQt5.QtWidgets import QPushButton
        
        parms_button        =   QPushButton()     
        parms_button.setText("Return")
        parms_button.setFixedSize(300,90)
        parms_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button.clicked.connect(self.return_from_export_status) 
        
        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT_DETAILS")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget] : buttons built"))

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)
        
        self.exportstatusLayout.addLayout(parmsbutonsLayout)
        self.exportstatusLayout.addStretch()

        self.setLayout(self.exportstatusLayout)


    def return_from_export_status(self) :

        if(is_debug_on(DataExport_ID,"DEBUG_DATA_EXPORT")) :
            add_debug_to_log("DataExportWidgets",print_to_string("[Export_Status_Widget][return_from_export_status]"))

        self.parent.display_export_histories()
       


# -----------------------------------------------------------------#
# -               end Export Status Widget                        -#
# -----------------------------------------------------------------#














