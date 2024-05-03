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


DEBUG_CLEANSE_ROWS                  =   False
DEBUG_CLEANSE_ROWS_FILTER           =   False
DEBUG_CLEANSE_ROWS_FILTER_DETAILS   =   False
DEBUG_CLEANSE_COLUMN_DETAILS        =   False
DEBUG_CLEANSE_COLUMN_SINGLE         =   False

DEBUG_FILTERS_COLUMN_TABLE          = False
DEBUG_FILTERS_STATS_TABLE           = False


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             general Data Import Housekeeping                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20

from dfcleanser.common.html_widgets import maketextarea

"""
#--------------------------------------------------------------------------
#   get subset criteria input 
#--------------------------------------------------------------------------
"""
"""
define_filter_df_input_title            =   "Define Filter Dataframe"
define_filter_df_input_id               =   "dcdfdefinedf"
define_filter_df_input_idList           =   ["dffiltertitle",
                                             "dffilteroption",
                                             None,None,None]

define_filter_df_input_labelList        =   ["df_to_filter_title",
                                             "filter_df_selection_criteria",
                                             "define df</br>Filter</br>Criteria",
                                             "Return","Help"]

define_filter_df_input_typeList         =   ["text","select",
                                             "button","button","button"]

define_filter_df_input_placeholderList  =   ["enter title for df to filter",
                                             "select df title (default - original)",
                                              None,None,None]

define_filter_df_input_reqList          =   [0,1]
"""

"""
#--------------------------------------------------------------------------
#   get subset criteria input 
#--------------------------------------------------------------------------
"""
get_subset_criteria_input_title           =   "Get Dataframe Subset Criteria"
get_subset_criteria_input_id              =   "dcdfsubsetcriteria"
get_subset_criteria_input_idList          =   ["gsselectstring",
                                                None,None,None]

get_subset_criteria_input_labelList       =   ["filter_df_selection_criteria",
                                               "Get df</br>From</br>Criteria",
                                               "Return","Help"]

get_subset_criteria_input_typeList        =   [maketextarea(7),
                                               "button","button","button"]

get_subset_criteria_input_placeholderList =   ["select string : can be editted manually (default - None)",
                                                None,None,None]

get_subset_criteria_input_reqList         =   [0]


"""
#--------------------------------------------------------------------------
#   save the new subset input 
#--------------------------------------------------------------------------
"""
save_subset_run_input_title              =   "Run Dataframe Subset"
save_subset_run_input_id                 =   "dfcsavedfsubset"
save_subset_run_input_idList             =   ["subsetdftitle",
                                              None,None,None,None,None]

save_subset_run_input_labelList          =   ["filtered_dataframe_title",
                                              "Save</br>Filtered df</br>as dfc df",
                                              "Apply</br>More</br>Filters",
                                              "Browse</br>Filtered df</br>In browser",
                                              "Return","Help"]

save_subset_run_input_typeList           =   ["text",
                                              "button","button","button","button","button"]

save_subset_run_input_placeholderList    =   ["filtered dataframe title",
                                              None,None,None,None,None]

