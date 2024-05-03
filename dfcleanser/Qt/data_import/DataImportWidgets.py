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

DEBUG_DATA_IMPORT_FILE_TYPES        =   False
DEBUG_DATA_IMPORT_HISTORY           =   False
DEBUG_DATA_EXPORT_HISTORY           =   False
DEBUG_DATA_IMPORT_PARMS             =   False


DEBUG_DATA_IMPORT_DFS_HISTORY       =   False
DEBUG_DATA_IMPORT                   =   False
DEBUG_DATA_IMPORT_DETAILS           =   False

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
# -           DataImport Tableviews and Models                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -           Table view and Model for Import History             -#
# -----------------------------------------------------------------#

class DataImportHistoryImportsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(DataImportHistoryImportsModel, self).__init__()
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
                return(Qt.AlignLeft)
            elif(column == 1) :
                return(Qt.AlignCenter)
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
# -                Table view for Import History                  -#
# -----------------------------------------------------------------#
class DataImportHistoryImportsTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   None

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("\n[DataImportHistoryImportsTable] : init")

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("[DataImportHistoryImportsTable] : end")


    def reload_data(self):
        
        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryImportsTable] : reload_data")

        import_history_data     =   self.load_import_history_data()
        self.model.reload_data(import_history_data)

    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryImportsTable] : init_tableview",self.dftitle)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        importsHistorydata     =   self.load_import_history_data()
        
        if(DEBUG_DATA_IMPORT_HISTORY) :
           print("  [DataImportHistoryImportsTable] :headers",self.column_headers)

        if(self.model is None) :
            self.model = DataImportHistoryImportsModel(importsHistorydata ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_HISTORY) :
           print("  [DataImportHistoryImportsTable] : model loaded")

        self.num_rows   =   len(importsHistorydata)
        
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
        nrows = len(importsHistorydata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_import_history_data(self):

        import_file_types    =   ["Pandas CSV Imports","Pandas FWF Imports","Pandas EXCEL Imports","Pandas JSON Imports","Pandas HTML Imports",
                                  "Pandas SQL TABLE Imports","Pandas SQL QUERY Imports","Custom Imports","Pandas XML Imports"]
        
        import_file_ids     =   [0,1,2,3,4,5,6,7,8]
       

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryImportsTable] : load_import_history_data ")

        file_type_totals    =   []

        for i in range(len(import_file_types)) :

            from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
            df_titles   =   ImportHistory.get_df_titles_for_file_type(import_file_ids[i])

            if(not (df_titles is None)) :
                file_type_totals.append(len(df_titles))
            else :
                file_type_totals.append(0)

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryImportsTable] : load_import_history_data  : file_type_totals  ",file_type_totals)

        data    =   []

        for i in range(len(import_file_types)) :

            data_row    =   []
            data_row.append(str(import_file_types[i]))
            data_row.append(str(file_type_totals[i]))

            data.append(data_row)

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryImportsTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["Import Type","Import Count"]
        self.column_widths      =   [360,100]

        return(data)

# -----------------------------------------------------------------#
# -         Table view and Model for Import History end           -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -           Table view and Model for Export History             -#
# -----------------------------------------------------------------#

class DataImportHistoryExportsModel(QtCore.QAbstractTableModel):
    def __init__(self, exportHistorydata, col_headers):

        super(DataImportHistoryExportsModel, self).__init__()
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
                return(Qt.AlignCenter)

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
class DataImportHistoryExportsTable(QtWidgets.QTableView):

    def __init__(self, **kwargs):  

        super().__init__()
        
        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("\n[DataImportHistoryExportsTable] ")

        self.mainLayout         =   None
        self.model              =   None

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("[DataImportHistoryExportsTable] : end")


    def reload_data(self):
        
        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryExportsTable] : reload_data")

        export_history_data     =   self.load_exportHistory_data()
        self.model.reload_data(export_history_data)
   
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryExportsTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        historydata     =   self.load_exportHistory_data()

        if(self.model is None) :
            self.model = DataImportHistoryExportsModel(historydata, self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_HISTORY) :
           print("  [DataImportHistoryExportsTable] : model loaded")

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

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryExportsTable] : load_exportHistory_data ")

        export_file_types    =   ["Pandas CSV Exports","Pandas EXCEL Exports","Pandas JSON Exports",
                                  "Pandas HTML Exports","Pandas SQL TABLE Exports","Custom Exports","Pandas XML Exports"]

        export_file_ids     =    [0,1,2,3,4,5,6]

        file_type_totals    =   []

        for i in range(len(export_file_types)) :

            from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
            df_titles   =   ExportHistory.get_df_titles_for_file_type(export_file_ids[i])

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

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryExportsTable] : data")
            for j in range(len(data)) :
                print("  [",j,"]",data[j])

        self.column_headers     =   ["Export Type","Export Count"]
        self.column_widths      =   [360,98]

        return(data)

# -----------------------------------------------------------------#
# -         Table view and Model for Export History end           -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -        Table view and Model for ImportTypes History           -#
# -----------------------------------------------------------------#

class DataImportTypesHistorysModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(DataImportTypesHistorysModel, self).__init__()
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

                #if( (index.column() == 0) and (retval == "X") ) :

                #    qtdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
                #    icon_name = qtdir +"\checkkmark.png"
                #    checkmark_icon  =   QtGui.QIcon(icon_name)

                #    retval  =  checkmark_icon 

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

            if(column == 0) :
                if(self._data[row][column] == "X") :
                    bgcolor = QtGui.QBrush(QColor(102, 255, 102))  
                else :  
                    bgcolor = QtGui.QBrush(QtCore.Qt.white)
            elif(column == 1):
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
# -             Table view for ImportTypes History                -#
# -----------------------------------------------------------------#
class DataImportTypesHistorysTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("\n[DataImportTypesHistorysTable] : dfparms",dfparms)

        self.mainLayout         =   None
        self.model              =   None

        self.file_type          =   dfparms[0]

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("\n[DataImportTypesHistorysTable] : init",self.file_type)

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataImportTypesHistorysTable] : init_tableview done")
    
    def reload_data(self):
        
        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("  [DataImportHistoryExportsTable] : reload_data")

        import_file_type_history_data     =   self.load_import_type_history_data()
        self.model.reload_data(import_file_type_history_data)
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataImportTypesHistorysTable] : init_tableview",self.file_type)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        importsHistorydata     =   self.load_import_type_history_data()
        
        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
           print("[DataImportTypesHistorysTable] : importsHistorydata : ",self.column_headers)


        if(self.model is None) :
            self.model = DataImportTypesHistorysModel(importsHistorydata ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
           print("[DataImportTypesHistorysTable] : model loaded : \n",importsHistorydata )

        self.num_rows   =   len(importsHistorydata)
        
        if(self.num_rows < 15) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(importsHistorydata)
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
    def load_import_type_history_data(self):

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataImportTypesHistorysTable] : load_import_type_history_data ")


        from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
        df_titles   =   ImportHistory.get_df_titles_for_file_type(self.file_type)

        if(len(df_titles) > 0) :

            df_file_names   =   []

            for i in range(len(df_titles)) :
            
                from dfcleanser.Qt.data_import.DataImportModel import ImportHistory
                history_entry   =   ImportHistory.get_df_title_entry(self.file_type,df_titles[i])

                from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT
                if(self.file_type == SQLTABLE_IMPORT) :
                    df_file_names.append(str(history_entry.get_full_parms()[0]) + " : " + str(history_entry.get_full_parms()[1]) + " : " + str(history_entry.get_full_parms()[2]))
                else :
                    df_file_names.append(str(history_entry.get_full_parms()[0])) 

            if(DEBUG_DATA_IMPORT_FILE_TYPES) :
                print("DataImportTypesHistorysTable] : load_import_type_history_data  : fdf_file_names  ",df_file_names)

            data    =   []

            for i in range(len(df_titles)) :

                data_row    =   []
                data_row.append(" ")
                data_row.append(str(df_titles[i]))
                data_row.append(str(df_file_names[i]))

                data.append(data_row)

            if(DEBUG_DATA_IMPORT_FILE_TYPES) :
                print("[DataImportTypesHistorysTable] : data\n ",data)

            from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT, SQLQUERY_IMPORT
            if(self.file_type == SQLTABLE_IMPORT) :
                self.column_headers     =   ["DEL","df Title","Database Table"] 
            elif(self.file_type == SQLQUERY_IMPORT) :
                self.column_headers     =   ["DEL","df Title","Database Query"] 
            else :
                self.column_headers     =   ["DEL","df Title","File Name"]


        else :

            data    =   []  
                
            data_row    =   []
            data_row.append(" ")
            data_row.append("no import file histories")
            data_row.append(" ")
            
            data.append(data_row)

            self.column_headers     =   ["DEL","df Title","File Name"]
            
        
        self.column_widths      =   [20,300,650]

        return(data)

