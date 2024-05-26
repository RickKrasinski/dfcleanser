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

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont


import dfcleanser.common.cfg as cfg 
from dfcleanser.common.cfg import print_to_string, add_debug_to_log

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataCleansing_ID



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
# -                   Cleanse Columns Widgets                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -    display columns table to select which column to cleanse    -#
# -----------------------------------------------------------------#

class DataCleansing_select_column_to_cleanse_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle

        self.colsStats.reload_data()

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataCleanseLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        cleanse_column_title_label   =   QLabel()
        cleanse_column_title_label.setText("\n\nColumns To Cleanse\n")
        cleanse_column_title_label.setAlignment(Qt.AlignCenter)
        cleanse_column_title_label.resize(480,50)
        cleanse_column_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.DataCleanseLayout.addWidget(cleanse_column_title_label)

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_cleanse]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 15) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        self.DataCleanseLayout.addWidget(self.colsStats)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][init_form] : colsStatsloaded"))
        
        from PyQt5.QtWidgets import QLabel,QPushButton
        note_label   =   QLabel()
        note_label.setText("\nDouble click on the column name to cleanse the column.\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")
        self.DataCleanseLayout.addWidget(note_label)
        
        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_cleanse_column) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(200,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_for_cleanse_column) 

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][init_form] : buttons built"))

        from PyQt5.QtWidgets import QHBoxLayout
        ccbutonsLayout  =   QHBoxLayout()
        ccbutonsLayout.addWidget(return_button)
        ccbutonsLayout.addWidget(help_button)
        ccbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.DataCleanseLayout.addLayout(ccbutonsLayout)

        self.DataCleanseLayout.addStretch()
        self.setLayout(self.DataCleanseLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][init_form] end"))


    # -----------------------------------------------------------------#
    # -      DataCleansing_select_column_to_cleanse_Widge             -#
    # -----------------------------------------------------------------#

    def select_column_to_cleanse(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][select_column_to_cleanse]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][select_column_to_cleanse] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :    
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][select_column_to_cleanse] : colname [",cell,"]"))

        self.parent.display_cleanse_single_column(self.dftitle,cell)

    def return_from_cleanse_column(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][return_from_cleanse_column]"))

        from dfcleanser.Qt.data_cleansing.DataCleansing import DFS_SELECT
        self.parent.init_stacked_index()

    def help_for_cleanse_column(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_select_column_to_cleanse_Widget][help_for_cleanse_column]"))
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_CHANGE_ID
        display_url(CLEANSE_CHANGE_ID)



# -----------------------------------------------------------------#
# -              Cleanse Single Column Objects                    -#
# -----------------------------------------------------------------#

green_color     =   QColor(173, 236, 196)
yellow_color    =   QColor(250, 246, 190)
red_color       =   QColor(241, 196, 183) 


# -----------------------------------------------------------------#
# -             Table view and Model for single column            -#
# -----------------------------------------------------------------#
class DataCleansingSingleColumnModel(QtCore.QAbstractTableModel):
    def __init__(self, coldata, colheaders):

        super(DataCleansingSingleColumnModel,self).__init__()
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
                    
                if(row == 10) :

                    skew = self._data[index.row()][index.column()]

                    if ( (not (skew is None)) and (not(skew == " ")) ) : # && value !== "nan" && value !== " ") {

                        skew = float(self._data[index.row()][index.column()])

                        if ( (skew < -1.0) or (skew > 1.0) ) :
                            bgcolor     =   red_color
                        elif (skew < 66) :
                            bgcolor     =  yellow_color
                        else : 
                            bgcolor     =  green_color

                    else :
                        bgcolor = QtGui.QBrush(QtCore.Qt.white)     

                elif(row == 11) : 

                    kurtosis = self._data[index.row()][index.column()]
                    
                    if ( (not (kurtosis is None)) and (not(kurtosis == " ")) ) : # && value !== "nan" && value !== " ") {

                        kurtosis = float(self._data[index.row()][index.column()])

                        if ( (kurtosis < -2.0) or (kurtosis > 2.0) ) :
                            bgcolor     =  red_color
                        elif ( (kurtosis < -1.0) or (kurtosis > 1.0) ) :
                            bgcolor     =  yellow_color
                        else :
                            bgcolor     =  green_color
                    
                    else :
                        bgcolor = QtGui.QBrush(QtCore.Qt.white)     

                else :
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

class DataCleansingSingleColumnTable(QtWidgets.QTableView):

    def __init__(self,  colparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.dftitle            =   colparms[0]
        self.colname            =   colparms[1]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable] : init"))

        self.init_tableview()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,dftitle,colname):
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][reload_data] : dftile : colname : ",dftitle,colname))

        self.dftitle    =   dftitle
        self.colname    =   colname
        
        statsdata       =   self.load_columns_info_data()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][reload_data] : statsdata : ",statsdata))

        self.model.reload_data(statsdata)

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 15) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (15 * DEFAULT_ROW_HEIGHT))

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statsdata     =   self.load_columns_info_data()
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
           add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = DataCleansingSingleColumnModel(statsdata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
           add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][init_tableview] : model loaded"))

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 15) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (15 * DEFAULT_ROW_HEIGHT))

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

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][load_columns_info_data]",self.dftitle,self.colname))

        self.data    =   []

        numeric_infotitles      =   ["Column Name","Column Data Type","Total Nans","Non Nan Count","Nans % of Totla Col Values","Column Uniques Count","Mean","Std","Min","Max","Skew","Kurtosis"]
        non_numeric_infotitles  =   ["Column Name","Column Data Type","Total Nans","Non Nan Count","Nans % of Totla Col Values","Column Uniques Count"]
        categorical_infotitles  =   ["Column Name","Column Data Type","Total Nans","Non Nan Count","Nans % of Totla Col Values","Category Count","Category Ordered"]
        
        from dfcleanser.sw_utilities.dfc_qt_model import get_columns_info, NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN
        infodata    =   get_columns_info(self.dftitle,self.colname)
        coltype     =   infodata[0]
        infovalues  =   infodata[1]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][load_columns_info_data]",coltype,"     \n        ",infovalues))

        formatted_values    =   []
        formatted_values.append(infovalues[0])
        formatted_values.append(infovalues[1])
        formatted_values.append(str(infovalues[2]))
        formatted_values.append(str(infovalues[3]))
        formatted_values.append(str(float("{0:.3f}".format(infovalues[4]))) + "%")

        if(coltype == NUMERIC_COLUMN) :

            formatted_values.append(str(float("{0:.3f}".format(infovalues[5]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[6]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[7]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[8]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[9]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[10]))))
            formatted_values.append(str(float("{0:.3f}".format(infovalues[11]))))
            
            infotitles  =  numeric_infotitles  

        elif(coltype == CATEGORICAL_COLUMN) :

            formatted_values.append(str(infovalues[5]))
            formatted_values.append(str(infovalues[6]))

            infotitles  =  categorical_infotitles

        else :

            formatted_values.append(str(infovalues[5]))
            infotitles  =  non_numeric_infotitles  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][load_columns_info_data] : infotitles :\n      ",infotitles))
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][load_columns_info_data] : formatted_values:\n      ",formatted_values))

        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(formatted_values[i])

            self.data.append(data_row)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable] : data"))
            for j in range(len(self.data)) :
                add_debug_to_log("DataCleansingWidgets",print_to_string("  [",j,"] : ",self.data[j]))

        self.column_headers     =   ["Stat Name","Stat Value"]
        self.column_widths      =   [240,240]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingSingleColumnTable][load_columns_info_data][end]"))

        return(self.data)