save_subset_run_input_reqList            =   [0]




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             Table view and Model for dffilter cols            -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                    Model for dffilter cols                    -#
# -----------------------------------------------------------------#
class DataCleansingdfFiltersColumnModel(QtCore.QAbstractTableModel):

    def __init__(self, coldata, colheaders):

        super(DataCleansingdfFiltersColumnModel,self).__init__()
        self._data          =   coldata
        self.column_names   =   colheaders

    def reload_data(self,coldata) :
        self._data = coldata

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
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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
# -                    Table for dffilter cols                    -#
# -----------------------------------------------------------------#
class DataCleansingdfFiltersColumnTable(QtWidgets.QTableView):

    def __init__(self,  colparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.working_df_to_filter   =   colparms[0]
        self.select_callback        =   colparms[1]

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("    [DataCleansingdfFiltersColumnTable] : init ",self.select_callback)
        if(DEBUG_CLEANSE_ROWS_FILTER_DETAILS) :    
            print("    [DataCleansingdfFiltersColumnTable] : init ",self.working_df_to_filter)

        if( not(self.select_callback is None)) :
            self.doubleClicked.connect(self.select_callback) 

        self.init_tableview()

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("    [DataCleansingdfFiltersColumnTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self) :
                    
        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][reload_data] : ")

        #self.working_df_to_filter   =   workingdf
        #self.select_callback        =   callback

        statsdata       =   self.load_columns_info_data()
        self.model.reload_data(statsdata)

        self.num_rows   =   len(statsdata)

        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][reload_data] : self.num_rows ",self.num_rows)
        
        if(self.num_rows < 12) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (12 * DEFAULT_ROW_HEIGHT))

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)
        
        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][reload_data] : end")
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statsdata     =   self.load_columns_info_data()
        
        if(DEBUG_FILTERS_COLUMN_TABLE) :
           print("    [DataCleansingdfFiltersColumnTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = DataCleansingdfFiltersColumnModel(statsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_FILTERS_COLUMN_TABLE) :
           print("    [DataCleansingdfFiltersColumnTable][init_tableview] : model loaded")

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 8) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (8 * DEFAULT_ROW_HEIGHT))

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
        nrows = len(statsdata)
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
    def load_columns_info_data(self):

        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][load_columns_info_data]")

        data    =   []

        df_col_names_list   =   self.working_df_to_filter.columns.tolist()

        if(DEBUG_FILTERS_COLUMN_TABLE) :
            print("    [DataCleansingdfFiltersColumnTable][load_columns_info_data] df_col_names_list ",df_col_names_list)


        for i in range(len(df_col_names_list)) :

            data_row    =   []  

            data_row.append(str(df_col_names_list[i]))
            data_row.append(str(self.working_df_to_filter[df_col_names_list[i]].dtype))
            data_row.append(str(self.working_df_to_filter[df_col_names_list[i]].nunique()))
            data_row.append(str(self.working_df_to_filter[df_col_names_list[i]].isnull().sum()))

            data.append(data_row)


        no_drop_headers     =   ["Column Name","Data Type","Uniques","Total Nans"]
        no_drop_widths      =   [330,80,80,85]

        self.column_headers     =   no_drop_headers
        self.column_widths      =   no_drop_widths

        return(data)

# -----------------------------------------------------------------#
# -               Form Widget for dffilter cols                   -#
# -----------------------------------------------------------------#