# -----------------------------------------------------------------#
# -       Table view and Model for ImportTypes History end        -#
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
                return(Qt.AlignLeft)
            elif(column == 1) :
                return(Qt.AlignCenter)
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
# -             Table view for ExportTypes History                -#
# -----------------------------------------------------------------#
class DataExportTypesHistorysTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()
        
        self.mainLayout         =   None
        self.model              =   None

        self.file_type          =   dfparms[0]

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("\n[DataExportTypesHistorysTable] : init",self.file_type)

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : done")

    def reload_data(self):
        
        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("  [DataExportHistoryExportsTable] : reload_data")

        export_file_type_history_data     =   self.load_export_type_history_data()
        self.model.reload_data(export_file_type_history_data)
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : init_tableview",self.file_type)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportsHistorydata     =   self.load_export_type_history_data()

        if(self.model is None) :
            self.model = DataImportTypesHistorysModel(exportsHistorydata ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
           print("[DataExportTypesHistorysTable] : model loaded : headers : ",self.column_headers)

        self.num_rows   =   len(exportsHistorydata)
        
        if(self.num_rows < 15) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (15 * DEFAULT_ROW_HEIGHT)

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

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[DataExportTypesHistorysTable] : load_export_type_history_data ")

        from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
        df_titles   =   ExportHistory.get_df_titles_for_file_type(self.file_type)

        if(len(df_titles) > 0) :

            df_file_names   =   []

            for i in range(len(df_titles)) :
            
                from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
                history_entry   =   ExportHistory.get_df_title_entry(self.file_type,df_titles[i])

                df_file_names.append(str(history_entry.get_full_parms()[0])) 

            if(DEBUG_DATA_IMPORT_FILE_TYPES) :
                print("[DataExportTypesHistorysTable] : load_export_type_history_data  : df_file_names  \n  ",df_file_names)

            data    =   []

            for i in range(len(df_titles)) :

                data_row    =   []
                data_row.append(" ")
                data_row.append(str(df_file_names[i]))
                data_row.append(str(df_titles[i]))

                data.append(data_row)

            if(DEBUG_DATA_IMPORT_FILE_TYPES) :
                print("[DataExportTypesHistorysTable] : data",len(data))
                for j in range(len(data)) :
                    print("    [",j,"] : ",data[j])

        else :

            data    =   []

            data_row    =   []
            data_row.append(" ")
            data_row.append("no export file histories")
            data_row.append(" ")

            data.append(data_row)


        self.column_headers     =   ["DEL","df Title","File Name"]
        self.column_widths      =   [20,300,650]

        return(data)

# -----------------------------------------------------------------#
# -       Table view and Model for ExportTypes History end        -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Import Details Obkects                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -          Table view and Model for Import Details              -#
# -----------------------------------------------------------------#

class DataImportDetailsModel(QtCore.QAbstractTableModel):
    def __init__(self, importdata, colheaders):

        super(DataImportDetailsModel, self).__init__()
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


class DataImportDetailsTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        if(DEBUG_DATA_IMPORT) :
            print("    [DataImportDetailsTable][init] : \n      ",dfparms)

        self.mainLayout         =   None
        self.model              =   None

        self.file_type          =   dfparms[0]
        self.dftitle            =   dfparms[1]
        self.table_parms        =   dfparms[2]

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [DataImportDetailsTable][init] : tableview done")

    def reload_data(self,reloadparms) :
        
        self.file_type          =   reloadparms[0]
        self.dftitle            =   reloadparms[1]
        self.table_parms        =   reloadparms[2] 

        if(DEBUG_DATA_IMPORT) :
            print("   [DataImportDetailsTable][reload_data] : filetype : dftitle : ",self.file_type,self.dftitle,"\n   table_parms : \n    ",self.table_parms)

        importdetailsdata       =   self.load_import_details_data()
        self.num_rows           =   len(importdetailsdata)
        self.model.reload_data(importdetailsdata)
        
        if(self.num_rows < 11) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (11 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)


    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [DataImportDetailsTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        importdetailsdata     =   self.load_import_details_data()
        
        if(DEBUG_DATA_IMPORT_DETAILS) :
           print("    [DataImportDetailsTable][init_tableview] : importdetailsdata \n      ")
           for k in range(len(importdetailsdata)) :
               print("      [",k,"] :",importdetailsdata[k])

        if(self.model is None) :
            self.model = DataImportDetailsModel(importdetailsdata  ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_DETAILS) :
           print("    [DataImportDetailsTable] : model loaded")

        self.num_rows   =   len(importdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
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
        nrows = len(importdetailsdata)
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
    def load_import_details_data(self):

        dftitleParms    =   [self.file_type,self.dftitle]
        
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [DataImportDetailsTable][load_import_details_data] dftitleParms : ",dftitleParms)
            print("    [DataImportDetailsTable][load_import_details_data] self.table_parms : \n    ",self.table_parms)  

        if(self.table_parms is None) :
            from dfcleanser.Qt.data_import.DataImportModel import get_import_details_values
            importValues    =  get_import_details_values(dftitleParms) 
        else:
            importValues    =  self.table_parms
        
        ptitles     =   importValues[0]
        pvals       =   importValues[1]
       
  
        if( (len(ptitles) > 0) and (len(pvals) > 0) and (len(ptitles) == len(pvals))) :
            
            data    =   []

            for i in range(len(ptitles)) :

                data_row    =   []
                data_row.append(str(ptitles[i]))
                data_row.append(str(pvals[i]))

                data.append(data_row)

        self.column_headers     =   ["Parameter Name","Parameter Value"]
        self.column_widths      =   [300,700]

        return(data)


# -----------------------------------------------------------------#
# -          Tableview and Model for Import Details end           -#
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

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("\n[DataExportDetailsTable] : init",dfparms)


        self.mainLayout         =   None
        self.model              =   None

        self.filetype           =   dfparms[0]
        self.filename           =   dfparms[1]

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : init_tableview end")

    def reload_data(self,reloadparms) :
        
        self.filetype          =   reloadparms[0]
        self.filename          =   reloadparms[1]
        
        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : reload_data : filetype : dftitle : ",self.filetype,self.filename)

        exportdetailsdata       =   self.load_export_details_data()
        self.num_rows           =   len(exportdetailsdata)
        self.model.reload_data(exportdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (25 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : reload_data : end : ")

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : init_tableview",self.filetype,self.filename)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        exportdetailsdata     =   self.load_export_details_data()
        
        if(DEBUG_DATA_IMPORT_PARMS) :
           print("[DataExportDetailsTable] : column headers : ",self.column_headers)

        if(self.model is None) :
            self.model = DataExportDetailsModel(exportdetailsdata  ,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_IMPORT_PARMS) :
           print("[DataExportDetailsTable] : model loaded ")

        self.num_rows   =   len(exportdetailsdata)
        
        if(self.num_rows < 25) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
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

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : load_export_details_data ")

        dftitleParms    =   [self.filetype,self.filename]

        from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
        exportValues    =  get_export_details_values(dftitleParms) 

        ptitles     =   exportValues[0]
        pvals       =   exportValues[1]

        if(DEBUG_DATA_IMPORT) :
            print("[DataExportDetailsTable] : \n  ptitles : ",ptitles,"\n  pvals : ",pvals)

        if( (len(ptitles) > 0) and (len(pvals) > 0) and (len(ptitles) == len(pvals))) :

            data    =   []

            for i in range(len(ptitles)) :

                data_row    =   []
                data_row.append(str(ptitles[i]))
                data_row.append(str(pvals[i]))

                data.append(data_row)

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataExportDetailsTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["Parameter Name","Parameter Value"]
        self.column_widths      =   [300,700]

        return(data)
    
# -----------------------------------------------------------------#
# -          Tableview and Model for Export Details end           -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           DataImport Tableviews and Models end                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                      DataImport Widgets                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                Data Import Histories Widget                   -#
# -----------------------------------------------------------------#
class Data_Import_Histories_Widget(QtWidgets.QWidget):

    def __init__(self,  histparms, **kwargs):  

        super().__init__()

        self.select_import_callback     =   histparms[0]
        self.select_export_callback     =   histparms[1]

        self.importHistory              =   None
        self.exportHistory              =   None

        self.init_form()

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("[Data_Import_Histories_Widget] end")

    def reload_data(self) :

        self.importHistory.reload_data()
        self.exportHistory.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("[Data_Import_Histories_Widget]  init_form")

        from PyQt5.QtWidgets import QLabel
        imports_title_label   =   QLabel()
        imports_title_label.setText("\nPandas Import History\n")
        imports_title_label.setAlignment(Qt.AlignCenter)
        imports_title_label.resize(480,50)
        imports_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        self.importHistory         =   DataImportHistoryImportsTable()
        if(not (self.select_import_callback is None)) :
            self.importHistory.doubleClicked.connect(self.select_import_callback)

        new_height  =   45 + (self.importHistory.num_rows * DEFAULT_ROW_HEIGHT)

        self.importHistory.setMinimumHeight(new_height)
        self.importHistory.setMaximumHeight(new_height)

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.importhistories     =   QWidget()

        self.importhistoriesLayout     =   QVBoxLayout()
        self.importhistoriesLayout.addWidget(imports_title_label)
        self.importhistoriesLayout.addWidget(self.importHistory)
        self.importhistoriesLayout.addStretch()

        self.importhistories.setLayout(self.importhistoriesLayout)

        from PyQt5.QtWidgets import QLabel
        exports_title_label   =   QLabel()
        exports_title_label.setText("\nPandas Export History\n")
        exports_title_label.setAlignment(Qt.AlignCenter)
        exports_title_label.resize(480,50)
        exports_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        self.exportHistory         =   DataImportHistoryExportsTable()
        if(not (self.select_export_callback is None)) :
            self.exportHistory.doubleClicked.connect(self.select_export_callback)

        new_height  =   45 + (self.exportHistory.num_rows * DEFAULT_ROW_HEIGHT)

        self.exportHistory.setMinimumHeight(new_height)
        self.exportHistory.setMaximumHeight(new_height)

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.exporthistories     =   QWidget()

        self.exporthistoriesLayout     =   QVBoxLayout()
        self.exporthistoriesLayout.addWidget(exports_title_label)
        self.exporthistoriesLayout.addWidget(self.exportHistory)
        self.exporthistoriesLayout.addStretch()

        self.exporthistories.setLayout(self.exporthistoriesLayout)

        from PyQt5.QtWidgets import QHBoxLayout, QWidget
        self.histories     =   QWidget()

        self.historiesLayout     =   QHBoxLayout()
        self.historiesLayout.addWidget(self.importhistories)
        self.historiesLayout.addWidget(self.exporthistories)

        self.histories.setLayout(self.historiesLayout)

        if( not(self.select_import_callback is None)) :
            from PyQt5.QtWidgets import QLabel
            history_notes_label   =   QLabel()
            history_notes_label.setText("Double Click on the Import Type or Export Type to get a list of previous imports or exports to use as input for an import. To Create a new import select the import from the taskbar above.")
            history_notes_label.setAlignment(Qt.AlignCenter)
            #history_notes_label.resize(9600,100)
            history_notes_label.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")

        self.finalhistories     =   QWidget()

        self.finalhistoriesLayout     =   QVBoxLayout()
        self.finalhistoriesLayout.addWidget(self.histories)
        if( not(self.select_import_callback is None)) :
            self.finalhistoriesLayout.addWidget(history_notes_label)
        self.finalhistoriesLayout.addStretch()

        self.setLayout(self.finalhistoriesLayout)


        if(DEBUG_DATA_IMPORT_HISTORY) :
            print("[Data_Import_Histories_Widget] init from end")


# -----------------------------------------------------------------#
# -                Data Import Histories Widget end               -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -          Data Import file Type Histories Widget               -#
# -----------------------------------------------------------------#
class Data_Import_File_Type_Histories_Widget(QtWidgets.QWidget):

    def __init__(self,  histparms, **kwargs):  

        super().__init__()

        self.filetype                   =   histparms[0]
        self.select_import_callback     =   histparms[1]
        self.delete_import_callback     =   histparms[2]
        self.return_import_callback     =   histparms[3]
        
        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("\n[Data_Import_File_Type_Histories_Widget]\n",self.filetype)

        self.init_form()

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Import_File_Type_Histories_Widget] end")
    
    def reload_data(self) :

        self.importfiletypehistory.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Import_File_Type_Histories_Widget] : init_form",self.filetype)

        if(self.filetype == 0) : filetitle  =   "CSV"
        elif(self.filetype == 1) : filetitle  =   "FWF"
        elif(self.filetype == 2) : filetitle  =   "Excel"
        elif(self.filetype == 3) : filetitle  =   "JSON"
        elif(self.filetype == 4) : filetitle  =   "HTML"
        elif(self.filetype == 5) : filetitle  =   "SQLTable"
        elif(self.filetype == 6) : filetitle  =   "SQLQuery"
        elif(self.filetype == 7) : filetitle  =   "Custom"
        elif(self.filetype == 8) : filetitle  =   "XML"
        else : filetitlle = "PDF"

        from PyQt5.QtWidgets import QLabel
        import_file_type_label   =   QLabel()
        import_file_type_label.setText("\nPandas " + str(filetitle) + " Import History\n")
        import_file_type_label.setAlignment(Qt.AlignCenter)
        import_file_type_label.resize(960,90)
        import_file_type_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        #from dfcleanser.Qt.data_import.DataImportHistoryTableViews import DataImportTypesHistorysTable
        ftparms     =   [self.filetype]
        self.importfiletypehistory        =   DataImportTypesHistorysTable(ftparms)
        self.importfiletypehistory.doubleClicked.connect(self.select_import_callback)
        
        new_height  =   45 + (self.importfiletypehistory.num_rows * DEFAULT_ROW_HEIGHT)

        self.importfiletypehistory.setMinimumHeight(new_height)
        self.importfiletypehistory.setMaximumHeight(new_height)
                
        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Import_File_Type_Histories_Widget] : self.importfiletypehistory built")

        from PyQt5.QtWidgets import QLabel
        import_file_type_notes_label   =   QLabel()
        import_file_type_notes_label.setText("\nClick on DEL column to select imports to delete from the history. Double Click on the df Title column to use the import for next parms.\n")
        import_file_type_notes_label.setAlignment(Qt.AlignCenter)
        import_file_type_notes_label.resize(960,50)
        import_file_type_notes_label.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")

        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        ftypes_button         =   QPushButton()     
        ftypes_button.setText("Delete\nSelected\nImport History(s)")
        ftypes_button.setFixedSize(300,90)
        ftypes_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        ftypes_button.clicked.connect(self.delete_import_callback) 
        
        ftypes_button1        =   QPushButton()     
        ftypes_button1.setText("Return")
        ftypes_button1.setFixedSize(300,90)
        ftypes_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        ftypes_button1.clicked.connect(self.return_import_callback) 

        from PyQt5.QtWidgets import QHBoxLayout
        ftypesbutonsLayout  =   QHBoxLayout()
        ftypesbutonsLayout.addWidget(ftypes_button)
        ftypesbutonsLayout.addWidget(ftypes_button1)
        ftypesbutonsLayout.setAlignment(Qt.AlignHCenter)

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Import_File_Type_Histories_Widget] : ftypesbutonsLayout built")

        from PyQt5.QtWidgets import QVBoxLayout
        self.filetypesLayout     =   QVBoxLayout()
        self.filetypesLayout.addWidget(import_file_type_label)
        self.filetypesLayout.addWidget(self.importfiletypehistory)
        self.filetypesLayout.addWidget(import_file_type_notes_label)
        self.filetypesLayout.addLayout(ftypesbutonsLayout)
        self.filetypesLayout.addStretch()

        self.setLayout(self.filetypesLayout)

# -----------------------------------------------------------------#
# -         Data Import file Type Histories Widget end            -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -          Data Export file Type Histories Widget               -#
# -----------------------------------------------------------------#
class Data_Export_File_Type_Histories_Widget(QtWidgets.QWidget):

    def __init__(self,  histparms, **kwargs):  

        super().__init__()

        self.filetype                   =   histparms[0]
        self.select_export_callback     =   histparms[1]
        self.delete_export_callback     =   histparms[2]
        self.return_export_callback     =   histparms[3]
        
        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("\n[Data_Export_File_Type_Histories_Widget]",self.filetype)

        self.init_form()

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_ExIport_File_Type_Histories_Widget] : end")
    
    def reload_data(self) :

        self.exportfiletypehistory.reload_data()

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form")

        if(self.filetype == 0) : filetitle  =   "CSV"
        elif(self.filetype == 1) : filetitle  =   "Excel"
        elif(self.filetype == 2) : filetitle  =   "JSON"
        elif(self.filetype == 3) : filetitle  =   "HTML"
        elif(self.filetype == 4) : filetitle  =   "SQLTable"
        elif(self.filetype == 5) : filetitle  =   "Custom"
        else : filetitle = "XML"

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

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form : table built")

        from PyQt5.QtWidgets import QLabel
        export_file_type_notes_label   =   QLabel()
        export_file_type_notes_label.setText("\nClick on DEL column to select exports to delete from the history. Double Click on the df Title column to use the export for next parms.\n")
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

        if(DEBUG_DATA_IMPORT_FILE_TYPES) :
            print("[Data_Export_File_Type_Histories_Widget] : init_form : end")