# -----------------------------------------------------------------#
# -        single column form, stats and buttons widget           -#
# -----------------------------------------------------------------#
class DataCleansing_cleanse_single_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        from dfcleanser.sw_utilities.dfc_qt_model import (NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN)

        from dfcleanser.common.common_utils import (is_categorical_col, is_numeric_col)  
        if(is_categorical_col(self.df,self.colname))  :
            self.formtype       =   CATEGORICAL_COLUMN 
        elif(is_numeric_col(self.df,self.colname)) :
            self.formtype       =   NUMERIC_COLUMN
        else :
            self.formtype       =   NON_NUMERIC_COLUMN   

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget] end"))

    def reload_form(self,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][reload_form] :dftitle : colname : ",dftitle,colname))

        self.dftitle        =   dftitle
        self.colname        =   colname

    def build_form(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_form]",self.formtype))

        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM
        from dfcleanser.sw_utilities.dfc_qt_model import NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN

        if(self.formtype == NUMERIC_COLUMN) :

            form_parms      =   [DCM.change_values_input_id,DCM.change_values_input_idList,DCM.change_values_input_labelList,DCM.change_values_input_typeList,DCM.change_values_input_placeholderList,DCM.change_values_input_reqList]
            comboMethods    =   None
            comboList       =   None
            file_methods    =   None
            button_methods  =   [self.change_numeric_value]
            cfg_parms       =   None
            form_title      =   "\n\nChange Column Value\n"
            form_width      =   550

            selectDicts     =   comboList

        elif(self.formtype == NON_NUMERIC_COLUMN) :

            if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
                add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_form] NON_NUMERIC_COLUMN"))

            form_parms      =   [DCM.nn_change_values_input_id,DCM.nn_change_values_input_idList,DCM.nn_change_values_input_labelList,DCM.nn_change_values_input_typeList,DCM.nn_change_values_input_placeholderList,DCM.nn_change_values_input_reqList]
            comboList       =   None
            comboMethods    =   None
            file_methods    =   None
            button_methods  =   [self.change_non_numeric_value]
            cfg_parms       =   None
            form_title      =   "\n\nChange Column Value\n"
            form_width      =   550

            selectDicts     =   comboList

        elif(self.formtype == CATEGORICAL_COLUMN) :
            
            if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
                add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_form] CATEGORICAL_COLUMN"))

            form_parms      =   [DCM.rename_category_input_id,DCM.rename_category_input_idList,DCM.rename_category_input_labelList,DCM.rename_category_input_typeList,DCM.rename_category_input_placeholderList,DCM.rename_category_input_reqList]
            comboList       =   None
            comboMethods    =   [None]
            file_methods    =   None
            button_methods  =   [self.rename_category,self.rename_category_return]
            cfg_parms       =   None
            form_title      =   "\n\nRename Category\n"
            form_width      =   550
            
            selectDicts     =   []

            import pandas as pd
            CI          =   pd.CategoricalIndex(self.df[self.colname])
            cats        =   CI.categories.tolist()
            strcats     =   []
            for i in range(len(cats)) :
                strcats.append(str(cats[i]))
            catlist     =   {"default":str(cats[0]),"list":strcats}
            selectDicts.append(catlist)
            
            if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
                add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_form] catlist \n         ",catlist))

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        value_form     =   dfcleanser_input_form_Widget(form_parms)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_form] end"))
        
        return(value_form)


    def build_cmd_buttons_layout(self,buttonsLayout) :
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_cmd_buttons_layout] self.formtype : ",self.formtype))

        # display function bar
        from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel

        uniques_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_cleansing\\uniques.png"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        uniques_label.setPixmap(pixmap)
        uniques_label.resize(90, 90)

        uniques_button        =   QPushButton()     
        uniques_button.setText("Uniques")
        uniques_button.setFixedSize(90,30)
        uniques_button.setToolTip("Uniques")
        uniques_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        uniques_button.clicked.connect(self.get_column_uniques) 
        
        uniquesLayout   =   QVBoxLayout()
        uniquesLayout.addWidget(uniques_label)
        uniquesLayout.addWidget(uniques_button)
        uniquesLayout.addStretch()
        uniquesLayout.setAlignment(Qt.AlignCenter)

        outliers_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_cleansing\\outliers.png"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        outliers_label.setPixmap(pixmap)
        outliers_label.resize(90, 90)

        outliers_button        =   QPushButton()     
        outliers_button.setText("Outliers")
        outliers_button.setFixedSize(90,30)
        outliers_button.setToolTip("Outliers")
        outliers_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        outliers_button.clicked.connect(self.get_column_outliers) 

        outliersLayout   =   QVBoxLayout()
        outliersLayout.addWidget(outliers_label)
        outliersLayout.addWidget(outliers_button)
        outliersLayout.addStretch()
        outliersLayout.setAlignment(Qt.AlignCenter)
       
        from dfcleanser.sw_utilities.dfc_qt_model import NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN

        if(self.formtype == NUMERIC_COLUMN) :
            buttonsLayout.addLayout(uniquesLayout)
            buttonsLayout.addLayout(outliersLayout)
        if(self.formtype == NON_NUMERIC_COLUMN) :
            buttonsLayout.addLayout(uniquesLayout)
        elif(self.formtype == CATEGORICAL_COLUMN) :
            buttonsLayout.addLayout(uniquesLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][build_cmd_buttons_layout] end"))


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QPushButton 
        self.DataCleanseFormLayout      =   QVBoxLayout()

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.change_value_form     =   self.build_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][init_form] : form built : "))

        # display function bar
        from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel

        from PyQt5.QtWidgets import QHBoxLayout
        self.cmd_butonsLayout  =   QHBoxLayout()
        self.build_cmd_buttons_layout(self.cmd_butonsLayout)
        self.cmd_butonsLayout.setAlignment(Qt.AlignCenter)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][init_form] : cmd buttons built : "))

        self.DataCleanseFormLayout.addWidget(self.change_value_form)
        self.DataCleanseFormLayout.addLayout(self.cmd_butonsLayout)
        self.DataCleanseFormLayout.addStretch()

        self.setLayout(self.DataCleanseFormLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][init_form] : end : "))

    # -----------------------------------------------------------------#
    # -    DataCleansing_cleanse_single_column_form_Widget Methods    -#
    # -----------------------------------------------------------------#

    def change_numeric_value(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][change_numeric_value]"))

        oldvalue        =   self.change_value_form.get_form_input_value_by_index(0)
        newvalue        =   self.change_value_form.get_form_input_value_by_index(1)
        changeparms     =   [self.dftitle,self.colname,oldvalue,newvalue]

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import  change_column_values  
        change_column_values(changeparms)

    def change_non_numeric_value(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][change_non_numeric_value]"))
    
    def rename_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][rename_category]"))

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import  rename_category
        oldcat  =   self.change_value_form.get_form_input_value_by_index(0)
        newcat  =   self.change_value_form.get_form_input_value_by_index(1)
        rename_category(self.dftitle,self.colname,oldcat,newcat)   

    def rename_category_return(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][rename_category_return]"))
        
        self.parent.display_cleanse_columns()

    def get_column_uniques(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            padd_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][get_column_uniques]"))

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import display_uniques_for_cleanse_column
        display_uniques_for_cleanse_column(self.dftitle,self.colname)
    
    def get_column_outliers(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_DETAILS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_form_Widget][get_column_outliers]"))
        
        from dfcleanser.Qt.data_cleansing.DataCleansingControl import display_outliers_for_cleanse_column
        display_outliers_for_cleanse_column(self.dftitle,self.colname)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            single column command taskbar widgets              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataCleansing_cleanse_single_column_float_nans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        round_button        =   QPushButton()     
        round_button.setText("Round\nColumn\nValues")
        round_button.setFixedSize(120,90)
        round_button.setToolTip("Round Column Values")
        round_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        round_button.clicked.connect(self.round_column) 
        cmdbutonsLayout.addWidget(round_button)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        drop_nan_rows_button        =   QPushButton()     
        drop_nan_rows_button.setText("Drop\nColumn\nNan Rows")
        drop_nan_rows_button.setFixedSize(120,90)
        drop_nan_rows_button.setToolTip("Drop Column Nan Rows")
        drop_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_nan_rows_button.clicked.connect(self.drop_nan_row) 
        cmdbutonsLayout.addWidget(drop_nan_rows_button)

        fill_nan_rows_button        =   QPushButton()     
        fill_nan_rows_button.setText("Fill\nNan Values")
        fill_nan_rows_button.setFixedSize(120,90)
        fill_nan_rows_button.setToolTip("Fill Nan Values")
        fill_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        fill_nan_rows_button.clicked.connect(self.display_fill_nan_values) 
        cmdbutonsLayout.addWidget(fill_nan_rows_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_fillna) 
        cmdbutonsLayout.addWidget(help_button)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))

    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def round_column(self)  :
        gen_round_column(self,self.dftitle,self.colname)
    def drop_nan_row(self)  :
        gen_drop_nan_row(self,self.dftitle,self.colname)
    def display_fill_nan_values(self)  :
        gen_display_fill_nan_values(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_fillna(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)


class DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        round_button        =   QPushButton()     
        round_button.setText("Round\nColumn\nValues")
        round_button.setFixedSize(120,90)
        round_button.setToolTip("Round Column Values")
        round_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        round_button.clicked.connect(self.round_column) 
        cmdbutonsLayout.addWidget(round_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_fillna) 
        cmdbutonsLayout.addWidget(help_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_float_nans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))
    
    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def round_column(self)  :
        gen_round_column(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_fillna(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)


class DataCleansing_cleanse_single_column_int_nans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        drop_nan_rows_button        =   QPushButton()     
        drop_nan_rows_button.setText("Drop\nColumn\nNan Rows")
        drop_nan_rows_button.setFixedSize(120,90)
        drop_nan_rows_button.setToolTip("Drop Column Nan Rows")
        drop_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_nan_rows_button.clicked.connect(self.drop_nan_row) 
        cmdbutonsLayout.addWidget(drop_nan_rows_button)

        fill_nan_rows_button        =   QPushButton()     
        fill_nan_rows_button.setText("Fill\nNan Values")
        fill_nan_rows_button.setFixedSize(120,90)
        fill_nan_rows_button.setToolTip("Fill Nan Values")
        fill_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        fill_nan_rows_button.clicked.connect(self.display_fill_nan_values) 
        cmdbutonsLayout.addWidget(fill_nan_rows_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_fillna) 
        cmdbutonsLayout.addWidget(help_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_int_nans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))


    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def drop_nan_row(self)  :
        gen_drop_nan_row(self,self.dftitle,self.colname)
    def display_fill_nan_values(self)  :
        gen_display_fill_nan_values(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_fillna(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)


class DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            padd_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_fillna) 
        cmdbutonsLayout.addWidget(help_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))

    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_fillna(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)

class DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        whitespace_button        =   QPushButton()     
        whitespace_button.setText("Remove\nWhite\nSpace")
        whitespace_button.setFixedSize(120,90)
        whitespace_button.setToolTip("Remove White Space")
        whitespace_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        whitespace_button.clicked.connect(self.remove_white_space) 
        cmdbutonsLayout.addWidget(whitespace_button)

        drop_nan_rows_button        =   QPushButton()     
        drop_nan_rows_button.setText("Drop\nColumn\nNan Rows")
        drop_nan_rows_button.setFixedSize(120,90)
        drop_nan_rows_button.setToolTip("Drop Column Nan Rows")
        drop_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_nan_rows_button.clicked.connect(self.drop_nan_row) 
        cmdbutonsLayout.addWidget(drop_nan_rows_button)

        fill_nan_rows_button        =   QPushButton()     
        fill_nan_rows_button.setText("Fill\nNan Values")
        fill_nan_rows_button.setFixedSize(120,90)
        fill_nan_rows_button.setToolTip("Fill Nan Values")
        fill_nan_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        fill_nan_rows_button.clicked.connect(self.display_fill_nan_values) 
        cmdbutonsLayout.addWidget(fill_nan_rows_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_column) 
        cmdbutonsLayout.addWidget(help_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))

    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def remove_white_space(self)  :
        gen_remove_white_space(self,self.dftitle,self.colname)
    def drop_nan_row(self)  :
        gen_drop_nan_row(self,self.dftitle,self.colname)
    def display_fill_nan_values(self)  :
        gen_display_fill_nan_values(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_column(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)


class DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()

        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        drop_rows_button        =   QPushButton()     
        drop_rows_button.setText("Drop\nCurrent\nValue Rows")
        drop_rows_button.setFixedSize(120,90)
        drop_rows_button.setToolTip("Drop Current Value Rows")
        drop_rows_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_rows_button.clicked.connect(self.drop_values_rows) 
        cmdbutonsLayout.addWidget(drop_rows_button)

        whitespace_button        =   QPushButton()     
        whitespace_button.setText("Remove\nWhite\nSpace")
        whitespace_button.setFixedSize(120,90)
        whitespace_button.setToolTip("Remove White Space")
        whitespace_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        whitespace_button.clicked.connect(self.remove_white_space) 
        cmdbutonsLayout.addWidget(whitespace_button)

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(120,90)
        return_button.setToolTip("Return")
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_column) 
        cmdbutonsLayout.addWidget(return_button)

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(120,90)
        help_button.setToolTip("Help")
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_column) 
        cmdbutonsLayout.addWidget(help_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[[DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget][init_form  end] : ",self.dftitle,self.colname))

    def drop_column(self) :
        gen_drop_column(self,self.dftitle,self.colname)
    def drop_values_rows(self)  :
        gen_drop_values_rows(self,self.dftitle,self.colname)
    def remove_white_space(self)  :
        gen_remove_white_space(self,self.dftitle,self.colname)
    def return_column(self) :
        gen_return_column(self)
    def help_column(self) :
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
        display_url(CLEANSE_FILLNA_COLUMN_ID)


class DataCleansing_cleanse_single_column_category_taskbar_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget]",self.dftitle,self.colname))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget] end"))


    def reload_data(self, dfparms) :

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][init_form] : ",self.dftitle,self.colname))

        # build the overall dtypes layout
        
        from PyQt5.QtWidgets import QPushButton, QHBoxLayout 

        #total_nans      =   self.df[self.colname].isnull().sum()

        from PyQt5.QtWidgets import QHBoxLayout
        cmdbutonsLayout  =   QHBoxLayout()
        
        drop_col_button        =   QPushButton()     
        drop_col_button.setText("Drop\nColumn")
        drop_col_button.setFixedSize(120,90)
        drop_col_button.setToolTip("Drop Column")
        drop_col_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_col_button.clicked.connect(self.drop_cat_column) 
        cmdbutonsLayout.addWidget(drop_col_button)

        add_cat_button        =   QPushButton()     
        add_cat_button.setText("Add\nNew\nCategory")
        add_cat_button.setFixedSize(120,90)
        add_cat_button.setToolTip("Add New Category")
        add_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        add_cat_button.clicked.connect(self.add_new_category) 
        cmdbutonsLayout.addWidget(add_cat_button)
        
        rem_cat_button        =   QPushButton()     
        rem_cat_button.setText("Remove\nCategory(s)")
        rem_cat_button.setFixedSize(120,90)
        rem_cat_button.setToolTip("Remove Category")
        rem_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        rem_cat_button.clicked.connect(self.remove_category) 
        cmdbutonsLayout.addWidget(rem_cat_button)

        rem_unused_cat_button        =   QPushButton()     
        rem_unused_cat_button.setText("Remove\nUnused\nCategory(s)")
        rem_unused_cat_button.setFixedSize(120,90)
        rem_unused_cat_button.setToolTip("Remove Unused Category(s)")
        rem_unused_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        rem_unused_cat_button.clicked.connect(self.remove_unused_category) 
        cmdbutonsLayout.addWidget(rem_unused_cat_button)

        reorder_cat_button        =   QPushButton()     
        reorder_cat_button.setText("Reorder\nCategories")
        reorder_cat_button.setFixedSize(120,90)
        reorder_cat_button.setToolTip("Reorder Categories")
        reorder_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        reorder_cat_button.clicked.connect(self.reorder_categories) 
        cmdbutonsLayout.addWidget(reorder_cat_button)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][init_form] : "))

        sort_cat_button        =   QPushButton()     
        sort_cat_button.setText("Sort\nCategory\nValues")
        sort_cat_button.setFixedSize(120,90)
        sort_cat_button.setToolTip("Sort Category Values")
        sort_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        sort_cat_button.clicked.connect(self.sort_categories) 
        cmdbutonsLayout.addWidget(sort_cat_button)

        toggle_cat_button        =   QPushButton()     
        toggle_cat_button.setText("Toggle\nCategory\nOrder")
        toggle_cat_button.setFixedSize(120,90)
        toggle_cat_button.setToolTip("Toggle Category Order")
        toggle_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        toggle_cat_button.clicked.connect(self.toggle_category_order) 
        cmdbutonsLayout.addWidget(toggle_cat_button)

        help_cat_button        =   QPushButton()     
        help_cat_button.setText("Help")
        help_cat_button.setFixedSize(120,90)
        help_cat_button.setToolTip("Help")
        help_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_cat_button.clicked.connect(self.help_category) 
        cmdbutonsLayout.addWidget(help_cat_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(cmdbutonsLayout)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][init_form][end] : "))


    def drop_cat_column(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][drop_cat_column]"))

        gen_drop_column(self,self.dftitle,self.colname)

    def add_new_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][add_new_category]"))

        self.parent.display_add_new_category(self.dftitle,self.colname)

    def remove_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][remove_category]"))

        self.parent.display_remove_category(self.dftitle,self.colname)

    def remove_unused_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][remove_unused_category]"))


        from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)

        import pandas as pd
        CI          =   pd.CategoricalIndex(df[self.colname])
        cats        =   CI.categories.tolist()
        num_cats    =   len(cats)
    
        cats_counts     =   CI.value_counts()
        counts_dict     =   cats_counts.to_dict()
        cat_counts      =   []

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][load_categories_data] cats : \n    ",cats))
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][load_categories_data] counts_dict : \n    ",counts_dict))

        counts_keys         =   list(counts_dict.keys())

        unused_categories   =   []

        for i in range(len(counts_keys)) :
            current_count   =   counts_dict.get(counts_keys[i])
            if(current_count == 0) :
                unused_categories.append(counts_keys[i])
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][load_categories_data] unused_categories : \n    ",len(unused_categories),unused_categories ))

        if(len(unused_categories) == 0) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("TDrop Unused Categories")
            dlg.setText("There are currently no unused categories")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            return()
        
        else :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Verify Drop Unused Categories")
            dlg.setText("There are " + str(len(unused_categories)) + " to Remove. Remove Now?")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            if(button == QMessageBox.Yes) :

                from dfcleanser.Qt.data_cleansing.DataCleansingControl import remove_unused_categories
                opstat  =   remove_unused_categories(self.dftitle,self.colname)

                if(opstat.get_status()) :

                    from PyQt5.QtWidgets import QMessageBox
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Remove Unused Categories Status")
                    dlg.setText("Unused Categories removed successfully")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setStyleSheet("QLabel{min-width: 300px;}")
                    button = dlg.exec()

                    from dfcleanser.common.cfg import df_Column_Changed_signal
                    df_Column_Changed_signal.issue_notice(self.dftitle)


                else :

                    title       =   "dfcleanser error"       
                    status_msg  =   "Error Removing Unused Categories selected "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)

        return()

    def reorder_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][reorder_categories]"))

        self.parent.display_reorder_category(self.dftitle,self.colname)

    def sort_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][sort_categories]"))

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import sort_categories
        opstat  =   sort_categories(self.dftitle,self.colname)

        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Sort Categories Status")
            dlg.setText("Categories sorted successfully")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)


        return()

    def toggle_category_order(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][toggle_category_order]"))
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)

        import pandas as pd

        CI              =   pd.CategoricalIndex(df[self.colname])
        cats_ordered    =   CI.ordered

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Verify Drop Unused Categories")
        if(cats_ordered) :
            dlg.setText("Current Categories are ordered - toggle to unordered?") 
        else :   
            dlg.setText("Current Categories are unordered - toggle to ordered?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setStyleSheet("QLabel{min-width: 300px;}")
        button = dlg.exec()

        if(button == QMessageBox.Yes) :

            try :  

                if(cats_ordered) :
                    CI  =   CI.as_unordered()
                else :
                    CI  =   CI.as_ordered()

                title       =   "dfcleanser mesage"   
                if(cats_ordered) :   
                    status_msg  =   "Categories toggled to ordered"
                else :
                    status_msg  =   "Categories toggled to unordered"

                from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                display_status_msg(title,status_msg)

                from dfcleanser.common.cfg import df_Column_Changed_signal
                df_Column_Changed_signal.issue_notice(self.dftitle)

            except Exception as e :

                title       =   "dfcleanser exception"       
                status_msg  =   "[Order Categories] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

    def help_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_category_taskbar_Widget][help_category]"))
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_CAT_COL_RENAME_ID
        display_url(CLEANSE_CAT_COL_RENAME_ID)

