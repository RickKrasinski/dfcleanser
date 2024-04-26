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

DEBUG_DATA_EXPORT                   =   True
DEBUG_DATA_EXPORT_FILE_TYPES        =   False
DEBUG_DATA_EXPORT_HISTORY           =   False
DEBUG_DATA_EXPORT_PARMS             =   False


DEBUG_DATA_IMPORT_DFS_HISTORY       =   False

DEBUG_DATA_EXPORT_DETAILS           =   False

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
        
        if(DEBUG_DATA_EXPORT) :
            print("  [EDataExport_Export_Widget] ")

        self.parent     =   exportparms[0]

        self.init_form()

        if(DEBUG_DATA_EXPORT) :
            print("  [DataExport_Export_Widget] : done")

    def reload_data(self) :

        self.export_histories.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_EXPORT) :
            print("[DataExport_Export_Widget]  init_form")

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

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[DataExport_Export_Widget] init from end")

    
    # -----------------------------------------------------------------#
    # -            display data export histories methods              -#
    # -----------------------------------------------------------------#

    def select_export_type_history(self) :

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[display_export_histories] select_export_type_history")


        for idx in self.export_histories.exportHistory.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[display_export_histories] select_export_type_history",row_number,column_number)

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
            #print("data model Qt.DisplayRole",row,column)
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
        
        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("\n  [DataExportsHistoryTable] ")

        self.mainLayout         =   None
        self.model              =   None

        self.init_tableview()

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [DataExportsHistoryTable] : end")


    def reload_data(self):
        
        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [DataExportsHistoryTable] : reload_data")

        export_history_data     =   self.load_exportHistory_data()
        self.model.reload_data(export_history_data)
   
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [DataExportsHistoryTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        historydata     =   self.load_exportHistory_data()

        if(self.model is None) :
            self.model = DataExportsHistoryModel(historydata, self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_EXPORT_HISTORY) :
           print("  [DataExportsHistoryTable] : model loaded")

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

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [DataExportsHistoryTable] : load_exportHistory_data ")

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

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("    [DataExportsHistoryTable] : data")
            for j in range(len(data)) :
                print("  [",j,"]",data[j])

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

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[Data_Export_Histories_Widget] end")

    def reload_data(self) :

        self.exportHistory.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[Data_Export_Histories_Widget]  init_form")


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

        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("[Data_Export_Histories_Widget] init from end")

    """
    def select_export_type_callback(self):
        
        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [Data_Export_Histories_Widget] : select_export_type_callback")

        row_number      =   None
        column_number   =   None

        for idx in self.exportHistory.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DATA_EXPORT_HISTORY) :
            print("  [Data_Export_Histories_Widget] : select_export_type_callback ",row_number,column_number)

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_DATA_EXPORT_HISTORY) :    
            print("  [Data_Export_Histories_Widget] : select_export_type_callback : colname [",cell,"]")

        self.export_type    =   cell
    """


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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("\n[DataExportTypesHistorysTable] : init",self.file_type)

        self.init_tableview()

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : done")

    def reload_data(self):
        
        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("  [DataExportHistoryExportsTable] : reload_data")

        export_file_type_history_data     =   self.load_export_type_history_data()
        self.model.reload_data(export_file_type_history_data)
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : init_tableview",self.file_type)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportsHistorydata     =   self.load_export_type_history_data()

        if(self.model is None) :
            self.model = DataExportTypesHistorysModel(exportsHistorydata ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
           print("[DataExportTypesHistorysTable] : model loaded : headers : ",self.column_headers)

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

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : load_export_type_history_data ")

        from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
        df_titles   =   ExportHistory.get_df_titles_for_file_type(self.file_type)

        df_file_names   =   []

        for i in range(len(df_titles)) :
            
            from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
            history_entry   =   ExportHistory.get_df_title_entry(self.file_type,df_titles[i])

            df_file_names.append(str(history_entry.get_full_parms()[0])) 

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : load_export_type_history_data  : df_file_names  \n  ",df_file_names)

        data    =   []

        for i in range(len(df_titles)) :

            data_row    =   []
            data_row.append(" ")
            data_row.append(str(df_file_names[i]))
            data_row.append(str(df_titles[i]))

            data.append(data_row)

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : data",len(data))
            for j in range(len(data)) :
                print("    [",j,"] : ",data[j])

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

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("\n[Data_Export_File_Type_Histories_Widget]",histparms)

        self.parent                     =   histparms[0]
        self.filetype                   =   histparms[1]
        self.select_export_callback     =   histparms[2]
        self.delete_export_callback     =   histparms[3]
        self.return_export_callback     =   histparms[4]

        self.init_form()

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[Data_ExIport_File_Type_Histories_Widget] : end")
    
    def reload_data(self) :

        self.exportfiletypehistory.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form")

        import dfcleanser.Qt.data_export.DataExportModel as DEM

        if(self.filetype == DEM.CSV_EXPORT)         : filetitle  =   "CSV"
        elif(self.filetype == DEM.EXCEL_EXPORT)     : filetitle  =   "Excel"
        elif(self.filetype == DEM.JSON_EXPORT)      : filetitle  =   "JSON"
        elif(self.filetype == DEM.HTML_EXPORT)      : filetitle  =   "HTML"
        elif(self.filetype == DEM.SQLTABLE_EXPORT)  : filetitle  =   "SQLTable"
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

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form : table built")

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

        if(DEBUG_DATA_EXPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form : end")


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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("\n    [DataExportDetailsTable] : init",dfparms)


        self.mainLayout         =   None
        self.model              =   None

        self.filetype           =   dfparms[0]
        self.filename           =   dfparms[1]

        self.init_tableview()

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("    [DataExportDetailsTable] : init_tableview end")

    def reload_data(self,reloadparms) :
        
        self.filetype          =   reloadparms[0]
        self.filename          =   reloadparms[1]
        
        if(DEBUG_DATA_EXPORT_PARMS) :
            print("    [DataExportDetailsTable] : reload_data : filetype : dftitle : ",self.filetype,self.filename)

        exportdetailsdata       =   self.load_export_details_data()
        self.num_rows           =   len(exportdetailsdata)
        self.model.reload_data(exportdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (25 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("    [DataExportDetailsTable] : reload_data : end : ")

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("    [DataExportDetailsTable] : init_tableview",self.filetype,self.filename)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportdetailsdata     =   self.load_export_details_data()
        
        if(DEBUG_DATA_EXPORT_PARMS) :
           print("    [DataExportDetailsTable] : column headers : ",self.column_headers)

        if(1):#self.model is None) :
            self.model = DataExportDetailsModel(exportdetailsdata  ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_EXPORT_PARMS) :
           print("    [DataExportDetailsTable] : model loaded ")

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
        
        if(DEBUG_DATA_EXPORT) :
            print("   [DataExportDetailsTable] : load_export_details_data ",self.filetype,self.filename)

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

        if(DEBUG_DATA_EXPORT) :
            print("    [DataExportDetailsTable] : \n      ptitles : ",ptitles,"\n      pvals : ",pvals)

        if( (len(ptitles) > 0) and (len(pvals) > 0) and (len(ptitles) == len(pvals))) :

            data    =   []

            for i in range(len(ptitles)) :

                data_row    =   []
                data_row.append(str(ptitles[i]))
                data_row.append(str(pvals[i]))

                data.append(data_row)

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("    [DataExportDetailsTable] : data")
            for j in range(len(data)) :
                print("        [",j,"] : ",data[j])

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
        
        if(DEBUG_DATA_EXPORT) :
            print("  [Export_With_Parms_Widget] ",importparms[1],importparms[2])

        self.parent             =   importparms[0]
        self.filetype           =   importparms[1]
        self.filename           =   importparms[2]

        self.init_form()

        if(DEBUG_DATA_EXPORT) :
            print("  [Export_With_Parms_Widget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_EXPORT) :
            print("  [Export_With_Parms_Widget][reload_table_data] : reloadparms : \n    ",reloadparms)

        self.filetype   =   reloadparms[0]
        self.filename   =   reloadparms[1]

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("  [Export_With_Parms_Widget] : filetype : filename : ",self.filetype,self.filename)

        parms   =   [self.filetype,self.filename]
        self.exportdetailsTable.reload_data(parms)

        if(DEBUG_DATA_EXPORT) :
            print("  [Export_With_Parms_Widget][reload_table_data] : end : ")


    def init_form(self):  

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("  [Export_With_Parms_Widget][init_form]")

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

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("\n  [Export_With_Parms_Widget][export_with_parms]",self.filetype,self.filename)

        dftitleParms    =   [self.filetype,self.filename]

        from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
        exportValues    =  get_export_details_values(dftitleParms) 
        ptitles         =   exportValues[0]
        pvals           =   exportValues[1]
       
        if(DEBUG_DATA_EXPORT_PARMS) :
            print("  [Export_With_Parms_Widget][export_with_parms]\n    [ptitles] : ",ptitles,"\n    [pvalues] : ",pvals)
    
        import dfcleanser.Qt.data_export.DataExportModel as DEM
        
        if(self.filetype == DEM.CSV_EXPORT) :
            export_labels   =   DEM.pandas_export_csv_labelList[:6]
        elif(self.filetype == DEM.EXCEL_EXPORT) :
            export_labels   =   DEM.pandas_export_excel_labelList[:7]
        elif(self.filetype == DEM.JSON_EXPORT) :
            export_labels   =   DEM.pandas_export_json_labelList[:5]
        elif(self.filetype == DEM.HTML_EXPORT) :
            export_labels   =   DEM.pandas_export_html_labelList[:6]
        elif(self.filetype == DEM.SQLTABLE_EXPORT) :
            export_labels   =   DEM.pandas_export_sqltable_labelList[:9]
        elif(self.filetype == DEM.CUSTOM_EXPORT) :
            export_labels   =   DEM.custom_export_labelList[:2]

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("  [Export_With_Parms_Widget][export_with_parms] : export_labels : \n    ",export_labels)

        from dfcleanser.sw_utilities.dfc_qt_model import build_cfg_parms_from_history
        if(self.filetype == DEM.SQLTABLE_EXPORT) :
            export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=False) 
        else : 
            if(self.filetype == DEM.CUSTOM_EXPORT) :
                export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=False) 
            else :     
                export_cfg_parms    =   build_cfg_parms_from_history(ptitles,pvals,export_labels,ADDL_PARMS=True)

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("  [export_with_parms]  cfg_parms :\n    ",export_cfg_parms)

        exportParms             =   [self.filetype , export_cfg_parms[0], export_cfg_parms]
        self.parent.display_export_form(exportParms)

    def return_from_export_parms(self) :

        if(DEBUG_DATA_EXPORT_PARMS) :
            print("[Export_With_Parms_Widget][return_from_export_parms]")

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
        
        if(DEBUG_DATA_EXPORT) :
            print("  [Export_Status_Widget] ",exportparms[1],exportparms[2],exportparms[3])

        self.parent             =   exportparms[0]
        self.filetype           =   exportparms[1]
        self.filename           =   exportparms[2]
        self.dftitle            =   exportparms[3]

        self.init_form()

        if(DEBUG_DATA_EXPORT) :
            print("[Export_Status_Widget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_EXPORT) :
            print("\n[Export_Status_Widget] reload_table_data : reloadparms : ",reloadparms)

        self.filetype   =   reloadparms[0]
        self.filename   =   reloadparms[1]
        self.dftitle    =   reloadparms[2]

        if(DEBUG_DATA_EXPORT) :
            print("\n[Export_Status_Widget] : filetype : dftitle : filename : ",self.filetype,self.dftitle,self.filename)

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

        if(DEBUG_DATA_EXPORT) :
            print("[Export_Status_Widget] : init_form")

        from PyQt5.QtWidgets import QVBoxLayout
        self.exportstatusLayout      =   QVBoxLayout()

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)

        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("[Export_Status_Widget] : df")

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
       
        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("[Export_Status_Widget] : labels")

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
        
        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("[Export_Status_Widget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)
        
        self.exportstatusLayout.addLayout(parmsbutonsLayout)
        self.exportstatusLayout.addStretch()

        self.setLayout(self.exportstatusLayout)


    def return_from_export_status(self) :

        if(DEBUG_DATA_EXPORT) :
            print("[Export_Status_Widget][return_from_export_status]")

        self.parent.display_export_histories()
       


# -----------------------------------------------------------------#
# -               end Export Status Widget                        -#
# -----------------------------------------------------------------#










"""
    
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       HTML Import Objects                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -               Table Model for HTML Import dfs                 -#
# -----------------------------------------------------------------#

class DataImportHTMLdfsModel(QtCore.QAbstractTableModel):
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
            #print("data model Qt.DisplayRole",row,column)
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

# -----------------------------------------------------------------#
# -               Table View for HTML Import dfs                  -#
# -----------------------------------------------------------------#

class DataImportHTMLdfsTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        if(DEBUG_DATA_IMPORT) :
            print("\n[DataImportHTMLdfsTable] : init",dfparms)


        self.mainLayout         =   None
        self.model              =   None

        self.dfslist            =   dfparms[0]

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataImportHTMLdfsTable] : init_tableview end")

    def reload_data(self,dfslist) :
        
        self.dfslist            =   dfslist
        
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : reload_data : dfslist : ",self.dfslist)

        jsondfsdata             =   self.load_html_dfs_data()
        self.num_rows           =   len(jsondfsdata)
        self.model.reload_data(jsondfsdata)
        
        if(self.num_rows < 25) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (25 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : reload_data : end : ")

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        html_dfs_data     =   self.load_html_dfs_data()
        
        if(DEBUG_DATA_IMPORT) :
           print("[DataImportHTMLdfsTable] : column headers : ",self.column_headers)

        if(self.model is None) :
            self.model = DataExportDetailsModel(html_dfs_data  ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT) :
           print("[DataImportHTMLdfsTable] : model loaded ")

        self.num_rows   =   len(html_dfs_data)
        
        if(self.num_rows < 25) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (25 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(html_dfs_data)
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
    def load_html_dfs_data(self):

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : load_html_dfs_data ")

        data    =   []

        for i in range(len(self.dfslist)) :

            data_row    =   []
            data_row.append(str(i))
            data_row.append(str(len(self.dfslist[i])))
        
            dfcols      =   list(self.dfslist[i].columns)
            data_row.append(str(len(dfcols)))

            dfcolslist  =   "[ "
            for j in range(len(dfcols)) :
                dfcolslist  =   dfcolslist + str(dfcols[j])
                if(j < (len(dfcols) - 1)) :
                    dfcolslist  =   dfcolslist + ", "
                else :
                    dfcolslist  =   dfcolslist + " ]"

            data_row.append(dfcolslist)

            data.append(data_row) 
    
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["Table","Rows","Columns","Columns List"]
        self.column_widths      =   [100,140,140,620]

        return(data)
    
# -----------------------------------------------------------------#
# -                  Widget for HTML Import dfs                   -#
# -----------------------------------------------------------------#

class DataImportHTMLdfsWidget(QtWidgets.QWidget):

    def __init__(self,  importparms, **kwargs):  

        super().__init__()
        
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] ")

        self.dfslist                =   importparms[0]
        self.select_table_action    =   importparms[1]
        self.return_action          =   importparms[2]
        self.help_action            =   importparms[3]

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [self.dfslist] \n    ",self.dfslist)

        self.init_form()

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_IMPORT) :
            print("\n[DataImportHTMLdfsWidget] reload_table_data : reloadparms : ",reloadparms)

        self.dfslist   =   reloadparms[0]
 
        self.importhtmldfsTable.reload_data([self.dfslist])
 
    def init_form(self):  

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : init_form")

        from PyQt5.QtWidgets import QVBoxLayout
        self.importhtmldfsLayout      =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.title_label    =   QLabel()
        self.title_label.setText("\n\nRetrieved HTML Tables")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(960,50)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : labels")

        self.importhtmldfsLayout.addWidget(self.title_label)

        importparms                     =   [self.dfslist] 
        self.importhtmldfsTable         =   DataImportHTMLdfsTable(importparms)
        self.importhtmldfsTable.doubleClicked.connect(self.select_table_action)

        self.importhtmldfsLayout.addWidget(self.importhtmldfsTable)

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : dfs table")

        from PyQt5.QtWidgets import QLabel
        self.note_label    =   QLabel()
        self.note_label.setText("\nTo get details on a specific table and import the table into a df click on the Table Id field.")
        self.note_label.setAlignment(Qt.AlignCenter)
        self.note_label.resize(960,50)
        self.note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")
       
        self.importhtmldfsLayout.addWidget(self.note_label)

        # buttons for dissplay import status
        from PyQt5.QtWidgets import QPushButton
        
        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(300,50)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_action) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(300,50)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_action) 
        
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(return_button)
        parmsbutonsLayout.addWidget(help_button)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)
        
        self.importhtmldfsLayout.addLayout(parmsbutonsLayout)
        self.importhtmldfsLayout.addStretch()

        self.setLayout(self.importhtmldfsLayout)




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                QT Widget to save json df form                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class DataImportHTMLdfSaveWidget(QtWidgets.QWidget) :


    def __init__(self,  dfparms, **kwargs):  

        super().__init__()

        self.df                             =   dfparms[0]
        self.save_as_json_action            =   dfparms[1]
        self.return_action                  =   dfparms[2]
        self.help_action                    =   dfparms[3]       
        
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfSaveWidget]")
        
        self.init_content()

    def reset_form_df(self,reload_parms) :

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfSaveWidget][]")

        self.df     =   reload_parms[0]

    def init_content(self) :

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfSaveWidget][init_content]")

        import dfcleanser.Qt.data_import.DataImportModel as DIM

        formParms           =   [DIM.pandas_import_html_json_id,DIM.pandas_import_html_json_idList,DIM.pandas_import_html_json_labelList,DIM.pandas_import_html_json_typeList,DIM.pandas_import_html_json_placeholderList,DIM.pandas_import_html_json_reqList] 
        comboMethods        =   []
        comboList           =   []
        cfg_parms           =   []
        file_methods        =   [self.select_json_file]
        button_methods      =   [self.save_as_json_action,self.return_action,self.help_action]

        formParms.append(comboList)
        formParms.append(comboMethods)            
        formParms.append(file_methods)
        formParms.append(button_methods)            
        formParms.append(cfg_parms)            
        formParms.append("Save html df")
        formParms.append(600) 

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.save_json_df_form     =   dfcleanser_input_form_Widget(formParms)
        
        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][init_content] form built : ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.save_json_df_formWidgetLayout     =   QVBoxLayout()
        self.save_json_df_formWidgetLayout.addWidget(self.save_json_df_form)
        self.save_json_df_formWidgetLayout.addStretch()

        self.setLayout(self.save_json_df_formWidgetLayout)

        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][init_content] end")

    def select_json_file(self) :

        if(DEBUG_DATA_IMPORT) :
            print("  [DataImportHTMLdfSaveWidget][select_json_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.save_json_df_form.set_form_input_value_by_index(1,fname[0])        
   

# -----------------------------------------------------------------#
# -              QT Widget to save json df form end               -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  HTML Import Objects end                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


    

# -----------------------------------------------------------------#
# -                   Import HTML Widgets end                     -#
# -----------------------------------------------------------------#





# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    DataImport Widgets end                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

"""





