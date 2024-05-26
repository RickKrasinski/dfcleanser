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
from dfcleanser.common.cfg import DataInspection_ID

 
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection Row Nans Objjects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#

class DataInspectionRowNansModel(QtCore.QAbstractTableModel):
    def __init__(self, nandata):

        super(DataInspectionRowNansModel, self).__init__()
        self._data = nandata

    def reload_data(self,nandata) :
        self._data = nandata

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
            odd = (column % 2) 
            if(odd) :
                return(Qt.AlignRight)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            odd = (column % 2) 
            if(odd):
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            else:
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
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
            odd = (section % 2) 
            if(odd) :
                return('Stat Value')
            else :
                return("Row Stat")
        return super().headerData(section, orientation, role)

# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class RowNansTable(QtWidgets.QTableView):

    #def __init__(self):
    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionColumnsWidgets",print_to_string("[RowNansTable] : init",self.dftitle))


        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)
        self.df     =   df

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionColumnsWidgets",print_to_string("[RowNansTable] : df",type(self.df)))
           

        self.init_tableview()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionColumnsWidgets",print_to_string("[RowNansTable] : init_tableview done"))

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionColumnsWidgets",print_to_string("[RowNansTable] : init_tableview",self.dftitle))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        nandata     =   self.load_nan_rows_data()

        if(self.model is None) :
            self.model = DataInspectionRowNansModel(nandata)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionColumnsWidgets",print_to_string("[RowNansTable] : model loaded \n ",nandata))


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
        nrows = 4
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [320,150]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_nan_rows_data(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("[RowNansTable] : load_nan_rows_data ",type(self.df)))

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_nan_stats, ROW_STATS  
        stats_data  =   get_nan_stats(self.df,ROW_STATS)
        statrows    =   stats_data[0]
        statvals    =   stats_data[1]

        data    =   []

        for i in range(len(statrows)) :

            data_row    =   []
            data_row.append(statrows[i])
            data_row.append(statvals[i])
            data.append(data_row)

        return(data)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection Row Nans Objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#        
      

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            DataInspection Column Nans Objjects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#

class DataInspectionColumnNansModel(QtCore.QAbstractTableModel):
    def __init__(self, nandata):

        super(DataInspectionColumnNansModel, self).__init__()
        self._data = nandata

    def reload_data(self,nandata) :
        self._data = nandata

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
            odd = (column % 2) 
            if(odd) :
                return(Qt.AlignRight)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            odd = (column % 2) 
            if(odd):
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            else:
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
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
            odd = (section % 2) 
            if(odd) :
                return('Stat Value')
            else :
                return("Column Stat")
        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -     Subclass of QTableView tp ddisplay column nans dtat       -#
# -----------------------------------------------------------------#
class ColumnNansTable(QtWidgets.QTableView):

    #def __init__(self):
    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("[ColumnNansTable] ",self.dftitle))
    

        self.init_tableview()
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[ColumnNansTable] : init_tableview"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        nandata     =   self.load_nan_columns_data()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[ColumnNansTable] : init_tableview : nandata\n ",nandata))

        if(self.model is None) :
            self.model = DataInspectionColumnNansModel(nandata)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[ColumnNansTable] : init_tableview : model set"))
        

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
        nrows = 4
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [310,150]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[ColumnNansTable] : end init_tableview"))


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_nan_columns_data(self):

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_nan_stats, COLUMN_STATS  
        stats_data  =   get_nan_stats(self.df,COLUMN_STATS)
        statrows    =   stats_data[0]
        statvals    =   stats_data[1]

        data    =   []

        for i in range(len(statrows)) :

            data_row    =   []
            data_row.append(statrows[i])
            data_row.append(statvals[i])
            data.append(data_row)

        return(data)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            DataInspection Column Nans Objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#        
 


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -          DataInspection Drop Row Nans Objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

nan_row_column_headers  =   ["Nan Cols Pct","Total Rows","Sample Row Ids"]
nan_row_column_widths   =   [80,90,290]

# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#

class DataInspectionDropRowNansModel(QtCore.QAbstractTableModel):
    def __init__(self, nandata):

        super(DataInspectionDropRowNansModel, self).__init__()
        self._data = nandata

    def reload_data(self,nandata) :
        self._data = nandata

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
            odd = (column % 2) 
            if(odd) :
                return(Qt.AlignRight)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            #odd = (column % 2) 
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
            #odd = (section % 2) 
            if(section == 0) :
                return(nan_row_column_headers[0])
            elif(section == 1) :
                return(nan_row_column_headers[1])
            else :
                return(nan_row_column_headers[2])
        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -     Subclass of QTableView tp ddisplay column nans dtat       -#