# -----------------------------------------------------------------#
# -              Cleanse Single Column Form Methods               -#
# -----------------------------------------------------------------#

def gen_drop_column(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][drop_column]"))

    from PyQt5.QtWidgets import QMessageBox
    dlg = QMessageBox(parent)
    dlg.setWindowTitle("Verify Drop Column")
    dlg.setText("Do you want to drop column " + colname)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setStyleSheet("QLabel{min-width: 300px;}")
    button = dlg.exec()

    if(button == QMessageBox.Yes) :

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import drop_column
        opstat  =   drop_column(dftitle,colname)

        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(parent)
            dlg.setWindowTitle("Drop Column Status")
            dlg.setText("Column " +  colname +" dropped successfully")
            dlg.setStandardButtons(QMessageBox.OK)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()


def gen_drop_values_rows(parent,dftitle,colname) :
        
    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][drop_values_rows)]"))
            
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()

    from dfcleanser.common.common_utils import run_jscript
    script  =   "display_Column_Uniques_To_Drop('" + dftitle + "','" + colname + "');"
    run_jscript(script)

    return()

    from PyQt5.QtWidgets import QMessageBox
    dlg = QMessageBox(parent)
    dlg.setWindowTitle("Verify Drop Value Rows")
    dlg.setText("Do you want to drop rows with value " + colname)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setStyleSheet("QLabel{min-width: 300px;}")
    button = dlg.exec()

    value   =   "TBD"

    if(button == QMessageBox.Yes) :

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import drop_value_rows
        opstat  =   drop_value_rows(dftitle,colname,value)

        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(parent)
            dlg.setWindowTitle("Drop Value Rows Status")
            dlg.setText("Rows dropped successfully")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()


def gen_round_column(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][round_column]"))

    parent.parent.display_round_column(dftitle,colname)

def gen_drop_nan_row(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][drop_nan_row]"))

    from PyQt5.QtWidgets import QMessageBox
    dlg = QMessageBox(parent)
    dlg.setWindowTitle("Verify Drop Nan Rows")
    dlg.setText("Do you want to drop rows with nan in  " + colname)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setStyleSheet("QLabel{min-width: 300px;}")
    button = dlg.exec()

    if(button == QMessageBox.Yes) :
            
        from dfcleanser.Qt.data_cleansing.DataCleansingControl import drop_nan_rows
        opstat  =   drop_nan_rows(dftitle,colname)

        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(parent)
            dlg.setWindowTitle("Rows With Nan Column Values Status")
            dlg.setText("Nan Rows Dropped successfully")
            dlg.setStandardButtons(QMessageBox.OK)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

def gen_display_fill_nan_values(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][display_fill_nan_values]",dftitle,colname))

    parent.parent.display_fillna_column(dftitle,colname)

def fill_nan_values(self) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][fill_nan_values]",self.dftitle,self.colname))

    fillvalue       =   "TBD"
    fillnamethod    =   "TBD"
    from dfcleanser.Qt.data_cleansing.DataCleansingControl import fill_nan_values
    opstat  =   fill_nan_values(self.dftitle,self.colname,fillvalue,fillnamethod)

    if(opstat.get_status()) :

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Fill Nan Values Status")
        dlg.setText("Nan Values Filled successfully")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setStyleSheet("QLabel{min-width: 300px;}")
        button = dlg.exec()

    else :

        if(len(opstat.get_errorMsg()) > 0 ) :
        
            title       =   "dfcleanser exception"       
            status_msg  =   opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

def gen_return_column(parent) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][retrun_column]"))

    parent.parent.display_cleanse_columns()

def gen_remove_white_space(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_taskbar_Widget][remove_white_space]"))

    parent.parent.display_whitespace_column(dftitle,colname)



# -----------------------------------------------------------------#
# -            Cleanse Numeric Single Column Widget               -#
# -----------------------------------------------------------------#