class DataCleansingdfFiltersColumnWidget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent                     =   dfparms[0]
        self.filter_working_df_title    =   dfparms[1]

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)

        
        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersColumnWidget] : self.filter_working_df_title ",self.filter_working_df_title)
        if(DEBUG_CLEANSE_ROWS_FILTER_DETAILS) :
            print("  [DataCleansingdfFiltersColumnWidget] : self.filter_working_df_title ",self.filter_working_df)

        self.init_form()

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget] end")

    def reload_data(self,parent,working_df_title) :
        
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget][reload_data] ")

        self.parent                     =   parent
        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)

        self.dfStats.reload_data()
        self.colsdfStats.reload_data()

    def init_form(self):  

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form]self.filter_working_df_title",self.filter_working_df_title)

        from PyQt5.QtWidgets import QLabel
        dffilter_title_label   =   QLabel()
        dffilter_title_label.setText("\n" + self.filter_working_df_title + "\n")
        dffilter_title_label.setAlignment(Qt.AlignCenter)
        dffilter_title_label.resize(480,50)
        dffilter_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        parms               =    [self.filter_working_df]
        self.dfStats        =    DataCleansingdfStatsTable(parms)

        if(self.dfStats.num_rows < 5) :
            new_height  =   45 + (self.dfStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (5 * DEFAULT_ROW_HEIGHT)

        self.dfStats.setMinimumHeight(new_height)
        self.dfStats.setMaximumHeight(new_height)

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] : dfStatsloaded")

        parms               =    [self.filter_working_df,self.select_column_to_drop]
        self.colsdfStats    =    DataCleansingdfFiltersColumnTable(parms)

        if(self.colsdfStats.num_rows < 12) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (12 * DEFAULT_ROW_HEIGHT)

        self.colsdfStats.setMinimumHeight(new_height)
        self.colsdfStats.setMaximumHeight(new_height)
        #self.colsdfStats.setFixedSize(600,new_height)

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("Click on the column name column to drop the column from the working df.")
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")

        from PyQt5.QtWidgets import QPushButton

        criteria_button        =   QPushButton()     
        criteria_button.setText("Define\ndf Filter\nCriteria")
        criteria_button.setFixedSize(200,70)
        criteria_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        criteria_button.clicked.connect(self.define_df_Filter) 

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_df_Filter) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(200,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_for_df_Filter) 

        if(DEBUG_CLEANSE_COLUMN_DETAILS) :
            print("  [DataCleansing_select_column_to_cleanse_Widget][init_form] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        ccbutonsLayout  =   QHBoxLayout()
        ccbutonsLayout.addWidget(criteria_button)
        ccbutonsLayout.addWidget(return_button)
        ccbutonsLayout.addWidget(help_button)
        ccbutonsLayout.setAlignment(Qt.AlignHCenter)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.criteria_container = QWidget(self)
        self.criteria_container.setMaximumSize(550,600)
        self.criteria_container.setMinimumSize(550,600)

        #criteria_container.setFixedWidth(620)

        self.dfCriteriaLayout     =   QVBoxLayout(self.criteria_container)
        self.dfCriteriaLayout.addWidget(dffilter_title_label)
        self.dfCriteriaLayout.addWidget(self.dfStats)
        self.dfCriteriaLayout.addWidget(self.colsdfStats)
        self.dfCriteriaLayout.addWidget(note_label)
        self.dfCriteriaLayout.addLayout(ccbutonsLayout)
        self.dfCriteriaLayout.addStretch()
        self.dfCriteriaLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.dfCriteriaLayout)
        self.final_widget.setFixedWidth(600)
        #self.final_widget.setFixedHeight(1100)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)



    # -----------------------------------------------------------------#
    # -                Cleanse Columns Widget methods                 -#
    # -----------------------------------------------------------------#

    def select_column_to_drop(self) :

        row_number      =   None
        column_number   =   None

        for idx in self.colsdfStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget][select_column_to_drop] ",row_number,column_number)

        model   =   self.colsdfStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_CLEANSE_ROWS_FILTER) :    
            print("  [DataCleansingdfFiltersColumnWidget][select_column_to_drop] : colname [",cell,"]")

        try :

            #self.filter_working_df      =    
            self.filter_working_df.drop(cell, axis=1, inplace=True)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[df filter] column '" + cell + "' dropped successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            self.dfStats.reload_data()
            self.colsdfStats.reload_data()

        except Exception as e:                   
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[filter df drop column] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

    def define_df_Filter(self) :

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget][define_df_Filter]")

        self.parent.display_cleanse_rows_criteria(self.filter_working_df_title)
        
    def return_from_df_Filter(self) :

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget][return_from_cleanse_column]")

        from dfcleanser.Qt.data_cleansing.DataCleansing import DFS_SELECT
        self.parent.init_stacked_index()


    def help_for_df_Filter(self) :

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersColumnWidget][help_for_df_Filter]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SUBSET_CRITERIA
        display_url(SUBSET_CRITERIA)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Objects for dffilter cols end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Objects  for dffilter criteria                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                    Model for dffilter cols                    -#