# -----------------------------------------------------------------#
class DataInspectionDropRowNansTable(QtWidgets.QTableView):

    #def __init__(self):
    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropRowNansTable] ",self.dftitle))

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()

    def reload_data(self):

        self.load_drop_rows_data()  

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropRowNansTable] : init_tableview"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        nandata     =   self.load_drop_rows_data()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropRowNansTable] : init_tableview :nandata\n",nandata))

        if(self.model is None) :
            self.model = DataInspectionDropRowNansModel(nandata)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropRowNansTable] : init_tableview : model set"))
        

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
        nrows = len(nandata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(nan_row_column_widths)) :
           self.setColumnWidth(i, nan_row_column_widths[i])     
        
        self.setWordWrap(True)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropRowNansTable] : end init_tableview"))


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_drop_rows_data(self):

        # build row nan percentiles
        rowswithnulls   =   self.df.isnull().sum(axis=1).tolist()
        
        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_row_nans_data
        pctilecounts, pctilerows    =   get_row_nans_data(self.df,rowswithnulls)
        
        pcttile_titles  =   ["95 - 100%","90 - 95%","85 - 90%","80 - 85%","75 - 80%",
                            "70 - 75%","65 - 70%","60 - 65%","55 - 60%","50 - 55%",
                            "45 - 50%","40 - 45%","35 - 40%","30 - 35%","25 - 30%",
                            "20 - 25%","15 - 20%","10 - 15%","5 - 10%","0 - 5%"]
        
        data    =   []

        for i in range(len(pctilecounts)) :
            data_row    =   [pcttile_titles[i],pctilecounts[i],str(pctilerows[i])]
            data.append(data_row)
        

        return(data)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            DataInspection Drop Row Nans Objects               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#        
 

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -          DataInspection Drop Col Nans Objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

nan_col_column_headers  =   ["Column Name","Rows Count","Pct Rows"]
nan_col_column_widths   =   [290,80,90]

# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#

class DataInspectionDropColNansModel(QtCore.QAbstractTableModel):
    def __init__(self, nandata):

        super(DataInspectionDropColNansModel, self).__init__()
        self._data = nandata

    def reload_data(self,nandata) :
        self._data = nandata

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
            odd = (column % 2) 
            if(odd) :
                return(Qt.AlignRight)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            #odd = (column % 2) 
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
            #odd = (section % 2) 
            if(section == 0) :
                return(nan_col_column_headers[0])
            elif(section == 1) :
                return(nan_col_column_headers[1])
            else :
                return(nan_col_column_headers[2])
        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -     Subclass of QTableView tp ddisplay column nans dtat       -#
# -----------------------------------------------------------------#
class DataInspectionDropColsNansTable(QtWidgets.QTableView):

    #def __init__(self):
    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropColsNansTable]",self.dftitle))


        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()

    def reload_data(self) :

        self.load_drop_cols_data()        
    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropColsNansTable] : init_tableview"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        nandata     =   self.load_drop_cols_data()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropColsNansTable] : init_tableview :nandata",nandata))

        if(self.model is None) :
            self.model = DataInspectionDropColNansModel(nandata)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("[DataInspectionDropColsNansTable] : init_tableview : model set"))
        

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
        nrows = len(nandata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [320,150]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(nan_col_column_widths)) :
           self.setColumnWidth(i, nan_col_column_widths[i])     
        
        self.setWordWrap(True)
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
           add_debug_to_log("DataInspectionRows",print_to_string("end init_tableview"))


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_drop_cols_data(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("[load_drop_cols_data]  "))

        # build column nan percentiles
        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_cols_nans_data
        df_nulls_sorted, df_cols_sorted     =   get_cols_nans_data(self.df)  

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("df_nulls_sorted",df_nulls_sorted))
            add_debug_to_log("DataInspectionRows",print_to_string("df_cols_sorted",df_cols_sorted))

        numrows         =   len(self.df)
        column_pcts     =   []

        for i in range(len(df_cols_sorted)) :
            column_pcts.append("{0:.2f}".format(100*(df_nulls_sorted[i]/numrows))+"%")

        data    =   []

        for i in range(len(df_cols_sorted)) :
            data_row    =   [df_cols_sorted[i],df_nulls_sorted[i],column_pcts[i]]
            data.append(data_row)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_NANS")) :
            add_debug_to_log("DataInspectionRows",print_to_string("column_pcts",column_pcts))

        return(data)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            DataInspection Drop Row Nans Objects               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#        
 

























 
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column uniques qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#