class DataCleansing_cleanse_single_column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_Widget]",self.dftitle,self.colname))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
           add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_Widget][reload_data] ",dftitle,colname))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.colsStats.reload_data(self.dftitle,self.colname) 

        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform.reload_form(self.dftitle,self.colname)#   =    DataCleansing_cleanse_single_column_form_Widget(parms)

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout

        self.DataCleanseLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.cleanse_column_title_label   =   QLabel()
        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.cleanse_column_title_label.setAlignment(Qt.AlignCenter)
        self.cleanse_column_title_label.resize(480,50)
        self.cleanse_column_title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")
        self.DataCleanseLayout.addWidget(self.cleanse_column_title_label)
        
        # build the cleanse form
        from PyQt5.QtWidgets import QHBoxLayout
        self.DataCleanse_form_layout    =   QHBoxLayout()

        # build the stats widget
        parms              =    [self.dftitle,self.colname]
        self.colsStats     =    DataCleansingSingleColumnTable(parms)

        if(self.colsStats.num_rows < 20) :
            new_height  =   35 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (20 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        self.DataCleanse_form_layout.addWidget(self.colsStats)

        # build the form widget
        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform   =    DataCleansing_cleanse_single_column_form_Widget(parms)

        self.DataCleanse_form_layout.addWidget(self.cleanseform)
        self.DataCleanse_form_layout.setAlignment(Qt.AlignCenter)

        self.DataCleanseLayout.addLayout(self.DataCleanse_form_layout)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df         =   get_dfc_dataframe_df(self.dftitle)
        total_nans      =   self.df[self.colname].isnull().sum()

        # build the cmd taskbar
        parms              =    [self.parent,self.dftitle,self.colname]
        if(total_nans > 0) :

            from dfcleanser.common.common_utils import is_float_col
            if(is_float_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_float_nans_taskbar_Widget(parms)
            else :
                self.taskbar       =    DataCleansing_cleanse_single_column_int_nans_taskbar_Widget(parms) 

        else :

            from dfcleanser.common.common_utils import is_float_col
            if(is_float_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget(parms)
            else :
                self.taskbar       =    DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget(parms) 

        self.DataCleanseLayout.addWidget(self.taskbar)
        self.DataCleanseLayout.addStretch()
        
        self.setLayout(self.DataCleanseLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN_SINGLE")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_single_column_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -            Cleanse Numeric Single Column Widget end           -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -           Cleanse Non Numeric Single Column Widget            -#
# -----------------------------------------------------------------#

class DataCleansing_cleanse_non_numeric_single_column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_non_numeric_single_column_Widget] : dftitle : colname : ",self.dftitle,self.colname))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_non_numeric_single_column_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_non_numeric_single_column_Widget][reload_data] ",dftitle,colname))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.colsStats.reload_data(self.dftitle,self.colname) 

        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform.reload_form(self.dftitle,self.colname)#   =    DataCleansing_cleanse_single_column_form_Widget(parms)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_non_numeric_single_column_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataCleanseLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.cleanse_column_title_label   =   QLabel()
        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.cleanse_column_title_label.setAlignment(Qt.AlignCenter)
        self.cleanse_column_title_label.resize(480,50)
        self.cleanse_column_title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")
        self.DataCleanseLayout.addWidget(self.cleanse_column_title_label)
        
        # build the cleanse form
        from PyQt5.QtWidgets import QHBoxLayout
        self.DataCleanse_form_layout    =   QHBoxLayout()

        # build the stats widget
        parms              =    [self.dftitle,self.colname]
        self.colsStats     =    DataCleansingSingleColumnTable(parms)

        if(self.colsStats.num_rows < 20) :
            new_height  =   35 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (20 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        self.DataCleanse_form_layout.addWidget(self.colsStats)

        # build the form widget
        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform   =    DataCleansing_cleanse_single_column_form_Widget(parms)

        self.DataCleanse_form_layout.addWidget(self.cleanseform)
        self.DataCleanse_form_layout.setAlignment(Qt.AlignCenter)

        self.DataCleanseLayout.addLayout(self.DataCleanse_form_layout)
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        total_nans      =   self.df[self.colname].isnull().sum()
        
        # build the cmd taskbar
        parms              =    [self.parent,self.dftitle,self.colname]
        if(total_nans > 0) :

            from dfcleanser.common.common_utils import is_float_col, is_int_col 
            if(is_float_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_float_nans_taskbar_Widget(parms)
            elif(is_int_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_int_nans_taskbar_Widget(parms)
            else :
                self.taskbar       =    DataCleansing_cleanse_single_column_nonnumeric_nans_taskbar_Widget(parms) 

        else :

            from dfcleanser.common.common_utils import is_float_col, is_int_col
            if(is_float_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_float_nonans_taskbar_Widget(parms)
            elif(is_int_col(self.df,self.colname)) :
                self.taskbar       =    DataCleansing_cleanse_single_column_int_nonans_taskbar_Widget(parms) 
            else :
                self.taskbar       =    DataCleansing_cleanse_single_column_nonnumeric_nonans_taskbar_Widget(parms) 

        self.DataCleanseLayout.addWidget(self.taskbar)
        self.DataCleanseLayout.addStretch()
        
        self.setLayout(self.DataCleanseLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_non_numeric_single_column_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -             Cleanse Category Single Column Widget             -#
# -----------------------------------------------------------------#

class DataCleansing_cleanse_category_single_column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_category_single_column_Widget] : dftitle : colname : ",self.dftitle,self.colname))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_category_single_column_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_category_single_column_Widget][reload_data] ",dftitle,colname))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.colsStats.reload_data(self.dftitle,self.colname) 

        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform.reload_form(self.dftitle,self.colname)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_category_single_column_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataCleanseLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.cleanse_column_title_label   =   QLabel()
        self.cleanse_column_title_label.setText("\n\n'" + self.colname + "'Cleansing\n")
        self.cleanse_column_title_label.setAlignment(Qt.AlignCenter)
        self.cleanse_column_title_label.resize(480,50)
        self.cleanse_column_title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")
        self.DataCleanseLayout.addWidget(self.cleanse_column_title_label)
        
        # build the cleanse form
        from PyQt5.QtWidgets import QHBoxLayout
        self.DataCleanse_form_layout    =   QHBoxLayout()

        # build the stats widget
        parms              =    [self.dftitle,self.colname]
        self.colsStats     =    DataCleansingSingleColumnTable(parms)

        if(self.colsStats.num_rows < 20) :
            new_height  =   35 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   35 + (20 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        self.DataCleanse_form_layout.addWidget(self.colsStats)

        # build the form widget
        parms              =    [self.parent,self.dftitle,self.colname]
        self.cleanseform   =    DataCleansing_cleanse_single_column_form_Widget(parms)

        self.DataCleanse_form_layout.addWidget(self.cleanseform)
        self.DataCleanse_form_layout.setAlignment(Qt.AlignCenter)

        self.DataCleanseLayout.addLayout(self.DataCleanse_form_layout)

        # build the cmd taskbar
        parms              =    [self.parent,self.dftitle,self.colname]
        self.taskbar       =    DataCleansing_cleanse_single_column_category_taskbar_Widget(parms)

        self.DataCleanseLayout.addWidget(self.taskbar)
        self.DataCleanseLayout.addStretch()
        
        self.setLayout(self.DataCleanseLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_category_single_column_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -            Cleanse Numeric Single Column Widget end           -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                     round column form widget                  -#
# -----------------------------------------------------------------#

class DataCleansing_Round_Column_Form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        from dfcleanser.sw_utilities.dfc_qt_model import NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget] end"))
    
    def reload_data(self,parent,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][reload_data] ",dftitle,colname))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.stats_table.reload_data(self.dftitle,self.colname) 

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

        self.DataCleanseRoundColumnLayout       =   QHBoxLayout()

        self.DataCleanseRoundColumnStatsLayout  =   QVBoxLayout()
        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)
        self.DataCleanseRoundColumnStatsLayout.addWidget(self.stats_table)
        self.DataCleanseRoundColumnStatsLayout.addStretch()
        
        self.DataCleanseRoundColumnLayout.addLayout(self.DataCleanseRoundColumnStatsLayout)


        self.DataCleanseRoundColumnFormLayout   =   QVBoxLayout()
               
        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM
        from dfcleanser.sw_utilities.dfc_qt_model import NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN

        form_parms      =   [DCM.col_round_input_id,DCM.col_round_input_idList,DCM.col_round_input_labelList,DCM.col_round_input_typeList,DCM.col_round_input_placeholderList,DCM.col_round_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.round_column_value,self.round_column_return,self.round_column_help]
        cfg_parms       =   None
        form_title      =   "\n\nRound Column Values\n"
        form_width      =   450

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)            

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.round_column_form     =   dfcleanser_input_form_Widget(form_parms)
        self.DataCleanseRoundColumnFormLayout.addWidget(self.round_column_form)
        self.DataCleanseRoundColumnFormLayout.addStretch()

        self.DataCleanseRoundColumnLayout.addLayout(self.DataCleanseRoundColumnFormLayout)
        self.DataCleanseRoundColumnLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.DataCleanseRoundColumnLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][init_form] : end : "))

    # -----------------------------------------------------------------#
    # -                Cleanse Single Column Form Methods             -#
    # -----------------------------------------------------------------#

    def round_column_value(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][round_column_value]"))

        round_digits    =   self.round_column_form.get_form_input_value_by_index(0)

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import round_column_data
        opstat  =   round_column_data(self.dftitle,self.colname,round_digits)

        self.parent.display_cleanse_single_column(self.dftitle,self.colname)
        

    def round_column_return(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][round_column_return]"))
        
        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

    def round_column_help(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Round_Column_Form_Widget][round_column_help]"))

        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

# -----------------------------------------------------------------#
# -                remove whitespace form widget                  -#
# -----------------------------------------------------------------#

class DataCleansing_Remove_Whitespace_Form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel 
        self.DataCleanseRemoveWhitespaceLayout          =   QHBoxLayout()

        self.DataCleanseRemoveWhitespaceTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveWhitespaceTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseRemoveWhitespaceTableLayout.addWidget(self.stats_table)
        self.DataCleanseRemoveWhitespaceTableLayout.addStretch()
        self.DataCleanseRemoveWhitespaceLayout.addLayout(self.DataCleanseRemoveWhitespaceTableLayout)

        self.DataCleanseRemoveWhitespaceFormLayout      =   QVBoxLayout()
               
        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM

        form_parms      =   [DCM.transform_remwhite_input_id,DCM.transform_remwhite_input_idList,DCM.transform_remwhite_input_labelList,DCM.transform_remwhite_input_typeList,DCM.transform_remwhite_input_placeholderList,DCM.transform_remwhite_input_reqList]
        comboMethods    =   [self.build_whitespace_char_list,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.remove_whitespace_value,self.remove_whitespace_return,self.remove_whitespace_help]
        cfg_parms       =   None
        form_title      =   "\n\nRemove Whitespace\n"
        form_width      =   400

        selectDicts         =   []
    
        wschars             =   {"default":"All","list":["All","Horizontal Tab","Linefeed","Formfeed","Cariage Return","Backspace","Vertical Tab"]}
        selectDicts.append(wschars)

        typesflag           =   {"default":"All","list":["Leading and Trailing","Leading Only","Trailing Only","All"]}
        selectDicts.append(typesflag)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)            

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.remove_whitespace_form     =   dfcleanser_input_form_Widget(form_parms)
        self.DataCleanseRemoveWhitespaceFormLayout.addWidget(self.remove_whitespace_form)

        from PyQt5.QtWidgets import QLabel, QLineEdit
        input_entry_label    =   QLabel()
        input_entry_label.setText("\nSelected WHitespace Chars")
        input_entry_label.setAlignment(Qt.AlignLeft)
        input_entry_label.resize(30,200)
        input_entry_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveWhitespaceFormLayout.addWidget(input_entry_label)

        self.input_entry_value    =   QLineEdit()
        self.input_entry_value.setAlignment(Qt.AlignLeft)
        self.input_entry_value.resize(30,200)
        self.input_entry_value.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveWhitespaceFormLayout.addWidget(self.input_entry_value)

        self.DataCleanseRemoveWhitespaceFormLayout.addStretch()
        
        self.DataCleanseRemoveWhitespaceLayout.addLayout(self.DataCleanseRemoveWhitespaceFormLayout)
        self.DataCleanseRemoveWhitespaceLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseRemoveWhitespaceLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][init_form] : end : "))

    # -----------------------------------------------------------------#
    # -           remove whitespace form widget Form Methods          -#
    # -----------------------------------------------------------------#

    def remove_whitespace_value(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][remove_whitespace_value]"))

        wschars         =   self.input_entry_value.text()
        leadflag        =   self.remove_whitespace_form.get_form_input_value_by_index(1)

        from dfcleanser.Qt.data_cleansing.DataCleansingControl import remove_whitespace
        opstat  =   remove_whitespace(self.dftitle,self.colname,wschars,leadflag)
 
        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Remove Whitespace Status")
            dlg.setText("Whitespace removed successfully")
            dlg.setStandardButtons(QMessageBox.OK)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

        self.parent.display_cleanse_single_column(self.dftitle,self.colname)
        
    def build_whitespace_char_list(self) :

 
        wschars         =   self.input_entry_value.text()
        currentwschar   =   self.remove_whitespace_form.get_form_input_value_by_index(0)
        leadflag        =   self.remove_whitespace_form.get_form_input_value_by_index(1)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][build_whitespace_char_list]",wschars,currentwschar,leadflag))
 
    def remove_whitespace_return(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][remove_whitespace_return]"))
        
        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

    def remove_whitespace_help(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][remove_whitespace_value]"))

        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

