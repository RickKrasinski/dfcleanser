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

DEBUG_DATA_INSPECT_DTYPES      =   False


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

class DataInspectionDataTypesModel(QtCore.QAbstractTableModel):
    def __init__(self, nandata):

        super(DataInspectionDataTypesModel, self).__init__()
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
           # odd = (section % 2) 
            if(section == 0) :
                return('Data Type')
            elif(section == 1) :
                return('Count')
            else :
                return("Column Names")
        return super().headerData(section, orientation, role)

# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataTypesTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("\n[DataTypesTable] : init")

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()
        
        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("[DataTypesTable] : init_tableview done")

        #self.doubleClicked.connect(self.handleDataTypedoubleclick)

        #if(DEBUG_DATA_INSPECT_DTYPES) :
        #    print("[DataTypesTable] : init done")


    #def handleDataTypedoubleclic(self, index) :

    #    print("[handleDataTypedoubleclic] : double clicked : row ",index.row)
    #    print("[handleDataTypedoubleclic] : double clicked : column ",index.column)



    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("[DataTypesTable] : init_tableview",self.dftitle)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dtypesdata     =   self.load_dtypes_data()

        if(self.model is None) :
            self.model = DataInspectionDataTypesModel(dtypesdata)
            self.setModel(self.model)

        if(DEBUG_DATA_INSPECT_DTYPES) :
           print("[DataTypesTable] : model loaded",dtypesdata)

        self.num_rows   =   len(dtypesdata)

        new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)

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
        nrows = len(dtypesdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [200,90,720]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_dtypes_data(self):

        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("[RowNansTable] : load_nan_rows_data ")

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_df_datatypes_data
        df_data_info = get_df_datatypes_data(self.df)

        dtypes_list             =   df_data_info[0]
        dtypes_counts_list      =   df_data_info[1]
        dtypes_dict             =   df_data_info[2]


        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("[df_data_info] : dtypes_list\n  ",dtypes_list,"\n  dtypes_counts_list : ",dtypes_counts_list,"\n  dtypes_dict \n",dtypes_dict)

        data    =   []

        for i in range(len(dtypes_list)) :

            data_row    =   []
            data_row.append(str(dtypes_list[i]))
            data_row.append(dtypes_counts_list[i])
            data_row.append(str(dtypes_dict.get(dtypes_list[i])))

            data.append(data_row)

        if(DEBUG_DATA_INSPECT_DTYPES) :
            print("[load_dtypes_data]  \n",data)

        return(data)