# -----------------------------------------------------------------#
class DataCleansingdfStatsModel(QtCore.QAbstractTableModel):
    
    def __init__(self, coldata, colheaders):

        super(DataCleansingdfStatsModel,self).__init__()
        self._data          =   coldata
        self.column_names   =   colheaders

    def reload_data(self,coldata) :
        self._data = coldata

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
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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
# -                    Table for dffilter cols                    -#
# -----------------------------------------------------------------#
class DataCleansingdfStatsTable(QtWidgets.QTableView):

    def __init__(self,  colparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.workingdf          =   colparms[0]

        if(DEBUG_FILTERS_STATS_TABLE) :
            print("\n[DataCleansingdfStatsTable] : init")

        self.init_tableview()

        if(DEBUG_FILTERS_STATS_TABLE) :
            print("[DataCleansingdfStatsTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_FILTERS_STATS_TABLE) :
            print("  [DataCleansingdfStatsTable][reload_data]  ")

        statsdata       =   self.load_columns_info_data()
        self.model.reload_data(statsdata)

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 5) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (5 * DEFAULT_ROW_HEIGHT))

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_FILTERS_STATS_TABLE) :
            print("  [DataCleansingdfStatsTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statsdata     =   self.load_columns_info_data()
        
        if(DEBUG_FILTERS_STATS_TABLE) :
           print("  [DataCleansingdfStatsTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = DataCleansingdfStatsModel(statsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_FILTERS_STATS_TABLE) :
           print("  [DataCleansingdfStatsTable][init_tableview] : model loaded")

        self.num_rows   =   len(statsdata)
        
        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view headerDEBDEBUG_CLEANSE_ROWS_FILTERUG_CLEANSE_ROWS_FILTER
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(statsdata)
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
    def load_columns_info_data(self):

        if(DEBUG_FILTERS_STATS_TABLE) :
            print("  [DataCleansingdfStatsTable][load_columns_info_data]")

        data    =   []

        df          =   self.workingdf

        numrows     =   len(df)
        numcols     =   len(df.columns)
    
        import pandas as pd
        if isinstance(df.index, pd.core.indexes.range.RangeIndex) :
            indextype       =   "RangeIndex"
        else :
        
            if ( (isinstance(df.index, pd.core.indexes.base.Index)) or 
                (isinstance(df.index, pd.core.indexes.multi.MultiIndex)) ) : #(dfIndexType == 'pandas.core.indexes.base.Index') :
        
                index_columns   =   df.index.names
            
                if(len(index_columns) == 1) :
                    indextype   =   "Index"
                else :
                    indextype   =   "MultiIndex"

        data_row    =   []  

        data_row.append(str(numrows))
        data_row.append(str(numcols))
        data_row.append(str(indextype))

        data.append(data_row)

        self.column_headers     =   ["Number of Rows","Number of Columns","Index Type"]
        self.column_widths      =   [200,200,200]

        return(data)


# -----------------------------------------------------------------#
# -             Form Widget for dffilter criteria                 -#
# -----------------------------------------------------------------#

class DataCleansingdfFiltersCriteriaWidget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent                     =   dfparms[0]
        self.filter_working_df_title    =   dfparms[1]
         
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget]  :  self.filter_working_df_title ",self.filter_working_df_title)

        self.init_form()

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget] end")

    def reload_data(self,parent,workingdf_title) :
        
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget][reload_data] workingdf_title ",workingdf_title)

        self.parent                     =   parent
        self.filter_working_df_title    =   workingdf_title

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)
        
        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][reload_data] filter_working_df_title ",self.filter_working_df_title)

        self.dfStats.reload_data()#self.filter_working_df)        
        
        if(self.dfStats.num_rows < 5) :
            new_height  =   45 + (self.dfStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (5 * DEFAULT_ROW_HEIGHT)

        self.dfStats.setMinimumHeight(new_height)
        self.dfStats.setMaximumHeight(new_height)

        # get colstats

        self.colsdfStats.reload_data()
        
        if(self.colsdfStats.num_rows < 6) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (6 * DEFAULT_ROW_HEIGHT)

        self.colsdfStats.setMinimumHeight(new_height)
        self.colsdfStats.setMaximumHeight(new_height)
    
    def init_form(self):  

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form]")

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)
        
        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] self.filter_working_df_title",self.filter_working_df_title)
        
        from PyQt5.QtWidgets import QLabel
        df_title_label   =   QLabel()
        df_title_label.setText("" + self.filter_working_df_title)
        df_title_label.setAlignment(Qt.AlignCenter)
        df_title_label.resize(700,50)
        df_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QLabel
        dffilter_title_label   =   QLabel()
        dffilter_title_label.setText("Build dataframe Filter - Define Criteria\n")
        dffilter_title_label.setAlignment(Qt.AlignCenter)
        dffilter_title_label.resize(480,50)
        dffilter_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        parms               =    [self.filter_working_df]
        self.dfStats        =    DataCleansingdfStatsTable(parms)

        self.dfStats.setMaximumSize(700,150)
        self.dfStats.setMinimumSize(700,150)

        if(self.dfStats.num_rows < 5) :
            new_height  =   45 + (self.dfStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (5 * DEFAULT_ROW_HEIGHT)

        self.dfStats.setMinimumHeight(new_height)
        self.dfStats.setMaximumHeight(new_height)

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] : dfStatsloaded")

        parms               =    [self.filter_working_df,self.select_column_to_drop]
        self.colsdfStats    =    DataCleansingdfFiltersColumnTable(parms)

        self.colsdfStats.setMaximumSize(700,400)
        self.colsdfStats.setMinimumSize(700,400)

        if(self.colsdfStats.num_rows < 6) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (6 * DEFAULT_ROW_HEIGHT)

        self.colsdfStats.setMinimumHeight(new_height)
        self.colsdfStats.setMaximumHeight(new_height)

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] :colsdfStats loaded")

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("Click on the column name column to drop the column from the working df.")
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")

        form_parms      =   [get_subset_criteria_input_id,get_subset_criteria_input_idList,get_subset_criteria_input_labelList,get_subset_criteria_input_typeList,get_subset_criteria_input_placeholderList,get_subset_criteria_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.get_df_from_criteria,self.return_from_df_criteria,self.help_for_df_criteria]
        cfg_parms       =   None
        form_title      =   "Define Filter Criteria"
        form_width      =   600

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_criteria_form     =   dfcleanser_input_form_Widget(form_parms)

        self.df_criteria_form.setMaximumSize(700,550)
        self.df_criteria_form.setMinimumSize(700,550)


        code    =   cfg.get_config_value(get_subset_criteria_input_id+"Parms")
        
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] cfg code : ",code[0])

        if(not (code is None)) :

            self.df_criteria_form.set_form_input_value_by_index(0,code[0])

        else :

            code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df, add_df_to_dfc\n"
            code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + self.filter_working_df_title + "')\n\n\n"
            code_preamble   =   code_preamble + "criteria = user defined criteria\n\n\n"
            code_preamble   =   code_preamble + "df = df[criteria]              \n"
            code_preamble   =   code_preamble + "add_df_to_dfc('" + self.filter_working_df_title + "',df)\n\n"
            self.df_criteria_form.set_form_input_value_by_index(0,code_preamble)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        criteria_container = QWidget(self)
        criteria_container.setMaximumSize(700,550)
        criteria_container.setMinimumSize(700,550)

        self.dfCriteriaLayout     =   QVBoxLayout(criteria_container)
        self.dfCriteriaLayout.addWidget(df_title_label)
        self.dfCriteriaLayout.addWidget(self.dfStats)
        self.dfCriteriaLayout.addWidget(self.colsdfStats)
        self.dfCriteriaLayout.addWidget(note_label)
        self.dfCriteriaLayout.addStretch()
        self.dfCriteriaLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.criteria_widget   =   QWidget()
        self.criteria_widget.setLayout(self.dfCriteriaLayout)
        self.criteria_widget.setFixedWidth(600)
        form_container = QWidget(self)
        form_container.setFixedWidth(1000)

        self.formLayout     =   QVBoxLayout(form_container)
        self.formLayout.addWidget(self.df_criteria_form)        
        self.formLayout.addStretch()
        self.formLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.form_widget   =   QWidget()
        self.form_widget.setLayout(self.formLayout)
        self.form_widget.setFixedWidth(1000)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.criteria_widget)
        self.final_layout.addWidget(self.form_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)


        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] end")

    # -----------------------------------------------------------------#
    # -                Cleanse Columns Widget methods                 -#
    # -----------------------------------------------------------------#

    def select_column_to_drop(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][select_column_to_cleanse]",self.filter_working_df_title)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)

        row_number      =   None
        column_number   =   None

        for idx in self.colsdfStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][select_column_to_cleanse] ",row_number,column_number)

        model   =   self.colsdfStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_CLEANSE_ROWS_FILTER) :    
            print("[DataCleansingdfFiltersCriteriaWidget][select_column_to_cleanse] : colname [",cell,"]")

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox()
        dlg.setTextFormat(Qt.RichText)
        dlg.setWindowTitle("Delete Column")
        dlg.setText("Delete the '" + cell + "' Column")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
        button = dlg.exec()

        if(button == QMessageBox.Yes) :

            try :

                self.filter_working_df      =    self.filter_working_df.drop(cell, axis=1, inplace=True)

                title       =   "dfcleanser mesage"       
                status_msg  =   "[df criteria]  column '" + cell + "' dropped successfully"
                from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                display_status_msg(title,status_msg)

                self.parent.display_cleanse_rows_criteria(self.filter_working_df_title)

            except Exception as e:                   
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[filter df drop column] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)


    def get_df_from_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][get_df_from_criteria]")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        code    =   self.df_criteria_form.get_form_input_value_by_index(0)
        code    =   code.replace("\\","\\\\")

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import apply_criteria_to_df
        apply_criteria_to_df(self.filter_working_df,code,opstat) 

        if(opstat.get_status()) :

            cfg.set_config_value(get_subset_criteria_input_id+"Parms",[code])
            self.filter_working_df_title = "Filtered_df"
            self.parent.display_cleanse_rows_save_df(self.filter_working_df_title)


    def return_from_df_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][return_from_df_criteria]")

        self.parent.display_cleanse_rows()

    def help_for_df_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][help_for_df_criteria]")
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SUBSET_CRITERIA
        display_url(SUBSET_CRITERIA)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Objects  for dffilter criteria end              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Objects  for dffilter process df               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