# -----------------------------------------------------------------#
# -                     fillna form widget                        -#
# -----------------------------------------------------------------#

class DataCleansing_Fillna_Form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget][reload_data]",dftitle,colname))
        
        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table.reload_data(self.dftitle,self.colname) #   =   DataCleansingSingleColumnTable(cparms)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        fillna_callbaks         =   [self.num_fillna_value,self.num_fillna_return,self.num_fillna_help]                
        self.fillna_form_parms  =   init_fill_na_input_form(self.df,self.colname,fillna_callbaks) 
        self.fillna_form        =   dfcleanser_input_form_Widget(self.fillna_form_parms)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel 
        self.DataCleanseFillnaLayout          =   QHBoxLayout()

        self.DataCleanseFillnaTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseFillnaTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseFillnaTableLayout.addWidget(self.stats_table)
        self.DataCleanseFillnaTableLayout.addStretch()
        self.DataCleanseFillnaLayout.addLayout(self.DataCleanseFillnaTableLayout)

        self.DataCleanseFillnaFormLayout      =   QVBoxLayout()
               
        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        fillna_callbaks         =   [self.num_fillna_value,self.num_fillna_return,self.num_fillna_help]                
        self.fillna_form_parms  =   init_fill_na_input_form(df,self.colname,fillna_callbaks) 
        self.fillna_form        =   dfcleanser_input_form_Widget(self.fillna_form_parms)

        self.DataCleanseFillnaFormLayout.addWidget(self.fillna_form)
        self.DataCleanseFillnaFormLayout.addStretch()
        
        self.DataCleanseFillnaLayout.addLayout(self.DataCleanseFillnaFormLayout)
        self.DataCleanseFillnaLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseFillnaLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget][init_form] : end : "))


    def num_fillna_value(self) :

        fillna_value(self.parent,self.fillna_form,self.dftitle,self.colname)

    def num_fillna_return(self) :

       fillna_return(self.parent,self.dftitle,self.colname) 

    def num_fillna_help(self) :

        fillna_help()

# -----------------------------------------------------------------#
# -            non numeric fillna form widget                     -#
# -----------------------------------------------------------------#

class DataCleansing_Non_Numeic_Fillna_Form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname
        
        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        fillna_callbaks         =   [self.nn_fillna_value,self.nn_fillna_return,self.nn_fillna_help]                
        self.fillna_form_parms  =   init_fill_na_input_form(self.df,self.colname,fillna_callbaks) 
        self.fillna_form        =   dfcleanser_input_form_Widget(self.fillna_form_parms)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel 
        self.DataCleanseFillnaLayout          =   QHBoxLayout()

        self.DataCleanseFillnaTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseFillnaTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseFillnaTableLayout.addWidget(self.stats_table)
        self.DataCleanseFillnaTableLayout.addStretch()
        self.DataCleanseFillnaLayout.addLayout(self.DataCleanseFillnaTableLayout)

        self.DataCleanseFillnaFormLayout      =   QVBoxLayout()
               
        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        fillna_callbaks         =   [self.nn_fillna_value,self.nn_fillna_return,self.nn_fillna_help]                
        self.fillna_form_parms  =   init_fill_na_input_form(df,self.colname,fillna_callbaks) 
        self.fillna_form        =   dfcleanser_input_form_Widget(self.fillna_form_parms)

        self.DataCleanseFillnaFormLayout.addWidget(self.fillna_form)
        self.DataCleanseFillnaFormLayout.addStretch()
        
        self.DataCleanseFillnaLayout.addLayout(self.DataCleanseFillnaFormLayout)
        self.DataCleanseFillnaLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseFillnaLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Fillna_Form_Widget][init_form] : end : "))

    def nn_fillna_value(self) :

        fillna_value(self.parent,self.fillna_form,self.dftitle,self.colname)

    def nn_fillna_return(self) :

       fillna_return(self.parent,self.dftitle,self.colname) 

    def nn_fillna_help(self) :

        fillna_help()


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Cleanse Column Widgets end                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                fillna form widget Form Methods                -#
# -----------------------------------------------------------------#

def fillna_value(parent,fillna_form,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[fillna_value]"))

    from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
    df  =   get_dfc_dataframe_df(dftitle)

    from dfcleanser.common.common_utils import is_numeric_col
    if(is_numeric_col(df,colname)) :

        fillna_value    =   fillna_form.get_form_input_value_by_index(0)
        fillna_method   =   fillna_form.get_form_input_value_by_index(1)

    else :

        fillna_value    =   fillna_form.get_form_input_value_by_index(0)
        fillna_method   =   None

    from dfcleanser.Qt.data_cleansing.DataCleansingControl import fill_nan_values

    fillparms   =   [dftitle,colname,fillna_value,fillna_method]
    opstat      =   fill_nan_values(fillparms)
 
    if(opstat.get_status()) :

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox(parent)
        dlg.setWindowTitle("Fillna Status")
        dlg.setText("Nan Values for " + colname + "Changed successfully")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setStyleSheet("QLabel{min-width: 300px;}")
        button = dlg.exec()

        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.issue_notice(dftitle)


    parent.display_cleanse_single_column(dftitle,colname)
        
def fillna_return(parent,dftitle,colname) :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[fillna_return]"))
        
    parent.display_cleanse_single_column(dftitle,colname)

def fillna_help() :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
        add_debug_to_log("DataCleansingWidgets",print_to_string("[fillna_help]"))

    from dfcleanser.common.common_utils import display_url
    from dfcleanser.common.help_utils import CLEANSE_FILLNA_COLUMN_ID
    display_url(CLEANSE_FILLNA_COLUMN_ID)

        
def init_fill_na_input_form(df,colname,callbacks) :
        
    import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM

    from dfcleanser.common.common_utils import is_numeric_col
    if(is_numeric_col(df,colname)) :

        form_parms      =   [DCM.col_fillna_input_id,DCM.col_fillna_input_idList,DCM.col_fillna_input_labelList,DCM.col_fillna_input_typeList,DCM.col_fillna_input_placeholderList,DCM.col_fillna_input_reqList]
        comboMethods    =   [None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [callbacks[0],callbacks[1],callbacks[2]]
        cfg_parms       =   None
        form_title      =   "\n\nFill Nans\n"
        form_width      =   400

        selectDicts         =   []
    
        fillnas         =   {"default" : "None - use fillna_value", "list" : ["None - use fillna_value","mean","median","min","max"]}
        selectDicts.append(fillnas)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)  

    else :

        form_parms      =   [DCM.nn_col_fillna_input_id,DCM.nn_col_fillna_input_idList,DCM.nn_col_fillna_input_labelList,DCM.nn_col_fillna_input_typeList,DCM.nn_col_fillna_input_placeholderList,DCM.nn_col_fillna_input_reqList]
        comboMethods    =   None 
        comboList       =   None
        file_methods    =   None
        button_methods  =   [callbacks[0],callbacks[1],callbacks[2]]
        cfg_parms       =   None
        form_title      =   "\n\nFill Nans\n"
        form_width      =   400

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)  

    return(form_parms)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Categorical Column Widgets                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -               Add New Category form widget                    -#
# -----------------------------------------------------------------#

class DataCleansing_Add_Category_Form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Add_Category_Form_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Add_Category_Form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        self.init_form()

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Add_Category_Form_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel 
        self.DataCleanseAddCategoryLayout          =   QHBoxLayout()

        self.DataCleanseAddCategoryTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseAddCategoryTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseAddCategoryTableLayout.addWidget(self.stats_table)
        self.DataCleanseAddCategoryTableLayout.addStretch()
        self.DataCleanseAddCategoryLayout.addLayout(self.DataCleanseAddCategoryTableLayout)

        self.DataCleanseAddCategoryFormLayout      =   QVBoxLayout()
               
        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM

        from dfcleanser.common.cfg import get_dfc_dataframe_df, set_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)


        form_parms      =   [DCM.add_category_input_id,DCM.add_category_input_idList,DCM.add_category_input_labelList,DCM.add_category_input_typeList,DCM.add_category_input_placeholderList,DCM.add_category_input_reqList]
        comboMethods    =   None 
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.add_new_category,self.add_new_category_return,self.add_new_category_help]
        cfg_parms       =   None
        form_title      =   "\n\nAdd Category\n"
        form_width      =   400

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)  

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.add_category_form     =   dfcleanser_input_form_Widget(form_parms)
        self.DataCleanseAddCategoryFormLayout.addWidget(self.add_category_form)
        self.DataCleanseAddCategoryFormLayout.addStretch()
        
        self.DataCleanseAddCategoryLayout.addLayout(self.DataCleanseAddCategoryFormLayout)
        self.DataCleanseAddCategoryLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseAddCategoryLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Add_Category_Form_Widget][init_form] : end : "))

    # -----------------------------------------------------------------#
    # -           radd new category form widget Form Methods          -#
    # -----------------------------------------------------------------#

    def add_new_category(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Add_Category_Form_Widget][add_new_category]"))

        newcat  =  self.add_category_form.get_form_input_value_by_index(0) 
        from dfcleanser.Qt.data_cleansing.DataCleansingControl import add_category

        opstat  =   add_category(self.dftitle,self.colname,newcat)
  
        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Add Category Status")
            dlg.setText("Category added successfully")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)


        self.parent.display_cleanse_single_column(self.dftitle,self.colname)
        
    def add_new_category_return(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][fillna_return]"))
        
        self.parent.display_cleanse_single_column(self.dftitle,self.colname)
    
    def add_new_category_help(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Whitespace_Form_Widget][fillna_return]"))
        
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_CAT_COL_ADD_ID
        display_url(CLEANSE_CAT_COL_ADD_ID)