# -----------------------------------------------------------------#
# -         Data Export file Type Histories Widget end            -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                   Import Parms Table Widget                   -#
# -----------------------------------------------------------------#
class Import_Parms_Widget(QtWidgets.QWidget):
    """            
    #------------------------------------------------------------------
    #   get import parms used to import a df
    #
    #------------------------------------------------------------------
    """

    def __init__(self,  importparms, **kwargs):  

        super().__init__()

        if(DEBUG_DATA_IMPORT) :
            print("    [Import_Parms_Widget] : importparms : ",importparms)

        self.filetype       =   importparms[0]
        self.dftitle        =   importparms[1]
        self.parmsdata      =   importparms[2]

        self.init_form()

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_Parms_Widget] : done")

    def reload_parms_data(self,parms) :

        self.filetype       =   parms[0]
        self.dftitle        =   parms[1]
        self.parmsdata      =   parms[2]  

        if(DEBUG_DATA_IMPORT) :
            print("    [Import_Parms_Widget][reload_parms_data] : filetype : dftitle : ",self.filetype,self.dftitle,"\n     parmsdata : \n      ",self.parmsdata)

        self.parms_title_label.setText("\n" + str(self.dftitle) + " Import Parms\n")
        reload_parms    =   [self.filetype,self.dftitle,self.parmsdata]
        self.parmsTable.reload_data(reload_parms)
        
        if(self.parmsTable.num_rows < 11) :
            new_height  =   45 + (self.parmsTable.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.parmsTable.setMinimumHeight(new_height)
        self.parmsTable.setMaximumHeight(new_height)

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [Import_Parms_Widget][init_form] filetype : dftitle : ",self.filetype,self.dftitle,"\n      parmsdata : \n      ",self.parmsdata)
        
        try :

            # build the overall parms layout
            from PyQt5.QtWidgets import QLabel, QVBoxLayout

            parmsLayout      =   QVBoxLayout()

            self.parms_title_label    =   QLabel()
            self.parms_title_label.setText("\n" + str(self.dftitle) + " Import Parms\n")
            self.parms_title_label.setAlignment(Qt.AlignCenter)
            self.parms_title_label.resize(960,50)
            self.parms_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

            details_parms       =   [self.filetype,self.dftitle,self.parmsdata]
            self.parmsTable     =   DataImportDetailsTable(details_parms)

            if(self.parmsTable.num_rows < 11) :
                new_height  =   45 + (self.parmsTable.num_rows * DEFAULT_ROW_HEIGHT)
            else :
                new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

            self.parmsTable.setMinimumHeight(new_height)
            self.parmsTable.setMaximumHeight(new_height)

            parmsLayout.addWidget(self.parms_title_label)
            parmsLayout.addWidget(self.parmsTable)
            parmsLayout.addStretch()

            self.setLayout(parmsLayout)

        except Exception as e:
            
            title       =   "dfcleanser exception"
            status_msg  =   "[Import_Parms_Widget][init_form] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_Parms_Widget] :init_form : end")

