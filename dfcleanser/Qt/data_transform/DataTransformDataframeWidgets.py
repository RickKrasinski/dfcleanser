"""
# DataTransformDataframeWidgets
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

import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM


DEBUG_TRANSFORM_DATAFRAME         =   True
DEBUG_TRANSFORM_COLUMN_DETAILS    =   False
DEBUG_TRANSFORM_DATETIME          =   True

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
# -                 Transform Dataframe Widgets                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataTransform_transform_dataframe_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_dataframe_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        from dfcleanser.common.cfg import DataTransform_add_df_signal
        DataTransform_add_df_signal.connectSignal(self.add_new_df)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_Widget] end")

    def reload_banner(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][reload_data] ")

        self.init_command_bar()
        
        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dataframes     =   get_dfc_dataframes_titles_list()

        if(dataframes  is None) :
            dataframes      =   []
            dataframes.append("no dfs defined")

        for i in range(len(dataframes)) :
            index = self.df_select.findText(dataframes[i])
            if(index <0) :
                self.df_select.addItem(dataframes[i])

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransformGui][add_new_df]  df_title",df_title)

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("self.df_select",type(self.df_select),self.df_select.count())

        #self.init_stacked_index()


    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][init_form]")

        self.init_command_bar()

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_transform")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addLayout(self.dfc_dfs_layout)
        self.transform_col_Layout.addStretch()

        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][init_form] end")

    def init_command_bar(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][init_command_bar]")

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.names_row_button       =   QPushButton()   
        self.df_index_button        =   QPushButton()    
        self.sort_df_button         =   QPushButton()   
        self.return_button          =   QPushButton()   

        button_bar1_button_list     =   [self.names_row_button,self.df_index_button,self.sort_df_button,self.return_button ] 
        button_bar1_text_list       =   ["Column\nNames Row","dataframe index","Sort df\n byColumn","Return"]
        button_bar1_size_list       =   [250,70]
        button_bar1_tool_tip_list   =   ["Column Names Row","dataframe index","Sort df","Return"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.transform_names_row,self.transform_df_index,self.transform_sort_df,self.return_from_transform_dataframe]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataTransformCmdbarLayout)
        self.parent.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][init_command_bar] end")


    # -----------------------------------------------------------------#
    # -              Transform dataframe Widget methods               -#
    # -----------------------------------------------------------------#

    def transform_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][transform_names_row]")

        self.parent.display_transform_dataframe_column_names()

    def transform_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_columns_Widget][transform_df_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_INDEX_MAIN)

    def transform_sort_df(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_Widget][transform_sort_df]")

        self.parent.display_transform_sort_df()

    def return_from_transform_dataframe(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][return_from_transform_dataframe]")

        self.parent.init_stacked_index()


# -----------------------------------------------------------------#
# -        Transfoprm Dataframe col names Main Command            -#
# -----------------------------------------------------------------#

class DataTransform_transform_dataframe_col_names_row_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_dataframe_col_names_row_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        from dfcleanser.common.cfg import DataTransform_add_df_signal
        DataTransform_add_df_signal.connectSignal(self.add_new_df)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_col_names_row_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

        self.init_command_bar()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dataframes     =   get_dfc_dataframes_titles_list()

        if(dataframes  is None) :
            dataframes      =   []
            dataframes.append("no dfs defined")

        for i in range(len(dataframes)) :
            self.df_select.addItem(dataframes[i])

    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransformGui][add_new_df]  df_title",df_title)

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("self.df_select",type(self.df_select),self.df_select.count())

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget][init_form]")

        self.init_command_bar()

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_transform")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addLayout(self.dfc_dfs_layout)
        self.transform_col_Layout.addStretch()

        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget][init_form] end")


    def init_command_bar(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget][init_command_bar]")

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.show_names_button       =   QPushButton()   
        self.save_names_button       =   QPushButton()    
        self.add_names_button        =   QPushButton()  
        self.drop_names_button       =   QPushButton()    
        self.return_button           =   QPushButton()   

        button_bar1_button_list     =   [self.show_names_button,self.save_names_button,self.add_names_button,self.drop_names_button,self.return_button ] 
        button_bar1_text_list       =   ["Show\nColumn\nNames Row","Save\nColumn\nNames Row","Add a\nColumn\nNames Row","Drop\nColumn\nNames Row","Return"]
        button_bar1_size_list       =   [196,70]
        button_bar1_tool_tip_list   =   ["Show Column Names Row","Save Column Names Row","Add Column Names Row","Drop Column Names Row","Return"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.show_col_names_row,self.save_col_names_row,self.add_col_names_row,self.drop_col_names_row,self.return_from_transform_col_names_row]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataTransformCmdbarLayout)
        self.parent.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_col_names_row_Widget][init_command_bar] end")

    def show_col_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][show_col_names_row]")
        
        self.parent.display_transform_col_names_row()

    def save_col_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_columns_Widget][save_col_names_row]")
        
        self.parent.display_transform_save_col_names_row()

    def add_col_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][add_col_names_row]")

        self.parent.display_transform_add_col_names_row() 

    def drop_col_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][drop_col_names_row]")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df      =   get_dfc_dataframe_df(self.dftitle)

        if(df is None) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[drop_col_names_row] invalid df '" + dftitle + "' selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            opstat.set_status(False)

        else :

            collist         =   df.columns.tolist()
            col_name_found  =   False
        
            for i in range(len(collist)) :
                if(not (collist[i] == str(i))) :
                    col_name_found  =   True
                    break

            if(not col_name_found) :

                title       =   "dfcleanser exception"       
                status_msg  =   "[drop_col_names_row] df has no column names to drop "
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                opstat.set_status(False)

            else :

                from dfcleanser.Qt.data_transform.DataTransformDataframeControl import drop_column_names_row
                opstat  =   drop_column_names_row(self.dftitle)

        if(opstat.get_status()) :

            title       =   "dfcleanser exception"       
            status_msg  =   "[drop_col_names_row] df column names dropped successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

    def return_from_transform_col_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_Widget][return_from_transform_col_names_row]")

        self.parent.display_transform_dataframes()


# -----------------------------------------------------------------# 
# -      Data Transform Dataframes Show Column Names Row          -#
# -----------------------------------------------------------------#

class DataTransformColumnsListModel(QtCore.QAbstractTableModel):
    def __init__(self, coldata, colheaders):

        super(DataTransformColumnsListModel,self).__init__()
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
            return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            
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

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)

class DataTransformColumnsListTable(QtWidgets.QTableView):

    def __init__(self,  colparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.dftitle            =   colparms[0]

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransformColumnsListTable] : init")

        self.init_tableview()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransformColumnsListTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,dftitle):
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransformColumnsListTable][reload_data] : dftile : colname : ",dftitle)

        self.dftitle    =   dftitle
        
        statsdata       =   self.load_columns_info_data()
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

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransformColumnsListTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statsdata     =   self.load_columns_info_data()
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
           print("  [DataTransformColumnsListTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = DataTransformColumnsListModel(statsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_TRANSFORM_DATAFRAME) :
           print("  [DataTransformColumnsListTable][init_tableview] : model loaded")

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

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransformColumnsListTable][load_columns_info_data]")

        data    =   []

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df      =   get_dfc_dataframe_df(self.dftitle)

        colnames     =   df.columns.tolist()

        for i in range(len(colnames)) :
                
            data_row    =   []

            data_row.append(colnames[i])
            data.append(data_row)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransformColumnsListTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["Column Name"]
        self.column_widths      =   [560]

        return(data)


class DataTransform_transform_column_names_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_column_names_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_column_names_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_column_names_Widget] end")

    def reload_data(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_column_names_Widget][reload_data] ")

        self.colslist.reload_data(self.dftitle)

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_column_names_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel
        cols_title_label   =   QLabel()
        cols_title_label.setText("\nColumn Names Row\n")
        cols_title_label.setAlignment(Qt.AlignCenter)
        #cols_title_label.resize(480,50)
        cols_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        parms           =   [self.dftitle]
        self.colslist   =   DataTransformColumnsListTable(parms)
        self.colslist.setFixedSize(360,350)

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addWidget(cols_title_label,Qt.AlignCenter)
        self.transform_col_Layout.addWidget(self.colslist,Qt.AlignCenter)
        self.transform_col_Layout.addStretch()
        self.transform_col_Layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_column_names_Widget][init_form] end")

# -----------------------------------------------------------------# 
# -      Data Transform Dataframes Save Column Names Row          -#
# -----------------------------------------------------------------#

class DataTransform_transform_dataframe_save_col_names_row_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_dataframe_save_col_names_row_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_save_col_names_row_Widget] end")

    def reload_data(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][reload_data] ")

        self.init_command_bar()

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][init_form]")

        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_save_row_transform_input_id,DTDM.df_save_row_transform_input_idList,DTDM.df_save_row_transform_input_labelList,
                             DTDM.df_save_row_transform_input_typeList,DTDM.df_save_row_transform_input_placeholderList,DTDM.df_save_row_transform_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   [self.select_json_file]
        button_methods  =   [self.save_column_nanes_row,self.return_from_save_column_names_row,self.help_for_save_column_names_row]
        cfg_parms       =   None
        form_title      =   "\n\nSave Column Names Row\n"
        form_width      =   550

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.save_row_form     =   dfcleanser_input_form_Widget(form_parms)


        fname       =   self.dftitle

        from dfcleanser.common.cfg import DataframeCleansercfg
        import os
        nbdir       =   DataframeCleansercfg.get_notebookpath()
        nbname      =   DataframeCleansercfg.get_notebookname()
        
        file_path   =   os.path.join(nbdir,nbname + "_files")
        filename    =   os.path.join(file_path,fname + "_column_names.json")

        label_text  =   "\n                   If column_names_file_name is blank the following default value will be used : \n                   " + filename 

        from PyQt5.QtWidgets import QLabel
        self.save_row_note_label   =   QLabel()
        self.save_row_note_label.setText(label_text)
        self.save_row_note_label.setAlignment(Qt.AlignLeft)
        self.save_row_note_label.resize(480,90)
        self.save_row_note_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_save_row_Layout     =   QVBoxLayout()
        self.transform_save_row_Layout.addWidget(self.save_row_form)
        self.transform_save_row_Layout.addWidget(self.save_row_note_label)
        self.transform_save_row_Layout.addStretch()

        self.setLayout(self.transform_save_row_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][init_form] end")


    def select_json_file(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][select_json_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.save_row_form.set_form_input_value_by_index(1,fname[0])        

    def save_column_nanes_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][save_column_nanes_row]")

        filename    =   self.save_row_form.get_form_input_value_by_index(0)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import save_df_column_names_row
        save_df_column_names_row(self.dftitle,filename)    
        
        #self.parent.display_transform_col_names_row()

    def return_from_save_column_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][return_from_save_column_names_row]")

        self.parent.display_transform_dataframes()

    def help_for_save_column_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_save_col_names_row_Widget][help_for_save_column_names_row]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_SAVE_COL_NAME_ID
        display_url(TRANSFORM_DF_SAVE_COL_NAME_ID)


class DataTransform_transform_dataframe_add_col_names_row_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_dataframe_add_col_names_row_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_add_col_names_row_Widget] end")

    def reload_data(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][reload_data] ")

        self.init_command_bar()

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][init_form]")

        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_add_row_transform_input_id,DTDM.df_add_row_transform_input_idList,DTDM.df_add_row_transform_input_labelList,
                             DTDM.df_add_row_transform_input_typeList,DTDM.df_add_row_transform_input_placeholderList,DTDM.df_add_row_transform_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   [self.select_json_file]
        button_methods  =   [self.add_column_names_row,self.return_from_add_column_names_row,self.help_for_add_column_names_row]
        cfg_parms       =   None
        form_title      =   "\nAdd Column Names Row\n"
        form_width      =   550

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.add_row_form     =   dfcleanser_input_form_Widget(form_parms)

        fname       =   self.dftitle

        from dfcleanser.common.cfg import DataframeCleansercfg
        import os
        nbdir       =   DataframeCleansercfg.get_notebookpath()
        nbname      =   DataframeCleansercfg.get_notebookname()
        
        file_path   =   os.path.join(nbdir,nbname + "_files")
        filename    =   os.path.join(file_path,fname + "_column_names.json")

        label_text  =   "\n                   If column_names_file_name is blank and column_names is blank the following default value will be used : \n                   " + filename 

        from PyQt5.QtWidgets import QLabel
        self.save_row_note_label   =   QLabel()
        self.save_row_note_label.setText(label_text)
        self.save_row_note_label.setAlignment(Qt.AlignLeft)
        self.save_row_note_label.resize(480,90)
        self.save_row_note_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")

        label1_text  =   "\n                   Enter column names as a list of single quoted name : ie .. ['col name','col name1']"

        from PyQt5.QtWidgets import QLabel
        self.save_row_note1_label   =   QLabel()
        self.save_row_note1_label.setText(label1_text)
        self.save_row_note1_label.setAlignment(Qt.AlignLeft)
        self.save_row_note1_label.resize(480,90)
        self.save_row_note1_label.setStyleSheet("font-size: 13px; font-weight: normal; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_add_row_Layout     =   QVBoxLayout()
        self.transform_add_row_Layout.addWidget(self.add_row_form)
        self.transform_add_row_Layout.addWidget(self.save_row_note_label)
        self.transform_add_row_Layout.addWidget(self.save_row_note1_label)
        self.transform_add_row_Layout.addStretch()

        self.setLayout(self.transform_add_row_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][init_form] end")

    def select_json_file(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][select_json_file]")

        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"json files (*.json)")
        self.save_row_form.set_form_input_value_by_index(1,fname[0])        

    def add_column_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][add_column_nanes_row]")
        
        self.parent.display_transform_col_names_row()

    def return_from_add_column_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][return_from_save_column_names_row]")

        self.parent.display_transform_dataframes()

    def help_for_add_column_names_row(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_add_col_names_row_Widget][help_for_save_column_names_row]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_SET_COL_NAME_ID
        display_url(TRANSFORM_DF_SET_COL_NAME_ID)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -    Transfoprm Dataframe col names rows Widgets end            -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Transfoprm Dataframe index Widgets              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataTransform_transform_dataframe_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_dataframe_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        from dfcleanser.common.cfg import DataTransform_add_df_signal
        DataTransform_add_df_signal.connectSignal(self.add_new_df)


        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_dataframe_index_Widget] end")

    def reload_data(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][reload_data] ")

        self.init_command_bar()

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dataframes     =   get_dfc_dataframes_titles_list()

        if(dataframes  is None) :
            dataframes      =   []
            dataframes.append("no dfs defined")

        for i in range(len(dataframes)) :
            index = self.df_select.findText(dataframes[i])
            if(index <0) :
                self.df_select.addItem(dataframes[i])


    # -----------------------------------------------------------------#
    # -            Add a new dataframe to the df combobox             -#
    # -----------------------------------------------------------------#
    def add_new_df(self,df_title):

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransformGui][add_new_df]  df_title",df_title)

        index = self.df_select.findText(df_title)
        if(index > -1) :
            self.df_select.removeItem(index) 
        else :
            self.df_select.addItem(df_title)   

        index = self.df_select.findText("no dfs defined")
        if(index > -1) :
            self.df_select.removeItem(index)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("self.df_select",type(self.df_select),self.df_select.count())


    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][init_form]")

        self.init_command_bar()

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_transform")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addLayout(self.dfc_dfs_layout)
        self.transform_col_Layout.addStretch()

        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][init_form] end")
        

    def init_command_bar(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][init_command_bar]")

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.show_index_button      =   QPushButton()   
        self.set_index_button       =   QPushButton()    
        self.reset_index_button     =   QPushButton()  
        self.append_index_button    =   QPushButton() 
        self.sort_index_button      =   QPushButton() 
        self.return_button          =   QPushButton()
        self.help_button            =   QPushButton()   

        button_bar1_button_list     =   [self.show_index_button,self.set_index_button,self.reset_index_button,self.append_index_button,self.sort_index_button,self.return_button,self.help_button] 
        button_bar1_text_list       =   ["Show\nIndex","Set\nIndex","Reset\nIndex","Append\nIndex","Sort\nIndex","Return","Help"]
        button_bar1_size_list       =   [142,70]
        button_bar1_tool_tip_list   =   ["Show Index","Set Index","Reset Index","Append Index","Sort Index","Return","Help"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.show_index,self.set_index,self.reset_index,self.append_index,self.sort_index,self.return_from_transform_index,self.help_for_transform_index]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataTransformCmdbarLayout)
        self.parent.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][init_command_bar] end")

    def show_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][show_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_SHOW_INDEX)

    def set_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][set_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_SET_INDEX)

    def reset_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][reset_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_RESET_INDEX)
    
    def append_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][append_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_APPEND_INDEX)
    
    def sort_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][sort_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_SORT_INDEX)

    def return_from_transform_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][return_from_transform_index]")

        self.parent.display_transform_dataframes()

    def help_for_transform_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_dataframe_index_Widget][help_for_transform_index]]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_INDEX_TASKBAR_ID
        display_url(TRANSFORM_DF_INDEX_TASKBAR_ID)


class DataTransform_transform_df_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_df_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_df_index_Widget] dftitle ; ",self.dftitle)

        self.init_form()


        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_df_index_Widget] end")

    def reload_data(self) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_df_index_Widget][reload_data] ")


    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_df_index_Widget][init_form]")

        from PyQt5.QtWidgets import QLabel
        colsindex_title_label   =   QLabel()
        colsindex_title_label.setText("\nColumn Index for df '" + self.dftitle + "'\n")
        colsindex_title_label.setAlignment(Qt.AlignCenter)
        colsindex_title_label.resize(960,50)
        colsindex_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsIndexTable
        self.IndexStats     =   DataInspectionColumnsIndexTable([self.dftitle])
        new_height          =   30 + (self.IndexStats.num_rows * DEFAULT_ROW_HEIGHT)
        self.IndexStats.setMinimumHeight(new_height)
        self.IndexStats.setMaximumHeight(new_height)

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addWidget(colsindex_title_label)
        self.transform_col_Layout.addWidget(self.IndexStats)
        self.transform_col_Layout.addStretch()
  
        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_df_index_Widget][init_form] end")

class DataTransform_transform_dataframe_set_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_set_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget] dftitle : ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_set_index_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,10,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nDouble click on column to be used as index column\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_set_index_transform_input_id,DTDM.df_set_index_transform_input_idList,DTDM.df_set_index_transform_input_labelList,
                             DTDM.df_set_index_transform_input_typeList,DTDM.df_set_index_transform_input_placeholderList,DTDM.df_set_index_transform_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.set_df_index,self.return_from_set_df_index,self.help_for_set_df_index]
        cfg_parms       =   None
        form_title      =   "Set df Index"
        form_width      =   550

        selectDicts     =   []
        
        dropsel             =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(dropsel)
        
        verifysel           =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(verifysel)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.set_index_form     =   dfcleanser_input_form_Widget(form_parms)
        
        from PyQt5.QtWidgets import QVBoxLayout
        self.set_index_Layout     =   QVBoxLayout()
        self.set_index_Layout.addWidget(self.cols_table)
        self.set_index_Layout.addWidget(note_label)
        self.set_index_Layout.addWidget(self.set_index_form)
        self.set_index_Layout.addStretch()

        self.setLayout(self.set_index_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATAFRAME) :    
            print("  [DataTransform_transform_set_index_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell

        index_columns   =   self.set_index_form.get_form_input_value_by_index(0)
        if(len(index_columns) == 0) :

            index_list  =   "[" + cell + "]"
            self.set_index_form.set_form_input_value_by_index(0,index_list)  

        else :  

            index_list  =   index_columns.replace("]",",")
            index_list  =   index_list + cell + "]"
            self.set_index_form.set_form_input_value_by_index(0,index_list)
    
    def set_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][set_df_index]")

        index_columns   =   self.set_index_form.get_form_input_value_by_index(0)
        dropflag        =   self.set_index_form.get_form_input_value_by_index(1)
        verifyflag      =   self.set_index_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import set_df_index     
        opstat  =   set_df_index(self.dftitle,index_columns,dropflag,verifyflag)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "df index set was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            self.parent.display_transform_dataframe_index()        

    def return_from_set_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][set_df_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_INDEX_MAIN)

    def help_for_set_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][set_df_index]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_SET_INDEX
        display_url(TRANSFORM_DF_SET_INDEX)


class DataTransform_transform_dataframe_reset_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_reset_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_reset_index_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_set_index_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,10,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nDouble click on column to be used as index column\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_reset_index_transform_input_id,DTDM.df_reset_index_transform_input_idList,DTDM.df_reset_index_transform_input_labelList,
                             DTDM.df_reset_index_transform_input_typeList,DTDM.df_reset_index_transform_input_placeholderList,DTDM.df_reset_index_transform_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.reset_df_index,self.return_from_reset_df_index,self.help_for_reset_df_index]
        cfg_parms       =   None
        form_title      =   "Reset df Index"
        form_width      =   550

        selectDicts     =   []

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df      =   get_dfc_dataframe_df(self.dftitle)

        index_levels    =   [" ","All"]
        index_columns   =   df.index.names
        if(len(index_columns) > 0) :
            for i in range(len(index_columns)) :
                if( not (index_columns[i] is None) ) :
                    index_levels.append(index_columns[i])
        cnames          =   {"default" : index_levels[0], "list" : index_levels, "size" : 5, "callback" : "change_reset_index_callback"}
        selectDicts.append(cnames)
        
        dropsel1        =   {"default" : "True",
                             "list" : ["True","False"]}
        selectDicts.append(dropsel1)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.reset_index_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.reset_index_Layout     =   QVBoxLayout()
        self.reset_index_Layout.addWidget(self.cols_table)
        self.reset_index_Layout.addWidget(note_label)
        self.reset_index_Layout.addWidget(self.reset_index_form)
        self.reset_index_Layout.addStretch()

        self.setLayout(self.reset_index_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][select_column_to_cleanse] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATAFRAME) :    
            print("  [DataTransform_transform_reset_index_Widget][select_column_to_cleanse] : colname [",cell,"]")

        self.colname    =   cell

        index_columns   =   self.reset_index_form.get_form_input_value_by_index(0)
        if(len(index_columns) == 0) :

            index_list  =   "[" + cell + "]"
            self.reset_index_form.set_form_input_value_by_index(0,index_list)  

        else :  

            index_list  =   index_columns.replace("]",",")
            index_list  =   index_list + cell + "]"
            self.reset_index_form.set_form_input_value_by_index(0,index_list)
    
    def reset_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][reset_df_index]")
        
        drop_columns    =   self.set_index_form.get_form_input_value_by_index(0)
        index_levels    =   self.set_index_form.get_form_input_value_by_index(1)
        reinsert_flag   =   self.set_index_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import reset_df_index     
        opstat  =   reset_df_index(self.dftitle,drop_columns,index_levels,reinsert_flag)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "df index reset was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            self.parent.display_transform_dataframe_index()        

    def return_from_reset_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][return_from_reset_df_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_INDEX_MAIN)

    def help_for_reset_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_reset_index_Widget][help_for_reset_df_index]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_RESET_INDEX
        display_url(TRANSFORM_DF_RESET_INDEX)

class DataTransform_transform_dataframe_append_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_append_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_append_index_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,10,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nDouble click on column to be appened to index column\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")


        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_append_index_transform_input_id,DTDM.df_append_index_transform_input_idList,DTDM.df_append_index_transform_input_labelList,
                             DTDM.df_append_index_transform_input_typeList,DTDM.df_append_index_transform_input_placeholderList,DTDM.df_append_index_transform_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.append_df_index,self.return_from_append_df_index,self.help_for_append_df_index]
        cfg_parms       =   None
        form_title      =   "Append df Index"
        form_width      =   550

        selectDicts     =   []

        dropsel         =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(dropsel)
        
        verifysel           =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(verifysel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.append_index_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.append_index_Layout     =   QVBoxLayout()
        self.append_index_Layout.addWidget(self.cols_table)
        self.append_index_Layout.addWidget(note_label)
        self.append_index_Layout.addWidget(self.append_index_form)
        self.append_index_Layout.addStretch()

        self.setLayout(self.append_index_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATAFRAME) :    
            print("  [DataTransform_transform_append_index_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell

        index_columns   =   self.append_index_form.get_form_input_value_by_index(0)
        if(len(index_columns) == 0) :

            index_list  =   "[" + cell + "]"
            self.append_index_form.set_form_input_value_by_index(0,index_list)  

        else :  

            index_list  =   index_columns.replace("]",",")
            index_list  =   index_list + cell + "]"
            self.append_index_form.set_form_input_value_by_index(0,index_list)

    
    def append_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][append_df_index]")
        
        append_columns  =   self.set_index_form.get_form_input_value_by_index(0)
        drop_flag       =   self.set_index_form.get_form_input_value_by_index(1)
        reinsert_flag   =   self.set_index_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import append_to_df_index     
        opstat  =   append_to_df_index(self.dftitle,append_columns,drop_flag,reinsert_flag)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "df index appended to successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            self.parent.display_transform_dataframe_index()        

    def return_from_append_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][return_from_append_df_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_INDEX_MAIN)

    def help_for_append_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_append_index_Widget][help_for_append_df_index]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_APPEND_INDEX
        display_url(TRANSFORM_DF_APPEND_INDEX)

class DataTransform_transform_dataframe_sort_index_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_sort_index_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_sort_index_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][init_form]")

        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.df_sort_index_transform_input_id,DTDM.df_sort_index_transform_input_idList,DTDM.df_sort_index_transform_input_labelList,
                             DTDM.df_sort_index_transform_input_typeList,DTDM.df_sort_index_transform_input_placeholderList,DTDM.df_sort_index_transform_input_reqList]
        comboMethods    =   [None,None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.sort_df_index,self.return_from_sort_df_index,self.help_for_sort_df_index]
        cfg_parms       =   None
        form_title      =   "\nSort df Index"
        form_width      =   550

        selectDicts     =   []

        ascsel          =   {"default" : "True", "list" : ["True","False"]}
        selectDicts.append(ascsel)
        methodsel       =   {"default":"quicksort","list":["quicksort","mergesort","heapsort"]}
        selectDicts.append(methodsel)
        nasel           =   {"default":"last","list":["first","last"]}
        selectDicts.append(nasel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.sort_index_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.sort_index_Layout     =   QVBoxLayout()
        self.sort_index_Layout.addWidget(self.sort_index_form)
        self.sort_index_Layout.addStretch()

        self.setLayout(self.sort_index_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][init_form] end")

    def sort_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][sort_df_index]")
        
        ascending_flag  =   self.set_index_form.get_form_input_value_by_index(0)
        sort_kind       =   self.set_index_form.get_form_input_value_by_index(1)
        na_position     =   self.set_index_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import sort_df_index     
        opstat  =   sort_df_index(self.dftitle,ascending_flag,sort_kind,na_position)

        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "df index sort was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            self.parent.display_transform_dataframe_index()        


    def return_from_sort_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][return_from_sort_df_index]")

        self.parent.display_transform_dataframe_index(DTDM.DF_INDEX_MAIN)

    def help_for_sort_df_index(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_index_Widget][help_for_sort_df_index]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_SORT_INDEX
        display_url(TRANSFORM_DF_SORT_INDEX)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              Transfoprm Dataframe index Widgets end           -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -              Transfoprm Dataframe sort df widgets             -#
# -----------------------------------------------------------------#

class DataTransform_transform_dataframe_sort_df_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("\n[DataTransform_transform_sort_df_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("[DataTransform_transform_sort_df_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,10,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nDouble click on column to select column\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")



        import dfcleanser.Qt.data_transform.DataTransformDataframeModel as DTDM

        form_parms      =   [DTDM.sort_df_column_input_id,DTDM.sort_df_column_input_idList,DTDM.sort_df_column_input_labelList,
                             DTDM.sort_df_column_input_typeList,DTDM.sort_df_column_input_placeholderList,DTDM.sort_df_column_input_reqList]
        comboMethods    =   [None,None,None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.sort_df,self.return_from_sort_df,self.help_for_sort_df]
        cfg_parms       =   None
        form_title      =   "Sort df by Column"
        form_width      =   550

        selectDicts     =   []

        ordersel        =   {"default" : "True","list" : ["True","False"]}
        selectDicts.append(ordersel)
        
        kindsel         =   {"default" : "quicksort","list" : ["quicksort","mergesort","heapsort"]}
        selectDicts.append(kindsel)
        
        napossel        =   {"default" : "last","list" : ["first","last"]}
        selectDicts.append(napossel)
        
        resetsel        =   {"default" : "False","list" : ["True","False"]}
        selectDicts.append(resetsel)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.sort_df_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.sort_df_Layout     =   QVBoxLayout()
        self.sort_df_Layout.addWidget(self.cols_table)
        self.sort_df_Layout.addWidget(note_label)
        self.sort_df_Layout.addWidget(self.sort_df_form)
        self.sort_df_Layout.addStretch()

        self.setLayout(self.sort_df_Layout)

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATAFRAME) :    
            print("  [DataTransform_transform_sort_df_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell

        self.sort_df_form.set_form_input_value_by_index(0,cell)

    
    def sort_df(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][sort_df]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()
        
        sort_column     =   self.sort_df_form.get_form_input_value_by_index(0)
        ascending_flag  =   self.sort_df_form.get_form_input_value_by_index(1)
        sort_kind       =   self.sort_df_form.get_form_input_value_by_index(2)
        na_position     =   self.sort_df_form.get_form_input_value_by_index(3)
        reset_flag      =   self.sort_df_form.get_form_input_value_by_index(4)  

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import sort_df_column     
        opstat  =   sort_df_column(self.dftitle,sort_column,ascending_flag,sort_kind,na_position,reset_flag)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "df sort by column was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            self.parent.display_transform_dataframes()        

    def return_from_sort_df(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][return_from_sort_df]")

        self.parent.display_transform_dataframes()

    def help_for_sort_df(self) :

        if(DEBUG_TRANSFORM_DATAFRAME) :
            print("  [DataTransform_transform_sort_df_Widget][help_for_sort_df]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DF_SORT_BY_COL_ID
        display_url(TRANSFORM_DF_SORT_BY_COL_ID)

# -----------------------------------------------------------------#
# -            Transfoprm Dataframe sort df widgets end           -#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Transfoprm datetime Widgets                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataTransform_transform_datetime_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("\n[DataTransform_transform_datetime_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_datetime_Widget] end")

    def reload_banner(self) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][reload_data] ")

        self.init_command_bar()

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][init_form]")

        self.init_command_bar()

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_transform")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        self.dfc_dfs_layout =   dfc_dfs_layout

        from PyQt5.QtWidgets import QVBoxLayout
        self.transform_col_Layout     =   QVBoxLayout()
        self.transform_col_Layout.addLayout(self.dfc_dfs_layout)
        self.transform_col_Layout.addStretch()

        self.setLayout(self.transform_col_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][init_form] end")

    def init_command_bar(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][init_command_bar]")

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.datetime_button        =   QPushButton()   
        self.timedelta_button       =   QPushButton()    
        self.calc_td_button         =   QPushButton()   
        self.merge_button           =   QPushButton()
        self.comp_button            =   QPushButton()
        self.return_button          =   QPushButton()   
        self.help_button            =   QPushButton()   

        button_bar1_button_list     =   [self.datetime_button,self.timedelta_button,self.calc_td_button,self.merge_button,self.comp_button,self.return_button,self.help_button] 
        button_bar1_text_list       =   ["Convert Column\nto datetime","Convert Column\nto timedelta","Calculate\n timedelta",
                                         "Merge Column\nfrom date,time","Get datetime \nComponents","Return","Help"]
        button_bar1_size_list       =   [143,75]
        button_bar1_tool_tip_list   =   ["Convert to datetime","Convert to timedelta","Calculate timedelta","Merge datetime","datetime Components","Return","Help"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.convert_to_datetime,self.convert_to_timedelta,self.calculate_timedelta,
                                         self.merge_datetime,self.datetime_components,self.return_from_transform_datetime,self.help_for_transform_datetime]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataTransformCmdbarLayout)
        self.parent.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][init_command_bar] end")


    def convert_to_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][convert_to_datetime]")

        self.parent.display_transform_datetime(DTDM.DATETIME_CONVERT)

    def convert_to_timedelta(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][convert_to_timedelta]")

        self.parent.display_transform_datetime(DTDM.DATETIME_CONVERT_TIMEDELTA)

    def calculate_timedelta(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][calculate_timedelta]")

        self.parent.display_transform_datetime(DTDM.DATETIME_CALCULATE_TIMEDELTA)

    """
    def split_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][split_datetime]")

        self.parent.display_transform_datetime(DTDM.DATETIME_SPLIT)
    """

    def merge_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][merge_datetime]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MERGE)

    def datetime_components(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][datetime_components]")
        
        self.parent.display_transform_datetime(DTDM.DATETIME_COMPONENTS)

    def return_from_transform_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][return_from_transform_datetime]")

        self.parent.init_stacked_index()

    def help_for_transform_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_Widget][help_for_transform_datetime]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_TASKBAR_ID
        display_url(TRANSFORM_DATETIME_TASKBAR_ID)


class DataTransform_transform_datatime_convert_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_datatime_convert_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_format_input_id,DTDM.datetime_format_input_idList,DTDM.datetime_format_input_labelList,
                             DTDM.datetime_format_input_typeList,DTDM.datetime_format_input_placeholderList,DTDM.datetime_format_input_reqList]
        comboMethods    =   [None,self.select_format_string]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.datetime_format,self.datetime_time_format,self.return_from_datetime_format,self.help_for_datetime_format]
        cfg_parms       =   None
        form_title      =   "\nConvert Column to datetime"
        form_width      =   550

        selectDicts     =   []

        errorssel         =   {"default":DTDM.error_handlers_text[1],"list":DTDM.error_handlers_text}
        selectDicts.append(errorssel)
    
        from dfcleanser.sw_utilities.DFCDataStores import get_Dict
        strftimedict = get_Dict("strftime")
            
        strftimekeys    =   list(strftimedict.keys())
        strftimelist    =   []
        for i in range(len(strftimekeys)) :
            strftimelist.append(strftimekeys[i] + " : " + strftimedict.get(strftimekeys[i]))    
    
        strftimesel     =   {"default":strftimelist[0],"list": strftimelist}
        selectDicts.append(strftimesel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.convert_form     =   dfcleanser_input_form_Widget(form_parms)

        from PyQt5.QtWidgets import QVBoxLayout
        self.convert_Layout     =   QVBoxLayout()
        
        self.convert_Layout.addWidget(self.cols_table)
        self.convert_Layout.addWidget(self.convert_form)
        self.convert_Layout.addStretch()

        self.setLayout(self.convert_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_datatime_convert_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell
        self.convert_form.set_form_input_value_by_index(0,cell) 


    def select_format_string(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][select_format_string]")
    
    def datetime_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][datetime_format]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        convert_column      =   self.convert_form.get_form_input_value_by_index(0)
        threshold           =   self.convert_form.get_form_input_value_by_index(1)
        error_method        =   self.convert_form.get_form_input_value_by_index(2)
        format_string       =   self.convert_form.get_form_input_value_by_index(3)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_datetime_datatype_transform
        opstat  =   process_datetime_datatype_transform(self.dftitle,convert_column,threshold,error_method,format_string)

        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "datetime conversion was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        
    
    def datetime_time_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][datetime_time_format]")
        
        from dfcleanser.common.common_utils import opStatus, is_numeric_col
        opstat = opStatus()
        
        convert_column      =   self.convert_form.get_form_input_value_by_index(0)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(self.dftitle)

        if(is_numeric_col(df,convert_column)) :
           
            self.parent.display_transform_datetime(DTDM.DATETIME_TIME_CONVERT,convert_column)

        else :

            threshold           =   self.convert_form.get_form_input_value_by_index(1)
            error_method        =   self.convert_form.get_form_input_value_by_index(2)
            format_string       =   self.convert_form.get_form_input_value_by_index(3)

            from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_datetime_datatype_transform
            opstat  =   process_datetime_datatype_transform(self.dftitle,convert_column,threshold,error_method,format_string)

            if(opstat.get_status()) :
        
                title       =   "dfcleanser status"       
                status_msg  =   "datetime conversion was successful "
                from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                display_status_msg(title,status_msg) 

                from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
                self.parent.display_transform_datetime(DATETIME_MAIN)        


    def return_from_datetime_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][return_from_datetime_format]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_datetime_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][help_for_datetime_format]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_FORMAT_ID
        display_url(TRANSFORM_DATETIME_FORMAT_ID)


class DataTransform_transform_datatime_time_convert_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]    

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget] dftitle ; ",self.dftitle, self.colname)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_datatime_time_convert_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_time_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_time_format_input_id,DTDM.datetime_time_format_input_idList,DTDM.datetime_time_format_input_labelList,
                             DTDM.datetime_time_format_input_typeList,DTDM.datetime_time_format_input_placeholderList,DTDM.datetime_time_format_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.datetime_time_format,self.return_from_datetime_time_format,self.help_for_datetime_time_format]
        cfg_parms       =   None
        form_title      =   "\nConvert Column to datetime.time"
        form_width      =   550

        selectDicts     =   []

        errorssel         =   {"default":DTDM.error_handlers_text[1],"list":DTDM.error_handlers_text}
        selectDicts.append(errorssel)
    
        sel_type_units  =   {"default":"INCREMENTS_IN_SECONDS","list":["INCREMENTS_IN_SECONDS","INCREMENTS_IN_MINUTES","INCREMENTS_IN_HOURS"]}
        selectDicts.append(sel_type_units)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.convert_form     =   dfcleanser_input_form_Widget(form_parms)

        self.convert_form.set_form_input_value_by_index(0,self.colname)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][init_form] form built")


        from PyQt5.QtWidgets import QVBoxLayout
        self.convert_Layout     =   QVBoxLayout()
        
        self.convert_Layout.addWidget(self.cols_table)
        self.convert_Layout.addWidget(self.convert_form)
        self.convert_Layout.addStretch()

        self.setLayout(self.convert_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][init_form] end")

    def select_time_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_time_convert_Widget][select_time_column]")

        return()
    
    def datetime_time_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][datetime_format]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        convert_column      =   self.convert_form.get_form_input_value_by_index(0)
        threshold           =   self.convert_form.get_form_input_value_by_index(1)
        error_method        =   self.convert_form.get_form_input_value_by_index(2)
        units               =   int(self.convert_form.get_form_input_value_by_index(3))
        units_type          =   self.convert_form.get_form_input_value_by_index(4)
        
        
        try :

            from dfcleanser.Qt.data_cleansing.Userfns import build_time_component
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(self.dftitle)

            df[convert_column]  =   df[convert_column].apply(build_time_component, time_incr=units, time_unit=units_type)

        except Exception as e:

            opstat.set_status(False)
                    
            title       =   "dfcleanser exception"       
            status_msg  =   "[display_transform_columns] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


        if(opstat.get_status()) :

            title       =   "dfcleanser status"       
            status_msg  =   "datetime conversion was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

        return(opstat.get_status())


    def return_from_datetime_time_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][return_from_datetime_format]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_datetime_time_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datatime_convert_Widget][help_for_datetime_format]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_FORMAT_ID
        display_url(TRANSFORM_DATETIME_FORMAT_ID)



class DataTransform_transform_calculate_timedelta_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.select_option  =   "select for datetime_column_name1"
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_calculate_timedelta_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_tdelta_input_id,DTDM.datetime_tdelta_input_idList,DTDM.datetime_tdelta_input_labelList,
                             DTDM.datetime_tdelta_input_typeList,DTDM.datetime_tdelta_input_placeholderList,DTDM.datetime_tdelta_input_reqList]
        comboMethods    =   [self.select_column_to_name,None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.calculate_timedelta,self.return_from_calculate_timedelta,self.help_for_calculate_timedelta]
        cfg_parms       =   None
        form_title      =   "\nCslculoate timedelta for dateime Columns"
        form_width      =   550

        selectDicts     =   []

        colsel         =   {"default":"select for datetime_column_name1","list":["select for datetime_column_name1","select for datetime_column_name2"]}
        selectDicts.append(colsel)

        tdeltasel         =   {"default":"timedelta","list":["timedelta","float64"], "callback":"change_convert_dtype_callback"}
        selectDicts.append(tdeltasel)
        
        dtsel           =   {"default":"Seconds","list":["Days","Hours","Minutes","Seconds","MilliSeconds","MicroSeconds"], "callback":"change_convert_units_callback"}
        selectDicts.append(dtsel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.calculate_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.calculate_Layout     =   QVBoxLayout()
        self.calculate_Layout.addWidget(self.cols_table)
        self.calculate_Layout.addWidget(self.calculate_form)
        self.calculate_Layout.addStretch()

        self.setLayout(self.calculate_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_calculate_timedelta_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell

        if(self.select_option == "select for datetime_column_name1") :
            self.calculate_form.set_form_input_value_by_index(0,cell) 
        else :
            self.calculate_form.set_form_input_value_by_index(1,cell) 

    def select_column_to_name(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][select_column_to_name]")
        
        self.select_option  =   self.calculate_form.get_form_input_value_by_index(2) 

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][select_column_to_name]",self.select_option)
 
    def calculate_timedelta(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][calculate_timedelta]")

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        column1         =   self.calculate_form.get_form_input_value_by_index(0)
        column2         =   self.calculate_form.get_form_input_value_by_index(1)
        new_column      =   self.calculate_form.get_form_input_value_by_index(2)
        new_datatype    =   self.calculate_form.get_form_input_value_by_index(3)
        new_units       =   self.calculate_form.get_form_input_value_by_index(4)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_calculate_timedelta_transform
        opstat  =   process_calculate_timedelta_transform(self.dftitle,column1,column2,new_column,new_datatype,new_units)  

        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "timedelta conversion was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        
        
    def return_from_calculate_timedelta(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][return_from_calculate_timedelta]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_calculate_timedelta(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_calculate_timedelta_Widget][help_for_calculate_timedelta]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_DELTA_ID
        display_url(TRANSFORM_DATETIME_DELTA_ID)

class DataTransform_transform_timedelta_convert_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_dtimedelta_convert_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.timedelta_format_input_id,DTDM.timedelta_format_input_idList,DTDM.timedelta_format_input_labelList,
                             DTDM.timedelta_format_input_typeList,DTDM.timedelta_format_input_placeholderList,DTDM.timedelta_format_input_reqList]
        comboMethods    =   [None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.timedelta_format,self.return_from_timedelta_format,self.help_for_timedelta_format]
        cfg_parms       =   None
        form_title      =   "\nConvert Column to timedelta"
        form_width      =   550

        selectDicts     =   []

        unitsel           =   {"default":"seconds","list":DTDM.timedelta_units}
        selectDicts.append(unitsel)

        errorssel         =   {"default":DTDM.error_handlers_text[1],"list":DTDM.error_handlers_text}
        selectDicts.append(errorssel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.convert_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.convert_Layout     =   QVBoxLayout()
        self.convert_Layout.addWidget(self.cols_table)
        self.convert_Layout.addWidget(self.convert_form)
        self.convert_Layout.addStretch()

        self.setLayout(self.convert_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_timedelta_convert_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell
        self.convert_form.set_form_input_value_by_index(0,cell) 
    
    def timedelta_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][timedelta_format]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        convert_column      =   self.convert_form.get_form_input_value_by_index(0)
        threshold           =   self.convert_form.get_form_input_value_by_index(1)
        units               =   self.convert_form.get_form_input_value_by_index(2)
        error_method        =   self.convert_form.get_form_input_value_by_index(3)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_timedelta_datatype_transform
        opstat  =   process_timedelta_datatype_transform(self.dftitle,convert_column,threshold,units,error_method)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "timedelta calculation was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        

    def return_from_timedelta_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][return_from_timedelta_format]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_timedelta_format(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_timedelta_convert_Widget][help_for_timedelta_format]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_DELTA_COL_ID
        display_url(TRANSFORM_DATETIME_DELTA_COL_ID)

class DataTransform_transform_split_datetime_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_split_datetime_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_split_input_id,DTDM.datetime_split_input_idList,DTDM.datetime_split_input_labelList,
                             DTDM.datetime_split_input_typeList,DTDM.datetime_split_input_placeholderList,DTDM.datetime_split_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.datetime_split,self.return_from_datetime_split,self.help_for_datetime_split]
        cfg_parms       =   None
        form_title      =   "\nSplit Column to date,time Columns"
        form_width      =   550
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.split_form     =   dfcleanser_input_form_Widget(form_parms)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][form built]")
        
        from PyQt5.QtWidgets import QVBoxLayout
        self.split_Layout     =   QVBoxLayout()
        self.split_Layout.addWidget(self.cols_table)
        self.split_Layout.addWidget(self.split_form)
        self.split_Layout.addStretch()

        self.setLayout(self.split_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_split_datetime_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell
        self.split_form.set_form_input_value_by_index(0,cell) 
   
    def datetime_split(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][datetime_split]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        column1      =   self.split_form.get_form_input_value_by_index(0)
        column2      =   self.split_form.get_form_input_value_by_index(1)
        column3      =   self.split_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_datetime_merge_split_transform
        from dfcleanser.Qt.data_transform.DataTransformDataframeModel import SPLIT        
        opstat  =   process_datetime_merge_split_transform(self.dftitle,SPLIT,column1,column2,column3)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "datetime split was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        

    def return_from_datetime_split(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][return_from_datetime_split]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_datetime_split(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_split_datetime_Widget][help_for_datetime_split]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_SPLIT_ID
        display_url(TRANSFORM_DATETIME_SPLIT_ID)


class DataTransform_transform_merge_datetime_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.select_option  =   "select for date_column_name"
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_merge_datetime_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_merge_input_id,DTDM.datetime_merge_input_idList,DTDM.datetime_merge_input_labelList,
                             DTDM.datetime_merge_input_typeList,DTDM.datetime_merge_input_placeholderList,DTDM.datetime_merge_input_reqList]
        comboMethods    =   [self.select_column_to_name,None,None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.merge_datetime,self.return_from_merge_datetime,self.help_for_merge_datetime]
        cfg_parms       =   None
        form_title      =   "\nMerge datetime Column from date,time Columns"
        form_width      =   550

        selectDicts     =   []

        colsel         =   {"default":"select for date_column_name","list":["select for date_column_name","select for time_column_name"]}
        selectDicts.append(colsel)

        ctypes          =   {"default":"datetime.datetime","list": ["datetime.datetime","np.datetime64","pd.Timestamp"]}
        selectDicts.append(ctypes)

        errorssel         =   {"default":DTDM.error_handlers_text[1],"list":DTDM.error_handlers_text}
        selectDicts.append(errorssel)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.merge_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.merge_Layout     =   QVBoxLayout()
        self.merge_Layout.addWidget(self.cols_table)
        self.merge_Layout.addWidget(self.merge_form)
        self.merge_Layout.addStretch()

        self.setLayout(self.merge_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_merge_datetime_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell

        if(self.select_option == "select for date_column_name") : 
            self.merge_form.set_form_input_value_by_index(0,cell)  
        else :
            self.merge_form.set_form_input_value_by_index(1,cell) 
    
    def select_column_to_name(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][select_column_to_name]")
        
        self.select_option  =   self.merge_form.get_form_input_value_by_index(2) 
 
    def merge_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][merge_datetime]")
        
        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        column1      =   self.merge_form.get_form_input_value_by_index(0)
        column2      =   self.merge_form.get_form_input_value_by_index(1)
        column3      =   self.merge_form.get_form_input_value_by_index(3)
        datatype     =   self.merge_form.get_form_input_value_by_index(4)
        threshold    =   self.merge_form.get_form_input_value_by_index(5)
        errorhdlr    =   self.merge_form.get_form_input_value_by_index(6)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_datetime_merge_split_transform
        from dfcleanser.Qt.data_transform.DataTransformDataframeModel import MERGE        
        opstat  =   process_datetime_merge_split_transform(self.dftitle,MERGE,column1,column2,column3,threshold,errorhdlr,datatype)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "datetime merge was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        

    def return_from_merge_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][return_from_merge_datetime]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_merge_datetime(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_merge_datetime_Widget][help_for_merge_datetime]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_MERGE_ID
        display_url(TRANSFORM_DATETIME_MERGE_ID)


class DataTransform_transform_datetime_components_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("\n[DataTransform_transform_datetime_components_Widget][init] ")

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget] dftitle ; ",self.dftitle)

        self.init_form()

        if(DEBUG_TRANSFORM_DATETIME) :
            print("[DataTransform_transform_datetime_components_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][reload_data] ")
        
        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][init_form]")

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms               =   [self.dftitle,8,self.select_column]
        self.cols_table     =   DataInspectionColumnsStatsTable(parms) 

        form_parms      =   [DTDM.datetime_comp_input_id,DTDM.datetime_comp_input_idList,DTDM.datetime_comp_input_labelList,
                             DTDM.datetime_comp_input_typeList,DTDM.datetime_comp_input_placeholderList,DTDM.datetime_comp_input_reqList]
        comboMethods    =   [None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.get_datetime_components,self.return_from_datetime_components,self.help_for_datetime_components]
        cfg_parms       =   None
        form_title      =   "\nGet datetime Component"
        form_width      =   550

        selectDicts     =   []

        comps           =   {"default":DTDM.dtcomps[0],"list":DTDM.dtcomps}
        selectDicts.append(comps)
        
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.comps_form     =   dfcleanser_input_form_Widget(form_parms)

        
        from PyQt5.QtWidgets import QVBoxLayout
        self.comps_Layout     =   QVBoxLayout()
        self.comps_Layout.addWidget(self.cols_table)
        self.comps_Layout.addWidget(self.comps_form)
        self.comps_Layout.addStretch()

        self.setLayout(self.comps_Layout)

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][init_form] end")

    def select_column(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][select_column]")

        row_number      =   None
        column_number   =   None

        for idx in self.cols_table.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][select_column] ",row_number,column_number)

        model   =   self.cols_table.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(DEBUG_TRANSFORM_DATETIME) :    
            print("  [DataTransform_transform_datetime_components_Widget][select_column] : colname [",cell,"]")

        self.colname    =   cell
        self.comps_form.set_form_input_value_by_index(0,cell) 

    def get_datetime_components(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][get_datetime_components]")

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        column1      =   self.comps_form.get_form_input_value_by_index(0)
        column2      =   self.comps_form.get_form_input_value_by_index(1)
        comptype     =   self.comps_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformDataframeControl import process_get_datetime_component
        opstat  =   process_get_datetime_component(self.dftitle,column1,column2,comptype)
        
        if(opstat.get_status()) :
        
            title       =   "dfcleanser status"       
            status_msg  =   "datetime componnts retrieved was successful "
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg) 

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

            from dfcleanser.Qt.data_transform.DataTransformDataframeModel import DATETIME_MAIN
            self.parent.display_transform_datetime(DATETIME_MAIN)        

    def return_from_datetime_components(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][return_from_datetime_components]")

        self.parent.display_transform_datetime(DTDM.DATETIME_MAIN)

    def help_for_datetime_components(self) :

        if(DEBUG_TRANSFORM_DATETIME) :
            print("  [DataTransform_transform_datetime_components_Widget][help_for_datetime_components]")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_DATETIME_COMP_ID
        display_url(TRANSFORM_DATETIME_COMP_ID)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Transfoprm datetime Widgets end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#




