class DataCleansingdfFiltersProcessdfWidget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent                     =   dfparms[0]
        self.filter_working_df_title    =   dfparms[1]
        
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersProcessdfWidget]  ")

        self.init_form()

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersProcessdfWidget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersProcessdfWidget][reload_data] ")

        self.parent                     =   parent
        self.filter_working_df_title    =   dftitle

        self.colsdfStats.reload_data()#self.filter_working_df_title,None)

    def init_form(self):  

        if(DEBUG_CLEANSE_ROWS) :
            print("  [DataCleansingdfFiltersProcessdfWidget][init_form]")

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.filter_working_df  =   get_dfc_dataframe_df(self.filter_working_df_title)

        from PyQt5.QtWidgets import QLabel
        self.dftitle_label   =   QLabel()
        self.dftitle_label.setText("\n"+self.filter_working_df_title)
        self.dftitle_label.setAlignment(Qt.AlignCenter)
        self.dftitle_label.resize(480,50)
        self.dftitle_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")


        from PyQt5.QtWidgets import QLabel
        dffilter_title_label   =   QLabel()
        dffilter_title_label.setText("Process New Filtered df\n")
        dffilter_title_label.setAlignment(Qt.AlignCenter)
        dffilter_title_label.resize(480,50)
        dffilter_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        parms               =    [self.filter_working_df]
        self.dfStats        =    DataCleansingdfStatsTable(parms)

        if(self.dfStats.num_rows < 5) :
            new_height  =   45 + (self.dfStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (5 * DEFAULT_ROW_HEIGHT)

        self.dfStats.setMinimumHeight(new_height)
        self.dfStats.setMaximumHeight(new_height)

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersCriteriaWidget][init_form] : dfStatsloaded")

        parms               =    [self.filter_working_df,None]
        self.colsdfStats    =    DataCleansingdfFiltersColumnTable(parms)

        if(self.colsdfStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsdfStats.setMinimumHeight(new_height)
        self.colsdfStats.setMaximumHeight(new_height)
        #self.colsdfStats.setFixedSize(600,new_height)

        form_parms      =   [save_subset_run_input_id,save_subset_run_input_idList,save_subset_run_input_labelList,save_subset_run_input_typeList,save_subset_run_input_placeholderList,save_subset_run_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.save_df_from_criteria,self.apply_new_filter,self.open_in_excel_df_criteria,self.return_from_df_criteria,self.help_for_df_criteria]
        cfg_parms       =   None
        form_title      =   "Process Filtered df"
        form_width      =   600

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.df_process_form     =   dfcleanser_input_form_Widget(form_parms)
            
        #self.df_process_form.set_form_input_value_by_index(0,self.filter_working_df_title)

        notes   =   "To save the new filtered as a df dfc df enter filtered_dataframe_title and click on Save Filtered df\n"
        notes   =   notes + "To apply another filter on the working df click on Apply New Filter.\n"
        notes   =   notes + "To open the Subset df in excel click on Save Open Subset df In Excel.\n"

        from PyQt5.QtWidgets import QLabel
        self.dffilter_note_label   =   QLabel()
        self.dffilter_note_label.setText(notes)
        self.dffilter_note_label.setAlignment(Qt.AlignLeft)
        self.dffilter_note_label.resize(600,120)
        self.dffilter_note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        criteria_container = QWidget(self)
        criteria_container.setFixedWidth(620)

        self.dfCriteriaLayout     =   QVBoxLayout(criteria_container)
        self.dfCriteriaLayout.addWidget(self.dftitle_label)
        self.dfCriteriaLayout.addWidget(self.dfStats)
        self.dfCriteriaLayout.addWidget(self.colsdfStats)
        self.dfCriteriaLayout.addWidget(self.df_process_form)
        self.dfCriteriaLayout.addWidget(self.dffilter_note_label)        
        self.dfCriteriaLayout.addStretch()
        self.dfCriteriaLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.dfCriteriaLayout)
        self.final_widget.setFixedWidth(600)
        #self.final_widget.setFixedHeight(900)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][init_form] end")

    # -----------------------------------------------------------------#
    # -                Cleanse Columns Widget methods                 -#
    # -----------------------------------------------------------------#

    def save_df_from_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][save_df_from_criteria]")

        new_df_title    =   self.df_process_form.get_form_input_value_by_index(0)

        if(len(new_df_title) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[save filtered df] invalid dftitle "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            from dfcleanser.common.cfg import dfc_df_history
            cfg.rename_dfc_dataframe("Filtered_df",new_df_title)

            title       =   "dfcleanser status"       
            status_msg  =   "filtered df stored as " + new_df_title
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            self.parent.display_cleanse_rows()

    def apply_new_filter(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][apply_new_filter]")

        self.parent.display_cleanse_rows_criteria(self.filter_working_df_title)

    def open_in_excel_df_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][open_in_excel_df_criteria]")

        from dfcleanser.common.common_utils import run_jscript
        script  =   "browse_df_in_df_browser('Filtered_df');"
        
        run_jscript(script)


    def return_from_df_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][return_from_df_criteria]")

        df_titles   =   cfg.get_dfc_dataframes_titles_list()
        if("Filtered_df" in df_titles) :
            cfg.drop_dfc_dataframe("Filtered_df")

        self.parent.display_cleanse_rows()


    def help_for_df_criteria(self) :

        if(DEBUG_CLEANSE_ROWS_FILTER) :
            print("  [DataCleansingdfFiltersProcessCriteriaWidget][help_for_df_criteria]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SUBSET_CRITERIA
        display_url(SUBSET_CRITERIA)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Objects  for dffilter process df end            -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