# -----------------------------------------------------------------#
# -                 end Import Parms Table Widget                 -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -              Import Parms with commands Widget                -#
# -----------------------------------------------------------------#
class Import_With_Parms_Widget(QtWidgets.QWidget):
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
        
        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Parms_Widget] ",importparms[0],importparms[1])

        self.filetype           =   importparms[0]
        self.dftitle            =   importparms[1]
        self.import_action      =   importparms[2]
        self.return_action      =   importparms[3]

        self.init_form()

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_With_Parms_Widget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_IMPORT) :
            print("\n[Import_With_Parms_Widget] reload_table_data : reloadparms : ",reloadparms)

        self.filetype   =   reloadparms[0]
        self.dftitle    =   reloadparms[1]
        self.parmsdata  =   reloadparms[2]

        if(DEBUG_DATA_IMPORT) :
            print("\n[Import_With_Parms_Widget] : filetype : dftitle : ",self.filetype,self.dftitle)

        reload_parms    =  [self.filetype,self.dftitle,self.parmsdata]
        self.importparmsTable.reload_parms_data(reload_parms)

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_With_Parms_Widget] : init_form")

        from PyQt5.QtWidgets import QVBoxLayout
        self.importwithparmsLayout      =   QVBoxLayout()

        importparms                     =   [self.filetype,self.dftitle,None] 
        self.importparmsTable           =   Import_Parms_Widget(importparms)

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_With_Parms_Widget] : parms table",type(self.importparmsTable))

        self.importwithparmsLayout.addWidget(self.importparmsTable)

        # buttons for dissplay import parms
        from PyQt5.QtWidgets import QPushButton
        parms_button         =   QPushButton()     
        parms_button.setText("Import\nWith Parms\nAbove")
        parms_button.setFixedSize(300,90)
        parms_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button.clicked.connect(self.import_action) 
        
        parms_button1        =   QPushButton()     
        parms_button1.setText("Return")
        parms_button1.setFixedSize(300,90)
        parms_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button1.clicked.connect(self.return_action) 
        
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("  [Import_With_Parms_Widget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.addWidget(parms_button1)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)

        
        self.importwithparmsLayout.addLayout(parmsbutonsLayout)
        self.importwithparmsLayout.addStretch()

        self.setLayout(self.importwithparmsLayout)


# -----------------------------------------------------------------#
# -         end Import Parms with commands Widget                 -#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              Import with Export parms objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -               Import with Export mapping data                 -#
# -----------------------------------------------------------------#

# pandas 1.5.x csv pams
csv_import_parms    =   ["filepath_or_buffer","sep","user_cols","header","index_label","encoding","compression","chunksize","stprage_option"]
csv_import_offsets  =   [2,-1,-1,3,-1,-1,-1,-1,-1]
csv_export_parms    =   ["path_or_buffer","sep","columns","header","index_label","encoding","compression","chunksize","storage_option"]
csv_export_offsets  =   [1,-1,-1,3,-1,-1,-1,-1,-1]


# -----------------------------------------------------------------#
# -           Import with Export Parms Dispplay Widget            -#
# -----------------------------------------------------------------#
class Import_With_Export_Parms_Widget(QtWidgets.QWidget):
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
        
        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Export_Parms_Widget] ",importparms[0],importparms[1])

        self.filetype           =   importparms[0]
        self.dftitle            =   importparms[1]
        self.filename           =   importparms[2]
        self.import_action      =   importparms[3]
        self.return_action      =   importparms[4]

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("  [Import_With_Export_Parms_Widget] : \n  ",self.import_action,"\n  ",self.return_action)

        self.init_form()

        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Export_Parms_Widget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Export_Parms_Widget][reload_table_data] : reloadparms : \n    ",reloadparms)

        self.filetype   =   reloadparms[0]
        self.dftitle    =   reloadparms[1]
        self.filename   =   reloadparms[2]

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("  [Import_With_Parms_Widget] : filetype : dftitle : ",self.filetype,self.dftitle,self.filename)

        self.import_with_export_values  =   self.map_export_parms_to_import_parms()
        
        importparms                     =   [self.filetype,self.dftitle,self.import_with_export_values] 
        self.importwithexportparmsTable.reload_parms_data(importparms)

    def init_form(self):  

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("  [Import_With_Export_Parms_Widget][init_form]")

        from PyQt5.QtWidgets import QVBoxLayout
        self.importwithexportparmsLayout        =   QVBoxLayout()

        self.import_with_export_values          =   self.map_export_parms_to_import_parms()

        importparms                             =   [self.filetype,self.dftitle,self.import_with_export_values] 
        self.importwithexportparmsTable         =   Import_Parms_Widget(importparms)

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("  [Import_With_Export_Parms_Widget][init_form] : parms table",type(self.importwithexportparmsTable))

        self.importwithexportparmsLayout.addWidget(self.importwithexportparmsTable)

        # buttons for dissplay import parms
        from PyQt5.QtWidgets import QPushButton
        parms_button         =   QPushButton()     
        parms_button.setText("Import\nWith Parms\nAbove")
        parms_button.setFixedSize(300,90)
        parms_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button.clicked.connect(self.import_action) 
        
        parms_button1        =   QPushButton()     
        parms_button1.setText("Return")
        parms_button1.setFixedSize(300,90)
        parms_button1.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button1.clicked.connect(self.return_action) 
        
        if(DEBUG_DATA_IMPORT_PARMS) :
            print("  [Import_With_Parms_Widget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.addWidget(parms_button1)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)
        
        self.importwithexportparmsLayout.addLayout(parmsbutonsLayout)
        self.importwithexportparmsLayout.addStretch()

        self.setLayout(self.importwithexportparmsLayout)

    def map_export_parms_to_import_parms(self) :

        export_parms    =   [self.filetype,self.filename]
        
        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Export_Parms_Widget][map_export_parms_to_import_parms] export_parms : \n    ",export_parms)

        from dfcleanser.Qt.data_import.DataImportModel import get_export_details_values
        exportValues    =  get_export_details_values(export_parms) 

        ptitles     =   exportValues[0]
        pvals       =   exportValues[1]
        
        if(DEBUG_DATA_IMPORT) :
            print("  [Import_With_Export_Parms_Widget][map_export_parms_to_import_parms] exportValues : \n    ",ptitles,"\n    ",pvals)

        export_to_import_map    =   []

        if( (len(ptitles) > 0) and (len(pvals) > 0) and (len(ptitles) == len(pvals))) :

            import_with_export_titles   =   ["dataframe_title"]
            import_with_export_values   =   [self.dftitle]

            import dfcleanser.Qt.data_export.DataExportModel as dem
            if(self.filetype == dem.SQLTABLE_EXPORT) :

                import_with_export_titles   =   ["server"]
                import_with_export_values   =   ["TBD"]
                import_with_export_titles   =   ["database"]
                import_with_export_values   =   ["TBD"]

            if(self.filetype == dem.CSV_EXPORT) :

                import_titles   =   ["filepath_or_buffer"]
                export_titles   =   ["path_or_buf"]

            elif(self.filetype == dem.EXCEL_EXPORT) :

                import_titles   =   ["io","sheet_name"]
                export_titles   =   ["excel_writer","sheet_name"]

            elif(self.filetype == dem.JSON_EXPORT) :

                import_titles   =   ["path_or_buf","orient"]
                export_titles   =   ["path_or_buf","orient"]

            elif(self.filetype == dem.HTML_EXPORT) :

                import_titles   =   ["io"]
                export_titles   =   ["buf"]

            elif(self.filetype == dem.SQLTABLE_EXPORT) :

                import_titles   =   ["table_name","schema"]
                export_titles   =   ["name","schema"]

            for i in range(len(export_titles)) :
                export_match    =   export_titles[i]
                if(export_match in ptitles) :
                    match_index     =   ptitles.index(export_match)
                    if(match_index > -1) :
                        import_with_export_titles.append(import_titles[i])
                        import_with_export_values.append(pvals[match_index]) 


            export_to_import_map    =   [import_with_export_titles,import_with_export_values]
            if(DEBUG_DATA_IMPORT) :
                print("  [Import_With_Export_Parms_Widget][map_export_parms_to_import_parms] export_to_import_map: \n  ",export_to_import_map)

        else :

            title       =   "dfcleanser error"
            status_msg  =   "[Import_With_Export_Parms_Widget][map_export_parms_to_import_parms]  error : invalid history"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)
            export_to_import_map    =   None

        return(export_to_import_map )

