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
# -               DataInspection Categories                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                Table Model for df categories                  -#
# -----------------------------------------------------------------#

class DataInspectionCategoriesModel(QtCore.QAbstractTableModel):
    def __init__(self, catdata, colheaders):

        super(DataInspectionCategoriesModel, self).__init__()
        self._data          =   catdata
        self.column_names   =   colheaders

    def reload_data(self,catdata) :
        self._data = catdata

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
# -       Subclass of QMainWindow to disp[lay df Categories       -#
# -----------------------------------------------------------------#
class DataInspectionCategoriesTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : init"))

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : init_tableview done"))

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : init_tableview",self.dftitle))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        catcolsdata     =   self.load_columns_cats_data()
        
        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
           add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : catcolsdata",catcolsdata,"\n",self.column_headers))


        if(self.model is None) :
            self.model = DataInspectionCategoriesModel(catcolsdata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
           add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : model loaded",catcolsdata))

        column_widths   =   [220,120,600]

        self.num_rows   =   len(catcolsdata)
        
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
        nrows = len(catcolsdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths     =   [220,100,710]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_columns_cats_data(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : load_columns_cats_data "))

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_df_categories_data
        df_data_info = get_df_categories_data(self.df)

        cat_candidates_list     =   df_data_info[0]
        categories_list         =   df_data_info[1]

        catcols                 =   categories_list[0]
        cat_ordered_list        =   categories_list[1]
        cat_categories_list     =   categories_list[2]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[df_data_info] : catcols\n  ",catcols,"\n  cat_ordered_list : ",cat_ordered_list,"\n  cat_categories_list \n",cat_categories_list))

        data    =   []

        for i in range(len(catcols)) :

            data_row    =   []
            data_row.append(str(catcols[i]))
            data_row.append(str(cat_ordered_list[i]))
            data_row.append(str(cat_categories_list[i]))

            data.append(data_row)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoriesTable] : data\n ",data))

        self.column_headers     =   ["Column Name","Ordered","Categories"]

        return(data)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             DataInspection Categories end                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -      DataInspection Category Candidates Table                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -           Table Model for category candidates                 -#
# -----------------------------------------------------------------#

class DataInspectionCategoryCandidatesModel(QtCore.QAbstractTableModel):
    def __init__(self, colsdata, col_headers):

        super(DataInspectionCategoryCandidatesModel, self).__init__()
        self._data = colsdata
        self.col_headers = col_headers

    def reload_data(self,colsdata) :
        self._data = colsdata

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
# -  bclass of QMainWindow to disp[lay the category candidates    -#
# -----------------------------------------------------------------#
class DataInspectionCategoryCandidatesTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoryCandidatesTable] : init"))

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoryCandidatesTable] : init_tableview done"))

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoryCandidatesTable] : init_tableview",self.dftitle))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        columnsdata     =   self.load_cat_candidates_data()

        if(self.model is None) :
            self.model = DataInspectionCategoryCandidatesModel(columnsdata, self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
           add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoryCandidatesTable] : model loaded",columnsdata))

        self.num_rows   =   len(columnsdata)

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
        nrows = len(columnsdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [120,100,100,100,100,520]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_cat_candidates_data(self):

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[DataInspectionCategoryCandidatesTable] : load_cat_candidates_data "))

        df_cols         =   self.df.columns

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_df_categories_data
        df_data_info =  get_df_categories_data(self.df)

        cat_candidates_list   =   df_data_info[0]

        catcandidates           =   cat_candidates_list[0]
        catcanddtypesList       =   cat_candidates_list[1]
        nans                    =   cat_candidates_list[2]
        whitespace              =   cat_candidates_list[3]
        catcanduniquescountList =   cat_candidates_list[4]
        catcandidatesuniques    =   cat_candidates_list[5]

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[df_data_info] : \n  catcandidates\n  ",catcandidates,"\n  types : \n    ",catcanddtypesList,"\n  nans \n    ",nans))
            add_debug_to_log("DataInspection",print_to_string("[df_data_info] : \n  whitespace\n    ",whitespace,"\n  uniquescount : \n    ",catcanduniquescountList,"\n uniques  \n    ",catcandidatesuniques))
        
        data            =   []

        for i in range(len(catcandidates)) :

            data_row    =   []
            data_row.append(catcandidates[i])
            data_row.append(str(catcanddtypesList[i]))
            data_row.append(str(nans[i]))
            data_row.append(str(whitespace[i]))
            data_row.append(str(catcanduniquescountList[i]))
            data_row.append(str(catcandidatesuniques[i]))

            data.append(data_row)

        if(is_debug_on(DataInspection_ID,"DEBUG_DATA_INSPECT_CATEGORIES")) :
            add_debug_to_log("DataInspection",print_to_string("[CatCandidatesTable] : data\n ",data))

        self.column_headers     =   ["Column Name","Data Type","Total Nans","White Space","Unique Count","Uniques"]

        return(data)

