# -----------------------------------------------------------------#
# -                Remove Category form widget                    -#
# -----------------------------------------------------------------#

class DataCleansing_Remove_Categories_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget]"))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)

        self.get_category_list(self.dftitle,self.colname)

    def get_category_list(self,dftitle,colname) :

        from PyQt5.QtWidgets import  QListWidget, QListWidgetItem, QAbstractItemView
        cats_to_reorder_List     =   QListWidget()
        cats_to_reorder_List.setStyleSheet("font-size: 11px; font-weight: normal; font-family: Tahoma; ")

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df     =   get_dfc_dataframe_df(dftitle)

        import pandas as pd
        CI          =   pd.CategoricalIndex(self.df[colname])
        cats        =   CI.categories.tolist()

        for i in range(len(cats)) :
            QListWidgetItem(str(cats[i]),cats_to_reorder_List)

        return(cats_to_reorder_List)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton 
        self.DataCleanseRemoveCategoryLayout          =   QHBoxLayout()

        self.DataCleanseRemoveCategoryTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveCategoryTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseRemoveCategoryTableLayout.addWidget(self.stats_table)
        self.DataCleanseRemoveCategoryTableLayout.addStretch()
        self.DataCleanseRemoveCategoryLayout.addLayout(self.DataCleanseRemoveCategoryTableLayout)

        self.DataCleanseRemoveCategoryFormLayout      =   QVBoxLayout()
               
        title_label    =   QLabel()
        title_label.setText("\nRemove Category\n")
        title_label.setAlignment(Qt.AlignLeft)
        title_label.resize(30,200)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveCategoryFormLayout.addWidget(title_label)

        self.cats_to_drop_List   =   self.get_category_list(self.dftitle,self.colname)
        self.DataCleanseRemoveCategoryFormLayout.addWidget(self.cats_to_drop_List)

        note_label    =   QLabel()
        note_label.setText("\nSelect Category To Remove\n")
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(30,200)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial;")
        self.DataCleanseRemoveCategoryFormLayout.addWidget(note_label)

        cmdbutonsLayout  =   QHBoxLayout()

        remove_cat_button        =   QPushButton()     
        remove_cat_button.setText("Remove\nCategory(s)")
        remove_cat_button.setFixedSize(120,90)
        remove_cat_button.setToolTip("Remove Category")
        remove_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        remove_cat_button.clicked.connect(self.remove_categories) 
        cmdbutonsLayout.addWidget(remove_cat_button)

        return_cat_button        =   QPushButton()     
        return_cat_button.setText("Return")
        return_cat_button.setFixedSize(120,90)
        return_cat_button.setToolTip("Return")
        return_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_cat_button.clicked.connect(self.return_remove_categories) 
        cmdbutonsLayout.addWidget(return_cat_button)
        
        help_cat_button        =   QPushButton()     
        help_cat_button.setText("Help")
        help_cat_button.setFixedSize(120,90)
        help_cat_button.setToolTip("Return")
        help_cat_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_cat_button.clicked.connect(self.help_remove_categories) 
        cmdbutonsLayout.addWidget(help_cat_button)

        cmdbutonsLayout.setAlignment(Qt.AlignCenter)
        self.DataCleanseRemoveCategoryFormLayout.addLayout(cmdbutonsLayout)
        self.DataCleanseRemoveCategoryFormLayout.addStretch()
        
        self.DataCleanseRemoveCategoryLayout.addLayout(self.DataCleanseRemoveCategoryFormLayout)
        self.DataCleanseRemoveCategoryLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseRemoveCategoryLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget][init_form] : end : "))

    # -----------------------------------------------------------------#
    # -            remove category form widget Form Methods           -#
    # -----------------------------------------------------------------#

    def remove_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget][remove_categories]"))

        categoryList    =   []
        opstat          =   self.remove_categories(self.dftitle,self.colname,categoryList)
 
        if(opstat.get_status()) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fillna Status")
            dlg.setText("Nan Values Changed successfully")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 300px;}")
            button = dlg.exec()

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)


        self.parent.display_cleanse_single_column(self.dftitle,self.colname)
        
    def return_remove_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget][return_categories]"))
        
        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

    def help_remove_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Remove_Categories_Widget][help_categories]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_CAT_COL_REMOVE_ID
        display_url(CLEANSE_CAT_COL_REMOVE_ID)



# -----------------------------------------------------------------#
# -           Transform reorder Categories Form Widget            -#
# -----------------------------------------------------------------#

class DataCleansing_Reorder_Categories_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][init] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.get_category_list(self.dftitle,self.colname)

    def get_category_list(self,dftitle,colname) :

        from PyQt5.QtWidgets import  QListWidget, QListWidgetItem, QAbstractItemView
        cats_to_reorder_List     =   QListWidget()
        cats_to_reorder_List.setStyleSheet("font-size: 11px; font-weight: normal; font-family: Tahoma; ")
        cats_to_reorder_List.setDragDropMode(QAbstractItemView.InternalMove)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df     =   get_dfc_dataframe_df(dftitle)

        import pandas as pd
        CI          =   pd.CategoricalIndex(self.df[colname])
        cats        =   CI.categories.tolist()

        for i in range(len(cats)) :
            QListWidgetItem(str(cats[i]),cats_to_reorder_List)

        return(cats_to_reorder_List)


    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton 
        self.DataCleanseReorderCategoryLayout          =   QHBoxLayout()

        self.DataCleanseReorderCategoryTableLayout     =   QVBoxLayout()

        blank_label    =   QLabel()
        blank_label.setText("\n\n\n\n")
        blank_label.setAlignment(Qt.AlignLeft)
        blank_label.resize(30,200)
        blank_label.setStyleSheet("font-size: 11px; font-weight: bold; font-family: Arial;")
        self.DataCleanseReorderCategoryTableLayout.addWidget(blank_label)

        cparms  =   [self.dftitle,self.colname]
        self.stats_table     =   DataCleansingSingleColumnTable(cparms)

        self.DataCleanseReorderCategoryTableLayout.addWidget(self.stats_table)
        self.DataCleanseReorderCategoryTableLayout.addStretch()
        self.DataCleanseReorderCategoryLayout.addLayout(self.DataCleanseReorderCategoryTableLayout)

        self.DataCleanseReorderCategoryFormLayout      =   QVBoxLayout()
               
        title_label    =   QLabel()
        title_label.setText("\nReorder Category\n")
        title_label.setAlignment(Qt.AlignLeft)
        title_label.resize(30,200)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial;")
        self.DataCleanseReorderCategoryFormLayout.addWidget(title_label)

        self.cats_to_reorder_List   =   self.get_category_list(self.dftitle,self.colname)
        self.DataCleanseReorderCategoryFormLayout.addWidget(self.cats_to_reorder_List)

        note_label    =   QLabel()
        note_label.setText("\nDrag and Drop Categories to choose order.\n")
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(30,200)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial;")
        self.DataCleanseReorderCategoryFormLayout.addWidget(note_label)

        from PyQt5.QtWidgets import QHBoxLayout, QPushButton
        cmdbuttonsLayout  =   QHBoxLayout()
         
        reorder_button        =   QPushButton()     
        reorder_button.setText("Reorder\nCategories")
        reorder_button.setFixedSize(200,70)
        reorder_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        reorder_button.clicked.connect(self.reorder_categories) 

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_reorder_categories) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(200,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_for_reorder_categories) 
         
        cmdbuttonsLayout.addWidget(reorder_button)
        cmdbuttonsLayout.addWidget(return_button)
        cmdbuttonsLayout.addWidget(help_button)
        cmdbuttonsLayout.setAlignment(Qt.AlignHCenter)

        self.DataCleanseReorderCategoryFormLayout.addLayout(cmdbuttonsLayout)
        self.DataCleanseReorderCategoryFormLayout.addStretch()
        
        self.DataCleanseReorderCategoryLayout.addLayout(self.DataCleanseReorderCategoryFormLayout)
        self.DataCleanseReorderCategoryLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DataCleanseReorderCategoryLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][init_form] end"))


    def reorder_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][reorder_categories]"))

        try :

            cat_items   =  []
            for i in range(self.cats_to_reorder_List.count()) :
                cat_items.append(self.cats_to_reorder_List.item(i))

            import pandas as pd
            CI          =   pd.CategoricalIndex(self.df[self.colname])
            CI.reorder_categories(cat_items)

            title       =   "dfcleanser status"       
            status_msg  =   "Categories Reordered Sucesfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)
        
        except Exception as e :

            title       =   "dfcleanser exception"       
            status_msg  =   "[Reorder Categories] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

        return()

    def return_from_reorder_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][return_from_reorder_categories]"))

        self.parent.display_cleanse_single_column(self.dftitle,self.colname)

    def help_for_reorder_categories(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_COLUMN")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_Reorder_Categories_Widget][help_for_reorder_categories]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_CAT_COL_REORDER_ID
        display_url(CLEANSE_CAT_COL_REORDER_ID)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Categorical Column Widgets end                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    Cleanse Rows Widgets                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                  display cleanse rows options                 -#
# -----------------------------------------------------------------#
class DataCleansing_cleanse_rows_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle

        self.init_form()

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][init_form]"))

        self.init_command_bar()

    def init_command_bar(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][init_command_bar]"))

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.excel_button       =   QPushButton()   
        self.filter_button      =   QPushButton()    
        self.drop_button        =   QPushButton()   
        self.return_button      =   QPushButton()   
        self.help_button        =   QPushButton()   

        button_bar1_button_list     =   [self.excel_button,self.filter_button,self.drop_button,self.return_button,self.help_button] 
        button_bar1_text_list       =   ["Cleanse df\nIn Excel","Filter\ndataframe","Drop\nDuplicate Rows","Return","Help"]
        button_bar1_size_list       =   [200,70]
        button_bar1_tool_tip_list   =   ["Cleanse In Excel","Filter Dataframe","Drop Duplicates","Return","Help"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.cleanse_rows_in_excel,self.filter_df_rows,self.drop_dup_df_rows,self.return_from_cleanse_rows,self.help_for_cleanse_rows]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataCleansingCmdbarLayout)
        self.parent.form.DataCleansingCmdbarLayout.addLayout(cmdbarLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][init_command_bar] end"))

    # -----------------------------------------------------------------#
    # -         DataCleansing_cleanse_rows_Widget methods             -#
    # -----------------------------------------------------------------#

    def cleanse_rows_in_excel(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][cleanse_rows_in_excel]"))

        from dfcleanser.common.cfg import get_dfc_dataframe_df, get_dfcleanser_location 
        from dfcleanser.common.common_utils import alert_user 
   
        df              =   get_dfc_dataframe_df(self.dftitle)

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


    def filter_df_rows(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][filter_df_rows]"))

        self.parent.display_cleanse_rows_filter_df()

    def drop_dup_df_rows(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][drop_dup_df_rows]"))

        self.parent.display_drop_duplicates(self.dftitle)

    def return_from_cleanse_rows(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][return_from_cleanse_column]"))

        self.parent.init_stacked_index()

    def help_for_cleanse_rows(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget][help_for_cleanse_column]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_ROW_ID
        display_url(CLEANSE_ROW_ID)