# -----------------------------------------------------------------#
# -           end Import with Export Parms Widget                 -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                    Import Status Widget                       -#
# -----------------------------------------------------------------#
class Import_Status_Widget(QtWidgets.QWidget):

    def __init__(self,  importparms, **kwargs):  

        super().__init__()
        
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("\n    [Import_Status_Widget] ",importparms[0],importparms[1])

        self.filetype           =   importparms[0]
        self.dftitle            =   importparms[1]
        self.return_action      =   importparms[2]

        self.init_form()

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [Import_Status_Widget] : done")
    
    def reload_table_data(self,reloadparms) :

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("\n[Import_Status_Widget] reload_table_data : reloadparms : ",reloadparms)

        self.filetype   =   reloadparms[0]
        self.dftitle    =   reloadparms[1]

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("\n[Import_Status_Widget] : filetype : dftitle : ",self.filetype,self.dftitle)

        reload_parms    =   [self.filetype,self.dftitle,None]
        self.importparmsTable.reload_parms_data(reload_parms)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.num_rows_label.setText("\n\n" + str(self.dftitle) + " : Num Rows : " + str(len(df)))
        self.num_cols_label.setText(str(self.dftitle) + " : Num Cols : " + str(len(df.columns)))


    def init_form(self):  

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [Import_Status_Widget] : init_form")

        from PyQt5.QtWidgets import QVBoxLayout
        self.importstatusLayout      =   QVBoxLayout()

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("    [Import_Status_Widget] : df",self.dftitle,df)

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
       
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[Import_Status_Widget] : labels")

        self.importstatusLayout.addWidget(self.num_rows_label)
        self.importstatusLayout.addWidget(self.num_cols_label)

        importparms                     =   [self.filetype,self.dftitle,None] 
        self.importparmsTable           =   Import_Parms_Widget(importparms)
        self.importstatusLayout.addWidget(self.importparmsTable)

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[Import_Status_Widget] : parms table",type(self.importparmsTable))

        # buttons for dissplay import status
        from PyQt5.QtWidgets import QPushButton
        
        parms_button        =   QPushButton()     
        parms_button.setText("Return")
        parms_button.setFixedSize(300,90)
        parms_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        parms_button.clicked.connect(self.return_action) 
        
        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[Import_With_Parms_Widget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        parmsbutonsLayout  =   QHBoxLayout()
        parmsbutonsLayout.addWidget(parms_button)
        parmsbutonsLayout.setAlignment(Qt.AlignHCenter)
        
        self.importstatusLayout.addLayout(parmsbutonsLayout)
        self.importstatusLayout.addStretch()

        self.setLayout(self.importstatusLayout)


# -----------------------------------------------------------------#
# -               end Import Status Widget                        -#
# -----------------------------------------------------------------#

    
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
            print("\n[DataImportHTMLdfsTable] : init")


        self.mainLayout         =   None
        self.model              =   None

        self.dfslist            =   dfparms[0]

        self.init_tableview()

        if(DEBUG_DATA_IMPORT_PARMS) :
            print("[DataImportHTMLdfsTable] : init_tableview end")

    def reload_data(self,dfslist) :
        
        self.dfslist            =   dfslist

        return()
        
        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsTable] : reload_data : self.dfslist : ",type(self.dfslist),len(self.dfslist))
            for i in range(len(self.dfslist)) :
                print("[DataImportHTMLdfsTable] : reload_data : self.dfslist : ",type(self.dfslist[i]))    

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
            new_height  =   40 + (25 * DEFAULT_ROW_HEIGHT)

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
            print("[DataImportHTMLdfsTable] : load_html_dfs_data ",len(self.dfslist))

        data    =   []

        for i in range(len(self.dfslist)) :

            if(DEBUG_DATA_IMPORT) :
                print("[DataImportHTMLdfsTable] : load_html_dfs_data ",type(self.dfslist[i]))


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
            print("\n[DataImportHTMLdfsWidget] reload_table_data : reloadparms : ")

        self.dfslist   =   reloadparms
 
        self.importhtmldfsTable.reload_data([self.dfslist])
 
    def init_form(self):  

        if(DEBUG_DATA_IMPORT) :
            print("[DataImportHTMLdfsWidget] : init_form")

        from PyQt5.QtWidgets import QVBoxLayout
        self.importhtmldfsLayout      =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.title_label    =   QLabel()
        self.title_label.setText("\n\nRetrieved HTML Tables\n")
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
        self.return_action                  =   dfparms[1]
        self.help_action                    =   dfparms[2]       
        
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
        button_methods      =   [self.add_df_to_dfcleanser,self.save_as_json_file,self.return_action,self.help_action]

        formParms.append(comboList)
        formParms.append(comboMethods)            
        formParms.append(file_methods)
        formParms.append(button_methods)            
        formParms.append(cfg_parms)            
        formParms.append("\nSave html df")
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
    # -                      add df to dfcleanser                     -#
    # -----------------------------------------------------------------#
    def add_df_to_dfcleanser(self) :

        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][add_df_to_dfcleanser]")

        df_title    =   self.save_json_df_form.get_form_input_value_by_index(0)

        from dfcleanser.common.cfg import add_df_to_dfc
        add_df_to_dfc(df_title,self.df)

        title       =   "dfcleanser status : [add_df_to_dfcleanser]"       
        status_msg  =   "df '" + df_title + "' added successfully "
        from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
        display_status_msg(title,status_msg)


    # -----------------------------------------------------------------#
    # -                     Save df as a json file                    -#
    # -----------------------------------------------------------------#
    def save_as_json_file(self) :

        if(DEBUG_DATA_IMPORT) :
             print("  [DataImportHTMLdfSaveWidget][save_as_json_file]")

        try :

            df_title    =   self.save_json_df_form.get_form_input_value_by_index(0)
            json_file_name    =   self.save_json_df_form.get_form_input_value_by_index(1)
            self.df.to_json(json_file_name)

            title       =   "dfcleanser status : [save_as_json_file]"       
            status_msg  =   "df '" + df_title + "' written as json file "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)
 

        except Exception as e:

            title       =   "dfcleanser exception"
            status_msg  =   "[save_as_json_file] save error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        self.statusBar().clearMessage()
     
   

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