# -----------------------------------------------------------------#
# -                  display drop duplicate rows                  -#
# -----------------------------------------------------------------#
class DataCleansing_drop_duplicate_rows_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df  =   get_dfc_dataframe_df(self.dftitle)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_cleanse_rows_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle

        #self.init_form()

    def init_form(self):  

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingdfFiltersColumnWidget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.dropdupsLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.dffilter_title_label   =   QLabel()
        self.dffilter_title_label.setText("\ndf : '"+self.dftitle+"' :  Number Rows : "+str(len(self.df))+"\n")
        self.dffilter_title_label.setAlignment(Qt.AlignCenter)
        self.dffilter_title_label.resize(480,50)
        self.dffilter_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.dropdupsLayout.addWidget(self.dffilter_title_label)

        from dfcleanser.Qt.data_cleansing.DataCleansingFilterdfWidgets import DataCleansingdfFiltersColumnTable
        parms              =    [self.df,self.add_column_to_subset]
        self.colsStats     =    DataCleansingdfFiltersColumnTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)
        self.colsStats.setFixedSize(600,new_height)

        self.dropdupsLayout.addWidget(self.colsStats)

        import dfcleanser.Qt.data_cleansing.DataCleansingModel as DCM
        from dfcleanser.sw_utilities.dfc_qt_model import NUMERIC_COLUMN, NON_NUMERIC_COLUMN, CATEGORICAL_COLUMN

        form_parms      =   [DCM.df_drop_dups_transform_input_id,DCM.df_drop_dups_transform_input_idList,DCM.df_drop_dups_transform_input_labelList,
                             DCM.df_drop_dups_transform_input_typeList,DCM.df_drop_dups_transform_input_placeholderList,DCM.df_drop_dups_transform_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.drop_duplicates,self.return_from_drop_duplicates,self.help_for_drop_duplicates]
        cfg_parms       =   None
        form_title      =   "\nDrop Duplicate Rows\n"
        form_width      =   650
        
        selectDicts         =   []
    
        colsuse             =   {"default":"All","list":["All","Use columns selected for duplicate match","Use columns not selected for duplicate match"]}
        selectDicts.append(colsuse)

        keepflag            =   {"default":"False","list":["first","last","False"]}
        selectDicts.append(keepflag)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)            

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.drop_dups_form     =   dfcleanser_input_form_Widget(form_parms)
        
        self.drop_dups_form.setMaximumSize(form_width,550)
        self.drop_dups_form.setMinimumSize(form_width,550)


        self.dropdupsLayout.addWidget(self.drop_dups_form)
        

        self.dropdupsLayout.addStretch()
        self.dropdupsLayout.setAlignment(QtCore.Qt.AlignCenter) 

        self.setLayout(self.dropdupsLayout)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingdfFiltersColumnWidget][init_form] end"))


    # -----------------------------------------------------------------#
    # -       DataCleansing_drop_duplicate_rows_Widget methods        -#
    # -----------------------------------------------------------------#

    def add_column_to_subset(self) :

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget][add_column_to_subset] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :    
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget][add_column_to_subset] : colname [",cell,"]"))

        subset_list     =    self.drop_dups_form.get_form_input_value_by_index(0)

        if(len(subset_list) == 0) :
            
            subset_list     =   "[" + cell + "]"
        
        else :

            if(subset_list.find(cell) == -1) :
                subset_list     =   subset_list.replace("]",","+ cell + "]")

        self.drop_dups_form.set_form_input_value_by_index(0,str(subset_list))

    def drop_duplicates(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget][drop_duplicates]"))

        subset_list         =   self.drop_dups_form.get_form_input_value_by_index(0)
        duplicate_match     =   self.drop_dups_form.get_form_input_value_by_index(1)
        if(duplicate_match == "Use columns selected for duplicate match") :

            subset  =   subset_list.replace("[","")
            subset  =   subset.replace("]","")
            subset  =   subset.split(",")

        elif(duplicate_match == "Use columns not selected for duplicate match") :

            subset  =   subset_list.replace("[","")
            subset  =   subset.replace("]","")
            subset  =   subset.split(",")

            inverse_subset  =   []

            all_columns     =   self.df.columns.tolist()

            for i in range(len(all_columns)) :
                if(not (all_columns[i] in subset)) :
                    inverse_subset.append(all_columns[i])

            subset  =   inverse_subset

        else :

            subset  =   None
        
        keep_duplicates     =   self.drop_dups_form.get_form_input_value_by_index(2)
        if(keep_duplicates == "False") :
            keep_duplicates     =   False
        

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansing_drop_duplicate_rows_Widget][drop_duplicates]",subset_list,duplicate_match,keep_duplicates))

        try :
        
	    if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            	add_debug_to_log("DataCleansingWidgets",print_to_string("subset",subset,type(subset)))

            self.df.drop_duplicates(subset,keep=keep_duplicates,inplace=True)
            #self.filter_working_df      =    
            #self.filter_working_df.drop(cell, axis=1, inplace=True)

            title       =   "dfcleanser mesage"       
            status_msg  =   "[df filter] column duplicates dropped successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            self.dffilter_title_label.setText("\ndf : '"+self.dftitle+"' :  Number Rows : "+str(len(self.df))+"\n")

        except Exception as e:                   
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[filter df drop column] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

    def return_from_drop_duplicates(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingdfFiltersColumnWidget][return_from_drop_duplicates]"))

        from dfcleanser.Qt.data_cleansing.DataCleansing import DFS_SELECT
        self.parent.init_stacked_index()

    def help_for_drop_duplicates(self) :

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSE_ROWS")) :
            add_debug_to_log("DataCleansingWidgets",print_to_string("[DataCleansingdfFiltersColumnWidget][help_for_drop_duplicates]"))
   
        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import CLEANSE_DROP_DUPS_ID
        display_url(CLEANSE_DROP_DUPS_ID)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Cleanse Rows Widgets end                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


